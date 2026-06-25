---
title: https://developer.android.com/distribute/aep/aep-req-cast-support
url: https://developer.android.com/distribute/aep/aep-req-cast-support
source: md.txt
---

Integrate Google Cast support into video and audio centric applications by
leveraging the Media3 library. This elevates the app's media experience by
offering a frictionless streaming experience, allowing users to effortlessly
cast video and audio from mobile devices to larger screens like TVs and smart
displays. This integration ensures a consistent, high-quality multi-screen
experience and is critical for maintaining parity in modern media-centric apps.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Implement [Cast using Media3](https://developer.android.com/media/media3/cast), ensuring the Cast icon is visible in the media player UI and successfully initiates a connection to a Cast-enabled device.
- Verify Output Switcher integration (available out-of-the-box in Media3). Ensure the device chip in media session and lock screen notification correctly handles player transfers when the output route changes from one device to another.

## Guideline applicability

This guideline applies to:

- Apps that have the following use cases:
  - Audio streaming, such as music, podcasts, live radio, audiobooks.
  - Video streaming, including TV, movies, live sports, live news, long-form landscape video clips, live-streaming, and transactional video
- Phone, tablet, desktop, and foldable form factors.

## Exemptions

The following exemptions apply for this guideline:

- Video calling apps and apps that offer exclusively short-form portrait video.
- Apps can use an equivalent alternative framework that provides similar quality, user capabilities, stability and compatibility across the ecosystem. [Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Media3 Cast** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Media3 Cast overview](https://developer.android.com/media/media3/cast)