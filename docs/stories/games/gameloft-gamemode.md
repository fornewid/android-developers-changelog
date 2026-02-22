---
title: https://developer.android.com/stories/games/gameloft-gamemode
url: https://developer.android.com/stories/games/gameloft-gamemode
source: md.txt
---

# Gameloft reduces device power consumption by 70%, resulting in 35% longer play time with the Game Mode API

## Background

For more than 20 years,[Gameloft](https://play.google.com/store/apps/dev?id=4826827787946964969)has created innovative gaming experiences for digital platforms, from mobile games to cross-platform PC and console titles. In addition to its own established franchises, Gameloft develops games for popular brands like LEGO, Universal, and Hasbro. With a team of 3,600 people worldwide, their games reach 55 million unique players in over 100 countries every month.

## What they did

First released in 2018, racing arcade game[Asphalt 9: Legends](https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM)needed a way to balance performance, fidelity, and battery. To do this, Gameloft originally used an in-house system called "game options," which allowed users to choose from three settings: better performance, better quality, or a balance of the two. If the player didn't choose a setting, the game would select one automatically based on the user's device.

Recently, Gameloft updated the game to incorporate the[Game Mode API](https://developer.android.com/games/gamemode/gamemode-api)as a way to improve the gameplay experience for users with newer devices. With Game Mode, they empowered players to use the[Game Dashboard](https://developer.android.com/games/gamedashboard/aboutdashboard)to customize the game's performance and adjust other system settings that affect their play experience.

Because users were already used to seeing Asphalt 9's game options feature, Gameloft integrated it with the Game Mode API in the background, improving the feature without disrupting the user experience. Users could choose from four options:

- [STANDARD](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_STANDARD)(60FPS on devices that support it and 30FPS on low-end devices),
- [PERFORMANCE](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE)(best quality but resource-intensive on high-end devices, 60FPS but lower quality on low-end devices),
- [BATTERY](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_BATTERY)(30FPS to reduce battery use), or
- [UNSUPPORTED](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_UNSUPPORTED)(visual settings stay in the options menu)

In Battery mode, graphic fidelity of environmental details is reduced to lower power consumption. High computational tasks such as ray tracing calculations for the reflections on the car and depth of field for the environmental props are removed, and complex shaders for motion blur and weather effects are simplified. The frame rate is also capped at 30FPS to save on CPU and GPU workload.
![Asphalt 9 - BATTERY Mode](https://developer.android.com/static/images/cards/distribute/stories/gameloft-asphalt9-gamemode-battery.jpg)**Asphalt 9 running in BATTERY Mode**

In Performance mode, the game detects the user's device capabilities and applies the optimal configuration of resources for maximum immersion without causing the device to thermally throttle. While devices can be boosted temporarily to deliver peak performance, it's not energy-efficient and generates a lot of heat. Entering peak performance sparingly, such as during loading, and then lowering to sustained performance optimizes the use of energy and provides a better user experience overall.
![Asphalt 9 - PERFORMANCE Mode](https://developer.android.com/static/images/cards/distribute/stories/gameloft-asphalt9-gamemode-performance.jpg)**Asphalt 9 running in PERFORMANCE Mode**

## Results

Gameloft expected players to enjoy the improved performance and gameplay, but it was Battery mode that had some of the biggest impact.**On some mobile devices, Battery mode reduced Asphalt 9's power consumption by up to 70%, resulting in 35% longer play time on average and a cooler device in the player's hand.**

"The implementation was easy to manage," said Alexandru Dumitru, Publishing Operations Manager at Gameloft, "and the team appreciated having a simple way to offer their users the latest and greatest performance experience."

Based on their success, Gameloft intends to implement the Game Mode API on other games in their portfolio. Players of competitive multiplayer and shooter titles would appreciate the extra performance, while building sims could benefit from the battery-saving mode.

## Get started with Game Mode

Understand your users and make better decisions about performance and fidelity tradeoffs by using the[Game Mode API](https://developer.android.com/games/gamemode/gamemode-api).