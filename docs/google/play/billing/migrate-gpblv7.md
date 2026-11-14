---
title: https://developer.android.com/google/play/billing/migrate-gpblv7
url: https://developer.android.com/google/play/billing/migrate-gpblv7
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/billing/llms.txt

This document describes how to migrate from Google Play Billing Library 5 or 6
to Google Play Billing Library 7 and how to integrate with the new optional
subscription capabilities.

For a full list of the changes in version 7.0.0, refer to the
[release notes](https://developer.android.com/google/play/billing/release-notes.md.txt).

## Overview

Google Play Billing Library 7 improves payment handling for
existing subscription features. These optional improvements
add support for paying with installment plans as well as
support for pending purchases for prepaid subscriptions.

## Backward-compatible Play Billing Library upgrade

All new Google Play Billing Library 7 APIs are optional, and
developers don't need to implement any API changes to update.

To migrate, you need to update API references and remove
certain APIs from your app as described in the release notes and later in this
migration guide.

## Upgrade from PBL 5 to PBL 7

The following sections describe how to upgrade from PBL 5 to PBL 7.

### Update Google Play Billing Library

Update the Play Billing Library dependency version in
your app's `build.gradle` file.

```groovy
dependencies {
    def billingVersion = 7.0.0

    implementation "com.android.billingclient:billing:$billingVersion"
}
```

Next, update your API references as described in the following sections.

### Change a user's subscription purchases

Play Billing Library 5 and earlier used [`ProrationMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode.md.txt)
to apply changes to a user's subscription purchases, such as upgrades
or downgrades. This API has been removed and replaced with
[`ReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode.md.txt).

### Handle subscription price changes

The previously deprecated `launchPriceConfirmationFlow` API has been removed.
For alternatives, see the [price changes guide](https://developer.android.com/google/play/billing/price-changes.md.txt).

### Handle subscription related API changes

The previously deprecated APIs `setOldSkuPurchaseToken`,
`setReplaceProrationMode`, `setReplaceSkusProrationMode` have been removed.

- Update `setOldSkuPurchaseToken` to [`setOldPurchaseToken`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setOldPurchaseToken).
- Update `setReplaceProrationMode` to [`setSubscriptionReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setSubscriptionReplacementMode).
- Update `setReplaceSkusProrationMode` to [`setSubscriptionReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setSubscriptionReplacementMode).

### Handle Play Billing Library errors

A new `NETWORK_ERROR` code indicates problems with the network connection
between the user's device and the Google Play system.

The `SERVICE_TIMEOUT` and `SERVICE_UNAVAILABLE` codes were also updated.

For more information, see [Handle BillingResult response codes](https://developer.android.com/google/play/billing/errors.md.txt).

### Handle pending transactions

The Play Billing Library no longer creates an order ID for pending purchases.
For these purchases, the order ID is populated after the purchase is moved
to the [`PURCHASED`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState.md.txt#PURCHASED) state. Make sure that your integration expects
an order ID only after a transaction has fully completed. You can still use
the purchase token for your records.

For more information about handling pending purchases, see the Play Billing
Library [integration guide](https://developer.android.com/google/play/billing/integrate.md.txt) and the
[purchase lifecycle management guide](https://developer.android.com/google/play/billing/lifecycle.md.txt).

### Handle removed alternative billing APIs

Removed
`BillingClient.Builder.enableAlternativeBilling`,
[`AlternativeBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener.md.txt), and
[`AlternativeChoiceDetails`](https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails.md.txt). Use
[`BillingClient.Builder.enableUserChoiceBilling()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder.md.txt#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener))
with [`UserChoiceBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener.md.txt) and
[`UserChoiceDetails`](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails.md.txt) in the listener callback instead.

This update is a renaming of the deprecated APIs with no behavior changes.

### Optional changes

PBL 7 includes two new optional APIs.

#### Support pending purchases for prepaid plans

See the [Handle Subscriptions and Pending Transactions](https://developer.android.com/google/play/billing/subscriptions.md.txt#pending) guide.

#### Virtual installment subscriptions

See the [Installment Subscriptions Integration](https://developer.android.com/google/play/billing/subscriptions.md.txt#installments) guide.

## Upgrade from PBL 6 to PBL 7

The following sections describe how to upgrade from PBL 6 to PBL 7.

### Update Google Play Billing Library

Update the Play Billing Library dependency version in
your app's `build.gradle` file.

```groovy
dependencies {
    def billingVersion = 7.0.0

    implementation "com.android.billingclient:billing:$billingVersion"
}
```

Next, update your API references as described in the following sections.

### Handle subscription related API changes

The previously deprecated APIs `setOldSkuPurchaseToken`,
`setReplaceProrationMode`, `setReplaceSkusProrationMode` have been removed.

- Update `setOldSkuPurchaseToken` to [`setOldPurchaseToken`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setOldPurchaseToken).
- Update `setReplaceProrationMode` to [`setSubscriptionReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setSubscriptionReplacementMode).
- Update `setReplaceSkusProrationMode` to [`setSubscriptionReplacementMode`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder.md.txt#setSubscriptionReplacementMode).

### Handle removed alternative billing APIs

Removed
`BillingClient.Builder.enableAlternativeBilling`,
[`AlternativeBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener.md.txt), and
[`AlternativeChoiceDetails`](https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails.md.txt). Use
[`BillingClient.Builder.enableUserChoiceBilling()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder.md.txt#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener))
with [`UserChoiceBillingListener`](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener.md.txt) and
[`UserChoiceDetails`](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails.md.txt) in the listener callback instead.

### Optional changes

PBL 7 includes two new optional APIs.

#### Support pending purchases for prepaid plans

See the [Handle Subscriptions and Pending Transactions](https://developer.android.com/google/play/billing/subscriptions.md.txt#pending) guide.

#### Virtual installment subscriptions

See the [Installment Subscriptions Integration](https://developer.android.com/google/play/billing/subscriptions.md.txt#installments) guide for
information on how to integrate these changes into your app.