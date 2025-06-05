## Chapter 65: jumpstarter/packages/jumpstarter-driver-corellium/jumpstarter_driver_corellium/client.py

 Chapter Title: Understanding the `CorelliumClient` Class in JumpStarter Project

   The file `jumpstarter/packages/jumpstarter-driver-corellium/jumpstarter_driver_corellium/client.py` is a crucial component of the JumpStarter project, specifically designed for interacting with Corellium's device simulation services. This Python module defines the `CorelliumClient` class, which inherits from the `CompositeClient` class in the jumpstart-driver-composite library.

   The primary purpose of the `CorelliumClient` class is to facilitate communication between JumpStarter and Corellium's device simulation services. It encapsulates the specific API calls and logic required for interacting with these services, making it easier to manage and extend.

   Important Functions or Classes:

   - `CorelliumClient(host, port, **kwargs)`: The constructor initializes a new instance of the `CorelliumClient`, taking in the host address and port number as required arguments. Additional keyword arguments can be provided to customize the client's behavior if necessary.

   This code fits within the JumpStarter project as part of the driver layer, responsible for interfacing with various device simulation services. By providing a `CorelliumClient`, the JumpStarter framework can support Corellium as one of its available device providers, enabling users to leverage Corellium's offerings seamlessly within the framework.

   Example Use Cases:

   - To create a new session with a specified iOS or Android device image on Corellium:
     ```python
     from jumpstarter_driver_corellium.client import CorelliumClient

     client = CorelliumClient(host='localhost', port=12345)
     session = client.create_session(device_image='iOS 14.0 Simulator (iPhone X)')
     ```
   - To execute a command on the device within an existing session:
     ```python
     from jumpstarter_driver_corellium.client import CorelliumClient

     client = CorelliumClient(host='localhost', port=12345)
     with session.connect() as ssh:
         result = ssh.run('uname -a')  # Run command and capture output
     print(result.stdout.decode())  # Print the command's output
     ```

 ```mermaid
sequenceDiagram
participant Driver as JumpStarter Driver
participant CorelliumClient as CorelliumClient

Driver->>CorelliumClient: connect(ip, api_key)
CorelliumClient-->>Driver: success or failure

CorelliumClient->>CorelliumServer: authenticate(api_key)
CorelliumServer-->>CorelliumClient: success or failure and token

Note over CorelliumClient: Saves the received token for later use

Device->>CorelliumServer: powerOn()

CorelliumServer-->>Device: powering on...

Device->>CorelliumClient: set_device(device_id)
CorelliumClient-->>Driver: success or failure

Device->>CorelliumServer: attach(device_id, emulator_version)

Note over CorelliumServer: Prepares the device for emulation and returns an emulator ID

CorelliumServer-->>Device: emulator started (emulator_id)

Device->>CorelliumClient: set_emulator(emulator_id)
CorelliumClient-->>Driver: success or failure

Device->>CorelliumServer: start(boot_args, kernel_args)

Note over CorelliumServer: Starts the emulated device with given boot and kernel arguments

Device->>CorelliumClient: started()
CorelliumClient-->>Driver: success or failure

Device->>CorelliumServer: (interaction loop: send commands, receive responses)

Device<--CorelliumServer: response(command, data)

Device->>CorelliumClient: (event loop: pass events to the driver)
CorelliumClient-->>Driver: event(event_type, data)

Note over Device: Performs actions based on events and sends corresponding commands

Device->>CorelliumServer: powerOff()

CorelliumServer-->>Device: powering off...

Device->>CorelliumClient: detach()
CorelliumClient-->>Driver: success or failure

Device->>CorelliumServer: powerOff()

Note over CorelliumServer: Powers down the emulated device and returns to idle state
```