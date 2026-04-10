---
title: https://developer.android.com/games/optimize/adpf/best-practices-adpf
url: https://developer.android.com/games/optimize/adpf/best-practices-adpf
source: md.txt
---

The [Android Dynamic Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf) helps developers
proactively manage device thermals and performance by letting games interact
with the system, receive thermal insights (like predicted headroom), and
influence behavior. Intelligent adaptation using ADPF prevents severe throttling
and enables smoother, longer gameplay. This guide provides practical strategies
to use ADPF effectively. It focuses on custom, granular scaling tied
directly to your game's specific quality settings and driven by ADPF thermal
data. By implementing these practices, you can proactively manage thermalsand
create games that perform better for longer-which results in a more reliable
and enjoyable experience for players.

## Customize performance scaling

Default ADPF plugin scaling might target generic engine presets, for example,
Low, Medium and High. If your game uses unique graphic quality options that are
different from these defaults, the plugin's assumptions won't match your
content. You must customize ADPF logic to directly control your game's specific
quality settings for effective thermal management, rather than relying on
mismatched defaults. Create fine-grained scaling logic using ADPF data for
better results:

- **Identify key levers**: Profile your game to find which graphics or gameplay features (shadows, resolution, particles, effects, view distance) most impact performance and heat.
- **Develop granular steps**: Define small, incremental adjustments for individual settings within your game's quality options. Gradually apply these changes based on thermal feedback from ADPF (for example, utilizing thermal headroom data) to gently ease pressure on the system before severe throttling occurs.

Your browser doesn't support the video tag. Rendering problem with ADPF in [Unity MegaCity Metro](https://github.com/Unity-Technologies/megacity-metro/tree/demo/vulkan).

The preceding video shows a rendering problem with ADPF in
[Unity MegaCity Metro](https://github.com/Unity-Technologies/megacity-metro/tree/demo/vulkan). Because ADPF adjusts the view distance based on a
general game engine range, rather than a range suited for the specific game
content, the view distance becomes excessively low when the device heats up,
which causes an issue where buildings are no longer visible.

## Isolate graphics settings

Avoid drastic preset changes. Adjusting individual graphics settings
independently provides finer control and a smoother experience when responding
to thermal conditions. Here are some tips when adjusting settings:

- **Prioritize impact**: Focus scaling efforts on settings within your quality options having the most significant thermal or performance impact identified during profiling.
- **Decouple settings**: Modify settings like shadows, resolution, and particles independently and sequentially as needed.
- **Smooth transitions**: Where feasible, transition visual settings gradually over a few frames to be less jarring.

Check how [Netmarble used the ADPF to optimize "Game of Thrones: Kingsroad"](https://developer.android.com/stories/games/netmarble-got-adpf).
They implemented dynamic resolution scaling and adaptive frame rate adjustments.

## Provide user control

Some players prefer consistent visuals over dynamic adjustments. Offer an option
to disable ADPF-driven scaling:

- **Implement an option**: Add a clearly labeled setting (for example, "Enable Dynamic Performance Adjustment") in your graphics menu.
- **Explain the choice**: Briefly describe that it enables automatic quality adjustments for smoother performance and thermal management.
- **Define behavior**: When enabled (recommended default), your custom ADPF scaling logic runs. When disabled, the game uses only the user's manually selected settings and ignores thermal data for scaling.

## Test across devices

Android hardware varies significantly in thermal capacity and performance. Test
thoroughly across different device types:

- **[Define device tiers](https://developer.android.com/games/distribute/guide-launch-game)**: Test on representative high-end, mid-range, and low-end devices from various manufacturers and SoC vendors.
- **Test thermal response**: Observe how different devices handle load and how effective your ADPF logic (and the user toggle) is on each tier.
- **Validate performance targets**: Ensure the game meets performance goals on each tier with ADPF active, and behaves predictably when disabled.
- **Gather feedback**: Use beta programs to collect performance and thermal data from diverse real-world devices.

## Monitor performance and iterate

Implementing ADPF requires ongoing monitoring and refinement to balance
sustained performance, thermal limits, and visual quality:

- **Establish baselines and targets**: Define acceptable performance (target FPS, frame times) and measure behavior without ADPF logic first.
- **Use profiling tools**: Regularly use the Android Studio Profiler, GPU vendor tools, and in-game overlays to track FPS, frame times, and ADPF thermal data during gameplay.
- **Experiment and tune**: Test different ADPF response strategies. Adjust how quickly and aggressively settings scale based on thermal input to find the optimal balance for your game.
- **Test long sessions**: Ensure testing includes extended playtime (15+ minutes) to observe sustained load performance and thermal stabilization with ADPF active.