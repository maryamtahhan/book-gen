# AI Book Generator for Any GitHub or Local Python Repository

import os
import base64
import requests
import argparse
from pathlib import Path
from dotenv import load_dotenv
from github import Github
from tqdm import tqdm
import re
import natsort

parser = argparse.ArgumentParser(description="Generate a technical book from a Python repo using a local LLM.")
parser.add_argument("--repo", help="GitHub repo in the form 'owner/repo' or full URL (if using GitHub)")
parser.add_argument("--path", help="Local path to a Python project (if using local files)")
parser.add_argument("--source", help="Path within the repo or local directory to start parsing from")
parser.add_argument("--clean", action="store_true", help="Remove intermediate chapter files after generating the book or clean without processing if used alone")
args = parser.parse_args()

BOOK_DIR = "book"
EXPLAINED_DIR = "book/explained"
OLLAMA_MODEL = "mistral"
OLLAMA_URL = "http://localhost:11434/api/generate"

load_dotenv()
Path(BOOK_DIR).mkdir(exist_ok=True)
Path(EXPLAINED_DIR).mkdir(exist_ok=True)

# Cleanup only and exit if --clean is passed alone
if args.clean and not (args.repo or args.path or args.source):
    for f in Path(BOOK_DIR).glob("chapter_*.md"):
        f.unlink()
    for f in Path(EXPLAINED_DIR).glob("*.md"):
        f.unlink()
    print("🧹 Cleaned intermediate chapter files.")
    exit(0)

REPO_NAME = args.repo
LOCAL_PATH = args.path
SOURCE_SUBPATH = args.source

if REPO_NAME:
    if REPO_NAME.startswith("https://github.com"):
        REPO_NAME = REPO_NAME.removeprefix("https://github.com/").removesuffix(".git")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    g = Github(GITHUB_TOKEN) if GITHUB_TOKEN else Github()
    repo = g.get_repo(REPO_NAME)
else:
    repo = None

if not SOURCE_SUBPATH:
    SOURCE_SUBPATH = "python" if repo else LOCAL_PATH

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def download_and_markdownify(filepath, save_as):
    if repo:
        contents = repo.get_contents(filepath)
        if contents.encoding == "base64":
            code = base64.b64decode(contents.content).decode("utf-8")
        else:
            code = contents.decoded_content.decode("utf-8")
    else:
        with open(filepath, "r") as f:
            code = f.read()

    markdown_output = f"# {filepath}\n\n```python\n{code}\n```"
    Path(f"{BOOK_DIR}/{save_as}").write_text(markdown_output)
    return code

def get_summary_and_diagram(file_list):
    prompt = f"""
You are generating a high-level project overview for a technical book. Given the following list of files:
{file_list}

1. Describe the overall architecture and purpose of the project.
2. Group files by functionality.
3. Provide a high-level explanation of how components interact.
4. If possible, generate a `mermaid` diagram of key components or data flow.
"""
    response = requests.post(OLLAMA_URL, json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False})
    return response.json().get("response", "(No response from model)") if response.status_code == 200 else "(Failed to summarize)"

def get_explanation(code, filename):
    explanation_prompt = f"""
You are writing a chapter for a technical book based on the project.
Explain the purpose and functionality of the file `{filename}` in clear, professional English.
Include:
- A brief overview of the file
- Descriptions of any important functions or classes
- Where this code fits in the project
- Example use cases if applicable
"""
    diagram_prompt = f"""
Now, based on the same file `{filename}`, generate a `mermaid` sequence diagram if applicable that visualizes how the key functions interact.
Wrap the diagram in a fenced code block like this:
```mermaid
...diagram here...
```
"""
    explanation = requests.post(OLLAMA_URL, json={"model": OLLAMA_MODEL, "prompt": explanation_prompt + code, "stream": False})
    diagram = requests.post(OLLAMA_URL, json={"model": OLLAMA_MODEL, "prompt": diagram_prompt + code, "stream": False})

    if explanation.status_code == 200 and diagram.status_code == 200:
        explanation_text = explanation.json().get("response", "(No response from model)")
        diagram_text = diagram.json().get("response", "")
        return explanation_text + "\n\n" + diagram_text
    return "(Failed to get response from local model)"

def get_python_files(path):
    files = []
    if repo:
        stack = [path]
        while stack:
            current_path = stack.pop()
            contents = repo.get_contents(current_path)
            for content_file in contents:
                if content_file.type == "dir":
                    stack.append(content_file.path)
                elif content_file.name.endswith(".py"):
                    files.append(content_file.path)
    else:
        p = Path(path)
        files = [str(f) for f in p.rglob("*.py")]
    return natsort.natsorted(files)

# === PROCESS FILES ===
python_files = get_python_files(SOURCE_SUBPATH)
all_chapters = []

# Add high-level project overview as Chapter 0
overview = get_summary_and_diagram("\n".join(python_files))
project_intro = f"# Chapter 0: Project Overview\n\n{overview}"
all_chapters.append(project_intro)

for i, file in enumerate(tqdm(python_files, desc="Generating Book")):
    chapter_base = f"chapter_{i+1:02d}_{Path(file).stem}"
    code = download_and_markdownify(file, chapter_base + ".md")
    explained = get_explanation(code, file)
    chapter_content = f"## Chapter {i+1}: {file}\n\n" + explained
    chapter_path = Path(f"{EXPLAINED_DIR}/{chapter_base}.md")
    chapter_path.write_text(chapter_content)
    all_chapters.append(chapter_content)

book_combined = "\n\n".join(all_chapters)
Path(f"{BOOK_DIR}/book.md").write_text(book_combined)

# Extract TOC from headings in book
toc_entries = []
for line in book_combined.splitlines():
    if line.startswith("## Chapter") or line.startswith("# Chapter"):
        title = line.lstrip("# ").strip()
        anchor = slugify(title)
        toc_entries.append(f"- [{title}](#{anchor})")

Path(f"{BOOK_DIR}/TOC.md").write_text("# Table of Contents\n\n" + "\n".join(toc_entries))

if args.clean:
    for f in Path(BOOK_DIR).glob("chapter_*.md"):
        f.unlink()
    for f in Path(EXPLAINED_DIR).glob("*.md"):
        f.unlink()

print("✅ All chapters, explanations, and visuals generated. Combined book and TOC ready.")