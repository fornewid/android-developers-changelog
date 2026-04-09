---
title: The Third Beta of Android 17  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/the-third-beta-of-android-17
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# The Third Beta of Android 17

###### 5-min read

![](/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

26

Mar
2026

[![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](/blog/authors/matthew-mccullough)

[##### Matthew McCullough](/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

[Android 17](/about/versions/17) has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store. In addition, Beta 3 brings a host of new capabilities to help you build better, more secure, and highly integrated applications.

### Get your apps, libraries, tools, and game engines ready!

If you develop an SDK, library, tool, or game engine, it's even more important to prepare any necessary updates now to prevent your downstream app and game developers from being blocked by compatibility issues and allow them to target the latest SDK features. Please let your downstream developers know if updates are needed to fully support Android 17.

![large_Android17Timeline01.png](/static/blog/assets/large_Android17_Timeline01_134db2bea6_Z1i8Hgs.webp)

Testing involves installing your production app or a test app making use of your library or engine using Google Play or other means onto a device or emulator running Android 17 Beta 3. Work through all your app's flows and look for functional or UI issues. Review the behavior changes to focus your testing. Each release of Android contains platform changes that improve privacy, security, and overall user experience, and these changes can affect your apps. Here are some changes to focus on:

* **Resizability on large screens:** Once you target Android 17, you can no longer opt out of maintaining orientation, resizability and aspect ratio constraints [on large screens](/about/versions/17/changes/ff-restrictions-ignored).
* **Dynamic code loading:** If your app targets Android 17 or higher, the Safer Dynamic Code Loading (DCL) protection introduced in Android 14 for DEX and JAR files now extends to native libraries. All native files loaded using System.load() must be marked as read-only. Otherwise, the system throws UnsatisfiedLinkError.
* **Enable CT by default**: [Certificate transparency (CT)](/privacy-and-security/security-config#CertificateTransparencySummary) is enabled by default. (On Android 16, CT is available but apps had to opt in.)
* **Local network protections**: Apps targeting Android 17 or higher have local network access blocked by default. Switch to using privacy preserving pickers if possible, and use the new ACCESS\_LOCAL\_NETWORK for broad, persistent access.

### Media and camera enhancements

#### Photo Picker customization options

Android now allows you to tailor the visual presentation of the photo picker to better complement your app’s user interface. By leveraging the new [PhotoPickerUiCustomizationParams](/reference/android/widget/photopicker/PhotoPickerUiCustomizationParams) API, you can modify the grid view aspect ratio from the standard 1:1 square to a 9:16 portrait display. This flexibility extends to both the ACTION\_PICK\_IMAGES intent and the embedded photo picker, enabling you to maintain a cohesive aesthetic when users interact with media.

![large_(Default)11aspectratio.png](/static/blog/assets/large_Default_11aspectratio_7ae50afc21_ZxN28a.webp)

This is all part of our effort to help make the privacy-preserving Android photo picker fit seamlessly with your app experience. [Learn more about how you can embed the photo picker directly into your app for the most native experience](https://android-developers.googleblog.com/2026/01/httpsandroid-developers.googleblog.com202506android-embedded-photo-picker.html%20.html).

```
  val params = PhotoPickerUiCustomizationParams.Builder()
.setAspectRatio(PhotoPickerUiCustomizationParams.ASPECT_RATIO_PORTRAIT_9_16)
.build()
val intent = Intent(MediaStore.ACTION_PICK_IMAGES).apply {
putExtra(MediaStore.EXTRA_PICK_IMAGES_UI_CUSTOMIZATION_PARAMS, params)
}
startActivityForResult(intent, REQUEST_CODE)
```

**Support for the RAW14 image format:** Android 17 introduces support for the RAW14 image format — the de-facto industry standard for high-end digital photography — via the new ImageFormat.RAW14 constant. RAW14 is a single-channel, 14-bit per pixel format that uses a densely packed layout where every four consecutive pixels are packed into seven bytes.

**Vendor-defined camera extensions:** Android 17 adds Vendor-defined extensions to enable hardware partners define and implement custom camera extension modes to provide you access to the best and latest camera features, such as 'Super Resolution' or cutting-edge AI-driven enhancements. You can query for these modes using the isExtensionSupported(int) API.

**Camera device type APIs:** New Android 17 APIs allow you to query the underlying device type to identify if a camera is built-in hardware, an external USB webcam, or a virtual camera.

#### Bluetooth LE Audio hearing aid support

Android now includes a specific device category for Bluetooth Low Energy (BLE) Audio hearing aids. With the addition of the [AudioDeviceInfo.TYPE\_BLE\_HEARING\_AID](/reference/android/media/AudioDeviceInfo#TYPE_BLE_HEARING_AID) constant, your app can now distinguish hearing aids from regular headsets.

```
  val audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
val devices = audioManager.getDevices(AudioManager.GET_DEVICES_OUTPUTS)
val isHearingAidConnected = devices.any { it.type == AudioDeviceInfo.TYPE_BLE_HEARING_AID }
```

#### Granular audio routing for hearing aids

Android 17 allows users to independently manage where specific system sounds are played. They can choose to route notifications, ringtones, and alarms to connected hearing aids or the device's built-in speaker.

#### Extended HE-AAC software encoder

Android 17 introduces a system-provided Extended HE-AAC software encoder. This encoder supports both low and high bitrates using unified speech and audio coding. You can access this encoder via the [MediaCodec](/reference/android/media/MediaCodec) API using the name `c2.android.xheaac.encoder` or by querying for the `audio/mp4a-latm` MIME type.

```
  val encoder = MediaCodec.createByCodecName("c2.android.xheaac.encoder")
val format = MediaFormat.createAudioFormat(MediaFormat.MIMETYPE_AUDIO_AAC, 48000, 1)
format.setInteger(MediaFormat.KEY_BIT_RATE, 24000)
format.setInteger(MediaFormat.KEY_AAC_PROFILE, MediaCodecInfo.CodecProfileLevel.AACObjectXHE)
encoder.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
```

### Performance and Battery Enhancements

#### Reduce wakelocks with listener support for allow-while-idle alarms

Android 17 introduces a new variant of AlarmManager.setExactAndAllowWhileIdle that accepts an OnAlarmListener instead of a PendingIntent. This new callback-based mechanism is ideal for apps that currently rely on continuous wakelocks to perform periodic tasks, such as messaging apps maintaining socket connections.

```
  val alarmManager = getSystemService(AlarmManager::class.java)
val listener = AlarmManager.OnAlarmListener {
// Do work here
}
alarmManager.setExactAndAllowWhileIdle(
AlarmManager.ELAPSED_REALTIME_WAKEUP,
SystemClock.elapsedRealtime() + 60000,
listener,
null
)
```

### Privacy updates

#### System-provided Location Button

![localcafe.jpg](/static/blog/assets/localcafe_7b76defb90_Z7SFAI.webp)

Android is introducing a system-rendered location button that you will be able to embed directly into your app's layout using an Android Jetpack library. When a user taps this system button, your app is granted precise location access for the current session only. To implement this, you need to declare the USE\_LOCATION\_BUTTON permission.

#### Discrete password visibility settings for touch and physical keyboards

This feature splits the existing "Show passwords" system setting into two distinct user preferences: one for touch-based inputs and another for physical (hardware) keyboard inputs. Characters entered via physical keyboards are now hidden immediately by default.

```
  val isPhysical = event.source and InputDevice.SOURCE_KEYBOARD == InputDevice.SOURCE_KEYBOARD
val shouldShow = android.text.ShowSecretsSetting.shouldShowPassword(context, isPhysical)
```

### Security

#### Enforced read-only dynamic code loading

To improve security against code injection attacks, Android now enforces that dynamically loaded native libraries must be read-only. If your app targets Android 17 or higher, all native files loaded using System.load() must be marked as read-only beforehand.

```
  val libraryFile = File(context.filesDir, "my_native_lib.so")
// Mark the file as read-only before loading to comply with Android 17+ security requirements
libraryFile.setReadOnly()
System.load(libraryFile.absolutePath)
```

#### Post-Quantum Cryptography (PQC) Hybrid APK Signing

To prepare for future advancements in quantum computing, Android is introducing support for Post-Quantum Cryptography (PQC) through the new v3.2 APK Signature Scheme. This scheme utilizes a hybrid approach, combining a classical signature with an ML-DSA signature.

### User experience and system UI

#### Better support for widgets on external displays

This feature improves the visual consistency of app widgets when they are shown on connected or external displays with different pixel densities using DP or SP units.

```
  val options = appWidgetManager.getAppWidgetOptions(appWidgetId)
val displayId = options.getInt(AppWidgetManager.OPTION_APPWIDGET_DISPLAY_ID)
val remoteViews = RemoteViews(context.packageName, R.layout.widget_layout)
remoteViews.setViewPadding(
R.id.container,
16f, 8f, 16f, 8f,
TypedValue.COMPLEX_UNIT_DIP
)
```

#### Hidden app labels on the home screen

![Hiddenapplabelsonthehomescreen.png](/static/blog/assets/Hiddenapplabelsonthehomescreen_564d344c7c_2aR4X3.webp)

Android now provides a user setting to hide app names (labels) on the home screen workspace. Ensure your app icon is distinct and recognizable.

#### Desktop Interactive Picture-in-Picture

Unlike traditional Picture-in-Picture, these pinned windows remain interactive while staying always-on-top of other application windows in desktop mode.

```
  val appTask: ActivityManager.AppTask = activity.getSystemService(ActivityManager::class.java).appTasks[0]
appTask.requestWindowingLayer(
ActivityManager.AppTask.WINDOWING_LAYER_PINNED,
context.mainExecutor,
object : OutcomeReceiver<Int, Exception> {
override fun onResult(result: Int) {
if (result == ActivityManager.AppTask.WINDOWING_LAYER_REQUEST_GRANTED) {
// Task successfully moved to pinned layer
}
}
override fun onError(error: Exception) {}
}
)
```

#### Redesigned screen recording toolbar

![large_Recording-redesign.png](/static/blog/assets/large_Recording_redesign_80bab493fe_1Xu1kV.webp)

### Core functionality

#### VPN app exclusion settings

By using the new ACTION\_VPN\_APP\_EXCLUSION\_SETTINGS Intent, your app can launch a system-managed Settings screen where users can select applications to bypass the VPN tunnel.

```
  val intent = Intent(Settings.ACTION_VPN_APP_EXCLUSION_SETTINGS)
if (intent.resolveActivity(packageManager) != null) {
startActivity(intent)
}
```

#### OpenJDK 25 and 21 API updates

This update brings extensive features and refinements from OpenJDK 21 and OpenJDK 25, including the latest Unicode support and enhanced SSL support for named groups in TLS.

### Get started with Android 17

You can [enroll any supported Pixel device](https://www.google.com/android/beta) or [use the 64-bit system images with the Android Emulator](/about/versions/17/get#on_emulator).

* Compile against the new SDK and report issues on the [feedback page](/about/versions/17/feedback).
* Test your current app for compatibility and learn whether your app is affected by changes in Android 17.

For complete information, visit the [Android 17 developer site](/about/versions/17).

* [#Android 17](/blog/topics/android-17)
* [#beta](/blog/topics/beta)

###### Written by:

* ## [Matthew McCullough](/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read\_more
  View profile](/blog/authors/matthew-mccullough)

  ![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

  ![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

* [![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](/blog/authors/matthew-mccullough)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow\_forward](/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](/blog/authors/matthew-mccullough) • 2 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)](/blog/authors/robert-clifford)

  26

  Mar
  2026

  26

  Mar
  2026

  ![](/static/blog/assets/Redefining_Location_5e4a362604_Z1wl0mf.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Redefining Location Privacy: New Tools and Improvements for Android 17](/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17)

  [arrow\_forward](/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17)

  A pillar of the Android ecosystem is our shared commitment to user trust. As the mobile landscape has evolved, so does our approach to protecting sensitive information.

  ###### [Robert Clifford](/blog/authors/robert-clifford) • 3 min read

  + [#Android 17](/blog/topics/android-17)
* [![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](/blog/authors/matthew-mccullough)

  05

  Mar
  2026

  05

  Mar
  2026

  ![](/static/blog/assets/android_Bench_f2e4dd4fda_2816Hg.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Elevating AI-assisted Android development and improving LLMs with Android Bench](/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench)

  [arrow\_forward](/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench)

  We want to make it faster and easier for you to build high-quality Android apps, and one way we’re helping you be more productive is by putting AI at your fingertips.

  ###### [Matthew McCullough](/blog/authors/matthew-mccullough) • 2 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)