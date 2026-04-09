---
title: https://developer.android.com/games/pgs/unity/migrate-to-v2
url: https://developer.android.com/games/pgs/unity/migrate-to-v2
source: md.txt
---

This document describes how to migrate existing games from the [games v1
SDK](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/package-summary)
to the [games v2
SDK](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary).
The Play Games plugin for Unity, versions 10 and earlier, uses the games v1 SDK.

## Before you begin

- Make sure that you have already set up Play Console and installed the Unity Editor.

## Download the Google Play Games plugin for Unity

To benefit from the latest features in the Play Games Services, download and
install the latest plugin version. Download it from the [gitHub
repository](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/current-build).

## Remove the old plugin

In the Unity Editor, remove the following folders or files.

```
Assets/GooglePlayGames

Assets/GeneratedLocalRepo/GooglePlayGames

Assets/Plugins/Android/GooglePlayGamesManifest.androidlib

Assets/Plugins/Android
```
[![Remove the highlighted folders in your Unity project.](https://developer.android.com/static/images/games/pgs/unityfolders.png)](https://developer.android.com/static/images/games/pgs/unityfolders.png) Remove the highlighted folders in your Unity project (click to enlarge).

## Import the new plugin to your Unity project

To import the plugin to your Unity project, follow these steps:

1. Open your game project.
2. In the Unity Editor, click **Assets \> Import Package \> Custom Package** to import the downloaded [`unitypackage`](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/current-build) file into your project's assets.
3. Make sure that your current build platform is set to **Android**.

   1. In the main menu, click **File \> Build Settings**.

   2. Select **Android** and click **Switch Platform**.

   3. There should be a new menu item under **Window \> Google Play Games** . If
      there isn't, refresh the assets by clicking **Assets \> Refresh** and
      then try setting the build platform again.

4. In the Unity Editor, click
   **File \> Build Settings \> Player Settings \> Other Settings**.

5. In the **Target API level** box, select a version.

6. In the **Scripting backend** box, enter `IL2CPP`.

7. In the **Target architectures** box, select a value.

8. Note the package name <var translate="no">package_name</var>.You can use this information
   later.

   ![The player settings in your Unity project](https://developer.android.com/static/images/games/unity-hub-project-setting.png) The player settings in your Unity project.
9. [Copy the Android resources from Play Console](https://developer.android.com/games/pgs/unity/unity-start#copy-android-resources)

10. [Add the Android resources to your Unity project](https://developer.android.com/games/pgs/unity/unity-start#set-up-unity-project)

## Update automatic sign-in code

Replace the `PlayGamesClientConfiguration` initialization class with the
`PlayGamesPlatform.Instance.Authenticate()` class.
The initialization and activation of
[`PlayGamesPlatform`](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform)
is not required. Calling `PlayGamesPlatform.Instance.Authenticate()` fetches the
result of automatic sign-in.

### C#

In the Unity Editor, locate the files with
`PlayGamesClientConfiguration` class.

    using GooglePlayGames;
    using GooglePlayGames.BasicApi;
    using UnityEngine.SocialPlatforms;

    public void Start() {
        PlayGamesClientConfiguration config =
            new PlayGamesClientConfiguration.Builder()
        // Enables saving game progress
        .EnableSavedGames()
        // Requests the email address of the player be available
        // will bring up a prompt for consent
        .RequestEmail()
        // Requests a server auth code be generated so it can be passed to an
        // associated backend server application and exchanged for an OAuth token
        .RequestServerAuthCode(false)
        // Requests an ID token be generated. This OAuth token can be used to
        // identify the player to other services such as Firebase.
        .RequestIdToken()
        .Build();

        PlayGamesPlatform.InitializeInstance(config);
        // recommended for debugging:
        PlayGamesPlatform.DebugLogEnabled = true;
        // Activate the Google Play Games platform
        PlayGamesPlatform.Activate();
    }

And update it to this:

    using GooglePlayGames;

    public void Start() {
        PlayGamesPlatform.Instance.Authenticate(ProcessAuthentication);
    }

    internal void ProcessAuthentication(SignInStatus status) {
        if (status == SignInStatus.Success) {
            // Continue with Play Games Services
        } else {
            // Disable your integration with Play Games Services or show a login
            // button to ask users to sign-in. Clicking it should call
            // PlayGamesPlatform.Instance.ManuallyAuthenticate(ProcessAuthentication).
        }
    }

## Choose a social platform

To choose a social platform, see
[choose a social platform](https://developer.android.com/games/pgs/unity/unity-start#choose-social-platform).

## Retrieve server authentication codes

To get server side access codes,
see [retrieve server authentication codes](https://developer.android.com/games/pgs/unity/unity-start#retrieve_server_authentication_codes).

## Remove sign-out code

Remove the code for sign-out. Play Games Services no longer requires an in-game
sign-out button.

Remove the code shown in the following example:

### C#

    // sign out
    PlayGamesPlatform.Instance.SignOut();

## Test your game

Ensure your game functions as designed by testing it. The tests you perform
depend on your game's features.

The following is a list of common tests to run.

1. **Successful sign-in**.

   1. Automatic sign-in works. The user should be signed in to
      Play Games Services upon launching the game.

   2. The welcome popup is displayed.


      [![Sample welcome popup.](https://developer.android.com/static/images/games/pgs/welcometoast.png)](https://developer.android.com/static/images/games/pgs/welcometoast.png) Sample welcome popup (click to enlarge).

      <br />

   3. Successful log messages are displayed. Run the following
      command in the terminal:

      ```bash
      adb logcat | grep com.google.android.
      ```

      A successful log message is shown in the following example:

      ```bash
      [$PlaylogGamesSignInAction$SignInPerformerSource@e1cdecc
      number=1 name=GAMES_SERVICE_BROKER>], returning true for shouldShowWelcomePopup.
      [CONTEXT service_id=1 ]
      ```
2. **Ensure UI component consistency**.

   1. Pop ups, leaderboards, and achievements display correctly and
      consistently on various screen sizes and orientations in the
      Play Games Services user interface (UI).

   2. Sign-out option is not visible in the Play Games Services
      UI.

   3. Make sure you can successfully retrieve Player ID, and if applicable,
      server-side capabilities work as expected.

   4. If the game uses server-side authentication, thoroughly test the
      `requestServerSideAccess` flow. Ensure the server receives the auth code
      and can exchange it for an access token.
      Test both success and failure scenarios for network errors, invalid
      `client ID` scenarios.

If your game was using any of the following features, test them to ensure that
they work the same as before the migration:

- **Leaderboards**: Submit scores and view leaderboards. Check for the correct ranking and display of player names and scores.
- **Achievements**: Unlock achievements and verify they are correctly recorded and displayed in the Play Games UI.
- **Saved Games**: If the game uses saved games, ensure that saving and loading the game progress works flawlessly. This is particularly critical to test across multiple devices and after app updates.

## Post migration tasks

Complete the following steps after you have migrated to games v2 SDK.

1. [Use Play App Signing](https://developer.android.com/games/pgs/unity/unity-start#create-test-release)

2. [Create an AAB file](https://developer.android.com/games/pgs/unity/unity-start#create_an_aab_file)

3. [Create an internal testing release](https://developer.android.com/games/pgs/unity/unity-start#create_an_internal_testing_release)

4. [Verify your App signing credentials](https://developer.android.com/games/pgs/unity/unity-start#set-up-app-signin)