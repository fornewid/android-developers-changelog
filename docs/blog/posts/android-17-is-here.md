---
title: https://developer.android.com/blog/posts/android-17-is-here
url: https://developer.android.com/blog/posts/android-17-is-here
source: md.txt
---

# Android 17 is Here

13-min read ![](https://developer.android.com/static/blog/assets/Strapi_Hero_White_e4dbee04d8_Z1qQbv3.webp) 16 Jun 2026 [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) Vice President, Product Management, Android Developer Today we're releasing Android 17 and making it available on most supported Pixel devices. Look for new devices running Android 17 in the coming months.
![AfD-Android-17.gif](https://developer.android.com/static/blog/assets/Af_D_Android_17_7410a1af06_Z2bzxdy.webp)

Android 17 marks the start of our transition to an intelligence system, putting your apps at the center. Android is shifting to adaptive-first development standards by introducing mandatory large-screen resizability, while simultaneously delivering next-generation privacy, security, media, camera, and performance. We'll cover all that in this post, as well as how we're bringing together next generation tools, libraries, and agent skills to help your apps embrace this opportunity.

Throughout the past year, from our Canary channel to our Beta releases, we've collaborated with many of you in the developer community to build a platform you and your users can trust. To that end, this moment marks the availability of the source code at the [Android Open Source Project](https://source.android.com/) (AOSP). This allows you to [examine the source code](https://cs.android.com/) for a deeper understanding of how Android works.

Let's dive deeper into Android 17.

## An intelligence system

With deep integration between hardware, software and AI, we're transforming Android from an operating system to an intelligence system. It's about delivering new helpful experiences that anticipate user needs, and it brings more opportunities for engagement with your apps. To that end, Android 17 expands the capabilities of AppFunctions, a platform API with a corresponding Jetpack library. It allows you to contribute your app's unique capabilities as orchestratable "tools" for Android MCP, the on-device equivalent of the [Model Context Protocol](https://modelcontextprotocol.io/). AI agents and assistants (like Google Gemini) can discover and execute AppFunctions to perform workflows on behalf of the user with direct access to the app's local state.

The Jetpack library, currently in alpha, makes adding AppFunctions as easy as annotating a class and adding KDoc comments.

```kotlin
/**
 *   A note app's [AppFunction]s.
 */
class NoteFunctions(
    private val noteRepository: NoteRepository
) {
    /**
     *   Adds a new note to the app.
     *
     *   @param appFunctionContext The execution context.
     *   @param title The title of the note.
     *   @param content The note's content.
     */
    @AppFunction(isDescribedByKDoc = true)
    suspend fun createNote(
        appFunctionContext: AppFunctionContext,
        title: String,
        content: String
    ): Note {
        return noteRepository.createNote(title, content)
    }
}
```

We've also launched an [AppFunctions agent skill](http://github.com/android/skills/tree/main/on-device/appfunctions) that analyzes your app's key workflows, automatically generates the required Kotlin code, optimizes your KDocs for LLM tool-calling, and provides ADB commands for testing and debugging.

The Gemini integration is currently in a private preview with trusted testers, but you can begin preparing your apps now. In addition to [ADB commands](https://developer.android.com/ai/appfunctions/add-appfunctions#verify-integration) to execute your AppFunctions, we've provided a [test agent app](http://github.com/android/appfunctions/releases/initial) that includes an interface to discover and execute your AppFunctions and simulate an AI agent integration. Join our integration early access program at [goo.gle/eap-af](http://goo.gle/eap-af) for a chance to be among the first apps to deploy AppFunctions to production.

## Adaptive-first

Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments. Now, with over [580 million large screen devices](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) in the hands of users and the [forthcoming launch of Googlebooks](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/), the next generation of ChromeOS built on the Android stack, adaptive is no longer just a technical goal. It's a massive opportunity to reach highly engaged users, which is one of the reasons we're shifting to an [adaptive-first development standard](https://developer.android.com/adaptive-apps).

### No resizability/orientation restrictions on large screens

To ensure apps deliver a premium experience across all form factors, including mobile devices running in desktop mode on connected displays, Android 17 (API level 37) removes the developer opt-out for orientation and resizability restrictions on [large screen devices](https://developer.android.com/guide/topics/large-screens) (sw \> 600 dp) for apps targeting API level 37. The system will ignore legacy manifest attributes and runtime APIs, including `screenOrientation`, `setRequestedOrientation()`, `resizeableActivity=false`, and aspect ratio constraints `(minAspectRatio/maxAspectRatio)`. Games (based on [app category](https://support.google.com/googleplay/android-developer/answer/9859673) in Google Play) remain exempt. Your app must be ready to adapt to any window size, respect the user's preferred device posture, and support free-form windowing natively.

### Next-gen multitasking: App Bubbles, Bubble Bar, and desktop interactive PiP

Android 17 introduces powerful new windowing capabilities that redefine how users multitask, demanding even greater layout flexibility from your apps:

- **App Bubbles:**Moving beyond the messaging bubbles API, users can now transform any app into a floating bubble by long-pressing its icon on the launcher. This feature is available across phones, foldables, and tablets, enabling lightweight multitasking for any workflow.
- **The Bubble Bar:** On large screens (tablets and foldables), the system taskbar now includes a dedicated Bubble Bar to organize, transition between, and dock these floating app bubbles.
- **Desktop interactive PiP:** In desktop environments, Android 17 introduces interactive Picture-in-Picture (PiP). Unlike traditional PiP windows which are read-only, these pinned windows remain fully interactive while staying always-on-top of other application windows.

![Bubbles (1).gif](https://developer.android.com/static/blog/assets/Bubbles_1_87589bd167_22skB6.webp) App Bubbles and Bubble Bar in action

### Activity recreation updates

To prevent disruptive state loss and stutter, Android 17 updates the default behavior for Activity recreation. The system will no longer restart activities by default for typical configuration changes that do not require a full UI redraw (including [CONFIG_KEYBOARD](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo#config_keyboard), [CONFIG_KEYBOARD_HIDDEN](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo#config_keyboard_hidden), [CONFIG_NAVIGATION](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo#config_navigation), [CONFIG_TOUCHSCREEN](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo#config_touchscreen), and [CONFIG_COLOR_MODE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo#config_color_mode)).

Instead, running activities will receive these updates via onConfigurationChanged(), enabling smooth transitions. If your application explicitly relies on a full restart to reload resources for these changes, you must now explicitly opt-in using the new [android:recreateOnConfigChanges](https://developer.android.com/reference/kotlin/android/R.attr#recreateonconfigchanges) manifest attribute.

### Continue On

Android 17 adds Continue On to help users seamlessly transition a task between Android devices. The user sees a suggestion for the most recently opened app from their mobile device in their tablet taskbar, providing a one-tap affordance to launch the app and deep-link where they left off. Continue on can support app-to-web transitions, including falling back to using the web if the app isn't installed.
![Continue On.png](https://developer.android.com/static/blog/assets/Continue_On_1a1c25e5ac_ZnJQqY.webp) Handoff Suggestion on a Tablet

```
class MyHandoffActivity : Activity() {

    ...

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Do stuff
    ...
    // Enable handoff
    setHandoffEnabled(true, null)
  }

  // Override and implement onHandoffActivityDataRequested
  override fun onHandoffActivityDataRequested(handoffRequestInfo: HandoffActivityDataRequestInfo) : HandoffActivityData {
    // Create and return handoff data
  }
}
```

### Go adaptive-first with Jetpack Compose

To help you adapt your apps to meet the new Android 17 requirements, we've launched the [Jetpack Compose adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive). This AI-powered developer workflow helps you implement the best adaptive practices:

- **Adaptive navigation:** Automatically transition between bottom navigation bars on mobile and edge-anchored navigation rails on large screens using `NavigationSuiteScaffold` from the Material 3 Adaptive library.
- **Multi-pane layouts:** Implement list-detail and supporting pane layouts natively using Navigation 3 Scenes (`ListDetailSceneStrategy` and `SupportingPaneSceneStrategy`) instead of fragile fragment transactions.
- **FlexBox \& Grid APIs:** Utilize Compose 1.11's dynamic layout components to easily adjust row and column spans on the fly, ensuring your content always fills the space beautifully.
- **Advanced non-touch input:** Leverage Compose 1.11's enhanced trackpad and mouse support, including native focus rings and new APIs (like `TrackpadInjectionScope` and `performTrackpadInput`) to easily test and deliver a true "laptop-class" experience on Googlebooks and Desktop Mode.
- **Dynamic window states:** Leverage Compose's reactive state model to seamlessly adapt your UI when the app transitions from full screen to a floating App Bubble or an interactive Desktop PiP window, ensuring a premium experience even at minimal dimensions.

### Android is Compose-first

Compose offers the easiest way to build adaptive apps, and that's just one of the [many reasons](https://developer.android.com/develop/ui/compose/first#why-compose-first) we believe that **all Android UI should be built with Compose** . To that end, [Android development is now Compose-first](https://developer.android.com/develop/ui/compose/first). All new Android APIs, libraries, tools, and developer guidance will be built exclusively for Jetpack Compose. Legacy View components (in the android.widget package) and View-based Jetpack libraries (like `Fragments`, `RecyclerView`, and `ViewPager`) are now in maintenance mode. They will receive only critical bug fixes, and no new features.

*** ** * ** ***

**TIP** Ready to migrate? Use our AI-driven [XML to Compose Migration Skill](https://github.com/android/skills/blob/main/jetpack-compose/migration/migrate-xml-views-to-jetpack-compose/SKILL.md) to automatically analyze your legacy View layouts and convert them into highly-adaptive Compose code.

*** ** * ** ***

## Performance \& efficiency

App performance means a smooth user interface, fast app start times, and efficient multitasking; Android 17 has impactful improvements in all of these areas.

### App memory limits

Memory usage is one of the silent foundations of overall performance. When a foreground app or service grows unchecked, memory management spikes CPU and battery utilization and eventually leads to the termination of other well-behaved cached apps and background jobs, ultimately forcing slower cold starts and impaired multitasking.

Starting in Android 17, the system will enforce strict app memory limits based on a device's total RAM, abruptly terminating offending processes. New things to help you navigate these tighter requirements:

- **R8 Optimizer:** TheR8 optimizer significantly reduces your app's bytecode memory footprint by shrinking classes, methods, and fields into shorter names, and stripping out unused code and resources. Use R8 in full mode along with the new [R8 configuration analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) to make sure your app is getting the most from R8.

![R8 Configuration Analyzer.png](https://developer.android.com/static/blog/assets/R8_Configuration_Analyzer_78f2101657_Z18pPMX.webp) The R8 Configuration Analyzer

- **LeakCanary in Android Studio Panda:**The profiler now features native LeakCanary integration as a dedicated task, fully integrated with your IDE and source code.
- **ApplicationExitInfo:** If your app is terminated by these limits, getDescription() from ApplicationExitInfo will return "MemoryLimiter:AnonSwap".
- **On-Device Anomaly Detection:** Part of ProfilingManager, you can leverage trigger-based profiling using `TRIGGER_TYPE_ANOMALY` to automatically capture heap dumps when the memory limit is reached.

```kotlin
val profilingManager = applicationContext
   .getSystemService(ProfilingManager::class.java)

val triggers = ArrayList<ProfilingTrigger>().apply {
  add(ProfilingTrigger.Builder(
    ProfilingTrigger.TRIGGER_TYPE_ANOMALY).build())
}
profilingManager.addProfilingTriggers(triggers)
```

And, we're working to surface more in-field memory metrics to you within Google Play Console.

### Generational garbage collection

[Android 17](https://developer.android.com/about/versions) introduces more frequent, less resource-intensive young-generation collections to[ART](https://developer.android.com/guide/platform#art)'s Concurrent Mark-Compact garbage collector (GC). By separating short-lived objects from stable, long-lived ones, the system runs frequent, lightweight "young-generation" sweeps rather than expensive full-heap scans, drastically reducing CPU usage, power drain, and UI stutter. Our testing has shown significant improvements in GC interference with application threads and a reduction in the maximum memory resident set size (RSS). ART improvements are also available to over a billion devices running Android 12 (API level 31) and higher through Google Play System updates.

### Lock-Free MessageQueue

For apps targeting SDK 37 or higher, the core [android.os.MessageQueue](https://developer.android.com/reference/android/os/MessageQueue) now implements a lock-free architecture, significantly reducing missed frames, improving app startup time, and radically improving the performance of busy queues in multithreaded scenarios. Note: This can break apps that use reflection on private [MessageQueue](https://developer.android.com/reference/android/os/MessageQueue) fields and methods. The [peekWhen](https://developer.android.com/reference/android/os/TestLooperManager#peekWhen()) and [poll](https://developer.android.com/reference/android/os/TestLooperManager#poll()) APIs have been added to [TestLooperManager](https://developer.android.com/reference/android/os/TestLooperManager) for instrumentation testing without relying on [MessageQueue](https://developer.android.com/reference/android/os/MessageQueue) internals.

### Static final fields now truly final

Starting from Android 17, apps targeting SDK 37 or higher won't be able to modify "static final" fields, allowing the runtime to apply performance optimizations more aggressively. An attempt to do so via reflection (or deep reflection) will lead to an IllegalAccessException being thrown.

Modifying them via JNI's `SetStatic<Type>Field` methods family will immediately crash the application.

### Custom notification view restrictions

To reduce memory usage we are further restricting the size of[custom notification views](https://developer.android.com/develop/ui/views/notifications/custom-notification). This update closes a loophole that allows apps to bypass existing limits using URIs. This behavior is gated by the target SDK version and takes effect for apps targeting API 37 and higher.

## Privacy \& Security

Maintaining user trust is at the heart of the Android ecosystem. Android 17 introduces robust features that protect sensitive data while simplifying user experiences.

### Privacy-preserving choices

Historically, apps required broad, permanent permissions to access information like contacts, precise location and media files. Android 17 continues the shift toward privacy-preserving choices that grant temporary, session-based access only to the data the user explicitly selects:

- **System-Level Contact Picker:** Utilizing `ACTION_PICK_CONTACTS`, apps can request temporary access only to specific fields (e.g., email or phone number) chosen by the user, eliminating the need for the broad `READ_CONTACTS` permission. It also fully supports work/personal profile separation.
- **Customizable Photo Picker aspect ratio:** Using PhotoPickerUiCustomizationParams, you can customize the system photo picker to show thumbnails in portrait mode. This is perfect for apps that always display photos and videos in portrait such as video based social media apps.
- **System-rendered Location Button:** A new system-rendered location button that you can embed in your app grants precise location access for the current session only.
- **EyeDropper API:** A new system-level API, `ACTION_OPEN_EYE_DROPPER`, allows your app to create a system-powered eyedropper enabling the user to select color from any pixel on the display. This provides a secure, privacy-preserving color-picking experience that eliminates the need for broad, sensitive screen capture or media projection permissions.

```kotlin
val eyeDropperLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
   if (result.resultCode == Activity.RESULT_OK) {
       val color = result.data?.getIntExtra(Intent.EXTRA_COLOR, Color.BLACK)
       // Use the picked color in your app
   }
}
fun launchColorPicker() {
   val intent = Intent(Intent.ACTION_OPEN_EYE_DROPPER)
   eyeDropperLauncher.launch(intent)
}
```
![Eyedropper Tester.webp](https://developer.android.com/static/blog/assets/Eyedropper_Tester_e6d521ab0a_1iI9YJ.webp) Picking a color from anywhere on the screen with the system EyeDropper

### Local network access

Apps targeting Android 17 now either require the [`ACCESS_LOCAL_NETWORK`](https://developer.android.com/reference/kotlin/android/Manifest.permission#access_local_network) runtime permission or the use of system-mediated, privacy-preserving device pickers for local network communication, such as talking to smart home devices or casting receivers. Because ACCESS_LOCAL_NETWORK falls under the existing [`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES) permission group, users who have already granted other [`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES) permissions will not be prompted again.

### SMS OTP protection

Android 17 expands SMS one-time-password (OTP) protection by delaying access to SMS messages for three hours:

- **WebOTP Format:** [Delayed for all apps that are not the intended recipient (domain mismatch).](https://developer.android.com/about/versions/17/behavior-changes-all#sms-otp-all-apps)
- **Standard SMS OTP:** [Delayed for all apps targeting SDK 37+.](https://developer.android.com/about/versions/17/behavior-changes-17#sms-otp-protection)

**Exemptions:** Default SMS, assistant, and connected companion apps are exempt. Apps are strongly encouraged to migrate to the [SMS Retriever](https://developer.android.com/identity/sms-retriever) or [SMS User Consent](https://developers.google.com/identity/sms-retriever/user-consent/overview) APIs.

### Post-Quantum Cryptography (PQC)

Android 17 is ready for the next generation of cryptographic security:

- **Keystore Integration:** Supported devices can generate ML-DSA (Module-Lattice-Based Digital Signature Algorithm) keys in secure hardware to produce quantum-safe signatures, exposed via standard JCA APIs.
- **Hybrid APK Signing:** Introducing the v3.2 APK Signature Scheme, which combines classical signatures with ML-DSA signatures to secure app delivery.

### Safer native dynamic code loading

If your app targets SDK 37 or higher, the Safer Dynamic Code Loading (DCL) protection [introduced in Android 14](https://developer.android.com/about/versions/14/behavior-changes-14#safer-dynamic-code-loading) for DEX and JAR files now extends to native libraries. All native files loaded using System.load must be marked as read-only. Otherwise, the system throws `UnsatisfiedLinkError`.

### Smarter password protection for physical inputs

With Android 17, we're making it safer to enter passwords, PINs, and other secrets when using a physical keyboard by no longer showing the last typed character by default.

Users can still easily customize these display settings to match their preferences (availability may vary by device manufacturer).

These enhanced privacy protections are automatically supported byAndroid's built-in SDK components and will be supported in Compose 1.12 for `SecureTextFields`.   
![Hide First Letter.gif](https://developer.android.com/static/blog/assets/Hide_First_Letter_274ffb63c2_p6kOS.webp) Smarter password protection for physical inputs

## Media and camera features that empower creators and delight users

Android 17 introduces new [creator features](https://blog.google/products-and-platforms/platforms/android/android-17-creator-features/) that give access to pro-quality cameras and media, all while improving the experience for consumers.

- [Eclipsa Video](https://developer.android.com/media/platform/integrate-eclipsa-video): HDR video standard built upon the [SMPTE ST 2094-50 specification](https://github.com/SMPTE/st2094-50) that introduces new metadata to help devices adapt content for their display headroom and ambient light conditions, as well as improve the simultaneous display of standard and HDR content.
- **RAW14 image format:** New support for the [RAW14 image format](https://developer.android.com/reference/kotlin/android/graphics/ImageFormat#raw14) provides a way for your professional camera app to capture the highest level of detail and color depth from compatible camera sensors.
- **Vendor-defined camera extensions:** Vendor-defined extensions enable hardware partners to define and implement custom camera extension modes, providing access to the best and latest camera features.
- **Extended HE-AAC software encoder: A new system-provided Extended HE-AAC software encoder, supports both low and high bitrates using unified speech and audio coding, providing significantly better audio quality for voice messages in low-bandwidth conditions, including support for loudness metadata.**
- [Versatile Video Coding (H.266)](https://developer.android.com/guide/topics/media/media-formats#video-formats): Enables OEMs to add codec support by defining the [video/vvc](https://developer.android.com/guide/topics/media/media-formats#video-formats) MIME type in [MediaFormat](https://developer.android.com/reference/android/media/MediaFormat), adding new VVC profiles in [MediaCodecInfo](https://developer.android.com/reference/android/media/MediaCodecInfo), and integrating support into [MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor).
- **Camera device type:** New APIs that query the underlying device type to identify if a camera is built-in hardware, an external USB webcam, or a virtual camera.
- **Constant Quality for Video Recording:** [setVideoEncodingQuality](https://developer.android.com/reference/android/media/MediaRecorder#setVideoEncodingQuality(int)) in[MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder) configures a constant quality (CQ) mode for video encoders to ensure uniform visual fidelity across the entire video.

### Better support for hearing aids

- **Bluetooth LE Audio hearing aid support:** Android now includes a specific device category for Bluetooth Low Energy (BLE) Audio hearing aids with the new [AudioDeviceInfo.TYPE_BLE_HEARING_AID](https://developer.android.com/reference/android/media/AudioDeviceInfo#TYPE_BLE_HEARING_AID) constant, so your app can distinguish hearing aids from regular headsets to provide a tailored experience for users with assistive listening devices.
- **Granular audio routing for hearing aids:** Android 17 allows users to independently manage where specific system sounds are played. They can choose to route notifications, ringtones, and alarms to connected hearing aids or the device's built-in speaker, helping to avoid unwanted in-ear interruptions while maintaining a Bluetooth connection for hearing aid management apps.

### CameraX and Media3

[CameraX](https://developer.android.com/jetpack/androidx/releases/camerax) and [Media3](https://developer.android.com/jetpack/androidx/releases/media3) have been updated for Android 17. They are there to do the heavy lifting, smoothing the rough edges of media development and simplifying building reliable camera capture, smooth media playback, and creative and complex editing experiences.

We've released an [agent skill](https://github.com/android/skills/tree/main/camera) that can migrate legacy Android camera implementations (Camera1 or raw Camera2 APIs) to CameraX.

**Note: You'll need to update your CameraX version to either 1.5.2 or 1.6.0+ to avoid a crash related to an added dynamic range mode on Android 17 devices.**

## Get your apps, libraries, tools, and game engines ready!

If you develop an Android SDK, library, tool, or game engine, it's critical to prepare any necessary updates now to prevent your downstream app and game developers from being blocked by compatibility issues and allow them to target the latest SDK features. Please let your downstream developers know if updates are needed to fully support Android 17.

Testing involves installing your production app or a test app making use of your library or engine using Google Play or other means onto a device or emulator running Android 17 Beta 4. Work through all your app's flows and look for functional or UI issues. Each release of Android contains platform changes that improve privacy, security, and overall user experience; review the app impacting behavior changes for apps [running on](https://developer.android.com/about/versions/17/behavior-changes-all) and [targeting](https://developer.android.com/about/versions/17/behavior-changes-17) Android 17 to focus your testing, including the following:

- **Resizability on large screens:** Once you target Android 17 (SDK 37), you can no longer opt out of maintaining orientation, resizability and aspect ratio constraints [on large screens](https://developer.android.com/about/versions/17/changes/ff-restrictions-ignored).
- **Dynamic code loading:** If your app targets SDK 37 or higher, the Safer Dynamic Code Loading (DCL) protection [introduced in Android 14](https://developer.android.com/about/versions/14/behavior-changes-14#safer-dynamic-code-loading) for DEX and JAR files now extends to native libraries. All native files loaded using System.load() must be marked as read-only. Otherwise, the system throws UnsatisfiedLinkError.
- **Enable CT by default:** [Certificate transparency (CT)](https://developer.android.com/privacy-and-security/security-config#CertificateTransparencySummary) is enabled by default. (On Android 16, CT is available but apps had to [opt in](https://developer.android.com/privacy-and-security/security-config#certificateTransparency).)
- **Local network protections:** Apps targeting SDK 37 or higher have [local network access blocked by default](https://developer.android.com/privacy-and-security/local-network-permission#android-17-enforcement). Switch to using privacy preserving pickers if possible, and use the new [`ACCESS_LOCAL_NETWORK`](https://developer.android.com/reference/kotlin/android/Manifest.permission#access_local_network) permission for broad, persistent access.
- **Background audio hardening:** Starting in Android 17, the audio framework enforces [restrictions on background audio interactions](https://developer.android.com/about/versions/17/changes/bg-audio) including audio playback, [audio focus](https://developer.android.com/media/optimize/audio-focus) requests, and [volume change](https://developer.android.com/reference/android/media/AudioManager#adjustStreamVolume(int,%20int,%20int)) APIs. Based on your feedback, we've made some changes since beta 2, including targetSDK gating while-in-use FGS enforcement and exempting alarm audio. Full details available in the [updated guidance](https://developer.android.com/about/versions/17/changes/bg-audio).
- **NPU access declaration:** Apps targeting Android 17 that need to directly access the NPU must declare [`FEATURE_NEURAL_PROCESSING_UNIT`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#feature_neural_processing_unit) in their manifest to avoid being blocked from accessing the NPU. This includes apps that use the[LiteRT NPU delegate](https://ai.google.dev/edge/litert/next/npu), vendor-specific SDKs, as well as the deprecated[NNAPI](https://developer.android.com/ndk/guides/neuralnetworks).

## Get started with Android 17

Your Pixel device should get Android 17 shortly if you haven't already been on the Android Beta. If you don't have a Pixel device, you can [use the 64-bit system images with the Android Emulator](https://developer.android.com/about/versions/17/get#on_emulator) in Android Studio. If you are currently on Android 17 Beta 4.1 and have not yet taken an Android 17 QPR1 beta, you can opt out of the program and you will then be offered the release version of Android 17 over the air.

## Getting the Android 17 beta on partner devices

Android 17 is available in beta on handset, tablet, and foldable form factors [from partners](https://developer.android.com/about/versions/17/devices) including Honor, iQOO, Lenovo, OnePlus, OPPO, Realme, Sharp, vivo, and Xiaomi.
![android-17-beta-partners.jpg](https://developer.android.com/static/blog/assets/android_17_beta_partners_f983e5def9_Z1fKXPq.webp)

For the best development experience with Android 17, we recommend that you use the latest Canary build of [Android Studio Quail](https://developer.android.com/studio/preview). Once you're set up, here are some of the things you should do:

- Test your current app for compatibility, learn whether your app is [affected by changes in Android 17](https://developer.android.com/about/versions/17/behavior-changes-all), and install your app onto a device or [Android Emulator](https://developer.android.com/studio/run/emulator) running Android 17 and extensively test it.

Thank you again to everyone who participated in our Android developer preview and beta program. We're looking forward to seeing how your apps take advantage of the updates in Android 17, and have plans to bring you updates in a fast-paced release cadence going forward.

For complete information on Android 17 please visit the [Android 17 developer site](https://developer.android.com/about/versions/17).
- [#Android 17](https://developer.android.com/blog/topics/android-17)
Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)
Continue reading
- [![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp)](https://developer.android.com/blog/authors/tibian-elsheikh)[![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp)](https://developer.android.com/blog/authors/jeffrey-jose) 29 Jun 2026 29 Jun 2026 ![](https://developer.android.com/static/blog/assets/Eclipsa_Video_V01_White_Strapi_10c5296e18_R3bTD.webp)

  ## [Eclipsa Video: HDR That Looks Right on Every Screen](https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen)

  [arrow_forward](https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen) We've all been there: You're scrolling through your favorite social media feed in a dim room, and suddenly an HDR video pops up. It's so intensely bright that you have to squint, or maybe you find yourself turning down your screen brightness just to read the caption.
  [Tibian Elsheikh](https://developer.android.com/blog/authors/tibian-elsheikh), [Jeffrey Jose](https://developer.android.com/blog/authors/jeffrey-jose) • 2 min read
- 3 Authors 22 Jun 2026 22 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_5c55395a9c_UkzvN.webp)

  ## [Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini)

  [arrow_forward](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini) At this year's Google I/O, we announced an update for spatial experiences: the Geospatial API is now available as a preview in ARCore for Jetpack XR.
  [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus), [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni), [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1) • 7 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Third Beta of Android 17](https://developer.android.com/blog/posts/the-third-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-third-beta-of-android-17) Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 5 min read
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#beta](https://developer.android.com/blog/topics/beta)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)