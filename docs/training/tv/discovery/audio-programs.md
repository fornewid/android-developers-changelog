---
title: https://developer.android.com/training/tv/discovery/audio-programs
url: https://developer.android.com/training/tv/discovery/audio-programs
source: md.txt
---

# Audio program attributes

Attributes for audio programs depend on the type of the content. The program type tells the system what metadata to expect so that the UI can be filled in appropriately. Audio programs can be one of these types:

- [`TYPE_TRACK`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_TRACK())
- [`TYPE_ALBUM`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_ALBUM())
- [`TYPE_ARTIST`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_ARTIST())
- [`TYPE_PLAYLIST`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_PLAYLIST())
- [`TYPE_STATION`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_STATION())

Use[`PreviewProgram.Builder`](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder)to build a program. You can read more about possible values for each field in the Java documentation for each setter on the builder.

The following example shows how to use`PreviewProgram.Builder`:  

    PreviewProgram program = new PreviewProgram.Builder()
                        .setChannelId(channelId)
                        .setTitle(clip.getTitle())
                        .setDescription(clip.getDescription())
                        .setType(TvContractCompat.PreviewPrograms.TYPE_ALBUM)
                        // Set required attributes
                        .build();

The following table shows the attributes that can be assigned to each type of audio program, and links to the corresponding setter in`PreviewProgram.Builder`. Attributes marked✔are required; those marked(✔)are optional.

|                                                                                Attribute                                                                                 | Track | Album | Artist | Playlist | Station |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|--------|----------|---------|
| [Author](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAuthor(java.lang.String))                                        | (✔)   | (✔)   |        | (✔)      |         |
| [Availability](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAvailability(int))                                         | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Channel ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setChannelId(long))                                             | ✔     | ✔     | ✔      | ✔        | ✔       |
| [Content ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String))                                 | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Duration](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDurationMillis(int))                                           | ✔     |       |        |          |         |
| [Genre](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setGenre(java.lang.String))                                          | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Intent URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setIntentUri(android.net.Uri))                                  | ✔     | ✔     | ✔      | ✔        | ✔       |
| [Interaction Count](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionCount(long))                               |       |       | (✔)    | (✔)      | (✔)     |
| [Interaction Type](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInteractionType(int))                                  |       |       | (✔)    | (✔)      | (✔)     |
| [Internal Provider ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInternalProviderId(java.lang.String))              | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Live](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLive(boolean))                                                     |       |       |        |          | (✔)     |
| [Logo URI (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoUri(android.net.Uri))                                 |       |       |        | (✔)      |         |
| [Logo Content Description (\*)](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setLogoContentDescription(java.lang.String)) |       |       |        | (✔)      |         |
| [Offer Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setOfferPrice(java.lang.String))                               | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Poster Art Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtAspectRatio(int))                      | ✔     | ✔     | ✔      | ✔        | ✔       |
| [Poster Art URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtUri(android.net.Uri))                           | ✔     | ✔     | ✔      | ✔        | ✔       |
| [Preview Audio URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewAudioUri(android.net.Uri))                     | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Preview Video URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewVideoUri(android.net.Uri))                     | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Release Date](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReleaseDate(java.lang.String))                             | (✔)   | (✔)   |        |          |         |
| [Short Description](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDescription(java.lang.String))                        | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Starting Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartingPrice(java.lang.String))                         | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Thumbnail Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailAspectRatio(int))                       | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Thumbnail URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailUri(android.net.Uri))                            | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Title](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setTitle(java.lang.String))                                          | ✔     | ✔     | ✔      | ✔        | ✔       |
| [Video Height](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoHeight(int))                                          | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Video Width](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoWidth(int))                                            | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |
| [Weight](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setWeight(int))                                                     | (✔)   | (✔)   | (✔)    | (✔)      | (✔)     |

| **(\*) Notes:**LOGO_CONTENT_DESCRIPTION is required when LOGO_URI is used.