## Chapter 133: jumpstarter/packages/jumpstarter-driver-raspberrypi/jumpstarter_driver_raspberrypi/driver.py

 The file `jumpstarter/packages/jumpstarter-driver-raspberrypi/jumpstarter_driver_raspberrypi/driver.py` is a Python module that contains classes for interacting with the digital input and output pins of a Raspberry Pi board within the JumpStarter project, which appears to be a modular system designed for IoT applications.

   The two primary classes in this file are `DigitalOutput` and `DigitalInput`, both inheriting from the base class `Driver`. These classes represent digital output and input devices respectively. They each have an associated pin number that controls the GPIO on the Raspberry Pi, as well as an instance of the corresponding GPIOZero device (either `DigitalOutputDevice` or `DigitalInputDevice`).

   Here are brief descriptions of important functions and class attributes:

   - The `pin` attribute specifies the number or label of the GPIO pin that the device is connected to. It can be either an integer or a string representing the pin's label (e.g., "17" or "GPIO17").

   - The `device` attribute is initialized as an instance of the appropriate GPIOZero device (`DigitalInputDevice` for `DigitalInput` and `DigitalOutputDevice` for `DigitalOutput`) upon instantiation, with its pin number set to that of the associated pin.

   - Both classes have a `client()` class method that returns the name of their respective client classes within the jumpstarter_driver_raspberrypi package. This is likely used for dependency injection or service discovery.

   - The `__post_init__` method is a Python special method that is called immediately after the instance's __init__() method. It initializes the device instances and checks if they have the correct type based on their class.

   - The `close()` method releases resources associated with the GPIO devices, such as closing the connection to the Raspberry Pi.

   - The `off()` method sets the output pin to a low (0V) state for the `DigitalOutput` class.

   - The `on()` method sets the output pin to a high (3.3V or 5V) state for the `DigitalOutput` class.

   - For the `DigitalInput` class, there are two exported methods: `wait_for_active()` and `wait_for_inactive()`, which allow the user to wait for an active (high) or inactive (low) state on the input pin respectively. These functions take a timeout parameter, allowing users to specify how long they want to wait before raising a TimeoutError if no change is detected.

   This code fits within the project by providing a way to interface with the Raspberry Pi's GPIO pins using a simple and consistent API, which aligns with the JumpStarter's modular design philosophy. This allows developers to easily integrate various devices into their projects without worrying about the underlying hardware details.

   Example use cases might include controlling an LED using `DigitalOutput` or reading sensor data using `DigitalInput`. For instance, you could create a new class that uses `DigitalInput` and `DigitalOutput` to control an LED based on temperature readings from a connected sensor:

```python
from jumpstarter.packages.jumpstarter-driver-raspberrypi import DigitalInput, DigitalOutput

class TemperatureLedController:
    temperature_sensor = DigitalInput("GPIO17")
    led = DigitalOutput("GPIO18")

    def __init__(self):
        self.temperature_sensor.wait_for_active()  # Ensure sensor is connected
        self.led.off()  # Turn off LED initially

    def start(self):
        if self.temperature_sensor.value:  # If sensor is active (i.e., reading temperature)
            self.led.on()  # Turn on the LED

    def stop(self):
        self.led.off()  # Turn off the LED
```

 ```mermaid
   sequenceDiagram
      participant Driver as D
      participant DigitalOutput as DO
      participant DigitalInput as DI
      participant GPIOZero as GZ

      D->>DO: __init__()
      DO->>GZ: Initialize as InputDevice(pin)
      GZ-->>DO: InputDevice(pin) (created as DO.device)

      D->>DI: __init__()
      DI->>GZ: Initialize as DigitalInputDevice(pin)
      GZ-->>DI: DigitalInputDevice(pin) (created as DI.device)

      note over DO: off():
        if not isinstance(DO.device, DigitalOutputDevice):
          DO.device.close()
          DO.device = DigitalOutputDevice(pin)
      end

      DO->>DO.device: off()
      note over DI: wait_for_inactive():
        DI.device.wait_for_inactive()
      end

      D->>DI: wait_for_inactive()
      DI->>DI.device: wait_for_inactive()

      note over DO: on():
        if not isinstance(DO.device, DigitalOutputDevice):
          DO.device.close()
          DO.device = DigitalOutputDevice(pin)
      end

      DO->>DO.device: on()
      note over DI: wait_for_active():
        DI.device.wait_for_active()
      end

      D->>DI: wait_for_active()
      DI->>DI.device: wait_for_active()
   ```

This Mermaid sequence diagram illustrates the interactions between a Driver, its DigitalOutput and DigitalInput child classes, and the GPIOZero library, focusing on the `off` and `wait_for_inactive` functions for the DigitalOutput class and the `wait_for_active` function for the DigitalInput class.