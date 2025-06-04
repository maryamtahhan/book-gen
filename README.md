# Technical Book Generator (Python Projects)

This tool automatically generates a technical book-style explanation of a
**Python-based GitHub codebase** using a local LLM (Mistral via Ollama)
on macOS.

---

## Features

- Clones or reads from any Python-based GitHub repo or local path
- Converts each `.py` file into a Markdown chapter
- Uses a local AI model (Mistral) via Ollama to generate human-readable explanations
- Adds Mermaid diagrams and project overviews
- Outputs a clean, combined `book.md` and TOC

---

## Installation Instructions (macOS)

### 1. Clone this repo and set up the environment

```bash
git clone https://github.com/maryamtahhan/book-gen.git
cd book-gen
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Install Ollama (for Apple Silicon / M-series chips)

```bash
brew install ollama
```

Or install the app from: [https://ollama.com](https://ollama.com)

### 3. Start the Ollama server

#### Option A (one-time terminal run):

```bash
ollama serve
```

Leave this terminal running.

#### Option B (run in background always):

```bash
brew services start ollama
```

### 4. Download and start the Mistral model

```bash
ollama run mistral
```

This will download the model on first run (~4–6 GB) and then start a local inference session.

---

## Optional: GitHub Token

To avoid rate limits with the GitHub API, you can create a fine-grained personal access token and store it in a `.env` file:

```
GITHUB_TOKEN=ghp_YourActualTokenHere
```

---

## Run the Generator

```bash
❯  python main.py --repo https://github.com/triton-lang/triton.git
```

This will:
- Save source code files in `book/`
- Save AI-written prose chapters in `book/explained/`

---

## Output Structure

```
book/
├── chapter_01_runtime.md
├── ...
└── explained/
    ├── chapter_01_runtime.md
    └── ...
```

