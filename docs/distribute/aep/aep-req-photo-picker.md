---
title: https://developer.android.com/distribute/aep/aep-req-photo-picker
url: https://developer.android.com/distribute/aep/aep-req-photo-picker
source: md.txt
---

Integrate the Android photo picker to provide users with a consistent, secure,
and feature-rich way to select photos and videos. By adopting this standard
interface, apps can allow users to access both local and cloud-backed assets
while enhancing privacy through reduced permission requirements.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- It must implement the standard or embedded Android photo picker in the primary user journey where a user is prompted to select photos or videos.
- The app should launch the photo picker to ensure full access to search and cloud-based assets.

**Note**: The requirement is not satisfied if the app only requests photo
permissions or manages limited access states.

## Guideline applicability

This guideline applies to:

- Apps that let users select photos or videos.
- Phone, tablet, and desktop form factors.

## Exemptions

The following exemptions apply for this guideline:

- Apps that perform bulk operations on photos as part of their core use case. To request an exemption, the app must provide evidence of the bulk photo use case and instructions for the Play team to verify.
- Apps that only access proprietary photos from their own private storage and don't require `READ_MEDIA_IMAGES` or `READ_MEDIA_VIDEO` permissions.
- Apps can use an equivalent alternative framework that provides similar quality, user capabilities, stability and compatibility across the ecosystem. [Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Photo Picker** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Photo picker overview](https://developer.android.com/training/data-storage/shared/photo-picker)
- [Embedded photo picker](https://developer.android.com/training/data-storage/shared/photo-picker/embedded)