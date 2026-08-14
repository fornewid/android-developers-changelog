---
title: https://developer.android.com/guide/navigation/navigation-3/metadata
url: https://developer.android.com/guide/navigation/navigation-3/metadata
source: md.txt
---

In Navigation 3, you use metadata to share arbitrary information between
different library components such as [`NavEntry`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntry), [`Scene`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene), and
[`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/package-summary#top-level-functions-summary). At its most basic, metadata is a `Map<String, Any>`.
However, the library [provides additional abstractions](https://developer.android.com/guide/navigation/navigation-3/metadata#dsl) to make reading
and writing metadata simpler and more type-safe.

## Provide `NavEntry` metadata

If your app builds its `NavEntry` instances directly, you provide metadata for
the entry using the `metadata` constructor parameter:


```kotlin
when (key) {
    is Home -> NavEntry(key, metadata = mapOf("key" to "value")) {}
}
```

<br />

If your app [uses the `entryProvider` DSL](https://developer.android.com/guide/navigation/navigation-3/basics#entry-provider-DSL), you provide metadata through the
`metadata` parameter of the `entry` function. There are two overloads of this
function: one that takes a map directly and another that takes a lambda that
passes the entry's key as an argument:


```kotlin
entry<Home>(metadata = mapOf("key" to "value")) { /* ... */ }
entry<Conversation>(metadata = { key: Conversation ->
    mapOf("key" to "value: ${key.id})")
}) { /* ... */ }
```

<br />

## Provide `Scene` metadata

By default, [`Scene.metadata`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene#metadata()) uses a [custom getter](https://kotlinlang.org/docs/properties.html#custom-getters-and-setters) that returns the
`metadata` of the last entry in its [`entries`](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/Scene#entries()) property, or an empty map
if that is `null`. When implementing the `Scene` interface, you can override
this default behavior as needed.

> [!TIP]
> **Tip:** The [default `SinglePaneScene` used by `NavDisplay`](https://developer.android.com/guide/navigation/navigation-3/scenes#example:single) only contains one entry, so its `metadata` returns the `metadata` of that `NavEntry`.

## Use the metadata DSL

Introduced in the `1.1.0-beta01` release of the library, the metadata
[domain-specific language](https://kotlinlang.org/docs/type-safe-builders.html) (DSL) provides a type-safe builder for creating
the `Map<String, Any>` used to store metadata.

### Define metadata keys

The DSL relies on the [`NavMetadataKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavMetadataKey) interface to keep the type of
the value associated with a metadata key consistent.

The convention for defining metadata keys is to include them as nested objects
of the class---or, in the case of functions or composables, a related object---that
will read the values associated with those keys:


```kotlin
// For classes such as scene strategies or nav entry decorators, you can define the keys
// as nested object.
class MySceneStrategy<T : Any> : SceneStrategy<T> {

    // ...

    object MyStringMetadataKey : NavMetadataKey<String>
}

// An example from NavDisplay.
// Because NavDisplay is a function, the metadata keys are defined in an object with the same name.
public object NavDisplay {

    public object TransitionKey :
        NavMetadataKey<AnimatedContentTransitionScope<Scene<*>>.() -> ContentTransform>
}
```

<br />

### Build metadata using the DSL

To create a metadata map, use the [`metadata`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#metadata(kotlin.Function1)) function, which takes a
lambda parameter. Within this lambda, use the [`put`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/MetadataScope#put(androidx.navigation3.runtime.NavMetadataKey,kotlin.Any)) function to add
entries to the map using a `NavMetadataKey` and corresponding value.


```kotlin
entry<Home>(
    metadata = metadata {
        put(NavDisplay.TransitionKey) { fadeIn() togetherWith fadeOut() }
        // An additional benefit of the metadata DSL is the ability to use conditional logic
        if (condition) {
            put(MySceneStrategy.MyStringMetadataKey, "Hello, world!")
        }
    }
) {
    // ...
}
```

<br />

> [!TIP]
> **Tip:** To build upon a base metadata map, you can use the `+` operator with the `metadata` function. For example, `baseMap + metadata { ... }`.

### Read metadata using metadata keys

The metadata DSL also provides functions to simplify reading metadata with a
`NavMetadataKey`.


```kotlin
// import androidx.navigation3.runtime.contains
// import androidx.navigation3.runtime.get

val hasMyString: Boolean = metadata.contains(MySceneStrategy.MyStringMetadataKey)
val myString: String? = metadata[MySceneStrategy.MyStringMetadataKey]
```

<br />

> [!TIP]
> **Tip:** If the indexed access operator syntax (`[]`) isn't working, you might need to manually add the import for `androidx.navigation3.runtime.get`.