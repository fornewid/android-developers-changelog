---
title: https://developer.android.com/registered-app-stores/overview
url: https://developer.android.com/registered-app-stores/overview
source: md.txt
---

A Registered App Store is a third-party app store that registers with Google to
access additional platform capabilities, including one-tap installs, while
upholding core ecosystem trust, security, and performance standards.

Becoming a registered app store is completely optional. If a store chooses not
to participate, it retains the same experience as any sideloaded app on
Android.

## What you can do as a Registered App Store

As a Registered App Store, you can offer your users:

- **One-tap installs**: Users can download and install apps directly from the store without secondary system confirmation screens.
- **Effective Communication**: Notification capabilities allows the store to keep users informed of important updates and status changes efficiently.

## Geographic availability

The Registered App Store status is available in [select regions](https://developer.android.com/registered-app-stores/faq#geographic-regions-registered-app-store). Starting
December 1, 2026, the program will be available on devices running Android 17
QPR2 and higher.

The user's home location determines feature availability for Registered App
Stores:

- International travel: Vacations or short-term international travel to unsupported regions don't disrupt existing one-tap installs or automatic updates.
- Permanent relocation: If a user relocates permanently, the user's device automatically adjusts feature availability to reflect the options supported in their new country of residence.

## Difference in user experience

The following table explains the differences between the Registered App Store
and standard app store flows.

| Feature | Registered App Store (Preferred) | Standard app store |
|---|---|---|
| Permission requirements | Automatically grants permission once verified. | Requires users to manually enable `REQUEST_INSTALL_PACKAGES` in System Settings. |
| Installation prompts | Unlocks direct one-tap installs without extra confirmation screens. | Requires manual per-install dialog confirmation for every app. |
| App updates | Updates in the background automatically with user control settings. | Requires manual user approval per update release. |

## What to expect during the registration process

Registering an app store follows a five-step process:

- **Interest form submission**: Submit the official Interest Form, providing organization identity details, public distribution links, and the Google Account used for Android Developer Console.
- **Pre-qualification**: Google reviews the submission to validate the provided organization account, developer and package name verification status, and brand legitimacy. Upon validation, the store will be given instructions to proceed with their application to the Registered App Store program in Android Developer Console.
- **Payment of registration fee**: This is a fixed annual registration fee.
- **Application and technical evaluation**: Enrolled developers submit their package name in Android Developer Console. This step requires uploading the store APK for malware scanning, declaring mandatory policy URLs, and continuously sharing the complete app catalog and ongoing app updates with Google for malware review. The store is then evaluated according to requirements.
- **Activation**: If a store is approved, its status will update to "Registered App Store" (RAS) and RAS features will be activated.

If you'd like to continue, begin the enrollment process by reviewing the
[Requirements](https://developer.android.com/registered-app-stores/requirements).