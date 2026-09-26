---
title: https://developer.android.com/tools/agents/android-cli
url: https://developer.android.com/tools/agents/android-cli
source: md.txt
---

Android CLI is a command-line interface that lets you build for Android more
efficiently using any tool of your choice. It standardizes
core development competencies for agent-first workflows, providing an entry
point to the official tools, skills, and knowledge you need to develop more
effectively. It can also streamline CI, maintenance, and any other scripted
automation for the increasingly distributed nature of Android development.

For example, an agent or script can use the CLI to do tasks such as the
following:

- Automate environment and Android SDK setup
- Scaffold new projects from templates
- Manage virtual devices, install APKs, and inspect live device screens and UI hierarchies directly from your terminal
- Connect to running Android Studio instances for semantic code analysis, Compose preview rendering, and dependency version lookups
- Test your app with [Journeys](https://developer.android.com/tools/agents/android-cli/journeys)

Android CLI also gives your agents access to
[Android skills](https://developer.android.com/tools/agents/android-skills)
and the specialized [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) to help ensure that
your projects apply Android-recommended patterns and best practices.

For a complete description of Android CLI commands and options, see the
[Android CLI command reference](https://developer.android.com/tools/agents/android-cli/commands).

## Install Android CLI

To install Android CLI, follow these steps:

1. [Download Android CLI](https://developer.android.com/tools/agents).

2. To make sure you're using the latest version, update
   Android CLI:

       android update

   > [!TIP]
   > **Tip:** Run [`android update`](https://developer.android.com/tools/agents/android-cli/commands/update) regularly to keep up with the latest features.

To check if Android CLI is already installed on your machine, run
`which android` or `command -v android`: if it returns a path, then it's
installed.

### Set up for agents

To help agents understand and use Android CLI, run [`android init`](https://developer.android.com/tools/agents/android-cli/commands/init) to
install the `android-cli` skill.


## Android skills

[View on GitHub](https://github.com/android/skills/tree/main/devtools/android-cli)

### Android CLI

To install the Android CLI skill, run:

    android init

<br />

## Data collected

Android CLI collects data on basic usage of the tool. Here's the data that we
collect:

- Invocations of the `android` command and sub-commands, for example `android run` and `android create`.
- Names of non-positional arguments or options used, for example `--sdk` or `--version`.
- Positional arguments and flag values that map to a fixed, predefined set of system options managed by Android CLI. For example, we collect emulator template names such as `medium_phone` and `large_desktop`, and agent names such as `GEMINI`, `CLAUDE`, or `CODEX`.
- Stack traces and exception messages, where identifying information is anonymized before collection to help ensure privacy.

Here are some examples of data that we *don't* collect:

- We don't collect responses of the CLI when a command is run.
- We don't collect user-created inputs or external identifiers passed to the CLI, such as specific Maven coordinates, local file paths, or custom project names. For example, if the command `android create --name=com.company.internal.app` is executed, we record that `android create` was executed using the `--name` argument but we don't store the value `com.company.internal.app`.

To disable data collection, use the `--no-metrics` flag when running a
command with Android CLI.

## Feedback and issues

If you encounter any issues or want to provide feedback,
[report a bug](https://issuetracker.google.com/issues/new?component=2091212).

## Known issues

- The `android emulator` command for Windows is currently disabled.
- Downloading Android CLI from Windows PowerShell isn't currently supported.

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
[`android info`](https://developer.android.com/tools/agents/android-cli/commands/info).

**Example:** `android --sdk=<path/to/sdk> sdk list`

### `-v, --verbose`

**Usage:** `android -v <command>`

**Description:** Enable verbose output. Specify multiple `-v` options to
increase verbosity (for example, `-v`, `-vv`, or `-vvv`).

### `-V, --version`

**Usage:** `android -V`

**Description:** Print version information and exit.

## Commands

For a complete description of Android CLI commands and options, see the
[Android CLI command reference](https://developer.android.com/tools/agents/android-cli/commands).