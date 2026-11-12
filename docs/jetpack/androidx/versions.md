---
title: https://developer.android.com/jetpack/androidx/versions
url: https://developer.android.com/jetpack/androidx/versions
source: md.txt
---

*** ** * ** ***

Jetpack libraries ship separately from the Android OS, so updates to the
libraries can happen independently and more frequently.

The libraries follow [strict semantic versioning](https://semver.org/) for binary compatibility with an added inter-version sequence of pre-release revisions.
A version string (like `1.0.1-beta02`) contains three numbers representing major, minor, and bugfix levels.
Pre-release versions also have a suffix that specifies the pre-release stage
(alpha, beta, release candidate) and revision number (01, 02, and so on).

**Please note** that `androidx` libraries are encouraged, but not required, to preserve source compatibility across minor versions. The reason being a major version update would force all artifacts that depend on the previous major version to be explicitly migrated, which would disrupt the workflow of developers.

Every version of a library moves through three pre-release stages on its way to
becoming a stable release. The criteria for each pre-release stage is:

**Alpha**

- Alpha releases are functionally stable, but may not be feature-complete.
- While a release is in alpha, APIs may be added, removed, or changed.

**Beta**

- Beta releases are functionally stable and have a feature-complete API surface.
- They are ready for production use but may contain bugs.
- A beta release cannot use experimental compiler features (such as `@UseExperimental`).
- Dependencies on other libraries must be beta, rc, or stable versions. No alpha dependencies are allowed.

**Release Candidate (RC)**

- A release candidate is a prospective stable release.
- It may contain critical last-minute fixes.
- Its API surface is final.
- Dependencies on other libraries must be rc or stable versions only.

A library can have multiple versions at the same time. Each version has a
different release stage. For example, while the stable release of
`androidx.activity` could be `1.0.0`, there might also be a `1.1.0-beta02`
release as well as a `2.0.0-alpha01` release.

Use this page to learn of the latest updates to the libraries.

The [AndroidX recent release notes page](https://developer.android.com/jetpack/androidx/versions/all-channel.md.txt)
lists the libraries that have recently changed. Google's
[Maven repository](https://dl.google.com/dl/android/maven2/index.html)
shows the complete version history.

Use the table below to view the most recent stable and preview versions of every
AndroidX library. The links on each row take you to the library's release notes.
In the release notes you'll find:

- The chronological history of all the releases.
- A code snippet with the default Gradle dependency declarations to use the artifacts.
- Links to the Kotlin and Java reference pages for the packages in each artifact.

> [!NOTE]
> **Note:** Jetpack libraries don't send any user data to a backend service of any kind. This means that integrating a Jetpack library into your app has no impact on your app's [Data safety form](https://developer.android.com/guide/topics/data/collect-share) in the Play Console.

**Minimum SDK Version**

AndroidX libraries have the default `minSdk` of 24. Individual libraries might
use a higher `minSdk` in cases when supporting the lowest API version is
impossible or prohibitively expensive. The default `minSdk` is meant to cover
99% of Android users based on the Google Play Store check-in information, as is
shown in Android Studio's New Project wizard. The default value is updated at a
yearly cadence. The default `minSdk` only affects new library releases, so
already released artifacts aren't affected and might support a lower `minSdk`.

### Jetpack libraries

Some AndroidX libraries, like camera, have multiple artifacts that are
maintained separately. These libraries are marked with an asterisk (\*). See the
release notes to view the version updates for all of the artifacts.

| Maven Group ID | Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|---|
| [A2UI protocol](https://developer.android.com/jetpack/androidx/releases/a2ui.md.txt), enabling AI agents to generate rich, interactive user interfaces that render native Compose components---without executing arbitrary code."\>a2ui | October 21, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/a2ui.md.txt#1.0.0-alpha02) |
| [A2UI protocol](https://developer.android.com/jetpack/androidx/releases/a2ui_compose), enabling AI agents to generate rich, interactive user interfaces that render native Compose components---without executing arbitrary code."\>a2ui.compose | October 21, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/a2ui_compose#1.0.0-alpha02) |
| [activity](https://developer.android.com/jetpack/androidx/releases/activity.md.txt) | September 23, 2026 | [1.13.0](https://developer.android.com/jetpack/androidx/releases/activity.md.txt#1.13.0) | - | - | [1.14.0-alpha03](https://developer.android.com/jetpack/androidx/releases/activity.md.txt#1.14.0-alpha03) |
| [ads](https://developer.android.com/jetpack/androidx/releases/ads.md.txt) | March 8, 2023 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/ads.md.txt#1.0.0-alpha05) |
| [annotation.keep](https://developer.android.com/jetpack/androidx/releases/annotation-keep.md.txt) | October 12, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/annotation-keep.md.txt#1.0.0-alpha01) |
| [annotation (\*)](https://developer.android.com/jetpack/androidx/releases/annotation.md.txt) | September 23, 2026 | [1.11.0](https://developer.android.com/jetpack/androidx/releases/annotation.md.txt#1.11.0) | - | - | - |
| [appcompat](https://developer.android.com/jetpack/androidx/releases/appcompat.md.txt) | August 12, 2026 | [1.8.0](https://developer.android.com/jetpack/androidx/releases/appcompat.md.txt#1.8.0) | - | - | - |
| [appfunctions](https://developer.android.com/jetpack/androidx/releases/appfunctions.md.txt) | November 04, 2026 | - | [1.0.0-rc01](https://developer.android.com/jetpack/androidx/releases/appfunctions.md.txt#1.0.0-rc01) | - | - |
| [appsearch](https://developer.android.com/jetpack/androidx/releases/appsearch.md.txt) | August 26, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/appsearch.md.txt#1.1.0) | - | - | [1.2.0-alpha02](https://developer.android.com/jetpack/androidx/releases/appsearch.md.txt#1.2.0-alpha02) |
| [appstate.statestore](https://developer.android.com/jetpack/androidx/releases/appstate-statestore.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/appstate-statestore.md.txt#1.0.0-alpha02) |
| [appstate.transform](https://developer.android.com/jetpack/androidx/releases/appstate-transform.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/appstate-transform.md.txt#1.0.0-alpha02) |
| [arch.core](https://developer.android.com/jetpack/androidx/releases/arch-core.md.txt) | February 22, 2023 | [2.2.0](https://developer.android.com/jetpack/androidx/releases/arch-core.md.txt#2.2.0) | - | - | - |
| [asynclayoutinflater](https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater.md.txt) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater.md.txt#1.1.0) | - | - | - |
| [autofill](https://developer.android.com/jetpack/androidx/releases/autofill.md.txt) | June 4, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/autofill.md.txt#1.3.0) | - | - | - |
| [benchmark](https://developer.android.com/jetpack/androidx/releases/benchmark.md.txt) | October 07, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/benchmark.md.txt#1.5.0) | - | - | [1.6.0-alpha01](https://developer.android.com/jetpack/androidx/releases/benchmark.md.txt#1.6.0-alpha01) |
| [biometric](https://developer.android.com/jetpack/androidx/releases/biometric.md.txt) | November 04, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/biometric.md.txt#1.1.0) | - | [1.4.0-beta01](https://developer.android.com/jetpack/androidx/releases/biometric.md.txt#1.4.0-beta01) | - |
| [bluetooth](https://developer.android.com/jetpack/androidx/releases/bluetooth.md.txt) | November 29, 2023 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/bluetooth.md.txt#1.0.0-alpha02) |
| [browser](https://developer.android.com/jetpack/androidx/releases/browser.md.txt) | March 25, 2026 | [1.10.0](https://developer.android.com/jetpack/androidx/releases/browser.md.txt#1.10.0) | - | - | - |
| [car-app](https://developer.android.com/jetpack/androidx/releases/car-app.md.txt) | October 07, 2026 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/car-app.md.txt#1.7.0) | [1.8.0-rc01](https://developer.android.com/jetpack/androidx/releases/car-app.md.txt#1.8.0-rc01) | - | [1.9.0-alpha03](https://developer.android.com/jetpack/androidx/releases/car-app.md.txt#1.9.0-alpha03) |
| [camera (\*)](https://developer.android.com/jetpack/androidx/releases/camera.md.txt) | November 04, 2026 | [1.6.2](https://developer.android.com/jetpack/androidx/releases/camera.md.txt#1.6.2) | [1.7.0-rc02](https://developer.android.com/jetpack/androidx/releases/camera.md.txt#1.7.0-rc02) | - | - |
| [camera.media3](https://developer.android.com/jetpack/androidx/releases/camera-media3.md.txt) | August 13, 2025 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/camera-media3.md.txt#1.0.0-alpha04) |
| [camera.featurecombinationquery](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery.md.txt) | November 04, 2026 | [1.6.2](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery.md.txt#1.6.2) | [1.7.0-rc02](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery.md.txt#1.7.0-rc02) | - | - |
| [camera.viewfinder (\*)](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder.md.txt) | November 04, 2026 | [1.6.2](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder.md.txt#1.6.2) | [1.7.0-rc02](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder.md.txt#1.7.0-rc02) | - | - |
| [cardview](https://developer.android.com/jetpack/androidx/releases/cardview.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/cardview.md.txt#1.0.0) | - | - | - |
| [collection](https://developer.android.com/jetpack/androidx/releases/collection.md.txt) | October 07, 2026 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/collection.md.txt#1.7.0) | - | - | - |
| [compose.remote.foundation](https://developer.android.com/jetpack/androidx/releases/compose_remote_foundation) | November 04, 2026 | - | - | - | [1.0.0-alpha06](https://developer.android.com/jetpack/androidx/releases/compose_remote_foundation#1.0.0-alpha06) |
| [compose](https://developer.android.com/jetpack/androidx/releases/compose.md.txt) | August 7, 2024 | - | - | - | [1.0.0-alpha06](https://developer.android.com/jetpack/androidx/releases/compose.md.txt#1.0.0-alpha06) |
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation.md.txt) | November 04, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-animation.md.txt#1.12.1) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-animation.md.txt#1.13.0-rc01) | - | - |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler.md.txt) | August 7, 2024 | [1.5.15](https://developer.android.com/jetpack/androidx/releases/compose-compiler.md.txt#1.5.15) | - | - | - |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation.md.txt) | November 04, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-foundation.md.txt#1.12.1) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-foundation.md.txt#1.13.0-rc01) | - | - |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material.md.txt) | November 04, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-material.md.txt#1.12.1) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-material.md.txt#1.13.0-rc01) | - | - |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt) | November 04, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt#1.4.0) | [1.5.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt#1.5.0-rc01) | - | - |
| [compose.material3.adaptive](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive.md.txt) | October 07, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive.md.txt#1.3.0) | - | - | [1.4.0-alpha03](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive.md.txt#1.4.0-alpha03) |
| [compose.remote](https://developer.android.com/jetpack/androidx/releases/compose-remote.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha23](https://developer.android.com/jetpack/androidx/releases/compose-remote.md.txt#1.0.0-alpha23) |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime.md.txt) | November 04, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-runtime.md.txt#1.12.1) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-runtime.md.txt#1.13.0-rc01) | - | - |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui.md.txt) | November 04, 2026 | [1.12.1](https://developer.android.com/jetpack/androidx/releases/compose-ui.md.txt#1.12.1) | [1.13.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-ui.md.txt#1.13.0-rc01) | - | - |
| [concurrent](https://developer.android.com/jetpack/androidx/releases/concurrent.md.txt) | July 29, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/concurrent.md.txt#1.3.0) | - | - | [1.4.0-alpha01](https://developer.android.com/jetpack/androidx/releases/concurrent.md.txt#1.4.0-alpha01) |
| [constraintlayout (\*)](https://developer.android.com/jetpack/androidx/releases/constraintlayout.md.txt) | July 29, 2026 | [2.2.2](https://developer.android.com/jetpack/androidx/releases/constraintlayout.md.txt#2.2.2) | - | - | - |
| [contentpager](https://developer.android.com/jetpack/androidx/releases/contentpager.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/contentpager.md.txt#1.0.0) | - | - | - |
| [coordinatorlayout](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout.md.txt) | November 04, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout.md.txt#1.3.0) | - | - | [1.4.0-alpha01](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout.md.txt#1.4.0-alpha01) |
| [locationbutton (\*)](https://developer.android.com/jetpack/androidx/releases/locationbutton) | June 17, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/locationbutton#1.0.0-alpha01) |
| [core (\*)](https://developer.android.com/jetpack/androidx/releases/core.md.txt) | November 04, 2026 | [1.19.1](https://developer.android.com/jetpack/androidx/releases/core.md.txt#1.19.1) | - | - | - |
| [core.uwb](https://developer.android.com/jetpack/androidx/releases/core-uwb.md.txt) | October 07, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/core-uwb.md.txt#1.0.0) | - | - | [1.1.0-alpha03](https://developer.android.com/jetpack/androidx/releases/core-uwb.md.txt#1.1.0-alpha03) |
| [credentials](https://developer.android.com/jetpack/androidx/releases/credentials.md.txt) | July 29, 2026 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/credentials.md.txt#1.6.0) | - | - | [1.7.0-alpha03](https://developer.android.com/jetpack/androidx/releases/credentials.md.txt#1.7.0-alpha03) |
| [credentials.providerevents](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents.md.txt) | September 09, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents.md.txt#1.0.0-beta01) | - |
| [credentials.registry](https://developer.android.com/jetpack/androidx/releases/credentials-registry.md.txt) | July 29, 2026 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/credentials-registry.md.txt#1.0.0-alpha05) |
| [cursoradapter](https://developer.android.com/jetpack/androidx/releases/cursoradapter.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/cursoradapter.md.txt#1.0.0) | - | - | - |
| [customview (\*)](https://developer.android.com/jetpack/androidx/releases/customview.md.txt) | April 23, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/customview.md.txt#customview-1.2.0) | - | - | - |
| [databinding](https://developer.android.com/jetpack/androidx/releases/databinding.md.txt) | September 5, 2019 | [3.5.0](https://developer.android.com/jetpack/androidx/releases/databinding.md.txt#3.5.0) | - | - | [3.6.0-alpha10](https://developer.android.com/jetpack/androidx/releases/databinding.md.txt#3.6.0-alpha10) |
| [datastore](https://developer.android.com/jetpack/androidx/releases/datastore.md.txt) | October 21, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/datastore.md.txt#1.3.0) | - | - | - |
| [documentfile](https://developer.android.com/jetpack/androidx/releases/documentfile.md.txt) | May 7, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/documentfile.md.txt#1.1.0) | - | - | - |
| [draganddrop](https://developer.android.com/jetpack/androidx/releases/draganddrop.md.txt) | May 11, 2022 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/draganddrop.md.txt#1.0.0) | - | - | - |
| [drawerlayout](https://developer.android.com/jetpack/androidx/releases/drawerlayout.md.txt) | March 22, 2023 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/drawerlayout.md.txt#1.2.0) | - | - | - |
| [dynamicanimation](https://developer.android.com/jetpack/androidx/releases/dynamicanimation.md.txt) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/dynamicanimation.md.txt#1.1.0) | - | - | - |
| [emoji](https://developer.android.com/jetpack/androidx/releases/emoji.md.txt) | December 17, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/emoji.md.txt#1.2.0) | - | - | - |
| [emoji2](https://developer.android.com/jetpack/androidx/releases/emoji2.md.txt) | September 23, 2026 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/emoji2.md.txt#1.7.0) | - | - | - |
| [enterprise](https://developer.android.com/jetpack/androidx/releases/enterprise.md.txt) | November 04, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/enterprise.md.txt#1.1.0) | - | - | [1.2.0-alpha01](https://developer.android.com/jetpack/androidx/releases/enterprise.md.txt#1.2.0-alpha01) |
| [exifinterface](https://developer.android.com/jetpack/androidx/releases/exifinterface.md.txt) | November 04, 2026 | [1.4.2](https://developer.android.com/jetpack/androidx/releases/exifinterface.md.txt#1.4.2) | - | [1.5.0-beta01](https://developer.android.com/jetpack/androidx/releases/exifinterface.md.txt#1.5.0-beta01) | - |
| [fragment](https://developer.android.com/jetpack/androidx/releases/fragment.md.txt) | September 23, 2026 | [1.9.1](https://developer.android.com/jetpack/androidx/releases/fragment.md.txt#1.9.1) | - | - | - |
| [games (\*)](https://developer.android.com/jetpack/androidx/releases/games.md.txt) | May 06, 2026 | [4.4.2](https://developer.android.com/jetpack/androidx/releases/games.md.txt#games-activity-4.4.2) | - | - | - |
| [glance.adaptive](https://developer.android.com/jetpack/androidx/releases/glance_adaptive) | November 04, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/glance_adaptive#1.0.0-alpha04) |
| [glance](https://developer.android.com/jetpack/androidx/releases/glance.md.txt) | August 26, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/glance.md.txt#1.2.0) | - | - | [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/glance.md.txt#1.3.0-alpha02) |
| [glance.wear](https://developer.android.com/jetpack/androidx/releases/glance-wear.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha22](https://developer.android.com/jetpack/androidx/releases/glance-wear.md.txt#1.0.0-alpha22) |
| [graphics (\*)](https://developer.android.com/jetpack/androidx/releases/graphics.md.txt) | October 07, 2026 | [1.0.4](https://developer.android.com/jetpack/androidx/releases/graphics.md.txt#graphics-core-1.0.4) | - | [1.1.0-beta01](https://developer.android.com/jetpack/androidx/releases/graphics.md.txt#graphics-core-1.1.0-beta01) | - |
| [gridlayout](https://developer.android.com/jetpack/androidx/releases/gridlayout.md.txt) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/gridlayout.md.txt#1.1.0) | - | - | - |
| [health](https://developer.android.com/jetpack/androidx/releases/health.md.txt) | September 23, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/health.md.txt#1.1.0) | - | - | - |
| [health.connect](https://developer.android.com/jetpack/androidx/releases/health-connect.md.txt) | August 26, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/health-connect.md.txt#1.1.0) | - | - | [1.2.0-alpha06](https://developer.android.com/jetpack/androidx/releases/health-connect.md.txt#1.2.0-alpha06) |
| [heifwriter](https://developer.android.com/jetpack/androidx/releases/heifwriter.md.txt) | November 04, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/heifwriter.md.txt#1.1.0) | [1.2.0-rc02](https://developer.android.com/jetpack/androidx/releases/heifwriter.md.txt#1.2.0-rc02) | - | - |
| [hilt](https://developer.android.com/jetpack/androidx/releases/hilt.md.txt) | July 01, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/hilt.md.txt#1.4.0) | - | - | - |
| [ink](https://developer.android.com/jetpack/androidx/releases/ink.md.txt) | November 04, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/ink.md.txt#1.0.0) | - | - | [1.1.0-alpha11](https://developer.android.com/jetpack/androidx/releases/ink.md.txt#1.1.0-alpha11) |
| [input](https://developer.android.com/jetpack/androidx/releases/input.md.txt) | November 04, 2026 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/input.md.txt#1.0.1) | - | - | - |
| [interpolator](https://developer.android.com/jetpack/androidx/releases/interpolator.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/interpolator.md.txt#1.0.0) | - | - | - |
| [javascriptengine](https://developer.android.com/jetpack/androidx/releases/javascriptengine.md.txt) | September 23, 2026 | [1.1.1](https://developer.android.com/jetpack/androidx/releases/javascriptengine.md.txt#1.1.1) | - | - | - |
| [jetifier](https://developer.android.com/jetpack/androidx/releases/jetifier.md.txt) | September 2, 2020 | - | - | [1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/jetifier.md.txt#1.0.0-beta10) | - |
| [leanback](https://developer.android.com/jetpack/androidx/releases/leanback.md.txt) | June 17, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/leanback.md.txt#1.2.0) | - | - | [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/leanback.md.txt#1.3.0-alpha02) |
| [legacy](https://developer.android.com/jetpack/androidx/releases/legacy.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/legacy.md.txt#1.0.0) | - | - | - |
| [lifecycle (\*)](https://developer.android.com/jetpack/androidx/releases/lifecycle.md.txt) | October 21, 2026 | [2.11.0](https://developer.android.com/jetpack/androidx/releases/lifecycle.md.txt#2.11.0) | - | - | [2.12.0-alpha05](https://developer.android.com/jetpack/androidx/releases/lifecycle.md.txt#2.12.0-alpha05) |
| [lint](https://developer.android.com/jetpack/androidx/releases/lint.md.txt) | June 17, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/lint.md.txt#1.0.0) | - | - | - |
| [loader](https://developer.android.com/jetpack/androidx/releases/loader.md.txt) | July 29, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/loader.md.txt#1.2.0) | - | - | - |
| [localbroadcastmanager](https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager.md.txt) | January 12, 2022 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager.md.txt#1.1.0) | - | - | - |
| [media](https://developer.android.com/jetpack/androidx/releases/media.md.txt) | May 06, 2026 | [1.8.0](https://developer.android.com/jetpack/androidx/releases/media.md.txt#1.8.0) | - | - | - |
| [media3](https://developer.android.com/jetpack/androidx/releases/media3.md.txt) | November 11, 2026 | [1.11.1](https://developer.android.com/jetpack/androidx/releases/media3.md.txt#1.11.1) | - | [1.12.0-beta01](https://developer.android.com/jetpack/androidx/releases/media3.md.txt#1.12.0-beta01) | - |
| [mediarouter](https://developer.android.com/jetpack/androidx/releases/mediarouter.md.txt) | October 21, 2026 | [1.8.1](https://developer.android.com/jetpack/androidx/releases/mediarouter.md.txt#1.8.1) | [1.9.0-rc01](https://developer.android.com/jetpack/androidx/releases/mediarouter.md.txt#1.9.0-rc01) | - | - |
| [multidex](https://developer.android.com/jetpack/androidx/releases/multidex.md.txt) | December 17, 2018 | [2.0.1](https://developer.android.com/jetpack/androidx/releases/multidex.md.txt#2.0.1) | - | - | - |
| [metrics](https://developer.android.com/jetpack/androidx/releases/metrics.md.txt) | October 8, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/metrics.md.txt#1.0.0) | - | - | - |
| [navigation](https://developer.android.com/jetpack/androidx/releases/navigation.md.txt) | September 23, 2026 | [2.10.2](https://developer.android.com/jetpack/androidx/releases/navigation.md.txt#2.10.2) | - | - | - |
| [navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3.md.txt) | November 04, 2026 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/navigation3.md.txt#1.2.1) | - | - | [1.3.0-alpha04](https://developer.android.com/jetpack/androidx/releases/navigation3.md.txt#1.3.0-alpha04) |
| [navigationevent](https://developer.android.com/jetpack/androidx/releases/navigationevent.md.txt) | October 07, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/navigationevent.md.txt#1.2.0) | - | - | - |
| [paging (\*)](https://developer.android.com/jetpack/androidx/releases/paging.md.txt) | October 12, 2026 | [3.5.3](https://developer.android.com/jetpack/androidx/releases/paging.md.txt#3.5.3) | - | - | - |
| [palette](https://developer.android.com/jetpack/androidx/releases/palette.md.txt) | October 21, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/palette.md.txt#1.1.0) | - | - | - |
| [pdf](https://developer.android.com/jetpack/androidx/releases/pdf.md.txt) | August 26, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/pdf.md.txt#1.0.0-beta01) | - |
| [percentlayout](https://developer.android.com/jetpack/androidx/releases/percentlayout.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/percentlayout.md.txt#1.0.0) | - | - | - |
| [performance](https://developer.android.com/jetpack/androidx/releases/performance.md.txt) | January 15, 2025 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/performance.md.txt#1.0.0-alpha01) |
| [photopicker](https://developer.android.com/jetpack/androidx/releases/photopicker.md.txt) | October 21, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/photopicker.md.txt#1.0.0-alpha03) |
| [preference](https://developer.android.com/jetpack/androidx/releases/preference.md.txt) | July 26, 2023 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/preference.md.txt#1.2.1) | - | - | - |
| [print](https://developer.android.com/jetpack/androidx/releases/print.md.txt) | April 23, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/print.md.txt#1.1.0) | - | - | - |
| [privacysandbox.activity](https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity.md.txt) | December 17, 2025 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity.md.txt#1.0.0-alpha03) |
| [privacysandbox.ads](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads.md.txt) | May 7, 2025 | - | - | [1.1.0-beta13](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads.md.txt#1.1.0-beta13) | - |
| [privacysandbox.plugins](https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins.md.txt) | August 9, 2023 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins.md.txt#1.0.0-alpha02) |
| [privacysandbox.sdkruntime](https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime.md.txt) | December 17, 2025 | - | - | - | [1.0.0-alpha19](https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime.md.txt#1.0.0-alpha19) |
| [privacysandbox.tools](https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools.md.txt) | December 17, 2025 | - | - | - | [1.0.0-alpha14](https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools.md.txt#1.0.0-alpha14) |
| [privacysandbox.ui](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui.md.txt) | December 17, 2025 | - | - | - | [1.0.0-alpha17](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui.md.txt#1.0.0-alpha17) |
| [profileinstaller](https://developer.android.com/jetpack/androidx/releases/profileinstaller.md.txt) | October 2, 2024 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller.md.txt#1.4.1) | - | - | - |
| [recommendation](https://developer.android.com/jetpack/androidx/releases/recommendation.md.txt) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/recommendation.md.txt#1.0.0) | - | - | - |
| [recyclerview (\*)](https://developer.android.com/jetpack/androidx/releases/recyclerview.md.txt) | July 29, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/recyclerview.md.txt#1.4.0) | - | - | - |
| [remotecallback](https://developer.android.com/jetpack/androidx/releases/remotecallback.md.txt) | November 19, 2025 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/remotecallback.md.txt#1.0.0-alpha03) |
| [resourceinspection](https://developer.android.com/jetpack/androidx/releases/resourceinspection.md.txt) | January 26, 2022 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/resourceinspection.md.txt#1.0.1) | - | - | - |
| [room](https://developer.android.com/jetpack/androidx/releases/room.md.txt) | September 09, 2026 | [2.8.5](https://developer.android.com/jetpack/androidx/releases/room.md.txt#2.8.5) | - | - | - |
| [room3](https://developer.android.com/jetpack/androidx/releases/room3.md.txt) | October 21, 2026 | [3.0.3](https://developer.android.com/jetpack/androidx/releases/room3.md.txt#3.0.3) | - | - | [3.1.0-alpha03](https://developer.android.com/jetpack/androidx/releases/room3.md.txt#3.1.0-alpha03) |
| [savedstate](https://developer.android.com/jetpack/androidx/releases/savedstate.md.txt) | October 21, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/savedstate.md.txt#1.5.0) | - | - | [1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/savedstate.md.txt#1.6.0-alpha05) |
| [security (\*)](https://developer.android.com/jetpack/androidx/releases/security.md.txt) | September 09, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/security.md.txt#1.1.0) | - | - | - |
| [sharetarget](https://developer.android.com/jetpack/androidx/releases/sharetarget.md.txt) | October 5, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/sharetarget.md.txt#1.2.0) | - | - | - |
| [slice](https://developer.android.com/jetpack/androidx/releases/slice.md.txt) | January 13, 2021 | - | - | - | [1.1.0-alpha02](https://developer.android.com/jetpack/androidx/releases/slice.md.txt#1.1.0-alpha02) |
| [slidingpanelayout](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout.md.txt) | January 26, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout.md.txt#1.2.0) | - | - | - |
| [startup](https://developer.android.com/jetpack/androidx/releases/startup.md.txt) | September 18, 2024 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/startup.md.txt#1.2.0) | - | - | - |
| [sqlite](https://developer.android.com/jetpack/androidx/releases/sqlite.md.txt) | October 21, 2026 | [2.7.1](https://developer.android.com/jetpack/androidx/releases/sqlite.md.txt#2.7.1) | - | - | [2.8.0-alpha03](https://developer.android.com/jetpack/androidx/releases/sqlite.md.txt#2.8.0-alpha03) |
| [swiperefreshlayout](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout.md.txt) | December 3, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout.md.txt#1.2.0) | - | - | - |
| [test.backup](https://developer.android.com/jetpack/androidx/releases/test-backup.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/test-backup.md.txt#1.0.0-alpha04) |
| [test (\*)](https://developer.android.com/jetpack/androidx/releases/test.md.txt) | November 09, 2026 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/test.md.txt#1.0.1) | - | - | [1.1.0-alpha04](https://developer.android.com/jetpack/androidx/releases/test.md.txt#1.1.0-alpha04) |
| [test.ext](https://developer.android.com/jetpack/androidx/releases/test-ext.md.txt) | May 19, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/test-ext.md.txt#1.0.0-alpha03) |
| [test.uiautomator](https://developer.android.com/jetpack/androidx/releases/test-uiautomator.md.txt) | November 04, 2026 | [2.4.1](https://developer.android.com/jetpack/androidx/releases/test-uiautomator.md.txt#2.4.1) | - | - | - |
| [text-vertical](https://developer.android.com/jetpack/androidx/releases/text-vertical.md.txt) | October 21, 2026 | - | - | [1.0.0-beta03](https://developer.android.com/jetpack/androidx/releases/text-vertical.md.txt#1.0.0-beta03) | - |
| [textclassifier](https://developer.android.com/jetpack/androidx/releases/textclassifier.md.txt) | March 23, 2022 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/textclassifier.md.txt#1.0.0-alpha04) |
| [tracing](https://developer.android.com/jetpack/androidx/releases/tracing.md.txt) | October 21, 2026 | [2.0.5](https://developer.android.com/jetpack/androidx/releases/tracing.md.txt#2.0.5) | - | - | - |
| [transition](https://developer.android.com/jetpack/androidx/releases/transition.md.txt) | September 23, 2026 | [1.7.2](https://developer.android.com/jetpack/androidx/releases/transition.md.txt#1.7.2) | - | - | - |
| [tv (\*)](https://developer.android.com/jetpack/androidx/releases/tv.md.txt) | May 06, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/tv.md.txt#1.1.0) | - | - | - |
| [tvprovider](https://developer.android.com/jetpack/androidx/releases/tvprovider.md.txt) | May 7, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/tvprovider.md.txt#1.1.0) | - | - | - |
| [vectordrawable](https://developer.android.com/jetpack/androidx/releases/vectordrawable.md.txt) | May 1, 2024 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/vectordrawable.md.txt#1.2.0) | - | - | - |
| [versionedparcelable](https://developer.android.com/jetpack/androidx/releases/versionedparcelable.md.txt) | January 29, 2025 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/versionedparcelable.md.txt#1.2.1) | - | - | - |
| [viewpager](https://developer.android.com/jetpack/androidx/releases/viewpager.md.txt) | December 11, 2024 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/viewpager.md.txt#1.1.0) | - | - | - |
| [viewpager2](https://developer.android.com/jetpack/androidx/releases/viewpager2.md.txt) | May 14, 2024 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/viewpager2.md.txt#1.1.0) | - | - | - |
| [wear (\*)](https://developer.android.com/jetpack/androidx/releases/wear.md.txt) | November 04, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/wear.md.txt#1.4.0) | - | - | - |
| [wear.compose](https://developer.android.com/jetpack/androidx/releases/wear-compose.md.txt) | November 04, 2026 | [1.7.1](https://developer.android.com/jetpack/androidx/releases/wear-compose.md.txt#1.7.1) | - | - | [1.8.0-alpha03](https://developer.android.com/jetpack/androidx/releases/wear-compose.md.txt#1.8.0-alpha03) |
| [wear.compose.remote](https://developer.android.com/jetpack/androidx/releases/wear-compose-remote.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha15](https://developer.android.com/jetpack/androidx/releases/wear-compose-remote.md.txt#1.0.0-alpha15) |
| [wear.protolayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout.md.txt) | July 29, 2026 | [1.4.2](https://developer.android.com/jetpack/androidx/releases/wear-protolayout.md.txt#1.4.2) | - | - | - |
| [wear.tiles](https://developer.android.com/jetpack/androidx/releases/wear-tiles.md.txt) | July 29, 2026 | [1.6.2](https://developer.android.com/jetpack/androidx/releases/wear-tiles.md.txt#1.6.2) | - | - | - |
| [wear.watchface](https://developer.android.com/jetpack/androidx/releases/wear-watchface.md.txt) | February 25, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/wear-watchface.md.txt#1.3.0) | - | - | - |
| [wear.watchfacepush](https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush.md.txt) | April 08, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush.md.txt#1.0.0) | - | - | - |
| [web](https://developer.android.com/jetpack/androidx/releases/web.md.txt) | November 04, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/web.md.txt#1.0.0-alpha01) |
| [webgpu](https://developer.android.com/jetpack/androidx/releases/webgpu.md.txt) | October 07, 2026 | - | - | - | [1.0.0-alpha06](https://developer.android.com/jetpack/androidx/releases/webgpu.md.txt#1.0.0-alpha06) |
| [webkit](https://developer.android.com/jetpack/androidx/releases/webkit.md.txt) | November 04, 2026 | [1.18.0](https://developer.android.com/jetpack/androidx/releases/webkit.md.txt#1.18.0) | - | - | [1.19.0-alpha01](https://developer.android.com/jetpack/androidx/releases/webkit.md.txt#1.19.0-alpha01) |
| [window](https://developer.android.com/jetpack/androidx/releases/window.md.txt) | June 17, 2026 | [1.5.1](https://developer.android.com/jetpack/androidx/releases/window.md.txt#1.5.1) | - | - | [1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/window.md.txt#1.6.0-alpha05) |
| [window.extensions.core](https://developer.android.com/jetpack/androidx/releases/window-extensions-core.md.txt) | June 7, 2023 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/window-extensions-core.md.txt#1.0.0) | - | - | - |
| [work](https://developer.android.com/jetpack/androidx/releases/work.md.txt) | September 23, 2026 | [2.12.0](https://developer.android.com/jetpack/androidx/releases/work.md.txt#2.12.0) | - | - | - |
| [xr.arcore](https://developer.android.com/jetpack/androidx/releases/xr-arcore.md.txt) | October 21, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/xr-arcore.md.txt#1.0.0) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/xr-arcore.md.txt#1.1.0-alpha01) |
| [xr.compose](https://developer.android.com/jetpack/androidx/releases/xr-compose.md.txt) | October 21, 2026 | - | - | [1.0.0-beta02](https://developer.android.com/jetpack/androidx/releases/xr-compose.md.txt#1.0.0-beta02) | - |
| [xr.compose.material3](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3.md.txt) | May 19, 2026 | - | - | - | [1.0.0-alpha17](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3.md.txt#1.0.0-alpha17) |
| [xr.glimmer](https://developer.android.com/jetpack/androidx/releases/xr-glimmer.md.txt) | October 21, 2026 | - | - | - | [1.0.0-alpha22](https://developer.android.com/jetpack/androidx/releases/xr-glimmer.md.txt#1.0.0-alpha22) |
| [xr.projected](https://developer.android.com/jetpack/androidx/releases/xr-projected.md.txt) | October 21, 2026 | - | - | - | [1.0.0-alpha14](https://developer.android.com/jetpack/androidx/releases/xr-projected.md.txt#1.0.0-alpha14) |
| [xr.runtime](https://developer.android.com/jetpack/androidx/releases/xr-runtime.md.txt) | October 21, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/xr-runtime.md.txt#1.0.0) | - | - | [1.1.0-alpha02](https://developer.android.com/jetpack/androidx/releases/xr-runtime.md.txt#1.1.0-alpha02) |
| [xr.scenecore](https://developer.android.com/jetpack/androidx/releases/xr-scenecore.md.txt) | October 21, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/xr-scenecore.md.txt#1.0.0) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/xr-scenecore.md.txt#1.1.0-alpha01) |


(\*) This library has multiple artifacts. See its release notes for more information.  

Last updated: November 09, 2026