---
title: https://developer.android.com/identity/sign-in/legacy-gsi-migration
url: https://developer.android.com/identity/sign-in/legacy-gsi-migration
source: md.txt
---

# Migrate from legacy Google Sign-In to Credential Manager and AuthorizationClient

Migrate from[Google Sign-In for Android](https://developers.google.com/identity/sign-in/android/start-integrating)to Android Credential Manager to streamline your app's authentication experience and future-proof your development practices. Google Sign-In for Android is deprecated and will be removed from the[Google Play Services Auth SDK](https://maven.google.com/web/index.html?q=play-services-auth#com.google.android.gms:play-services-auth). (`com.google.android.gms:play-services-auth`) in 2025.

For**authentication** , developers should migrate their Android projects to[Credential Manager](https://developer.android.com/identity/sign-in/legacy-gsi-migration#authentication), which fully supports One Tap and button flows for Sign in with Google. See our[blog post](https://android-developers.googleblog.com/2024/09/streamlining-android-authentication-credential-manager-replaces-legacy-apis.html)for details.

For**authorization** actions that need access to user data stored by Google such as Google Drive, use the[AuthorizationClient API](https://developer.android.com/identity/sign-in/legacy-gsi-migration#authorization).

## Migrate authentication to the Credential Manager API

With a streamlined, unified API that enables support for modern features and practices while improving the authentication experience for your users, Credential Manager offers several key advantages over legacy Google Sign-In for Android:

- Simplified and streamlined flows built with Credential Manager have been shown to[reduce average sign-up and sign-in times](https://developers.googleblog.com/2023/10/how-kayak-reduced-sign-in-time-and-improved-security-with-passkeys.html)by up to 50%.
- Credential Manager integrates support for multiple sign-in methods, including[Sign in with Google](https://developer.android.com/training/sign-in/credential-manager),[passkeys](https://developers.google.com/identity/passkeys)and passwords.
- Credential Manager is a single, unified API that provides a more consistent user interface across Android devices, aligns with evolving security standards, and simplifies your development process.
- Credential Manager provides a consistent, unified[user experience](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys)across all authentication methods.
- Starting with Android 14, Credential Manager supports third-party password and passkey providers, allowing users to select their preferred credential provider.
- Credential Manager fully supports the[Sign in with Google](https://developer.android.com/training/sign-in/credential-manager)button, so developers can drop this directly into existing flows.
- Credential Manager supports One Tap capabilities, so developers can directly prompt users to sign in with their Google Account with a single tap.

To begin your Credential Manager integration,[read the developer guide](https://developer.android.com/training/sign-in/passkeys). Read about[authentication user experience with passkeys](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys)to understand how your identity flows should be designed. Read the[Integrate Credential Manager with Sign in with Google](https://developer.android.com/training/sign-in/credential-manager)guide for implementation details on One Tap or the Sign in with Google button.

## Migrate authorization to the AuthorizationClient API

In contrast with legacy Google Sign-In, the authentication and authorization functions are now available as two separate and distinct flows. Credential Manager is the API you use for***authentication*** on Android. For***authorization***actions, such as accessing a service like Google Drive, use the AuthorizationClient API. This separation helps you map user flows to user intent, so that your users can sign up or sign in with their Google Accounts, and you can separately provide authorization permissions from their Google Account when they are needed by the application as opposed to login time alone.

To learn more about authorization, read the[Authorize Access to User Data](https://developers.google.com/identity/sign-in/android/authorize-access)guide, and check out the[AuthorizationClient API](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/AuthorizationClient)documentation.