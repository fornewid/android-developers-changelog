---
title: https://developer.android.com/guide/playcore/engage/tv/recommendations/rest
url: https://developer.android.com/guide/playcore/engage/tv/recommendations/rest
source: md.txt
---

> Documentation index: https://developer.android.com/guide/playcore/engage/tv/recommendations/llms.txt

The Google TV Video Discovery REST API lets partners send non-personalized
recommendation candidates to Google TV and Android TV devices from their
backend servers. Sending candidates from their backend keeps a partner's
catalog and live programming recommendations fresh on these devices without
requiring users to open the partner's app.

Partners send candidates to recommendations feeds. Google creates each feed for
the partner and configures the countries or regions and the TV device languages
that the feed is shown to. A feed can contain movies, TV shows, and live TV
programs.

If you want to publish personalized recommendations from the user's device, see
[Integrate recommendations on-device using Engage
SDK](https://developer.android.com/guide/playcore/engage/tv/recommendations).

> [!NOTE]
> **Note:** In the REST API, a **recommendation candidate** takes the place of an on-device Engage SDK entity (`MovieEntity`, `TvShowEntity`, or `LiveTvProgramEntity`). On the device, your app publishes entities for the signed-in user. With the REST API, your backend server sends candidates to a recommendations feed, and Google TV and Android TV devices can show them to any user in that feed's audience.

## Prerequisites

Before integrating with the REST API, make sure you have the following:

- A Google Cloud project to make API requests from.
- A Google Workspace account associated with your organization.
- Your partner ID and recommendations feed IDs, provided by your Google TV partner representative during onboarding. See [Recommendations feeds](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#feeds) for how these IDs are used.

## Gain access

Access to the Google TV Video Discovery REST API is restricted to registered
Google TV media partners. Each caller is authenticated using a Google Cloud
service account that is mapped on the server to exactly one partner ID.

To request and configure API access, follow these steps:

1. **Create a Google Workspace account** . Follow the instructions on the [Google Workspace support page](https://support.google.com/a/answer/53926) to set up an account for your organization.
2. **Locate your Google Workspace Customer ID** . Find your Customer ID (for example, `C0123abcd`) by following the steps in [Find your customer ID](https://support.google.com/a/answer/10070793).
3. **Create a Google Cloud project and service account** . In the Google Cloud Console under your Google Workspace organization, create a Google Cloud project and a [service account](https://cloud.google.com/iam/docs/service-accounts-create) for your backend server.
4. **Request partner onboarding** . Provide your **Google Workspace Customer
   ID** , **Google Cloud Project ID** , and **service account email address** (or unique numeric ID) to your Google TV partner representative, together with the countries or regions and TV device languages you want to send candidates to. Your Google TV partner representative notifies you after mapping your Google Workspace organization, project, and service account to your partner ID, and gives you the recommendations feed IDs created for your partner.
5. **Enable the API and generate credentials** . After your representative confirms access is granted, enable the Google TV Video Discovery API (`tvvideodiscovery.googleapis.com`) in your Google Cloud project and generate OAuth 2.0 credentials for your service account.
6. **Authenticate your requests** . Request OAuth 2.0 access tokens using the
   following OAuth scope and pass the token in the `Authorization: Bearer` HTTP
   header on every call:

       https://www.googleapis.com/auth/tvvideodiscovery

## Rate limits

Requests to `replaceCandidates` are subject to the following per-project rate
limits and per-request payload caps:

| Limit | Value |
|---|---|
| Requests per minute per Google Cloud project | 5 |
| Requests per day per Google Cloud project | 100 |
| `RecommendationCandidate` items per request | 1 to 25 |

Requests to a staging feed count against the same quota as requests to the
corresponding production feed.

## Recommendations feeds

The API organizes recommendation candidates into recommendations feeds. A feed
is identified by a resource name with the following format:

    partners/{partner}/recommendationsFeeds/{recommendationsFeed}

### Partners

`{partner}` is the partner ID that Google assigns to you during onboarding. The
service account that you authenticate with is mapped to exactly one partner ID.
Requests that name any other partner fail with `403 PERMISSION_DENIED`.

### Feed IDs

`{recommendationsFeed}` is a feed ID that Google creates for you during
onboarding. You can't create feeds with the API.

Each feed targets an audience that Google configures when it creates the feed:

- **Countries or regions**: where the feed's candidates are shown.
- **TV device languages** : the languages that the targeted users have set on their TV device. This isn't the language of the text that you send. To provide text in more than one language, see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string).

Google decides where a feed's candidates appear on Google TV and Android TV
devices. You send candidates to every feed in the same way.

### Staging feeds

Each feed has a matching staging feed named `{recommendationsFeed}-staging`. A
staging feed is served only to test accounts on an allowlist. Use it to
validate your integration before you send candidates to the production feed.

Staging feeds use the same endpoint, credentials, request validation, and quota
as production feeds. Only the audience differs.

### Replacement

The feed is the unit of replacement. Each `replaceCandidates` call replaces all
candidates previously stored for that feed and leaves every other feed
untouched.

## Replace recommendation candidates

Use the `partners.recommendationsFeeds.replaceCandidates` method to send the
complete list of recommendation candidates for one feed.

### HTTP request

    POST https://tvvideodiscovery.googleapis.com/v1/{name=partners/*/recommendationsFeeds/*}:replaceCandidates

The URL path contains the resource name of the feed whose candidates are
replaced. The request body contains every field that isn't part of the URL path.

### Path parameters

| Parameter | Description |
|---|---|
| `name` | Required. The resource name of the feed, in the format `partners/{partner}/recommendationsFeeds/{recommendationsFeed}`. `{partner}` must be the partner ID that your service account is mapped to. `{recommendationsFeed}` must be a feed ID that Google created for that partner, or that feed ID with the `-staging` suffix. |

### `ReplaceCandidatesRequest`

The JSON request body has the following structure:

| Field | Type | Required | Description |
|---|---|---|---|
| `recommendation_candidates` | `array of RecommendationCandidate` | Yes | A list of 1 to 25 [`RecommendationCandidate`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#recommendation-candidate) items. These candidates replace the feed's current candidates. |

## Candidate schemas

Each item in `recommendation_candidates` is a `RecommendationCandidate` object
that contains one candidate-type payload, optional recommendation reasons, and
optional display availability windows.

### `RecommendationCandidate`

A `RecommendationCandidate` object contains exactly one media-type payload
field, optional recommendation reasons, and optional availability intervals.

#### Union field `candidate_type`

`candidate_type` is required: set exactly one of the following fields. The
fields are mutually exclusive, and a candidate that sets none or more than one
is rejected. There is no `candidate_type` key in the JSON; set the chosen field
directly on the `RecommendationCandidate` object.

| Field | Type | Description |
|---|---|---|
| `movie_candidate` | `MovieCandidate` | An on-demand movie (see [`MovieCandidate`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#movie-candidate)). |
| `tv_show_candidate` | `TvShowCandidate` | A TV show at the show level (see [`TvShowCandidate`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#tv-show-candidate)). |
| `live_tv_program_candidate` | `LiveTvProgramCandidate` | A scheduled live TV broadcast or streamed event (see [`LiveTvProgramCandidate`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#live-tv-program-candidate)). |

#### Context and availability

Both fields are optional:

| Field | Type | Required | Description |
|---|---|---|---|
| `recommendation_contexts` | `array of RecommendationContext` | No | Why the candidate is recommended, and for how long each reason applies (see [`RecommendationContext`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#recommendation-context)). |
| `availability_intervals` | `array of Interval` | No | Time windows during which the candidate may be shown (see [`Interval`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#interval)). Each window starts at its `start_time` (inclusive) and ends at its `end_time` (exclusive). If unset, the candidate is eligible for as long as it is stored. A candidate whose windows are all in the past is never shown. |

### `MovieCandidate`

The `MovieCandidate` object represents an on-demand movie:

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | `LocalizedString` | Yes | Title of the movie (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 100 Unicode code points and is shown as sent. |
| `description` | `LocalizedString` | Yes | Short description of the movie (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 400 Unicode code points. |
| `localized_media_images` | `array of LocalizedMediaImage` | Yes | 16:9 artwork images, one entry per language (see [`LocalizedMediaImage`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-media-image)). Must contain at least one image. Provide the largest source available; 1920x1080 pixels is recommended. |
| `localized_provider_playback_uris` | `array of LocalizedProviderPlaybackUri` | Yes | Deep links per platform and per language (see [`LocalizedProviderPlaybackUri`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-provider-playback-uri)). At least one entry must list `PLATFORM_ANDROID_TV`. |
| `release_date` | `Date` | Yes | Release date of the movie (see [`Date`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#date)). |
| `external_entity_ids` | `array of ExternalEntityId` | No | External catalog identifiers for entity matching (see [`ExternalEntityId`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#external-entity-id)). At most one entry per identifier type. |
| `duration` | `string` (`Duration`) | No | How long the movie lasts (see [`Duration`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#duration)). For example, `"7200s"` for 2 hours. |
| `content_ratings` | `array of ContentRating` | No | Official content ratings (see [`ContentRating`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#content-rating)). |

### `TvShowCandidate`

The `TvShowCandidate` object represents a TV show at the show level. Google TV
and Android TV devices show a card for the show; use the deep link to decide
whether playback starts on the show page or on a specific episode.

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | `LocalizedString` | Yes | Title of the TV show (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 100 Unicode code points and is shown as sent. |
| `description` | `LocalizedString` | Yes | Short description of the TV show (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 400 Unicode code points. |
| `localized_media_images` | `array of LocalizedMediaImage` | Yes | 16:9 artwork images, one entry per language (see [`LocalizedMediaImage`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-media-image)). Must contain at least one image. Provide the largest source available; 1920x1080 pixels is recommended. |
| `localized_provider_playback_uris` | `array of LocalizedProviderPlaybackUri` | Yes | Deep links per platform and per language (see [`LocalizedProviderPlaybackUri`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-provider-playback-uri)). At least one entry must list `PLATFORM_ANDROID_TV`. The `uri` can point to the show page or to an episode. |
| `first_episode_air_date` | `Date` | Yes | Air date of the first episode (see [`Date`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#date)). |
| `external_entity_ids` | `array of ExternalEntityId` | No | External catalog identifiers for entity matching (see [`ExternalEntityId`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#external-entity-id)). At most one entry per identifier type. |
| `season_count` | `integer` (int32) | No | Number of seasons available on your service. |
| `content_ratings` | `array of ContentRating` | No | Official content ratings (see [`ContentRating`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#content-rating)). |

### `LiveTvProgramCandidate`

The `LiveTvProgramCandidate` object represents a scheduled live TV broadcast or
streamed event. The broadcast window is part of the candidate and is separate
from the parent candidate's `availability_intervals`, which control when the
card may be shown.

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | `LocalizedString` | Yes | Title of the live TV program (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 100 Unicode code points and is shown as sent. |
| `description` | `LocalizedString` | Yes | Short description of the live TV program (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 400 Unicode code points. |
| `localized_media_images` | `array of LocalizedMediaImage` | Yes | 16:9 artwork images, one entry per language (see [`LocalizedMediaImage`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-media-image)). Must contain at least one image. Provide the largest source available; 1920x1080 pixels is recommended. |
| `localized_provider_playback_uris` | `array of LocalizedProviderPlaybackUri` | Yes | Deep links per platform and per language (see [`LocalizedProviderPlaybackUri`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-provider-playback-uri)). At least one entry must list `PLATFORM_ANDROID_TV`. |
| `broadcast_interval` | `Interval` | Yes | Broadcast start and end of the program (see [`Interval`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#interval)). Both `start_time` and `end_time` are required. |
| `external_entity_ids` | `array of ExternalEntityId` | No | External catalog identifiers for entity matching (see [`ExternalEntityId`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#external-entity-id)). At most one entry per identifier type. |
| `content_ratings` | `array of ContentRating` | No | Official content ratings (see [`ContentRating`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#content-rating)). |

## Supporting schemas

The candidate payloads reference the following shared objects for localized
text, deep links, artwork, external identifiers, recommendation reasons,
display intervals, content ratings, and well-known date and time types.

### `LocalizedString`

The `LocalizedString` object carries the same text in one or more languages.
Each value is tagged with its language so that Google TV and Android TV
devices can show the text that matches the user's TV device language:

| Field | Type | Required | Description |
|---|---|---|---|
| `values` | `array of LocalizedText` | Yes | The text in each language that you provide (see [`LocalizedText`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-text)). Must contain at least one value. |

### `LocalizedText`

The `LocalizedText` object is text in a single language:

| Field | Type | Required | Description |
|---|---|---|---|
| `text` | `string` | Yes | The text in the language given by `language_code`. |
| `language_code` | `string` | Yes | BCP-47 language code of `text`, such as `"en-US"` or `"sr-Latn"`. |

### `LocalizedMediaImage`

The `LocalizedMediaImage` object pairs an image with the language of any text
in the image:

| Field | Type | Required | Description |
|---|---|---|---|
| `language_code` | `string` | Yes | BCP-47 language code of the text in the image, such as `"en-US"` or `"sr-Latn"`. |
| `image` | `MediaImage` | Yes | A 16:9 image (see [`MediaImage`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#media-image)). Provide the largest source available; 1920x1080 pixels is recommended. |

### `LocalizedProviderPlaybackUri`

The `LocalizedProviderPlaybackUri` object pairs a deep link with the language
of the content it opens and the app that opens it:

| Field | Type | Required | Description |
|---|---|---|---|
| `playback_uri` | `PlaybackUri` | Yes | The deep link and the platforms it applies to (see [`PlaybackUri`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#playback-uri)). |
| `language_code` | `string` | Yes | BCP-47 language code of the content that the deep link opens, such as `"en-US"` or `"sr-Latn"`. |
| `package_name` | `string` | Yes | Android application package name used to open the deep link (for example, `"com.example.tvapp"`). |

### `PlaybackUri`

The `PlaybackUri` object defines a deep link and its target platforms:

| Field | Type | Required | Description |
|---|---|---|---|
| `uri` | `string` | Yes | Deep link URI that starts playback of the candidate in your app. |
| `platforms` | `array of string (enum)` | Yes | Platforms that this deep link applies to. Allowed values: `PLATFORM_UNSPECIFIED`, `PLATFORM_ANDROID_TV`, `PLATFORM_ANDROID`, `PLATFORM_IOS`. Include `PLATFORM_ANDROID_TV` for Google TV and Android TV devices. |

### `MediaImage`

The `MediaImage` object specifies an image URL, its pixel dimensions, and
accessibility text:

| Field | Type | Required | Description |
|---|---|---|---|
| `url` | `string` | Yes | Publicly accessible HTTPS URL of the image. |
| `width` | `integer` | Yes | Unmodified (maximum) image width in pixels. |
| `height` | `integer` | Yes | Unmodified (maximum) image height in pixels. |
| `accessibility_text` | `string` | Yes | Accessibility (alt) text describing the image. |

### `ExternalEntityId`

The `ExternalEntityId` object maps a candidate to an identifier in an external
catalog. Set exactly one of the following fields per entry, and include at most
one entry per identifier type in a candidate's `external_entity_ids` list:

| Field | Type | Required | Description |
|---|---|---|---|
| `tms_root_id` | `string` | One of | Gracenote TMS root ID. Identifies a title: a movie, a show, or an episode. |
| `tms_id` | `string` | One of | Gracenote TMS variant ID. Identifies an edition or a broadcast listing. |
| `data_feed_element_id` | `string` | One of | Entity ID from your Media Actions data feed. This value is unrelated to the `{recommendationsFeed}` segment of the resource name. |

### `RecommendationContext`

The `RecommendationContext` object explains why a candidate is recommended and
for how long that explanation applies:

| Field | Type | Required | Description |
|---|---|---|---|
| `recommendation_reason` | `RecommendationReason` | No | Why the candidate is recommended (see [`RecommendationReason`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#recommendation-reason)). |
| `validity_interval` | `Interval` | No | Time window during which this context applies (see [`Interval`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#interval)). For example, a candidate is new for only a limited number of days. If unset, the context applies for as long as the candidate is stored. |

### `RecommendationReason`

The `RecommendationReason` object carries one reason. Set exactly one of the
following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `top_on_partner` | `object` | One of | The candidate is a ranked top item on your service. Contains a single positive integer field `rank` (for example, `{"rank": 1}` for "Top 1 on Partner"). |
| `popular_on_partner` | `object` | One of | The candidate is popular on your service. Pass an empty object (`{}`). |
| `new_on_partner` | `object` | One of | The candidate is new on your service. Pass an empty object (`{}`). |
| `generic` | `object` | One of | A custom reason. Contains a single `LocalizedString` field `generic_reason` (see [`LocalizedString`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#localized-string)). Each value is 1 to 100 Unicode code points. |

### `ContentRating`

The `ContentRating` object represents an official content rating assigned by a
rating agency:

| Field | Type | Required | Description |
|---|---|---|---|
| `rating_system` | `string` | Yes | Rating agency or system, for example `"MPAA"`, `"BBFC"`, or `"CBFC"`. |
| `rating_value` | `string` | Yes | Rating as defined by `rating_system`, for example `"PG-13"` or `"U/A 13+"`. |

### `Timestamp`

A `Timestamp` is encoded in JSON as an RFC 3339 string in UTC with a `Z`
suffix, for example `"2026-10-01T18:00:00Z"`. Fractional seconds are allowed,
for example `"2026-10-01T18:00:00.500Z"`.

### `Duration`

A `Duration` is encoded in JSON as a string that contains the number of seconds
followed by the suffix `s`, for example `"7200s"` for 2 hours. Fractional
seconds are allowed, for example `"5400.5s"`.

### `Date`

A `Date` is a calendar date without a time zone. It is encoded in JSON as an
object with the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `year` | `integer` | Yes | Year of the date, for example `2025`. |
| `month` | `integer` | No | Month of the year, from `1` to `12`. Set to `0` or omit if the month isn't known. |
| `day` | `integer` | No | Day of the month, from `1` to `31`, and valid for the given year and month. Set to `0` or omit if the day isn't known. Requires `month`. |

For example, `{"year": 2025, "month": 1, "day": 17}` represents January 17,
2025, `{"year": 2025, "month": 1}` represents January 2025 with an unknown day,
and `{"year": 2025}` represents a date in 2025 with an unknown month and day.

### `Interval`

An `Interval` is a half-open time window that starts at `start_time`
(inclusive) and ends at `end_time` (exclusive). A time `T` is inside the
interval when `start_time <= T` and `T < end_time`.

| Field | Type | Required | Description |
|---|---|---|---|
| `start_time` | `string` (`Timestamp`) | Yes | Inclusive start of the window (see [`Timestamp`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#timestamp)), for example `"2026-10-01T18:00:00Z"`. |
| `end_time` | `string` (`Timestamp`) | Yes | Exclusive end of the window (see [`Timestamp`](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#timestamp)), for example `"2026-10-01T21:00:00Z"`. Must be later than `start_time`. |

## Example request

The following example replaces the candidates of feed `in-en-cricket` of
partner `example-partner` with three candidates (a movie, a TV show, and a live
TV program). The movie carries its text in two languages:

```bash
curl -X POST \
  "https://tvvideodiscovery.googleapis.com/v1/partners/example-partner/recommendationsFeeds/in-en-cricket:replaceCandidates" \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "recommendation_candidates": [
      {
        "movie_candidate": {
          "title": {
            "values": [
              {
                "text": "Example Action Movie",
                "language_code": "en-US"
              },
              {
                "text": "Película de acción de ejemplo",
                "language_code": "es-419"
              }
            ]
          },
          "description": {
            "values": [
              {
                "text": "An example action movie synopsis.",
                "language_code": "en-US"
              },
              {
                "text": "Sinopsis de una película de acción de ejemplo.",
                "language_code": "es-419"
              }
            ]
          },
          "localized_media_images": [
            {
              "language_code": "en-US",
              "image": {
                "url": "https://www.example.com/images/movie-1001-16x9-en.jpg",
                "width": 1920,
                "height": 1080,
                "accessibility_text": "Artwork for Example Action Movie"
              }
            },
            {
              "language_code": "es-419",
              "image": {
                "url": "https://www.example.com/images/movie-1001-16x9-es.jpg",
                "width": 1920,
                "height": 1080,
                "accessibility_text": "Imagen de Película de acción de ejemplo"
              }
            }
          ],
          "localized_provider_playback_uris": [
            {
              "playback_uri": {
                "uri": "https://www.example.com/watch/movie-1001?lang=en",
                "platforms": ["PLATFORM_ANDROID_TV", "PLATFORM_ANDROID"]
              },
              "language_code": "en-US",
              "package_name": "com.example.tvapp"
            },
            {
              "playback_uri": {
                "uri": "https://www.example.com/watch/movie-1001?lang=es",
                "platforms": ["PLATFORM_ANDROID_TV", "PLATFORM_ANDROID"]
              },
              "language_code": "es-419",
              "package_name": "com.example.tvapp"
            }
          ],
          "release_date": {
            "year": 2025,
            "month": 11,
            "day": 14
          },
          "external_entity_ids": [
            {
              "tms_root_id": "MV001234560000"
            }
          ],
          "duration": "7200s",
          "content_ratings": [
            {
              "rating_system": "MPAA",
              "rating_value": "PG-13"
            }
          ]
        },
        "recommendation_contexts": [
          {
            "recommendation_reason": {
              "top_on_partner": {
                "rank": 1
              }
            }
          }
        ],
        "availability_intervals": [
          {
            "start_time": "2026-11-01T00:00:00Z",
            "end_time": "2026-12-01T00:00:00Z"
          }
        ]
      },
      {
        "tv_show_candidate": {
          "title": {
            "values": [
              {
                "text": "Example Drama Series",
                "language_code": "en-US"
              }
            ]
          },
          "description": {
            "values": [
              {
                "text": "An example drama series synopsis.",
                "language_code": "en-US"
              }
            ]
          },
          "localized_media_images": [
            {
              "language_code": "en-US",
              "image": {
                "url": "https://www.example.com/images/show-2002-16x9.jpg",
                "width": 1920,
                "height": 1080,
                "accessibility_text": "Artwork for Example Drama Series"
              }
            }
          ],
          "localized_provider_playback_uris": [
            {
              "playback_uri": {
                "uri": "https://www.example.com/watch/show-2002",
                "platforms": ["PLATFORM_ANDROID_TV"]
              },
              "language_code": "en-US",
              "package_name": "com.example.tvapp"
            }
          ],
          "first_episode_air_date": {
            "year": 2024,
            "month": 3,
            "day": 8
          },
          "external_entity_ids": [
            {
              "data_feed_element_id": "show-2002"
            }
          ],
          "season_count": 3,
          "content_ratings": [
            {
              "rating_system": "TV_PG",
              "rating_value": "TV-14"
            }
          ]
        },
        "recommendation_contexts": [
          {
            "recommendation_reason": {
              "new_on_partner": {}
            },
            "validity_interval": {
              "start_time": "2026-11-01T00:00:00Z",
              "end_time": "2026-11-15T00:00:00Z"
            }
          }
        ],
        "availability_intervals": [
          {
            "start_time": "2026-11-01T00:00:00Z",
            "end_time": "2026-12-01T00:00:00Z"
          }
        ]
      },
      {
        "live_tv_program_candidate": {
          "title": {
            "values": [
              {
                "text": "Championship Live Broadcast",
                "language_code": "en-US"
              }
            ]
          },
          "description": {
            "values": [
              {
                "text": "Live coverage of the championship match.",
                "language_code": "en-US"
              }
            ]
          },
          "localized_media_images": [
            {
              "language_code": "en-US",
              "image": {
                "url": "https://www.example.com/images/live-prog-500-16x9.jpg",
                "width": 1920,
                "height": 1080,
                "accessibility_text": "Artwork for Championship Live Broadcast"
              }
            }
          ],
          "localized_provider_playback_uris": [
            {
              "playback_uri": {
                "uri": "https://www.example.com/live/sports-1",
                "platforms": ["PLATFORM_ANDROID_TV"]
              },
              "language_code": "en-US",
              "package_name": "com.example.tvapp"
            }
          ],
          "broadcast_interval": {
            "start_time": "2026-11-15T18:00:00Z",
            "end_time": "2026-11-15T21:00:00Z"
          },
          "external_entity_ids": [
            {
              "tms_id": "EP012345670001"
            }
          ],
          "content_ratings": [
            {
              "rating_system": "TV_PG",
              "rating_value": "TV-PG"
            }
          ]
        },
        "recommendation_contexts": [
          {
            "recommendation_reason": {
              "generic": {
                "generic_reason": {
                  "values": [
                    {
                      "text": "Live this weekend",
                      "language_code": "en-US"
                    }
                  ]
                }
              }
            }
          }
        ],
        "availability_intervals": [
          {
            "start_time": "2026-11-14T18:00:00Z",
            "end_time": "2026-11-15T21:00:00Z"
          }
        ]
      }
    ]
  }'
```

## Response and replacement behavior

This section describes the HTTP response returned by `replaceCandidates` and
how each call updates your stored candidates.

### `ReplaceCandidatesResponse`

If the request succeeds, the API returns HTTP `200 OK` with a
`ReplaceCandidatesResponse` body:

| Field | Type | Description |
|---|---|---|
| `replaced_candidates_count` | `integer` (int32) | Number of candidates replaced. |

For the preceding [example request](https://developer.android.com/guide/playcore/engage/tv/recommendations/rest.md.txt#example-request), the response is:

```json
{
  "replaced_candidates_count": 3
}
```

### Replacement behavior

Understanding how `replaceCandidates` updates stored candidates is essential
for designing your integration:

- **Full replacement per feed**. Each call completely replaces the previously stored candidate list for the feed named in the URL path. Always send the complete set of active candidates for that feed.
- **Other feeds remain unchanged** . Feeds that you don't send candidates to remain unchanged until you do. For example, replacing the candidates of one feed doesn't modify your stored candidates for any other feed, and replacing the candidates of `{recommendationsFeed}-staging` doesn't modify `{recommendationsFeed}`.
- **One call per feed**. To update several feeds, make one call per feed. The calls are independent: if one fails, the other feeds keep their new candidates and you retry only the failed call.
- **Resend active feeds at least every 30 days** . Even if your catalog for a feed hasn't changed, resend each active feed at least once every 30 days (or on a regular daily or weekly schedule with randomized jitter) so your candidates remain active and don't expire. Setting an `availability_intervals` `end_time` far in the future doesn't replace periodic resending.
- **Atomic execution**. The API applies the request atomically. If any candidate fails validation, the API rejects the entire request and the feed keeps its previous candidates.