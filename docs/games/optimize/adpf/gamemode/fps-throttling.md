---
title: https://developer.android.com/games/optimize/adpf/gamemode/fps-throttling
url: https://developer.android.com/games/optimize/adpf/gamemode/fps-throttling
source: md.txt
---

Android FPS throttling is a Game Mode intervention that helps games run at a
more stable frame rate in order to reduce battery consumption. The intervention
is available in [Android 13](https://developer.android.com/about/versions/13/get) or later.

As more Android devices ship with displays that have higher refresh rates, such
as 90 Hz and 120 Hz, most games try to pace at a high FPS. However, they usually
don't consider user preferences for prioritizing performance or battery life.
This causes several problems:

- Games that can't consistently pace at the higher FPS end up having unstable
  or uneven FPS.

- Users often don't really want to have higher FPS because the battery runs out
  too quickly.

FPS throttling is only able to *limit* the frame rate. For an
example, when a game runs at 60 FPS originally, FPS throttling intervention
cannot make it run at 120 FPS but throttling at 40 FPS and 30 FPS is valid.

FPS throttling can result in up to a 50% GPU power reduction and a 20% system
power reduction. It also helps run unpaced games at a smoother and less janky
frame rate.

An unpaced game often has higher peak frame rates but with
[higher variance](https://developer.android.com/games/sdk/frame-pacing#how-it-works) of frame time. This
significantly impacts how the performance is perceived by players. The FPS
throttling intervention only helps unpaced games achieve frame pacing from the
platform side.

The results of the FPS throttling intervention may vary based on the device
used, environmental conditions, and other factors.

## Interactions with app frame-pacing implementations

When both the app frame-pacing implementation and FPS throttling are enforced,
generally the final frame rate is the lower targeting frame rate.

> [!IMPORTANT]
> **Important:** An exception to this is when an app force sleeps the render thread to achieve frame-pacing. In this case, the FPS throttling intervention can't limit the frame rate any further.

## Get started

This section describes how to set up and use FPS throttling using
[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb).

> [!IMPORTANT]
> **Important:** Make sure your game hasn't [declared support](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api#declare_support_for_game_modes) for the Game Mode API so the FPS throttling intervention isn't overridden.

### Enable game mode interventions

To enable game mode interventions for a game, use the following command:

    adb shell device_config put game_overlay <PACKAGE_NAME> <CONFIG>

### Set the FPS intervention

​​To set the target FPS throttling intervention, use the `device_config` command.
Here's an example that sets FPS throttling for performance and battery mode:

    adb shell device_config put game_overlay <PACKAGE_NAME> mode=2,fps=90:mode=3,fps=30

Details of the parameters:

- `mode` \[2\|3\]: `2` and `3` for performance and battery mode
- `fps` \[0\|30\|40\|45\|60\|90\|120\]: depending on the device you are using (whether a 120, 90, or 60 Hz device), we recommend choosing the frame rates that are divisors of the device's maximum refresh rate. `0` is the default value.

Here are the frame rates that each display type supports:

- 60 Hz displays: 60 FPS, 30 FPS
- 90 Hz displays: 90 FPS, 45 FPS, 30 FPS
- 120 Hz displays: 120 FPS, 60 FPS, 40 FPS, 30 FPS

### Get results

To view and analyze the results, you can inspect the FPS counter or capture
a Perfetto trace. Here's example of how to view the FPS counter in a game that
is running at 120 FPS:

#### View the FPS counter

To verify your FPS throttling settings, you can run the game and open the FPS
counter in Game Dashboard. To do so, follow these steps:

1. While running your game, swipe down and the press Game Dashboard icon.

2. Turn on the FPS counter by pressing the **FPS** button.

3. Close Game Dashboard by pressing the **X** button. Swipe right on the arrow
   to display the FPS counter.

#### Capture a Perfetto trace

To get an in-depth look at the performance of your game, we recommend you
perform a Perfetto trace. For more information on performing a trace, see
[Quickstart: Record traces on Android](https://perfetto.dev/docs/quickstart/android-tracing).

When you perform a trace, use the `android.game_interventions` data source.
After the trace completes, the **trace viewer** page is displayed. In the
navigation bar, select **Info and stats** and then view the **Game mode and
intervention** list. For example:

![Example of intervention list table](https://developer.android.com/static/games/optimize/adpf/gamemode/images/fps-throttling-perfetto-intervention-list-table.png)

FPS throttling interventions are shown in the format of "fps=X", where `X` is
the throttling FPS in a specific game mode. `0` is the default value.