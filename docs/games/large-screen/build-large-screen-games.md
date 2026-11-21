---
title: https://developer.android.com/games/large-screen/build-large-screen-games
url: https://developer.android.com/games/large-screen/build-large-screen-games
source: md.txt
---

> Documentation index: https://developer.android.com/games/llms.txt

Devices that can run Android games come in a variety of form
factors---foldables, tablets,
Android XR, Android TV, Googlebook, and Android Auto---which represent a
wide range of display sizes. Android supports
multiple display modes, including multi-window, multi-display, multi-instance,
and picture-in-picture. Foldable devices can be in various folded states, or
postures, such as tabletop posture or book posture.

![Depiction of the three quality tiers as layers stacked vertically.](https://developer.android.com/static/images/docs/quality-guidelines/quality_guidelines_header.png)

To ensure your game provides a great user experience regardless of device form
factor, screen size, display mode, or posture, follow the large screen
compatibility checklists and complete the compatibility tests.

## Why large screen instead of adaptive for games

In Android apps, *adaptive* means reflowing UI panes across arbitrary
window sizes and both orientations without letterboxing. Not every game can
adapt to all arbitrary aspect ratios or reflow a portrait game board into a
landscape layout. Instead, games render across defined anchor aspect ratios and
cleanly letterbox or pillarbox themselves outside those ratios or orientations.

The large screen quality guidelines for games parallel Android's three-tier
[adaptive app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) framework---Ready (Tier 3),
Optimized (Tier 2), and Differentiated (Tier 1)---tailored specifically for
game engines, anchor aspect ratios, continuity, and precision game inputs across
foldables and tablets.

Google Play [ranks optimized games higher than unoptimized games](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps.md.txt#google_play).
Games that don't meet at least Tier 3 requirements on specific devices might not
appear in search results unless a user searches for the game directly.

### Key concepts

The following concepts apply when building games for large screens:

- **Layout orientation**: the orientation the game uses to lay out its UI and position the camera.
- **Window orientation**: the orientation of the system window that the game renders within.
- **Large screen** : any window or display area with a smallest width of at least 600 dp (`sw >= 600dp`), which corresponds to the [`WindowSizeClass`](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass.md.txt) medium width breakpoint. This includes tablets and the unfolded inner display of foldables.
- **Input**: the game must be playable using the inputs available on a given form factor.

### Quality tiers

Games follow the same three-tier quality progression as apps: Ready, Optimized,
and Differentiated. Each form factor has specific requirements for tiering:

![Icon for Tier 3 Ready](https://developer.android.com/static/images/docs/quality-guidelines/tier-3/tier_3_icon.svg)

### [Tier 3 (Ready)](https://developer.android.com/games/large-screen/tier-3.md.txt)

Games that are Ready run full screen across their supported orientations and
anchor aspect ratios on large screens and foldables. They handle dynamic
configuration changes---including folding, unfolding, rotation, and window
resizing---without losing state or offsetting touch inputs, and they support
multi-window and multi-resume continuity. The baseline Tier 3 guidelines apply
directly to foldables and tablets.

![Icon for Tier 2 Optimized](https://developer.android.com/static/images/docs/quality-guidelines/tier-2/tier_2_icon.svg)

### [Tier 2 (Optimized)](https://developer.android.com/games/large-screen/tier-2.md.txt)

Games that are large screen optimized build upon Tier 3 as a shared horizontal
baseline to deliver an enhanced experience across tablets and foldables. They
feature proportional UI scaling and high-resolution graphics tailored for larger
displays, styled visual framing when letterboxing is used, smooth frame pacing,
and full start-to-finish playability using external controllers, keyboards, and
mice.

![Icon for Tier 1 Differentiated](https://developer.android.com/static/images/docs/quality-guidelines/tier-1/tier_1_icon.svg)

### [Tier 1 (Differentiated)](https://developer.android.com/games/large-screen/tier-1.md.txt)

While Tier 3 and Tier 2 are shared across form factors, Tier 1 is separated by
form factor so you can build an optimal experience for each device.
Guidelines are available for foldables.

## Game large screen quality tests

The compatibility tests help you discover quality issues in your game. You can
combine the tests or integrate groups of tests together in your own test plans.

For layout and UX purposes, test on at least the following device
configurations:

- **Foldables**: square-style (1:1 and 10:9 inner screen) and passport-style
  (4:3 inner screen) foldables:

  | Release year | Device model | Foldable style |
  |---|---|---|
  | 2025 | Pixel 10 Pro Fold | Square style |
  | 2025 | Samsung Z Fold 7 | Square style |
  | 2025 | Honor Magic V5 | Square style |
  | 2026 | Pixel 11 Pro Fold | Square style |
  | 2026 | Samsung Z Fold 8 | Passport style |
  | 2026 | Samsung Z Fold 8 Ultra | Square style |
  | 2026 | Honor Magic V6 | Square style |

- **Tablets**: standard (approximately 11-inch to 12.4-inch, 1280x800 dp)
  and ultra-large (approximately 13-inch to 14.6-inch, up to 1480x924 dp)
  displays:

  | Release year | Manufacturer | Device model |
  |---|---|---|
  | 2025 | Samsung | Galaxy Tab S11 |
  | 2025 | Samsung | Galaxy Tab S11 Ultra |
  | 2025 | Samsung | Galaxy Tab S11 Ultra 5G |
  | 2025 | Samsung | Galaxy Tab S11 5G |
  | 2026 | Samsung | Galaxy Tab S12 Ultra |
  | 2026 | Samsung | Galaxy Tab S12+ |