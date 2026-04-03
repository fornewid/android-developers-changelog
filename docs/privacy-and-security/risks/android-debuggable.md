---
title: android:debuggable  |  Security  |  Android Developers
url: https://developer.android.com/privacy-and-security/risks/android-debuggable
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Guides](https://developer.android.com/privacy-and-security/security-tips)

# android:debuggable Stay organized with collections Save and categorize content based on your preferences.



**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

The `android:debuggable` [attribute](/guide/topics/manifest/application-element) sets whether the application is
debuggable. It is set for the application as a whole and can't be overridden by
individual components. The attribute is set to `false` by default.

Allowing the application to be debuggable in itself is not a vulnerability, but
it does expose the application to greater risk through unintended and
unauthorized access to administrative functions. This can allow attackers more
access to the application and resources used by the application than intended.

## Impact

Setting the android:debuggable flag to true enables an attacker to debug the
application, making it easier for them to gain access to parts of the
application that should be kept secure.

## Mitigations

Always make sure to set the `android:debuggable` flag to `false` when shipping
your application.