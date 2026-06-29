---
title: https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4
url: https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Updates to the Android XR SDK: Introducing Developer Preview 4

5-min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp) 19 May 2026 [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld)[![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva) [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld) \& [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva) Today we're excited to launch Developer Preview 4 of the Android XR SDK, continuing our focus on unifying cross-device development for headsets, wired XR glasses, and [intelligent eyewear](https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026). To keep our platform intuitive, we are adopting more descriptive naming for our form factors, where AI glasses are now audio glasses and display AI glasses are now display glasses, with these changes appearing in our documentation starting today.

This release is packed with updates that help you build incredible experiences for XR devices, enable deeper immersive experiences on XR headsets, and streamline the path for creating augmented experiences on audio and display glasses. Also, our core libraries---including XR Runtime, Jetpack SceneCore, and ARCore for Jetpack XR--- will be officially moving to Beta soon!

To give you early access to hardware and resources for building immersive and augmented experiences on upcoming devices---like display and audio glasses and XREAL's Project Aura --- we're announcing the [Android XR Developer Catalyst Program](https://goo.gle/Catalyst_IO26). Learn more and [start your application](http://g.co/dev/catalyst) today.

## Building Augmented Experiences for Audio and Display Glasses

Starting out with our libraries for augmented experiences, Developer Preview 4 introduces new APIs that help you create and test your apps.

### Jetpack Projected: Device Availability and ProjectedTestRule APIs

The Jetpack Projected library helps bridge app experiences from the phone to the user's field of view. We've added the [Device Availability API,](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-availability) which consolidates wear state and connectivity signals into standard Android [`Lifecycle.State`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State) values. This lets you adjust your applications behavior based on whether the device is worn.

```kotlin
val xrDevice = XrDevice.getCurrentDevice(projectedContext)

// Observe the device lifecycle flow
xrDevice.getLifecycle().currentStateFlow
    .collect { state ->
        when (state) {
            Lifecycle.State.STARTED -> { /* Device is available (worn) */ }
            Lifecycle.State.CREATED -> { /* Device is unavailable (not worn) */ }
            Lifecycle.State.DESTROYED -> { /* Device is DISCONNECTED */ }
        }
    }
```

To simplify testing, the new [`ProjectedTestRule`](https://developer.android.com/reference/kotlin/androidx/xr/projected/testing/ProjectedTestRule) API in the projected-testing artifact automates the setup of projected test environments. This helps you write clean, reliable unit tests without the boilerplate code.

```kotlin
// from the 'androidx.xr.projected:projected-testing:1.0.0-alpha07' artifact
@get:Rule
val projectedTestRule = ProjectedTestRule()

@Test
fun testProjectedContextInitialization() {
    // by default, ProjectedTestRule automatically creates and connects
    // a projected device before each test
    val projectedContext = ProjectedContext.createProjectedDeviceContext(context)

    // assert the projected context is successfully initialized
    assertThat(projectedContext).isNotNull()
}
```

### Jetpack Compose Glimmer: Google Sans Flex and new components

Our UI library for display glasses, Jetpack Compose Glimmer, now includes [Google Sans Flex](https://fonts.google.com/specimen/Google+Sans+Flex) for improved legibility on optical see-through displays. We've also added several interactive components:

- [Stacks](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/vertical-stacks): Designed for touchpad-optimized groups, showing one item at a time.
- [Title Chips](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips): Provides categorization and context for content cards.

![glimmer (1).gif](https://developer.android.com/static/blog/assets/glimmer_1_8146fe1828_Z1U7Jvt.webp)

## Building Immersive Experiences for XR Headsets and Wired XR Glasses

If you're looking to build fully immersive experiences for XR Headsets and wired XR Glasses, we have several big updates.

### Beta Transition \& Modern Architecture

XR Runtime, Jetpack SceneCore, and the ARCore for Jetpack XR perception features ([Depth Maps](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth), [Eye/Hand Tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face), Hit Testing, and [Spatial Anchors](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors)) will soon move to Beta, so we've streamlined the Jetpack XR APIs. We've removed legacy Guava and RxJava3 packages in favor of a modern, Kotlin-first architecture.

### Jetpack SceneCore: glTF and Custom Meshes

We're expanding 3D model capabilities by adding the ability to fine tune 3D models and access specific nodes with a 3D model. Using [GltfModelNode](https://developer.android.com/reference/androidx/xr/scenecore/GltfModelNode), you can modify properties like pose, materials, and textures, and even run [animations](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfAnimation) for specific nodes.

```kotlin
// Create a new PBR material
pbrMaterial = KhronosPbrMaterial.create(
    session = xrSession,
    alphaMode = AlphaMode.OPAQUE
)

// Load a texture.
val texture = Texture.create(
    session = xrSession,
    path = Path("textures/texture_name.png")
)

// Apply the texture and configure occlusion to define how the material handles ambient lighting.
pbrMaterial.setOcclusionTexture(
    texture = texture,
    strength = 0.5f
)

// Access the hierarchy of nodes within the model entity.
val entityNodes = entity.nodes

// Find the specific node to apply the material override.
val myEntityNode = entityNodes.find { it.name == "node_name" }

// Apply the PBR material to the node.
myEntityNode?.setMaterialOverride(
   material = newMaterial
)
```

We're also bringing Custom Meshes to SceneCore. Custom meshes let you build geometry on the fly programmatically, which is ideal for creating custom 3D models. This feature will launch as experimental, so try it out and let us know what you think!

```kotlin
// Create the mesh
val roadMesh =
    CustomMesh.BuilderFromMeshData(session, roadVertexLayout)
        .addVertexData(ByteBufferRegion(roadDataBuffer, 0, vertexDataSize))
        .setIndexData(ByteBufferRegion(roadDataBuffer, vertexDataSize, indexDataSize))
        .setTopology(MeshSubsetTopology.TRIANGLES)
        .build()

// Define the material
val roadMaterial = KhronosPbrMaterial.create(session, AlphaMode.OPAQUE)

// Instantiate the entity using the custom mesh and material
val roadEntity =
    MeshEntity.create(
        session,
        roadMesh,
        listOf(roadMaterial),
        pose = roadPose,
    )
```

### Compose for XR: Native glTF Support

We now have native glTF support directly in Compose for XR with [SpatialGltfModel](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModel.composable). Use this along with [SpatiallGltfModelState](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#SpatialGltfModelState(androidx.xr.compose.subspace.SpatialGltfModelSource)) to access [nodes](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#nodes()) and [animations](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#animations()) in the glTF model, or use them to add textures and materials to your 3D models.

```kotlin
val myGltfModelState = rememberSpatialGltfModelState(
        source = SpatialGltfModelSource.fromPath(
            Paths.get("models/my_animated_model.glb")
        )
    )

    val myGltfAnimation =
        myGltfModelState.animations.find { it.name == "animation_name" }

    DisposableEffect(myGltfAnimation) {
        myGltfAnimation?.loop()

        onDispose {
            myGltfAnimation?.stop()
        }
    }

    SpatialGltfModel(state = myGltfModelState, modifier = modifier)
```

### ARCore for Jetpack XR: Geospatial API Preview for Wired XR Glasses

We're also providing an early preview of the Geospatial API for wired XR Glasses in ARCore for Jetpack XR. This update enables high-precision anchoring of digital content tied to real-world locations in over 87 countries.

By combining ARCore's Visual Positioning System (VPS) with the reasoning and audio capabilities of the Gemini Live API, you can create contextually aware experiences that understand both the location and position of your user. Imagine building an immersive, AI-guided walking tour that provides real-time audio descriptions of nearby places, seamlessly blending digital information with the physical environment.

## Start Building the Future Today

It's an amazing time to develop for Android XR. With the Jetpack XR SDK moving to Beta soon and a robust set of new tools at your fingertips, explore each of the following areas to get your app's experiences ready for XR!

### Read the documentation, explore the samples, and check out the XR experiments

Head to the [official Android Developer site](http://developer.android.com/xr) for full technical guides, API reference, and instructions on setting up the new emulator. Get inspired with our samples and experiments. See how we've used these APIs to build immersive spatial layouts, load 3D models, explore spatial audio, and more!

- [Visit the Android XR webpage](http://developer.android.com/xr)
- [Explore XR samples](https://developer.android.com/develop/xr/samples)
- [Explore XR experiments](https://developer.android.com/develop/xr/experiments)

### Check out what's new for game engines

We've added official support for [Unreal Engine](https://www.unrealengine.com/) and [Godot](https://godotengine.org/), and we've launched two new tools to accelerate development for Android XR with Unity and the [Android XR Interaction Framework](https://developer.android.com/xr/axrif). And, based on your feedback, we are introducing the [Android XR Engine Hub](https://developer.android.com/xr/engine-hub) to allow you to run your experiences directly from your preferred engine,

- [Read the blog post about what's new for Android XR and game engines](https://android-developers.googleblog.com/2026/05/android-xr-updates-unity-unreal-godot.html)

### Apply for the [Android XR Developer Catalyst Program](http://g.co/dev/catalyst)

Don't miss your chance to build for the latest Android XR hardware. Apply today for the opportunity to gain access to pre-release hardware, including our audio and display glasses prototype and XREAL's Project Aura.

[Learn more and apply today](http://g.co/dev/catalyst)

We look forward to seeing the amazing XR experiences you build as we move toward the launch of more Android XR devices later this year!

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Android XR](https://developer.android.com/blog/topics/android-xr)
- [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
- [#Developer Preview](https://developer.android.com/blog/topics/developer-preview)
- [#Unity](https://developer.android.com/blog/topics/unity)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
Written by:

-

  ## [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/amy-zeppenfeld) ![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp) ![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)
-

  ## [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/stevan-silva) ![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp) ![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)
Continue reading
- [![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1R62M0.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.
  [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) • 3 min read
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
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) • 2 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)