---
title: https://developer.android.com/games/playgames/integrity
url: https://developer.android.com/games/playgames/integrity
source: md.txt
---

Google Play Games on PC supports integrity protection through the Play
Integrity API and several other Google Play features to help ensure that
your game hasn't been tampered with or installed from an untrustworthy source.

## Play Integrity API

The [Play Integrity API](https://developer.android.com/google/play/integrity) helps protect your
games from potentially risky and fraudulent interactions. The API
enables you to reduce attacks and abuse such as
fraud, cheating, and unauthorized access. The
[Play Integrity API](https://developer.android.com/google/play/integrity) replaces the
SafetyNet Attestation API (SNAA) and Play App Licencing API.
SNAA does not work with Google Play Games on PC.

### Device Integrity Field

The
[`deviceRecognitionVerdict`](https://developer.android.com/google/play/integrity/verdict#device-integrity-field)
field contains a single value, `deviceRecognitionVerdict`,
that represents how well a device can enforce app integrity. By default,
`deviceRecognitionVerdict` can have one of these values:

- `MEETS_DEVICE_INTEGRITY`: The app is running on an Android-powered device with Google Play services. The device passes system integrity checks and meets Android compatibility requirements.
- `MEETS_VIRTUAL_INTEGRITY`: The app is running in a virtual Android environment with Google Play services, currently limited to Google Play Games on PC. The environment meets core Android compatibility requirements and passes Google Play integrity checks.
- None (a blank value): The app is running on a device that has signs of attack (such as API hooking) or system compromise (such as being rooted), or the app is running on a non-physical device (such as an emulator) that does not pass Google Play integrity checks.

The Play Integrity API uses the `deviceRecognitionVerdict` value
`MEETS_VIRTUAL_INTEGRITY` to indicate that the game is running on Google Play Games on PC. Here's an example of a passing response from
the Play Integrity API:

    deviceIntegrity: {
        // "MEETS_VIRTUAL_INTEGRITY" indicates the game is running on Google Play Games on PC
        deviceRecognitionVerdict: ["MEETS_VIRTUAL_INTEGRITY"]
    }

If you have a cross-platform game available on both mobile and
Google Play Games on PC, make sure your
validation logic checks for both `MEETS_VIRTUAL_INTEGRITY` and
`MEETS_DEVICE_INTEGRITY`.

## Automatic protection

Google Play's [automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279) is a service
that helps you protect your game against unauthorized redistribution and
piracy. When users get your protected app from an unknown distribution
channel, they'll be prompted to get your official app from
Google Play. Automatic protection works in your app without a data
connection. It can be turned on with one click in the
Play Console, and requires no developer work before testing and no
backend server integration. Automatic protection can add the following
features to your game:

- **Installer checks**: Automatic protection can add Google Play installer checks to your app's code that happen at runtime when your app is opened. If the installer checks fail, users will be prompted to get your app on Google Play.
- **Anti-tamper protection** **(this feature is only available to selected Play partners)**: Automatic protection can add runtime checks to your app's code to detect modification and use advanced obfuscation techniques to prevent the checks from being removed or reverse engineered. If the checks fail, the user will be prompted to get your app on Google Play or the app will not run.

Automatic protection requires no code changes or developer work before
testing. Learn more about
[automatic protection in the Play Console help center](https://support.google.com/googleplay/android-developer/answer/10183279).