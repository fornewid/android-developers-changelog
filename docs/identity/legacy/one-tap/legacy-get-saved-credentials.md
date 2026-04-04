---
title: https://developer.android.com/identity/legacy/one-tap/legacy-get-saved-credentials
url: https://developer.android.com/identity/legacy/one-tap/legacy-get-saved-credentials
source: md.txt
---

# Sign users in with their saved credentials

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app,[migrate to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

Use the One Tap sign-in client to request permission from the user to retrieve one of the credentials they previously used to sign in to your app. These credentials can be either a Google Account or a username-password combination they saved with Google using Chrome, Android autofill or Smart Lock for Passwords.

![One-tap sign-in UI](https://developer.android.com/identity/legacy/one-tap/images/multi_account_sign-in.png)

When credentials are successfully retrieved, you can use them to frictionlessly sign the user in to your app.

If the user hasn't saved any credentials, no UI is presented, and you can provide your normal signed-out experience.

## Where should I use One Tap sign-in?

If your app requires users to sign in, display the One Tap UI on your sign-in screen. This can be helpful even if you already have a "Sign in with Google" button: because the One Tap UI can be configured to show only credentials the user previously used to sign-in, it can be a reminder to users who infrequently sign in how they signed in last time, and prevent them from accidentally creating new accounts with your app.

If sign-in is optional for your app, consider using One Tap sign-in on any screen that has an experience enhanced by signing in. For example, if users can browse content with your app while signed out, but can only post comments or add items to a shopping cart after signing in, that would be a sensible context for One Tap sign-in.

Sign-in optional apps should also use One Tap sign-in on their sign-in screens, for the reasons stated above.

## Before you begin

- Set up your Google APIs console project and Android project as described in[Get started with One Tap sign-in](https://developer.android.com/identity/legacy/one-tap/legacy-get-started).
- If you support password-based sign-in,[optimize your app for autofill](https://developer.android.com/guide/topics/text/autofill-optimize)(or use Smart Lock for Passwords) so users can save their password credentials after signing in.

## 1. Configure the One Tap sign-in client

You can configure the One Tap sign-in client to sign users in with saved passwords, saved Google Accounts, or either. (Supporting both is recommended, to enable one-tap account creation for new users and automatic or one-tap sign-in for as many returning users as possible.)

If your app uses password-based sign-in, use`setPasswordRequestOptions()`to enable password credential requests.

If your app uses Google Sign-in, use`setGoogleIdTokenRequestOptions()`to enable and configure Google ID token requests:

- Set the server client ID to[the ID you created in the Google APIs console](https://developer.android.com/identity/legacy/one-tap/legacy-get-started#api-console). Note this is your server's client ID, not your Android client ID.

- Configure the client to filter by authorized accounts. When you enable this option, the One Tap client only prompts users to sign in to your app with Google Accounts they've already used in the past. Doing so can help users sign in successfully when they're not sure if they already have an account or which Google Account they used, and prevents users from accidentally creating new accounts with your app.

- If you want to sign users in automatically when possible, enable the feature with`setAutoSelectEnabled()`. Automatic sign-in is possible when the following criteria are met:

  - The user has exactly one credential saved for your app. That is, one saved password or one saved Google Account.
  - The user hasn't disabled automatic sign-in in their[Google Account settings](https://passwords.google.com/options).
- While optional, we recommend that you strongly consider using a nonce to improve sign-in security and avoid replay attacks. Use[setNonce](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/BeginSignInRequest.GoogleIdTokenRequestOptions.Builder#parameters_2)to include a nonce in each request. See SafetyNet's[Obtain a nonce](https://developer.android.com/training/safetynet/attestation#obtain-nonce)section for suggestions and additional detail on generating a nonce.

### Java

```java
public class YourActivity extends AppCompatActivity {
  // ...

  private SignInClient oneTapClient;
  private BeginSignInRequest signInRequest;

  @Override
  public void onCreate(@Nullable Bundle savedInstanceState,
                       @Nullable PersistableBundle persistentState) {
      super.onCreate(savedInstanceState, persistentState);

      oneTapClient = Identity.getSignInClient(this);
      signInRequest = BeginSignInRequest.builder()
              .setPasswordRequestOptions(PasswordRequestOptions.builder()
                      .setSupported(true)
                      .build())
              .setGoogleIdTokenRequestOptions(GoogleIdTokenRequestOptions.builder()
                      .setSupported(true)
                      // Your server's client ID, not your Android client ID.
                      .setServerClientId(getString(R.string.default_web_client_id))
                      // Only show accounts previously used to sign in.
                      .setFilterByAuthorizedAccounts(true)
                      .build())
              // Automatically sign in when exactly one credential is retrieved.
              .setAutoSelectEnabled(true)
              .build();
      // ...
  }
  // ...
}
```

### Kotlin

```kotlin
class YourActivity : AppCompatActivity() {
    // ...

    private lateinit var oneTapClient: SignInClient
    private lateinit var signInRequest: BeginSignInRequest

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        oneTapClient = Identity.getSignInClient(this)
        signInRequest = BeginSignInRequest.builder()
            .setPasswordRequestOptions(BeginSignInRequest.PasswordRequestOptions.builder()
                .setSupported(true)
                .build())
            .setGoogleIdTokenRequestOptions(
                BeginSignInRequest.GoogleIdTokenRequestOptions.builder()
                    .setSupported(true)
                    // Your server's client ID, not your Android client ID.
                    .setServerClientId(getString(R.string.your_web_client_id))
                    // Only show accounts previously used to sign in.
                    .setFilterByAuthorizedAccounts(true)
                    .build())
            // Automatically sign in when exactly one credential is retrieved.
            .setAutoSelectEnabled(true)
            .build()
        // ...
    }
    // ...
}
```

## 2. Check for a signed-in user

If your Activity could be used by a signed-in user or a signed-out user, check the user's status before displaying the One Tap sign-in UI.

You should also keep track of whether the user has already declined to use One Tap sign-in by either closing the prompt or tapping outside of it. This can be as simple as a boolean property of your Activity. (See[Stop displaying the One Tap UI](https://developer.android.com/identity/legacy/one-tap/legacy-get-saved-credentials#disable-one-tap), below.)

## 3. Display the One Tap sign-in UI

If the user isn't signed in and hasn't already declined to use One Tap sign-in, call the client object's`beginSignIn()`method, and attach listeners to the`Task`it returns. Apps typically do this in the Activity's`onCreate()`method or after screen transitions when using a single-Activity architecture.

The One Tap client will call the success listener if the user has any saved credentials for your app. In the success listener, get the pending intent from the`Task`result and pass it to`startIntentSenderForResult()`to start the One Tap sign-in UI.

If the user doesn't have any saved credentials, the One Tap client will call the failure listener. In this case, no action is necessary: you can simply continue presenting the app's signed-out experience. However, if you support One Tap sign-up, you could start that flow here for a seamless account creation experience. See[Create new accounts with one tap](https://developer.android.com/identity/legacy/one-tap/create-new-accounts).  

### Java

    oneTapClient.beginSignIn(signUpRequest)
            .addOnSuccessListener(this, new OnSuccessListener<BeginSignInResult>() {
                @Override
                public void onSuccess(BeginSignInResult result) {
                    try {
                        startIntentSenderForResult(
                                result.getPendingIntent().getIntentSender(), REQ_ONE_TAP,
                                null, 0, 0, 0);
                    } catch (IntentSender.SendIntentException e) {
                        Log.e(TAG, "Couldn't start One Tap UI: " + e.getLocalizedMessage());
                    }
                }
            })
            .addOnFailureListener(this, new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // No saved credentials found. Launch the One Tap sign-up flow, or
                    // do nothing and continue presenting the signed-out UI.
                    Log.d(TAG, e.getLocalizedMessage());
                }
            });

### Kotlin

    oneTapClient.beginSignIn(signInRequest)
        .addOnSuccessListener(this) { result ->
            try {
                startIntentSenderForResult(
                    result.pendingIntent.intentSender, REQ_ONE_TAP,
                    null, 0, 0, 0, null)
            } catch (e: IntentSender.SendIntentException) {
                Log.e(TAG, "Couldn't start One Tap UI: ${e.localizedMessage}")
            }
        }
        .addOnFailureListener(this) { e ->
            // No saved credentials found. Launch the One Tap sign-up flow, or
            // do nothing and continue presenting the signed-out UI.
            Log.d(TAG, e.localizedMessage)
        }

## 4. Handle the user's response

The user's response to the One Tap sign-in prompt will be reported to your app using your Activity's`onActivityResult()`method. If the user chose to sign in, the result will be a saved credential. If the user declined to sign in, either by closing the One Tap UI or tapping outside it, the result will return with the code`RESULT_CANCELED`. Your app needs to handle both possibilities.

### Sign in with retrieved credentials

If the user chose to share credentials with your app, you can retrieve them by passing the intent data from`onActivityResult()`to the One Tap client's`getSignInCredentialFromIntent()`method. The credential will have a non-null`googleIdToken`property if the user shared a Google Account credential with your app, or a non-null`password`property if the user shared a saved password.

Use the credential to authenticate with your app's backend.

- If a username and password pair was retrieved, use them to sign in the same way you would if the user had manually supplied them.
- If Google Account credentials were retrieved, use the ID token to authenticate with your backend. If you've chosen to use a nonce to help avoid replay attacks check the response value on your backend server. See[Authenticate with a backend using ID tokens](https://developer.android.com/identity/legacy/one-tap/idtoken-auth).

### Java

```java
public class YourActivity extends AppCompatActivity {

  // ...
  private static final int REQ_ONE_TAP = 2;  // Can be any integer unique to the Activity.
  private boolean showOneTapUI = true;
  // ...

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
      super.onActivityResult(requestCode, resultCode, data);

      switch (requestCode) {
          case REQ_ONE_TAP:
              try {
                  SignInCredential credential = oneTapClient.getSignInCredentialFromIntent(data);
                  String idToken = credential.getGoogleIdToken();
                  String username = credential.getId();
                  String password = credential.getPassword();
                  if (idToken !=  null) {
                      // Got an ID token from Google. Use it to authenticate
                      // with your backend.
                      Log.d(TAG, "Got ID token.");
                  } else if (password != null) {
                      // Got a saved username and password. Use them to authenticate
                      // with your backend.
                      Log.d(TAG, "Got password.");
                  }
              } catch (ApiException e) {
                  // ...
              }
              break;
      }
  }
}
```

### Kotlin

```kotlin
class YourActivity : AppCompatActivity() {

    // ...
    private val REQ_ONE_TAP = 2  // Can be any integer unique to the Activity
    private var showOneTapUI = true
    // ...

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        when (requestCode) {
             REQ_ONE_TAP -> {
                try {
                    val credential = oneTapClient.getSignInCredentialFromIntent(data)
                    val idToken = credential.googleIdToken
                    val username = credential.id
                    val password = credential.password
                    when {
                        idToken != null -> {
                            // Got an ID token from Google. Use it to authenticate
                            // with your backend.
                            Log.d(TAG, "Got ID token.")
                        }
                        password != null -> {
                            // Got a saved username and password. Use them to authenticate
                            // with your backend.
                            Log.d(TAG, "Got password.")
                        }
                        else -> {
                            // Shouldn't happen.
                            Log.d(TAG, "No ID token or password!")
                        }
                    }
                } catch (e: ApiException) {
                    // ...
                }
            }
        }
    }
    // ...
}
```

### Stop displaying the One Tap UI

If the user declined to sign in, the call to`getSignInCredentialFromIntent()`will throw an`ApiException`with a`CommonStatusCodes.CANCELED`status code. When this happens, you should temporarily disable the One Tap sign-in UI so you don't annoy your users with repeated prompts. The following example accomplishes this by setting a property on the Activity, which it uses to determine whether to offer the user One Tap sign-in; however, you could also save a value to`SharedPreferences`or use some other method.

It's important to implement your own rate limiting of One Tap sign-in prompts. If you don't, and a user cancels several prompts in a row, the One Tap client will not prompt the user for the next 24 hours.
**Note:** If you encounter this 24-hour cooldown period during development, you can reset the cooldown by clearing Google Play services' app storage. Alternatively, to toggle on/off this cooldown on a test device and/or emulator alike, simply go to the Dialer app and input the following code:`*#*#66382723#*#*`. Upon submission, there will be no feedback, but your dialer will clear all input and may close. The cooldown should be toggled off after this. To toggle it back on, input the same code again.  

### Java

```java
public class YourActivity extends AppCompatActivity {

  // ...
  private static final int REQ_ONE_TAP = 2;  // Can be any integer unique to the Activity.
  private boolean showOneTapUI = true;
  // ...

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
      super.onActivityResult(requestCode, resultCode, data);

      switch (requestCode) {
          case REQ_ONE_TAP:
              try {
                  // ...
              } catch (ApiException e) {
                  switch (e.getStatusCode()) {
                      case CommonStatusCodes.CANCELED:
                          Log.d(TAG, "One-tap dialog was closed.");
                          // Don't re-prompt the user.
                          showOneTapUI = false;
                          break;
                      case CommonStatusCodes.NETWORK_ERROR:
                          Log.d(TAG, "One-tap encountered a network error.");
                          // Try again or just ignore.
                          break;
                      default:
                          Log.d(TAG, "Couldn't get credential from result."
                                  + e.getLocalizedMessage());
                          break;
                  }
              }
              break;
      }
  }
}
```

### Kotlin

```kotlin
class YourActivity : AppCompatActivity() {

    // ...
    private val REQ_ONE_TAP = 2  // Can be any integer unique to the Activity
    private var showOneTapUI = true
    // ...

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        when (requestCode) {
            REQ_ONE_TAP -> {
                try {
                    // ...
                } catch (e: ApiException) {
                    when (e.statusCode) {
                        CommonStatusCodes.CANCELED -> {
                            Log.d(TAG, "One-tap dialog was closed.")
                            // Don't re-prompt the user.
                            showOneTapUI = false
                        }
                        CommonStatusCodes.NETWORK_ERROR -> {
                            Log.d(TAG, "One-tap encountered a network error.")
                            // Try again or just ignore.
                        }
                        else -> {
                            Log.d(TAG, "Couldn't get credential from result." +
                                " (${e.localizedMessage})")
                        }
                    }
                }
            }
        }
    }
    // ...
}
```

## 5. Handle sign-out

When a user signs out of your app, call the One Tap client's`signOut()`method. Calling`signOut()`disables automatic sign-in until the user signs in again.

Even if you don't use automatic sign-in, this step is important because it ensures that when users sign out of your app, the authentication state of any Play services APIs you use also get reset.

## Next steps

If you configured the One Tap client to retrieve Google credentials, your app can now get Google ID tokens that represent your users' Google Accounts. Learn how you can[use these tokens on the backend](https://developer.android.com/identity/legacy/one-tap/idtoken-auth).

If you support Google Sign-in, you can also use the One Tap client to[add frictionless account creation flows to your app](https://developer.android.com/identity/legacy/one-tap/create-new-accounts).