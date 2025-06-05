# jumpstarter/packages/jumpstarter-testing/conftest.py

```python
import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def anyio_backend():
    return "asyncio"

```