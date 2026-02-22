---
title: https://developer.android.com/guide/playcore/engage/tv/continue-watching/client
url: https://developer.android.com/guide/playcore/engage/tv/continue-watching/client
source: md.txt
---

This guide covers how to integrate Continue Watching into your Android TV app
using the Engage SDK.

## Pre-work

| **Important:** [Express interest in developing the Video Discovery API](http://g.co/tv/vda).

Complete the [Pre-work](https://developer.android.com/guide/playcore/engage/tv/getting-started#pre-work) instructions in the Getting Started guide.

## Integration

| **Note:** The Continue Watching API works differently from the [Watch Next API](https://developer.android.com/training/tv/discovery/watch-next-add-programs). Instead of adding or removing items one by one, it replaces the entire list of "continue watching" items each time it updates. This means you need to send all the items you want to show every time you update. You should display as many entities as possible in the continue watching row, but no more than 10. Also, the new API combines the steps for publishing the list and the items into one, making it simpler. Keep in mind that Google TV might not show all the items you send, as it combines lists from different apps.

### Create entities

The SDK has defined different entities to represent each item type. Continuation
cluster supports following entities:

1. [`MovieEntity`](https://developer.android.com/guide/playcore/engage/watch#movieentity)
2. [`TvEpisodeEntity`](https://developer.android.com/guide/playcore/engage/watch#tvepisodeentity)
3. [`LiveStreamingVideoEntity`](https://developer.android.com/guide/playcore/engage/watch#livestreamingvideoentity)
4. [`VideoClipEntity`](https://developer.android.com/guide/playcore/engage/watch#videoclipentity)

| **Note:** [`TvShowEntity`](https://developer.android.com/guide/playcore/engage/watch#tvshowentity) and [`TvSeasonEntity`](https://developer.android.com/guide/playcore/engage/watch#tvseasonentity) are not supported for the Continuation cluster for continue watching. When a user finishes one TV Episode, the next `TvEpisodeEntity` should be published for the user to continue watching the next episode.

Specify the platform-specific URIs and poster images for these entities.

Also, create playback URIs for each platform---such as Android TV, Android, or
iOS---if you haven't already. So when a user continues watching on each platform,
the app uses a targeted playback URI to play the video content.
**Note:** In the rare case when the playback URIs are identical for all platforms, you will still have to repeat it for every platform that you want to continue watching to happen.  

    // Required. Set this when you want continue watching entities to show up on
    // Google TV
    val playbackUriTv = PlatformSpecificUri.Builder()
        .setPlatformType(PlatformType.TYPE_ANDROID_TV)
        .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_tv"))
        .build()

    // Required. Set this when you want continue watching entities to show up on
    // Google TV Android app, Entertainment Space, Playstore Widget
    val playbackUriAndroid = PlatformSpecificUri.Builder()
        .setPlatformType(PlatformType.TYPE_ANDROID_MOBILE)
        .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_android"))
        .build()

    // Optional. Set this when you want continue watching entities to show up on
    // Google TV iOS app
    val playbackUriIos = PlatformSpecificUri.Builder()
        .setPlatformType(PlatformType.TYPE_IOS)
        .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_ios"))
        .build()

    val platformSpecificPlaybackUris =
        Arrays.asList(playbackUriTv, playbackUriAndroid, playbackUriIos)

Poster images require a URI and pixel dimensions (height and width). Target
different form factors by providing multiple poster images, but verify that all
images maintain a 16:9 aspect ratio and a minimum height of 200 pixels for
correct display of the "Continue Watching" entity, especially within Google's
[Entertainment Space](https://support.google.com/entertainmentspace/answer/10346911). Images with a height less than 200
pixels may not be shown.  

    val images = Arrays.asList(
        Image.Builder()
            .setImageUri(Uri.parse("http://www.example.com/entity_image1.png"))
            .setImageHeightInPixel(300)
            .setImageWidthInPixel(169)
            .build(),
        Image.Builder()
            .setImageUri(Uri.parse("http://www.example.com/entity_image2.png"))
            .setImageHeightInPixel(640)
            .setImageWidthInPixel(360)
            .build()
        // Consider adding other images for different form factors
    )

#### MovieEntity

This example show how to create a `MovieEntity` with all the required fields:  

    val movieEntity = MovieEntity.Builder()
       .setWatchNextType(WatchNextType.TYPE_CONTINUE)
       .setName("Movie name")
       .addPlatformSpecificPlaybackUri(platformSpecificPlaybackUris)
       .addPosterImages(images)
       // Timestamp in millis for sample last engagement time 12/1/2023 00:00:00
       .setLastEngagementTimeMillis(1701388800000)
       // Suppose the duration is 2 hours, it is 72000000 in milliseconds
       .setDurationMills(72000000)
       // Suppose last playback offset is 1 hour, 36000000 in milliseconds
       .setLastPlayBackPositionTimeMillis(36000000)
       .build()

Providing details like genres and content ratings gives Google TV the power to
showcase your content in more dynamic ways and connect it with the right
viewers.  

    val genres = Arrays.asList("Action", "Science fiction")
    val rating1 = RatingSystem.Builder().setAgencyName("MPAA").setRating("PG-13").build()
    val contentRatings = Arrays.asList(rating1)
    val movieEntity = MovieEntity.Builder()
        ...
        .addGenres(genres)
        .addContentRatings(contentRatings)
        .build()

Entities automatically remain available for 60 days unless you specify a shorter
expiration time. Only set a custom expiration if you need the entity to be
removed before this default period.  

    // Set the expiration time to be now plus 30 days in milliseconds
    val expirationTime = DisplayTimeWindow.Builder()
        .setEndTimestampMillis(now().toMillis()+2592000000).build()
    val movieEntity = MovieEntity.Builder()
        ...
        .addAvailabilityTimeWindow(expirationTime)
        .build()

#### TvEpisodeEntity

This example show how to create a `TvEpisodeEntity` with all the required
fields:  

    val tvEpisodeEntity = TvEpisodeEntity.Builder()
        .setWatchNextType(WatchNextType.TYPE_CONTINUE)
        .setName("Episode name")
        .addPlatformSpecificPlaybackUri(platformSpecificPlaybackUris)
        .addPosterImages(images)
        // Timestamp in millis for sample last engagement time 12/1/2023 00:00:00
        .setLastEngagementTimeMillis(1701388800000)
        .setDurationMills(72000000) // 2 hours in milliseconds
        // 45 minutes and 15 seconds in milliseconds is 2715000
        .setLastPlayBackPositionTimeMillis(2715000)
        .setEpisodeNumber("2")
        .setSeasonNumber("1")
        .setShowTitle("Title of the show")
        .build()

Episode number string (such as `"2"`), and season number string (such as `"1"`)
will be expanded to the proper form before being displayed on the continue
watching card. Note that they should be a numeric string, don't put "e2", or
"episode 2", or "s1" or "season 1".

If a particular TV show has a single season, set season number as 1.

To maximize the chances of viewers finding your content on Google TV, consider
providing additional data such as genres, content ratings, and availability time
windows, as these details can enhance displays and filtering options.  

    val genres = Arrays.asList("Action", "Science fiction")
    val rating1 = RatingSystem.Builder().setAgencyName("MPAA").setRating("PG-13").build()
    val contentRatings = Arrays.asList(rating1)
    val tvEpisodeEntity = TvEpisodeEntity.Builder()
        ...
        .addGenres(genres)
        .addContentRatings(contentRatings)
        .setSeasonTitle("Season Title")
        .setShowTitle("Show Title")
        .build()

#### VideoClipEntity

Here's an example of creating a `VideoClipEntity` with all the required fields.

`VideoClipEntity` represents a user generated clip like a Youtube video.  

    val videoClipEntity = VideoClipEntity.Builder()
        .setPlaybackUri(Uri.parse("https://www.example.com/uri_for_current_platform"))
        .setWatchNextType(WatchNextType.TYPE_CONTINUE)
        .setName("Video clip name")
        .addPlatformSpecificPlaybackUri(platformSpecificPlaybackUris)
        .addPosterImages(images)
        // Timestamp in millis for sample last engagement time 12/1/2023 00:00:00
        .setLastEngagementTimeMillis(1701388800000)
        .setDurationMills(600000) //10 minutes in milliseconds
        .setLastPlayBackPositionTimeMillis(300000) //5 minutes in milliseconds
        .addContentRating(contentRating)
        .build()

You can optionally set the creator, creator image, created time in milliseconds,
or availability time window .

#### LiveStreamingVideoEntity

Here's an example of creating an `LiveStreamingVideoEntity` with all the
required fields.  

    val liveStreamingVideoEntity = LiveStreamingVideoEntity.Builder()
        .setPlaybackUri(Uri.parse("https://www.example.com/uri_for_current_platform"))
        .setWatchNextType(WatchNextType.TYPE_CONTINUE)
        .setName("Live streaming name")
        .addPlatformSpecificPlaybackUri(platformSpecificPlaybackUris)
        .addPosterImages(images)
        // Timestamp in millis for sample last engagement time 12/1/2023 00:00:00
        .setLastEngagementTimeMillis(1701388800000)
        .setDurationMills(72000000) //2 hours in milliseconds
        .setLastPlayBackPositionTimeMillis(36000000) //1 hour in milliseconds
        .addContentRating(contentRating)
        .build()

Optionally, you can set the start time, broadcaster, broadcaster icon, or
availability time window for the live streaming entity.

For detailed information on attributes and requirements, see the [API
reference](https://developer.android.com/reference/com/google/android/engage/video/datamodel/package-summary).

### Provide Continuation cluster data

`AppEngagePublishClient` is responsible for publishing the Continuation cluster.
You use the `publishContinuationCluste` method to publish a
`ContinuationCluster` object.

Make sure to initialize the client and check for service availability as
described in the [Getting Started guide](https://developer.android.com/guide/playcore/engage/tv/getting-started#common-integration).  

    client.publishContinuationCluster(
        PublishContinuationClusterRequest
            .Builder()
            .setContinuationCluster(
                ContinuationCluster.Builder()
                    .setAccountProfile(accountProfile)
                    .addEntity(movieEntity1)
                    .addEntity(movieEntity2)
                    .addEntity(tvEpisodeEntity1)
                    .addEntity(tvEpisodeEntity2)
                    .setSyncAcrossDevices(true)
                    .build()
            )
            .build()
    )

When the service receives the request, the following actions take place within
one transaction:

- Existing `ContinuationCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated `ContinuationCluster`.

In case of an error, the entire request is rejected and the existing state is
maintained.

The publish APIs are upsert APIs; it replaces the existing content. If you need
to update a specific entity in the continuation cluster, you will need to
publish all entities again.

Continuation cluster data should only be provided for adult accounts. Publish
only when the account profile belongs to an adult.
| **Warning:** Don't call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

#### Cross-device syncing

`SyncAcrossDevices` flag controls whether a user's `ContinuationCluster` data is
synchronized across devices such as TV, phone, tablets, etc. Cross-device
syncing is disabled by default.

Values:

- `true`: Continuation cluster data is shared across all the user's devices for a seamless viewing experience. We strongly recommend this option for the best cross-device experience.
- `false`: Continuation cluster data is restricted to the current device.

#### Obtain Consent

The media application must provide a clear setting to enable or disable
cross-device syncing. Explain the benefits to the user and store the user's
preference once and apply it in `publishContinuationCluster` accordingly.  

    // Example to allow cross device syncing.
    client.publishContinuationCluster(
        PublishContinuationClusterRequest
            .Builder()
            .setContinuationCluster(
                ContinuationCluster.Builder()
                    .setAccountProfile(accountProfile)
                    .setSyncAcrossDevices(true)
                    .build()
            )
            .build()
    )

To get the most out of our cross-device feature, verify that the app obtains
user consent and enable `SyncAcrossDevices` to `true`. This allows content to
seamlessly sync across devices, leading to a better user experience and
increased engagement. For example, a partner who implemented this saw a 40%
increase in "continue watching" clicks because their content was surfaced on
multiple devices.

#### Delete the Video discovery data

To manually delete a user's data from the Google TV server before the standard
60-day retention period, use the `deleteClusters` method. Upon receiving the
request, the service will delete all existing video discovery data for the
account profile, or for the entire account.
| **Important:** It is important to set syncAcrossDevices flag to true even in the delete requests so that the data is deleted from the server (even when the delete reason is USER_LOGOUT).

The [`DeleteReason`](https://developer.android.com/reference/com/google/android/engage/service/DeleteReason) enum defines the reason for data deletion.
The following code removes continue watching data on logout.  


    // If the user logs out from your media app, you must make the following call
    // to remove continue watching data from the current google TV device,
    // otherwise, the continue watching data will persist on the current
    // google TV device until 60 days later.
    client.deleteClusters(
        DeleteClustersRequest.Builder()
            .setAccountProfile(AccountProfile())
            .setReason(DeleteReason.DELETE_REASON_USER_LOG_OUT)
            .setSyncAcrossDevices(true)
            .build()
    )

| **Warning:** Don't call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

## Testing

Use the [verification app](https://developer.android.com/guide/playcore/engage/tv/getting-started#testing) to verify that Engage SDK integration is
working correctly.
| **Note:** Check if your app is correctly calling `isServiceAvailable` and `publishClusters` APIs in logcat. Before submitting the APK, check if you are able to see `publishClusters` is called logs in your logcat during development to verify that you are calling the APIs at the correct events.

After you invoke the publish API, confirm that your data is being correctly
published by checking the verification app. Your continuation cluster should be
displayed as a distinct row within the app's interface.

- Test these actions in your app:
  - Sign in.
  - Switch between profiles(if applicable).
  - Start, then pause a video, or return to the home page.
  - Close the app during video playback.
  - Remove an item from the "Continue Watching" row (if supported).
- After each action, confirm that your app invoked the `publishContinuationClusters` API and that the data is correctly displayed in the verification app.
- The verification app shows a green "All Good" check mark for correctly
  implemented entities.

  ![Verification App Success Screenshot](https://developer.android.com/static/images/guide/playcore/engage/va-success.png) **Figure 1.** Verification App Success
- The verification app will flag any problematic entities.

  ![Verification App Error Screenshot](https://developer.android.com/static/images/guide/playcore/engage/va-error.png) **Figure 2.** Verification App Error
- To troubleshoot entities with errors, use your TV remote to select and click
  the entity in the verification app. The specific problems will be displayed
  and highlighted in red for your review (see example below).

  ![Verification App error details](https://developer.android.com/static/images/guide/playcore/engage/va-error-details.png) **Figure 3.** Verification App Error Details