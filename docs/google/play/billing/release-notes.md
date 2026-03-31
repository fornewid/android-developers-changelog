---
title: Google Play Billing Library release notes  |  Android Developers
url: https://developer.android.com/google/play/billing/release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Monetization](https://developer.android.com/google/play/billing)

Send feedback

# Google Play Billing Library release notes Stay organized with collections Save and categorize content based on your preferences.



This document contains release notes for the Google Play Billing Library.

## Google Play Billing Library 8.3.0 Release (2025-12-23)

Version 8.3.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

* New APIs for [external payments](/google/play/billing/externalpaymentlinks):

  + Added classes to support external payments flow:
    - [`BillingProgram.EXTERNAL_PAYMENTS`](/reference/com/android/billingclient/api/BillingClient.BillingProgram#EXTERNAL_PAYMENTS)
    - [`EnableBillingProgramParams`](/reference/com/android/billingclient/api/EnableBillingProgramParams)
    - [`DeveloperBillingOptionParams`](/reference/com/android/billingclient/api/DeveloperBillingOptionParams)
    - [`DeveloperProvidedBillingDetails`](/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails)
    - [`DeveloperProvidedBillingListener`](/reference/com/android/billingclient/api/DeveloperProvidedBillingListener)
  + Added [`enableBillingProgram(EnableBillingProgramParams)`](/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)) to enable
    external payments.
  + Added [`BillingFlowParams.Builder.enableDeveloperBillingOption`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#enableDeveloperBillingOption(com.android.billingclient.api.DeveloperBillingOptionParams)) to
    launch the external payments flow.

## Google Play Billing Library 8.2.1 Release (2025-12-15)

Version 8.2.1 of the Google Play Billing Library and Kotlin extensions are now
available.

### Bug fixes

* Fixed a bug in [`isBillingProgramAvailableAsync`](/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) and
  [`createBillingProgramReportingDetailsAsync`](/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)). Update to version 8.2.1
  to use these APIs introduced in 8.2.0.

## Google Play Billing Library 8.2.0 Release (2025-12-09)

Version 8.2.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

* New APIs for [external content links](/google/play/billing/externalcontentlinks) and [external offers](/google/play/billing/external):

  + Added [`enableBillingProgram`](/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(int)) to setup the `BillingClient` for
    these programs.
  + Added [`isBillingProgramAvailableAsync`](/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)) to determine user eligibility.
  + Added [`createBillingProgramReportingDetailsAsync`](/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)) to create the
    external transaction token that must be used for reporting.
  + Added [`launchExternalLink`](/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)) to initiate the external link to
    a digital content offer or an app download.
