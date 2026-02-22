---
title: https://developer.android.com/ndk/guides/graphics/validation-layer
url: https://developer.android.com/ndk/guides/graphics/validation-layer
source: md.txt
---

Most explicit graphics APIs don't perform error-checking because doing so can
result in a performance penalty. Vulkan has *validation layers* that provide
error-checking during development, avoiding the performance penalty in the
release build of your app. Validation layers rely on a general purpose
layering mechanism that intercepts API entry points.

## Single Khronos validation layer

Previously, Vulkan provided multiple validation layers that needed to be enabled
in a specific order. Beginning with the 1.1.106.0 Vulkan SDK release, your app
only has to enable a [single validation
layer](https://vulkan.lunarg.com/doc/view/latest/windows/validation_layers.html),
`VK_LAYER_KHRONOS_validation`, to get all features from the previous
validation layers.
| **Note:** The unified `VK_LAYER_KHRONOS_validation` layer is also supported on non-mobile devices so you can share the same validation code across all platforms.

## Use validation layers packaged in your APK

Packaging validation layers within your APK ensures optimal compatibility.
The validation layers are available as prebuilt binaries or are buildable from
source code.
| **Note:** Android 9 (API level 28) and higher allows Vulkan to load layers that are located separately from your app's APK. See [Use external validation
| layers](https://developer.android.com/ndk/guides/graphics/validation-layer#vl-external) for more information.

### Use prebuilt binaries

Download the latest Android Vulkan Validation layer binaries from the [GitHub
release page](https://github.com/KhronosGroup/Vulkan-ValidationLayers/releases).

The easiest way to add the layers to your APK is to extract the prebuilt layer
binaries to the `src/main/jniLibs/` directory of your module, with ABI
directories (such as `arm64-v8a` or `x86-64`) intact, like this:  

```
src/main/jniLibs/
  arm64-v8a/
    libVkLayer_khronos_validation.so
  armeabi-v7a/
    libVkLayer_khronos_validation.so
  x86/
    libVkLayer_khronos_validation.so
  x86-64/
    libVkLayer_khronos_validation.so
```

### Build the validation layer from source code

To debug into the validation layer source code, pull the latest source from the
Khronos Group [GitHub
repository](https://github.com/KhronosGroup/Vulkan-ValidationLayers) and follow
the build instructions there.

### Verify the validation layer is packaged correctly

Regardless of whether you build with the Khronos prebuilt layers or layers built
from source, the build process produces a final file structure in your APK like
the following:  

```
lib/
  arm64-v8a/
    libVkLayer_khronos_validation.so
  armeabi-v7a/
    libVkLayer_khronos_validation.so
  x86/
    libVkLayer_khronos_validation.so
  x86-64/
    libVkLayer_khronos_validation.so
```

The following command shows how to verify that your APK contains the validation
layer as expected:  

```
$ jar -tf project.apk | grep libVkLayer
lib/x86_64/libVkLayer_khronos_validation.so
lib/armeabi-v7a/libVkLayer_khronos_validation.so
lib/arm64-v8a/libVkLayer_khronos_validation.so
lib/x86/libVkLayer_khronos_validation.so
```

## Enable a validation layer during instance creation

The Vulkan API allows an app to enable layers during instance creation. Entry
points that a layer intercepts must have one of the following objects as the
first parameter:

- `VkInstance`
- `VkPhysicalDevice`
- `VkDevice`
- `VkCommandBuffer`
- `VkQueue`

Call [`vkEnumerateInstanceLayerProperties()`](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkEnumerateInstanceLayerProperties.html)
to list the available layers and their properties. Vulkan enables layers when
[`vkCreateInstance()`](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkCreateInstance.html)
executes.

The following code snippet shows how an app can use the Vulkan API to
programmatically query and enable layers:  

```c++
// Enable just the Khronos validation layer.
static const char *layers[] = {"VK_LAYER_KHRONOS_validation"};

// Get the layer count using a null pointer as the last parameter.
uint32_t instance_layer_present_count = 0;
vkEnumerateInstanceLayerProperties(&instance_layer_present_count, nullptr);

// Enumerate layers with a valid pointer in the last parameter.
VkLayerProperties layer_props[instance_layer_present_count];
vkEnumerateInstanceLayerProperties(&instance_layer_present_count, layer_props);

// Make sure selected validation layers are available.
VkLayerProperties *layer_props_end = layer_props + instance_layer_present_count;
for (const char* layer:layers) {
  assert(layer_props_end !=
  std::find_if(layer_props, layer_props_end, [layer](VkLayerProperties layerProperties) {
    return strcmp(layerProperties.layerName, layer) == 0;
  }));
}

// Create a Vulkan instance, requesting all enabled layers or extensions
// available on the system
VkInstanceCreateInfo instanceCreateInfo{
  .sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
  .pNext = nullptr,
  .pApplicationInfo = &appInfo,
  .enabledLayerCount = sizeof(layers) / sizeof(layers[0]),
  .ppEnabledLayerNames = layers,
```

## Default logcat output

The validation layer emits warning and error messages in logcat labeled with a
`VALIDATION` tag. A validation layer message looks like the following (with
line breaks added here for easier scrolling):  

```
Validation -- Validation Error:
  [ VUID-VkDeviceQueueCreateInfo-pQueuePriorities-parameter ]
Object 0: VK_NULL_HANDLE, type = VK_OBJECT_TYPE_DEVICE; | MessageID = 0xd6d720c6 |
vkCreateDevice: required parameter
  pCreateInfo->pQueueCreateInfos[0].pQueuePriorities specified as NULL.
The Vulkan spec states: pQueuePriorities must be a valid pointer to an array of
  queueCount float values
  (https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html
  #VUID-VkDeviceQueueCreateInfo-pQueuePriorities-parameter)
```

## Enable the debug callback

The Debug Utils extension `VK_EXT_debug_utils` lets your application create a
debug messenger that passes validation layer messages to an application-supplied
callback. Your device may not implement this extension, but it is implemented in
the most recent validation layers. There's also a deprecated extension called
`VK_EXT_debug_report`, which provides similar capabilities if
`VK_EXT_debug_utils` is not available.

Before using the Debug Utils extension, you should make sure that your device
or a loaded validation layer supports it. The following example shows how to
check whether the debug utils extension is supported and register a callback if
the extension is supported by either the device or validation layer.  

```c++
// Get the instance extension count.
uint32_t inst_ext_count = 0;
vkEnumerateInstanceExtensionProperties(nullptr, &inst_ext_count, nullptr);

// Enumerate the instance extensions.
VkExtensionProperties inst_exts[inst_ext_count];
vkEnumerateInstanceExtensionProperties(nullptr, &inst_ext_count, inst_exts);

// Check for debug utils extension within the system driver or loader.
// Check if the debug utils extension is available (in the driver).
VkExtensionProperties *inst_exts_end = inst_exts + inst_ext_count;
bool debugUtilsExtAvailable = inst_exts_end !=
  std::find_if(inst_exts, inst_exts_end, [](VkExtensionProperties
    extensionProperties) {
    return strcmp(extensionProperties.extensionName,
      VK_EXT_DEBUG_UTILS_EXTENSION_NAME) == 0;
  });

if ( !debugUtilsExtAvailable ) {
  // Also check the layers for the debug utils extension.
  for (auto layer: layer_props) {
    uint32_t layer_ext_count;
    vkEnumerateInstanceExtensionProperties(layer.layerName, &layer_ext_count,
      nullptr);
    if (layer_ext_count == 0) continue;
    VkExtensionProperties layer_exts[layer_ext_count];
    vkEnumerateInstanceExtensionProperties(layer.layerName, &layer_ext_count,
    layer_exts);

    VkExtensionProperties * layer_exts_end = layer_exts + layer_ext_count;
    debugUtilsExtAvailable = layer_exts != std::find_if(
      layer_exts, layer_exts_end,[](VkExtensionProperties extensionProperties) {
        return strcmp(extensionProperties.extensionName,
        VK_EXT_DEBUG_UTILS_EXTENSION_NAME) == 0;
      });
    if (debugUtilsExtAvailable) {
        // Add the including layer into the layer request list if necessary.
        break;
    }
  }
}

if (!debugUtilsExtAvailable) return; // since this snippet depends on debugUtils

const char * enabled_inst_exts[] = { ..., VK_EXT_DEBUG_UTILS_EXTENSION_NAME };
uint32_t enabled_extension_count =
  sizeof(enabled_inst_exts)/sizeof(enabled_inst_exts[0]);

// Pass the instance extensions into vkCreateInstance.
VkInstanceCreateInfo instance_info = {};
instance_info.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
instance_info.enabledExtensionCount = enabled_extension_count;
instance_info.ppEnabledExtensionNames = enabled_inst_exts;

// NOTE: Can still return VK_ERROR_EXTENSION_NOT_PRESENT if validation layer
// isn't loaded.
vkCreateInstance(&instance_info, nullptr, &instance);

auto pfnCreateDebugUtilsMessengerEXT =
  (PFN_vkCreateDebugUtilsMessengerEXT)vkGetInstanceProcAddr(
    tutorialInstance, "vkCreateDebugUtilsMessengerEXT");
auto pfnDestroyDebugUtilsMessengerEXT =
  (PFN_vkDestroyDebugUtilsMessengerEXT)vkGetInstanceProcAddr(
    tutorialInstance, "vkDestroyDebugUtilsMessengerEXT");

// Create the debug messenger callback with your the settings you want.
VkDebugUtilsMessengerEXT debugUtilsMessenger;
if (pfnCreateDebugUtilsMessengerEXT) {
  VkDebugUtilsMessengerCreateInfoEXT messengerInfo;
  constexpr VkDebugUtilsMessageSeverityFlagsEXT kSeveritiesToLog =
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT |
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT;

constexpr VkDebugUtilsMessageTypeFlagsEXT kMessagesToLog =
  VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT |
  VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT |
  VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT;

  messengerInfo.sType           = VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT;
  messengerInfo.pNext           = nullptr;
  messengerInfo.flags           = 0;
  messengerInfo.messageSeverity = kSeveritiesToLog;
  messengerInfo.messageType     = kMessagesToLog;

  // The DebugUtilsMessenger callback is explained in the following section.
  messengerInfo.pfnUserCallback = &DebugUtilsMessenger;
  messengerInfo.pUserData       = nullptr; // Custom user data passed to callback

  pfnCreateDebugUtilsMessengerEXT(instance, &messengerInfo, nullptr,
    &debugUtilsMessenger);
}

// Later, when shutting down Vulkan, call the following:
if (pfnDestroyDebugUtilsMessengerEXT) {
    pfnDestroyDebugUtilsMessengerEXT(instance, debugUtilsMessenger, nullptr);
}
```

After your app registers and enables the callback, the system routes debugging
messages to it.  

```c++
#include <android/log.h>

VKAPI_ATTR VkBool32 VKAPI_CALL DebugUtilsMessenger(
                        VkDebugUtilsMessageSeverityFlagBitsEXT messageSeverity,
                        VkDebugUtilsMessageTypeFlagsEXT messageTypes,
                        const VkDebugUtilsMessengerCallbackDataEXT *callbackData,
                        void *userData)
{
  const char validation[]  = "Validation";
  const char performance[] = "Performance";
  const char error[]       = "ERROR";
  const char warning[]     = "WARNING";
  const char unknownType[] = "UNKNOWN_TYPE";
  const char unknownSeverity[] = "UNKNOWN_SEVERITY";
  const char* typeString      = unknownType;
  const char* severityString  = unknownSeverity;
  const char* messageIdName   = callbackData->pMessageIdName;
  int32_t messageIdNumber     = callbackData->messageIdNumber;
  const char* message         = callbackData->pMessage;
  android_LogPriority priority = ANDROID_LOG_UNKNOWN;

  if (messageSeverity & VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT) {
    severityString = error;
    priority = ANDROID_LOG_ERROR;
  }
  else if (messageSeverity & VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT) {
    severityString = warning;
    priority = ANDROID_LOG_WARN;
  }
  if (messageTypes & VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT) {
     typeString = validation;
  }
  else if (messageTypes & VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT) {
     typeString = performance;
  }

  __android_log_print(priority,
                     "AppName",
                     "%s %s: [%s] Code %i : %s",
                     typeString,
                     severityString,
                     messageIdName,
                     messageIdNumber,
                     message);

  // Returning false tells the layer not to stop when the event occurs, so
  // they see the same behavior with and without validation layers enabled.
  return VK_FALSE;
}
```

## Use external validation layers

You don't have to package validation layers in your APK; devices running Android
9 (API level 28) and higher can use validation layers external to your binary
and turn them off and on dynamically. Follow the steps in this section to push
validation layers to your test device:

### Enable your app to use external validation layers

Android's security model and policies differ significantly from other
platforms. To load external validation layers, one of the following conditions
must be true:

- The target app is **debuggable**. This option results in more debug
  information, but might negatively affect the performance of your app.

- The target app is run on a **userdebug** build of the operating system that
  grants root access.

- Apps targeting Android 11 (API level 30) or higher only: Your target Android
  manifest file includes the following
  [`meta-data`](https://developer.android.com/guide/topics/manifest/meta-data-element) element:

  ```xml
  <meta-data android:name="com.android.graphics.injectLayers.enable"
    android:value="true"/>
  ```

### Load an external validation layer

Devices running Android 9 (API level 28) and higher allow Vulkan to [load the
validation layer from your app's local storage](https://developer.android.com/ndk/guides/graphics/validation-layer#layers-local-storage). Starting
in Android 10 (API level 29), Vulkan can also load the validation layer [from a
separate APK](https://developer.android.com/ndk/guides/graphics/validation-layer#apk-containing-layers). You can choose whichever method you like
as long as your Android version supports it.

#### Load a validation layer binary from your device's local storage

Because Vulkan looks for the binary in your device's temporary data storage
directory, you must first push the binary to that directory using [Android Debug
Bridge (adb)](https://developer.android.com/studio/command-line/adb), as follows:

1. Use the [`adb push`](https://developer.android.com/studio/command-line/adb#copyfiles) command to load the
   layer binary into your app's data storage on the device:

   ```
   $ adb push libVkLayer_khronos_validation.so /data/local/tmp
   ```
2. Use the [`adb shell`](https://developer.android.com/studio/command-line/adb#shellcommands) and `run-as`
   commands to load the layer through your app process. That is, the binary
   has the same device access that the app has without requiring root access.

   ```
   $ adb shell run-as com.example.myapp cp
     /data/local/tmp/libVkLayer_khronos_validation.so .
   $ adb shell run-as com.example.myapp ls libVkLayer_khronos_validation.so
   ```
3. [Enable the layer](https://developer.android.com/ndk/guides/graphics/validation-layer#enable-layers-outside-app).

#### Load a validation layer binary from another APK

You can use `adb` to [install an APK](https://developer.android.com/studio/command-line/adb#move) that
contains the layer and then [enable the layer](https://developer.android.com/ndk/guides/graphics/validation-layer#enable-layers-outside-app).  

```
adb install --abi abi path_to_apk
```

## Enable layers outside the application

You can enable Vulkan layers either per-app or globally. Per-app settings
*persist* across reboots, while global properties are *cleared* on
reboot.

### Enable layers on a per-app basis

The following steps describe how to enable layers on a per-app basis:

1. Use adb shell settings to enable the layers:

       $ adb shell settings put global enable_gpu_debug_layers 1

2. Specify the target application to enable the layers on:

   ```
   $ adb shell settings put global gpu_debug_app <package_name>
   ```
3. Specify the list of layers to enable (from top to bottom), separating each
   layer by a colon:

   ```
   $ adb shell settings put global gpu_debug_layers <layer1:layer2:layerN>
   ```

   Since we have a single Khronos validation layer, the command will likely
   look like:  

       $ adb shell settings put global gpu_debug_layers VK_LAYER_KHRONOS_validation

4. Specify one or more packages to search for layers inside of:

   ```
   $ adb shell settings put global
     gpu_debug_layer_app <package1:package2:packageN>
   ```

| **Note:** You can also enable the `enable_gpu_debug_layers` setting through the on-device developer options. After you enable developer options, open the **Settings** app on your test device, navigate to **Developer options \>
| Debugging** and make sure the option to **Enable GPU debug layers** is turned on.

You can check whether the settings are enabled using the following commands:  

```
$ adb shell settings list global | grep gpu
enable_gpu_debug_layers=1
gpu_debug_app=com.example.myapp
gpu_debug_layers=VK_LAYER_KHRONOS_validation
```

Because the settings you apply persist across device reboots, you may want to
clear the settings after the layers are loaded:  

```
$ adb shell settings delete global enable_gpu_debug_layers
$ adb shell settings delete global gpu_debug_app
$ adb shell settings delete global gpu_debug_layers
$ adb shell settings delete global gpu_debug_layer_app
```

### Enable layers globally

You can enable one or more layers globally until the next reboot.
This attempts to load the layers for all applications, including native
executables.  

```
$ adb shell setprop debug.vulkan.layers <layer1:layer2:layerN>
```