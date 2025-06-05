## Chapter 6: jumpstarter/examples/soc-pytest/jumpstarter_example_soc_pytest/test_on_rpi4.py

 The file `jumpstarter/examples/soc-pytest/jumpstarter_example_soc_pytest/test_on_rpi4.py` is a test script written using the pytest framework for testing the functionality of a Raspberry Pi 4 (RPI4) device, specifically focusing on its power management, TPM2 device, camera, and HDMI output. This script is designed to work with JumpStarter, a platform that provides tools for automating various aspects of software development and testing in embedded systems.

   The test script defines the `TestResource` class, which inherits from `JumpstarterTest`. It sets up a selector for RPI4 devices, allowing it to target specific hardware during tests. The test script uses several fixtures, such as console, video, and shell, to set up and tear down resources required for each test.

   - The `console` fixture returns a `PexpectAdapter` instance that wraps the console of the RPI4 device. It also provides an option to redirect its log output to stdout.
   - The `video` fixture returns an instance of `ImageHash`, which allows for capturing and comparing images from the RPI4's camera.
   - The `shell` fixture initializes a new session with the RPI4 device, performs login, and provides access to the shell after login. It also powers off the device at the end of the test.

   The test script contains several test methods that demonstrate various functionalities of the RPI4 device:
   - `test_setup_device` sets up the RPI4 device by writing a specific image to its storage, booting it, and checking if it successfully boots into the login prompt.
   - `test_tpm2_device` demonstrates the functionality of the TPM2 device by creating a new key pair, signing a message, verifying the signature, and asserting that the operation was successful.
   - `test_power_off_camera`, `test_power_on_camera`, `test_power_on_hdmi`, and `test_login_console_hdmi` test the power management features of the RPI4 device, specifically its camera, HDMI output, and login console.

   This code fits into the JumpStarter project as a demonstration of how to write tests for devices using the JumpStarter framework and pytest. Users can run this script to verify that their RPI4 device is functioning correctly under various conditions, such as power management or TPM2 usage.

 ```mermaid
   sequenceDiagram
      participant Client as Raspberry Pi Client
      participant DUTLink as JumpStarter DUT Link
      participant Console as RPi4 Console
      participant Video as RPi4 Camera
      participant Shell as Command Shell (RPi4)
      participant TestResource as Test Resource Function

      Note over TestResource: This function is responsible for executing the tests on an RPi4 device using JumpStarter.

      TestResource->>Client: Setup Device Fixture
      Client->>DUTLink: Power Off
      DUTLink->>Device: Write Image File
      DUTLink->>Device: Switch Storage to Device
      DUTLink->>Device: Power On
      Note right of Console: The RPi4 boots up and logs in automatically.
      DUTLink-->>Console: Connect to Console for Testing
      Note over Shell: Various commands are executed on the RPi4 via the Command Shell.
      Console->>Shell: Executes Commands
      Shell-->>Console: Outputs Results
      Note left of Console: After testing is complete, the device powers off.
      Console->>DUTLink: Power Off

      TestResource->>Shell: Test TPM2 Device Functionality

      TestResource->>Video: Take Snapshots Before and After Power Cycle
      DUTLink->>Device: Power Off
      Note right of Video: Camera takes a snapshot before power off.
      DUTLink-->>Video: Save Snapshot as "camera_off.jpeg"
      DUTLink->>Device: Power On
      Note left of Video: Camera takes a snapshot after power on.
      DUTLink-->>Video: Save Snapshot as "camera_on.jpeg"

      TestResource->>Console: Login to RPi4 Console Fixture
      TestResource->>Video: Take Snapshot After Boot
      Console->>Shell: Executes Commands for Video Assertion
      Shell-->>Console: Outputs Results of Assertion
      Note right of Console: If assertion passes, the device powers off.
      Console->>DUTLink: Power Off
   ```

This Mermaid sequence diagram illustrates how the key functions interact when testing on an RPi4 device using JumpStarter. The diagram includes the Raspberry Pi Client, DUT Link (JumpStarter DUT Link), Console (RPi4 Console), Video (RPi4 Camera), and Command Shell (RPi4). Each function or action is represented as a participant or note, and the interactions between them are depicted using lines and arrows.