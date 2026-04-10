---
title: https://developer.android.com/stories/games/cat-daddy-agdk
url: https://developer.android.com/stories/games/cat-daddy-agdk
source: md.txt
---

# 2K reduces ANR rate by 35% with the Android Game Development Kit

## Background

![](https://developer.android.com/static/images/stories/games/nba2k.png)

Cat Daddy Games is a wholly-owned[2K](https://play.google.com/store/apps/dev?id=6681606924556273560)studio based in Kirkland, Washington and the developer of NBA 2K Mobile. The team wanted to improve the overall quality and stability of their games, specifically by reducing "Application Not Responding" errors (ANRs). ANRs occur when the UI thread of an Android app is blocked for too long. When that happens, the app's main thread, which is responsible for updating the UI, can't draw or process user input events, causing frustration to the user. If the app is running in the foreground, the system displays a dialog that allows the user to force-quit the app.

## What they did

Reducing ANRs has been a high priority for Cat Daddy. The QA team worked relentlessly and nailed down a common ANR pattern: they found that when the app was paused and then quickly resumed, a large amount of touch input could cause an ANR. Further investigation with[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)showed that this ANR was of type android.os.MessageQueue.nativePollOnce, the most common type of ANR for NBA 2K Mobile.

Cat Daddy also saw that the improved input handling in GameActivity could avoid this type of ANRs, so they decided to move to GameActivity.

[GameActivity](https://developer.android.com/games/agdk/game-activity)is a component of the[Android Game Development Kit](https://developer.android.com/stories/games/games/agdk), which is designed to assist Android games in processing app cycle commands, input events, and text input in the application's C/C++ code. GameActivity offers a number of game-focused improvements over`NativeActivity`, such as[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment), rendering to a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView), and other support for popular game development-related libraries.

GameActivity also uses double buffering in its input buffer, allowing the game to better handle this case of high input volume.

## Results

By implementing GameActivity, Cat Daddy was able to significantly improve the input handling of the game, leading to a 35% reduction in ANR errors. This improved the user experience and created a more stable gameplay experience.

As an added bonus, because GameActivity inherits from[`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity), CatDaddy was also able to integrate EmbeddedWebView and EmbeddedVideoView, which were required for some of the most popular social game integrations.

## Get started

Improve your own game experience with[GameActivity](https://developer.android.com/games/agdk/game-activity)and the rest of the[Android Game Development Kit](https://developer.android.com/games/agdk).