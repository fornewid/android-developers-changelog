---
title: https://developer.android.com/identity/legacy/gsi/additional-scopes
url: https://developer.android.com/identity/legacy/gsi/additional-scopes
source: md.txt
---

| **Warning:**
|
| **The Google Sign-In for Android API is outdated and no longer supported.**
| To ensure the continued security and usability of your app, [migrate your Sign in with
| Google implementation to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager-siwg) today. Credential Manager
| supports passkey, password, and federated identity authentication (such as
| Sign-in with Google), stronger security, and a more consistent user
| experience.
|
| **For Wear developers:** Credential Manager is supported in Wear OS
| 5.1 and later on selected watches. Developers actively supporting Wear OS 3, 4
| and 5.0 devices with Sign in with Google should continue using Google Sign-in
| for Android for your Wear applications. Sign in with Google support will be
| available on Credential Manager APIs for these versions of WearOS at a later
| date.
| **Warning:** This page is out of date, refer to [Authorize access to Google user data](https://developer.android.com/identity/authorization) for the latest best practice.

For the best user experience, you should request as few scopes as possible when
initially signing in users. If your app's core functionality isn't tied to a
Google service, the `GoogleSignInOptions.DEFAULT_SIGN_IN` configuration is often
all you need at sign-in.

If your app has features that can make use of Google API data, but are not
required as part of your app's core functionality, you should design your app to
be able to gracefully handle cases when API data isn't accessible. For example,
you might hide a list of recently saved files when the user hasn't granted Drive
access.

You should request additional scopes that you need to access Google APIs only
when the user performs an action that requires access to a particular API. For
example, you might request permission to access the user's Drive only when the
user taps a "Save to Drive" button for the first time.

By using this technique, you can avoid overwhelming new users, or confusing
users as to why they are being asked for certain permissions.

## Request permissions required by user actions

Whenever a user performs an action that requires a scope that isn't requested at
sign-in, call `GoogleSignIn.hasPermissions` to check if the user has already
granted the required permissions. If not, call `GoogleSignIn.requestPermissions`
to launch an activity that requests the additional required scopes from the
user.

For example, if a user performs an action that requires access to their Drive
app storage, do the following:

    if (!GoogleSignIn.hasPermissions(
            GoogleSignIn.getLastSignedInAccount(getActivity()),
            Drive.SCOPE_APPFOLDER)) {
        GoogleSignIn.requestPermissions(
                MyExampleActivity.this,
                RC_REQUEST_PERMISSION_SUCCESS_CONTINUE_FILE_CREATION,
                GoogleSignIn.getLastSignedInAccount(getActivity()),
                Drive.SCOPE_APPFOLDER);
    } else {
        saveToDriveAppFolder();
    }

In your activity's `onActivityResult` callback, you can check if the required
permissions were successfully acquired, and if so, carry out the user action.

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == Activity.RESULT_OK) {
            if (RC_REQUEST_PERMISSION_SUCCESS_CONTINUE_FILE_CREATION == requestCode) {
                saveToDriveAppFolder();
            }
        }
    }

You can also pass a `GoogleSignInOptionsExtension` to `hasPermissions` and
`requestPermissions` to check for and acquire a set of permissions more
conveniently.