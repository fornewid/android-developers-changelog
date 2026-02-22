---
title: https://developer.android.com/guide/topics/manifest/uses-configuration-element
url: https://developer.android.com/guide/topics/manifest/uses-configuration-element
source: md.txt
---

# &lt;uses-configuration>

syntax:
:

    ```xml
    <uses-configuration
      android:reqFiveWayNav=["true" | "false"]
      android:reqHardKeyboard=["true" | "false"]
      android:reqKeyboardType=["undefined" | "nokeys" | "qwerty" | "twelvekey"]
      android:reqNavigation=["undefined" | "nonav" | "dpad" | "trackball" | "wheel"]
      android:reqTouchScreen=["undefined" | "notouch" | "stylus" | "finger"] />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Indicates the hardware and software features the application requires. For example, an application might specify that it requires a physical keyboard or a particular navigation device, like a trackball. The specification is used to avoid installing the application on devices where it doesn't work.

    **Note:** Most apps don't use this manifest tag.*Always*support input with a directional pad (D-pad) to assist sight-impaired users and support devices that provide D-pad input in addition to or instead of touch.

    For information about how to support D-pad input in your app, read[Handle controller actions](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-input). If your app absolutely can't function without a touchscreen, then instead use the[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)tag to declare the required touchscreen type, ranging from`"android.hardware.faketouch"`for basic touch-style events to more advanced touch types such as`"android.hardware.touchscreen.multitouch.jazzhand"`for distinct input from multiple fingers.

attributes:
:

    `android:reqFiveWayNav`
    :   Whether the application requires a five-way navigation control. It's`"true"`if it does, and`"false"`if not. A five-way control is one that can move the selection up, down, right, or left, and also provides a way of invoking the current selection. It can be a directional pad (D-pad), trackball, or other device.

        If an application requires a directional control, but not a control of a particular type, it can set this attribute to`"true"`and ignore the[reqNavigation](https://developer.android.com/guide/topics/manifest/uses-configuration-element#nav)attribute. However, if it requires a particular type of directional control, it can ignore this attribute and set`reqNavigation`instead.

    `android:reqHardKeyboard`
    :   Whether the application requires a hardware keyboard. It's`"true"`if it does, and`"false"`if not.

    `android:reqKeyboardType`
    :   The type of keyboard the application requires, if any. This attribute doesn't distinguish between hardware and software keyboards. If a hardware keyboard of a certain type is required, specify the type here and also set the`reqHardKeyboard`attribute to`"true"`.

        The value must be one of the following strings:

        |     Value     |                                                                        Description                                                                         |
        |---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | "`undefined`" | The application doesn't require a keyboard. A keyboard requirement isn't defined. This is the default value.                                               |
        | "`nokeys`"    | The application doesn't require a keyboard.                                                                                                                |
        | "`qwerty`"    | The application requires a standard QWERTY keyboard.                                                                                                       |
        | "`twelvekey`" | The application requires a twelve-key keypad, like those on most phones, with keys for the digits from`0`through`9`, plus star (`*`) and pound (`#`) keys. |

    `android:reqNavigation`
    :   The navigation device required by the application, if any. The value must be one of the following strings:

        |     Value     |                                                             Description                                                              |
        |---------------|--------------------------------------------------------------------------------------------------------------------------------------|
        | "`undefined`" | The application doesn't require any type of navigation control. The navigation requirement isn't defined. This is the default value. |
        | "`nonav`"     | The application doesn't require a navigation control.                                                                                |
        | "`dpad`"      | The application requires a D-pad for navigation.                                                                                     |
        | "`trackball`" | The application requires a trackball for navigation.                                                                                 |
        | "`wheel`"     | The application requires a navigation wheel.                                                                                         |

        If an application requires a navigational control, but the exact type of control doesn't matter, it can set the[reqFiveWayNav](https://developer.android.com/guide/topics/manifest/uses-configuration-element#five)attribute to`"true"`rather than setting this one.

    `android:reqTouchScreen`
    :   The type of touch screen the application requires, if any. The value must be one of the following strings:

        |     Value     |                                                                                                                                                                                Description                                                                                                                                                                                 |
        |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | "`undefined`" | The application doesn't require a touch screen. The touch screen requirement is undefined. This is the default value.                                                                                                                                                                                                                                                      |
        | "`notouch`"   | The application doesn't require a touch screen.                                                                                                                                                                                                                                                                                                                            |
        | "`stylus`"    | The application requires a touch screen that is operated with a stylus.                                                                                                                                                                                                                                                                                                    |
        | "`finger`"    | The application requires a touch screen that is operated with a finger. **Note:** If some type of touch input is required for your app, instead use the[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)tag to declare the required touchscreen type, beginning with`"android.hardware.faketouch"`for basic touch-style events. |

introduced in:
:   API level 3

see also:
:
    - [configChanges](https://developer.android.com/guide/topics/manifest/activity-element#config)attribute of the[<activity>](https://developer.android.com/guide/topics/manifest/activity-element)element
    - [ConfigurationInfo](https://developer.android.com/reference/android/content/pm/ConfigurationInfo)