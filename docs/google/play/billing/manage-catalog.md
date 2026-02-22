---
title: https://developer.android.com/google/play/billing/manage-catalog
url: https://developer.android.com/google/play/billing/manage-catalog
source: md.txt
---

This guide explains how to use the Google Play Developer API to create and
manage a product catalog for your Play app.

To sell products in your app through Google Play's billing system you need to
set up a catalog with all the products you want to make available for purchase
by your users. This can be done through the Play Console, or you can automate
catalog management using the Google Play Developer API. Automation can help
ensure your catalog is always up-to-date, and scale to large catalogs where
manual coordination is impractical. In this guide you will see how to use the
[Play Developer API](https://developers.google.com/android-publisher#subscriptions) to create and manage a product catalog
for your Play app. Review our [Getting ready](https://developer.android.com/google/play/billing/getting-ready#dev-api) guide for
instructions on how to set up the Google Play Developer API for your backend
integration.

## Catalog Management APIs

To read about the different types of product you can sell with Google Play's
billing system, read [Understand in-app product types and catalog
considerations](https://support.google.com/googleplay/android-developer/answer/14590082). Google offers two main sets of APIs for catalog
management on Play, corresponding to the two main product categories:

- One-time products
- Subscription products

### One-time products

The one-time products (previously referred to as in-app products) use the
[one-time product object model](https://support.google.com/googleplay/android-developer/answer/16430488)
which lets you configure multiple purchase options and offers for your one-time
products. The one-time product object model provides you greater flexibility in
how you sell products, and reduces the complexity of managing them. Your
existing in-app products will be migrated to the one-time product object model.
For more information see [Migration of in-app products](https://support.google.com/googleplay/android-developer/answer/16430488).

The [`monetization.onetimeproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts) and the
[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts) endpoints let you
manage one-time products from your backend. This includes creating, updating,
and deleting products, and managing prices and availability. Depending on how you handle
one-time product purchases, you will model consumable products (can be bought as
many times as desired) or permanent entitlements (cannot be made twice by the
same user). You can decide which one-time products should be consumable or not.
| **Note:** You can continue to use the [`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts) service to manage your existing in-app products. While Google Play maintains backward compatibility for in-app products created with the inappproducts service, it's recommended to migrate them to the [one-time product model](https://support.google.com/googleplay/android-developer/answer/16430488).

### Subscription products

The [`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions) endpoint helps you manage subscription
products from your developer backend. You can do things such as create, update,
and delete subscriptions, or control their regional availability and pricing. In
addition to the [`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions) endpoint, we also provide
[`monetization.subscriptions.basePlans`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans) and
[`monetization.subscriptions.basePlans.offers`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers) to respectively manage
subscriptions' base plans and offers.
| **Note:** The inappproducts API includes some legacy features to manage subscriptions, as in the past all Google Play products were managed through this endpoint. You should **no longer** use this endpoint to manage subscription products, and you should [migrate](https://developer.android.com/google/play/billing/migrate-gpblv5#manage-subscription-product-catalog) any subscription publishing integrations to use the new [`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions) API. For more information on this deprecation, visit [our blog post](https://android-developers.googleblog.com/2023/06/changes-to-google-play-developer-api-june-2023.).

### Batch methods

The [`onetimeproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts),
[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts), and the [`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
endpoints provide a number of batch methods that allow retrieving or managing up
to 100 entities under the same app at the same time.

Batch methods, when used with enabled latency tolerance, support higher
throughput and are particularly useful for large-catalog developers for initial
catalog creation or catalog reconciliation.

### Update propagation latency versus throughput

After a product creation or modification request is complete, changes may not be
immediately visible to end users on their devices due to network or backend
processing delays. By default, all product modification requests are
latency-sensitive. This means they are optimized for fast propagation through
backend systems, typically reflecting on end-user devices within minutes.
However, there is an hourly limit on the number of such modification requests.
For cases where you need to create or update many products (for example, during
initial large catalog creation), you can use batch methods with the
`latencyTolerance`field set to
[`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance). This will
significantly increase update throughput. Latency-tolerant updates will take up
to 24 hours to propagate to end-user devices.

### Quota configuration

There are several quota limits you should be aware of when using Play Developer
API to manage your product catalog:

1. The Google Play Developer APIs are organized into categories called buckets, where each bucket has its own per-minute quota limit. For more information, see [quotas](https://developers.google.com/android-publisher/quotas).
2. Product modification endpoints also enforce a limit of 7,200 queries per hour. This is a single limit across both one-time products and subscriptions and across all modification requests, including creation, update, activate, delete. Batch modification method calls count as one query for this quota, regardless of the number of individual requests included or their latency sensitivity.
3. Latency sensitive modifications also have a limit of 7,200 modifications per hour. For batch methods, every nested modification request counts separately for the purpose of this quota. This quota has practical implications only for the users of batch API performing latency sensitive updates, as in other cases quota 2 will be exhausted before or at the same time as this quota.

Here are several illustrative examples to understand the quota usage of
different requests:

- A single `get` request to fetch one item will consume 1 token of quota 1 and no tokens of quota 2 and 3 (as they concern only modification endpoints).
- A batch `get` request to fetch up to 100 items will also consume 1 token of quota 1 and no tokens of quota 2 and 3.
- A single `modification` request for one item will consume 1 token of quota 1 , 1 token of quota 2. If the request is latency sensitive, it will also consume 1 token of quota 3. Because quota C has the same limit as quota 2, it has no practical implications for users using only single modification methods.
- A batch `modification` request for 100 latency tolerant items will consume 1 token of quota 1, 1 token of quota 2. This quota setup should allow for ample margin to keep your catalog updated, but if your algorithm is not conscious of this quota and goes beyond this rate you may get an error per additional call.
- A batch `modification` request for 100 latency sensitive items will consume 1 token of quota 1, 1 token of quota 2, and 100 tokens of quota 3.

### Catalog Management API usage recommendations

By adhering to these guidelines, you optimize your interactions with the API,
ensuring a smooth and efficient catalog management experience.

#### Monitor your usage

You should be aware of heavy usage processes. For example, at the beginning of
your integration your catalog management endpoints are more likely to consume
more quota to create your full initial catalog and this could potentially affect
production usage of other endpoints like the purchase status API if you are
close to the overall usage limit. You need to monitor your quota consumption to
make sure that you are not exceeding the API quotas. There are several ways to
monitor usage. For example, you can use the Google Cloud APIs quota dashboard,
or any other in-house or third party API monitoring tool of your choice.

#### Optimize API quota usage

Optimizing rate consumption is highly recommended to minimize the likelihood of
API errors. To implement this effectively, we recommend that you:

- Choose the right catalog management strategy. Once you understand the API quota, you need to choose the right strategy for your application to achieve your catalog management goals efficiently.
- Only make the minimum amount of calls you need to reflect your changes.
- Don't send redundant or unnecessary modification calls to the APIs. This might require you to keep a changelog in your backend catalog.
- Stay under the product modification hourly limit of 7,200 queries. You may want to build sync processes that require you to make large numbers of product modifications in a short period of time (for example, an initial catalog creation). If you expect these processes to go over the hourly limit, implement waits as necessary to slow the usage to a safe level. Consider using batch methods with latency tolerant updates to achieve higher throughput.
- Proactively prepare to scale. As your application grows, you may need to scale up your usage of the API and the various endpoints. Read [the Google
  Play Developer API quotas documentation](https://developers.google.com/android-publisher/quotas) for details on how to increase your quota when you are getting close to the maximum usage.
- Strategically schedule heavy processes. Try to schedule your heavy catalog processes around critical usage peaks, for example you can avoid running a full catalog sync during your peak sales times of the week.

#### Add quota error handling logic

No matter how efficiently you build your catalog management logic, you should
make it resilient to unexpected quota limits, given that the daily quota is
shared by endpoints used in independent modules of your integration. Make sure
you include quota throttling errors in your error handling, and implement the
appropriate waits. Every call made to Google Play Developer APIs will generate a
response. In the event of a call failure, you will receive a failure response
that includes an HTTP response status code and an `errors` object, providing
further details about the error domain and a debug message. For example, if you
surpass your daily limit, you may encounter an error similar to the following:  

    {
      "code" : 403,
      "errors" : [ {
        "domain" : "usageLimits",
        "message" : "Daily Limit Exceeded. The quota will be reset at midnight Pacific Time (PT). You may monitor your quota usage and adjust limits in the API
      Console: https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/quotas?project=xxxxxxx",
      "reason" : "dailyLimitExceeded",
      "extendedHelp" : "https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/quotas?project=xxxxxx"
      } ],
    }

## Catalog management implementation

Developers use the Google Play Developer API product publishing endpoints to
keep their catalog synchronized between their backend and Google Play. Making
sure your Google Play catalog is always up to date with your backend's catalog
latest information has advantages to create a better user experience. For
example:

- You will be able to consult the entire list of available offers, and manage offer and base plan tags to influence your own eligibility and offer surfacing logic.
- You can check the different price points and product details users are seeing across platforms, and make sure they are consistent.
- You will have product details at hand in your backend when processing new purchases, without the need to increase latency and risk of failure by making additional calls to the Google Play Developer API during user critical flows.

There are [certain limits and considerations](https://support.google.com/googleplay/android-developer/answer/14590082) you should keep in
mind when creating your product catalog on Google Play. Once you understand
these limits and you know how you want to structure your catalog, it's time to
decide on your synchronization strategy.

### Catalog synchronization strategies

The Google Play Developer API publishing endpoints allow you to make updates to
your catalog as changes occur. On occasion, you might need to take a periodic
updates approach, where you send a battery of changes in the same process. Each
approach requires different design choices. Each synchronization strategy will
fit some use cases better than others, and you might have a set of needs that
calls for both, depending on the situation. Sometimes you may want to make an
update to a product the moment you are aware of a new change, for example to
process an urgent product update (i.e. a wrong price needs to be corrected as
soon as possible). Other times you can use a periodic background sync to ensure
your backend and Play catalogs are always consistent. Read some common use cases
where you might want to implement these different catalog management strategies.

**When to send updates as your local catalog changes**

Ideally, updates should happen as soon as there is any change to your backend's
product catalog, to minimize discrepancies.

This type of updates is a good option when:

- You must ensure that your products are always up-to-date.
- You need to make a few changes to your products each day.
- You need to update products that are already in production and being sold.

This approach is simpler to implement, and lets you keep your catalog in sync
with the least amount discrepancy window.

**When to use periodic updates**

Periodic updates are run asynchronously to the product edition on your backend,
and they are a good option when:

- You don't have to ensure your products are updated on a short notice.
- You need to plan bulk updates or conciliation processes.
- You already have a Content or Catalog Management System to handle your digital products, and that updates your catalog constantly

In case of large catalogs, consider using batch methods with latency tolerant
updates to achieve maximum throughput.
| **Note:** While you may send updates to your Google Play product catalog immediately upon any changes, this does not necessarily mean the changes will be immediately available to your users in-app. There may still be some latency in the process due to network or backend processing delays. Similarly, while periodic updates are performed with some delay, they can still be designed to update your catalog frequently if needed, making your changes available to users with similar latency to on demand updates. Additionally, the `latencyTolerance` field in batch methods lets you choose between optimizing for fast update propagation or higher throughput. Ultimately, the choice between these two options should be based on your specific requirements and limitations.

### Create your product catalog

If you have a large catalog to upload to Google Play, you may want to automate
the initial load. This type of heavy process works best if a periodic strategy
combined with latency tolerant batch methods is followed.

#### Create one-time products

For initial one-time product catalog creation, we recommend using the
[monetization.onetimeproducts.batchUpdate](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchUpdate)
or the [`inapp_products.insert`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/insert) method with the
`allowMissing` field set to `true` and the `latencyTolerance` field set to
[`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance). This will minimize the
time it takes to create the catalog within quota limits.

#### Create subscription products

For initial subscription large catalog creation, we recommend using the
[`monetization.subscriptions.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchUpdate) method
with the `allowMissing` field set to `true` and the `latencyTolerance`field set
to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance). This will minimize
the time it takes to create the catalog within quota limits.

For smaller subscription catalogs the Play Developer API provides the
[`monetization.subscriptions.create`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/create) method.
Alternatively you can create subscriptions using
[`monetization.subscriptions.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch) method with the
`allowMissing` parameter as described in the Product updates section.

All of the earlier methods create subscriptions along with their base plans
(supplied within the Subscription object). These base plans are initially
inactive. To manage base plans' status, you can use the
[`monetization.subscriptions.basePlans`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans) endpoint, including activating a
base plan to make it available for purchase. Additionally, the
[`monetization.subscriptions.basePlans.offers`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers) endpoint lets you create and
manage offers.

### Product updates

The following methods enable you to efficiently modify your existing products,
ensuring your offerings align with your latest adjustments.

#### Update one-time products

The following methods are available to you to help update existing one-time products.

- [monetization.onetimeproducts.batchUpdate](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchUpdate)
- [`inappproducts.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/patch) : The patch endpoint is used to update a resource partially. This means you can update specific fields that you specify in the request body. The patch endpoint is typically used when you only need to update a few fields of a resource.
- [`inappproducts.update`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/update) : The update endpoint is used to update a resource in its entirety. This means that you will need to send the entire resource object in the request body. The update endpoint is typically used when you need to update all fields in a resource. When the `allowMissing` parameter is set to `true` and the supplied product ID does not already exist, the endpoint will insert the product instead of failing.
- [`inappproducts.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchUpdate) : This is a batch version of the update endpoint, which lets you modify multiple products with a single query. Use it together with the `latencyTolerance` field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance) to achieve higher throughput.

#### Update subscription products

To update existing subscriptions, you can use the
[`monetization.subscriptions.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch) method. This method
takes the following required parameters:

- `packageName`: The package name of the app that the subscription belongs to.
  - `productId`: The subscription's unique product ID.
- `regionsVersion`: The [region configuration version](https://developers.google.com/android-publisher/api-ref/rest/v3/RegionsVersion).

Unless you are creating a new subscription by using the `allowMissing` parameter
, you must provide the `updateMask` parameter. This parameter is a
comma-separated list of fields that you want to update.

For example, if you only want to update a listing of a subscription product, you
would specify the `listings` field to the `updateMask` parameter.

You can use [`monetization.subscriptions.batchUpdate`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchUpdate) to update multiple subscriptions at the same time.
Use it together with the `latencyTolerance` field set to
[`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance) to achieve higher
throughput.

To activate, deactivate, delete base plans or to migrate subscribers to the
latest base plan price versions use the [`monetization.subscriptions.basePlans`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans) endpoint.

Additionally, you can update your base plans' offers with the
[`monetization.subscriptions.basePlans.offers.patch`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/patch)
method.

### Catalog reconciliation

Whether you choose to update your Google Play catalog every time your backend's
catalog changes or periodically, if you have a catalog management system or a
database outside of Google Play's catalog there could be situations where it
falls out of sync with the catalog on your apps configuration on Play. This
could be due to emergency manual catalog changes in the Console, an outage on
your catalog management system or maybe if you lost your latest data.

You can build a catalog reconciliation process to avoid a prolonged discrepancy
window.

#### Diff system consideration

We recommend building a diff system to detect inconsistencies and reconcile the
two systems. Here are some things to consider when building a diff system to
help keep your catalogs in sync:

- **Understand the data models:** The first step is to understand the data models of the developer CMS and the Google Play Developer API. This includes knowing the different types of data that are stored in each system, and how the different data elements map to each other.
- **Define the diff rules:** Once you understand the data models, you need to define the diff rules. These rules will determine how the data in the two systems are compared. For example, you may want to match product IDs and compare key attributes of the subscription and its associated base plans and offers.
- **Implement a diff algorithm:** Once you have defined the diff rules, you need to implement the diff algorithm. This algorithm will take the data from the two systems and compare it according to the rules you have defined. To get the catalog data from Google Play, you can use the [`monetization.onetimeproducts.list`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/list), [`monetization.onetimeproducts.batchGet`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchGet), [`inappproducts.list`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/list), [`inappproducts.batchGet`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchGet), [`monetization.subscriptions.list`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/list) and [`monetization.subscriptions.batchGet`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchGet) methods.
- **Generate diff reports:** The diff algorithm will generate a diff report. This report will show the differences between both systems.
- **Reconcile differences:** Once you have generated the diff report, you need to resolve the differences. This may involve updating the data in your CMS, or it may involve updating the data on Google Play's side using the Developer API catalog management endpoints, depending on how you normally update your catalog. To reconcile out of sync products, use the update endpoints as described in the Product updates section.

### Product deprecation

The Google Play Developer API provides the following methods to assist you in
deprecating your products:

For one-time products:

- [`monetization.onetimeproducts.delete`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/delete)
- [`monetization.onetimeproducts.batchDelete`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchDelete)
- [`inappproducts.delete`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/delete)
- [`inappproducts.batchDelete`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchDelete)

For subscription products:

- [`monetization.subscriptions.delete`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/delete) for subscriptions. A subscription cannot be removed once at least one base plan has been activated.

Deprecating a product might be necessary in various scenarios,
such as:

- Creation by mistake.
- Discontinuing a feature or service.

We recommend incorporating product deprecation into your catalog management
strategy.