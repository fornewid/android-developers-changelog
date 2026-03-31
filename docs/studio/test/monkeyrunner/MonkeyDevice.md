---
title: MonkeyDevice  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/test/monkeyrunner/MonkeyDevice
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Studio](https://developer.android.com/studio)

# MonkeyDevice Stay organized with collections Save and categorize content based on your preferences.



A monkeyrunner class that represents a device or emulator accessible by the workstation running
`monkeyrunner`.

This class is used to control an Android device or emulator. The methods send UI events,
retrieve information, install and remove applications, and run applications.

You normally do not have to create an instance of `MonkeyDevice`. Instead, you
use
`MonkeyRunner.waitForConnection()` to create a new object from a connection to a device or
emulator. For example, instead of
using:

```
newdevice = MonkeyDevice()
```

you would use:

```
newdevice = MonkeyRunner.waitForConnection()
```

## Summary

| Constants | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *string* | [DOWN](#ACTION_DOWN) | Use this with the `type` argument of `press()` or `touch()` to send a DOWN event. |
| *string* | [UP](#ACTION_UP) | Use this with the `type` argument of `press()` or `touch()` to send an UP event. |
| *string* | [DOWN\_AND\_UP](#ACTION_DOWN_AND_UP) | Use this with the `type` argument of `press()` or `touch()` to send a DOWN event immediately followed by an UP event. |

| Methods | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| void | [broadcastIntent](#broadcastIntent) (*string* uri, *string* action, *string* data, *string* mimetype, *iterable* categories *dictionary* extras, *component* component, *iterable* flags)  Broadcasts an Intent to this device, as if the Intent were coming from an application. |
| void | [drag](#drag) (*tuple* start, *tuple* end, *float* duration, *integer* steps)  Simulates a drag gesture (touch, hold, and move) on this device's screen. |
| *object* | [getProperty](#getProperty) (*string* key)  Given the name of a system environment variable, returns its value for this device. The available variable names are listed in the [detailed description](#getProperty) of this method. |
| *object* | [getSystemProperty](#getSystemProperty) (*string* key)  . The API equivalent of `adb shell getprop <key>. This is provided for use by platform developers.` |
| void | [installPackage](#installPackage) (*string* path)  Installs the Android application or test package contained in packageFile onto this device. If the application or test package is already installed, it is replaced. |
| *dictionary* | [instrument](#instrument) (*string* className, *dictionary* args)  Runs the specified component under Android instrumentation, and returns the results in a dictionary whose exact format is dictated by the component being run. The component must already be present on this device. |
| void | [press](#press) (*string* name, *dictionary* type)  Sends the key event specified by type to the key specified by keycode. |
| void | [reboot](#reboot) (*string* into)  Reboots this device into the bootloader specified by bootloadType. |
| void | [removePackage](#removePackage) (*string* package)  Deletes the specified package from this device, including its data and cache. |
| *object* | [shell](#shell) (*string* cmd)  Executes an `adb` shell command and returns the result, if any. |
| void | [startActivity](#startActivity) (*string* uri, *string* action, *string* data, *string* mimetype, *iterable* categories *dictionary* extras, *component* component, *flags*)  Starts an Activity on this device by sending an Intent constructed from the supplied arguments. |
| `MonkeyImage` | [takeSnapshot](#takeSnapshot)()  Captures the entire screen buffer of this device, yielding a `MonkeyImage` object containing a screen capture of the current display. |
| void | [touch](#touch) (*integer* x, *integer* y, *integer* type)  Sends a touch event specified by type to the screen location specified by x and y. |
| void | [type](#touch) (*string* message)  Sends the characters contained in message to this device, as if they had been typed on the device's keyboard. This is equivalent to calling `press()` for each keycode in `message` using the key event type `DOWN_AND_UP`. |
| void | [wake](#touch) ()  Wakes the screen of this device. |

## Constants

#### *string* DOWN

`press()` or
`touch()` value.
Specifies that a DOWN event type should be sent to the device, corresponding to
pressing down on a key or touching the screen.

#### *string* UP

`press()` or
`touch()` value.
Specifies that an UP event type should be sent to the device, corresponding to
releasing a key or lifting up from the screen.

#### *string* DOWN\_AND\_UP

`press()`,
`touch()` or
`type()` value.
Specifies that a DOWN event type followed by an UP event type should be sent to the
device, corresponding to typing a key or clicking the screen.



## Public methods

#### void broadcastIntent ( *string* uri, *string* action, *string* data, *string* mimetype, *iterable* categories *dictionary* extras, *component* component, *iterable* flags)

Broadcasts an Intent to this device, as if the Intent were coming from an
application. See `Intent` for more information about the
arguments.

##### Arguments

|  |  |
| --- | --- |
| uri | The URI for the Intent. (see `Intent.setData()`). |
| action | The action for this Intent (see `Intent.setAction()`). |
| data | The data URI for this Intent (see `Intent.setData()`). |
| mimetype | The MIME type for the Intent (see `Intent.setType()`). |
| categories | An iterable data structure containing strings that define categories for this Intent (see `Intent.addCategory()`). |
| extras | A dictionary of extra data for this Intent (see `Intent.putExtra()` for an example). The key for each dictionary item should be a *string*. The item's value can be any simple or structured data type. |
| component | The component for this Intent (see `ComponentName`). Using this argument will direct the Intent to a specific class within a specific Android package. |
| flags | An iterable data structure containing flags that control how the Intent is handled (see `Intent.setFlags()`). |

#### void drag ( *tuple* start, *tuple* end, *float* duration, *integer* steps)

Simulates a drag gesture (touch, hold, and move) on this device's screen.

##### Arguments

|  |  |
| --- | --- |
| start | The starting point of the drag gesture, in the form of a *tuple* (x,y) where x and y are *integers*. |
| end | The end point of the drag gesture, in the form of a *tuple* (x,y) where x and y are *integers*. |
| duration | The duration of the drag gesture in seconds. The default is 1.0 seconds. |
| steps | The number of steps to take when interpolating points. The default is 10. |

#### *object* getProperty (*string* key)

Given the name of a system environment variable, returns its value for this device.

##### Arguments

|  |  |
| --- | --- |
| key | The name of the system environment variable. The available variable names are listed in [Table 1. Property variable names](#table1) at the end of this topic. |

##### Returns

* The value of the variable. The data format varies according to the variable requested.

#### *object* getSystemProperty (*string* key)

Synonym for `getProperty()`.

##### Arguments

|  |  |
| --- | --- |
| key | The name of the system environment variable. The available variable names are listed in [Table 1. Property Variable Names](#table1). |

##### Returns

* The value of the variable. The data format varies according to the variable requested.

#### void installPackage (*string* path)

Installs the Android application or test package contained in packageFile
onto this device. If the application or test package is already installed, it is
replaced.

##### Arguments

|  |  |
| --- | --- |
| path | The fully-qualified path and filename of the `.apk` file to install. |

#### *dictionary* instrument ( *string* className, *dictionary* args)

Runs the specified component with Android instrumentation, and returns the results
in a dictionary whose exact format is dictated by the component being run. The
component must already be present on this device.

Use this method to start a test case that uses one of Android's test case classes.
See [Testing
Fundamentals](/tools/testing/testing_android) to learn more about unit testing with the Android testing
framework.

##### Arguments

|  |  |
| --- | --- |
| className | The name of an Android component that is already installed on this device, in the standard form packagename/classname, where packagename is the Android package name of a `.apk` file on this device, and classname is the class name of an Android component (Activity, ContentProvider, Service, or BroadcastReceiver) in that file. Both packagename and classname must be fully qualified. See `ComponentName` for more details. |
| args | A dictionary containing flags and their values. These are passed to the component as it is started. If the flag does not take a value, set its dictionary value to an empty string. |

##### Returns

* A dictionary containing the component's output. The contents of the dictionary
  are defined by the component itself.

  If you use `InstrumentationTestRunner` as the class name in
  the componentName argument, then the result dictionary contains
  the single key "stream". The value of "stream" is a *string* containing
  the test output, as if `InstrumentationTestRunner` was run from the
  command line. The format of this output is described in
  [Testing in Other IDEs](/tools/testing/testing_otheride).

#### void press (*string* name, *integer* type)

Sends the key event specified by `type` to the key specified by
`keycode`.

##### Arguments

|  |  |
| --- | --- |
| name | The name of the keycode to send. See `KeyEvent` for a list of keycode names. Use the keycode name, not its integer value. |
| type | The type of key event to send. The allowed values are `DOWN`, `UP`, and `DOWN_AND_UP`. |

#### void reboot (*string* bootloadType)

Reboots this device into the bootloader specified by `bootloadType`.

##### Arguments

|  |  |
| --- | --- |
| into | The type of bootloader to reboot into. The allowed values are "bootloader", "recovery", or "None". |

#### void removePackage (*string* package)

Deletes the specified package from this device, including its data and cache.

##### Arguments

|  |  |
| --- | --- |
| package | The Android package name of an `.apk` file on this device. |

#### *object* shell (*string* cmd)

Executes an `adb` shell command and returns the result, if any.

##### Arguments

|  |  |
| --- | --- |
| cmd | The command to execute in the `adb` shell. The form of these commands is described in the topic [Android Debug Bridge](/tools/help/adb). |

##### Returns

* The results of the command, if any. The format of the results is determined by the
  command.

#### void startActivity ( *string* uri, *string* action, *string* data, *string* mimetype, *iterable* categories *dictionary* extras, *component* component, *iterable* flags)

Starts an Activity on this device by sending an Intent constructed from the
supplied arguments.

##### Arguments

|  |  |
| --- | --- |
| uri | The URI for the Intent. (see `Intent.setData()`). |
| action | The action for the Intent (see `Intent.setAction()`). |
| data | The data URI for the Intent (see `Intent.setData()`). |
| mimetype | The MIME type for the Intent (see `Intent.setType()`). |
| categories | An iterable data structure containing strings that define categories for the Intent (see `Intent.addCategory()`). |
| extras | A dictionary of extra data for the Intent (see `Intent.putExtra()` for an example). The key for each dictionary item should be a *string*. The item's value can be any simple or structured data type. |
| component | The component for the Intent (see `ComponentName`). Using this argument will direct the Intent to a specific class within a specific Android package. |
| flags | An iterable data structure containing flags that control how the Intent is handled (see `Intent.setFlags()`). |

#### `MonkeyImage` takeSnapshot ()

Captures the entire screen buffer of this device, yielding a
screen capture of the current display.

##### Returns

* A [MonkeyImage](/tools/help/MonkeyImage) object containing the image of the current display.

#### void touch ( *integer* x, *integer* y, *string* type)

Sends a touch event specified by type to the screen location specified
by x and y.

##### Arguments

|  |  |
| --- | --- |
| x | The horizontal position of the touch in actual device pixels, starting from the left of the screen in its current orientation. |
| y | The vertical position of the touch in actual device pixels, starting from the top of the screen in its current orientation. |
| type | The type of key event to send. The allowed values are `DOWN`, `UP`, and `DOWN_AND_UP`. |

#### void type (*string* message)

Sends the characters contained in message to this device, as if they
had been typed on the device's keyboard. This is equivalent to calling
`press()` for each keycode in `message`
using the key event type `DOWN_AND_UP`.

##### Arguments

|  |  |
| --- | --- |
| message | A string containing the characters to send. |

#### void wake ()

Wakes the screen of this device.

---

## Appendix

**Table 1.**Property variable names used with
[getProperty()](#getProperty) and
[getSystemProperty()](#getSystemProperty).

| Property Group | Property | Description | Notes |
| --- | --- | --- | --- |
| `build` | `board` | Code name for the device's system board | See `Build` |
| `brand` | The carrier or provider for which the OS is customized. |
| `device` | The device design name. |
| `fingerprint` | A unique identifier for the currently-running build. |
| `host` |  |
| `ID` | A changelist number or label. |
| `model` | The end-user-visible name for the device. |
| `product` | The overall product name. |
| `tags` | Comma-separated tags that describe the build, such as "unsigned" and "debug". |
| `type` | The build type, such as "user" or "eng". |
| `user` |  |
| `CPU_ABI` | The name of the native code instruction set, in the form CPU type plus ABI convention. |
| `manufacturer` | The product/hardware manufacturer. |
| `version.incremental` | The internal code used by the source control system to represent this version of the software. |
| `version.release` | The user-visible name of this version of the software. |
| `version.sdk` | The user-visible SDK version associated with this version of the OS. |
| `version.codename` | The current development codename, or "REL" if this version of the software has been released. |
| `display` | `width` | The device's display width in pixels. | See `DisplayMetrics` for details. |
| `height` | The device's display height in pixels. |
| `density` | The logical density of the display. This is a factor that scales DIP (Density-Independent Pixel) units to the device's resolution. DIP is adjusted so that 1 DIP is equivalent to one pixel on a 160 pixel-per-inch display. For example, on a 160-dpi screen, density = 1.0, while on a 120-dpi screen, density = .75. The value does not exactly follow the real screen size, but is adjusted to conform to large changes in the display DPI. See `density` for more details. |
| `am.current` | `package` | The Android package name of the currently running package. | The `am.current` keys return information about the currently-running Activity. |
| `action` | The current activity's action. This has the same format as the `name` attribute of the `action` element in a package manifest. |
| `comp.class` | The class name of the component that started the current Activity. See `comp.package` for more details. |
| `comp.package` | The package name of the component that started the current Activity. A component is specified by a package name and the name of class that the package contains. |
| `data` | The data (if any) contained in the Intent that started the current Activity. |
| `categories` | The categories specified by the Intent that started the current Activity. |
| `clock` | `realtime` | The number of milliseconds since the device rebooted, including deep-sleep time. | See `SystemClock` for more information. |
| `uptime` | The number of milliseconds since the device rebooted, *not* including deep-sleep time |
| `millis` | current time since the UNIX epoch, in milliseconds. |