---
title: https://developer.android.com/google/play/developer-api
url: https://developer.android.com/google/play/developer-api
source: md.txt
---

# Google Play Developer APIs

## Overview

The Google Play Console provides a suite of REST-based web service APIs that let you perform publishing, reporting, and other app-management functions directly for your app.

Not all developers need to use these developer APIs --- in most cases you can continue to manage your apps directly using the Google Play Console. However, if you have a large number of APKs to manage, or have to track user purchases and subscriptions, you might find these APIs to be useful.

### What's included

The Google Play Developer APIs let you focus on designing and developing your app, while spending less time and effort managing your releases, even as you grow to new markets.

The Google Play Console includes a suite of APIs that you can use to manage your app:

- The[Publishing API](https://developer.android.com/google/play/developer-api#publishing)lets you upload and publish apps, and perform other publishing-related tasks.
- The[Subscriptions and In-App Purchases API](https://developer.android.com/google/play/developer-api#subscriptions)lets you manage in-app purchases and subscriptions. (This was previously known as the "Purchase Status API".)
- The[Reporting API](https://developer.android.com/google/play/developer-api#reporting)lets you retrieve information about your app's quality from Android vitals.
- The[Reply to Reviews API](https://developer.android.com/google/play/developer-api#reviews)lets you retrieve and reply to reviews of your app.
- The[Permissions API](https://developer.android.com/google/play/developer-api#permissions)lets you automate permission management within the Play Console.
- The[Play Games Services Management API](https://developer.android.com/games/pgs/management/management)lets you issue REST calls to programmatically control the metadata underlying the Google Play Games Services features.
- The[Voided Purchases API](https://developer.android.com/google/play/developer-api#voided-purchases)provides a list of orders that are associated with purchases that a user has voided.

### Getting started

To get started with the Google Play Developer APIs, see the[getting started](https://developers.google.com/android-publisher/getting_started)documentation.

## Publishing API

The[Publishing API](https://developers.google.com/android-publisher#publishing)lets you to automate frequent tasks having to do with app distribution. This provides functions similar to those available to a developer through the Play Console, such as:

- Uploading new versions of an app
- Releasing apps, by assigning APKs to various[tracks](https://developers.google.com/android-publisher/tracks)(alpha, beta, staged rollout, or production)
- Creating and modifying Google Play Store listings, including localized text and graphics and multidevice screenshots

Those tasks are performed using the[edits](https://developers.google.com/android-publisher/edits)functionality, which takes a transactional approach to making changes. This lets you bundle several changes into a single draft edit, then commit the changes all at once. (None of the changes take effect until the edit is committed.)
| **Note:** Not all developers need to use this API. All the functionality provided by the API is also available through the Google Play Console. However, this API lets you integrate your app and listing update process with your existing tools, which is useful for some developers. In particular, if you have a large number of APKs to manage, or localized listings in many different locales, you may find this API invaluable.

### Best practices

- Limit the number of app updates. Don't publish alpha or beta updates more frequently than once a day (production apps should be updated even less frequently than that). Every update costs your users time and possibly money. If you update too frequently, users might start ignoring updates, or even uninstall the product.

## Subscriptions and In-App Purchases API

The[Subscriptions and In-App Purchases API](https://developers.google.com/android-publisher#subscriptions)allows you to manage your app's catalog of in-app products and subscriptions. In addition, with the Subscriptions and In-App Purchases API, you can quickly retrieve the details of any purchase using a standard`GET`request.

In the request, you supply information about the purchase --- app package name, purchase or subscription ID, and the purchase token. The server responds with a JSON object describing the associated purchase details, order status, developer payload, and other information.

You can use this API in several ways, such as for reporting and reconciliation of individual orders and for verifying purchases and subscription expirations. You can also use the API to learn about canceled orders and confirm whether in-app products have been consumed, including whether they were consumed before being canceled.
| **Note:** The Subscriptions and In-App Purchases API does not use the transactional "edits" functionality used by the[Publishing API](https://developer.android.com/google/play/developer-api/publisher-api). Methods for the[Inappproducts](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)and[Purchases.subscriptions](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions)resources take effect immediately. Each resource's API reference page notes specifically whether the methods for that resource use the "edits" model.

### Best practices

- Store subscription information on your server to avoid making unnecessary API calls. When your app needs to verify a subscription, you should rely on the cached information on your server instead of repeating the API call to Google.
- There are two scenarios in which your secure server should use the Google Play Developer API to get subscription information:
  - Your server receives a new purchase token that has not been seen before.
  - Your server receives a real-time developer notification (RTDN), which indicates that you need to use the purchase token to get the new subscription information.
- Don't poll the API for subscription status on a regular basis. For example, don't call the API daily to check each subscription.
- Since you receive an RTDN when the subscription expires or renews, you don't need to schedule an API call based on the scheduled expiry time.

## Reporting API

The[Reporting API](https://developers.google.com/play/developer/reporting)is for developers who want to build automated workflows on top of Play Console data, or developers who use Play Console data for internal business reporting and analysis, potentially alongside other datasets. This gives you programmatic access to app-level data and metrics for internal reporting, analysis, and automation.

The reporting API offers access to Android vitals data, including crash rate, ANR rate, wake-up and wake-lock issues, and error stack traces.

### Best practices

- This version of the Reporting API has a default limit of 10 queries per second. You can view your quota usage in the[Quotas section](https://pantheon.corp.google.com/apis/api/playdeveloperreporting.googleapis.com/quotas)of the Google Cloud Console. If you need to exceed this limit, you can submit a quota request using[this form](https://support.google.com/googleplay/android-developer/contact/apiqr).

## Reply to Reviews API

The[Reply to Reviews API](https://developers.google.com/android-publisher/reply-to-reviews)allows you to view user feedback for your app and reply to this feedback. You can use this API to interact with users directly within your existing customer support toolkit, such as a CRM system.

The Reply to Reviews API allows you to access feedback only for production versions of your app. If you want to see feedback on alpha or beta versions of your app, use the Google Play Console instead. Also, note that the API shows only the reviews that include comments. If a user rates your app but does not provide a comment, their feedback is not accessible from the API.

## Permissions API

The Permissions API gives developers the ability to[automate permission management](https://developers.google.com/android-publisher/api-ref/rest/v3/users/list)within the Play Console. This can allow you flexible control over who has access to your developer account, without manual involvement.

With the Permissions API, you can perform administrative functions such as:

- Removing users' access when they leave your company.
- Granting access to an app when a user joins the relevant team.

## Voided purchases API

The[Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases)provides a list of orders that are associated with purchases that a user has voided. You can use information from this list to implement a revocation system that prevents the user from accessing products from those orders.

This API applies to one-time in-app orders and app subscriptions.

A purchase can be voided in the following ways:

- The user requests a refund for their order.
- The user cancels their order.
- An order is charged back.
- Developer cancels or refunds order. Note: only revoked orders will be shown in the Voided Purchases API. If developer refunds without setting the revoke option, orders will not show up in the API.
- Google cancels or refunds order.

By using this API, you help create a more balanced and fair experience for all of your app's users, particularly if your app is a game.