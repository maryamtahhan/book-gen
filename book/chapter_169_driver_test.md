# jumpstarter/packages/jumpstarter-driver-yepkit/jumpstarter_driver_yepkit/driver_test.py

```python
from .driver import Ykush
from jumpstarter.common.utils import serve


def test_drivers_yepkit():
    instance = Ykush()

    with serve(instance) as client:
        client.on()
        client.off()

```