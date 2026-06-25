---
title: https://developer.android.com/distribute/aep/aep-req-share-sheet
url: https://developer.android.com/distribute/aep/aep-req-share-sheet
source: md.txt
---

Use [Android Sharesheet](https://developer.android.com/training/sharing/send) for any general content-sharing flow to provide a
consistent, faster, and more secure experience for users.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Utilize `ACTION_SEND` and `Intent.createChooser()` to invoke the system Chooser. This native implementation offers several key benefits:
  - **Familiarity**: It maintains a standard interface that respects user muscle memory.
  - **Intelligent targeting**: It surfaces system-ranked Direct Share targets, such as frequent contacts.
  - **Efficiency and security**: It provides a faster and more secure method for sharing content with preferred apps.
- All external sharing intents must be routed through the system chooser.
- Custom in-app share menus must be transitioned to this native implementation, though app-specific actions can still be integrated using standard system chooser capabilities.

## Guideline applicability

This guideline applies to:

- Apps that provide a comparable external content sharing implementation on a non-Android platform.
- Phone, tablet, foldable, and desktop form factors.

## Exemptions

Sharesheet need not be applied for in-app forwarding, such as forwarding a
message to another user within the same messaging app.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Sharesheet** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Receive simple data from other apps](https://developer.android.com/training/sharing/receive#providing-direct-share-targets)
- [Sharing simple data](https://developer.android.com/training/sharing)