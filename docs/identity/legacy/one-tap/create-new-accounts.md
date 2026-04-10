---
title: https://developer.android.com/identity/legacy/one-tap/create-new-accounts
url: https://developer.android.com/identity/legacy/one-tap/create-new-accounts
source: md.txt
---

# Create new accounts with one tap

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app,[migrate to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

If you support signing in with Google Accounts, you can use the One Tap sign-in client to also give your users a frictionless account creation experience that never takes them out of the context of your app.

![One-tap sign-up UI](https://developer.android.com/identity/legacy/one-tap/images/sign-up.png)

When you display the One Tap UI, users are prompted to create a new account with your app using one of the Google Accounts on their device. If the user chooses to continue, you get an ID token with basic profile information---their name, profile photo, and their verified email address---which you can use to create the new account.

Implementing One Tap account creation has two parts:

- Integrating the One Tap client into your app, which is described on this page. This is mostly the same as using One Tap sign-in, but with some differences in configuration.
- Adding to your backend the ability to create user accounts from Google ID tokens, which is discussed in[Using ID tokens on the backend](https://developer.android.com/identity/legacy/one-tap/idtoken-auth).

## Where should I use One Tap sign-up?

The most impactful place to offer One Tap sign-up to users is in a context where signing in would enable new features. First, try to sign the user in with a saved credential. If no saved credentials are found, offer to create a new account for the user.

## Before you begin

Set up your Google APIs console project and Android project as described in[Get started with One Tap sign-in](https://developer.android.com/identity/legacy/one-tap/legacy-get-started).

## 1. Configure the One Tap client

To configure the One Tap client for account creation, do the following:

- Do not enable password credential requests. (One-tap sign-up is only possible with token-based authentication.)
- Enable Google ID token requests using`setGoogleIdTokenRequestOptions()`and these settings:

  - Set the server client ID to[the ID you created in the Google APIs console](https://developer.android.com/identity/legacy/one-tap/legacy-get-started#api-console). Note this is your server's client ID, not your Android client ID.
  - Configure the client to show all Google Accounts on the device---that is, don't filter by authorized accounts.
  - Optionally, you can also[request the verified phone number](https://developer.android.com/android/reference/com/google/android/gms/auth/api/identity/BeginSignInRequest.GoogleIdTokenRequestOptions.Builder#public-beginsigninrequest.googleidtokenrequestoptions.builder-setrequestverifiedphonenumber-boolean-requestverifiedphonenumber)for the account.

### Java

```java
public class YourActivity extends AppCompatActivity {

  // ...

  private SignInClient oneTapClient;
  private BeginSignInRequest signUpRequest;

  @Override
  public void onCreate(@Nullable Bundle savedInstanceState,
                       @Nullable PersistableBundle persistentState) {
      super.onCreate(savedInstanceState, persistentState);

      oneTapClient = Identity.getSignInClient(this);
      signUpRequest = BeginSignInRequest.builder()
              .setGoogleIdTokenRequestOptions(GoogleIdTokenRequestOptions.builder()
                      .setSupported(true)
                      // Your server's client ID, not your Android client ID.
                      .setServerClientId(getString(R.string.your_web_client_id))
                      // Show all accounts on the device.
                      .setFilterByAuthorizedAccounts(false)
                      .build())
              .build();

      // ...
  }
}
```

### Kotlin

```kotlin
class YourActivity : AppCompatActivity() {
    // ...

    private lateinit var oneTapClient: SignInClient
    private lateinit var signUpRequest: BeginSignInRequest

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        oneTapClient = Identity.getSignInClient(this)
        signUpRequest = BeginSignInRequest.builder()
            .setGoogleIdTokenRequestOptions(
                BeginSignInRequest.GoogleIdTokenRequestOptions.builder()
                    .setSupported(true)
                    // Your server's client ID, not your Android client ID.
                    .setServerClientId(getString(R.string.your_web_client_id))
                    // Show all accounts on the device.
                    .setFilterByAuthorizedAccounts(false)
                    .build())
            .build()
        // ...
    }
    // ...
}
```

## 2. Keep track of One Tap UI cancellation

You should keep track of whether the user has already declined to use One Tap sign-up by either closing the prompt or tapping outside of it. This can be as simple as a boolean property of your Activity. (See[Stop displaying the One Tap UI](https://developer.android.com/identity/legacy/one-tap/create-new-accounts#disable-one-tap), below.)

## 3. Display the One Tap sign-up UI

If the user hasn't declined to use One Tap to create a new account, call the client object's`beginSignIn()`method, and attach listeners to the`Task`it returns. Apps typically do this step when a One Tap sign-in request doesn't find any saved credentials---that is, in the failure listener of the sign-*in*request.

The One Tap client will call the success listener if the user has one or more Google Accounts set up on the device. In the success listener, get the pending intent from the`Task`result and pass it to`startIntentSenderForResult()`to start the One Tap UI.

If the user doesn't have any Google Accounts on the device, the One Tap client will call the failure listener. In this case, no action is necessary: you can simply continue presenting the app's signed-out experience, and the user can sign up with your normal account creation flow.  

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
                    // No Google Accounts found. Just continue presenting the signed-out UI.
                    Log.d(TAG, e.getLocalizedMessage());
                }
            });

### Kotlin

    oneTapClient.beginSignIn(signUpRequest)
        .addOnSuccessListener(this) { result ->
            try {
                startIntentSenderForResult(
                    result.pendingIntent.intentSender, REQ_ONE_TAP,
                    null, 0, 0, 0)
            } catch (e: IntentSender.SendIntentException) {
                Log.e(TAG, "Couldn't start One Tap UI: ${e.localizedMessage}")
            }
        }
        .addOnFailureListener(this) { e ->
            // No Google Accounts found. Just continue presenting the signed-out UI.
            Log.d(TAG, e.localizedMessage)
        }

## 4. Handle the user's response

The user's response to the One Tap sign-up prompt will be reported to your app using your Activity's`onActivityResult()`method. If the user chose to create an account, the result will be a Google ID token. If the user declined to sign up, either by closing the One Tap UI or tapping outside it, the result will return with the code`RESULT_CANCELED`. Your app needs to handle both possibilities.

### Create an account with a Google ID token

If the user chose to sign up with a Google Account, you can get an ID token for the user by passing the intent data from`onActivityResult()`to the One Tap client's`getSignInCredentialFromIntent()`method. The credential will have a non-null`googleIdToken`property.

Use the ID token to create an account on your backend (see[Authenticate with a backend using ID tokens](https://developer.android.com/identity/legacy/one-tap/idtoken-auth)) and sign the user in.

The credential also contains any additional details you have requested, such as the account's verified phone number if available.  

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
                  if (idToken !=  null) {
                      // Got an ID token from Google. Use it to authenticate
                      // with your backend.
                      Log.d(TAG, "Got ID token.");
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
                    when {
                        idToken != null -> {
                            // Got an ID token from Google. Use it to authenticate
                            // with your backend.
                            Log.d(TAG, "Got ID token.")
                        }
                        else -> {
                            // Shouldn't happen.
                            Log.d(TAG, "No ID token!")
                        }
                    }
                } catch (e: ApiException) {
                    // ...
            }
        }
    }
    // ...
}
```

### Stop displaying the One Tap UI

If the user declined to sign in, the call to`getSignInCredentialFromIntent()`will throw an`ApiException`with a`CommonStatusCodes.CANCELED`status code. When this happens, you should temporarily stop displaying the One Tap sign-in UI so you don't annoy your users with repeated prompts. The following example accomplishes this by setting a property on the Activity, which it uses to determine whether to offer the user One Tap sign-in; however, you could also save a value to`SharedPreferences`or use some other method.

It's important to implement your own rate limiting of One Tap sign-in prompts. If you don't, and a user cancels several prompts in a row, the One Tap client will not prompt the user for the next 24 hours.
**Note:** If you encounter this 24-hour cooldown period during development, you can reset the cooldown by clearing Google Play services' app storage.  

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

## Next steps

When a user completes the One Tap sign-up flow, you get a Google ID token, which includes some basic profile information: the user's email address, full name, and profile picture URL. For many apps, this information is enough for you to[authenticate the user on backend](https://developer.android.com/identity/legacy/one-tap/idtoken-auth)and create a new account.

If you require additional information to complete account creation---for instance, the user's birth date---present the user with a sign-up details flow, where you request this additional info. Then, send it to your backend to complete account creation.