---
title: List of KTX extensions  |  Kotlin  |  Android Developers
url: https://developer.android.com/kotlin/ktx/extensions-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Get started](https://developer.android.com/get-started/overview)
* [Kotlin](https://developer.android.com/kotlin)
* [Guides](https://developer.android.com/kotlin/first)

# List of KTX extensions Stay organized with collections Save and categorize content based on your preferences.



## androidx.activity

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.activity:activity-ktx:1.13.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.activity:activity-ktx:1.13.0")
}
```

#### Extension functions

##### For [OnBackPressedDispatcher](/reference/kotlin/androidx/activity/OnBackPressedDispatcher)

|  |  |
| --- | --- |
| [OnBackPressedCallback](/reference/kotlin/androidx/activity/OnBackPressedCallback) | `OnBackPressedDispatcher.addCallback(owner: LifecycleOwner? = null, enabled: Boolean = true, onBackPressed: OnBackPressedCallback.() -> Unit)` Create and add a new [OnBackPressedCallback](/reference/kotlin/androidx/activity/OnBackPressedCallback) that calls [onBackPressed](/reference/kotlin/androidx/activity/package-summary#androidx.activity$addCallback(androidx.activity.OnBackPressedDispatcher,%20androidx.lifecycle.LifecycleOwner,%20kotlin.Boolean,%20kotlin.Function1((androidx.activity.OnBackPressedCallback,%20kotlin.Unit)))/onBackPressed) in [OnBackPressedCallback.handleOnBackPressed](/reference/kotlin/androidx/activity/OnBackPressedCallback#handleOnBackPressed()). |

##### For [ComponentActivity](/reference/kotlin/androidx/activity/ComponentActivity)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)<VM> | `ComponentActivity.viewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the ComponentActivity's ViewModel, if [factoryProducer](/reference/kotlin/androidx/activity/package-summary#androidx.activity$viewModels(androidx.activity.ComponentActivity,%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) first time. |

## androidx.benchmark

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.4.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.4.1")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `beginTraceSection(sectionName: String)` |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `endTraceSection()` |

## androidx.benchmark.junit4

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.4.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.4.1")
}
```

#### Extension functions

##### For [BenchmarkRule](/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `BenchmarkRule.measureRepeated(crossinline block: BenchmarkRule.Scope.() -> Unit)` Benchmark a block of code. |

## androidx.collection

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.collection:collection-ktx:1.6.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.collection:collection-ktx:1.6.0")
}
```

#### Extension functions

##### For [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$contains(androidx.collection.LongSparseArray((androidx.collection.contains.T)),%20kotlin.Long)/key). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](/reference/kotlin/androidx/collection/package-summary#androidx.collection$forEach(androidx.collection.LongSparseArray((androidx.collection.forEach.T)),%20kotlin.Function2((kotlin.Long,%20androidx.collection.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)),%20kotlin.Long,%20androidx.collection.getOrDefault.T)/key), or [defaultValue](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)),%20kotlin.Long,%20androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)<T> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/collection/package-summary#androidx.collection$plus(androidx.collection.LongSparseArray((androidx.collection.plus.T)),%20androidx.collection.LongSparseArray((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)),%20kotlin.Long,%20androidx.collection.remove.T)/key) only if it is mapped to [value](/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)),%20kotlin.Long,%20androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)<T> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArrayCompat<T>.contains(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$contains(androidx.collection.SparseArrayCompat((androidx.collection.contains.T)),%20kotlin.Int)/key). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseArrayCompat<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](/reference/kotlin/androidx/collection/package-summary#androidx.collection$forEach(androidx.collection.SparseArrayCompat((androidx.collection.forEach.T)),%20kotlin.Function2((kotlin.Int,%20androidx.collection.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArrayCompat<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)),%20kotlin.Int,%20androidx.collection.getOrDefault.T)/key), or [defaultValue](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)),%20kotlin.Int,%20androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArrayCompat<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArrayCompat<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseArrayCompat<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)<T> | `SparseArrayCompat<T>.plus(other: SparseArrayCompat<T>)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/collection/package-summary#androidx.collection$plus(androidx.collection.SparseArrayCompat((androidx.collection.plus.T)),%20androidx.collection.SparseArrayCompat((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArrayCompat<T>.remove(key: Int, value: T)` Removes the entry for [key](/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)),%20kotlin.Int,%20androidx.collection.remove.T)/key) only if it is mapped to [value](/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)),%20kotlin.Int,%20androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseArrayCompat<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)<T> | `SparseArrayCompat<T>.valueIterator()` Return an iterator over the collection's values. |

#### Extension properties

##### For [LongSparseArray](/reference/kotlin/androidx/collection/LongSparseArray)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [SparseArrayCompat](/reference/kotlin/androidx/collection/SparseArrayCompat)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseArrayCompat<T>.size()` Returns the number of key/value pairs in the collection. |

#### Top-level functions

|  |  |
| --- | --- |
| [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap)<K, V> | `arrayMapOf()` Returns an empty new [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap). |
| [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap)<K, V> | `arrayMapOf(vararg pairs: Pair<K, V>)` Returns a new [ArrayMap](/reference/kotlin/androidx/collection/ArrayMap) with the specified contents, given as a list of pairs where the first component is the key and the second component is the value. |
| [ArraySet](/reference/kotlin/androidx/collection/ArraySet)<T> | `arraySetOf()` Returns an empty new [ArraySet](/reference/kotlin/androidx/collection/ArraySet). |
| [ArraySet](/reference/kotlin/androidx/collection/ArraySet)<T> | `arraySetOf(vararg values: T)` Returns a new [ArraySet](/reference/kotlin/androidx/collection/ArraySet) with the specified contents. |
| [LruCache](/reference/kotlin/androidx/collection/LruCache)<K, V> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](/reference/kotlin/androidx/collection/LruCache) with the given parameters. |

## androidx.core.animation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.animation.Animator](https://developer.android.com/reference/android/animation/Animator.html)

