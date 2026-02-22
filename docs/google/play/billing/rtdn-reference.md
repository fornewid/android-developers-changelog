---
title: https://developer.android.com/google/play/billing/rtdn-reference
url: https://developer.android.com/google/play/billing/rtdn-reference
source: md.txt
---

This document lists and describes the types of[Real-time developer notifications](https://developer.android.com/google/play/billing/getting-ready#configure-rtdn)that you can receive from Google Play.
| **Note:** You must call the[Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)after receiving Real-time developer notifications to get the complete status and update your own backend state. These notifications tell you only that the purchase state changed. They do not give you complete information about the purchase.

## Encoding

Each publish made to a Cloud Pub/Sub topic contains a single base64-encoded data field.  

    {
      "message": {
        "attributes": {
          "key": "value"
        },
        "data": "eyAidmVyc2lvbiI6IHN0cmluZywgInBhY2thZ2VOYW1lIjogc3RyaW5nLCAiZXZlbnRUaW1lTWlsbGlzIjogbG9uZywgIm9uZVRpbWVQcm9kdWN0Tm90aWZpY2F0aW9uIjogT25lVGltZVByb2R1Y3ROb3RpZmljYXRpb24sICJzdWJzY3JpcHRpb25Ob3RpZmljYXRpb24iOiBTdWJzY3JpcHRpb25Ob3RpZmljYXRpb24sICJ0ZXN0Tm90aWZpY2F0aW9uIjogVGVzdE5vdGlmaWNhdGlvbiB9",
        "messageId": "136969346945"
      },
      "subscription": "projects/myproject/subscriptions/mysubscription"
    }

After you decode the base64-encoded data field, the`DeveloperNotification`contains the following fields:  

    {
      "version": string,
      "packageName": string,
      "eventTimeMillis": long,
      "oneTimeProductNotification": OneTimeProductNotification,
      "subscriptionNotification": SubscriptionNotification,
      "voidedPurchaseNotification": VoidedPurchaseNotification,
      "testNotification": TestNotification
    }

These fields are described in the following table.

|----------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property name**          | **Value**                  | **Description**                                                                                                                                                                                                                                                                              |
| version                    | string                     | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields.                                                                                                                                                                              |
| packageName                | string                     | The package name of the application that this notification relates to (for example, \`com.some.thing\`).                                                                                                                                                                                     |
| eventTimeMillis            | long                       | The timestamp when the event occurred, in milliseconds since the Epoch.                                                                                                                                                                                                                      |
| subscriptionNotification   | SubscriptionNotification   | If this field is present, then this notification is related to a subscription, and this field contains additional information related to the subscription. Note that this field is mutually exclusive with oneTimeProductNotification, voidedPurchaseNotification, and testNotification.     |
| oneTimeProductNotification | OneTimeProductNotification | If this field is present, then this notification is related to a one-time purchase, and this field contains additional information related to the purchase. Note that this field is mutually exclusive with subscriptionNotification, voidedPurchaseNotification, and testNotification.      |
| voidedPurchaseNotification | VoidedPurchaseNotification | If this field is present, then this notification is related to a voided purchase, and this field contains additional information related to the voided purchase. Note that this field is mutually exclusive with oneTimeProductNotification, subscriptionNotification, and testNotification. |
| testNotification           | TestNotification           | If this field is present, then this notification is related to a test publish. These are sent only through the Google Play Developer Console. Note that this field is mutually exclusive with oneTimeProductNotification, subscriptionNotification, and voidedPurchaseNotification.          |

## SubscriptionNotification

A`SubscriptionNotification`contains the following fields:  

    {
      "version": string,
      "notificationType": int,
      "purchaseToken": string
    }

|-------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property name** | **Value** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| version           | string    | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| notificationType  | int       | The notificationType for a subscription can have the following values: - (1) SUBSCRIPTION_RECOVERED - A subscription was recovered from account hold or resumed from pause. - (2) SUBSCRIPTION_RENEWED - An active subscription was renewed. - (3) SUBSCRIPTION_CANCELED - A subscription was either voluntarily or involuntarily cancelled. For voluntary cancellation, sent when the user cancels. - (4) SUBSCRIPTION_PURCHASED - A new subscription was purchased. - (5) SUBSCRIPTION_ON_HOLD - A subscription has entered account hold (if enabled). - (6) SUBSCRIPTION_IN_GRACE_PERIOD - A subscription has entered grace period (if enabled). - (7) SUBSCRIPTION_RESTARTED - User has restored their subscription from**Play \> Account \> Subscriptions** . The subscription was canceled but had not expired yet when the user restores. For more information, see[Restorations](https://developer.android.com/google/play/billing/subscriptions#restore). - (8) SUBSCRIPTION_PRICE_CHANGE_CONFIRMED (DEPRECATED) - A subscription price change has successfully been confirmed by the user. - (9) SUBSCRIPTION_DEFERRED - A subscription's recurrence time has been extended. - (10) SUBSCRIPTION_PAUSED - A subscription has been paused. - (11) SUBSCRIPTION_PAUSE_SCHEDULE_CHANGED - A subscription pause schedule has been changed. - (12) SUBSCRIPTION_REVOKED - A subscription has been revoked from the user before the expiration time. - (13) SUBSCRIPTION_EXPIRED - A subscription has expired. - (17) SUBSCRIPTION_ITEMS_CHANGED - An item in a subscription bundle has been changed. - (18) SUBSCRIPTION_CANCELLATION_SCHEDULED - A cancellation for an installment subscription has been scheduled to take effect at the end of the commitment period. - (19) SUBSCRIPTION_PRICE_CHANGE_UPDATED - A subscription item's price change details are updated. - (20) SUBSCRIPTION_PENDING_PURCHASE_CANCELED - A pending transaction of a subscription has been canceled. - (22) SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED - A subscription's[consent period for price step-up](https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-stepup-consent)has begun or the user has provided consent for the price step-up. This RTDN is sent only for subscriptions in a region where price step-up is required. |
| purchaseToken     | string    | The token provided to the user's device when the subscription was purchased.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Example

Here's an example of a notification for a new subscription purchase:  

    {
      "version":"1.0",
      "packageName":"com.some.thing",
      "eventTimeMillis":"1503349566168",
      "subscriptionNotification":
      {
        "version":"1.0",
        "notificationType":4,
        "purchaseToken":"PURCHASE_TOKEN"
      }
    }

## OneTimeProductNotification

| **Note:** A`OneTimeProductNotification`is sent only if you've chosen to receive one-time product purchase events. For more information, see[Enable real-time developer notifications for your app](https://developer.android.com/google/play/billing/getting-ready#enable-rtdn "Real-time developer notifications").

A`OneTimeProductNotification`contains the following fields:  

    {
      "version": string,
      "notificationType": int,
      "purchaseToken": string,
      "sku": string
    }

|-------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property Name** | **Value** | **Description**                                                                                                                                                                                                                                              |
| version           | string    | The version of this notification. Initially, this will be "1.0". This version is distinct from other version fields.                                                                                                                                         |
| notificationType  | int       | The type of notification. It can have the following values: - (1) ONE_TIME_PRODUCT_PURCHASED - A one-time product was successfully purchased by a user. - (2) ONE_TIME_PRODUCT_CANCELED - A pending one-time product purchase has been canceled by the user. |
| purchaseToken     | string    | The token provided to the user's device when purchase was made.                                                                                                                                                                                              |
| sku               | string    | The purchased one-time product ID (for example, "sword_001")                                                                                                                                                                                                 |

### Example

Here's an example of a notification for a new one-time purchase:  

    {
      "version":"1.0",
      "packageName":"com.some.thing",
      "eventTimeMillis":"1503349566168",
      "oneTimeProductNotification":
      {
        "version":"1.0",
        "notificationType":1,
        "purchaseToken":"PURCHASE_TOKEN",
        "sku":"my.sku"
      }
    }

## VoidedPurchaseNotification

A`VoidedPurchaseNotification`contains the following fields:

|-------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property Name** | **Value** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `purchaseToken`   | `string`  | The token associated with the purchase that has been voided. This information is provided to the developer when a new purchase occurs.                                                                                                                                                                                                                                                                                                                                                                       |
| `orderId`         | `string`  | The unique order ID associated with the transaction that has been voided. For one time purchases, this represents the only order ID generated for the purchase. For auto-renewing subscriptions, a new order ID is generated for each renewal transaction.                                                                                                                                                                                                                                                   |
| `productType`     | `int`     | The**productType**for a voided purchase can have the following values: - (1)`PRODUCT_TYPE_SUBSCRIPTION`- A subscription purchase has been voided. - (2)`PRODUCT_TYPE_ONE_TIME`- A one-time purchase has been voided.                                                                                                                                                                                                                                                                                         |
| `refundType`      | `int`     | The**refundType**for a voided purchase can have the following values: - (1)`REFUND_TYPE_FULL_REFUND`- The purchase has been fully voided. - (2)`REFUND_TYPE_QUANTITY_BASED_PARTIAL_REFUND`- The purchase has been partially voided by a quantity-based partial refund, applicable only to multi-quantity purchases. A purchase can be partially voided multiple times. Note when the remaining total quantity of a multi-quantity purchase is refunded, the**refundType**will be**REFUND_TYPE_FULL_REFUND**. |

### Example

Here's an example of a notification for a new voided purchase:  

    {
      "version":"1.0",
      "packageName":"com.some.app",
      "eventTimeMillis":"1503349566168",
      "voidedPurchaseNotification":
      {
        "purchaseToken":"PURCHASE_TOKEN",
        "orderId":"GS.0000-0000-0000",
        "productType":1
        "refundType":1
      }
    }

### Consuming VoidedPurchaseNotification

When your RTDN client receives a`VoidedPurchaseNotification`, note the following information:

- **`packageName`**: Identifies the app.
- **`eventTimeMillis`**: Informs you of the time the status change occurred.
- **`purchaseToken`**: The token provided to the user's device when the product was purchased.
- **`orderId`**: Identifies the order associated with the voided transaction.
- **`productType`**: Indicates if the voided purchase was an in-app purchase or a subscription.
- **`refundType`**: Specifies the type of refund that voided the purchase.

| **Tip:** If you only need to locate the right purchase and order for entitlement adjustments, the information provided in the`VoidedPurchaseNotification`is sufficient. For additional data about voided purchases, use the[Google Play Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases). This API provides a pull model for retrieving voided purchase data within a specified timestamp range.
| **Note:** For partially voided multi-quantity purchases, the`refundableQuantity`field provided by[`purchases.productsv2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2)contains the remaining number of purchased products that have not been voided.

## TestNotification

A`TestNotification`contains the following fields:  

    {
      "version": string
    }

|-------------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| **Property name** | **Value** | **Description**                                                                                                 |
| version           | string    | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields. |

### Example

Here's an example of a test notification:  

    {
      "version":"1.0",
      "packageName":"com.some.thing",
      "eventTimeMillis":"1503350156918",
      "testNotification":
      {
        "version":"1.0"
      }
    }