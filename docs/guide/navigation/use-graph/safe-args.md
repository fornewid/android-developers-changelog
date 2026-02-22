---
title: https://developer.android.com/guide/navigation/use-graph/safe-args
url: https://developer.android.com/guide/navigation/use-graph/safe-args
source: md.txt
---

The recommended way to navigate between destinations is to use the Safe Args
Gradle plugin. This plugin generates object and builder classes that enable
type-safe navigation between destinations. Use Safe Args for
navigating and [passing data between destinations](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args).
| **Note:** If you aren't using Gradle, you must use other navigation methods.
| **Warning:** Safe Args is only available for Android views and fragments. If you are using Compose, see the guide on [type safe navigation](https://developer.android.com/guide/navigation/navigation-type-safety).

## Enable Safe Args

To add [Safe Args](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#Safe-args)
to your project, include the following `classpath` in your top level `build.gradle` file:  

### Groovy

```groovy
buildscript {
    repositories {
        google()
    }
    dependencies {
        def nav_version = "2.9.7"
        classpath "androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version"
    }
}
```

### Kotlin

```kotlin
buildscript {
    repositories {
        google()
    }
    dependencies {
        val nav_version = "2.9.7"
        classpath("androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version")
    }
}
```

You must also apply one of two available plugins.

To generate Java language code suitable for Java or mixed Java and Kotlin modules, add
this line to **your app or module's** `build.gradle` file:  

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs")
}
```

Alternatively, to generate Kotlin code suitable for Kotlin-only modules add:  

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs.kotlin'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs.kotlin")
}
```

You must have `android.useAndroidX=true` in your
[`gradle.properties` file](https://developer.android.com/studio/build#properties-files) as per
[Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate#migrate)).

## Generated code

After enabling Safe Args, your generated code contains classes and methods for
each action you've defined as well as classes that correspond to each sending
and receiving destination.

Safe Args generates a class for each destination where an action originates. The
generated class name adds "Directions" to the originating destination class
name. For example, if the originating destination is named
`SpecifyAmountFragment`, the generated class is named
`SpecifyAmountFragmentDirections`.

The generated class contains a static method for each action defined in the
originating destination. This method takes any defined [action parameters](https://developer.android.com/guide/navigation/navigation-pass-data) as
arguments and returns a [`NavDirections`](https://developer.android.com/reference/androidx/navigation/NavDirections) object that you can pass directly
to [`navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(androidx.navigation.NavDirections)).

## Safe Args example

For example, consider a navigation graph with a single action that connects two
destinations, `SpecifyAmountFragment` and `ConfirmationFragment`. The
`ConfirmationFragment` takes a single `float` parameter that you provide as part
of the action.

Safe Args generates a `SpecifyAmountFragmentDirections` class with a single
method, `actionSpecifyAmountFragmentToConfirmationFragment()`, and an inner
class called `ActionSpecifyAmountFragmentToConfirmationFragment`. The inner
class is derived from `NavDirections` and stores the associated action ID and
`float` parameter. The returned `NavDirections` object can then be passed
directly to `navigate()`, as shown in the following example:  

### Kotlin

    override fun onClick(v: View) {
        val amount: Float = ...
        val action =
            SpecifyAmountFragmentDirections
                .actionSpecifyAmountFragmentToConfirmationFragment(amount)
        v.findNavController().navigate(action)
    }

### Java

    @Override
    public void onClick(View view) {
        float amount = ...;
        action =
            SpecifyAmountFragmentDirections
                .actionSpecifyAmountFragmentToConfirmationFragment(amount);
        Navigation.findNavController(view).navigate(action);
    }

For more information about passing data between destinations with Safe Args, see
[Use Safe Args to pass data with type safety](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args).

## Ensure type safety by using Safe Args

Navigate between destinations using the Safe Args
Gradle plugin. This plugin generates simple object and builder classes that
enable type-safe navigation and argument passing between destinations.
| **Note:** For other ways to navigate, see [Navigate to a destination](https://developer.android.com/guide/navigation/navigation-navigate).

To add [Safe Args](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#Safe-args)
to your project, include the following `classpath` in your top level `build.gradle` file:  

### Groovy

```groovy
buildscript {
    repositories {
        google()
    }
    dependencies {
        def nav_version = "2.9.7"
        classpath "androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version"
    }
}
```

### Kotlin

```kotlin
buildscript {
    repositories {
        google()
    }
    dependencies {
        val nav_version = "2.9.7"
        classpath("androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version")
    }
}
```

You must also apply one of two available plugins.

To generate Java language code suitable for Java or mixed Java and Kotlin modules, add
this line to **your app or module's** `build.gradle` file:  

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs")
}
```

Alternatively, to generate Kotlin code suitable for Kotlin-only modules add:  

### Groovy

```groovy
plugins {
  id 'androidx.navigation.safeargs.kotlin'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.navigation.safeargs.kotlin")
}
```

You must have `android.useAndroidX=true` in your
[`gradle.properties` file](https://developer.android.com/studio/build#properties-files) as per
[Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate#migrate)).

After you enable Safe Args, the plugin generates code that contains classes and
methods for each action you've defined. For each action, Safe Args also
generates a class for each *originating destination* , which is the destination
from which the action originates. The generated class name is a combination of
the originating destination class name and the word "Directions". For example,
if the destination is named `SpecifyAmountFragment`, the generated class is
named `SpecifyAmountFragmentDirections`. The generated class contains a static
method for each action defined in the originating destination. This method takes
any defined action parameters as arguments and returns a `NavDirections` object
that you can pass to `navigate()`.

As an example, assume we have a navigation graph with a single action that
connects the originating destination, `SpecifyAmountFragment`, to a receiving
destination, `ConfirmationFragment`.

Safe Args generates a `SpecifyAmountFragmentDirections` class with a single
method, `actionSpecifyAmountFragmentToConfirmationFragment()`, which returns a
`NavDirections` object. This returned `NavDirections` object can then be passed
directly to `navigate()`, as shown in the following example:  

### Kotlin

```kotlin
override fun onClick(view: View) {
    val action =
        SpecifyAmountFragmentDirections
            .actionSpecifyAmountFragmentToConfirmationFragment()
    view.findNavController().navigate(action)
}
```

### Java

```java
@Override
public void onClick(View view) {
    NavDirections action =
        SpecifyAmountFragmentDirections
            .actionSpecifyAmountFragmentToConfirmationFragment();
    Navigation.findNavController(view).navigate(action);
}
```

For more information on passing data between destinations with Safe Args, see
[Use Safe Args to pass data with type safety](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args) in *Pass data between
destinations*.