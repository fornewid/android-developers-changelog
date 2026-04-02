---
title: Game program attributes  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/game-programs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Game program attributes Stay organized with collections Save and categorize content based on your preferences.




All game programs have the type attribute
[`TYPE_GAME`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_GAME()).

The following table shows the attributes that can be assigned to a game program,
each linked to the corresponding setter in
[`PreviewProgram.Builder`](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder).
Attributes marked ✔ are required; those marked (✔) are optional.

| Attribute | Required or Optional |
| --- | --- |
| [Author](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAuthor(java.lang.String)) | (✔) |
| [Availability](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAvailability(int)) | (✔) |
| [Channel ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setChannelId(long)) | ✔ |
| [Content ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String)) | (✔) |
| [Genre](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setGenre(java.lang.String)) | (✔) |
| [Intent URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setIntentUri(android.net.Uri)) | ✔ |
| [Internal Provider ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInternalProviderId(java.lang.String)) | (✔) |
| [Offer Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setOfferPrice(java.lang.String)) | (✔) |
| [Poster Art Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtAspectRatio(int)) | ✔ |
| [Poster Art URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtUri(android.net.Uri)) | ✔ |
| [Preview Video URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewVideoUri(android.net.Uri)) | (✔) |
| [Release Date](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReleaseDate(java.lang.String)) | (✔) |
| [Review Rating](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRating(java.lang.String)) | (✔) |
| [Review Rating Style](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRatingStyle(int)) | (✔) |
| [Short Description](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDescription(java.lang.String)) | (✔) |
| [Starting Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartingPrice(java.lang.String)) | (✔) |
| [Thumbnail URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailUri(android.net.Uri)) | (✔) |
| [Thumbnail Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailAspectRatio(int)) | (✔) |
| [Title](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setTitle(java.lang.String)) | ✔ |
| [Video Height](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoHeight(int)) | (✔) |
| [Video Width](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoWidth(int)) | (✔) |
| [Weight](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setWeight(int)) | (✔) |

[Previous

arrow\_back

Audio program attributes](/training/tv/discovery/audio-programs)

[Next

Add programs

arrow\_forward](/training/tv/discovery/watch-next-add-programs)