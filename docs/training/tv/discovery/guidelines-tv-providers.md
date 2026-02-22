---
title: https://developer.android.com/training/tv/discovery/guidelines-tv-providers
url: https://developer.android.com/training/tv/discovery/guidelines-tv-providers
source: md.txt
---

# Watch Next guidelines for TV providers

In addition to the[Watch Next guidelines for app developers](https://developer.android.com/training/tv/discovery/guidelines-app-developers), Live TV providers must follow these guidelines when inserting content into the Watch Next channel.

### Live TV programs

Use the Watch Next API only to add movie and TV items. For example, if the user watches 45 minutes of the movie*Deadpool*, add the movie.

Don't use the channel-level entity. For example, if the user stops watching the channel TBS at 4:30pm,*don't*add the channel.

#### Unfinished content

Include Live TV items in Watch Next if one of the following is true:

- The user pauses a live broadcast and it is still on when the**Play Next**row renders. In this case, resume the content from the paused timestamp.
- The user has on-demand or DVR entitlements to that item. In this case, resume the content from the point the user left off. This supersedes the live broadcast.

#### New episodes

If the user starts a series, as described in the[guidelines for app developers](https://developer.android.com/training/tv/discovery/guidelines-app-developers#new-and-next-tv-episodes), and is fully caught up, then add a new episode into the Watch Next channel with[`WATCH_NEXT_TYPE_NEW`](https://developer.android.com/training/tv/discovery/watch-next-programs).
| **Note:** Add a new episode only if the episode is a first airing. Re-runs are not considered new episodes.

#### Remove a program

For all the previous scenarios, if a currently live program is added to the user's**Play Next** row, remove it once the live program completes*unless*one of the following is true:

- It is available on the user's digital video recorder (DVR).
- It is available on the service as a video on demand (VOD).

### Digital video recorder (DVR) programs

Add DVR recordings to the**Play Next** row*only*if one of the following is true:

- The user starts watching the recording but does not complete it.
- The recorded program is a new episode, as described[in another section](https://developer.android.com/training/tv/discovery/guidelines-tv-providers#live-tv-new-episodes)in this guide.

## TV on demand (TVOD) providers

Providers of on-demand TV content must follow the guidelines in this section.

### Rentals

If the user rents a piece of content from your service, add it to the Watch Next channel under the following conditions:

- The user has rented the content but has not yet viewed it. Use[`WATCH_NEXT_TYPE_NEW`](https://developer.android.com/training/tv/discovery/watch-next-programs)to add the content and set`lastEngagementTimeUtcMillis`as the timestamp when the user rented the content.
- The rental is about to expire. In this case, add it to the Watch Next channel 48 hours before the expiration time and set the type to`WATCH_NEXT_TYPE_NEW`.

If the user starts watching the content and leaves it unfinished, follow the[guidelines for unfinished content](https://developer.android.com/training/tv/discovery/guidelines-app-developers#types-of-content).

### Purchases

If the user purchases a piece of content from your service, add it to the Watch Next channel. Use[`WATCH_NEXT_TYPE_NEW`](https://developer.android.com/training/tv/discovery/watch-next-programs)and set`lastEngagementTimeUtcMillis`as the timestamp when the user purchased the content.

If the user starts watching the content and leaves it unfinished, follow the[guidelines for unfinished content](https://developer.android.com/training/tv/discovery/guidelines-app-developers#types-of-content).

### Non-purchased and non-rented content

*Don't*use the Watch Next API to surface new content the user has not already rented or purchased. For example, if the user rents one episode of a show and finishes watching it, don't push the next episode to Watch Next unless the user rents or purchases it.