---
title: https://developer.android.com/games/engines/unity/unity-vkquality
url: https://developer.android.com/games/engines/unity/unity-vkquality
source: md.txt
---

# VkQuality Unity engine plugin

The VkQuality plugin for the Unity engine provides launch-time recommendations
of the graphics API---Vulkan or OpenGL ES---to use for your game on specific
devices.

VkQuality recommends Vulkan on a more restricted set of devices than the Unity
engine's default allow list. Use VkQuality to gain the performance benefits of
Vulkan while limiting the use of Vulkan to newer devices with newer graphics
drivers, which limits your game's exposure to driver issues. VkQuality only
makes quality recommendations, not guarantees, as it's still possible to
encounter driver issues on recommended devices. VkQuality supports custom lists,
which gives you the ability to add or remove device recommendations for your
game.
| **Note:** VkQuality always recommends OpenGL ES on older devices that run Android 9.0 (API level 28) or lower or don't support at least version 1.1 of the Vulkan API. VkQuality returns the `RECOMMENDATION_GLES_BECAUSE_OLD_DEVICE` enum value on these devices.

## Enable Vulkan in your Unity engine game

VkQuality requires your game to have both the OpenGL ES and Vulkan renderers
enabled in the Unity project settings. Enable the renderers by using the [Auto
Graphics API](https://developer.android.com/games/engines/unity/start-in-unity#auto_graphics_api) option or by [manually setting](https://developer.android.com/games/engines/unity/start-in-unity#manual_graphics_apis) the graphics APIs.

## Get the VkQuality plugin for Unity engine

Download the VkQuality plugin [from GitHub](https://github.com/android/vkquality/releases). The plugin is
compatible with Unity 2021 and higher. Use Unity 2021 LTS or higher to enable
Vulkan on Android. The plugin package contains a basic sample project that uses
the plugin to set the graphics API at startup and then displays a string set to
the device's active graphics API.

## Manage the VkQuality Vulkan recommendation list

VkQuality includes a default recommendation list of supported devices. For
information on using a custom recommendation list, see the [Use a custom
recommendation list](https://developer.android.com/games/engines/unity/unity-vkquality#use-a-custom-recommendation-list) section.

The recommendation list includes three categories:

- Vulkan device allow list
- GPU recommendation allow list
- GPU recommendation deny list

### Device allow list matches

VkQuality first checks whether the active device is included in the device allow
list, and whether it's running the minimum Android version and Vulkan driver
version specified in the allow list for that device. If these criteria are met,
VkQuality recommends Vulkan by returning the
`RECOMMENDATION_VULKAN_BECAUSE_DEVICE_MATCH` enum value.

If the device is on the allow list, but is running an Android version or driver
version below the minimum specified for it in the allow list, VkQuality
recommends OpenGL ES by returning `RECOMMENDATION_GLES_BECAUSE_OLD_DRIVER`.

### GPU recommendation matches

If no device match is found on the device allow list, VkQuality evaluates the
GPU model and driver version against the GPU recommendation allow and deny
lists. If the GPU model and driver version match an entry in the GPU
recommendation allow list, VkQuality recommends Vulkan by returning the
`RECOMMENDATION_VULKAN_BECAUSE_PREDICTION_MATCH` enum constant.

If the GPU model and driver version match against an entry in the GPU
recommendation deny list, VkQuality recommends OpenGL ES by returning
`RECOMMENDATION_GLES_BECAUSE_PREDICTION_MATCH`.

### Recommendations without a match

If no matches are found, VkQuality recommends Vulkan if the Android API level of
the running device is equal to or higher than the Future API level in the
recommendation list. The default recommendation list has a Future API level of
36, meaning on unmatched devices running API level 36 or higher, VkQuality
returns the `RECOMMENDATION_VULKAN_BECAUSE_FUTURE_ANDROID` enum constant.

If no matches are found on the device allow list or GPU recommendation lists,
and the API level of the device is below the Future API level, VkQuality
recommends OpenGL ES by returning `RECOMMENDATION_GLES_BECAUSE_NO_DEVICE_MATCH`.

## Add the VkQuality archive file to your project

The VkQuality plugin is the `VkQuality-1.x.x.aar` file located in the
`Assets/Android/Plugins` directory of the downloaded package archive. The actual
version number of the .aar file matches the version number of the package
archive name. To install the plugin, perform the following steps:

1. Copy the .aar file to the `Assets/Android/Plugins` directory of your project. (Create the needed `Android` and `Plugins` subdirectories if they don't exist.)

![The VkQuality .aar file in the required project directory.](https://developer.android.com/static/images/games/engines/unity/unity-vkquality-unityassets.png) **Figure 1.**The VkQuality .aar file in the required project directory.

1. Select the `VkQuality-1.x.x` plugin file in the Unity **Project** hierarchy to bring up its **Import Settings** in the **Inspector** pane. Ensure the **Android** platform is checked.

![Figure 2. The VkQuality plugin platform import settings.](https://developer.android.com/static/images/games/engines/unity/unity-vkquality-unityplugin.png) **Figure 2.** The VkQuality plugin platform import settings.

## Use a custom activity to call VkQuality

Unlike typical Unity engine plugins, VkQuality must be executed to obtain a
graphics API recommendation before the Unity engine is initialized. You then use
the [Unity player command-line arguments](https://docs.unity3d.com/Manual/android-custom-activity-command-line.html) feature to set the
graphics API based on the VkQuality recommendation. On Android, passing
command-line arguments requires overriding the default behavior of the
[UnityPlayerActivity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) by [creating a custom
activity](https://docs.unity3d.com/Manual/android-custom-activity.html).

If your game is already using a custom activity, see the [Add VkQuality to an
existing custom activity](https://developer.android.com/games/engines/unity/unity-vkquality#add-vkquality-to-an-existing-custom-activity) section. To create a new custom activity for your
game, see [Add a custom activity to your Unity project](https://developer.android.com/games/engines/unity/unity-vkquality#add-a-custom-activity-to-your-unity-project), which follows next.

### Add a custom activity to your Unity engine project

An example custom activity that uses VkQuality is included in the [plugin
package](https://github.com/android/vkquality/releases/latest) in `Assets/Plugins/Android/VkQualityTestActivity.java`.
To customize the file and use it in your game, perform the following steps:

1. Copy the `VkQualityTestActivity.java` file into your `Assets/Plugins/Android` directory.
2. Rename it to something appropriate for your game (for example, `MyGameActivity.java`).
3. Open the file in a text editor.
4. Change the class name from `VkQualityTestActivity` to the name you gave the file (for example, `MyGameActivity.java`).
5. Change the package name from `com.google.android.games.VkQualityTest` to match the value of the **Package Name** field in your Unity Project Settings **Player** category under **Other Settings** (for example, `com.mycompany.mygame`).
6. Save and close the file.

Add a custom manifest file that references your custom activity, and tell Unity
to use your custom manifest file:

1. Copy the `AndroidManifest.xml` file from the `Assets/Plugins/Android` directory of the plugin package into your project's `Asset/Plugins/Android` directory.
2. Open the file in a text editor.
3. Change the value of the `activity android:name` setting from `com.google.android.games.VkQualityTest.VkQualityTestActivity` to the package and activity names you used in the previous steps (for example, `com.mycompany.mygame.MyGameActivity`).
4. Save and close the file.
5. Open the Unity settings window and select the **Player** settings. Expand the **Publishing Settings** section, and check the **Custom Main Manifest** checkbox.

![Figure 3.The Custom Main Manifest option in the Unity Player settings.](https://developer.android.com/static/images/games/engines/unity/unity-vkquality-unitymanifest.png) **Figure 3.** The **Custom Main Manifest** option in the Unity **Player** settings.

Your project is now set up to use the custom activity that calls VkQuality at
startup and chooses Vulkan or OpenGL ES based on the VkQuality recommendation.

### Add VkQuality to an existing custom activity

If your game already has a custom activity overriding the default
`UnityPlayerActivity`, integrate VkQuality recommendations by adding the
following code:

First, add the VkQuality import statement to the list of imports at the top of
the custom activity file:  

### Kotlin

```kotlin
import com.google.android.games.vkquality.VKQuality;
```

### Java

```java
import com.google.android.games.vkquality.VKQuality;
```

Next, create some constants in the body of your `Activity` class for the
graphics API choices:  

### Kotlin

```kotlin
companion object {
  private const val OVERRIDE_NONE = 0
  private const val OVERRIDE_GLES = 1
  private const val OVERRIDE_VULKAN = 2
```

### Java

```java
private static final int OVERRIDE_NONE = 0;
private static final int OVERRIDE_GLES = 1;
private static final int OVERRIDE_VULKAN = 2;
```

Create a variable to track the API selection:  

### Kotlin

```kotlin
private var apiOverride = OVERRIDE_NONE
```

### Java

```java
private int apiOverride = OVERRIDE_NONE;
```

Add the following function to your `Activity` class:  

### Kotlin

```kotlin
private fun CheckVkQuality() {
    val vkQuality = VKQuality(this)
    val startResult = vkQuality.StartVkQuality("")
    if (startResult == VKQuality.INIT_SUCCESS) {
        // In the current release, we can assume GetVkQuality is
        // ready as soon as StartVkQuality has returned success.
        val getResult = vkQuality.GetVkQuality()
        LogVkQualityResult(getResult)
        apiOverride =
            when (getResult) {
                VKQuality.RECOMMENDATION_VULKAN_BECAUSE_DEVICE_MATCH,
                VKQuality.RECOMMENDATION_VULKAN_BECAUSE_PREDICTION_MATCH,
                VKQuality.RECOMMENDATION_VULKAN_BECAUSE_FUTURE_ANDROID -> OVERRIDE_VULKAN
                VKQuality.RECOMMENDATION_GLES_BECAUSE_OLD_DEVICE,
                VKQuality.RECOMMENDATION_GLES_BECAUSE_OLD_DRIVER,
                VKQuality.RECOMMENDATION_GLES_BECAUSE_NO_DEVICE_MATCH,
                VKQuality.RECOMMENDATION_GLES_BECAUSE_PREDICTION_MATCH -> OVERRIDE_GLES
                else -> OVERRIDE_GLES
            }
        vkQuality.StopVkQuality()
    } else {
        Log.e("VKQUALITY", "VkQuality start failed with result: $startResult")
    }
}
```

### Java

```java
private void CheckVkQuality() {
  VKQuality vkQuality = new VKQuality(this);
  // An empty string specifies use of the default
  // built-in device list file.
  int startResult = vkQuality.StartVkQuality("");
  if (startResult == VKQuality.INIT_SUCCESS) {
      // In the current release, we can assume GetVkQuality is
      // ready as soon as StartVkQuality has returned success.
      int getResult = vkQuality.GetVkQuality();

      switch (getResult) {
          case VKQuality.RECOMMENDATION_VULKAN_BECAUSE_DEVICE_MATCH:
          case VKQuality.RECOMMENDATION_VULKAN_BECAUSE_PREDICTION_MATCH:
          case VKQuality.RECOMMENDATION_VULKAN_BECAUSE_FUTURE_ANDROID:
              apiOverride = OVERRIDE_VULKAN;
              break;
          case VKQuality.RECOMMENDATION_GLES_BECAUSE_OLD_DEVICE:
          case VKQuality.RECOMMENDATION_GLES_BECAUSE_OLD_DRIVER:
          case VKQuality.RECOMMENDATION_GLES_BECAUSE_NO_DEVICE_MATCH:
          case VKQuality.RECOMMENDATION_GLES_BECAUSE_PREDICTION_MATCH:
          default:
              apiOverride = OVERRIDE_GLES;
              break;
      }
      vkQuality.StopVkQuality();
  } else {
      Log.e("VKQUALITY", "VkQuality start failed with result: " + startResult);
  }
}
```

Call the `CheckVkQuality` function from the top of an `onCreate()` override
function before calling the base class implementation:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  CheckVkQuality()
  super.onCreate(savedInstanceState)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    CheckVkQuality();
    super.onCreate(savedInstanceState);
}
```

Finally, add an override of the `updateUnityCommandLineArguments()` function
that uses the value of `apiOverride` to pass a command-line argument to the
Unity engine specifying which graphics API to use:  

### Kotlin

```kotlin
override fun updateUnityCommandLineArguments(cmdLine: String): String {
  if (apiOverride == OVERRIDE_VULKAN) {
      Log.i("VKQUALITY", "Passing -force-vulkan")
      return appendCommandLineArgument(cmdLine, "-force-vulkan")
  } else if (apiOverride == OVERRIDE_GLES) {
      Log.i("VKQUALITY", "Passing -force-gles")
      return appendCommandLineArgument(cmdLine, "-force-gles")
  }
  Log.i("VKQUALITY", "No override passed")
  // let Unity pick the Graphics API based on PlayerSettings
  return cmdLine
}

private fun appendCommandLineArgument(cmdLine: String, arg: String?): String {
    return if (arg == null || arg.isEmpty()) cmdLine
    else if (cmdLine == null || cmdLine.isEmpty()) arg else "$cmdLine $arg"
}
```

### Java

```java
@Override protected String updateUnityCommandLineArguments(String cmdLine)
{
    if (apiOverride == OVERRIDE_VULKAN) {
        Log.i("VKQUALITY", "Passing -force-vulkan");
        return appendCommandLineArgument(cmdLine, "-force-vulkan");
    }
    else if (apiOverride == OVERRIDE_GLES) {
        Log.i("VKQUALITY", "Passing -force-gles");
        return appendCommandLineArgument(cmdLine, "-force-gles");
    }
    Log.i("VKQUALITY", "No override passed");
    // let Unity pick the Graphics API based on PlayerSettings
    return cmdLine;
}

private String appendCommandLineArgument(String cmdLine, String arg) {
    if (arg == null || arg.isEmpty())
        return cmdLine;
    else if (cmdLine == null || cmdLine.isEmpty())
        return arg;
    else
        return cmdLine + " " + arg;
}
```

Your custom activity now calls VkQuality at startup and chooses Vulkan or OpenGL
ES based on the VkQuality recommendation.

## Use a custom recommendation list

Specify a custom recommendation list file by passing the name of the file
containing the list to `StartVkQuality()` instead of passing an empty string:  

### Kotlin

```kotlin
val startResult = vkQuality.StartVkQuality("<var translate="no">CUSTOM_FILE_NAME</var>.vkq")
```

### Java

```java
int startResult = vkQuality.StartVkQuality("<var translate="no">CUSTOM_FILE_NAME</var>.vkq");
```

VkQuality first looks for the file in your application's internal storage
directory. If the file is not in internal storage, VkQuality tries to load the
file from your app bundle's assets. If the file isn't in either location,
VkQuality returns the `ERROR_MISSING_DATA_FILE` enum value.

To create a custom recommendation list file, use the **VkQuality List Editor**
tool located in the [GitHub repository](https://github.com/android/vkquality/tree/main/list_editor). Documentation for the
tool is located in its [README](https://github.com/android/vkquality/tree/main/list_editor/README.md).
| **Note:** To include a custom recommendation list file in your app bundle assets, export the list from the **VkQuality List Editor** using the **.aar library** option and place the exported `.aar` file in the `Assets/Android/Plugins` directory. Unity does not include the `.vkq` file if you put it directly in the `Assets/Android/Plugins` directory, it *must* be bundled in an `.aar` library container. The `.vkq` filetype extension is still used when specifying the filename for `StartVkQuality()`.