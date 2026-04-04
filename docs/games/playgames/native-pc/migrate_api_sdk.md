---
title: https://developer.android.com/games/playgames/native-pc/migrate_api_sdk
url: https://developer.android.com/games/playgames/native-pc/migrate_api_sdk
source: md.txt
---

If your Google Play Games on PC Native games directly call the [Play Billing
APIs](https://developers.google.com/android-publisher#subscriptions), you must migrate your game to use the PC SDK.

Depending on the game engine you are using, you can integrate the [`C++ SDK`](https://developer.android.com/games/playgames/native-pc/setup#c++)
or the [`C# SDK`](https://developer.android.com/games/playgames/native-pc/setup#c).
Refer to the [sample](https://github.com/playgameservices/native-pc-sdk-sample/)
projects that demonstrate examples that can be used to migrate
your Native game to SDK.

## Setup and preparation

This section describes the migration steps from an API-based solution to the
Google Play Games on PC Native SDK.

### Command-line arguments

Google Play Games on PC Native SDK relies on some command-line arguments passed
in during your game process startup to authenticate users. These arguments need
to be passed in to the process that calls [Initialize
SDK](https://developer.android.com/games/playgames/native-pc/setup#step-4). If your game startup involves
multiple processes, you have to verify that all the arguments are passed to the
process that ultimately uses the SDK. Checkout the [Supporting multi
game-processes](https://developer.android.com/games/playgames/native-pc/setup#step-5) step of the setup.

## API mapping

To complete the migration, you will need to remove all the direct API calls to
the Play servers. There are corresponding function calls in the SDK to achieve
the same functionality. This section lists out the mapping for each
functionality.

### Google Sign-In

Google Sign-In, also known as [Sign in with
Google](https://developer.android.com/identity/sign-in/credential-manager-siwg), is an OAuth authentication
method that provides a one-click authentication option for users with their
Google Account. In API-based projects, you associate a player's account with
their purchases. SDK-based solutions don't require this association.

SDK-based solutions use the [Google Play Games](https://play.google.com/googleplaygames) client's Google Account that
is already associated with the player's Gamer Profile and entitlements. This
provides a more seamless experience for players and a more secure environment
for developers because the SDK can communicate securely with the Google Play
Games client through IPC.

Instead of Google Sign-In, call [Initialize
SDK](https://developer.android.com/games/playgames/native-pc/setup#step-4) as early as possible. Act on the error code accordingly to provide a
secure environment for your game's runtime.

> [!NOTE]
> **Note:** You can use [Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg) for your in-game authentication.

### Get product list

In the API solution, your backend server retrieves the product list using the
Play Developer API [`inappproduct.gets`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/get) endpoint.

In the SDK, retrieve the in-app product list directly on the client using the
[`QueryProductDetails`](https://developer.android.com/games/playgames/native-pc/billing#step-2) function.

### Get purchases

In the API solution, your backend server retrieves user purchases using the Play
Developer API [`purchases.products.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get) endpoint.

In the SDK, use the [`QueryPurchases`](https://developer.android.com/games/playgames/native-pc/billing#step-1) function directly from your game
client.

### Launch purchase flow

In the API solution, launching the purchase flow requires calling multiple
endpoints for setup and acquiring the necessary tokens.

In the SDK, launch the process by calling the `BillingClient`'s
[`LaunchPurchaseFlow`](https://developer.android.com/games/playgames/native-pc/billing#step-3) function. The SDK handles all necessary work.

### Process the purchase

[Processing the user's purchase](https://developer.android.com/games/playgames/native-pc/billing#step-4)
involves acknowledging and consuming the purchase after successfully validating
that it is legitimate. Both API-solution and SDK-solution recommends the steps
to be completed from your backend for security purposes.

The process is similar for both API-solution and SDK-solution:

After retrieving the [purchaseToken](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get) from the purchase, such as
[ProductPurchase.purchaseToken](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products) in the API solution or
[ProductPurchaseDetails](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/query-purchases-result-value#product_purchase_details)'s [purchase_token](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details#purchase_token) in the SDK solution,
send it to your backend for [verification](https://developer.android.com/google/play/billing/security#verify).

Once it is verified, your backend can securely [acknowledge](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge) or [consume](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume)
the purchase after granting the entitlement.

> [!WARNING]
> **Warning:** SDK-solution exposes [AcknowledgePurchase](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#classgoogle_1_1play_1_1billing_1_1_billing_client_1ae2885b0119c6c9bf7e4eb51147ba6e74) and [ConsumePurchase](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#classgoogle_1_1play_1_1billing_1_1_billing_client_1a952bb4e38e8000318b54fb02beb971b6) functions to be called from the client-side but this is not recommended and requires allow-listing.

## Submit for testing

To submit your game for testing, follow these steps.

### Package for submission

Games using the SDK must be packaged in Windows App Bundle format and uploaded
through **Play Console**. Refer to the documentation to package your game in
Windows App Bundle for:

- Self managed publishing: [Installer publishing](https://developer.android.com/games/playgames/native-pc/publish/developer-installed#convert-wab)
- Play managed publishing: [Play managed publishing](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation#package-wab)