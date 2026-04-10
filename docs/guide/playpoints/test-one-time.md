---
title: https://developer.android.com/guide/playpoints/test-one-time
url: https://developer.android.com/guide/playpoints/test-one-time
source: md.txt
---

# Self-test using promo codes from Play Console

You can test your one-time products for Play Points using[Test promo codes](https://developer.android.com/google/play/billing/test#promo). To do so, do the following:

- Create test campaigns and test promo codes in the Play Console. In your test campaign, specify the product IDs of your one-time products.

- On a test device, use the**Redeem**menu in the Play Store app. By doing this you can verify that you can receive one-time products for Points promotions in your app. The following screenshot displays an example:

  ![Redeem menu in the Play Store app.](https://developer.android.com/static/images/guide/playpoints/test2.png)**Figure 1.**: Redeem menu in the Play Store app.

Verify the following scenarios using promo codes:

- App is not installed: The user redeems Play Points, the Play Store asks you to install your app, then your app should detect and deliver the items.

- App is installed, but not running: The user redeems Play Points, the Play Store asks you to open your app, then your app should detect and serve the items.

- App is installed and running: The user redeems Play Points, then your app should receive and detect the items.

| **Note:** Testing with promo code purchases won't create or return an orderID; however, Play points promotions will once published.

With the previously described test steps, you can verify your API integration is working properly and you are ready to configure and submit Play Points promotions (if the feature is enabled for your game).