## Chapter 176: jumpstarter/packages/jumpstarter-kubernetes/jumpstarter_kubernetes/exporters.py

 The `jumpstarter/packages/jumpstarter-kubernetes/jumpstarter_kubernetes/exporters.py` file is a crucial part of the project that deals with managing Kubernetes Custom Resources for Exporter objects, which are responsible for collecting and exporting data from a system to a specific endpoint.

   The file defines several classes and functions for creating, listing, retrieving, and deleting Exporter Custom Resources. These resources include `V1Alpha1Exporter`, `V1Alpha1ExporterDevice`, and `V1Alpha1ExporterStatus`. Each of these classes represents different aspects of the Exporter object, such as its metadata, status, devices, and overall structure.

   Additionally, the file includes a class called `ExportersV1Alpha1Api` that serves as an interface for interacting with the Kubernetes API to create, retrieve, update, and delete Exporter objects. This class provides methods like `list_exporters()`, `get_exporter()`, `create_exporter()`, `get_exporter_config()`, and `delete_exporter()`.

   In the context of the project, these exporters are used to gather data from various sources within a system and export it to an external service for further processing or analysis. For example, an Exporter could collect performance metrics from pods running in a Kubernetes cluster and send them to a monitoring service like Prometheus.

   By using this file, developers can easily manage their Exporter resources and customize the data collection process as needed for their specific use cases.

 ```mermaid
    sequenceDiagram
        participant User as User
        participant API as API
        participant ExporterV1Alpha1Api as ExporterAPI
        participant CoreApi as CoreApi

        User->>ExporterAPI: List_exporters()
        ExporterAPI-->>User: Returns list of exporters in the cluster

        User->>ExporterAPI: Get_exporter(name)
        ExporterAPI-->>User: Returns a single exporter object

        User->>ExporterAPI: Create_exporter(name, labels, oidc_username)
        ExporterAPI->>CoreApi: Create namespaced custom object (namespace, group, plural, version, body)
        CoreApi-->>ExporterAPI: Acknowledgement of creation
        ExporterAPI->>User: Exporter object created in the cluster
        Note over ExporterAPI: Wait for credentials to become available
        ExporterAPI->>CoreApi: Get namespaced custom object (namespace, group, plural, version, name)
        CoreApi-->>ExporterAPI: Updated exporter object with credentials
        loop Check if updated exporter has credentials
            ExporterAPI->>CoreApi: Get namespaced custom object (namespace, group, plural, version, name)
            CoreApi-->>ExporterAPI: Updated exporter object
        end
        Note over ExporterAPI: Retry until timeout or exporter has credentials
        if timeout then
          ExporterAPI->>User: Raise Exception("Timeout waiting for exporter credentials")
        else
          ExporterAPI-->>User: Return the created exporter object
        end

        User->>ExporterAPI: Get_exporter_config(name)
        ExporterAPI->>CoreApi: Read namespaced secret (secret name, namespace)
        CoreApi-->>ExporterAPI: Secret data including token
        ExporterAPI->>User: Return the exporter config with endpoint, token and export

        User->>ExporterAPI: Delete_exporter(name)
        ExporterAPI->>CoreApi: Delete namespaced custom object (namespace, name, group, plural, version)
        CoreApi-->>ExporterAPI: Acknowledgement of deletion
    ```