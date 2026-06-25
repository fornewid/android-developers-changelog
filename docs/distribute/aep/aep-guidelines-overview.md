---
title: https://developer.android.com/distribute/aep/aep-guidelines-overview
url: https://developer.android.com/distribute/aep/aep-guidelines-overview
source: md.txt
---

This document acts as a centralized resource for exploring and understanding the
technical requirements of the Apps Experience Program (AEP).

When partners leverage the full potential of Android and Google Play to create
richer experiences, they spark deeper user engagement that fuels long-term
value. To achieve this, optimize your app to meet a set of AEP guidelines
organized into three core themes:

- Providing consistent and rich user experiences
- Expanding your reach across form factors
- Delivering stable and modern user experiences

By participating in the AEP and meeting these guidelines, eligible developers
qualify for the program rate card.

> [!NOTE]
> **Note:** Not all guidelines apply to every app. Guideline applicability depends on your app's core use cases and supported form factors.

## Provide consistent and rich user experiences

This theme focuses on high-impact features that drive user re-engagement and
ensure your brand presence throughout the Play Store and Android OS.

- [Phishing Resistant Authentication](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth): Secure sign-in using Passkeys or an approved SSO provider.
- [Restore Credentials](https://developer.android.com/distribute/aep/aep-req-restore-credentials): Provide a Zero-Tap Login experience during device restoration.
- [Engage SDK](https://developer.android.com/distribute/aep/aep-req-engage-sdk): Surface personalized recommendations and continuation content on Google surfaces.
- [Play Content](https://developer.android.com/distribute/aep/aep-req-play-content): Showcase your app's digital offerings through Play's discovery surfaces.
- [Title Availability](https://developer.android.com/distribute/aep/aep-req-new-title-availability): Launch new titles on the Android platform at the same time they become available on any other comparable non-Android platforms.
- [Feature Availability](https://developer.android.com/distribute/aep/aep-req-feature-availability): Launch new features on the Android platform at the same time they become available on any other comparable non-Android platforms.
- **Cross-platform design system**:

  The cross-platform design guidelines only apply if your app provides a
  comparable design system on a non-Android platform.
  - [Material UX](https://developer.android.com/distribute/aep/aep-req-material-ux): Adopt Material Design components and patterns for a cohesive look and feel.
  - [System Emoji](https://developer.android.com/distribute/aep/aep-req-system-emojis): Support the latest system emoji to ensure consistent expression across the platform.
  - [Dark Theme Support](https://developer.android.com/distribute/aep/aep-req-dark-theme): Dynamically shift the UI to reduce eye strain and improve legibility.
  - [Themed App Icons](https://developer.android.com/distribute/aep/aep-req-theme-app-icons): Provide adaptive icons that tint to match the user's chosen system theme.
  - [Physics Based Motion](https://developer.android.com/distribute/aep/aep-req-physics-based-motion): Implement fluid, natural animations that respond to user input with realistic momentum.
  - [Share Sheet](https://developer.android.com/distribute/aep/aep-req-share-sheet): Use the standard system share interface for a predictable and efficient sharing flow.

## Expand your reach across form factors

Users move seamlessly between different hardware throughout their day. This
theme ensures your app remains available and optimized for the entire Android
ecosystem, from the smallest screens to the largest displays.

- Mobile: Support phone, tablet, and foldable form factors with adaptive layouts.
- XR: Enable 2D window support for immersive devices.
- TV: Optimize for the leanback experience on Android TV.
- Auto: Integrate with Android Auto and Android Automotive OS.
- Wear: Build for the wrist with Wear OS optimized surfaces.
- Desktop: Support Googlebook with Adaptive layouts by March 1, 2027

For more information see, the [Form Factor Support](https://developer.android.com/distribute/aep/aep-req-form-factor-support) AEP guideline.

## Deliver stable and modern user experiences

A premium feel starts with technical excellence. This theme ensures your app is
performant, stable, and adopts the latest Android platform behaviors to feel
modern and responsive.

- [Stability](https://developer.android.com/distribute/aep/aep-req-stability): Maintain high performance with aggregated crash, ANR, memory usage, and Jank rates below program thresholds.
- [Quality - Jetpack Compose](https://developer.android.com/distribute/aep/aep-req-jetpack-compose): Use the recommended modern UI toolkit (or an equivalent alternative) to build scalable and high-quality UI.
- **Android standards**:

  Leverage modern Android APIs to enhance navigation fluidity, maximize screen
  utility, and enable AI-driven discovery of your app's core features.
  - [Predictive Back](https://developer.android.com/distribute/aep/aep-req-predictive-background): Provide a visual preview of navigation destinations to prevent accidental exits.
  - [Edge to Edge](https://developer.android.com/distribute/aep/aep-req-edge-to-edge): Maximize screen space and achieve a bezel-less aesthetic by drawing behind system bars.
  - [Android MCP](https://developer.android.com/distribute/aep/aep-req-android-mcp): Enable AI agents like Gemini to discover and invoke core app features.
- **Vertical-specific guidelines**:

  These guidelines apply only to apps with relevant use cases, such as media
  playback, communication services, and camera-centric features. Google Play
  will assess your app's use cases against these vertical-specific criteria
  during enrollment. You will have the opportunity to provide context early in
  the enrollment process, so an exemption request is not required.

  Apps can use an equivalent alternative framework that provides similar
  quality, user capabilities, stability and compatibility across the
  ecosystem. [Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for
  consideration.
  - [Media3](https://developer.android.com/distribute/aep/aep-req-media-3): Adopt the unified toolkit for high-quality media playback and sessions.
  - [CameraX](https://developer.android.com/distribute/aep/aep-req-camera-x): Ensure consistent and high-quality camera capture across the ecosystem.
  - [Cast Support](https://developer.android.com/distribute/aep/aep-req-cast-support): Stream content seamlessly from mobile devices to larger screens.
  - [Photo Picker](https://developer.android.com/distribute/aep/aep-req-photo-picker): Provide a secure and consistent interface for media selection.
  - [Preload Caching](https://developer.android.com/distribute/aep/aep-req-preload-caching): Minimize playback latency in scrollable feeds.
  - [Night Mode](https://developer.android.com/distribute/aep/aep-req-night-mode): Leverage hardware-accelerated low-light capture for still images.
  - [Android Telecom Framework](https://developer.android.com/distribute/aep/aep-req-telecom-api): Register VoIP calls as a core feature in the system.
  - [Picture in Picture Support (PiP)](https://developer.android.com/distribute/aep/aep-req-picture-in-picture): Enable seamless multitasking during video playback or calling, and navigation.