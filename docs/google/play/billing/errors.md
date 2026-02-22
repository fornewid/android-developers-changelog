---
title: https://developer.android.com/google/play/billing/errors
url: https://developer.android.com/google/play/billing/errors
source: md.txt
---

When a Play Billing Library call triggers an action, the library returns a[`BillingResult`](https://developer.android.com/reference/com/android/billingclient/api/BillingResult)response to inform developers of the outcome. For example, if you use[`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener))to get the available offers for the user, the response code either contains an OK code and provides the right[`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails)object, or it contains a different response that indicates the reason why the[`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails)object couldn't be provided.

Not all response codes are errors. The[`BillingResponseCode`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode)reference page provides a detailed description of each of the responses discussed in this guide. Some examples of response codes that don't indicate errors are:

- [`BillingClient.BillingResponseCode.OK`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK): the action triggered by the call was completed successfully.
- [`BillingClient.BillingResponseCode.USER_CANCELED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED): for actions that display Play Store UI flows to the user, this response indicates the user navigated away from those UI flows without completing the process.

When the response code does indicate an error, the cause is sometimes due to transient conditions, and thus recovery is possible. When a call to a Play Billing Library method returns a[`BillingResponseCode`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode)value that indicates a recoverable condition, you should retry the call. In other cases, conditions are not considered transient and therefore a retry is not recommended.

Transient errors call for different retry strategies depending on factors like whether the error happens when users are in session---for example, when a user is going through a purchase flow---or the error happens in the background---for example, when you're querying the user's existing purchases during[`onResume`](https://developer.android.com/reference/android/app/Activity#onResume()). The[retry strategies section](https://developer.android.com/google/play/billing/errors#retry_strategies)below provides examples of these different strategies and the Retriable[`BillingResult`](https://developer.android.com/reference/com/android/billingclient/api/BillingResult)Responses[section](https://developer.android.com/google/play/billing/errors#retriable_billingresult_responses)recommends which strategy works best for each response code.

In addition to the response code, some error responses include messages for debugging and logging purposes.
| **Tip:** Before you deploy your app to the production environment, you can test how your app handles the various BillingResult response error codes by using the Response Simulator. For more information, see[Test BillingResult response codes](https://developer.android.com/google/play/billing/test-response-codes).

## Retry strategies

### Simple retry

In situations where the user is in session, it's better to implement a simple retry strategy so that the error disrupts the user experience as little as possible. In that case, we recommend a simple retry strategy with a maximum number of attempts as an exit condition.

The following example demonstrates a simple retry strategy to handle an error when establishing a[`BillingClient`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient)connection:  

    class BillingClientWrapper(context: Context) : PurchasesUpdatedListener {
      // Initialize the BillingClient.
      private val billingClient = BillingClient.newBuilder(context)
        .setListener(this)
        .enablePendingPurchases()
        .build()

      // Establish a connection to Google Play.
      fun startBillingConnection() {
        billingClient.startConnection(object : BillingClientStateListener {
          override fun onBillingSetupFinished(billingResult: BillingResult) {
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
              Log.d(TAG, "Billing response OK")
              // The BillingClient is ready. You can now query Products Purchases.
            } else {
              Log.e(TAG, billingResult.debugMessage)
              retryBillingServiceConnection()
            }
          }

          override fun onBillingServiceDisconnected() {
            Log.e(TAG, "GBPL Service disconnected")
            retryBillingServiceConnection()
          }
        })
      }

      // Billing connection retry logic. This is a simple max retry pattern
      private fun retryBillingServiceConnection() {
        val maxTries = 3
        var tries = 1
        var isConnectionEstablished = false
        do {
          try {
            billingClient.startConnection(object : BillingClientStateListener {
              override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                  isConnectionEstablished = true
                  Log.d(TAG, "Billing connection retry succeeded.")
                } else {
                  Log.e(
                    TAG,
                    "Billing connection retry failed: ${billingResult.debugMessage}"
                  )
                }
              }
            })
          } catch (e: Exception) {
            e.message?.let { Log.e(TAG, it) }
          } finally {
            tries++
          }
        } while (tries <= maxTries && !isConnectionEstablished)
      }
      ...
    }

### Exponential backoff retry

We recommend using exponential backoff for Play Billing Library operations that happen in the background and don't affect the user experience while the user is in session.

For example, it would be appropriate to implement this when acknowledging new purchases because this operation can happen in the background, and acknowledgment doesn't need to happen in real time if an error occurs.  

    private fun acknowledge(purchaseToken: String): BillingResult {
      val params = AcknowledgePurchaseParams.newBuilder()
        .setPurchaseToken(purchaseToken)
        .build()
      var ackResult = BillingResult()
      billingClient.acknowledgePurchase(params) { billingResult ->
        ackResult = billingResult
      }
      return ackResult
    }

    suspend fun acknowledgePurchase(purchaseToken: String) {

      val retryDelayMs = 2000L
      val retryFactor = 2
      val maxTries = 3

      withContext(Dispatchers.IO) {
        acknowledge(purchaseToken)
      }

      AcknowledgePurchaseResponseListener { acknowledgePurchaseResult ->
        val playBillingResponseCode =
        PlayBillingResponseCode(acknowledgePurchaseResult.responseCode)
        when (playBillingResponseCode) {
          BillingClient.BillingResponseCode.OK -> {
            Log.i(TAG, "Acknowledgement was successful")
          }
          BillingClient.BillingResponseCode.ITEM_NOT_OWNED -> {
            // This is possibly related to a stale Play cache.
            // Querying purchases again.
            Log.d(TAG, "Acknowledgement failed with ITEM_NOT_OWNED")
            billingClient.queryPurchasesAsync(
              QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.SUBS)
                .build()
            )
            { billingResult, purchaseList ->
              when (billingResult.responseCode) {
                BillingClient.BillingResponseCode.OK -> {
                  purchaseList.forEach { purchase ->
                    acknowledge(purchase.purchaseToken)
                  }
                }
              }
            }
          }
          in setOf(
             BillingClient.BillingResponseCode.ERROR,
             BillingClient.BillingResponseCode.SERVICE_DISCONNECTED,
             BillingClient.BillingResponseCode.SERVICE_UNAVAILABLE,
           ) -> {
            Log.d(
              TAG,
              "Acknowledgement failed, but can be retried --
              Response Code: ${acknowledgePurchaseResult.responseCode} --
              Debug Message: ${acknowledgePurchaseResult.debugMessage}"
            )
            runBlocking {
              exponentialRetry(
                maxTries = maxTries,
                initialDelay = retryDelayMs,
                retryFactor = retryFactor
              ) { acknowledge(purchaseToken) }
            }
          }
          in setOf(
             BillingClient.BillingResponseCode.BILLING_UNAVAILABLE,
             BillingClient.BillingResponseCode.DEVELOPER_ERROR,
             BillingClient.BillingResponseCode.FEATURE_NOT_SUPPORTED,
           ) -> {
            Log.e(
              TAG,
              "Acknowledgement failed and cannot be retried --
              Response Code: ${acknowledgePurchaseResult.responseCode} --
              Debug Message: ${acknowledgePurchaseResult.debugMessage}"
            )
            throw Exception("Failed to acknowledge the purchase!")
          }
        }
      }
    }

    private suspend fun <T> exponentialRetry(
      maxTries: Int = Int.MAX_VALUE,
      initialDelay: Long = Long.MAX_VALUE,
      retryFactor: Int = Int.MAX_VALUE,
      block: suspend () -> T
    ): T? {
      var currentDelay = initialDelay
      var retryAttempt = 1
      do {
        runCatching {
          delay(currentDelay)
          block()
        }
          .onSuccess {
            Log.d(TAG, "Retry succeeded")
            return@onSuccess;
          }
          .onFailure { throwable ->
            Log.e(
              TAG,
              "Retry Failed -- Cause: ${throwable.cause} -- Message: ${throwable.message}"
            )
          }
        currentDelay *= retryFactor
        retryAttempt++
      } while (retryAttempt < maxTries)

      return block() // last attempt
    }

## Retriable BillingResult responses

### [NETWORK_ERROR](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR)(Error Code 12)

| **Note:** This error is only returned in Google Play Billing Library 6 and up. Previous versions are not supported.

#### Problem

This error indicates that there was a problem with the network connection between the device and Play systems.

#### Possible resolution

To recover, use simple retries or exponential backoff, depending on which action triggered the error.

### [SERVICE_TIMEOUT](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT)(Error Code -3)

| **Note:** This error is only returned in Google Play Billing Library 5.2.0 and earlier. Starting with Google Play Billing 6.0.0,[SERVICE_UNAVAILABLE](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE)is returned for the problem described below, and`SERVICE_TIMEOUT`is deprecated.

#### Problem

This error indicates that the request has reached the maximum timeout before Google Play is able to respond. This could be caused, for example, by a delay in the execution of the action requested by the Play Billing Library call.

#### Possible resolution

This is usually a transient issue. Retry the request using either either a simple or exponential backoff strategy, depending on which action returned the error.

Unlike[`SERVICE_DISCONNECTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED)below, the connection to the Google Play Billing service is not severed, and you only need to retry whatever Play Billing Library operation was attempted.

### [SERVICE_DISCONNECTED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED)(Error Code -1)

#### Problem

This fatal error indicates that the client app's connection to the Google Play Store service via the[`BillingClient`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient)has been severed.

#### Possible resolution

##### Strongly Recommended: Enable Automatic Service Reconnection

The Play Billing Library version 8.0.0 introduced the`enableAutoServiceReconnection()`feature.**It is highly recommended that you enable this feature** when building your`BillingClient`. This allows the library to automatically attempt to re-establish the connection when a billing API call is made while the service is disconnected, significantly reducing the occurrences of this error.  

### Kotlin

    val billingClient = BillingClient.newBuilder(context)
        .setListener(listener)
        .enablePendingPurchases()
        .enableAutoServiceReconnection() // Enable automatic service reconnection
        .build()

### Java

    BillingClient billingClient = BillingClient.newBuilder(context)
        .setListener(listener)
        .enablePendingPurchases()
        .enableAutoServiceReconnection() // Enable automatic service reconnection
        .build();

##### If you have enabled automatic service reconnection

The Play Billing Library will automatically attempt to reconnect. If you still receive a`SERVICE_DISCONNECTED`response code when making an API call, it indicates that the library was unable to reconnect after its automatic attempts. In this scenario, you should implement retry logic in your app:

- **For user-initiated actions (in-session):**Use simple retries of the API call. The underlying issue might be temporary.
- **For background requests:**Implement retries with exponential backoff to avoid overwhelming the system if the disconnection is prolonged.

##### If you have NOT enabled automatic service reconnection

To avoid this error as much as possible, always check the connection to Google Play services before making calls with the Play Billing Library by calling[`BillingClient.isReady()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isReady()).

To attempt recovery from[`SERVICE_DISCONNECTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED), your client app should try to re-establish the connection using[`BillingClient.startConnection`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#startConnection(com.android.billingclient.api.BillingClientStateListener)).

Just like with[`SERVICE_TIMEOUT`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT), use simple retries or exponential backoff, depending on which action triggered the error.

### [SERVICE_UNAVAILABLE](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE)(Error Code 2)

#### Important Note:

Starting in Google Play Billing Library 6.0.0,`SERVICE_UNAVAILABLE`is no longer returned for network issues. It is returned when the billing service is unavailable and the deprecated`SERVICE_TIMEOUT`case scenarios.

#### Problem

This transient error indicates the Google Play Billing service is currently unavailable. In most cases, this means there is a network connection issue anywhere between the client device and Google Play Billing services.

#### Possible resolution

This is usually a transient issue. Retry the request using either either a simple or exponential backoff strategy, depending on which action returned the error.

Unlike[`SERVICE_DISCONNECTED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED), the connection to the Google Play Billing service is not severed, and you need to retry whatever operation is being attempted.

### [BILLING_UNAVAILABLE](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE)(Error Code 3)

#### Problem

This error indicates that a user billing error occurred during the purchase process. Examples of when this can occur include:

- The Play Store app on the user's device is out of date.
- The user is in an unsupported country.
- The user is an enterprise user, and their enterprise admin has disabled users from making purchases.
- Google Play is unable to charge the user's payment method. For example, the user's credit card might have expired.

#### Possible resolution

Automatic retries are unlikely to help in this case. However, a manual retry can help if the user addresses the condition that caused the issue. For example, if the user updates their Play Store version to a supported version, then a manual retry of the initial operation could work.

If this error occurs when the user is not in session, retrying might not make sense. When you receive a[`BILLING_UNAVAILABLE`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE)error as a result of the purchase flow, it's very likely the user received feedback from Google Play during the purchase process and might be aware of what went wrong. In this case, you could show an error message specifying something went wrong and offer a "Try again" button to give the user the option of a manual retry after they address the issue.

### [ERROR](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR)(Error Code 6)

#### Problem

This is a fatal error that indicates an internal problem with Google Play itself.

#### Possible resolution

Sometimes internal Google Play problems that lead to[`ERROR`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR)are transient, and a retry with an exponential backoff can be implemented for mitigation. When users are in session, a simple retry is preferable.

### [ITEM_ALREADY_OWNED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_ALREADY_OWNED)

#### Problem

This response indicates that the Google Play user already owns the subscription or one-time purchase product they are attempting to purchase. In most cases, this is not a transient error, except when it is caused by a stale Google Play's cache.

#### Possible resolution

To avoid this error happening when the cause is not a cache issue, don't offer a product for purchase when the user already owns it. Make sure you check the user's entitlements when you show the products available for purchase, and filter what the user can purchase accordingly. When the client app receives this error due to a cache issue, the error triggers Google Play's cache to get updated with the latest data from Play's backend. Retrying after the error should resolve this specific transient instance in this case. Call[`BillingClient.queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener))after getting an[`ITEM_ALREADY_OWNED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_ALREADY_OWNED)to check if the user has acquired the product, and if it's not the case implement a simple retry logic to reattempt the purchase.

### [ITEM_NOT_OWNED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_NOT_OWNED)

#### Problem

This purchase response indicates that the Google Play user does not own the subscription or one-time purchase product the user is attempting to replace, acknowledge or consume. This is not a transient error in most cases except when it is caused by Google Play's cache getting into a stale state.

#### Possible resolution

When the error is received because of a cache issue, the error triggers Google Play's cache to get updated with the latest data from Play's backend. Retrying with a simple retry strategy after the error should resolve this specific transient instance. Call[`BillingClient.queryPurchasesAsync()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_ALREADY_OWNED)after getting an[`ITEM_NOT_OWNED`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_NOT_OWNED)to check if the user has acquired the product. If they have not, use simple retry logic to reattempt the purchase.

## Non-Retriable BillingResult responses

You can't recover from these errors using retry logic.

### [FEATURE_NOT_SUPPORTED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED)

#### Problem

This non-retriable error indicates that the Google Play Billing feature is not supported on the user's device, likely due to an old Play Store version.

For example, perhaps some of your users' devices don't support in-app messaging.

#### Possible mitigation

Use[`BillingClient.isFeatureSupported()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isFeatureSupported(java.lang.String))to check feature support before making the call to the Play Billing Library.  

    when {
      billingClient.isReady -> {
        if (billingClient.isFeatureSupported(BillingClient.FeatureType.IN_APP_MESSAGING)) {
           // use feature
        }
      }
    }

### [USER_CANCELED](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED)

#### Problem

The user has clicked out of the billing flow UI.

#### Possible resolution

This is informational only and can fail gracefully.

### [ITEM_UNAVAILABLE](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_UNAVAILABLE)

#### Problem

The Google Play Billing subscription or one-time purchase product is not available for purchase for this user.

#### Possible mitigation

Make sure your app refreshes the product details via[`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener))as recommended. Take into account how often your product catalog changes on the Play Console configuration to implement extra refreshes if needed. Only attempt to sell products on Google Play Billing that return the right information via[`queryProductDetailsAsync`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)). Check the product eligibility configuration for any inconsistencies. For example, you might be querying for a product that is only available for a region other than the one the user is trying to purchase. To be available for purchase, a product needs to be active, its app needs to be published, and its app needs to be available in the user's country.

Sometimes, in particular during testing, everything is correct in the product configuration, but users still see this error. This might be due to a propagation delay of the product details across Google's servers. Try again later.

### [DEVELOPER_ERROR](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#DEVELOPER_ERROR)

#### Problem

This is a fatal error that indicates you're improperly using an API. For example, supplying incorrect parameters to[`BillingClient.launchBillingFlow`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams))can cause this error.

#### Possible resolution

Make sure that you are correctly using the different Play Billing Library calls. Also, check the debug message for more info about the error.