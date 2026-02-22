---
title: https://developer.android.com/identity/legacy/one-tap/idtoken-auth
url: https://developer.android.com/identity/legacy/one-tap/idtoken-auth
source: md.txt
---

# Authenticate with a backend using ID tokens

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app,[migrate to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

The One Tap sign-in client retrieves a Google ID token when the user selects a Google Account. An ID token is a signed assertion of a user's identity that also contains a user's basic profile information, possibly including an email address that has been verified by Google.

When ID tokens are available, you can use them to securely authenticate with your app's backend, or to automatically sign up the user for a new account without the need to verify the user's email address.

To sign in or sign up a user with an ID token, send the token to your app's backend. On the backend, verify the token using either a Google API client library or a general-purpose JWT library. If the user hasn't signed in to your app with this Google Account before, create a new account.

If you've optionally chosen to use a nonce to help avoid replay attacks, use[getNonce](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/GetSignInIntentRequest#public-string-getnonce)to send it along with the ID Token to your backend server, and check for the expected value. We recommend that you strongly consider using a nonce to improve user safety and security.

## Get an ID token from the credentials object

After you retrieve a user's credentials, check if the credentials object includes an ID token. If it does, send it to your backend.  

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