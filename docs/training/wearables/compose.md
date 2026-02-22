---
title: https://developer.android.com/training/wearables/compose
url: https://developer.android.com/training/wearables/compose
source: md.txt
---

Compose for Wear OS Material version <button value="2.5">2.5</button> <button value="3" default="">3</button>

*** ** * ** ***

![](https://developer.android.com/static/wear/images/components/Compose_hero_m3.png)

[Compose for Wear OS](https://developer.android.com/jetpack/androidx/releases/wear-compose) is similar to
Compose for mobile. However, there are some key differences. This guide
walks you through the similarities and differences.

Compose for Wear OS is part of Android Jetpack, and like the other Wear Jetpack
libraries you use, it helps you write better code faster. This is our
recommended approach for building user interfaces for [Wear OS apps](https://developer.android.com/training/wearables/user-interfaces#apps).

If you are unfamiliar with using the Jetpack Compose toolkit, check out the
[Compose pathway](https://developer.android.com/courses/pathways/compose). Many of the development principles for mobile Compose
apply to Compose for Wear OS. See [Why Compose](https://developer.android.com/jetpack/compose/why-adopt) for more information on the
general advantages of a declarative UI framework. To learn more about Compose
for Wear OS, see the [Compose for Wear OS Pathway](https://developer.android.com/courses/pathways/wear-compose) and the [Wear OS samples
repository](https://github.com/android/wear-os-samples/tree/main/ComposeStarter#readme) on GitHub.

## Material Design in Jetpack Compose on Wear OS

Jetpack Compose on Wear OS offers an implementation of

[Material 3](https://developer.android.com/design/ui/wear/guides/get-started), which helps you design more engaging app

experiences. The
[Material Design components](https://developer.android.com/design/ui/wear/guides/components/buttons) on
Wear OS are built on top of
[Wear Material Theming](https://developer.android.com/design/ui/wear/guides/styles/theme). This theming
is a systematic way to customize Material Design and better reflect your
product's brand.

## Compatibility

Compose for Wear OS works on watches that support Wear OS 3.0 (API Level 30) and watches that use Wear OS 2.0 (API level 25 and above). Using [version 1.5](https://developer.android.com/jetpack/androidx/releases/wear-compose) of Compose for Wear OS requires using version 1.8 of [androidx.compose](https://developer.android.com/jetpack/androidx/releases/compose) libraries and Kotlin 1.9.0. You can use the [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping) and [Compose to Kotlin compatibility map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) to check Compose compatibility.

## Surfaces

Compose for Wear OS makes building apps on Wear OS easier. For more information
see [Apps](https://developer.android.com/training/wearables/apps#building-an-app). Use our built-in
components to create user experiences that conform to Wear OS guidelines.
For more information about components, see our
[design guidance](https://developer.android.com/design/ui/wear/guides/components/buttons).

## Setting up

Using Jetpack Compose with Wear OS is similar to using Jetpack Compose for
any other Android project. The main difference is that Jetpack Compose for Wear
adds Wear-specific libraries that make it easier to create user interfaces
tailored to watches.
In some cases those components share the same name as
their non-wear counterparts, such as

[`androidx.wear.compose.material3.Button`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.String,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material3.ButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.wear.compose.material3.SurfaceTransformation,kotlin.Function1)) and
[`androidx.compose.material3.Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)).


### Create a new app in Android Studio

To create a new project that includes Jetpack Compose, proceed as follows:

1. If you're in the **Welcome to Android Studio** window, click **Start a new
   Android Studio project** . If you already have an Android Studio project open, select **File \> New \> Import Sample** from the menu bar.
2. Search for **Compose for Wear** and select **Compose for Wear OS Starter.**
3. In the **Configure your project** window, do the following:
   1. Set the **Application name**.
   2. Choose the **Project location** for your sample.
4. Click **Finish**.
5. Verify that the project's `build.gradle` file is configured correctly, as described in [Gradle properties files](https://developer.android.com/studio/build#properties-files).

Now you're ready to start developing an app using Compose for Wear OS.

### Jetpack Compose toolkit dependencies

To use Jetpack Compose with Wear OS, you'll need to include Jetpack Compose
toolkit dependencies in your app's `build.gradle` file. Most of the dependency
changes related to Wear OS are in the
[top architectural layers](https://developer.android.com/jetpack/compose/layering), surrounded by a red box
in the following image.

![](https://developer.android.com/static/wear/images/components/ComposeDependencies.png)

That means many of the dependencies you already use with Jetpack Compose don't
change when targeting Wear OS. For example, the UI, runtime, compiler, and
animation dependencies remain the same.

However, Wear OS has its own versions of `material` and `material3`, `foundation`, and
`navigation` libraries, so check that you're using the proper libraries.

Use the
[`WearComposeMaterial`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary)
version of APIs where possible. While it's technically possible to use the
mobile version of Compose Material, it is not optimized for the unique
requirements of Wear OS. In addition, mixing Compose Material with Compose
Material for Wear OS can result in unexpected behavior. For example, because
each library has its own `MaterialTheme` class, there's the possibility of
colors, typography, or shapes being inconsistent if both versions are used.

The following table outlines the dependency differences between Wear OS and
Mobile:

|---|---|---|
| **Wear OS Dependency** (androidx.wear.\*) | **Comparison** | **Mobile Dependency** (androidx.\*) |
| [androidx.wear.compose:compose-material3](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary) | ***instead of*** | androidx.compose.material:material3 |
| [androidx.wear.compose:compose-navigation](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary) | ***instead of*** | androidx.navigation:navigation-compose |
| [androidx.wear.compose:compose-foundation](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/package-summary) | ***in addition to*** | androidx.compose.foundation:foundation |

| **Note:** Other non-mobile material dependencies can be used, such as material ripple and material icons extended.

The following snippet shows an example `build.gradle` file that includes these
dependencies:

### Kotlin

```kotlin
dependencies {

    val composeBom = platform("androidx.compose:compose-bom:2026.01.01")

    // General compose dependencies
    implementation(composeBom)
    implementation("androidx.activity:activity-compose:1.12.4")
    implementation("androidx.compose.ui:ui-tooling-preview:1.10.3")
    // Other compose dependencies

    // Compose for Wear OS dependencies
    implementation("androidx.wear.compose:compose-material3:1.5.6")

    // Foundation is additive, so you can use the mobile version in your Wear OS app.
    implementation("androidx.wear.compose:compose-foundation:1.5.6")

    // Wear OS preview annotations
    implementation("androidx.wear.compose:compose-ui-tooling:1.5.6")

    // If you are using Compose Navigation, use the Wear OS version (NOT THE MOBILE VERSION).
    // Uncomment the line below and update the version number.
    // implementation("androidx.wear.compose:compose-navigation:1.5.6")

    // Testing
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.3")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.4.0")
    androidTestImplementation("androidx.compose.ui:ui-test-junit4:1.0.3")
    debugImplementation("androidx.compose.ui:ui-tooling:1.4.1")

}
```

## Feedback

Try out Compose for Wear OS and use the
[issue tracker](https://issuetracker.google.com/issues/new?component=1077552&template=1598429&pli=1) to provide suggestion and feedback.

Join the
[#compose-wear channel](https://surveys.jetbrains.com/s3/kotlin-slack-sign-up)
on Kotlin Slack to connect with developer community and let us know your
experience.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Resources in Compose](https://developer.android.com/develop/ui/compose/resources)
- [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
- [Get Started with Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation)