---
title: https://developer.android.com/develop/adaptive-apps/guides/googlebook/overview
url: https://developer.android.com/develop/adaptive-apps/guides/googlebook/overview
source: md.txt
---

Googlebooks are built on the Android technology stack and ChromeOS desktop
foundations.

Googlebooks combine mobile convenience with desktop capabilities, featuring
high-resolution touchscreens, dedicated keyboards, precision trackpads, all-day
battery life, and OS-level Gemini integration.

With Googlebook, users can transition from quick interactions on their phones to
extended, immersive sessions in a desktop environment.

## Adapt your app

You don't need to build a separate app from the ground up to support Googlebook.
Adaptive development enables Android apps to scale across large displays and
laptop form factors from a single codebase.

If your app already implements adaptive layouts, window size classes, and
multi-input support, you can build directly on that solid foundation.
![Wireframe diagram comparing a single-column mobile screen with a two-pane desktop layout.](https://developer.android.com/static/develop/adaptive-apps/images/googlebook/multipane-layout.png) **Figure 1.** Adaptive layouts reorganizing mobile views into a multi-pane desktop experience.

See:

- [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)
- [Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes)
- [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

## Get noticed on Google Play

Optimizing your app for Googlebook expands its visibility across the Android
ecosystem:

- **Storefront discovery:** Google Play highlights optimized titles with
  dedicated badging, enhanced search, and featured placements across curated
  store homepages.

- **Program incentives:** Delivering desktop-optimized quality prepares your
  app for the [Apps Experience Program](https://developer.android.com/distribute/aep), where you can enroll to access a
  program rate card designed to support business growth.

- **Device setup transfer:** When users sign in to set up a Googlebook, their
  Android phone's settings, saved passwords, Wi-Fi networks, and messages sync
  with end-to-end encryption, and optimized apps are highlighted for transfer
  during onboarding.

![Google Play storefront showing collections of apps and games with Optimized for desktop badges.](https://developer.android.com/static/develop/adaptive-apps/images/googlebook/play-desktop-badges.png) **Figure 2.** Apps optimized for desktop badging and dedicated collections on Google Play.

See:

- [Increase app availability across device types](https://developer.android.com/develop/adaptive-apps/guides/increase-app-availability)
- [Adaptive app quality guidelines](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality)

## Build on desktop fundamentals

On Googlebook, your app operates in a desktop environment alongside a
desktop-class Chrome browser and system tools. Instead of stretching mobile
interfaces across a wide screen, reorganize content into functional groupings
for higher information density, precision input, and active multitasking.

### Adopt a multi-pane architecture

Design your app UI to expand, reflow, or reveal additional detail as window
boundaries change:

- **Coordinate adaptive scenes:** With [Navigation 3](https://developer.android.com/guide/navigation/navigation-3), implement
  [`ListDetailSceneStrategy`](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-listdetail) and
  [`SupportingPaneSceneStrategy`](https://developer.android.com/guide/navigation/navigation-3/recipes/material-supportingpane) to coordinate
  side-by-side panes directly from your back stack when expanded window space
  is available.

- **Add persistent navigation:** Use [scene decorators](https://developer.android.com/guide/navigation/navigation-3/scenes/scene-decorators) to wrap screens with
  persistent desktop navigation rails.

- **Organize complex content:** Pair scene strategies with layout primitives
  such as [`Grid`](https://developer.android.com/develop/adaptive-apps/guides/grid) and [`FlexBox`](https://developer.android.com/develop/adaptive-apps/guides/flexbox), along with experimental
  [`mediaQuery`](https://developer.android.com/reference/kotlin/androidx/compose/ui/mediaQuery.composable) and [Styles](https://developer.android.com/develop/ui/compose/styles) APIs, to arrange content and
  adjust visual styles dynamically for desktop displays.

See:

- [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)
- [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)
- [Build a supporting pane layout](https://developer.android.com/develop/adaptive-apps/guides/build-a-supporting-pane-layout)

### Respond to dynamic window sizes and desktop ergonomics

In free-form desktop windowing, users can resize app windows dynamically at any
time. Make your app adaptable to window size changes with:

- **Window size classes:** Base your layout decisions on available window
  space using [window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) rather than physical display dimensions.

- **Typography and target sizing:** Adjust your type scale for desktop viewing
  distances, set layout maximum widths to keep line lengths readable, define
  explicit click targets to prevent misclicks, and explore layout patterns in
  the [desktop design gallery](https://developer.android.com/design/ui/gallery?keywords=form_desktop).

![Diagram illustrating Compact, Medium, Expanded, Large, and Extra-large width window size class breakpoints.](https://developer.android.com/static/develop/adaptive-apps/images/googlebook/window-size-classes.png) **Figure 3.** Representations of width-based window size classes.

See:

- [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability)
- [Query information for adaptive layouts with mediaQuery](https://developer.android.com/develop/adaptive-apps/guides/mediaquery)
- [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)

## Deliver differentiated experiences for Googlebook

Once your core layout is adaptive, enrich your app with features specific to
Googlebook's hardware and desktop environment.

### Support precision input and keyboard shortcuts

Jetpack Compose natively supports physical keyboard navigation and pointer
selection. Optimize for Googlebook's backlit keyboards, haptic glass trackpads,
and external mice with the following:

- **Contextual cursors:** Integrate [contextual cursors](https://developer.android.com/guide/topics/large-screens/cursors) for text entry,
  pane resizing, and tool selection.

- **Pointer interactions:** Implement right-click context menus and hover
  states for interactive elements.

- **Keyboard shortcuts:** Make your app's keyboard shortcuts discoverable
  through the [Keyboard Shortcuts Helper](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper).

See:

- [Input compatibility on large screens](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens)
- [Handle keyboard actions](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands)
- [Pointer input in Compose](https://developer.android.com/develop/ui/compose/touch-input/pointer-input)

> [!NOTE]
> **Note:** For information on custom input methods and launchers, see [Keyboard apps
> and launcher compatibility](https://developer.android.com/develop/adaptive-apps/guides/googlebook/keyboard-apps-and-launcher-compatibility).

### Enable multi-instance workflows and drag and drop

On Googlebook, apps run in free-form windows where users work across multiple
tasks simultaneously.
![Android desktop task switcher showing multiple running app windows.](https://developer.android.com/static/develop/adaptive-apps/images/googlebook/task-switcher.png) **Figure 4.** Task switcher displaying multiple open windows and app instances.

Extend the user experience with these features:

- **Multi-instance support:** Enable users to launch independent windows of
  your app side by side to compare content or manage multiple documents.

- **Cross-window drag and drop:** Pair multi-instance support with [drag and
  drop](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop) so users can move text, images, and files between windows or drop
  items onto an empty workspace to start a task.

- **Customizable header bars:** Style your [app bars](https://developer.android.com/develop/ui/compose/components/app-bars) with custom
  backgrounds, search bars, or tabs inside the desktop caption header bar
  while respecting system window controls.

  ![Illustration of a user dragging an item from one free-form app window and dropping it into another window.](https://developer.android.com/static/develop/adaptive-apps/images/googlebook/drag-and-drop.png) **Figure 5.** Multi-window multitasking with cross-window drag and drop.

See:

- [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)
- [Support multi-window mode](https://developer.android.com/develop/adaptive-apps/guides/support-multi-window-mode)
- [Support connected displays](https://developer.android.com/develop/adaptive-apps/guides/support-connected-displays)

### Connect devices and tap into Gemini intelligence

Googlebook is the perfect companion for your Android phone with features like:

- **Cross-device handoff and continuity:** Use [Continue On](https://developer.android.com/develop/better-together/continue-on) so users can
  pick up tasks from their Android phone directly from the Googlebook taskbar.

  Pass state through `HandoffActivityData` to preserve context such as
  document position or active tabs, with optional web fallbacks.

  > [!NOTE]
  > **Note:** Googlebook also connects with Android phones through cross-device file access in the *Files* app and phone app streaming with *Cast My Apps*.

- **Desktop widgets and built-in intelligence:** Surface glanceable,
  actionable content with customizable [widgets](https://developer.android.com/design/ui/widget) that complement
  Googlebook's desktop environment and built-in Gemini tools (such as Magic
  Pointer, Rambler, and Create My Widget).

Evaluate your implementation against the [desktop app quality guidelines](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/experiences/desktop) to
verify that your app meets desktop usability standards.

See:

- [Support cross-device continuity on Googlebook](https://developer.android.com/develop/adaptive-apps/guides/googlebook/cross-device-continuity)
- [Enable and customize cross-device handoff](https://developer.android.com/develop/better-together/continue-on/enable-support)
- [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance)

## Accelerate your workflow with dedicated tooling

Testing and optimizing your app for Googlebook integrates directly into your
development workflow:

- **Desktop emulator in Android Studio:** Run a virtual desktop environment on
  your workstation to test free-form window resizing, verify multi-instance
  interactions, and debug mouse, trackpad, and keyboard input using [Android
  Studio preview](https://developer.android.com/studio/preview).

- **On-device Linux and agentic development:** Googlebook includes an isolated
  Linux terminal environment powered by a Level 5 security-certified pKVM
  hypervisor, along with the Antigravity development platform and CLI tools so
  you can build, test, and deploy apps directly on the device.

- **AI-assisted layout modernization:** Install the [adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) through
  the [Android CLI](https://developer.android.com/tools/agents/android-cli) to give AI coding agents context for refactoring mobile
  layouts into responsive Compose containers.

See:

- [ADB debugging on Googlebook](https://developer.android.com/develop/adaptive-apps/guides/googlebook/adb-debugging)
- [Test different screen and window sizes](https://developer.android.com/training/testing/different-screens)
- [Preview your UI with composable previews](https://developer.android.com/develop/ui/compose/tooling/previews)
- [Overview of Android skills](https://developer.android.com/tools/agents/android-skills)