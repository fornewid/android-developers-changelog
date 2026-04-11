---
title: https://developer.android.com/health-and-fitness/health-connect/comparison-guide
url: https://developer.android.com/health-and-fitness/health-connect/comparison-guide
source: md.txt
---

With many health, fitness, and wellness apps running on Android devices,
users often need to switch between platforms to manage their data. Health
Connect solves this by providing a single place for Android users to manage
access to their health and fitness data, offering granular control.

The Google Health API platform offers two primary integration paths: Health
Connect for on-device Android data, and the Google Health API for cloud-based,
cross-platform data.

## Platform overview

The following table summarizes the key APIs within the Google Health API
platform:

| API | Status | Audience | Storage |
|---|---|---|---|
| Health Connect | Available | Android mobile developers | On-device |
| Google Health API | Available | Web, server-to-server (S2S), and platform-agnostic developers | Cloud |
| Fitbit Web API | Transitioning | Existing Fitbit ecosystem developers | Cloud |
| Google Fit API | Deprecating | Legacy Google Fit (Android and REST) API developers | Cloud |

## Health Connect

Consider integrating with [Health Connect](https://developer.android.com/guide/health-and-fitness/health-connect) if you're an Android
mobile developer.

We **don't** recommend migrating to Health Connect if you're an existing Google
Fitbit Web API developer. However, if you're integrated with the Fit APIs, we
recommend migrating to Health Connect only if you are a step-tracking app.

> [!NOTE]
> **Note:** The Google Fit APIs have been deprecated and we plan to support them until **2026** . See [Migration guide](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide) for instructions on migrating to Health Connect.

Health Connect unifies data across Android's portfolio of devices and apps into
an ecosystem, providing a common health platform for Android developers. It
provides a secure, on-device store for health and fitness data, standardizes
the data schema, and centralizes permissions control.

- **Architecture**: Local / Android Path (Mobile-centric).
- **Availability**: Part of the Android framework starting with Android 14. For Android 13 and lower, it is available through the Google Play Store.
- **Data storage**: Device-centric, where data is stored locally on the user's device.

### Health Connect distinctives

The following is a summary of how Health Connect differs from the Fit Android
API:

- **Intended audience:** Health Connect is intended for Android mobile developers.
- **Device-centric:** Users access and store data on their devices.
- **No account needed:** The data is not associated with a Google Account.
- **Built-in permissions:** Health and fitness data management is centralized.

### Integrate with Health Connect

The following resources help you integrate with and learn more about
Health Connect:

- **Integrate** : See [Get started](https://developer.android.com/guide/health-and-fitness/health-connect/develop/get-started) to start integrating with Health Connect.
- **Learn more** : To learn more about Health Connect, watch the [Introducing new APIs for health and fitness in Health Connect by Android](https://www.youtube.com/watch?v=d14GVcnbTeo) video on YouTube.
- **Resources** : For more information, see the [documentation](https://developer.android.com/guide/health-and-fitness/health-connect).
- **Migration** : Fit API developers can follow the [Fit migration guide](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide).

## Google Health API

The [Google Health API](https://developers.google.com/health) is a unified web
API designed for server-to-server (S2S) interactions. It is an
account-centric, platform-agnostic interface that
replaces the existing Fitbit Web API functionality.

### Google Health API distinctives

- **Architecture**: Cloud Path (Server-to-server).
- **Audience**: Developers requiring a reconciled view of health and medical data across platforms.
- **Data needs**: Required if your app is web-based, uses the OAuth protocol, or requires low-latency data from Fitbit or Pixel Watch.
- **Availability**: Available.

## Legacy APIs

The following APIs are considered legacy and are being deprecated or
transitioned to newer alternatives.

### Google Fit API

The [Google Fit API](https://developers.google.com/fit) (including the REST API) is officially scheduled
for end of service by the end of 2026. We recommend integrating with
Health Connect or the Google Health API. All developers using Google Fit APIs
must transition. We recommend removing Google Fit integration and encouraging
users to connect to new integrations. For instructions, see the
[Fit migration guide](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide).

### Fitbit Web API

[The Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/developer-guide/) is a platform-agnostic interface to integrate
with the Fitbit ecosystem. In the Fitbit Web API, the user's data is tied to
their Fitbit account instead of their device. Existing developers should
prepare to transition to the Google Health API to access unified health data.

> [!CAUTION]
> **Caution:** The Fitbit Web API will migrate to the Google Health API. For instructions, see the [Fitbit migration guide](https://developers.google.com/health/migration).