---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/confirmation-overlay
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/confirmation-overlay
source: md.txt
---

# Confirmation overlay

![](https://developer.android.com/static/wear/images/confirmation-overlay/dialogs-hero.png)

[Confirmation overlays](https://developer.android.com/reference/androidx/wear/widget/ConfirmationOverlay)display a temporary message expressing a state change at the top of the current view.

## Usage

In most cases, an explicit confirmation is not needed. A visible change in the UI is enough to show that an action succeeded. If the user's action is not visible in the UI, use the confirmation overlay to give the necessary feedback to the user. It's better to show a change in the UI itself rather than showing a confirmation overlay.

Add a message to your message history instead of showing a confirmation overlay:

![](https://developer.android.com/static/wear/images/confirmation-overlay/Confirmation-overlay-notifications-example.png)

Show a confirmation overlay if a change in action doesn't cause a change in the UI:

![](https://developer.android.com/static/wear/images/confirmation-overlay/confirmation-overlay-message-message-sent.png)

## Adaptive layouts

Larger display accommodations have been made to dialogs to ensure that user experience is enhanced with increased real estate affordance. Updates include reduced scrolling, generous margins, and larger tap targets.

### **Margins**

Margin percentages are universally applied.

![](https://developer.android.com/static/wear/images/confirmation-overlay/confirmation-overlay-margins-adaptive-layouts.png)

![](https://developer.android.com/static/wear/images/confirmation-overlay/confirmation-overlay-margins-adaptive-layouts-2.png)

### **Rigid line length guidelines**

Line guidelines are universally applied. The max line length is of 3 lines with max character limit of 36 (30 with not Latin).

![](https://developer.android.com/static/wear/images/confirmation-overlay/confirmation-overlay-margins-rigid-line-lenght-guidelines-adaptive-layouts.png)