---
title: https://developer.android.com/games/pgs/android/android-signin
url: https://developer.android.com/games/pgs/android/android-signin
source: md.txt
---

In order to access Google Play Games Services functionality, your game needs to provide the
authenticated player's account. This documentation describes how to
implement a seamless authentication experience in your game.

The Play Games Services v2 SDK brings a number of improvements that increase the
number of users authenticated into your game, and make development easier:

- Improvements for users:
  - After selecting a default account, users are authenticated without needing to interact with a prompt.
  - Users no longer need to download the Play Games App to authenticate with Play Games Services or create a new account.
  - Users can now manage their Play Games Services accounts for multiple games from a single page.
- Improvements for developers:
- Client code no longer needs to handle the authentication or sign-out flow, as login is automatically triggered when the game starts, and account management is handled in the OS settings.

> [!NOTE]
> **Note:** You must follow additional steps if you want to enable recall functionality. For more information, see [Integrate the PGS Recall API within
> your game](https://developer.android.com/games/pgs/recall/recall-setup).

## New client integration

This section shows how to do a new client integration with Play Games Services
Sign In v2.

> [!NOTE]
> **Note:** If you already have a client integration with v1, follow the instructions in [Migrate from v1 to v2](https://developer.android.com/games/pgs/android/migrate-to-v2) to migrate your integration.

### Add the dependency

Add the Play Game Services SDK dependency to your app's root-level
`build.gradle` file. If you are using Gradle, you can add or update the
dependency as follows:

    dependencies {
     implementation "com.google.android.gms:play-services-games-v2:+"
    }

### Define the project ID

To add the Play Games Services SDK project ID to your app, complete the
following steps:

1. In your app's `AndroidManifest.xml` file, add the following `<meta-data>`
   element and attributes to the `<application>` element:

       <manifest>
         <application>
           <meta-data android:name="com.google.android.gms.games.APP_ID"
                      android:value="@string/game_services_project_id"/>
         </application>
       </manifest>

   Define the String resource reference `@string/game_services_project_id`
   using your games' Game services project id as the value. Your Games services
   project id can be found under your game name in the *Configuration* page on
   the Google Play Console.
2. In your `res/values/strings.xml` file, add a string resource reference
   and set your project ID as the value. In Google Play Console, you can find your
   project ID under your game name in the **Configuration** page. For example:

       <!-- res/values/strings.xml -->
       <resources>
         <!-- Replace 0000000000 with your game's project id. Example value shown above.  -->
         <string translatable="false"  name="game_services_project_id"> 0000000000 </string>
       </resources>

### Initialize the SDK

Initialize Play Games SDK in the `onCreate(..)` callback of your `Application`
class.

    import com.google.android.gms.games.PlayGamesSdk;

    ...

    @Override
    public void onCreate(){
      super.onCreate();
      PlayGamesSdk.initialize(this);
    }

### Get the authentication result

When your game launches, it will always attempt to authenticate the user. To
authenticate the user, you must verify that the user successfully authenticated,
and then get their Player ID.

To verify the authentication attempt, call `GamesSignInClient.isAuthenticated()`
and use `addOnCompleteListener` to retrieve the results. For example:

    GamesSignInClient gamesSignInClient = PlayGames.getGamesSignInClient(getActivity());

    gamesSignInClient.isAuthenticated().addOnCompleteListener(isAuthenticatedTask -> {
      boolean isAuthenticated =
        (isAuthenticatedTask.isSuccessful() &&
         isAuthenticatedTask.getResult().isAuthenticated());

      if (isAuthenticated) {
        // Continue with Play Games Services
      } else {
        // Show a sign-in button to ask players to authenticate. Clicking it should
        // call GamesSignInClient.signIn().
      }
    });

> [!IMPORTANT]
> **Key Point:** If the authentication fails when the game launches, Play Games Services would retry authentication automatically. Play Games Services doesn't require a manual **Sign in** button to be implemented.

> [!NOTE]
> **Note:** You shouldn't store the player ID returned from the Android SDK in the game's backend, as it's possible for an untrusted device to tamper with it. Instead, you should [enable server-side API access](https://developer.android.com/games/pgs/android/server-access) and retrieve the player ID or other data with a server-side call directly from the game's backend.

### Prevent auto-triggered profile creation

You can disable auto-triggered profile creation prompts
through the manifest file. This allows users without a Play Games Services
profile to continue to load the game without being prompted to create a
Play Games Services profile.
For more information, see [Profile creation options](https://developer.android.com/games/pgs/signin#profile-creation-options).

To use this feature, ensure that the following conditions are met:

- No Play Games Services profile exists on any of the Google Accounts signed in on the device.
- Your game is integrated with the Play Games Services SDK `com.google.android.gms:play-services-games-v2:21.0.0` or higher.

To prevent the automatically triggered profile creation prompts, complete the
following steps:

1. In the `AndroidManifest.xml` file, add the
   `com.google.android.gms.games.SUPPRESS_GAME_PROFILE_CREATION` tag in the
   `<meta-data>` element and attributes to the `<application>` element:


   ```
   <application>
       ...
       <meta-data
           android:name="com.google.android.gms.games.SUPPRESS_GAME_PROFILE_CREATION"
           android:value="true" />
       ...
   </application>
   ```

   <br />

   Setting this flag to true informs Play Games Services that your game will
   handle the profile creation process. Consequently, the Play Games Services
   won't automatically display the profile creation user interface for users
   on the device who don't have an existing Play Games Services profile.
2. When you call any Play Games Services API, the
   [`GamesClientStatusCodes.SIGN_IN_REQUIRED`](https://developers.google.com/android/reference/com/google/android/gms/common/api/CommonStatusCodes#SIGN_IN_REQUIRED())
   status code indicates that the call failed because the user couldn't be
   automatically authenticated due to the absence of a Play Games Services
   profile.

   This allows users without a Play Games Services
   profile to proceed with your implemented authentication methods without
   immediately being prompted to create a Play Games Services profile.
   Profile creation can be initiated by calling
   [`GamesSignInService.signin()`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient#public-abstract-taskauthenticationresult-signin).

   > [!NOTE]
   > **Note:** For users who already have a profile but failed the initial authentication, Play Games Services attempts to authenticate them again when you call `GamesSignInService.signin()`.

   ```java
   import com.google.android.gms.games.PlayGames;
   ...

   // Get the achievements client using Play Games services.
   AchievementsClient achievementsClient = PlayGames.getAchievementsClient(getActivity());
   achievementsClient.getAchievementsIntent()
       .addOnFailureListener(
           new OnFailureListener() {
             @Override
             public void onFailure(@NonNull Exception exception) {
               int statusCode = ((ApiException) exception).getStatusCode();
               if (statusCode == GamesClientStatusCodes.SIGN_IN_REQUIRED) {
                 // SIGN_IN_REQUIRED: The user needs to sign in with Play Games Services.
                 // Call GamesSignInService.signin() to prompt for
                 // authentication at a suitable time which will trigger the
                 // profile creation UI.
                 // (e.g., after a tutorial). Use GamesSignInService.isAuthenticated() to check auth status.
               }
             }
           });
   ```

   > [!NOTE]
   > **Note:** When the `com.google.android.gms.games.SUPPRESS_GAME_PROFILE_CREATION` tag is enabled, automatic profile creation is disabled on the new devices, which in turn prevents the retrieval of `com.google.android.gms.games.PROFILELESS_RECALL_ENABLED` tokens. You must manually initiate the authentication process on the second device once a Play Games Services profile has been created.

3. After you add the suppression tag, use the `logcat` window to verify the
   addition. The `logcat` output contains a message similar to the following:
   "Game opted out of automatic profile creation prompt (using manifest)".