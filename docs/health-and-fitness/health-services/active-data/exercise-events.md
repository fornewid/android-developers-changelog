---
title: Handle exercise events  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-services/active-data/exercise-events
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Fitness Guides](https://developer.android.com/health-and-fitness/fitness)

# Handle exercise events Stay organized with collections Save and categorize content based on your preferences.




Health Services provides support for [`ExerciseEvents`](/reference/kotlin/androidx/health/services/client/data/ExerciseEvent),
which notify your app when an event has occurred during an exercise and supply
associated metadata.

## Add dependencies

Using exercise events requires the latest version of the Health Services SDK.

To add a dependency on Health Services, you must add the Google Maven repository
to your project. For more information, see
[Google's Maven repository](/studio/build/dependencies#google-maven).

Then, in your module-level `build.gradle` file, add the following dependency:

### Groovy

```
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-rc01"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-rc01")
}
```

## Check capabilities

As with all exercises and data types in Health Services,
[check capabilities at startup](/training/wearables/health-services/active-data#capabilites). For
[`ExerciseEvents`](/reference/kotlin/androidx/health/services/client/data/ExerciseEvent)
in particular, in addition to requesting `ExerciseCapabilities`,
use
[`ExerciseTypeCapabilities.supportedExerciseEvents`](/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#getSupportedExerciseEvents())
to verify which exercise events are supported for the given exercise.
After confirming the particular `ExerciseEvent` is supported,
you should also query the capabilities of the exercise event using
[`getExerciseEventCapabilityDetails`](/reference/kotlin/androidx/health/services/client/data/ExerciseTypeCapabilities#getExerciseEventCapabilityDetails).

The following example shows how to query capabilities to confirm the
`GOLF_SHOT_EVENT` is supported, and then confirm that the `GOLF_SHOT_EVENT`
supports Swing Type Classification.

```
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
```

## Request exercise events in an exercise

To start the exercise and request an exercise event as part of the exercise,
[declare the `ExerciseConfig` for the exercise](/training/wearables/health-services/active-data#start)
and add a field for [`exerciseEventType`](/reference/kotlin/androidx/health/services/client/data/ExerciseEventType).

The following example requests `GOLF_SHOT_EVENT` as part of a `GOLF` exercise:

```
val config = ExerciseConfig(
  exerciseType = ExerciseType.GOLF,
  dataTypes = setOf(....),
  // ...
  exerciseEventTypes = setOf(ExerciseEventType.GOLF_SHOT_EVENT),
)
```

## Register for exercise event updates

You can receive `ExerciseEvent` updates as part of the existing infrastructure
your app has for [receiving exercise updates](/training/wearables/health-services/active-data#updates).
The following example shows how you would incorporate support for
`GolfShotEvent` updates:

```
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
```