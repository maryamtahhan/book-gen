## Chapter 48: jumpstarter/packages/jumpstarter-cli/jumpstarter_cli/get.py

 In the `jumpstarter/packages/jumpstarter-cli/jumpstarter_cli/get.py` file, we have defined a set of commands for retrieving information about various resources within the Jumpstarter project. The purpose of this file is to provide an interface for users to view one or many exporters and leases, each of which serves specific roles in the context of Jumpstarter.

   The `get()` function acts as a group containing multiple subcommands, specifically `get_exporters()` and `get_leases()`. Each subcommand is responsible for displaying a different type of resource in various output formats based on user preferences. These output formats are determined by the `output` parameter passed to each function, which can take values from the `OutputMode` and `OutputType` enumerations defined in other modules.

   The `get_exporters()` function retrieves a list of exporters that match a given filter (if provided) and displays them using the selected output format. Similarly, the `get_leases()` function retrieves a list of leases and displays them accordingly. Both functions utilize the `config`, `opt_selector`, and `handle_exceptions` objects to access configuration data, parse command-line arguments, and manage exceptions respectively.

   In terms of where this code fits in the project, these commands are part of the Jumpstarter CLI (Command Line Interface) package, which is responsible for providing an easy-to-use interface for interacting with various components of the Jumpstarter system. This includes managing resources like exporters and leases, as well as other functionalities like deployments and services.

   Example use cases could include displaying a list of all available exporters in JSON format or showing information about specific leases in YAML format for further processing by other tools:

   ```sh
   jumpstarter get exporters --output json
   jumpstarter get leases my-lease --output yaml
   ```

 ```mermaid
   sequenceDiagram
        participant User as User
        participant Config as Config
        participant Exporter as Exporter
        participant Lease as Lease

        User->>Config: get_exporters("selector")
        Config-->Exporter: list_exporters(filter="selector")
        Exporter-->>User: exporter details (JSON, YAML, NAME)

        User->>Config: get_leases("selector")
        Config-->Lease: list_leases(filter="selector")
        Lease-->>User: lease details (JSON, YAML, NAME)
   ```

This diagram illustrates how the key functions interact in the `get.py` script. The user interacts with the script by invoking commands like `get exporters` or `get leases`, passing a selector if necessary. These commands are handled by the `get_exporters()` and `get_leases()` functions, respectively. Each of these functions retrieves relevant data from the Config object, which manages interactions with the underlying configuration data. The Exporter and Lease objects then provide the detailed information requested by the user in the desired format (JSON, YAML, or NAME).