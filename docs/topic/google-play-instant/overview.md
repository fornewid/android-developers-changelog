---
title: https://developer.android.com/topic/google-play-instant/overview
url: https://developer.android.com/topic/google-play-instant/overview
source: md.txt
---

# Overview of Google Play Instant

**Important:** Starting in August 2021, all new instant experiences and updates to existing experiences must publish with instant-enabled app bundles on Google Play.  
**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Google Play Instant enables native apps and games to launch on devices running Android 5.0 (API level 21) or higher without being installed. You can build these types of experiences, called*instant apps* and*instant games* , using Android Studio. By allowing users to run an instant app or instant game, known as providing an*instant experience*, you improve your app or game's discovery, which helps drive more active users or installations.
| **Note:** Instant apps and games can use only a subset of APIs within the Android SDK and the Android NDK. When creating an instant experience, make sure you[request only supported permissions](https://developer.android.com/topic/google-play-instant/getting-started/instant-enabled-app-bundle#request-supported-permissions).

This guide presents an overview of the Google Play Instant experience.

## How the instant experience works

With Google Play Instant, users can tap on a button in the Play Store, Google Play Games app, or a website banner to use an app or game without installing it first. Figures 1 and 2 show examples of these discovery surfaces.

When Google Play receives one of these requests for an instant app or game, it sends the necessary files to the Android device that sent the request. The device then runs the app or game.

Instant experiences fall into two categories: "Try" experiences in the Play Store and "Instant play" games in the Google Play Games app.  
![The 'Try Now' button appears next to the 'Install' button](https://developer.android.com/static/topic/google-play-instant/images/gpi-try-now.png)**Figure 1.** The**Try Now**button that appears on an instant-enabled app or game's page on Google Play  
![The 'Instant play' button appears in the Google Play Games app](https://developer.android.com/static/topic/google-play-instant/images/play-instant-games-full-experience.png)**Figure 2.** The**Instant play** button appears on a full experience game in the[Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games)

### Instant "Try" experience in the Play Store

Instant experiences are shown using a**Try now**button in the Play Store (as shown in Figure 1). This type of experience is typically a smaller trial version of your app or game created with the goal of driving installs. For example, game developers may want to build the first level of their game as an instant experience and then prompt users to install the full game.

Google Play Instant also allows you to[display a prompt](https://developer.android.com/topic/google-play-instant/getting-started/instant-enabled-app-bundle#install-prompt)within your instant experience, inviting users to install the full experience on their device.

### "Instant play" full game experience in the Play Games app

Full games that are packaged using Google Play Instant are eligible to be featured prominently on the homepage of the[Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games). These "Instant play" games are*full experience* games, not trial versions. Players tap on the**Instant play** button (as shown in Figure 2) to play the full game without installing it first. To learn more, see[Instant play games](https://developer.android.com/topic/google-play-instant/instant-play-games).

## Enable instant experiences by reducing app or game size

Your app or game must be under 15 MB to enable these instant experiences, but the smaller you make it, the better it will be for users.

Reducing the size of your instant app or game has a number of benefits including:

- Higher user engagement or installations and business success
- Enabling all instant surfaces including the**Try now**button in the Play Store
- "Instant play" homepage featuring in the Google Play Games app

To learn how you can reduce the size of your app or game, see[Reduce the size of your instant app or game](https://developer.android.com/topic/google-play-instant/guides/reduce-module-size).

## Considerations

Some apps contain more advanced architectural elements, which the following sections describe. If your app or game contains any of the following elements, read the section for that element.

### Deep links

If your existing app already uses deep links or Android App Links, see the guide on how to[create app links for your instant experience](https://developer.android.com/training/app-links/instant-app-links).
| **Note:** Users can opt out of opening links within apps. A menu in the device's system settings called**Instant apps**provides this option.

### Multiple entry points

It's possible to provide different instant experiences from the same app or game by creating multiple entry points. For example, a puzzle game might have two different modes: a single-player, timed challenge and a multi-player matchup. You could deploy these modes as separate instant experiences, allowing players to try out different aspects of gameplay.

To create these different entry points, configure a different entry point for each experience that you'd like to provide. To learn more, see[Provide multiple entry points into an instant experience](https://developer.android.com/topic/google-play-instant/guides/multiple-entry-points).
| **Caution:** Don't use a central routing activity in your instant experience. Instead, provide multiple entry points so that the Android framework does the routing for you. This approach enables you to achieve more modularization in your app or game.

## Learn more

To learn more about Google Play Instant, see the following resources:

- [List of known issues](https://issuetracker.google.com/issues?q=status:open+componentid:316045)
- [StackOverflow component for instant apps](https://stackoverflow.com/questions/tagged/android-instant-apps)
- [Developer stories](https://developer.android.com/stories/instant-apps)

## Additional resources

For more information about Google Play Instant, consult the following resources.

### Training

- Google I/O 2018:[The future of apps on Android and Google Play: modular, instant, and dynamic](https://www.youtube.com/watch?v=0raqVydJmNE&t=1057s)
- Google I/O 2018:[How game developers are providing success](https://youtu.be/LN1YQeo6yNk)