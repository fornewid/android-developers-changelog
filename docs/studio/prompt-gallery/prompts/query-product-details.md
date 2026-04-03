---
title: Query for ProductDetails  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/prompt-gallery/prompts/query-product-details
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Query for ProductDetails Stay organized with collections Save and categorize content based on your preferences.



Create the code to query for [`ProductDetails`](/reference/com/android/billingclient/api/ProductDetails), complete
with instructional placeholders for product IDs.

---

```
You are an expert Android developer with extensive knowledge of the Play Billing Library and associated documentation.

Analyze the language (Kotlin or Java) from the current file provided below and generate all code in that same language. Use modern, idiomatic patterns for that language's asynchronous operations (e.g., Coroutines for Kotlin, Listeners/Callbacks for Java).

Your response must be structured in two main sections:
1. Explanation with snippets:
- Provide a detailed, step-by-step explanation of how to query for product details.
- Intersperse small, focused code snippets within the explanation to illustrate each individual step (e.g., creating the list of `QueryProductDetailsParams.Product` objects, building the final `QueryProductDetailsParams`, and handling the asynchronous response).

2. Full working example:
- After the explanation, provide a complete and working example.
- This should provide a realistic demonstration of the new query function being called within `onBillingSetupFinished` and how a developer would use the response.

The code you generate for both the snippets and the full example must accomplish the following:
1. Query for product details given a `BillingClient` instance.
2. Define a list of `QueryProductDetailsParams.Product` objects using placeholder product IDs.
3. Include a prominent code comment instructing the developer to replace the placeholder IDs.
4. Create a `QueryProductDetailsParams` object for the query.
5. Call `billingClient.queryProductDetailsAsync()` to execute the query.
6. Correctly handle the asynchronous result and include appropriate error logging.

Note: Caching `ProductDetails` objects isn't recommended because stale objects can cause `launchBillingFlow()` failures.

Current file:
$CURRENT_FILE
```


To run this prompt in Android Studio, click **Gemini** in the sidebar and paste it in the chat field.
  
To save and retrieve prompts in the Studio IDE, go to **Settings > Gemini > Prompt Library**.


---