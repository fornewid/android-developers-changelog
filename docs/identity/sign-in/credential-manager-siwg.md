---
title: https://developer.android.com/identity/sign-in/credential-manager-siwg
url: https://developer.android.com/identity/sign-in/credential-manager-siwg
source: md.txt
---

Credential Manager's Sign in with Google implementation lets you configure
sign-up and sign-in experiences. Credential Manager abstracts authentication
complexity, while ensuring secure profile sharing and a consistent sign-up flow
across the entire Android ecosystem. Sign in with Google lets your users use
their Google Account to sign in and give consent to securely share their profile
information with your app.

The cross-platform nature of Sign in with Google helps you provide sign-in
access for your app on any device across Android, iOS, and the
[web](https://developers.google.com/identity/gsi/web/guides/overview).

This guide explains the following areas:

- Benefits of Sign in with Google
- User interface guidelines
- Prerequisites for implementation

This guide assumes you're familiar with the following concepts:

- [Credential Manager](https://developer.android.com/identity/credential-manager)
- [Google Cloud projects](https://developers.google.com/workspace/guides/create-project)

> [!NOTE]
> **Note:** For authorization actions needed to access data stored in a Google Account, such as data stored in Google Drive, use the [AuthorizationClient
> API](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient). If you use Firebase Authentication for your app, you can learn more about integrating Sign in with Google and Credential Manager in the [Firebase guide](https://firebase.google.com/docs/auth/android/google-signin).

## Benefits of Sign in with Google

Using Sign in with Google as the authentication mechanism for your app has the
following benefits:

- Sign in with Google ensures that a user has signed in to their Google Account recently. Additionally, a user's Google ID Token can include information about the last time they authenticated with their Google Account on the device. Account management systems can use this information as an indicator to make decisions about account security.
- The [bottom sheet](https://developer.android.com/identity/sign-in/credential-manager-siwg#use-credential) implementation supports [Automatic
  Sign-In](https://support.google.com/accounts/answer/12849458#zippy=%2Cautomatic-sign-in), which removes manual steps for returning users who have already authorized the app.
- Sign in with Google supports cross-platform authentication.

> [!NOTE]
> **Note:** For apps in security-focused industries such as healthcare and financial services, the trust signals returned by Sign in with Google are an indicator of account safety. For more information about the security features of Sign in with Google, see [Security bundle](https://developers.google.com/identity/siwg/security-bundle).

## Version compatibility

Credential Manager's Sign in with Google implementation works on devices running
Android 4.4 (API level 19) and higher.

## User interface guidelines

When incorporating Sign in with Google, we recommend that you implement both of
the following user interfaces:

- The bottom sheet UI, which can also include other sign-in options such as passkeys and passwords.
- A distinct "Sign in with Google" button.

We recommend that you implement both the interfaces for the following reasons:

- The bottom sheet is a user-dismissible UI, while the button is a persistent UX element. The button allows users to restart the authentication flow without needing to restart the app if they dismiss the bottom sheet.
- The bottom sheet excludes accounts that require re-authentication; however, the button flow lets users access these accounts.
- If no Google Accounts exist on the device, the bottom sheet UI does not appear. However, the button allows users to add a new account to the device.

### Use the bottom sheet UI

Credential Manager's bottom sheet UI is integrated within the Credential Manager
API. You don't need to create your own user interface to use the bottom sheet
UI.

Using the bottom sheet UI gives users a consistent authentication experience
across Sign in with Google, passkeys, and passwords.
![The Credential Manager bottom sheet credential selection UI.](https://developer.android.com/static/identity/sign-in/images/credential_manager_bottom_sheet.svg) The Credential Manager bottom sheet credential selection UI.

> [!NOTE]
> **Note:** The appearance of the bottom sheet depends on the user's Google Account settings. The settings are enabled by default; however, if the user disables "Sign-in prompts" for any Google Account on the device under **Google Account
> Settings \> Sign in with Google \> Sign-in prompts**, the bottom sheet is suppressed for all accounts.

### Use a Sign in with Google button

The Sign in with Google button presents users with a distinct option to use
their Google Account to sign up for and sign in to your app.
![The Sign in with Google button.](https://developer.android.com/static/identity/sign-in/images/sign_in_with_google_button.svg) The Sign in with Google button.

## Prerequisites to implement Sign in with Google

To implement Sign in with Google, complete the following setup:

- **Configure the Google Auth Platform** : For more information about
  configuring your Google Cloud project, see [Get started with the Google Auth
  Platform](https://support.google.com/cloud/answer/15544987).

  > [!NOTE]
  > **Note:** You use the client ID configured in the Google Auth Platform while implementing the Credential Manager APIs for Sign in with Google.

- **Complete brand verification** : Your brand must be verified for your app
  name to be visible to users on the Sign in with Google consent screen. For
  more information about brand verification, see [OAuth App Verification Help
  Center](https://support.google.com/cloud/answer/13463073) and [Submit app for brand verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification)

## See also

Case studies:

- [Lokmat](https://developers.google.com/identity/sign-in/case-studies/lokmat)
- [Reddit](https://developers.google.com/identity/sign-in/case-studies/reddit)