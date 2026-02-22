---
title: https://developer.android.com/guide/navigation/navigation-3/modularize
url: https://developer.android.com/guide/navigation/navigation-3/modularize
source: md.txt
---

This page is a guide for modularizing your navigation code. It is intended to
complement the general [guidance for app modularization](https://developer.android.com/topic/modularization).

## Overview

Modularizing your navigation code is the process of separating related
navigation keys, and the content they represent, into individual modules. This
provides a clear separation of responsibilities and lets you navigate
between different features in your app.

To modularize your navigation code, do the following:

- Create two submodules: `api` and `impl` for each feature in your app
- Place navigation keys for each feature into its `api` module
- Place `entryProviders` and navigable content for each feature into the associated `impl` module
- Provide `entryProviders` to your main app modules, either directly or using dependency injection

| **Tip:** If you've created [custom scenes](https://developer.android.com/guide/navigation/navigation-3/custom-layouts) for use in your app, we recommend containing those scenes within their own module or modules. This makes it possible both for feature modules to access the helper functions used to populate metadata *and* for the main app module to use the scene strategies when creating its `NavDisplay`.

## Separate features into api and implementation submodules

For each feature in your app, create two submodules named `api` and `impl`
(short for "implementation"). Use the following table to decide where to place
navigation code.

|---|---|
| **Module name** | **Contains** |
| `api` | [navigation keys](https://developer.android.com/guide/navigation/navigation-3/basics#create-back) |
| `impl` | Content for that feature, including definitions for `NavEntry`s and the `entryProvider`. See also [resolve keys to content](https://developer.android.com/guide/navigation/navigation-3/basics#resolve-keys). |

This approach allows one feature to navigate to another by allowing its content,
contained in its `impl` module, to depend on the navigation keys of another
module, contained in that module's `api` module.
![Feature module dependency diagram showing how `impl` modules can
depend on `api` modules.](https://developer.android.com/static/images/topic/libraries/architecture/nav3-module-graph.png) **Figure 1.** Feature module dependency diagram showing how implementation modules can depend on api modules.

## Separate navigation entries using extension functions

In Navigation 3, navigable content is defined [using navigation entries](https://developer.android.com/guide/navigation/navigation-3/basics#resolve-keys). To
separate these entries into separate modules, create extension functions on
[`EntryProviderScope`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/EntryProviderScope) and move them into the `impl` module for that feature.
These are known as *entry builders*.

The following code example shows an entry builder that builds two navigation
entries.


```kotlin
// import androidx.navigation3.runtime.EntryProviderScope
// import androidx.navigation3.runtime.NavKey

fun EntryProviderScope<NavKey>.featureAEntryBuilder() {
    entry<KeyA> {
        ContentRed("Screen A") {
            // Content for screen A
        }
    }
    entry<KeyA2> {
        ContentGreen("Screen A2") {
            // Content for screen A2
        }
    }
}
```

<br />

Call that function using the [`entryProvider` DSL](https://developer.android.com/guide/navigation/navigation-3/basics#entry-provider-DSL) when defining your
`entryProvider` in your main app module.


```kotlin
// import androidx.navigation3.runtime.entryProvider
// import androidx.navigation3.ui.NavDisplay
NavDisplay(
    entryProvider = entryProvider {
        featureAEntryBuilder()
    },
    // ...
)
```

<br />

## Use dependency injection to add entries to the main app

In the preceding code example, each entry builder is called directly by the main app
using the `entryProvider` DSL. If your app has a lot of screens or feature
modules, this may not scale well.

To solve this, have each feature module contribute its entry builders into the
app's activity using dependency injection.

For example, the following code uses [Dagger multibindings](https://dagger.dev/dev-guide/multibindings.html),
specifically `@IntoSet`, to inject the entry builders into a `Set` owned by
`MainActivity`. These are then called iteratively inside `entryProvider`,
negating the need to explicitly call numerous entry builder functions.

**Feature module**


```kotlin
// import dagger.Module
// import dagger.Provides
// import dagger.hilt.InstallIn
// import dagger.hilt.android.components.ActivityRetainedComponent
// import dagger.multibindings.IntoSet

@Module
@InstallIn(ActivityRetainedComponent::class)
object FeatureAModule {

    @IntoSet
    @Provides
    fun provideFeatureAEntryBuilder() : EntryProviderScope<NavKey>.() -> Unit = {
        featureAEntryBuilder()
    }
}
```

<br />

**App module**


```kotlin
// import android.os.Bundle
// import androidx.activity.ComponentActivity
// import androidx.activity.compose.setContent
// import androidx.navigation3.runtime.EntryProviderScope
// import androidx.navigation3.runtime.NavKey
// import androidx.navigation3.runtime.entryProvider
// import androidx.navigation3.ui.NavDisplay
// import javax.inject.Inject

class MainActivity : ComponentActivity() {

    @Inject
    lateinit var entryBuilders: Set<@JvmSuppressWildcards EntryProviderScope<NavKey>.() -> Unit>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            NavDisplay(
                entryProvider = entryProvider {
                    entryBuilders.forEach { builder -> this.builder() }
                },
                // ...
            )
        }
    }
}
```

<br />

If your navigation entries need to navigate---for example, they contain UI elements that navigate to new screens---inject an object capable of modifying the app's navigation state into each builder function.

## Resources

For code samples showing how to modularize Navigation 3 code, see:

- [The Navigation 3 architecture code recipes](https://github.com/android/nav3-recipes/?tab=readme-ov-file#architecture)
- [The modularization learning journey from the Now in Android
  app](https://github.com/android/nowinandroid/blob/main/docs/ModularizationLearningJourney.md)
- [Androidify](https://github.com/android/androidify)