---
title: https://developer.android.com/google/play/billing/developer-payload
url: https://developer.android.com/google/play/billing/developer-payload
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/billing/llms.txt

Developer payload has historically been used for various purposes, including
fraud prevention and attributing purchases to the correct user. With versions
2.2 and higher of the Google Play Billing Library, intended use cases that
previously relied on developer payload are now fully supported in other parts
of the library.

With this support in place, we have deprecated developer payload, starting with
version 2.2 of the Google Play Billing Library. Methods associated with
developer payload have been deprecated in version 2.2 and were removed in
version 3.0. Note that your app can continue to retrieve developer
payload for purchases made using either previous versions of the library or
AIDL.

For a detailed list of changes, see the
[Google Play Billing Library 2.2 release notes](https://developer.android.com/google/play/billing/release-notes.md.txt#2-2) and
[Google Play Billing Library 3.0 release notes](https://developer.android.com/google/play/billing/release-notes.md.txt#3-0).

## Purchase verification

To ensure purchases are authentic and not forged or replayed, Google recommends
using the purchase token (obtained from the [`getPurchaseToken()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getpurchasetoken) method in
the [`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt) object) along with the Google Play Developer APIs to
verify purchases are authentic. For more information, see
[Fight fraud and abuse](https://developer.android.com/google/play/billing/security.md.txt).

## Purchase attribution

Many apps, particularly games, need to ensure that a purchase is correctly
attributed to the in-game character or avatar or in-app user profile that
initiated the purchase. Starting with Google Play Billing Library 2.2, your app
can pass obfuscated account and profile identifiers to Google when launching the
purchase dialog and have them returned when retrieving a purchase.

Use the [`setObfuscatedAccountId()`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder.md.txt#setObfuscatedAccountId(java.lang.String)) and [`setObfuscatedProfileId()`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder.md.txt#setobfuscatedprofileid)
parameters in [`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.md.txt) and retrieve them using the
[`getAccountIdentifiers()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getAccountIdentifiers()) method in the [`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt) object.

> [!NOTE]
> **Note:** Purchases made using previous versions of the library using [`setAccountId()`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder.md.txt#setAccountId(java.lang.String)) (renamed to `setObfuscatedAccountId()`) are not returned by `getAccountIdentifiers()`.

## Associate metadata with a purchase

Google recommends storing metadata about a purchase on a secure backend
server that you maintain. This purchase metadata should be associated with the
purchase token obtained using [`getPurchaseToken`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getPurchaseToken()) in the [`Purchase`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt)
object. This data can be persisted by passing the purchase token and metadata
to your backend when your [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener.md.txt) is called after a
successful purchase.

To ensure metadata is associated if the purchase flow is interrupted, store it
on your backend server with your user's account ID, SKU, and timestamp before
launching the purchase dialog.

If the purchase flow is interrupted before your [`PurchasesUpdatedListener`](https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener.md.txt)
is called, your app will discover the purchase once your app resumes and calls
[`BillingClient.queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.md.txt#querypurchasesasync). You can then send the values
retrieved from the `Purchase` object's [`getPurchaseTime()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getPurchaseTime()),
[`getSku()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getsku), and [`getPurchaseToken()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getpurchasetoken) methods to your backend server
to look up metadata, associate the metadata with the purchase token, and
continue processing the purchase. Note that the timestamp you initially stored
won't exactly match the value from the `Purchase` object's
[`getPurchaseTime()`](https://developer.android.com/reference/com/android/billingclient/api/Purchase.md.txt#getPurchaseTime()), so you would need to compare them in an approximate
way. For example, you can check if the values are within a certain time period
of each other.