|  |  |
| --- | --- |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `Animator.addListener(crossinline onEnd: (animator: Animator) -> Unit = {}, crossinline onStart: (animator: Animator) -> Unit = {}, crossinline onCancel: (animator: Animator) -> Unit = {}, crossinline onRepeat: (animator: Animator) -> Unit = {})` Add a listener to this Animator using the provided actions. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `Animator.addPauseListener(crossinline onResume: (animator: Animator) -> Unit = {}, crossinline onPause: (animator: Animator) -> Unit = {})` Add a pause and resume listener to this Animator using the provided actions. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `Animator.doOnCancel(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been cancelled. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `Animator.doOnEnd(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has ended. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `Animator.doOnPause(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been paused. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `Animator.doOnRepeat(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has repeated. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `Animator.doOnResume(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has resumed after a pause. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `Animator.doOnStart(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has started. |

## androidx.core.content

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.content.Context](https://developer.android.com/reference/android/content/Context.html)

|  |  |
| --- | --- |
| T? | `Context.getSystemService()` Return the handle to a system-level service by class. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Context.withStyledAttributes(set: AttributeSet? = null, attrs: IntArray, @AttrRes defStyleAttr: Int = 0, @StyleRes defStyleRes: Int = 0, block: TypedArray.() -> Unit)` Executes [block](/reference/kotlin/androidx/core/content/package-summary#androidx.core.content$withStyledAttributes(android.content.Context,%20android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.content.res.TypedArray,%20kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html) receiver. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Context.withStyledAttributes(@StyleRes resourceId: Int, attrs: IntArray, block: TypedArray.() -> Unit)` Executes [block](/reference/kotlin/androidx/core/content/package-summary#androidx.core.content$withStyledAttributes(android.content.Context,%20kotlin.Int,%20kotlin.IntArray,%20kotlin.Function1((android.content.res.TypedArray,%20kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html) receiver. |

##### For [android.content.SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SharedPreferences.edit(commit: Boolean = false, action: Editor.() -> Unit)` Allows editing of this preference instance with a call to [apply](https://developer.android.com/reference/android/content/SharedPreferences/Editor.html#apply()) or [commit](https://developer.android.com/reference/android/content/SharedPreferences/Editor.html#commit()) to persist the changes. |

#### Top-level functions

|  |  |
| --- | --- |
| [ContentValues](https://developer.android.com/reference/android/content/ContentValues.html) | `contentValuesOf(vararg pairs: Pair<String, Any?>)` Returns a new [ContentValues](https://developer.android.com/reference/android/content/ContentValues.html) with the given key/value pairs as elements. |

## androidx.core.content.res

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.content.res.TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `TypedArray.getBooleanOrThrow(@StyleableRes index: Int)` Retrieve the boolean value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getBooleanOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getColorOrThrow(@StyleableRes index: Int)` Retrieve the color value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getColorOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList.html) | `TypedArray.getColorStateListOrThrow(@StyleableRes index: Int)` Retrieve the color state list value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getColorStateListOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `TypedArray.getDimensionOrThrow(@StyleableRes index: Int)` Retrieve the dimension value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getDimensionPixelOffsetOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel offset value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionPixelOffsetOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getDimensionPixelSizeOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel size value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionPixelSizeOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html) | `TypedArray.getDrawableOrThrow(@StyleableRes index: Int)` Retrieve the drawable value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDrawableOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `TypedArray.getFloatOrThrow(@StyleableRes index: Int)` Retrieve the float value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getFloatOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Typeface](https://developer.android.com/reference/android/graphics/Typeface.html) | `TypedArray.getFontOrThrow(@StyleableRes index: Int)` Retrieve the font value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getFontOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getIntOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getIntOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getIntegerOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getIntegerOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `TypedArray.getResourceIdOrThrow(@StyleableRes index: Int)` Retrieves the resource identifier for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getResourceIdOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `TypedArray.getStringOrThrow(@StyleableRes index: Int)` Retrieve the string value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getStringOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)> | `TypedArray.getTextArrayOrThrow(@StyleableRes index: Int)` Retrieve the text array value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getTextArrayOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) | `TypedArray.getTextOrThrow(@StyleableRes index: Int)` Retrieve the text value for the attribute at [index](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getTextOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| R | `TypedArray.use(block: (TypedArray) -> R)` Executes the given [block](/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$use(android.content.res.TypedArray,%20kotlin.Function1((android.content.res.TypedArray,%20androidx.core.content.res.use.R)))/block) function on this TypedArray and then recycles it. |

## androidx.core.database

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.database.Cursor](https://developer.android.com/reference/android/database/Cursor.html)

|  |  |
| --- | --- |
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)? | `Cursor.getBlobOrNull(index: Int)` Returns the value of the requested column as a nullable byte array. |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)? | `Cursor.getDoubleOrNull(index: Int)` Returns the value of the requested column as a nullable double. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)? | `Cursor.getFloatOrNull(index: Int)` Returns the value of the requested column as a nullable float. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)? | `Cursor.getIntOrNull(index: Int)` Returns the value of the requested column as a nullable integer. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)? | `Cursor.getLongOrNull(index: Int)` Returns the value of the requested column as a nullable long. |
| [Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html)? | `Cursor.getShortOrNull(index: Int)` Returns the value of the requested column as a nullable short. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)? | `Cursor.getStringOrNull(index: Int)` Returns the value of the requested column as a nullable string. |

## androidx.core.database.sqlite

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.database.sqlite.SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html)

|  |  |
| --- | --- |
| T | `SQLiteDatabase.transaction(exclusive: Boolean = true, body: SQLiteDatabase.() -> T)` Run [body](/reference/kotlin/androidx/core/database/sqlite/package-summary#androidx.core.database.sqlite$transaction(android.database.sqlite.SQLiteDatabase,%20kotlin.Boolean,%20kotlin.Function1((android.database.sqlite.SQLiteDatabase,%20androidx.core.database.sqlite.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.core.graphics

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)

|  |  |
| --- | --- |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `Bitmap.applyCanvas(block: Canvas.() -> Unit)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.html) to draw on this bitmap and executes the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$applyCanvas(android.graphics.Bitmap,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) on the newly created canvas. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Bitmap.contains(p: Point)` Returns true if the specified point is inside the bitmap. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Bitmap.contains(p: PointF)` Returns true if the specified point is inside the bitmap. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Bitmap.get(x: Int, y: Int)` Returns the value of the pixel at the specified location. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `Bitmap.scale(width: Int, height: Int, filter: Boolean = true)` Creates a new bitmap, scaled from this bitmap, when possible. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Bitmap.set(x: Int, y: Int, color: Int)` Writes the specified [color int](https://developer.android.com/reference/android/graphics/Color.html) into the bitmap (assuming it is mutable) at the specified `(x, y)` coordinate. |

##### For [android.graphics.Canvas](https://developer.android.com/reference/android/graphics/Canvas.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withClip(clipRect: Rect, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.Rect,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withClip(clipRect: RectF, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.RectF,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withClip(left: Int, top: Int, right: Int, bottom: Int, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withClip(left: Float, top: Float, right: Float, bottom: Float, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withClip(clipPath: Path, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.Path,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipPath](https://developer.android.com/reference/android/graphics/Canvas.html#clipPath(android.graphics.Path, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withMatrix(matrix: Matrix = Matrix(), block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withMatrix(android.graphics.Canvas,%20android.graphics.Matrix,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.concat](https://developer.android.com/reference/android/graphics/Canvas.html#concat(android.graphics.Matrix)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withRotation(degrees: Float = 0.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withRotation(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.rotate](https://developer.android.com/reference/android/graphics/Canvas.html#rotate(float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withSave(block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withSave(android.graphics.Canvas,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save()) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withScale(x: Float = 1.0f, y: Float = 1.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withScale(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.scale](https://developer.android.com/reference/android/graphics/Canvas.html#scale(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withSkew(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withSkew(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.skew](https://developer.android.com/reference/android/graphics/Canvas.html#skew(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Canvas.withTranslation(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withTranslation(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.translate](https://developer.android.com/reference/android/graphics/Canvas.html#translate(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.html)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Color.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Color.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Color.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Color.component4()` Returns the fourth component of the color. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.html)! | `Color.convertTo(colorSpace: Named)` Converts the color receiver to a color in the specified color space. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.html)! | `Color.convertTo(colorSpace: ColorSpace)` Converts the color receiver to a color in the specified color space. |
| operator [Color](https://developer.android.com/reference/android/graphics/Color.html) | `Color.plus(c: Color)` Composites two translucent colors together. |

##### For [android.graphics.ImageDecoder.Source](https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html)

|  |  |
| --- | --- |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `Source.decodeBitmap(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Bitmap from a Source |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html) | `Source.decodeDrawable(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Drawable from a Source |

##### For [android.graphics.Matrix](https://developer.android.com/reference/android/graphics/Matrix.html)

|  |  |
| --- | --- |
| operator [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `Matrix.times(m: Matrix)` Multiplies this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) by another matrix and returns the result as a new matrix. |
| [FloatArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float-array/index.html) | `Matrix.values()` Returns the 9 values of this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) as a new array of floats. |

##### For [android.graphics.Paint](https://developer.android.com/reference/android/graphics/Paint.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Paint.setBlendMode(blendModeCompat: BlendModeCompat?)` Convenience method to configure the BlendMode of a Paint in a backward compatible way. |

##### For [android.graphics.Path](https://developer.android.com/reference/android/graphics/Path.html)

|  |  |
| --- | --- |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `Path.and(p: Path)` Returns the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)<[PathSegment](/reference/kotlin/androidx/core/graphics/PathSegment)> | `Path.flatten(error: Float = 0.5f)` Flattens (or approximate) the [Path](https://developer.android.com/reference/android/graphics/Path.html) with a series of line segments. |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.html) | `Path.minus(p: Path)` Returns the difference of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `Path.or(p: Path)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.html) | `Path.plus(p: Path)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `Path.xor(p: Path)` Returns the union minus the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |

##### For [android.graphics.Picture](https://developer.android.com/reference/android/graphics/Picture.html)

|  |  |
| --- | --- |
| [Picture](https://developer.android.com/reference/android/graphics/Picture.html) | `Picture.record(width: Int, height: Int, block: Canvas.() -> Unit)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.html) to record commands in this [Picture](https://developer.android.com/reference/android/graphics/Picture.html), executes the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$record(android.graphics.Picture,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) on the newly created canvas and returns this [Picture](https://developer.android.com/reference/android/graphics/Picture.html). |

##### For [android.graphics.Point](https://developer.android.com/reference/android/graphics/Point.html)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Point.component1()` Returns the x coordinate of this point. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Point.component2()` Returns the y coordinate of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `Point.minus(p: Point)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `Point.minus(xy: Int)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `Point.plus(p: Point)` Offsets this point by the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `Point.plus(xy: Int)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `Point.toPointF()` Returns a [PointF](https://developer.android.com/reference/android/graphics/PointF.html) representation of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `Point.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PointF](https://developer.android.com/reference/android/graphics/PointF.html)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `PointF.component1()` Returns the x coordinate of this point. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `PointF.component2()` Returns the y coordinate of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `PointF.minus(p: PointF)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `PointF.minus(xy: Float)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `PointF.plus(p: PointF)` Offsets this point by the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `PointF.plus(xy: Float)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [Point](https://developer.android.com/reference/android/graphics/Point.html) | `PointF.toPoint()` Returns a [Point](https://developer.android.com/reference/android/graphics/Point.html) representation of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `PointF.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html)

|  |  |
| --- | --- |
| [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.html) | `Mode.toColorFilter(color: Int)` Creates a new [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.html) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html) as the alpha compositing or blending mode, and the specified [color](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$toColorFilter(android.graphics.PorterDuff.Mode,%20kotlin.Int)/color). |
| [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.html) | `Mode.toXfermode()` Creates a new [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.html) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html) as the alpha compositing or blending mode. |

##### For [android.graphics.Rect](https://developer.android.com/reference/android/graphics/Rect.html)

|  |  |
| --- | --- |
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.and(r: Rect)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Rect.component1()` Returns "left", the first component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Rect.component2()` Returns "top", the second component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Rect.component3()` Returns "right", the third component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Rect.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Rect.contains(p: Point)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Rect.minus(r: Rect)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.minus(xy: Int)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.minus(xy: Point)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.or(r: Rect)` Returns the union of two rectangles as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.plus(r: Rect)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.plus(xy: Int)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.plus(xy: Point)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `Rect.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.Rect,%20kotlin.Int)/factor). |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `Rect.toRectF()` Returns a [RectF](https://developer.android.com/reference/android/graphics/RectF.html) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Rect.toRegion()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.html) representation of this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Rect.xor(r: Rect)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.RectF](https://developer.android.com/reference/android/graphics/RectF.html)

|  |  |
| --- | --- |
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.and(r: RectF)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `RectF.component1()` Returns "left", the first component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `RectF.component2()` Returns "top", the second component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `RectF.component3()` Returns "right", the third component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `RectF.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `RectF.contains(p: PointF)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `RectF.minus(r: RectF)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.minus(xy: Float)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.minus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.or(r: RectF)` Returns the union of two rectangles as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.plus(r: RectF)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.plus(xy: Float)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.plus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.RectF,%20kotlin.Int)/factor). |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.times(factor: Float)` Returns a new rectangle representing this rectangle's components each scaled by [factor](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.RectF,%20kotlin.Float)/factor). |
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `RectF.toRect()` Returns a [Rect](https://developer.android.com/reference/android/graphics/Rect.html) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.html) | `RectF.toRegion()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.html) representation of this rectangle. |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `RectF.transform(m: Matrix)` Transform this rectangle in place using the supplied [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) and returns this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `RectF.xor(r: RectF)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.Region](https://developer.android.com/reference/android/graphics/Region.html)

|  |  |
| --- | --- |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.and(r: Rect)` Return the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.and(r: Region)` Return the intersection of this region and the specified region as a new region. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Region.contains(p: Point)` Return true if the region contains the specified [Point](https://developer.android.com/reference/android/graphics/Point.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Region.forEach(action: (rect: Rect) -> Unit)` Performs the given action on each rect in this region. |
| operator [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)<[Rect](https://developer.android.com/reference/android/graphics/Rect.html)> | `Region.iterator()` Returns an [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html) over the rects in this region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.minus(r: Rect)` Return the difference of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.minus(r: Region)` Return the difference of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.not()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.or(r: Rect)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.or(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.plus(r: Rect)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.plus(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.unaryMinus()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.xor(r: Rect)` Return the union minus the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `Region.xor(r: Region)` Return the union minus the intersection of this region and the specified region as a new region. |

##### For [android.graphics.Shader](https://developer.android.com/reference/android/graphics/Shader.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Shader.transform(block: Matrix.() -> Unit)` Wrap the specified [block](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$transform(android.graphics.Shader,%20kotlin.Function1((android.graphics.Matrix,%20kotlin.Unit)))/block) in calls to [Shader.getLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.html#getLocalMatrix(android.graphics.Matrix)) and [Shader.setLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.html#setLocalMatrix(android.graphics.Matrix)). |

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.component1()` Return the alpha component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.component2()` Return the red component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.component3()` Return the green component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.component4()` Return the blue component of a color int. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `Int.convertTo(colorSpace: Named)` Converts the color int receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `Int.convertTo(colorSpace: ColorSpace)` Converts the color int receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.html) | `Int.toColor()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.html) instance from a color int. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `Int.toColorLong()` Converts the specified ARGB [color int](https://developer.android.com/reference/android/graphics/Color.html) to an RGBA [color long](https://developer.android.com/reference/android/graphics/Color.html) in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace/Named.html#SRGB) color space. |

##### For [kotlin.Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.component4()` Returns the fourth component of the color. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `Long.convertTo(colorSpace: Named)` Converts the color long receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `Long.convertTo(colorSpace: ColorSpace)` Converts the color long receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.html) | `Long.toColor()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.html) instance from a [color long](https://developer.android.com/reference/android/graphics/Color.html). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Long.toColorInt()` Converts the specified [color long](https://developer.android.com/reference/android/graphics/Color.html) to an ARGB [color int](https://developer.android.com/reference/android/graphics/Color.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `String.toColorInt()` Return a corresponding [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) color of this [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html). |

#### Extension properties

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.alpha()` Return the alpha component of a color int. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.blue()` Return the blue component of a color int. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.green()` Return the green component of a color int. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Int.luminance()` Returns the relative luminance of a color int, assuming sRGB encoding. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Int.red()` Return the red component of a color int. |

##### For [kotlin.Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)

|  |  |
| --- | --- |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.alpha()` Return the alpha component of a color long. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.blue()` Return the blue component of a color long. |
| [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace.html) | `Long.colorSpace()` Returns the color space encoded in the specified color long. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.green()` Return the green component of a color long. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Long.isSrgb()` Indicates whether the color is in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace/Named.html#SRGB) color space. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Long.isWideGamut()` Indicates whether the color is in a [wide-gamut](https://developer.android.com/reference/android/graphics/ColorSpace.html) color space. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.luminance()` Returns the relative luminance of a color. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `Long.red()` Return the red component of a color long. |

#### Top-level functions

|  |  |
| --- | --- |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888)` Returns a mutable bitmap with the specified [width](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)/width) and [height](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)/height). |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888, hasAlpha: Boolean = true, colorSpace: ColorSpace = ColorSpace.get(ColorSpace.Named.SRGB))` Returns a mutable bitmap with the specified [width](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace)/width) and [height](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace)/height). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `rotationMatrix(degrees: Float, px: Float = 0.0f, py: Float = 0.0f)` Creates a rotation matrix, defined by a rotation angle in degrees around the pivot point located at the coordinates ([px](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$rotationMatrix(kotlin.Float,%20kotlin.Float,%20kotlin.Float)/px), [py](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$rotationMatrix(kotlin.Float,%20kotlin.Float,%20kotlin.Float)/py)). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `scaleMatrix(sx: Float = 1.0f, sy: Float = 1.0f)` Creates a scale matrix with the scale factor [sx](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$scaleMatrix(kotlin.Float,%20kotlin.Float)/sx) and [sy](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$scaleMatrix(kotlin.Float,%20kotlin.Float)/sy) respectively on the `x` and `y` axis. |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `translationMatrix(tx: Float = 0.0f, ty: Float = 0.0f)` Creates a translation matrix with the translation amounts [tx](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$translationMatrix(kotlin.Float,%20kotlin.Float)/tx) and [ty](/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$translationMatrix(kotlin.Float,%20kotlin.Float)/ty) respectively on the `x` and `y` axis. |

## androidx.core.graphics.drawable

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)

|  |  |
| --- | --- |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `Bitmap.toAdaptiveIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this adaptive [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |
| [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.html) | `Bitmap.toDrawable(resources: Resources)` Create a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.html) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `Bitmap.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.html)

|  |  |
| --- | --- |
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) | `Color.toDrawable()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) from this [Color](https://developer.android.com/reference/android/graphics/Color.html) (via [Color.toArgb](https://developer.android.com/reference/android/graphics/Color.html#toArgb())). |

##### For [android.graphics.drawable.Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html)

|  |  |
| --- | --- |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `Drawable.toBitmap(@Px width: Int = intrinsicWidth, @Px height: Int = intrinsicHeight, config: Config? = null)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) representation of this [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Drawable.updateBounds(@Px left: Int = bounds.left, @Px top: Int = bounds.top, @Px right: Int = bounds.right, @Px bottom: Int = bounds.bottom)` Updates this drawable's bounds. |

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.html)

|  |  |
| --- | --- |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `Uri.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [Uri](https://developer.android.com/reference/android/net/Uri.html). |

##### For [kotlin.ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)

|  |  |
| --- | --- |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `ByteArray.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html). |

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|  |  |
| --- | --- |
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) | `Int.toDrawable()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) from this color value. |

## androidx.core.location

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.location.Location](https://developer.android.com/reference/android/location/Location.html)

|  |  |
| --- | --- |
| operator [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `Location.component1()` Returns the latitude of this [Location](https://developer.android.com/reference/android/location/Location.html). |
| operator [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `Location.component2()` Returns the longitude of this [Location](https://developer.android.com/reference/android/location/Location.html). |

## androidx.core.net

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.html)

|  |  |
| --- | --- |
| [File](https://developer.android.com/reference/java/io/File.html) | `Uri.toFile()` Creates a [File](https://developer.android.com/reference/java/io/File.html) from the given [Uri](https://developer.android.com/reference/android/net/Uri.html). |

##### For [java.io.File](https://developer.android.com/reference/java/io/File.html)

|  |  |
| --- | --- |
| [Uri](https://developer.android.com/reference/android/net/Uri.html) | `File.toUri()` Creates a Uri from the given file. |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|  |  |
| --- | --- |
| [Uri](https://developer.android.com/reference/android/net/Uri.html) | `String.toUri()` Creates a Uri from the given encoded URI string. |

## androidx.core.os

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.os.Handler](https://developer.android.com/reference/android/os/Handler.html)

|  |  |
| --- | --- |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `Handler.postAtTime(uptimeMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postAtTime](https://developer.android.com/reference/android/os/Handler.html#postAtTime(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `Handler.postDelayed(delayInMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postDelayed](https://developer.android.com/reference/android/os/Handler.html#postDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |

#### Top-level functions

|  |  |
| --- | --- |
| [Bundle](https://developer.android.com/reference/android/os/Bundle.html) | `bundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [Bundle](https://developer.android.com/reference/android/os/Bundle.html) with the given key/value pairs as elements. |
| [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.html) | `persistableBundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.html) with the given key/value pairs as elements. |
| T | `trace(sectionName: String, block: () -> T)` Wrap the specified [block](/reference/kotlin/androidx/core/os/package-summary#androidx.core.os$trace(kotlin.String,%20kotlin.Function0((androidx.core.os.trace.T)))/block) in calls to [Trace.beginSection](https://developer.android.com/reference/android/os/Trace.html#beginSection(java.lang.String)) (with the supplied [sectionName](/reference/kotlin/androidx/core/os/package-summary#androidx.core.os$trace(kotlin.String,%20kotlin.Function0((androidx.core.os.trace.T)))/sectionName)) and [Trace.endSection](https://developer.android.com/reference/android/os/Trace.html#endSection()). |

## androidx.core.text

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.text.Spannable](https://developer.android.com/reference/android/text/Spannable.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Spannable.clearSpans()` Clear all spans from this text. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Spannable.set(start: Int, end: Int, span: Any)` Add [span](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/span) to the range [start](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/start)&hellip;[end](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/end) of the text. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Spannable.set(range: IntRange, span: Any)` Add [span](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.ranges.IntRange,%20kotlin.Any)/span) to the [range](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.ranges.IntRange,%20kotlin.Any)/range) of the text. |

##### For [android.text.SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html)

|  |  |
| --- | --- |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.backgroundColor(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$backgroundColor(android.text.SpannableStringBuilder,%20kotlin.Int,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [BackgroundColorSpan](https://developer.android.com/reference/android/text/style/BackgroundColorSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.bold(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$bold(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a bold [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.color(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$color(android.text.SpannableStringBuilder,%20kotlin.Int,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [ForegroundColorSpan](https://developer.android.com/reference/android/text/style/ForegroundColorSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.inSpans(vararg spans: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Array((kotlin.Any)),%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in [spans](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Array((kotlin.Any)),%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/spans). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.inSpans(span: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Any,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in [span](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Any,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/span). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.italic(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$italic(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in an italic [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.scale(proportion: Float, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$scale(android.text.SpannableStringBuilder,%20kotlin.Float,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [RelativeSizeSpan](https://developer.android.com/reference/android/text/style/RelativeSizeSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.strikeThrough(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$strikeThrough(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [StrikethroughSpan](https://developer.android.com/reference/android/text/style/StrikethroughSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.subscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$subscript(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [SubscriptSpan](https://developer.android.com/reference/android/text/style/SubscriptSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.superscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$superscript(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [SuperscriptSpan](https://developer.android.com/reference/android/text/style/SuperscriptSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `SpannableStringBuilder.underline(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$underline(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in an [UnderlineSpan](https://developer.android.com/reference/android/text/style/UnderlineSpan.html). |

##### For [android.text.Spanned](https://developer.android.com/reference/android/text/Spanned.html)

|  |  |
| --- | --- |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<out T> | `Spanned.getSpans(start: Int = 0, end: Int = length)` Get all spans that are instance of T. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `Spanned.toHtml(option: Int = TO_HTML_PARAGRAPH_LINES_CONSECUTIVE)` Returns a string of HTML from the spans in this [Spanned](https://developer.android.com/reference/android/text/Spanned.html). |

##### For [kotlin.CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `CharSequence.isDigitsOnly()` Returns whether the given [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) contains only digits. |
| [Spannable](https://developer.android.com/reference/android/text/Spannable.html) | `CharSequence.toSpannable()` Returns a new [Spannable](https://developer.android.com/reference/android/text/Spannable.html) from [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html), or the source itself if it is already an instance of [SpannableString](https://developer.android.com/reference/android/text/SpannableString.html). |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.html) | `CharSequence.toSpanned()` Returns a new [Spanned](https://developer.android.com/reference/android/text/Spanned.html) from [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html), or the source itself if it is already an instance of [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `CharSequence.trimmedLength()` Returns the length that the specified [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) would have if spaces and ASCII control characters were trimmed from the start and end, as by [String.trim](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/trim.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|  |  |
| --- | --- |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `String.htmlEncode()` Html-encode the string. |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.html) | `String.parseAsHtml(flags: Int = FROM_HTML_MODE_LEGACY, imageGetter: ImageGetter? = null, tagHandler: TagHandler? = null)` Returns a [Spanned](https://developer.android.com/reference/android/text/Spanned.html) from parsing this string as HTML. |

#### Extension properties

##### For [java.util.Locale](https://developer.android.com/reference/java/util/Locale.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Locale.layoutDirection()` Returns layout direction for a given locale. |

#### Top-level functions

|  |  |
| --- | --- |
| [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html) | `buildSpannedString(builderAction: SpannableStringBuilder.() -> Unit)` Builds new string by populating a newly created [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) using the provided [builderAction](/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$buildSpannedString(kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) and then converting it to [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html). |

## androidx.core.transition

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)

|  |  |
| --- | --- |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.addListener(crossinline onEnd: (transition: Transition) -> Unit = {}, crossinline onStart: (transition: Transition) -> Unit = {}, crossinline onCancel: (transition: Transition) -> Unit = {}, crossinline onResume: (transition: Transition) -> Unit = {}, crossinline onPause: (transition: Transition) -> Unit = {})` Add a listener to this Transition using the provided actions. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.doOnCancel(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been cancelled. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.doOnEnd(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has ended. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.doOnPause(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been paused. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.doOnResume(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has resumed after a pause. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `Transition.doOnStart(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has started. |

## androidx.core.util

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.util.AtomicFile](https://developer.android.com/reference/android/util/AtomicFile.html)

|  |  |
| --- | --- |
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | `AtomicFile.readBytes()` Gets the entire content of this file as a byte array. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `AtomicFile.readText(charset: Charset = Charsets.UTF_8)` Gets the entire content of this file as a String using UTF-8 or specified [charset](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$readText(android.util.AtomicFile,%20java.nio.charset.Charset)/charset). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AtomicFile.tryWrite(block: (out: FileOutputStream) -> Unit)` Perform the write operations inside [block](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$tryWrite(android.util.AtomicFile,%20kotlin.Function1((java.io.FileOutputStream,%20kotlin.Unit)))/block) on this file. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AtomicFile.writeBytes(array: ByteArray)` Sets the content of this file as an [array](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeBytes(android.util.AtomicFile,%20kotlin.ByteArray)/array) of bytes. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AtomicFile.writeText(text: String, charset: Charset = Charsets.UTF_8)` Sets the content of this file as [text](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeText(android.util.AtomicFile,%20kotlin.String,%20java.nio.charset.Charset)/text) encoded using UTF-8 or specified [charset](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeText(android.util.AtomicFile,%20kotlin.String,%20java.nio.charset.Charset)/charset). |

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.LongSparseArray((androidx.core.util.contains.T)),%20kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.containsKey(key: Long)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.LongSparseArray((androidx.core.util.containsKey.T)),%20kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.LongSparseArray((androidx.core.util.containsValue.T)),%20androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.LongSparseArray((androidx.core.util.forEach.T)),%20kotlin.Function2((kotlin.Long,%20androidx.core.util.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Long,%20androidx.core.util.getOrDefault.T)/key), or [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Long,%20androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)<T> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.LongSparseArray((androidx.core.util.plus.T)),%20android.util.LongSparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `LongSparseArray<T>.putAll(other: LongSparseArray<T>)` Update this collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.LongSparseArray((androidx.core.util.putAll.T)),%20android.util.LongSparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)),%20kotlin.Long,%20androidx.core.util.remove.T)/key) only if it is mapped to [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)),%20kotlin.Long,%20androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)<T> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.Pair](https://developer.android.com/reference/android/util/Pair.html)

|  |  |
| --- | --- |
| operator F | `Pair<F, S>.component1()` Returns the first component of the pair. |
| operator S | `Pair<F, S>.component2()` Returns the second component of the pair. |
| [Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)<F, S> | `Pair<F, S>.toKotlinPair()` Returns this [Pair](https://developer.android.com/reference/android/util/Pair.html) as a [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html). |

##### For [android.util.Range](https://developer.android.com/reference/android/util/Range.html)

|  |  |
| --- | --- |
| infix [Range](https://developer.android.com/reference/android/util/Range.html)<T> | `Range<T>.and(other: Range<T>)` Return the intersection of this range and [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$and(android.util.Range((androidx.core.util.and.T)),%20android.util.Range((androidx.core.util.and.T)))/other). |
| operator [Range](https://developer.android.com/reference/android/util/Range.html)<T> | `Range<T>.plus(value: T)` Return the smallest range that includes this and [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)),%20androidx.core.util.plus.T)/value). |
| operator [Range](https://developer.android.com/reference/android/util/Range.html)<T> | `Range<T>.plus(other: Range<T>)` Return the smallest range that includes this and [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)),%20android.util.Range((androidx.core.util.plus.T)))/other). |
| [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html)<T> | `Range<T>.toClosedRange()` Returns this [Range](https://developer.android.com/reference/android/util/Range.html) as a [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html). |

##### For [android.util.Size](https://developer.android.com/reference/android/util/Size.html)

|  |  |
| --- | --- |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Size.component1()` Returns "width", the first component of this [Size](https://developer.android.com/reference/android/util/Size.html). |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Size.component2()` Returns "height", the second component of this [Size](https://developer.android.com/reference/android/util/Size.html). |

##### For [android.util.SizeF](https://developer.android.com/reference/android/util/SizeF.html)

|  |  |
| --- | --- |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `SizeF.component1()` Returns "width", the first component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.html). |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `SizeF.component2()` Returns "height", the second component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.html). |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.contains(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseArray((androidx.core.util.contains.T)),%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.containsKey(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseArray((androidx.core.util.containsKey.T)),%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseArray((androidx.core.util.containsValue.T)),%20androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseArray<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseArray((androidx.core.util.forEach.T)),%20kotlin.Function2((kotlin.Int,%20androidx.core.util.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArray<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Int,%20androidx.core.util.getOrDefault.T)/key), or [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Int,%20androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArray<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)<T> | `SparseArray<T>.plus(other: SparseArray<T>)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseArray((androidx.core.util.plus.T)),%20android.util.SparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseArray<T>.putAll(other: SparseArray<T>)` Update this collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseArray((androidx.core.util.putAll.T)),%20android.util.SparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseArray<T>.remove(key: Int, value: T)` Removes the entry for [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)),%20kotlin.Int,%20androidx.core.util.remove.T)/key) only if it is mapped to [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)),%20kotlin.Int,%20androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseArray<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)<T> | `SparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.contains(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseBooleanArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.containsKey(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseBooleanArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.containsValue(value: Boolean)` Returns true if the collection contains [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseBooleanArray,%20kotlin.Boolean)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseBooleanArray.forEach(action: (key: Int, value: Boolean) -> Unit)` Performs the given [action](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseBooleanArray,%20kotlin.Function2((kotlin.Int,%20kotlin.Boolean,%20kotlin.Unit)))/action) for each key/value entry. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.getOrDefault(key: Int, defaultValue: Boolean)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/key), or [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.getOrElse(key: Int, defaultValue: () -> Boolean)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Boolean)))/key), or from [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Boolean)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseBooleanArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html) | `SparseBooleanArray.plus(other: SparseBooleanArray)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseBooleanArray,%20android.util.SparseBooleanArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseBooleanArray.putAll(other: SparseBooleanArray)` Update this collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseBooleanArray,%20android.util.SparseBooleanArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseBooleanArray.remove(key: Int, value: Boolean)` Removes the entry for [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/key) only if it is mapped to [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseBooleanArray.set(key: Int, value: Boolean)` Allows the use of the index operator for storing values in the collection. |
| [BooleanIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-boolean-iterator/index.html) | `SparseBooleanArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.contains(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseIntArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.containsKey(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseIntArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.containsValue(value: Int)` Returns true if the collection contains [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseIntArray,%20kotlin.Int)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseIntArray.forEach(action: (key: Int, value: Int) -> Unit)` Performs the given [action](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseIntArray,%20kotlin.Function2((kotlin.Int,%20,%20kotlin.Unit)))/action) for each key/value entry. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseIntArray.getOrDefault(key: Int, defaultValue: Int)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/key), or [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/defaultValue) when not present. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseIntArray.getOrElse(key: Int, defaultValue: () -> Int)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Int)))/key), or from [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Int)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseIntArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html) | `SparseIntArray.plus(other: SparseIntArray)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseIntArray,%20android.util.SparseIntArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseIntArray.putAll(other: SparseIntArray)` Update this collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseIntArray,%20android.util.SparseIntArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseIntArray.remove(key: Int, value: Int)` Removes the entry for [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/key) only if it is mapped to [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseIntArray.set(key: Int, value: Int)` Allows the use of the index operator for storing values in the collection. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseIntArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.contains(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseLongArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.containsKey(key: Int)` Returns true if the collection contains [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseLongArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.containsValue(value: Long)` Returns true if the collection contains [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseLongArray,%20kotlin.Long)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseLongArray.forEach(action: (key: Int, value: Long) -> Unit)` Performs the given [action](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseLongArray,%20kotlin.Function2((kotlin.Int,%20kotlin.Long,%20kotlin.Unit)))/action) for each key/value entry. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `SparseLongArray.getOrDefault(key: Int, defaultValue: Long)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/key), or [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/defaultValue) when not present. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `SparseLongArray.getOrElse(key: Int, defaultValue: () -> Long)` Return the value corresponding to [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Long)))/key), or from [defaultValue](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Long)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `SparseLongArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html) | `SparseLongArray.plus(other: SparseLongArray)` Creates a new collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseLongArray,%20android.util.SparseLongArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseLongArray.putAll(other: SparseLongArray)` Update this collection by adding or replacing entries from [other](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseLongArray,%20android.util.SparseLongArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SparseLongArray.remove(key: Int, value: Long)` Removes the entry for [key](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/key) only if it is set to [value](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SparseLongArray.set(key: Int, value: Long)` Allows the use of the index operator for storing values in the collection. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `SparseLongArray.valueIterator()` Return an iterator over the collection's values. |

##### For [kotlin.Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)

|  |  |
| --- | --- |
| [Half](https://developer.android.com/reference/android/util/Half.html) | `Double.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html). |

##### For [kotlin.Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)

|  |  |
| --- | --- |
| [Half](https://developer.android.com/reference/android/util/Half.html) | `Float.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html). |

##### For [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)

|  |  |
| --- | --- |
| [Pair](https://developer.android.com/reference/android/util/Pair.html)<F, S> | `Pair<F, S>.toAndroidPair()` Returns this [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html) as an Android [Pair](https://developer.android.com/reference/android/util/Pair.html). |

##### For [kotlin.Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html)

|  |  |
| --- | --- |
| [Half](https://developer.android.com/reference/android/util/Half.html) | `Short.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|  |  |
| --- | --- |
| [Half](https://developer.android.com/reference/android/util/Half.html) | `String.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html). |

##### For [kotlin.ranges.ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html)

|  |  |
| --- | --- |
| [Range](https://developer.android.com/reference/android/util/Range.html)<T> | `ClosedRange<T>.toRange()` Returns this [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html) as a [Range](https://developer.android.com/reference/android/util/Range.html). |

#### Extension properties

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseBooleanArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseIntArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SparseLongArray.size()` Returns the number of key/value entries in the collection. |

#### Top-level functions

|  |  |
| --- | --- |
| [LruCache](https://developer.android.com/reference/android/util/LruCache.html)<K, V> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/android/util/LruCache.html) with the given parameters. |
| infix [Range](https://developer.android.com/reference/android/util/Range.html)<T> | `T.rangeTo(that: T)` Creates a range from this [Comparable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparable/index.html) value to [that](/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$rangeTo(androidx.core.util.rangeTo.T,%20androidx.core.util.rangeTo.T)/that). |

## androidx.core.view

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Menu.contains(item: MenuItem)` Returns `true` if [item](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$contains(android.view.Menu,%20android.view.MenuItem)/item) is found in this menu. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Menu.forEach(action: (item: MenuItem) -> Unit)` Performs the given action on each item in this menu. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Menu.forEachIndexed(action: (index: Int, item: MenuItem) -> Unit)` Performs the given action on each item in this menu, providing its sequential index. |
| operator [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html) | `Menu.get(index: Int)` Returns the menu at [index](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$get(android.view.Menu,%20kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Menu.isEmpty()` Returns true if this menu contains no items. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Menu.isNotEmpty()` Returns true if this menu contains one or more items. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)> | `Menu.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the items in this menu. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Menu.minusAssign(item: MenuItem)` Removes [item](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$minusAssign(android.view.Menu,%20android.view.MenuItem)/item) from this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.doOnAttach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is attached to a window. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.doOnDetach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is detached from a window. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.doOnLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is laid out. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.doOnNextLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is next laid out. |
| [OneShotPreDrawListener](/reference/kotlin/androidx/core/view/OneShotPreDrawListener) | `View.doOnPreDraw(crossinline action: (view: View) -> Unit)` Performs the given action when the view tree is about to be drawn. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `View.drawToBitmap(config: Config = Bitmap.Config.ARGB_8888)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) representation of this [View](https://developer.android.com/reference/android/view/View.html). |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `View.postDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postDelayed](https://developer.android.com/reference/android/view/View.html#postDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `View.postOnAnimationDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postOnAnimationDelayed](https://developer.android.com/reference/android/view/View.html#postOnAnimationDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.setPadding(@Px size: Int)` Sets the view's padding. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.updateLayoutParams(block: LayoutParams.() -> Unit)` Executes [block](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$updateLayoutParams(android.view.View,%20kotlin.Function1((android.view.ViewGroup.LayoutParams,%20kotlin.Unit)))/block) with the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.updateLayoutParams(block: T.() -> Unit)` Executes [block](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$updateLayoutParams(android.view.View,%20kotlin.Function1((androidx.core.view.updateLayoutParams.T,%20kotlin.Unit)))/block) with a typed version of the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.updatePadding(@Px left: Int = paddingLeft, @Px top: Int = paddingTop, @Px right: Int = paddingRight, @Px bottom: Int = paddingBottom)` Updates this view's padding. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `View.updatePaddingRelative(@Px start: Int = paddingStart, @Px top: Int = paddingTop, @Px end: Int = paddingEnd, @Px bottom: Int = paddingBottom)` Updates this view's relative padding. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `ViewGroup.contains(view: View)` Returns `true` if [view](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$contains(android.view.ViewGroup,%20android.view.View)/view) is found in this view group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `ViewGroup.forEach(action: (view: View) -> Unit)` Performs the given action on each view in this view group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `ViewGroup.forEachIndexed(action: (index: Int, view: View) -> Unit)` Performs the given action on each view in this view group, providing its sequential index. |
| operator [View](https://developer.android.com/reference/android/view/View.html) | `ViewGroup.get(index: Int)` Returns the view at [index](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$get(android.view.ViewGroup,%20kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `ViewGroup.isEmpty()` Returns true if this view group contains no views. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `ViewGroup.isNotEmpty()` Returns true if this view group contains one or more views. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)<[View](https://developer.android.com/reference/android/view/View.html)> | `ViewGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the views in this view group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `ViewGroup.minusAssign(view: View)` Removes [view](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$minusAssign(android.view.ViewGroup,%20android.view.View)/view) from this view group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `ViewGroup.plusAssign(view: View)` Adds [view](/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$plusAssign(android.view.ViewGroup,%20android.view.View)/view) to this view group. |

##### For [android.view.ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `MarginLayoutParams.setMargins(@Px size: Int)` Sets the margins in the ViewGroup's MarginLayoutParams. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `MarginLayoutParams.updateMargins(@Px left: Int = leftMargin, @Px top: Int = topMargin, @Px right: Int = rightMargin, @Px bottom: Int = bottomMargin)` Updates the margins in the [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)'s [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `MarginLayoutParams.updateMarginsRelative(@Px start: Int = marginStart, @Px top: Int = topMargin, @Px end: Int = marginEnd, @Px bottom: Int = bottomMargin)` Updates the relative margins in the ViewGroup's MarginLayoutParams. |

#### Extension properties

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.html)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)> | `Menu.children()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the items in this menu. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `Menu.size()` Returns the number of items in this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `View.isGone()` Returns true when this view's visibility is [View.GONE](https://developer.android.com/reference/android/view/View.html#GONE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `View.isInvisible()` Returns true when this view's visibility is [View.INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `View.isVisible()` Returns true when this view's visibility is [View.VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE), false otherwise. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginBottom()` Returns the bottom margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginEnd()` Returns the end margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginLeft()` Returns the left margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginRight()` Returns the right margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginStart()` Returns the start margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `View.marginTop()` Returns the top margin if this view's [LayoutParams](/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)<[View](https://developer.android.com/reference/android/view/View.html)> | `ViewGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the child views in this view group. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `ViewGroup.size()` Returns the number of views in this view group. |

## androidx.core.widget

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.core:core-ktx:1.18.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-ktx:1.18.0")
}
```

#### Extension functions

##### For [android.widget.TextView](https://developer.android.com/reference/android/widget/TextView.html)

|  |  |
| --- | --- |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `TextView.addTextChangedListener(crossinline beforeTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline onTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline afterTextChanged: (text: Editable?) -> Unit = {})` Add a text changed listener to this TextView using the provided actions |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `TextView.doAfterTextChanged(crossinline action: (text: Editable?) -> Unit)` Add an action which will be invoked after the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `TextView.doBeforeTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked before the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `TextView.doOnTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked when the text is changing. |

## androidx.dynamicanimation.animation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.dynamicanimation:dynamicanimation-ktx:"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.dynamicanimation:dynamicanimation-ktx:")
}
```

#### Extension functions

##### For [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation)

|  |  |
| --- | --- |
| [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `SpringAnimation.withSpringForceProperties(func: SpringForce.() -> Unit)` Updates or applies spring force properties like [SpringForce.mDampingRatio](/reference/kotlin/androidx/dynamicanimation/animation), [SpringForce.mFinalPosition](/reference/kotlin/androidx/dynamicanimation/animation) and stiffness on SpringAnimation. |

#### Top-level functions

|  |  |
| --- | --- |
| [FlingAnimation](/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) | `flingAnimationOf(setter: (Float) -> Unit, getter: () -> Float)` Creates [FlingAnimation](/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) for a property that can be accessed via the provided setter and getter. |
| [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `springAnimationOf(setter: (Float) -> Unit, getter: () -> Float, finalPosition: Float = Float.NaN)` Creates [SpringAnimation](/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) for a property that can be accessed via the provided setter and getter. |

## androidx.fragment.app

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.fragment:fragment-ktx:1.8.9"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.fragment:fragment-ktx:1.8.9")
}
```

#### Extension functions

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|  |  |
| --- | --- |
| F | `View.findFragment()` Find a [Fragment](/reference/kotlin/androidx/fragment/app/Fragment) associated with a [View](https://developer.android.com/reference/android/view/View.html). |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)<VM> | `Fragment.activityViewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access parent activity's [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel), if [factoryProducer](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$activityViewModels(androidx.fragment.app.Fragment,%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) first time. |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)<VM> | `Fragment.createViewModelLazy(viewModelClass: KClass<VM>, storeProducer: () -> ViewModelStore, factoryProducer: () -> ViewModelProvider.Factory = null)` Helper method for creation of [ViewModelLazy](/reference/kotlin/androidx/lifecycle/ViewModelLazy), that resolves `null` passed as [factoryProducer](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$createViewModelLazy(androidx.fragment.app.Fragment,%20kotlin.reflect.KClass((androidx.fragment.app.createViewModelLazy.VM)),%20kotlin.Function0((androidx.lifecycle.ViewModelStore)),%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) to default factory. |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)<VM> | `Fragment.viewModels(noinline ownerProducer: () -> ViewModelStoreOwner = { this }, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) by **default** scoped to this [Fragment](/reference/kotlin/androidx/fragment/app/Fragment): |

##### For [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction)

|  |  |
| --- | --- |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.add(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager), inflating the Fragment's view into the container view specified by [containerViewId](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$add(androidx.fragment.app.FragmentTransaction,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle)/containerViewId), to later retrieve via [FragmentManager.findFragmentById](/reference/kotlin/androidx/fragment/app/FragmentManager#findFragmentById(kotlin.Int)). |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.add(tag: String, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager) without adding the Fragment to any container view. |
| [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `FragmentTransaction.replace(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Replace an existing fragment that was added to a container. |

##### For [FragmentManager](/reference/kotlin/androidx/fragment/app/FragmentManager)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `FragmentManager.commit(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$commit(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `FragmentManager.commitNow(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$commitNow(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `FragmentManager.transaction(now: Boolean = false, allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$transaction(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |

## androidx.fragment.app.testing

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.fragment:fragment-testing:1.8.9"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.fragment:fragment-testing:1.8.9")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using given [FragmentFactory](/reference/kotlin/androidx/fragment/app/FragmentFactory) and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](/reference/kotlin/androidx/fragment/app/testing/package-summary#androidx.fragment.app.testing$launchFragment(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0((androidx.fragment.app.testing.launchFragment.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) and waits for it to reach a resumed state. |
| [FragmentScenario](/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)<F!> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](/reference/kotlin/androidx/fragment/app/testing/package-summary#androidx.fragment.app.testing$launchFragmentInContainer(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0((androidx.fragment.app.testing.launchFragmentInContainer.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |

## androidx.lifecycle

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-core-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.10.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.lifecycle:lifecycle-livedata-core-ktx:2.10.0")
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.10.0")
    implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:2.10.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.10.0")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.10.0")
}
```

#### Extension functions

##### For [kotlinx.coroutines.flow.Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT)` Creates a LiveData that has values collected from the origin [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration)` Creates a LiveData that has values collected from the origin [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |

##### For [org.reactivestreams.Publisher](/reference/kotlin/androidx/lifecycle)

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `Publisher<T>.toLiveData()` Creates an observable [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) stream from a ReactiveStreams [Publisher](/reference/kotlin/androidx/lifecycle). |

##### For [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)

|  |  |
| --- | --- |
| [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<T> | `LiveData<T>.asFlow()` Creates a [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) containing values dispatched by originating [LiveData](/reference/kotlin/androidx/lifecycle/LiveData): at the start a flow collector receives the latest value held by LiveData and then observes LiveData updates. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<X> | `LiveData<X>.distinctUntilChanged()` Creates a new [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) object does not emit a value until the source `this` LiveData value has been changed. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<Y> | `LiveData<X>.map(crossinline transform: (X) -> Y)` Returns a [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) mapped from `this` LiveData by applying [transform](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$map(androidx.lifecycle.LiveData((androidx.lifecycle.map.X)),%20kotlin.Function1((androidx.lifecycle.map.X,%20androidx.lifecycle.map.Y)))/transform) to each value set on `this` LiveData. |
| [Observer](/reference/kotlin/androidx/lifecycle/Observer)<T> | `LiveData<T>.observe(owner: LifecycleOwner, crossinline onChanged: (T) -> Unit)` Adds the given [onChanged](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)),%20androidx.lifecycle.LifecycleOwner,%20kotlin.Function1((androidx.lifecycle.observe.T,%20kotlin.Unit)))/onChanged) lambda as an observer within the lifespan of the given [owner](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)),%20androidx.lifecycle.LifecycleOwner,%20kotlin.Function1((androidx.lifecycle.observe.T,%20kotlin.Unit)))/owner) and returns a reference to observer. |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<Y> | `LiveData<X>.switchMap(crossinline transform: (X) -> LiveData<Y>)` Returns a [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) mapped from the input `this` `LiveData` by applying [transform](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$switchMap(androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.X)),%20kotlin.Function1((androidx.lifecycle.switchMap.X,%20androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.Y)))))/transform) to each value set on `this`. |
| Publisher<T> | `LiveData<T>.toPublisher(lifecycle: LifecycleOwner)` Adapts the given [LiveData](/reference/kotlin/androidx/lifecycle/LiveData) stream to a ReactiveStreams [Publisher](/reference/kotlin/androidx/lifecycle). |

##### For [ViewModelProvider](/reference/kotlin/androidx/lifecycle/ViewModelProvider)

|  |  |
| --- | --- |
| VM | `ViewModelProvider.get()` Returns an existing ViewModel or creates a new one in the scope (usually, a fragment or an activity), associated with this `ViewModelProvider`. |

##### For [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|  |  |
| --- | --- |
| suspend T | `LifecycleOwner.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:CREATED) state. |
| suspend T | `LifecycleOwner.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:RESUMED) state. |
| suspend T | `LifecycleOwner.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:STARTED) state. |

##### For [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)

|  |  |
| --- | --- |
| suspend T | `Lifecycle.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:CREATED) state. |
| suspend T | `Lifecycle.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:RESUMED) state. |
| suspend T | `Lifecycle.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:STARTED) state. |
| suspend T | `Lifecycle.whenStateAtLeast(minState: Lifecycle.State, block: suspend CoroutineScope.() -> T)` Runs the given [block](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/block) on a [CoroutineDispatcher](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/index.html) that executes the [block](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/block) on the main thread and suspends the execution unless the [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)'s state is at least [minState](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/minState). |

#### Extension properties

##### For [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle)

|  |  |
| --- | --- |
| [LifecycleCoroutineScope](/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `Lifecycle.coroutineScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|  |  |
| --- | --- |
| [LifecycleCoroutineScope](/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `LifecycleOwner.lifecycleScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [LifecycleOwner](/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel)

|  |  |
| --- | --- |
| [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) | `ViewModel.viewModelScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel). |

#### Top-level functions

|  |  |
| --- | --- |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext,%20kotlin.Long,%20kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)),%20kotlin.Unit)))/block) that executes on a [LiveDataScope](/reference/kotlin/androidx/lifecycle/LiveDataScope). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<T> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext,%20java.time.Duration,%20kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)),%20kotlin.Unit)))/block) that executes on a [LiveDataScope](/reference/kotlin/androidx/lifecycle/LiveDataScope). |

## androidx.navigation

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-runtime-ktx:2.9.7"
    implementation "androidx.navigation:navigation-fragment-ktx:2.9.7"
    implementation "androidx.navigation:navigation-ui-ktx:2.9.7"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-runtime-ktx:2.9.7")
    implementation("androidx.navigation:navigation-fragment-ktx:2.9.7")
    implementation("androidx.navigation:navigation-ui-ktx:2.9.7")
}
```

#### Extension functions

##### For [android.app.Activity](https://developer.android.com/reference/android/app/Activity.html)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `Activity.findNavController(@IdRes viewId: Int)` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) given the id of a View and its containing [Activity](https://developer.android.com/reference/android/app/Activity.html). |
| [NavArgsLazy](/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> | `Activity.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the Activity's extras as an Args instance. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `View.findNavController()` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) associated with a [View](https://developer.android.com/reference/android/view/View.html). |

