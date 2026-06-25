---
title: https://developer.android.com/distribute/aep/aep-req-picture-in-picture
url: https://developer.android.com/distribute/aep/aep-req-picture-in-picture
source: md.txt
---

Adopt Picture-in-Picture (PiP) mode to ensure that apps featuring primary video
playback, video calling, communication, or active navigation allow content to
seamlessly shrink to a floating window when a user navigates away. This
functionality is critical for modern multi-tasking, preventing a restrictive
experience where users are forced to keep an app fully open just to continue a
stream or call.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- The app must use Android's PiP APIs.
- The app must smoothly transition primary video content into PiP mode on app exit.
- Playback must continue without interruption or pausing during the transition.
- The transition must be fluid and immediate. Apps that fully close and then slowly re-open as a floating window provide a sub-par experience and don't meet the requirement.

## Guideline applicability

This guideline applies to:

- Apps that have the following use cases:
  - Video playback (including SFV and live streaming)
  - Video calling and chat
  - Maps and navigation
- Phone, tablet, foldable, and desktop form factors.

## Exemptions

Apps can use an equivalent alternative framework that provides similar quality,
user capabilities, stability and compatibility across the ecosystem.
[Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Picture-in-Picture** feature. These resources are for your reference only
and don't contain additional program requirements.

- [Picture-in-picture (PiP) in Compose](https://developer.android.com/develop/ui/compose/system/picture-in-picture)