---
title: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
url: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini

6 min read ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_5c55395a9c_UkzvN.webp) 17 Jun 2026 3 Authors [Coco Fatus,](https://developer.android.com/blog/authors/coco-fatus) [Alon Hetzroni,](https://developer.android.com/blog/authors/alon-hetzroni) [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1) [At this year's Google I/O](https://www.youtube.com/watch?v=1KOO2lqsdaA), we announced an update for spatial experiences: the [Geospatial API](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial) is now available as a preview in [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore). By bringing Google's Visual Positioning System (VPS) to Android XR, Android XR enables anchoring digital content to the physical world with sub-meter accuracy and precise orientation in supported areas.\* To explore what the Geospatial API could unlock, our team built a demo: the XR Geospatial Tour.

Imagine walking into a new city, putting on a pair of wired XR glasses (like the upcoming XREAL Project Aura), and instantly having a knowledgeable, local guide showing you around. You don't need to stare down at a 2D map---instead, 3D models gently guide your path, and an intelligent voice tells you about the historical landmarks right in front of you. We combined the [Geospatial APIs](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial), [Gemini API using Firebase AI Logic](https://firebase.google.com/docs/ai-logic), [Google Maps Grounding](https://ai.google.dev/gemini-api/docs/maps-grounding), and [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) to create a hands-free, immersive walking tour experience.
[Video](https://www.youtube.com/watch?v=HpQLXX19boI)

*Disclaimer: Video and Tour Guide application are for demonstration purposes only. Some sequences have been shortened. Any hardware depicted may be under development; final product details may differ.*

Let's walk through the implementation details and show how we tied these APIs together to build a world-scale spatial experience.

## 1. Pinpointing the User with ARCore Geospatial API (VPS)

Enhance your navigation experience on XR by combining the power of GPS with the precision of VPS. The accuracy and precise orientation that comes with VPS allows 3D waypoints to align with the physical world.

This is why the Geospatial API on Android XR can help you build custom experiences. By using advanced computer vision, VPS tries to provide a [GeospatialPose](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/GeospatialPose) (including latitude, longitude, and heading) that is more accurate than GPS.

Here's how we retrieve the user's Geospatial pose by mapping the device's orientation to a Geospatial coordinate:

```kotlin
// Retrieve the current geospatial pose from the ARCore session
val result = geospatial.createGeospatialPoseFromPose(arDevice.state.value.devicePose)
if (result is CreateGeospatialPoseFromPoseSuccess) {
    val pose = result.pose
    Log.d("VPS", "Accurate Location: ${pose.latitude}, ${pose.longitude}")
}
```

Because the entire experience relies on this accuracy, we monitor the `horizontalAccuracy` and `orientationYawAccuracy` until they meet our thresholds. If the user is indoors or in an unrecognized area, we prompt them to "walk to an outdoor public space and look around".

## 2. Crafting the Itinerary with Gemini API \& Google Maps Grounding

Once we have a location, we use the [Gemini API using Firebase AI Logic](https://firebase.google.com/docs/ai-logic) to prompt the Gemini model to act as a local tour guide. We pass the user's coordinates to the model and ask it to output a structured JSON response containing nearby walking tours:

```kotlin
   val configForTools = ToolConfig(
      functionCallingConfig = null,
      retrievalConfig = retrievalConfig {
        latLng = FirebaseLatLng(pose.latitude, pose.longitude)
        languageCode = "en"
      }
    )

    val responseJsonSchema = Schema.obj(
      mapOf(
        "locationIntro" to Schema.string(),
        "tours" to Schema.array(
          Schema.obj(
            mapOf(
              "title" to Schema.string(),
              "description" to Schema.string(),
              "stops" to Schema.array(
                Schema.obj(
                  mapOf(
                    "name" to Schema.string(),
                    "detailedName" to Schema.string(),
                    "description" to Schema.string()
                  )
                )
              )
            )
          )
        )
      )
    )

    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
      modelName = "gemini-3.5-flash",
      tools = listOf(Tool.googleMaps()),
      generationConfig = generationConfig {
        responseMimeType = "application/json"
        responseSchema = responseJsonSchema
      }
    )

   val result = model.generateContent("The user is at latitude ${pose.latitude} and longitude ${pose.longitude}. Generate exactly 3 diverse tours near this location (e.g., historical, food, nature). All tour ideas should be walking distance only.")
```

Large Language Models are great at generating rich descriptions, but they can sometimes hallucinate exact latitude/longitude coordinates. To solve this, we used [Google Maps Grounding](https://ai.google.dev/gemini-api/docs/maps-grounding) to ground the AI.

## 3. A Voice to Guide You: Gemini 2.5 TTS

To make the tour guide feel truly present, we implemented dynamic voiceovers.

Using the `gemini-2.5-flash-tts model`, we can configure our model generation config to natively return audio data instead of just text! Here's how you can request the `ResponseModality.AUDIO`:

```kotlin
val ttsModel = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-2.5-flash-tts",
        generationConfig = generationConfig {
            // Instruct the model to return Audio
            responseModalities = listOf(ResponseModality.AUDIO)
        }
    )

val response = ttsModel.generateContent("Say in a neutral but positive voice:\n$prompt")

// Extract the raw audio bytes from the response
val audioBytes = response.candidates.firstOrNull()?.content?.parts
    ?.filterIsInstance<InlineDataPart>()
    ?.firstOrNull { it.mimeType.contains("audio") }?.inlineData
```

## 4. Bringing it to Life in 3D with Jetpack XR

The final piece of the puzzle is rendering this data in the user's field of view. The Jetpack XR SDK makes it intuitive to transition from a 2D Android UI to spatial computing.

We used Jetpack Compose for XR to build spatial components. To represent points of interest along the tour, we built a Composable called InfoSphere, which contains a GltfModel of a 3D orb that floats in space and can be interacted with to reveal information.

Using Jetpack XR SDK, we can place 3D models alongside the Compose UI using [SpatialBox](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialBox.composable) and [SceneCoreEntity](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SceneCoreEntity.composable). We also used [InteractableComponent](https://developer.android.com/reference/androidx/xr/scenecore/InteractableComponent) to respond to user taps.

By combining [AnimatedSpatialVisibility](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/AnimatedSpatialVisibility.composable) for traditional Compose UI surfaces with SceneCoreEntity 3D elements, we're able to seamlessly blend data into the physical world.

```kotlin
@Composable
fun InfoSphere(
    content: InfoBubbleContent,
    session: Session,
    sphereModel: GltfModel,
    isSelected: Boolean,
    onClick: () -> Unit
) {
    // SpatialBox lets us arrange 3D components and SpatialPanels together
    SpatialBox(
        SubspaceModifier
            .offset(x = 2.dp, y = 1.dp, z = (-3).dp) // Positioned in 3D space
    ) {
        // Smoothly animate the visibility of our 2D Compose UI Panel
        AnimatedSpatialVisibility(visible = isSelected) {
            SpatialPanel {
                InfoBubble(content) // Regular 2D Compose UI
            }
        }
        // Render our interactive 3D sphere
        SceneCoreEntity(
            factory = {
                GltfModelEntity.create(session, sphereModel).also { entity ->
                    // Make the 3D model respond to user taps
                    entity.addComponent(InteractableComponent.create(session) { inputEvent ->
                        if (inputEvent.action == InputEvent.Action.UP) {
                            onClick()
                        }
                    })
                }
            }
        )
    }
}
```

## Explore what's possible with Android XR today

Building the XR Geospatial Tour app showed us that the barrier to entry for world-scale spatial experiences is lower than ever for Android developers. With the Geospatial API now available in preview on Android XR, your apps can seamlessly understand the physical world around them. By combining [Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose)'s APIs with the high-precision location data of VPS and the generative capabilities of Gemini, we can create experiences that understand both where the user is and what they are looking at.

To help you get hands-on with Android XR, we are thrilled to open applications for the [Android XR Developer Catalyst Program](https://developer.android.com/develop/xr/catalyst), which includes XREAL Project Aura. Starting today, you can apply to get access to an XREAL Project Aura devkit or our display glasses devkit over the coming months!

\**Disclaimer: Available on select devices. Internet connection required. Works on compatible apps and surfaces. Results may vary.*
Written by:

-

  ## [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus)

  ###### UX Designer

  [read_more
  View profile](https://developer.android.com/blog/authors/coco-fatus) ![View Coco Fatus's profile](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_1PQrHm.webp) ![View Coco Fatus's profile](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_1PQrHm.webp)
-

  ## [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni)

  ###### UX Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alon-hetzroni) ![View Alon Hetzroni's profile](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_1Th2rE.webp) ![View Alon Hetzroni's profile](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_1Th2rE.webp)
-

  ## [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/blog-author-1) ![View Azin Mehrnoosh's profile](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_Z2cXYIR.webp) ![View Azin Mehrnoosh's profile](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_Z2cXYIR.webp)
Continue reading
- [![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)](https://developer.android.com/blog/authors/blair-harmon) 19 Aug 2026 19 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_116_Preparing_your_app_for_expanded_memory_limits_strapi_0aac62fa12_1hkk5a.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Preparing your app for broader memory limits](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits)

  [arrow_forward](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits) A great user experience is central to Android's mission, and delivering on that promise requires keeping devices fast, responsive, and reliable.
  [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon) • 2 min read
  - [#App Memory Limits](https://developer.android.com/blog/topics/app-memory-limits)
  - [#Android Vitals](https://developer.android.com/blog/topics/android-vitals)
  - [#Multi-Process Architecture](https://developer.android.com/blog/topics/multi-process-architecture)
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +3 ↩
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_Z1YdYO1.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Jetpack XR SDK core libraries reach beta: The next milestone for Android XR](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr) Since introducing the Android XR SDK, developers have transformed their ideas into innovative immersive experiences across headsets and wired XR glasses.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld), [Greg Underwood](https://developer.android.com/blog/authors/greg-underwood), [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen) • 2 min read
  - [#Jetpack XR SDK](https://developer.android.com/blog/topics/jetpack-xr-sdk)
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)