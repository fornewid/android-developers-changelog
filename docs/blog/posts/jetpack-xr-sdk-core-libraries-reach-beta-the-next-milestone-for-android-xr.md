---
title: https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr
url: https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Jetpack XR SDK core libraries reach beta: The next milestone for Android XR

2 min read ![](https://developer.android.com/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_Z1YdYO1.webp) 18 Aug 2026 3 Authors [Amy Zeppenfeld,](https://developer.android.com/blog/authors/amy-zeppenfeld) [Greg Underwood,](https://developer.android.com/blog/authors/greg-underwood) [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen) Since introducing the Android XR SDK, developers have transformed their ideas into innovative, immersive experiences for XR headsets and wired XR glasses. As the ecosystem expands, you can more easily take those experiences from preview to production and reach users wherever they are.

Today, we're excited to announce that **Jetpack SceneCore** , **ARCore for Jetpack XR** , and **XR Runtime** have reached beta with **Jetpack Compose for XR** to follow soon! This means the APIs are stabilizing, making it a great time to start integrating them into your production workflows and creating for Android XR.

### Why the Jetpack XR SDK?

The Jetpack XR SDK includes all the tools and libraries you need to build immersive and augmented experiences for Android XR. Whether you're porting an existing 2D app or creating a new 3D XR app from scratch, you can do so using the familiar Android development tools you already know and love.

To support your development, this release focuses on providing the fundamental building blocks across the SDK:

- [**Jetpack SceneCore**](https://developer.android.com/jetpack/androidx/releases/xr-scenecore): Build and manipulate the Android XR scene graph with 3D content. You can arrange [3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#place-3d-scenecore), play [spatial audio](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio), and use the robust [entity-component](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities) system to create, control, and manage entities.
- [**ARCore for Jetpack XR**](https://developer.android.com/jetpack/androidx/releases/xr-arcore): Bring digital content into the real world with perception capabilities. This library powers [depth estimation](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth), [persistent anchors](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors), [hit testing](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes#perform-hit-test), and [plane identification](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes).
- [**XR Runtime**](https://developer.android.com/jetpack/androidx/releases/xr-runtime): Provides the essential runtime foundation of the SDK, handling device lifecycles, session creation, and system configurations that enable the API surface.
- [**Jetpack Compose for XR**](https://developer.android.com/jetpack/androidx/releases/xr-compose): Create[spatial UI layouts](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose) that take advantage of Android XR's spatial capabilities. This library lets you use familiar Compose concepts to create spatial UIs and will be reaching Beta soon.

### What's new in Beta?

Direct feedback from the developer previews helped shape these beta releases, introducing several important API refinements to ensure these libraries are ready for production.

- **Expanded testing support: New capabilities are now available across the immersive XR libraries, including testing for** [**spatial audio**](https://developer.android.com/reference/androidx/xr/scenecore/testing/SpatialAudioTrackTester)**,** [**XR devices**](https://developer.android.com/reference/androidx/xr/runtime/testing/XrDeviceTestRule)**, and** [**session configuration**](https://developer.android.com/reference/kotlin/androidx/xr/runtime/testing/SessionTestRule)**. See the** [**release notes for each library**](https://developer.android.com/jetpack/androidx/explorer?case=all)**for details.**
- **Kotlin coroutines support** : To better align with Kotlin coroutines, [Session.create](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session) is now a suspend function.
- **Terminology and class updates** : AnchorEntity has been renamed to [AnchorSpace](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AnchorSpace), and both [ActivitySpace](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace) and [AnchorSpace](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AnchorSpace) now extend a common [SpaceEntity](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpaceEntity) class for more consistent spatial management across scenes.

See the full [release notes](https://developer.android.com/jetpack/androidx/versions) for each library to check out specific details on naming and API changes.

### Get started and provide feedback

To add these dependencies, include the Google Maven repository in your project and add the newest XR libraries to your build.gradle files.

```kotlin
dependencies {
    implementation("androidx.xr.scenecore:scenecore:1.0.0-beta02")
    implementation("androidx.xr.arcore:arcore:1.0.0-beta02")
    implementation("androidx.xr.runtime:runtime:1.0.0-beta02")

    implementation("androidx.xr.compose:compose:1.0.0-alpha17")

}
```

The ecosystem of Android XR devices that power immersive experiences is expanding, ranging from XR headsets to wired XR glasses. There's never been a better time to start building immersive experiences with the Jetpack XR SDK Beta. Dive in and start building and testing on [Samsung Galaxy XR](https://www.samsung.com/us/xr/galaxy-xr/galaxy-xr/) or [Android XR Emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses) today.
- [#Jetpack XR SDK](https://developer.android.com/blog/topics/jetpack-xr-sdk)
- [#Android XR](https://developer.android.com/blog/topics/android-xr)
- [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
Written by:

-

  ## [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/amy-zeppenfeld) ![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp) ![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)
-

  ## [Greg Underwood](https://developer.android.com/blog/authors/greg-underwood)

  ###### Software Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/greg-underwood) ![View Greg Underwood's profile](https://developer.android.com/static/blog/assets/PXL_20260813_200301431_PORTRAIT_7a5276fd7a_Z1fcMvp.webp) ![View Greg Underwood's profile](https://developer.android.com/static/blog/assets/PXL_20260813_200301431_PORTRAIT_7a5276fd7a_Z1fcMvp.webp)
-

  ## [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/yasmine-evjen) ![View Yasmine Evjen's profile](https://developer.android.com/static/blog/assets/unnamed_3_41b10aa98e_Z1Fjttc.webp) ![View Yasmine Evjen's profile](https://developer.android.com/static/blog/assets/unnamed_3_41b10aa98e_Z1Fjttc.webp)
Continue reading
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld)[![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 4](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4)

  [arrow_forward](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4) We're excited to launch Developer Preview 4 of the Android XR SDK, continuing our focus on unifying cross-device development for headsets, wired XR glasses, and intelligent eyewear.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld), [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva) • 5 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
  - [#Developer Preview](https://developer.android.com/blog/topics/developer-preview)
  - [#Unity](https://developer.android.com/blog/topics/unity)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +3 ↩
- [![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1R62M0.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.
  [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) • 2 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)
- [![View Luke Hopkins's profile](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![View Ryan Bartley's profile](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.
  [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) • 4 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)