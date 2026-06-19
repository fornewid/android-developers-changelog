---
title: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
url: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
source: md.txt
---

# Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini

###### 7-min read

![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_acccdca10d_Z1skkVv.webp) 18 Jun 2026 3 Authors

##### [Coco Fatus,](https://developer.android.com/blog/authors/coco-fatus)
[Alon Hetzroni,](https://developer.android.com/blog/authors/alon-hetzroni)
[Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1)

[At this year's Google I/O](https://www.youtube.com/watch?v=1KOO2lqsdaA), we announced an update for spatial experiences: the [Geospatial API](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial) is now available as a preview in [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore). By bringing Google's Visual Positioning System (VPS) to Android XR, Android XR enables anchoring digital content to the physical world with sub-meter accuracy and precise orientation in supported areas.\* To explore what the Geospatial API could unlock, our team built a demo: the XR Geospatial Tour.

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

###### Written by:

-

  ## [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus)

  ###### UX Designer

  [read_more
  View profile](https://developer.android.com/blog/authors/coco-fatus) ![](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_1PQrHm.webp) ![](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_1PQrHm.webp)
-

  ## [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni)

  ###### UX Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alon-hetzroni) ![](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_1Th2rE.webp) ![](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_1Th2rE.webp)
-

  ## [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/blog-author-1) ![](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_Z2cXYIR.webp) ![](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_Z2cXYIR.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 16 Jun 2026 16 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_Hero_White_e4dbee04d8_Z1qQbv3.webp)

  ## [Android 17 is Here](https://developer.android.com/blog/posts/android-17-is-here)

  [arrow_forward](https://developer.android.com/blog/posts/android-17-is-here) Today we're releasing Android 17 and making it available on most supported Pixel devices. Look for new devices running Android 17 in the coming months.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  13 min read

  - [#Android 17](https://developer.android.com/blog/topics/android-17)
- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 18 Jun 2026 18 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together) Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_D_Android_XR_Strapi_39d27725e6_Zhwmdd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  ###### [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) •
  3 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)