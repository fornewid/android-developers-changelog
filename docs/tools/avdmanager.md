---
title: avdmanager  |  Android Studio  |  Android Developers
url: https://developer.android.com/tools/avdmanager
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [SDK tools guides](https://developer.android.com/tools)

# avdmanager Stay organized with collections Save and categorize content based on your preferences.




The `avdmanager` is a command-line tool that lets you create and manage
Android Virtual Devices (AVDs) from the command line. An AVD lets you define the
characteristics of an Android handset, Wear OS watch, or Android TV device
that you want to simulate in the Android Emulator.

If you're using Android Studio, then you don't need to use this tool and you
can instead
[create and manage AVDs from the IDE](/studio/run/managing-avds).

The `avdmanager` tool is included in the Android SDK Command-Line Tools package
at
`android_sdk/cmdline-tools/version/bin/avdmanager`.

## Syntax

To use `avdmanager`, use the following syntax:

```
avdmanager [global options] command [command options]
```

### Global options

**Table 1.** List of global options for
avdmanager.

| Global option | Description |
| --- | --- |
| `-s` | `--silent` | Silent mode: only errors are printed out. |
| `-h` | `--help` | Usage help. |
| `-v` | `--verbose` | Verbose mode: errors, warnings, and informational messages are printed. |
| `--clear cache` | Clear the SDK Manager repository manifest cache. |

### Commands and command options

**Table 2.** List of commands and options
for avdmanager.

| Command and options | Description |
| --- | --- |
| `create avd -n name -k "sdk_id" [-c {path|size}] [-f] [-p path]` | Create a new AVD. You must provide a name for the AVD and specify the ID of the SDK package to use for the AVD using sdk\_id wrapped in quotes. For example, the following command creates an AVD named `test` using the x86 system image for API level 25:     ``` avdmanager create avd -n test -k "system-images;android-25;google_apis;x86" ```  The following describes the usages for the other options:  * `-c {path|size}`: The path to the SD   card image for this AVD or the size of a new SD card image to create   for this AVD in KB or MB, denoted with `K` or   `M`. For example, `-c path/to/sdcard/` or   `-c 1000M`. * `-f`: Force creation of the AVD. Use this option if you   need to overwrite an existing AVD with a new AVD using the same name. * `-p path`: Path to the location where the   directory for this AVD's files will be created. If you don't specify   a path, the AVD is created in   `~/.android/avd/`. |
| `delete avd -n name` | Delete an AVD. You must specify the AVD with name. |
| `move avd -n name [-p path] [-r new-name]` | Move or rename an AVD. You must specify the AVD with name. The following describes the usages for the other options:  * `-p path`: The absolute path to the location at   which to create the directory where this AVD's files will be moved. If   you don't include this argument, the AVD won't be moved. You might   choose not to include this argument if you want to rename the AVD in   place. * `-r new-name`: The new name of the AVD being   renamed. |
| `list [target|device|avd] [-c]` | List all available targets, device definitions, or AVDs. If you don't specify `target`, `device`, or `avd`, `avdmanager` lists all three. Include the `-c` argument to receive a compact output suitable for scripts. The `-c` argument is not available when listing all three options together. |