##### For [NavGraphBuilder](/reference/kotlin/androidx/navigation/NavGraphBuilder)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.activity(@IdRes id: Int, builder: ActivityNavigatorDestinationBuilder.() -> Unit)` Construct a new [ActivityNavigator.Destination](/reference/kotlin/androidx/navigation/ActivityNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.navigation(@IdRes id: Int, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a nested [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavGraph](/reference/kotlin/androidx/navigation/NavGraph)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `NavGraph.contains(@IdRes id: Int)` Returns `true` if a destination with `id` is found in this navigation graph. |
| operator [NavDestination](/reference/kotlin/androidx/navigation/NavDestination) | `NavGraph.get(@IdRes id: Int)` Returns the destination with `id`. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraph.minusAssign(node: NavDestination)` Removes `node` from this navigation graph. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraph.plusAssign(node: NavDestination)` Adds a destination to this NavGraph. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraph.plusAssign(other: NavGraph)` Add all destinations from another collection to this one. |

##### For [NavController](/reference/kotlin/androidx/navigation/NavController)

|  |  |
| --- | --- |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavController.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavHost](/reference/kotlin/androidx/navigation/NavHost)

|  |  |
| --- | --- |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavHost.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavigatorProvider](/reference/kotlin/androidx/navigation/NavigatorProvider)

|  |  |
| --- | --- |
| operator T | `NavigatorProvider.get(name: String)` Retrieves a registered [Navigator](/reference/kotlin/androidx/navigation/Navigator) by name. |
| operator T | `NavigatorProvider.get(clazz: KClass<T>)` Retrieves a registered [Navigator](/reference/kotlin/androidx/navigation/Navigator) using the name provided by the [Navigator.Name annotation](/reference/kotlin/androidx/navigation/Navigator.Name). |
| [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) | `NavigatorProvider.navigation(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](/reference/kotlin/androidx/navigation/NavGraph) |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavigatorProvider.plusAssign(navigator: Navigator<out NavDestination>)` Register a navigator using the name provided by the [Navigator.Name annotation](/reference/kotlin/androidx/navigation/Navigator.Name). |
| operator [Navigator](/reference/kotlin/androidx/navigation/Navigator)<out [NavDestination](/reference/kotlin/androidx/navigation/NavDestination)!>? | `NavigatorProvider.set(name: String, navigator: Navigator<out NavDestination>)` Register a [Navigator](/reference/kotlin/androidx/navigation/Navigator) by name. |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)<VM> | `Fragment.navGraphViewModels(@IdRes navGraphId: Int, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access a [ViewModel](/reference/kotlin/androidx/lifecycle/ViewModel) scoped to a navigation graph present on the {@link NavController} back stack: |

#### Top-level functions

|  |  |
| --- | --- |
| [ActivityNavigator.Extras](/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) | `ActivityNavigatorExtras(activityOptions: ActivityOptionsCompat? = null, flags: Int = 0)` Create a new [ActivityNavigator.Extras](/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) instance with a specific [ActivityOptionsCompat](/reference/kotlin/androidx/core/app/ActivityOptionsCompat) instance and/or any `Intent.FLAG_ACTIVITY_` flags. |
| [NavOptions](/reference/kotlin/androidx/navigation/NavOptions) | `navOptions(optionsBuilder: NavOptionsBuilder.() -> Unit)` Construct a new [NavOptions](/reference/kotlin/androidx/navigation/NavOptions) |

## androidx.navigation.fragment

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-fragment-ktx:2.9.7"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-fragment-ktx:2.9.7")
}
```

#### Extension functions

##### For [NavGraphBuilder](/reference/kotlin/androidx/navigation/NavGraphBuilder)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.dialog(@IdRes id: Int)` Construct a new [DialogFragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.dialog(@IdRes id: Int, builder: DialogFragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [DialogFragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.fragment(@IdRes id: Int)` Construct a new [FragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavGraphBuilder.fragment(@IdRes id: Int, builder: FragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [FragmentNavigator.Destination](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |

##### For [Fragment](/reference/kotlin/androidx/fragment/app/Fragment)

|  |  |
| --- | --- |
| [NavController](/reference/kotlin/androidx/navigation/NavController) | `Fragment.findNavController()` Find a [NavController](/reference/kotlin/androidx/navigation/NavController) given a [Fragment](/reference/kotlin/androidx/fragment/app/Fragment) |
| [NavArgsLazy](/reference/kotlin/androidx/navigation/NavArgsLazy)<Args> | `Fragment.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the Fragment's arguments as an Args instance. |

#### Top-level functions

|  |  |
| --- | --- |
| [FragmentNavigator.Extras](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) | `FragmentNavigatorExtras(vararg sharedElements: Pair<View, String>)` Create a new [FragmentNavigator.Extras](/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) instance with the given shared elements |

## androidx.navigation.ui

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.navigation:navigation-ui-ktx:2.9.7"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.navigation:navigation-ui-ktx:2.9.7")
}
```

#### Extension functions

##### For [android.view.MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `MenuItem.onNavDestinationSelected(navController: NavController)` Attempt to navigate to the [NavDestination](/reference/kotlin/androidx/navigation/ui) associated with this [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html). |

##### For [androidx.appcompat.app.AppCompatActivity](/reference/kotlin/androidx/navigation/ui)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [androidx.appcompat.widget.Toolbar](/reference/kotlin/androidx/navigation/ui)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Toolbar.setupWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `Toolbar.setupWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.appbar.CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui) and [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui) and [Toolbar](/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.bottomnavigation.BottomNavigationView](/reference/kotlin/androidx/navigation/ui)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `BottomNavigationView.setupWithNavController(navController: NavController)` Sets up a [BottomNavigationView](/reference/kotlin/androidx/navigation/ui) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.navigation.NavigationView](/reference/kotlin/androidx/navigation/ui)

