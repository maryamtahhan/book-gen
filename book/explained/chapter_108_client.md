## Chapter 108: jumpstarter/packages/jumpstarter-driver-opendal/jumpstarter_driver_opendal/client.py

 This is a Python script that defines two classes `OpendalAdapter` and `FlasherClient`. The `OpendalAdapter` class allows for working with files using different operators (like "fs" for file system or "dut" for device). The `FlasherClient` class inherits from the abstract base class `DriverClient` and provides methods for flashing images to a device ("flash") and dumping images from the device ("dump"). It also defines a command line interface (CLI) that can be used to execute these operations.

   The script also defines a `StorageMuxClient` class that handles connecting and disconnecting storage devices from host or device, as well as reading and writing files using different operators. It inherits from the `FlasherClient` class to provide flashing and dumping capabilities, and extends its functionality with the ability to work with local files on disk. Finally, a `StorageMuxFlasherClient` is defined that inherits from both `FlasherClient` and `StorageMuxClient`, combining all of their functionalities.

   To use this script, you would typically instantiate one of the client classes (either `FlasherClient`, `StorageMuxClient`, or `StorageMuxFlasherClient`) with some configuration data, and then call its methods to perform the desired operations on your storage device. For example:

   ```python
   client = FlasherClient(config)
   client.flash("/path/to/image.bin")
   client.dump("/path/to/dumped_image.bin")
   ```

   The script also provides a command line interface (CLI) that can be used to execute these operations from the terminal. To use the CLI, you would run the script with the desired arguments:

   ```bash
   python script.py flash /path/to/image.bin
   python script.py dump /path/to/dumped_image.bin
   ```

 This script defines two classes `OpendalAdapter` and `FlasherClient`. `OpenadalAdapter` is used to wrap a file handle with additional context like the operator, client, and path. It's used by both `FlasherClient` and `StorageMuxFlasherClient`.

   The `FlasherClient` class inherits from `DriverClient` and implements two abstract methods `flash()` and `dump()` that are responsible for flashing an image to the device under test (DUT) or dumping an image from it. It also has a `cli` method that returns a click command group object that contains commands for flashing and dumping images.

   The `StorageMuxClient` class also inherits from `DriverClient`. It has methods to connect/disconnect storage to the host or DUT, read or write data from/to the storage, and write/read local files to/from the storage. It also has a `cli` method that returns a click command group object with commands for connecting, disconnecting, reading, writing files, and reading/writing local files.

   The `StorageMuxFlasherClient` class is a combination of `FlasherClient` and `StorageMuxClient`. It inherits all the methods from both classes and implements the flashing and dumping functionalities using the storage connection methods provided by `StorageMuxClient`. Its `cli` method returns a click command group object that contains commands for flashing, dumping, connecting, disconnecting, reading/writing files, and reading/writing local files.