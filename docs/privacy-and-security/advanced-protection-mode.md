---
title: https://developer.android.com/privacy-and-security/advanced-protection-mode
url: https://developer.android.com/privacy-and-security/advanced-protection-mode
source: md.txt
---

Android Advanced Protection Mode (AAPM) is a new feature launched in Android
16 aimed at enhancing the security of Android devices for at-risk users, such
as journalists and activists. It functions as a single setting that implements
a set of pre-determined configurations designed to bolster device protection.
AAPM prioritizes security over some potentially diminished functionality and
usability, meaning some features might be restricted to minimize the attack
surface.

## Impact

AAPM changes the behavior of certain system services to enhance security. If
your app caters to security-conscious users, you must adapt to these
restrictions.

- System signals: When a user enables AAPM, the system notifies subscribed apps so they can adapt to the restricted environment.
- Required app modifications: You must update your app to handle the behavioral changes triggered by AAPM. For example, your app must account for:
  - Disabled 2G and WEP network connections.
  - Blocked app sideloading.
  - Active forensic logging.
  - Blocked calls from unknown numbers.
  - Enabled spam protection mechanisms for links in messaging apps.
  - Additional custom mitigations to protect at-risk users

## Integrate with AAPM

In order to use the relevant APIs the following permission needs to be declared.

### Get permission

    <uses-permission android:name="android.permission.QUERY_ADVANCED_PROTECTION_MODE" />

### Check status

Check that the user has AAPM turned on in the
device. This is done using the `AdvancedProtectionManager` system service.

    import android.security.advancedprotection.AdvancedProtectionManager

    // ... inside your Activity or Service
    val aapmManager = getSystemService(AdvancedProtectionManager::class.java)

    if (aapmManager?.isAdvancedProtectionEnabled) {
        // 🛡️ User is in Advanced Protection Mode.
        // Engage shields: Disable risky features, enforce stricter authentication.
        // TODO: Add Method which implements extra protections
    }

### Listen for runtime changes

Users can toggle AAPM on or off while your app is running. Register a Callback
to receive real-time updates.

    import android.security.advancedprotection.AdvancedProtectionManager
    import java.util.concurrent.Executor

    // Define the callback
    val aapmCallback = AdvancedProtectionManager.Callback { isEnabled ->
        if (isEnabled) {
            // TODO: User just engaged protections. Lock it down!
        } else {
            // TODO: User disabled protections. You may relax restrictions.
        }
    }

    // Register the callback (for example, in onStart)
    // Ensure you use the correct executor (for example, mainExecutor for UI updates)
    aapmManager?.registerAdvancedProtectionCallback(mainExecutor, aapmCallback)

> [!NOTE]
> **Note:** When an application terminates, its registered callbacks are removed. Because a terminated application cannot resume and receive AAPM status changes, it's best to register callbacks during the app's initialization phase. Additionally, perform an on-demand AAPM status query during initialization to ensure you have the current state.