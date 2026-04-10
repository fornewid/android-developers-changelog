---
title: https://developer.android.com/games/pgs/android/migrate-to-v2
url: https://developer.android.com/games/pgs/android/migrate-to-v2
source: md.txt
---

This document describes how to migrate existing games from the [games v1
SDK](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/package-summary) to the [games v2 SDK](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary).

## Before you begin

You can use any preferred IDE, such as Android Studio, to migrate your game.
Complete the following steps before you migrate to games v2:

- [Download and install Android Studio](https://developer.android.com/codelabs/basic-android-kotlin-compose-install-android-studio)
- Your game must use the games v1 SDK

## Update the dependencies

1. In your module's `build.gradle` file, find this line in the module level
   dependencies.

   ```yaml
   implementation "com.google.android.gms:play-services-games:+"
   ```

   Replace it with the following code:

   ```yaml
   implementation "com.google.android.gms:play-services-games-v2:version"
   ```

   Replace <var translate="no">version</var> with the

   [latest version of the games SDK](https://mvnrepository.com/artifact/com.google.android.gms/play-services-games).
2. After you update the dependencies, ensure that you complete all the steps in
   this document.

## Define the project ID

To add the Play Games Services SDK project ID to your app, complete the
following steps:

1. In the `AndroidManifest.xml` file, add the following `<meta-data>`
   element and attributes to the `<application>` element:

       <manifest>
         <application>
           <meta-data android:name="com.google.android.gms.games.APP_ID"
                      android:value="@string/game_services_project_id"/>
         </application>
       </manifest>

   Define the String resource reference `@string/game_services_project_id`
   using your games' Game services project ID as the value. Your Games services
   project ID can be found under your game name in the **Configuration** page on
   the Google Play Console.
2. In the `res/values/strings.xml` file, add a string resource reference
   and set your project ID as the value. For example:

       <!-- res/values/strings.xml -->
       <resources>
         <!-- Replace 0000000000 with your game's project id. Example value shown above.  -->
         <string translatable="false"  name="game_services_project_id"> 0000000000 </string>
       </resources>

## Migrate from deprecated Google Sign-In

Replace the [`GoogleSignInClient`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInClient)
class with the [`GamesSignInClient`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient)
class.

### Java

Locate the files with `GoogleSignInClient` class.

    import com.google.android.gms.auth.api.signin.GoogleSignIn;
    import com.google.android.gms.auth.api.signin.GoogleSignInClient;
    import com.google.android.gms.auth.api.signin.GoogleSignInOptions;

    // ... existing code

    @Override
    public void onCreate(@Nullable Bundle bundle) {
        super.onCreate(bundle);

        // ... existing code

        GoogleSignInOptions signInOption =
    new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN).build();
        // Client used to sign in to Google services
        GoogleSignInClient googleSignInClient =
    GoogleSignIn.getClient(this, signInOptions);
    }

And update it to this:

    import com.google.android.gms.games.PlayGamesSdk;
    import com.google.android.gms.games.PlayGames;
    import com.google.android.gms.games.GamesSignInClient;

    // ... existing code

    @Override
    public void onCreate(){
        super.onCreate();
        PlayGamesSdk.initialize(this);
        // Client used to sign in to Google services
        GamesSignInClient gamesSignInClient =
    PlayGames.getGamesSignInClient(getActivity());
    }

### Kotlin

Locate the files with `GoogleSignInClient` class.

    import com.google.android.gms.auth.api.signin.GoogleSignIn
    import com.google.android.gms.auth.api.signin.GoogleSignInClient
    import com.google.android.gms.auth.api.signin.GoogleSignInOptions

    // ... existing code

    val signInOptions = GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN

    // ... existing code

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val googleSignInClient: GoogleSignInClient =
    GoogleSignIn.getClient(this, signInOptions)
    }

And update it to this:

    import com.google.android.gms.games.PlayGames
    import com.google.android.gms.games.PlayGamesSdk
    import com.google.android.gms.games.GamesSignInClient

    // ... existing code

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        PlayGamesSdk.initialize(this)
        // client used to sign in to Google services
        val gamesSignInClient: GamesSignInClient =
    PlayGames.getGamesSignInClient(this)
    }

### Update the `GoogleSignIn` code

[`GoogleSignIn`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignIn) API
is not supported in the games v2 SDK. Replace the `GoogleSignIn` API
code with the [`GamesSignInClient`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient) API as shown in the following example.

