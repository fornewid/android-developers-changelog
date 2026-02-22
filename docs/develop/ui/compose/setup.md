---
title: https://developer.android.com/develop/ui/compose/setup
url: https://developer.android.com/develop/ui/compose/setup
source: md.txt
---

For the best experience developing with Compose, download and install [Android
Studio](https://developer.android.com/studio). It includes many [smart editor features](https://developer.android.com/develop/ui/compose/tooling), such as new project
templates and the ability to immediately preview your Compose UI and animations.

[Get Android Studio](https://developer.android.com/studio)

Follow these instructions to create a new Compose app project, set up
Compose for an existing app project, or import a sample app written in Compose.

## Create a new app with support for Compose

If you want to start a new project that includes support for Compose by default,
Android Studio includes various project templates to help you get started. To
create a new project that has Compose setup correctly, proceed as follows:

1. If you're in the **Welcome to Android Studio** window, click **Start a new
   Android Studio project** . If you already have an Android Studio project open , select **File \> New \> New Project** from the menu bar.
2. In the **Select a Project Template** window, select **Empty
   Activity** and click **Next**.
3. In the **Configure your project** window, do the following:
   1. Set the **Name, Package name** , and **Save location** as you normally would. Note that, in the **Language** dropdown menu, **Kotlin** is the only available option because Jetpack Compose works only with classes written in Kotlin.
   2. In the **Minimum API level dropdown** menu, select API level 21 or higher.
4. Click **Finish**.

Now you're ready to start developing an app using Jetpack Compose. To help you
get started and learn about what you can do with the toolkit, try the [Jetpack
Compose tutorial](https://developer.android.com/develop/ui/compose/tutorial).

## Set up Compose for an existing app

First, configure the Compose compiler using the [Compose
Compiler Gradle plugin](https://developer.android.com/develop/ui/compose/compiler).

Then, add the following definition to your app's `build.gradle` file:  

### Groovy

    android {
        buildFeatures {
            compose true
        }
    }

### Kotlin

    android {
        buildFeatures {
            compose = true
        }
    }

Setting the `compose` flag to `true` inside the Android [`BuildFeatures`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/dsl/BuildFeatures)
block enables [Compose functionality](https://developer.android.com/develop/ui/compose/tooling) in Android Studio.

Finally, add the Compose BOM and the subset of Compose library dependencies
you need to your dependencies from the following block:  

### Groovy

    dependencies {

        def composeBom = platform('androidx.compose:compose-bom:2026.01.01')
        implementation composeBom
        androidTestImplementation composeBom

        // Choose one of the following:
        // Material Design 3
        implementation 'androidx.compose.material3:material3'
        // or skip Material Design and build directly on top of foundational components
        implementation 'androidx.compose.foundation:foundation'
        // or only import the main APIs for the underlying toolkit systems,
        // such as input and measurement/layout
        implementation 'androidx.compose.ui:ui'

        // Android Studio Preview support
        implementation 'androidx.compose.ui:ui-tooling-preview'
        debugImplementation 'androidx.compose.ui:ui-tooling'

        // UI Tests
        androidTestImplementation 'androidx.compose.ui:ui-test-junit4'
        debugImplementation 'androidx.compose.ui:ui-test-manifest'

        // Optional - Add window size utils
        implementation 'androidx.compose.material3.adaptive:adaptive'

        // Optional - Integration with activities
        implementation 'androidx.activity:activity-compose:1.11.0'
        // Optional - Integration with ViewModels
        implementation 'androidx.lifecycle:lifecycle-viewmodel-compose:2.8.5'
        // Optional - Integration with LiveData
        implementation 'androidx.compose.runtime:runtime-livedata'
        // Optional - Integration with RxJava
        implementation 'androidx.compose.runtime:runtime-rxjava2'

    }

### Kotlin

    dependencies {

        val composeBom = platform("androidx.compose:compose-bom:2026.01.01")
        implementation(composeBom)
        androidTestImplementation(composeBom)

        // Choose one of the following:
        // Material Design 3
        implementation("androidx.compose.material3:material3")
        // or skip Material Design and build directly on top of foundational components
        implementation("androidx.compose.foundation:foundation")
        // or only import the main APIs for the underlying toolkit systems,
        // such as input and measurement/layout
        implementation("androidx.compose.ui:ui")

        // Android Studio Preview support
        implementation("androidx.compose.ui:ui-tooling-preview")
        debugImplementation("androidx.compose.ui:ui-tooling")

        // UI Tests
        androidTestImplementation("androidx.compose.ui:ui-test-junit4")
        debugImplementation("androidx.compose.ui:ui-test-manifest")

        // Optional - Add window size utils
        implementation("androidx.compose.material3.adaptive:adaptive")

        // Optional - Integration with activities
        implementation("androidx.activity:activity-compose:1.11.0")
        // Optional - Integration with ViewModels
        implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.8.5")
        // Optional - Integration with LiveData
        implementation("androidx.compose.runtime:runtime-livedata")
        // Optional - Integration with RxJava
        implementation("androidx.compose.runtime:runtime-rxjava2")

    }

| **Note:** Jetpack Compose is shipped using a Bill of Materials (BOM), to keep the versions of all library groups in sync. Read more about it in the [Bill of
| Materials page](https://developer.android.com/develop/ui/compose/bom/bom).

## Try Jetpack Compose sample apps

The fastest way to experiment with the capabilities of Jetpack Compose is by
trying [Jetpack Compose sample apps](https://github.com/android/compose-samples) hosted on GitHub. To import
a sample app project from Android Studio, proceed as follows:

1. If you're in the **Welcome to Android Studio** window, select **Import an
   Android code sample** . If you already have an Android Studio project open, select **File \> New \> Import Sample** from the menu bar.
2. In the search bar near the top of the **Browse Samples** wizard, type "compose".
3. Select one of the Jetpack Compose sample apps from the search results and click **Next**.
4. Either change the **Application name** and **Project location** or keep the default values.
5. Click **Finish**.

Android Studio downloads the sample app to the path you specified and opens the
project. You can then inspect `MainActivity.kt` in each of the examples to see
Jetpack Compose APIs such as crossfade animation, custom components, using
typography, and displaying light and dark colors in the in-IDE preview.

To use Jetpack Compose for Wear OS, see [Set up Jetpack Compose on Wear OS](https://developer.android.com/training/wearables/compose-setup).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Navigating with Compose](https://developer.android.com/develop/ui/compose/navigation)
- [Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing)
- [React to focus](https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus)