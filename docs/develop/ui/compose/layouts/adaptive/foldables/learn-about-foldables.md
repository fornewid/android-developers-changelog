---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables
source: md.txt
---

Foldable devices provide an opportunity for innovative app development. Large
and small screens on the same device offer complementary but distinct
interactive experiences. Folding features such as tabletop posture and book
posture enable imaginative layouts and unconventional user interfaces.
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/foldables/foldable_multiple_postures.png) **Figure 1.** Foldable device in multiple postures: folded, open flat, open flat rotated to landscape, and half opened (tabletop).

## Responsive/adaptive design

Support for foldable devices begins with responsive design. Responsive layouts
enable an app to look and work great on a range of display sizes. Implement
responsive design with the [`BoxWithConstraints`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#BoxWithConstraints(androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)) composable.

But to optimally support the folded and unfolded screens of a foldable device,
the layout needs to adapt. The differences in screen size and aspect ratio of
folded and unfolded screens can be quite large, such that even a responsive
layout can't adequately accommodate both displays. Adaptive design creates
alternative layouts optimized for different screen sizes and configurations.
Adaptive layouts provide an optimized user experience when a foldable device is
folded or unfolded, in portrait or landscape orientation, or in tabletop or book
posture.

For example, a large screen foldable device unfolded in landscape orientation is
like a tablet; a two‑pane layout with a navigation rail makes excellent
use of the wide screen. Folded, the device is similar to a standard phone; a
single column layout with a bottom navigation bar is straightforward but
effective. Because the layouts are separate, you can optimize each for its
specific use case.
Your browser doesn't support the video tag. **Figure 2.** Adaptive layouts optimized for both folded and unfolded screens.

Foldable devices fold in a variety of ways, such as inward, with the display
folding into the interior of the device, or outward, with the display wrapping
around the device. Responsive/adaptive design prepares your app to support all
kinds of foldable form factors.

To learn more about responsive/adaptive design for foldables, see the following:

- [Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)
- Material Design --- [Applying layout](https://m3.material.io/foundations/layout/applying-layout/window-size-classes)

## Foldable states and postures

The fold of a foldable device divides the screen into two portions. The fold can
be a flexible area of the screen or, on dual‑screen devices, a hinge that
separates the two displays.

The fold has dimension and an [`occlusionType`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.OcclusionType) property, which defines
whether the fold obscures part of the display. On dual‑screen devices, the
`occlusionType` is `FULL`, no content is viewable in the fold (hinge) area even
though an app might span both screens.

Foldable devices can be in various folded states, such as [`FLAT`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#FLAT()) (fully
open) or [`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED()) (somewhere between fully open and completely closed).
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/foldables/foldable_postures_flat_and_half_opened.png) **Figure 3.** Foldable device in flat and half-opened states.

When a device is in the `HALF_OPENED` state, two postures are possible,
depending on the orientation of the fold: tabletop posture (horizontal fold) and
book posture (vertical fold).

Tabletop and book postures offer new layout possibilities, but the `HALF_OPENED`
device state also imposes some limitations. For example, UI controls near the
fold can be difficult for users to access, and text overlaying the fold can be
hard to read (or unreadable if `occlusionType` is `FULL`).

Design your layouts so that UI elements are accessible in all device states.
Position dialog boxes and pop‑up menus so they don't overlay the fold.
Make sure important content is viewable when the device is partially folded.
Split content into two areas when the device is half opened---top and bottom
in tabletop posture, left and right in book posture.

For more information about folds and foldable postures, see [Make your app fold
aware](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware).

## App continuity

An app stops and restarts as it transitions from one screen to another when a
device folds or unfolds. To maintain continuity for the user, the app should
restore its state when recreating the app layout on a folded or unfolded screen.
For example, apps should do the following:

- Retain text typed into input fields
- Restore the keyboard state
- Restore the scroll position of scrollable fields
- Resume media playback where it left off when the app was stopped

The different screen layouts of a foldable device should also complement one
another. For example, if the folded screen shows an image and description for a
product from an online store, the unfolded screen should maintain continuity by
showing the same image and description, but also include complementary content,
such as product specifications or reviews.

To learn more about managing app state and continuity, see [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
and [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).

## Multitasking

Large screen foldables have a tablet‑sized screen that's ideal for
multitasking in multi‑window mode. Foldables support split‑screen
mode; some even support desktop windowing mode, where apps are contained in
movable, resizable windows, similar to a desktop windowing system.

|---|---|
| ![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/foldables/large_foldable_unfolded_vertically_light.png) | ![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/foldables/large_foldable_unfolded_vertically_desktop_windows.png) |
| **Figure 4.** Foldable device in landscape orientation running three apps in split-screen mode (left) and desktop windowing mode (right). ||

Android 12 (API level 31) and later versions default to multi‑window mode---on large screens, all apps run in multi‑window mode regardless of app configuration. On previous versions down to Android 7.0 (API level 24), you must configure your app to be resizable to support multi‑window mode.

For information about multitasking in multi‑window mode, see [Support
multi-window mode](https://developer.android.com/guide/topics/ui/multi-window).

## Drag and drop

Large screen foldable devices provide ample screen space for drag and drop
interactions. Multi‑window mode on foldables enables drag and drop between
apps.

Drag and drop interactions create a productive and engaging user experience. Add
drag and drop capabilities to your app using the Android drag and drop
framework. For more information, see [Enable drag and drop](https://developer.android.com/guide/topics/ui/drag-drop).

## Additional resources

- [Test different screen and window sizes](https://developer.android.com/training/testing/different-screens)