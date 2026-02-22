---
title: https://developer.android.com/studio/tools/help/android
url: https://developer.android.com/studio/tools/help/android
source: md.txt
---

# android

This tool is no longer supported. Use Android Studio to[create AVDs](https://developer.android.com/studio/run/managing-avds)and[create projects](https://developer.android.com/studio/projects/create-project), and use[`sdkmanager`](https://developer.android.com/studio/intro/update#sdk-manager)to view and install SDK packages.

`android`is a command-line tool located in the`tools/`directory of the Android SDK.`android`lets you:

- Create, delete, and view Android Virtual Devices (AVDs). (Now done using Android Studio or, from the command line,[avdmanager](https://developer.android.com/studio/command-line/avdmanager).)
- Create and update Android projects. (Now done using Android Studio.)
- Update your Android SDK with new platforms, add-ons, and documentation. (Now done using the command-line tool[sdkmanager](https://developer.android.com/studio/command-line/sdkmanager).)

If you are using Android Studio, the`android`tool's features are integrated into the IDE, so you don't need to use this tool directly.

**Note:** The documentation of options below is not exhaustive and may be out of date. For the most current list of options, execute`android
--help`.

## Syntax

The syntax for`android`is as follows:  

```
android [global options] action [action options]
```

### Global options

`-s`
:   Silent mode: only errors are printed.

`-h`
:   Usage help.

`-v`
:   Verbose mode: errors, warnings and informational messages are printed.

### AVD actions and options

The following table lists actions and options for AVDs:

|    Action    |            Option            |                                                                                                               Description                                                                                                                | Comments |
|--------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `avd`        | None                         | Launch the AVD Manager.                                                                                                                                                                                                                  |          |
| `sdk`        | None                         | Launch the Android SDK Manager.                                                                                                                                                                                                          |          |
| `create avd` | `-n <name>`                  | The name for the AVD.                                                                                                                                                                                                                    | Required |
| `create avd` | `-t <targetID>`              | Target ID of the system image to use with the new AVD. To obtain a list of available targets, use`android list targets`.                                                                                                                 | Required |
| `create avd` | `-c <path>|<size>[K|M]`      | The path to the SD card image to use with this AVD or the size of a new SD card image to create for this AVD. For example,`-c path/to/sdcard`or`-c 1000M`.                                                                               |          |
| `create avd` | `-f`                         | Force creation of the AVD.                                                                                                                                                                                                               |          |
| `create avd` | `-p <path>`                  | Path to the location to create the directory for this AVD's files.                                                                                                                                                                       |          |
| `create avd` | `-s <name>|<width>-<height>` | The skin to use for this AVD, identified by name or dimensions. The`android`tool scans for a matching skin by name or dimension in the`skins/`directory of the target referenced in the`-t <targetID>`argument. For example,`-s HVGA-L`. |          |
| `delete avd` | `-n <name>`                  | The name of the AVD to delete.                                                                                                                                                                                                           | Required |
| `move avd`   | `-n <name>`                  | The name of the AVD to move.                                                                                                                                                                                                             | Required |
| `move avd`   | `-p <path>`                  | Path to the location to create the directory for this AVD's files.                                                                                                                                                                       |          |
| `move avd`   | `-r <new-name>`              | New name of the AVD being renamed.                                                                                                                                                                                                       |          |
| `update avd` | `-n <name>`                  | The name of the AVD to move.                                                                                                                                                                                                             | Required |

### Project actions and options

The following table lists actions and options for projects:

|         Action          |         Option          |                                                       Description                                                        | Comments |
|-------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|----------|
| `create project`        | `-n <name>`             | The name for the project.                                                                                                | Required |
| `create project`        | `-t <targetID>`         | Target ID of the system image to use with the new AVD. To obtain a list of available targets, use`android list targets`. | Required |
| `create project`        | `-k <path>|<size>[K|M]` | Package namespace.                                                                                                       | Required |
| `create project`        | `-a`                    | Name for the default`Activity`class.                                                                                     | Required |
| `create project`        | `-p <path>`             | Location of the project directory.                                                                                       | Required |
| `update project`        | `-n <name>`             | The name of the project to update.                                                                                       |          |
| `update project`        | `-p <path>`             | Location path of the project.                                                                                            | Required |
| `update project`        | `-l <library path>`     | Location path of an Android Library to add, relative to the main project.                                                |          |
| `update project`        | `-s <subprojects>`      | Update any projects in subfolders, such as test projects.                                                                |          |
| `update project`        | `-t <targetID>`         | Target ID to set for the project.                                                                                        |          |
| `create test-project`   | `-n <name>`             | The name of the project.                                                                                                 |          |
| `create test-project`   | `-p <path>`             | Location path of the project.                                                                                            | Required |
| `create test-project`   | `-m <main>`             | The name of the project.                                                                                                 | Required |
| `update test-project`   | `-p <path>`             | Location path of the project to test, relative to the new project.                                                       | Required |
| `update test-project`   | `-m <main>`             | The main class of the project to test.                                                                                   | Required |
| `create lib-project`    | `-k <packageName>`      | Package name of the library project.                                                                                     | Required |
| `create lib-project`    | `-p <path>`             | Location path of the project.                                                                                            | Required |
| `create lib-project`    | `-t <targetID>`         | Target ID of the library project.                                                                                        | Required |
| `create lib-project`    | `-n <name>`             | The name of the project.                                                                                                 | Required |
| `update lib-project`    | `-p <path>`             | Location path of the project.                                                                                            | Required |
| `update lib-project`    | `-l <libraryPath>`      | Location path of an Android Library to add, relative to the main project.                                                |          |
| `update lib-project`    | `-t <name>`             | Target ID of the library project.                                                                                        |          |
| `create uitest-project` | `-n <name>`             | The name of the UI test project.                                                                                         |          |
| `create uitest-project` | `-t <name>`             | Target ID of the UI test project.                                                                                        | Required |
| `create uitest-project` | `-p <path>`             | Location path of the UI test project.                                                                                    | Required |

### Update actions

`update adb`
:   Updates adb to support the USB devices declared in the SDK add-ons.

`update sdk`
:   Updates the SDK by suggesting new platforms to install if available.