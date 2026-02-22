---
title: https://developer.android.com/games/pgs/android/android-signin
url: https://developer.android.com/games/pgs/android/android-signin
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
| documentation](https://developer.android.com/games/pgs/v1/android/signin).

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

| **Note:** You must follow additional steps if you want to enable recall functionality. For more information, see [Integrate the PGS Recall API within
| your game](https://developer.android.com/games/pgs/recall/recall-setup).

## New client integration

This section shows how to do a new client integration with Play Games Services
Sign In v2.
| **Note:** If you already have a client integration with v1, follow the instructions in [Migrate from v1 to v2](https://developer.android.com/games/pgs/android/migrate-to-v2) to migrate your integration.

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

To verify the authentication attempt, call `GamesSignInClient.isAuthenticated()` and
use `addOnCompleteListener` to retrieve the results. For example:

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

If the user chooses not to get authenticated when the game launches, it is
recommended that you continue showing a button with the Play Games icon or
present the user with a sign-in screen that has a button with the Play Games
icon as one of the authentication options, and attempt to authenticate the user
again by calling `GamesSignInClient.signIn()` if the user presses the button.
After verifying that the user is authenticated, you can retrieve the Player ID
to identify the user. For example:

    PlayGames.getPlayersClient(activity).getCurrentPlayer().addOnCompleteListener(mTask -> {
        // Get PlayerID with mTask.getResult().getPlayerId()
      }
    );

| **Note:** You should not store the player ID returned from the Android SDK in the game's backend, as it's possible for an untrusted device to tamper with it. Instead, you should [enable server-side API access](https://developer.android.com/games/pgs/android/server-access) and retrieve the player ID or other data with a server-side call directly from the game's backend.