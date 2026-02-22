---
title: https://developer.android.com/stories/games/pokemon-tcg-pocket-vulkan
url: https://developer.android.com/stories/games/pokemon-tcg-pocket-vulkan
source: md.txt
---

# Pokémon TCG Pocket: Adopting Vulkan-only development for casual games

![Game title logo screenshot from Pokémon TCG Pocket.](https://developer.android.com/static/images/cards/distribute/stories/pokemon_tcg_pocket_logo.png)

The Pokémon Trading Card Game (TCG) has been enjoyed across the globe for nearly 30 years. The recently released Pokémon TCG Pocket is designed to let players experience Pokémon collections and battles anytime, anywhere, without the need for physical cards. The game's accessibility on smartphones has contributed to its widespread popularity among users.

While it may appear to be a casual trading card game, Pokemon TCG Pocket utilizes complex shaders, posing a significant challenge in reducing compilation time. To address this and ensure high-quality graphics and a smooth gaming experience, the Android version of Pokémon TCG Pocket has embraced Vulkan, the next-generation graphics API.

This document delves into the Pokémon TCG Pocket development team's adoption of Vulkan, the challenges encountered, and the advantages Vulkan offers.
**Figure 1.**Pokémon TCG Pocket game play scenes.

#### Reasons for adopting Vulkan

Initially, the Pokémon TCG Pocket development team planned to use OpenGL ES. However, they decided to adopt Vulkan, a graphics API with a promising future. The primary reasons for choosing Vulkan were:

- **Long-term app management**: Recognizing the trend of Vulkan becoming the dominant graphics API for Android, the team determined that Vulkan is the optimal choice for long-term app management.
- **Stable performance on low-spec devices**: To provide a smooth experience for a wide range of users, stable performance on low-spec devices is essential. Vulkan's ability to reduce CPU load is expected to improve frame rates and battery consumption.
- **Avoidance of large-scale post-release changes**: Switching from OpenGL ES to Vulkan after release would entail extensive modifications, potentially disrupting the user experience. Adopting Vulkan from the outset mitigated the need for such significant changes.

#### Implement Vulkan with Unity

Pokémon TCG Pocket uses Unity as its game engine. Unity offers a streamlined process for implementing Vulkan with a single click. By using Unity, the development team seamlessly integrated Vulkan without requiring specialized training. Additionally, the lack of Vulkan-specific adaptations for development environments and tools contributed to cost-effectiveness.
![Auto Graphics API in Unity](https://developer.android.com/static/images/cards/distribute/stories/Pokemon-TCG-Pocket-figure2.png)**Figure 2.**Auto Graphics API in Unity.

#### Challenges in implementing Vulkan

While Vulkan implementation was relatively straightforward, the development team encountered some challenges afterward:

- **Device-specific issues**: Compared to OpenGL ES, some manufacturers' drivers exhibited lower stability with Vulkan, leading to device-specific issues.
- **Incomplete Vulkan support in middleware**: Some middleware lacked full Vulkan support, requiring the team to wait for middleware updates.

The development team addressed these challenges through multiple strategies, including assembling a team of experienced consumer game developers for troubleshooting (as they were well experienced in the low-level graphics API or custom engine) and collaborating with Google and Unity teams for individual issue resolution. To expand device compatibility, testing included mid- to old high-end devices (released 2-3 years ago) to determine the[recommended device specifications](https://app-ptcgp.pokemon-support.com/hc/en-us/articles/39076135557145-What-is-the-recommended-smart-device-for-this-app "Recommended device specifications").

#### Advantages of Vulkan

Adopting Vulkan brought several benefits to Pokémon TCG Pocket:

- **Reduced shader compilation time**: Vulkan significantly reduced shader compilation time, even for a large number of shaders. For example, the OpenGL ES compilation time could exceed 1 second, but this is no longer a concern with Vulkan rendering.
- **Expanded range of supported devices**: Improvements in frame rate and battery consumption allowed for a wider range of supported devices, ensuring a smoother experience for more users.
- **Better telemetry with Vulkan validation layers** : The[Vulkan validation layer](https://developer.android.com/ndk/guides/graphics/validation-layer)was very useful in identifying the root cause of problems, supplementing the data provided by Vitals ANR/Crash reports.

#### Message to developers

The Pokémon TCG Pocket development team offers the following advice to developers considering Vulkan for their projects:

- Beyond shader compilation time reduction, Vulkan offers substantial performance benefits.
- Using[vkQuality](https://developer.android.com/games/engines/unity/unity-vkquality)to fall back to OpenGL ES could potentially expand device support, even though Pokémon TCG Pocket is not using it yet.

#### Conclusion

By embracing Vulkan, the Pokémon TCG Pocket development team was able to optimize graphics across a broad range of devices to ensure a smooth and engaging experience for every player. With ongoing feature additions and evolving future potential, Vulkan is expected to bring even more benefits over time.