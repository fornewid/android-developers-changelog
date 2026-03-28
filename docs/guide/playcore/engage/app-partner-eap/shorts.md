---
title: https://developer.android.com/guide/playcore/engage/app-partner-eap/shorts
url: https://developer.android.com/guide/playcore/engage/app-partner-eap/shorts
source: md.txt
---

book_path: /distribute/other-docs/_book.yaml
project_path: /distribute/other-docs/_project.yaml

You can use the Engage SDK to integrate short-form video content
recommendations into the Google TV **For You** page. The app on the device
pushes recommendation candidates to the Google TV backend using the Engage SDK.

## Overview

Short-form video integration uses the [`PortraitMediaEntity`](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaEntity) object. This
object provides the necessary metadata fields for social media content and is
optimized for vertical, social-oriented videos.

## Implementation

Follow these steps to publish recommendations:

### Set up Engage SDK

Add the Engage SDK dependency to your app-level `build.gradle` file, and
implement a service to provide recommendation clusters to the SDK as
described in the [Engage SDK for TV integration guide](https://developer.android.com/guide/playcore/engage/tv).

### Build and publish shorts recommendations

Build a list of `PortraitMediaEntity` objects and publish them using the
SDK.

#### Example implementation

The following code demonstrates how to build a `PortraitMediaEntity`:

### Kotlin

    val interaction = Interaction.Builder()
        .setCountValue(1200000L)
        .setLabelType(LabelType.LIKE)
        .build()

    val portraitMediaPost = PortraitMediaPost.Builder()
        .addVisualContent(
            Image.Builder()
                .setImageUri(Uri.parse("https://example.com/poster.jpg"))
                .setImageHeightInPixel(1920)
                .setImageWidthInPixel(1080)
                .build())
        .setTextContent("Check out this amazing vertical video!")
        .setIsVideoContent(true)
        .setVideoDurationMillis(30000L)
        .build()

    val entity = PortraitMediaEntity.Builder()
        .setEntityId("unique_short_id_123")
        .setActionLinkUri(Uri.parse("https://example.com/shorts/123"))
        .addPlatformSpecificPlaybackUri(
            PlatformSpecificUri.Builder()
                .setPlatformType(PlatformType.TYPE_ANDROID_TV)
                .setActionUri(Uri.parse("app://tv/shorts/123"))
                .build()
        )
        .setPortraitMediaPost(portraitMediaPost)
        .addInteractions(listOf(interaction))
        .setCommentsSummary("Users are praising the creative editing in this video.")
        .build()

### Java

    Interaction interaction = new Interaction.Builder()
        .setCountValue(1200000L)
        .setLabelType(LabelType.LIKE)
        .build();

    PortraitMediaPost portraitMediaPost = new PortraitMediaPost.Builder()
        .addVisualContent(
            new Image.Builder()
                .setImageUri(Uri.parse("https://example.com/poster.jpg"))
                .setImageHeightInPixel(1920)
                .setImageWidthInPixel(1080)
                .build())
        .setTextContent("Check out this amazing vertical video!")
        .setIsVideoContent(true)
        .setVideoDurationMillis(30000L)
        .build();

    PortraitMediaEntity entity = new PortraitMediaEntity.Builder()
        .setEntityId("unique_short_id_123")
        .setActionLinkUri(Uri.parse("https://example.com/shorts/123"))
        .addPlatformSpecificPlaybackUri(
            new PlatformSpecificUri.Builder()
                .setPlatformType(PlatformType.TYPE_ANDROID_TV)
                .setActionUri(Uri.parse("app://tv/shorts/123"))
                .build()
        )
        .setPortraitMediaPost(portraitMediaPost)
        .addInteractions(ImmutableList.of(interaction))
        .setCommentsSummary("Users are praising the creative editing in this video.")
        .build();

To present a custom count indicator, including a customized visual or label, use
`setCount`, `setCountWithOptionalLabel`, `addVisual()`, and `addVisuals()`. See
the Javadocs for more details.

#### Publish cluster

After building entity objects, publish them in a cluster:

### Kotlin

    val recommendationCluster = RecommendationCluster.Builder()
        .setTitle("Shorts for you")
        .addEntity(entity) // entity from previous example
        .build()
    client.publishRecommendationClusters(
      PublishRecommendationClustersRequest.Builder()
        .addRecommendationCluster(recommendationCluster)
        .build()
    )

### Java

    RecommendationCluster recommendationCluster = new RecommendationCluster.Builder()
        .setTitle("Shorts for you")
        .addEntity(entity) // entity from previous example
        .build();
    client.publishRecommendationClusters(
      new PublishRecommendationClustersRequest.Builder()
        .addRecommendationCluster(recommendationCluster)
        .build()
    );

## Field mapping summary

The following table outlines the fields available for the `PortraitMediaEntity`
object:

| Component | Field | Required? | Description |
|---|---|---|---|
| [**PortraitMediaEntity**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaEntity) | `actionLinkUri` | Yes | Deep link to view the short-form video in the app. |
| [**PortraitMediaEntity**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaEntity) | `portraitMediaPost` | Yes | An object containing metadata about the video post. See below for details. |
| [**PortraitMediaEntity**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaEntity) | `commentsSummary` | No | A summary of the video's comments to provide immediate social context. |
| [**PortraitMediaPost**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaPost) | `visualContent` | Yes | Provide poster images with a **2:3 aspect ratio**. You may supply 2x and 4x versions for better scaling. |
| [**PortraitMediaPost**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaPost) | `isVideoContent` | No | Whether the post is a video. |
| [**PortraitMediaPost**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaPost) | `videoDurationMillis` | No | The duration of the video in milliseconds. |
| [**PortraitMediaPost**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaPost) | `timestamp` | No | The timestamp of when the content was posted. |
| [**PortraitMediaPost**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaPost) | `textContent` | No | Text content associated with the post. |
| [**Profile**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/Profile) | `name` | Yes | Name of the content creator. |
| [**Profile**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/Profile) | `avatar` | Yes | Avatar image of the content creator. |
| [**Interaction**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/Interaction) | `count` | Yes | Display count of interactions (for example, "1.2M"). |
| [**Interaction**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/Interaction) | `label` or `visuals` | Yes | A text label (for example, "Likes") or visual icon representing the interaction type. |
| [**Interaction**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/Interaction) | `countValue` | No | The interaction count as a numeric value for ranking or sorting. |
| [**PortraitMediaEntity**](https://developer.android.com/reference/com/google/android/engage/social/datamodel/PortraitMediaEntity) | `platformSpecificPlaybackUris` | No | Provide playback URIs specific to different platforms (for example, TV or Mobile). |