---
title: https://developer.android.com/games/engines/cocos/cocos-overview
url: https://developer.android.com/games/engines/cocos/cocos-overview
source: md.txt
---

# About Cocos Creator

[Cocos Creator](https://www.cocos.com)is a cross-platform game engine used by many developers all over the world. It helps you create 2D and 3D games and applications with great efficiency.

![Cocos creator UI](https://developer.android.com/static/images/games/engines/cocos/cyberpunk.jpg)

## Steps to build a game for Android in Cocos Creator

To use Cocos Creator to build your game for Android platform, follow these steps:

1. [Download](https://www.cocos.com/en/creator/download)and[install](https://docs.cocos.com/creator/manual/en/getting-started/install/)the**Cocos Dashboard**.

2. Launch the**Cocos Dashboard** . Go to the**Editor** tab and click**Download** to add a version of the Cocos Creator. We highly recommend that you use the latest version if possible.![cocos creator dashboard editor](https://developer.android.com/static/images/games/engines/cocos/dashboard-editor.png)

3. Go to the**Project** tab and click**New** to create a new Cocos Creator project.![cocos creator dashboard project](https://developer.android.com/static/images/games/engines/cocos/dashboard-project.png)

4. Choose an editor version, input your project name, select a location to store, and then click**Create** .![cocos creator dashboard project create](https://developer.android.com/static/images/games/engines/cocos/dashboard-project-create.png)

5. You are good to go for creating your game!

6. [Export your game to Android](https://docs.cocos.com/creator/manual/en/editor/publish/native-options.html#build-for-android)using the**Project \> Build** panel.![cocos creator build panel](https://developer.android.com/static/images/games/engines/cocos/build-panel.png)

7. Compile and Generate the Android application in Android Studio.

## Notable features

### Google Play Instant

With[Google Play Instant](https://developer.android.com/topic/google-play-instant), people can use an app or game without installing it first. Increase engagement with your Android app or gain more installs by surfacing your instant app across the Play Store and Google Play Games app. To see how it works in Cocos Creator, refer to[Publish your game as Google Play Instant app in Cocos Creator](https://developer.android.com/games/engines/cocos/cocos-playinstant).

### Android App Bundle (AAB)

An Android App Bundle (or AAB) is a publishing format that includes all your app's compiled code and resources, and defers APK generation and signing to Google Play. For more details, refer to[Publish your game with Android App Bundle in Cocos Creator](https://developer.android.com/games/engines/cocos/cocos-aab).

### Swappy

The Android Frame Pacing library, also known as Swappy, is part of the[Android Game SDK](https://android.googlesource.com/platform/frameworks/opt/gamesdk/). It helps[OpenGL](https://source.android.com/docs/core/graphics/arch-egl-opengl)and[Vulkan](https://source.android.com/docs/core/graphics/arch-vulkan)games achieve smooth rendering and correct frame pacing on Android.

Developers can easily activate Swappy in Cocos Creator by selecting the "Enable Swappy" checkbox on the build panel.

For more information, refer to the Google document[Frame Pacing Library Overview](https://source.android.com/docs/core/graphics/frame-pacing).

### Vulkan

[Vulkan](https://source.android.com/docs/core/graphics/arch-vulkan), a low-overhead, cross-platform API for high-performance 3D graphics, is supported in Cocos Creator as one of the graphics API backends. Developers can select Vulkan as the graphics API for Android from the build panel in Cocos Creator.