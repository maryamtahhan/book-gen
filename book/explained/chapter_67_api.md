## Chapter 67: jumpstarter/packages/jumpstarter-driver-corellium/jumpstarter_driver_corellium/corellium/api.py

 The file `jumpstarter/packages/jumpstarter-driver-corellium/jumpstarter_driver_corellium/corellium/api.py` is a Python module for interacting with the Corellium REST API, specifically designed for use by the Corellium driver within the JumpStarter project. It provides an API client class (`ApiClient`) that encapsulates all HTTP requests to the Corellium API using the provided token and base URL.

   Important functions in this file include:

1. `__init__()` - Initializes a new instance of the API client, taking the host and token as parameters for creating HTTP requests with proper authorization headers.
2. `baseurl` - Returns the base URL path used for all API calls.
3. `get_project(self, project_ref: str = 'Default Project') -> Optional[Project]` - Retrieves a project based on its reference (either id or name). If the project is not found, it returns None.
4. `get_device(self, model: str) -> Optional[Device]` - Retrieves a device spec from Corellium's list based on the given model name. If the device is not found, it returns None.
5. `create_instance(self, name: str, project: Project, device: Device, os_version: str, os_build: str) -> Instance` - Creates a new virtual instance using the provided project, device spec, and operating system details. Returns an `Instance` object on success, otherwise raises an exception.
6. `get_instance(self, instance_ref: str) -> Optional[Instance]` - Retrieves an existing instance by its name or id. If the instance is not found, it returns None.
7. `set_instance_state(self, instance: Instance, instance_state: str) -> None` - Sets the state of a virtual instance using Corellium's API. Valid instance states are listed in the function description. Returns nothing on success; raises an exception if something goes wrong.
8. `destroy_instance(self, instance: Instance) -> None` - Deletes a virtual instance from Corellium's API. Does not return anything since Corellium's API returns a HTTP 204 response. Raises an exception if something goes wrong.
9. `get_instance_console_id(self, instance: Instance, console_name: str) -> Optional[str]` - Retrieves the id of an instance's console by its name. If the console is not found, it returns None.
10. `get_instance_console_url(self, instance: Instance, console_id: str) -> Optional[str]` - Retrieves a websocket URL to stream logs from a specific console for an instance based on its id. If the console is not found, it returns None.

   This code fits within the project by providing the ability to interact with Corellium's API programmatically, allowing the Corellium driver to perform various operations such as creating, managing, and deleting virtual instances or retrieving their status and logs.

   Example use cases include initializing a new API client instance using the Corellium host and token:
   ```python
   api_client = ApiClient('api.corellium.com', '<API token>')
   ```
   Then, using the functions provided by the API client to create, manage, and delete virtual instances or retrieve their status and logs:
   ```python
   project = api_client.get_project('<Project name or id>')
   device = api_client.get_device('<Device model>')
   instance = api_client.create_instance('MyInstance', project, device, '<OS version>', '<OS build>')
   # ... manage the instance using set_instance_state() or get_instance_console_url() ...
   api_client.destroy_instance(instance)
   ```

 ```mermaid
    sequenceDiagram
        participant C as Client
        participant API as Corellium API
        C->>API: get_project()
        API-->>C: Returns Project object or None

        C->>API: get_device(model)
        API-->>C: Returns Device object or None

        C->>API: create_instance(name, project, device, os_version, os_build)
        API-->>C: Returns Instance object

        C->>API: get_instance(instance_ref)
        API-->>C: Returns Instance object or None

        C->>API: set_instance_state(instance, instance_state)
        API-->>C: No response (204 HTTP status code)

        C->>API: destroy_instance(instance)
        API-->>C: No response (204 HTTP status code)

        C->>API: get_instance_console_id(instance, console_name)
        API-->>C: Returns console id or None

        C->>API: get_instance_console_url(instance, console_id)
        API-->>C: Returns console URL (websocket)
    ```