|  |  |
| --- | --- |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavigationView.setupWithNavController(navController: NavController)` Sets up a [NavigationView](/reference/kotlin/androidx/navigation/ui) for use with a [NavController](/reference/kotlin/androidx/navigation/NavController). |

##### For [NavController](/reference/kotlin/androidx/navigation/NavController)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `NavController.navigateUp(drawerLayout: DrawerLayout?)` Handles the Up button by delegating its behavior to the given [NavController](/reference/kotlin/androidx/navigation/NavController). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `NavController.navigateUp(appBarConfiguration: AppBarConfiguration)` Handles the Up button by delegating its behavior to the given [NavController](/reference/kotlin/androidx/navigation/NavController). |

#### Top-level functions

|  |  |
| --- | --- |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(navGraph: NavGraph, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/navigation/ui). |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(topLevelMenu: Menu, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/navigation/ui). |
| [AppBarConfiguration](/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `AppBarConfiguration(topLevelDestinationIds: Set<Int>, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](/reference/kotlin/androidx/navigation/ui). |

## androidx.paging

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.paging:paging-common-ktx:2.1.2"
    implementation "androidx.paging:paging-runtime-ktx:2.1.2"
    implementation "androidx.paging:paging-rxjava2-ktx:2.1.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.paging:paging-common-ktx:2.1.2")
    implementation("androidx.paging:paging-runtime-ktx:2.1.2")
    implementation("androidx.paging:paging-rxjava2-ktx:2.1.2")
}
```

#### Extension functions

##### For [Factory](/reference/kotlin/androidx/paging/DataSource.Factory)

|  |  |
| --- | --- |
| Flowable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toFlowable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Flowable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toFlowable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toLiveData(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| [LiveData](/reference/kotlin/androidx/lifecycle/LiveData)<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toLiveData(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| Observable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toObservable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Observable<[PagedList](/reference/kotlin/androidx/paging/PagedList)<Value>> | `DataSource.Factory<Key, Value>.toObservable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](/reference/kotlin/androidx/paging/RxPagedListBuilder). |

