---
title: https://developer.android.com/guide/playcore/engage/tv/fc-automation
url: https://developer.android.com/guide/playcore/engage/tv/fc-automation
source: md.txt
---

This guide describes the data model and integration steps for publishing video
and live TV content using the Engage SDK.

## `MovieEntity` data model

The `MovieEntity` represents a full-length film. The following table summarizes
the key fields.

| Public Methods | Type | Requirement | Description |
|---|---|---|---|
| [`getName()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getName()) | String | Required | The title of the movie (e.g., "Avengers: Endgame") |
| [`getDescription()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getDescription()) | String | Required | A summary providing context that appears on hover |
| [`getPosterImages()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getPosterImages()) | List\<Image\> | Required | A list of images used for the movie's poster display |
| [`getPlatformSpecificPlaybackUris()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getPlatformSpecificPlaybackUris()) | List\<PlatformSpecificUri\> | Required | Deep links for playback on specific platforms |
| [`getDurationMillis()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getDurationMillis()) | Long | Required | The total duration of the movie in milliseconds |
| `getCallToAction` | String | Required (GTV) | Text displayed to prompt user interaction (e.g., "Watch Now") |
| `getTags` | List\<String\> | Optional | Keywords used for categorization (e.g., "Action/Thriller") |

## `LiveTvProgramEntity` data model

The `LiveTvProgramEntity` represents a program airing or scheduled to air on a specific channel.

| Public Methods | Type | Requirement | Description |
|---|---|---|---|
| [`getName()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getName()) | String | Required | The title of the program (e.g., "NBC CT Late News") |
| [`getDescription()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getDescription()) | String | Required | A summary providing context about the program |
| [`getPosterImages()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getPosterImages()) | List\<Image\> | Required | Images used for the program's display |
| [`getAvailabilityTimeWindows()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getAvailabilityTimeWindows()) | List\<DisplayTimeWindow\> | Required | The scheduled time windows for the program |
| [`getChannelId()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelId()) | String | Required | Unique identifier for the TV channel |
| [`getChannelName()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelName()) | String | Required | Name of the TV channel |
| [`getChannelLogoImage()`](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelLogoImage()) | Image | Required | Logo image for the TV channel |
| `getCallToAction()` | String | Required (GTV) | Interaction prompt text |
| `getTags()` | List\<String\> | Optional | Keywords used for categorization |

> [!NOTE]
> **Note:** These public methods (e.g., `setCallToAction()`, `addTag()`, `addBadge()`) are also available for other video entities, such as `TvShowEntity`, `TvEpisodeEntity`, and `TvSeasonEntity`.

## Builder usage examples

### `MovieEntity` example

See [MovieEntity.Builder](https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity.Builder).

    MovieEntity movie = new MovieEntity.Builder()
        .setName("La hora 25")
        .setDescription("Brogan tiene 24 horas para revalorar su vida antes de ser encarcelado")
        .addPosterImage(new Image.Builder()
            .setImageUri(Uri.parse("https://www.example.com/movie_poster.png"))
            .build())
        .addPlatformSpecificPlaybackUri(new PlatformSpecificUri.Builder()
            .setUri("https://www.example.com")
            .setPlatformType(PlatformType.TYPE_TV)
            .build())
        .setDurationMillis(7200000L)
        .setCallToAction("Watch Now")
        .addTag("Action/Thriller")
        .build();

### `LiveTvProgramEntity` example

See [LiveTvProgramEntity.Builder](https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity.Builder).

    LiveTvProgramEntity liveProgram = new LiveTvProgramEntity.Builder()
        .setName("3:30AM: NBC CT Late News")
        .setDescription("The latest local news, weather and investigative stories.")
        .setChannelId("https://www.example.com")
        .setChannelName("Tastemade")
        .setChannelLogoImage(new Image.Builder()
            .setImageUri(Uri.parse("https://example.com/v1/channels/logo.png"))
            .build())
        .addAvailabilityTimeWindow(new DisplayTimeWindow.Builder()
            .setStartTimestampMillis(1756713600000L)
            .setEndTimestampMillis(1756715400000L)
            .build())
        .addPosterImage(new Image.Builder()
            .setImageUri(Uri.parse("https://example.com/v1/assets/image.jpg"))
            .build())
        .setCallToAction("Watch Now")
        .addTag("News")
        .build();

## API

`publishRecommendationClusters()` will be used to send candidate content to the Feature Carousel. Cluster
type should be set as `RecommendationClusterType.TYPE_PROVIDER_ROW`.

> [!NOTE]
> **Note:** Make sure that candidate content for the Feature Carousel is sent in every `publishRecommendationClusters()` call or else it will be overwritten.

## Engage SDK version

Note the minimum Engage SDK version required for this integration:

    engage-tv: 1.0.6