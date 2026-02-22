---
title: https://developer.android.com/google/play/billing/backend
url: https://developer.android.com/google/play/billing/backend
source: md.txt
---

Your secure server backend plays a key role in your app's management of in-app purchases through Google Play. Google Play's billing system provides a way to manage the most important aspects of your digital product business, from setting up the catalog to tracking your transactions.
![](https://developer.android.com/static/images/google/play/billing/backend-arch.svg)**Figure 1.**Diagram of a typical backend integration with Google Play's billing system.

The[Google Play Developer API](https://developers.google.com/android-publisher)includes several endpoints to keep your backend in sync with the Google Play backend. In particular, the[Subscriptions and in-app purchases API](https://developers.google.com/android-publisher#subscriptions)handles functionality related to your digital product sales on Google Play.
![](https://developer.android.com/static/images/google/play/billing/subs-api.png)**Figure 2.**Billing-related endpoints provided by the Google Play Developer API.

## Automated digital product catalog management

There are many use cases where it's potentially useful to have a digital product catalog management integration in your backend. For example, this integration could enable you to do the following:

- Keep a mirror of your products' details on your backend for access when granting entitlements.
- Set up a batch process to update all of your prices automatically.
- Connect your own catalog management system with the catalog in Google Play's billing system to make sure it's updated synchronously.

You can use the[`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)and[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)endpoints to manage your digital product catalog.

## Purchase lifecycle management and entitlement sync

Monitoring purchase lifecycle events is essential for quick, accurate response to changes in your users' entitlements. You should build purchase status management into your backend for both subscriptions and one-time purchases so that all of your purchases are secure and all of your entitlements are consistent.

Google Play's billing system sends[Real-time developer notifications](https://developer.android.com/google/play/billing/rtdn-reference)(RTDN) for both types of purchase, and your backend should be ready to import these messages and make the necessary changes. To learn how to leverage an RTDN client and the Google Play Developer API to manage your purchase lifecycle, see the[purchase lifecycle guide](https://developer.android.com/google/play/billing/lifecycle).

## Fraud and abuse prevention

Prevent abuse by moving sensitive logic to your backend and monitoring voided purchases on Google Play. The Google Play Developer API offers functions to acknowledge new purchases, consume in-app product purchases, and handle voided purchases. To learn more about preventing fraud and abuse, see[Fight fraud and abuse](https://developer.android.com/google/play/billing/security).

## Automated financial conciliation and reporting

You can import your reporting data from Google Play by downloading your[Play Console reports](https://support.google.com/googleplay/android-developer/answer/6135870). You can leverage[Google Cloud Storage APIs](https://cloud.google.com/storage/)to download the information available to you on the Play Console to address any use cases related to this information.

## External transaction management

If you are integrating with the[alternative billing](https://developer.android.com/google/play/billing/alternative)or[external offers](https://developer.android.com/google/play/billing/external)APIs, use the[`Externaltransactions APIs`](https://developer.android.com/google/play/billing/outside-gpb-backend)to report and manage completed transactions.