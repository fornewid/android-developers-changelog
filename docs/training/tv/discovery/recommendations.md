---
title: Recommend content on the home screen  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/recommendations
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Recommend content on the home screen Stay organized with collections Save and categorize content based on your preferences.



The Android TV *home screen* displays recommended content using *channels* and
*programs*. Channels are displayed as individual rows on the home screen, with
cards that display all of the available programs for that channel.

Your app should have at least one channel. The first channel your
app creates becomes its [default channel](/training/tv/discovery/recommendations-channel#default-channel),
and Android TV displays that channel automatically on the home screen. Your app
can offer other channels, but the user must select and approve those channels
before they are added to the home screen.

If your app features TV shows, movies, or other video content, we recommend that
you support [video previews](/training/tv/discovery/preview-videos) and
integrate with the [Watch Next channel](/training/tv/discovery/recommendations-channel#watch-next).
The Watch Next channel is controlled by the Android system. Your app can add
user-related programs to this channel, such as programs that the user marked as
interesting, stopped watching in the middle, or that are related to the content
the user is watching (like the next episode in a series or next season of a
show).

## Ensure compatibility

The home screen displays recommendations two different ways depending on the
version of Android:

* In Android 8.0 (API level 26) and later, apps can show recommendations in one or
  more channels that appear on separate rows. One channel (the default channel)
  always appears. The user can discover and add the other channels to their home
  screen. Learn how to create [recommendation channels](/training/tv/discovery/recommendations-channel)
  on the home screen.
* Before Android 8.0, Android TV shows all recommendations in a single
  recommendations row that always appears on the screen. Learn how to create the
  [recommendation row](/training/tv/discovery/recommendations-row) on the home
  screen.

To be able to show recommendations on all versions of Android TV, your app
should implement both recommendation APIs. Test the current system API level and
use the appropriate API to build the recommendation row or channels.

### Kotlin

```
if (android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
  // Use the home screen recommendation channels API
} else {
  // Use the recommendations row API
}
```

### Java

```
if (android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
  // Use the home screen recommendation channels API
} else {
  // Use the recommendations row API
}
```

If your app was compiled using API level 25 or earlier, it can still run on
Android TV in level 26. The old recommendations behavior is forward-compatible,
but constrained:

* The recommendations row is automatically converted and appears as a new
  channel on the home screen.
* The programs on the converted channel respond to updates from your
  [recommendation service](/training/tv/discovery/recommendations-row#service),
  but the user cannot use the TV's UI to manipulate the programs on the channel
  (add/remove programs, copy programs to the Watch Next channel).
* If you update the app to API level 26, the converted channel
  still appears on TVs running API 26. The TV removes the converted channel from
  the screen the first time your app displays a channel created with the new API.
  This happens immediately if the app creates a
  [default channel](/training/tv/discovery/recommendations-channel#the_default_channel),
  or later when the user selects and adds any other channel created by your app.

**Note:** This forward-compatible behavior is temporary, it will be removed sometime
in the future. To ensure compatibility, the best practice is to implement both
APIs, as described above.

[Next

Channels on the home screen

arrow\_forward](/training/tv/discovery/recommendations-channel)