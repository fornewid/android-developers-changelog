---
title: https://developer.android.com/stories/games/rv-appstudios-pad
url: https://developer.android.com/stories/games/rv-appstudios-pad
source: md.txt
---

# RV AppStudios improves user retention with Google Play Asset Delivery

## Background

![Puzzle Kids game](https://developer.android.com/static/images/cards/distribute/stories/puzzle-kids-framed.png)

US-based developer
[RV AppStudios](https://play.google.com/store/apps/dev?id=7430005971129979939)
has over 200 million downloads to date across their portfolio of casual games,
educational kids apps, and utility apps. As an early tester of Google Play Asset
Delivery with their app
[Puzzle Kids - Animals Shapes and Jigsaw Puzzles](https://play.google.com/store/apps/details?id=com.rvappstudios.jigsaw.puzzles.kids),
the team looked to optimize the size of their app, save money, and improve the
user experience by removing any friction when new asset packs would be required
to be downloaded.

## What they did

When a user installs the Puzzle Kids app, a base level of content is included in
the initial install. As the user progresses through the in-app content, in order
to access new levels and content, the user is required to download additional
game files. In order to deliver these additional content bundles, RV AppStudios
pays a third-party CDN to host the content and manage the delivery.

Play Asset Delivery was an appealing solution to help save CDN costs and improve
user performance. The integration process was very simple, taking the team less
than a day of development time to integrate the plugin into their existing
projects and to do the basic settings for the plugin. "Google Play Asset
Delivery met our expectations in a manner of cost, time, and effort to implement
the plugin" said Vivek Dave, President at
[RV AppStudios](https://play.google.com/store/apps/dev?id=7430005971129979939).

Three custom delivery options are available with Play Asset Delivery:
Install-Time, Fast-Follow, and On-Demand. Install-Time allows game developers to
package up to 1GB of assets with their initial game download, while On-Demand
and Fast-Follow allow developers to dynamically download assets post-launch (the
latter of which will be automatically triggered after installation). For Puzzle
Kids, the team utilizes the On-Demand delivery mode for their 17 asset packs.

## Results

Just over 23MB of assets are delivered as players progress through the levels
in Puzzle Kids. Using Play Asset Delivery's On-Demand mode, they saw a **4.7%
increase in 15-day retention and 21% reduction in crashes \& ANRs**. Overall,
these changes helped improve the user experience by offering more stable,
transparent, and secure downloads, while also saving costs for RV AppStudios.

## Get started

Get started today by learning more about
[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery).