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

The [AndroidX recent release notes page](https://developer.android.com/jetpack/androidx/versions/all-channel)
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

AndroidX libraries have the default `minSdk` of 23. Individual libraries might
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

<br />

| Maven Group ID | Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|---|
| [activity](https://developer.android.com/jetpack/androidx/releases/activity) | March 11, 2026 | [1.13.0](https://developer.android.com/jetpack/androidx/releases/activity#1.13.0) | - | - | - |
| [ads](https://developer.android.com/jetpack/androidx/releases/ads) | March 8, 2023 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/ads#1.0.0-alpha05) |
| [annotation (\*)](https://developer.android.com/jetpack/androidx/releases/annotation) | July 15, 2026 | [1.10.0](https://developer.android.com/jetpack/androidx/releases/annotation#1.10.0) | - | - | [1.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/annotation#1.11.0-alpha01) |
| [appcompat](https://developer.android.com/jetpack/androidx/releases/appcompat) | April 08, 2026 | [1.7.1](https://developer.android.com/jetpack/androidx/releases/appcompat#1.7.1) | - | - | [1.8.0-alpha01](https://developer.android.com/jetpack/androidx/releases/appcompat#1.8.0-alpha01) |
| [appfunctions](https://developer.android.com/jetpack/androidx/releases/appfunctions) | July 01, 2026 | - | - | - | [1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/appfunctions#1.0.0-alpha10) |
| [appsearch](https://developer.android.com/jetpack/androidx/releases/appsearch) | March 25, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/appsearch#1.1.0) | - | - | [1.2.0-alpha01](https://developer.android.com/jetpack/androidx/releases/appsearch#1.2.0-alpha01) |
| [arch.core](https://developer.android.com/jetpack/androidx/releases/arch-core) | February 22, 2023 | [2.2.0](https://developer.android.com/jetpack/androidx/releases/arch-core#2.2.0) | - | - | - |
| [asynclayoutinflater](https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/asynclayoutinflater#1.1.0) | - | - | - |
| [autofill](https://developer.android.com/jetpack/androidx/releases/autofill) | June 4, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/autofill#1.3.0) | - | - | - |
| [benchmark](https://developer.android.com/jetpack/androidx/releases/benchmark) | July 01, 2026 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/benchmark#1.4.1) | - | - | [1.5.0-alpha07](https://developer.android.com/jetpack/androidx/releases/benchmark#1.5.0-alpha07) |
| [biometric](https://developer.android.com/jetpack/androidx/releases/biometric) | April 22, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/biometric#1.1.0) | - | - | [1.4.0-alpha07](https://developer.android.com/jetpack/androidx/releases/biometric#1.4.0-alpha07) |
| [bluetooth](https://developer.android.com/jetpack/androidx/releases/bluetooth) | November 29, 2023 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/bluetooth#1.0.0-alpha02) |
| [browser](https://developer.android.com/jetpack/androidx/releases/browser) | March 25, 2026 | [1.10.0](https://developer.android.com/jetpack/androidx/releases/browser#1.10.0) | - | - | - |
| [car-app](https://developer.android.com/jetpack/androidx/releases/car-app) | May 19, 2026 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/car-app#1.7.0) | - | [1.8.0-beta01](https://developer.android.com/jetpack/androidx/releases/car-app#1.8.0-beta01) | [1.9.0-alpha01](https://developer.android.com/jetpack/androidx/releases/car-app#1.9.0-alpha01) |
| [camera (\*)](https://developer.android.com/jetpack/androidx/releases/camera) | July 01, 2026 | [1.6.1](https://developer.android.com/jetpack/androidx/releases/camera#1.6.1) | - | - | [1.7.0-alpha02](https://developer.android.com/jetpack/androidx/releases/camera#1.7.0-alpha02) |
| [camera.media3](https://developer.android.com/jetpack/androidx/releases/camera-media3) | August 13, 2025 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/camera-media3#1.0.0-alpha04) |
| [camera.featurecombinationquery](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery) | July 01, 2026 | [1.6.1](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery#1.6.1) | - | - | [1.7.0-alpha02](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery#1.7.0-alpha02) |
| [camera.viewfinder (\*)](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder) | July 01, 2026 | [1.6.1](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.6.1) | - | - | [1.7.0-alpha02](https://developer.android.com/jetpack/androidx/releases/camera-viewfinder#1.7.0-alpha02) |
| [cardview](https://developer.android.com/jetpack/androidx/releases/cardview) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/cardview#1.0.0) | - | - | - |
| [collection](https://developer.android.com/jetpack/androidx/releases/collection) | March 11, 2026 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/collection#1.6.0) | - | - | - |
| [compose](https://developer.android.com/jetpack/androidx/releases/compose) | August 7, 2024 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/compose#1.6.0) | - | - | - |
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | July 01, 2026 | [1.11.4](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.11.4) | - | [1.12.0-beta02](https://developer.android.com/jetpack/androidx/releases/compose-animation#1.12.0-beta02) | - |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | August 7, 2024 | [1.5.15](https://developer.android.com/jetpack/androidx/releases/compose-compiler#1.5.15) | - | - | - |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | July 01, 2026 | [1.11.4](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.11.4) | - | [1.12.0-beta02](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.12.0-beta02) | - |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | July 01, 2026 | [1.11.4](https://developer.android.com/jetpack/androidx/releases/compose-material#1.11.4) | - | [1.12.0-beta02](https://developer.android.com/jetpack/androidx/releases/compose-material#1.12.0-beta02) | - |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | July 15, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.4.0) | - | - | [1.5.0-alpha24](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.5.0-alpha24) |
| [compose.material3.adaptive](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) | June 17, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.2.0) | [1.3.0-rc01](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.3.0-rc01) | - | - |
| [compose.remote](https://developer.android.com/jetpack/androidx/releases/compose-remote) | July 15, 2026 | - | - | - | [1.0.0-alpha15](https://developer.android.com/jetpack/androidx/releases/compose-remote#1.0.0-alpha15) |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | July 01, 2026 | [1.11.4](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.11.4) | - | [1.12.0-beta02](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.12.0-beta02) | - |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | July 01, 2026 | [1.11.4](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.11.4) | - | [1.12.0-beta02](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.0-beta02) | - |
| [concurrent](https://developer.android.com/jetpack/androidx/releases/concurrent) | July 16, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/concurrent#1.3.0) | - | - | - |
| [constraintlayout (\*)](https://developer.android.com/jetpack/androidx/releases/constraintlayout) | February 26, 2025 | [2.2.1](https://developer.android.com/jetpack/androidx/releases/constraintlayout#2.2.1) | - | - | - |
| [contentpager](https://developer.android.com/jetpack/androidx/releases/contentpager) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/contentpager#1.0.0) | - | - | - |
| [coordinatorlayout](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout) | February 26, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout#1.3.0) | - | - | - |
| [locationbutton (\*)](https://developer.android.com/jetpack/androidx/releases/locationbutton) | June 17, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/locationbutton#1.0.0-alpha01) |
| [core (\*)](https://developer.android.com/jetpack/androidx/releases/core) | July 01, 2026 | [1.19.0](https://developer.android.com/jetpack/androidx/releases/core#1.19.0) | - | - | - |
| [core.uwb](https://developer.android.com/jetpack/androidx/releases/core-uwb) | May 19, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/core-uwb#1.0.0) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/core-uwb#1.1.0-alpha01) |
| [credentials](https://developer.android.com/jetpack/androidx/releases/credentials) | May 06, 2026 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/credentials#1.6.0) | - | - | [1.7.0-alpha02](https://developer.android.com/jetpack/androidx/releases/credentials#1.7.0-alpha02) |
| [credentials.providerevents](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents) | March 11, 2026 | - | - | - | [1.0.0-alpha06](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents#1.0.0-alpha06) |
| [credentials.registry](https://developer.android.com/jetpack/androidx/releases/credentials-registry) | December 17, 2025 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/credentials-registry#1.0.0-alpha04) |
| [cursoradapter](https://developer.android.com/jetpack/androidx/releases/cursoradapter) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/cursoradapter#1.0.0) | - | - | - |
| [customview (\*)](https://developer.android.com/jetpack/androidx/releases/customview) | April 23, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/customview#customview-1.2.0) | - | - | - |
| [databinding](https://developer.android.com/jetpack/androidx/releases/databinding) | September 5, 2019 | [3.5.0](https://developer.android.com/jetpack/androidx/releases/databinding#3.5.0) | - | - | [3.6.0-alpha10](https://developer.android.com/jetpack/androidx/releases/databinding#3.6.0-alpha10) |
| [datastore](https://developer.android.com/jetpack/androidx/releases/datastore) | May 06, 2026 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/datastore#1.2.1) | - | - | [1.3.0-alpha09](https://developer.android.com/jetpack/androidx/releases/datastore#1.3.0-alpha09) |
| [documentfile](https://developer.android.com/jetpack/androidx/releases/documentfile) | May 7, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/documentfile#1.1.0) | - | - | - |
| [draganddrop](https://developer.android.com/jetpack/androidx/releases/draganddrop) | May 11, 2022 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/draganddrop#1.0.0) | - | - | - |
| [drawerlayout](https://developer.android.com/jetpack/androidx/releases/drawerlayout) | March 22, 2023 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/drawerlayout#1.2.0) | - | - | - |
| [dynamicanimation](https://developer.android.com/jetpack/androidx/releases/dynamicanimation) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/dynamicanimation#1.1.0) | - | - | - |
| [emoji](https://developer.android.com/jetpack/androidx/releases/emoji) | December 17, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/emoji#1.2.0) | - | - | - |
| [emoji2](https://developer.android.com/jetpack/androidx/releases/emoji2) | September 10, 2025 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/emoji2#1.6.0) | - | - | - |
| [enterprise](https://developer.android.com/jetpack/androidx/releases/enterprise) | January 13, 2021 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/enterprise#1.1.0) | - | - | - |
| [exifinterface](https://developer.android.com/jetpack/androidx/releases/exifinterface) | December 3, 2025 | [1.4.2](https://developer.android.com/jetpack/androidx/releases/exifinterface#1.4.2) | - | - | - |
| [fragment](https://developer.android.com/jetpack/androidx/releases/fragment) | July 01, 2026 | [1.8.9](https://developer.android.com/jetpack/androidx/releases/fragment#1.8.9) | - | - | [1.9.0-alpha02](https://developer.android.com/jetpack/androidx/releases/fragment#1.9.0-alpha02) |
| [games (\*)](https://developer.android.com/jetpack/androidx/releases/games) | May 06, 2026 | [4.4.2](https://developer.android.com/jetpack/androidx/releases/games#games-activity-4.4.2) | - | - | - |
| [glance](https://developer.android.com/jetpack/androidx/releases/glance) | July 01, 2026 | [1.1.1](https://developer.android.com/jetpack/androidx/releases/glance#1.1.1) | [1.2.0-rc01](https://developer.android.com/jetpack/androidx/releases/glance#1.2.0-rc01) | - | [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/glance#1.3.0-alpha02) |
| [glance.wear](https://developer.android.com/jetpack/androidx/releases/glance-wear) | July 15, 2026 | - | - | - | [1.0.0-alpha14](https://developer.android.com/jetpack/androidx/releases/glance-wear#1.0.0-alpha14) |
| [graphics (\*)](https://developer.android.com/jetpack/androidx/releases/graphics) | May 06, 2026 | [1.0.4](https://developer.android.com/jetpack/androidx/releases/graphics#graphics-core-1.0.4) | - | - | - |
| [gridlayout](https://developer.android.com/jetpack/androidx/releases/gridlayout) | April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/gridlayout#1.1.0) | - | - | - |
| [health](https://developer.android.com/jetpack/androidx/releases/health) | May 06, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/health#1.0.0) | [1.1.0-rc02](https://developer.android.com/jetpack/androidx/releases/health#1.1.0-rc02) | - | - |
| [health.connect](https://developer.android.com/jetpack/androidx/releases/health-connect) | April 22, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0) | - | - | [1.2.0-alpha04](https://developer.android.com/jetpack/androidx/releases/health-connect#1.2.0-alpha04) |
| [heifwriter](https://developer.android.com/jetpack/androidx/releases/heifwriter) | October 22, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/heifwriter#1.1.0) | - | - | [1.2.0-alpha01](https://developer.android.com/jetpack/androidx/releases/heifwriter#1.2.0-alpha01) |
| [hilt](https://developer.android.com/jetpack/androidx/releases/hilt) | July 01, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/hilt#1.4.0) | - | - | - |
| [ink](https://developer.android.com/jetpack/androidx/releases/ink) | July 15, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/ink#1.0.0) | - | - | [1.1.0-alpha05](https://developer.android.com/jetpack/androidx/releases/ink#1.1.0-alpha05) |
| [input](https://developer.android.com/jetpack/androidx/releases/input) | November 19, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/input#1.0.0) | - | - | - |
| [interpolator](https://developer.android.com/jetpack/androidx/releases/interpolator) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/interpolator#1.0.0) | - | - | - |
| [javascriptengine](https://developer.android.com/jetpack/androidx/releases/javascriptengine) | May 06, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/javascriptengine#1.1.0) | - | - | - |
| [jetifier](https://developer.android.com/jetpack/androidx/releases/jetifier) | September 2, 2020 | - | - | [1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/jetifier#1.0.0-beta10) | - |
| [leanback](https://developer.android.com/jetpack/androidx/releases/leanback) | June 17, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/leanback#1.2.0) | - | - | [1.3.0-alpha02](https://developer.android.com/jetpack/androidx/releases/leanback#1.3.0-alpha02) |
| [legacy](https://developer.android.com/jetpack/androidx/releases/legacy) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/legacy#1.0.0) | - | - | - |
| [lifecycle (\*)](https://developer.android.com/jetpack/androidx/releases/lifecycle) | June 17, 2026 | [2.11.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0) | - | - | - |
| [lint](https://developer.android.com/jetpack/androidx/releases/lint) | June 17, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/lint#1.0.0) | - | - | - |
| [loader](https://developer.android.com/jetpack/androidx/releases/loader) | July 15, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/loader#1.1.0) | [1.2.0-rc01](https://developer.android.com/jetpack/androidx/releases/loader#1.2.0-rc01) | - | - |
| [localbroadcastmanager](https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager) | January 12, 2022 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager#1.1.0) | - | - | - |
| [media](https://developer.android.com/jetpack/androidx/releases/media) | May 06, 2026 | [1.8.0](https://developer.android.com/jetpack/androidx/releases/media#1.8.0) | - | - | - |
| [media3](https://developer.android.com/jetpack/androidx/releases/media3) | July 7, 2026 | [1.10.1](https://developer.android.com/jetpack/androidx/releases/media3#1.10.1) | - | [1.11.0-beta01](https://developer.android.com/jetpack/androidx/releases/media3#1.11.0-beta01) | [1.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/media3#1.11.0-alpha01) |
| [mediarouter](https://developer.android.com/jetpack/androidx/releases/mediarouter) | February 11, 2026 | [1.8.1](https://developer.android.com/jetpack/androidx/releases/mediarouter#1.8.1) | - | - | [1.9.0-alpha01](https://developer.android.com/jetpack/androidx/releases/mediarouter#1.9.0-alpha01) |
| [multidex](https://developer.android.com/jetpack/androidx/releases/multidex) | December 17, 2018 | [2.0.1](https://developer.android.com/jetpack/androidx/releases/multidex#2.0.1) | - | - | - |
| [metrics](https://developer.android.com/jetpack/androidx/releases/metrics) | October 8, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/metrics#1.0.0) | - | - | - |
| [navigation](https://developer.android.com/jetpack/androidx/releases/navigation) | July 01, 2026 | [2.9.8](https://developer.android.com/jetpack/androidx/releases/navigation#2.9.8) | - | - | [2.10.0-alpha06](https://developer.android.com/jetpack/androidx/releases/navigation#2.10.0-alpha06) |
| [navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3) | July 15, 2026 | [1.1.4](https://developer.android.com/jetpack/androidx/releases/navigation3#1.1.4) | - | - | [1.2.0-alpha06](https://developer.android.com/jetpack/androidx/releases/navigation3#1.2.0-alpha06) |
| [navigationevent](https://developer.android.com/jetpack/androidx/releases/navigationevent) | July 15, 2026 | [1.1.2](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.1.2) | - | - | [1.2.0-alpha02](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.2.0-alpha02) |
| [paging (\*)](https://developer.android.com/jetpack/androidx/releases/paging) | May 06, 2026 | [3.5.0](https://developer.android.com/jetpack/androidx/releases/paging#3.5.0) | - | - | - |
| [palette](https://developer.android.com/jetpack/androidx/releases/palette) | July 01, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/palette#1.0.0) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/palette#1.1.0-alpha01) |
| [pdf](https://developer.android.com/jetpack/androidx/releases/pdf) | July 01, 2026 | - | - | - | [1.0.0-alpha19](https://developer.android.com/jetpack/androidx/releases/pdf#1.0.0-alpha19) |
| [percentlayout](https://developer.android.com/jetpack/androidx/releases/percentlayout) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/percentlayout#1.0.0) | - | - | - |
| [performance](https://developer.android.com/jetpack/androidx/releases/performance) | January 15, 2025 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/performance#1.0.0-alpha01) |
| [photopicker](https://developer.android.com/jetpack/androidx/releases/photopicker) | July 01, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/photopicker#1.0.0-alpha02) |
| [preference](https://developer.android.com/jetpack/androidx/releases/preference) | July 26, 2023 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/preference#1.2.1) | - | - | - |
| [print](https://developer.android.com/jetpack/androidx/releases/print) | April 23, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/print#1.1.0) | - | - | - |
| [privacysandbox.activity](https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity) | December 17, 2025 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/privacysandbox-activity#1.0.0-alpha03) |
| [privacysandbox.ads](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads) | May 7, 2025 | - | - | [1.1.0-beta13](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ads#1.1.0-beta13) | - |
| [privacysandbox.plugins](https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins) | August 9, 2023 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/privacysandbox-plugins#1.0.0-alpha02) |
| [privacysandbox.sdkruntime](https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime) | December 17, 2025 | - | - | - | [1.0.0-alpha19](https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime#1.0.0-alpha19) |
| [privacysandbox.tools](https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools) | December 17, 2025 | - | - | - | [1.0.0-alpha14](https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools#1.0.0-alpha14) |
| [privacysandbox.ui](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui) | December 17, 2025 | - | - | - | [1.0.0-alpha17](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui#1.0.0-alpha17) |
| [profileinstaller](https://developer.android.com/jetpack/androidx/releases/profileinstaller) | October 2, 2024 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.4.1) | - | - | - |
| [recommendation](https://developer.android.com/jetpack/androidx/releases/recommendation) | September 21, 2018 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/recommendation#1.0.0) | - | - | - |
| [recyclerview (\*)](https://developer.android.com/jetpack/androidx/releases/recyclerview) | December 17, 2025 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/recyclerview#1.4.0) | - | - | - |
| [remotecallback](https://developer.android.com/jetpack/androidx/releases/remotecallback) | November 19, 2025 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/remotecallback#1.0.0-alpha03) |
| [resourceinspection](https://developer.android.com/jetpack/androidx/releases/resourceinspection) | January 26, 2022 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/resourceinspection#1.0.1) | - | - | - |
| [room](https://developer.android.com/jetpack/androidx/releases/room) | November 19, 2025 | [2.8.4](https://developer.android.com/jetpack/androidx/releases/room#2.8.4) | - | - | - |
| [room3](https://developer.android.com/jetpack/androidx/releases/room3) | July 01, 2026 | [3.0.0](https://developer.android.com/jetpack/androidx/releases/room3#3.0.0) | - | - | - |
| [savedstate](https://developer.android.com/jetpack/androidx/releases/savedstate) | May 19, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/savedstate#1.5.0) | - | - | - |
| [security (\*)](https://developer.android.com/jetpack/androidx/releases/security) | June 17, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/security#1.1.0) | - | - | - |
| [sharetarget](https://developer.android.com/jetpack/androidx/releases/sharetarget) | October 5, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/sharetarget#1.2.0) | - | - | - |
| [slice](https://developer.android.com/jetpack/androidx/releases/slice) | January 13, 2021 | - | - | - | [1.1.0-alpha02](https://developer.android.com/jetpack/androidx/releases/slice#1.1.0-alpha02) |
| [slidingpanelayout](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout) | January 26, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout#1.2.0) | - | - | - |
| [startup](https://developer.android.com/jetpack/androidx/releases/startup) | September 18, 2024 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/startup#1.2.0) | - | - | - |
| [sqlite](https://developer.android.com/jetpack/androidx/releases/sqlite) | July 01, 2026 | [2.7.0](https://developer.android.com/jetpack/androidx/releases/sqlite#2.7.0) | - | - | - |
| [swiperefreshlayout](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout) | December 3, 2025 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout#1.2.0) | - | - | - |
| [test (\*)](https://developer.android.com/jetpack/androidx/releases/test) | January 14, 2026 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/test#1.0.1) | - | - | [1.1.0-alpha04](https://developer.android.com/jetpack/androidx/releases/test#1.1.0-alpha04) |
| [test.ext](https://developer.android.com/jetpack/androidx/releases/test-ext) | May 19, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/test-ext#1.0.0-alpha03) |
| [test.uiautomator](https://developer.android.com/jetpack/androidx/releases/test-uiautomator) | July 01, 2026 | [2.4.0](https://developer.android.com/jetpack/androidx/releases/test-uiautomator#2.4.0) | - | - | - |
| [text-vertical](https://developer.android.com/jetpack/androidx/releases/text-vertical) | April 22, 2026 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/text-vertical#1.0.0-alpha05) |
| [textclassifier](https://developer.android.com/jetpack/androidx/releases/textclassifier) | March 23, 2022 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/textclassifier#1.0.0-alpha04) |
| [tracing](https://developer.android.com/jetpack/androidx/releases/tracing) | July 15, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/tracing#1.3.0) | - | [2.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/tracing#2.0.0-beta01) | - |
| [transition](https://developer.android.com/jetpack/androidx/releases/transition) | January 14, 2026 | [1.7.0](https://developer.android.com/jetpack/androidx/releases/transition#1.7.0) | - | - | - |
| [tv (\*)](https://developer.android.com/jetpack/androidx/releases/tv) | May 06, 2026 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/tv#1.1.0) | - | - | - |
| [tvprovider](https://developer.android.com/jetpack/androidx/releases/tvprovider) | May 7, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/tvprovider#1.1.0) | - | - | - |
| [vectordrawable](https://developer.android.com/jetpack/androidx/releases/vectordrawable) | May 1, 2024 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/vectordrawable#1.2.0) | - | - | - |
| [versionedparcelable](https://developer.android.com/jetpack/androidx/releases/versionedparcelable) | January 29, 2025 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/versionedparcelable#1.2.1) | - | - | - |
| [viewpager](https://developer.android.com/jetpack/androidx/releases/viewpager) | December 11, 2024 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/viewpager#1.1.0) | - | - | - |
| [viewpager2](https://developer.android.com/jetpack/androidx/releases/viewpager2) | May 14, 2024 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/viewpager2#1.1.0) | - | - | - |
| [wear (\*)](https://developer.android.com/jetpack/androidx/releases/wear) | July 15, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/wear#1.4.0) | - | - | - |
| [wear.compose](https://developer.android.com/jetpack/androidx/releases/wear-compose) | July 15, 2026 | [1.6.2](https://developer.android.com/jetpack/androidx/releases/wear-compose#1.6.2) | - | - | [1.7.0-alpha06](https://developer.android.com/jetpack/androidx/releases/wear-compose#1.7.0-alpha06) |
| [wear.compose.remote](https://developer.android.com/jetpack/androidx/releases/wear-compose-remote) | July 01, 2026 | - | - | - | [1.0.0-alpha07](https://developer.android.com/jetpack/androidx/releases/wear-compose-remote#1.0.0-alpha07) |
| [wear.protolayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout) | July 01, 2026 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/wear-protolayout#1.4.1) | - | - | - |
| [wear.tiles](https://developer.android.com/jetpack/androidx/releases/wear-tiles) | July 01, 2026 | [1.6.1](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.6.1) | - | - | - |
| [wear.watchface](https://developer.android.com/jetpack/androidx/releases/wear-watchface) | February 25, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/wear-watchface#1.3.0) | - | - | - |
| [wear.watchfacepush](https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush) | April 08, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush#1.0.0) | - | - | - |
| [webgpu](https://developer.android.com/jetpack/androidx/releases/webgpu) | April 22, 2026 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/webgpu#1.0.0-alpha05) |
| [webkit](https://developer.android.com/jetpack/androidx/releases/webkit) | July 15, 2026 | [1.16.0](https://developer.android.com/jetpack/androidx/releases/webkit#1.16.0) | - | - | [1.17.0-alpha04](https://developer.android.com/jetpack/androidx/releases/webkit#1.17.0-alpha04) |
| [window](https://developer.android.com/jetpack/androidx/releases/window) | June 17, 2026 | [1.5.1](https://developer.android.com/jetpack/androidx/releases/window#1.5.1) | - | - | [1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/window#1.6.0-alpha05) |
| [window.extensions.core](https://developer.android.com/jetpack/androidx/releases/window-extensions-core) | June 7, 2023 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/window-extensions-core#1.0.0) | - | - | - |
| [work](https://developer.android.com/jetpack/androidx/releases/work) | July 15, 2026 | [2.11.2](https://developer.android.com/jetpack/androidx/releases/work#2.11.2) | - | - | [2.12.0-alpha01](https://developer.android.com/jetpack/androidx/releases/work#2.12.0-alpha01) |
| [xr.arcore](https://developer.android.com/jetpack/androidx/releases/xr-arcore) | July 15, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/xr-arcore#1.0.0-beta01) | - |
| [xr.compose](https://developer.android.com/jetpack/androidx/releases/xr-compose) | July 15, 2026 | - | - | - | [1.0.0-alpha16](https://developer.android.com/jetpack/androidx/releases/xr-compose#1.0.0-alpha16) |
| [xr.compose.material3](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3) | May 19, 2026 | - | - | - | [1.0.0-alpha17](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3#1.0.0-alpha17) |
| [xr.glimmer](https://developer.android.com/jetpack/androidx/releases/xr-glimmer) | July 01, 2026 | - | - | - | [1.0.0-alpha15](https://developer.android.com/jetpack/androidx/releases/xr-glimmer#1.0.0-alpha15) |
| [xr.projected](https://developer.android.com/jetpack/androidx/releases/xr-projected) | July 15, 2026 | - | - | - | [1.0.0-alpha10](https://developer.android.com/jetpack/androidx/releases/xr-projected#1.0.0-alpha10) |
| [xr.runtime](https://developer.android.com/jetpack/androidx/releases/xr-runtime) | July 15, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/xr-runtime#1.0.0-beta01) | - |
| [xr.scenecore](https://developer.android.com/jetpack/androidx/releases/xr-scenecore) | July 15, 2026 | - | - | [1.0.0-beta01](https://developer.android.com/jetpack/androidx/releases/xr-scenecore#1.0.0-beta01) | - |

<br />


(\*) This library has multiple artifacts. See its release notes for more information.  

Last updated: July 15, 2026