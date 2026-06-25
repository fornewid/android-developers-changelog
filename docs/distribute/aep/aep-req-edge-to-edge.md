---
title: https://developer.android.com/distribute/aep/aep-req-edge-to-edge
url: https://developer.android.com/distribute/aep/aep-req-edge-to-edge
source: md.txt
---

Implement edge-to-edge drawing by default to maximize screen space and achieve a
modern, premium, bezel-less aesthetic. By extending the UI canvas behind the
system navigation and status bars, apps provide a more immersive experience
fundamental to a high-quality feel.

## Required implementation

To qualify for AEP, you app must adhere to the following requirements:

- The core interactive UI doesn't intersect system bars on the home-screen.
- The app draws behind transparent status bars and gesture navigation bars.
- The app doesn't have existing Play Console warnings or alerts related to edge-to-edge.
- To attain a contemporary, bezel-less aesthetic look, system bars should be rendered as transparent rather than solid.

## Guideline applicability

This requirement applies to all apps that want to qualify for AEP on the phone,
tablet, foldable, desktop, and XR form factors.

## Exemptions

There are no exemptions for this guideline.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Edge-to-Edge** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Edge-to-Edge enforcement](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge)
- [Display content edge-to-edge in views](https://developer.android.com/develop/ui/views/layout/edge-to-edge)
- [About window insets](https://developer.android.com/develop/ui/compose/layouts/insets)