---
title: https://developer.android.com/build/releases/agp-1-1-1-release-notes
url: https://developer.android.com/build/releases/agp-1-1-1-release-notes
source: md.txt
---

# Android plugin for Gradle, revision 1.1.1 (February 2015)

Dependencies:
General Notes:
:
    - Modified build variants so only variants that package a [Wear](https://developer.android.com/training/wearables/apps) app trigger Wear-specific build tasks.
    - Changed dependency related issues to fail at build time rather than at debug time. This behavior lets you run diagnostic tasks (such as 'dependencies') to help resolve the conflict.
    - Fixed the `android.getBootClasspath()` method to return a value.