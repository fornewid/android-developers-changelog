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

## Migration paths

The correct migration path for your game depends on how it implements Play Games Services v1 and
handles player identity. To ensure a smooth transition and prevent player data
loss, identify the scenario that best matches your existing setup and follow the
corresponding steps.

### Option 1: For Games where IGA is bound to Play Games Services Player ID

This scenario applies to games that have used the Play Games Services `Player ID` as the only
identifier for a player's In-Game Account (IGA) and have not previously
requested or stored an `OpenID`. The central challenge is to link the existing
IGA to a primary identifier (the `OpenID`) without losing the connection to the
player's progress.

The migration flow includes the following steps:

1. When the game launches, the Play Games Services v2 SDK automatically and silently authenticates the platform.
2. The game presents its login screen. This screen must feature a [**Sign in
   with Google**](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/current-build) (SiWG)
   button, replacing the **Google Play** button. To integrate:

   1. Download [CredManBridge.java](https://github.com/android/games-samples/blob/wickedcube/multi-login-credman/trivialkart/trivialkart-unity/Assets/Plugins/Android/CredManBridge.java) to your folder. This Java class acts as
      a bridge between Unity and the `androidx.credentials` library.

      ##### CredManBridge.java


          package com.wickedcube.trivialkart;
          import android.accounts.Account;
          import android.content.Context;
          import android.util.Log;
          import android.os.CancellationSignal;
          import androidx.credentials.CredentialManager;
          import androidx.credentials.GetCredentialRequest;
          import androidx.credentials.GetCredentialResponse;
          import androidx.credentials.exceptions.GetCredentialException;
          import androidx.credentials.exceptions.NoCredentialException;
          import com.google.android.libraries.identity.googleid.GetGoogleIdOption;
          import com.google.android.libraries.identity.googleid.GoogleIdTokenCredential;
          import com.google.android.gms.auth.api.identity.AuthorizationClient;
          import com.google.android.gms.auth.api.identity.AuthorizationRequest;
          import com.google.android.gms.auth.api.identity.AuthorizationResult;
          import com.google.android.gms.common.api.ApiException;
          import com.google.android.gms.auth.api.identity.Identity;
          import com.google.android.gms.common.api.Scope;
          import com.unity3d.player.UnityPlayer;
          import java.util.Collections;
          import java.util.List;
          import java.util.concurrent.Executor;
          import java.util.concurrent.Executors;

          <br />





          public class CredManBridge {



          // --- MODE 1: SILENT SIGN-IN (Called on Awake) ---
          // Tries to auto-select an authorized account. If it fails, it does NOT show UI.
          public static void signInSilent(Context context, String webClientId) {
            CredentialManager credentialManager = CredentialManager.create(context);
            CancellationSignal cancellationSignal = new CancellationSignal();
            Executor executor = Executors.newSingleThreadExecutor();



          Log.d("CredMan", "Attempting Silent Sign-In...");



          GetGoogleIdOption silentOption = new GetGoogleIdOption.Builder()
              .setFilterByAuthorizedAccounts(true) // Strict: Only authorized accounts
              .setServerClientId(webClientId)
              .setAutoSelectEnabled(true)          // Auto-select if possible
              .build();



          GetCredentialRequest silentRequest = new GetCredentialRequest.Builder()
              .addCredentialOption(silentOption)
              .build();



          credentialManager.getCredentialAsync(
              context,
              silentRequest,
              cancellationSignal,
              executor,
              new androidx.credentials.CredentialManagerCallback<GetCredentialResponse, GetCredentialException>() {
                  @Override
                  public void onResult(GetCredentialResponse result) {
                      Log.d("CredMan", "Silent Sign-In Successful!");
                      handleSignInResult(context, result, webClientId);
                  }


                  @Override
                  public void onError(GetCredentialException e) {
                      // Send a specific error code so Unity knows to just stay on the Start Screen
                      Log.d("CredMan", "Silent sign-in failed. Keeping UI hidden.");
                      UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "SilentFailed");
                  }
              }




          );
          }



          // --- MODE 2: INTERACTIVE SIGN-IN (Called on Button Click) ---
          // Forces the Account Selection / "Add Account" sheet to appear.
          public static void signInInteractive(Context context, String webClientId) {
            CredentialManager credentialManager = CredentialManager.create(context);
            CancellationSignal cancellationSignal = new CancellationSignal();
            Executor executor = Executors.newSingleThreadExecutor();



          Log.d("CredMan", "Starting Interactive Sign-In...");



          GetGoogleIdOption interactiveOption = new GetGoogleIdOption.Builder()
              .setFilterByAuthorizedAccounts(false) // Show ALL accounts (and "Add Account")
              .setServerClientId(webClientId)
              .setAutoSelectEnabled(false)          // Force the UI to show
              .build();



          GetCredentialRequest interactiveRequest = new GetCredentialRequest.Builder()
              .addCredentialOption(interactiveOption)
              .build();



          credentialManager.getCredentialAsync(
              context,
              interactiveRequest,
              cancellationSignal,
              executor,
              new androidx.credentials.CredentialManagerCallback() {
                  @Override
                  public void onResult(GetCredentialResponse result) {
                      Log.d("CredMan", "Interactive Sign-In Successful!");
                      handleSignInResult(context, result, webClientId);
                  }


                  @Override
                  public void onError(GetCredentialException e) {
                      Log.e("CredMan", "Interactive Sign-In Canceled or Failed", e);
                      UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "Canceled");
                  }
              }




          );
          }



          private static void handleSignInResult(Context context, GetCredentialResponse result, String webClientId) {
            try {
              GoogleIdTokenCredential credential = GoogleIdTokenCredential.createFrom(result.getCredential().getData());
              String email = credential.getId();


              Account account = new Account(email, "com.google");
              // Requesting GAMES_LITE scope to check for pre-existing V1 grants
              List<Scope> requestedScopes = Collections.singletonList(new Scope("https://www.googleapis.com/auth/games_lite"));

              AuthorizationRequest authRequest = new AuthorizationRequest.Builder()
                  .setRequestedScopes(requestedScopes)
                  .setAccount(account)
                  .requestOfflineAccess(webClientId)
                  .build();

              AuthorizationClient authClient = Identity.getAuthorizationClient(context);

              authClient.authorize(authRequest)
                  .addOnSuccessListener(authorizationResult -> {
                      if (authorizationResult.getServerAuthCode() != null) {
                          // CASE 1: RETURNING USER (Success)
                          // The user has already granted GAMES_LITE in the past.
                          // We got the code directly without showing UI.
                          Log.i("CredMan", "PGS v1: Existing grant found. Returning user detected. Auth Code retrieved.");
                          UnityPlayer.UnitySendMessage("AuthManager", "OnSignInSuccess", authorizationResult.getServerAuthCode());
                      }
                      else if (authorizationResult.hasResolution()) {
                          // CASE 2: NEW USER (PendingIntent)
                          // The user has NOT granted GAMES_LITE before. The API returned a PendingIntent
                          // (authorizationResult.getPendingIntent()) to show the consent screen.
                          // As per your flow, we DISCARD this intent and do not show UI.
                          Log.i("CredMan", "PGS v1: No existing grant (PendingIntent returned). This is a NEW user or they revoked access.");
                          Log.i("CredMan", "PGS v1: Discarding PendingIntent. Proceeding as New User.");

                          // Notify Unity that this is a "New User" so it can trigger V2 logic instead of failing
                          UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "NewUser_NoGrant");
                      }
                      else {
                          // Edge Case: No code and no resolution?
                          Log.e("CredMan", "PGS v1: Authorization success but no Auth Code or Resolution returned.");
                          UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "No Auth Code returned");
                      }
                  })
                  .addOnFailureListener(e -> {
                      // CASE 3: GENERIC FAILURE
                      Log.e("CredMan", "PGS v1: Authorization failed completely.", e);
                      UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "Authorization Failed: " + e.getMessage());
                  });



          `} catch (Exception e) {
              UnityPlayer.UnitySendMessage("AuthManager", "OnSignInError", "Parsing Error: " + e.getMessage());
          }
          }
          }
          `

      <br />

   2. **Credential Manager Integration:**

      - Use `GetGoogleIdOption` with `setFilterByAuthorizedAccounts(true)` for silent sign-ins to only sign in users who have previously authorized the app.
      - Use `setFilterByAuthorizedAccounts(false)` for interactive sign-ins to allow users to select an account or add a new one.
   3. **Scope Request:**

      - After obtaining the base Google credential, it creates an `AuthorizationRequest` requesting the specific legacy scope: <https://www.googleapis.com/auth/games_lite>.
      - This scope is critical as it grants the server permission to look up the user's legacy PlayerID.
   4. **Result Handling:**

      - If the user grants permission (or has previously granted it), the bridge returns the `ServerAuthCode` to Unity.
      - If the user has not granted permission (New User scenario), the API returns a `PendingIntent`. In this sample, the intent is discarded, and the user is treated as a new user to simplify the flow.