* Changes to the [external offers program](/google/play/billing/external):

  + There are policy changes for the external offers program. See
    [program changes](https://support.google.com/googleplay/android-developer/answer/16505463) for details. To understand how to launch
    external offer flows with the new APIs, see the [integration guide](/google/play/billing/external/integration).
  + Deprecated the [`BillingClient.Builder.enableExternalOffer`](/reference/com/android/billingclient/api/BillingClient.Builder#enableExternalOffer()) API.
  + Deprecated the [`isExternalOfferAvailableAsync`](/reference/com/android/billingclient/api/BillingClient#isExternalOfferAvailableAsync(com.android.billingclient.api.ExternalOfferAvailabilityListener)) API.
  + Deprecated the [`createExternalOfferReportingDetailsAsync`](/reference/com/android/billingclient/api/BillingClient#createExternalOfferReportingDetailsAsync(com.android.billingclient.api.ExternalOfferReportingDetailsListener)) API.
  + Deprecated the [`showExternalOfferInformationDialog`](/reference/com/android/billingclient/api/BillingClient#showExternalOfferInformationDialog(android.app.Activity,com.android.billingclient.api.ExternalOfferInformationDialogListener)) API.

## Google Play Billing Library 8.1.0 Release (2025-11-06)

Version 8.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

* Suspended subscriptions

  A new parameter has been added to the
  [`BillingClient.queryPurchasesAsync()`](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener))
  method to include suspended subscriptions when querying for subscriptions.
  Suspended subscriptions are still attributed to the user, but are not active,
  either because the user paused the subscription or their renewal payment method
  was declined.

  The [`Purchase`](/reference/com/android/billingclient/api/Purchase) object returned in the listener will return `isSuspended() = true`
  for any suspended subscriptions. In this case, you shouldn't grant access
  to the purchased subscription, and instead guide the user to the
  [subscriptions center](https://play.google.com/store/account/subscriptions)
  where the user can manage their payment methods
  or pause state to re-activate their subscription.
* Updates to [subscriptions](/google/play/billing/subscriptions):

  + The [`BillingFlowParams.ProductDetailsParams`](/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams)
    object now has the `setSubscriptionProductReplacementParams()` method
    in which you can specify product level replacement information.
  + The `SubscriptionProductReplacementParams` object has
    two setter methods:

    - `setOldProductId`: The old product that needs to be replaced by
      the product in current [`ProductDetails`](/reference/com/android/billingclient/api/ProductDetails).
    - `setReplacementMode`: This is the item level replacement mode. The modes are essentially the
      same as SubscriptionUpdateParams, but the value mapping has
      been updated. A new replacement mode `KEEP_EXISTING` is introduced
      that lets you keep the existing payment schedule unchanged
      for an item.
  + [SubscriptionUpdateParams setSubscriptionReplacementMode](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)) will be
    deprecated. You should use `SubscriptionProductReplacementParams.setReplacementMode`
    instead.
* Updated `minSdkVersion` to 23.
* Enabled [pre-order APIs for one-time products](/google/play/billing/one-time-product-multi-purchase-options-offers#pre-order)

  The `ProductDetails.oneTimePurchaseOfferDetails.getPreorderDetails()` API
  that gets the pre-order details is now available for use.
* Google Play Billing Library now supports [Kotlin version 2.2.0](https://kotlinlang.org/docs/whatsnew22.html).

## Google Play Billing Library 8.0.0 Release (2025-06-30)

Version 8.0.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* *In-app items* will now be referred to as *one-time products*.
* Multiple purchase options and offers for one-time products.

  You can now have multiple purchase options and offers for your one-time
  products. This provides you flexibility in how you sell your products and
  reduces the complexity of managing them.
* Improved the [`queryProductDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) method.

  Prior to PBL 8.0.0, the [`queryProductDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) method didn't
  return products that couldn't be fetched. This could be due to reasons such
  as the product is not found or no offers are available to the user. With PBL
  8.0.0, unfetched products are returned with a new product-level status code
  that provides information about unfetched products. Note that there is a
  change in the signature of the
  [`ProductDetailsResponseListener.onProductDetailsResponse()`](/google/play/billing/integrate#automatic-service-reconnection) which
  requires changes in your app. For more information, see [process the
  result](/google/play/billing/integrate#process-the-result).
* Automatic service reconnection.

  The new `BillingClient.Builder.enableAutoServiceReconnection()` builder
  parameter lets developers opt-in to automatic service reconnection, which
  simplifies connection management by handling reconnections to
  the Play Billing Service automatically and eliminating the need to manually
  call `startConnection()` in the event of a service disconnection.
  For more information, see [Automatically Re-establish a Connection](/google/play/billing/integrate#automatic-service-reconnection).
* Sub-response codes for the [`launchBillingFlow()`](/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) method.

  The [BillingResult](/reference/com/android/billingclient/api/BillingResult) returned from [`launchBillingFlow()`](/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)) will now
  include a sub-response code field. This field will only be populated in some
  cases to provide a more specific reason for the failure. The sub-response
  field can have the following values:

  + `PAYMENT_DECLINED_DUE_TO_INSUFFICIENT_FUNDS` - Returned when the user's
    funds are less than the price of the item they are attempting
    to purchase.
  + `USER_INELIGIBLE` - Returned when the user doesn't meet the configured
    eligibility requirements for a subscription offer.
  + `NO_APPLICABLE_SUB_RESPONSE_CODE` - The default value, returned when no
    other sub-response code is applicable.
* Removed the `queryPurchaseHistory()` method.

  The `queryPurchaseHistory()` method that was previously marked as
  deprecated has now been removed. See [Query Purchase History](/google/play/billing/query-purchase-history) for
  details on what alternative APIs to use instead.
* Removed the `querySkuDetailsAsync()` method.

  The `querySkuDetailsAsync()` method that was previously marked as deprecated
  has now been removed. You should use [queryProductDetailsAsync](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)) instead.
* Removed the `BillingClient.Builder.enablePendingPurchases()` method.

  The `enablePendingPurchases()` method with no parameters that was previously
  marked as deprecated has now been removed. You should use
  `enablePendingPurchases(PendingPurchaseParams params)` instead. Note that
  the deprecated `enablePendingPurchases()` is functionally equivalent to
  `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`.
* Removed the overloaded `queryPurchasesAsync()` method that takes a [skuType](/reference/com/android/billingclient/api/BillingClient.SkuType).

  The `queryPurchasesAsync(String skuType, PurchasesResponseListener
  listener)` method that was previously marked as
  deprecated has now been removed. Alternately, use
  [`queryPurchasesAsync(QueryPurchasesParams queryPurchasesParams,
  PurchasesResponseListener listener)`](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)).

## Google Play Billing Library 7.1.1 Release (2024-10-03)

Version 7.1.1 of the Google Play Billing Library and Kotlin extensions are now
available.

### Bug fixes

* Fixed a bug in Play Billing Library 7.1.0 related to [testing
  `BillingResult` response codes](/google/play/billing/test-response-codes).

## Google Play Billing Library 7.1.0 Release (2024-09-19)

Version 7.1.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Improved thread safety related to connection status and management.
* Introduced partial changes for testing [`BillingResult`](/reference/com/android/billingclient/api/BillingResult)
  response codes which is fully released in Play Billing Library 7.1.1. To
  test your integration using this feature, you'll need to upgrade to Play
  Billing Library 7.1.1. A bug exists that will only impact applications with
  [billing overrides testing enabled](/google/play/billing/test-response-codes#enable-billing-overrides-testing) and does
  not affect regular usage. For more information, see [Test `BillingResult`
  response codes](/google/play/billing/test-response-codes).

## Google Play Billing Library 7.0.0 Release (2024-05-14)

Version 7.0.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added APIs to support installment subscriptions.

  + Added [`ProductDetails.InstallmentPlanDetails`](/reference/com/android/billingclient/api/ProductDetails.InstallmentPlanDetails) for
    installment base plans that users are eligible to purchase. This API
    helps your app identify the installment plan and its commitment setup to
    provide related information to the user. To learn more, see our
    [subscription installments guide](/google/play/billing/subscriptions#installments).
* Added [`PendingPurchasesParams`](/reference/com/android/billingclient/api/PendingPurchasesParams) and
  [`BillingClient.Builder.enablePendingPurchases(PendingPurchaseParams)`](/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases(PendingPurchaseParams))
  to replace
  [`BillingClient.Builder.enablePendingPurchases()`](/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases()),
  which has been deprecated in this release.

  + The deprecated `enablePendingPurchases()` is functionally equivalent to
    `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`.
* Added APIs to support pending transactions for subscription prepaid plans:

  + Use
    [`PendingPurchasesParams.Builder.enablePrepaidPlans()`](/reference/com/android/billingclient/api/PendingPurchasesParams.Builder#enablePrepaidPlans())
    along with
    [`BillingClient.Builder.enablePendingPurchases(PendingPurchaseParams)`](/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases(PendingPurchaseParams))
    to enable pending transactions for subscription prepaid plans. When
    adding support, be sure that your app also correctly manages
    subscription lifecycles. To learn more see our [pending purchases
    guide](/google/play/billing/subscriptions#pending).
  + Added [`Purchase.PendingPurchaseUpdate`](/reference/com/android/billingclient/api/Purchase.PendingPurchaseUpdate) and
    [`Purchase.getPendingPurchaseUpdate()`](/reference/com/android/billingclient/api/Purchase.getPendingPurchaseUpdate()) for
    retrieving the pending top-up or upgrade or downgrade to an existing
    subscription.
* Removed
  [`BillingClient.Builder.enableAlternativeBilling()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener)),
  [`AlternativeBillingListener`](/reference/com/android/billingclient/api/AlternativeBillingListener), and
  [`AlternativeChoiceDetails`](/reference/com/android/billingclient/api/AlternativeChoiceDetails).

  + Developers should use
    [`BillingClient.Builder.enableUserChoiceBilling()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener))
    with [`UserChoiceBillingListener`](/reference/com/android/billingclient/api/UserChoiceBillingListener) and
    [`UserChoiceDetails`](/reference/com/android/billingclient/api/UserChoiceDetails) in the listener callback
    instead.
* Removed [`BillingFlowParams.ProrationMode`](/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode),
  [`BillingFlowParams.SubscriptionUpdateParams.Builder.setReplaceProrationMode()`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setReplaceProrationMode(int)),
  and
  [`BillingFlowParams.SubscriptionUpdateParams.Builder.setReplaceSkusProrationMode()`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setReplaceSkusProrationMode(int)).

  + Developers should use
    [`BillingFlowParams.SubscriptionUpdateParams.ReplacementMode`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode)
    with
    [`BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int))
    instead.
* Removed
  [`BillingFlowParams.SubscriptionUpdateParams.Builder#setOldSkuPurchaseToken()`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldSkuPurchaseToken(java.lang.String)).

  + Developers should use
    [`BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken(java.lang.String)`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken(java.lang.String))
    instead.
* [`BillingClient.queryPurchaseHistoryAsync()`](/reference/com/android/billingclient/api/BillingClient#queryPurchaseHistoryAsync(com.android.billingclient.api.QueryPurchaseHistoryParams,com.android.billingclient.api.PurchaseHistoryResponseListener))
  has been deprecated and will be removed in a future release. Developers
  should use the following alternatives instead:

  + Acknowledged and pending purchases: Use
    [`BillingClient.queryPurchasesAsync()`](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))
    to fetch the active purchases.
  + Consumed purchases: Developers should keep track of consumed purchases
    on their own servers.
  + Canceled purchases: Use the [voided-purchases](https://developers.google.com/android-publisher/voided-purchases)
    developer API.
  + For more details, see [Query Purchase History](/google/play/billing/query-purchase-history)
* [`BillingFlowParams.ProductDetailsParams.setOfferToken()`](/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams.Builder#setOfferToken(java.lang.String))
  now throws an exception when developers specify an empty `offerToken`.
* Updated `minSdkVersion` to 21 and `targetSdkVersion` to 34.

## Google Play Billing Library 6.2.1 Release (2024-04-16)

Version 6.2.1 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Fixed a bug in
  [`BillingClient.showAlternativeBillingOnlyInformationDialog()`](/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener))
  where the
  [`AlternativeBillingOnlyInformationDialogListener`](/reference/com/android/billingclient/api/AlternativeBillingOnlyInformationDialogListener)
  may not be called in certain cases when the dialog completes.

## Google Play Billing Library 6.2.0 Release (2024-03-06)

Version 6.2.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added APIs to support [external offers](/google/play/billing/external)
  + Added
    [`BillingClient.Builder.enableExternalOffer()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableExternalOffer())
    to enable the ability to provide external offers.
  + Added
    [`BillingClient.isExternalOfferAvailableAsync()`](/reference/com/android/billingclient/api/BillingClient#isExternalOfferAvailableAsync(com.android.billingclient.api.ExternalOfferAvailabilityListener))
    to check the availability of providing external offers functionality.
  + Added
    [`BillingClient.showExternalOfferInformationDialog()`](/reference/com/android/billingclient/api/BillingClient#showExternalOfferInformationDialog(android.app.Activity,%20com.android.billingclient.api.ExternalOfferInformationDialogListener))
    to show an information dialog to users before leading users outside the
    app.
  + Added
    [`BillingClient.createExternalOfferReportingDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#createExternalOfferReportingDetailsAsync(com.android.billingclient.api.ExternalOfferReportingDetailsListener))
    to create a payload required to report transactions made through
    external offers.

## Google Play Billing Library 6.1.0 Release (2023-11-14)

Version 6.1.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added APIs to support [alternative billing only (i.e. without user choice)](/google/play/billing/alternative)
  + Added
    [`BillingClient.Builder.enableAlternativeBillingOnly()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBillingOnly())
    to functionally enable the ability to offer alternative billing only.
  + Added
    [`BillingClient.isAlternativeBillingOnlyAvailableAsync()`](/reference/com/android/billingclient/api/BillingClient#isAlternativeBillingOnlyAvailableAsync(com.android.billingclient.api.AlternativeBillingOnlyAvailabilityListener))
    to check the availability of offering alternative billing only.
  + Added
    [`BillingClient.showAlternativeBillingOnlyInformationDialog()`](/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener))
    to show an information dialog to inform users when alternative billing
    only is being used.
  + Added
    [`BillingClient.createAlternativeBillingOnlyReportingDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#createAlternativeBillingOnlyReportingDetailsAsync(com.android.billingclient.api.AlternativeBillingOnlyReportingDetailsListener))
    to create a payload required to report transactions made through
    alternative billing only.
* Updated the user choice billing APIs
  + Added [`UserChoiceBillingListener`](/reference/com/android/billingclient/api/UserChoiceBillingListener)
    to replace
    [AlternativeBillingListener](/reference/com/android/billingclient/api/AlternativeBillingListener)
    which has been marked as deprecated.
  + Added [`UserChoiceDetails`](/reference/com/android/billingclient/api/UserChoiceDetails)
    to replace
    [`AlternativeChoiceDetails`](/reference/com/android/billingclient/api/AlternativeChoiceDetails)
    which has been marked as deprecated.
  + Added
    [`BillingClient.Builder.enableUserChoiceBilling()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener))
    to replace
    [`BillingClient.Builder.enableAlternativeBilling()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener))
    which has been marked as deprecated.
* Added
  [`BillingClient.getBillingConfigAsync()`](/reference/com/android/billingclient/api/BillingClient#getBillingConfigAsync(com.android.billingclient.api.GetBillingConfigParams,%20com.android.billingclient.api.BillingConfigResponseListener))
  to retrieve Google Play country.

## Google Play Billing Library 6.0.1 Release (2023-06-22)

Version 6.0.1 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

Update Play Billing Library to be compatible with Android 14.

## Google Play Billing Library 6.0 Release (2023-05-10)

Version 6.0.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added new [`ReplacementMode`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode)
  enum to replace
  [`ProrationMode`](/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode).

  Note that `ProrationMode` is still available for backward compatibility
  reasons.
* Removed order ID for [`PENDING`](/reference/com/android/billingclient/api/Purchase.PurchaseState#PENDING)
  purchases.

  Previously, the order ID would always be created even if the purchase was
  pending. Starting with version 6.0.0, an order ID will not be created for
  pending purchases, and for these purchases, the order ID will be populated
  after the purchase is moved to the
  [`PURCHASED`](/reference/com/android/billingclient/api/Purchase.PurchaseState#PURCHASED)
  state.
* Removed `queryPurchases` and `launchPriceConfirmationFlow` methods.

  The `queryPurchases` and `launchPriceConfirmationFlow` methods that have
  previously been marked as deprecated have now been removed in Play Billing
  Library 6.0.0. Developers should use
  [`queryPurchasesAsync`](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))
  instead of `queryPurchases`. For `launchPriceConfirmationFlow` alternatives,
  see [Price changes](/google/play/billing/price-changes).
* Added new network error response code.

  A new network error response code,
  [`NETWORK_ERROR`](/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR),
  has been added starting with PBL version 6.0.0. This code is returned when
  an error occurs due to a network connection issue. These network connection
  errors were previously reported as `SERVICE_UNAVAILABLE`.
* Updated [`SERVICE_UNAVAILABLE`](/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE)
  and
  [`SERVICE_TIMEOUT`](/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT).

  Starting with PBL version 6.0.0, errors due to timeout in processing will be
  returned as `SERVICE_UNAVAILABLE` instead of the current `SERVICE_TIMEOUT`.

  The behavior does not change in earlier versions of PBL.
* Removed
  [`SERVICE_TIMEOUT`](/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT).

  Starting with PBL version 6.0.0, `SERVICE_TIMEOUT` will no longer be
  returned. Previous versions of PBL will still return this code.
* Added additional logging.

  The Play Billing Library 6 release includes additional logging, which
  provides insight into API usage (such as success and failure) and service
  connection issues. This information will be used to improve the performance
  of the Play Billing Library and provide better support for errors.

## Google Play Billing Library 5.2.1 Release (2023-06-22)

Version 5.2.1 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

Update Play Billing Library to be compatible with Android 14.

## Google Play Billing Library 5.2 Release (2023-04-06)

Version 5.2.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added classes to support alternative billing flows on mobile/tablet for
  users in South Korea:
  + [`AlternativeBillingListener`](/reference/com/android/billingclient/api/AlternativeBillingListener)
  + [`AlternativeChoiceDetails`](/reference/com/android/billingclient/api/AlternativeChoiceDetails)
  + [`AlternativeChoiceDetails.Product`](/reference/com/android/billingclient/api/AlternativeChoiceDetails.Product)
* Added
  [`BillingFlowParams.SubscriptionUpdateParams.Builder.setOriginalExternalTransactionId()`](/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String))
  method to specify the external transaction id of the originating
  subscription.
* Added
  [`BillingClient.Builder.enableAlternativeBilling()`](/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener))
  method to allow users in South Korea to select an alternative billing
  option.

## Google Play Billing Library 5.1 Release (2022-10-31)

Version 5.1.0 of the Google Play Billing Library and Kotlin extensions are now
available.

This version contains the following changes.

### Summary of changes

* Added
  [`ProductDetails.SubscriptionOfferDetails.getOfferId()`](/reference/com/android/billingclient/api/ProductDetails.SubscriptionOfferDetails#getOfferId())
  method to retrieve the offer ID.
* Added
  [`ProductDetails.SubscriptionOfferDetails.getBasePlanId()`](/reference/com/android/billingclient/api/ProductDetails.SubscriptionOfferDetails#getBasePlanId())
  method to retrieve the base plan ID.
* Updated the `targetSdkVersion` to 31.

## Google Play Billing Library 5.0 Release (2022-05-11)

Version 5.0.0 of the Google Play Billing Library and Kotlin extensions are now
available.

This version contains the following changes.

### Summary of changes

* Introduced a new model for subscriptions, including new entities that enable
  you to create multiple offers for a single subscription product. For more
  information, see the [migration guide](/google/play/billing/migrate-gpblv5).
* Added
  [`BillingClient.queryProductDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener))
  to replace `BillingClient.querySkuDetailsAsync()`.
* Added `setIsOfferPersonalized()` method for EU personalized pricing
  disclosure requirements. To learn more about how to use this method, see
  [Indicate a personalized
  price](/google/play/billing/integrate#personalized-price).
* Removed `queryPurchases()`, which was previously deprecated and replaced by
  queryPurchasesAsync introduced in Google Play Billing Library 4.0.0.
* `launchPriceChangeFlow` has been deprecated and will be removed in a future
  release. To learn more about alternatives, see [Launch a price change
  confirmation flow](/google/play/billing/subscriptions#price-change-launch).
* Removed
  [`setVrPurchaseFlow()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setVrPurchaseFlow(boolean)),
  which was previously used when instantiating a purchase flow. In previous
  versions, this method redirected the user to complete the purchase on their
  Android-powered device. Once you remove this method, users will complete the
  purchase through the standard purchase flow.

## Google Play Billing Library 4.1 release (2022-02-23)

Version 4.1.0 of the Google Play Billing Library and Kotlin extensions are now
available.

This version contains the following changes.

### Summary of changes

* Added
  [`BillingClient.showInAppMessages()`](/reference/com/android/billingclient/api/BillingClient#showInAppMessages(android.app.Activity,%20com.android.billingclient.api.InAppMessageParams,%20com.android.billingclient.api.InAppMessageResponseListener))
  to help with handling subscription payment declines. To learn more about how
  to use in-app messaging for handling subscriptions payment declines, see
  [Handling payment
  declines](/google/play/billing/subscriptions#payment-declines).

## Google Play Billing Library 4.0 Release (2021-05-18)

Version 4.0.0 of the Google Play Billing Library and Kotlin extensions are now
available.

### Summary of changes

* Added
  [`BillingClient.queryPurchasesAsync()`](/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(java.lang.String,%20com.android.billingclient.api.PurchasesResponseListener))
  to replace
  [`BillingClient.queryPurchases()`](/reference/com/android/billingclient/api/BillingClient#queryPurchases(java.lang.String))
  which will be removed in a future release.
* Added new subscription replacement mode
  [`IMMEDIATE_AND_CHARGE_FULL_PRICE`](/google/play/billing/subscriptions#change).
* Added
  [`BillingClient.getConnectionState()`](/reference/com/android/billingclient/api/BillingClient#getConnectionState())
  method to retrieve the Play Billing Library's connection state.
* Updated Javadoc and implementation to indicate which thread a method can be
  called on and which thread results are posted.
* Added
  [`BillingFlowParams.Builder.setSubscriptionUpdateParams()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setSubscriptionUpdateParams(com.android.billingclient.api.BillingFlowParams.SubscriptionUpdateParams))
  as a new way to initiate subscription updates. This replaces
  `BillingFlowParams#getReplaceSkusProrationMode`,
  `BillingFlowParams#getOldSkuPurchaseToken`, `BillingFlowParams#getOldSku`,
  `BillingFlowParams.Builder#setReplaceSkusProrationMode`,
  `BillingFlowParams.Builder#setOldSku` which have been removed.
* Added
  [`Purchase.getQuantity()`](/reference/com/android/billingclient/api/Purchase#getQuantity())
  and
  [`PurchaseHistoryRecord.getQuantity()`](/reference/com/android/billingclient/api/PurchaseHistoryRecord#getQuantity()).
* Added
  [`Purchase#getSkus()`](/reference/com/android/billingclient/api/Purchase#getSkus())
  and
  [`PurchaseHistoryRecord#getSkus()`](/reference/com/android/billingclient/api/PurchaseHistoryRecord#getSkus()).
  These replace `Purchase#getSku` and `PurchaseHistoryRecord#getSku` which
  have been removed.
* Removed `BillingFlowParams#getSku`, `BillingFlowParams#getSkuDetails` and
  `BillingFlowParams#getSkuType`.

## Google Play Billing Library 3.0.3 Release (2021-03-12)

Version 3.0.3 of the Google Play Billing Library, Kotlin extension, and Unity
plugin are now available.

### Java and Kotlin Bug fixes

* Fix memory leak when
  [`endConnection()`](/reference/com/android/billingclient/api/BillingClient#endConnection())
  is called.
* Fix issue when the Google Play Billing Library is used by apps which use the
  single task launch mode. A
  [`onPurchasesUpdated()`](/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated)
  callback will be triggered when an app is resumed from the Android launcher
  and the billing dialog was visible prior to being suspended.

### Unity Bug fixes

* Update to Java version 3.0.3 to fix memory leak and resolve issue preventing
  purchases when an app is resumed from the Android launcher and the billing
  dialog was visible prior to being suspended.

## Google Play Billing Library 3.0.2 Release (2020-11-24)

Version 3.0.2 of the Google Play Billing Library and Kotlin extension are now
available.

### Bug fixes

* Fixed a bug in the Kotlin extension where the coroutine fails with error
  "Already resumed".
* Fixed unresolved references when the Kotlin extension is used with the
  kotlinx.coroutines library version 1.4+.

## Google Play Billing Library 3.0.1 Release (2020-09-30)

Version 3.0.1 of the Google Play Billing Library and Kotlin extension are now
available.

### Bug fixes

* Fixed a bug where if the app was killed and restored during the billing
  flow, `PurchasesUpdatedListener` may not be called with the purchase result.

## Google Play Billing Library 3.0 Release (2020-06-08)

Version 3.0.0 of the Google Play Billing Library, Kotlin extension, and Unity
plugin are now available.

### Summary of changes

* Removed rewarded SKU support.
* Removed the `ChildDirected` and `UnderAgeOfConsent` parameters.
* Removed deprecated developer payload methods.
* Removed deprecated methods `BillingFlowParams.setAccountId()` and
  `BillingFlowParams.setDeveloperId()`.
* Removed deprecated methods `BillingFlowParams.setOldSkus(String oldSku)` and
  `BillingFlowParams.addOldSku(String oldSku)`.
* Added nullability annotations.

### Bug fixes

* [`SkuDetails.getIntroductoryPriceCycles()`](/reference/com/android/billingclient/api/SkuDetails#getIntroductoryPriceCycles())
  now returns `int` instead of `String`.
* Fixed a bug where the billing flow would be treated as having extra params
  even if no extra params were set.

## Google Play Billing Library 2.2.1 Release (2020-05-20)

Version 2.2.1 of the Google Play Billing library is now available.

### Bug fixes

* Updated the default version of the Java Play Billing library that the Kotlin
  extension depends on.

## Google Play Billing Library 2.2.0 release and Unity support (2020-03-23)

Version 2.2.0 of the Google Play Billing provides functionality that helps
developers ensure purchases are attributed to the correct user. These changes
replace the need to build custom solutions based on developer payload. As part
of this update, the developer payload functionality has been deprecated and will
be removed in a future release. For more information, including recommended
alternatives, see [Developer payload](/google/play/billing/developer-payload).

### Google Play Billing Billing Library 2 for Unity

In addition to the current Java and Kotlin versions of Google Play Billing
Library 2, we released a version of the library for use with Unity. Game
developers using the Unity in-app purchase API can upgrade now to take advantage
of all Google Play Billing Library 2 features and to make the subsequent
upgrades to future versions of the Google Play Billing Library easier.

To learn more, see [Use Google Play Billing with
Unity](/google/play/billing/unity).

### Summary of changes

* Java Google Play Billing Library
  + In
    [`AcknowledgePurchaseParams`](/reference/com/android/billingclient/api/AcknowledgePurchaseParams),
    deprecated
    [`setDeveloperPayload()`](/reference/com/android/billingclient/api/AcknowledgePurchaseParams.Builder#setDeveloperPayload(java.lang.String))
    and
    [`getDeveloperPayload()`](/reference/com/android/billingclient/api/AcknowledgePurchaseParams#getDeveloperPayload())
    methods.
  + In
    [`ConsumeParams`](/reference/com/android/billingclient/api/ConsumeParams),
    deprecated
    [`setDeveloperPayload()`](/reference/com/android/billingclient/api/ConsumeParams.Builder#setDeveloperPayload(java.lang.String))
    and
    [`getDeveloperPayload()`](/reference/com/android/billingclient/api/ConsumeParams#getdeveloperpayload)
    methods.
  + In
    [`BillingFlowParams`](/reference/com/android/billingclient/api/BillingFlowParams.Builder),
    renamed
    [`setAccountId()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setAccountId(java.lang.String))
    to
    [`setObfuscatedAccountId()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)),
    and documented length restriction of 64 characters and restriction
    disallowing Personally Identifiable Information (PII) in this field.
    [`setAccountId()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setaccountid)
    has been marked as deprecated and will be removed in a future library
    version.
  + In `BillingFlowParams`, added [`setObfuscatedProfileId()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid)
    which works similarly to
    [`setObfuscatedAccountId()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)).
    For more information, see [Developer payload updates and
    alternatives](/google/play/billing/developer-payload).
  + In [`Purchase`](/reference/com/android/billingclient/api/Purchase),
    added the
    [`getAccountIdentifiers()`](/reference/com/android/billingclient/api/Purchase#getAccountIdentifiers())
    method to return the obfuscated account identifiers set in
    `BillingFlowParams`.
  + In
    [`BillingClient`](/reference/com/android/billingclient/api/BillingClient),
    the
    [`loadRewardedSku()`](/reference/com/android/billingclient/api/BillingClient#loadRewardedSku(com.android.billingclient.api.RewardLoadParams,%20com.android.billingclient.api.RewardResponseListener))
    method has been marked deprecated as part of deprecating rewarded SKUs.
    You can find more information about the deprecation in the [Play Console
    Help
    Center](https://support.google.com/googleplay/android-developer/answer/9155268).

## Google Play Billing Library 2.1.0 Release and Kotlin Extension 2.1.0 Release (2019-12-10)

Version 2.1.0 of the Google Play Billing library and the new Kotlin extension
are now available. The Play Billing Library Kotlin extension provides idiomatic
API alternatives for Kotlin consumption, featuring better null-safety and
coroutines. For code examples, see [Use the Google Play Billing
Library](/google/play/billing/billing_library_overview).

This version contains the following changes.

### Summary of changes

* In
  [`BillingFlowParams`](/reference/com/android/billingclient/api/BillingFlowParams),
  deprecated `setOldSku(String oldSku)` and replaced with `setOldSku(String
  oldSku, String purchaseToken)`, to disambiguate when multiple accounts on
  the device own the same sku.

## Google Play Billing Library 2.0.3 Release (2019-08-05)

Version 2.0.3 of the Google Play Billing library is now available.

### Bug fixes

* Fixed a bug where `querySkuDetailsAsync()` would occasionally fail with code
  `DEVELOPER_ERROR` instead of returning a successful result.

## Google Play Billing Library 2.0.2 Release (2019-07-08)

Version 2.0.2 of the Google Play Billing library is now available. This release
contains updates to the reference documentation and does not change library
functionality.

## Google Play Billing Library 2.0.1 Release (2019-06-06)

Version 2.0.1 of the Google Play Billing library is now available. This version
contains the following changes.

### Bug fixes

* Fixed a bug where debug messages were being returned as `null` in some
  cases.
* Fixed a potential memory leak issue.

## Google Play Billing Library 2.0 Release (2019-05-07)

Version 2.0 of the Google Play Billing library is now available. This version
contains the following changes.

### Purchases must be acknowledged within three days

**Note:** This section describes a new requirement for acknowledging all purchases.
If you are already consuming purchases using `consumeAsync()`, you don't need to
make any further changes if you consume purchases within 3 days, as
`consumeAsync()` automatically acknowledges a purchase. Failure to properly
acknowledge purchases will result in purchases being refunded.**Note:** This requirement applies only to apps that use the Google Play Billing
Library version 2.0 and newer. This requirement doesn't apply if you use an
older version of the Google Play Billing Library, or if you use the AIDL API.

Google Play supports purchasing products from inside of your app (in-app) or
outside of your app (out-of-app). In order for Google Play to ensure a
consistent purchase experience regardless of where the user purchases your
product, you must acknowledge all purchases received through the Google Play
Billing Library as soon as possible after granting entitlement to the user. If
you don't acknowledge a purchase within three days, the user automatically
receives a refund, and Google Play revokes the purchase. For [pending
transactions](#2_0_pending) (new in version 2.0), the three-day window starts
when the purchase has moved to the `PURCHASED` state and does not apply while
the purchase is in a `PENDING` state.

For subscriptions, you must acknowledge any purchase that has a new purchase
token. This means that all initial purchases, plan changes, and re-signups need
to be acknowledged, but you don't need to acknowledge subsequent renewals. To
determine if a purchase needs acknowledgment, you can check the acknowledgement
field in the purchase.

The `Purchase` object now includes an
[`isAcknowledged()`](/reference/com/android/billingclient/api/Purchase#isacknowledged)
method that indicates whether a purchase has been acknowledged. In addition, the
Google Play Developer API includes acknowledgement boolean values for both
[`Purchases.products`](https://developers.google.com/android-publisher/api-ref/purchases/products)
and
[`Purchases.subscriptions`](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions).
Before acknowledging a purchase, be sure to use these methods to determine if
the purchase has already been acknowledged.

You can acknowledge a purchase by using one of the following methods:

* For consumable products, use `consumeAsync()`, found in the client API.
* For products that aren't consumed, use `acknowledgePurchase()`, found in the
  client API.
* A new `acknowledge()` method is also available in the Server API.

### BillingFlowParams.setSku() has been removed

The previously-deprecated `BillingFlowParams#setSku()` method has been removed
in this release. Before rendering products in a purchase flow, you must now call
[`BillingClient.querySkuDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#queryskudetailsasync),
passing the resulting
[`SkuDetails`](/reference/com/android/billingclient/api/SkuDetails) object to
[`BillingFlowParams.Builder.setSkuDetails()`](/reference/com/android/billingclient/api/BillingFlowParams.Builder#setskudetails).

**Note:** Caching `SkuDetails` between user sessions is not recommended, as
`SkuDetails` objects are valid only for a limited time before you must refresh
them again by calling `querySkuDetailsAsync()`.

For code examples, see [Use the Google Play Billing
Library](/google/play/billing/billing_library_overview).

### Developer payload is supported

Version 2.0 of the Google Play Billing library adds support for *developer
payload*—arbitrary strings that can be attached to purchases. You can
attach a developer payload parameter to a purchase, but only when the purchase
is acknowledged or consumed. This is unlike developer payload in AIDL, where the
payload could be specified when launching the purchase flow. Because purchases
can now be initiated [from outside of your app](#2_0_acknowledge), this change
ensures that you always have an opportunity to add a payload to purchases.

To access the payload in the new library, `Purchase` objects now include a
[`getDeveloperPayload()`](/reference/com/android/billingclient/api/Purchase#getdeveloperpayload)
method.

**Note:** You cannot modify a payload after it is assigned.

### Consistent offers

**Note:** This feature is being tested, and general availability is not guaranteed.

When you offer a discounted SKU, Google Play now returns the original price of
the SKU so that you can show users that they are receiving a discount.

[`SkuDetails`](/reference/com/android/billingclient/api/SkuDetails) contains two
new methods for retrieving the original SKU price:

* [`getOriginalPriceAmountMicros()`](/reference/com/android/billingclient/api/SkuDetails#getOriginalPriceAmountMicros())
  + returns the unformatted original price of the SKU before discount.
* [`getOriginalPrice()`](/reference/com/android/billingclient/api/SkuDetails#getOriginalPrice())
  + returns the original price with additional currency formatting.

### Pending transactions

With version 2.0 of the Google Play Billing library, you *must* support
purchases where additional action is required before granting entitlement. For
example, a user might choose to purchase your in-app product at a physical store
using cash. This means that the transaction is completed outside of your app. In
this scenario, you should grant entitlement only after the user has completed
the transaction.

To enable pending purchases, call
[`enablePendingPurchases()`](/reference/com/android/billingclient/api/BillingClient.Builder#enablependingpurchases)
as part of initializing your app.

Use
[`Purchase.getPurchaseState()`](/reference/com/android/billingclient/api/Purchase#getpurchasestate)
to determine whether the purchase state is `PURCHASED` or `PENDING`. Note that
you should grant entitlement only when the state is `PURCHASED`. You should
check for `Purchase` status updates by doing the following:

1. When starting your app, call [`BillingClient.queryPurchases()`](/reference/com/android/billingclient/api/BillingClient#querypurchases)
   to retrieve the list of unconsumed products associated with the user.
2. Call `Purchase.getPurchaseState()` on each returned `Purchase` object.
3. Implement the [`onPurchasesUpdated()`](/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated)
   method to respond to changes to `Purchase` objects.

In addition, the Google Play Developer API includes a `PENDING` state for
[`Purchases.products`](https://developers.google.com/android-publisher/api-ref/purchases/products).
Pending transactions are not supported for subscriptions.

This release also introduces a new real-time developer notification type,
`OneTimeProductNotification`. This notification type contains a single message
whose value is either `ONE_TIME_PRODUCT_PURCHASED` or
`ONE_TIME_PRODUCT_CANCELED`. This notification type is sent only for purchases
associated with delayed forms of payment, such as cash.

When acknowledging pending purchases, be sure to acknowledge only when the
purchase state is `PURCHASED` and not `PENDING`.

**Note:** Pending transactions can be tested using license testers. In addition to
two test credit cards, license testers have access to two new test instruments
for delayed forms of payment which automatically complete or cancel after a
couple of minutes. While testing your application, you should verify that your
application does not grant entitlement or acknowledge the purchase immediately
after purchasing with either of these two new instruments. When purchasing using
the new test instrument that automatically completes, you should verify that
your application grants entitlement and acknowledges the purchase once the
purchase completes.

### API changes

Version 2.0 of the Google Play Billing library contains several API changes to
support new features and clarify existing functionality.

#### consumeAsync

[`consumeAsync()`](/reference/com/android/billingclient/api/BillingClient#consumeasync)
now takes a
[`ConsumeParams`](/reference/com/android/billingclient/api/ConsumeParams) object
instead of a `purchaseToken`. `ConsumeParams` contains the `purchaseToken` as
well as an optional developer payload.

The previous version of `consumeAsync()` has been removed in this release.

#### queryPurchaseHistoryAsync

To minimize confusion,
[`queryPurchaseHistoryAsync()`](/reference/com/android/billingclient/api/BillingClient#queryPurchaseHistoryAsync(java.lang.String,%20com.android.billingclient.api.PurchaseHistoryResponseListener))
now returns a
[`PurchaseHistoryRecord`](/reference/com/android/billingclient/api/PurchaseHistoryRecord)
object instead of a `Purchase` object. The `PurchaseHistoryRecord` object is the
same as a `Purchase` object, except that it reflects only the values returned by
`queryPurchaseHistoryAsync()` and does not contain the `autoRenewing`,
`orderId`, and `packageName` fields. Note that nothing has changed with the
returned data—`queryPurchaseHistoryAsync()` returns the same data as
before.

#### BillingResult return values

APIs that previously returned a `BillingResponse` integer value now return a
[`BillingResult`](/reference/com/android/billingclient/api/BillingResult)
object. `BillingResult` contains the `BillingResponse` integer as well as a
debug string that you can use to diagnose errors. The debug string uses an en-US
locale and is not meant to be shown to end users.

### Bug fixes

* [`SkuDetails.getIntroductoryPriceAmountMicros()`](/reference/com/android/billingclient/api/SkuDetails#getIntroductoryPriceAmountMicros())
  now returns a `long` instead of a `String`.

## Google Play Billing Library 1.2.2 Release (2019-03-07)

Version 1.2.2 of the Google Play Billing library is now available. This version
contains the following changes.

### Bug fixes

* Fixed a threading issue introduced in v1.2.1. Background calls no longer
  block the main thread.

### Other changes

* Although using the main thread is still recommended, you can now instantiate
  the Google Play Billing Library from a background thread.
* Instantiation has been fully migrated to the background thread to reduce the
  chance of causing ANRs.

## Play Billing Library 1.2.1 Release (2019-03-04)

Version 1.2.1 of the Google Play Billing library is now available. This version
contains the following changes.

### Major changes

* Added support for [rewarded
  products](/google/play/billing/billing_rewarded_products). For more
  information on monetization options, see [Add rewarded-product-specific
  features](/distribute/best-practices/earn/monetization-options).

### Other changes

* Added public constructors for `PurchasesResult` and `SkuDetailsResult` to
  make testing easier.
* `SkuDetails` objects can use a new method, `getOriginalJson()`.
* All AIDL service calls are now handled by background threads.

### Bug fixes

* Null callback listeners are no longer passed into public APIs.

## Google Play Billing Library 1.2 Release (2018-10-18)

Version 1.2 of the Google Play Billing library is now available. This version
contains the following changes.

### Summary of changes

* The Google Play Billing Library is now licensed under the [Android Software
  Development Kit License Agreement](/studio/terms).
* Added the `launchPriceChangeConfirmationFlow` API, which prompts users to
  review a pending change to a subscription price.
* Added support for a new proration mode, `DEFERRED`, when upgrading or
  downgrading a user's subscription.
* In the `BillingFlowParams` class, replaced `setSku()` with
  `setSkuDetails()`.
* Minor bug fixes and code optimizations.

#### Price change confirmation

You can now change the price of a subscription in Google Play Console
and prompt users to review and accept the new price when they enter your app.

To use this API, create a `PriceChangeFlowParams` object by using the
`skuDetails` of the subscription product, and then call
`launchPriceChangeConfirmationFlow()`. Implement the
`PriceChangeConfirmationListener` to handle the result when the price change
confirmation flow finishes, as shown in the following code snippet:

### Kotlin

```
val priceChangeFlowParams = PriceChangeFlowParams.newBuilder()
    .setSkuDetails(skuDetailsOfThePriceChangedSubscription)
    .build()

billingClient.launchPriceChangeConfirmationFlow(activity,
        priceChangeFlowParams,
        object : PriceChangeConfirmationListener() {
            override fun onPriceChangeConfirmationResult(responseCode: Int) {
                // Handle the result.
            }
        })
```

### Java

```
PriceChangeFlowParams priceChangeFlowParams =
        PriceChangeFlowParams.newBuilder()
    .setSkuDetails(skuDetailsOfThePriceChangedSubscription)
    .build();

billingClient.launchPriceChangeConfirmationFlow(activity,
        priceChangeFlowParams,
        new PriceChangeConfirmationListener() {
            @Override
            public void onPriceChangeConfirmationResult(int responseCode) {
                // Handle the result.
            }
        });
```

The price change confirmation flow displays a dialog containing the new pricing
information, asking users to accept the new price. This flow returns a response
code of type
[`BillingClient.BillingResponse`](/reference/com/android/billingclient/api/BillingClient.BillingResponse).

#### New proration mode

When upgrading or downgrading a user's subscription, you can use a new proration
mode, `DEFERRED`. This mode updates the user's subscription when it next renews.
To learn more about how to set this proration mode, see [Set proration
mode](/google/play/billing/billing_subscriptions#set-proration-mode).

#### New method for setting SKU details

In the `BillingFlowParams` class, the `setSku()` method has been deprecated.
This change serves to optimize the Google Play Billing flow.

When constructing a new instance of `BillingFlowParams` in your in-app billing
client, we recommend that you instead work with the JSON object directly using
`setSkuDetails()`, as shown in the following code snippet:

In the `BillingFlowParams` Builder class, the `setSku()` method has been
deprecated. Instead, use the `setSkuDetails()` method, as shown in the following
code snippet. The object passed into `setSkuDetails()` object comes from the
[`querySkuDetailsAsync()`](/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener))
method.

### Kotlin

```
private lateinit var mBillingClient: BillingClient
private val mSkuDetailsMap = HashMap<String, SkuDetails>()

private fun querySkuDetails() {
    val skuDetailsParamsBuilder = SkuDetailsParams.newBuilder()
    mBillingClient.querySkuDetailsAsync(skuDetailsParamsBuilder.build()
    ) { responseCode, skuDetailsList ->
        if (responseCode == 0) {
            for (skuDetails in skuDetailsList) {
                mSkuDetailsMap[skuDetails.sku] = skuDetails
            }
        }
    }
}

private fun startPurchase(skuId: String) {
    val billingFlowParams = BillingFlowParams.newBuilder()
    .setSkuDetails(mSkuDetailsMap[skuId])
    .build()
}
```

### Java

```
private BillingClient mBillingClient;
private Map<String, SkuDetails> mSkuDetailsMap = new HashMap<>();

private void querySkuDetails() {
    SkuDetailsParams.Builder skuDetailsParamsBuilder
            = SkuDetailsParams.newBuilder();
    mBillingClient.querySkuDetailsAsync(skuDetailsParamsBuilder.build(),
            new SkuDetailsResponseListener() {
                @Override
                public void onSkuDetailsResponse(int responseCode,
                        List<SkuDetails> skuDetailsList) {
                    if (responseCode == 0) {
                        for (SkuDetails skuDetails : skuDetailsList) {
                            mSkuDetailsMap.put(skuDetails.getSku(), skuDetails);
                        }
                    }
                }
            });
}

private void startPurchase(String skuId) {
    BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
            .setSkuDetails(mSkuDetailsMap.get(skuId))
            .build();
}
```

## Play Billing Library 1.1 Release (2018-05-07)

Version 1.1 of the Google Play Billing library is now available. This version
contains the following changes.

### Summary of changes

* Added support to specify a proration mode in [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams)
  when upgrading/downgrading an existing subscription.
* The `replaceSkusProration` boolean flag in [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams)
  is no longer supported. Use `replaceSkusProrationMode` instead.
* [`launchBillingFlow()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.html#launchBillingFlow(android.app.Activity,%0Acom.android.billingclient.api.BillingFlowParams)) now triggers a callback
  for failed responses.

### Behavior changes

Version 1.1 of the Google Play Billing library contains the following behavior
changes.

#### Developers can set `replaceSkusProrationMode` in [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams) class

A `ProrationMode` provides further details on the type of proration when
upgrading or downgrading a user's subscription.

### Kotlin

```
BillingFlowParams.newBuilder()
    .setSku(skuId)
    .setType(billingType)
    .setOldSku(oldSku)
    .setReplaceSkusProrationMode(replaceSkusProrationMode)
    .build()
```