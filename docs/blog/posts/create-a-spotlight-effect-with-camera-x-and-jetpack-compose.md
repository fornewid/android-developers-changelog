---
title: https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose
url: https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Create a spotlight effect with CameraX and Jetpack Compose

###### 8-min read

![](https://developer.android.com/static/blog/assets/camera_X_Jetpack_09bc5a0414_Z1DttIl.webp) 23 Jan 2025 [![](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)](https://developer.android.com/blog/authors/jolanda-verhoef) [##### Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef)

###### Developer Relations Engineer

Hey there! Welcome back to our series on CameraX and Jetpack Compose. In the previous posts, we've covered the fundamentals of setting up a camera preview and added tap-to-focus functionality.

**🧱** [**Part 1**](https://medium.com/androiddevelopers/getting-started-with-camerax-in-jetpack-compose-781c722ca0c4)**:** Building a basic camera preview using the new camera-compose artifact. We covered permission handling and basic integration.

**👆** [**Part 2**](https://medium.com/androiddevelopers/tap-to-focus-mastering-camerax-transformations-in-jetpack-compose-440853280a6e)**:** Using the Compose gesture system, graphics, and coroutines to implement a visual tap-to-focus.

**🔦 Part 3 (this post):** Exploring how to overlay Compose UI elements on top of your camera preview for a richer user experience.

**📂** [**Part 4**](https://medium.com/androiddevelopers/adaptive-camera-smooth-tabletop-mode-with-animations-f57d77696e0f): Using adaptive APIs and the Compose animation framework to smoothly animate to and from tabletop mode on foldable phones.

In this post, we'll dive into something a bit more visually engaging --- implementing a spotlight effect on top of our camera preview, using face detection as the basis for the effect. Why, you say? I'm not sure. But it sure looks cool 🙂. And, more importantly, it demonstrates how we can easily translate sensor coordinates into UI coordinates, allowing us to use them in Compose!
![face-detection.gif](https://developer.android.com/static/blog/assets/face_detection_f698c55a29_tsgeq.webp)

## **Enable face detection**

First, let's modify the CameraPreviewViewModel to enable face detection. We'll use the [`Camera2Interop`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2Interop) API, which allows us to interact with the underlying Camera2 API from CameraX. This gives us the opportunity to use camera features that are not exposed by CameraX directly. We need to make the following changes:

- Create a StateFlow that contains the face bounds as a list of [`Rect`](https://developer.android.com/reference/kotlin/androidx/compose/ui/geometry/Rect)s.
- Set the [`STATISTICS_FACE_DETECT_MODE`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#STATISTICS_FACE_DETECT_MODE) capture request option to FULL, which enables face detection.
- Set a [`CaptureCallback`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession.CaptureCallback) to get the face information from the capture result.

```kotlin
class CameraPreviewViewModel : ViewModel() {
    ...
    private val _sensorFaceRects = MutableStateFlow(listOf<Rect>())
    val sensorFaceRects: StateFlow<List<Rect>> = _sensorFaceRects.asStateFlow()

    private val cameraPreviewUseCase = Preview.Builder()
        .apply {
            Camera2Interop.Extender(this)
                .setCaptureRequestOption(
                    CaptureRequest.STATISTICS_FACE_DETECT_MODE,
                    CaptureRequest.STATISTICS_FACE_DETECT_MODE_FULL
                )
                .setSessionCaptureCallback(object : CameraCaptureSession.CaptureCallback() {
                    override fun onCaptureCompleted(
                        session: CameraCaptureSession,
                        request: CaptureRequest,
                        result: TotalCaptureResult
                    ) {
                        super.onCaptureCompleted(session, request, result)
                        result.get(CaptureResult.STATISTICS_FACES)
                            ?.map { face -> face.bounds.toComposeRect() }
                            ?.toList()
                            ?.let { faces -> _sensorFaceRects.update { faces } }
                    }
                })
        }
        .build().apply {
    ...
}
```

With these changes in place, our view model now emits a list of [`Rect`](https://developer.android.com/reference/kotlin/androidx/compose/ui/geometry/Rect) objects representing the bounding boxes of detected faces in sensor coordinates.

## **Translate sensor coordinates to UI coordinates**

The bounding boxes of detected faces that we stored in the last section use coordinates in the **sensor coordinate system**. To draw the bounding boxes in our UI, we need to transform these coordinates so that they are correct in the Compose coordinate system. We need to:

- Transform the **sensor coordinates** into **preview buffer coordinates**
- Transform the **preview buffer coordinates** into **Compose UI coordinates**

These transformations are done using transformation matrices. Each of the transformations has its own matrix:

- Our `SurfaceRequest` holds on to a [`TransformationInfo`](https://developer.android.com/reference/androidx/camera/core/SurfaceRequest.TransformationInfo) instance, which contains a [`sensorToBufferTranform`](https://developer.android.com/reference/androidx/camera/core/SurfaceRequest.TransformationInfo#getSensorToBufferTransform()) matrix.
- Our [`CameraXViewfinder`](https://developer.android.com/reference/kotlin/androidx/camera/compose/package-summary#CameraXViewfinder(androidx.camera.core.SurfaceRequest,androidx.compose.ui.Modifier,androidx.camera.viewfinder.core.ImplementationMode,androidx.camera.viewfinder.compose.MutableCoordinateTransformer)) has an associated [`CoordinateTransformer`](https://developer.android.com/reference/kotlin/androidx/camera/viewfinder/compose/CoordinateTransformer). You might remember that we already used this transformer in the previous blog post to transform tap-to-focus coordinates.

We can create a helper method that can do the transformation for us:

```kotlin
private fun List<Rect>.transformToUiCoords(
    transformationInfo: SurfaceRequest.TransformationInfo?,
    uiToBufferCoordinateTransformer: MutableCoordinateTransformer
): List<Rect> = this.map { sensorRect ->
    val bufferToUiTransformMatrix = Matrix().apply {
        setFrom(uiToBufferCoordinateTransformer.transformMatrix)
        invert()
    }

    val sensorToBufferTransformMatrix = Matrix().apply {
        transformationInfo?.let {
            setFrom(it.sensorToBufferTransform)
        }
    }

    val bufferRect = sensorToBufferTransformMatrix.map(sensorRect)
    val uiRect = bufferToUiTransformMatrix.map(bufferRect)

    uiRect
}
```

- We iterate through the list of detected faces, and for each face execute the transformation.
- The `CoordinateTransformer.transformMatrix` that we get from our `CameraXViewfinder` transforms coordinates from UI to buffer coordinates by default. In our case, we want the matrix to work the other way around, transforming buffer coordinates into UI coordinates. Therefore, we use the `invert()` method to invert the matrix.
- We first transform the face from sensor coordinates to buffer coordinates using the `sensorToBufferTransformMatrix`, and then transform those buffer coordinates to UI coordinates using the `bufferToUiTransformMatrix`.

## **Implement the spotlight effect**

Now, let's update the `CameraPreviewContent` composable to draw the spotlight effect. We'll use a [`Canvas`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/package-summary#Canvas(android.graphics.Canvas)) composable to draw a gradient mask over the preview, making the detected faces visible:

```kotlin
@Composable
fun CameraPreviewContent(
    viewModel: CameraPreviewViewModel,
    modifier: Modifier = Modifier,
    lifecycleOwner: LifecycleOwner = LocalLifecycleOwner.current
) {
    val surfaceRequest by viewModel.surfaceRequest.collectAsStateWithLifecycle()
    val sensorFaceRects by viewModel.sensorFaceRects.collectAsStateWithLifecycle()
    val transformationInfo by
        produceState<SurfaceRequest.TransformationInfo?>(null, surfaceRequest) {
            try {
                surfaceRequest?.setTransformationInfoListener(Runnable::run) { transformationInfo ->
                    value = transformationInfo
                }
                awaitCancellation()
            } finally {
                surfaceRequest?.clearTransformationInfoListener()
            }
        }
    val shouldSpotlightFaces by remember {
        derivedStateOf { sensorFaceRects.isNotEmpty() && transformationInfo != null} 
    }
    val spotlightColor = Color(0xDDE60991)
    ..

    surfaceRequest?.let { request ->
        val coordinateTransformer = remember { MutableCoordinateTransformer() }
        CameraXViewfinder(
            surfaceRequest = request,
            coordinateTransformer = coordinateTransformer,
            modifier = ..
        )

        AnimatedVisibility(shouldSpotlightFaces, enter = fadeIn(), exit = fadeOut()) {
            Canvas(Modifier.fillMaxSize()) {
                val uiFaceRects = sensorFaceRects.transformToUiCoords(
                    transformationInfo = transformationInfo,
                    uiToBufferCoordinateTransformer = coordinateTransformer
                )

                // Fill the whole space with the color
                drawRect(spotlightColor)
                // Then extract each face and make it transparent

                uiFaceRects.forEach { faceRect ->
                    drawRect(
                        Brush.radialGradient(
                            0.4f to Color.Black, 1f to Color.Transparent,
                            center = faceRect.center,
                            radius = faceRect.minDimension * 2f,
                        ),
                        blendMode = BlendMode.DstOut
                    )
                }
            }
        }
    }
}
```

Here's how it works:

- We collect the list of faces from the view model.
- To make sure we're not recomposing the whole screen every time the list of detected faces changes, we use `derivedStateOf` to keep track of whether any faces are detected at all. This can then be used with `AnimatedVisibility` to animate the colored overlay in and out.
- The `surfaceRequest` contains the information we need to transform sensor coordinates to buffer coordinates in the `SurfaceRequest.TransformationInfo`. We use the `produceState` function to set up a listener in the surface request, and clear this listener when the composable leaves the composition tree.
- We use a `Canvas` to draw a translucent pink rectangle that covers the entire screen.
- We defer the reading of the `sensorFaceRects` variable until we're inside the `Canvas` draw block. Then we transform the coordinates into UI coordinates.
- We iterate over the detected faces, and for each face, we draw a radial gradient that will make the inside of the face rectangle transparent.
- We use `BlendMode.DstOut` to make sure that we are cutting out the gradient from the pink rectangle, creating the spotlight effect.

*Note: When you change the camera to *`*DEFAULT_FRONT_CAMERA*`* you will notice that the spotlight is mirrored! This is a known issue, tracked in the *[*Google Issue Tracker*](https://issuetracker.google.com/390643162)*.*

## **Result**

With this code, we have a fully functional spotlight effect that highlights detected faces. You can find the full code snippet [here](https://gist.github.com/JolandaVerhoef/74d4696b804736c698450bd34b5c9ff8#file-3_spotlight_effect-kt).

This effect is just the beginning --- by using the power of Compose, you can create a myriad of visually stunning camera experiences. Being able to transform sensor and buffer coordinates into Compose UI coordinates and back means we can utilize all Compose UI features and integrate them seamlessly with the underlying camera system. With animations, advanced UI graphics, simple UI state management, and full gesture control, your imagination is the limit!

In the final post of the series, we'll dive into how to use adaptive APIs and the Compose animation framework to seamlessly transition between different camera UIs on foldable devices. Stay tuned!

*** ** * ** ***

The code snippets in this blog have the following license:

`// Copyright 2024 Google LLC. SPDX-License-Identifier: Apache-2.0`

Many thanks to [Nick Butcher](https://medium.com/u/22c02a30ae04?source=post_page---user_mention--8a7fa5b76641---), [Alex Vanyo](https://medium.com/u/e4ae3ec302ba?source=post_page---user_mention--8a7fa5b76641---), [Trevor McGuire](https://medium.com/u/6d8983119154?source=post_page---user_mention--8a7fa5b76641---), [Don Turner](https://medium.com/u/7f5a2cb6598e?source=post_page---user_mention--8a7fa5b76641---) and Lauren Ward for reviewing and providing feedback. Made possible by the hard work of [Yasith Vidanaarachch](https://medium.com/u/dadfb5fc55f9?source=post_page---user_mention--8a7fa5b76641---).

- [#Android](https://developer.android.com/blog/topics/android)
- [#Compose](https://developer.android.com/blog/topics/compose)
- [#Mobile App Development](https://developer.android.com/blog/topics/mobile-app-development)

###### Written by:

-

  ## [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jolanda-verhoef) ![](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp) ![](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)](https://developer.android.com/blog/authors/jose-alcerreca) 22 Apr 2022 22 Apr 2022 ![](https://developer.android.com/static/blog/assets/alternativesto_Idiling_13a59b7d0b_Z1sfmFQ.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Alternatives to Idling Resources in Compose tests: the waitUntil APIs (updated)](https://developer.android.com/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated)

  [arrow_forward](https://developer.android.com/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated) In this article you'll learn how to use the waitUntil test API in Compose to wait for certain conditions to be met.

  ###### [Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca) •
  3 min read

  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#Idling Resources](https://developer.android.com/blog/topics/idling-resources)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/jean-pierre-pralle) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/Streamline_user_animation_V02_Strapi_abd12985d7_SvAX9.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Streamline User Journeys with Verified Email via Credential Manager](https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager)

  [arrow_forward](https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager) Today, we're excited to announce a new verified email credential issued by Google, which developers can now retrieve directly from Android's Credential Manager Digital Credential API.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Jean-Pierre Pralle](https://developer.android.com/blog/authors/jean-pierre-pralle) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Android CLI and skills: Build Android apps 3x faster using any agent](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent) Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando), [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)