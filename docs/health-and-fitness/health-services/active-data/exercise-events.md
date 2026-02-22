---
title: https://developer.android.com/health-and-fitness/health-services/active-data/exercise-events
url: https://developer.android.com/health-and-fitness/health-services/active-data/exercise-events
source: md.txt
---

Health Services provides support for [`ExerciseEvents`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseEvent),
which notify your app when an event has occurred during an exercise and supply
associated metadata.

## Add dependencies

Using exercise events requires the latest version of the Health Services SDK.

To add a dependency on Health Services, you must add the Google Maven repository
to your project. For more information, see
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven).

Then, in your module-level `build.gradle` file, add the following dependency:

### Groovy

```groovy
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-beta01")
}
```

## Check capabilities

As with all exercises and data types in Health Services,
[check capabilities at startup](https://developer.android.com/training/wearables/health-services/active-data#capabilites). For
[`ExerciseEvents`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseEvent)
in particular, in addition to requesting `ExerciseCapabilities`,
use
[`ExerciseTypeCapabilities.supportedExerciseEvents`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#getSupportedExerciseEvents())
to verify which exercise events are supported for the given exercise.
After confirming the particular `ExerciseEvent` is supported,
you should also query the capabilities of the exercise event using
[`getExerciseEventCapabilityDetails`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#getExerciseEventCapabilityDetails).

The following example shows how to query capabilities to confirm the
`GOLF_SHOT_EVENT` is supported, and then confirm that the `GOLF_SHOT_EVENT`
supports Swing Type Classification.

    fun handleCapabilities(capabilities: ExerciseCapabilities) {
      val golfCapabilities = capabilities.typeToCapabilities[ExerciseType.GOLF]
      val golfShotEventSupported =
        golfCapabilities
          ?.supportedExerciseEvents
          ?.contains(ExerciseEventType.GOLF_SHOT_EVENT)
      val golfSwingTypeClassificationSupported =
        golfCapabilities
          ?.getExerciseEventCapabilityDetails(ExerciseEventType.GOLF_SHOT_EVENT)
          ?.isSwingTypeClassificationSupported ?: false
    }

## Request exercise events in an exercise

To start the exercise and request an exercise event as part of the exercise,
[declare the `ExerciseConfig` for the exercise](https://developer.android.com/training/wearables/health-services/active-data#start)
and add a field for [`exerciseEventType`](https://developer.android.com/reference/kotlin/androidx/health/services/client/data/ExerciseEventType).

The following example requests `GOLF_SHOT_EVENT` as part of a `GOLF` exercise:

    val config = ExerciseConfig(
      exerciseType = ExerciseType.GOLF,
      dataTypes = setOf(....),
      // ...
      exerciseEventTypes = setOf(ExerciseEventType.GOLF_SHOT_EVENT),
    )

## Register for exercise event updates

You can receive `ExerciseEvent` updates as part of the existing infrastructure
your app has for [receiving exercise updates](https://developer.android.com/training/wearables/health-services/active-data#updates).
The following example shows how you would incorporate support for
`GolfShotEvent` updates:

    val callback = object : ExerciseUpdateCallback {
      override fun onExerciseUpdateReceived(update: ExerciseUpdate) {
          ...
      }
      // [ExerciseEvent] intended to come through with low latency and out of
      // band of onExerciseUpdateReceived()
      override fun onExerciseEventReceived(event: ExerciseEvent) {
        when (event) {
          is GolfShotEvent -> {
            if (it.swingType == GolfShotSwingType.PUTT) {
              println("Putt detected!")
            }
          }
        }
      }
    }