---
title: https://developer.android.com/training/wearables/tiles
url: https://developer.android.com/training/wearables/tiles
source: md.txt
---

# Tiles provide quick access to the information and actions users need to get things done. The tiles carousel is revealed by a swipe on the watch face, and additional swipes will switch between tiles. Tiles themselves cannot be scrolled.

Users can choose what tiles they want to see. There are tiles to check the weather, set a timer, track daily fitness progress, quick-start a workout, play a song, scan an upcoming meeting, and send a message to a favorite contact.
![Tiles next to each other.](https://developer.android.com/static/wear/images/tiles/m3-tiles-examples.png)**Figure 1.**: Tiles give users access to information and actions.

Instead of using[Compose](https://developer.android.com/compose)(or[Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)), Tiles are defined declaratively using Jetpack's[protolayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout)and[tiles](https://developer.android.com/jetpack/androidx/releases/wear-tiles)libraries. Because Tiles are rendered in a separate, remote environment, they require different approaches to load, display, and update data within them. Their simplicity makes them straightforward to build, test, and deploy.

## Core principles

Wear OS provides tiles as a way for you to show a small amount of key information, which users can read through after they glance at a tile for a few seconds. To provide this high-quality experience for users, follow these best practices:

- Don't overcrowd tiles with too much content. Instead, allow users to tap on tiles to learn more and take action on another surface in your app. See[Include (at least) one container](https://developer.android.com/design/ui/wear/guides/surfaces/tiles/bestpractices#include_at_least_one_container).
- Declaratively define your tile's layout and content. The system is responsible for the final rendering.
- Don't fetch content frequently or start long-running asynchronous work in your tile service. To perform work which may take some time to complete---such as network calls---use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#expedited)to schedule background tasks, and cache or store the results in local storage.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Show dynamic updates in tiles](https://developer.android.com/training/wearables/tiles/dynamic)
- [Migrate to ProtoLayout namespaces](https://developer.android.com/training/wearables/tiles/migrate-to-protolayout)