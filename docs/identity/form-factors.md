---
title: https://developer.android.com/identity/form-factors
url: https://developer.android.com/identity/form-factors
source: md.txt
---

# Authenticate across form factors

Credential Manager simplifies authentication across the entire Android ecosystem. It provides a consistent experience for users and a unified API surface for developers to use passkeys, passwords, and federated sign-in mechanisms such as Sign in with Google. While the core programming interface remains consistent across form-factors, each form factor has unique UI and UX considerations. Successful implementation requires adapting your app's authentication flows to the specific input methods, screen sizes, and user contexts of each device.

This guide provides an overview of how to implement Credential Manager on different Android form factors, highlighting key considerations and linking to more detailed documentation.

## Mobile devices

Mobile devices, including phones, tablets, and foldables, represent the most common target for Android development. The standard Credential Manager implementation is well-suited for these devices, which typically feature touchscreens and on-device keyboards. The user experience on this form factor serves as the baseline from which you adapt for others. Authentication flows should be suited to the form factor and use the full capabilities of the device's screen real estate and input methods.

## Wear OS

Wear OS devices are characterized by their small screens and limited on-device input. Credential Manager's passkeys implementation provides a secure environment for users to sign in to apps, without needing a connected paired phone and without the need to remember a password.

The API for Wear OS is identical to mobile, so you can reuse an existing mobile integration. In addition to passkeys, Sign in with Google, and passwords with Credential Manager, you can use other authentication methods including Data Layer Token Sharing, OAuth, or your existing solutions. These can be used as backups while you transition your users to Credential Manager, or in the case of Data Layer Token Sharing, as a long-term solution.

Using Credential Manager for Wear OS has the following requirements:

- Minimum API level: minSdkVersion 33 or higher
  - Includes support for passwords, passkeys, and Sign in with Google
- GMS version: The same as required for mobile apps

The user interface on Wear OS devices is as follows:  
![A users passkey as the preferred authentication solution on Wear OS](https://developer.android.com/static/wear/images/design/passkeys-sign-in.png)**Figure 1a:**Passkeys![Passkeys, passwords, and Sign in With Google are all available for a user to authenticate with](https://developer.android.com/static/wear/images/design/passkey-password-gsi-options.png)**Figure 1b:**Passkeys, passwords, and Sign in with Google

For detailed implementation guidance and code samples, see the following resources:

- [Authentication on wearables](https://developer.android.com/training/wearables/apps/auth-wear)
- [UI design recommendations for Wear OS](https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/sign-in)
- [Wear Credential Manager sample](https://github.com/android/identity-samples/tree/credman-compose/Shrine/wear)

### Limitations

Using Credential Manager on Wear OS has the following limitations:

- Does not support creating passkeys.
- Does not support[Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials).

## Android XR

With Android XR---which includes virtual and augmented reality---apps render in 3D space. User input is fundamentally different from those in other form factors, relying on natural inputs like hand gestures.

Adapting Credential Manager for XR means rethinking the authentication UI---whether with passkeys, passwords, or federated sign-in methods---for a 3D space. For example, authentication prompts appear in floating panels, and users make selections using hand gestures. You also need to consider any specific hardware or software prerequisites for your target XR devices.

A critical design challenge is creating an intuitive and secure authentication experience within a VR or AR environment. You must also consider how to manage identity in multi-user XR scenarios, where different people might use the same device.

Using Credential Manager for Android XR has the following requirements:

- Minimum API level:`minSdkVersion`34 or higher
- GMS version: The same as required for mobile apps
- Emulator:
  - Minimum emulator system image:
    - macOS: Google Play XR ARM 64 v8a System Image Revision 7
    - Windows: Google Play XR Intel x86_64 Atom System Image Revision 7
  - Emulator versions later than 35.6.11 Stable

A sign-in experience on XR might look like the following:
![Credential Manager UI in XR](https://developer.android.com/static/identity/form-factors/images/credman-xr.png)**Figure 2:**Credential Manager UI in XR

### Flows unsupported by XR

Credential Manager in Android XR does not support authentication flows that require another device to scan a QR Code. This is observable during sign-in processes on XR headsets and when testing with the emulator.

To learn more about XR, see[Android XR](https://developer.android.com/xr).