---
title: https://developer.android.com/training/tv/discovery/video-programs
url: https://developer.android.com/training/tv/discovery/video-programs
source: md.txt
---

> Documentation index: https://developer.android.com/training/tv/discovery/llms.txt

A video program's attributes depend on the type of its content. The program type
tells the system what metadata to expect so that the UI can be filled in
appropriately.

Video programs can be one of the following types:

- [`TYPE_MOVIE`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_MOVIE)
- [`TYPE_TV_SERIES`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_TV_SERIES)
- [`TYPE_TV_SEASON`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_TV_SEASON)
- [`TYPE_TV_EPISODE`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_TV_EPISODE)
- [`TYPE_CLIP`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_CLIP)
- [`TYPE_EVENT`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_EVENT)
- [`TYPE_CHANNEL`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms.md.txt#TYPE_CHANNEL)

Use [`PreviewProgram.Builder`](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt) to build a program. You can read more about
possible values for each field in the reference docs for each setter on the
builder.


```kotlin
val program = PreviewProgram.Builder()
    .setChannelId(channelId)
    .setTitle(clip.getTitle())
    .setDescription(clip.getDescription())
    .setType(TvContractCompat.PreviewPrograms.TYPE_MOVIE)
    // Set required attributes.
    .build()
```

<br />


The following table shows the attributes that can be assigned to each type of
video program. Each attribute links to the corresponding setter in
[`PreviewProgram.Builder`](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt).
Attributes marked ✔ are required; those marked (✔) are optional.

| Attribute | Movie | TV Series | TV Season | TV Episode | Clip | Event | Channel |
|---|---|---|---|---|---|---|---|
| [Author](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setAuthor(java.lang.String)) |   |   |   |   | (✔) |   |   |
| [Availability](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setAvailability(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Canonical Genres](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setCanonicalGenres(java.lang.String[])) | (✔) | (✔) | (✔) | (✔) |   |   |   |
| [Channel ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setChannelId(long)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Content ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setContentId(java.lang.String)) |   |   |   |   | (✔) |   |   |
| [Content Ratings](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setContentRatings(android.media.tv.TvContentRating[])) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [DurationMillis](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setDurationMillis(int)) | ✔ |   |   | ✔ | ✔ | (✔) |   |
| [Episode Number](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setEpisodeNumber(int)) |   |   |   | ✔ |   |   |   |
| [Episode Title](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setEpisodeTitle(java.lang.String)) |   |   |   | (✔) |   |   |   |
| [Genre](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setGenre(java.lang.String)) | (✔) | (✔) | (✔) | (✔) |   |   |   |
| [Intent URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setIntentUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Interaction Count](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setInteractionCount(long)) |   |   |   |   | (✔) | (✔) |   |
| [Interaction Type](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setInteractionType(int)) |   |   |   |   | (✔) | (✔) |   |
| [Internal Provider ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setInternalProviderId(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Item Count](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setItemCount(int)) |   | (✔) | (✔) |   |   |   |   |
| [Live](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setLive(boolean)) | (✔) |   |   | (✔) | (✔) | (✔) | (✔) |
| [Logo URI (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setLogoUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Logo Content Description (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setLogoContentDescription(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Offer Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setOfferPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Poster Art Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setPosterArtAspectRatio(int)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Poster Art URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setPosterArtUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Preview Video URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setPreviewVideoUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Release Date](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setReleaseDate(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |   |
| [Review Rating](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setReviewRating(java.lang.String)) | (✔) | (✔) | (✔) | (✔) |   |   | (✔) |
| [Review Rating Style](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setReviewRatingStyle(int)) | (✔) | (✔) | (✔) | (✔) |   |   | (✔) |
| [Season Display Number](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setSeasonNumber(int)) |   |   | ✔ | ✔ |   |   |   |
| [Short Description](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setDescription(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Start Time UTC Millis (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setStartTimeUtcMillis(long)) | ✔ |   |   | ✔ | ✔ | ✔ |   |
| [End Time UTC Millis (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setEndTimeUtcMillis(long)) | ✔ |   |   | ✔ | ✔ | ✔ |   |
| [Starting Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setStartingPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setThumbnailAspectRatio(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setThumbnailUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Title](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setTitle(java.lang.String)) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Video Height](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setVideoHeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Video Width](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setVideoWidth(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Weight](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder.md.txt#setWeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) | (✔) |

> [!NOTE]
> **Note:** (\*) `LOGO_CONTENT_DESCRIPTION` is required when `LOGO_URI` is used. `START` and `END` times only appear on the screen when the `LIVE` attribute is `true`.

##### Preview images

The recommended sizes for preview images are as follows:

|---|---|---|---|
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