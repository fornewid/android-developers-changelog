---
title: Stylus input in text fields  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/stylus-input/stylus-input-in-text-fields
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Stylus input in text fields Stay organized with collections Save and categorize content based on your preferences.



The Jetpack
[`androidx.compose.material3`](/jetpack/androidx/releases/compose-material3)
library enables users to write into any [`TextField`](/reference/kotlin/androidx/compose/material/TextField.composable#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) component in
any app using a stylus.

[![

Your browser doesn't support the video tag.
](/images/develop/ui/compose/touch-input/stylus-input/shared/handwriting_input_animation_poster.png)](/static/images/develop/ui/compose/touch-input/stylus-input/shared/handwriting_input_animation.webm)


**Figure 1.** Handwritten input with a stylus.

To enable stylus input by default, add the library dependency to your app's
`build.gradle` file:

### Kotlin

```
dependencies {
    implementation("androidx.compose.foundation:foundation:LATEST_COMPOSE_VERSION")
}

android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "LATEST_EXTENSION_VERSION"
    }

    kotlinOptions {
        jvmTarget = "LATEST_JVM_VERSION"
    }
}
```

### Groovy

```
dependencies {
    implementation 'androidx.compose.foundation:foundation:LATEST_COMPOSE_VERSION'
}

android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = 'LATEST_EXTENSION_VERSION'
    }

    kotlinOptions {
        jvmTarget = 'LATEST_JVM_VERSION'
    }
}
```

## `TextField`

Stylus handwriting is enabled for all `TextField` components by default on
Android 14 and higher and the
[`androidx.compose.foundation:foundation:1.7.0`](/jetpack/androidx/releases/compose-foundation)
dependency. Handwriting mode is started for a `TextField` when a stylus motion
event is detected within the handwriting bounds of the component.

The handwriting bounds include 40 dp of vertical padding and 10 dp of horizontal
padding around the input field.

![Input field with surrounding rectangle indicating the bounds for detection of stylus motion events.](/static/images/develop/ui/compose/touch-input/stylus-input/shared/edittext_handwriting_bounds.png)


**Figure 2.** Handwriting bounds of `TextField` components.

Stylus handwriting is not supported for `TextField` fields when the input method
editor is requested with [`KeyboardType.Password`](/reference/kotlin/androidx/compose/ui/text/input/KeyboardType#Password()).

## Input delegation

Apps can display placeholder UI elements that appear to be text input fields but
are actually just static UI elements with no text input capability. Search
fields are a common example. Tapping the static UI element triggers a transition
to a new UI that contains a functional text input field focused for input.

[

Your browser doesn't support the video tag.
](/static/images/develop/ui/compose/touch-input/stylus-input/shared/handwriting_input_delegation.mp4)


**Figure 3.** Input delegation from static UI element to text input field.

### Stylus input delegation

Use the handwriting delegation APIs to support stylus handwriting input for
placeholder input fields (see [`handwritingDetector`](/reference/kotlin/androidx/compose/foundation/text/handwriting/handwritingDetector.modifier#(androidx.compose.ui.Modifier).handwritingDetector(kotlin.Function0)) and
[`handwritingHandler`](/reference/kotlin/androidx/compose/foundation/text/handwriting/handwritingHandler.modifier#(androidx.compose.ui.Modifier).handwritingHandler())). The placeholder UI element is
configured to delegate handwriting to a functional input field. For an example
implementation, see
[`HandwritingDetectorSample.kt`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/samples/src/main/java/androidx/compose/foundation/samples/HandwritingDetectorSample.kt).

Stylus handwriting mode starts when the functional input field gains focus and
creates an
[`InputConnection`](/reference/kotlin/android/view/inputmethod/InputConnection).

[

Your browser doesn't support the video tag.
](/static/images/develop/ui/compose/touch-input/stylus-input/shared/handwriting_input_delegation_with_stylus.mp4)


**Figure 4.** Stylus input delegation from static UI element to text input field.

## Testing

Stylus handwriting is supported on Android 14 and higher devices with a
compatible stylus input device and an [input method
editor](/develop/ui/views/touch-and-input/creating-input-method) (IME) that
supports the Android 14 stylus handwriting APIs.

If you don't have a stylus input device, simulate stylus input on any device
with root access (including emulators) using the following Android Debug Bridge
(adb) commands:

```
// Android 14
adb shell setprop persist.debug.input.simulate_stylus_with_touch true && adb shell stop && adb shell start

// Android 15 and higher
// Property takes effect after screen reconfiguration such as orientation change.
adb shell setprop debug.input.simulate_stylus_with_touch true
```

Use the Gboard beta for testing if you are using a device that doesn't support
stylus.

## Additional resources

* Material Design — [Text fields](https://m3.material.io/components/text-fields/overview)
* [Handle user input](/develop/ui/compose/text/user-input)

[Previous

arrow\_back

Overview](/develop/ui/compose/touch-input/stylus-input)

[Next

Advanced stylus features

arrow\_forward](/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features)