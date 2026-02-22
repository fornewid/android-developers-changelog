---
title: https://developer.android.com/ndk/guides/rootless-debug-gles
url: https://developer.android.com/ndk/guides/rootless-debug-gles
source: md.txt
---

On devices running Android 10 (API level 29) and higher, OpenGL ES (GLES) layering is
available. A debuggable app can load GLES layers from its APK, from its base
directory, or from a selected layer APK.

GLES layer usage is similar to
[Vulkan validation layer](https://developer.android.com/ndk/guides/graphics/validation-layer) usage.

## Requirements

GLES layers are supported only on GLES versions 2.0+.
| **Warning:** When layering is enabled, GLES 1.x exclusive functions continue to route to GLES 1.x drivers, but functions shared with GLES 2.0+, such as `glGetString()`, are routed to 2.0+ drivers.

## Layer initialization

After populating standard entry points, the EGL Loader instantiates a GLES
`LayerLoader`. If debug layers are enabled, the `LayerLoader` scans specified
directories for layers, like the
[Vulkan loader](https://developer.android.com/ndk/guides/graphics/validation-layer#ilp) does.

If layering is enabled, the `LayerLoader` searches for and enumerates a specified
layer list. The layer list is specified by colon separated filenames.

The `LayerLoader` traverses the layers in the order you specify, so the first
layer is directly below the application. For each layer, the `LayerLoader`
tracks the `AndroidGLESLayer_Initialize` and
`AndroidGLESLayer_GetProcAddress` entry points. The layers *must* provide these
interfaces to be loadable.  

```c++
typedef void* (*PFNEGLGETNEXTLAYERPROCADDRESSPROC)(void*, const char*);
void* AndroidGLESLayer_Initialize(void* layer_id, PFNEGLGETNEXTLAYERPROCADDRESSPROC get_next_layer_proc_address))
```

`AndroidGLESLayer_Initialize()` provides an identifier for the layer to use
(`layer_id`) and an entry point that can be called to look up functions below
the layer. The entry point can be used as shown in the following code sample:  

```c++
const char* func = "eglFoo";
void* gpa = get_next_layer_proc_address(layer_id, func);
```

`AndroidGLESLayer_GetProcAddress` takes the address of the next call in the
chain that the layer should call when finished. If there is only one layer,
`next` points directly to the driver for most functions.  

```c++
typedef __eglMustCastToProperFunctionPointerType EGLFuncPointer;
void* AndroidGLESLayer_GetProcAddress(const char *funcName, EGLFuncPointer next)
```

For each layer that the GLES `LayerLoader` finds, it calls
`AndroidGLESLayer_Initialize`, walks `libEGL`'s function lists, and calls
`AndroidGLESLayer_GetProcAddress` for all known functions. It is up to the layer
to determine how to track the next address. If the layer intercepts a function,
it tracks the function's address. If the layer doesn't intercept a function,
`AndroidGLESLayer_GetProcAddress` returns the same function address it was
passed. The `LayerLoader` then updates the function hook list to point to the
layer's entry point.

The layers aren't required to do anything with the information
`AndroidGLESLayer_Initialize` and `get_next_layer_proc_address` provide, but
providing the data makes it easier for existing layers, like
[Android GPU Inspector](https://developer.android.com/agi) and
[RenderDoc](https://renderdoc.org/), to support
Android. With that data, a layer can look up functions independently instead of
waiting for calls to `AndroidGLESLayer_GetProcAddress`. If the layers choose to
initialize themselves before the loader has queried all the entry points, they
must use `get_next_layer_proc_address`. `eglGetProcAddress` must
be passed down the chain to the platform.

## Place layers

The GLES `LayerLoader` searches for layers in the following locations, in order
of priority:

**1. System location for root**

This requires root access  

```bash
adb root
adb disable-verity
adb reboot
adb root
adb shell setenforce 0
adb shell mkdir -p /data/local/debug/gles
adb push <layer>.so /data/local/debug/gles/
```

**2. Application's base directory**

Target application must be debuggable, or you must have root access:  

```bash
adb push libGLTrace.so /data/local/tmp
adb shell run-as com.android.gl2jni cp /data/local/tmp/libGLTrace.so .
adb shell run-as com.android.gl2jni ls | grep libGLTrace
libGLTrace.so
```

**3. External APK**

Determine the ABI of your target application, then install an APK containing
the layers you wish to load:  

```bash
adb install --abi armeabi-v7a layers.apk
```

**4. In the target application's APK**

The following example shows how to place layers in the application APK:  

```
$ jar tf GLES_layers.apk
lib/arm64-v8a/libGLES_glesLayer1.so
lib/arm64-v8a/libGLES_glesLayer2.so
lib/arm64-v8a/libGLES_glesLayer3.so
lib/armeabi-v7a/libGLES_glesLayer1.so
lib/armeabi-v7a/libGLES_glesLayer2.so
lib/armeabi-v7a/libGLES_glesLayer3.so
resources.arsc
AndroidManifest.xml
META-INF/CERT.SF
META-INF/CERT.RSA
META-INF/MANIFEST.MF
```

## Enable layers

You can enable GLES layers either per app or globally. Per-app settings persist
across reboots, while global properties are cleared on reboot.

Android's security model and policies differ
significantly from other platforms. In order to load external layers, one of the
following must be true:

- The target app's manifest file includes the following
  [meta-data element](https://developer.android.com/guide/topics/manifest/meta-data-element) (only applies
  to apps that target Android 11 (API level 30) or higher):

  `<meta-data android:name="com.android.graphics.injectLayers.enable" android:value="true" />`

  You should use this option to profile your application.
- The target app is debuggable. This option gives you more debug information,
  but might negatively affect the performance of your app.

- The target app is run on a userdebug build of the operating system which
  grants root access.

To enable layers per app:  

```
# Enable layers
adb shell settings put global enable_gpu_debug_layers 1

# Specify target application
adb shell settings put global gpu_debug_app <package_name>

# Specify layer list (from top to bottom)
# Layers are identified by their filenames, such as "libGLLayer.so"
adb shell settings put global gpu_debug_layers_gles <layer1:layer2:layerN>

# Specify packages to search for layers
adb shell settings put global gpu_debug_layer_app <package1:package2:packageN>
```

To disable layers per app:  

```
# Delete the global setting that enables layers
adb shell settings delete global enable_gpu_debug_layers

# Delete the global setting that selects target application
adb shell settings delete global gpu_debug_app

# Delete the global setting that specifies layer list
adb shell settings delete global gpu_debug_layers_gles

# Delete the global setting that specifies layer packages
adb shell settings delete global gpu_debug_layer_app
```

To enable layers globally:  

```
# This attempts to load layers for all applications, including native
# executables
adb shell setprop debug.gles.layers <layer1:layer2:layerN>
```

## Create a layer

Layers must expose the following two functions described in
[EGL Loader initialization](https://developer.android.com/ndk/guides/rootless-debug-gles#egl-loader):  

```c++
AndroidGLESLayer_Initialize
AndroidGLESLayer_GetProcAddress
```

### Passive layers

For a layer that only intercepts a handful of functions, a
passively initialized layer is optimal. The passively initialized layer waits
for GLES `LayerLoader` to initialize the function it needs.

The following code sample shows how to create a passive layer.  

```c++
namespace {

std::unordered_map<std::string, EGLFuncPointer> funcMap;

EGLAPI EGLBoolean EGLAPIENTRY glesLayer_eglChooseConfig (
  EGLDisplay dpy, const EGLint *attrib_list, EGLConfig *configs, EGLint config_size,
  EGLint *num_config) {

  EGLFuncPointer entry = funcMap["eglChooseConfig"];

  typedef EGLBoolean (*PFNEGLCHOOSECONFIGPROC)(
    EGLDisplay, const EGLint*, EGLConfig*, EGLint, EGLint*);

  PFNEGLCHOOSECONFIGPROC next = reinterpret_cast<PFNEGLCHOOSECONFIGPROC>(entry);

  return next(dpy, attrib_list, configs, config_size, num_config);
}

EGLAPI EGLFuncPointer EGLAPIENTRY eglGPA(const char* funcName) {

  #define GETPROCADDR(func) if(!strcmp(funcName, #func)) { \
    return (EGLFuncPointer)glesLayer_##func; }

  GETPROCADDR(eglChooseConfig);

  // Don't return anything for unrecognized functions
  return nullptr;
}

EGLAPI void EGLAPIENTRY glesLayer_InitializeLayer(
  void* layer_id, PFNEGLGETNEXTLAYERPROCADDRESSPROC get_next_layer_proc_address) {
     // This function is purposefully empty, since this layer does not proactively
     // look up any entrypoints
  }

EGLAPI EGLFuncPointer EGLAPIENTRY glesLayer_GetLayerProcAddress(
  const char* funcName, EGLFuncPointer next) {
  EGLFuncPointer entry = eglGPA(funcName);
  if (entry != nullptr) {
    funcMap[std::string(funcName)] = next;
    return entry;
  }
  return next;
}

}  // namespace

extern "C" {
  __attribute((visibility("default"))) EGLAPI void AndroidGLESLayer_Initialize(
    void* layer_id, PFNEGLGETNEXTLAYERPROCADDRESSPROC get_next_layer_proc_address) {
    return (void)glesLayer_InitializeLayer(layer_id, get_next_layer_proc_address);
  }
  __attribute((visibility("default"))) EGLAPI void* AndroidGLESLayer_GetProcAddress(
    const char *funcName, EGLFuncPointer next) {
    return (void*)glesLayer_GetLayerProcAddress(funcName, next);
  }
}
```

### Active layers

For more formalized layers that need to fully initialize up front, or layers
that need to look up extensions not known to the EGL Loader, active layer
initialization is required. The layer uses
the `get_next_layer_proc_address` that `AndroidGLESLayer_Initialize` provides to
look up a function. The layer must still respond to
`AndroidGLESLayer_GetProcAddress` requests from the loader so the platform knows
where to route calls. The following code sample shows how to create an active
layer.  

```c++
namespace {

std::unordered_map<std::string, EGLFuncPointer> funcMap;

EGLAPI EGLBoolean EGLAPIENTRY glesLayer_eglChooseConfig (
  EGLDisplay dpy, const EGLint *attrib_list, EGLConfig *configs, EGLint config_size,
  EGLint *num_config) {

  EGLFuncPointer entry = funcMap["eglChooseConfig"];

  typedef EGLBoolean (*PFNEGLCHOOSECONFIGPROC)(
    EGLDisplay, const EGLint*, EGLConfig*, EGLint, EGLint*);

  PFNEGLCHOOSECONFIGPROC next = reinterpret_cast<PFNEGLCHOOSECONFIGPROC>(entry);

  return next(dpy, attrib_list, configs, config_size, num_config);
}

EGLAPI EGLFuncPointer EGLAPIENTRY eglGPA(const char* funcName) {

  #define GETPROCADDR(func) if(!strcmp(funcName, #func)) { \
    return (EGLFuncPointer)glesLayer_##func; }

  GETPROCADDR(eglChooseConfig);

  // Don't return anything for unrecognized functions
  return nullptr;
}

EGLAPI void EGLAPIENTRY glesLayer_InitializeLayer(
  void* layer_id, PFNEGLGETNEXTLAYERPROCADDRESSPROC get_next_layer_proc_address) {

  // Note: This is where the layer would populate its function map with all the
  // functions it cares about
  const char* func = "eglChooseConfig";
  funcMap[func] = get_next_layer_proc_address(layer_id, func);
}

EGLAPI EGLFuncPointer EGLAPIENTRY glesLayer_GetLayerProcAddress(
  const char* funcName, EGLFuncPointer next) {
  EGLFuncPointer entry = eglGPA(funcName);
  if (entry != nullptr) {
    return entry;
  }

  return next;
}

}  // namespace

extern "C" {
  __attribute((visibility("default"))) EGLAPI void AndroidGLESLayer_Initialize(
    void* layer_id, PFNEGLGETNEXTLAYERPROCADDRESSPROC get_next_layer_proc_address) {
    return (void)glesLayer_InitializeLayer(layer_id, get_next_layer_proc_address);
  }
  __attribute((visibility("default"))) EGLAPI void* AndroidGLESLayer_GetProcAddress(
    const char *funcName, EGLFuncPointer next) {
    return (void*)glesLayer_GetLayerProcAddress(funcName, next);
  }
}
```