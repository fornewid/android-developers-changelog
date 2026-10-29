---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/troubleshooting
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/troubleshooting
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

If you are having problems with the Geospatial API, here are some common steps
to take.

<br />

### API Key authorization never succeeds

If API Key authorization is not working, follow these steps:

- Ensure that you have [enabled the ARCore API](https://console.cloud.google.com/apis/library/arcore) for the correct project in Google Cloud.
- If you have any API Key restrictions enabled, temporarily disable them.
- Use [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) to verify that the API Key is included in
  your app's build. It must be in a `<meta-data>` element in the
  `<application>` element in your app's `AndroidManifest.xml`:

      <meta-data
        android:name="com.google.android.ar.API_KEY"
        android:value="API_KEY"/>

- Ensure that the API Key listed in [your project's
  credentials](https://console.cloud.google.com/apis/credentials) exactly matches the API Key used by your app,
  with no spaces or any other characters.


<br />

<br />

### Geospatial localization quality never reaches expected values

If the quality of poses returned by the Geospatial API does not reach expected
results, here are some possible causes:

- The area is not mapped by an official Google Street View source.
  - To check, open Google Maps and enter Street View near the expected localization position. The attribution of the Street View images must be **Google Street View**. Other sources are not considered for VPS.
- The area is in a restricted region.
- The area does not have sufficient eligible feature points.
  - VPS only uses high-quality feature points that are unlikely to change over a long period of time. For example, trees may vary a lot in appearance across the year, so they are unsuitable to use as feature points.
  - The area may have changed significantly due to infrastructural works compared to recent captures of Google Street View.

<br />