---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

After the user [grants permission for face tracking](https://developer.android.com/training/permissions/requesting),
your app can retrieve face shape information through ARCore for Jetpack XR. Face
shape information can help your app display the user in the virtual world, for
example, for a virtual glasses try-on.

## Create an ARCore for Jetpack XR session

Obtain face information through a Jetpack XR Runtime [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session),
which your [app can create](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Face tracking is not enabled by default on XR sessions. To enable face tracking,
configure the session and set the
[`FaceTrackingMode.USER`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.FaceTrackingMode#USER()) mode:


```kotlin
val newConfig = session.config.copy(
    faceTracking = Config.FaceTrackingMode.USER,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}
```

<br />

> [!NOTE]
> **Note:** Enabling this mode requires the `android.permission.FACE_TRACKING` [runtime permission](https://developer.android.com/training/permissions/requesting) to be granted to your app.

## Retrieve face data

Use [`Face.getUserFace(session)`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Face#getUserFace(androidx.xr.runtime.Session)) to retrieve user face data, which
contains the following:

- **Face blendshape values** : A face's possible expressions are a combination of [68 blend shape values](https://developer.android.com/reference/kotlin/androidx/xr/arcore/FaceBlendShapeType). Each blend shape value represents a facial movement or deformation of the face, and the value indicates its intensity, ranging from `0.0` to `1.0`. For an explanation of each blend shape type, see [Understand face blendshape types](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face#blendshape-table).
- **Confidence values for regions** : The face has [three regions](https://developer.android.com/reference/kotlin/androidx/xr/arcore/FaceConfidenceRegion). Confidence values indicate the degree of certainty of accuracy for the given poses, ranging from `0.0` to `1.0`, where `1.0` indicates the highest confidence.


```kotlin
val face = Face.getUserFace(session) ?: return
face.state.collect { state ->
    if (state.trackingState != TrackingState.TRACKING) return@collect

    val confidence = state.getConfidence(FaceConfidenceRegion.FACE_CONFIDENCE_REGION_LOWER)
    val blendShapeValue = state.blendShapes[FaceBlendShapeType.FACE_BLEND_SHAPE_TYPE_LIPS_TOWARD]
}
```

<br />

## Understand face blendshape types

The following tables list each [type of face blend shape](https://developer.android.com/reference/kotlin/androidx/xr/arcore/FaceBlendShapeType):

### Upper region blendshapes

| Name | Reference Images ||
|---|---|---|
| `BROW_LOWERER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `BROW_LOWERER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/browLowererL_front.png) `BROW_LOWERER_L = 1.0` |
| `BROW_LOWERER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `BROW_LOWERER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/browLowererR_front.png) `BROW_LOWERER_R = 1.0` |
| `EYES_CLOSED_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_CLOSED_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesClosedL_front.png) `EYES_CLOSED_L = 1.0` |
| `EYES_CLOSED_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_CLOSED_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesClosedR_front.png) `EYES_CLOSED_R = 1.0` |
| `EYES_LOOK_DOWN_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_DOWN_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookDownL_front.png) `EYES_LOOK_DOWN_L = 1.0` |
| `EYES_LOOK_DOWN_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_DOWN_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookDownR_front.png) `EYES_LOOK_DOWN_R = 1.0` |
| `EYES_LOOK_LEFT_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_LEFT_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookLeftL_front.png) `EYES_LOOK_LEFT_L = 1.0` |
| `EYES_LOOK_LEFT_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_LEFT_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookLeftR_front.png) `EYES_LOOK_LEFT_R = 1.0` |
| `EYES_LOOK_RIGHT_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_RIGHT_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookRightL_front.png) `EYES_LOOK_RIGHT_L = 1.0` |
| `EYES_LOOK_RIGHT_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_RIGHT_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookRightR_front.png) `EYES_LOOK_RIGHT_R = 1.0` |
| `EYES_LOOK_UP_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_UP_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookUpL_front.png) `EYES_LOOK_UP_L = 1.0` |
| `EYES_LOOK_UP_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `EYES_LOOK_UP_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/eyesLookUpR_front.png) `EYES_LOOK_UP_R = 1.0` |
| `INNER_BROW_RAISER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `INNER_BROW_RAISER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/innerBrowRaiserL_front.png) `INNER_BROW_RAISER_L = 1.0` |
| `INNER_BROW_RAISER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `INNER_BROW_RAISER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/innerBrowRaiserR_front.png) `INNER_BROW_RAISER_R = 1.0` |
| `LID_TIGHTENER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LID_TIGHTENER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lidTightenerL_front.png) `LID_TIGHTENER_L = 1.0` |
| `LID_TIGHTENER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LID_TIGHTENER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lidTightenerR_front.png) `LID_TIGHTENER_R = 1.0` |
| `OUTER_BROW_RAISER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `OUTER_BROW_RAISER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/outerBrowRaiserL_front.png) `OUTER_BROW_RAISER_L = 1.0` |
| `OUTER_BROW_RAISER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `OUTER_BROW_RAISER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/outerBrowRaiserR_front.png) `OUTER_BROW_RAISER_R = 1.0` |
| `UPPER_LID_RAISER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `UPPER_LID_RAISER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/upperLidRaiserL_front.png) `UPPER_LID_RAISER_L = 1.0` |
| `UPPER_LID_RAISER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `UPPER_LID_RAISER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/upperLidRaiserR_front.png) `UPPER_LID_RAISER_R = 1.0` |

### Lower region blendshapes

| Name | Reference Images ||
|---|---|---|
| `CHEEK_PUFF_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_PUFF_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekPuffL_front.png) `CHEEK_PUFF_L = 1.0` |
| `CHEEK_PUFF_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_PUFF_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekPuffR_front.png) `CHEEK_PUFF_R = 1.0` |
| `CHEEK_RAISER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_RAISER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekRaiserL_front.png) `CHEEK_RAISER_L = 1.0` |
| `CHEEK_RAISER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_RAISER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekRaiserR_front.png) `CHEEK_RAISER_R = 1.0` |
| `CHEEK_SUCK_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_SUCK_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekSuckL_front.png) `CHEEK_SUCK_L = 1.0` |
| `CHEEK_SUCK_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHEEK_SUCK_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/cheekSuckR_front.png) `CHEEK_SUCK_R = 1.0` |
| `CHIN_RAISER_B` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHIN_RAISER_B = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/chinRaiserB_front.png) `CHIN_RAISER_B = 1.0` |
| `CHIN_RAISER_T` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `CHIN_RAISER_T = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/chinRaiserT_front.png) `CHIN_RAISER_T = 1.0` |
| `DIMPLER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `DIMPLER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/dimplerL_front.png) `DIMPLER_L = 1.0` |
| `DIMPLER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `DIMPLER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/dimplerR_front.png) `DIMPLER_R = 1.0` |
| `JAW_DROP` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `JAW_DROP = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/jawDrop_front.png) `JAW_DROP = 1.0` |
| `JAW_SIDEWAYS_LEFT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `JAW_SIDEWAYS_LEFT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/jawSidewaysLeft_front.png) `JAW_SIDEWAYS_LEFT = 1.0` |
| `JAW_SIDEWAYS_RIGHT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `JAW_SIDEWAYS_RIGHT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/jawSidewaysRight_front.png) `JAW_SIDEWAYS_RIGHT = 1.0` |
| `JAW_THRUST` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_threeQuarters.png) `JAW_THRUST = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/jawThrust_threeQuarters.png) `JAW_THRUST = 1.0` |
| `LIP_CORNER_DEPRESSOR_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_CORNER_DEPRESSOR_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipCornerDepressorL_front.png) `LIP_CORNER_DEPRESSOR_L = 1.0` |
| `LIP_CORNER_DEPRESSOR_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_CORNER_DEPRESSOR_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipCornerDepressorR_front.png) `LIP_CORNER_DEPRESSOR_R = 1.0` |
| `LIP_CORNER_PULLER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_CORNER_PULLER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipCornerPullerL_front.png) `LIP_CORNER_PULLER_L = 1.0` |
| `LIP_CORNER_PULLER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_CORNER_PULLER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipCornerPullerR_front.png) `LIP_CORNER_PULLER_R = 1.0` |
| `LIP_FUNNELER_LB` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_FUNNELER_LB = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipFunnelerLB_front.png) `LIP_FUNNELER_LB = 1.0` |
| `LIP_FUNNELER_LT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_FUNNELER_LT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipFunnelerLT_front.png) `LIP_FUNNELER_LT = 1.0` |
| `LIP_FUNNELER_RB` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_FUNNELER_RB = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipFunnelerRB_front.png) `LIP_FUNNELER_RB = 1.0` |
| `LIP_FUNNELER_RT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_FUNNELER_RT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipFunnelerRT_front.png) `LIP_FUNNELER_RT = 1.0` |
| `LIP_PRESSOR_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_PRESSOR_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipPressorL_front.png) `LIP_PRESSOR_L = 1.0` |
| `LIP_PRESSOR_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_PRESSOR_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipPressorR_front.png) `LIP_PRESSOR_R = 1.0` |
| `LIP_PUCKER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_PUCKER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipPuckerL_front.png) `LIP_PUCKER_L = 1.0` |
| `LIP_PUCKER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_PUCKER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipPuckerR_front.png) `LIP_PUCKER_R = 1.0` |
| `LIP_STRETCHER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_STRETCHER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipStretcherL_front.png) `LIP_STRETCHER_L = 1.0` |
| `LIP_STRETCHER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_STRETCHER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipStretcherR_front.png) `LIP_STRETCHER_R = 1.0` |
| `LIP_SUCK_LB` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_SUCK_LB = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipSuckLB_front.png) `LIP_SUCK_LB = 1.0` |
| `LIP_SUCK_LT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_SUCK_LT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipSuckLT_front.png) `LIP_SUCK_LT = 1.0` |
| `LIP_SUCK_RB` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_SUCK_RB = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipSuckRB_front.png) `LIP_SUCK_RB = 1.0` |
| `LIP_SUCK_RT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_SUCK_RT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipSuckRT_front.png) `LIP_SUCK_RT = 1.0` |
| `LIP_TIGHTENER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_TIGHTENER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipTightenerL_front.png) `LIP_TIGHTENER_L = 1.0` |
| `LIP_TIGHTENER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIP_TIGHTENER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipTightenerR_front.png) `LIP_TIGHTENER_R = 1.0` |
| `LIPS_TOWARD` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LIPS_TOWARD = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lipsToward_front.png) `JAW_DROP = 1.0 and LIPS_TOWARD = 1.0` |
| `LOWER_LIP_DEPRESSOR_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LOWER_LIP_DEPRESSOR_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lowerLipDepressorL_front.png) `LOWER_LIP_DEPRESSOR_L = 1.0` |
| `LOWER_LIP_DEPRESSOR_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `LOWER_LIP_DEPRESSOR_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/lowerLipDepressorR_front.png) `LOWER_LIP_DEPRESSOR_R = 1.0` |
| `MOUTH_LEFT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `MOUTH_LEFT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/mouthLeft_front.png) `MOUTH_LEFT = 1.0` |
| `MOUTH_RIGHT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `MOUTH_RIGHT = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/mouthRight_front.png) `MOUTH_RIGHT = 1.0` |
| `NOSE_WRINKLER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `NOSE_WRINKLER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/noseWrinklerL_front.png) `NOSE_WRINKLER_L = 1.0` |
| `NOSE_WRINKLER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `NOSE_WRINKLER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/noseWrinklerR_front.png) `NOSE_WRINKLER_R = 1.0` |
| `UPPER_LIP_RAISER_L` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `UPPER_LIP_RAISER_L = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/upperLipRaiserL_front.png) `UPPER_LIP_RAISER_L = 1.0` |
| `UPPER_LIP_RAISER_R` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) `UPPER_LIP_RAISER_R = 0.0` | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/upperLipRaiserR_front.png) `UPPER_LIP_RAISER_R = 1.0` |
| `TONGUE_OUT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) TONGUE_OUT = 0.0 | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/tongueOut.png) TONGUE_OUT = 1.0 |
| `TONGUE_LEFT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) TONGUE_LEFT = 0.0 | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/tongueLeft.png) TONGUE_LEFT = 1.0 |
| `TONGUE_RIGHT` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) TONGUE_RIGHT = 0.0 | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/tongueRight.png) TONGUE_RIGHT = 1.0 |
| `TONGUE_UP` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) TONGUE_UP = 0.0 | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/tongueUp.png) TONGUE_UP = 1.0 |
| `TONGUE_DOWN` | ![Neutral face reference image](https://developer.android.com/static/images/develop/xr/openxr/neutral_front.png) TONGUE_DOWN = 0.0 | ![face tracking reference image](https://developer.android.com/static/images/develop/xr/openxr/tongueDown.png) TONGUE_DOWN = 1.0 |