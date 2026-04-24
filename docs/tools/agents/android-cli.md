---
title: https://developer.android.com/tools/agents/android-cli
url: https://developer.android.com/tools/agents/android-cli
source: md.txt
---

Android CLI is a command-line interface that enables you to more easily and
efficiently build for Android using any tool of your choice. It standardizes
core development competencies for agent-first workflows, providing an entry
point to the official tools, skills, and knowledge you need to develop more
effectively. It can also streamline CI, maintenance, and any other scripted
automation for the increasingly distributed nature of Android development.

For example, an agent or script can use the CLI to automate environment setup,
scaffold new projects from templates, and manage virtual devices directly from
your terminal. It also gives your agents access to [Android skills](https://developer.android.com/tools/agents/android-skills)
and the specialized [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) to help ensure that your
projects apply Android-recommended patterns and best practices.

## Install Android CLI

To install Android CLI, follow these steps:

1. [Download Android CLI](https://developer.android.com/tools/agents).

2. To make sure you're using the latest version, update
   Android CLI:

       android update

   > [!TIP]
   > **Tip:** Run [`android update`](https://developer.android.com/tools/agents/android-cli#update) regularly to keep up with the latest features.

To check if Android CLI is already installed on your machine, run
`which android` or `command -v android`: if it returns a path, then it's
installed.

### Set up for agents

To help agents understand and use Android CLI, run `init` to install the
`android-cli` skill:

    android init

## Known issues

- The `android emulator` command for Windows is currently disabled.

If you encounter any issues or wish to provide feedback, please
[report a bug](https://issuetracker.google.com/issues/new?component=2091212).

## Configure Android CLI

Create a `.androidrc` file to automatically apply flags and options
every time you invoke Android CLI. Save the file in the following
location, depending on your operating system:

- **macOS and Linux** : `~/.androidrc`
- **Windows** : `%USERPROFILE%\.androidrc`

Add the flags you want to apply automatically to the file, one per line.

For example, to make Android CLI use a specific Android SDK by default
every time, add the [`--sdk`](https://developer.android.com/tools/agents/android-cli#sdk) flag to your file:

    --sdk=<path-to-sdk>

## Global options

These are optional flags that you can use with other Android CLI commands.

### `-h, --help`

**Usage:** `android <command> -h`

**Description:** Display the help manual for the tool or specific command in
question.

**Examples:**

- `android -h`
- `android create -h`

### `--sdk`

**Usage:** `android --sdk=<path-to-sdk> <command>`

**Description:** The path to the Android SDK that you want to use for the
command that follows. You can use the `--sdk` setting to temporarily override
the default Android SDK instead of changing your
[global environment variables](https://developer.android.com/tools/variables#envar) every time you want to
switch. To check which Android SDK you're using by default, run
[`android info`](https://developer.android.com/tools/agents/android-cli#info).

**Example:** `android --sdk=<path/to/sdk> sdk list`

## Commands

This section lists all the Android CLI commands and describes what they do.
All of these commands should be preceded by `android`, for example
`android create`, `android run`, and so on. Optional modifiers are enclosed
in brackets `[]` and mandatory arguments are not.

### `create`

**Usage:** `android create [--dry-run] [--verbose] [--name=<application-name>] [--output=<dest-path>] [<template-name>]`

**Description:** Initialize a new project from a template. To see the template
options, run `android create -h`.

**Arguments (mandatory):**

- `-o, --output` - The destination project directory path.

**Options:**

- `--dry-run` - Simulates the entire project creation process without actually saving any files. For example, you can do a dry run to see what the different templates do before committing to one.
- `--verbose` - Enables verbose output, including information such as which files are being copied from the template.
- `--name=<application-name>` - The name of the project directory. If omitted, the output directory is used.
- `<template-name>` - The name of the template to create a new project from. If omitted, `empty-activity-agp-9` is used.

**Example:** `android create --dry-run --verbose empty-activity-agp-9`

### `create list`

**Usage:** `android create list`

**Description:** List all the available templates to create a new project from.

### `describe`

**Usage:** `android describe [--project_dir=<project-directory>]`

**Description:** Analyzes an Android project to generate descriptive metadata.
This command identifies and outputs the paths to JSON files that detail the
project's structure, including build targets and their corresponding output
artifact locations (for example, APK files). This information enables
other tools and commands to locate build artifacts efficiently.

**Options:**

- `--project_dir` - The project directory to describe. If omitted, the current directory is used.

**Example:** `android describe --project_dir=/path/to/your/project`

### `docs`

**Usage:**

- `android docs search <query>`
- `android docs fetch <kb-url>`

**Description:** The `android docs` command is a two-step process for
accessing the [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) directly from the CLI.
First, search for documentation related to your query using the `search`
command. The search results will include special URLs starting with `kb://`,
which you can then use with the `fetch` command to output the documentation
commands to the terminal.

**Examples:**

- `android docs search 'How do I improve my app performance?'`
- `android docs fetch kb://android/topic/performance/overview`

### `emulator create`

**Usage:** `android emulator create [--list-profiles] [--profile=<profile-name>]`

**Description:** Create a virtual device.

**Options:**

- `--list-profiles` - List the device profiles that can be used to create a device.
- `--profile=<profile-name>` - Create a device with the specified profile. If this is omitted, the `medium_phone` profile will be created.

### `emulator list`

**Usage:** `android emulator list`

**Description:** List the available virtual devices.

### `emulator start`

**Usage:** `android emulator start <device-name>`

**Description:** Launch the specified virtual device.

**Arguments (mandatory):**

- `<device-name>` - The device name to start (for example, `medium_phone`). Use `android emulator list` to see the available devices.

**Example:** `android emulator start medium_phone`

### `emulator stop`

**Usage:** `android emulator stop <device-serial-number>`

**Description:** Stop the specified virtual device.

**Arguments (mandatory):**

- `<device-serial-number>` - The device serial number to stop.

**Example:** `android emulator stop emulator-5554`

### `info`

**Usage:** `android info`

**Description:** Display the path to the default Android SDK used. To change
the Android SDK used, use [`--sdk`](https://developer.android.com/tools/agents/android-cli#sdk).

### `init`

**Usage:** `android init`

**Description:** Set up your environment for agents by installing the
`android-cli` skill.

### `layout`

**Usage:** `android layout [--pretty] [--output] [--diff]`

**Description:** Returns the UI layout of the active Android app (connected
through a physical device or emulator) in JSON format.

**Options:**

- `-p, --pretty` - Formats the JSON output with indentation and line breaks for human readability.
- `-o, --output` - Specifies a file location to save the layout tree. If omitted, the JSON is printed directly to stdout.
- `-d, --diff` - Returns a list of only the layout elements that have changed since the last internal snapshot was taken (the last time layout was run), instead of the full layout tree.

**Example:** : `android layout --output=./hierarchy.json`

### `skills add`

Android skills are special instructions designed to help agents better
understand and execute specific patterns that follow best practices and
guidance on Android development. To learn more, see
[Intro to Android skills](https://developer.android.com/tools/agents/android-skills).

**Usage:** `android skills add [--all] [--agent=<agent-name>] [--skill=<skill-name>]`

**Description:** Install Android skills to the skills directories for all
detected agents. If you don't have any existing agent directories and don't
specify particular agents, the skills will be installed for Gemini and
Antigravity at `~/.gemini/antigravity/skills`.

**Options:**

- `--all` - Add all the Android skills at once. If omitted (and `--skill` isn't specified), only the `android-cli` skill will be installed.
- `--agent` - A comma-separated list of agents to install the skill for. If omitted, the skill will be installed for all detected agents.
- `--skill` - The skill name that you want to install. If omitted (and `--all` isn't specified), only the `android-cli` skill will be installed.

**Example:** `android skills add --agent='gemini' edge-to-edge`

### `skills find`

**Usage:** `android skills find <string>`

**Description:** Find skills that match a given string.

**Arguments (mandatory):**

- `string` - String that matches a skill description.

**Example:** `android skills find 'performance'`

### `skills list`

**Usage:** `android skills list [--long]`

**Description:** List the available skills.

**Options:**

- `--long` - Output additional information for each skill, including the description of the skill and which agents it's already installed for.

### `skills remove`

**Usage:** `android skills remove [--agent] --skill=<skill-name>`

**Description:** Remove a skill. If you don't specify particular agents, the
skill will be removed for all agents.

**Arguments (mandatory):**

- `--skill` - The name of the skill to remove.

**Options:**

- `--agent` - A comma-separated list of agents to remove the skill from. If omitted, the skill will be removed for all agents.

**Example:** `android skills remove --agent='gemini' --skill=edge-to-edge`

### `screen capture`

**Usage:** `android screen capture [--output] [--annotate]`

**Description:** Captures a screenshot of the connected device.

**Options:**

- `-o, --output` - Specifies a file location to save the screenshot. If omitted, the raw PNG data will be printed directly to stdout.
- `-a, --annotate` - Draws labeled bounding boxes around all the UI elements detected on the image, to use with the `resolve` command.

**Example:** `android screen capture --output=ui.png`

### `screen resolve`

**Usage:** `android screen resolve --screenshot=<path> --string=<string>`

**Description:** Translates the visual labels from an annotated screenshot,
captured using `screen capture`, into actual screen coordinates (x, y).
Useful for scripting clicks on elements without having to manually calculate
their positions.

**Flags:**

- `--screenshot` - The path to the annotated screenshot.
- `--string` - A string that includes at least one placeholder corresponding to a UI element label in the format `#<number>`. The `#<number>` part will be replaced by the screen coordinates.

**Example:**

If the label 5 is at coordinates (500, 1000), then the command

    android screen resolve --screenshot=ui.png --string="input tap #5"

returns the output

    input tap 500 1000

### `sdk install`

**Usage:** `android sdk install <package[@version]> [--beta] [--canary] [--force]`

**Description:** Install the specified SDK package(s).

**Arguments (mandatory):**

- `package[@version]` - A space-separated list of packages to install. If a version isn't specified, the latest version of the package in the channel (by default the stable channel) is installed.

**Options:**

- `--beta` - Include beta packages.
- `--canary` - Include canary packages.
- `--force` - Force downgrading to an older version.

**Examples:**

- `android sdk install platforms/android-34 build-tools/34.0.0` - Install the latest versions of the Android SDK Platform 34 and SDK Built Tools 34.0.0 packages from the stable channel.
- `android sdk install platforms/android-34@2` - Install version 2 of the Android SDK Platform 34 package.
- `android sdk install --canary system-images/android-35/google_apis/x86_6` - Install the latest version of the Android 35 system image from the canary channel.
- `android sdk install --force platforms/android-33@1` - Revert to version 1 of the Android SDK Platform 33 package from the stable channel.

### `sdk list`

**Usage:** `android sdk list <package-pattern>`

**Description:** List the installed and available SDK packages.

**Arguments (mandatory):**

- `<package-pattern>` - Filter packages by pattern. Supports regular expressions.

**Options:**

- `--all` - Show all installed and available packages.
- `--all-versions` - Show all versions for each package.
- `--beta` - Include beta packages.
- `--canary` - Include canary packages.

### `sdk remove`

**Usage:** `android sdk remove <package-name>`

**Description:** Remove a package from the SDK.

**Arguments (mandatory):**

- `<package-name>` - The name of the package to remove.

**Example:** `android sdk remove build-tools/36.1.0`

### `run`

**Usage:** `android run [--debug] [--activity=<activity-name>] [--device=<serial-number>] [--type=<param>] --apks=<apk-paths>`

**Description:** Deploy an Android app to a connected device or emulator. It
doesn't perform any build steps; you must provide the path(s) to the APK
files that you want to install.

**Arguments (mandatory):**

- `--apks` - A comma-separated list of path(s) to the APK files that you want to install. The path is relative to where you currently are in the file system.

**Options:**

- `--activity` - The name of the [activity](https://developer.android.com/guide/components/activities/intro-activities) to launch once the APK is installed. If there are multiple activities, you must specify one activity to launch initially.
- `--debug` - Deploys the app in [debug mode](https://developer.android.com/studio/debug). After running the app in debug mode, you must [connect your debugger](https://developer.android.com/studio/debug#attach-debugger) from an IDE, such as Android Studio, or a command-line tool to start debugging.
- `--device` - The serial number of the target device or emulator. Only needed if multiple devices are connected. To find the device serial numbers, run `adb devices`.
- `--type` - The [component type](https://developer.android.com/guide/topics/manifest/manifest-intro#components) to start. Use this if you'd like to start a background service directly instead of a UI activity. Types supported:
  - `ACTIVITY`
  - `WATCH_FACE`
  - `TILE`
  - `COMPLICATION`
  - `DECLARATIVE_WATCH_FACE`

**Examples:**

- `android run --apks=app/build/outputs/apk/debug/app-debug.apk` - Deploys a single APK to the default device.
- `android run --apks=base.apk,density-hdpi.apk,lang-en.apk` - Deploys multiple APKs to the default device.
- `android run --apks=app-debug.apk --type=SERVICE --activity=.sync.DataSyncService` - Test a service without an activity.
- `android run --apks=app-debug.apk --device=emulator-5554` - Deploys the APK to a specific device.

### `sdk update`

**Usage:** `android sdk update [--beta] [--canary] [<package-name>]`

**Description:** Update one or all packages to the latest version in the
channel (by default the stable channel). If you don't specify a package, all
packages will be updated.

**Options:**

- `<package-name>` - The name of the package to update.
- `--beta` - Include beta packages.
- `--canary` - Include canary packages.
- `--force` - Force downgrading to an older version.

**Examples:**

- `android sdk update` - Check for and install updates for everything in your SDK.
- `android sdk update build-tools/34.0.0` - Update the Android SDK Build Tools 34.0.0 package to the latest version in the stable channel.
- `android sdk update --canary platforms/android-35` - Update the Android SDK Platforms 35 package to the latest version in the canary channel.

### `update`

**Usage:** `android update`

**Description:** Update the Android CLI.

### `-V, --version`

**Description:** Show the current version of the Android CLI.