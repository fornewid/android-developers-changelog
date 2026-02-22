---
title: https://developer.android.com/stories/games/devsisters
url: https://developer.android.com/stories/games/devsisters
source: md.txt
---

# Cookie Run: OvenBreak saves over $200K CDN cost with Play Asset Delivery

![](https://developer.android.com/static/images/distribute/stories/Devsisters_PAD_thumbnail.png)

Devsisters is a global mobile game developer and publisher, producing casual games based on the Cookie Run IP. Their most popular games include[Cookie Run: OvenBreak](https://play.google.com/store/apps/details?id=com.devsisters.gb)(running arcade) and[Cookie Run: Kingdom](https://play.google.com/store/apps/details?id=com.devsisters.ck)(social RPG), which are loved by users worldwide, especially in Korea, Taiwan, and the US. Although Cookie Run: OvenBreak is a casual game, the accumulated resources over five years increased the CDN capacity up to 2.5GB, which led to increased CDN cost. Devsisters needed to find a sustainable model for their games with large file sizes.

![](https://developer.android.com/static/images/distribute/stories/Devsisters_CDN.png)

## What they did

Devsisters identified that the large CDN download was causing a negative first time user experience, which also increased user churn. Users were spending a long time watching the download screen before playing the game for the first time.

In an effort to decrease the game's unnecessary resources, Devsisters switched to Play Asset Delivery. Using one Install-Time asset pack allowed them to package up to 1GB of assets with their initial game download.

"Even with a quick shift using the Install-Time delivery option, we were able to see promising results. For new games, we would like to design the data structure that could fully take advantage of all three custom delivery options: Install-Time, Fast-Follow, and On-Demand," said Hyoungook Bae, VP of Devsisters.

## Results

Devsisters decreased the secondary download size using CDN by 40%, from 2.5GB to 1GB, and through additional asset optimization, they managed to reduce the CDN cost by 84%, over $200K annually. They also decreased the overall binary size by 46%. Day one to day 14 retention improved as well, which was a significant win for Devsisters, as they shared how increasing retention is usually challenging and complex.

## Get started

Get started today by learning more about[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery).