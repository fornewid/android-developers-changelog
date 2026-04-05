---
title: Incorporate face tracking in your app with ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Incorporate face tracking in your app with ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

After the user [grants permission for face tracking](/training/permissions/requesting),
your app can retrieve face shape information through ARCore for Jetpack XR. Face
shape information can help your app display the user in the virtual world, for
example, for a virtual glasses try-on.

## Create an ARCore for Jetpack XR session

Obtain face information through a Jetpack XR Runtime [`Session`](/reference/kotlin/androidx/xr/runtime/Session),
which your [app can create](/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Face tracking is not enabled by default on XR sessions. To enable face tracking,
configure the session and set the
[`FaceTrackingMode.USER`](/reference/kotlin/androidx/xr/runtime/FaceTrackingMode#USER()) mode:

```
val newConfig = session.config.copy(
    faceTracking = FaceTrackingMode.BLEND_SHAPES,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}

FaceTracking.kt
```

**Note:** Enabling this mode requires the `android.permission.FACE_TRACKING`
[runtime permission](/training/permissions/requesting) to be granted to your app.

## Retrieve face data

Use [`Face.getUserFace(session)`](/reference/kotlin/androidx/xr/arcore/Face#getUserFace(androidx.xr.runtime.Session)) to retrieve user face data, which
contains the following:

* **Face blendshape values**: A face's possible expressions are a combination
  of [68 blend shape values](/reference/kotlin/androidx/xr/arcore/FaceBlendShapeType). Each blend shape value
  represents a facial movement or deformation of the face, and the value
  indicates its intensity, ranging from `0.0` to `1.0`. For an explanation of
  each blend shape type, see
  [Understand face blendshape types](#blendshape-table).
* **Confidence values for regions**: The face has
  [three regions](/reference/kotlin/androidx/xr/arcore/FaceConfidenceRegion). Confidence values indicate the degree
  of certainty of accuracy for the given poses, ranging from `0.0` to `1.0`,
  where `1.0` indicates the highest confidence.

```
val face = Face.getUserFace(session) ?: return
face.state.collect { state ->
    if (state.trackingState != TrackingState.TRACKING) return@collect

    val confidence = state.getConfidence(FaceConfidenceRegion.FACE_CONFIDENCE_REGION_LOWER)
    val blendShapeValue = state.blendShapes[FaceBlendShapeType.FACE_BLEND_SHAPE_TYPE_LIPS_TOWARD]
}

FaceTracking.kt
```

## Understand face blendshape types

The following tables list each [type of face blend shape](/reference/kotlin/androidx/xr/arcore/FaceBlendShapeType):

### Upper region blendshapes

| Name | Reference Images | |
| `BROW_LOWERER_L` | Neutral face reference image   `BROW_LOWERER_L = 0.0` | face tracking reference image   `BROW_LOWERER_L = 1.0` |
| `BROW_LOWERER_R` | Neutral face reference image   `BROW_LOWERER_R = 0.0` | face tracking reference image   `BROW_LOWERER_R = 1.0` |
| `EYES_CLOSED_L` | Neutral face reference image   `EYES_CLOSED_L = 0.0` | face tracking reference image   `EYES_CLOSED_L = 1.0` |
| `EYES_CLOSED_R` | Neutral face reference image   `EYES_CLOSED_R = 0.0` | face tracking reference image   `EYES_CLOSED_R = 1.0` |
| `EYES_LOOK_DOWN_L` | Neutral face reference image   `EYES_LOOK_DOWN_L = 0.0` | face tracking reference image   `EYES_LOOK_DOWN_L = 1.0` |
| `EYES_LOOK_DOWN_R` | Neutral face reference image   `EYES_LOOK_DOWN_R = 0.0` | face tracking reference image   `EYES_LOOK_DOWN_R = 1.0` |
| `EYES_LOOK_LEFT_L` | Neutral face reference image   `EYES_LOOK_LEFT_L = 0.0` | face tracking reference image   `EYES_LOOK_LEFT_L = 1.0` |
| `EYES_LOOK_LEFT_R` | Neutral face reference image   `EYES_LOOK_LEFT_R = 0.0` | face tracking reference image   `EYES_LOOK_LEFT_R = 1.0` |
| `EYES_LOOK_RIGHT_L` | Neutral face reference image   `EYES_LOOK_RIGHT_L = 0.0` | face tracking reference image   `EYES_LOOK_RIGHT_L = 1.0` |
| `EYES_LOOK_RIGHT_R` | Neutral face reference image   `EYES_LOOK_RIGHT_R = 0.0` | face tracking reference image   `EYES_LOOK_RIGHT_R = 1.0` |
| `EYES_LOOK_UP_L` | Neutral face reference image   `EYES_LOOK_UP_L = 0.0` | face tracking reference image   `EYES_LOOK_UP_L = 1.0` |
| `EYES_LOOK_UP_R` | Neutral face reference image   `EYES_LOOK_UP_R = 0.0` | face tracking reference image   `EYES_LOOK_UP_R = 1.0` |
| `INNER_BROW_RAISER_L` | Neutral face reference image   `INNER_BROW_RAISER_L = 0.0` | face tracking reference image   `INNER_BROW_RAISER_L = 1.0` |
| `INNER_BROW_RAISER_R` | Neutral face reference image   `INNER_BROW_RAISER_R = 0.0` | face tracking reference image   `INNER_BROW_RAISER_R = 1.0` |
| `LID_TIGHTENER_L` | Neutral face reference image   `LID_TIGHTENER_L = 0.0` | face tracking reference image   `LID_TIGHTENER_L = 1.0` |
| `LID_TIGHTENER_R` | Neutral face reference image   `LID_TIGHTENER_R = 0.0` | face tracking reference image   `LID_TIGHTENER_R = 1.0` |
| `OUTER_BROW_RAISER_L` | Neutral face reference image   `OUTER_BROW_RAISER_L = 0.0` | face tracking reference image   `OUTER_BROW_RAISER_L = 1.0` |
| `OUTER_BROW_RAISER_R` | Neutral face reference image   `OUTER_BROW_RAISER_R = 0.0` | face tracking reference image   `OUTER_BROW_RAISER_R = 1.0` |
| `UPPER_LID_RAISER_L` | Neutral face reference image   `UPPER_LID_RAISER_L = 0.0` | face tracking reference image   `UPPER_LID_RAISER_L = 1.0` |
| `UPPER_LID_RAISER_R` | Neutral face reference image   `UPPER_LID_RAISER_R = 0.0` | face tracking reference image   `UPPER_LID_RAISER_R = 1.0` |

### Lower region blendshapes

| Name | Reference Images | |
| `CHEEK_PUFF_L` | Neutral face reference image   `CHEEK_PUFF_L = 0.0` | face tracking reference image   `CHEEK_PUFF_L = 1.0` |
| `CHEEK_PUFF_R` | Neutral face reference image   `CHEEK_PUFF_R = 0.0` | face tracking reference image   `CHEEK_PUFF_R = 1.0` |
| `CHEEK_RAISER_L` | Neutral face reference image   `CHEEK_RAISER_L = 0.0` | face tracking reference image   `CHEEK_RAISER_L = 1.0` |
| `CHEEK_RAISER_R` | Neutral face reference image   `CHEEK_RAISER_R = 0.0` | face tracking reference image   `CHEEK_RAISER_R = 1.0` |
| `CHEEK_SUCK_L` | Neutral face reference image   `CHEEK_SUCK_L = 0.0` | face tracking reference image   `CHEEK_SUCK_L = 1.0` |
| `CHEEK_SUCK_R` | Neutral face reference image   `CHEEK_SUCK_R = 0.0` | face tracking reference image   `CHEEK_SUCK_R = 1.0` |
| `CHIN_RAISER_B` | Neutral face reference image   `CHIN_RAISER_B = 0.0` | face tracking reference image   `CHIN_RAISER_B = 1.0` |
| `CHIN_RAISER_T` | Neutral face reference image   `CHIN_RAISER_T = 0.0` | face tracking reference image   `CHIN_RAISER_T = 1.0` |
| `DIMPLER_L` | Neutral face reference image   `DIMPLER_L = 0.0` | face tracking reference image   `DIMPLER_L = 1.0` |
| `DIMPLER_R` | Neutral face reference image   `DIMPLER_R = 0.0` | face tracking reference image   `DIMPLER_R = 1.0` |
| `JAW_DROP` | Neutral face reference image   `JAW_DROP = 0.0` | face tracking reference image   `JAW_DROP = 1.0` |
| `JAW_SIDEWAYS_LEFT` | Neutral face reference image   `JAW_SIDEWAYS_LEFT = 0.0` | face tracking reference image   `JAW_SIDEWAYS_LEFT = 1.0` |
| `JAW_SIDEWAYS_RIGHT` | Neutral face reference image   `JAW_SIDEWAYS_RIGHT = 0.0` | face tracking reference image   `JAW_SIDEWAYS_RIGHT = 1.0` |
| `JAW_THRUST` | Neutral face reference image   `JAW_THRUST = 0.0` | face tracking reference image   `JAW_THRUST = 1.0` |
| `LIP_CORNER_DEPRESSOR_L` | Neutral face reference image   `LIP_CORNER_DEPRESSOR_L = 0.0` | face tracking reference image   `LIP_CORNER_DEPRESSOR_L = 1.0` |
| `LIP_CORNER_DEPRESSOR_R` | Neutral face reference image   `LIP_CORNER_DEPRESSOR_R = 0.0` | face tracking reference image   `LIP_CORNER_DEPRESSOR_R = 1.0` |
| `LIP_CORNER_PULLER_L` | Neutral face reference image   `LIP_CORNER_PULLER_L = 0.0` | face tracking reference image   `LIP_CORNER_PULLER_L = 1.0` |
| `LIP_CORNER_PULLER_R` | Neutral face reference image   `LIP_CORNER_PULLER_R = 0.0` | face tracking reference image   `LIP_CORNER_PULLER_R = 1.0` |
| `LIP_FUNNELER_LB` | Neutral face reference image   `LIP_FUNNELER_LB = 0.0` | face tracking reference image   `LIP_FUNNELER_LB = 1.0` |
| `LIP_FUNNELER_LT` | Neutral face reference image   `LIP_FUNNELER_LT = 0.0` | face tracking reference image   `LIP_FUNNELER_LT = 1.0` |
| `LIP_FUNNELER_RB` | Neutral face reference image   `LIP_FUNNELER_RB = 0.0` | face tracking reference image   `LIP_FUNNELER_RB = 1.0` |
| `LIP_FUNNELER_RT` | Neutral face reference image   `LIP_FUNNELER_RT = 0.0` | face tracking reference image   `LIP_FUNNELER_RT = 1.0` |
| `LIP_PRESSOR_L` | Neutral face reference image   `LIP_PRESSOR_L = 0.0` | face tracking reference image   `LIP_PRESSOR_L = 1.0` |
| `LIP_PRESSOR_R` | Neutral face reference image   `LIP_PRESSOR_R = 0.0` | face tracking reference image   `LIP_PRESSOR_R = 1.0` |
| `LIP_PUCKER_L` | Neutral face reference image   `LIP_PUCKER_L = 0.0` | face tracking reference image   `LIP_PUCKER_L = 1.0` |
| `LIP_PUCKER_R` | Neutral face reference image   `LIP_PUCKER_R = 0.0` | face tracking reference image   `LIP_PUCKER_R = 1.0` |
| `LIP_STRETCHER_L` | Neutral face reference image   `LIP_STRETCHER_L = 0.0` | face tracking reference image   `LIP_STRETCHER_L = 1.0` |
| `LIP_STRETCHER_R` | Neutral face reference image   `LIP_STRETCHER_R = 0.0` | face tracking reference image   `LIP_STRETCHER_R = 1.0` |
| `LIP_SUCK_LB` | Neutral face reference image   `LIP_SUCK_LB = 0.0` | face tracking reference image   `LIP_SUCK_LB = 1.0` |
| `LIP_SUCK_LT` | Neutral face reference image   `LIP_SUCK_LT = 0.0` | face tracking reference image   `LIP_SUCK_LT = 1.0` |
| `LIP_SUCK_RB` | Neutral face reference image   `LIP_SUCK_RB = 0.0` | face tracking reference image   `LIP_SUCK_RB = 1.0` |
| `LIP_SUCK_RT` | Neutral face reference image   `LIP_SUCK_RT = 0.0` | face tracking reference image   `LIP_SUCK_RT = 1.0` |
| `LIP_TIGHTENER_L` | Neutral face reference image   `LIP_TIGHTENER_L = 0.0` | face tracking reference image   `LIP_TIGHTENER_L = 1.0` |
| `LIP_TIGHTENER_R` | Neutral face reference image   `LIP_TIGHTENER_R = 0.0` | face tracking reference image   `LIP_TIGHTENER_R = 1.0` |
| `LIPS_TOWARD` | Neutral face reference image   `LIPS_TOWARD = 0.0` | face tracking reference image   `JAW_DROP = 1.0 and LIPS_TOWARD = 1.0` |
| `LOWER_LIP_DEPRESSOR_L` | Neutral face reference image   `LOWER_LIP_DEPRESSOR_L = 0.0` | face tracking reference image   `LOWER_LIP_DEPRESSOR_L = 1.0` |
| `LOWER_LIP_DEPRESSOR_R` | Neutral face reference image   `LOWER_LIP_DEPRESSOR_R = 0.0` | face tracking reference image   `LOWER_LIP_DEPRESSOR_R = 1.0` |
| `MOUTH_LEFT` | Neutral face reference image   `MOUTH_LEFT = 0.0` | face tracking reference image   `MOUTH_LEFT = 1.0` |
| `MOUTH_RIGHT` | Neutral face reference image   `MOUTH_RIGHT = 0.0` | face tracking reference image   `MOUTH_RIGHT = 1.0` |
| `NOSE_WRINKLER_L` | Neutral face reference image   `NOSE_WRINKLER_L = 0.0` | face tracking reference image   `NOSE_WRINKLER_L = 1.0` |
| `NOSE_WRINKLER_R` | Neutral face reference image   `NOSE_WRINKLER_R = 0.0` | face tracking reference image   `NOSE_WRINKLER_R = 1.0` |
| `UPPER_LIP_RAISER_L` | Neutral face reference image   `UPPER_LIP_RAISER_L = 0.0` | face tracking reference image   `UPPER_LIP_RAISER_L = 1.0` |
| `UPPER_LIP_RAISER_R` | Neutral face reference image   `UPPER_LIP_RAISER_R = 0.0` | face tracking reference image   `UPPER_LIP_RAISER_R = 1.0` |
| `TONGUE_OUT` | Neutral face reference image   TONGUE\_OUT = 0.0 | face tracking reference image   TONGUE\_OUT = 1.0 |
| `TONGUE_LEFT` | Neutral face reference image   TONGUE\_LEFT = 0.0 | face tracking reference image   TONGUE\_LEFT = 1.0 |
| `TONGUE_RIGHT` | Neutral face reference image   TONGUE\_RIGHT = 0.0 | face tracking reference image   TONGUE\_RIGHT = 1.0 |
| `TONGUE_UP` | Neutral face reference image   TONGUE\_UP = 0.0 | face tracking reference image   TONGUE\_UP = 1.0 |
| `TONGUE_DOWN` | Neutral face reference image   TONGUE\_DOWN = 0.0 | face tracking reference image   TONGUE\_DOWN = 1.0 |