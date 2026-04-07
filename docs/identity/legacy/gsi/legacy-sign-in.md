---
title: https://developer.android.com/identity/legacy/gsi/legacy-sign-in
url: https://developer.android.com/identity/legacy/gsi/legacy-sign-in
source: md.txt
---

# Integrate Google Sign-In into your Android app

| **Warning:**
|
| **The Google Sign-In for Android API is outdated and no longer supported.** To ensure the continued security and usability of your app,[migrate your Sign in with Google implementation to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager-siwg)today. Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.
|
| **For Wear developers:**Credential Manager is supported in Wear OS 5.1 and later on selected watches. Developers actively supporting Wear OS 3, 4 and 5.0 devices with Sign in with Google should continue using Google Sign-in for Android for your Wear applications. Sign in with Google support will be available on Credential Manager APIs for these versions of WearOS at a later date.

To integrate Google Sign-In into your Android app, configure Google Sign-In and add a button to your app's layout that starts the sign-in flow.

## Before you begin

Configure a Google Cloud console project and set up your Android Studio project.

## Configure Google Sign-in and the GoogleSignInClient object

1. In your sign-in activity's`onCreate`method, configure Google Sign-in to request the user data required by your app. For example, to configure Google Sign-in to request users' ID and basic profile information, create a[`GoogleSignInOptions`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInOptions.Builder.html#GoogleSignInOptions.Builder())object with the`DEFAULT_SIGN_IN`parameter. To request users' email addresses as well, create the`GoogleSignInOptions`object with the`requestEmail`option.

       // Configure sign-in to request the user's ID, email address, and basic
       // profile. ID and basic profile are included in DEFAULT_SIGN_IN.
       GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
               .requestEmail()
               .build();

   If you need to request additional scopes to access Google APIs, specify them with[`requestScopes`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInOptions.Builder.html#requestScopes(com.google.android.gms.common.api.Scope,com.google.android.gms.common.api.Scope...)). For the best user experience, on sign-in, only request the scopes that are required for your app to minimally function. Request any additional scopes only when you need them, so that your users see the consent screen in the context of an action they performed. See[Requesting Additional Scopes](https://developers.google.com/identity/sign-in/android/additional-scopes).
2. Then, also in your sign-in activity's`onCreate`method, create a`GoogleSignInClient`object with the options you specified.

       // Build a GoogleSignInClient with the options specified by gso.
       mGoogleSignInClient = GoogleSignIn.getClient(this, gso);

## Check for an existing signed-in user

In your activity's`onStart`method, check if a user has already signed in to your app with Google.  

    // Check for existing Google Sign In account, if the user is already signed in
    // the GoogleSignInAccount will be non-null.
    GoogleSignInAccount account = GoogleSignIn.getLastSignedInAccount(this);
    updateUI(account);

If`GoogleSignIn.getLastSignedInAccount`returns a`GoogleSignInAccount`object (rather than`null`), the user has already signed in to your app with Google. Update your UI accordingly---that is, hide the sign-in button, launch your main activity, or whatever is appropriate for your app.

If`GoogleSignIn.getLastSignedInAccount`returns`null`, the user has not yet signed in to your app with Google. Update your UI to display the Google Sign-in button.
| **Note:** If you need to detect changes to a user's auth state that happen outside your app, such as access token or ID token revocation, or to perform cross-device sign-in, you might also call`GoogleSignInClient.silentSignIn`when your app starts.

## Add the Google Sign-in button to your app

1. ![A blue button with a white 'G' logo and the text 'Sign in with Google'](https://developer.android.com/static/identity/legacy/gsi/images/btn_google_signin_light_normal_web.png)

   Add the[`SignInButton`](https://developers.google.com/android/reference/com/google/android/gms/common/SignInButton)in your application's layout:  

       <com.google.android.gms.common.SignInButton
        android:id="@+id/sign_in_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

2. **Optional** : If you are using the default sign-in button graphic instead of providing your own sign-in button assets, you can customize the button's size with the[`setSize`](https://developers.google.com/android/reference/com/google/android/gms/common/SignInButton.html#setSize(int))method.

       // Set the dimensions of the sign-in button.
       SignInButton signInButton = findViewById(R.id.sign_in_button);
       signInButton.setSize(SignInButton.SIZE_STANDARD);

3. In the Android activity (for example, in the`onCreate`method), register your button's`OnClickListener`to sign in the user when clicked:

       findViewById(R.id.sign_in_button).setOnClickListener(this);

## Start the sign-in flow

1. ![Google's account selection screen showing a list of accounts to choose for sign-in](https://developer.android.com/static/identity/legacy/gsi/images/choose-account.png)In the activity's`onClick`method, handle sign-in button taps by creating a sign-in intent with the[`getSignInIntent`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInClient#getSignInIntent())method, and starting the intent with`startActivityForResult`.

       @Override
       public void onClick(View v) {
           switch (v.getId()) {
               case R.id.sign_in_button:
                   signIn();
                   break;
               // ...
           }
       }

       private void signIn() {
           Intent signInIntent = mGoogleSignInClient.getSignInIntent();
           startActivityForResult(signInIntent, RC_SIGN_IN);
       }

   Starting the intent prompts the user to select a Google Account to sign in with. If you requested scopes beyond`profile`,`email`, and`openid`, the user is also prompted to grant access to the requested resources.
2. After the user signs in, you can get a[`GoogleSignInAccount`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount.html)object for the user in the activity's`onActivityResult`method.

       @Override
       public void onActivityResult(int requestCode, int resultCode, Intent data) {
           super.onActivityResult(requestCode, resultCode, data);

           // Result returned from launching the Intent from GoogleSignInClient.getSignInIntent(...);
           if (requestCode == RC_SIGN_IN) {
               // The Task returned from this call is always completed, no need to attach
               // a listener.
               Task<GoogleSignInAccount> task = GoogleSignIn.getSignedInAccountFromIntent(data);
               handleSignInResult(task);
           }
       }

   The`GoogleSignInAccount`object contains information about the signed-in user, such as the user's name.  

       private void handleSignInResult(Task<GoogleSignInAccount> completedTask) {
           try {
               GoogleSignInAccount account = completedTask.getResult(ApiException.class);

               // Signed in successfully, show authenticated UI.
               updateUI(account);
           } catch (ApiException e) {
               // The ApiException status code indicates the detailed failure reason.
               // Please refer to the GoogleSignInStatusCodes class reference for more information.
               Log.w(TAG, "signInResult:failed code=" + e.getStatusCode());
               updateUI(null);
           }
       }

   You can also get the user's email address with[`getEmail`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount.html#getEmail()), the user's Google ID (for client-side use) with[`getId`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount.html#getId()), and an ID token for the user with[`getIdToken`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount.html#getIdToken()). If you need to pass the signed-in user to a backend server,[send the ID token to your backend server](https://developers.google.com/identity/sign-in/android/backend-auth)and validate the token on the server.