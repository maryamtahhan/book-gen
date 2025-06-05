## Chapter 223: jumpstarter/packages/jumpstarter/jumpstarter/common/storage.py

 The `jumpstarter/packages/jumpstarter/jumpstarter/common/storage.py` file is a Python module in the JumpStarter project, which provides utility functions for interacting with storage devices asynchronously.

   This file defines two main asynchronous functions:

1. `wait_for_storage_device(storage_device, mode, timeout, *, logger)` - This function waits for a specified storage device to become available in the desired mode (either read-only or write-only). It does this by continuously attempting to open the file and checking its size until it exceeds zero or the specified timeout is reached. The function also logs progress and errors to the provided logger object.

2. `write_to_storage_device(storage_device, resource, timeout, fsync_timeout, leeway, *, logger)` - This function writes an asynchronous data stream (represented by `resource`) to a specified storage device. It first waits for the storage device to become available in write-mode using the `wait_for_storage_device` function. Then, it writes the data to the file and fsyncs the file to ensure all data is written before proceeding further. The function logs progress and errors to the provided logger object.

3. `read_from_storage_device(storage_device, resource, timeout, *, logger)` - This function reads an asynchronous data stream (represented by `resource`) from a specified storage device. It first waits for the storage device to become available in read-mode using the `wait_for_storage_device` function. Then, it reads the data from the file and sends it through the provided resource stream. The function logs progress and errors to the provided logger object.

   These functions are used within the JumpStarter project for handling storage tasks, such as writing and reading files to external devices in a way that is scalable and efficient using the AnyIO library. For example, when the user connects an external drive or SD card to their device during the setup process, these functions are called to write the necessary data to the storage device.

 ```mermaid
    sequenceDiagram
        participant User as User
        participant CommonStorage as CommonStorage
        participant FileReadStream as FileReadStream
        participant FileWriteStream as FileWriteStream
        participant AnyByteStream as AnyByteStream
        participant Logger as Logger

        User->>CommonStorage: read_from_storage_device(storage_device, resource, timeout)
        CommonStorage->>CommonStorage: await wait_for_storage_device(storage_device, mode, timeout, logger)
        CommonStorage-->>User: storage_device

        activate CommonStorage
        CommonStorage->>CommonStorage: with os.fdopen(os.open(path, os.O_RDONLY), "rb") as file
        CommonStorage->>FileReadStream: FileReadStream(file)
        CommonStorage-->>User: FileReadStream
        deactivate CommonStorage

        User->>CommonStorage: write_to_storage_device(storage_device, resource, timeout, fsync_timeout, leeway, logger)
        CommonStorage->>CommonStorage: await wait_for_storage_device(storage_device, mode, timeout, logger)
        CommonStorage-->>User: storage_device

        activate CommonStorage
        CommonStorage->>CommonStorage: with os.fdopen(os.open(path, os.O_WRONLY), "wb") as file
        CommonStorage->>FileWriteStream: FileWriteStream(file)
        CommonStorage-->>User: FileWriteStream
        deactivate CommonStorage

        User->>AnyByteStream: Data to write or read
        AnyByteStream->>CommonStorage: Streamed data
    ```