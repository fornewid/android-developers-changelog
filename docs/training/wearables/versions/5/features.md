---
title: https://developer.android.com/training/wearables/versions/5/features
url: https://developer.android.com/training/wearables/versions/5/features
source: md.txt
---

# Explore features

Wear OS 5 introduces several features to help enhance your Wear OS app experience. Before you add these features to your app,[prepare your app](https://developer.android.com/training/wearables/versions/5/changes)for compatibility with Wear OS 5.  
![App launcher icons appear next to each other both vertically and horizontally](https://developer.android.com/static/wear/images/grid-app-launcher.png)**Figure 1.**The grid-based app launcher view that's supported on devices that run Wear OS 5 and higher.

## Grid-based app launcher

Wear OS 5 introduces a built-in, system-provided app launcher that resembles a grid. As shown in figure 1, this grid-based app launcher is visually similar to several launchers that device manufacturers already offer on Wear OS.

In system settings (in the "General" section), users can choose between this grid-based app launcher and the list-based app launcher that appears on previous versions of Wear OS. Alternatively, go to the bottom of the app launcher view, and select the "grid" or "list" icon.

To provide the best possible experience for launcher icons, follow the[adaptive icon](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive)guidance.

## Let user choose media output device

Starting in Wear OS 5, the system UI that[lets users choose](https://developer.android.com/training/wearables/apps/audio#let-user-choose)which device should play media and show information about the currently-playing media content.

## Enhancements to Watch Face Format

Watch Face Format version 2 is supported for devices that run Wear OS 5 or higher. This version includes several enhancements, including the following:

- **[Flavors](https://developer.android.com/training/wearables/wff/user-configuration/flavor):**Preset configurations for your watch face that users can browse in a companion app.
- **Goal progress complication type:**Useful when users can exceed a goal such as step count.
- **Weighted elements complication type:**Useful for showing discrete subsets of data.
- **[Weather conditions](https://developer.android.com/training/wearables/wff/weather):**Show the current weather, as well as forecast conditions for hours or days into the future.
- A**heart rate**system data source.

Learn more about the[Watch Face Format](https://developer.android.com/training/wearables/wff). In the[XML reference](https://developer.android.com/training/wearables/wff/watch-face), look for items that changed in version 2.

## Screenshot detection

Android 14, and by extension Wear OS 5, introduces a privacy-preserving[screenshot detection API](https://developer.android.com/about/versions/14/features/screenshot-detection).

## Updates to Health Services

Wear OS 5 introduces the following additions to help you measure health and fitness data more precisely and effectively.

### More detailed running metrics

As of Wear OS 5, Health Services supports additional data types related to running, including the following:

- **Ground contact time:**The amount of time, during a single step, that a runner's foot is in contact with the ground.
- **Stride length:**The distance covered by a single step.
- **Vertical oscillation:**The distance that a user's center of mass moves up and down with each step.
- **Vertical ratio:**Vertical oscillation divided by stride length.

As with all data types that Health Services supports, you should[check exercise capabilities](https://developer.android.com/health-and-fitness/guides/health-services/compatibility)to confirm they are supported on the device running your app.

### Debounced goals

Starting in Wear OS 5, Health Services supports[debounced goals](https://developer.android.com/health-and-fitness/guides/health-services/active-data/debounced-goals)to help improve the user experience for people who want to maintain a specific threshold or range---such as heart rate---throughout their workout.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Some hardware buttons can be app-context-aware {:#app-context-aware-buttons}](https://developer.android.com/training/wearables/versions/5/app-context-aware-button)