To request a server side access token, use the
[`GamesSignInClient.requestServerSideAccess()`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient) method.
For more information, see
[Update the server side access classes](https://developer.android.com/games/pgs/android/migrate-to-v2#request-access).

### Java

Locate the files with `GoogleSignIn` class.

    // Request code used when invoking an external activity.
    private static final int RC_SIGN_IN = 9001;

    private boolean isSignedIn() {
        GoogleSignInAccount account = GoogleSignIn.getLastSignedInAccount(this);
        GoogleSignInOptions signInOptions =
        GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN;
        return GoogleSignIn.hasPermissions(account, signInOptions.getScopeArray());
    }

    private void signInSilently() {
        GoogleSignInOptions signInOptions =
            GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN;
        GoogleSignInClient signInClient = GoogleSignIn.getClient(this, signInOptions);
        signInClient
            .silentSignIn()
            .addOnCompleteListener(
                this,
                task -> {
                if (task.isSuccessful()) {
                    // The signed-in account is stored in the task's result.
                    GoogleSignInAccount signedInAccount = task.getResult();
                    showSignInPopup();
                } else {
                    // Perform interactive sign in.
                    startSignInIntent();
                }
            });
    }

    private void startSignInIntent() {
        GoogleSignInClient signInClient = GoogleSignIn.getClient(this,
            GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN);
        Intent intent = signInClient.getSignInIntent();
        startActivityForResult(intent, RC_SIGN_IN);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == RC_SIGN_IN) {
            GoogleSignInResult result =
            Auth.GoogleSignInApi.getSignInResultFromIntent(data);
            if (result.isSuccess()) {
                // The signed-in account is stored in the result.
                GoogleSignInAccount signedInAccount = result.getSignInAccount();
                showSignInPopup();
            } else {
                String message = result.getStatus().getStatusMessage();
                if (message == null || message.isEmpty()) {
                    message = getString(R.string.signin_other_error);
            }
            new AlertDialog.Builder(this).setMessage(message)
                .setNeutralButton(android.R.string.ok, null).show();
            }
        }
    }

    private void showSignInPopup() {
    Games.getGamesClient(requireContext(), signedInAccount)
        .setViewForPopups(contentView)
        .addOnCompleteListener(
            task -> {
                if (task.isSuccessful()) {
                    logger.atInfo().log("SignIn successful");
                } else {
                    logger.atInfo().log("SignIn failed");
                }
            });
      }

