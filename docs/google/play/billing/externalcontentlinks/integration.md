---
title: https://developer.android.com/google/play/billing/externalcontentlinks/integration
url: https://developer.android.com/google/play/billing/externalcontentlinks/integration
source: md.txt
---

This document describes how to integrate the Play Billing Library APIs to offer external content links in eligible apps. This includes the ability to link users in the US outside your Play app to provide users with offers to in-app digital content and app downloads. To learn more about this program, see[program requirements](https://support.google.com/googleplay/android-developer/answer/16470497).

## Play Billing Library setup

[Add the Play Billing Library dependency](https://developer.android.com/google/play/billing/getting-ready#dependency)to your Android app. To use the[external links](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener))APIs you need to use version 8.2.1 or higher. If you need to migrate from an earlier version, follow the instructions in the[migration guide](https://developer.android.com/google/play/billing/migrate-gpblv8)before adding the external content links.

## Initialize the billing client

To initialize the billing client follow the same steps as described in[Initialize a`BillingClient`](https://developer.android.com/google/play/billing/integrate#initialize)with the following modifications:

- Don't enable the`PurchasesUpdatedListener`- this listener is not needed for external content links.
- Call`enableBillingProgram()`with`BillingProgram.EXTERNAL_CONTENT_LINK`to indicate that your app uses the external content links.

The following example shows initializing a`BillingClient`with these modifications:  

### Kotlin

    val billingClient = BillingClient.newBuilder(context)
      .enableBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
      .build()

### Java

    private BillingClient billingClient = BillingClient.newBuilder(context)
        .enableBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
        .build();

## Connect to Google Play

After you initialize the`BillingClient`, connect to Google Play as described in[Connect to Google Play](https://developer.android.com/google/play/billing/integrate#connect_to_google_play).

## Check user eligibility

After you connect to Google Play, you must check if the user is eligible for the external content links program by calling the[`isBillingProgramAvailableAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener))method. This method returns`BillingResponseCode.OK`if the user is eligible for external content links program. The following sample shows how to check the user eligibility for external content links:  

### Kotlin

    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_CONTENT_LINK,
      object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
          billingProgram: Int, billingResult: BillingResult) {
            if (billingResult.responseCode !=  BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external content links unavailable, etc.
                return
            }

            // External content links are available. Prepare an external
            // transaction token.
          }
        })

### Java

    billingClient.isBillingProgramAvailableAsync(
      BillingProgram.EXTERNAL_CONTENT_LINK,
      new BillingProgramAvailabilityListener() {
        @Override
        public void onBillingProgramAvailabilityResponse(
          int billingProgram, BillingResult billingResult) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external content links unavailable, etc.
                return;
            }

            // External content links are available. Prepare an external
            // transaction token.
          }

        });

See the[response handling](https://developer.android.com/google/play/billing/externalcontentlinks/integration#response-handling)section for details on how your app should respond to other response codes. If you're[using Kotlin extensions](https://developer.android.com/google/play/billing/integrate#dependency), you can use Kotlin coroutines so you don't have to define a separate listener.

## Prepare an external transaction token

Next, you must generate an external transaction token from the Play Billing Library. A new external transaction token must be generated each time the user visits an external website through the external links API. This can be done by calling the[`createBillingProgramReportingDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener))API. The token should be generated immediately before the user is linked out.

**Note**: The external transaction token should never be cached and you should generate a new token each time the user is linked out.  

### Kotlin

    val params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
            .build();

    billingClient.createBillingProgramReportingDetailsAsync(
      params,
      object : BillingProgramReportingDetailsListener {
        override fun onCreateBillingProgramReportingDetailsResponse(
          billingResult: BillingResult,
          billingProgramReportingDetails: BillingProgramReportingDetails?) {
            if (billingResult.responseCode !=  BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return
            }
            val externalTransactionToken =
                billingProgramReportingDetails?.externalTransactionToken
            // Persist the external transaction token locally. Pass it to the
            // external website when launchExternalLink is called.
        }
      })

### Java

    BillingProgramReportingDetailsParams params =
        BillingProgramReportingDetailsParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
            .build();

    billingClient.createBillingProgramReportingDetailsAsync(
      params,
      new BillingProgramReportingDetailsListener() {
        @Override
        public void onCreateBillingProgramReportingDetailsResponse(
          BillingResult billingResult,
          @Nullable BillingProgramReportingDetails
            billingProgramReportingDetails) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return;
            }

            String transactionToken =
              billingProgramReportingDetails.getExternalTransactionToken();

            // Persist the external transaction token locally. Pass it to the
            // external website when launchExternalLink is called.
          }
      });

If you're[using Kotlin extensions](https://developer.android.com/google/play/billing/integrate#dependency), you can use Kotlin coroutines so you don't have to define a separate listener.

## Launch the external link

After the external transaction token is ready, the user may be linked outside of the app to a digital content offer or app download by calling[`launchExternalLink`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener))method. Google Play might render additional information dialogs to the user depending on their user settings when you call this API.

