---
title: https://developer.android.com/tools/agents/android-cli/commands/preview_render
url: https://developer.android.com/tools/agents/android-cli/commands/preview_render
source: md.txt
---

Builds a target and renders its Jetpack Compose @Preview functions to PNG images
and optional component tree JSON files.

## Usage

    android preview render [-h] [--component-tree] [--daemon] [--format=PARAM] [--fqn=PARAM] [--no-image] [--output=PARAM] [<reference>] [-- <build_args>]

## Options

- `--component-tree` - Save the component tree (bounds, component names, source locations, semantics, parameters, and modifiers) to a companion JSON file.
- `--daemon` - Run the preview renderer as a persistent background daemon (shuts down after 10 minutes of inactivity).
- `-f,--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `--fqn=PARAM` - Fully qualified name of a preview to render. Can be specified multiple times.
- `-h,--help` - Shows the help message for the specified command.
- `--no-image` - Skip rendering the preview image (requires --component-tree).
- `-o,--output=PARAM` - Directory or file path to write rendered preview outputs (defaults to a temporary directory).

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<reference>` - Build reference (\[system://\]\[path\]?\[target\]).
- `-- <build_args>` - Arguments passed verbatim to the build system. Use -- to separate from other arguments.

## Description

`android preview render` compiles the target and renders Jetpack Compose
`@Preview` functions offscreen (to a temporary directory by default, or to the
path specified by `--output`), printing the absolute paths of the generated PNG
images and optional component tree JSON files to standard output.

Pass a build reference (`[system://][path]?[target]`) to select the workspace
and target to build, or omit `<reference>` to use the default target in the
current workspace.

### Filter and configure preview output

- `--fqn`: Specifies the fully qualified name of a `@Preview` function to render (for example, `com.example.app.HomeScreenKt.HomeScreenPreview`). At least one `--fqn` is required; repeat `--fqn` to render multiple previews in a single build, or run [`android preview list`](https://developer.android.com/tools/agents/android-cli/commands/preview_list) to discover available previews.
- `-o, --output`: Directory or file path (`.png` or `.json`) where rendered preview outputs are written (defaults to a temporary directory).
- `--daemon`: Keeps the preview renderer running as a background daemon that shuts down after 10 minutes of inactivity, speeding up subsequent renders.
- `--component-tree`: Writes a companion JSON file containing the rendered component hierarchy, bounds, source locations, semantics, parameters, and modifiers.
- `--no-image`: Skips PNG image generation when only the `--component-tree` JSON output is needed.
- `-f, --format`: Selects `text` (default) or structured `json` output.

### Examples

Render a specific `@Preview` function in `:app` in the current Gradle workspace:

    android preview render :app --fqn=com.example.app.HomeScreenKt.HomeScreenPreview

Render multiple `@Preview` functions using the background daemon and export
their component trees:

    android preview render :app \
      --daemon \
      --component-tree \
      --fqn=com.example.app.HomeScreenKt.HomeScreenPreview \
      --fqn=com.example.app.SettingsScreenKt.SettingsPreview