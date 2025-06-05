## Chapter 114: jumpstarter/packages/jumpstarter-driver-power/jumpstarter_driver_power/client.py

 The file `jumpstarter/packages/jumpstarter-driver-power/jumpstarter_driver_power/client.py` is a crucial component of the Jumpstarter project, serving as the client for interacting with the power driver. This client class, named `PowerClient`, inherits from `DriverClient` and provides methods to manage device power, namely turning on (`on()`), turning off (`off()`), and performing a power cycle (`cycle()`).

   The `cycle()` function initiates a power cycle sequence by turning the device off, waiting for a specified duration, and then turning it back on. This is useful when the device requires a soft reset or needs to be rebooted.

   The `read()` method allows for continuous reading of power status updates from the driver. It returns a generator yielding `PowerReading` objects.

   In addition, a command-line interface (CLI) is provided for controlling the power device directly from the terminal using simple commands like `on`, `off`, and `cycle`. The CLI allows users to specify optional parameters like wait time in the `cycle` command.

   When working with virtual power devices, such as simulations or mockups, an instance of the `VirtualPowerClient` class can be used instead. This client behaves similarly but includes additional methods for destroying the virtual device after it's been powered off.

   In summary, this code provides a powerful and flexible interface for controlling various power devices within the Jumpstarter project. Whether interacting through continuous updates or using the CLI, users can easily manage their devices without needing extensive programming knowledge.

 ```mermaid
    sequenceDiagram
        participant PowerClient as PC
        participant DriverClient as DC

        note over PC,DC: Initialize classes
        DC->>PC: Inherit from DriverClient
        DC->>PC: Define on() function
        DC->>PC: Define off() function
        DC->>PC: Define cycle() function
        DC->>PC: Define read() generator function
        DC->>PC: Define cli() function

        PC->>DC: Call "on"
        DC-->>PC: Executes command

        PC->>DC: Call "off"
        DC-->>PC: Executes command

        PC->>DC: Call "cycle" with wait parameter
        DC-->>PC: Executes power cycle sequence

        PC->>DC: Start reading stream of PowerReading objects
        for v in DC.streamingcall("read"):
            PC-->>DC: Receive each PowerReading object
            DC->>PC: Process and yield PowerReading object

        PC->>DC: Call cli()
        DC-->>PC: Returns base command group with on(), off(), and cycle() commands

        PC->>DC.cli(): Call on() command
        DC-->>PC: Executes power on

        PC->>DC.cli(): Call off() command
        DC-->>PC: Executes power off

        PC->>DC.cli(): Call cycle(wait) command with wait=2
        DC-->>PC: Power cycles the device after waiting for 2 seconds
   ```