## Chapter 42: jumpstarter/packages/jumpstarter-cli/jumpstarter_cli/common.py

 The file `jumpstarter/packages/jumpstarter-cli/jumpstarter_cli/common.py` is a module in the Jumpstarter project's command-line interface (CLI). This module provides utility functions, classes, and command line option definitions that are shared across multiple command handlers within the CLI.

   Here are descriptions of important elements in this file:

   - `opt_selector` is a click option definition that allows users to specify a label query as an argument for filtering objects based on their labels. The query supports '=', '==', and '!=' operators.

   - The `DurationParamType` class extends the click ParamType abstract base class. This custom parameter type is used to validate command line arguments that represent durations. It accepts either a `timedelta` object or a string that can be converted into a `timedelta`.

   - The `DURATION` variable is an instance of the `DurationParamType`. This is used for convenience when defining click options requiring duration input.

   - `opt_duration_partial` is a partial function that allows for easier definition of command line options expecting duration input.

This code plays a crucial role in the project by standardizing the handling and validation of common command line arguments, such as labels and durations, across various command handlers in the CLI. For example, when users specify a label query using `-l` or `--selector`, the options are filtered appropriately based on their constraints. Similarly, duration input is validated to ensure it adheres to specified formats, making the user experience consistent and seamless across commands.

 ```mermaid
   sequenceDiagram
      participant User as User
      participant CLI as CLI
      participant Common as Common

      User->>CLI: Run command with options (opt_selector, opt_duration_partial)
      CLI->>Common: Parse options (opt_selector, opt_duration_partial)
      Common->>Common: Initialize DurationParamType and partial(click.option)
      Common->>CLI: Return parsed options

      User->>Common: Call function with parsed options
      Common->>Common: Execute function based on selector and duration
      Note over Common: Function may perform various tasks such as filtering, sorting, or querying data

      Common-->>User: Return result
   ```