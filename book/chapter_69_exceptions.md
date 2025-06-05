# jumpstarter/packages/jumpstarter-driver-corellium/jumpstarter_driver_corellium/corellium/exceptions.py

```python
"""
Corellium API client exceptions module
"""
from jumpstarter.common.exceptions import JumpstarterException


class CorelliumApiException(JumpstarterException):
    """
    Exception raised when something goes wrong with Corellium's API.
    """

```