---
title: https://developer.android.com/identity/sign-in/credential-manager-faq
url: https://developer.android.com/identity/sign-in/credential-manager-faq
source: md.txt
---

# Credential Manager FAQ

The question-and-answer pairs on this page are meant to help you gain more understanding of[Credential Manager](https://developer.android.com/training/sign-in/passkeys)'s implementation details.

Your feedback is a crucial part of improving the Credential Manager API. Share any issues you find or ideas for improving the API using the following link:

[Give feedback](https://docs.google.com/forms/d/e/1FAIpQLSdlCw9F01l_7wYO4-Yna5rYO1KKS9huAy5NwPp1PCCnf4tPXg/viewform)

### Integration

**Why is there a need for another Jetpack library for app authentication?**

The Jetpack Credential Manager library provides a unified sign-in experience across all Android versions. It also lets you get more timely updates with the latest features. It has backward compatibility, with general support on Android 4.4 and higher, and support for passkeys on Android 9 and higher.

**Where do these credentials come from?**

Credentials come from credential providers and password managers, such as[Google Password Manager](https://passwords.google/), that are integrated with Credential Manager and that the user has enabled. Also, for passkeys, users can choose to get them from another device using the hybrid flow.

**What are the different use cases where Credential Manager makes more sense or is more necessary to implement?**

Credential Manager offers your app a seamless \& secure way to manage authentication flows in a consolidated API that offers a unified user interface for several sign-in methods. This has several benefits:

- Users appreciate seeing all their credentials in one place; passkeys, passwords and federated credentials such as Sign in With Google, without needing to tap on 3 different places
- Offers a simpler login experience by consolidating the sign-in methods for each account.

  Additionally, on Android 14 devices, the user interface surfaces only the safest \& simplest authentication method. For instance, if a user has both a passkey and a password for the same account, only the passkey are suggested in the account chooser.
- Supports multiple sign-in mechanisms within a single API. It brings support for passkeys on Android apps, enabling the transition to a passwordless future. And at the same time, it also supports passwords and federated sign in like Sign in With Google, simplifying integration requirements and ongoing maintenance.

**There are multiple dependencies to add during integration, what is the need of multiple dependencies? Isn't it possible to have just one single dependency to achieve the same?**

There is 1 required dependency and 1 optional. The apps include different ones depending on their use cases.

1. \[**Required** \][**androidx.credentials:credentials**](https://developer.android.com/training/sign-in/passkeys#add-dependencies): Contains the core Credential Manager functionalities including password and passkey support.
2. \[**Optional** \][**androidx.credentials:credentials-play-services-auth**](https://developer.android.com/training/sign-in/passkeys#add-dependencies): Provides support from Google Play services for Credential Manager, which lets you use the APIs on older devices.

**Does Credential Manager support using credentials from another device?**

Credential Manager supports cross-device passkey usage through the hybrid transport.

**Can developers merge their sign-up and sign-in flows into one API call using Credential Manager?**

Not planned right now.

### UX

**If users have already set up a provider not registered with Credential Manager, what UX is shown to the users?**

Providers not registered with Credential Manager continue to operate with the[autofill framework](https://developer.android.com/guide/topics/text/autofill), showing suggestions in the keyboard and drop-down menu.

### Others

**Why is there a need for Credential Manager when there are different sign-in options already in place and screen locks are also there?**

On Android devices, users have different solutions to facilitate authentication to apps and websites. As each app may integrate with different combinations of solutions, the user experience may be drastically different.

Credential Manager provides a coherent and consistent sign in user experience to 3P services on Android, regardless of the sign-in method that the user prefers or that the app supports: username and password, passkey, or federated identity.

**What specific user requirements are catered using passkeys through the Credential Manager API?**

- Eliminate the need for users to create and remember difficult passwords.
- Create a phishing-resistant form of signing in which increases security for users.

**How much time would it take for an update to be released for the major bugs?**

Jetpack has biweekly releases. The platform has security releases, quarterly releases, and dessert releases depending on the type and severity of a bug. Learn more about the[Jetpack release process](https://developer.android.com/jetpack/androidx/versions).

**Is there any impact on Performance (App Startup time) after integration?**

It is recommended to wisely choose when to initialize your Credential manager sign-in flow and measure your app performance once the API is initialized.

**Is this API compatible with Android Go devices?**

Yes, the API is compatible with Go devices.

**If developers use SMS OTP or federated identity for sign in, is that also supported with Credential Manager?**

Credential Manager supports passkeys, passwords and Google ID tokens as sign-in methods. A Google ID token can also be used for sign-up workflows.