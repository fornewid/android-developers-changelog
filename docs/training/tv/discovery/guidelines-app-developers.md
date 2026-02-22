---
title: https://developer.android.com/training/tv/discovery/guidelines-app-developers
url: https://developer.android.com/training/tv/discovery/guidelines-app-developers
source: md.txt
---

# Watch Next guidelines for app developers

Follow these guidelines when you insert content into the Watch Next channel.

## Types of content to include in the Watch Next channel

Limit your app's programmatic additions to traditional movies and TV shows. Don't add clips and other short-form content.

### Include unfinished movies

Add unfinished movies to the Watch Next channel using[`TYPE_MOVIE`](https://developer.android.com/training/tv/discovery/video-programs). A movie is unfinished if it is started but not finished based on the following guidelines:

- A movie is started if the user watches more than 3% or 2 minutes, whichever timestamp is earlier.
- A movie is finished if the end credits start. In this case, do*not*add it to the Watch Next channel. You can determine this state using a technology that auto-detects the end credits or use an approximation based on the content length.

### Include unfinished TV episodes

Add unfinished TV episodes to the Watch Next channel using[`TYPE_TV_EPISODE`](https://developer.android.com/training/tv/discovery/video-programs). An episode is unfinished if it is started but not finished based on the following guidelines:

- An episode is started if the user watches more than 2 minutes.
- An episode is finished if the end credits start. In this case, do*not*add it to the Watch Next channel. You can determine this state using a technology that auto-detects the end credits or use an approximation based on the content length, such as less than 3 minutes remaining in an episode.

## Handle new TV episodes and next TV episodes

Add new episodes and next episodes of series that the user has started, based on the following guidelines, to the Watch Next channel using[`TYPE_TV_EPISODE`](https://developer.android.com/training/tv/discovery/video-programs):

- The user starts a series if they watch more than 2 minutes, or 1 minute after the introduction completes, of any episode in the series.
- If the user starts a series and finishes an episode, and the next episode in the series is available in your service, add this next episode to the Watch Next channel using[`WATCH_NEXT_TYPE_NEXT`](https://developer.android.com/training/tv/discovery/watch-next-programs).
- If the user is fully caught up on all current episodes in a series and a new season or episode becomes available, add this new episode to the Watch Next channel using[`WATCH_NEXT_TYPE_NEW`](https://developer.android.com/training/tv/discovery/watch-next-programs). Add the new episode no matter how long it has been since the user last watched the series, such as after a year or more.

## When to add an item to the Watch Next channel

Add unfinished content and new episodes of previously viewed series to the Watch Next channel according to the following guidelines.

### When to add unfinished content

When a user has an unfinished piece of content, add that content to the Watch Next channel immediately when either of the following occur:

- The user exits the app on Android TV.
- The user pauses or stops playback for a piece of content for more than 5 minutes.

In these scenarios, publish any unfinished content immediately, with a maximum latency of 5 seconds. For example, when the user exits the Android TV app, publish any unfinished items using the Watch Next API within 5 seconds.

Publish any unfinished content to Android TV using the Watch Next API regardless of where the viewing occurred. For example, if the user watches a movie in their Chrome browser and pauses it, then the app on the Android TV must publish the unfinished content to the Android TV immediately, with a maximum latency of 5 seconds.

### When to add new episodes

Add new episodes of a previously watched series immediately when all of the following are true:

- The new episode is available on your service.
- The user completes the previous episode.
- The user is entitled to watch the new episode.

Add the new episode no matter how long it has been since the user last watched the series, such as after a year or more.

### Eligibility of content and UI updates

The user must interact with the content within your app for the content to be eligible to be published to the Watch Next channel.

Don't add more than one episode from the same TV series. For example, don't add an unfinished episode and a new episode from the same series.

Don't update all items in the**Play Next** row when one item changes.*Only*update the item the user has interacted with since the last update.

## What data to include for a Watch Next item

Include the following for each Watch Next item:

- Watch Next type
- Last playback position
- Duration
- Last engagement time
- Video program attributes: in addition to the required attributes marked in the[video program attributes table](https://developer.android.com/training/tv/discovery/video-programs#attribute-table), the[Content ID attribute](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String))must be set for every video program. The Content ID attribute must match the internal ID you provide in the[Media Actions](https://developers.google.com/actions/media)feed. This lets Android TV reconcile the asset more effectively and provides a high-confidence feature to users.

## Remove content from the Watch Next channel

Remove content once the user finishes watching a movie or there is no unwatched available episode for a TV series.