---
title: https://developer.android.com/privacy-and-security/safetynet
url: https://developer.android.com/privacy-and-security/safetynet
source: md.txt
---

> [!WARNING]
> **Warning:** The SafetyNet Attestation API is deprecated and has been replaced by the [Play Integrity API](https://developer.android.com/google/play/integrity/overview). The SafetyNet reCAPTCHA API is being deprecated and replaced with [reCAPTCHA](https://cloud.google.com/recaptcha/docs/instrument-android-apps).

This page explains how to add SafetyNet APIs to your app.

## Before you begin

To prepare your app, first make sure that your app's build file uses the
following values:

- A `minSdkVersion` of `19` or higher
- A `compileSdkVersion` of `28` or higher

Then complete the steps in the following sections.

## Configure your app

In your `settings.gradle` file, include
[Google's Maven repository](https://maven.google.com/web/index.html)
and [Maven central repository](https://search.maven.org/artifact)
in both your `dependencyResolutionManagement` and `pluginManagement` repository sections:

    pluginManagement {
        repositories {
            ...
            google()
            mavenCentral()
        }
    }

    dependencyResolutionManagement {
        ...
        repositories {
            google()
            mavenCentral()
        }
    }

Add the [Google Play services](http://developer.google.com/android)
dependency for the Google Play API to your
[module's Gradle build file](https://developer.android.com/studio/build#module-level),
which is commonly `app/build.gradle`:

    dependencies {
      implementation 'com.google.android.gms:play-services-safetynet:18.1.0'
    }

## More information

**[SafetyNet Safe Browsing API](https://developer.android.com/training/safetynet/safebrowsing)**
:   Learn how the SafetyNet Safe Browsing API provides services for determining
    whether a URL has been marked as a known threat by Google.

**[SafetyNet reCAPTCHA API](https://developer.android.com/training/safetynet/recaptcha)**
:   Learn how the SafetyNet reCAPTCHA API protects your app from malicious
    traffic.

**[SafetyNet Verify Apps API](https://developer.android.com/training/safetynet/verify-apps)**
:   Learn how the SafetyNet Verify Apps API protects devices against potentially
    harmful apps.

## Additional resources

- [Security tips](https://developer.android.com/training/articles/security-tips)
- [Compatibility Test Suite (CTS)](https://source.android.com/compatibility/cts)