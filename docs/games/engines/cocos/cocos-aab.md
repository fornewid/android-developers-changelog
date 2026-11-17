---
title: https://developer.android.com/games/engines/cocos/cocos-aab
url: https://developer.android.com/games/engines/cocos/cocos-aab
source: md.txt
---

> Documentation index: https://developer.android.com/games/llms.txt

An [Android App Bundle](https://developer.android.com/guide/app-bundle.md.txt) is a publishing format that includes all your app's
compiled code and resources, and defers APK generation and signing to Google
Play.

Google Play uses your app bundle to generate and serve optimized APKs for each
device configuration, so only the code and resources that are needed for a
specific device are downloaded to run your app. You no longer have to build,
sign, and manage multiple APKs to optimize support for different devices, and
users get smaller, more-optimized downloads.

## How to publish your game with AAB format

In Cocos Creator, just check the **Generate App Bundle (Google Play)** option in
the Android Build panel. Your game will then be published with the AAB format.
![Cocos Creator Android Build panel with Generate App Bundle option.](https://developer.android.com/static/images/games/engines/cocos/abb.png) **Figure 1.** Generate App Bundle option in the Android Build panel.