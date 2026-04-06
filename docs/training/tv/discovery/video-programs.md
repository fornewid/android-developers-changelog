---
title: Video program attributes  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/video-programs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Video program attributes Stay organized with collections Save and categorize content based on your preferences.




A video program's attributes depend on the type of its content. The program type
tells the system what metadata to expect so that the UI can be filled in
appropriately.

Video programs can be one of the following types:

* [`TYPE_MOVIE`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_MOVIE())
* [`TYPE_TV_SERIES`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_TV_SERIES())
* [`TYPE_TV_SEASON`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_TV_SEASON())
* [`TYPE_TV_EPISODE`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_TV_EPISODE())
* [`TYPE_CLIP`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_CLIP())
* [`TYPE_EVENT`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_EVENT())
* [`TYPE_CHANNEL`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_CHANNEL())

Use [`PreviewProgram.Builder`](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder) to build a program. You can read more about possible values for each field in the reference docs for each setter on the builder.

### Kotlin

```
val program = PreviewProgram.Builder()
        .setChannelId(channelId)
        .setTitle(clip.getTitle())
        .setDescription(clip.getDescription())
        .setType(TvContractCompat.PreviewPrograms.TYPE_MOVIE)
        // Set required attributes
        .build()
```

### Java

```
PreviewProgram program = new PreviewProgram.Builder()
        .setChannelId(channelId)
        .setTitle(clip.getTitle())
        .setDescription(clip.getDescription())
        .setType(TvContractCompat.PreviewPrograms.TYPE_MOVIE)
        // Set required attributes
        .build();
```

The following table shows the attributes that can be assigned to each type of
video program. Each attribute links to the corresponding setter in
[`PreviewProgram.Builder`](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder).
Attributes marked ✔ are required; those marked (✔) are optional.

| Attribute | Movie | TV Series | TV Season | TV Episode | Clip | Event | Channel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Author](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAuthor(java.lang.String)) |  |  |  |  | (✔) |  |  |
| [Availability](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAvailability(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Canonical Genres](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setCanonicalGenres(java.lang.String[])) | (✔) | (✔) | (✔) | (✔) |  |  |  |
| [Channel ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setChannelId(long)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Content ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String)) |  |  |  |  | (✔) |  |  |
| [Content Ratings](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentRatings(android.media.tv.TvContentRating[])) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [DurationMillis](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDurationMillis(int)) | ✔ |  |  | ✔ | ✔ | (✔) |  |
| [Episode Number](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setEpisodeNumber(int)) |  |  |  | ✔ |  |  |  |
| [Episode Title](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setEpisodeTitle(java.lang.String)) |  |  |  | (✔) |  |  |  |
| [Genre](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setGenre(java.lang.String)) | (✔) | (✔) | (✔) | (✔) |  |  |  |
| [Intent URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setIntentUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Interaction Count](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionCount(long)) |  |  |  |  | (✔) | (✔) |  |
| [Interaction Type](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionType(int)) |  |  |  |  | (✔) | (✔) |  |
| [Internal Provider ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInternalProviderId(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Item Count](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setItemCount(int)) |  | (✔) | (✔) |  |  |  |  |
| [Live](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLive(boolean)) | (✔) |  |  | (✔) | (✔) | (✔) | (✔) |
| [Logo URI (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Logo Content Description (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoContentDescription(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Offer Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setOfferPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) || [Poster Art Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtAspectRatio(int)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Poster Art URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

| [Preview Video URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewVideoUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Release Date](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReleaseDate(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |  |
| [Review Rating](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRating(java.lang.String)) | (✔) | (✔) | (✔) | (✔) |  |  | (✔) |
| [Review Rating Style](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRatingStyle(int)) | (✔) | (✔) | (✔) | (✔) |  |  | (✔) |
| [Season Display Number](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setSeasonNumber(int)) |  |  | ✔ | ✔ |  |  |  |
| [Short Description](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDescription(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Start Time UTC Millis (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartTimeUtcMillis(long)) | ✔ |  |  | ✔ | ✔ | ✔ |  |
| [End Time UTC Millis (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setEndTimeUtcMillis(long)) | ✔ |  |  | ✔ | ✔ | ✔ |  |
| [Starting Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartingPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailAspectRatio(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Title](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setTitle(java.lang.String)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Video Height](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoHeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Video Width](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoWidth(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Weight](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setWeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |

**(\*) Note:** `LOGO_CONTENT_DESCRIPTION` is required when
`LOGO_URI` is used. `START` and `END` times
only appear on the screen when the `LIVE` attribute is `true`.  

##### Preview images

The recommended sizes for preview images are as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| **Attribute** | **Aspect Ratio** | **Width** | **Height** |
| `ASPECT_RATIO_16_9` | 16:9 | 272 dp | 153 dp |
| `ASPECT_RATIO_3_2` | 3:2 | 229.5 dp | 153 dp |
| `ASPECT_RATIO_4_3` | 4:3 | 204 dp | 153 dp |
| `ASPECT_RATIO_1_1` | 1:1 | 153 dp | 153 dp |
| `ASPECT_RATIO_2_3` | 2:3 | 102 dp | 153 dp |
| `ASPECT_RATIO_MOVIE_POSTER` | 1:1.441 | 106 dp | 153 dp |

For best quality, use 16:9 or 4:3 preview videos that are at least the sizes
specified in this table. Use an opaque logo for the best user experience.

You can specify the exact preview video sizes using `VIDEO_WIDTH`
and `VIDEO_HEIGHT`.

[Previous

arrow\_back

Channels on the home screen](/training/tv/discovery/recommendations-channel)

[Next

Audio program attributes

arrow\_forward](/training/tv/discovery/audio-programs)