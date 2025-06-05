## Chapter 115: jumpstarter/packages/jumpstarter-driver-power/jumpstarter_driver_power/client_test.py

 In the `jumpstarter/packages/jumpstarter-driver-power/jumpstarter_driver_power/client_test.py` file, we find a test function named `test_log_stream`. This module is part of the unit testing suite for the client class in the `driver` package within the project's `jumpstarter-driver-power` package.

   The purpose of this test is to ensure that the logging functionality of the `AsyncDriverClient` object, which represents a connection between the JumpStarter application and a specific driver (e.g., a power driver), is working correctly. Specifically, it checks whether the `log()` method within the client instance correctly logs two events: "power on" when the device is turned on, and "power off" when the device is turned off.

   The test function uses the `unittest.mock` library to create a mock power driver (`MockPower`) and replace the actual logging mechanism used by the client during the test with a MagicMock object (`log`). This allows us to verify that the correct log messages are called, ensuring that the logging functionality behaves as expected without relying on an external power driver.

   The function uses the `serve` context manager from the `jumpstarter.common.utils` module to create a mock server running the `MockPower` object. Within this server context, it sets up the test by establishing a connection using the client and initializing the MagicMock log object as an attribute of the client instance.

   Finally, the function uses the `with` statement with the client's `log_stream()` method to create a context manager that ensures the log messages are flushed and captured correctly during testing. It then sends on and off commands to the power driver (simulated by the mock power driver) and verifies that the corresponding log messages have been called using the `assert_called_with()` method of the MagicMock object.

   In a real-world scenario, this test might be part of a larger test suite for the JumpStarter project, helping to ensure that the logging functionality of the driver connection is robust and reliable. This test can also serve as an example of how to write unit tests for classes that interact with external resources like drivers, by mocking these dependencies and verifying their behavior using MagicMock objects.

 ```mermaid
sequenceDiagram
participant Driver as Driver
participant Test as Test
participant Log as Log

Test->>Driver: on()
Driver->>Log: logs "power on" (as INFO)

Test->>Driver: off()
Driver->>Log: logs "power off" (as INFO)
   ```

This sequence diagram illustrates that when the test function calls `on()` and `off()` on a mock power driver, it also logs these actions to a log object. The log messages are of `INFO` level.