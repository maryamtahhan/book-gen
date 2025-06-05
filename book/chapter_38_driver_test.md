# jumpstarter/packages/jumpstarter-cli-driver/jumpstarter_cli_driver/driver_test.py

```python
from click.testing import CliRunner

from . import driver


def test_list_drivers():
    runner = CliRunner()

    result = runner.invoke(
        driver,
        ["list"],
    )
    assert result.exit_code == 0

```