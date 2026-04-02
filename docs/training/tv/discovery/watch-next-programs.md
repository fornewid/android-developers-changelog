---
title: Watch Next attributes  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/watch-next-programs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Watch Next attributes Stay organized with collections Save and categorize content based on your preferences.




When you add an audio or video program to the **Play Next** row, you must include
the attributes in the following table in addition to the attributes for audio and
video programs. Each attribute is linked to the corresponding setter in
[`WatchNextProgram.Builder`](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder).

**Note:** If you are integrating with the client-side
[WatchNext API](/reference/androidx/tvprovider/media/tv/WatchNextProgram), you must populate and align the
[Internal Provider ID](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder#setInternalProviderId(java.lang.String))
with the internal ID you provide in the [Media Actions](https://developers.google.com/actions/media)
feed. Doing so helps Android TV reconcile the asset more effectively and
provides a high-confidence feature to users.

| Attribute | Notes |
| --- | --- |
| [Watch Next Type](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder#setWatchNextType(int)) | One of:  * [`WATCH_NEXT_TYPE_CONTINUE`](/reference/androidx/tvprovider/media/tv/TvContractCompat.WatchNextPrograms#WATCH_NEXT_TYPE_CONTINUE()) * [`WATCH_NEXT_TYPE_NEXT`](/reference/androidx/tvprovider/media/tv/TvContractCompat.WatchNextPrograms#WATCH_NEXT_TYPE_NEXT()) * [`WATCH_NEXT_TYPE_NEW`](/reference/androidx/tvprovider/media/tv/TvContractCompat.WatchNextPrograms#WATCH_NEXT_TYPE_NEW()) * [`WATCH_NEXT_TYPE_WATCHLIST`](/reference/androidx/tvprovider/media/tv/TvContractCompat.WatchNextPrograms#WATCH_NEXT_TYPE_WATCHLIST()) |
| [Last Enagagement Time](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder#setLastEngagementTimeUtcMillis(long)) | The time the user or app last engaged with the program. |
| [Last Playback Position](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder#setLastPlaybackPositionMillis(int)) | Only required for `WATCH_NEXT_TYPE_CONTINUE`. |
| [Duration](/reference/androidx/tvprovider/media/tv/WatchNextProgram.Builder#setDurationMillis(int)) | Only required for `WATCH_NEXT_TYPE_CONTINUE`. |

[Previous

arrow\_back

Add programs](/training/tv/discovery/watch-next-add-programs)

[Next

Guidelines for app developers

arrow\_forward](/training/tv/discovery/guidelines-app-developers)