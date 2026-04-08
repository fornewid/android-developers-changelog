---
title: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables
source: md.txt
---

Foldable devices enable a unique user experiences, transitioning smoothly
between compact phone-sized screens and expansive tablet-like displays.
Foldables introduce unique physical states, or postures, such as tabletop and
book posture, that apps can take advantage of to offer specialized layouts and
enhanced multitasking capabilities.

## Guidelines

Create a premium user experience on premium foldable devices.

### Postures and states

| ID | Tests | Description |
|---|---|---|
| Foldables_Postures | [T-Foldables_Postures](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_Postures) | App supports all foldable postures and related use cases: - Tabletop posture --- Video calling and video or audio playback. - Book posture --- Reading lengthy text content. See [Learn about foldables](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables). |
| Foldables_Camera | [T-Foldables_Camera](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_Camera) | Camera apps adjust their preview for folded and unfolded states and support front and back screen preview. |

### Multitasking and multi-instance

| ID | Tests | Description |
|---|---|---|
| Foldables_Multitasking_Scenarios | [T-Foldables_PiP](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_PiP) and [T-Foldables_Attachments](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_Attachments) | App supports various multitasking scenarios, for example: - Picture-in-picture mode: With the device folded and unfolded,app is able to enter and exit picture‑in‑picture mode in portrait and landscape orientations and in multi‑window mode. See [Picture-in-picture (PiP) support](https://developer.android.com/guide/topics/ui/picture-in-picture). - Attachments: Messaging apps can open attachments (such as videos) in a separate window with the device folded and unfolded. |
| Foldables_PiP | [T-Foldables_PiP](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_PiP) | App supports interactive picture‑in‑picture functionality that enables custom controls and user interaction. |
| Foldables_Multi-Instance | [T-Foldables_Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_Multi-Instance) | In folded and unfolded device states, the app is able to launch multiple instances of itself in separate windows. See [Multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance) in [Support multi-window mode.](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) |

## Tests

To verify that your app provides a differentiated experience on foldable
devices, complete the following tests.

### Foldable postures and states

| ID | Feature | Description |
|---|---|---|
| T-Foldables_Postures | [Foldables_Postures](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Postures) | View the app in all foldable postures, including tabletop and book postures. Verify that UI elements transition to the optimal location (for example, media controllers move to the horizontal screen area in tabletop posture). |
| T-Foldables_Camera | [Foldables_Camera](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Camera) | Activate the camera from within the app. Verify that the camera preview is correct when the device is folded and unfolded and rotated to portrait and landscape orientations. With the device unfolded, verify that the preview is correct on front and back screens. |

### Multitasking and multi-instance

| ID | Feature | Description |
|---|---|---|
| T-Foldables_PiP | [Foldables_Multitasking_Scenarios](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Multitasking_Scenarios) | With the device folded and unfolded, enter and exit picture‑in‑picture mode in portrait and landscape orientations and in multi‑window mode. In multi‑window mode, change the window size while picture‑in‑picture mode is active. In picture-in-picture mode, interact with any custom controls and verify their functionality. |
| T-Foldables_Attachments | [Foldables_Multitasking_Scenarios](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Multitasking_Scenarios) | With the device folded and unfolded, open and close attachments and notifications in portrait and landscape orientations and in multi‑window mode. |
| T-Foldables_Multi-Instance | [T-Foldables_Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#T-Foldables_Multi-Instance) | With the device folded and unfolded, launch multiple instances of the app in separate windows in portrait and landscape orientations and in multi‑window mode. |