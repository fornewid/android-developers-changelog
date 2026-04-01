---
title: https://developer.android.com/games/engines/engines-overview
url: https://developer.android.com/games/engines/engines-overview
source: md.txt
---

# Using a game engine on Android

![Beaker, light-bulb, lightning
bolt](https://developer.android.com/static/images/cluster-illustrations/sample-app-16-9.svg)

As a developer, using a
[game engine](https://en.wikipedia.org/wiki/Game_engine) lets you
concentrate your energy into building your game instead of having to build an
entire technology stack.

## Take advantage of Android development tools

Android development tools can assist your Android game development no matter
which game engine is being used. [Android Studio](https://developer.android.com/games/develop/develop-as)
includes tools you can use to:

- Examine the performance of your game using system, CPU and memory profilers
- Inspect the contents of your game's package or application bundle
- Integrate additional features of the Android SDK and NDK

The [Android GPU Inspector](https://developer.android.com/agi) can characterize the rendering performance of
your game and help you investigate the details of rendered frames using frame
capture.

## Evaluate your engine

When considering a game engine for use on Android, you should evaluate its
compatibility with Google Play requirements and support of desired Android
features. Make sure your game engine supports common requirements as listed
below.

### Google Play requirements

Starting in August 2021, Google Play will require all Android apps to be
submitted as [Android App Bundles](https://developer.android.com/guide/app-bundle#get_started), and to use a
[target API level](https://developer.android.com/distribute/best-practices/develop/target-sdk) of 30 or
higher. Verify that the engine you want to use can meet these requirements.
| **Note:** For apps that target Android 16 (API level 36), the system ignores screen orientation, aspect ratio, and app resizablility restrictions to improve the layout of apps on form factors with smallest width \>= 600dp. See [App
| orientation, aspect ratio, and
| resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).

### In-app purchases

If your game design uses in-app purchases verify that your engine has support
for the [Google Play Billing Library](https://developer.android.com/google/play/billing) (GPBL). Depending on
the engine, GPBL may be directly integrated into the engine, or may be
accessible via an add-on or plugin.

### Google Play Core features

The [Google Play Core Library](https://developer.android.com/guide/playcore) provides a runtime interface to
the Google Play Store. With the Play Core Library, you can:

- Notify the user about app updates
- Download and access data in asset packs
- Request in-app reviews

If you intend to use any of these features, verify the engine supports the
Google Play Core Library, either directly or using an add-on or plugin.

### Application permissions

Some Android features require user consent before they can be used by a game.
The Android [Permissions](https://developer.android.com/guide/topics/permissions/overview) system is used to
request access to these features. If your game requires permissions, make sure
the engine has a method of specifying them in its project options, or allows you
to customize the application manifest to include required permissions.

### Notifications

Android [Notifications](https://developer.android.com/guide/topics/ui/notifiers/notifications) are used to
notify or message the user when they aren't playing your game. If this feature
is important to your game, verify the engine supports sending and processing
notifications.

## Engine resources

The following commercial and open-source game engines have robust support for
Android. For each game engine, we have provided guides on configuring engine
projects for Android to help ensure a polished and engaging user experience when
running on an Android device.

### Defold

Defold is an open-source engine that uses the Lua programming language as its
scripting language. Defold has extensive support for 2D games and graphics, with
built-in support for particles, sprites, tile maps and Spine models. Although
Defold has a 2D focus, it uses a 3D rendering engine and supports rendering 3D
models and meshes, as well as customizing materials and shaders. Physics support
is built-in, with options for 2D or 3D physics. Defold is based around a visual
editor with layout and property tools for game scenes and objects. The Defold
editor includes integrated script editing and debugging features. Native code is
supported in the Defold engine through a plugin system.

#### Guides

- [Install and configure projects for Android](https://developer.android.com/games/engines/defold/defold-configure)
- [Support multiple form factors and screen sizes](https://developer.android.com/games/engines/defold/defold-formfactor)
- [Export to Android](https://developer.android.com/games/engines/defold/defold-export)

### Godot

Godot is an open-source engine suitable for both 2D and 3D games. It supports a
range of capabilities that encompasses everything from 2D sprites and tile maps
to 3D models with physically-based rendering and global illumination. It has a
built in physics system that supports 2D and 3D physics. There are multiple
programming language options for Godot, including the custom GDScript language,
C# 8.0, C++, as well as visual scripting. Godot engine projects are built around
core Scene and Node objects. It includes a visual editor for creation and
editing of these objects. The editor also features integrated editing and
debugging support for the GDScript language.

#### Guides

- [Install and configure projects for Android](https://developer.android.com/games/engines/godot/godot-configure)
- [Godot renderer options](https://developer.android.com/games/engines/godot/godot-renderers)
- [Support multiple form factors and screen sizes](https://developer.android.com/games/engines/godot/godot-formfactor)
- [Export to Android](https://developer.android.com/games/engines/godot/godot-export)

### Cocos

Cocos Creator is both an efficient,lightweight,free and open source
cross-platform 2D and 3D graphics engine and a real-time interactive 2D and 3D
digital content creation platform. Cocos Creator offers many advantages such as
high performance, low power consumption, streaming loading, and cross-platform
publishing. You can use it to create projects in fields such as games, cars, XR,
metaverse, and so on.

#### Guides

- [Steps to build a game for Android in Cocos Creator](https://developer.android.com/games/engines/cocos/cocos-overview)
- [Publish your game as Google Play Instant app in Cocos Creator](https://developer.android.com/games/engines/cocos/cocos-playinstant)
- [Publish your game with Android App Bundle in Cocos Creator](https://developer.android.com/games/engines/cocos/cocos-aab)
- [Remote debugging on Android](https://developer.android.com/games/engines/cocos/cocos-remotedebugging)

### Unity

Unity is a commercial game engine that has been used by many games. Unity is
designed for both 2D and 3D game development. Unity has been used for everything
from basic 2D sprite games to games featuring large complex 3D worlds. Unity has
multiple renderer options, including the Universal Render Pipeline, designed for
performant 2D or 3D graphics on mobile device hardware. Unity uses the C#
programming language, with plugin support for interfacing with native code.
Because of its popularity, Unity has a wide range of official and community
information and education resources. Unity operates the Unity Asset Store, which
is a vast marketplace of prebuilt art and code assets, both free and paid,
available for use in Unity projects.

#### Guides

- [Android development with Unity](https://developer.android.com/games/engines/unity/unity-on-android)
- [Create an Android App Bundle with Unity](https://blogs.unity3d.com/2018/10/03/support-for-android-app-bundle-aab-in-unity-2018-3-beta/)
- [Integrate Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity)
- [Lighting for mobile games in Unity](https://developer.android.com/games/optimize/lighting-for-mobile-games-with-unity)
- [Use Android Performance Tuner with Unity](https://developer.android.com/games/sdk/performance-tuner/unity)

### Unreal

Unreal Engine 4 is a commercial game engine specializing in high-end 3D games
with sophisticated graphics. Unreal includes a visual editor for editing game
levels and working with imported models and material assets. Unreal Engine 4
does not use a built-in scripting programming language. The Unreal Editor does
feature a visual scripting system called Blueprints, which can be used to
construct game and interface logic. Game functionality can also be implemented
as C++ code. Epic Games, the developer of Unreal, operates the Unreal Engine
Marketplace as a digital storefront for Unreal Engine resources. The Unreal
Engine Marketplace has a wide variety of prebuilt art and code assets available,
both free and paid, for use in Unreal projects. The [Android Game Development
Extension](https://developer.android.com/games/agde) can be used to debug Unreal projects running on Android.

For information, see [Android development with Unreal](https://developer.android.com/games/engines/unreal/unreal-on-android).