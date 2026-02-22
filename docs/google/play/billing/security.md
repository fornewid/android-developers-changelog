---
title: https://developer.android.com/google/play/billing/security
url: https://developer.android.com/google/play/billing/security
source: md.txt
---

As your app grows in popularity, it can also attract the unwanted attention of malicious users that might want to abuse your app. This topic describes recommendations that you should use to help prevent these attacks on your billing integration and decrease the impact of abuse in your app.

## Move sensitive logic to your backend

As much as your app design permits, move sensitive data and logic to a backend server that you control. The more data and logic you have in a frontend device, the more vulnerable it is to being modified or tampered with.

For example, an online chess game should validate all moves in the backend instead of trusting that the frontend always sends legal moves.

Furthermore, if you find vulnerabilities or security issues, depending on your system design, it might be easier to debug, fix, and roll out updates on the backend rather than the frontend.

## Verify purchases before granting entitlements

A special case of sensitive data and logic that should be handled in the backend is purchase verification and acknowledgement. After a user has made a purchase, you should do the following:

1. Send the corresponding`purchaseToken`to your backend. This means that you should maintain a record of all`purchaseToken`values for all purchases.
2. Verify that the`purchaseToken`value for the current purchase does not match any previous`purchaseToken`values.`purchaseToken`is globally unique, so you can safely use this value as a primary key in your database.
3. Use the[`Purchases.products:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get)or[`Purchases.subscriptionsv2:get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)endpoints in the Google Play Developer API to verify with Google that the purchase is legitimate.
4. If the purchase is legitimate and has not been used in the past, you can then safely grant entitlement to the in-app item or subscription.
5. For subscriptions, when[`linkedPurchaseToken`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)is set in`Purchases.subscriptionsv2:get`, you should also remove the`linkedPurchaseToken`from your database and revoke the entitlement that is granted to the`linkedPurchaseToken`to ensure that multiple users are not entitled for the same purchase.
6. You should grant entitlement only when the purchase state is`PURCHASED`and make sure to handle the`PENDING`purchases correctly. If there is a spike of`CANCELED`purchases, you may be granting entitlements when the purchase is still in`PENDING`state. You can find more information at[Handling pending transactions](https://developer.android.com/google/play/billing/integrate#pending).
7. After granting entitlement, if you want to consume and acknowledge a consumable product, use the[`Purchases.products:consume`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume)Play Developer API on your secure backend server. To acknowledge a non-consumable product or a subscription, call the relevant Play Developer API endpoint, either[`Purchases.products:acknowledge`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge)or[`Purchases.subscriptions:acknowledge`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge)on your secure backend server. Acknowledgment is required, as it notifies Google Play that the user has been granted entitlement to the purchase. You should acknowledge the purchase immediately after granting entitlement.

   Note that while you can acknowledge or consume the purchase on the client side through your app, server side APIs provide additional protection against issues like poor network connectivity and malicious activity. For example, consider if a user has purchased an item from your app but they lost network connectivity while the purchase was being validated. Without server acknowledgment, they might need to log back in through the app to complete the acknowledgement process. Otherwise, if the user does not log back in within three days, the purchase is automatically refunded due to lack of purchase acknowledgement. Server acknowledgment prevents this scenario by sending acknowledgment as soon as Google Play notifies the server that the purchase is valid.

   For more information about purchase acknowledgment and consumption, see[Processing purchases](https://developer.android.com/google/play/billing/integrate#process).

| **Note:** Do not grant entitlement when the purchase state is`PENDING`.
| **Note:** Do not use`orderId`to check for duplicate purchases or as a primary key in your database, as not all purchases are guaranteed to generate an`orderId`. In particular, purchases made with promo codes do not generate an`orderId`.

## Protecting your unlocked content

To prevent malicious users from redistributing your unlocked content, do not bundle it in your APK file. Instead, do one of the following:

- Use a real-time service to deliver your content, such as a content feed. Delivering content through a real-time service also enables you to keep your content fresh.
- Use a remote server to deliver your content.

When you deliver content from a remote server or a real-time service, you can store the unlocked content in device memory or store it on the device's SD card. If you store content on an SD card, be sure to encrypt the content and use a device-specific encryption key.

## Detect and handle voided purchases

*Voided purchases* are purchases that have been canceled, revoked, or charged back. If a voided purchase had previously granted in-app items or other content to a user, you can use the[Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases)to obtain the reason the purchase was voided along with any associated content that you can claw back.
| **Note:** Voided purchases without any associated clawback content are not exposed by the Voided Purchases API.

Purchases for in-app items and subscriptions can be voided for a variety of reasons, including the following:

- A purchase is canceled, either by the user, by the developer, or by Google (including unacknowledged auto-canceled purchases). For subscriptions, note that this refers to canceling the*purchase* of a subscription, rather than[canceling the subscription itself](https://support.google.com/googleplay/answer/7018481?co=GENIE.Platform%3DAndroid).
- A purchase is charged back.
- The app developer cancels or refunds a user order and checks the "revoke" option in the console.

Based on the reason for the voided purchase, and taking previous user behavioral data into account, you can decide on a course of action. We recommend implementing one or more of the following:

- **Perform clawbacks:**When a purchase is voided, you can claw back unused items as if they were never purchased. For example, if an in-game currency purchase was voided, you could claw back currency that was already granted to the user. In the case where the user has already spent the currency, consider setting the currency balance to negative and limiting app activity and future purchases until the currency balance is positive.
- **Multiple strikes implementation:**Consider taking less drastic actions for first-time offenders, such as displaying in-app warnings. For repeat offenders, consider more severe measures.
- **Temporarily disable purchases:**Similar to the multiple strikes implementation, consider disabling purchases for users with voided purchases until you can more thoroughly investigate why the purchases were voided.
- **Temporarily or permanently disallow access to your app:**For extreme cases with repeated malicious activity, consider disallowing access to your app, either temporarily or permanently.
- **Make frequent calls to the Voided Purchases API:** When you detect one or more voided purchases, consider making more frequent calls to the Voided Purchases API to claw back purchases before the user can consume them. You can find more information on Voided Purchases API quotas in the[Voided Purchases API documentation](https://developers.google.com/android-publisher/voided-purchases#quotas).

## Help Google detect fraud before it happens

Some types of fraud are related to malicious users who create multiple Google and in-app accounts to hide their activity.

Use the[`setObfuscatedAccountId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String))and[`setObfuscatedProfileId`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid)methods in the builder for[`BillingFlowParams`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder)to help Google map Google Accounts to in-app accounts.

Google uses this data to detect suspicious behavior and block some types of fraudulent transactions before they are completed.

## Taking action against trademark and copyright infringement

If you are using a remote server to deliver or manage content, have your app verify the purchase state of the unlocked content whenever a user accesses the content. This allows you to revoke use when necessary and minimize piracy. If you see your content being redistributed on Google Play, be sure to act quickly and decisively. For more details, see the[Frequently Asked Copyright Questions](https://support.google.com/legal/answer/4558836)page in the Copyright Help Center.