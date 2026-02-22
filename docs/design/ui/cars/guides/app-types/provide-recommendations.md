---
title: https://developer.android.com/design/ui/cars/guides/app-types/provide-recommendations
url: https://developer.android.com/design/ui/cars/guides/app-types/provide-recommendations
source: md.txt
---

# Provide recommendations

The last design step for Android Auto is to identify 10 media items to be showcased as recommendations when the user isn't listening to anything.

Recommended content can appear in the dashboard, allowing users to quickly discover or find new media content.

If the app doesn't provide a source for these recommendations, the default logic is to pull recommendations from the top of the browse tree -- which may not appeal to the user. For example, this default logic might suggest multiple episodes of the same podcast, while the user might prefer having a variety of podcasts to choose from.
| **Note:** Apps can send recommendations through the media browser service using a lookup key in the[`EXTRA_SUGGESTED`](https://developer.android.com/reference/android/service/media/MediaBrowserService.BrowserRoot#EXTRA_SUGGESTED)string.

## Consider the context

Users may have different listening habits in different settings, so keep the driving context in mind when choosing your recommendations. You may want to pull media content from the user's listening history in the car, rather than from what they listen to in their living room.

## Recommendation example

![Recommendations example](https://developer.android.com/static/images/design/ui/cars/app-cuj/recommendations-fig-1.png)This card supplies a For You pane with suggested playlists (Android Auto example).

## UX requirements

Providing relevant recommendations helps drivers quickly choose media with minimal distraction.

In the following table, requirements in the SHOULD column are recommended but not required:

| Requirement level |                                 Requirements                                  |
|-------------------|-------------------------------------------------------------------------------|
| SHOULD            | Provide a source from which to pull relevant media recommendations for users. |