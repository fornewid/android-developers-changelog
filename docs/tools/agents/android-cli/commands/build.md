---
title: https://developer.android.com/tools/agents/android-cli/commands/build
url: https://developer.android.com/tools/agents/android-cli/commands/build
source: md.txt
---

Build android artifacts.

## Usage

    android build [-h] [<reference>] [-- <build_args>]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<reference>` - Build reference (\[system://\]\[path\]?\[target\]).
- `-- <build_args>` - Arguments passed verbatim to the build system. Use -- to separate from other arguments.

## Description

`android build` detects the build system of a workspace (Gradle, Bazel, Soong,
Lightbuild, or a build system declared in the Android CLI configuration) and
builds the requested target with it.

Pass a build reference (`[system://][path]?[target]`) to select the workspace
and target to build, or omit `<reference>` to build the default target in the
current workspace.

### Build references

A build reference has three optional parts:

- `system://`: Forces a specific build system (for example, `gradle://` or `bazel://`) instead of detecting it from the workspace.
- `path`: Directory inside the workspace to build from, absolute or relative to the current directory (defaults to the current directory).
- `?target`: What to build, in the build system's own syntax (for example, a Gradle project path such as `:app` or `:app@debug`, or a Bazel label such as `//app:app`).

The `?` separator is required whenever `system://` or `path` is present (for
example, `gradle://?`, `./app?`, or `gradle://./app?:app`). Without `?`, the
whole reference is treated as the target.

Arguments after `--` are passed verbatim to the underlying build system.

### Examples

Build the default target in the current workspace:

    android build

Build `:app` in the current Gradle workspace:

    android build :app

Build the `debug` variant of `:app` (`:app@debug`) from the Gradle workspace at
`$HOME/my-app`, passing extra arguments to Gradle:

    android build $HOME/my-app?:app@debug -- --offline

Build a Bazel target, forcing the Bazel build system:

    android build bazel://?//app:app