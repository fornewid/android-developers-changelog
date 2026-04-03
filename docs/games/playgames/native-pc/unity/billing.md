---
title: https://developer.android.com/games/playgames/native-pc/unity/billing
url: https://developer.android.com/games/playgames/native-pc/unity/billing
source: md.txt
---

The Billing API lets you to sell digital goods and subscriptions. The C#
wrapper provides a type-safe, asynchronous interface for the underlying Google
Play Billing Library.

**Namespace:** `PlayPcSdkManaged.Billing`

**Client Class:** `BillingClient`

## Create the client

Always use the factory to create a `BillingClient`. This ensures that Unity-safe
callbacks are automatically registered.

```c#
using UnityEngine;
using System;
using System.Threading.Tasks;
using System.Collections.Generic;
// Required SDK Namespaces
using PlayPcSdkManaged.Billing;
using PlayPcSdkManaged.Unity;

public class BillingManager : MonoBehaviour
{
    private BillingClient _billingClient;

    public void SetupBilling()
    {
        try
        {
            // Creates the client with the required UnityBillingCallbacksHandler
            _billingClient = PlayPcSdkFactory.CreateBillingClient();
            Debug.Log("Billing Client created successfully.");
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to create Billing Client: {ex.Message}");
        }
    }

    private void OnDestroy()
    {
        // Always dispose of the client to clean up native C++ resources
        _billingClient?.Dispose();
    }
}
```

## Query product details

Before displaying items for sale, you must query details like price, title, and
description from Google Play.

```c#
public async Task GetProductDetailsAsync()
{
    try
    {
        // Define the list of products you want to query
        var productList = new List
        {
            // Use ProductType.InApp for consumables/non-consumables
            new ProductId { Id = "gem_pack_100", ProductType = ProductType.InApp },
            // Use ProductType.Subs for subscriptions
            new ProductId { Id = "gold_subscription", ProductType = ProductType.InApp }
        };

        var queryParams = new QueryProductDetailsParams { ProductIds = productList };

        // Async call
        var result = await _billingClient.QueryProductDetailsAsync(queryParams);

        if (result.IsOk)
        {
            foreach (var product in result.Value.ProductDetailsList)
            {
                // The formatted price (e.g., "$0.99") is inside the ProductOffers list
                if (product.ProductOffers != null && product.ProductOffers.Count > 0)
                {
                    var price = product.ProductOffers[0].FormattedPrice;
                    var offerToken = product.ProductOffers[0].OfferToken;
                    Debug.Log($"Product: {product.Title} | Price: {price} | Token: {offerToken}");
                }
            }
        }
        else
        {
            Debug.LogError($"Query Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```

## Launch purchase flow

To initiate a purchase, call `LaunchPurchaseFlowAsync` with the `OfferToken`
from the product details step.

```c#
public async Task BuyItemAsync(string offerToken)
{
    try
    {
        var purchaseParams = new LaunchPurchaseFlowParams
        {
            OfferToken = offerToken,
            Quantity = 1,
            // Optional: Attach obfuscated IDs for fraud detection
            ObfuscatedAccountId = "user_12345_hash",
            ObfuscatedProfileId = "profile_abcde_hash"
        };

        var result = await _billingClient.LaunchPurchaseFlowAsync(purchaseParams);

        if (result.IsOk)
        {
            var purchase = result.Value.ProductPurchaseDetails;
            Debug.Log($"Purchase Successful! Order ID: {purchase.OrderId}");

            // IMPORTANT: You must now Acknowledge or Consume this purchase.
            // If you don't, Google Play will refund the user after a few days.
            if (!purchase.IsAcknowledged)
            {
                // Decide based on your game logic if it's consumable or permanent
                await HandlePurchaseAsync(purchase);
            }
        }
        else if (result.Code == BillingError.UserCanceled)
        {
            Debug.Log("User canceled the purchase flow.");
        }
        else
        {
            Debug.LogError($"Purchase Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```

## Query existing purchases (Restore)

Call `QueryPurchasesAsync` on game startup to restore items you already own, for
example, after a game reinstallation, or to check for pending transactions.

This example demonstrates how to route purchases to *Acknowledge* for
permanent items or *Consume* for consumables.

```c#
public async Task CheckExistingPurchasesAsync()
{
    try
    {
        // Fetches all purchases owned by the user
        var result = await _billingClient.QueryPurchasesAsync();

        if (result.IsOk)
        {
            foreach (var purchase in result.Value.ProductPurchaseDetails)
            {
                Debug.Log($"User owns: {purchase.ProductId} | State: {purchase.PurchaseState}");

                // Process any purchase that hasn't been acknowledged yet
                if (purchase.PurchaseState == PurchaseState.Purchased && !purchase.IsAcknowledged)
                {
                    await HandlePurchaseAsync(purchase);
                }
            }
        }
        else
        {
            Debug.LogError($"Restore Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}

// Helper method to route purchases
private async Task HandlePurchaseAsync(ProductPurchaseDetails purchase)
{
    // Example logic: "gem_pack" is consumable, everything else is permanent
    if (purchase.ProductId.Contains("gem_pack"))
    {
        await ConsumeItemAsync(purchase.PurchaseToken);
    }
    else
    {
        await AcknowledgeItemAsync(purchase.PurchaseToken);
    }
}
```

## Acknowledge a purchase

Non-consumable items (for example, "Premium Upgrade" or "Level Pack") must be
acknowledged. This indicates to Google Play that you have granted the item to
the user.

```c#
public async Task AcknowledgeItemAsync(string purchaseToken)
{
    try
    {
        var acknowledgeParams = new AcknowledgePurchaseParams
        {
            PurchaseToken = purchaseToken
        };

        var result = await _billingClient.AcknowledgePurchaseAsync(acknowledgeParams);

        if (result.IsOk)
        {
            Debug.Log("Purchase Acknowledged. Usage rights granted permanently.");
        }
        else
        {
            Debug.LogError($"Acknowledge Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```

## Consume a purchase

Consumable items, such as "100 Gems" or "Health Potion", must be consumed to
allow for repurchase.

```c#
public async Task ConsumeItemAsync(string purchaseToken)
{
    try
    {
        var consumeParams = new ConsumePurchaseParams
        {
            PurchaseToken = purchaseToken
        };

        var result = await _billingClient.ConsumePurchaseAsync(consumeParams);

        if (result.IsOk)
        {
            Debug.Log("Item Consumed. User can buy it again.");
            // Add the gems/coins to the user's inventory here
        }
        else
        {
            Debug.LogError($"Consume Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```