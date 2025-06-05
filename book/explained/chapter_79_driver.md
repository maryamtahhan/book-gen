## Chapter 79: jumpstarter/packages/jumpstarter-driver-energenie/jumpstarter_driver_energenie/driver.py

 The file `jumpstarter/packages/jumpstarter-driver-energenie/jumpstarter_driver_energenie/driver.py` is a Python script that serves as a custom driver for the EnerGenie Programmable surge protector with LAN interface in the JumpStarter project.

   The script defines a class `EnerGenie`, which inherits from both `PowerInterface` and `Driver`. This class encapsulates methods to communicate with an EnerGenie device and control its power switches.

   Important functions within this file include:

   - `login()`: Initializes a session with the EnerGenie device by sending a POST request to the login page of the device. The function returns `True` if the login is successful (status code 200) and `False` otherwise.

   - `__post_init__()`: This method sets up the initial properties of the EnerGenie class, such as the host, password, slot number, base URL for API requests, and logs debugging information. It also checks if the provided inputs are valid.

   - `set_switch(self, switch_number, state)`: Sets the state of a specific power switch on the EnerGenie device based on the given `switch_number` (1-4) and `state` (1 for ON and 0 for OFF). This function first ensures that the login is successful and handles any exceptions during API communication.

   - `on(self) -> None`: Calls `set_switch()` to set the state of the specified slot (default is slot 1) to ON.

   - `off(self) -> None`: Calls `set_switch()` to set the state of the specified slot (default is slot 1) to OFF.

   - `read() -> AsyncGenerator[PowerReading, None]`: This function is not implemented in this file since the EnerGenie device does not support reading power consumption data. It raises a `NotImplementedError`.

   The code provided fits within the project by allowing users to control and interact with their EnerGenie devices programmatically through the JumpStarter framework.

   Example use cases include setting up an automated script to turn on or off specific power switches in response to certain conditions, such as temperature thresholds, time-of-day triggers, or incoming sensor data from IoT devices.

 ```mermaid
sequenceDiagram
participant User as User
participant EnerGenie as EnerGenie

User->>EnerGenie: on()
EnerGenie->>EnerGenie: set_switch(slot, 1)
EnerGenie->>EnerGenie: login()
EnerGenie->>EnerGenie: requests.post(base_url, data={"pw": password})
EnerGenie->>EnerGenie: if response.status_code == 200
    EnerGenie-->>EnerGenie: login successful!
EnerGenie->>EnerGenie: data = {"cte{slot}": 1}
EnerGenie->>EnerGenie: requests.post(base_url, data=data)
EnerGenie->>EnerGenie: if response.status_code != 200
    EnerGenie-->>EnerGenie: Set switch {slot} to 1 state failed!
EnerGenie->>EnerGenie: else
    EnerGenie-->>EnerGenie: Set switch {slot} to 1 state successful
    EnerGenie-->>User: operation completed

User->>EnerGenie: off()
EnerGenie->>EnerGenie: set_switch(slot, 0)
EnerGenie->>EnerGenie: login()
EnerGenie->>EnerGenie: requests.post(base_url, data={"pw": password})
EnerGenien->>EnerGenie: if response.status_code == 200
    EnerGenie-->>EnerGenie: login successful!
EnerGenie->>EnerGenie: data = {"cte{slot}": 0}
EnerGenie->>EnerGenie: requests.post(base_url, data=data)
EnerGenie->>EnerGenie: if response.status_code != 200
    EnerGenie-->>EnerGenie: Set switch {slot} to 0 state failed!
EnerGenie->>EnerGenie: else
    EnerGenie-->>EnerGenie: Set switch {slot} to 0 state successful
    EnerGenie-->>User: operation completed
```

This Mermaid sequence diagram illustrates the interactions between the User and the EnerGenie driver object when calling the `on()` and `off()` functions. It shows how the `set_switch()` function is called to control the state of a specific switch, and how the login function is used to communicate with the device before executing any commands. The diagram also demonstrates the error handling for failed login or command execution scenarios.