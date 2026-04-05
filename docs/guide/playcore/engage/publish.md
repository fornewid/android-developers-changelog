---
title: https://developer.android.com/guide/playcore/engage/publish
url: https://developer.android.com/guide/playcore/engage/publish
source: md.txt
---

# Engage SDK Cluster publishing guidelines

This guide includes a set of guidelines for cluster publishing that developers can use when integrating with Engage SDK.

## Recommendation clusters

### Cluster Title

We recommend providing a unique and relevant cluster title that gives users more insight on the content of the cluster.

Here are some examples of good cluster titles based on the content:

- Shopping-related clusters
  - *Lightning Deals*
  - *Weekly must buys*
  - *Related to your purchase of Pixel Buds*
  - *Women's rain boots*
- Clusters of books on health
  - *Health, mind \& body*
  - *Recommended for you in Health*
  - *Best-sellers in Fitness*

### Cluster Content

When publishing recommendation clusters, developers must consider whether or not the user is signed in to the developer's application.

### When user is signed in

If the user is signed in to the developer app, we recommend publishing personalized or user-generated content clusters. Because personalized and user-generated content is more relevant to the user, they are more motivated to visit the developer app from the Google surface.

- Personalized recommendations can be published.
  - Here are some examples of personalized recommendations:
    - Top picks based on the user's watch history.
    - Books similar to books that are in the user's read history.
    - Songs by the user's favorite artists.
- User-generated content libraries can be published.
  - Here are some examples of user-generated content libraries:
    - The user's watchlist from the developer app.
    - A self-reported list of the user's favorite artists from the developer app.

|       Recommendation type        |                                           Content freshness strategy                                           |                                                                                                                                        Content freshness guideline                                                                                                                                         |
|----------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Personalized recommendations     | **Lenient** We recommend updating the recommendations once per day so users can see new recommendations daily. | Because users do not have an exact expectation of what the recommendation content will be, the content freshness strategy can be lenient.                                                                                                                                                                  |
| User-generated content libraries | **Strict** We recommend updating the content library as users exit the developer app.                          | It's important for this content to be in sync with the data displayed on Google surfaces. This is because unlike personalized recommendations, the user expects an exact set of content. Any significant delay in publishing will confuse users. Therefore, the content freshness strategy must be strict. |

### When user is not signed in

If a user is not signed in to the developer app, we still recommend publishing clusters so that users are encouraged to visit the developer app from the Google surface.

- Non-personalized recommendation clusters should be published.
  - Here are some examples of non-personalized recommendations:
    - Top 10 books read this year.
    - Newly released movies.
    - Trending podcasts.
