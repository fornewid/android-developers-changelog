---
title: https://developer.android.com/stories/games/cdpr
url: https://developer.android.com/stories/games/cdpr
source: md.txt
---

# CD Projekt RED reduces update size by 90% and increases update rates by 10% with Play Asset Delivery

Based in Warsaw, Poland, game developer CD Projekt RED (CDPR) reimagined their mini-game in The Witcher 3,[GWENT: The Witcher Card Game](https://play.google.com/store/apps/details?id=com.cdprojektred.gwent), to launch as a standalone free-to-play title on Google Play in March of 2020. With a large initial file size and regular updates requiring additional device storage, users were often forced to reinstall the full game in order to receive an updated version. This was the most prominent point of frustration among the game's community. In an effort to help with differential patching, CDPR has seen great success by implementing Play Asset Delivery.
![GWENT: The Witcher Card Game by CD Projekt RED](https://developer.android.com/static/images/cards/distribute/stories/cdpr-thumbnail.png)**GWENT: The Witcher Card Game by CD Projekt RED**

## What they did

CDPR was an early partner to implement Play Asset Delivery (PAD). With three different delivery modes available, they initially implemented on-demand, allowing for asset packs to be installed while the game is running. CDPR then adopted fast-follow delivery, automatically serving over 40 asset packs that range in size from 4 MB to 160 MB each, as soon as the game was installed. The benefit of using fast-follow is it permits downloads to happen in the background, even if the user has not opened the game. Upon the next open, the game is updated and ready to be played right away. "It's the only reliable solution that provides us with all key features: delta patching, in-game and in-store downloading, and dynamic updates," said Maciej Włodarkiewicz, Lead Producer.

## Results

CDPR was particularly pleased with the way PAD helped streamline app updates. They saw major improvement in update rates and reduction in reinstalls thanks to Play Asset Delivery auto-updates and delta patching. With this, CDPR was able to reduce their update size by 90%. An update that used to require download and extra storage space of more than 2GB now only takes a couple hundred MB.

Almost immediately after implementing PAD, CDPR saw a reduction of reinstalls and an increase in the speed of players updating to the latest app version. Between app versions 7.0 to 7.1, they saw almost a 10% lift in the percentage of active devices updated to the latest app version and a 4.8x reduction in uninstalls on day 1 of the new version release. Using fast-follow and background downloads, GWENT was able to save users an average of 8 minutes of idle wait time, compared to using a content delivery network.

## Get started

Get started today by learning more about[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery).