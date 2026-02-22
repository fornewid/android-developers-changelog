---
title: https://developer.android.com/about/versions/jelly-bean
url: https://developer.android.com/about/versions/jelly-bean
source: md.txt
---

# Jelly Bean

### Android 4.3

[![Android 4.3 on phone and tablet](https://developer.android.com/static/images/jb-android-43.jpg)](https://developer.android.com/static/images/jb-android-43_2x.png)

Welcome to Android 4.3, a sweeter version ofJelly Bean!

Android 4.3 includes performance optimizations and great new features for users and developers. This document provides a glimpse of what's new for developers.

See the[Android 4.3 APIs](https://developer.android.com/about/versions/android-4.3)document for a detailed look at the new developer APIs.

Find out more about the new Jelly Bean features for users at[www.android.com](https://www.android.com/whatsnew).

## Faster, Smoother, More Responsive

Android 4.3 builds on the performance improvements already included in Jelly Bean ---**vsync timing** ,**triple buffering** ,**reduced touch latency** ,**CPU input boost** , and**hardware-accelerated 2D rendering**--- and adds new optimizations that make Android even faster.

For a graphics performance boost, the hardware-accelerated 2D renderer now**optimizes the stream of drawing commands** , transforming it into a more efficient GPU format by rearranging and merging draw operations. For multithreaded processing, the renderer can also now use**multithreading across multiple CPU cores**to perform certain tasks.

Android 4.3 also improves**rendering for shapes and text**. Shapes such as circles and rounded rectangles are now rendered at higher quality in a more efficient manner. Optimizations for text include increased performance when using multiple fonts or complex glyph sets (CJK), higher rendering quality when scaling text, and faster rendering of drop shadows.

**Improved window buffer allocation**results in a faster image buffer allocation for your apps, reducing the time taken to start rendering when you create a window.

For highest-performance graphics, Android 4.3 introduces support for**OpenGL ES 3.0** and makes it accessible to apps through both framework and native APIs. On supported devices, the hardware accelerated 2D rendering engine takes advantage of OpenGL ES 3.0 to optimize**texture management** and increase**gradient rendering fidelity**.

## OpenGL ES 3.0 for High-Performance Graphics

Android 4.3 introduces platform support for[Khronos OpenGL ES 3.0](http://www.khronos.org/opengles/3_X/), providing games and other apps with highest-performance 2D and 3D graphics capabilities on supported devices. You can take advantage of OpenGL ES 3.0 and related EGL extensions using either**framework APIs** or**native API bindings**through the Android Native Development Kit (NDK).

Key new functionality provided in OpenGL ES 3.0 includes acceleration of advanced visual effects, high quality ETC2/EAC texture compression as a standard feature, a new version of the GLSL ES shading language with integer and 32-bit floating point support, advanced texture rendering, and standardized texture size and render-buffer formats.

You can use the OpenGL ES 3.0 APIs to create highly complex, highly efficient graphics that run across a range of compatible Android devices, and you can support a single, standard texture-compression format across those devices.

OpenGL ES 3.0 is an optional feature that depends on underlying graphics hardware. Support is already available on Nexus 7 (2013), Nexus 4, and Nexus 10 devices.

## Enhanced Bluetooth Connectivity

#### Connectivity with Bluetooth Smart devices and sensors

Now you can design and build apps that interact with the latest generation of small, low-power devices and sensors that use[Bluetooth Smart technology](http://www.bluetooth.com/Pages/Bluetooth-Smart-Devices.aspx).  
![](https://developer.android.com/static/images/jb-btle.png)

Android 4.3 gives you a single, standard API for interacting with Bluetooth Smart devices.

Android 4.3 introduces built-in platform support for**Bluetooth Smart Ready**in the central role and provides a standard set of APIs that apps can use to discover nearby devices, query for GATT services, and read/write characteristics.

With the new APIs, your apps can efficiently scan for devices and services of interest. For each device, you can check for supported GATT services by UUID and manage connections by device ID and signal strength. You can connect to a GATT server hosted on the device and read or write characteristics, or register a listener to receive notifications whenever those characteristics change.

You can implement support for any GATT profile. You can read or write standard characteristics or add support for custom characteristics as needed. Your app can function as either client or server and can transmit and receive data in either mode. The APIs are generic, so you'll be able to support interactions with a variety of devices such as proximity tags, watches, fitness meters, game controllers, remote controls, health devices, and more.

Support for Bluetooth Smart Ready is already available on Nexus 7 (2013) and Nexus 4 devices and will be supported in a growing number of Android-compatible devices in the months ahead.

#### AVRCP 1.3 Profile

Android 4.3 adds built-in support for**Bluetooth AVRCP 1.3** , so your apps can support richer interactions with remote streaming media devices. Apps such as media players can take advantage of AVRCP 1.3 through the**remote control client APIs**introduced in Android 4.0. In addition to exposing playback controls on the remote devices connected over Bluetooth, apps can now transmit metadata such as track name, composer, and other types of media metadata.

Platform support for AVRCP 1.3 is built on the Bluedroid Bluetooth stack introduced by Google and Broadcom in Android 4.2. Support is available right away on Nexus devices and other Android-compatible devices that offer A2DP/AVRCP capability.

## Support for Restricted Profiles

![Setting up a Restricted Profile](https://developer.android.com/static/images/jb-profiles-create-n713.png)

A tablet owner can set up one or more restricted profiles in Settings and manage them independently.
![Setting Restrictions in a Profile](https://developer.android.com/static/images/jb-profiles-restrictions-n713.png)

Your app can offer restrictions to let owners manage your app content when it's running in a profile.

Android 4.3 extends the multiuser feature for tablets with**restricted profiles** , a new way to manage users and their capabilities on a single device. With restricted profiles, tablet owners can quickly set up**separate environments** for each user, with the ability to manage**finer-grained restrictions**in the apps that are available in those environments. Restricted profiles are ideal for friends and family, guest users, kiosks, point-of-sale devices, and more.

Each restricted profile offers an isolated and secure space with its own local storage, home screens, widgets, and settings. Unlike with users, profiles are created from the tablet owner's environment, based on the owner's installed apps and system accounts. The owner controls which installed apps are enabled in the new profile, and access to the owner's accounts is disabled by default.

Apps that need to access the owner's accounts --- for sign-in, preferences, or other uses --- can opt-in by declaring a manifest attribute, and the owner can review and manage those apps from the profile configuration settings.

For developers, restricted profiles offer a new way to deliver more value and control to your users. You can implement**app restrictions**--- content or capabilities controls that are supported by your app --- and advertise them to tablet owners in the profile configuration settings.

You can add app restrictions directly to the profile configuration settings using predefined boolean, select, and multi-select types. If you want more flexibility, you can even launch your own UI from profile configuration settings to offer any type of restriction you want.

When your app runs in a profile, it can check for any restrictions configured by the owner and enforce them appropriately. For example, a media app might offer a restriction to let the owner set a maturity level for the profile. At run time, the app could check for the maturity setting and then manage content according to the preferred maturity level.

If your app is not designed for use in restricted profiles, you can opt out altogether, so that your app can't be enabled in any restricted profile.

## Optimized Location and Sensor Capabilities

[Google Play services](https://developer.android.com/google/play-services)offers advanced location APIs that you can use in your apps. Android 4.3**optimizes these APIs**on supported devices with new hardware and software capabilities that minimize use of the battery.  
[![](https://developer.android.com/static/images/google/gps-location.png)]()

**Hardware geofencing**optimizes for power efficiency by performing location computation in the device hardware, rather than in software. On devices that support hardware geofencing, Google Play services geofence APIs will be able to take advantage of this optimization to save battery while the device is moving.

**Wi-Fi scan-only mode**is a new platform optimization that lets users keep Wi-Fi scan on without connecting to a Wi-Fi network, to improve location accuracy while conserving battery. Apps that depend on Wi-Fi for location services can now ask users to enable scan-only mode from Wi-Fi advanced settings. Wi-Fi scan-only mode is not dependent on device hardware and is available as part of the Android 4.3 platform.

New sensor types allow apps to better manage sensor readings. A**game rotation vector** lets game developers sense the device's rotation without having to worry about magnetic interference.**Uncalibrated gyroscope** and**uncalibrated magnetometer**sensors report raw measurements as well as estimated biases to apps.

The new hardware capabilities are already available on Nexus 7 (2013) and Nexus 4 devices, and any device manufacturer or chipset vendor can build them into their devices.

## New Media Capabilities

#### Modular DRM framework

To meet the needs of the next generation of media services, Android 4.3 introduces a**modular DRM framework**that enables media application developers to more easily integrate DRM into their own streaming protocols, such as MPEG DASH (Dynamic Adaptive Streaming over HTTP, ISO/IEC 23009-1).

Through a combination of new APIs and enhancements to existing APIs, the media DRM framework provides an**integrated set of services**for managing licensing and provisioning, accessing low-level codecs, and decoding encrypted media data. A new MediaExtractor API lets you get the PSSH metadata for DASH media. Apps using the media DRM framework manage the network communication with a license server and handle the streaming of encrypted data from a content library.

#### VP8 encoder

Android 4.3 introduces built-in support for**VP8 encoding** , accessible from framework and native APIs. For apps using native APIs, the platform includes**OpenMAX 1.1.2 extension headers**to support VP8 profiles and levels. VP8 encoding support includes settings for target bitrate, rate control, frame rate, token partitioning, error resilience, reconstruction and loop filters. The platform API introduces VP8 encoder support in a range of formats, so you can take advantage of the best format for your content.

VP8 encoding is available in software on all compatible devices running Android 4.3. For highest performance, the platform also supports hardware-accelerated VP8 encoding on capable devices.

#### Video encoding from a surface

Starting in Android 4.3 you can use a surface as the input to a video encoder. For example, you can now direct a stream from an OpenGL ES surface to the encoder, rather than having to copy between buffers.

#### Media muxer

Apps can use new media muxer APIs to combine elementary audio and video streams into a single output file. Currently apps can multiplex a single MPEG-4 audio stream and a single MPEG-4 video stream into a**single MPEG-4 output file**. The new APIs are a counterpart to the media demuxing APIs introduced in Android 4.2.

#### Playback progress and scrubbing in remote control clients

Since Android 4.0, media players and similar applications have been able to offer playback controls from remote control clients such as the device lock screen, notifications, and remote devices connected over Bluetooth. Starting in Android 4.3, those applications can now also expose playback**progress and speed** through their remote control clients, and receive commands to jump to a specific**playback position**.

## New Ways to Build Beautiful Apps

### Access to notifications

Notifications have long been a popular Android feature because they let users see information and updates from across the system, all in one place. Now in Android 4.3, apps can**observe the stream of notifications**with the user's permission and display the notifications in any way they want, including sending them to nearby devices connected over Bluetooth.

You can access notifications through new APIs that let you**register a notification listener**service and with permission of the user, receive notifications as they are displayed in the status bar. Notifications are delivered to you in full, with all details on the originating app, the post time, the content view and style, and priority. You can evaluate fields of interest in the notifications, process or add context from your app, and route them for display in any way you choose.

The new API gives you callbacks when a notification is added, updated, and removed (either because the user dismissed it or the originating app withdrew it). You'll be able to launch any intents attached to the notification or its actions, as well as dismiss it from the system, allowing your app to provide a complete user interface to notifications.

**Users remain in control** of which apps can receive notifications. At any time, they can look in Settings to see which apps have notification access and**enable or disable access**as needed. Notification access is disabled by default --- apps can use a new Intent to take the user directly to the Settings to enable the listener service after installation.

#### View overlays

You can now create**transparent overlays**on top of Views and ViewGroups to render a temporary View hierarchy or transient animation effects without disturbing the underlying layout hierarchy. Overlays are particularly useful when you want to create animations such as sliding a view outside of its container or dragging items on the screen without affecting the view hierarchy.

#### Optical bounds layout mode

A new layout mode lets you manage the positioning of Views inside ViewGroups according to their**optical bounds**, rather than their clip bounds. Clip bounds represent a widget's actual outer boundary, while the new optical bounds describe the where the widget appears to be, within the clip bounds. You can use the optical bounds layout mode to properly align widgets that use outer visual effects such as shadows and glows.

#### Custom rotation animation types

Apps can now define the exit and entry animation types used on a window when the device is rotated. You can set window properties to enable**jump-cut** ,**cross-fade** , or**standard**window rotation. The system uses the custom animation types when the window is fullscreen and is not covered by other windows.

#### Screen orientation modes

Apps can set new orientation modes for Activities to ensure that they are displayed in the proper orientation when the device is flipped. Additionally, apps can use a new mode to**lock the screen** to its current orientation. This is useful for apps using the camera that want to**disable rotation**while shooting video.

#### Intent for handling Quick Responses

Android 4.3 introduces a new public Intent that lets any app**handle Quick Responses**--- text messages sent by the user in response to an incoming call, without needing to pick up the call or unlock the device. Your app can listen for the intent and send the message to the caller over your messaging system. The intent includes the recipient (caller) as well as the message itself.

## Support for International Users

![](https://developer.android.com/static/images/jb-rtl-arabic-n4.png)![](https://developer.android.com/static/images/jb-rtl-hebrew-n4.png)

More parts of Android 4.3 are optimized for RTL languages.

#### RTL improvements

Android 4.3 includes RTL performance enhancements and broader RTL support across framework UI widgets, including ProgressBar/Spinner and ExpandableListView. More debugging information visible through the`uiautomatorviewer`tool. In addition, more system UI components are now RTL aware, such as notifications, navigation bar and the Action Bar.

To provide a better systemwide experience in RTL scripts, more default system apps now support RTL layouts, including Launcher, Quick Settings, Phone, People, SetupWizard, Clock, Downloads, and more.

#### Utilities for localization

![](https://developer.android.com/static/images/jb-pseudo-locale-zz.png)

Pseudo-locales make it easier to test your app's localization.

Android 4.3 also includes new utilities and APIs for creating better RTL strings and testing your localized UIs. A new**BidiFormatter**class provides a simple API for wrapping Unicode strings, so that RTL-script data is displayed as intended in LTR-locale messages and vice-versa. To let you use this utility more broadly in your apps, the BidiFormatter API is also now available for earlier platform versions through the Support Package in the Android SDK.

To assist you with managing date formatting across locales, Android 4.3 includes a new**getBestDateTimePattern()**method that automatically generates the best possible localized form of a Unicode UTS date for a locale that you specify. It's a convenient way to provide a more localized experience for your users.

To help you test your app more easily in other locales, Android 4.3 introduces**pseudo-locales** as a new developer option. Pseudo-locales simulate the language, script, and display characteristics associated with a locale or language group. Currently, you can test with a pseudo-locale for**Accented English**, which lets you see how your UI works with script accents and characters used in a variety of European languages.

## Accessibility and UI Automation

Starting in Android 4.3, accessibility services can**observe and filter key events**, such as to handle keyboard shortcuts or provide navigation parity with gesture-based input. The service receives the events and can process them as needed before they are passed to the system or other installed apps.

Accessibility services can declare**new capability attributes**to describe what their services can do and what platform features they use. For example, they can declare the capability to filter key events, retrieve window content, enable explore-by-touch, or enable web accessibility features. In some cases, services must declare a capability attribute before they can access related platform features. The system uses the service's capability attributes to generate an opt-in dialog for users, so they can see and agree to the capabilities before launch.

Building on the accessibility framework in Android 4.3, a new**UI automation framework**lets tests interact with the device's UI by simulating user actions and introspecting the screen content. Through the UI automation framework you can perform basic operations, set rotation of the screen, generate input events, take screenshots, and much more. It's a powerful way to automate testing in realistic user scenarios, including actions or sequences that span multiple apps.

## Enterprise and Security

#### Wi-Fi configuration for WPA2-Enterprise networks

Apps can now configure the**Wi-Fi credentials** they need for connections to**WPA2 enterprise access points**. Developers can use new APIs to configure Extensible Authentication Protocol (EAP) and Encapsulated EAP (Phase 2) credentials for authentication methods used in the enterprise. Apps with permission to access and change Wi-Fi can configure authentication credentials for a variety of EAP and Phase 2 authentication methods.

#### Android sandbox reinforced with SELinux

Android now uses**SELinux**, a mandatory access control (MAC) system in the Linux kernel to augment the UID based application sandbox. This protects the operating system against potential security vulnerabilities.

#### KeyChain enhancements

The KeyChain API now provides a method that allows applications to confirm that system-wide keys are bound to a**hardware root of trust** for the device. This provides a place to create or store private keys that**cannot be exported**off the device, even in the event of a root or kernel compromise.

#### Android Keystore Provider

Android 4.3 introduces a keystore provider and APIs that allow applications to create exclusive-use keys. Using the APIs, apps can create or store private keys that**cannot be seen or used by other apps**, and can be added to the keystore without any user interaction.

The keystore provider provides the same security benefits that the KeyChain API provides for system-wide credentials, such as binding credentials to a device. Private keys in the keystore cannot be exported off the device.

#### Restrict Setuid from Android Apps

The`/system`partition is now mounted`nosuid`for zygote-spawned processes, preventing Android applications from executing`setuid`programs. This reduces root attack surface and likelihood of potential security vulnerabilities.

## New Ways to Analyze Performance

![](https://developer.android.com/static/images/jb-systrace.png)

Systrace uses a new command syntax and lets you collect more types of profiling data.

#### Enhanced Systrace logging

Android 4.3 supports an enhanced version of the**Systrace** tool that's easier to use and that gives you access to more types of information to profile the performance of your app. You can now collect trace data from**hardware modules** ,**kernel functions** ,**Dalvik VM** including garbage collection,**resources loading**, and more.

Android 4.3 also includes new Trace APIs that you can use in your apps to mark specific sections of code to trace using Systrace**begin/end events**. When the marked sections of code execute, the system writes the begin/end events to the trace log. There's minimal impact on the performance of your app, so timings reported give you an accurate view of what your app is doing.

You can visualize app-specific events in a timeline in the Systrace output file and analyze the events in the context of other kernel and user space trace data. Together with existing Systrace tags, custom app sections can give you new ways to understand the performance and behavior of your apps.  
![](https://developer.android.com/static/images/jb-gpu-profile-clk-n4.png)![](https://developer.android.com/static/images/jb-gpu-profile-cal-n4.png)

On-screen GPU profiling in Android 4.3.

#### On-screen GPU profiling

Android 4.3 adds new developer options to help you analyze your app's performance and pinpoint rendering issues on any device or emulator.

In the**Profile GPU rendering** option you can now visualize your app's effective framerate on-screen, while the app is running. You can choose to display profiling data as on-screen**bar or line graphs**, with colors indicating time spent creating drawing commands (blue), issuing the commands (orange), and waiting for the commands to complete (yellow). The system updates the on-screen graphs continuously, displaying a graph for each visible Activity, including the navigation bar and notification bar.

A green line highlights the**16ms threshold**for rendering operations, so you can assess the your app's effective framerate relative to a 60 fps goal (because 1/60th of a second equals roughly 16ms). If you see operations that cross the green line, you can analyze them further using Systrace and other tools.

On devices running Android 4.2 and higher, developer options are hidden by default. You can reveal them at any time by tapping 7 times on**Settings \> About phone \> Build number**on any compatible Android device.

#### StrictMode warning for file URIs

The latest addition to the StrictMode tool is a policy constraint that warns when your app exposes a`file://`URI to the system or another app. In some cases the receiving app may not have access to the`file://`URI path, so when sharing files between apps, a`content://`URI should be used (with the appropriate permission). This new policy helps you catch and fix such cases. If you're looking for a convenient way to store and expose files to other apps, try using the`FileProvider`content provider that's available in the[Support Library](https://developer.android.com/tools/support-library).

### Android 4.2

![Android 4.2 on phone and tablet](https://developer.android.com/static/images/jb-device-2.png)

Welcome to Android 4.2, the latest version ofJelly Bean!

Android 4.2 has performance optimizations, a refreshed system UI, and great new features for users and developers. This document provides a glimpse of what's new for developers.

See the[Android 4.2 APIs](https://developer.android.com/about/versions/android-4.2)document for a detailed look at the new developer APIs.

Find out more about the new Jelly Bean features for users at[www.android.com](https://www.android.com/whatsnew).

## Faster, Smoother, More Responsive

Android 4.2 builds on the performance improvements already included in Jelly Bean ---**vsync timing** ,**triple buffering** ,**reduced touch latency** , and**CPU input boost**--- and adds new optimizations that make Android even faster.

Improvements in the**hardware-accelerated 2D renderer** make common animations such as scrolling and swiping smoother and faster. In particular,**drawing is optimized**for layers, clipping and certain shapes (rounded rects, circles and ovals).

A variety of**WebView rendering optimizations**make scrolling of web pages smoother and free from jitter and lags.

Android's**Renderscript Compute** is the first computation platform ported to run directly on a**mobile device GPU** . It automatically takes advantage of**GPU computation** resources whenever possible, dramatically improving performance for graphics and image processing. Any app using Renderscript on a supported device can benefit immediately from this GPU integration**without recompiling**.  
[![10-inch tablet running Android 4.2](https://developer.android.com/static/images/jb-nexus10-1.png)]()

## Refined, refreshed UI

Android 4.2 refines the Jelly Bean user experience and brings familiar Android UI patterns such as status bar, system bar, and notifications window to all tablets.

All screen sizes now feature the**status bar** on top, with pull-down access to**notifications** and a new**Quick Settings** menu. The familiar**system bar** appears on the bottom, with buttons easily accessible from either hand. The**Application Tray**is also available on all screen sizes.

## One tablet, many users

Now several users can**share a single Android tablet** , with each user having convenient access to a**dedicated user space**. Users can switch to their spaces with a single touch from the lock screen.

On a multiuser device, Android gives each user a separate environment, including user-specific emulated SD card storage. Users also have their own homescreens, widgets, accounts, settings, files, and apps, and the system keeps these separate. All users share core system services, but the system ensures that each user's applications and data remain isolated. In effect, each of the multiple users has their own Android device.

Users can install and uninstall apps at any time in their own environments. To save storage space, Google Play downloads an APK only if it's not already installed by another user on the device. If the app is already installed, Google Play records the new user's installation in the usual way but doesn't download another copy of the app. Multiple users can run the same copy of an APK because the system creates a new instance for each user, including a user-specific data directory.

For developers,**multi-user support is transparent**--- your apps do not need to do anything special to run normally in a multi-user environment and there are no changes you need to make in your existing or published APKs. The system manages your app in each user space just as it does in a single-user environment.

## New ways to engage users

![Calendar lock screen widget](https://developer.android.com/static/images/jb-lock-calendar.png)

You can extend**app widgets**to run on the lock screen, for instant access to your content.

### Lock screen widgets

In Android 4.2, users can place**app widgets** directly on their**lock screens**, for instant access to favorite app content without having to unlock. Users can add as many as five lock screen widgets, choosing from widgets provided by installed apps. The lock screen displays each widget in its own panel, letting users swipe left and right to view different panels and their widgets.

Like all app widgets, lock screen widgets can display**any kind of content**and they can accept direct user interaction. They can be entirely self-contained, such as a widget that offers controls to play music, or they can let users jump straight to an Activity in your app, after unlocking along the way as needed.

For developers, lock screen widgets offer a great new way to engage users. They let you put your content in front of users in a location they'll see often, and they give you more opportunities to bring users directly into your app.

You can take advantage of this new capability by building a new app widget or by extending an existing home screen widget. If your app already includes home screen widgets, you can extend them to the lock screen with minimal change. To give users an optimal experience, you can update the widget to use the full lock screen area when available and resize when needed on smaller screens. You can also add features to your widgets that might be especially useful or convenient on the lock screen.

### Daydream

Daydream is an**interactive screensaver mode**that starts when a user's device is docked or charging. In this mode, the system launches a daydream --- a remote content service provided by an installed app --- as the device screensaver. A user can enable Daydream from the Settings app and then choose the daydream to display.

Daydreams combine the best capabilities of live wallpapers and home screen widgets, but they are more powerful. They let you offer the any kind of content in a completely new context, with user interactions such as flipping through photos, playing audio or video, or jumping straight into your app with a single touch.

Because daydreams can start automatically when a device is charging or docked, they also give your app a great way to support new types of user experiences, such as leanback or exhibition mode, demo or kiosk mode, and "attract mode" --- all without requiring special hardware.  
![Daydream screensaver mode](https://developer.android.com/static/images/jb-dream-1.png)

Daydreamlets you create powerful interactive screensavers that display any kind of content.

Daydreams are similar to Activities and can do anything that Activity can do --- from rendering a UI hierarchy (without using RemoteViews) to drawing directly using Canvas, OpenGL, SurfaceTexture, and more. They can play video and audio and they can even accept direct user interaction. However, daydreams are not Activities, so they don't affect the backstack or appear in Recents and they cannot be launched directly from your app.

Implementing a daydream is straightforward and you can take advantage of UI components and resources that you've already created for other parts of your app. You can provide multiple daydreams in your app and you can offer distinct content and display settings for each.

## External display support

Android 4.2 introduces platform support for**external displays**that goes far beyond mirroring --- apps can now target unique content to any one or multiple displays that are attached to an Android device. Apps can build on this to deliver new kinds of interaction and entertainment experiences to users.

### Display manager

Apps interact with displays through a new display manager system service. Your app can enumerate the displays and check the capabilities of each, including size, density, display name, ID, support for secure video, and more. Your app can also receive callbacks when displays are added or removed or when their capabilities change, to better manage your content on external displays.

### Presentation window

To make it easy to show content on an external display, the framework provides a new UI object called a**Presentation**--- a type of dialog that represents a window for your app's content on a specific external display. Your app just gives the display to use, a theme for the window, and any unique content to show. The Presentation handles inflating resources and rendering your content according to the characteristics of the targeted display.  
![](https://developer.android.com/static/images/external-display.png)

You can take full control of two or more independent displays using**Presentation**.

A Presentation gives your app full control over the remote display window and its content and lets you manage it based on user input events such as key presses, gestures, motion events, and more. You can use all of the normal tools to create a UI and render content in the Presentation, from building an arbitrary view hierarchy to using SurfaceView or SurfaceTexture to draw directly into the window for streamed content or camera previews.

### Preferred display selection

When multiple external displays are available, you can create as many Presentations as you need, with each one showing unique content on a specific display. In many cases, you might only want to show your content on a single external display --- but always on the that's best for Presentation content. For this, the system can help your app choose the best display to use.

To find the best display to use, your app can query the display manager for the system's**preferred Presentation display**and receive callbacks when that display changes. Alternatively, you can use the media router service, extended in Android 4.2, to receive notifications when a system video route changes. Your app can display content by default in the main Activity until a preferred Presentation display is attached, at which time it can automatically switch to Presentation content on the preferred display. Your apps can also use media router's MediaRouteActionProvider and MediaRouteButton to offer standard display-selection UI.

### Protected content

For apps that handle protected or encrypted content, the display API now reports the**secure video capabilities**of attached displays. Your app query a display to find out if it offers a secure video output or provides protected graphics buffers and then choose the appropriate content stream or decoding to make the content viewable. For additional security on SurfaceView objects, your app can set a secure flag to indicate that the contents should never appear in screenshots or on a non-secure display output, even when mirrored.

### Wireless display

Starting in Android 4.2, users on supported devices can connect to an external display over Wi-Fi, using Wi-Fi Display (a peer-to-peer wireless display solution that complies with the[Miracast™](http://www.wi-fi.org/wi-fi-certified-miracast%E2%84%A2)certification program). When a wireless display is connected, users can stream any type of content to the big screen, including photos, games, maps, and more.

Apps can take advantage of**wireless displays**in the same way as they do other external displays and no extra work is needed. The system manages the network connection and streams your Presentation or other app content to the wireless display as needed.

## Native RTL support

![RTL layout mirroring](https://developer.android.com/static/images/jb-rtl.png)

Developers can now**mirror their layouts**for RTL languages.

Android 4.2 introduces**full native support for RTL**(right-to-left) layouts, including layout mirroring. With native RTL support, you can deliver the same great app experience to all of your users, whether their language uses a script that reads right-to-left or one that reads left-to-right.

When the user switches the system language to a right-to-left script, the system now provides automatic mirroring of app UI layouts and all view widgets, in addition to bidi mirroring of text elements for both reading and character input.

Your app can take advantage of**RTL layout mirroring**in your app with minimal effort. If you want the app to be mirrored, you simply declare a new attribute in your app manifest and change all "left/right" layout properties to new "start/end" equivalents. The system then handles the mirroring and display of your UI as appropriate.

For precise control over your app UI, Android 4.2 includes new APIs that let you manage layout direction, text direction, text alignment, gravity, and locale direction in View components. You can even create custom versions of layout, drawables, and other resources for display when a right-to-left script is in use.

To help you debug and optimize your custom right-to-left layouts, the HierarchyViewer tool now lets you see start/end properties, layout direction, text direction, and text alignment for all the Views in the hierarchy.

## Enhancements for international languages

Android 4.2 includes a variety of**font and character optimizations**for international users:

- For Korean users, a new font choice is available --- Nanum (나눔글꼴) Gothic, a unicode font designed especially for the Korean-language script.
- Improved support for Japanese vertical text displayed in WebViews.
- Improved font kerning and positioning for Indic, Thai, Arabic, and Hebrew default fonts.

The default Android keyboard also includes an updated set of dictionaries:

- Improved dictionaries for French (with bigram support), English, and Russian
- New dictionaries for Danish, Greek, Finnish, Lithuanian, Latvian, Polish, Slovenian, Serbian, Swedish, Turkish

## New ways to create beautiful UI

### Nested Fragments

For more control over your UI components and to make them more modular, Android 4.2 lets you**nest Fragments inside of Fragments**. For any Fragment, a new Fragment manager lets you insert other Fragments as child nodes in the View hierarchy.

You can use nested Fragments in a variety of ways, but they are especially useful for implementing dynamic and reusable UI components inside of a UI component that is itself dynamic and reusable. For example, if you use ViewPager to create fragments that swipe left and right, you can now insert fragments into each Fragment of the view pager.

To let you take advantage of nested Fragments more broadly in your app, this capability is added to the latest version of the**Android Support Library**.

## Accessibility

The system now helps accessibility services**distinguish between touch exploration and accessibility gestures**while in touch-exploration mode. When a user touches the screen, the system notifies the service that a generic touch interaction has started. It then tracks the speed of the touch interaction and determines whether it is a touch exploration (slow) or accessibility gesture (fast) and notifies the service. When the touch interaction ends, the system notifies the service.

The system provides a new global accessibility option that lets an accessibility service open the Quick Settings menu based on an action by the user. Also added in Android 4.2 is a new accessibility feedback type for**Braille devices**.

To give accessibility services insight into the meaning of Views for accessibility purposes, the framework provides new APIs for associating a View as the label for another View. The label for each View is available to accessibility services through AccessibilityNodeInfo.

## Improved Camera with HDR

Android 4.2 introduces a**new camera hardware interface and pipeline** for improved performance. On supported devices, apps can use a new**HDR camera scene mode**to capture an image using high dynamic range imaging techniques.

Additionally, the framework now provides an API to let apps check whether the camera shutter sound can be disabled. Apps can then let the user disable the sound or choose an alternative sound in place of the standard shutter sound, which is recommended.

## Renderscript Computation

In Android 4.2, Renderscript Compute introduces new scripting features, new optimizations, and direct GPU integration for the highest performance in computation operations.

### Filterscript

Filterscript is a subset of Renderscript that is focused on**optimized image processing across a broad range of device chipsets**. Developers can write their image processing operations in Filterscript using the standard Renderscript runtime API, but within stricter constraints that ensure wider compatibility and improved optimization across CPUs, GPUs, and DSPs.

Filterscript is ideal for hardware-accelerating simple image-processing and computation operations such as those that might be written for OpenGL ES fragment shaders. Because it places a relaxed set of constraints on hardware, your operations are optimized and accelerated on more types of device chipsets. Any app targeting API level 17 or higher can make use of Filterscript.

### Script intrinsics

In Android 4.2, Renderscript adds support for a set of script intrinsics --- pre-implemented**filtering primitives that are accelerated**to reduce the amount of code that you need to write and to ensure that your app gets the maximum performance gain possible.

Intrinsics are available for blends, blur, color matrix, 3x3 and 5x5 convolve, per-channel lookup table, and converting an Android YUV buffer to RGB.

### Script groups

You can now create**groups of Renderscript scripts**and execute them all with a single call as though they were part of a single script. This allows Renderscript to optimize execution of the scripts in ways that it could not do if the scripts were executed individually.  
![Renderscipt optimizations chart](https://developer.android.com/static/images/jb-rs-chart-versions.png)

Renderscript image-processing benchmarks run on different Android platform versions (Android 4.0, 4.1, and 4.2) in CPU only on a Galaxy Nexus device.
![](https://developer.android.com/static/images/jb-rs-chart-gpu.png)

Renderscript image-processing benchmarks comparing operations run with GPU + CPU to those run in CPU only on the same Nexus 10 device.

If you have a directed acyclic graph of Renderscript operations to run, you can use a builder class to create a script group defining the operations. At execution time, Renderscript optimizes the run order and the connections between these operations for best performance.

### Ongoing optimization improvements

When you use Renderscript for computation operations, you apps benefit from**ongoing performance and optimization improvements**in the Renderscript engine itself, without any impact on your app code or any need for recompilation.

As optimization improves, your operations execute faster and on more chipsets, without any work on your part. The chart at right highlights the performance gain delivered by ongoing Renderscript optimization improvements across successive versions of the Android platform.

### GPU Compute

Renderscript Compute is the first computation platform ported to run directly on a mobile device GPU. It now automatically takes advantage of**GPU computation**resources whenever possible to improve performance. With GPU integration, even the most complex computations for graphics or image processing can execute with dramatically improved performance.

Any app using Renderscript on a supported device can benefit immediately from this GPU integration, without recompiling. The Nexus 10 tablet is the first device to support this integration.

## New built-in developer options

The Android 4.2 system includes a variety of new developer options that make it easier to create great looking apps that perform well. The new options expose features for**debugging and profiling**your app from any device or emulator.

On devices running Android 4.2, developer options are hidden by default, helping to create a better experience for users. You can reveal the developer options at any time by tapping 7 times on**Settings** \>**About phone** \>**Build number**on any compatible Android device.  
![](https://developer.android.com/static/images/jb-dev-options-device.png)

Newdeveloper optionsgive you more ways to profile and debug on a device.

New developer options in Android 4.2 include:

- **Take bug report**--- immediately takes a screen shot and dumps device state information to local file storage, then attaches them to a new outgoing email message.
- **Power menu bug reports**--- Adds a new option to the device power menu and quick settings to take a bug report (see above).
- **Verify apps over usb**--- Allows you to disable app checks for sideloading apps over USB, while still checking apps from other sources like the browser. This can speed up the development process while keeping the security feature enabled.
- **Show hardware layers updates**--- Flashes hardware layers green when they update.
- **Show GPU overdraw**--- Highlights GPU overdraw areas.
- **Force 4x MSAA**--- Enables 4x MSAA in Open GL ES 2.0 apps.
- **Simulate secondary displays**--- Creates one or more non-secure overlay windows on the current screen for use as a simulated remote display. You can control the simulated display's size and density.
- **Enable OpenGL traces**--- Lets you trace OpenGL execution using Logcat, Systrace, or callstack on glGetError.

## New Platform Technologies

Android 4.2 includes a variety of new and**enhanced platform technologies**to support innovative communications use-cases across a broad range of hardware devices. In most cases, the new platform technologies and enhancements do not directly affect your apps, so you can benefit from them without any modification.

### Security enhancements

Every Android release includes dozens of security enhancements to protect users. Here are some of the enhancements in Android 4.2:

- **Application verification**--- Users can choose to enable "Verify Apps" and have applications screened by an application verifier, prior to installation. App verification can alert the user if they try to install an app that might be harmful; if an application is especially bad, it can block installation.
- **More control of premium SMS**--- Android will provide a notification if an application attempts to send SMS to a short code that uses premium services which might cause additional charges. The user can choose whether to allow the application to send the message or block it.
- **Always-on VPN**--- VPN can be configured so that applications will not have access to the network until a VPN connection is established. This prevents applications from sending data across other networks.
- **Certificate Pinning**--- The libcore SSL implementation now supports certificate pinning. Pinned domains will receive a certificate validation failure if the certificate does not chain to a set of expected certificates. This protects against possible compromise of Certificate Authorities.
- **Improved display of Android permissions**--- Permissions have been organized into groups that are more easily understood by users. During review of the permissions, the user can click on the permission to see more detailed information about the permission.
- **installd hardening**--- The installd daemon does not run as the root user, reducing potential attack surface for root privilege escalation.
- **init script hardening**--- init scripts now apply O_NOFOLLOW semantics to prevent symlink related attacks.
- **FORTIFY_SOURCE**--- Android now implements FORTIFY_SOURCE. This is used by system libraries and applications to prevent memory corruption.
- **ContentProvider default configuration**--- Applications which target API level 17 will have "export" set to "false" by default for each ContentProvider, reducing default attack surface for applications.
- **Cryptography**--- Modified the default implementations of SecureRandom and Cipher.RSA to use OpenSSL. Added SSLSocket support for TLSv1.1 and TLSv1.2 using OpenSSL 1.0.1
- **Security Fixes**--- Upgraded open source libraries with security fixes include WebKit, libpng, OpenSSL, and LibXML. Android 4.2 also includes fixes for Android-specific vulnerabilities. Information about these vulnerabilities has been provided to Open Handset Alliance members and fixes are available in Android Open Source Project. To improve security, some devices with earlier versions of Android may also include these fixes.

### New Bluetooth stack

Android 4.2 introduces a new Bluetooth stack optimized for use with Android devices. The new Bluetooth stack developed in collaboration between Google and Broadcom replaces the stack based on BlueZ and provides improved compatibility and reliability.

### Low-latency audio

Android 4.2 improves support for low-latency audio playback, starting from the improvements made in Android 4.1 release for audio output latency using OpenSL ES, Soundpool and tone generator APIs. These improvements depend on hardware support --- devices that offer these low-latency audio features can advertise their support to apps through a hardware feature constant. New AudioManager APIs are provided to query the native audio sample rate and buffer size, for use on devices which claim this feature.

### New camera hardware interface

Android 4.2 introduces a new implementation of the camera stack. The camera subsystem includes the implementations for components in the camera pipeline such as burst mode capture with processing controls.

### New NFC hardware interface and controller interface

Android 4.2 introduces support for controllers based on the NCI standard from the NFC-Forum. NCI provides a standard communication protocol between an NFC Controller (NFCC) and a device Host, and the new NFC stack developed in collaboration between Google and Broadcom supports it.

### Dalvik runtime optimizations

The Dalvik runtime includes enhancements for performance and security across a wider range of architectures:

- x86 JIT support from Intel and MIPS JIT support from MIPS
- Optimized garbage-collection parameters for devices with \> 512MB
- Default implementations of SecureRandom and Cipher.RSA now use OpenSSL
- SSLSocket support for TLSv1.1 and TLSv1.2 via OpenSSL 1.0.1
- New intrinsic support for StrictMath methods abs, min, max, and sqrt
- BouncyCastle updated to 1.47
- zlib updated to 1.27
- dlmalloc updated to 2.8.6

### Android 4.1

![](https://developer.android.com/static/images/jb-android-4.1.png)

Welcome to Android 4.1 the first version of Jelly Bean!

Android 4.1 is the fastest and smoothest version of Android yet. We've made improvements throughout the platform and added great new features for users and developers. This document provides a glimpse of what's new for developers.

See the[Android 4.1 APIs](https://developer.android.com/about/versions/android-4.1)document for a detailed look at the new developer APIs.

Find out more about the Jelly Bean features for users at[www.android.com](https://www.android.com/whatsnew).

## Faster, Smoother, More Responsive

Android 4.1 is optimized to deliver Android's best performance and lowest touch latency, in an effortless, intuitive UI.

To ensure a consistent framerate, Android 4.1 extends**vsync timing**across all drawing and animation done by the Android framework. Everything runs in lockstep against a 16 millisecond vsync heartbeat --- application rendering, touch events, screen composition, and display refresh --- so frames don't get ahead or behind.

Android 4.1 also adds**triple buffering**in the graphics pipeline, for more consistent rendering that makes everything feel smoother, from scrolling to paging and animations.

Android 4.1 reduces touch latency not only by**synchronizing touch** to vsync timing, but also by actually**anticipating** where your finger will be at the time of the screen refresh. This results in a more reactive and uniform touch response. In addition, after periods of inactivity, Android applies a**CPU input boost**at the next touch event, to make sure there's no latency.

**Tooling** can help you get the absolute best performance out of your apps. Android 4.1 is designed to work with a new tool called**systrace** , which collects data directly from the Linux kernel to produce an overall picture of system activities. The data is represented as a group of vertically stacked time series graphs, to help isolate rendering interruptions and other issues. The tool is available now in the[Android SDK](https://developer.android.com/tools)(Tools R20 or higher)  
![](https://developer.android.com/static/images/jb-accessibility-focus-250.png)  

## Enhanced Accessibility

New APIs for accessibility services let you handle gestures and manage**accessibility focus**as the user moves through the on-screen elements and navigation buttons using accessibility gestures, accessories, and other input. The Talkback system and explore-by-touch are redesigned to use accessibility focus for easier use and offer a complete set of APIs for developers.

Accessibility services can link their own**tutorials**into the Accessibility settings, to help users configure and use their services.

Apps that use standard View components**inherit support**for the new accessibility features automatically, without any changes in their code. Apps that use custom Views can use new accessibility node APIs to indicate the parts of the View that are of interest to accessibility services.  

## Support for International Users

![](https://developer.android.com/static/images/jb-r2l.png)

### Bi-Directional Text and Other Language Support

Android 4.1 helps you to reach more users through support for**bi-directional text**in TextView and EditText elements. Apps can display text or handle text editing in left-to-right or right-to-left scripts. Apps can make use of new Arabic and Hebrew locales and associated fonts.

Other types of new language support include:

- Additional Indic languages: Kannada, Telugu, and Malayalam
- The new Emoji characters from Unicode version 6.0
- Better glyph support for Japanese users (renders Japanese-specific versions of glyphs when system language is set to Japanese)
- Arabic glyphs optimized for WebViews in addition to the Arabic glyphs for TextViews
- Vertical Text support in WebViews, including Ruby Text and additional Vertical Text glyphs
- Synthetic Bold is now available for all fonts that don't have dedicated bold glyphs

### User-installable keymaps

The platform now supports**user-installable keyboard maps**, such as for additional international keyboards and special layout types. By default, Android 4.1 includes 27 international keymaps for keyboards, including Dvorak. When users connect a keyboard, they can go to the Settings app and select one or more keymaps that they want to use for that keyboard. When typing, users can switch between keymaps using a shortcut (ctrl-space).

You can create an app to**publish additional keymaps**to the system. The APK would include the keyboard layout resources in it, based on standard Android keymap format. The application can offer additional keyboard layouts to the user by declaring a suitable broadcast receiver for ACTION_QUERY_KEYBOARD_LAYOUTS in its manifest.

## New Ways to Create Beautiful UI

![](https://developer.android.com/static/images/jb-notif-ex1.png)

Developers can create custom notification styles like those shown in the examples above to display rich content and actions.

### Expandable notifications

Notifications have long been a unique and popular feature on Android. Developers can use them to place important or time-based information in front of users in the notification bar, outside of the app's normal UI.

Android 4.1 brings a major update to the Android notifications framework. Apps can now display**larger, richer notifications** to users that can be expanded and collapsed with a pinch or swipe. Notifications support**new types of content**, including photos, have configurable priority, and can even include multiple actions.

Through an improved**notification builder** , apps can create notifications that use a larger area, up to 256 dp in height. Three**templated notification styles**are available:

- BigTextStyle --- a notification that includes a multiline TextView object.
- BigInboxStyle --- a notification that shows any kind of list such as messages, headlines, and so on.
- BigPictureStyle --- a notification that showcases visual content such as a bitmap.

In addition to the templated styles, you can create your own notification styles**using any remote View**.

Apps can add up to three**actions**to a notification, which are displayed below the notification content. The actions let the users respond directly to the information in the notification in alternative ways. such as by email or by phone call, without visiting the app.

With expandable notifications, apps can give more information to the user, effortlessly and on demand. Users remain in control and can long-press any notification to get information about the sender and optionally disable further notifications from the app.  
![](https://developer.android.com/static/images/jb-appwidgets.png)

App Widgetscan resize automatically to fit the home screen and load different content as their sizes change.  

### Resizable app widgets

Android 4.1 introduces improved App Widgets that can**automatically resize** , based on where the user drops them on the home screen, the size to which the user expands them, and the amount of room available on the home screen. New App Widget APIs let you take advantage of this to**optimize your app widget content**as the size of widgets changes.

When a widget changes size, the system notifies the host app's widget provider, which can reload the content in the widget as needed. For example, a widget could display larger, richer graphics or additional functionality or options. Developers can still maintain control over maximum and minimum sizes and can update other widget options whenever needed.

You can also supply separate landscape and portrait layouts for your widgets, which the system inflates as appropriate when the screen orientation changes.

App widgets can now be displayed in third party launchers and other host apps through a new bind Intent (AppWidgetManager.ACTION_APPWIDGET_BIND).

### Simplified task navigation

Android 4.1 makes it easy for you to manage the "Up" navigation that's available to users from inside of your apps and helps ensure a consistent experience for users.

You can**define the intended Up navigation** for individual Activity components of your UI by adding a new**XML attribute**in the app's manifest file. At run time, as Activities are launched, the system extracts the Up navigation tree from the manifest file and automatically creates the Up affordance navigation in the action bar. Developers who declare Up navigation in the manifest no longer need to manage navigation by callback at run time, although they can also do so if needed.

Also available is a new**TaskStackBuilder**class that lets you quickly put together a synthetic task stack to start immediately or to use when an Activity is launched from a PendingIntent. Creating a synthetic task stack is especially useful when users launch Activities from remote views, such as from Home screen widgets and notifications, because it lets the developer provide a managed, consistent experience on Back navigation.

### Easy animations for Activity launch

You can use a new helper class,**ActivityOptions**, to create and control the animation displayed when you launch your Activities. Through the helper class, you can specify custom animation resources to be used when the activity is launched, or request new zoom animations that start from any rectangle you specify on screen and that optionally include a thumbnail bitmap.

### Transitions to Lights Out and Full Screen Modes

New system UI flags in View let you to cleanly transition from a normal application UI (with action bar, navigation bar, and system bar visible), to "lights out mode" (with status bar and action bar hidden and navigation bar dimmed) or "full screen mode" (with status bar, action bar, and navigation bar all hidden).

### New types of remoteable Views

Developers can now use**GridLayout** and**ViewStub**views in Home screen widgets and notifications. GridLayout lets you structure the content of your remote views and manage child views alignments with a shallower UI hierarchy. ViewStub is an invisible, zero-sized View that can be used to lazily inflate layout resources at runtime.

### Live wallpaper preview

Android 4.1 makes it easier for users to**find and install Live Wallpapers**from apps that include them. If your app includes Live Wallpapers, you can now start an Activity (ACTION_CHANGE_LIVE_WALLPAPER) that shows the user a preview of the Live Wallpaper from your own app. From the preview, users can directly load the Live Wallpaper.

### Higher-resolution contact photos

With Android 4.1, you can store**contact photos** that are as large as**720 x 720** , making contacts even richer and more personal. Apps can store and retrieve contact photos at that size or use any other size needed. The maximum photo size supported on specific devices may vary, so apps should**query the built-in contacts provider**at run time to obtain the max size for the current device.

## New Input Types and Capabilities

### Find out about devices being added and removed

Apps can**register to be notified**when any new input devices are attached, by USB, Bluetooth, or any other connection type. They can use this information to change state or capabilities as needed. For example, a game could receive notification that a new keyboard or joystick is attached, indicating the presence of a new player.

### Query the capabilities of input devices

Android 4.1 includes APIs that let apps and games take full advantage of all input devices that are connected and available.

Apps can query the device manager to enumerate all of the input devices currently attached and learn about the capabilities of each.

### Control vibrator on input devices

Among other capabilities, apps can now make use of any**vibrator service** associated with an attached input device, such as for**Rumble Pak**controllers.

## Animation and Graphics

### Vsync for apps

Extending vsync across the Android framework leads to a more consistent framerate and a smooth, steady UI. So that apps also benefit, Android 4.1**extends vsync timing**to all drawing and animations initiated by apps. This lets them optimize operations on the UI thread and provides a stable timebase for synchronization.

Apps can take advantage of vsync timing for free, through Android's**animation framework**. The animation framework now uses vsync timing to automatically handle synchronization across animators.

For specialized uses, apps can access vsync timing through APIs exposed by a new Choreographer class. Apps can request invalidation on the next vsync frame --- a good way to schedule animation when the app is not using the animation framework. For more advanced uses, apps can post a callback that the Choreographer class will run on the next frame.

### New animation actions and transition types

The animation framework now lets you define start and end actions to take when running ViewPropertyAnimator animations, to help synchronize them with other animations or actions in the application. The action can run any runnable object. For example, the runnable might specify another animation to start when the previous one finishes.

You can also now specify that a ViewPropertyAnimator use a layer during the course of its animation. Previously, it was a best practice to animate complicated views by setting up a layer prior to starting an animation and then handling an onAnimationEnd() event to remove the layer when the animation finishes. Now, the withLayer() method on ViewPropertyAnimator simplifies this process with a single method call.

A new transition type in LayoutTransition enables you to automate animations in response to all layout changes in a ViewGroup.

## New Types of Connectivity

### Android Beam

Android Beam is a popular NFC-based technology that lets users instantly share, just by touching two NFC-enabled phones together.

In Android 4.1, Android Beam makes it easier to share images, videos, or other payloads by**leveraging Bluetooth for the data transfer**. When the user triggers a transfer, Android Beam hands over from NFC to Bluetooth, making it really easy to manage the transfer of a file from one device to another.

### Wi-Fi Network Service Discovery

Android 4.1 introduces support for multicast**DNS-based service discovery**, which lets applications find and connect to services offered by peer devices over Wi-Fi networks --- including mobile devices, printers, cameras, media players, and others. Developers can take advantage of Wi-Fi network service discovery to build cross-platform or multiplayer games and application experiences.

Using the service discovery API, apps can create and register any kind of service, for any other NSD-enabled device to discover. The service is advertised by multicast across the network using a human-readable string identifier, which lets user more easily identify the type of service.

Consumer devices can use the API to scan and discover services available from devices connected to the local Wi-Fi network. After discovery, apps can use the API to resolve the service to an IP address and port through which it can establish a socket connection.

You can take advantage of this API to build new features into your apps. For example, you could let users connect to a webcam, a printer, or an app on another mobile device that supports Wi-Fi peer-to-peer connections.

### Wi-Fi P2P Service Discovery

[Ice Cream Sandwich](https://developer.android.com/about/versions/android-4.0-highlights)introduced support for Wi-Fi Peer-to-Peer (P2P), a technology that lets apps**discover and pair directly** , over a high-bandwidth peer-to-peer connection (in compliance with the Wi-Fi Alliance's[Wi-Fi Direct™](http://www.wi-fi.org/discover-and-learn/wi-fi-direct)certification program). Wi-Fi P2P is an ideal way to share media, photos, files and other types of data and sessions, even where there is no cell network or Wi-Fi available.

Android 4.1 takes Wi-Fi P2P further, adding API support for**pre-associated service discovery**. Pre-associated service discovery lets your apps get more useful information from nearby devices about the services they support, before they attempt to connect. Apps can initiate discovery for a specific service and filter the list of discovered devices to those that actually support the target service or application.

For example, this means that your app could discover only devices that are "printers" or that have a specific game available, instead of discovering all nearby Wi-Fi P2P devices. On the other hand, your app can advertise the service it provides to other devices, which can discover it and then negotiate a connection. This greatly simplifies discovery and pairing for users and lets apps take advantage of Wi-Fi P2P more effectively.

With Wi-Fi P2P service discovery, you can create apps and**multiplayer games**that can share photos, videos, gameplay, scores, or almost anything else --- all without requiring any Internet or mobile network. Your users can connect using only a direct p2p connection, which avoids using mobile bandwidth.

### Network Bandwidth Management

Android 4.1 helps apps**manage data usage** appropriately when the device is**connected to a metered network**, including tethering to a mobile hotspot. Apps can query whether the current network is metered before beginning a large download that might otherwise be relatively expensive to the user. Through the API, you can now get a clear picture of which networks are sensitive to data usage and manage your network activity accordingly.

## New Media Capabilities

### Media codec access

Android 4.1 provides low-level access to platform hardware and software codecs. Apps can query the system to discover what**low-level media codecs**are available on the device and then and use them in the ways they need. For example, you can now create multiple instances of a media codec, queue input buffers, and receive output buffers in return. In addition, the media codec framework supports protected content. Apps can query for an available codec that is able to play protected content with a DRM solution available on the device.

### USB Audio

USB audio output support allows hardware vendors to build hardware such as**audio docks** that interface with Android devices. This functionality is also exposed with the Android**Open Accessory Development Kit**(ADK) to give all developers the chance to create their own hardware.

### Audio record triggering

Android now lets you**trigger audio recording**based on the completion of an audio playback track. This is useful for situations such as playing back a tone to cue your users to begin speaking to record their voices. This feature helps you sync up recording so you don't record audio that is currently being played back and prevents recordings from beginning too late.

### Multichannel audio

Android 4.1 supports**multichannel audio** on devices that have hardware multichannel audio out through the**HDMI port**. Multichannel audio lets you deliver rich media experiences to users for applications such as games, music apps, and video players. For devices that do not have the supported hardware, Android automatically downmixes the audio to the number of channels that are supported by the device (usually stereo).

Android 4.1 also adds built-in support for encoding/decoding AAC 5.1 audio.

### Audio preprocessing

Developers can apply**preprocessing effects**to audio being recorded, such as to apply noise suppression for improving speech recording quality, echo cancellation for acoustic echo, and auto gain control for audio with inconsistent volume levels. Apps that require high quality and clean audio recording will benefit from these preprocessors.

### Audio chaining

MediaPlayer supports**chaining audio streams together**to play audio files without pauses. This is useful for apps that require seamless transitions between audio files such as music players to play albums with continuous tracks or games.

### Media Router

The new APIs MediaRouter, MediaRouteActionProvider, and MediaRouteButton provide standard mechanisms and UI for**choosing where to play media**. Support is built-in for wired headsets and a2dp bluetooth headsets and speakers, and you can add your own routing options within your own app.

## Renderscript Computation

Android 4.1 extends Renderscript computation to give you more flexibility. You can now**sample textures** in your Renderscript compute scripts, and**new pragmas** are available to define the floating point precision required by your scripts. This lets you enable**NEON instructions**such as fast vector math operations on the CPU path, that wouldn't otherwise be possible with the full IEEE 754-2008 standard.

You can now**debug** your Renderscript compute scripts on**x86-based emulator and hardware devices**. You can also define multiple root-style kernels in a single Renderscript source file.

## Android Browser and WebView

In Android 4.1, the Android Browser and WebViews include these enhancements:

- Better HTML5 video user experience, including touch-to-play/pause and smooth transition from inline to full screen mode.
- Improved rendering speed and reduced memory usage for better scrolling and zooming performance.
- Improved HTML5/CSS3/Canvas animation performance.
- Improved text input.
- Updated JavaScript Engine (V8) for better JavaScript performance.
- Support for the updated HTML5 Media Capture specification (the "capture" attribute on input type=file elements).

## Google APIs and services

To extend the capabilities of Android even further, several new services for Android are available.

### Google Cloud Messaging for Android

Google Cloud Messaging (GCM) is a service that lets developers send**short message data**to their users on Android devices, without needing a proprietary sync solution.

GCM handles all the details of**queuing messages and delivering them** efficiently to the targeted Android devices. It supports message**multicasting** and can reach up to 1000 connected devices simultaneously with a single request. It also supports message**payloads**, which means that in addition to sending tickle messages to an app on the device, developers can send up to 4K of data.

Google Cloud Messaging is completely**free for all developers** and sign-up is easy. See the[Google Cloud Messaging](https://developer.android.com/google/gcm)page for registration, downloads, and documentation.

### App Encryption

Starting with Android 4.1, Google Play will help protect application assets by encrypting all paid apps with a device-specific key before they are delivered and stored on a device.

### Smart App Updates

Smart app updates is a new feature of Google Play that introduces a better way of delivering**app updates** to devices. When developers publish an update, Google Play now delivers only the**bits that have changed** to devices, rather than the entire APK. This makes the updates much lighter-weight in most cases, so they are faster to download, save the device's battery, and conserve bandwidth usage on users' mobile data plan. On average, a smart app update is about**1/3 the size**of a full APK update.

### Google Play services

Google Play services helps developers to**integrate Google services**, such as authentication, into their apps delivered through Google Play.

Google Play services is automatically provisioned to end user devices by Google Play, so all you need is a**thin client library**in your apps.

Because your app only contains the small client library, you can take advantage of these services without a big increase in download size and storage footprint. Also, Google Play will**deliver regular updates**to the services, without developers needing to publish app updates to take advantage of them.

For more information about the APIs included in Google Play Services, see the[Google Play services](http://developers.google.com/android/google-play-services/index.html)developer page.