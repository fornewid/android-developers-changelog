---
title: https://developer.android.com/develop/ui/compose/tooling/lint
url: https://developer.android.com/develop/ui/compose/tooling/lint
source: md.txt
---

[Android Lint](https://developer.android.com/studio/write/lint) is a powerful tool for verifying the correctness or
your code. It is highly recommended that you fix any identified lint errors
before releasing your app to production.

Compose ships with a number of lint checks by default. This helps verify the
correctness of your Compose code.

## Minimum version requirement for Compose lint checks

To simplify compatibility and improve stability for lint check support, Compose
1.9 requires Android Gradle Plugin (AGP) / Lint version 8.8.2 or higher.

If you're using an AGP version lower than 8.8.2 and are unable to upgrade, you
can specify the lint version to use in your `gradle.properties` file:  

    android.experimental.lint.version = 8.8.2

Previously, the complex dependencies of Compose lint checks led to frequent
compatibility issues and made it difficult to determine the correct tool
versions (Android Studio, AGP/Lint, Compose).

Minimum version requirements for Compose, AGP, and Studio are as follows:

|---|---|---|
| **Compose Version** | **Required AGP / Lint version** | **Required Studio version** |
| 1.9 | 8.8.2+ | Ladybug+ |
| 1.8 | 8.6.0+ | Koala Feature Drop -\> Meerkat |
| 1.7 | 8.4.0+ | Jellyfish -\> Meerkat |