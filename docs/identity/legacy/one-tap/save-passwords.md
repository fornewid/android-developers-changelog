---
title: https://developer.android.com/identity/legacy/one-tap/save-passwords
url: https://developer.android.com/identity/legacy/one-tap/save-passwords
source: md.txt
---

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app, [migrate to
| Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

To enable One Tap sign-in for returning users, you can prompt users to save
their password with Google. The user will be able to sign in with their saved
passwords in your app and on the web.

When you start the save password flow, the user will be presented with a
bottomsheet dialog allowing them to choose if they want to save their password
and to which Google Account they want to save it.

![Save password screenshot](https://developer.android.com/static/identity/legacy/one-tap/images/save-password.png)

## Launch password save bottomsheet dialog

You should launch the password save dialog after you have authenticated the
username and password with your backend. Keep the credentials in memory while
authenticating. After you have confirmed the credentials are valid, launch the
save dialog by doing the following:

1. Create a new `SignInPassword` object. It should be initialized with the user
   id they use with your service (for example their username or email address)
   and password that you want to save.

       private static final int REQUEST_CODE_GIS_SAVE_PASSWORD = 2; /* unique request id */
       private void savePassword() {
           SignInPassword signInPassword = new SignInPassword(userId, password);
           ...

2. Create a `SavePasswordRequest` object

       SavePasswordRequest savePasswordRequest =
           SavePasswordRequest.builder().setSignInPassword(signInPassword).build();

3. Get a `PendingIntent` to display the password save dialog from
   `Identity.getCredentialSavingClient` and launch the flow:

       Identity.getCredentialSavingClient(activity)
          .savePassword(savePasswordRequest)
          .addOnSuccessListener(
              result -> {
                  startIntentSenderForResult(
                      result.getPendingIntent().getIntentSender(),
                      REQUEST_CODE_GIS_SAVE_PASSWORD,
                      /* fillInIntent= */ null,
                      /* flagsMask= */ 0,
                      /* flagsValue= */ 0,
                      /* extraFlags= */ 0,
                      /* options= */ null);
              })

## Handle password save results

Handle the result of the password save flow in onActivityResult:

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CODE_GIS_SAVE_PASSWORD) {
            if (resultCode == Activity.RESULT_OK) {
                /* password was saved */
            } else if (resultCode == Activity.RESULT_CANCELED) {
                /* password saving was cancelled */
            }
        }
    }

| **Note:** Consider using the [Activity Result API](https://developer.android.com/training/basics/intents/result) to manage Activity callbacks.

    private ActivityResultLauncher<IntentSenderRequest> savePasswordHandler =
        registerForActivityResult(new ActivityResultContracts.StartIntentSenderForResult(), result -> {
            // handle intent result here
        });