---
title: https://developer.android.com/registered-app-stores/requirements
url: https://developer.android.com/registered-app-stores/requirements
source: md.txt
---

A Registered App Store is a third-party app store that completes formal
verification with Android to deliver a one-tap installation experience while
upholding core ecosystem trust, security, and performance standards.

Participating Registered App Stores must comply with the following requirements:

### 1. Developer eligibility

- **Registered organization:** App stores must be registered as an organization through the Android Developer Console.
- **Android developer verification:** App store developers must complete and maintain verified status under Android developer verification.
- **Package name ownership:** The store's package name must be registered in Android Developer Console.
- **Native Android app:** The store must be distributed as a standalone Android package (APK). Purely web-based wrappers or non-APK installation mechanisms are not eligible.

### 2. Operate as a legitimate marketplace

- **Open access:** Function as an open third-party marketplace for all eligible developers with clear, non-discriminatory policies. App stores that choose to allow advertising must permit developers to integrate any ad network that complies with the store's own applicable trust and safety network that complies with the store's own applicable trust and safety policies.
- **Developer authorization:** Maintain direct contractual relationships with developers, including written authorization, license rights, and permissions necessary to distribute apps and their content.
- **Intellectual property (IP) compliance:** Respect IP rights, maintain a clear process and external-facing functional channel for handling IP disputes, and don't engage in impersonation.

### 3. Provide a transparent user experience

- **Primary purpose and consumer interface:** The app store's primary function must be the discovery, installation, and management of apps. The store must provide a consumer-facing destination with a dedicated launcher icon that is explicitly installed by the user.
- **Discovery:** The store must allow users to browse all listed apps through a user interface.
  - **Uninstallation:** Users must have the option to uninstall an app directly from the same listing or management page used to install it.
  - **App delivery and updates:** App stores must reliably deliver updates to apps it has installed on the device whenever newer versions become available.
  - **App archiving:** App stores must [support the archiving](https://developer.android.com/about/versions/15/features#app-archiving) and the restore of archived apps feature for appropriate Android versions. Users must have the option to turn on / off the feature.
  - App stores must be self-updatable.
- **Clear app information:** App listing pages must display clear and relevant information to help users evaluate content before installation, including but not limited to:
  - App name and developer name
  - Clear description of functionality
  - Version code or name and download size
  - A [data safety section](https://developer.android.com/about/versions/14/features/app-metadata#data-types-purposes) detailing collection, use, and sharing of user data using the App Metadata Bundle (effective date: Dec 1, 2027)
  - Applicable legal and safety disclosures
  - Valid developer contact information
- **User control:** Ensure app installations and ownership changes occur only with explicit user consent and provide clear user controls for automatic or manual updates. App stores must not install apps silently without user consent. For background and remote downloads and installs, they should notify the user about the download or install progress and completion appropriately. If an app installation was initiated on another device, the store must display a notification to the user that does not close automatically.
- **Ecosystem non-interference:** App stores must not interfere with, disrupt, damage, or access in an unauthorized manner the user's device, other devices or computers, servers, networks, application programming interfaces (APIs), or services, including but not limited to other apps on the device, any Google service, or an authorized carrier's network. For example, it must not block the installation of other app stores, interfere with other stores, or suppress or manipulate operating system security notifications.
- **Ads experience:** App stores and their app catalog must not display disruptive off-screen or out-of-context advertisements.
- **User support channels:** Offer direct and accessible customer support channels.
- **Platform requirements:**
  - App stores must handle the required intents for app stores.
  - The store must declare `INSTALL_PACKAGES_AS_REGISTERED_APP_STORE`.
  - The store must declare the `REQUEST_INSTALL_PACKAGES` permission.
  - The store must ensure it fixes major security vulnerabilities surfaced to them.

### 4. Ensure ecosystem trust and safety

- App stores must define objectionable content and behaviors in their terms and trust and safety policies and publish those terms and policies. Stores must moderate their catalog and enforce policy violations.
- **Security:** Proactively and in good faith prevent the distribution of malware and Potentially Harmful Apps (PHAs) and prohibit illegal or fraudulent activity through robust policy enforcement. If more than 1% of install attempts or 2% of apps in the catalog over a 30 day period are found to be PHA, Google will assess variable fees required to screen and remediate high-risk catalogs.
- **Privacy and compliance:** Publish and in good faith enforce clear privacy policies, don't violate applicable laws and regulations (for example, COPPA, CCPA), and manage government requests appropriately.
  - The store must provide an operational channel to receive and process government and legal removal requests.
- **User Safety:** Provide parental controls as required by law and enforce policies against deceptive or disruptive practices.
- **App Defense Alliance Certification:** App stores must achieve and annually renew certification under the [App Defense Alliance (ADA) Mobile Profile](https://www.appdefensealliance.org/certification/certified-products)
  - MASA certification AL2, demonstrating adherence to established industry cybersecurity baselines. (Effective date: June 1, 2027)
- App stores must integrate with the catalog submission API to share its store APK and catalog APKs with Google for security scanning. For more information, see [Submit your app
  catalog](https://developer.android.com/registered-app-stores/enroll#submit-your-app-catalog).
- App stores must adhere to applicable laws \& regulations including but not limited to age assurance and minor protection. Stores whose primary purpose is, or become used primarily for, hosting objectionable content such as Child Sexual Abuse Material (CSAM), non-consensual intimate imagery (NCII), terrorist content, or systemic financial fraud are not allowed and will face immediate deregistration.
- App stores remain responsible and liable for their entire catalog. Google won't moderate the content available within registered app stores.

### 5. Ensure technical health

- **Target API requirements:** On any device where the store is installed, the store APK must target an SDK level at minimum N-1 to get the RAS experience, where N is the major SDK version of the device. Minor versions are not considered here. For example, an app store continuing to target version 2.0 even after the release of 3.1 will still get the RAS experience if they are eligible.
- **Memory consumption limit:** Starting December 1, 2027, RAS must have a memory consumption limit policy in place to ensure good device health.
- **Technical requirements:** Registered App Stores must meet technical requirements updated annually to reflect evolving OS and technologies, and ensure ecosystem health.

Failure to meet any of these requirements, including non-payment of invoices by
the due date, may result in Android removing your app store from the program
until the issues are resolved. Android will provide advance notice with an
opportunity to remediate the issues prior to taking action.

Registered App Store requirements will evolve as the Android ecosystem improves
and adds new features to best serve users.

## Submit the interest form

After reviewing the requirements, submit the [Registered App Store Interest
Form](https://support.google.com/android-developer-console/contact/registered_app_store_interest_form).

## Next Steps

Once your interest application is accepted, you will receive information to
continue with registration as outlined in the [Enrollment guide](https://developer.android.com/registered-app-stores/enroll).