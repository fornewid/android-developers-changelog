---
title: https://developer.android.com/privacy-and-security/advanced-protection-mode
url: https://developer.android.com/privacy-and-security/advanced-protection-mode
source: md.txt
---

# Advanced Protection Mode

Android Advanced Protection Mode (AAPM) is a new feature aimed at enhancing the security of Android devices for at-risk users. It functions as a single setting that implements a set of pre-determined configurations designed to bolster device protection. AAPM prioritizes security over some potentially diminished functionality and usability, meaning some features might be restricted to minimize the attack surface.

## Impact

The impact towards developers is described in the following:

- Functionality: AAPM operates as a single setting that activates a collection of security configurations designed to enhance the protection of at-risk users' devices. It will introduce changes to the behavior of certain services, which app developers will need to address.
- Signal to Subscribed Apps: Upon a user enabling AAPM, a signal will be transmitted to all subscribed applications. This signal is a notification to these applications to adapt to the altered behavior of the features enabled by AAPM.
- App Modifications: Developers of subscribed applications are required to modify their apps to comply with the behavioral changes triggered by AAPM. Examples of such modifications include:
  - Adjusting app logic to accommodate the disabling of 2G and WEP network connections.
  - Modifying app behavior to align with the prevention of sideloading.
  - Adapting to the presence of forensic logging.
  - Adjusting functionalities related to call handling due to the blocking of calls from unknown numbers.
  - Integrating with or accommodating spam protection mechanisms for links within messaging apps.
  - Including additional mitigations from app developers to further protect at-risk users.
- Target Audience: Primarily, AAPM is anticipated to affect apps that incorporate security features tailored for users with heightened security awareness. These apps stand to benefit from automatic activation when a user opts for AAPM.

## Integrate with AAPM

In order to use the relevant APIs the following permission needs to be declared  

    <uses-permission android:name="android.permission.QUERY_ADVANCED_PROTECTION_MODE" />

The following APIs are from the newly introduced`AdvancedProtectionManager`system service.  

    public class AdvancedProtectionManager() {
      // Check the current status
      public boolean isAdvancedProtectionEnabled();

      // Be alerted when status changes
      public void registerAdvancedProtectionCallback(Executor executor, Callback callback);

      public void unregisterAdvancedProtectionCallback(Callback callback);
    }

    public class Callback() {
      // Called when advanced protection state changes
      void onAdvancedProtectionChanged(boolean enabled);
    }

| **Note:** When an application terminates, its registered callbacks are removed. Because a terminated application cannot resume and receive AAPM status changes, it's best to register callbacks during the app's initialization phase. Additionally, perform an on-demand AAPM status query during initialization to ensure you have the current state.