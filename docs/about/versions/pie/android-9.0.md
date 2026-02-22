---
title: https://developer.android.com/about/versions/pie/android-9.0
url: https://developer.android.com/about/versions/pie/android-9.0
source: md.txt
---

Android 9 (API level 28) introduces great new features and capabilities for
users and developers. This document highlights what's new for developers.

To learn about the new APIs, read the
[API diff report](https://developer.android.com/sdk/api_diff/28/changes) or visit the
[Android API reference](https://developer.android.com/reference/packages). Also be sure to check out
[Android 9 Behavior Changes](https://developer.android.com/about/versions/pie/android-9.0-changes-all) to learn
about areas where platform changes may affect your apps.

## Indoor positioning with Wi-Fi RTT

![New RTT APIs support indoor positioning in your apps.](https://developer.android.com/static/images/about/versions/pie/rtt-nav.png)

Android 9 adds platform support for the IEEE 802.11-2016 Wi-Fi
protocol---also known as *Wi-Fi Round-Trip-Time* (RTT)---to let you take advantage
of indoor positioning in your apps.

On devices running Android 9 with hardware support, your apps can use the
[RTT APIs](https://developer.android.com/reference/android/net/wifi/rtt/package-summary) to measure the
distance to nearby RTT-capable Wi-Fi *access points* (APs). The device must have
location services enabled and Wi-Fi scanning turned on (under
**Settings \> Location** ), and your app must have the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission. The device doesn't need to connect to the access points to use RTT.
To maintain privacy, only the phone is able to determine the distance to the
access point; the access points do not have this information.

If your device measures the distance to 3 or more access points, you can use a
multilateration algorithm to estimate the device position that best fits those
measurements. The result is typically accurate within 1 to 2 meters.

With this accuracy, you can build new experiences, like in-building navigation
and fine-grained location-based services, such as disambiguated voice control
(for example, *"Turn on this light"* ) and location-based information (such as
*"Are there special offers for this product?"*).

See the WiFi RTT API in use in the
[Android WifiRttScan](https://github.com/android/connectivity-samples/tree/main/WifiRttScan) demo app.

For more information, see
[Wi-Fi location: ranging with RTT](https://developer.android.com/guide/topics/connectivity/wifi-rtt).

## Display cutout support

![Developer options screen showing different cutout sizes](https://developer.android.com/static/images/about/versions/pie/emulator-devoptions-cutout_2x.png)

Testing display cutout by using emulator

Android 9 offers support for the latest edge-to-edge screens
that contain display cutouts for cameras and speakers. The
[`DisplayCutout`](https://developer.android.com/reference/android/view/DisplayCutout)
class lets you find out the location and shape of the non-functional areas where
content shouldn't be displayed. To determine the existence and placement of
these cutout areas, use the
[`getDisplayCutout()`](https://developer.android.com/reference/android/view/WindowInsets#getDisplayCutout())
method.

A new window layout attribute,
[`layoutInDisplayCutoutMode`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#layoutInDisplayCutoutMode),
allows your app to lay out its content around a device's cutouts. You can set
this attribute to one of the following values:

- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT)
- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES)
- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER)

You can simulate a screen cutout on any device or emulator running Android 9
as follows:

1. Enable [developer options](https://developer.android.com/studio/debug/dev-options).
2. In the **Developer options** screen, scroll down to the **Drawing** section and select **Simulate a display with a cutout**.
3. Select the size of the cutout.

| **Note:** We recommend that you test the content display around the cutout area by using a device or emulator running Android 9.

## Notifications

Android 9 introduces several enhancements to notifications, all of which are
available to developers targeting API level 28 and above.
![Messaging notifications](https://developer.android.com/static/images/about/versions/pie/p-messaging.jpg)

MessagingStyle with photo attached.
![Messaging notification](https://developer.android.com/static/images/about/versions/pie/p-replies.jpg)

MessagingStyle with replies and conversation.

<br />

For sample code that uses notifications, including Android 9 features, see the
[People
Sample](https://github.com/android/user-interface-samples/tree/main/People).

### Enhanced messaging experience

Starting in Android 7.0 (API level 24), you could add an action to reply to
messages or enter other text directly from a notification. Android 9 enhances
this feature with the following enhancements:

- Simplified support for conversation participants: The
  [`Person`](https://developer.android.com/reference/android/app/Person)
  class is used to identify people involved in a conversation, including their
  avatars and URIs. Many other APIs, such as
  [`addMessage()`](https://developer.android.com/reference/android/app/Notification.MessagingStyle#addMessage(java.lang.CharSequence,%20long,%20android.app.Person)),
  now leverage the `Person` class instead of a `CharSequence`. The `Person` class
  also supports the Builder design pattern.

- Support for images: Android 9 now displays images in Messaging Notifications
  on phones. You can use
  [`setData()`](https://developer.android.com/reference/android/app/Notification.MessagingStyle.Message#setData(java.lang.String,%20android.net.Uri))
  on the message to display an image. The following code snippet demonstrates how
  to create a `Person` and a message containing an image.

### Kotlin

```kotlin
// Create new Person.
val sender = Person()
        .setName(name)
        .setUri(uri)
        .setIcon(null)
        .build()
// Create image message.
val message = Message("Picture", time, sender)
        .setData("image/", imageUri)
val style = Notification.MessagingStyle(getUser())
        .addMessage("Check this out!", 0, sender)
        .addMessage(message)
```

### Java

```java
// Create new Person.
Person sender = new Person()
        .setName(name)
        .setUri(uri)
        .setIcon(null)
        .build();
// Create image message.
Message message = new Message("Picture", time, sender)
        .setData("image/", imageUri);
Notification.MessagingStyle style = new Notification.MessagingStyle(getUser())
        .addMessage("Check this out!", 0, sender)
        .addMessage(message);
```

- Save replies as drafts: Your app can retrieve the
  [`EXTRA_REMOTE_INPUT_DRAFT`](https://developer.android.com/reference/android/app/Notification#EXTRA_REMOTE_INPUT_DRAFT)
  sent by the system when a user inadvertently closes a messaging notification.
  You can use this extra to pre-populate text fields in the app so users can
  finish their reply.

- Identify if a conversation is a group conversation: You can use
  [`setGroupConversation()`](https://developer.android.com/reference/android/app/Notification.MessagingStyle#setGroupConversation(boolean))
  to purposefully identify a conversation as a group or non-group conversation.

- Set the semantic action for an intent: The
  [`setSemanticAction()`](https://developer.android.com/reference/android/app/Notification.Action.Builder#setSemanticAction(int))
  method allows you to give semantic meaning to an action, such
  as "mark as read," "delete," "reply," and so on.

- SmartReply: Android 9 supports the same suggested replies available in your
  messaging app. Use
  [`RemoteInput.setChoices()`](https://developer.android.com/reference/android/app/RemoteInput.Builder#setChoices(java.lang.CharSequence%5B%5D))
  to provide an array of standard responses to the user.

### Channel settings, broadcasts, and Do Not Disturb

Android 8.0 introduced [Notification Channels](https://developer.android.com/guide/topics/ui/notifiers/notifications#ManageChannels),
allowing you to create a
user-customizable channel for each type of notification you want to display.
Android 9 simplifies notification channel settings with these changes:

- Blocking channel groups: Users can now block entire groups of channels
  within the notification settings for an app. You can use the
  [`isBlocked()`](https://developer.android.com/reference/android/app/NotificationChannelGroup#isBlocked())
  method to identify when a group is blocked and, as a result, not send any
  notifications for channels in that group.

  Additionally, your app can query for current channel group settings using
  the new
  [`getNotificationChannelGroup()`](https://developer.android.com/reference/android/app/NotificationManager#getNotificationChannelGroup(java.lang.String))
  method.
- New broadcast intent types: The Android system now sends broadcast intents
  when the blocking state of notification channels and channel groups' changes.
  The app that owns the blocked channel or group can listen for these intents and
  react accordingly. For further information on these intent actions and extras,
  refer to the updated constants list in the
  [`NotificationManager`](https://developer.android.com/reference/android/app/NotificationManager#constants)
  reference. For information on reacting to broadcast intents, refer to
  [Broadcasts](https://developer.android.com/guide/components/broadcasts.html).

- [`NotificationManager.Policy`](https://developer.android.com/reference/android/app/NotificationManager.Policy#constants)
  has three new Do-Not-Disturb priority categories:

  - [`PRIORITY_CATEGORY_ALARMS`](https://developer.android.com/reference/android/app/NotificationManager.Policy#PRIORITY_CATEGORY_ALARMS) prioritizes alarms.
  - [`PRIORITY_CATEGORY_MEDIA`](https://developer.android.com/reference/android/app/NotificationManager.Policy#PRIORITY_CATEGORY_MEDIA) prioritizes sounds from media sources, such as media and voice navigation.
  - [`PRIORITY_CATEGORY_SYSTEM`](https://developer.android.com/reference/android/app/NotificationManager.Policy#PRIORITY_CATEGORY_SYSTEM) prioritizes system sounds.
- `NotificationManager.Policy` also has seven new Do-Not-Disturb constants you
  can use to suppress visual interruption:

  - [`SUPPRESSED_EFFECT_FULL_SCREEN_INTENT`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_FULL_SCREEN_INTENT) prevents the notification from launching full-screen activity.
  - [`SUPPRESSED_EFFECT_LIGHTS`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_LIGHTS) blocks notification lights.
  - [`SUPPRESSED_EFFECT_PEEK`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_PEEK) prevents notifications from sliding briefly into view ("peeking").
  - [`SUPPRESSED_EFFECT_STATUS_BAR`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_STATUS_BAR) prevents notifications from appearing in the status bar on devices that support status bars.
  - [`SUPPRESSED_EFFECT_BADGE`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_BADGE) blocks badges on on devices that support badging. For more information, refer to [Modify a notification badge](https://developer.android.com/training/notify-user/badges.html).
  - [`SUPPRESSED_EFFECT_AMBIENT`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_AMBIENT) blocks notifications on devices that support ambient displays.
  - [`SUPPRESSED_EFFECT_NOTIFICATION_LIST`](https://developer.android.com/reference/android/app/NotificationManager.Policy#SUPRESSED_EFFECT_NOTIFICATION_LIST) prevents notifications from appearing in the list view on devices that support a list view, such as notification shade or lockscreen.

## Multi-camera support and camera updates

On devices running Android 9, you can access streams
simultaneously from [two or more physical
cameras](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA).
On devices with either dual-front or dual-back cameras, you can create
innovative features not possible with just a single camera, such as seamless
zoom, bokeh, and stereo vision. The API also lets you call a logical or fused
camera stream that automatically switches between two or more cameras.

Other improvements in camera include additional [Session
parameters](https://developer.android.com/reference/android/hardware/camera2/params/SessionConfiguration)
that help to reduce delays during initial capture, and surface sharing that lets
camera clients handle various use cases without the need to stop and start
camera streaming. We've also added APIs for display-based [flash
support](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_EXTERNAL_FLASH)
and access to [OIS
timestamps](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#STATISTICS_OIS_TIMESTAMPS)
for app-level image stabilization and special effects.

In Android 9 the [multi-camera
API](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA)
supports monochrome cameras for devices with
`https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_FULL` or
`https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_LIMITED` capability.
Monochrome output is achieved via the
`https://developer.android.com/reference/android/graphics/ImageFormat#YUV_420_888`
format with Y as grayscale, U (Cb) as 128, and V (Cr) as 128.

Android 9 also enables support for [external USB/UVC
cameras](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics) on
supported devices.

## ImageDecoder for drawables and bitmaps

Android 9 introduces the
[`ImageDecoder`](https://developer.android.com/reference/android/graphics/ImageDecoder)
class, which provides a modernized approach for decoding images. Use this class
instead of the [`BitmapFactory`](https://developer.android.com/reference/android/graphics/BitmapFactory)
and [`BitmapFactory.Options`](https://developer.android.com/reference/android/graphics/BitmapFactory.Options)
APIs.

`ImageDecoder` lets you create a
[`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable) or a
[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap) from a byte buffer, a file,
or a URI. To decode an image, first call
[`createSource()`](https://developer.android.com/reference/android/graphics/ImageDecoder#createSource(java.nio.ByteBuffer))
with the source of the encoded image. Then, call
[`decodeDrawable()`](https://developer.android.com/reference/android/graphics/ImageDecoder#decodeDrawable(android.graphics.ImageDecoder.Source))
or [`decodeBitmap()`](https://developer.android.com/reference/android/graphics/ImageDecoder#decodeBitmap(android.graphics.ImageDecoder.Source))
by passing the [`ImageDecoder.Source`](https://developer.android.com/reference/android/graphics/ImageDecoder.Source)
object to create a [`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable)
or a [`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap). To change the
default settings, pass [`OnHeaderDecodedListener`](https://developer.android.com/reference/android/graphics/ImageDecoder.OnHeaderDecodedListener) to
`decodeDrawable()` or `decodeBitmap()`. `ImageDecoder` calls
[`onHeaderDecoded()`](https://developer.android.com/reference/android/graphics/ImageDecoder.OnHeaderDecodedListener#onHeaderDecoded(android.graphics.ImageDecoder,%20android.graphics.ImageDecoder.ImageInfo,%20android.graphics.ImageDecoder.Source))
with the image's default width and height, once they are known.
If the encoded image is an animated GIF or WebP, `decodeDrawable()` returns a
`Drawable` that is an instance of the
[`AnimatedImageDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable)
class.

There are different methods you can use to set image properties:

- To scale the decoded image to an exact size, pass the target dimensions into [`setTargetSize()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setTargetSize(int,%20int)). You can also scale images using a sample size. Pass the sample size directly to [`setTargetSampleSize()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setTargetSampleSize(int)).
- To crop an image within the range of the scaled image, call [`setCrop()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setCrop(android.graphics.Rect)).
- To create a mutable bitmap, pass `true` into [`setMutableRequired()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setMutableRequired(boolean)).

`ImageDecoder` also lets you add customized and complicated effects to an image
such as rounded corners or
circle masks. Use
[`setPostProcessor()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setPostProcessor(android.graphics.PostProcessor))
with an instance of the
[`PostProcessor`](https://developer.android.com/reference/android/graphics/PostProcessor)
class to execute whatever drawing commands you want.
| **Note:** When you post-process an [`AnimatedImageDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable), the effects appear in all frames of the animation.

## Animation

Android 9 introduces the
[`AnimatedImageDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable)
class for drawing and displaying GIF and WebP animated images.
`AnimatedImageDrawable` works similarly to
[`AnimatedVectorDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable)
in that the render thread drives the animations of `AnimatedImageDrawable`.
The render thread also uses a worker thread to decode, so that decoding does not
interfere with other operations on the render thread. This implementation allows
your app to display an animated image without managing its updates or
interfering with other events on your app's UI thread.

An `AnimatedImageDrawable` can be decoded using an instance of
[`ImageDecoder`](https://developer.android.com/reference/android/graphics/ImageDecoder). The following
code snippet shows how to use `ImageDecoder` to decode your
`AnimatedImageDrawable`:

### Kotlin

```transact-sql
@Throws(IOException::class)
private fun decodeImage() {
    val decodedAnimation = ImageDecoder.decodeDrawable(
        ImageDecoder.createSource(resources, R.drawable.my_drawable))

    // Prior to start(), the first frame is displayed.
    (decodedAnimation as? AnimatedImageDrawable)?.start()
}
```

### Java

```scdoc
private void decodeImage() throws IOException {
    Drawable decodedAnimation = ImageDecoder.decodeDrawable(
        ImageDecoder.createSource(getResources(), R.drawable.my_drawable));

    if (decodedAnimation instanceof AnimatedImageDrawable) {
        // Prior to start(), the first frame is displayed.
        ((AnimatedImageDrawable) decodedAnimation).start();
    }
}
```

`ImageDecoder` has several methods allowing you to further modify the image.
For example, you can use the
[`setPostProcessor()`](https://developer.android.com/reference/android/graphics/ImageDecoder#setPostProcessor(android.graphics.PostProcessor))
method to modify the appearance of the image, such as applying a circle mask or
rounded corners.

## HDR VP9 Video, HEIF image compression, and Media APIs

Android 9 provides built-in support for High Dynamic Range (HDR) VP9 Profile 2,
so you can deliver HDR-enabled movies to your users from YouTube, Play Movies,
and other sources on HDR-capable devices.

Android 9 also adds support for encoding images using the High Efficiency Image
File format ([HEIF](https://developer.android.com/reference/android/media/MediaFormat#MIMETYPE_IMAGE_ANDROID_HEIC)
or HEIC), which improves compression and reduces storage space and network data
usage. HEIF still image samples are supported in the
[`MediaMuxer`](https://developer.android.com/reference/android/media/MediaMuxer#addTrack(android.media.MediaFormat))
and [`MediaExtractor`](https://developer.android.com/reference/android/media/MediaExtractor#getTrackFormat(int))
classes. With platform support on Android 9 devices, it's easy to send and
utilize HEIF images from your backend server. After you've made sure that your
app is compatible with this data format for sharing and display, give HEIF a try
as an image storage format in your app. You can do a jpeg-to-heic conversion
using [`ImageDecoder`](https://developer.android.com/reference/android/graphics/ImageDecoder) or
[`BitmapFactory`](https://developer.android.com/reference/android/graphics/BitmapFactory) (which obtains
a bitmap from a JPEG file). You can then use
[`HeifWriter`](https://developer.android.com/reference/androidx/heifwriter/HeifWriter) to write HEIF
still images from YUV byte buffers, or instances of
[`Surface`](https://developer.android.com/reference/android/view/Surface) or
[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap).

Media metrics are also available from the
[`AudioTrack`](https://developer.android.com/reference/android/media/AudioTrack#getMetrics()),
[`AudioRecord`](https://developer.android.com/reference/android/media/AudioRecord#getMetrics()),
and [`MediaDrm`](https://developer.android.com/reference/android/media/MediaDrm#getMetrics()) classes.

Android 9 introduces methods to the
[`MediaDRM`](https://developer.android.com/reference/android/media/MediaDrm) class to get metrics, HDCP
levels, security levels, and number of sessions, and to add more control over
security levels and secure stops. See the [API Diff
report](https://developer.android.com/sdk/api_diff/28/changes) for details.

In Android 9, the [AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio) API adds
support for several additional AAudioStream attributes, including usage, content
type, and input preset. Using these attributes, you can create streams that are
tuned for VoIP or camcorder applications. You can also set the session ID to
associate an AAudio stream with a submix that can include effects. Use the
[`AudioEffect`](https://developer.android.com/reference/android/media/audiofx/AudioEffect) API to control the
effects.

Android 9 introduces the
[`AudioEffect`](https://developer.android.com/reference/android/media/audiofx/AudioEffect) API for
[dynamics processing](https://developer.android.com/reference/android/media/audiofx/DynamicsProcessing).
With this class, you can build channel-based audio effects---including
equalization, multi-band compression, and limiter---across multiple stages. The
number of bands and active stages is configurable, and most parameters can be
controlled in real time.

## Data cost sensitivity in JobScheduler

Beginning in Android 9, [`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler)
can use network status signals provided by carriers to improve the handling
of network-related jobs.

Jobs can declare their estimated data size, signal prefetching, and specify
detailed network requirements. `JobScheduler` then manages work according to
the network status. For example, when the network signals that it is congested,
`JobScheduler` might defer large network requests. When on an
unmetered network, `JobScheduler` can run prefetch jobs to
improve the user experience, such as by prefetching headlines.

When adding jobs, make sure to use [`setEstimatedNetworkBytes()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setEstimatedNetworkBytes(long,%20long)),
[`setPrefetch()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setPrefetch(boolean)),
and [`setRequiredNetwork()`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setRequiredNetwork(android.net.NetworkRequest))
when appropriate to help
`JobScheduler` handle the work properly. When your job executes,
be sure to use the [`Network`](https://developer.android.com/reference/android/net/Network) object
returned by
[`JobParameters.getNetwork()`](https://developer.android.com/reference/android/app/job/JobParameters#getNetwork()).
Otherwise you'll implicitly use the device's default network which
may not meet your requirements, causing unintended data usage.

## Neural Networks API 1.1

The [Neural Networks API](https://developer.android.com/ndk/guides/neuralnetworks) was introduced
in Android 8.1 (API level 27) to accelerate on-device machine learning on
Android. Android 9 expands and improves the API, adding
support for nine new operations:

- Element-wise mathematical operations:
  - [`ANEURALNETWORKS_DIV`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a139794099b4137599bbc73af18b0d42a)
  - [`ANEURALNETWORKS_SUB`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a06a4248fe5ec71820ab95b87613780be)
- Array operations:
  - [`ANEURALNETWORKS_BATCH_TO_SPACE_ND`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a2bdfefbdc6409b4bbcacc16c72002703)
  - [`ANEURALNETWORKS_SPACE_TO_BATCH_ND`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a91f17c92abe95e211de39c3715acd535)
  - [`ANEURALNETWORKS_SQUEEZE`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a1207019989837ee9d10c5b6663504933)
  - [`ANEURALNETWORKS_STRIDED_SLICE`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a89695302f8b1e7ae7ce8f4d8c0b8a752)
  - [`ANEURALNETWORKS_TRANSPOSE`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a92d7bc95eb68525334b6cfe80cd271ee)
  - [`ANEURALNETWORKS_PAD`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0aaced01fc41e401b81cefcf53780558d1)
  - [`ANEURALNETWORKS_MEAN`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0a047fe95a35b27f45c05432b6ca18eb6c)


**Known issue:** When passing
`https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaf06d1affd33f3bc698d0c04eceb23298a07984961d5c7c12f0f8c811bedd85dc3`
tensors to the
`https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaabbe492c60331b13038e39d4207940e0aaced01fc41e401b81cefcf53780558d1`
operation, which is available on Android 9 and higher,
the output from NNAPI may not match output from higher-level machine
learning frameworks, such as
[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/). You
should instead pass only
[`ANEURALNETWORKS_TENSOR_FLOAT32`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaf06d1affd33f3bc698d0c04eceb23298aee4bc05d71c31e22e39e05470e965447)
until the issue is resolved.

Additionally, the API also introduces a new function,
[`ANeuralNetworksModel_relaxComputationFloat32toFloat16()`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1gab822719f98f0c92e5da3684cdaca6ba0),
that allows you to specify whether to calculate
[`ANEURALNETWORKS_TENSOR_FLOAT32`](https://developer.android.com/ndk/reference/group/neural-networks#group___neural_networks_1ggaf06d1affd33f3bc698d0c04eceb23298aee4bc05d71c31e22e39e05470e965447)
with a range and precision as low as that of the IEEE 754 16-bit floating-point
format.

## Autofill framework

Android 9 introduces multiple improvements that autofill
services can implement to further enhance the user experience when filling out
forms. To learn more about how to use autofill features in your app, see the
[Autofill Framework](https://developer.android.com/guide/topics/text/autofill) guide.

## Security enhancements

Android 9 introduces a number of security features, which the
following sections summarize:

### Android Protected Confirmation

Supported devices that run Android 9 or higher give you the
ability to use Android Protected Confirmation. When using this workflow, your
app displays a prompt to the user, asking them to approve a short statement.
This statement allows the app to reaffirm that the user would like to complete a
sensitive transaction, such as making a payment.

If the user accepts the statement, Android Keystore receives and stores a
cryptographic signature that's protected by a keyed-hash message authentication
code (HMAC). After Android Keystore confirms the message's validity, your app
can use the key generated from `trustedConfirmationRequired` in the trusted
execution environment (TEE) to sign the message that the user accepted. The
signature indicates, with very high confidence, that the user has seen the
statement and has agreed to it.


**Caution:**Android Protected Confirmation doesn't provide a
secure information channel for the user. Your app cannot assume any
confidentiality guarantees beyond those that the Android platform offers. In
particular, don't use this workflow to display sensitive information that you
wouldn't ordinarily show on the user's device.

For guidance on adding support for Android Protected Confirmation, see the
[Android Protected
Confirmation](https://developer.android.com/training/articles/security-android-protected-confirmation)
guide.

### Unified biometric authentication dialog

In Android 9, the system provides biometric authentication dialogs on behalf
of your app. This functionality creates a standardized look, feel, and placement
for the dialog, giving users more confidence that they're authenticating against
a trusted biometric credential checker.

If your app uses
[`FingerprintManager`](https://developer.android.com/reference/android/hardware/fingerprint/FingerprintManager)
to display a fingerprint authentication dialog to users, switch to using
[`BiometricPrompt`](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt)
instead. `BiometricPrompt` relies on the system to display the authentication
dialog. It also changes its behavior to adapt to the type of biometric
authentication that a user has chosen.
| **Note:** Before using `BiometricPrompt` in your app, you should first use the [`hasSystemFeature()`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)) method to ensure that the device supports `FEATURE_FINGERPRINT`, `FEATURE_IRIS`, or `FEATURE_FACE`. If a device doesn't support biometric authentication, you can fall back to verifying the user's PIN, pattern, or password using the [`createConfirmDeviceCredentialIntent()`](https://developer.android.com/reference/android/app/KeyguardManager#createConfirmDeviceCredentialIntent(java.lang.CharSequence,%20java.lang.CharSequence)) method.

### Hardware security module

Supported devices running Android 9 or higher installed can
have a StrongBox KeyMint (previously Keymaster), an implementation of
the KeyMint (previously Keymaster) HAL that resides in a hardware security
module. The module contains the following:

- Its own CPU.
- Secure storage.
- A true random-number generator.
- Additional mechanisms to resist package tampering and unauthorized sideloading of apps.

When checking keys stored in the StrongBox KeyMint, the system corroborates a
key's integrity with the Trusted Execution Environment (TEE).

To learn more about using StrongBox KeyMint, see [Hardware Security
Module](https://developer.android.com/training/articles/keystore#HardwareSecurityModule).

### Secure key import into Keystore

Android 9 provides additional key decryption security by adding
the ability to import encrypted keys securely into the Keystore using an
ASN.1‑encoded key format. The KeyMint then decrypts the keys in the
Keystore, so the content of the keys never appears as plaintext in the device's host memory.
| **Note:** This feature is supported only on devices that ship with Keymaster 4 or higher.

Learn more about how to [Import encrypted keys more
securely](https://developer.android.com/training/articles/keystore#ImportingEncryptedKeys).

### APK signature scheme with key rotation

Android 9 adds support for APK Signature Scheme v3. This scheme has the option
to include a proof-of-rotation record in its signing block for each signing
certificate. This capability enables your app to be signed with a new signing
certificate by linking the APK file's past signing certificates to the one with
which it is now signed.
| **Note:** Devices running Android 8.1 (API level 27) or lower don't support changing the signing certificate. If your app's `minSdkVersion` is `27` or lower, use an old signing certificate to sign your app in addition to the new signature.

Learn more on how to rotate keys using
[`apksigner`](https://developer.android.com/studio/command-line/apksigner#usage-rotate).

### Option to allow key decryption only on unlocked devices

Android 9 introduces the `unlockedDeviceRequired` flag. This option determines
whether the Keystore requires the screen to be unlocked before allowing
decryption of any in-flight or stored data using the specified key. These types
of keys are well suited for encrypting sensitive data to store on disk, such as
health or enterprise data. The flag provides users a higher assurance that the
data cannot be decrypted while the device is locked should their phone be lost
or stolen.
| **Note:** When the `unlockedDeviceRequired` flag is enabled, encryption and signature verification can still happen at any time. The flag prevents **only
| decryption** of data when the device is unlocked.

To keep a key safe from decryption while the device is locked, enable the flag
by passing `true` to the [`setUnlockedDeviceRequired()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired(boolean))
method. After completing this step, when the user's screen is locked, any
attempts to decrypt or sign data using this key fail. A locked device requires a
PIN, password, fingerprint, or some other trusted factor before it can be
accessed.

### Legacy encryption support

Android 9 devices that ship with Keymaster 4 support the Triple Data
Encryption Algorithm, or Triple DES. If your app interoperates with legacy
systems that require Triple DES, use this type of cipher when encrypting
sensitive credentials.

To learn more about how to make your app more secure, see [Security for Android
Developers](https://developer.android.com/topic/security).

### Deprecation of WPS

Wi-Fi Protected Setup (WPS) is deprecated for security reasons.

## Android backups

Android 9 adds new functionality and developer options related
to backup and restore. Details about these changes appear in the following
sections.

### Client-side encryption backups

Android 9 adds support for encrypting Android backups with a
client-side secret. This support is enabled automatically when the following
conditions are met:

- The user has [enabled
  backup](https://support.google.com/pixelphone/answer/7179901) using Android 9 or higher.
- The user has [set a screen
  lock](https://support.google.com/android/answer/2819522) for their device that requires a PIN, pattern, or password to unlock.

When this privacy measure is enabled, the device's PIN, pattern, or password is
required to restore data from the backups made by the user's device. To learn
more about the technology behind this feature, see the [Google Cloud Key Vault
Service](https://developer.android.com/about/versions/pie/security/ckv-whitepaper) whitepaper.

### Define device conditions required for backup

If your app data includes sensitive information or preferences, Android 9
gives you the ability to [define the device
conditions](https://developer.android.com/guide/topics/data/autobackup#define-device-conditions) under which
your app's data is included in the user's backup, such as when client-side
encryption is enabled or a local device-to-device transfer is taking place.

To learn more about backing up data on Android devices, see [Data
Backup Overview](https://developer.android.com/guide/topics/data/backup).

## Accessibility

Android 9 introduces enhancements to the accessibility
framework that make it easier to provide even better experiences to users of
your app.

### Navigation semantics

Attributes added in Android 9 make it easier for you to define how
accessibility services, especially screen readers, navigate from one part of the
screen to another. These attributes can help users who are visually impaired
quickly move through text in your app's UI and allow them to make a selection.

For example, in a shopping app, a screen reader can help users navigate
directly from one category of deals to the next, without the screen reader
having to read all items in a category before moving on to the next.

#### Accessibility pane titles

In Android 8.1 (API level 27) and lower, accessibility services cannot always
determine when a specific pane of the screen was updated, such as when an activity replaces one fragment with another fragment. Panes consist of
logically-grouped, visually-related UI elements that typically comprise a
fragment.

In Android 9, you can provide *accessibility pane titles*, or individually
identifiable titles, for these panes. If a pane has an accessibility pane title,
accessibility services receive more detailed information when the pane changes.
This capability allows services to provide more granular information to the user
about what's changed in the UI.

To specify the title of a pane, use the
[`android:accessibilityPaneTitle`](https://developer.android.com/reference/android/R.attr#accessibilityPaneTitle)
attribute. You can also update the title of a UI pane that is replaced at
runtime using [`setAccessibilityPaneTitle()`](https://developer.android.com/reference/android/view/View#setAccessibilityPaneTitle(java.lang.CharSequence)).
For example, you could provide a title for the content area of a
[`Fragment`](https://developer.android.com/reference/android/support/v4/app/Fragment) object.

#### Heading-based navigation

If your app displays textual content that includes logical headings, set the
[`android:accessibilityHeading`](https://developer.android.com/reference/android/R.attr#accessibilityHeading)
attribute to `true` for the instances of
[`View`](https://developer.android.com/reference/android/view/View) that represent those headings. By
adding these headings, you allow accessibility services to help users navigate
directly from one heading to the next. Any accessibility service can use this
capability to improve users' UI navigation experience.

#### Group navigation and output

Screen readers have traditionally used the
[`android:focusable`](https://developer.android.com/reference/android/R.attr#focusable) attribute to
determine when they should read a
[`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup), or a collection of
[`View`](https://developer.android.com/reference/android/view/View) objects, as a single unit. That way,
users could understand that the views were logically related to each other.

In Android 8.1 and lower, you need to mark each `View` object within a
`ViewGroup` as non-focusable and the `ViewGroup` itself as focusable. This
arrangement caused some instances of `View` to be marked focusable in a way that
made keyboard navigation more cumbersome.

Starting in Android 9, you can use the
[`android:screenReaderFocusable`](https://developer.android.com/reference/android/R.attr#screenReaderFocusable)
attribute in place of the `android:focusable` attribute in situations where
making a `View` object focusable has undesirable consequences. Screen readers
place focus on all elements that have set either `android:screenReaderFocusable`
or `android:focusable` to `true`.

### Convenience actions

Android 9 adds support for performing convenience actions on behalf of users:

Interaction with tooltips
:   Added features in the accessibility framework give you access to
    [tooltips](https://developer.android.com/guide/topics/ui/tooltips) in an app's UI. Use
    [`getTooltipText()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getTooltipText())
    to read the text of a tooltip, and use the
    [`ACTION_SHOW_TOOLTIP`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_SHOW_TOOLTIP)
    and [`ACTION_HIDE_TOOLTIP`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_HIDE_TOOLTIP)
    to instruct instances of [`View`](https://developer.android.com/reference/android/view/View) to show or
    hide their tooltips.

Added global actions
:   Android 9 introduces support for two additional device actions in the
    [`AccessibilityService`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
    class. Your service can help users lock their devices and take screenshots
    using the
    [`GLOBAL_ACTION_LOCK_SCREEN`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#GLOBAL_ACTION_LOCK_SCREEN)
    and [`GLOBAL_ACTION_TAKE_SCREENSHOT`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#GLOBAL_ACTION_TAKE_SCREENSHOT)
    actions, respectively.

### Window change details

Android 9 makes it easier to track updates to an app's windows when an app
redraws multiple windows simultaneously. When a
[`TYPE_WINDOWS_CHANGED`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_WINDOWS_CHANGED)
event occurs, use the
[`getWindowChanges()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#getWindowChanges())
API to determine how the windows have changed. During a multiwindow update, each
window produces its own set of events.
The [`getSource()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityRecord#getSource())
method returns the root view of the window associated with each event.

If an app has defined [accessibility pane titles](https://developer.android.com/about/versions/pie/android-9.0#a11y-pane-titles) for its
[`View`](https://developer.android.com/reference/android/view/View) objects, your service can recognize
when the app's UI is updated. When a
[`TYPE_WINDOW_STATE_CHANGED`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_WINDOW_STATE_CHANGED)
event occurs, use the types returned by
[`getContentChangeTypes()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#getContentChangeTypes())
to determine how the window has changed. For example, the framework can
detect when a pane has a new title, or when a pane has disappeared.
|
| Google is committed to improving accessibility for all Android users, providing
| enhancements that enable you to build services, such as the [Talkback](https://support.google.com/accessibility/android/answer/6283677)
| screen reader, for users with accessibility needs. To learn more about how to
| make your app more accessible and to build accessibility services, see [Accessibility](https://developer.android.com/guide/topics/ui/accessibility).

## Rotation

To eliminate unintentional rotations, we've added a mode that pins the current
orientation even if the device position changes. Users can trigger rotation
manually when needed by pressing a button in the system bar.

The compatibility impacts for apps are minimal in most cases. However, if your
app has any customized rotation behavior or uses any unusual screen orientation
settings, you might run into issues that would have gone unnoticed before, when
user rotation preference was always set to portrait. We encourage you to take a
look at the rotation behavior in all the key activities of your app and make
sure that all of your screen orientation settings are still providing the
optimal experience.

For more details, see the associated [behavior
changes](https://developer.android.com/about/versions/pie/android-9.0-changes-all#screen-rotation-changes).
![Rotating mobile showing new rotation mode letting users manually trigger rotation](https://developer.android.com/static/images/about/versions/pie/rotate-changes.gif)


A new rotation mode lets users trigger rotation manually when needed using a button in the system bar.

## Text

Android 9 brings the following text-related features to the
platform:

- Precomputed Text: The
  [`PrecomputedText`](https://developer.android.com/reference/android/text/PrecomputedText) class improves
  text-rendering performance by enabling you to compute and cache the required
  information ahead of time. It also enables your app to perform text layout off
  the main thread.

- Magnifier: The [`Magnifier`](https://developer.android.com/reference/android/widget/Magnifier) class is a
  platform widget that provides a magnifier API, allowing for a consistent
  magnifier-feature experience across all apps.

- Smart Linkify: Android 9 enhances the
  [`TextClassifier`](https://developer.android.com/reference/android/view/textclassifier/TextClassifier) class,
  which leverages machine learning to identify some entities in selected text and
  suggest actions. For example, `TextClassifier` can enable your app to detect
  that the user has selected a phone number. Your app could then suggest that the
  user make a phone call using that number. The features in `TextClassifier`
  replace the functionality of the `Linkify` class.

- Text Layout: Several convenience methods and attributes make it easier to
  implement your UI design. For details, see the reference documentation for
  [`TextView`](https://developer.android.com/reference/android/widget/TextView).

### ART ahead-of-time conversion of DEX files

On devices running Android 9 or higher, the Android runtime
(ART) ahead-of-time compiler further optimizes compressed Dalvik Executable
format (DEX) files by converting the DEX files in an app package into a more
compact representation. This change allows your app to start faster and consume
less disk space and RAM.

This improvement particularly benefits low-end devices with slower disk I/O
speeds.

## On-device system tracing

Android 9 allows you to record system traces from your device,
then share a report of these recordings with your development team. This report
supports multiple formats, including HTML.

By collecting these traces, you can capture timing data related to your app's
processes and threads and view other types of globally-significant device
states.
| **Note:** You don't need to [instrument your code](https://developer.android.com/reference/android/os/Trace) to record traces, but doing so can help you see what parts of your app's code may be contributing to hanging threads or UI jank.

To learn more about this tool, see [Perform on-device system
tracing](https://developer.android.com/studio/profile/systrace-on-device).