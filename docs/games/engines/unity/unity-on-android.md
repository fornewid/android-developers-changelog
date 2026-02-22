---
title: https://developer.android.com/games/engines/unity/unity-on-android
url: https://developer.android.com/games/engines/unity/unity-on-android
source: md.txt
---

Unity is a cross-platform game engine used by many games on the Google Play Store. Unity's modular tools help you produce and deliver highly engaging 2D or 3D mobile games.

## Create a Unity game for Android

To create a game experience for players on Android, follow these steps:

1. [Download](https://unity3d.com/get-unity/download)and[install the Unity Hub](https://docs.unity3d.com/Manual/GettingStartedInstallingUnity.html).
2. To start Unity Hub, click**Installs** tab and then click**Install Unity editor** . Install a version of the Unity Editor that[supports 64-bit apps](https://developer.android.com/games/optimize/64-bit#unity-developers). These versions support[Android App Bundles](https://developer.android.com/guide/app-bundle), which enable smaller, more optimized downloads.

   ![Add an editor in the Unity Hub](https://developer.android.com/static/images/games/unity-hub-add-editor.png)
3. When you install the Unity Editor, make sure to include the[**Android Build Support**](https://docs.unity3d.com/Manual/android-sdksetup.html)module by checking the box next to it.

   - Expand the**Android Build Support** module. If you are using Unity 2019 or later, add the**Android SDK \& NDK Tools**module.

   ![Add the Android Build Support NDK option in the Unity Hub](https://developer.android.com/static/images/games/unity-hub-add-ndk.png)
4. In the**Projects** tab, click**New project**.

   ![Start a new project](https://developer.android.com/static/images/games/unity-start-new-project.png)
5. To develop your game, see the[learn](https://learn.unity.com/learn/)page.

## Play Asset Delivery

Play Asset Delivery enables AssetBundles and other assets to be packaged into an Android App Bundle and delivered through Google Play. Refer to the[documentation](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity)and[Runtime API reference](https://developer.android.com/reference/unity/namespace/Google/Play/AssetDelivery)for more information on how to integrate this feature with Unity plugins.

## Play Integrity API

Play Integrity API helps you check that your game is unmodified, installed by Google Play, and running on either a genuine Android-powered device or a genuine instance of Google Play Games for PC. Your game's backend server can respond when you detect risky traffic to prevent unauthorized access and cheating. Refer to the[documentation](https://developer.android.com/google/play/integrity/setup#unity)and[Runtime API reference](https://developer.android.com/reference/unity/namespace/Google/Play/Integrity)for more information on how to integrate this feature with Unity plugins.

## Play In-app Updates

Play In-app Updates lets you prompt users to update to the latest version of your game, when a new version is available, without the user needing to visit the Play Store. Refer to the[documentation](https://developer.android.com/guide/playcore/in-app-updates/unity)and[Runtime API reference](https://developer.android.com/reference/unity/namespace/Google/Play/AppUpdate)for more information on how to integrate this feature with Unity plugins.

## Play In-app Reviews

Play In-app Reviews lets you prompt users to submit Play Store ratings and reviews without leaving your game. Refer to the[documentation](https://developer.android.com/guide/playcore/in-app-review/unity)and[Runtime API reference](https://developer.android.com/reference/unity/namespace/Google/Play/Review)for more information on how to integrate this feature with Unity plugins.

## Play Games Services

Play Games Services lets you access the Google Play Games API through Unity's[social interface](http://docs.unity3d.com/Documentation/ScriptReference/Social.html)to provide access to features like player authentication with Google Play Games accounts, interaction with friends lists, and achievement management (unlocking, revealing, and incrementing). Detailed setup and usage instructions are available in the[documentation](https://developer.android.com/games/pgs/unity/unity-start).

## 16 KB page size support

A page is the granularity at which an operating system manages[memory](https://android-developers.googleblog.com/2024/08/adding-16-kb-page-size-to-android.html). To improve the operating system performance overall and to give device manufacturers an option to make this trade-off, Android 15 (API level 35) and higher can run with 4 KB or 16 KB page sizes. Devices configured with 16 KB page sizes use slightly more memory on average but also gain various performance improvements.

Unity has 16 KB page support for[Unity 2021, 2022](https://discussions.unity.com/t/info-unity-engine-support-for-16-kb-memory-page-sizes-android-15/1589588)and[Unity 6](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html).