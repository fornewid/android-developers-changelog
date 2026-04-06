---
title: Generate a BillingClient  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/prompt-gallery/prompts/generate-billing-client
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Generate a BillingClient Stay organized with collections Save and categorize content based on your preferences.




Create a complete, robust [`BillingClient`](/reference/com/android/billingclient/api/BillingClient) singleton with
listeners and a connection retry policy.

---

```
You are an expert Android developer with extensive knowledge of the Play Billing Library and associated documentation.

Analyze the language (Kotlin or Java) from the current file provided below and generate all code in that same language.

Your task is to generate a complete, production-ready class for managing the `BillingClient`. The class must perform the following actions:
1.  Create a singleton instance.
2.  Initialize the `BillingClient`.
3.  Attach a `PurchasesUpdatedListener`.
4.  Call `enablePendingPurchases()`.
5.  Attach a `BillingClientStateListener`.
6.  Handle `onBillingSetupFinished` and `onBillingServiceDisconnected`.
7.  `onBillingServiceDisconnected` must contain a retry policy.

Current file:
$CURRENT_FILE
```


To run this prompt in Android Studio, click **Gemini** in the sidebar and paste it in the chat field.
  
To save and retrieve prompts in the Studio IDE, go to **Settings > Gemini > Prompt Library**.


---