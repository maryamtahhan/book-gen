## Chapter 251: jumpstarter/packages/jumpstarter/jumpstarter/streams/metadata.py

 The `jumpstarter/packages/jumpstarter/jumpstarter/streams/metadata.py` file in the Jumpstarter project defines a custom ObjectStream class named `MetadataStream`. This class is used to send and receive data along with additional metadata as key-value pairs, such as headers or tags, in a bi-directional stream connection.

   The purpose of this custom `MetadataStream` is to extend the functionality of AnyIO's built-in ObjectStream, allowing users to easily attach metadata to messages sent over the stream, just like in gRPC (https://grpc.io/docs/guides/metadata/) and other protocols that utilize metadata for request and response handling.

   The `MetadataStream` class inherits from `ObjectStream[bytes]`, meaning it can send and receive raw bytes as data over the stream, while also providing additional functionality to manage metadata attached to those bytes. Key functions within this class include:

   - `send(self, item: bytes)`: Sends an item (bytes) over the underlying stream.
   - `receive(self) -> bytes`: Receives an item from the underlying stream as bytes.
   - `send_eof(self)`: Marks the end of the data transmission for this stream.
   - `aclose(self)`: Closes the underlying stream connection.

   A property named `extra_attributes` is defined, which returns a dictionary containing both the metadata attached to the stream and the metadata of the underlying stream instance (if any). This allows users to easily access and manipulate the metadata associated with the stream.

   In the context of the Jumpstarter project, this `MetadataStream` class can be utilized when creating custom client or server handlers that communicate over bi-directional streams. Example use cases may include adding authentication headers, tracking request/response timestamps, or implementing custom logging based on specific metadata tags.

   Here's a simple example of using the `MetadataStream`:

```python
import anyio
from jumpstarter.packages.jumpstarter.jumpstarter.streams import MetadataStream

async def client_handler(stream: MetadataStream):
    # Set metadata on the outgoing stream, such as an authentication token
    await stream.send("Hello world!".encode(), metadata={"auth": "token123"})

    # Receive data from the server with attached metadata
    received_data = await stream.receive()
    print(f"Received: {received_data.decode()} Metadata: {stream.extra_attributes['metadata']}")

async def server_handler(stream: MetadataStream):
    # Receive data with metadata from the client
    data, metadata = await stream.receive()

    # Access client's metadata for further processing or validation
    auth_token = metadata.get("auth")
    if not auth_token:
        raise ValueError("Authentication token missing.")

    # Send response to the client with additional metadata
    await stream.send(b"OK", metadata={"status": "200 OK"})
```

 ```mermaid
sequenceDiagram
    participant User as User
    participant MetadataStream as MetadataStream
    participant GRPCStream as GRPCStream

    User->>MetadataStream: Initialize MetadataStream with user data
    User->>MetadataStream: Send metadata with each message
    User->>MetadataStream: Close connection

    MetadataStream->>GRPCStream: Receive messages from GRPCStream
    MetadataStream->>GRPCStream: Forward messages and metadata
    MetadataStream->>GRPCStream: Close connection

    Note over MetadataStream, GRPCStream: Inherits behavior from ObjectStream
    ```