3. To support the Credential Manager and Google Identity services, ensure the
   following dependencies are added to your `mainTemplate.gradle` gradle
   configuration.

   ```
   dependencies {
   // Standard Unity dependencies
   implementation fileTree(dir: 'libs', include: ['*.jar'])

   // Credential Manager and Identity Libraries
   implementation 'androidx.credentials:credentials:1.3.0'
   implementation 'androidx.credentials:credentials-play-services-auth:1.3.0'
   implementation 'com.google.android.libraries.identity.googleid:googleid:1.1.1'

   // Play Services Auth for legacy scope handling
   implementation 'com.google.android.gms:play-services-auth:21.2.0'
   }
   ```
   - **Credential Manager:** Handles the core identity orchestration and UI for account selection.
   - **GoogleID Library:** Specifically provides `GetGoogleIdOption` for retrieving `OpenID` Connect tokens.
   - **Play Services Auth:** Required to maintain compatibility and request the `GAMES_LITE` scope for legacy `Player ID` retrieval.
4. When the player taps the SiWG button and selects a Google Account, the game
   must retrieve two distinct identifiers:

   - The `OpenID`, the primary identifier for binding the IGA.
   - The Play Games Services `Player ID`, retrieved by using the `GAMES_LITE` scope, to look up the player's IGA in your backend system and perform the binding.
