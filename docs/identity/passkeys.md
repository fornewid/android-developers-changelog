---
title: https://developer.android.com/identity/passkeys
url: https://developer.android.com/identity/passkeys
source: md.txt
---

# About passkeys

[Passkeys](https://developers.google.com/identity/passkeys)offer a more secure and user-friendly alternative to passwords. They allow users to sign in to websites and applications using their device's built-in unlock mechanisms such as pattern, PIN, password or biometrics like fingerprint or facial recognition. The Credential Manager API builds on the[Web Authentication standard](https://www.w3.org/TR/webauthn-2/)to facilitate the integration of passkey authentication flows.

## Benefits of passkeys

Passkeys offer many benefits over other authentication mechanisms.

- **Improved sign-in experience**: Users can authenticate using methods like fingerprint or facial recognition instead of typing passwords, resulting in a smoother and quicker sign-in experience.
- **Improved security**: Passkeys use public-key cryptography so that data breaches of service providers don't result in compromised accounts. Passkeys are based on industry standard APIs and protocols that are not subject to phishing attacks.
- **Unified experience across devices and platforms**: With the ability to sync passkeys across devices, users benefit from simplified authentication regardless of the device or platform they use, including Windows, iOS, and Linux.
- **Seamless authentication on new devices** : Passkeys support[Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials)to seamlessly sign in users to new devices.
- **Reduced friction during sign-in**: Passkeys don't require users to remember passwords, reducing the friction of forgotten passwords.

To see examples that illustrate these benefits, see the[case studies of apps that adopted passkeys](https://developers.google.com/identity/passkeys/case-studies).

## How passkeys work in Credential Manager

Use the Credential Manager API in your[relying party client app](https://developer.android.com/identity/credential-manager#authentication-terminology)and[relying party app server](https://developer.android.com/identity/credential-manager#authentication-terminology)to create authentication solutions with passkeys.

The steps to**create a passkey**can be summarized as follows:

1. Your client app requests the options required to create credentials from your app server.
2. Your client app uses these options to send a request to the Credential Manager API to generate a public-private key pair.
3. The public key is stored on the app server and the private key is securely stored on the user's device on a credential provider like Google Password Manager.

The steps to**sign in with a passkey**are as follows:

1. Your client app requests the credential request options from the app server, which sends a challenge with its response. The app server securely stores this challenge for later verification.
2. After the user consents to using the passkey by using their device's screen unlock, the credential provider uses the stored private key to sign the challenge, creating a signed assertion.
3. Send the signed assertion to the app server and performs the following checks:

   - If the challenge matches the stored challenge.
   - If the signature in the assertion can be verified with the public key.

   If the app server successfully verifies the assertion, the user is signed in.

![With passkeys, public keys are stored on the app server and private keys on the user's device](https://developer.android.com/static/identity/passkeys/images/passkeys.png)**Figure 1.**Public keys are stored on the app server and private keys on the user's device. Both keys are used to authenticate a user.**Note:** Our guides focus on the changes required in the client app, but include a brief overview of the server-side implementation. To learn more about the server-side implementation, see[Server-side passkey implementation](https://developers.google.com/identity/passkeys/developer-guides/server-introduction).

## Android version compatibility

Credential Manager's passkeys implementation works on devices running Android 9 (API level 28) and higher.

## Cross-platform support

Passkeys are compatible with several operating systems, including Android, Microsoft Windows, macOS, and iOS. They also work with a variety of popular browsers, such as Chrome, Microsoft Edge, and Safari.

See[Supported environments](https://developers.google.com/identity/passkeys/supported-environments)to check the support status on Chrome and Android. To learn about adding passkeys to your website, see[Passkeys on the web](https://developer.chrome.com/docs/identity/passkeys).

## Support across form-factors

Passkeys work on other Google-developed form factors, including Android, Wear OS, and Android XR. To learn more, see[Form factors](https://developer.android.com/identity/form-factors).

## Next steps

- [Create a passkey](https://developer.android.com/identity/passkeys/create-passkeys)
- [Sign in with passkeys](https://developer.android.com/identity/passkeys/sign-in-with-passkeys)
- [Manage passkeys](https://developer.android.com/identity/passkeys/manage-passkeys)
- [Understand passkey user experience flows](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys)
- [Learn more about passkeys](https://developers.google.com/identity/passkeys/developer-guides)