When calling the`launchExternalLink`method, details of the external link must be provided through[`LaunchExternalLinkParams`](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams). This class contains the following parameters:

- **Link URI**- The link to the external website where the digital content or app download is offered. For app downloads, this link must be registered and approved in the Play Developer Console.
- **Link Type**- The type of content being offered to the user.
- **Launch Mode** - Specifies how the link is launched. For app downloads, you must set this to`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`.
- **Billing Program** - Set this to`BillingProgram.EXTERNAL_CONTENT_LINK`.

### Kotlin

    val params =
      LaunchExternalLinkParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
        .setLinkUri(Uri.parse("https://www.myapprovedsite.com"))
        .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
        .setLaunchMode(
          LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
        .build()

    val listener : LaunchExternalLinkResponseListener =
        object : LaunchExternalLinkResponseListener {
          override fun onLaunchExternalLinkResponse(
            billingResult: BillingResult) {
            if (billingResult.responseCode !=  BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return
            }

            // If Launch Mode was set to LAUNCH_IN_EXTERNAL_BROWSER_OR_APP, the
            // user was directed outside of the app by Play. This does not give
            // any information on the user's actions during the link out, such
            // as if a transaction was completed.

            // If Launch Mode was set to CALLER_WILL_LAUNCH_LINK, then your app
            // may proceed to direct the user to the external website.
        }
    }

    billingClient.launchExternalLink(activity, params, listener)

### Java

    LaunchExternalLinkParams params =
      LaunchExternalLinkParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
        .setLinkUri(Uri.parse("https://www.myapprovedsite.com"))
        .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
        .setLaunchMode(
          LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
        .build()

    LaunchExternalLinkResponseListener listener =
      new LaunchExternalLinkResponseListener() {
        @Override
        public void onLaunchExternalLinkResponse(BillingResult billingResult) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return;
            }

            // If Launch Mode was set to LAUNCH_IN_EXTERNAL_BROWSER_OR_APP, the
            // user was directed outside of the app by Play. This does not give
            // any information on the user's actions during the link out, such
            // as if a transaction was completed.

            // If Launch Mode was set to CALLER_WILL_LAUNCH_LINK, then your app
            // may proceed to direct the user to the external website.
        }
      }

    billingClient.launchExternalLink(activity, params, listener);

## Response handling

When an error occurs, the methods`isBillingProgramAvailableAsync()`, and`createBillingProgramReportingDetailsAsync()`, and`onLaunchExternalLinkResponse()`might provide a`BillingResponseCode`other than`BillingResponseCode.OK`. Consider handling these response codes as follows:

- `ERROR`: This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling the API again or by calling`launchExternalLink()`the next time you attempt to direct the user outside the app.
- `FEATURE_NOT_SUPPORTED`: The external content link APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- `USER_CANCELED`: Don't proceed with opening the external website. Call`launchExternalLink()`again the next time you attempt to direct the user outside of the app.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for external content links and therefore don't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be handled with an appropriate retry policy. In the case of`SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external content links

License testers should be used to test your external offers integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See[Test in-app billing with application licensing](https://support.google.com/googleplay/android-developer/answer/6062777)for more information on configuring license testers.

## Next steps

After you've finished in-app integration, you're ready to[integrate your backend](https://developer.android.com/google/play/billing/outside-gpb-backend).