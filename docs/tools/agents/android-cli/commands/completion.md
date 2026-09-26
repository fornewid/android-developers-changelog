---
title: https://developer.android.com/tools/agents/android-cli/commands/completion
url: https://developer.android.com/tools/agents/android-cli/commands/completion
source: md.txt
---

Installs shell autocomplete configuration for Android CLI in the current user profile.

## Usage

    android completion [-h] [<shell>]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<shell>` - If provided, prints the completion configuration script for the specified shell without installing it. Supports Bash and Zsh.

## Description

`android completion` configures tab-completion for `android` commands, subcommands, and options in your shell.

When run without arguments, `android completion` automatically detects your active shell and updates your user profile (such as the `~/.bashrc` or `~/.zshrc` files) to load the completion script on startup. When a `<shell>` argument (`bash` or `zsh`) is provided, the completion script is printed to standard output without modifying any files on disk.

### Supported shells

- `bash`: Generates or installs a Bash completion script.
- `zsh`: Generates or installs a Zsh completion script.

### Examples

Automatically install autocomplete into your current user profile:

    android completion

Print the Bash autocomplete script to standard output or load it in the current session:

    source <(android completion bash)

Print the Zsh autocomplete script to standard output or load it in the current session:

    source <(android completion zsh)