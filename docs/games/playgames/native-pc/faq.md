---
title: https://developer.android.com/games/playgames/native-pc/faq
url: https://developer.android.com/games/playgames/native-pc/faq
source: md.txt
---

This document answers common questions about SDKs and publishing for Google Play Games on PC.

## Monetization

1. Can I use the purchase flow without a backend server?

   From a security perspective, Google recommends using a backend server.

   For more information, see [Process without a backend server](https://developer.android.com/games/playgames/native-pc/billing#process-no-backend).

   > [!NOTE]
   > **Note:** To process purchases without a backend server, you need special permissions. If your game requires these permissions, contact your Google partner.

2. Are existing API-based payment systems allowed after integrating the Google Play Games on PC SDK?

   All payments must be handled by Google Play Games on PC SDK using the
   Google Play Billing. You cannot use your existing API-based payment method
   in the same game.
3. How can we consume purchases in developer mode?

   Consume purchase in the developer mode within 3 minutes, otherwise the
   purchase will be refunded.
4. Are recurring payments or subscriptions supported?

   Not for the immediate future although you are welcome to provide specific
   use cases for us to add into our future roadmap.
5. What is the Billing Error in my purchase calls?

   [BillingError](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/billing#billingerror) is the response of the payment result. LaunchPurchaseFlow
   will return immediately without blocking but you must listen to the callback
   in order to know when it has finished and to capture the result.
6. How can I use client-side purchase verification?

   We recommend using server-side purchase and its verification process.
   Processing purchases from your client app requires your game to be on an
   allowlist. Please contact your Google Partner if your game requires access.
   For more information, see [Process without a backend server](https://developer.android.com/games/playgames/native-pc/billing#process-no-backend).
7. What are the API limits for querying product details?

   The maximum number of products that can be queried in a single call to the
   [`QueryProductDetails`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#queryproductdetails) API is 50. If you exceed this limit, you must
   split the request into multiple calls.
8. What parameters are required when calling Query Purchases or Launch Purchase
   Flow in the Billing Client?

   The function accepts `QueryPurchasesContinuation`, which is a function
   callback with the `std::function<void(QueryPurchasesResult)>` signature. The
   callback passes the result to you with all the `ProductPurchaseDetails`.
   This information is available in the SDK header files in the
   `includes/billing/models.h` file.

   The resulting `launch_purchase_flow_result` has `ok()` and `code()`
   functions. The `ok()` function returns whether the flow is successful. The
   `code()` function returns the `BillingError` enum
   (`includes/billing/enums.h`), which has 10 possible error cases, such as
   user canceled or network error.
9. Is a custom ordering supported for the Launch Purchase Flow in the Billing
   Client?

   In the current SDK design, there is no way to pass in your own payload.
   However, you can provide any combination of `obfuscated_account_id` and
   `obfuscated_profile_id`. You can provide none, just one, or both.

   The `offer_token` field is required and specifies the purchase offer that
   the user is attempting to buy in the checkout flow. For now, each SKU in
   Google Play has exactly one offer (for example, buy one item for $10). In
   the future, the Play billing team will provide support for multiple offers.

   To ensure metadata is associated in the case of purchase flow interruptions,
   store the metadata on your backend server prior to launching the purchase
   dialog and associate it with your user's account ID, the SKU being
   purchased, and the current timestamp. For more information, see
   [Associate a purchase with internal data](https://developer.android.com/google/play/billing/developer-payload#associate).
10. What are the prerequisites for switching from Google billing with OAuth to
    the DLL-based Google billing?

    Games can continue to use the OAuth sign-in with Google to manage the
    signed-in account, but Google recommends that you stop using the legacy REST
    billing APIs. Switching from the REST billing APIs (with OAuth2 sign-in) to
    the SDK flow can be a feature-flagged operation, so both can coexist for a
    period of time while the game switches over.
11. Is the Launch Purchase Flow API call processed through a web browser?

    No, the purchase flow is now completed entirely in-game using a seamless
    WebView overlay, without leaving the game client.
12. Does a user need to sign in separately for each game to make a purchase?

    The foreground account in Google Play Games is used for each game session,
    so you don't need to sign in again. The account that you use in Google Play
    Games when the game session starts is the account that API calls are issued
    as. The purchase flow will use this account automatically.
13. Can a game support both the PC SDK and legacy payment systems at the
    same time?

    The payment system operates under a dual-flow model depending on the game
    binary version. Users on legacy builds continue on the existing flow, and
    users on new builds transition to SDK-based payments. Users on both payment
    flows coexist during the transition period.

## Windows App Bundle

1. When submitting a WAB using a 3P launcher, is the game package required for
   review?

   You can just submit your installer and don't need to submit your entire game
   package, the reviewer will be able to download your game package using the
   installer.

   > [!NOTE]
   > **Note:** This guidance is specifically for developers using a 3P launcher to call your game.

2. Are there any limitations of WAB file size?

   You can upload up to 10 GB file size for a WAB.
3. Why isn't my game installing or appearing after I uploaded my WAB?

   If your game is being onboarded without a pre-existing PC version (a "first-
   time WAB"), the system may automatically place it into a Managed Publishing
   holding state. This happens because there is no existing baseline to update.
   To fully release the WAB and make the game available for installation, you
   must navigate to the Google Play Console and manually execute the
   [required publish action](https://developer.android.com/games/playgames/native-pc/publish/developer-installed#send-review) (for example, click "Publish changes").
4. How do I upload the WAB for internal testing?

   Share the allowlist accounts with Google so Google can enable them for
   internal testing. After Google has the list, Google makes sure they are
   included in the onboarding process.
5. Where should the WAB package be uploaded?

   You can upload the WAB package at the location mentioned in the first
   question. However, you cannot publish it manually. You must provide the
   Google backend staff with a precise UTC time (down to the hour). Google then
   configures the release schedule and ensures it is published on time.

## PC SDK

1. What are the differences between the Legacy API and
   Google Play Games on PC SDK?

   - The legacy API only offers billing functionality.
   - The PC SDK supports Google Desktop Service (GDS) and full PC features.
   - No browser-based Google Sign-in is required with the PC SDK.
2. Is there an alternative way to initialize the SDK by launching the game
   directly using the game launcher, without going through Google Play Games on PC?

   Your game must be launched through the Google Play Games on PC client. For
   more details, refer to this [developer document](https://developer.android.com/games/playgames/native-pc/setup#step-4).
3. Does the PC SDK support multibyte characters in the PEM certification
   file?

   Yes, the SDK supports multibyte characters for certification.
4. How does the SDK handle Google Account sign-in for multiple instances or
   accounts?

   Each game launch in Google Play Games is treated as a "game session" and
   each "game session" can have an account associated with it. They can be
   different. So if you launch the game with account A, and then switch to
   account B and relaunch both can run at the same time.
5. Does the Play Install Referrer integration work with the PC SDK?

   The PC SDK (25.5.409.0 and higher) supports the Play Install Referrer API.
   For more information, see [Play Install Referrer API](https://developer.android.com/games/playgames/native-pc/install_referrer).

## Launcher

1. If a player uses a 3P launcher instead of the Google Play Client, will their
   Play Games Services account sync automatically?

   For the SDK functions to operate, the game must be launched directly through
   the Google Play Games client. If another process, such as an installer or
   launcher application, initiates the game, then that process must itself be
   launched from the Google Play Games client. The game must pass all
   parameters received from the client to the client process.
2. How do I handle initialization if Google Play Games launches a third-party
   game launcher?

   You are not required to integrate the SDK directly into your launcher.
   However, you must pass all command-line arguments received by the launcher
   from the Google Play Games client directly to the spawned child process (the
   game executable). If initialization fails (for example, by returning
   `kActionRequiredShutdownClientProcess`), all processes including the
   launcher must be terminated so Google Play Games can attempt to recover and
   relaunch the game automatically. For more details, see
   [Step 5 in the setup guide](https://developer.android.com/games/playgames/native-pc/setup#step-5).
3. How can I handle updates and maintenance to my game and launcher after it is
   in production?

   Subsequent updates and maintenance must be implemented through your
   launcher. The Google Play Games client does not support update functions, so
   the launcher must be capable of updating both the game and the launcher
   itself.
4. How does the installer receive the GPG session token for Auto-Play?

   GPG passes the session token using the `--g_session_token=<token>`
   command-line argument to the installer. To enable this, you must set
   `acceptsCommandLineArguments="true"` in your `play_publishing_config.xml`.

   The installer is responsible for extracting this token and using it to
   launch the game. If the token generation fails, GPG launches the installer
   without the token (fallback).

## Initialization

1. When I start a game using the Google Play Games app, does it sync my Google
   Account details?

   After launching the game through Google Play Games client, the account is
   automatically synchronized and there's no need to login through the Google
   Login process again.
2. Is it possible to reuse the initialization parameters multiple times?

   This is possible as long as the Google Play Games client is running and the
   login information is valid. However, in scenarios like the one described in
   the guide, all processes launched by the game must be terminated when the
   user closes the game or the game exits due to an SDK initialization failure,
   such as `kActionRequiredShutdownClientProcess`.
3. Is there any way to create a shortcut to open the game directly?

   You can use the following URI for opening the game directly:

   `googleplaygames://launch/?pid=2&id=com.company.gamename`

   The URI supports detecting whether the Google Play Games on PC client is
   opened. If the client is not open, the Google Play Games client opens before
   the game or launcher runs. You need to manage the game or launcher to
   prevent multiple instances from running.
4. Is there any way to verify the Google Play Games on PC installation without
   using the SDK?

   You can verify the installation status of Google Play Games on PC without
   integrating the SDK by checking for the presence of the following Windows
   Registry key:

   `HKEY_LOCAL_MACHINE\SOFTWARE\Google\Play Games Services`

   The presence of this key indicates that the Google Play Games services
   (required to run games on PC) are installed on the machine. If the key is
   missing, you should direct the user to the
   [Google Play Games on PC installation page](https://play.google.com/googleplaygames) to download and install the
   client.

## Testing

1. Are there any open testing or closed testing environments similar to the
   mobile?

   While a dedicated end-to-end sandbox isn't available, we recognize the need
   for a production-like testing environment for developers. A more robust
   solution will be offered soon.
2. How can I add new testers?

   Your Google point of contact creates an email group for each PC project,
   where the testers' Google Accounts must be added. Only members of this email
   group are authorized to download the test packages within Google Play Games.

## Miscellaneous

1. Can I use a VPN?

   For developers requiring to test their game in [regions](https://support.google.com/googleplay/answer/11358071#zippy=%2Ccountryregion-availability) where Google Play Games on PC is not supported, we recommend that you use a VPN to
   acquire an IP address from a [supported region](https://support.google.com/googleplay/answer/11358071).

   Ensure that you enable [TUN mode](https://proprivacy.com/guides/tun-tap) on VPN. Guidance on enabling TUN mode
   and configuring the firewall can be found in the VPN provider's operating
   manual.

   After the TUN mode is enabled, [install](https://play.google.com/googleplaygames/?e=WebskySupportFCCInFCP::Arm_Launch) the Google Play Games on PC and
   the [emulator](https://developer.android.com/games/playgames/emulator) for testing purposes.
2. How can I start developing for Google Play Games on PC in Unity or UE
   Editor?

   - Enable the [developer Mode](https://developer.android.com/games/playgames/native-pc/setup/developer_mode) and proceed with testing.
   - Add the `manifest.xml` and `.dll` files. For more information, see [developer document](https://developer.android.com/games/playgames/native-pc/setup#prerequisites).
   - Register an [early access partner GUID](https://developer.android.com/games/playgames/native-pc/setup/developer_mode#step-2) for testing purposes.
3. How can I use registry keys correctly?

   You should create registry keys based on the root hive. You can set the root
   hive as either `HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_USER` depending on your
   purpose and the nature of the data. The `HKEY_LOCAL_MACHINE` hive is used as
   an example in the guidelines.
4. What are the requirements for Google's review of PC packages?

   PC packages undergo malware scanning, after which reviewers test only the
   game installation, successful startup, and uninstallation processes.
5. Is it necessary to integrate all APIs?

   Other APIs are not required, but they offer additional benefits.
   `google::play::billing` is required for in-app purchases and selling digital
   content. `google::play::install_referrer` is required for tracking referral
   data to help you understand which traffic sources send the most users to
   download your app. `google::play::games::integrity` is required to protect
   your app from bad actors by detecting potentially risky devices and unknown
   emulators.
6. Why are some game processes terminated when the Google Play Games client is
   closed, while others are not?

   Google doesn't control the sub processes or processes of the running game.
   The behavior depends on whether the game is an emulated Android game or a
   PC game. Emulated games are installed inside their own environment,
   so their behavior depends largely on emulator initialization and shutdown.
7. Should I use Google Play Games uninstallation capability or a custom
   uninstaller?

   Google recommends using our Google Play Games uninstallation capability.

## Further assistance

If you need further help not covered in this FAQ, please reach out to
[google-play-games-pc@google.com](mailto:google-play-games-pc@google.com)