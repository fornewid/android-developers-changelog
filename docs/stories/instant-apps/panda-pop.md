---
title: https://developer.android.com/stories/instant-apps/panda-pop
url: https://developer.android.com/stories/instant-apps/panda-pop
source: md.txt
---

# Panda Pop finds high-quality players with instant apps

![](https://developer.android.com/static/images/distribute/stories/panda-pop-icon.png)

[Jam City](https://play.google.com/store/apps/dev?id=5509190841173705883)is a leading developer in social gaming and the maker of[Panda Pop](https://play.google.com/store/apps/details?id=com.sgn.pandapop.gp)(built with Unity), a top-grossing bubble shooter game with the goal to rescue baby pandas trapped in bubbles! Jam City decided to leverage instant apps to optimize Panda Pop from a code architecture and design standpoint, as well as to see if they could acquire high-quality players.

Instant apps allows Panda Pop players to get a full gameplay experience instantly, without waiting to download and install the full game.

They built and launched an instant version of[Panda Pop](https://play.google.com/store/apps/details?id=com.sgn.pandapop.gp), which you can play by clicking the "Try Now" button on its Play Store listing.

### What they did

![](https://developer.android.com/static/images/distribute/stories/panda-pop.png)

The Panda Pop team chose to limit the instant apps to the first 10 levels, and only show the gameplay (removing the Main Menu and Map scenes). This decision significantly reduced the build size, as they were able to remove unnecessary code and game assets such as sprites and textures.

They removed any unused plugins, as well as reducing texture sizes and other assets like scenes, scripts, and animations. Finally, the team optimized the in-game bone animations -- which was accomplished by using a different Unity plugin -- and removed all of the unused[prefabs](https://docs.unity3d.com/Manual/Prefabs.html).

Marcelo Ferreiro, Director of Engineering, commented:

*"Instant apps is a win-win for players and developers - players get a fully functional gameplay experience before downloading, and developers get a promising new way to acquire high-quality users."*

Ferreiro also commented:

*"Building the instant app was a great opportunity for Jam City to see where Panda Pop could be optimized. We've taken those learnings and applied them to the full version of the game, which now runs smoother and with a reduced memory footprint."*

### Get started

Instant apps will be broadly available for games in the coming months.[Sign up here](https://docs.google.com/forms/d/e/1FAIpQLSeUodw6iqSKppOtm22vYwCgAnngES9lXV6821UBlF2bM3r-wg/viewform)to apply for the beta and receive more information as it is available.