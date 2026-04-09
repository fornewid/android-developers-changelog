---
title: Audio program attributes  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/audio-programs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Audio program attributes Stay organized with collections Save and categorize content based on your preferences.




Attributes for audio programs depend on the type of the content. The program
type tells the system what metadata to expect so that the UI can be filled in
appropriately. Audio programs can be one of these types:

* [`TYPE_TRACK`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_TRACK())
* [`TYPE_ALBUM`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_ALBUM())
* [`TYPE_ARTIST`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_ARTIST())
* [`TYPE_PLAYLIST`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_PLAYLIST())
* [`TYPE_STATION`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_STATION())

Use [`PreviewProgram.Builder`](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder)
to build a program. You can read more about possible values for each field in
the Java documentation for each setter on the builder.

The following example shows how to use `PreviewProgram.Builder`:

```
PreviewProgram program = new PreviewProgram.Builder()
                    .setChannelId(channelId)
                    .setTitle(clip.getTitle())
                    .setDescription(clip.getDescription())
                    .setType(TvContractCompat.PreviewPrograms.TYPE_ALBUM)
                    // Set required attributes
                    .build();
```

The following table shows the attributes that can be assigned to each type of
audio program, and links to the corresponding setter in
`PreviewProgram.Builder`. Attributes marked ✔ are required; those marked (✔) are optional.

| Attribute | Track | Album | Artist | Playlist | Station |
| --- | --- | --- | --- | --- | --- |
| [Author](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAuthor(java.lang.String)) | (✔) | (✔) |  | (✔) |  |
| [Availability](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAvailability(int)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Channel ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setChannelId(long)) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Content ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Duration](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDurationMillis(int)) | ✔ |  |  |  |  |
| [Genre](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setGenre(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Intent URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setIntentUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Interaction Count](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionCount(long)) |  |  | (✔) | (✔) | (✔) |
| [Interaction Type](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionType(int)) |  |  | (✔) | (✔) | (✔) |
| [Internal Provider ID](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInternalProviderId(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Live](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLive(boolean)) |  |  |  |  | (✔) |
| [Logo URI (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoUri(android.net.Uri)) |  |  |  | (✔) |  |
| [Logo Content Description (\*)](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoContentDescription(java.lang.String)) |  |  |  | (✔) |  |
| [Offer Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setOfferPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Poster Art Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtAspectRatio(int)) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Poster Art URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtUri(android.net.Uri)) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Preview Audio URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewAudioUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Preview Video URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewVideoUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Release Date](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReleaseDate(java.lang.String)) | (✔) | (✔) |  |  |  |
| [Short Description](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDescription(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Starting Price](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartingPrice(java.lang.String)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail Aspect Ratio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailAspectRatio(int)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Thumbnail URI](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailUri(android.net.Uri)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Title](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setTitle(java.lang.String)) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Video Height](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoHeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Video Width](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoWidth(int)) | (✔) | (✔) | (✔) | (✔) | (✔) |
| [Weight](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setWeight(int)) | (✔) | (✔) | (✔) | (✔) | (✔) |

**(\*) Notes:** LOGO\_CONTENT\_DESCRIPTION is required when LOGO\_URI is used.

[Previous

arrow\_back

Video program attributes](/training/tv/discovery/video-programs)

[Next

Game program attributes

arrow\_forward](/training/tv/discovery/game-programs)