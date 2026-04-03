---
title: https://developer.android.com/guide/playcore/engage/samples
url: https://developer.android.com/guide/playcore/engage/samples
source: md.txt
---

# Engage SDK Sample Apps

The Engage SDK includes a set of sample apps that demonstrate how to integrate the SDK in your app to publish different types of content. These apps are a great way to learn how to use the SDK, to get started with the integration in your own app, as well as some best practices.

The[sample apps](https://github.com/googlesamples/engage-sdk-samples)are available in the following languages:

- Java
- Kotlin

To run a sample app, clone the[Engage SDK Samples repository](https://github.com/googlesamples/engage-sdk-samples)and open the sample app project in your preferred IDE. Then, follow the instructions in the README file to build and run the app.

The sample apps repository includes two apps to demonstrate publishing different types of content:

- [Read Sample App](https://developer.android.com/guide/playcore/engage/samples#read-sample-app)
- [Watch Sample App](https://developer.android.com/guide/playcore/engage/samples#watch-sample-app)

## Read Sample App

This sample app demonstrates how to integrate 'reading' content using the Engage SDK APIs. The app includes the usage of different APIs mentioned in the[Engage SDK Read: Third-party technical integration instructions](https://developer.android.com/guide/playcore/engage/read)

When reviewing this sample app, consider the following:

- The app is written entirely in Java.
- The main focal point of the code is in the[read/publish](https://github.com/googlesamples/engage-sdk-samples/tree/main/read/app/src/main/java/com/google/samples/quickstart/engagesdksamples/read/publish)directory, containing all code necessary to publish through the Engage SDK.
- The app demonstrates the use of WorkManager as recommended in the Engage API docs, and[EngageServiceWorker](https://github.com/googlesamples/engage-sdk-samples/blob/main/read/app/src/main/java/com/google/samples/quickstart/engagesdksamples/read/publish/EngageServiceWorker.java)is the worker which does the publishing.
- [EbookToEntityConverter](https://github.com/googlesamples/engage-sdk-samples/blob/main/read/app/src/main/java/com/google/samples/quickstart/engagesdksamples/read/converters/EbookToEntityConverter.java)contains methods to build an Entity for publishing. This class is useful to show how to construct an entity from the data that already exists in your application.

| **Note:** The sample app uses one worker for publishing, passing in flags indicating which cluster to publish. Depending on your app architecture, you might choose to use multiple workers.

[Link to Engage SDK Read Sample App on GitHub](https://github.com/googlesamples/engage-sdk-samples/tree/main/read)

## Watch Sample App

This sample app demonstrates how to integrate video content using the Engage SDK APIs. The app includes the usage of different APIs mentioned in the[Engage SDK Watch: Third-party technical integration instructions](https://developer.android.com/guide/playcore/engage/watch)

When reviewing this sample app, consider the following:

- The app is written entirely in Kotlin.
- The main focal point of the code is in the[watch/publish](https://github.com/googlesamples/engage-sdk-samples/tree/main/watch/app/src/main/java/com/google/samples/quickstart/engagesdksamples/watch/publish)directory, containing all code necessary to publish through the Engage SDK.
- The app demonstrates the use of WorkManager as recommended in the Engage API docs, and[EngageServiceWorker](https://github.com/googlesamples/engage-sdk-samples/blob/main/watch/app/src/main/java/com/google/samples/quickstart/engagesdksamples/watch/publish/EngageServiceWorker.kt)is the worker which does the publishing.
- [ItemToEntityConverter](https://github.com/googlesamples/engage-sdk-samples/blob/main/watch/app/src/main/java/com/google/samples/quickstart/engagesdksamples/watch/data/converters/ItemToEntityConverter.kt)contains methods to build an Entity for publishing. This class is useful to show how to construct an entity from the data that already exists in your application.

| **Note:** The sample app uses one worker for publishing, passing in flags indicating which cluster to publish. Depending on your app architecture, you might choose to use multiple workers.

[Link to Engage SDK Watch Sample App on GitHub](https://github.com/googlesamples/engage-sdk-samples/tree/main/watch)

## Additional Tips

Here are some additional tips for using the Engage SDK sample apps:

- Use the sample apps to understand how to call specific Engage SDK APIs in your app.
- Experiment with different features of the Engage SDK.

## Support

Contact[`engage-developers@google.com`](mailto:engage-developers@google.com)if you have any questions that are not covered here.