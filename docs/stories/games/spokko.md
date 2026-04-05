---
title: https://developer.android.com/stories/games/spokko
url: https://developer.android.com/stories/games/spokko
source: md.txt
---

# The Witcher: Monster Slayer increases reach with Android Performance Tuner

## Background

![Witcher: Monster Slayer game art featuring Leshy](https://developer.android.com/static/images/cards/distribute/stories/spokko-witcher-monster-slayer.png "Witcher: Monster Slayer")

Based in Poland, Spokko is a group of ambitious creators who are working with a very demanding IP. Although it is part of the CD PROJEKT family, Spokko is an independent company that has transferred the great world of[The Witcher: Monster Slayer](https://play.google.com/store/apps/details?id=com.spokko.witchermonsterslayer)to smartphones.

The Witcher: Monster Slayer is a location-based RPG game that uses augmented-reality technology. It's a computationally intensive game that would challenge many devices. At launch, Spokko wanted to ensure their game would reach the largest number of users, while providing a high quality experience for everyone.

## What they did

The Witcher: Monster Slayer started with a three-phase soft launch in New Zealand, and added several additional countries over time. They started with the technical phase, to check the compatibility of devices and examine technical issues. The second phase focused on retention, to better understand whether users like the game and how to increase their session duration. The third phase focused on monetization, and whether players would be willing to pay for additional in-game items, and what items they were interested in. They also collected a lot of gameplay data, which allowed them to optimize the game for as many devices as possible, and to improve the gameplay balance on both newer and older Android devices.

During the initial technical phase, Spokko used[Android Performance Tuner](https://developer.android.com/games/sdk/performance-tuner)to assess the game's performance on different devices based on actual usage during the soft-launch. They also used[Play Developer Console](https://play.google.com/console/about/)and[Device catalog](https://play.google.com/console/about/devicecatalog/)to add additional devices over time. With this information, they were able to turn off under-performing devices and confidently launch on a wider variety of devices. "APT allowed us, above all, to get acquainted with the technical capabilities of individual devices and what their performance was like. We were also able to get statistics using information about issues in the area of the worst-performing hardware. APT allowed us to investigate which exact smartphones give us the best performance," said Kacper Bąk, Lead of Business Intelligence.

## Results

Initially, the team only enabled devices that officially supported ARCore. By using Android Performance Tuner, they gained a comprehensive overview of the hardware on which The Witcher: Monster Slayer was running. Eventually, they added many devices that did not support ARCore, expanding from 520 devices to 9280 devices in only two weeks, which led to a 10% increase in downloads.

As Mateusz Janczewski, Executive Producer, puts it, "Initially, we planned to make Monster Slayer available on devices with ARCore, which significantly limited the number of devices players could download the game on. However, the opinions of players encouraged us to look for additional solutions that would extend the availability. We came up with the idea to use the Device catalog, along with the Android Performance Tuner, for this particular purpose. Without these technologies, we would not meet the requests of players, and we would not be able to increase the number of devices compatible with the game in such an extremely short time."

In the future, Spokko plans to add additional telemetry around quality levels to decide which devices should play the game with normal quality or high quality. They also plan to add telemetry to different sections of the game, to better understand how different parts perform, such as on the map, within combat, or during cutscenes.

## Get started

Get started today by learning more about[Android Performance Tuner](https://developer.android.com/games/sdk/performance-tuner)and discover how you can increase your game's reach, while ensuring that all your players have a high quality experience.