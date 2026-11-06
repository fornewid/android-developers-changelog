---
title: https://developer.android.com/identity/sign-in/restore-credentials
url: https://developer.android.com/identity/sign-in/restore-credentials
source: md.txt
---

Credential Manager's Restore Credentials feature lets users automatically
restore their app accounts and be signed in upon first opening an app after
setting up a new device. A restore credential, also known as a restore key, is a
type of credential that can be saved locally or backed up to a cloud provider,
and then used to provision access on the user's new device.

> [!NOTE]
> **Note:** It is a particularly recommended feature for apps that already support passkeys because of the common underlying server-side implementation. To jump straight to the code, see [Implement Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials-implementation) and [Test Restore
> Credentials](https://developer.android.com/identity/sign-in/test-restore-credentials).

This guide assumes you're familiar with the following concepts:

- [Credential Manager](https://developer.android.com/identity/credential-manager)
- [Passkeys](https://developer.android.com/identity/passkeys)

## Benefits

The benefits of the Restore Credentials feature include:

- **Seamless user experience**: Users can begin using the app immediately on their new device without needing to manually sign in.
- **Increased user retention and reduced support costs**: Automatic sign-in during device upgrades prevents user drop-off and significantly lowers support costs associated with abandoned accounts and password recovery flows.
- **Enhanced security**: Silent credential restoration eliminates extra login screens and manual account recovery prompts, reducing vulnerability to phishing and credential theft attacks.
- **Immediate engagement**: You can engage users with notifications or other prompts as soon as they start using their new device.
- **Support for multiple authentication mechanisms** : It works with multiple authentication mechanisms, including:
  - [Passkeys](https://developer.android.com/identity/passkeys)
  - [Passwords](https://developer.android.com/identity/passwords)
  - [Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg)

## Process overview

The following sections describe the process required on each device:

### On the previous device

Generate the restore key after the user authenticates to your app, immediately
after they sign in, and during a subsequent app launch if they're already signed
in.
The Android backup service automatically stores the generated restore key on the
device, and based on the user's backup settings, also saves it in the cloud.

For a user to be able to back up to the cloud, they must meet the following
requirements:

- Be signed in to their Google Account.
- Have Android data backup enabled. For more information, see [Data backup](https://developer.android.com/identity/data/backup).
- Have a screen unlock mechanism set up, such as pattern, PIN, password, or biometrics.

If these conditions aren't met, an [`E2eeUnavailableException`](https://developer.android.com/reference/androidx/credentials/exceptions/restorecredential/E2eeUnavailableException) is thrown.
When this happens, catch the exception and call `createCredential()` again with
`isCloudBackupEnabled = false` so the restore key is still saved locally for
device-to-device (D2D) transfers.

> [!NOTE]
> **Note:** The process of generating the restore key is silent and doesn't require user interaction after their initial authentication.

### On the new device

When the user sets up their new device, Restore Credentials works silently in
the background during the device setup process. Users can choose to restore data
either from the following options:

- **From a cloud backup**: If a cloud backup is used, the restore key is downloaded with the app data to the new device.
- **Using a device-to-device transfer**: When users transfer data directly between their old and new devices during setup, the restore key moves from the old to the new device through a USB cable or wireless Wi-Fi device-to-device (D2D) transfer.

After the restore key is available on the new device, you can use it to sign in
the user.
![The flow to restore credentials from an old device to a new device requires no user interaction](https://developer.android.com/static/identity/sign-in/images/restore-credentials-flow-on-devices.png) **Figure 1:**Process overview to restore credentials

## Pair Restore Credentials with App Data Backup

Apart from logging in the user, your app should transfer the user's local
settings, offline drafts, and dark theme preferences to deliver a complete,
zero-friction device transition:

- **Restore identity**: Use Restore Credentials to silently re-authenticate account access.
- **Restore state and preferences** : Configure [Auto Backup (`dataExtractionRules`)](https://developer.android.com/identity/data/autobackup) to preserve user preferences, local databases, and app state across cloud and cable device transfers. Exclude raw authentication tokens, hardware-bound Android Keystore ciphertext, and your local `has_synced_restore_credential` marker so stale session state isn't copied onto the new device.

## Handle multiple system profiles and app accounts

When implementing the Restore Credentials feature, consider the following
constraints regarding multi-account apps and system-level profiles.

### Apps with multiple signed-in accounts

Some apps allow users to switch between multiple active accounts (for example, a
personal and a work email account within the same app). Restore Credentials
supports only one account per app. If a user is signed in to multiple accounts,
you must select only one account for which to create the restore key. Typically,
this should be the primary or most recently used account.

### Devices with multiple system profiles

On devices configured with separate [system profiles](https://source.android.com/docs/devices/admin/multi-user) (such as a corporate
device with a managed work profile and a personal profile), the restore key is
available to the primary profile set up during initial device onboarding. If an
enterprise IT policy disables cross-device backup or credential transfer inside
a managed work profile, `createCredential()` or `getCredential()` may return no
credential and your app should fall back to standard sign-in.

## Limitations

Restore Credentials is supported on Android phones, foldables, and tablets
running Android 9 (API level 28) or higher with Google Play services version
`242200000` or higher. Cross-device-category restoration (such as restoring from
a phone to Wear OS, Android TV, Android Auto, Android XR, or ChromeOS) isn't
supported; see [Authenticate across form factors](https://developer.android.com/identity/form-factors).

## Next steps

- [**Implement Restore Credentials**](https://developer.android.com/identity/sign-in/restore-credentials-implementation): Create, retrieve, and clear restore keys in your Android app using Credential Manager.
- [**Test Restore Credentials**](https://developer.android.com/identity/sign-in/test-restore-credentials): Verify cloud and device-to-device restore flows in Android Studio or with automated JUnit 5 backup tests.
- [**Restore Credentials Android skill**](https://developer.android.com/agents/skills/identity/restore-credentials/skill): Use the Android CLI skill to guide coding agents through a two-tier Restore Credentials integration.