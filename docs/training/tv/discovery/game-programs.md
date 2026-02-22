---
title: https://developer.android.com/training/tv/discovery/game-programs
url: https://developer.android.com/training/tv/discovery/game-programs
source: md.txt
---

# Game program attributes

All game programs have the type attribute[`TYPE_GAME`](https://developer.android.com/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#TYPE_GAME()).

The following table shows the attributes that can be assigned to a game program, each linked to the corresponding setter in[`PreviewProgram.Builder`](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder). Attributes marked✔are required; those marked(✔)are optional.

|                                                                          Attribute                                                                          | Required or Optional |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| [Author](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAuthor(java.lang.String))                           | (✔)                  |
| [Availability](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setAvailability(int))                            | (✔)                  |
| [Channel ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setChannelId(long))                                | ✔                    |
| [Content ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setContentId(java.lang.String))                    | (✔)                  |
| [Genre](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setGenre(java.lang.String))                             | (✔)                  |
| [Intent URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setIntentUri(android.net.Uri))                     | ✔                    |
| [Internal Provider ID](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setInternalProviderId(java.lang.String)) | (✔)                  |
| [Offer Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setOfferPrice(java.lang.String))                  | (✔)                  |
| [Poster Art Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtAspectRatio(int))         | ✔                    |
| [Poster Art URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPosterArtUri(android.net.Uri))              | ✔                    |
| [Preview Video URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setPreviewVideoUri(android.net.Uri))        | (✔)                  |
| [Release Date](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReleaseDate(java.lang.String))                | (✔)                  |
| [Review Rating](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRating(java.lang.String))              | (✔)                  |
| [Review Rating Style](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setReviewRatingStyle(int))                | (✔)                  |
| [Short Description](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setDescription(java.lang.String))           | (✔)                  |
| [Starting Price](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setStartingPrice(java.lang.String))            | (✔)                  |
| [Thumbnail URI](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailUri(android.net.Uri))               | (✔)                  |
| [Thumbnail Aspect Ratio](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setThumbnailAspectRatio(int))          | (✔)                  |
| [Title](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setTitle(java.lang.String))                             | ✔                    |
| [Video Height](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoHeight(int))                             | (✔)                  |
| [Video Width](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setVideoWidth(int))                               | (✔)                  |
| [Weight](https://developer.android.com/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setWeight(int))                                        | (✔)                  |