- Publish a sign-in card.
  - In order to encourage users to sign in to the developer app, developers may choose to publish a sign-in card along with the non-personalized recommendation cluster. Check out the section below for more details on how to publish a[Sign In Card](https://developer.android.com/guide/playcore/engage/publish#user-management-cluster-signin).

|       Recommendation type        |                                                                                     Content freshness strategy                                                                                     |                                                                                                        Content freshness guideline                                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Non-personalized recommendations | **Lenient** We recommend updating the recommendations once per day.                                                                                                                                | Because users do not have an exact expectation of what the recommendation content will be, the content freshness strategy can be lenient.                                                                                                 |
| Sign-in card in recommendations  | **Strict** We recommend updating the sign-in card state as users exit the developer app. After users have signed in, developers must delete the card by calling`deleteUserManagementCluster()`API. | It's important for the sign-in state to be in sync with the Google surface. It's confusing for a user to see a sign-in card on Google's surface when they're already signed in. Therefore, the content freshness strategy must be strict. |

## Continuation clusters

When publishing continuation clusters, developers must consider whether or not the user is signed in to the developer's application.

### When user is signed in

- User-generated continuation clusters should be published.
  - Here are some examples of user-generated continuation clusters:
    - Continue Watching from where the user left off.
    - Continue Reading from where the user left off.

|          Continuation type           |                              Content freshness strategy                               |                                                                                                                                         Content freshness guideline                                                                                                                                          |
|--------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User-generated continuation clusters | **Strict** We recommend updating the content library as users exit the developer app. | It's important for this content to be in sync with the data displayed on Google's surfaces. This is because unlike personalized recommendations, the user expects an exact set of content. Any significant delay in publishing will confuse users. Therefore, the content freshness strategy must be strict. |

### When user is not signed in

Continuation journeys are primarily intended for signed-in users; however, you can also publish continuation clusters for signed-out users if your app supports guest sessions.

## User Management Cluster

The main aim of the User Management Cluster is to nudge users to perform certain actions on the provider app. The signin action directs users to the app's sign in page so that the app can publish content (or provide more personalized content)

### Sign In Card

|  Attribute  |                    Requirement                     |                                  Description                                   |
|-------------|----------------------------------------------------|--------------------------------------------------------------------------------|
| Action Uri  | Required                                           | Deeplink to Action (i.e. navigates to app sign in page)                        |
| Image       | Optional - If not provided, Title must be provided | Image Shown on the Card 16x9 aspect ratio images with a resolution of 1264x712 |
| Title       | Optional - If not provided, Image must be provided | Title on the Card                                                              |
| Action Text | Optional                                           | Text Shown on the CTA (i.e. Sign in)                                           |
| Subtitle    | Optional                                           | Optional Subtitle on the Card                                                  |

### Kotlin

```kotlin
var SIGN_IN_CARD_ENTITY =
      SignInCardEntity.Builder()
          .addPosterImage(
              Image.Builder()
                  .setImageUri(Uri.parse("http://www.x.com/image.png"))
                  .setImageHeightInPixel(500)
                  .setImageWidthInPixel(500)
                  .build())
          .setActionText("Sign In")
          .setActionUri(Uri.parse("http://xx.com/signin"))
          .build()

appEngagePublishClient.publishUserAccountManagementRequest(
            PublishUserAccountManagementRequest.Builder()
                .setSignInCardEntity(SIGN_IN_CARD_ENTITY)
                .build());
```

### Java

```java
SignInCardEntity SIGN_IN_CARD_ENTITY =
      new SignInCardEntity.Builder()
          .addPosterImage(
              new Image.Builder()
                  .setImageUri(Uri.parse("http://www.x.com/image.png"))
                  .setImageHeightInPixel(500)
                  .setImageWidthInPixel(500)
                  .build())
          .setActionText("Sign In")
          .setActionUri(Uri.parse("http://xx.com/signin"))
          .build();

appEngagePublishClient.publishUserAccountManagementRequest(
            new PublishUserAccountManagementRequest.Builder()
                .setSignInCardEntity(SIGN_IN_CARD_ENTITY)
                .build());
```

After users have signed in, developers must delete the card by calling`deleteUserManagementCluster()`API.

## Update Publish Status

If for any internal business reason, none of the clusters is published, we**strongly recommend** updating the publish status using the**updatePublishStatus**API. This is important because :

- Providing the status in all scenarios, even when the content is published (STATUS == PUBLISHED), is critical to populate dashboards that use this explicit status to convey the health and other metrics of your integration.
- If no content is published but the integration status isn't broken (STATUS == NOT_PUBLISHED), Google can avoid triggering alerts in the app health dashboards. It confirms that content is not published due to an**expected**situation from the provider's standpoint.
- It helps developers provide insights into when the data is published vs not.
- Google may use the status codes to nudge the user to do certain actions in the app so they can see the app content or overcome it.

The list of eligible publish status codes are :  

    // Content is published
    AppEngagePublishStatusCode.PUBLISHED,

    // Content is not published as user is not signed in
    AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN,

    // Content is not published as user is not subscribed
    AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SUBSCRIPTION,

    // Content is not published as user location is ineligible
    AppEngagePublishStatusCode.NOT_PUBLISHED_INELIGIBLE_LOCATION,

    // Content is not published as there is no eligible content
    AppEngagePublishStatusCode.NOT_PUBLISHED_NO_ELIGIBLE_CONTENT,

    // Content is not published as the feature is disabled by the client
    // Available in v1.3.1
    AppEngagePublishStatusCode.NOT_PUBLISHED_FEATURE_DISABLED_BY_CLIENT,

    // Content is not published as the feature due to a client error
    // Available in v1.3.1
    AppEngagePublishStatusCode.NOT_PUBLISHED_CLIENT_ERROR,

    // Content is not published as the feature due to a service error
    // Available in v1.3.1
    AppEngagePublishStatusCode.NOT_PUBLISHED_SERVICE_ERROR,

    // Content is not published due to some other reason
    // Reach out to engage-developers@ before using this enum.
    AppEngagePublishStatusCode.NOT_PUBLISHED_OTHER

If the content is not published due to a user not logged in, we would recommend publishing the Sign In Card. If for any reason providers are not able to publish the Sign In Card then we recommend calling the**updatePublishStatus** API with the status code**NOT_PUBLISHED_REQUIRES_SIGN_IN**  

### Kotlin

```kotlin
client.updatePublishStatus(
   PublishStatusRequest.Builder()
     .setStatusCode(AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN)
     .build())
```

### Java

```java
client.updatePublishStatus(
    new PublishStatusRequest.Builder()
        .setStatusCode(AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN)
        .build());
```

## WorkManager for cluster publishing

We recommend using[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)to publish clusters, because it is the recommended solution for background work where the execution must be both opportunistic and guaranteed.

- WorkManager performs your background work as soon as it can.
- WorkManager handles the logic to start your work under a variety of conditions, even if a user navigates away from your app.

When the user navigates away from the app, we recommend starting a background job that publishes continuation clusters along with recommendation clusters. A good place to handle this logic is[`Activity.onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()), which is called when the user navigates away from the app.

We suggest using[`PeriodicWorkRequest`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest)to schedule a recurring job that publishes clusters every 24 hours. By using a[`CANCEL_AND_REENQUEUE`](https://developer.android.com/reference/androidx/work/ExistingPeriodicWorkPolicy#CANCEL_AND_REENQUEUE)policy for triggering the work, developers can ensure that WorkManager sends the updated data every time a user navigates away from the app. This helps prevent users from seeing stale data.

The following example demonstrates this:  

    // Define the PublishClusters Worker requiring input
    public class PublishClusters extends Worker {

       public PublishClusters(Context appContext, WorkerParameters workerParams) {
           super(appContext, workerParams);
       }

       @NonNull
       @Override
       public Result doWork() {
           // publish clusters
       }
       ...
    }

    public static void schedulePublishClusters(Context appContext) {
    // Create a PeriodicWorkRequest to schedule a recurring job to update
    // clusters at a regular interval
    PeriodicWorkRequest publishClustersEntertainmentSpace =
    // Define the time for the periodic job
           new PeriodicWorkRequest.Builder(PublishClusters.class, 24, TimeUnit.HOURS)
    // Set up a tag for the worker.
    // Tags are Unique identifier, which can be used to identify that work
    // later in order to cancel the work or observe its progress.
              .addTag("Publish Clusters to Entertainment Space")
              .build();

    // Trigger Periodic Job, this will ensure that the periodic job is triggered
    // only once since we have defined a uniqueWorkName
    WorkManager.getInstance(appContext).enqueueUniquePeriodicWork(
    // uniqueWorkName
         "publishClustersEntertainmentSpace",
    // If a work with the uniqueWorkName is already running, it will cancel the
    // existing running jobs and replace it with the new instance.
    // ExistingPeriodicWorkPolicy#CANCEL_AND_REENQUEUE
         ExistingPeriodicWorkPolicy.CANCEL_AND_REENQUEUE,
    // Recurring Work Request
    publishClustersEntertainmentSpace);

    }

## Handle broadcast intents

In addition to making publish content API calls through a job, it is also required to set up a[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver)to receive the request for a content publish.

However,**developers must be careful not to rely solely on broadcasts** , because they are only triggered in certain scenarios---mainly, for app reactivation and forcing a data sync.**They are only triggered when the Engage Service determines that the content might be stale.**That way, there is greater confidence that the user will have a fresh content experience, even if the application has not been opened for a long time.

The`BroadcastReceiver`must be set up in the following two ways:

- Dynamically register an instance of the`BroadcastReceiver`class using`Context.registerReceiver()`. This enables communication from applications that are still live in memory.
- Statically declare an implementation with the`<receiver>`tag in your`AndroidManifest.xml`file. This allows the application to receive broadcast intents when it is not running, and also allows the application to publish the content.