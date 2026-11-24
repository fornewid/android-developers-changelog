---
title: https://developer.android.com/jetpack/androidx/compose-roadmap
url: https://developer.android.com/jetpack/androidx/compose-roadmap
source: md.txt
---

> Documentation index: https://developer.android.com/jetpack/androidx/llms.txt

Last updated: November 2026

Welcome to the Jetpack Compose roadmap, outlining upcoming plans for Jetpack
Compose. For completed features, please see [release notes](https://developer.android.com/jetpack/androidx/releases/compose.md.txt).

These are the features that the team is currently thinking about and working on.
This roadmap is shared with the best intent, however, it's not exhaustive and
priorities might change as we learn more and continue to get feedback from you -
our users.

*In Focus* items are being worked on soon and are likely to land in an upcoming
stable release. *Backlog* items are planned but not likely to land soon.

## Core Libraries

|---|---|---|---|
| **Area** | **In Focus** | **Backlog** | **Done** |
| Material 3 | Scrollbars Styles integration with Material 3 Bottom sheet improvements and bug fixes Adaptive Components | Motion Subsystem M3 Component updates | Stabilize Material 3 Expressive Components Focus indications Adaptive Navigation 3 integration Pickers Tooltips SearchBar Bottom sheets |
| Foundation | Styles (Experimental) UIMediaQuery (Experimental) Gesture disambiguation |   | FlexBox layout Grid layout Stabilize LazyLayoutCacheWindow Drag and drop support in Lazy layouts Stabilize AnchoredDraggable Public API for anchored components |
| Graphics | Export portion of Bitmap | Improvements to AVDs Blur improvements Advanced Graphical Effects Performance improvements: shadows, ripples | Mesh Gradients GraphicsLayer Outsets Wide Color Gamut and HDR support Progressive blur and Dialog/Popup window blurs Polygon shapes and morphing Performance improvements: vector caching Drop shadows and inner shadows |
| Text | Text selection and API improvements Multistyle text editing | Support all IME flags | Support Variable fonts using downloadable fonts Programmatic text selection (SelectionState) Editable text formatting (BasicTextField) Credential Manager integration Per-line line height Smart text selection and linkify Support autosize Text Autofill Hardware keyboard input Styled string resources Support Drag \& Drop across screens Clickables in text AccessibilityChecks |
| Animation | Layout animation visual debugging (Experimental) Advanced layout animation |   | DeferredTransition and DeferredTargetAnimation CapturedAnimatedVisibility Shared element transitions Shared element visual debugging LazyList Item Animations |
| Compiler \& Runtime | SlotTable Rewrite (Experimental) LazyList Scheduling / Thread Utilization | Modifier Hoisting Optimization Shared SlotTable for Subcompositions | Keyed SideEffect computedStateOf Recomposition tracing External Type Stability Configuration Group Eliding Optimizations Strong Skipping Mode Intrinsic Remember Support multithreaded scheduler |
| Testing | Screenshot testing improvements | Support Common tests | Support Multi modal input injection Test synchronization APIs (hasPendingWork, runWithoutImplicitWait) Stabilize ComposeUiTest APIs and custom failure handling Standard Test dispatcher Accessibility Checks for Compose |
| Performance | Startup performance |   | Time to Initial Display (TTID) startup performance on par with Views Scroll performance (with respect to jank) is on par with Views since Compose 1.9.0 |
| Tools | GenAI \& UI development experiments Ongoing Quality \& Performance improvements | More advanced Animation / Navigation support (Concepting) | Glance Widgets Preview @Preview Screenshot Testing Preview Organization \& Zoom [Compose Preview](https://developer.android.com/jetpack/compose/tooling/previews) [Animation Preview](https://developer.android.com/jetpack/compose/tooling/animation-preview) [Interactive mode](https://developer.android.com/jetpack/compose/tooling/previews#preview-interactive) [Multipreview Templates](https://developer.android.com/jetpack/compose/tooling/previews#multipreview-templates) [Preview Parameters](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewParameter.md.txt) [Live Edit](https://developer.android.com/jetpack/compose/tooling/iterative-development#live-edit) [Compose UI Check](https://twitter.com/androidstudio/status/1716549517363880225) [Layout Inspector: Recomposition Counts \& Highlights](https://developer.android.com/jetpack/compose/tooling/layout-inspector) |

## Platforms

|---|---|---|
| **Platform** | **In Focus** | **Done** |
| Homescreen widgets |   | [Compose API](https://goo.gle/glance) |
| TV Compose |   | [Compose API](https://developer.android.com/jetpack/androidx/releases/tv.md.txt) |

## Proposals

If you would like to propose an item for consideration for inclusion on the
roadmap please review [existing proposals](https://issuetracker.google.com/issues?q=hotlistid:3426315+status:open) or [create a new
one](https://issuetracker.google.com/issues/new?component=612128&template=1604926).