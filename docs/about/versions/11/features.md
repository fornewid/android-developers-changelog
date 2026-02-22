---
title: https://developer.android.com/about/versions/11/features
url: https://developer.android.com/about/versions/11/features
source: md.txt
---

Android 11 introduces great new features and APIs for developers. The sections
below help you learn about features for your apps and get started with the
related APIs.

For a detailed list of new, modified, and removed APIs, read the
[API diff report](https://developer.android.com/sdk/api_diff/30/changes). For details on new APIs
visit the [Android API reference](https://developer.android.com/reference) --- new APIs are highlighted for
visibility. Also, to learn about areas where platform changes may
affect your apps, be sure to check out Android 11 behavior
changes [for apps that target Android R](https://developer.android.com/about/versions/11/behavior-changes-11)
and [for all apps](https://developer.android.com/about/versions/11/behavior-changes-all), as well as
[privacy changes](https://developer.android.com/about/versions/11/privacy).

## New experiences

### Device controls

Android 11 includes a new [`ControlsProviderService`](https://developer.android.com/reference/android/service/controls/ControlsProviderService) API that
you can use to expose controls for connected, external devices. These controls
appear under **Device controls** in the Android power menu. For more
information, see [Control external devices](https://developer.android.com/guide/topics/ui/device-control).

### Media Controls

Android 11 updates how media controls are displayed. Media controls appear near
quick settings. Sessions from multiple apps are arranged in a swipeable carousel
which includes streams playing locally on the phone, remote streams, such as
those detected on external devices or cast sessions, and previous, resumable
sessions in the order they were last played.

Users can restart previous sessions from the carousel without having to start
the app. When playback begins, the user interacts with the media controls in the usual
way.

For more information, see [media controls](https://developer.android.com/guide/topics/media/media-controls).

### Screens

#### Better support for waterfall displays

Android 11 provides several APIs to support *waterfall displays* ,
displays which
wrap around the edge of the device. These displays are treated as a variant of
displays with display cutouts. The existing
[`DisplayCutout`](https://developer.android.com/reference/android/view/DisplayCutout)`.getSafeInset...()`
methods now return the safe inset to avoid waterfall areas as well as cutouts.
To render your app content in the waterfall area, do the following:

- Call
  [`DisplayCutout.getWaterfallInsets()`](https://developer.android.com/reference/android/view/DisplayCutout#getWaterfallInsets())
  to get exact dimensions of the waterfall inset.

- Set the window layout attribute `layoutInDisplayCutoutMode` to
  [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS)
  to allow the window to extend into the cutout and waterfall areas on all edges
  of the screen. You must make sure that no essential content is in the cutout
  or waterfall areas.

| **Note:** If you do not set the window to `LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`, Android displays the window in letterboxed mode, avoiding the notch and waterfall areas.

#### Hinge angle sensor and foldables

Android 11 makes it possible for apps running on
devices with hinge-based screen configurations to
determine the angle of the hinge by providing a new sensor
with [`TYPE_HINGE_ANGLE`](https://developer.android.com/reference/android/hardware/Sensor#TYPE_HINGE_ANGLE),
and a new
[`SensorEvent`](https://developer.android.com/reference/android/hardware/SensorEvent) that can monitor
the hinge angle and provides a measurement in degrees between two
integral parts of the device. You can use these raw measurements to perform
granular animations as the user manipulates the device.

See [Foldables](https://developer.android.com/guide/topics/ui/foldables#hinge_angle).

### Conversations

#### Conversation improvements

Android 11 makes a number of improvements to the way
*conversations* are handled. Conversations are real-time, bidirectional
communications between two or more people. These conversations are given special
prominence, and users have several new options in how to interact with them.

For more information about conversations and how your app can support them, see
[People and conversations](https://developer.android.com/guide/topics/ui/conversations).

#### Chat Bubbles

[Bubbles](https://developer.android.com/guide/topics/ui/bubbles) are now available to developers to
help surface conversations across the system.
Bubbles was an experimental feature in Android 10 that was enabled through
a developer option; in Android 11, this is no longer necessary.

If an app targets Android 11 (API level 30) or higher, its notifications are not
presented as bubbles unless they fulfill the new
[conversation requirements](https://developer.android.com/guide/topics/ui/conversations). Specifically,
the notification must be associated with a shortcut.

Prior to Android 11, if you wanted a notification to be bubbled,
you needed to explicitly specify that the notification was set to always launch
in document UI mode. Beginning with Android 11, you no longer need
to explicitly make that setting; if the notification is bubbled, the platform
automatically sets the notification to always launch in document UI mode.

There are a number of improvements to bubble performance, and users have
more flexibility in enabling and disabling bubbles from each app. For
developers who implemented experimental support, there are a few changes to
the APIs in Android 11:

- The [`BubbleMetadata.Builder()`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#Notification.BubbleMetadata.Builder()) constructor with no parameters is deprecated. Instead, use either of the two new constructors [`BubbleMetadata.Builder(PendingIntent, Icon)`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#Notification.BubbleMetadata.Builder(android.app.PendingIntent,%20android.graphics.drawable.Icon)) or [`BubbleMetadata.Builder(String)`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata.Builder#Notification.BubbleMetadata.Builder(java.lang.String)).
- Create [`BubbleMetadata`](https://developer.android.com/reference/android/app/Notification.BubbleMetadata) from a shortcut ID by calling `BubbleMetadata.Builder(String)`. The string passed should match the shortcut ID provided to [`Notification.Builder`](https://developer.android.com/reference/android/app/Notification.Builder).
- Create bubble icons with [`Icon.createWithContentUri()`](https://developer.android.com/reference/android/graphics/drawable/Icon#createWithContentUri(java.lang.String)), or with the new method [`createWithAdaptiveBitmapContentUri()`](https://developer.android.com/reference/android/graphics/drawable/Icon#createWithAdaptiveBitmapContentUri(java.lang.String)).

### 5G visual indicators

For information on displaying 5G indicators on users' devices, see
[Tell your users when they're on
5G](https://developer.android.com/training/connectivity/5g/enhance-with-5g#indicator).

## Privacy

Android 11 introduces a large number of changes and
restrictions to enhance user privacy. To learn more, see the
[Privacy](https://developer.android.com/about/versions/11/privacy) page.

## Security

### Biometric authentication updates

To help you control the level of security for your app's data,
Android 11 provides several improvements to biometric
authentication. These changes also appear in the [Jetpack Biometric
library](https://developer.android.com/jetpack/androidx/releases/biometric).

#### Authentication types

Android 11 introduces the
[`BiometricManager.Authenticators`](https://developer.android.com/reference/kotlin/android/hardware/biometrics/BiometricManager.Authenticators)
interface, which you can use to [declare the types of authentication that your
app supports](https://developer.android.com/training/sign-in/biometric-auth#declare-supported-authentication-types).

#### Determine which authentication type was used

After the user authenticates, you can check whether the user authenticated using
a device credential or a biometric credential by calling
[`getAuthenticationType()`](https://developer.android.com/reference/kotlin/android/hardware/biometrics/BiometricPrompt.AuthenticationResult#getauthenticationtype).

#### Additional support for auth-per-use keys

Android 11 provides more support for [authentication using
auth-per-use keys](https://developer.android.com/training/sign-in/biometric-auth#auth-per-use-keys).

#### Deprecated methods

Android 11 deprecates the following methods:

- The `setDeviceCredentialAllowed()` method.
- The `setUserAuthenticationValidityDurationSeconds()` method.
- The overloaded version of `canAuthenticate()` that takes no arguments.

### Secure sharing of large datasets

In some situations, such as those that involve machine learning or media
playback, your app might want to use the same large dataset as another app. In
previous versions of Android, your app and another app would each need to
download a separate copy of the same dataset.

To help reduce data redundancy, both over the network and on disk,
Android 11 allows these large datasets to be cached on the
device using *shared data blobs* . To learn more about sharing datasets, see the
[in-depth guide on sharing large datasets](https://developer.android.com/about/versions/11/features/shared-datasets).

### Perform file-based encryption after an OTA restart without user credentials

After the device completes an OTA update and restarts, the Credential Encrypted
keys (CE) that are placed in credential-protected storage are immediately
available for [File-Based
Encryption (FBE)](https://source.android.com/security/encryption/file-based)
operations. This means that, after an OTA update, your app can resume operations
that require the CE keys before the user enters their PIN, pattern, or password.
| **Note:** This change only affects device restarts that occur because of an OTA update. If your app always needs access to CE keys before the user enters their PIN, pattern, or password following a device restart, continue to [support
| Direct Boot](https://developer.android.com/training/articles/direct-boot).

## Performance and quality

### Wireless debugging

Android 11 supports deploying and debugging your app wirelessly
from your workstation via Android Debug Bridge (adb). For example, you can
deploy your debuggable app to multiple remote devices without physically
connecting your device via USB and contending with common USB connection issues,
such as driver installation. For more information, see
[Run apps on a hardware device](https://developer.android.com/studio/run/device#wireless).

### ADB Incremental APK installation

Installing large (2GB+) APKs on a device can take a long time, even if only a
small change is made to an app. ADB (Android Debug Bridge) Incremental APK
installation accelerates this process by installing enough of the APK to launch
the app while streaming the remaining data in the background. `adb install` will
use this feature automatically if it is supported by the device and you have the
latest [SDK Platform-Tools](https://developer.android.com/studio/releases/platform-tools) installed. If it is
not supported, the default installation method is silently used.

Use the following [adb command](https://developer.android.com/studio/command-line/adb#incremental) to use the
feature. If the device does not support incremental installation, the command
fails and prints a verbose explanation.

`adb install --incremental`

Before running an ADB incremental APK install, you must sign your APK and create
an
[APK Signature Scheme v4 file](https://developer.android.com/studio/command-line/apksigner#v4-signing-enabled).
The v4 signature file must be placed next to the APK for this feature to work.

### Error detection using the native memory allocator

GWP-ASan is a native memory allocator feature that helps find use-after-free and
heap-buffer-overflow bugs. You can enable this feature globally or for specific
subprocesses of your app. To learn more, see the
[GWP-Asan guide](https://developer.android.com/ndk/guides/gwp-asan).

### Neural Networks API 1.3

Android 11 expands and improves the [Neural Networks
API (NNAPI)](https://developer.android.com/ndk/guides/neuralnetworks).

#### New operations

NNAPI 1.3 introduces a new operand type, `TENSOR_QUANT8_ASYMM_SIGNED`, to
support [TensorFlow Lite's new quantization
scheme](https://www.tensorflow.org/lite/performance/quantization_spec).

Additionally, NNAPI 1.3 introduces the following new operations:

- `QUANTIZED_LSTM`
- `IF`
- `WHILE`
- `ELU`
- `HARD_SWISH`
- `FILL`
- `RANK`

#### New ML controls

NNAPI 1.3 introduces new controls to help machine learning run smoothly:

- **QoS API:** The new Quality of Service API includes support for
  prioritization and task deadlines in NNAPI with the following new functions:

  - [`ANeuralNetworksDevice_wait()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksdevice_wait)
  - [`ANeuralNetworksCompilation_setPriority()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworkscompilation_setpriority)
  - [`ANeuralNetworksCompilation_setTimeout()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworkscompilation_settimeout)
  - [`ANeuralNetworksExecution_setTimeout()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksexecution_settimeout)
- **Memory domain input/output:** NNAPI 1.3 includes support for memory domains
  as input and output to execution. This removes unnecessary copies of the same
  data among different system components, improving the runtime performance of
  Android neural networks. This feature adds a set of new NDK APIs for use with
  [`ANeuralNetworksMemoryDesc`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ga92661bd0904009e8d0c9e8e1bf40bd84)
  and
  [`ANeuralNetworkMemory`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ga9a6b7719f0613ba9e2c93cffd97ebfc0)
  objects, including the following functions:

  - [`ANeuralNetworksMemoryDesc_create()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_create)
  - [`ANeuralNetworksMemoryDesc_free()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_free)
  - [`ANeuralNetworksMemoryDesc_addInputRole()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_addinputrole)
  - [`ANeuralNetworksMemoryDesc_addOutputRole()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_addoutputrole)
  - [`ANeuralNetworksMemoryDesc_setDimensions()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_setdimensions)
  - [`ANeuralNetworksMemoryDesc_finish()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemorydesc_finish)
  - [`ANeuralNetworksMemory_createFromDesc()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemory_createfromdesc)
  - [`ANeuralNetworksMemory_copy()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmemory_copy)

  To learn more, see the [neural network memory domain
  sample](https://github.com/android/ndk-samples/tree/develop/nn-samples/sequence).
- **Dependency API and sync fence support:** NNAPI 1.3 includes support for
  asynchronous compute with dependencies, allowing greatly reduced overhead when
  invoking small chained models. This feature adds the following new functions:

  - [`ANeuralNetworksEvent_createFromSyncFenceFd()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksevent_createfromsyncfencefd)
  - [`ANeuralNetworksEvent_getSyncFenceFd()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksevent_getsyncfencefd)
  - [`ANeuralNetworksExecution_startComputeWithDependencies()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksexecution_startcomputewithdependencies)
- **Control flow:** NNAPI 1.3 includes support for general control flow with the
  new graph operations `ANEURALNETWORKS_IF` and `ANEURALNETWORKS_WHILE`, which
  accept other models as arguments using the new `ANEURALNETWORKS_MODEL` operand
  type. Additionally, this feature adds the following new functions:

  - [`ANeuralNetworksModel_setOperandValueFromModel()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksmodel_setoperandvaluefrommodel)
  - [`ANeuralNetworks_getDefaultLoopTimeout()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworks_getdefaultlooptimeout)
  - [`ANeuralNetworks_getMaximumLoopTimeout()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworks_getmaximumlooptimeout)
  - [`ANeuralNetworksExecution_setLoopTimeout()`](https://developer.android.com/ndk/reference/group/neural-networks#aneuralnetworksexecution_setlooptimeout)

#### NDK Thermal API

When devices get too warm, they may throttle the CPU and/or GPU, and this can
affect apps in unexpected ways. Apps or games that incorporate complex graphics,
heavy computation, or sustained network activity are more likely to encounter
issues.

Use the [NDK Thermal API](https://developer.android.com/ndk/reference/group/thermal) in
Android 11 to monitor temperature changes on the device, and then
take action to maintain lower power usage and cooler device temperature. This
API is similar to the [Java Thermal API](https://developer.android.com/about/versions/10/features#thermal); you can
use it to receive notifications for any thermal status change or to poll
the current status directly.

### Text and input

#### Improved IME transitions

Android 11 introduces new APIs to improve transitions for input method editors
(IMEs), such as on-screen keyboards. These APIs make it easier to adjust your
app's content in synchronization with the IME's appearance and disappearance,
and with other elements like the status and navigation bars.

To show an IME while any `EditText` has the focus, call
`view.getInsetsController().`[show(Type.ime())](https://developer.android.com/reference/android/view/WindowInsetsController#show(int)).
(You can call this method on any view in
the same hierarchy as the focused `EditText`, you don't have to call
it on the `EditText` specifically.) To hide the IME, call
`view.getInsetsController().`[hide(Type.ime())](https://developer.android.com/reference/android/view/WindowInsetsController#hide(int)).
You can check whether an IME is currently visible by calling
`view.getRootWindowInsets().`[isVisible(Type.ime())](https://developer.android.com/reference/android/view/WindowInsets#isVisible(int)).

To synchronize your app's views with the appearance and disappearance of the IME, set a listener on a view by providing a
[`WindowInsetsAnimation.Callback`](https://developer.android.com/reference/android/view/View#setWindowInsetsAnimationCallback(android.view.WindowInsetsAnimation.Callback))
to [`View.setWindowInsetsAnimationCallback()`](https://developer.android.com/reference/android/view/View#setWindowInsetsAnimationCallback(android.view.WindowInsetsAnimation.Callback)).
(You can set this listener on *any* view, it doesn't have to be an `EditText`.)
The IME calls your listener's
[`onPrepare()`](https://developer.android.com/reference/android/view/WindowInsetsAnimation.Callback#onPrepare(android.view.WindowInsetsAnimation))
method, then it calls
[`onStart()`](https://developer.android.com/reference/android/view/WindowInsetsAnimation.Callback#onStart(android.view.WindowInsetsAnimation,%20android.view.WindowInsetsAnimation.Bounds))
at the beginning of the transition. It then calls
[`onProgress()`](https://developer.android.com/reference/android/view/WindowInsetsAnimation.Callback#onProgress(android.view.WindowInsets,%20java.util.List%3Candroid.view.WindowInsetsAnimation%3E))
at each progression in the transition. When the transition has finished, the IME calls
[`onEnd()`](https://developer.android.com/reference/android/view/WindowInsetsAnimation.Callback#onEnd(android.view.WindowInsetsAnimation)).
At any point in the transition, you can find out how much progress the transition has made by calling
[`WindowInsetsAnimation.getFraction()`](https://developer.android.com/reference/android/view/WindowInsetsAnimation#getFraction()).

For an example of how to use these APIs, see the new
[WindowInsetsAnimation](https://github.com/android/user-interface-samples/tree/main/WindowInsetsAnimation)
code sample.

##### Controlling the IME animation

You can also take control of the IME animation, or the animation of another
system bar like the navigation bar. To do this, first call
[`setOnApplyWindowInsetsListener()`](https://developer.android.com/reference/android/view/View#setOnApplyWindowInsetsListener(android.view.View.OnApplyWindowInsetsListener))
to set a new listener for window inset changes:  

### Kotlin

```kotlin
rootView.setOnApplyWindowInsetsListener { rootView, windowInsets ->
    val barsIme = windowInsets.getInsets(Type.systemBars() or Type.ime())
    rootView.setPadding(barsIme.left, barsIme.top, barsIme.right, 
                          barsIme.bottom)

      // We return the new WindowInsets.CONSUMED to stop the insets being
      // dispatched any further into the view hierarchy. This replaces the
      // deprecated WindowInsets.consumeSystemWindowInsets() and related
      // functions.
    WindowInsets.CONSUMED
}
```

### Java

```java
mRoot.setOnApplyWindowInsetsListener(new View.OnApplyWindowInsetsListener() {
   @Override
   public WindowInsets onApplyWindowInsets(View v, WindowInsets insets) {

       Insets barsIME = insets.getInsets(Type.systemBars() | Type.ime());
       mRootView.setPadding(barsIme.left, barsIme.top, barsIme.right,
                             barsIme.bottom);

      // We return the new WindowInsets.CONSUMED to stop the insets being
      // dispatched any further into the view hierarchy. This replaces the
      // deprecated WindowInsets.consumeSystemWindowInsets() and related
      // functions.
       return WindowInsets.CONSUMED;
   }
});
```

To move the IME or other system bar, call the controller's
[`controlWindowInsetsAnimation()`](https://developer.android.com/reference/android/view/WindowInsetsController#controlWindowInsetsAnimation(int,%20long,%20android.view.animation.Interpolator,%20android.view.WindowInsetsAnimationControlListener))
method:  

### Kotlin

```kotlin
view.windowInsetsController.controlWindowInsetsAnimation(
       Type.ime(),
       1000,
       LinearInterpolator(),
       cancellationSignal,
       object : WindowInsetsAnimationControlListener() {
           fun onReady(controller: WindowInsetsAnimationController,
                         types: Int) {
               // update IME inset
             controller.setInsetsAndAlpha(Insets.of(0, 0, 0, inset),
                           1f /* alpha */, 0.1 /* fraction progress */)
           }
       }
);
```

### Java

```java
mRoot.getWindowInsetsController().controlWindowInsetsAnimation(
       Type.ime(), 1000, new LinearInterpolator(), cancellationSignal,
       new WindowInsetsAnimationControlListener() {
           @Override
           public void onReady(
                   @NonNull WindowInsetsAnimationController controller,
                   int types
                   ) {
                   // update IME inset
                   controller.setInsetsAndAlpha(Insets.of(0, 0, 0, inset),
                           1f /* alpha */, 0.1 /* fraction progress */);
           }

           @Override
           public void onCancelled() {}
       });
```

#### Updates to the ICU libraries

Android 11 updates the `android.icu` package to use version 66
of the
[ICU library](http://site.icu-project.org/), compared to version
63 in Android 10. The new library version includes updated CLDR locale data
and a number of enhancements to internationalization support in Android.

Notable changes in the new library versions include the following:

- Many formatting APIs now support a new return object type that extends `FormattedValue`.
- The `LocaleMatcher` API is enhanced with a builder class, support for the [`java.util.Locale`](https://developer.android.com/reference/kotlin/java/util/Locale) type, and a result class featuring additional data about a match.
- Unicode 13 is now supported.

### Media

#### Allocating MediaCodec buffers

Android 11 includes a new `MediaCodec` APIs that gives
apps more control when allocating input and output buffers. This lets your
app manage memory more efficiently.

##### New classes:

- [`MediaCodec.LinearBlock`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.LinearBlock)
- [`MediaCodec.OutputFrame`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.OutputFrame)
- [`MediaCodec.QueueRequest`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.QueueRequest)

##### New methods:

- [`MediaCodec.getQueueRequest()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec#getQueueRequest(kotlin.Int))
- [`MediaCodec.getOutputFrame()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec#getOutputFrame(kotlin.Int))
- [`MediaCodec.LinearBlock.isCodecCopyFreeCompatible()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.LinearBlock#isCodecCopyFreeCompatible(kotlin.Array))

In addition, the behavior of two methods in [`MediaCodec.Callback()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.Callback) have changed:

[`onInputBufferAvailable()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.Callback#onInputBufferAvailable(android.media.MediaCodec,%20kotlin.Int))
:   Instead of calling `MediaCodec.getInputBuffer()` and
    `MediaCodec.queueInputBuffer()` with the index, if configured to use the Block
    Model API, apps should use `MediaCodec.getQueueRequest` with the index, attaching
    a LinearBlock/HardwareBuffer to the slot.

[`onOutputBufferAvailable()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec.Callback#onOutputBufferAvailable(android.media.MediaCodec,%20kotlin.Int,%20android.media.MediaCodec.BufferInfo))
:   Instead of calling `MediaCodec.getOutputBuffer()` with the index,
    apps may use `MediaCodec.getOutputFrame()` with the index to get the `OutputFrame`
    object with more information and LinearBlock/HardwareBuffer buffers.

#### Low-latency decoding in MediaCodec

Android 11 enhances
[`MediaCodec`](https://developer.android.com/reference/kotlin/android/media/MediaCodec)
to support low-latency decoding for games and other real-time apps. You can
check whether a codec supports low-latency decoding by passing
[`FEATURE_LowLatency`](https://developer.android.com/reference/kotlin/android/media/MediaCodecInfo.CodecCapabilities#feature_lowlatency)
to
[`MediaCodecInfo.CodecCapabilities.isFeatureSupported()`](https://developer.android.com/reference/kotlin/android/media/MediaCodecInfo.CodecCapabilities#isfeaturesupported).

To turn low-latency decoding on or off, do either of the following:

- Set the new key [`KEY_LOW_LATENCY`](https://developer.android.com/reference/kotlin/android/media/MediaFormat#key_low_latency) to 0 or 1 using [`MediaCodec.configure()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec#configure).
- Set the new parameter key [`PARAMETER_KEY_LOW_LATENCY`](https://developer.android.com/reference/kotlin/android/media/MediaCodec#parameter_key_low_latency) to 0 or 1 using [`MediaCodec.setParameters()`](https://developer.android.com/reference/kotlin/android/media/MediaCodec#setparameters).

| **Note:** Supporting low-latency decoding can require additional resources, such as higher power consumption. Use low-latency decoding only when necessary.

#### New AAudio function AAudioStream_release()

The function
[`AAudioStream_close()`](https://developer.android.com/ndk/reference/group/audio#group___audio_1gad5f5e59999bb4f4b5ec6f5efcd09520b)
releases and closes an audio stream at the same time. This can be dangerous. If
another process tries to access the stream after it's been closed, the process
will crash.

The new function
[`AAudioStream_release()`](https://developer.android.com/ndk/reference/group/audio#group___audio_1ga3a3f524d1a36022ff0300699bb0c8f7b)
releases the stream but does not close it. This frees its resources and leaves
the stream in a known state. The object persists until you call
`AAudioStream_close()`.

#### MediaParser API

[MediaParser](https://developer.android.com/reference/android/media/MediaParser) is a new low level API for
media extraction. It is more flexible than
[MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor) and provides additional
control over media extraction functionality.

#### Audio capture from a USB device

When an application without [`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO) permission uses [`UsbManager`](https://developer.android.com/reference/android/hardware/usb/UsbManager#openDevice(android.hardware.usb.UsbDevice)) to request direct access to a USB audio device with audio capture
capability (such as a USB headset), a new warning message appears asking the
user to confirm permission to use the device. The system ignores any "always
use" option, so the user must acknowledge the warning and grant permission every
time an app requests access.

To avoid this behavior, your app should request the `RECORD_AUDIO` permission.
| **Note:** This behavior only applies to apps that connect directly to USB peripherals using the [`UsbManager` API](https://developer.android.com/reference/android/hardware/usb/UsbManager#openDevice(android.hardware.usb.UsbDevice)). The vast majority of media players, games, and communication apps use the Audio APIs and aren't affected by this change.

#### Concurrent mic access

Android 11 adds new methods to the `AudioRecord`, `MediaRecorder`, and
`AAudioStream` APIs. These methods enable and disable the ability to capture concurrently
regardless of the selected use case. See [Sharing Audio Input](https://developer.android.com/guide/topics/media/sharing-audio-input#concurrent-capture-r).

#### Output switcher

Android 11 implements new behavior for apps that use the
cast and mediarouter APIs.

In addition to accessing casting options from within an app the switching
options also appear in the system media player. This helps to give the user a
seamless journey when moving between devices as they change their viewing and
listening contexts, such as watching video in the kitchen versus on a phone,
or listening to audio in the home or car. See [the output switcher](https://developer.android.com/guide/topics/media/media-routing#output-switcher).

### Connectivity

#### Wi-Fi Passpoint enhancements

For information on Passpoint capabilities added in Android 11, see
[Passpoint](https://developer.android.com/guide/topics/connectivity/passpoint).

#### Wi-Fi Suggestion API is expanded

Android 11 expands the
[Wi-Fi Suggestion API](https://developer.android.com/guide/topics/connectivity/wifi-suggest)
to increase your app's network management capabilities, including the following:

- Connectivity management apps can manage their own networks by allowing disconnection requests.
- Passpoint networks are integrated into the Suggestion API and can be suggested to the user.
- Analytics APIs enable you to get information about the quality of your networks.

#### CallScreeningService updates

Starting in Android 11, a
[CallScreeningService](https://developer.android.com/reference/android/telecom/CallScreeningService) can
request
information about the STIR/SHAKEN verification status (verstat) for incoming
calls. This information is provided as part of the
[call details](https://developer.android.com/reference/android/telecom/Call.Details)
for incoming calls.

If a `CallScreeningService` holds the
[`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)
permission, the app is notified when there are incoming calls from, or
outgoing calls to, a number in the user's contacts.

For more information, see [Prevent caller ID
spoofing](https://developer.android.com/guide/topics/connectivity/telecom/prevent-spoofing).

#### Open Mobile API updates

For information on OMAPI support on Android 11 and higher, see [Open Mobile API
reader support](https://developer.android.com/guide/topics/connectivity/omapi).

#### Performant VPNs

Apps that target API level 30 and higher or that are running
on devices launched on API level 29 and higher can apply IKEv2/IPsec to VPNs for
both user-configured and app-based VPNs.

The VPNs run native to the operating system, simplifying the code required to
establish IKEv2/IPsec VPN connections in an app.

#### Per-process network access control

For information on enabling network access on a per-process basis, see [Manage
network usage](https://developer.android.com/training/basics/network-ops/managing#manage-usage).

#### Allow multiple installed Passpoint configurations with the same FQDN

Starting in Android 11, you can use
[`PasspointConfiguration.getUniqueId()`](https://developer.android.com/reference/android/net/wifi/hotspot2/PasspointConfiguration#getUniqueId())
to get a unique identifier for a `PasspointConfiguration` object, which enables
your app's users to install multiple profiles with the same fully qualified
domain name (FQDN).

This functionality is helpful when a carrier deploys more than one combination
of Mobile Country Code (MCC) and Mobile Network Code (MNC) on their network, but
has only a single FQDN. On Android 11 and higher, it is possible
to install more than one profile with the same FQDN that will match the network
as the Home provider when the user installs a SIM with either MCC or MNC.
| **Note:** Each configuration is identified by a unique key that depends on the content of the configuration. In order to update an existing profile, you must remove it using [`WifiManager.removePasspointConfiguration()`](https://developer.android.com/reference/android/net/wifi/WifiManager#removePasspointConfiguration(java.lang.String)). Not removing the existing configuration will cause a new profile to be added with both configurations.

#### GNSS antenna support

Android 11 introduces the
[`GnssAntennaInfo`](https://developer.android.com/reference/kotlin/android/location/GnssAntennaInfo) class, which makes it
possible for your app to make more use of centimeter-accuracy positioning that
the Global Navigation Satellite System (GNSS) can provide.

Learn more in the guide on [antenna calibration
information](https://developer.android.com/guide/topics/sensors/gnss#antenna-calibration-information).

### Graphics

#### NDK image decoder

The NDK [`ImageDecoder`](https://developer.android.com/ndk/reference/group/image-decoder) API provides a
standard API for Android C/C++ apps to decode images directly. App developers no
longer need to use the framework APIs (via JNI) or bundle third-party
image-decoding libraries. For more information, see the
[Image decoder developer guide](https://developer.android.com/ndk/guides/image-decoder).

#### Frame rate API

Android 11 provides an API that enables apps to inform the system
of their intended frame rate, to reduce judder on devices that support multiple
refresh rates. For information on how to use this API, see the
[Frame rate guide](https://developer.android.com/guide/topics/media/frame-rate).

#### Requesting and checking for low latency support

Certain displays can perform graphics post-processing, such as some external
displays and TVs. This post-processing improves the graphics but can
increase latency. Newer displays which support HDMI 2.1 have an *auto low
latency mode* (*ALLM* , also known as *game mode* ), which minimizes latency by
switching off this post-processing. For more details on ALLM, refer to the
[HDMI 2.1 specification](https://www.hdmi.org/spec/hdmi2_1).

A window can request that auto low latency mode be used, if it is available.
ALLM is particularly useful for applications like games and videoconferencing,
where low latency is more important than having the best possible graphics.

To toggle minimal post-processing on or off, call
[`Window.setPreferMinimalPostProcessing()`](https://developer.android.com/reference/android/view/Window#setPreferMinimalPostProcessing(boolean)),
or set the window's
[`preferMinimalPostProcessing`](https://developer.android.com/reference/android/R.attr#preferMinimalPostProcessing)
attribute to `true`. Not all displays support minimal
post-processing; to find out if a particular display does support it, call the
new method
[`Display.isMinimalPostProcessingSupported()`](https://developer.android.com/reference/android/view/Display#isMinimalPostProcessingSupported()).
| **Note:** If the user disables minimal post-processing, or if the display does not support low latency mode, calling `Window.setPreferMinimalPostProcessing()` has no effect.

#### Performant graphics debug layer injection

Applications can now load external graphics layers
([GLES](https://developer.android.com/ndk/guides/rootless-debug-gles),
[Vulkan](https://developer.android.com/ndk/guides/graphics/validation-layer)) into native application code to
expose the same functionality as a debuggable app, but without incurring the
performance overhead. This feature is especially important when profiling your
application with tools like [GAPID](https://gapid.dev/). To profile
your app, include the following
[meta-data element](https://developer.android.com/guide/topics/manifest/meta-data-element) in your app
manifest file instead of making the application debuggable:  

```xml
<application ... >
    <meta-data android:name="com.android.graphics.injectLayers.enable"
                  android:value="true" />
</application>
```

### Images and camera

#### Mute notification sounds and vibrations during active capture

Beginning with Android 11, when actively using the camera, your
app can mute only vibrations, both sounds and vibrations, or neither using
[`setCameraAudioRestriction()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#setCameraAudioRestriction(int)).

#### Expanded camera support in Android emulator

For information on the expanded support for cameras in the emulator starting
with Android 11, see [Camera support](https://developer.android.com/studio/run/advanced-emulator-usage#camera).

### Support for concurrent use of more than one camera

Android 11 adds APIs to query support for using more
than one camera at a time, including both a front-facing and rear-facing camera.

To check for support on the device on which your app is running, use the
following methods:

- [`getConcurrentCameraIds()`](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds()) returns a `Set` of combinations of camera IDs that can stream concurrently with guaranteed stream combinations when configured by the same application process.
- [`isConcurrentSessionConfigurationSupported()`](https://developer.android.com/reference/android/hardware/camera2/CameraManager#isConcurrentSessionConfigurationSupported(java.util.Map%3Cjava.lang.String,%20android.hardware.camera2.params.SessionConfiguration%3E)) queries whether camera devices can concurrently support the corresponding session configurations.

#### Better support for HEIF images with multiple frames

Beginning with Android 11, if you call [`ImageDecoder.decodeDrawable()`](https://developer.android.com/reference/android/graphics/ImageDecoder#decodeDrawable(android.graphics.ImageDecoder.Source)) and pass an HEIF image containing a sequence of frames (such as an animation or a burst photo), the method returns an [`AnimatedImageDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable) containing the entire image sequence. On earlier versions of Android, the method returned a `BitmapDrawable` of just a single frame.

If the HEIF graphic contains multiple frames that are not in a sequence, you can retrieve an individual frame by calling [`MediaMetadataRetriever.getImageAtIndex()`](https://developer.android.com/reference/android/media/MediaMetadataRetriever#getImageAtIndex(int)).

### Accessibility

#### Updates for accessibility service developers

If you create a custom accessibility service, you can use the following
features in Android 11:

- The user-facing explanation of an accessibility service now allows for HTML and images in addition to plain text. This flexibility makes it easier to explain to end-users what your service does and how it can help them.
- To work with a description of a UI element's state that's more semantically meaningful than `contentDescription`, call the `getStateDescription()` method.
- To request that touch events bypass the system's touch explorer, call [`setTouchExplorationPassthroughRegion()`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityService#setTouchExplorationPassthroughRegion). Similarly, to request that gestures bypass the system's gesture detector, call [`setGestureDetectionPassthroughRegion()`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityService#setGestureDetectionPassthroughRegion(kotlin.Int,%20android.graphics.Region)).
- You can request IME actions, such as "enter" and "next", as well as screenshots of windows that don't enable the `FLAG_SECURE` flag.

## Additional features

### App process exit reasons

Android 11 introduces the
[`ActivityManager.getHistoricalProcessExitReasons()`](https://developer.android.com/reference/kotlin/android/app/ActivityManager#gethistoricalprocessexitreasons)
method, which reports the reasons for any recent process terminations. Apps can
use this method to gather crash diagnostic information, such as whether a
process termination is due to ANRs, memory issues, or other reasons.
Additionally, you can use the new
[`setProcessStateSummary()`](https://developer.android.com/reference/android/app/ActivityManager#setProcessStateSummary(byte%5B%5D))
method to store custom state information for later analysis.

The `getHistoricalProcessExitReasons()` method returns instances of the
[`ApplicationExitInfo`](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo)
class, which contains information related to an app process's death. By calling
`getReason()` on an instance of this class, you can determine why your app's
process was killed. For example, a return value of `REASON_CRASH` indicates that
an unhandled exception occurred in your app. If your app needs to ensure
uniqueness for exit events, it can maintain an app-specific identifier, such as
a hash value based on the timestamp from the
[`getTimestamp()`](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo#gettimestamp)
method.
| **Note:** Some devices cannot report low-memory kills. On these devices, the `getHistoricalProcessExitReasons()` method returns `REASON_SIGNALED` instead of `REASON_LOW_MEMORY`, and the return value of [`getStatus()`](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo#getstatus) is `SIGKILL`.  
|
| To check whether a device can report low-memory kills, call [`ActivityManager.isLowMemoryKillReportSupported()`](https://developer.android.com/reference/kotlin/android/app/ActivityManager#islowmemorykillreportsupported).

#### Additional resources

For more information, read the article about [new Android 11 tools to make
apps more private and
stable](https://medium.com/androiddevelopers/new-android-11-tools-to-make-apps-more-private-and-stable-c9dcea0af415) on Medium.

### Resource loaders

Android 11 introduces a new API that allows apps to dynamically
extend how resources are searched and loaded. The new API classes
[`ResourcesLoader`](https://developer.android.com/reference/kotlin/android/content/res/loader/ResourcesLoader)
and
[`ResourcesProvider`](https://developer.android.com/reference/kotlin/android/content/res/loader/ResourcesProvider)
are primarily responsible for providing the new functionality. Together, they
provide the ability to supply additional resources and assets, or modify the
values of existing resources and assets.

`ResourcesLoader` objects are containers that supply `ResourcesProvider` objects
to an app's
[`Resources`](https://developer.android.com/reference/kotlin/android/content/res/Resources) instance. In
turn, `ResourcesProvider` objects provide methods to load resource data from
APKs and resource tables.

One primary use case for this API is custom asset loading. You can use
[`loadFromDirectory()`](https://developer.android.com/reference/kotlin/android/content/res/loader/ResourcesProvider#loadfromdirectory)
to create a `ResourcesProvider` that redirects the resolution of file-based
resources and assets, causing it to search a specific directory rather than the application
APK. You can access these assets through the `open()` family of methods from the
[`AssetManager`](https://developer.android.com/reference/kotlin/android/content/res/AssetManager)
API class, just like with assets bundled in the APK.

### APK signature scheme v4

Android 11 adds support for [APK Signature Scheme v4](https://developer.android.com/studio/command-line/apksigner#v4-signing-enabled). This scheme
produces a new kind of signature in a separate file (<var translate="no">apk-name</var>`.apk.idsig`) but
is otherwise similar to v2 and v3. No changes are made to the APK. This scheme supports
[ADB incremental APK installation](https://developer.android.com/about/versions/11/features#incremental), which speeds up APK install.

### Dynamic intent filters

In order to receive intents, an app must declare at compile time which types of
data it is able to receive by defining an
[intent filter](https://developer.android.com/guide/components/intents-filters#Receiving) in the app
manifest. In Android 10 and lower, apps have no way of changing their intent
filters at runtime. This is a problem for virtualization apps (such as virtual
machines and remote desktops) because they have no way of knowing exactly what
software the user will install inside them.

Android 11 introduces MIME groups, a new manifest element which allows an app to
declare a dynamic set of MIME types in an intent filter and modify it
programmatically at runtime. To use a MIME group, include a data element in your
app manifest with the new `android:mimeGroup` attribute:  

```xml
<intent-filter>
  <action android:name="android.intent.action.SEND"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <data android:mimeGroup="myMimeGroup"/>
</intent-filter>
```

The value of the `android:mimeGroup` attribute is an arbitrary string ID that
identifies the MIME group at runtime. You can access and update the contents of
a MIME group by passing its ID to the following new methods in the
[`PackageManager`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager) API
class:

- [`getMimeGroup()`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#getmimegroup)
- [`setMimeGroup()`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#setmimegroup)

When you add a MIME type to a MIME group programmatically, it functions exactly
the same as a static MIME type explicitly declared in the manifest.
| **Note:** `mimeGroup` strings are defined on a per-package basis. Within the same package, you can use the same `mimeGroup` string in multiple intent filters or components to declare a MIME group that is shared between them. Different packages cannot share a MIME group, but they can use the same `mimeGroup` string without interfering with each other.

### Autofill enhancements

Android 11 introduces improvements for autofill services.

#### Hint identifiers in AssistStructure.ViewNode

It is often useful for autofill services to compute a signature hash for a view
based on the view's properties. The
[view hint](https://developer.android.com/guide/topics/text/autofill-optimize#hints) is a particularly good
property to include when computing a signature hash, but the hint string might
change with the phone's locale. To solve this problem, Android 11
expands
[`AssistStructure.ViewNode`](https://developer.android.com/reference/android/app/assist/AssistStructure.ViewNode)
with a new
[`getHintIdEntry()`](https://developer.android.com/reference/android/app/assist/AssistStructure.ViewNode#getHintIdEntry())
method, which returns the resource identifier for a view's hint text. This
method provides a locale-independent value that you can use to compute signature
hashes.

#### Datasets shown events

To help autofill services improve their suggestions, Android 11 provides a way
to identify cases where an autofill service presented datasets but the user did
not select any of them. In Android 11,
[`FillEventHistory`](https://developer.android.com/reference/kotlin/android/service/autofill/FillEventHistory)
reports a new
[`TYPE_DATASETS_SHOWN`](https://developer.android.com/reference/android/service/autofill/FillEventHistory.Event#TYPE_DATASETS_SHOWN)
event type. `FillEventHistory` logs an event of this type whenever the autofill
service presents one or more datasets to the user. Autofill services can use
these events in conjunction with the existing
[`TYPE_DATASET_SELECTED`](https://developer.android.com/reference/android/service/autofill/FillEventHistory.Event#TYPE_DATASET_SELECTED)
event to determine whether the user selected any of the provided autofill
options.

#### IME integration

Keyboards and other IMEs can now display autofill suggestions inline, in a
suggestion strip or similar interface, instead of in a drop-down menu.
To protect sensitive information like passwords and credit-card numbers,
the suggestions are displayed to the user but are not known to the IME until
the user selects one. For information on how IMEs and password managers can
support this feature, see
[Integrating autofill with keyboards](https://developer.android.com/guide/topics/text/ime-autofill).

### Data sharing with content capture service

Starting in Android 11, your app can share data with the device's
content capture service. This capability makes it easier for a device to deliver
in-context intelligence, such as showing the name of a song that's currently
playing in the user's environment.

To make data from your app available to the content capture service, call the
[`shareData()`](https://developer.android.com/reference/kotlin/android/view/contentcapture/ContentCaptureManager#sharedata)
method on an instance of `ContentCaptureManager`. If the system accepts the
data-sharing request, your app receives a write-only file descriptor to share
with the content capture service.