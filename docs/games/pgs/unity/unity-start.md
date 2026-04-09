---
title: https://developer.android.com/games/pgs/unity/unity-start
url: https://developer.android.com/games/pgs/unity/unity-start
source: md.txt
---

This document guides you through setting up your Unity project to use the
Google Play Games plugin for Unity. You learn how to install the plugin and
configure your Unity project. The document also covers how to verify the
authentication service.

## Before you begin

Review the [software requirements](https://developer.android.com/games/pgs/unity/overview#requirements).
Set up Play Console and install the Unity Editor.

- [Set up Play Console](https://developer.android.com/games/pgs/console/setup) for your game.

- Install Unity Editor and
  [build your game in Unity](https://developer.android.com/games/engines/unity/unity-on-android).

## Plugin Installation

To download and install the Google Play Games plugin for Unity, follow these
steps in Unity Editor:

1. Download the [GitHub repo](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/current-build).

2. In the `current-build` directory, locate the `unitypackage` file. This file
   represents the plugin. For example, it should resemble the following:

         current-build/GooglePlayGamesPluginForUnity-X.YY.ZZ.unitypackage

## Set up Unity project

To set up a Unity project in player settings, follow these steps:

1. Open your game project.

2. In the Unity Editor, click **Assets \> Import Package \> Custom Package**
   to import the `unitypackage` file into your project's assets.

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

### Create a new keystore

To validate your credentials, you need a key.
Follow these steps:

1. In the Unity Editor, click **File \> Build settings \> Player settings**.
2. In the **Publishing settings** section, click **Keystore manager** .
   1. In the **Keystore manager** window, click **Keystore \> Create new \> Anywhere**.
   2. Select a folder and provide a name for the keystore.
   3. In the **Password** box, enter a password and confirm.
   4. Click **Add key**.

Note the folder name. You can use this name to
[create a credential](https://developer.android.com/games/pgs/console/setup#create_a_credential) in
Google Cloud.

## Copy the Android resources from Play Console

Each achievement, leaderboard, and event you create in
Play Console includes an Android resource that you use when you
[set up your Unity project](https://developer.android.com/games/pgs/unity/unity-start#set-up-unity-project).

To get the Android resources for your game, follow these steps:

1. In the [Google Play Console](https://play.google.com/apps/publish/),
   open the game.

2. In the **Play Games Services - Configuration** page (**Grow users \>
   Play Games Services \> Setup and
   management \> Configuration** ),
   click **Get resources**.

3. In the **Resources** window, click the **Android(XML)** tab.

4. Select and copy the Android resources (`AndroidManifest.xml`) content.

## Add the Android resources to your Unity project

Add the following Android resources to your Unity project:

1. In the Unity Editor, click **Window \> Google Play Games \> Setup \>
   Android Setup**.

   - In the **Directory to save constants** field, enter the folder name for the constants file.
   - In the **Constants class name** field, enter the name of the C# class to
     create, including the namespace.

     For example, if the C# class is `id.cs` and present under
     **Assets \> myproject \> scripts \> id.cs** .
     The constants class name can be `myproject.scripts.id`.
   - In the **Resources definition** field, paste the Android resources data
     (`AndroidManifest.xml` file) you copied from the Google Play Console.

   - Optional: In the **Client ID** field, enter the client ID of the linked
     web app.

     To get the client ID for your game from Google Cloud, see
     [Creating client IDs](https://cloud.google.com/endpoints/docs/frameworks/java/creating-client-ids).

     This is only needed if you have a [web-based backend](https://developer.android.com/games/pgs/android/server-access)
     for your game and need a server auth code to exchange for an access token
     by the backend server, or if you need an ID token for the player to make
     other non-game API calls.
   - Click **Setup**. This configures your game with the client ID and
     generates a C# class that contains constants for each of your Android
     resources.

2. In the Unity Editor, click **Window \> Google Play Games \> Setup \>
   Nearby Connections Setup**.

   - In the **Nearby connection service ID** field, enter the
     <var translate="no">package_name</var>.

     Use the same <var translate="no">package_name</var> that you used in
     [set up Unity project](https://developer.android.com/games/pgs/unity/unity-start#set-unity-player-settings).
   - Click **Setup**.

## Choose a social platform

The Google Play Games Services plugin implements Unity's
[social interface](http://docs.unity3d.com/Documentation/ScriptReference/Social.html),
for compatibility with games that already use that interface when integrating
with other platforms. However, some features are unique to Play Games and are
offered as extensions to the standard social interface provided by Unity.

The standard API calls can be accessed through the **Social.Active** object,
which is a reference to an **ISocialPlatform** interface. The non-standard
Google Play Games Services extensions can be accessed by casting the **Social.Active**
object to the **PlayGamesPlatform** class, where the additional methods are
available.

### Use the plugin without overriding the default social platform

When you call
[`PlayGamesPlatform.Activate`](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#activate),
Google Play Games Services becomes your default social platform implementation. This means
that the Google Play Games Services plugin carries out static calls to methods in `Social` and
`Social.Active`, which is the expected behavior for most games using the plugin.

However, if for some reason you want to keep the default implementation
accessible (for example, to use it to submit achievements and leaderboards to a
different social platform), you can use the Google Play Games Services plugin without
overriding the default one. To do this:

1. Call the `PlayGamesPlatform.Activate` method.
2. If `Xyz` is the name of a method that you call on the `Social` class, don't call `Social.Xyz`. Instead, call `PlayGamesPlatform.Instance.Xyz`.
3. Use the [`PlayGamesPlatform.Instance`](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#instance) property instead of `Social.Active` when you interact with Google Play Games Services.

That way, you can even submit scores and achievements simultaneously to two or
more social platforms:

        // Submit achievement to original default social platform
        Social.ReportProgress("MyAchievementIdHere", 100.0f, callback);

        // Submit achievement to Google Play
        PlayGamesPlatform.Instance.ReportProgress("MyGooglePlayAchievementIdHere", 100.0f, callback);

## Verify the authentication service

A connection to Play Games Services is automatically attempted using the
[Platform authentication](https://developer.android.com/games/pgs/signin) when your game is opened. If the
connection succeeds, your game displays a sign-in prompt and is ready to use the
Google Play Games Services plugin for Unity.

If a user has never used Google Play Games Services on their device, they are
automatically taken through one-time setup screen to create a Play Games
account.

In the `Start` method of your script, listen to the result of the automatic
authentication attempt, fetch the authentication status, and disable Play Games
Services features if the user is not authenticated.

If the Unity plugin version is before `v11`, you can't use the authentication
feature.

        using GooglePlayGames;

        public void Start() {
          PlayGamesPlatform.Instance.Authenticate(ProcessAuthentication);
        }

        internal void ProcessAuthentication(SignInStatus status) {
          if (status == SignInStatus.Success) {
            // Continue with Play Games Services
          } else {
            // Disable your integration with Play Games Services or show a login button
            // to ask users to authenticate. Clicking it should call
            // PlayGamesPlatform.Instance.ManuallyAuthenticate(ProcessAuthentication).
          }
        }

The result code is an enum that you can use to identify the reason for and
authentication failure.

If you prefer using Unity's Social platform, you can alternatively use the
following code:

      using GooglePlayGames;

      public void Start() {
        PlayGamesPlatform.Activate();
        Social.localUser.Authenticate(ProcessAuthentication);
      }

You cannot make any Google Play Games Services API calls until you get a successful
return value from `Authenticate`. As a result, we recommend that games display a
standby screen until the callback is called to ensure users can't start playing
the game until authentication completes.

> [!NOTE]
> **Note:** For more information about how Player IDs work, visit the topic [here on
> next generation Player IDs](https://developer.android.com/games/pgs/next-gen-player-ids)

## Use Play App Signing

Google manages and protects your app's signing key using Play App Signing.
You can use Play App Signing to sign optimized, distribution of
[Android APP Bundle](https://developer.android.com/guide/app-bundle)(AAB) files. Play App Signing stores your
app signing key on Google's secure infrastructure.
To use Play App Signing, you have to first create and download an AAB file from
Unity Editor. You can then upload the AAB file to
Play Console and create an internal testing release.

### Create an AAB file

To create an AAB file in Unity Editor, follow these steps:

1. In the Unity Editor, click **File \> Build settings**.
2. Select **Build App Bundle ( Google Play )**.

   For more information, see
   [Android Build Settings reference](https://docs.unity3d.com/Manual/android-build-settings.html).
3. Click **Build**.

4. Download the AAB file from the Unity Editor.

### Create an internal testing release

To create an internal testing release and add testers in
Play Console, perform the following steps:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Navigate to the **Test and release** page (**Testing \>
   Internal testing**).
3. Click **Upload** and select the AAB file.
4. In the **Release details** field, enter a name.
5. Click **Next** and review the release details.
6. Click **Save and publish**.
7. On the **Testers** tab, click **Create email list** to add up to 100 testers.

   For more information,
   see [Internal test: manage up to 100 testers](https://support.google.com/googleplay/android-developer/answer/9845334?ref_topic=7071528&sjid=2952420096171068663-AP#internal_test).
8. In the **Feedback URL or email address**, enter a feedback URL or and email
   address to provide feedback.

9. Click **Save**.

### Verify your App signing credentials

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Navigate to the **Test and release** page (**Setup \> App signing**).
3. Verify your App signing credentials.

## Build and run the project

You can build and run the game project at this point. When game starts, you'll
see the automatic authentication attempt.

You need a physical Android-powered device with USB debugging enabled or an
emulator that can run the developed project.

### Retrieve server authentication codes

In order to access Google APIs on a backend web server on behalf of the current
player, you need to get an authentication code from the client application and
pass this to your web server application. The code can then be exchanged for
an access token to make calls to the various APIs. For information about the
workflow, see
[sign in with Google for web](https://developers.google.com/identity/gsi/web/guides/overview).

To get the server side access code:

1. Add the web client ID for your game in the Play Console.
   1. In the [Google Play Console](https://play.google.com/apps/publish/), select your game.
   2. In the **Configuration** page (**Grow users \> Play Games Services \> Setup and Management \>
      Configuration** ), click **Add credential**.
   3. In the **Add credential** page, select **Game server**.
   4. [Generate an OAuth 2.0 client ID](https://developer.android.com/games/pgs/console/setup#generate_an_oauth_20_client_id).
   5. Note the client ID value. You'll need to provide this value later.
2. Add the web client ID to Unity hub.

   1. In the Unity hub, [set up Google Play Games for Unity and authenticate](https://developer.android.com/games/pgs/unity/unity-start).
   2. In the Unity hub, go to **Window \> Google Play Games \> Setup \>
      Android Setup**.
   3. Enter the client ID value.
3. Retrieve server auth code for additional scopes.

   ### C#

   ```c#
   using GooglePlayGames.BasicApi;

   // Define selectedScope having additional identity scopes.
   private List selectedScopes = new List();

   // Add scopes you want to request.
   selectedScopes.Add(AuthScope.OPEN_ID);
   selectedScopes.Add(AuthScope.PROFILE);
   selectedScopes.Add(AuthScope.EMAIL);

   // Call RequestServerSideAccess with additional scopes and retrieve
   // authcode and grantedscopes list.
   PlayGamesPlatform.Instance.RequestServerSideAccess(
       /* forceRefreshToken= */ false,selectedScopes
       (AuthResponse authResponse) =>
       {
       string authCode = authResponse.GetAuthCode();
       List grantedScopes = authResponse.GetGrantedScopes();

       // send authCode to server...
   });
   ```

## Set up and add features

- [Enable](https://developer.android.com/games/pgs/console/enable-features) Play Games Services features.

- Add features to your game using the Play Games Services APIs:

  - [Achievements](https://developer.android.com/games/pgs/unity/achievements)

  - [Leaderboards](https://developer.android.com/games/pgs/unity/leaderboards)

  - [Friends](https://developer.android.com/games/pgs/unity/friends)

  - [Save games](https://developer.android.com/games/pgs/unity/saved-games)

  - [Player stats](https://developer.android.com/games/pgs/unity/stats)

  - [Events](https://developer.android.com/games/pgs/unity/events)

- [Recall API for Unity](https://developer.android.com/games/pgs/recall/recall-setup#unity-sdk)
  (supported only for Unity plugin version v11 and above)