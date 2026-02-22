---
title: https://developer.android.com/google/play/billing/getting-ready
url: https://developer.android.com/google/play/billing/getting-ready
source: md.txt
---

| **Note:** Before reading this topic, make sure you've read through the[Play Console Help Center documentation](https://support.google.com/googleplay/android-developer/topic/3450769), which describes critical purchase-related concepts, as well as how to create and configure your products for sale.

This topic lists and describes the setup steps you need to take before you can sell products in your app. At a high level, this setup includes creating a developer account, creating and configuring the products you want to sell, and enabling and configuring the APIs that you use to sell and manage your products. This topic also describes how to configure Real-time developer notifications to be notified whenever the status of a product changes.

## Set up a Google Play developer account

To publish your apps and games on Google Play, use the[Google Play Console](https://developer.android.com/distribute/console). You also use the Google Play Console to manage your billing-related products and settings.

To access the Google Play Console, you need to[set up a Google Play Developer Account](https://support.google.com/googleplay/android-developer/answer/6112435).

To sell paid apps and in-app purchases on Google Play, you must also set up a profile in the[Google Payments Center](https://pay.google.com)and then link that profile to your Google Play developer account. To learn how to link your profile to your account, or to learn how to check if you already have a linked account and profile, see[Link a Google Play developer account to your payments profile](https://support.google.com/googleplay/android-developer/answer/3092739).

## Enable billing-related features in the Google Play Console

Once you've set up a developer account, you must publish a version of your app that includes the Google Play Billing Library. This step is required to enable billing-related features in the Google Play Console, such as configuring the products you want to sell.

### Add library dependency

To integrate Google Play's billing system, first add a dependency to the Google Play Billing Library in your app. This library provides access to Android APIs that connect you to Google Play. From there, you can access purchase information, query for updates about purchases, prompt a user to make new purchases, and more.

The Google Play Billing Library is available from[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven). Add the dependency to your app's`build.gradle`file as shown:  

### Groovy

```groovy
dependencies {
    def billing_version = "8.3.0"

    implementation "com.android.billingclient:billing:$billing_version"
}
```

### Kotlin

```kotlin
dependencies {
    val billing_version = "8.3.0"

    implementation("com.android.billingclient:billing:$billing_version")
}
```

If you're using Kotlin, the Play Billing Library KTX module contains Kotlin extensions and coroutines support that enable you to write idiomatic Kotlin when using Google Play's billing system. To include these extensions in your project, add the following dependency to your app's`build.gradle`file as shown:  

### Groovy

```groovy
dependencies {
    def billing_version = "8.3.0"

    implementation "com.android.billingclient:billing-ktx:$billing_version"
}
```

### Kotlin

```kotlin
dependencies {
    val billing_version = "8.3.0"

    implementation("com.android.billingclient:billing-ktx:$billing_version")
}
```

The Kotlin code examples found on this page leverage KTX where possible.

### Upload your app

Once you've added the library to your app, build and publish your app. For this step,[create your app](https://support.google.com/googleplay/android-developer/answer/113469)and then publish to any track, including the[internal test track](https://support.google.com/googleplay/android-developer/answer/3131213).

## Create and configure your products

After enabling Google Play Billing features for your app, you need to configure products to sell.

The steps to create one-time products and subscriptions are similar. For each product, you need to provide a unique product ID, a title, a description, and pricing information. Subscriptions have additional required information, such as selecting whether it's an auto-renewing or prepaid renewal type for the base plan.

The Google Play Console provides a web interface that you can use to manage your products.

- To create and configure one-time products, see[Create a managed product](https://support.google.com/googleplay/android-developer/answer/1153481). Note that the Google Play Console refers to one-time products as*managed products*.

- To create and configure subscriptions, see[Create a subscription](https://support.google.com/googleplay/android-developer/answer/140504).

As an alternative to the web interface, you can also manage your products by using the[`inappproducts`](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)REST resource for in-app products and the[`monetization.subscriptions`](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)REST resource for subscription products in the Google Play Developer API.

## Configure the Google Play Developer API

The Google Play Developer API is a server-to-server API that complements the Google Play Billing Library on Android. This API provides functionality not available in the Google Play Billing Library, such as securely verifying purchases and issuing refunds to your users.

As part of integrating Google Play's billing system into your app, you must configure access to the Google Play Developer API through the Google Play Console. For instructions, see[Getting Started with Google Play Developer API](https://developers.google.com/android-publisher/getting_started).

Once you've configured access to the Google Play Developer API, be sure that you've granted the**View financial data** permission, which is needed to access billing-related functionality. For information on best practices, along with more information on configuring permissions, see[Add developer account users and manage permissions](https://support.google.com/googleplay/android-developer/answer/2528691).

## Configure Real-time developer notifications

Real-time developer notifications (RTDN) is a mechanism to receive notifications from Google whenever there is a change in a user's entitlement within your app. RTDN leverages the use of[Google Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/overview), which allows you to receive data that is either pushed to a URL that you set or is polled using a[client library](https://cloud.google.com/pubsub/docs/reference/libraries). These notifications allow you to react immediately to subscription state changes, avoiding the need to poll the Google Play Developer API. Note that inefficient use of the Google Play Developer API can lead to API quota restrictions.
| **Note:** You must call the[Google Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)after receiving Real-time developer notifications to get the complete status and update your own backend state. These notifications tell you only that the purchase state changed. They do not give you complete information about the purchase.

[Cloud Pub/Sub](https://cloud.google.com/pubsub/)is a fully-managed real-time messaging service that you can use to send and receive messages between independent applications. Google Play uses Cloud Pub/Sub to publish push notifications on topics to which you subscribe.

To receive notifications, you need to create a backend server to consume the messages sent to your topic. Your server can then consume these messages by responding to HTTPS requests to a registered endpoint or by using the[Cloud Pub/Sub Client Libraries](https://cloud.google.com/pubsub/docs/reference/libraries). These libraries are available in a variety of languages. More information can also be found in the[Create a Pub/Sub subscription](https://developer.android.com/google/play/billing/getting-ready#create-sub)section in this topic.

### Determine pricing and quotas

For details on pricing and quotas, refer to[pricing](https://cloud.google.com/pubsub/pricing)and[quotas](https://cloud.google.com/pubsub/quotas).

#### Estimate data usage

The data portion of the subscription notification is approximately 1KB of data per request. Each publish and pull requires a separate request, or approximately 2KB of data per notification. The number of notifications per month depends on your billing cycle and your users' behavior. You should expect*at least*one notification for each user during a billing cycle.

### Setup Cloud Pub/Sub

To enable Real-time developer notifications, you must first set up Cloud Pub/Sub using your own Google Cloud Platform (GCP) project and then enable the notifications for your app.

To use Cloud Pub/Sub, you must have a GCP project with the Cloud Pub/Sub API enabled. If you are not familiar with GCP and Cloud Pub/Sub, see the[Quickstart guide](https://cloud.google.com/pubsub/docs/quickstart-console).
| **Note:** You must configure Real-time developer notifications for*each*Android app separately. This means that you can choose to use the same GCP project as the one used to access the Play Developer API, or you can create a new GCP project for each app. If you have multiple apps, you must use the same Google Cloud Console project for the Google Play Developer API, but you can use different Google Cloud Console projects for each individual app.

### Create a topic

To start receiving notifications, you must create a[topic](https://cloud.google.com/pubsub/architecture#the_basics_of_a_publishsubscribe_service)to which Google Play should publish the notifications. To create a topic, follow the instructions in[Create the topic](https://cloud.google.com/pubsub/docs/quickstart-console#create_a_topic).

### Create a Pub/Sub subscription

To receive messages published to a topic, you must create a Pub/Sub subscription to that topic. To create a Pub/Sub subscription, do the following:

1. Read the[Cloud Pub/Sub Subscriber Guide](https://cloud.google.com/pubsub/subscriber)to determine whether to configure the subscription as either a*push subscription* or a*pull subscription* .
   - A push subscription allows Cloud Pub/Sub to send notifications to your secure backend by issuing HTTPS requests.
   - A pull subscription requires your secure backend server to initiate requests to the Cloud Pub/Sub server to retrieve messages.
2. Follow the instructions in[Add a subscription](https://cloud.google.com/pubsub/docs/quickstart-console#add_a_subscription)to create a subscription.

| **Note:** Pull subscriptions are commonly used to optimize resource utilization when a large number of messages are processed, which generally don't apply to RTDN. If you are unsure whether to start with push or pull, we suggest you use push, as it is generally easier to implement. See[Pull or push delivery](https://cloud.google.com/pubsub/docs/subscriber#push_pull)to help decide whether a push or pull subscription is best for your app.

### Grant publish rights on your topic

[Cloud Pub/Sub](https://cloud.google.com/pubsub/)requires that you grant Google Play privileges to publish notifications to your topic.

1. Open the[Google Cloud Console](https://console.cloud.google.com/).
2. Select your project, and then click**Pub/Sub**in the left-hand navigation.
3. Find your topic, and open the permissions details.

   ![accessing configuration for the permissions topic](https://developer.android.com/static/images/google/play/billing/permissions-link.png)**Figure 1.** Accessing configuration for the*Permissions*topic.
4. Add the service account`google-play-developer-notifications@system.gserviceaccount.com`, and grant it the role of**Pub/Sub Publisher**.

   ![adding google play service account as pub/sub publisher](https://developer.android.com/static/images/google/play/billing/add-service-account.png)**Figure 2.**Adding Google Play service account as Pub/Sub publisher.
5. Click**Save**to complete the topic set up.

   ![a configured topic](https://developer.android.com/static/images/google/play/billing/configured-topic.png)**Figure 3.**A configured topic.

### Enable Real-time developer notifications for your app

To enable Real-time developer notifications for your app, do the following:

1. Open the[Google Play Console](https://play.google.com/console/).
2. Select your app.
3. Go to**Monetize \> Monetization setup**.
4. Scroll to the**Real-time developer notifications**section at the top of the page.

   ![Real-time developer notifications section](https://developer.android.com/static/images/google/play/billing/rtdn-section.png)**Figure 4.**Real-time developer notifications section.
5. Check**Enable real-time notifications**.

6. In the**Topic name** field, enter the full Cloud Pub/Sub topic name that you configured earlier. The topic name should be in the format of`projects/{project_id}/topics/{topic_name}`where`project_id`is the unique identifier for your project, and`topic_name`is the name of the topic created earlier.

7. Click**Send Test Message**to send a test message. Performing a test publish helps to ensure that everything is set up and configured properly. If the test publish succeeds, a message is displayed stating that the test publish was successful. If you have attached a subscription for this topic, you should receive the test message.

   For a pull subscription, go to the subscription in Cloud Console, click**View Messages** , and proceed to pull messages. You should acknowledge any message you have pulled to avoid repeated delivery by Cloud Pub/Sub. For a[push subscription](https://cloud.google.com/pubsub/docs/push), check if the test message is delivered to your push endpoint. A successful response code will serve as a message acknowledgement.

   If the publish fails, an error is shown. Ensure that the topic name is correct and that the`google-play-developer-notifications@system.gserviceaccount.com`service account has**Pub/Sub Publisher**access to the topic.
8. Choose which notification types you'd like to receive.

   - **Get notifications for subscriptions and all voided purchases**- receive real-time developer notifications related to subscriptions and voided purchases. You won't receive notifications for one-time product purchases.
   - **Get all notifications for subscriptions and one-time products** - receive notifications for all subscription and voided purchase events. You'll also receive one-time product purchase events, such as`ONE_TIME_PRODUCT_PURCHASED`and`ONE_TIME_PRODUCT_CANCELED`. See[One-time purchase lifecycle](https://developer.android.com/google/play/billing/lifecycle/one-time)to learn more about these purchase events.
9. Click**Save changes**.

### Verifying your configuration

To receive Real-time developer notifications, you should create a secure backend server to consume the messages sent to your Cloud Pub/Sub topic.

You can test your configuration by using the**Send Test Message** button in the Google Play Console as described in the previous section. If you have not configured a backend server to consume notifications, you can use the`gcloud`command line tool to verify the configuration. For instructions on processing messages using`gcloud`, see[Pull the message from the subscription](https://cloud.google.com/pubsub/docs/quickstart-console#pull_the_message_from_the_subscription).

## Next steps

- [Integrate the library into your app](https://developer.android.com/google/play/billing/integrate)