#### Top-level functions

|  |  |
| --- | --- |
| [PagedList.Config](/reference/kotlin/androidx/paging/PagedList.Config) | `Config(pageSize: Int, prefetchDistance: Int = pageSize, enablePlaceholders: Boolean = true, initialLoadSizeHint: Int = pageSize * PagedList.Config.Builder.DEFAULT_INITIAL_PAGE_MULTIPLIER, maxSize: Int = PagedList.Config.MAX_SIZE_UNBOUNDED)` Constructs a [PagedList.Config](/reference/kotlin/androidx/paging/PagedList.Config), convenience for [PagedList.Config.Builder](/reference/kotlin/androidx/paging/PagedList.Config.Builder). |
| [PagedList](/reference/kotlin/androidx/paging/PagedList)<Value> | `PagedList(dataSource: DataSource<Key, Value>, config: PagedList.Config, notifyExecutor: Executor, fetchExecutor: Executor, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, initialKey: Key? = null)` Constructs a [PagedList](/reference/kotlin/androidx/paging/PagedList), convenience for [PagedList.Builder](/reference/kotlin/androidx/paging/PagedList.Builder). |

## androidx.palette.graphics

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.palette:palette-ktx:1.0.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.palette:palette-ktx:1.0.0")
}
```

#### Extension functions

##### For [Palette](/reference/kotlin/androidx/palette/graphics/Palette)

|  |  |
| --- | --- |
| operator [Palette.Swatch](/reference/kotlin/androidx/palette/graphics/Palette.Swatch)? | `Palette.get(target: Target)` Returns the selected swatch for the given target from the palette, or `null` if one could not be found. |

## androidx.preference

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.preference:preference-ktx:1.2.1"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.preference:preference-ktx:1.2.1")
}
```

