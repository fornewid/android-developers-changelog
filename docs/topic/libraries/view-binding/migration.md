---
title: Migrate from Kotlin synthetics to Jetpack view binding  |  App architecture  |  Android Developers
url: https://developer.android.com/topic/libraries/view-binding/migration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Migrate from Kotlin synthetics to Jetpack view binding Stay organized with collections Save and categorize content based on your preferences.




Kotlin Android Extensions is deprecated, which means that using Kotlin
synthetics for view binding is no longer supported. If your app uses Kotlin
synthetics for view binding, use this guide to migrate to Jetpack view binding.

If your app doesn't already use Kotlin synthetics for view binding, see [View
binding](/topic/libraries/view-binding) for basic usage information.

## Update the Gradle file

Like Android Extensions, Jetpack view binding is enabled on a module-by-module
basis. For each module that uses view binding, set the `viewBinding` build
option to `true` in the module-level `build.gradle` file:

### Groovy

```
android {
    ...
    buildFeatures {
        viewBinding true
    }
}
```

### Kotlin

```
android {
    ...
    buildFeatures {
        viewBinding = true
    }
}
```

If your app doesn't use [`Parcelable`](/reference/android/os/Parcelable)
features, remove the line that enables Kotlin Android Extensions:

### Groovy

```
plugins {
  id 'kotlin-android-extensions'
}
```

### Kotlin

```
plugins {
    kotlin("android.extensions")
}
```

**Note:** If your app uses `Parcelable` features, switch to using the
standalone `kotlin-parcelize` Gradle plugin described in
[Parcelable implementation generator](/kotlin/parcelize).

To learn more about enabling view binding in a module, see [Setup
instructions](/topic/libraries/view-binding#setup).

## Update activity and fragment classes

With Jetpack view binding, a binding class is generated for each XML layout file
that the module contains. The name of this binding class is the name of the XML
file in Pascal case with the word *Binding* added at the end. For example, if
the name of the layout file is `result_profile.xml`, the name of the generated
binding class is `ResultProfileBinding`.

To use the generated binding classes instead of synthetic properties to
reference views, change your activity and fragment classes by doing the
following:

1. Remove all imports from `kotlinx.android.synthetic`.
2. Inflate an instance of the generated binding class for the activity or
   fragment to use.

   * For activities, follow the instructions in [Use view binding in
     activities](/topic/libraries/view-binding#activities) to inflate an
     instance in your activity's
     [`onCreate()`](/reference/kotlin/android/app/Activity#oncreate) method.
   * For fragments, follow the instructions in [Use view binding in
     fragments](/topic/libraries/view-binding#fragments) to inflate an instance
     in your fragment's
     [`onCreateView()`](/reference/kotlin/androidx/fragment/app/Fragment#oncreateview)
     method.
3. Change all view references to use the binding class instance instead of
   synthetic properties:

```
// Reference to "name" TextView using synthetic properties.
name.text = viewModel.nameString

// Reference to "name" TextView using the binding class instance.
binding.name.text = viewModel.nameString
```

To learn more, see the [Usage](/topic/libraries/view-binding#usage) section in
the view binding guide.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [View binding](/topic/libraries/view-binding)
* [Paging library overview](/topic/libraries/architecture/paging/v3-overview)
* [Test your Paging implementation](/topic/libraries/architecture/paging/test)