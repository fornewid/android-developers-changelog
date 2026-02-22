---
title: https://developer.android.com/games/playgames/native-pc/billing
url: https://developer.android.com/games/playgames/native-pc/billing
source: md.txt
---

> [!CAUTION]
> **Caution:** The SDK only supports in-app purchases. If your game requires subscriptions please contact your Google Partner for assistance.

Monetize your game by selling digital products using Play Billing. The SDK
offers APIs to show products available to buy, launch the purchase flow, and
process purchases. Calls to these billing APIs are performed using
the Google Account that launched the game inside of the Google Play Games
client and don't require any additional sign-in steps.

If you have integrated with the
[Android Play Billing library](https://developer.android.com/google/play/billing/integrate), these
Play Billing APIs should look familiar. Any server-side integrations with Play
Billing can be reused by PC titles as they are the same across both Android \&
PC.

## Prerequisites

- Complete the [SDK setup](https://developer.android.com/games/playgames/native-pc/setup).

- Read the overview of [Google Play's billing system](https://developer.android.com/google/play/billing).

- Complete [Play Billing setup](https://developer.android.com/google/play/billing/getting-ready).

## **Step 1**: Query for previous purchases \& purchases completed outside of your application

When your application starts up or when it re-enters the foreground,
query for purchases. This is necessary to detect purchases that occurred outside
of your game or to unlock access to purchases previously made by the user.

1. Query for purchases using [`BillingClient::QueryPurchases`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#querypurchases).

2. Continue by [processing the purchases](https://developer.android.com/games/playgames/native-pc/billing#step-4).

    // Query for purchases when:
    // - Application starts up
    // - Application window re-enters the foreground
    auto promise = std::make_shared<std::promise<QueryPurchasesResult>>();
    billing_client.QueryPurchases([promise](QueryPurchasesResult result) {
       promise->set_value(std::move(result));
    });

    auto query_purchases_result = promise->get_future().get();
    if (query_purchases_result.ok()) {
      auto purchases = query_purchases_result.value().product_purchase_details;
      // Process the purchases
    } else {
      // Handle the error
    }

## **Step 2**: Show products available to buy

You are ready to query for your available products and display them to your
users. Querying for product details is an important step before displaying your
products to your users, as it returns localized product information.

Before offering a product for sale, check that the user does not already own
the product. If the user has a consumable that is still in their purchase
history, you must consume the product before they can buy it again.

1. Query for product details using [`BillingClient::QueryProductDetails`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#queryproductdetails). Pass in the product IDs that you registered inside of the Google Play Console.
2. Render the [`ProductDetails`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-details) which includes the product's localized name \& offer price.
3. Keep a reference to the product's [`offer_token`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-offer#offer_token). This is used to launch a purchase flow for the offer.

    QueryProductDetailsParams params;
    params.product_ids.push_back({"example_costmetic_1", ProductType::kTypeInApp});
    params.product_ids.push_back({"example_costmetic_1", ProductType::kTypeInApp});
    params.product_ids.push_back({"example_battle_pass", ProductType::kTypeInApp});

    auto promise = std::make_shared<std::promise<QueryProductDetailsResult>>();
    billing_client.QueryProductDetails(params, [promise](QueryProductDetailsResult result) {
       promise->set_value(std::move(result));
    });

    auto query_product_details_result = promise->get_future().get();
    if (query_product_details_result.ok()) {
       auto product_details = query_product_details_result.value().product_details;
       // Display the available products and their offers to the user
    } else {
       // Handle the error
    }

## **Step 3**: Launch a purchase flow

When the user shows an intent to buy a product you have showed them you're ready
to launch the purchase flow.

1. Start by calling [`BillingClient::LaunchPurchaseFlow()`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#launchpurchaseflow). Pass in the [`offer_token`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-offer#offer_token) obtained when querying the product details.
2. Once the purchase has been completed the continuation function will be called with the result.
3. If successful, the continuation contains a [`ProductPurchaseDetails`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details). Continue by [processing the purchase](https://developer.android.com/games/playgames/native-pc/billing#step-4).

    LaunchPurchaseFlowParams params { product_offer.offer_token };

    auto promise = std::make_shared<std::promise<LaunchPurchaseFlowResult>>();
    billing_client.LaunchPurchaseFlow(params, [promise](LaunchPurchaseFlowResult result) {
       promise->set_value(std::move(result));
    });
    // The purchase flow has started and is now in progress.

    auto launch_purchase_flow_result = promise->get_future().get();

    // The purchase flow has now completed.
    if (launch_purchase_flow_result.ok()) {
       auto purchase = launch_purchase_flow_result.value().product_purchase_details;
       // Process the purchase
    } else if (launch_purchase_flow_result.code() == BillingError::kUserCanceled) {
       // Handle an error caused by the user canceling the purchase flow
    } else {
       // Handle any other error codes
    }

## **Step 4**: Process a purchase

> [!WARNING]
> **Warning:** Failing to complete purchase processing within three days will result in the transaction being **automatically refunded** and the entitlement being voided. If you are using a tester account, it needs to process the purchase flow within 3 minutes.

### Process with a backend server

> [!TIP]
> **Tip:** Using the [server-side Play Billing APIs](https://developer.android.com/google/play/billing/security#verify) to complete the purchase is more secure than without a backend server and is recommended.

For games with a backend server, complete the processing by sending the
[`purchase_token`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details#purchase_token) to your backend server. Complete the
remainder of processing using the
[server-side Play Billing APIs](https://developer.android.com/google/play/billing/security#verify). This server-side integration
is the same as done for an Android game that has integrated with Play Billing.

    void ProcessPurchasesWithServer(std::vector<ProductPurchaseDetails> purchases) {
       std::vector<std::string> purchase_tokens;
       for (const auto& purchase : purchases) {
          purchase_tokens.push_back(purchase.purchase_token);
       }

       // Send purchase tokens to backend server for processing
    }

### Process without a backend server

> [!NOTE]
> **Note:** Processing purchases without a backend server requires your game to be allow-listed. Please contact your Google Partner if your game requires access.

1. Ensure the user's payment is not pending by checking
   [`ProductPurchaseDetails::purchase_state`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details#purchase_state) is
   [`PurchaseState::kPurchaseStatePurchased`](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/billing#purchasestate). If
   the purchase state is pending notify the user that they need to complete
   additional steps before they can receive their purchased product.

2. Grant the user access to the purchased product \& update your game's
   entitlement storage.

3. For non-consumable purchases (products that may only ever be purchased once)
   check if the purchase has already been acknowledged using
   [`ProductPurchaseDetails::is_acknowledged`](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details#is_acknowledged).

   1. If the purchase has not been acknowledged notify Google that the user is being granted an entitlement to the product by calling [`BillingClient::AcknowledgePurchase`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#acknowledgepurchase).
4. For consumable purchases (products that may be purchased more than once)
   notify Google that the user is being granted an entitlement to the product by
   calling [`BillingClient::ConsumePurchase`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#consumepurchase).

> [!NOTE]
> **Note:** Because consumption requests can occasionally fail, you must check your secure backend server to ensure that each purchase token hasn't been used so your app doesn't grant entitlement multiple times for the same purchase. For this reason we strongly recommend processing consumable purchases with a backend server. Alternatively, your app can wait until you receive a successful consumption response from Google Play before granting entitlement. If you choose to withhold purchases from the user until Google Play sends a successful consumption response, you must be very careful not to lose track of the purchases for which you have sent a consumption request.

    void ProcessPurchasesWithoutServer(std::vector<ProductPurchaseDetails> purchases) {
       std::vector<std::string> entitled_product_ids;
       for (const auto& purchase : purchases) {
          auto was_successful = ProcessPurchasePurchaseWithoutServer(purchase);
          if (was_successful) {
             entitled_product_ids.push_back(purchase.product_id);
          }
       }

       // Note that non-consumable products that were previously purchased may have
       // been refunded. These purchases will stop being returned by
       // `QueryPurchases()`. If your game has given a user access to one of these
       // products storage they should be revoked.
       //
       // ...
    }

    bool ProcessPurchasePurchaseWithoutServer(ProductPurchaseDetails purchase) {
       auto is_purchase_completed =
          purchase.purchase_state == PurchaseState::kPurchaseStatePurchased;
       if (!is_purchase_completed) {
          // Notify the user that they need to take additional steps to complete
          // this purchase.
          return false;
       }

       // Determine if the product ID is associated with a consumable product.
       auto is_consumable = IsConsumableProductId(purchase.product_id);
       if (is_consumable) {
          // Grant an entitlement to the product to the user.
          // ...
          // Then, notify Google by consuming the purchase.

          ConsumePurchaseParams params { purchase.purchase_token };
          auto promise = std::make_shared<std::promise<ConsumePurchaseResult>>();
          billing_client.ConsumePurchase(params, [promise](ConsumePurchaseResult result) {
             promise->set_value(std::move(result));
          });

          auto consume_purchase_result = promise->get_future().get();
          if (!consume_purchase_result.ok()) {
             // Examine the failure code & message for more details & notify user
             // of failure.
             // ...
             return false;
          }

          return true;
       }

       // Otherwise the product is assumed to be a non-consumable.

       // Grant an entitlement to the product to the user.
       // ...
       // Then, notify Google by acknowledging the purchase (if not already done).

       if (purchase.is_acknowledged) {
          return true;
       }

       AcknowledgePurchaseParams params { purchase.purchase_token };
       auto promise = std::make_shared<std::promise<AcknowledgePurchaseResult>>();
       billing_client.AcknowledgePurchase(params, [promise](AcknowledgePurchaseResult result) {
          promise->set_value(std::move(result));
       });

       auto acknowledge_purchase_result = promise->get_future().get();
       if (!acknowledge_purchase_result.ok()) {
          // Examine the failure code & message for more details & notify user
          // of failure.
          // ...
          return false;
       }

       return true;
    }

## **Step 5**: Test your integration

You are now ready to test your integration with Play Billing. To test during the
development phase, we recommend leveraging **license testers**. License testers
have access to test payments that avoid charging real money for purchases.

For instructions on how to setup license testers and a suite of manual tests
we recommend exercising see the documentation on how to
[test your Google Play Billing Library integration](https://developer.android.com/google/play/billing/test).