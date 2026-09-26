---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_render-compose-preview
url: https://developer.android.com/tools/agents/android-cli/commands/studio_render-compose-preview
source: md.txt
---

Renders a Compose preview in Android Studio.

## Usage

    android studio render-compose-preview [-h] [--output-image-file=PARAM] [--pid=PARAM] [--print-semantics] [--project=PARAM] <path> <composable>

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--output-image-file=PARAM` - The filename to write the resulting image to.
- `--pid=PARAM` - The PID of the Android Studio instance to connect to.
- `--print-semantics` - If `true`, prints out the semantics tree.
- `--project=PARAM` - The name or path of the project open in Android Studio to query. Use [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) to get the names of available projects.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<path>` - The path of the file containing the Compose preview, relative to the current directory or absolute.
- `<composable>` - The name of the composable.

## Description

`android studio render-compose-preview` renders a Jetpack Compose `@Preview` function using Android Studio's layout rendering engine and optionally prints its accessibility semantics tree.

Requires Android Studio Quail 2 or higher.

### Configure preview output (`--output-image-file` and `--print-semantics`)

- `--output-image-file`: Saves the rendered PNG preview to the specified file path. If omitted, a temporary PNG file is created.
- `--print-semantics`: Prints the Compose preview's accessibility semantics tree in JSON format so AI agents can inspect interactive nodes, text, and bounds alongside the rendered visual image.

### Examples

Render `HotelDetailScreenPreview` to `preview_hotel.png` and print its semantics tree:

    android studio render-compose-preview \
      --output-image-file=preview_hotel.png \
      --print-semantics \
      app/src/main/java/com/example/myapp/ui/DetailScreen.kt \
      HotelDetailScreenPreview