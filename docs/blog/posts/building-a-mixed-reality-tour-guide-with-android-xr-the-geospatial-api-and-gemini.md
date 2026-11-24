---
title: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
url: https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini

6 min read ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_5c55395a9c_2h4Keb.webp) 17 Jun 2026 3 Authors [Coco Fatus,](https://developer.android.com/blog/authors/coco-fatus.md.txt) [Alon Hetzroni,](https://developer.android.com/blog/authors/alon-hetzroni.md.txt) [Azin Mehrnoosh](https://developer.android.com/blog/authors/azin-mehrnoosh.md.txt) [At this year's Google I/O](https://www.youtube.com/watch?v=1KOO2lqsdaA), we announced an update for spatial experiences: the [Geospatial API](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.md.txt) is now available as a preview in [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore.md.txt). By bringing Google's Visual Positioning System (VPS) to Android XR, Android XR enables anchoring digital content to the physical world with sub-meter accuracy and precise orientation in supported areas.\* To explore what the Geospatial API could unlock, our team built a demo: the XR Geospatial Tour.

Imagine walking into a new city, putting on a pair of wired XR glasses (like the upcoming XREAL Project Aura), and instantly having a knowledgeable, local guide showing you around. You don't need to stare down at a 2D map---instead, 3D models gently guide your path, and an intelligent voice tells you about the historical landmarks right in front of you. We combined the [Geospatial APIs](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.md.txt), [Gemini API using Firebase AI Logic](https://firebase.google.com/docs/ai-logic), [Google Maps Grounding](https://ai.google.dev/gemini-api/docs/maps-grounding), and [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk.md.txt) to create a hands-free, immersive walking tour experience.
[Video](https://www.youtube.com/watch?v=HpQLXX19boI)

*Disclaimer: Video and Tour Guide application are for demonstration purposes only. Some sequences have been shortened. Any hardware depicted may be under development; final product details may differ.*

Let's walk through the implementation details and show how we tied these APIs together to build a world-scale spatial experience.

## 1. Pinpointing the User with ARCore Geospatial API (VPS)

Enhance your navigation experience on XR by combining the power of GPS with the precision of VPS. The accuracy and precise orientation that comes with VPS allows 3D waypoints to align with the physical world.

This is why the Geospatial API on Android XR can help you build custom experiences. By using advanced computer vision, VPS tries to provide a [GeospatialPose](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/GeospatialPose.md.txt) (including latitude, longitude, and heading) that is more accurate than GPS.

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

Using Jetpack XR SDK, we can place 3D models alongside the Compose UI using [SpatialBox](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialBox.composable.md.txt) and [SceneCoreEntity](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SceneCoreEntity.composable.md.txt). We also used [InteractableComponent](https://developer.android.com/reference/androidx/xr/scenecore/InteractableComponent.md.txt) to respond to user taps.

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

Building the XR Geospatial Tour app showed us that the barrier to entry for world-scale spatial experiences is lower than ever for Android developers. With the Geospatial API now available in preview on Android XR, your apps can seamlessly understand the physical world around them. By combining [Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose.md.txt)'s APIs with the high-precision location data of VPS and the generative capabilities of Gemini, we can create experiences that understand both where the user is and what they are looking at.

To help you get hands-on with Android XR, we are thrilled to open applications for the [Android XR Developer Catalyst Program](https://developer.android.com/develop/xr/catalyst), which includes XREAL Project Aura. Starting today, you can apply to get access to an XREAL Project Aura devkit or our display glasses devkit over the coming months!

\**Disclaimer: Available on select devices. Internet connection required. Works on compatible apps and surfaces. Results may vary.*
Written by:

-

  ## [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus.md.txt)

  ###### UX Designer

  [read_more
  View profile](https://developer.android.com/blog/authors/coco-fatus) ![View Coco Fatus's profile](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_O16qq.webp) ![View Coco Fatus's profile](https://developer.android.com/static/blog/assets/Coco_Fatus_78a5f60501_O16qq.webp)
-

  ## [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni.md.txt)

  ###### UX Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alon-hetzroni) ![View Alon Hetzroni's profile](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_ZuMMVo.webp) ![View Alon Hetzroni's profile](https://developer.android.com/static/blog/assets/ahetzroni_profile_3fbed6e24c_ZuMMVo.webp)
-

  ## [Azin Mehrnoosh](https://developer.android.com/blog/authors/azin-mehrnoosh.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/azin-mehrnoosh) ![View Azin Mehrnoosh's profile](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_ZKATrt.webp) ![View Azin Mehrnoosh's profile](https://developer.android.com/static/blog/assets/unnamed_6_5b79453d9b_ZKATrt.webp)
Continue reading
- [![View Matthew Forsythe's profile](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_1FlQLe.webp)](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) 19 Nov 2026 19 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_139_Android_developer_verification_Going_global_together_Strapi_01_png_12aa1e5aae_ZkNaef.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Expanding Android developer verification in 2027](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt) After over a year of joint preparation with industry leaders, regional partners, app distributors, and Android communities, our user protections successfully went live on September 30 for participating stores across Brazil, Indonesia, Singapore, and Thailand.
  [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
- [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating apps: New adaptive quality standards on Google Play](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) To give users the premium experience they expect and ensure your apps shine across every screen size, Google Play is introducing new adaptive app quality requirements that go into effect April 2027.
  [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) • 4 min read
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - +1 ↩
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)