5. In subsequent game launches, players can access their IGA by the SiWG flow,
   without requiring games to use `Player ID` as a primary identifier.

You can perform step 4 using a game client-side implementation.

1. The developer calls Android Credential Manager API to sign the user in with a Google Account.
2. After the user completes SiwG and selects a Google Account, the developer receives a result object, containing the ID token, the email address.
3. The developer constructs an Account object from the email address.
4. The developer calls the Authorization API with the `GAMES_LITE` scope and the Account.
5. If the account has a pre-existing grant on the `GAMES_LITE` scope, the Authorization API returns a token directly in the response object.
   1. Use the response token to call Play Games Services servers and retrieve Play Games Services `Player ID`.
   2. The developer verifies if the Play Games Services `Player ID` was linked with an in-game account.
      1. The developer knows this is a returning user from Play Games Services v1.
   3. The developer can link the new gaia ID with the previous Play Games Services v1 account.
6. Or, if the account doesn't have a pre-existing grant on the `GAMES_LITE` scope, the Authorization API returns a PendingIntent.
   1. The developer knows the user doesn't have an existing account from Play Games Services v1.
   2. The developer can safely discard the PendingIntent without showing any UI.

### Option 2: For Games already binding IGA to OpenID

Developers in this group have the most straightforward migration path. If your
game's in-game account is already primarily bound to the OpenID, you only need
to perform the standard technical SDK migration from v1 to v2 as outlined in the
steps.

## Update automatic sign-in code

Replace the `PlayGamesClientConfiguration` initialization class with the
`PlayGamesPlatform.Instance.Authenticate()` class.
The initialization and activation of
[`PlayGamesPlatform`](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform)
is not required. Calling `PlayGamesPlatform.Instance.Authenticate()` fetches the
result of automatic sign-in.
For more information about the recommended authentication flow with Play Games Services v2
integration, see [User experience guideline for ideal authentication flow](https://developer.android.com/games/pgs/platform-authentication#ux-auth-guidelines).

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