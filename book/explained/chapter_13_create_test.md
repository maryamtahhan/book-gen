## Chapter 13: jumpstarter/packages/jumpstarter-cli-admin/jumpstarter_cli_admin/create_test.py

 This Python script defines functions for creating and testing the creation of CustomResources (Client-defined Kubernetes resources) using a command-line tool, called `create`. The resources defined here are Client-defined Resources with API version `jumpstarter.dev/v1alpha1`:

    - A `ClientObjectReference` named `{name}-credential`, which is used as a reference to the credential object in Exporter and ExportSet objects.
    - A `Device` resource, which represents a hardware device that can be managed by Kubernetes. This resource is not defined here, but it should be created according to the API schema of your specific use case.

The script defines two resources: `Client` (representing Clients) and `Exporter` (representing Exporters). The test functions for each resource are structured similarly, where they create a mock Kubernetes API client, patch the necessary methods to return predefined responses, and then invoke the `create` command using a `CliRunner`.

The tests cover the following scenarios:

1. Creating a Client or Exporter without saving the configuration (using the `--save` flag).
2. Creating a Client or Exporter with insecure TLS configuration (using the `--insecure-tls` flag).
3. Creating a Client or Exporter with no interactive mode (using the `--nointeractive` flag).
4. Saving the configuration to a custom path using the `--out` flag.
5. Outputting the configuration in JSON, YAML, or name format using the appropriate flags.

The test functions for Clients and Exporters are tested separately to ensure that the creation process is working correctly for each resource. The scripts use the `pytest` library for running the tests. To run the tests, save this script as a .py file (e.g., create.py) and execute `pytest create.py` in your terminal.

 This code provides test cases for creating both a client and an exporter in Kubernetes using the `kubectl` command-line tool. The tests cover various scenarios such as:

1. Creating without saving the configuration (client and exporter)
2. Insecure TLS configuration for client and exporter
3. Accepting or denying insecure TLS prompts during creation
4. Saving configurations with custom paths for both client and exporter
5. Creating with no interactive prompts
6. Creating with JSON and YAML outputs for both client and exporter
7. Creating with name output for both client and exporter

The code uses the `unittest` library for testing, and patch decorators to mock various functions required for creating resources in Kubernetes. The tests are organized logically by resource type (client and exporter) and the scenarios being tested.