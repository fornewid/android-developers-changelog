---
title: Launch checklist  |  Play for Native PC  |  Android Developers
url: https://developer.android.com/games/playgames/native-pc/checklist
source: html-scrape
---

* [Home](https://developer.android.com/)
* [Play for Native PC](https://developer.android.com/games/playgames/native-pc)
* [Guides](https://developer.android.com/games/playgames/native-pc/setup)

# Launch checklist Stay organized with collections Save and categorize content based on your preferences.



Use this checklist to make sure your game meets all requirements and best
practices before you submit it for review on Google Play Games on PC.

## Set up and configure your project

* **Download and import the SDK:** Integrate the latest Play Games PC SDK for
  your environment. For more information, see the [Unity guide](/games/playgames/native-pc/unity/unity_start) or [C++
  guide](/games/playgames/native-pc/setup).
* **Create the application manifest:** Create a `manifest.xml` file mapping
  the `<PackageName>` to your claimed Play Console package. For more
  information, see the [Manifest guide](/games/playgames/native-pc/setup#step-2).
* **Digitally sign your executable:** Sign your game using an Authenticode
  Digital Signature and safeguard the certificate for all future updates.
  Although you can skip this step during local development by enabling
  developer mode, you must sign your final binary with an actual production
  certificate from a known certificate authority. For more information, see
  [Digitally sign your game](/games/playgames/native-pc/setup#step-3).
* **Format and send the certificate:** Send the [certificate information](https://support.google.com/googleplay/games-on-pc-developer/contact/new_title_onboarding)
  to your Google representative. The certificate file should only contain
  certificate-related information; verify all non-certificate blocks are
  removed. You can use OpenSSL to convert DER/CER files to the required PEM
  format.

## Integrate APIs and features

* **Initialize the SDK:** Implement SDK initialization logic, for example,
  `InitializeAsync`, during startup before you use other features. For more
  information, see the [Initialization guide](/games/playgames/native-pc/setup).
* **Implement seamless sign-in:** Authenticate players automatically using the
  Play Games client account through the Recall API. For more information, see
  the [Seamless Sign-In guide](/games/playgames/native-pc/pgs).
* **Integrate Play Integrity:** Use the `IntegrityClient` to request tokens
  and verify the legitimacy of game sessions on your backend. For more
  information, see the [Play Integrity guide](/games/playgames/native-pc/trust).
* **Add Play Install Referrer:** Integrate the Install Referrer API if you
  need to track user acquisition sources for PC. For more information, see the
  [Install Referrer guide](/games/playgames/native-pc/install_referrer).
* **Handle initialization errors:** To use the SDK, call
  `GooglePlayInitialize` (C++) or `GooglePlayInitialization.InitializeAsync`
  (C#) to initialize the API. You must call this and verify that the
  continuation callback completes with `InitializeResult::ok()` (C++) or
  `Result.IsOk` (C#) returns `true` before you can use any other API.
* **Handle mandatory shutdown:** Handle `kActionRequiredShutdownClientProcess`
  by shutting down the client process as soon as possible.
* **Handle Google Play Games installation requirements:** Handle
  `kSdkRuntimeUnavailable` by informing users that Google Play Games and the
  SDK runtime must be installed to proceed.
* **Handle Google Play Games updates:** Handle `kSdkRuntimeUpdateRequired` by
  notifying users that a Google Play Games runtime update is required.

**Note:** For specific Action and User Flow details for each error code, see
[InitializationError](/games/playgames/native-pc/reference/namespace/google/play/initialization#initializationerror).

## Implement Play Billing

* **Check purchase types:** Confirm your game relies only on in-app purchases,
  because recurring payments and subscriptions aren't supported. For more
  information, see the [Billing FAQ](/games/playgames/native-pc/faq).
* **Query product details:** Use `QueryProductDetails` to retrieve localized
  store data. If you have more than 50 products, split the request into
  multiple calls. For more information, see the [Query products guide](/games/playgames/native-pc/billing).
* **Launch the purchase flow:** Use `LaunchPurchaseFlow` to process
  transactions natively. A five-minute timeout error occurs if you close the
  payment browser without paying. For more information, see the [Purchase flow
  guide](/games/playgames/native-pc/billing).
* **Restore existing purchases:** Call `QueryPurchases` on startup and
  foregrounding to catch unacknowledged cross-device purchases. For more
  information, see the [Restore purchases guide](/games/playgames/native-pc/billing).
* **Secure backend processing:** Validate the `purchaseToken` on your backend
  before granting entitlements and finalizing with `AcknowledgePurchase` or
  `ConsumePurchase`. For more information, see the
  [Secure processing guide](/games/playgames/native-pc/billing).

## Test in developer mode and perform pre-launch QA

* **Test in developer mode:** Add `<IsDeveloperMode>true</IsDeveloperMode>` to
  your manifest and configure your early-access partner GUID for local
  integrated development environment (IDE) testing. If you don't have an
  early-access partner GUID, complete the [express interest form](/games/playgames/native-pc/setup/developer_mode#prerequisites).
* **Manage developer mode purchases:** When you test purchases in developer
  mode, consume the purchase within three minutes to prevent automatic
  refunds. For more information, see the [Testing FAQ](/games/playgames/native-pc/faq).
* **Remove developer mode:** You must remove the `<IsDeveloperMode>` tag
  before packaging your release build as soon as possible. For more
  information, see the [Developer mode guide](/games/playgames/native-pc/setup/developer_mode).
* **Forward arguments using third-party launchers:** Pass all unknown
  command-line arguments received by the launcher from the Google Play Games
  client directly to the spawned game process. For more information, see the
  [Multi-process guide](/games/playgames/native-pc/setup).
* **Test with a VPN:** If you test from an unsupported region, use a virtual
  private network (VPN) with TUN mode enabled to acquire a supported IP
  address. For more information, see the [VPN testing FAQ](/games/playgames/native-pc/faq).
* **Support desktop shortcuts:** For seamless shortcut support, see the
  [Shortcut FAQ](/games/playgames/native-pc/faq#create-game-shortcut) for shortcut execution. Directly launching the game or a
  third-party launcher using a shortcut might lead to initialization errors.

## Package, test, and publish your game

* **Package the WAB:** Use the Play Publishing Tool to package your game into
  a Windows App Bundle (WAB). The WAB file must be under the 10 GB file size
  limit. For more information, see the [Packaging guide](/games/playgames/native-pc/publish/developer-installed).
* **Submit third-party launcher installers:** If you use a third-party
  launcher, submit its installer inside the WAB. For more information, see the
  [Installer publishing guide](/games/playgames/native-pc/publish/developer-installed).
* **Update the game and launcher or installer:** Your package content,
  including launcher installers, must be self-updatable. Manage all resources
  your game needs, including updating the launcher itself.
* **Share launch information with Google:** Contact your Play partner and
  share your package name, launch countries (using ISO 2-character codes, for
  example US, CA, MX), and launch date and time in Coordinated Universal Time
  (UTC).
* **Set up testing access:** Provide an External Google Group to add to an
  allowlist for testing, documentation, and Google Drive access. Share an
  email list of test accounts with your Play partner, because Play Console
  Test Tracks aren't supported for PC.
* **Add the PC form factor:** Explicitly add the 'Google Play Games on PC' form
  factor to your app in the Google Play Console. If you can't access this tab,
  contact your Play partner to add your account to an allowlist.
* **Configure PC requirements:** Enter the hardware requirements (RAM, GPU,
  storage) for Windows PCs. For more information, see the [PC requirements
  guide](/games/playgames/native-pc/publish/developer-installed).
* **Upload store assets:** Upload your packaged WAB file to the
  **Production track** and configure visual assets. For more information, see
  the [Asset upload guide](/games/playgames/native-pc/publish/developer-installed).
* **Publish for user environment testing:** Select **Publish** in the Google
  Play Console. Unlike the Android version, selecting **Publish** on the WAB
  doesn't trigger a public release. Instead, it makes the app searchable for
  your shared test accounts to conduct tests in a user environment after
  Google's review process.
* **Launch officially:** Google controls the launch based on the official
  launch date you shared with your Play partner.

## Migrate from the API to the SDK

Migrating from the API to the SDK is an optional step. If you choose to migrate,
follow these recommendations:

* **Remove legacy REST APIs:** Map legacy Play Developer API calls (for
  example, `purchases.products.get`) to the client-side Native SDK functions.
  For more information, see the [Migration guide](/games/playgames/native-pc/migrate_api_sdk).
* **Verify command-line arguments:** Command-line arguments in the SDK
  environment might differ from those in the API environment. Verify that your
  package handles and passes all arguments correctly. For more information,
  see [Verify](/games/playgames/native-pc/migrate_api_sdk#command-line-arguments).
* **Verify the registry path:** For a seamless migration to the Native SDK,
  the registry configuration must remain consistent with previous versions.
  For more information, see the [WAB file guide](/games/playgames/native-pc/publish/developer-installed#convert-wab).

## See also

* [Frequently asked questions](/games/playgames/native-pc/faq)