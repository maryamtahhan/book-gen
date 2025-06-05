## Chapter 16: jumpstarter/packages/jumpstarter-cli-admin/jumpstarter_cli_admin/get.py

 This chapter discusses the purpose and functionality of the file `jumpstarter/packages/jumpstarter-cli-admin/jumpstarter_cli_admin/get.py`. This module is a part of the larger Jumpstarter project, which aims to manage Kubernetes objects related to IoT devices.

   The primary purpose of this file is to define command line interface (CLI) commands for retrieving various Jumpstarter Kubernetes objects, specifically clients, exporters, and leases. These objects are important components in the Jumpstarter system, representing different aspects of connected IoT devices within a Kubernetes cluster.

   The file contains three main functions: `get_client()`, `get_exporter()`, and `get_lease()`. Each function defines a CLI command (`get client`, `get exporter`, and `get lease`) for retrieving the respective objects in a Kubernetes cluster. These functions accept various arguments, such as the name of the object to be retrieved, the Kubernetes namespace, kubeconfig, context, and output format. Some functions also accept additional flags, like the ability to display device information for exporters.

   The functions use asynchronous API calls to interact with Kubernetes APIs (ClientsV1Alpha1Api, ExportersV1Alpha1Api, LeasesV1Alpha1Api) and handle exceptions using helper functions defined within the same module (handle_k8s_api_exception() and handle_k8s_config_exception()). These helper functions print meaningful error messages for users.

   After retrieving an object, the functions use other helper functions in the same module to format and display the results to the user. For example, there are `print_client()`, `print_clients()`, `print_exporter()`, `print_exporters()`, `print_lease()`, and `print_leases()` functions that help with formatting and outputting the retrieved objects in a clear and readable manner.

   Example use cases for these commands include:

   - Retrieving a specific client from a Kubernetes cluster using `jumpstarter-cli get client [client-name]`.
   - Listing all clients in a Kubernetes namespace using `jumpstarter-cli get client --namespace my-namespace`.
   - Retrieving an exporter with device information from a Kubernetes cluster using `jumpstarter-cli get exporter [exporter-name] -d`.
   - Listing all exporters in a Kubernetes namespace along with their associated devices using `jumpstarter-cli get exporter --namespace my-namespace -d`.
   - Retrieving a specific lease from a Kubernetes cluster using `jumpstarter-cli get lease [lease-name]`.
   - Listing all leases in a Kubernetes namespace using `jumpstarter-cli get lease --namespace my-namespace`.

 ```mermaid
    sequenceDiagram
        participant User as User
        participant CLI as CLI
        participant ClientsApi as Clients Api
        participant ExportersApi as Exporters Api
        participant LeasesApi as Leases Api

        User->>CLI: Run command (get, client, exporter, lease)
        CLI->>ClientsApi: Create ClientsV1Alpha1Api instance (with namespace, kubeconfig, context)
        CLI->>ExportersApi: Create ExportersV1Alpha1Api instance (with namespace, kubeconfig, context)
        CLI->>LeasesApi: Create LeasesV1Alpha1Api instance (with namespace, kubeconfig, context)

        ClientsApi->>ClientsApi: Call get_client(name) or list_clients()
        ExportersApi->>ExportersApi: Call get_exporter(name) or list_exporters()
        LeasesApi->>LeasesApi: Call get_lease(name) or list_leases()

        ClientsApi<--ClientsApi: Response (client object or client list)
        ExportersApi<--ExportersApi: Response (exporter object or exporter list)
        LeasesApi<--LeasesApi: Response (lease object or lease list)

        CLI->>User: Print client, exporter, or lease objects (with appropriate formatting based on output option)
    ```