---
title: https://developer.android.com/stories/games/ea-agde
url: https://developer.android.com/stories/games/ea-agde
source: md.txt
---

# Firemonkeys reduced development and debugging time with AGDE

[Electronic Arts](https://play.google.com/store/apps/dev?id=6605125519975771237)(EA) is a game company headquartered in California, USA. It produces a wide variety of games across different genres, such as: sports, action, racing, and simulation. EA's development studio, Firemonkeys, is best known as the developer of[Real Racing 3](https://play.google.com/store/apps/details?id=com.ea.games.r3_na),[The Sims FreePlay](https://play.google.com/store/apps/details?id=com.ea.games.simsfreeplay_na), and[Need For Speed: No Limits](https://play.google.com/store/apps/details?id=com.ea.game.nfs14_row). Firemonkeys uses a custom game engine to develop games, and now uses[Android Game Development Extension (AGDE)](https://developer.android.com/games/agde)in its development workflow for all of their Android games. The studio was looking for a way to streamline their build and debugging workflows, to ultimately save development effort and cost, and AGDE provided that.

![Screenshot from The Sims: Freeplay](https://developer.android.com/static/images/cards/distribute/stories/sims-freeplay-screenshot.webp "Figure 1: Screenshot from The Sims: Freeplay")**Figure 1**: Screenshot from The Sims: Freeplay

## How they use it

Firemonkeys uses AGDE to produce all of their Android builds for testing, as well as to debug native C/C++ code on Android. Their game building workflow includes a combination of precompiled headers and[Unity](https://en.wikipedia.org/wiki/Single_Compilation_Unit)builds to improve compile times - both of which are well supported by AGDE. For debugging, Firemonkeys frequently uses AGDE to debug C/C++ code. Patrick Broddesson, Technical Director at EA, said, "We are happy with the debugging interface and performance. We use the disassembly view for those times when more complex issues arise, and AGDE has great tools for that." When it comes to profiling, the ability to quickly launch Android Studio Profilers from the extension itself made the profiling process easier and faster when looking into device specific problems.

Firemonkeys' engineering team was already intimately familiar with Visual Studio, and integrating AGDE into their existing workflow for a new or existing project was easily achieved within a few days. "The integration process is simple, and the extension comes with documentation and sample apps for guidance," said Broddesson.

![AGDE debugging in progress](https://developer.android.com/static/images/cards/distribute/stories/ea-agde-case-study-screenshot.png "Figure 2: AGDE debugging in progress")**Figure 2**: AGDE debugging in progress

## Results

Using AGDE allows Firemonkeys to unify development environments, and automate build pipelines across platforms and devices. AGDE enabled Firemonkeys to take advantage of their existing Visual Studio IDE together with AGDE's debugging interfaces to address Firemonkeys' Android development needs. Broddesson states that the integration has been successful and a marked improvement over their previous workflows. "Using AGDE has most definitely reduced the development time of new Android features, as well as the time spent debugging complex Android specific bugs." The Firemonkeys team found that using AGDE resulted in less maintenance, and quicker setup time for new projects, especially for cross-platform projects that are already setup with Visual Studio as the main IDE. "The biggest win for us from using AGDE is that we can minimize context switching for our engineering team by not having to move between different IDEs and debugging tools."

Overall, Firemonkeys expects that using AGDE's building, debugging, and profiling tools will reduce the development costs for Android specific features by 10-15%. "The cost savings result from reducing obstacles in engineering workflows for our teams", said Broddesson.

## Get started

Learn how the[Android Game Development Extension](https://developer.android.com/games/agde)enables you to target Android when building cross-platform games with C/C++ in Visual Studio.