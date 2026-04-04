---
title: https://developer.android.com/stories/games/epic-agde
url: https://developer.android.com/stories/games/epic-agde
source: md.txt
---

# &quot;AGDE is freaking awesome!&quot; for Android development with Unreal Engine

[Unreal Engine](https://www.unrealengine.com/en-US/) is a game engine
developed by Epic Games that gives creators across industries freedom
and control to deliver cutting-edge entertainment, compelling
visualizations, and immersive virtual worlds. Some major Android games are
built using Unreal Engine.

![Screenshot of Unreal Engine Suntemple sample running on Pixel 4](https://developer.android.com/static/images/cards/distribute/stories/unreal-suntemple-screenshot.jpg "Figure 1: Screenshot of Unreal Engine Suntemple sample running on Pixel 4")
**Figure 1**. Screenshot of Unreal Engine Suntemple sample running on Pixel 4

Epic and other game developers use [Android
Studio](https://developer.android.com/studio) for debugging C++, Kotlin or
Java programming languages, but many game developers have development
workflows for other platforms centered around Visual Studio.
The Unreal Engine Mobile Team focuses on feature development and
optimization of Unreal Engine for mobile platforms. The team has been using
Android Game Development Extension (AGDE) for both Unreal Engine Android
development and for Fortnite Android debugging and optimization.

## How they use it

Before adopting [Android Game Development Extension (AGDE)](https://developer.android.com/games/agde), debugging and
building for Android required opening the generated Gradle project in
Android Studio and then switching between the two development environments
for compiling or debugging, each with their own sets of key bindings. This
was both jarring to the developer and also time-consuming, especially for
iterative development. Now with AGDE, the entire development work cycle for
Android games is within Visual Studio! Developers who have migrated to the
new development workflow will find it is significantly faster and more
convenient for Unreal Engine Development.

After installing AGDE, whenever you generate your Visual Studio project
files for Unreal Engine (UE) 4.26.2 or later, Unreal Build Tool will also
generate Android build targets for use with AGDE. From then on, the Unreal
Engine development and debugging experience from within Visual Studio is
the same for Android as PC and other platforms. Pressing F5 inside Visual
Studio kicks AGDE into action, which then triggers the C++ Android build
and generates or updates the Android Application Package (APK). AGDE then
starts a C++ debugging session on the device, allowing the use of familiar
Visual Studio debugging features such as breakpoints, watches, and also
looking at disassembly and registers. AGDE-enabled Android builds also take
advantage of Unreal Build Tool's Incredibuild integration to provide
distributed builds across computers for Android C++ code.

![Screenshot of AGDE with Unreal Engine](https://developer.android.com/static/images/cards/distribute/stories/epic-agde-case-study-screenshot.png "Figure 2: Screenshot of AGDE with Unreal Engine")
**Figure 2**. Screenshot of AGDE with Unreal Engine

## Results

"Given our Visual Studio-centric development environment, we were very
excited to incorporate AGDE into our workflows. We definitely consider our
use of AGDE a success because Fortnite and Unreal Engine Mobile engineers
are using AGDE daily for their work," said Jack Porter, Unreal Engine
Mobile Team Lead. "AGDE allowed Epic to more quickly and conveniently debug
issues, and staying inside Visual Studio made a significant improvement
from their previous workflow. The use of AGDE has definitely saved us
significant time, and helped us find bugs that otherwise could not have
been found".

"We expect to continue using AGDE at Epic, and plan to have our
documentation recommend AGDE as the supported Unreal Engine Android
developer workflow for all Unreal Engine licensees," said Porter.
Dmytro Vovk, an Unreal Engine Mobile team developer, has been using AGDE as
part of his daily work on Unreal Engine and Fortnite Mobile, and says "AGDE
is freaking awesome! Finally I can debug assembly and see registers being
updated as I step through the code. Android debugging from the comfort of
Visual Studio makes my day-to-day work much easier and keeps me in my
development flow."

## Get started

Learn how the
[Android Game Development Extension](https://developer.android.com/games/agde)
enables you to target Android when building cross-platform games with C/C++
in Visual Studio.