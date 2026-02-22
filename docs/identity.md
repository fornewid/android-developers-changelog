---
title: https://developer.android.com/identity
url: https://developer.android.com/identity
source: md.txt
---

# Identity

![](http://developer.android.com/static/images/cluster-illustrations/identity.svg)  

### Identity

Your Android app's security and functionality is reliant on user identity management. This involves verifying who your users are (authentication), controlling access to users' data (authorization), and offering a smooth account creation process.

A central hub for various sign-in methods, including passkeys, Credential Manager helps users sign in to your app with a single tap. This eliminates the need for users to remember which method they have to use, and instead focus on choosing the right account.  
[Add sign-up and sign-in](http://developer.android.com/identity/sign-in)[![](http://developer.android.com/static/images/picto-icons/key.svg)](http://developer.android.com/identity/sign-in/credential-manager)  

### [One-tap sign-in](http://developer.android.com/identity/sign-in/credential-manager)

Build flows using Credential Manager to sign in users with a single tap, across passkeys, Sign in with Google, and passwords.  
[Learn more](http://developer.android.com/identity/sign-in/credential-manager)  
[![](http://developer.android.com/static/images/picto-icons/pathway.svg)](http://developer.android.com/identity/sign-in/credential-manager-siwg)  

### [Simple account creation](http://developer.android.com/identity/sign-in/credential-manager-siwg)

Android streamlines user sign-up. With Sign in with Google, make sign up a single tap for users, and offer passkey creation as a part of that key journey.  
[Learn more](http://developer.android.com/identity/sign-in/credential-manager-siwg)  
[![](http://developer.android.com/static/images/picto-icons/speedometer.svg)](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)  

### [Unified interface](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)

Credential Manager offers a seamless identity experience; showing all sign-in mechanisms in one place. Offer a one-tap sign-in, or simplify account creation.  
[Learn more](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)  
[![](http://developer.android.com/static/images/picto-icons/multiple-screens.svg)](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys#unified_sign-in)  

### [Integrated with Google Password Manager](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys#unified_sign-in)

Users can save and store passwords in Google Password Manager to use safely on all of their devices. On Android 14+, users can also enable their password manager of choice.  
[Learn more](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys#unified_sign-in)

## Passkeys improve the authentication user experience on Android

Sign-in can be a major source of confusion and app abandonment.

Passkeys, available through Credential Manager, improve user experience by making sign-in easier and more secure; they are phishing-resistant and cannot be reused. Users can sign in by unlocking their device with their fingerprint, face recognition, or a local PIN, rather than having to remember and type in a password.

![](https://developer.android.com/static/images/identity/identity-passkeys.png)  
[Read more](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)[![](http://developer.android.com/static/images/identity/quick-account-creation.png)](http://developer.android.com/identity/sign-in/credential-manager-siwg#enable-sign-up)  

### [Quick account creation](http://developer.android.com/identity/sign-in/credential-manager-siwg#enable-sign-up)

Streamline your signup process and reduce abandonment rates by integrating Sign in with Google during account creation.

This one-click signup option leverages familiar user credentials, minimizing friction and improving user experience.

By prioritizing Sign in with Google at signup, you can dramatically improve your app's onboarding process and user satisfaction.  
[Read more](http://developer.android.com/identity/sign-in/credential-manager-siwg#enable-sign-up)[![](http://developer.android.com/static/images/identity/single-click-sign-in.png)](http://developer.android.com/identity/sign-in/credential-manager)  

### [Single click sign-in](http://developer.android.com/identity/sign-in/credential-manager)

Credential Manager is a Jetpack API that supports multiple sign-in methods, such as username and password, passkeys, and federated sign-in (such as Sign-in with Google) in a single API, simplifying the integration for developers.

Users can sign in to your app with a single click, without worrying about the right option to pick. Credential Manager unifies the sign-in interface across authentication methods, making it clearer and easier for users to sign into apps, regardless of the method they choose.  
[Read more](http://developer.android.com/identity/sign-in/credential-manager)![](http://developer.android.com/static/images/picto-icons/launch.svg)  

## Get started with authentication

A collection of guides to you get started with implementing authentication into your app.  
Getting started

### [User authentication with passkeys](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)

This guide contains best-practice examples on how to implement passkeys in your Android app. Learn how to configure key app user journeys to be more user friendly.  
[View the guide](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)  
Getting started

### [Integrate Credential Manager with Passkeys](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)

Learn how to optimize your app's user experience with passkeys. Contains visual examples of app user journey's and implementation best practices.  
[View the guide](http://developer.android.com/design/ui/mobile/guides/patterns/passkeys)  
Getting started

### [Integrate Credential Manager with Sign in with Google](http://developer.android.com/identity/sign-in/credential-manager-siwg)

Streamline your app's sign up and sign in flows with Credential Manager and Sign in with Google. This integration provides convenient options like auto sign-in, One Tap, and the dedicated Sign in with Google button.  
[View the guide](http://developer.android.com/identity/sign-in/credential-manager-siwg)  
Getting started

### [Integrate Credential Manager with WebView](http://developer.android.com/identity/sign-in/credential-manager-webview)

This document describes how to integrate the Credential Manager API with an Android app that uses WebView.  
[View the guide](http://developer.android.com/identity/sign-in/credential-manager-webview)  
Getting started

### [Integrate Firebase Authentication with Sign in with Google](https://firebase.google.com/docs/auth/android/google-signin)

Learn how to implement Sign in with Google using the Firebase Authentication library.  
[launchView the guide](https://firebase.google.com/docs/auth/android/google-signin)

## Latest news and videos

## Migrate from legacy APIs to Credential Manager

[![](http://developer.android.com/static/images/identity/g-round.svg)](http://developer.android.com/identity/sign-in/legacy-gsi-migration)  

### [Migrate from legacy Google Sign-In](http://developer.android.com/identity/sign-in/legacy-gsi-migration)

Google Sign-In for Android is now deprecated and is planned to be removed in 2025. Move to Credential Manager for a smoother user experience and to keep your app up-to-date.

Credential Manager focuses on sign-up and sign-in. For authorization, use AuthorizationClient for granular authorization requests to Google Accounts (like Drive, Calendar, or Photos).  
[View the guide](http://developer.android.com/identity/sign-in/legacy-gsi-migration)  
[![](http://developer.android.com/static/images/identity/migrate-from-smart-lock.png)](http://developer.android.com/identity/sign-in/smart-lock-migration)  

### [Migrate from Smart Lock for Passwords](http://developer.android.com/identity/sign-in/smart-lock-migration)

Upgrade your Android app to keep password saving working and support third-party password managers. Smart Lock has been removed, and Credential Manager offers a smoother experience.  
[View the guide](http://developer.android.com/identity/sign-in/smart-lock-migration)  
[![](http://developer.android.com/static/images/identity/migrate-from-fido2.png)](http://developer.android.com/identity/sign-in/fido2-migration)  

### [Migrate from FIDO2](http://developer.android.com/identity/sign-in/fido2-migration)

Learn how to migrate your Android apps from local FIDO2 credentials to Credential Manager.  
[View the guide](http://developer.android.com/identity/sign-in/fido2-migration)

## Resources for credential providers

[![](http://developer.android.com/static/images/picto-icons/sync-2.svg)](http://developer.android.com/identity/sign-in/credential-provider)  

### [Integrate with your credential provider solution](http://developer.android.com/identity/sign-in/credential-provider)

Credential Manager lets users choose from any sign-in method (passkeys, Sign in with Google, and passwords) on an Android app. Learn how to integrate your own credential provider solution.  
[View the guide](http://developer.android.com/identity/sign-in/credential-provider)  
[![](http://developer.android.com/static/images/picto-icons/kotlin-friendly-sdk.svg)](http://developer.android.com/identity/sign-in/privileged-apps)  

### [Make Credential Manager calls on behalf of other parties](http://developer.android.com/identity/sign-in/privileged-apps)

Privileged apps, such as web browsers, can securely manage passkeys for other apps. This feature requires approval to ensure only trusted apps handle user credentials.  
[View the guide](http://developer.android.com/identity/sign-in/privileged-apps)