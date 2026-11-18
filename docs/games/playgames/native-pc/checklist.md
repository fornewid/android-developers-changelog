---
title: https://developer.android.com/games/playgames/native-pc/checklist
url: https://developer.android.com/games/playgames/native-pc/checklist
source: md.txt
---

> Documentation index: https://developer.android.com/games/playgames/native-pc/llms.txt

Use this checklist to make sure your game meets all requirements and best
practices before you submit it for review on Google Play Games on PC.

## Set up and configure your project

- **Download and import the SDK:** Integrate the latest Play Games PC SDK for your environment. For more information, see the [Unity guide](https://developer.android.com/games/playgames/native-pc/unity/unity_start.md.txt) or [C++ guide](https://developer.android.com/games/playgames/native-pc/setup.md.txt).
- **Create the application manifest:** Create a `manifest.xml` file mapping the `<PackageName>` to your claimed Play Console package. For more information, see the [Manifest guide](https://developer.android.com/games/playgames/native-pc/setup.md.txt#step-2).
- **Digitally sign your executable:** Sign your game using an Authenticode Digital Signature and safeguard the certificate for all future updates. Although you can skip this step during local development by enabling developer mode, you must sign your final binary with an actual production certificate from a known certificate authority. For more information, see [Digitally sign your game](https://developer.android.com/games/playgames/native-pc/setup.md.txt#step-3).
- **Format and send the certificate:** Configure your certificate in Play Console, share the certificate information with your Google representative, or email [google-play-games-pc@google.com](mailto:google-play-games-pc@google.com) during onboarding. The certificate file must contain only certificate-related information; verify that all non-certificate blocks are removed. You can use OpenSSL to convert DER or CER files to the required PEM format.

## Integrate APIs and features

- **Initialize the SDK:** Implement SDK initialization logic, for example, `InitializeAsync`, during startup before you use other features. For more information, see the [Initialization guide](https://developer.android.com/games/playgames/native-pc/setup.md.txt).
- **Implement seamless sign-in:** Authenticate players automatically using the Play Games client account through the Recall API. For more information, see the [Seamless Sign-In guide](https://developer.android.com/games/playgames/native-pc/pgs.md.txt).
- **Integrate Play Integrity:** Use the `IntegrityClient` to request tokens and verify the legitimacy of game sessions on your backend. For more information, see the [Play Integrity guide](https://developer.android.com/games/playgames/native-pc/trust.md.txt).
- **Add Play Install Referrer:** Integrate the Install Referrer API if you need to track user acquisition sources for PC. For more information, see the [Install Referrer guide](https://developer.android.com/games/playgames/native-pc/install_referrer.md.txt).
- **Handle initialization errors:** To use the SDK, call `GooglePlayInitialize` (C++) or `GooglePlayInitialization.InitializeAsync` (C#) to initialize the API. You must call this and verify that the continuation callback completes with `InitializeResult::ok()` (C++) or `Result.IsOk` (C#) returns `true` before you can use any other API.
- **Handle mandatory shutdown:** Handle `kActionRequiredShutdownClientProcess` by shutting down the client process as soon as possible.
- **Handle Google Play Games installation requirements:** Handle `kSdkRuntimeUnavailable` by informing users that Google Play Games and the SDK runtime must be installed to proceed.
- **Handle Google Play Games updates:** Handle `kSdkRuntimeUpdateRequired` by notifying users that a Google Play Games runtime update is required.

> [!NOTE]
> **Note:** For specific Action and User Flow details for each error code, see [InitializationError](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/initialization.md.txt#initializationerror).

## Implement Play Billing

- **Check purchase types:** Confirm your game relies only on in-app purchases, because recurring payments and subscriptions aren't supported. For more information, see the [Billing FAQ](https://developer.android.com/games/playgames/native-pc/faq.md.txt).
- **Query product details:** Use `QueryProductDetails` to retrieve localized store data. If you have more than 50 products, split the request into multiple calls. For more information, see the [Query products guide](https://developer.android.com/games/playgames/native-pc/billing.md.txt).
- **Launch the purchase flow:** Use `LaunchPurchaseFlow` to process transactions natively. A five-minute timeout error occurs if you close the payment browser without paying. For more information, see the [Purchase flow guide](https://developer.android.com/games/playgames/native-pc/billing.md.txt).
- **Restore existing purchases:** Call `QueryPurchases` on startup and foregrounding to catch unacknowledged cross-device purchases. For more information, see the [Restore purchases guide](https://developer.android.com/games/playgames/native-pc/billing.md.txt).
- **Secure backend processing:** Validate the `purchaseToken` on your backend before granting entitlements and finalizing with `AcknowledgePurchase` or `ConsumePurchase`. For more information, see the [Secure processing guide](https://developer.android.com/games/playgames/native-pc/billing.md.txt).
- **Account for licensing key propagation delay:** When configuring new billing or licensing keys in the Play Console, allow several hours for the backend cache to synchronize across commerce serving environments before conducting live purchase tests. Purchases attempted before synchronization completes will return Error Code 6.

## Test in developer mode and perform pre-launch QA

- **Test in developer mode:** Add `<IsDeveloperMode>true</IsDeveloperMode>` to your manifest and configure your early-access partner GUID for local integrated development environment (IDE) testing. To start onboarding, email [google-play-games-pc@google.com](mailto:google-play-games-pc@google.com) for assistance with the next steps.
- **Manage developer mode purchases:** When you test purchases in developer mode, consume the purchase within three minutes to prevent automatic refunds. For more information, see the [Testing FAQ](https://developer.android.com/games/playgames/native-pc/faq.md.txt).
- **Remove developer mode:** You must remove the `<IsDeveloperMode>` tag before packaging your release build as soon as possible. For more information, see the [Developer mode guide](https://developer.android.com/games/playgames/native-pc/setup/developer_mode.md.txt).
- **Forward arguments using third-party launchers:** Pass all unknown command-line arguments received by the launcher from the Google Play Games client directly to the spawned game process. For more information, see the [Multi-process guide](https://developer.android.com/games/playgames/native-pc/setup.md.txt).
- **Test with a VPN:** If you test from an unsupported region, use a VPN with TUN mode enabled to acquire a supported IP address. For more information, see the [VPN testing FAQ](https://developer.android.com/games/playgames/native-pc/faq.md.txt).
- **Support desktop shortcuts:** For seamless shortcut support, see the [Shortcut FAQ](https://developer.android.com/games/playgames/native-pc/faq.md.txt#create-game-shortcut) for shortcut execution. Directly launching the game or a third-party launcher using a shortcut might lead to initialization errors.

## Package, test, and publish your game

- **Package the WAB:** Use the Play Publishing Tool to package your game into a Windows App Bundle (WAB). The WAB file must be under the 10 GB file size limit for Installer Publishing and 200 GB for Play Managed Publishing. For more information, see [Play Managed Publishing](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation.md.txt) or [Installer Publishing](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt).
- **Use the latest SDKs and tools:** Compile and package your release with the [latest versions](https://developer.android.com/games/playgames/native-pc/downloads) of the Play Games PC SDK, Play Games PC Unity SDK, Play PC developer tool, and Play publishing tool.
- **Confirm if elevation is required:** If your Installer, Launcher, or Uninstaller needs to be run as admin every time it is launched, remember to check whether you have set `INSTALLER_REQUIRES_ELEVATION`, `LAUNCHER_REQUIRES_ELEVATION`, or `UNINSTALLER_REQUIRES_ELEVATION` to `true`. Otherwise, they won't run with admin privileges, which will lead to startup failure. See [WAB Config File Format](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt#convert-wab) for more details.
- **Submit third-party launcher installers:** If you use a third-party launcher, submit its installer inside the WAB. For more information, see the [Installer publishing guide](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt).
- **Handle Auto-Play session token:** If you enable Auto-Play by setting `acceptsCommandLineArguments="true"` in `play_publishing_config.xml`, verify that your installer extracts the `--g_session_token=<token>` command-line argument and uses it to launch the game. Make sure your installer handles the fallback case where the token isn't present. For more information, see the [Launcher FAQ](https://developer.android.com/games/playgames/native-pc/faq.md.txt#Launcher).
- **Update the game and launcher or installer:** [Play Managed Publishing](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation.md.txt) automatically manages game updates. If you use [Installer Publishing](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt), your package content, including launcher installers, must be self-updatable and manage all resources your game needs, including updating the launcher itself.
- **Add the PC form factor:** In Play Console, go to **Test and
  release \> Advanced settings \> Form factors and platforms** and click **Add
  Windows** in the **Windows** section. If the **Windows** option isn't visible, you need to onboard your account first. **Prepared to start
  onboarding?** Reach out by email to [google-play-games-pc@google.com](mailto:google-play-games-pc@google.com). The onboarding specialists will assist you with the next steps.
- **Configure PC requirements:** Enter the hardware requirements (RAM, GPU, storage) for Windows PCs and agree to the review policy in Play Console. For more information, see the [PC requirements guide](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation.md.txt#configure-windows-pc).
- **Set up testing access:** Configure up to 100 testers on the **Google Play Games on PC** **Internal testing** track in Play Console (**Test and release \> Testing \> Internal
  testing** ) and upload your `.wab` file. Testers must accept the opt-in web link and install the build using `googleplaygames://deeplink/details?id=PACKAGE_NAME`. Closed and open testing tracks aren't supported on Windows.
- **Upload store assets and submit to production:** Upload your **Google Play Games on PC** store listing assets, select target countries that match or are a subset of your Android targeting, and submit your `.wab` file on the **Google Play Games on PC** **Production** track (**Test and
  release \> Production** ). Reviews take up to seven days. For more information, see the [Production publishing guide](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation.md.txt#send-review).
- **Control your launch timing:** Use **Managed publishing** on the **Publishing overview** page in Play Console to control when your approved release goes live.
- **Test during pre-registration:** During the pre-registration phase, you must conduct internal testing in a country that is not included in your selected pre-registration regions.
- **Verify installer process termination:** confirm that the primary installer process remains active until all of the required registry keys are created and registered. If the process exits prematurely, then installation verification fails. For more information, see [Installer publishing](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt).
- **Maintain consistent registry hives and clean up on uninstall:** Google Play Games on PC checks `HKEY_LOCAL_MACHINE` before `HKEY_CURRENT_USER` and uses the first matching value. Keep the registry hive consistent across updates and shared-launcher titles, and remove registry keys during uninstallation so stale `HKEY_LOCAL_MACHINE` entries don't shadow valid `HKEY_CURRENT_USER` paths. For more information, see [Installer publishing](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt).

## Migrate from the API to the SDK

Migrating from the API to the SDK is an optional step. If you choose to migrate,
follow these recommendations:

- **Remove legacy REST APIs:** Map legacy Play Developer API calls (for example, `purchases.products.get`) to the client-side Native SDK functions. For more information, see the [Migration guide](https://developer.android.com/games/playgames/native-pc/migrate_api_sdk.md.txt).
- **Verify command-line arguments:** Command-line arguments in the SDK environment might differ from those in the API environment. Verify that your package handles and passes all arguments correctly. For more information, see [Verify](https://developer.android.com/games/playgames/native-pc/migrate_api_sdk.md.txt#command-line-arguments).
- **Verify the registry path:** For a seamless migration to the Native SDK, the registry configuration must remain consistent with previous versions. For more information, see the [WAB file guide](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt#convert-wab).

## See also

- [Frequently asked questions](https://developer.android.com/games/playgames/native-pc/faq.md.txt)