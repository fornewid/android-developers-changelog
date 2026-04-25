---
title: https://developer.android.com/jetpack/androidx/compose-roadmap
url: https://developer.android.com/jetpack/androidx/compose-roadmap
source: md.txt
---

Last updated: April 2026

Welcome to the Jetpack Compose roadmap, outlining upcoming plans for Jetpack
Compose. For completed features, please see [release notes](https://developer.android.com/jetpack/androidx/releases/compose).

These are the features that the team is currently thinking about and working on.
This roadmap is shared with the best intent, however, it's not exhaustive and
priorities might change as we learn more and continue to get feedback from you -
our users.

*In Focus* items are being worked on soon and are likely to land in an upcoming
stable release. *Backlog* items are planned but not likely to land soon.

## Core Libraries

|---|---|---|---|
| **Area** | **In Focus** | **Backlog** | **Done** |
| Material 3 | Scrollbars Styles integration with Material 3 Stabilize Material 3 Expressive Components Bottom sheet improvements and bug fixes Focus indications Adaptive Components | Motion Subsystem M3 Component updates |
| Foundation | Styles (Experimental) FlexBox layout (Experimental) Grid layout (Experimental) UIMediaQuery (Experimental) Gesture disambiguation |   | Drag and drop support in Lazy layouts Stabilize AnchoredDraggable Public API for anchored components |
| Graphics | Mesh Gradients GraphicsLayer Outsets Export portion of Bitmap Performance improvements: vector caching | Improvements to AVDs Blur improvements Advanced Graphical Effects Performance improvements: shadows, ripples | Drop shadows and inner shadows |
| Text | Text selection and API improvements Multistyle text editing | Support all IME flags Support Variable fonts via downloadable fonts Text selection and API improvements | Smart text selection and linkify Support autosize Text Autofill Hardware keyboard input Styled string resources Support Drag \& Drop across screens Clickables in text AccessibilityChecks |
| Animation | Layout animation visual debugging Advanced layout animation |   | Shared element transitions Shared element visual debugging LazyList Item Animations |
| Compiler \& Runtime | SlotTable Rewrite LazyList Scheduling / Thread Utilization | Modifier Hoisting Optimization Shared SlotTable for Subcompositions | External Type Stability Configuration Group Eliding Optimizations Strong Skipping Mode Intrinsic Remember Support multithreaded scheduler |
| Testing | Screenshot testing improvements | Support Multi modal input injection Support Common tests | Standard Test dispatcher Accessibility Checks for Compose |
| Tools | GenAI \& UI development experiments Ongoing Quality \& Performance improvements | More advanced Animation / Navigation support (Concepting) | Glance Widgets Preview @Preview Screenshot Testing Preview Organization \& Zoom [Compose Preview](https://developer.android.com/jetpack/compose/tooling/previews) [Animation Preview](https://developer.android.com/jetpack/compose/tooling/animation-preview) [Interactive mode](https://developer.android.com/jetpack/compose/tooling/previews#preview-interactive) [Multipreview Templates](https://developer.android.com/jetpack/compose/tooling/previews#multipreview-templates) [Preview Parameters](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewParameter) [Live Edit](https://developer.android.com/jetpack/compose/tooling/iterative-development#live-edit) [Compose UI Check](https://twitter.com/androidstudio/status/1716549517363880225) [Layout Inspector: Recomposition Counts \& Highlights](https://developer.android.com/jetpack/compose/tooling/layout-inspector) |

## Platforms

|---|---|---|
| **Platform** | **In Focus** | **Done** |
| Homescreen widgets |   | [Compose API](https://goo.gle/glance) |
| TV Compose |   | [Compose API](https://developer.android.com/jetpack/androidx/releases/tv) |

## Proposals

If you would like to propose an item for consideration for inclusion on the
roadmap please review [existing proposals](https://issuetracker.google.com/issues?q=hotlistid:3426315+status:open) or [create a new
one](https://issuetracker.google.com/issues/new?component=612128&template=1604926).