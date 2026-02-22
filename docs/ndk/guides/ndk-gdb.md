---
title: https://developer.android.com/ndk/guides/ndk-gdb
url: https://developer.android.com/ndk/guides/ndk-gdb
source: md.txt
---

# ndk-gdb

The NDK includes a shell script named`ndk-gdb`to start a command-line native debugging session (historically gdb but now lldb). Users who prefer to use a GUI should read the documentation for[debugging in Android Studio](https://developer.android.com/studio/debug)instead.

## Requirements

For command-line native debugging to work, these requirements must be met:

- Build your app using the`ndk-build`script. The`ndk-gdb`script does not support using the legacy`make APP=<name>`method to build.
- Enable app debugging in your`AndroidManifest.xml`file by including an`<application>`element that sets the`android:debuggable`attribute to`true`.
- Build your app to run on Android 2.2 (Android API level 8) or higher.
- Debug on a device or emulator running Android 2.2 or higher. For debugging purposes, the target API level that you declare in your`AndroidManifest.xml`file does not matter.
- Develop your app in a Unix shell. On Windows, use[Cygwin](https://www.cygwin.com/)or the experimental`ndk-gdb-py`[Python](https://www.python.org/)implementation.
- Use GNU Make 3.81 or higher.

## Usage

To invoke the`ndk-gdb`script, change into the application directory or any directory under it. For example:  

```
cd $PROJECT
$NDK/ndk-gdb
```

Here,`$PROJECT`points to your project's root directory, and`$NDK`points to your NDK installation path.

When you invoke`ndk-gdb`, it configures the session to look for your source files and symbol/debug versions of your generated native libraries. On successfully attaching to your application process,`ndk-gdb`outputs a long series of error messages, noting that it cannot find various system libraries. This is normal, because your host machine does not contain symbol/debug versions of these libraries on your target device. You can safely ignore these messages.

Next,`ndk-gdb`displays the usual lldb prompt.

You interact with`ndk-gdb`in the same way as you would with lldb. See the helpful \[GDB to LLDB command map\](https://lldb.llvm.org/use/map.html) if you're unfamiliar with lldb but know gdb.

`ndk-gdb`handles many error conditions, and displays an informative error message if it finds a problem. these checks include making sure that the following conditions are satisfied:

- Checks that ADB is in your path.
- Checks that your application is declared debuggable in its manifest.
- Checks that, on the device, the installed application with the same package name is also debuggable.

By default,`ndk-gdb`searches for an already-running application process, and displays an error if it doesn't find one. You can, however, use the`--start`or`--launch=<name>`option to automatically start your activity before the debugging session. For more information, see[Options](https://developer.android.com/ndk/guides/ndk-gdb#opt).

### Options

To see a complete list of options, type`ndk-gdb --help`on the command line. Table 1 shows a number of the more commonly used ones, along with brief descriptions.

**Table 1.**Common ndk-gdb options and their descriptions.

Starting`ndk-gdb`with this option specified launches the first launchable activity listed in your application manifest. Use`--launch=<name>`to start the next launchable activity. To dump the list of launchable activities, run`--launch-list`from the command line.

|             Option              |                                                                                                                                                                                                                                                                          Description\>                                                                                                                                                                                                                                                                          |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--verbose`                     | This option tells the build system to print verbose information about the native-debugging session setup. It is necessary only for debugging problems when the debugger can't connect to the app, and the error messages that`ndk-gdb`displays are not enough.                                                                                                                                                                                                                                                                                                  |
| `--force`                       | By default,`ndk-gdb`aborts if it finds that another native debugging session is already running on the same device. This option kills the other session, and replaces it with a new one. Note that this option does not kill the actual app being debugged, which you must kill separately.                                                                                                                                                                                                                                                                     |
| `--start`                       | When you start`ndk-gdb`, it tries by default to attach to an existing running instance of your app on the target device. You can override this default behavior by using`--start`to explicitly launch the application on the target device before the debugging session.                                                                                                                                                                                                                                                                                        |
| `--launch=<name>`               | This option is similar to`--start`, except that it allows you to start a specific activity from your application. This feature is only useful if your manifest defines multiple launchable activities.                                                                                                                                                                                                                                                                                                                                                          |
| `--launch-list`                 | This convenience option prints the list of all launchable activity names found in your app manifest.`--start`uses the first activity name.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `--project=<path>`              | This option specifies the app project directory. It is useful if you want to launch the script without first having to change to the project directory.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--port=<port>`                 | By default,`ndk-gdb`uses local TCP port 5039 to communicate with the app it is debugging on the target device. Using a different port allows you to natively debug programs running on different devices or emulators connected to the same host machine.                                                                                                                                                                                                                                                                                                       |
| `--adb=<file>`                  | This option specifies the[adb](https://developer.android.com/tools/help/adb)tool executable. It is only necessary if you have not set your path to include that executable.                                                                                                                                                                                                                                                                                                                                                                                     |
| - `-d` - `-e` - `-s <serial>`   | These flags are similar to the adb commands with the same names. Set these flags if you have several devices or emulators connected to your host machine. Their meanings are as follows: `-d` :   Connect to a single physical device. `-e` :   Connect to a single emulator device. `-s <serial>` :   Connect to a specific device or emulator. Here,`<serial>`is the device's name as listed by the`adb devices`command. Alternatively, you can define the`ADB_SERIAL`environment variable to list a specific device, without the need for a specific option. |
| - `--exec=<file>` - `-x <file>` | This option tells`ndk-gdb`to run the debugger initialization commands found in`<file>`after connecting to the process it is debugging. This is a useful feature if you want to do something repeatedly, such as setting up a list of breakpoints, and then resuming execution automatically.                                                                                                                                                                                                                                                                    |
| `--nowait`                      | Disable pausing the Java code until the debugger connects. Passing this option may cause the debugger to miss early breakpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--tui``-t`                     | Enable Text User Interface if it is available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--gnumake-flag=<flag>`         | This option is an extra flag (or flags) to pass to the`ndk-build`system when querying it for project information. You can use multiple instances of this option in the same command.                                                                                                                                                                                                                                                                                                                                                                            |

**Note:** The final three options in this table are only for the Python version of`ndk-gdb`.