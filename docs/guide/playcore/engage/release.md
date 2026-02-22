---
title: https://developer.android.com/guide/playcore/engage/release
url: https://developer.android.com/guide/playcore/engage/release
source: md.txt
---

This document contains release notes for the Engage SDK.

## Release Summary

| Release Version |    Date    |
|-----------------|------------|
| 1.5.11          | 2025-12-15 |
| 1.5.10          | 2025-10-14 |
| 1.5.9           | 2025-08-18 |
| 1.5.8           | 2025-04-25 |
| 1.5.7           | 2025-03-03 |
| 1.5.6           | 2025-01-07 |
| 1.5.5           | 2024-08-26 |
| 1.5.4           | 2024-08-07 |
| 1.5.3           | 2024-07-24 |
| 1.5.2           | 2024-06-14 |
| 1.5.0           | 2024-05-01 |
| 1.4.0           | 2024-03-04 |
| 1.3.1           | 2023-10-24 |
| 1.3.0           | 2023-09-14 |
| 1.2.1           | 2023-08-30 |
| 1.2.0           | 2023-07-19 |
| 1.1.0           | 2023-06-29 |
| 1.0.0           | 2023-06-08 |

## Engage SDK 1.5.11 Release (2025-12-15)

This version contains the following changes.

### Summary of changes

- Added last user interaction timestamp in`FoodShoppingCart`,`FoodShoppingList`, and`ShoppingList`.
- Added APIs to publish multiple shopping carts and lists.
  - `AppEngageFoodClient.publishFoodShoppingCarts`
  - `AppEngageFoodClient.publishFoodShoppingLists`
  - `AppEngageShoppingClient.publishShoppingLists`

## Engage SDK 1.5.10 Release (2025-10-14)

This version contains the following changes.

### Summary of changes

- Added`LiveTvChannelEntity`and`LiveTvProgramEntity`to engage video data model.

## Engage SDK 1.5.9 Release (2025-08-18)

This version contains the following changes.

### Summary of changes

- Added`RecommendationClusterType`to`RecommendationCluster`.
- Added`Description`,`Genre`,`ContentRatings`and`RecommendationReason`to`LiveStreamingVideoEntity`.

## Engage SDK 1.5.8 Release (2025-04-25)

This version contains the following changes.

### Summary of changes

- Added`AccountProfile`and`syncAcrossDevices`to`PublishRecommendationClustersRequest`.
- Added`Locale`to the`AccountProfile`.
- Added`MediaActionFeedEntity`to engage video data model.
- Added`PlatformSpecificPlaybackUri`to`TVShowEntity`.
- Added`description`field to`MovieEntity`and`TVShowEntity`.
- Added`RecommendationReason`to`MovieEntity`and`TVShowEntity`.

## Engage SDK 1.5.7 Release (2025-03-03)

This version contains the following changes.

### Summary of changes

- Support for`DisplayTimeWindow`in travel entities.
- Addition of travel specific broadcast intents.

## Engage SDK 1.5.6 Release (2025-01-07)

This version contains the following changes.

### Summary of changes

- Addition of`ContinueSearchCluster`in Travel vertical.
- Support for localized timestamp across entities in Travel vertical.
- Renaming of`ContinuationCluster`to`ReservationCluster`in Travel vertical.

## Engage SDK 1.5.5 Release (2024-08-26)

This version contains the following changes.

### Summary of changes

- Add crop type in Image.
- Support multiple interactions in PortraitMediaEntity.

## Engage SDK 1.5.4 Release (2024-08-07)

This version contains the following changes.

### Summary of changes

- Add last user interaction timestamp in`ShoppingCart`.
- Add support for publishing multiple shopping carts using`publishShoppingCarts`API in`AppEngageShoppingClient`.

## Engage SDK 1.5.3 Release (2024-07-24)

This version contains the following changes.

### Summary of changes

- Infra improvements.
- Create a TV specific variant of Engage SDK.

## Engage SDK 1.5.2 Release (2024-06-14)

This version contains the following changes.

### Summary of changes

- Add video preview content in`SocialPostEntity`and`PortraitMediaEntity`.

## Engage SDK 1.5.0 Release (2024-05-01)

This version contains the following changes.

### Summary of changes

- SDK size reduction

## Engage SDK 1.4.0 Release (2024-03-04)

This version contains the following changes.

### Summary of changes

- Add expiry for`ShoppingCart`and`FoodShoppingCart`

## Engage SDK 1.3.1 Release (2023-10-24)

This version contains the following changes.

### Summary of changes

- Added new publish status codes

  - AppEngagePublishStatusCode.NOT_PUBLISHED_FEATURE_DISABLED_BY_CLIENT
  - AppEngagePublishStatusCode.NOT_PUBLISHED_CLIENT_ERROR
  - AppEngagePublishStatusCode.NOT_PUBLISHED_SERVER_ERROR
- Update Image to have an enum indicating the theme

  - IMAGE_THEME_LIGHT
  - IMAGE_THEME_DARK
- Update metadata for`TvEpisodeEntity`and`TvSeasonEntity`

## Engage SDK 1.3.0 Release (2023-09-14)

This version contains the following changes.

### Summary of changes

- Updated the metadata for the[listen vertical](https://developer.android.com/guide/playcore/engage/listen)

## Engage SDK 1.2.1 Release (2023-08-30)

This version contains the following changes.

### Summary of changes

- Updated the metadata for the[Sign In Card](https://developer.android.com/guide/playcore/engage/publish#user-management-cluster-signin)

## Engage SDK 1.2.0 Release (2023-07-19)

This version contains the following changes.

### Summary of changes

- Adds support for social vertical. Refer to the[social integration guide](https://developer.android.com/guide/playcore/engage/social)for more details

## Engage SDK 1.1.0 Release (2023-06-29)

This version contains the following changes.

### Summary of changes

- Supports custom action CTA in Shopping Cart \& Reorder.
- Supports display time window for specific entities.
- `AppEngageShoppingClient`and`AppEngageFoodClient`now support additional methods to publish and delete all the clusters from a single client.

## Engage SDK 1.0.0 Release (2023-06-08)

This version contains the following changes.

### Summary of changes

- Initial Public Release