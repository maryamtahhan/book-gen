## Chapter 116: jumpstarter/packages/jumpstarter-driver-power/jumpstarter_driver_power/common.py

 Chapter Title: Understanding `jumpstarter/packages/jumpstarter-driver-power/jumpstart_driver_power/common.py` in the JumpStarter Project

   This chapter focuses on dissecting the purpose and functionality of the Python module file, `common.py`, located within the `jumpstarter-driver-power` package of the JumpStarter project. The primary intent of this code is to provide a shared utility space for defining common data models, functions, and properties related to power measurements in the broader context of the JumpStarter system.

   The key class defined in `common.py` is the `PowerReading` model, which inherits from the Pydantic base model. This class represents a single instance of power measurement data, encapsulating two properties: voltage (in volts) and current (in amperes). The class also provides a calculated property called `apparent_power`, which is the product of the voltage and current values.

   The `apparent_power` property is defined using a decorator function @property, allowing users to access it as if it were an attribute rather than a method. This is a common practice in object-oriented programming that helps maintain a clean and readable API for the class.

   Within the broader context of the JumpStarter project, this code serves as a foundation for various modules dealing with power measurement, calculations, and control across different components of the system. For instance, when interacting with a battery pack or charging port, the shared `PowerReading` model can be utilized to standardize how power data is represented and exchanged.

   As an example use case, consider a module responsible for controlling a DC-DC converter. This module would rely on the `PowerReading` class to encapsulate the input voltage and current readings, as well as calculate the output apparent power after adjusting for the conversion efficiency. The shared nature of this data model ensures consistency and simplifies the development process across different components within the system.

 ```mermaid
sequenceDiagram
actor User as U
participant Driver as D
participant PowerReading as PR

U->>D: start()
D->>PR: get_power_reading()
PR->>D: PowerReading(voltage, current)
D->>U: show_power_reading(apparent_power)

U->>D: stop()
D->>PR: clear_power_reading()
```

In this Mermaid diagram, the `User` (U) interacts with the `Driver` (D). The Driver uses a `PowerReading` (PR) object to get and show power readings. When the User asks for the start(), the Driver gets the Power Reading object, and when they ask for stop(), the Driver clears the Power Reading object.