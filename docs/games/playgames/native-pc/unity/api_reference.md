---
title: https://developer.android.com/games/playgames/native-pc/unity/api_reference
url: https://developer.android.com/games/playgames/native-pc/unity/api_reference
source: md.txt
---

This page lists the classes, interfaces, structures, and enumerations available
in the Google Play Games PC SDK for Unity API.

## Namespace: PlayPcSdkManaged.Initialization

Handles the connection lifecycle between the Unity game and the
Play Games PC SDK runtime.

### Classes

| Type | Name | Description |
|---|---|---|
| `Class` | `GooglePlayInitialization` | The static entry point for the SDK. Contains methods to initialize the connection asynchronously. |
| `Class` | `InitializeResult` | Represents the result of an initialization operation. |

### Enums

| Type | Name | Description |
|---|---|---|
| `Enum` | `InitializationError` | Error codes returned during initialization (e.g., `SdkRuntimeUnavailable`, `SdkRuntimeUpdateRequired`). |

## Namespace: PlayPcSdkManaged.Billing

Provides access to Google Play Billing features, including In-App Purchases
(IAP) and Subscriptions.

### Classes

Clients and results

| Type | Name | Description |
|---|---|---|
| `Class` | `BillingClient` | The main client for interacting with the Billing service. Manages the native C++ connection and must be disposed. |
| `Class` | `QueryProductDetailsResult` | The result returned by `QueryProductDetailsAsync`. Contains the list of product details on success. |
| `Class` | `LaunchPurchaseFlowResult` | The result returned by `LaunchPurchaseFlowAsync`. Contains purchase details on success. |
| `Class` | `QueryPurchasesResult` | The result returned by `QueryPurchasesAsync`. Contains the list of user-owned purchases. |
| `Class` | `AcknowledgePurchaseResult` | The result returned by `AcknowledgePurchaseAsync`. |
| `Class` | `ConsumePurchaseResult` | The result returned by `ConsumePurchaseAsync`. |

### Structs

Parameters and Models

| Type | Name | Description |
|---|---|---|
| `Struct` | `QueryProductDetailsParams` | Input parameters for querying product details, containing the list of Product IDs. |
| `Struct` | `LaunchPurchaseFlowParams` | Input parameters for launching a purchase, including `OfferToken`, `Quantity`, and obfuscated IDs. |
| `Struct` | `AcknowledgePurchaseParams` | Input parameters for acknowledging a purchase, requiring the `PurchaseToken`. |
| `Struct` | `ConsumePurchaseParams` | Input parameters for consuming a purchase, requiring the `PurchaseToken`. |
| `Struct` | `ProductId` | Represents a product identifier and its type (`InApp` or `Subs`). |
| `Struct` | `ProductDetails` | Detailed information about a product, including title, description, and available offers. |
| `Struct` | `ProductOffer` | Represents a specific pricing offer for a product, including `FormattedPrice` and `OfferToken`. |
| `Struct` | `ProductPurchaseDetails` | Details of a transaction, including `OrderId`, `PurchaseState`, and `PurchaseToken`. |

### Enums

| Type | Name | Description |
|---|---|---|
| `Enum` | `BillingError` | Status codes representing the outcome of a billing operation (e.g., `Ok`, `UserCanceled`, `ItemAlreadyOwned`). |
| `Enum` | `ProductType` | Defines the type of product: `InApp` (1) or `Subs` (Subscription). |
| `Enum` | `PurchaseState` | The state of the purchase: `Unspecified` (0), `Purchased` (1), or `Pending` (2). |

## Namespace: PlayPcSdkManaged.Integrity

Provides access to the Play Integrity API for anti-abuse and fraud detection.

### Classes

Clients and results

| Type | Name | Description |
|---|---|---|
| `Class` | `IntegrityClient` | The main client for interacting with the Integrity API. Manages the native C++ connection and must be disposed. |
| `Class` | `PrepareIntegrityTokenResult` | The result returned by `PrepareIntegrityTokenAsync`. |
| `Class` | `RequestIntegrityTokenResult` | The result returned by `RequestIntegrityTokenAsync`. Contains the signed token bytes on success. |

### Structs (Parameters \& Models)

| Type | Name | Description |
|---|---|---|
| `Struct` | `PrepareIntegrityTokenParams` | Input parameters for the prepare step, requiring the `CloudProjectNumber`. |
| `Struct` | `RequestIntegrityTokenParams` | Input parameters for the request step, requiring `RequestTokenData` and a `RequestHash`. |
| `Struct` | `RequestTokenData` | Intermediate data returned by the prepare step (containing `WarmUpSessionId`) required for the subsequent request. |

### Enums

| Type | Name | Description |
|---|---|---|
| `Enum` | `IntegrityError` | Status codes representing the outcome of an integrity operation (e.g., `Ok`, `CloudProjectNumberIsInvalid`, `NetworkError`). |

## Namespace: PlayPcSdkManaged.Unity

Unity-specific helpers and adapters for the SDK.

### Classes

| Type | Name | Description |
|---|---|---|
| `Class` | `PlayPcSdkFactory` | The factory class used to create instances of `BillingClient` and `IntegrityClient`, and to retrieve the `InitializationHandler`. This class handles the Unity-specific callback generation. |

## Namespace: PlayPcSdkManaged.Core

Core infrastructure shared across SDK modules.

### Classes

| Type | Name | Description |
|---|---|---|
| `Class` | `Result<TError, TValue>` | The base class for all API results. Provides properties `IsOk`, `Code`, `ErrorMessage`, and `Value`. |