And update it to this:

    private void signInSilently() {
        gamesSignInClient.isAuthenticated().addOnCompleteListener(isAuthenticatedTask -> {
        boolean isAuthenticated =
            (isAuthenticatedTask.isSuccessful() &&
                isAuthenticatedTask.getResult().isAuthenticated());
            if (isAuthenticated) {
                // Continue with Play Games Services
            } else {
                // If authentication fails, either disable Play Games Services
                // integration or
                // display a login button to prompt players to sign in.
                // Use`gamesSignInClient.signIn()` when the login button is clicked.
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        // When the activity is inactive, the signed-in user's state can change;
        // therefore, silently sign in when the app resumes.
        signInSilently();
    }

### Kotlin

Locate the files with `GoogleSignIn` class.

    // Request codes we use when invoking an external activity.
    private val RC_SIGN_IN = 9001

    // ... existing code

    private fun isSignedIn(): Boolean {
        val account = GoogleSignIn.getLastSignedInAccount(this)
        val signInOptions = GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN
        return GoogleSignIn.hasPermissions(account, *signInOptions.scopeArray)
    }

    private fun signInSilently() {
        val signInOptions = GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN
        val signInClient = GoogleSignIn.getClient(this, signInOptions)
        signInClient.silentSignIn().addOnCompleteListener(this) { task ->
            if (task.isSuccessful) {
                // The signed-in account is stored in the task's result.
                val signedInAccount = task.result
                // Pass the account to showSignInPopup.
                showSignInPopup(signedInAccount)
            } else {
                // Perform interactive sign in.
                startSignInIntent()
            }
        }
    }

    private fun startSignInIntent() {
        val signInClient = GoogleSignIn.getClient(this, GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
        val intent = signInClient.signInIntent
        startActivityForResult(intent, RC_SIGN_IN)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == RC_SIGN_IN) {
            val result = Auth.GoogleSignInApi.getSignInResultFromIntent(data)
            if (result.isSuccess) {
                // The signed-in account is stored in the result.
                val signedInAccount = result.signInAccount
                showSignInPopup(signedInAccount) // Pass the account to showSignInPopup.
            } else {
                var message = result.status.statusMessage
                if (message == null || message.isEmpty()) {
                    message = getString(R.string.signin_other_error)
            }
            AlertDialog.Builder(this)
                .setMessage(message)
                .setNeutralButton(android.R.string.ok, null)
                .show()
            }
        }
    }

    private fun showSignInPopup(signedInAccount: GoogleSignInAccount) {
        // Add signedInAccount parameter.
        Games.getGamesClient(this, signedInAccount)
            .setViewForPopups(contentView) // Assuming contentView is defined.
            .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                logger.atInfo().log("SignIn successful")
            } else {
                logger.atInfo().log("SignIn failed")
            }
        }
    }

And update it to this:

    private fun signInSilently() {
        gamesSignInClient.isAuthenticated.addOnCompleteListener { isAuthenticatedTask ->
            val isAuthenticated = isAuthenticatedTask.isSuccessful &&
            isAuthenticatedTask.result.isAuthenticated
            if (isAuthenticated) {
                // Continue with Play Games Services
            } else {
                // To handle a user who is not signed in, either disable Play Games Services integration
                // or display a login button. Selecting this button calls `gamesSignInClient.signIn()`.
            }
        }
    }

    override fun onResume() {
        super.onResume()
        // Since the state of the signed in user can change when the activity is
        // not active it is recommended to try and sign in silently from when the
        // app resumes.
        signInSilently()
    }

### Add the `GamesSignInClient` code

If the player is successfully authenticated, remove the Play Games Services sign-in
button from your game. If the user chooses not to authenticate when the game launches,
continue showing a button with the Play Games Services icon,
and start the login process with
[`GamesSignInClient.signIn()`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient).

### Java

    private void startSignInIntent() {
        gamesSignInClient
            .signIn()
            .addOnCompleteListener( task -> {
                if (task.isSuccessful() && task.getResult().isAuthenticated()) {
                    // sign in successful
                } else {
                    // sign in failed
                }
            });
      }

### Kotlin

    private fun startSignInIntent() {
        gamesSignInClient
            .signIn()
            .addOnCompleteListener { task ->
                if (task.isSuccessful && task.result.isAuthenticated) {
                    // sign in successful
                } else {
                    // sign in failed
                }
            }
      }

### Remove sign-out code

Remove the code for [`GoogleSignInClient.signOut`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInClient#public-taskvoid-signout).

Remove the code shown in the following example:

### Java

    // ... existing code

    private void signOut() {
        GoogleSignInClient signInClient = GoogleSignIn.getClient(this,
        GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN);
        signInClient.signOut().addOnCompleteListener(this,
        new OnCompleteListener() {
            @Override
            public void onComplete(@NonNull Task task) {
               // At this point, the user is signed out.
            }
        });
    }

### Kotlin

    // ... existing code

    private fun signOut() {
        val signInClient = GoogleSignIn.getClient(this, GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
        signInClient.signOut().addOnCompleteListener(this) {
        // At this point, the user is signed out.
        }
    }

### Check successful authentication

Include the following code to check if you have automatically authenticated and
add the custom logic if you have it available.

### Java

    private void checkIfAutomaticallySignedIn() {
    gamesSignInClient.isAuthenticated().addOnCompleteListener(isAuthenticatedTask -> {
    boolean isAuthenticated =
        (isAuthenticatedTask.isSuccessful() &&
        isAuthenticatedTask.getResult().isAuthenticated());

        if (isAuthenticated) {
            // Continue with Play Games Services
            // If your game requires specific actions upon successful sign-in,
            // you can add your custom logic here.
            // For example, fetching player data or updating UI elements.
        } else {
            // Show a login button to ask  players to sign-in. Clicking it should
            // call GamesSignInClient.signIn().
            }
        });
    }

### Kotlin

    private void checkIfAutomaticallySignedIn() {
    gamesSignInClient.isAuthenticated()
        .addOnCompleteListener { task ->
        val isAuthenticated = task.isSuccessful && task.result?.isAuthenticated ?: false

            if (isAuthenticated) {
                // Continue with Play Games Services
            } else {
                // Disable your integration or show a login button
            }
        }
    }

## Update client class names and methods

When you migrate to games v2, the methods used to get the client class names
are different.
Use the corresponding
[`PlayGames.getxxxClient()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayGames#public-method-summary)
methods instead of
[`Games.getxxxClient()`](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/Games#public-method-summary)
methods.

For example, for
[`LeaderboardsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient)
use `PlayGames.getLeaderboardsClient()` instead of the
`Games.getLeaderboardsClient()` method.

Remove any code related to the `GamesClient` and `GamesMetadataClient` classes
as we don't have any replacement classes in games v2.

### Java

Locate the code for `LeaderboardsClient`.

    import com.google.android.gms.games.LeaderboardsClient;
    import com.google.android.gms.games.Games;

    @Override
    public void onCreate(@Nullable Bundle bundle) {
        super.onCreate(bundle);
            // Get the leaderboards client using Play Games services.
        LeaderboardsClient leaderboardsClient = Games.getLeaderboardsClient(this,
            GoogleSignIn.getLastSignedInAccount(this));
    }

And update it to this:

    import com.google.android.gms.games.LeaderboardsClient;
    import com.google.android.gms.games.PlayGames;

     @Override
    public void onCreate(@Nullable Bundle bundle) {
        super.onCreate(bundle);
            // Get the leaderboards client using Play Games services.
            LeaderboardsClient leaderboardsClient = PlayGames.getLeaderboardsClient(getActivity());
    }

### Kotlin

Locate the code for `LeaderboardsClient`.

    import com.google.android.gms.games.LeaderboardsClient
    import com.google.android.gms.games.Games
    // Initialize the variables.
    private lateinit var leaderboardsClient: LeaderboardsClient

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        leaderboardsClient = Games.getLeaderboardsClient(this,
            GoogleSignIn.getLastSignedInAccount(this))
    }

And update it to this:

    import com.google.android.gms.games.LeaderboardsClient
    import com.google.android.gms.games.PlayGames
        // Initialize the variables.
    private lateinit var leaderboardsClient: LeaderboardsClient

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        leaderboardsClient = PlayGames.getLeaderboardsClient(this)
    }

Similarly, use the corresponding methods for the following clients:
`AchievementsClient`, `EventsClient`, `GamesSignInClient`,
`PlayerStatsClient`, `RecallClient`, `SnapshotsClient`, or `PlayersClient`.

## Update the server side access classes

To request a server side access token, use the
[`GamesSignInClient.requestServerSideAccess()`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient)
method instead of the
[`GoogleSignInAccount.getServerAuthCode()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount#getServerAuthCode())
method.

For more information, see
[Send the server auth code](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/package-summary).

The following example shows how to request a server side access token.

### Java

Locate the code for `GoogleSignInOptions` class.

        private static final int RC_SIGN_IN = 9001;
        private GoogleSignInClient googleSignInClient;

        private void startSignInForAuthCode() {
            /** Client ID for your backend server. */
            String webClientId = getString(R.string.webclient_id);
            GoogleSignInOptions signInOption = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
                .requestServerAuthCode(webClientId)
                .build();

            GoogleSignInClient signInClient = GoogleSignIn.getClient(this, signInOption);
            Intent intent = signInClient.getSignInIntent();
            startActivityForResult(intent, RC_SIGN_IN);
        }

        /** Auth code to send to backend server */
        private String mServerAuthCode;

        @Override
        protected void onActivityResult(int requestCode, int resultCode, Intent data) {
            super.onActivityResult(requestCode, resultCode, data);
            if (requestCode == RC_SIGN_IN) {
                GoogleSignInResult result = Auth.GoogleSignInApi.getSignInResultFromIntent(data);
            if (result.isSuccess()) {
                mServerAuthCode = result.getSignInAccount().getServerAuthCode();
            } else {
                String message = result.getStatus().getStatusMessage();
                if (message == null || message.isEmpty()) {
                    message = getString(R.string.signin_other_error);
                }
                new AlertDialog.Builder(this).setMessage(message)
                    .setNeutralButton(android.R.string.ok, null).show();
            }
          }
        }
      
And update it to this:

      private void startRequestServerSideAccess() {
          GamesSignInClient gamesSignInClient = PlayGames.getGamesSignInClient(this);
          gamesSignInClient
              .requestServerSideAccess(OAUTH_2_WEB_CLIENT_ID,
               /* forceRefreshToken= */ false, /* additional AuthScope */ scopes)
              .addOnCompleteListener(task -> {
                  if (task.isSuccessful()) {
                      AuthResponse authresp = task.getResult();
                      // Send the authorization code as a string and a
                      // list of the granted AuthScopes that were granted by the
                      // user. Exchange for an access token.
                      // Verify the player with Play Games Services REST APIs.
                  } else {
                    // Authentication code retrieval failed.
                  }
            });
      }
      
### Kotlin

Locate the code for `GoogleSignInOptions` class.

      // ... existing code

      private val RC_SIGN_IN = 9001
      private lateinit var googleSignInClient: GoogleSignInClient

      // Auth code to send to backend server.
      private var mServerAuthCode: String? = null

      private fun startSignInForAuthCode() {
          // Client ID for your backend server.
          val webClientId = getString(R.string.webclient_id)

          val signInOption = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_GAMES_SIGN_IN)
              .requestServerAuthCode(webClientId)
              .build()

          googleSignInClient = GoogleSignIn.getClient(this, signInOption)
          val intent = googleSignInClient.signInIntent
          startActivityForResult(intent, RC_SIGN_IN)
      }

      override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
          super.onActivityResult(requestCode, resultCode, data)
          if (requestCode == RC_SIGN_IN) {
              val result = Auth.GoogleSignInApi.getSignInResultFromIntent(data)
              if (result.isSuccess) {
                  mServerAuthCode = result.signInAccount.serverAuthCode
              } else {
                  var message = result.status.statusMessage
                  if (message == null || message.isEmpty()) {
                      message = getString(R.string.signin_other_error)
                  }
                  AlertDialog.Builder(this).setMessage(message)
                      .setNeutralButton(android.R.string.ok, null).show()
                }
            }
      }
      
And update it to this:

      private void startRequestServerSideAccess() {
      GamesSignInClient gamesSignInClient = PlayGames.getGamesSignInClient(this);
          gamesSignInClient
              .requestServerSideAccess(OAUTH_2_WEB_CLIENT_ID, /* forceRefreshToken= */ false,
              /* additional AuthScope */ scopes)
              .addOnCompleteListener(task -> {
                  if (task.isSuccessful()) {
                      AuthResponse authresp = task.getResult();
                      // Send the authorization code as a string and a
                      // list of the granted AuthScopes that were granted by the
                      // user. Exchange for an access token.
                      // Verify the player with Play Games Services REST APIs.
                  } else {
                    // Authentication code retrieval failed.
                  }
            });
      }
      
## Migrate from GoogleApiClient

For older existing integrations your game may be depending on the
`GoogleApiClient` API variation of the Play Games Services SDK. This was
[deprecated in late 2017](https://android-developers.googleblog.com/2017/11/moving-past-googleapiclient_21.html)
and replaced by "connectionless" clients.
To migrate you can replace the `GoogleApiClient` class with a "connectionless"
equivalent.
The following table lists the common class mappings from games v1 to games v2:

<br />

| games v2 (Current) | games v1 (Legacy) |
| games v2 (Current) | games v1 (Legacy) |
|---|---|
| com.google.android.gms.games.AchievementsClient | com.google.android.gms.games.achievement.Achievements |
| com.google.android.gms.games.LeaderboardsClient | com.google.android.gms.games.leaderboard.Leaderboard |
| com.google.android.gms.games.SnapshotsClient | com.google.android.gms.games.snapshot.Snapshots |
| com.google.android.gms.games.PlayerStatsClient | com.google.android.gms.games.stats.PlayerStats |
| com.google.android.gms.games.PlayersClient | com.google.android.gms.games.Players |
| com.google.android.gms.games.GamesClientStatusCodes | com.google.android.gms.games.GamesStatusCodes |

<br />

## Build and run the game


To build and run on Android Studio,
see [Build and run your app](https://developer.android.com/studio/run).

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

Complete the following steps after you have migrated to games v2.

### Publish the game

Build the APK(s) and publish the game in the Play Console.

1. In the Android Studio menu, select **Build \> Build Bundles(s) / APK(s) \> Build APK(s)**.
2. Publish your game. For more information, see [Publish private apps from the Play Console](https://support.google.com/googleplay/work/answer/6145139).