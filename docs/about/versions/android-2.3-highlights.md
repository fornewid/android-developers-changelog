---
title: https://developer.android.com/about/versions/android-2.3-highlights
url: https://developer.android.com/about/versions/android-2.3-highlights
source: md.txt
---

# Gingerbread

The Android 2.3 platform introduces many new and exciting features for users and developers. This document provides a glimpse at some of the new features and technologies in Android 2.3. For detailed information about the new developer APIs, see the[Android 2.3 version notes](https://developer.android.com/about/versions/android-2.3).

- [New User Features](https://developer.android.com/about/versions/android-2.3-highlights#UserFeatures)
- [New Developer Features](https://developer.android.com/about/versions/android-2.3-highlights#DeveloperApis)
- [New Platform Technologies](https://developer.android.com/about/versions/android-2.3-highlights#PlatformTechnologies)

## New User Features

![](https://developer.android.com/static/sdk/images/2.3/home-menu.png)![](https://developer.android.com/static/sdk/images/2.3/home-plain.png)

### UI refinements for simplicity and speed

The user interface is refined in many ways across the system, making it easier to learn, faster to use, and more power-efficient. A simplified visual theme of colors against black brings vividness and contrast to the notification bar, menus, and other parts of the UI. Changes in menus and settings make it easier for the user to navigate and control the features of the system and device.

### Faster, more intuitive text input

The Android soft keyboard is redesigned and optimized for faster text input and editing. The keys themselves are reshaped and repositioned for improved targeting, making them easier to see and press accurately, even at high speeds. The keyboard also displays the current character and dictionary suggestions in a larger, more vivid style that is easier to read.

The keyboard adds the capability to correct entered words from suggestions in the dictionary. As the user selects a word already entered, the keyboard displays suggestions that the user can choose from, to replace the selection. The user can also switch to voice input mode to replace the selection. Smart suggestions let the user accept a suggestion and then return to correct it later, if needed, from the original set of suggestions.

New multitouch key-chording lets the user quickly enter numbers and symbols by pressing Shift+\<*letter* \> and ?123+\<*symbol*\>, without needing to manually switch input modes. From certain keys, users can also access a popup menu of accented characters, numbers, and symbols by holding the key and sliding to select a character.  
![](https://developer.android.com/static/sdk/images/2.3/onetouch.png)  
![](https://developer.android.com/static/sdk/images/2.3/selection.png)

### One-touch word selection and copy/paste

When entering text or viewing a web page, the user can quickly select a word by press-hold, then copy to the clipboard and paste. Pressing on a word enters a free-selection mode --- the user can adjust the selection area as needed by dragging a set of bounding arrows to new positions, then copy the bounded area by pressing anywhere in the selection area. For text entry, the user can slide-press to enter a cursor mode, then reposition the cursor easily and accurately by dragging the cursor arrow. With both the selection and cursor modes, no use of a trackball is needed.  
:running:  
![](https://developer.android.com/static/sdk/images/2.3/power.png)

### Improved power management

The Android system takes a more active role in managing apps that are keeping the device awake for too long or that are consuming CPU while running in the background. By managing such apps --- closing them if appropriate --- the system helps ensure best possible performance and maximum battery life.

The system also gives the user more visibility over the power being consumed by system components and running apps. The Application settings provides an accurate overview of how the battery is being used, with details of the usage and relative power consumed by each component or application.

### Control over applications

A shortcut to the Manage Applications control now appears in the Options Menu in the Home screen and Launcher, making it much easier to check and manage application activity. Once the user enters Manage Applications, a new Running tab displays a list of active applications and the storage and memory being used by each. The user can read further details about each application and if necessary stop an application or report feedback to its developer.

### New ways of communicating, organizing

An updated set of standard applications lets the user take new approaches to managing information and relationships.  
![](https://developer.android.com/static/sdk/images/2.3/sipcall.png)  
![](https://developer.android.com/static/sdk/images/2.3/ffc.png)  

**Internet calling**

The user can make voice calls over the internet to other users who have SIP accounts. The user can add an internet calling number (a SIP address) to any Contact and can initiate a call from Quick Contact or Dialer. To use internet calling, the user must create an account at the SIP provider of their choice --- SIP accounts are not provided as part of the internet calling feature. Additionally, support for the platform's SIP and internet calling features on specific devices is determined by their manufacturers and associated carriers.  
![](https://developer.android.com/static/sdk/images/2.3/nfc.png)

**Near-field communications**

An NFC Reader application lets the user read and interact with near-field communication (NFC) tags. For example, the user can "touch" or "swipe" an NFC tag that might be embedded in a poster, sticker, or advertisement, then act on the data read from the tag. A typical use would be to read a tag at a restaurant, store, or event and then rate or register by jumping to a web site whose URL is included in the tag data. NFC communication relies on wireless technology in the device hardware, so support for the platform's NFC features on specific devices is determined by their manufacturers.

**Downloads management**

The Downloads application gives the user easy access to any file downloaded from the browser, email, or another application. Downloads is built on a completely new download manager facility in the system that any other applications can use, to more easily manage and store their downloads.

**Camera**

The application now lets the user access multiple cameras on the device, including a front-facing camera, if available.

## New Developer Features

Android 2.3 delivers a variety of features and APIs that let developers bring new types of applications to the Android platform.

- [Enhancements for gaming](https://developer.android.com/about/versions/android-2.3-highlights#gaming)
- [New forms of communication](https://developer.android.com/about/versions/android-2.3-highlights#communication)
- [Rich multimedia](https://developer.android.com/about/versions/android-2.3-highlights#multimedia)

### Enhancements for gaming

**Performance**

Android 2.3 includes a variety of improvements across the system that make common operations faster and more efficient for all applications. Of particular interest to game developers are:

- Concurrent garbage collector --- The Dalvik VM introduces a new, concurrent garbage collector that minimizes application pauses, helping to ensure smoother animation and increased responsiveness in games and similar applications.
- Faster event distribution --- The plaform now handles touch and keyboard events faster and more efficiently, minimizing CPU utilization during event distribution. The changes improve responsiveness for all applications, but especially benefit games that use touch events in combination with 3D graphics or other CPU-intensive operations.
- Updated video drivers --- The platform uses updated third-party video drivers that improve the efficiency of OpenGL ES operations, for faster overall 3D graphics performance.

**Native input and sensor events**

Applications that use native code can now receive and process input and sensor events directly in their native code, which dramatically improves efficiency and responsiveness.

Native libraries exposed by the platform let applications handle the same types of input events as those available through the framework. Applications can receive events from all supported sensor types and can enable/disable specific sensors and manage event delivery rate and queueing.

**Gyroscope and other new sensors, for improved 3D motion processing**

Android 2.3 adds API support for several new sensor types, including gyroscope, rotation vector, linear acceleration, gravity, and barometer sensors. Applications can use the new sensors in combination with any other sensors available on the device, to track three-dimensional device motion and orientation change with high precision and accuracy. For example, a game application could use readings from a gyroscope and accelerometer on the device to recognize complex user gestures and motions, such as tilt, spin, thrust, and slice.

**Open API for native audio**

The platform provides a software implementation of[Khronos OpenSL ES](http://www.khronos.org/opensles/), a standard API that gives applications access to powerful audio controls and effects from native code. Applications can use the API to manage audio devices and control audio input, output, and processing directly from native code.

**Native graphics management**

The platform provides an interface to its[Khronos EGL](http://www.khronos.org/egl/)library, which lets applications manage graphics contexts and create and manage OpenGL ES textures and surfaces from native code.

**Native access to Activity lifecycle, window management**

Native applications can declare a new type of Activity class,`NativeActivity`whose lifecycle callbacks are implemented directly in native code. The`NativeActivity`and its underlying native code run in the system just as do other Activities --- they run in the application's system process and execute on the application's main UI thread, and they receive the same lifecycle callbacks as do other Activities.

The platform also exposes native APIs for managing windows, including the ability to lock/unlock the pixel buffer to draw directly into it. Through the API, applications can obtain a native window object associated with a framework Surface object and interact with it directly in native code.

**Native access to assets, storage**

Applications can now access a native Asset Manager API to retrieve application assets directly from native code without needing to go through JNI. If the assets are compressed, the platform does streaming decompression as the application reads the asset data. There is no longer a limit on the size of compressed`.apk`assets that can be read.

Additionally, applications can access a native Storage Manager API to work directly with OBB files downloaded and managed by the system. Note that although platform support for OBB is available in Android 2.3, development tools for creating and managing OBB files will not be available until early 2011.

**Robust native development environment**

The Android NDK (r5 or higher) provides a complete set of tools, toolchains, and libraries for developing applications that use the rich native environment offered by the Android 2.3 platform. For more information or to download the NDK, please see the[Android NDK](https://developer.android.com/sdk/ndk/index.html)page.

### New forms of communication

**Internet telephony**

Developers can now add SIP-based internet telephony features to their applications. Android 2.3 includes a full SIP protocol stack and integrated call management services that let applications easily set up outgoing and incoming voice calls, without having to manage sessions, transport-level communication, or audio record or playback directly.

Support for the platform's SIP and internet calling features on specific devices is determined by their manufacturers and associated carriers.

**Near Field Communications (NFC)**

The platform's support for Near Field Communications (NFC) lets developers get started creating a whole new class of applications for Android. Developers can create new applications that offer proximity-based information and services to users, organizations, merchants, and advertisers.

Using the NFC API, applications can read and respond to NFC tags "discovered" as the user "touches" an NFC-enabled device to elements embedded in stickers, smart posters, and even other devices. When a tag of interest is collected, applications can respond to the tag, read messages from it, and then store the messages, prompting the user as needed.

Starting from Android 2.3.3, applications can also write to tags and set up peer-to-peer connections with other NFC devices.

NFC communication relies on wireless technology in the device hardware, so support for the platform's NFC features on specific devices is determined by their manufacturers.

### Rich multimedia

**Mixable audio effects**

A new audio effects API lets developers easily create rich audio environments by adding equalization, bass boost, headphone virtualization (widened soundstage), and reverb to audio tracks and sounds. Developers can mix multiple audio effects in a local track or apply effects globally, across multiple tracks.

**Support for new media formats**

The platform now offers built-in support for the VP8 open video compression format and the WebM open container format. The platform also adds support for AAC encoding and AMR wideband encoding (in software), so that applications can capture higher quality audio than narrowband.

**Access to multiple cameras**

The Camera API now lets developers access any cameras that are available on a device, including a front-facing camera. Applications can query the platform for the number of cameras on the device and their types and characteristics, then open the camera needed. For example, a video chat application might want to access a front-facing camera that offers lower-resolution, while a photo application might prefer a back-facing camera that offers higher-resolution.

## New Platform Technologies

### Media Framework

- New media framework fully replaces OpenCore, maintaining all previous codec/container support for encoding and decoding.
- Integrated support for the VP8 open video compression format and the WebM open container format
- Adds AAC encoding and AMR wideband encoding

### Linux Kernel

- Upgraded to 2.6.35

### Networking

- SIP stack, configurable by device manufacturer
- Support for Near Field Communications (NFC), configurable by device manufacturer
- Updated BlueZ stack

### Dalvik runtime

- Dalvik VM:
  - Concurrent garbage collector (target sub-3ms pauses)
  - Adds further JIT (code-generation) optimizations
  - Improved code verification
  - StrictMode debugging, for identifying performance and memory issues
- Core libraries:
  - Expanded I18N support (full worldwide encodings, more locales)
  - Faster Formatter and number formatting. For example, float formatting is 2.5x faster.
  - HTTP responses are gzipped by default. XML and JSON API response sizes may be reduced by 60% or more.
  - New collections and utilities APIs
  - Improved network APIs
  - Improved file read and write controls
  - Updated JDBC
- Updates from upstream projects:
  - OpenSSL 1.0.0a
  - BouncyCastle 1.45
  - ICU 4.4
  - zlib 1.2.5

For more information about the new developer APIs, see the[Android 2.3 version notes](https://developer.android.com/about/versions/android-2.3)and the[API Differences Report](https://developer.android.com/sdk/api_diff/9/changes).