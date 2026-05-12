---
title: https://developer.android.com/developer-verification/guides/faq
url: https://developer.android.com/developer-verification/guides/faq
source: md.txt
---

This guide answers some of the most common questions regarding Android developer
verification.

## General

- **Why is identity verification important to security and why is this change
  happening now?** Identity verification establishes accountability. This
  creates a crucial connection between apps and their creators, making it much
  harder for malicious actors to quickly distribute another harmful app after
  we take the first one down.

  Online scams and malware campaigns are becoming more aggressive and often
  rely on social engineering. In a common attack, scammers use high-pressure
  tactics to trick users into installing apps that are actually malware
  designed to steal personal information and drain bank accounts. While
  automated systems catch many threats, bad actors can quickly create new
  anonymous apps to replace those taken down. Identity verification helps
  disrupt this cycle by requiring a real accountable identity behind the
  software. This makes it significantly harder for scammers to scale their
  attacks.

  Users have also asked for more transparency to help them navigate downloads
  with confidence and our research shows that users feel safer when they know
  an app is connected to a verified person or organization. *Last updated May
  11, 2026*
- **What happens if I don't comply?** If you do not verify your identity and
  register your apps by the September **deadline** , your apps will be blocked
  from being installed by users on [certified Android devices](https://www.android.com/certified/partners/) in applicable
  regions. *Last updated: Sept 3, 2025*

- **I'm a hobbyist/student. What is "limited distribution"?** We understand
  that not everyone is a professional developer. We are introducing a free
  developer account type that will allow teachers, students, and hobbyists to
  distribute apps to 20 devices without needing to provide a government ID.
  [Learn more about limited distribution accounts](https://developer.android.com/guides/limited-distribution). *Last updated: March
  25, 2026*

- **Will Android Debug Bridge (ADB) install work without registration?** As a
  developer, you are free to install apps without verification with ADB. This is
  designed to support developers' need to develop, test apps that are not
  intended or not yet ready to distribute to the wider consumer population.
  *Last updated: Sept 3, 2025*

- **Do enterprise apps need to complete the verification requirements?** Apps
  distributed through your organization store, on managed devices, won't need to
  complete the verification requirements since your IT admin has vetted them.
  However, we recommend to still register and claim these apps since this
  creates a smooth installation, if the app is downloaded from another source
  (not the managed store) or to a non-managed device. *Last updated: Sept 3,
  2025*

- **If I want to modify or hack some apk and install it on my own device, do I
  have to verify?** Apps installed using ADB won't require verification. This
  ensures developers can build and test apps that aren't intended or not yet
  ready to be distributed to the wider consumer population. *Last updated:
  Sept 11, 2025*

- **How does this program impact developers in sanctioned countries?** Devices
  in sanctioned countries will be excluded from ADV checks. This allows any
  developer to continue distributing apps in these regions without
  verification, though users there won't benefit from the enhanced security
  benefits of the program. Last updated: March 25, 2026

- **What Android versions will the developer verification requirements be
  enforced on?** It will apply to all certified Android devices running
  Android 7 or higher. These updates are delivered through Google Play
  services to help maintain consistent security across the ecosystem. *Last
  updated: March 23, 2026*

- **Does this mean Android is becoming a closed system?** No. Android remains
  an open ecosystem where you distribute through a variety of channels you
  choose and install software from multiple sources.

  - For developers, this includes Android app stores or sideloading using
    your own website, messaging app, and more.

  - For users, most users won't see a change in their download experience
    at all. Power users can choose to install apps from unverified
    developers after a one-time advanced flow setup launching August 2026.
    *Last updated: May 11, 2026*

## Identity and accounts

- **What is a D-U-N-S number and how do I get one?** A D-U-N-S number is a unique nine-digit identifier for businesses provided by Dun \& Bradstreet. It is required if you are registering as an **organization** . If your organization does not have one, you can [get one for free](https://www.dnb.com/en-us/smb/duns/get-a-duns.html) from the Dun \& Bradstreet website. The process can take up to 28 days so you should make preparations to obtain a D-U-N-S number. *Last updated: Sept 3,
  2025*
- **How is my personal information handled?** We use your personal information to verify your identity, and it is handled in accordance with [Google's
  Privacy Policy](https://policies.google.com/privacy). We are committed to protecting your data. *Last updated: Sept 3, 2025*
- **How does this impact developers who do not want to verify, preferring to
  remain anonymous?** While we respect developer privacy, we must balance it
  with user safety. Adding this security layer protects all users by default
  and Google is only using your information to verify your identity and allow
  you to register which apps belong to you. We will handle your personal
  information in accordance with our Privacy Policy.

  Developers who want to remain unverified can use a limited distribution
  account, which requires no ID verification. Or you can distribute your app
  as you normally do and ask your users to use the one-time advanced flow.
  *Last updated: May 11, 2026*
- **Why is there a $25 fee for the ADC? How can I pay?** The $25 fee for the
  **Full Distribution** account in the ADC helps cover administrative costs and
  investment in protecting the ecosystem, similar to Play's $25 registration
  fee. We are actively working to support multiple forms of payment to
  accommodate developers globally and will have more details when the console
  launches. We are waiving the fee for developers who qualify for a Limited
  Distribution account. *Last update: March 25, 2026*

- **What happens if I cannot provide a government ID?** For developers like
  students and hobbyists who don't want to provide a government ID, we offer
  a limited distribution account (launching in August). This lets you share
  apps with up to 20 specific devices for testing and personal use at no cost
  and without ID verification. *Last updated: May 11, 2026*

## Package name registration and signing keys

- **I distribute my apps through Play and other channels** : To simplify the process, developers with a Play Console account can use it as the single place to manage all their verification requirements, including for their apps distributed outside of Play. *Last updated: Sept 3, 2025*
- **I use Play App Signing, are my apps claimed automatically?** Yes. If you use Play App Signing, we have the necessary information to securely identify your ownership. Your eligible apps will be part of the automatic registration process. *Last updated: Sept 3, 2025*
- **Can I recover a lost signing key?** We strongly recommend all developers use a secure key management solution. If you lose your signing key you won't be able to register your packages. *Last updated: March 23, 2026*
- **Can my app use multiple signing keys?** The Android Developer Console lets you add and verify multiple signing keys for a single package. *Last
  updated: March 23, 2026*
- **Can I register without an eligible key?** In cases where a package name is already in use, you may be informed that your key is not eligible to claim it outright. You should consider using a different package name. If this is not possible, you can request to register the package name, but this will require an additional review, and that package name may also be used by other developers. Last updated: *March 19, 2026*

## Advanced flow

- **Can users still sideload apps from unverified developers?** Yes. Android is introducing an advanced flow for power users who want to take educated risks to install apps from unverified developers. It's a **one-time** setup for users to install apps from unverified developers after acknowledging the risks. It's designed to protect user choice while adding in safeguards to protect users from being tricked or coerced into disabling security protections. Preview it in our [video](https://youtube.com/shorts/WcPElxbOeXY) or [blog post](https://goo.gle/advance-flow). *Last updated:
  March 23, 2026*
- **Can I still use independent app stores?** Yes. You can continue to use any alternative app store. For apps distributed on alternative app stores from verified developers, users won't see a change in their download experience at all. For apps distributed on alternative app stores from unverified developers, users can enable advanced flow with a one-time setup. *Last
  updated: May 11, 2026*
- **How does the advanced flow work for users?**

  - Enable developer mode in system settings: Activating this is
    [simple](https://www.android.com/intl/en_uk/articles/enable-android-developer-settings/). This prevents accidental triggers or "one-tap" bypasses
    often used in high-pressure scams.

  - Confirm you aren't being coached: There is a quick check to make sure
    that no one is talking you into turning off your security. While power
    users know how to vet apps, scammers often pressure victims into
    disabling protections.

  - Restart your phone and reauthenticate: This cuts off any remote access
    or active phone calls a scammer might be using to watch what you're
    doing.

  - Come back after the protective waiting period and verify: There is a
    one-time, one-day wait and then you can confirm that this is really you
    who's making this change with our biometric authentication (fingerprint or
    face unlock) or device PIN. Scammers rely on manufactured urgency, so
    this breaks their spell and gives you time to think.

  - Install apps: Once you confirm you understand the risks, you're all set
    to install apps from unverified developers, with the option of enabling for
    7 days or indefinitely. For safety, you'll still see a warning that the app
    is from an unverified developer, but you can just tap "Install Anyway."
    *Last updated: March 23, 2026*

- **Why is there a 24-hour waiting period to enable the advanced flow?** The
  waiting period is a defense against social engineering and coaching scams.
  Fraudsters often pressure victims into making immediate security changes
  while on a live call. This 24-hour pause breaks that sense of urgency and
  gives users time to verify the request independently. *Last updated: May 11,
  2026*

- **Are ADB installs impacted by the 24-hour waiting period for advanced
  flow?** No, there are no changes to how ADB works. You will be able to
  install applications using ADB as usual. The waiting period does not apply
  to ADB installs. *Last updated: March 23, 2026*

- **Do I need to keep Developer Mode on to keep this verification turned off?
  Some apps (e.g. banking, etc.) won't let me use it if I have Developer Mode
  on.** No, you don't have to keep developer options enabled after you enable
  the advanced flow. Once you make the change on your device, it's enabled.
  *Last updated: March 23, 2026*

- **If I enable the advanced flow on my current Android device, do I have to
  enable it again on my new device?** No, it will be carried through your new
  device. You won't have to complete this flow every time you get a new
  device. *Last updated: March 25, 2026*

- **Is there an ADB command to bypass the 24-hour waiting period?** This
  option is not supported at this point. We will consider this for future
  versions. *Last updated: March 25, 2026*

- **Can I update unregistered apps if I disable the advanced flow?**
  Unregistered apps can only be installed or updated when the advanced flow is
  enabled or by using ADB so if the advanced flow is disabled updates to
  unregistered apps will fail. *Last updated: March 25, 2026*

- **Can I update existing unregistered apps on my device without the use of
  the advanced flow and/or ADB?** No. Unregistered apps can only be installed
  or updated when the advanced flow is enabled or by using ADB so if the
  advanced flow is disabled updates to unregistered apps will fail. *Last
  updated March 25, 2026*

- **For apps that are being developed under NDA, won't going through Android
  developer verification and registering package names violate the NDA?** No.
  Verification is narrowly focused on the developer's identity to establish
  accountability. Android Developer Verification does not collect information
  about the app content or functionality so no confidential app content or
  purpose needs to be [shared](http://shared.In). *Last updated: March 25, 2026*

## I need additional support

**Where can I get help or provide feedback?** Your feedback is crucial for
helping us improve this process. [Reach out with any questions here](https://forms.gle/SXWXdFpteEWXNM1X6). For
additional information on these requirements, visit the [Android Developer
Console Help Center](https://support.google.com/android-developer-console) and the [Play Console Help Center](https://support.google.com/googleplay/android-developer#topic=16689288).