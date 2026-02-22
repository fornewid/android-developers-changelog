---
title: https://developer.android.com/topic/google-play-instant/instant-play-games-checklist
url: https://developer.android.com/topic/google-play-instant/instant-play-games-checklist
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Your game must meet the following requirements in order to be maintained in the Instant play program. Use the[self-review checklist](https://developer.android.com/topic/google-play-instant/instant-play-games-checklist#self-review-checklist)to verify compliance.
| **Important:** We are not accepting new Instant Game submissions for featuring in the Play Games app. However, Instant Games that have already been approved will continue to run on our surfaces as normal.

## Requirements

Instant play must meet all of the[Google Play Instant requirements](https://developer.android.com/topic/google-play-instant/game-tech-requirements), as well as all of the following technical and policy requirements:

1. The game is published using app bundle.

2. The game size is 15 MB or less ([downloading additional assets is possible post-launch](https://developer.android.com/topic/google-play-instant/getting-started/cloud-delivery-assets)).

3. The game supports Google Play Instant[sandbox restrictions](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#target-sandbox-version).

4. The game targets Android 8.0 (API level 26) or later.

5. The game supports 64-bit architectures.

6. The game does not use notifications.

7. The game only requires permissions from the[list of supported Google Play Instant permissions](https://developer.android.com/topic/google-play-instant/getting-started/instant-enabled-app-bundle#configure-permissions).

8. Automatic[sign-in using Google Play Games Services](https://developer.android.com/topic/google-play-instant/getting-started/support-play-games-services)is required.

   - If silent sign-in fails, prompt the user with interactive sign-in. Users should be able to cancel interactive sign-in. For more information, see the[Google Play Games Services quality checklist](https://developers.google.com/games/services/checklist#sign-in).
9. Provide a[view for Google Play Games Services popups](https://developers.google.com/games/services/android/signin#displaying_game_pop-ups)so that users can clearly see that they are signed in.

10. The game integrates a cloud save solution keyed by the Google Play Games Services player ID so that user game state persists across Instant play sessions and devices. You can use a product like[Cloud Firestore](https://firebase.google.com/docs/firestore)or another cloud database. Ensure that player progress is keyed by Google Play Games Services player ID and restored as soon as a player logs in.

    - Game save is mandatory in games that support any sort of persistence across play sessions. Other types of games (for example, roguelikes and simple board games) that are designed for short play sessions don't require game save. However, we strongly recommend using game saves or leaderboards for persisting this state so users do not lose their valuable scores or achievements.
11. If you don't have one already, add a landscape[promo video](https://support.google.com/googleplay/android-developer/answer/1078870)showing gameplay to your store listing. Users enjoy videos that feature gameplay taken directly from the game. Google Play will auto-generate a highlights clip from this video, which will be included in the Google Play Games app. You can capture video directly using[adb](https://developer.android.com/studio/command-line/adb#screenrecord). If your game has a portrait mode only, you can then convert it to landscape using a number of video editors.

12. The game does not include an install button for itself. An install button is not needed as the Instant play should be the same experience as the installed game. Users still have the ability to install the game from the details page in the Google Play Games app and the Google Play Store.

13. The game does not implement the[Google Play Games Services Anti-Piracy](https://developers.google.com/games/services/android/antipiracy)feature, or include the[`com.android.vending.CHECK_LICENSE`](https://developer.android.com/google/play/licensing/adding-licensing)permission in the manifest. The anti-piracy feature prevents users from pirating games that must be purchased; it has no benefit for free games. Enabling the anti-piracy check will prevent Google Play Instant apps from signing in to Google Play Games Services.

14. If the game uses OpenGL, ensure that it targets OpenGL ES 2.0, as it is the only version fully supported for Google Play Instant apps on devices running Android 7 and earlier. Ensure that you specify the correct version with[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element), setting`android:glEsVersion`to`0x00020000`.

15. Specify`1337`as the instant flavor in your`AndroidManifest.xml`file to indicate that this is a full-experience Instant play game (and not a trial game):

    ```carbon
      <?xml version="1.0" encoding="utf-8"?>
      <manifest xmlns:android="http://schemas.android.com/apk/res/android"
         xmlns:dist="http://schemas.android.com/apk/distribution"
         package="com.yourapp.package">
         <dist:module dist:instant="true" />
         <application android:allowBackup="true">
             <meta-data android:name="com.google.android.gms.instant.flavor" android:value="1337"/>
            ...
         </application>
      </manifest>
    ```
    | **Important:** This`meta-data`tag should only go in the manifest for the Instant play version of your game. It must**not** be in the manifest for the installable version.  
    |
    | This`meta-data`tag should be placed directly inside the`<application>`element and**not** , for example, inside an`<activity>`element.
16. The game is monetized in non-disruptive ways according to the following guidelines:

    - Make sure banner ads are unobtrusive to gameplay.
    - Place ads at natural breaks in the gameplay in between page content, levels, or stages. Don't overwhelm users with ads. Repeated ads often lead to poor user experiences and accidental clicks.
    - Pre-roll ads that are shown before the game is played need to be skippable after a maximum of 5 seconds.
    - Ads must not be disguised as in-game components or elements of menu/game navigation.
    - Cross-promotion to other games is acceptable, subject to the preceding ads requirements.

## Self-review checklist

Google verifies compliance and bug-free operation by running your game through a review. You can save time by checking compliance and proper behavior*prior*to starting the review process. Use the self-review checklist below:

1. **Promo video**
   - The game has a[promo video](https://support.google.com/googleplay/android-developer/answer/1078870)showing gameplay in the Play Console.
2. **Ads and in-app purchases**
   - Banner ads are unobtrusive and don't lead to accidental touches.
   - Ads are at natural breaks in the gameplay and don't overwhelm users.
   - Any pre-roll ads are skippable after a maximum of 5 seconds.
   - No install button is present anywhere in the game.
3. **Data use**
   - Users can start playing your game in less than 15 seconds over an LTE or 4G connection.
4. **Back button**
   - The player can exit the game using the back button on the root game menu. An exit confirmation dialog is allowed but not required. If a confirmation dialog is used, the game should exit if the user confirms exit or presses the back button again.
5. **Google Google Play Games Services sign-in**
   1. When opening the game from the Google Play Games app, the following occur:
      - The game attempts to silently sign in the user to Google Play Games Services.
      - Google Play Games Services displays a "Hey there" welcome message with the player's gamer ID.
   2. If silent sign-in fails, interactive sign-in starts. The user has the option to cancel sign-in to avoid an infinite sign-in loop.
6. **Restoring game state (game save / in-app purchases)**
   - Verify that game state can be restored:
     1. Play the game and make some meaningful progress (for example, reach a new level or new high score) and, if applicable, make an In-App Purchase (IAP).
     2. Quit the game and then remove it from the device (typically in**Settings \> Applications**).
     3. Relaunch the game**on the same device** and verify that**both the game progress and IAPs**are automatically restored.
     4. Relaunch the game**on a different device** and verify that**both the game progress and IAPs**are automatically restored.
7. **Offline support**
   - Verify that the game is playable offline:
     1. Launch the game when online and get to a playable state.
     2. Quit the game and kill the game process.
     3. Switch to airplane mode on the device.
     4. Relaunch the game and verify that the game is playable offline.
8. **Device support**
   - Ensure the game is fully playable on Android tablets.
   - Ensure the game runs on Android 5 (API level 21) and later.