#### Extension functions

##### For [PreferenceGroup](/reference/kotlin/androidx/preference/PreferenceGroup)

|  |  |
| --- | --- |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `PreferenceGroup.contains(preference: Preference)` Returns `true` if `preference` is found in this preference group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `PreferenceGroup.forEach(action: (preference: Preference) -> Unit)` Performs the given action on each preference in this preference group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `PreferenceGroup.forEachIndexed(action: (index: Int, preference: Preference) -> Unit)` Performs the given action on each preference in this preference group, providing its sequential index. |
| operator T? | `PreferenceGroup.get(key: CharSequence)` Returns the preference with `key`, or `null` if no preference with `key` is found. |
| operator [Preference](/reference/kotlin/androidx/preference/Preference) | `PreferenceGroup.get(index: Int)` Returns the preference at `index`. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `PreferenceGroup.isEmpty()` Returns true if this preference group contains no preferences. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `PreferenceGroup.isNotEmpty()` Returns true if this preference group contains one or more preferences. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)<[Preference](/reference/kotlin/androidx/preference/Preference)> | `PreferenceGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the preferences in this preference group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `PreferenceGroup.minusAssign(preference: Preference)` Removes `preference` from this preference group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `PreferenceGroup.plusAssign(preference: Preference)` Adds `preference` to this preference group. |

#### Extension properties

##### For [PreferenceGroup](/reference/kotlin/androidx/preference/PreferenceGroup)

|  |  |
| --- | --- |
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)<[Preference](/reference/kotlin/androidx/preference/Preference)> | `PreferenceGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the preferences in this preference group. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `PreferenceGroup.size()` Returns the number of preferences in this preference group. |

