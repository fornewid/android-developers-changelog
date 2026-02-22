---
title: https://developer.android.com/stories/games/gameloft-pad
url: https://developer.android.com/stories/games/gameloft-pad
source: md.txt
---

# Gameloft acquires 10% more new users with Google Play Asset Delivery

## Background

In 2000,[Gameloft](https://play.google.com/store/apps/dev?id=4826827787946964969)was created with a passion for games and a desire to bring them to players around the world. They were an early pioneer developing for mobile and now have a portfolio of over 190 games. Many of Gameloft's mobile games are graphically-intense and have a large download size. This made them a compelling partner in the early development of Google Play Asset Delivery (PAD), a set of delivery features for games services that build on our App Bundle infrastructure. PAD provides free, dynamic delivery of the right game assets to the right devices at the right time. This intrigued Gameloft as they set out to switch from the traditional APK + OBB system, reducing CDN costs, and improving the overall user experience for their players.

## What they did

The integration process was relatively straightforward. Moving to the app bundle format made for an easy change from Google Expansion files to Install-Time. Implementing the Fast-Follow and On-Demand systems was also simple since they are similar to Gameloft's existing DLC systems and contain everything needed for replacement, including fast download speeds, download progress info, and download state. "Since the heavy lifting was already handled by the PAD SDK, it was just a matter of replacing a few calls and letting PAD do the rest," said Maximiliano Rodriguez, Platforms Operations Director at Gameloft.

Once moved to the Android App Bundle, Gameloft integrated PAD's three delivery modes:

- **Install-Time** ---in*Asphalt Xtreme*, originally released using the Google Expansion Files (OBBs).
- **Fast-Follow** ---in*Asphalt 8*, originally released using an in-house asset-delivery system for secondary downloads.
- **On-Demand** ---in*Minion Rush: Despicable Me*, originally released using an in-house asset-delivery system for downloading additional assets as users progress through levels in the game.

![](https://developer.android.com/static/images/cards/distribute/stories/asphalt-8-pad.png)**Asphalt 8**

## Results

Gameloft saw a reduction in CDN costs for both*Asphalt 8* \&*Minion Rush*. With Fast-Follow delivery, they have had a significant increase in the number of users who completed the secondary download to start playing the game. This also resulted in better user retention, with 10% more new players compared to their previous CDN asset delivery system.

With the promising early results and seamless implementation process, Gameloft plans to use PAD in more of their upcoming releases. They plan to lower their game's footprint on devices and provide an overall better experience by dropping the old APK + OBB system in place of using the app bundle format and PAD's Install-Time feature. At the same time, they are investigating the switch to On-Demand for additional games that use their proprietary asset-delivery system, as well as combining Play Asset Delivery delivery modes in the same game. For example, the initial asset download in a game could be through Fast-Follow, then the in-game asset downloads could be through On-Demand. They suggest splitting data into three categories:

- The data that your app needs to run the first time.
- The data that your app can live without for the beginning, but will need after a few minutes of usage.
- The optional data that only some users will need.

## Get started

Get started today by learning more about[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery)and discover how Gameloft approaches building for larger screens in the[Apps, Games, \& Insights podcast](http://appsgamesinsights.googledevelopers.libsynpro.com/building-for-larger-screens-and-better-game-experiences-episode-7).