## androidx.room

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.room:room-ktx:2.8.4"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.room:room-ktx:2.8.4")
}
```

#### Extension functions

##### For [RoomDatabase](/reference/kotlin/androidx/room/RoomDatabase)

|  |  |
| --- | --- |
| suspend R | `RoomDatabase.withTransaction(block: suspend () -> R)` Calls the specified suspending [block](/reference/kotlin/androidx/room/package-summary#androidx.room$withTransaction(androidx.room.RoomDatabase,%20kotlin.coroutines.SuspendFunction0((androidx.room.withTransaction.R)))/block) in a database transaction. |

## androidx.slice.builders

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.slice:slice-builders-ktx:1.0.0-alpha08"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.slice:slice-builders-ktx:1.0.0-alpha08")
}
```

#### Extension functions

##### For [GridRowBuilderDsl](/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl)

|  |  |
| --- | --- |
| [GridRowBuilder](/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `GridRowBuilderDsl.cell(buildCell: CellBuilderDsl.() -> Unit)` |
| [GridRowBuilder](/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `GridRowBuilderDsl.seeMoreCell(buildCell: CellBuilderDsl.() -> Unit)` |

##### For [ListBuilderDsl](/reference/kotlin/androidx/slice/builders/ListBuilderDsl)

|  |  |
| --- | --- |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.gridRow(buildGrid: GridRowBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.header(buildHeader: HeaderBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.inputRange(buildInputRange: InputRangeBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.range(buildRange: RangeBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.row(buildRow: RowBuilderDsl.() -> Unit)` |
| [ListBuilder](/reference/kotlin/androidx/slice/builders/ListBuilder) | `ListBuilderDsl.seeMoreRow(buildRow: RowBuilderDsl.() -> Unit)` |

#### Top-level functions

|  |  |
| --- | --- |
| [Slice](/reference/kotlin/androidx/slice/Slice) | `list(context: Context, uri: Uri, ttl: Long, addRows: ListBuilderDsl.() -> Unit)` Reduces verbosity required to build a Slice in Kotlin. |
| [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction) | `tapSliceAction(pendingIntent: PendingIntent, icon: IconCompat, imageMode: Int = ICON_IMAGE, title: CharSequence)` Factory method to build a tappable [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction). |
| [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction) | `toggleSliceAction(pendingIntent: PendingIntent, icon: IconCompat? = null, title: CharSequence, isChecked: Boolean)` Factory method to build a toggleable [SliceAction](/reference/kotlin/androidx/slice/builders/SliceAction). |

## androidx.sqlite.db

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.sqlite:sqlite-ktx:2.6.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.sqlite:sqlite-ktx:2.6.2")
}
```

#### Extension functions

##### For [SupportSQLiteDatabase](/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase)

|  |  |
| --- | --- |
| T | `SupportSQLiteDatabase.transaction(exclusive: Boolean = true, body: SupportSQLiteDatabase.() -> T)` Run [body](/reference/kotlin/androidx/sqlite/db/package-summary#androidx.sqlite.db$transaction(androidx.sqlite.db.SupportSQLiteDatabase,%20kotlin.Boolean,%20kotlin.Function1((androidx.sqlite.db.SupportSQLiteDatabase,%20androidx.sqlite.db.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.work

#### Dependency

#### Extension functions

##### For [com.google.common.util.concurrent.ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)

|  |  |
| --- | --- |
| suspend R | `ListenableFuture<R>.await()` Awaits for the completion of the [ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html) without blocking a thread. |

##### For [Operation](/reference/kotlin/androidx/work/Operation)

|  |  |
| --- | --- |
| suspend [Operation.State.SUCCESS](/reference/kotlin/androidx/work/Operation.State.SUCCESS)! | `Operation.await()` Awaits an [Operation](/reference/kotlin/androidx/work/Operation) without blocking a thread. |

##### For [Data](/reference/kotlin/androidx/work/Data)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `Data.hasKeyWithValueOfType(key: String)` Returns true if the instance of [Data](/reference/kotlin/androidx/work/Data) has a value corresponding to the given [key](/reference/kotlin/androidx/work/package-summary#androidx.work$hasKeyWithValueOfType(androidx.work.Data,%20kotlin.String)/key) with an expected type T. |

##### For [Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder)

|  |  |
| --- | --- |
| [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `OneTimeWorkRequest.Builder.setInputMerger(@NonNull inputMerger: KClass<out InputMerger>)` Sets an [InputMerger](/reference/kotlin/androidx/work/InputMerger) on the [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder). |

#### Top-level functions

|  |  |
| --- | --- |
| [OneTimeWorkRequest.Builder](/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `OneTimeWorkRequestBuilder()` Creates a [OneTimeWorkRequest](/reference/kotlin/androidx/work/OneTimeWorkRequest) with the given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit, flexTimeInterval: Long, flexTimeIntervalUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `PeriodicWorkRequestBuilder(repeatInterval: Duration, flexTimeInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](/reference/kotlin/androidx/work/ListenableWorker). |
| [Data](/reference/kotlin/androidx/work/Data) | `workDataOf(vararg pairs: Pair<String, Any?>)` Converts a list of pairs to a [Data](/reference/kotlin/androidx/work/Data) object. |

## androidx.work.testing

#### Dependency

### Groovy

```
dependencies {
    implementation "androidx.work:work-testing:2.11.2"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.work:work-testing:2.11.2")
}
```

#### Top-level functions

|  |  |
| --- | --- |
| [TestListenableWorkerBuilder](/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder)<W> | `TestListenableWorkerBuilder(context: Context, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestListenableWorkerBuilder](/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder). |
| [TestWorkerBuilder](/reference/kotlin/androidx/work/testing/TestWorkerBuilder)<W> | `TestWorkerBuilder(context: Context, executor: Executor, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestWorkerBuilder](/reference/kotlin/androidx/work/testing/TestWorkerBuilder). |

## com.google.android.play.core.ktx

#### Dependency

### Groovy

```
dependencies {
    implementation "com.google.android.play:core-ktx:1.8.1"
}
```

### Kotlin

```
dependencies {
    implementation("com.google.android.play:core-ktx:1.8.1")
}
```

#### Extension functions

##### For [com.google.android.play.core.appupdate.AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html)

|  |  |
| --- | --- |
| suspend [AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html) | `AppUpdateManager.requestAppUpdateInfo()` Requests the update availability for the current app |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `AppUpdateManager.requestCompleteUpdate()` For a flexible update flow, triggers the completion of the update. |
| Flow<[AppUpdateResult](/reference/kotlin/com/google/android/play/core/ktx/AppUpdateResult)> | `AppUpdateManager.requestUpdateFlow()` Entry point for monitoring the availability and progress of updates. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `AppUpdateManager.startUpdateFlowForResult(appUpdateInfo: AppUpdateInfo, appUpdateType: Int, fragment: Fragment, requestCode: Int)` A version of [AppUpdateManager.startUpdateFlowForResult](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo, int, android.app.Activity, int)) that accepts an AndroidX Fragment for returning the result. |

##### For [com.google.android.play.core.splitinstall.SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html)

|  |  |
| --- | --- |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SplitInstallManager.requestCancelInstall(sessionId: Int)` Suspend version of [SplitInstallManager.cancelInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#cancelInstall(int)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SplitInstallManager.requestDeferredInstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredInstall(java.util.List<java.lang.String>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SplitInstallManager.requestDeferredLanguageInstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredLanguageInstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SplitInstallManager.requestDeferredLanguageUninstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredLanguageUninstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `SplitInstallManager.requestDeferredUninstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredUninstall(java.util.List<java.lang.String>)) |
| suspend [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SplitInstallManager.requestInstall(modules: List<String> = listOf(), languages: List<String> = listOf())` Initiates installation of the requested modules/languages. |
| Flow<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)> | `SplitInstallManager.requestProgressFlow()` Creates and returns a buffered [Flow](/reference/kotlin/com/google/android/play/core/ktx) that will deliver all progress events for ongoing split installations. |
| suspend [SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) | `SplitInstallManager.requestSessionState(sessionId: Int)` Suspend version of [SplitInstallManager.getSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#getSessionState(int)) |
| suspend [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)> | `SplitInstallManager.requestSessionStates()` Suspend version of [SplitInstallManager.getSessionStates](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#getSessionStates()) |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SplitInstallManager.startConfirmationDialogForResult(sessionState: SplitInstallSessionState, fragment: Fragment, requestCode: Int)` A version of [SplitInstallManager.startConfirmationDialogForResult](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#startConfirmationDialogForResult(com.google.android.play.core.splitinstall.SplitInstallSessionState, android.app.Activity, int)) that accepts an AndroidX Fragment for returning the result. |

#### Extension properties

##### For [com.google.android.play.core.appupdate.AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html)

|  |  |
| --- | --- |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `AppUpdateInfo.installStatus()` Returns the progress status of the update. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `AppUpdateInfo.isFlexibleUpdateAllowed()` Returns `true` if flexible update is allowed. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `AppUpdateInfo.isImmediateUpdateAllowed()` Returns `true` if immediate update is allowed. |

##### For [com.google.android.play.core.install.InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html)

|  |  |
| --- | --- |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `InstallState.hasTerminalStatus()` This signifies that this is a terminal status (there will be no more updates) and should be handled accordingly (success, cancellation or failure). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `InstallState.installErrorCode()` Returns the error code for an install, or {@link InstallErrorCode#NO\_ERROR}. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `InstallState.installStatus()` Returns the status of an install. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)! | `InstallState.packageName()` Returns the package name for the app being installed. |

##### For [com.google.android.play.core.splitinstall.SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)

|  |  |
| --- | --- |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `SplitInstallSessionState.bytesDownloaded()` The bytes downloaded by this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SplitInstallSessionState.errorCode()` The error code of this update. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `SplitInstallSessionState.hasTerminalStatus()` Signifies that this update is terminal, meaning there will be no more updates for this session. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)> | `SplitInstallSessionState.languages()` The languages included by this update. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)> | `SplitInstallSessionState.moduleNames()` The modules included by this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SplitInstallSessionState.sessionId()` The session id of this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `SplitInstallSessionState.status()` The status code of this update. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `SplitInstallSessionState.totalBytesToDownload()` The total bytes to download by this update. |

#### Top-level functions

|  |  |
| --- | --- |
| [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.html) | `SplitInstallStateUpdatedListener(onRequiresConfirmation: (SplitInstallSessionState) -> Unit, onInstalled: (SplitInstallSessionState) -> Unit, onFailed: (SplitInstallSessionState) -> Unit = {}, onPending: (SplitInstallSessionState) -> Unit = {}, onDownloaded: (SplitInstallSessionState) -> Unit = {}, onDownloading: (SplitInstallSessionState) -> Unit = {}, onInstalling: (SplitInstallSessionState) -> Unit = {}, onCanceling: (SplitInstallSessionState) -> Unit = {}, onCanceled: (SplitInstallSessionState) -> Unit = {}, onNonTerminalStatus: (SplitInstallSessionState) -> Unit = {}, onTerminalStatus: (SplitInstallSessionState) -> Unit = {})` A convenience function for creating a [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.html). |