---
title: https://developer.android.com/kotlin/ktx/extensions-list
url: https://developer.android.com/kotlin/ktx/extensions-list
source: md.txt
---

## androidx.activity

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.activity:activity-ktx:1.13.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.activity:activity-ktx:1.13.0")
}
```

#### Extension functions

##### For [OnBackPressedDispatcher](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedDispatcher.md.txt)

|---|---|
| [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback.md.txt) | `OnBackPressedDispatcher.addCallback(owner: LifecycleOwner? = null, enabled: Boolean = true, onBackPressed: OnBackPressedCallback.() -> Unit)` Create and add a new [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback.md.txt) that calls [onBackPressed](https://developer.android.com/kotlin/ktx/extensions-list#androidx.activity$addCallback(androidx.activity.OnBackPressedDispatcher, androidx.lifecycle.LifecycleOwner, kotlin.Boolean, kotlin.Function1((androidx.activity.OnBackPressedCallback, kotlin.Unit)))/onBackPressed) in [OnBackPressedCallback.handleOnBackPressed](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback.md.txt#handleOnBackPressed()). |

##### For [ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity.md.txt)

|---|---|
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)\<VM\> | `ComponentActivity.viewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the ComponentActivity's ViewModel, if [factoryProducer](https://developer.android.com/kotlin/ktx/extensions-list#androidx.activity$viewModels(androidx.activity.ComponentActivity, kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory.md.txt) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt) first time. |

## androidx.benchmark

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.5.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.5.0")
}
```

#### Top-level functions

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `beginTraceSection(sectionName: String)` <br /> |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `endTraceSection()` <br /> |

## androidx.benchmark.junit4

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.5.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.5.0")
}
```

#### Extension functions

##### For [BenchmarkRule](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `BenchmarkRule.measureRepeated(crossinline block: BenchmarkRule.Scope.() -> Unit)` Benchmark a block of code. |

## androidx.collection

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.collection:collection-ktx:1.7.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.collection:collection-ktx:1.7.0")
}
```

#### Extension functions

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$contains(androidx.collection.LongSparseArray((androidx.collection.contains.T)), kotlin.Long)/key). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$forEach(androidx.collection.LongSparseArray((androidx.collection.forEach.T)), kotlin.Function2((kotlin.Long, androidx.collection.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)), kotlin.Long, androidx.collection.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)), kotlin.Long, androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray.md.txt)\<T\> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$plus(androidx.collection.LongSparseArray((androidx.collection.plus.T)), androidx.collection.LongSparseArray((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)), kotlin.Long, androidx.collection.remove.T)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)), kotlin.Long, androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)\<T\> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.contains(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$contains(androidx.collection.SparseArrayCompat((androidx.collection.contains.T)), kotlin.Int)/key). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArrayCompat<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$forEach(androidx.collection.SparseArrayCompat((androidx.collection.forEach.T)), kotlin.Function2((kotlin.Int, androidx.collection.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArrayCompat<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)), kotlin.Int, androidx.collection.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)), kotlin.Int, androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArrayCompat<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseArrayCompat<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat.md.txt)\<T\> | `SparseArrayCompat<T>.plus(other: SparseArrayCompat<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$plus(androidx.collection.SparseArrayCompat((androidx.collection.plus.T)), androidx.collection.SparseArrayCompat((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArrayCompat<T>.remove(key: Int, value: T)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)), kotlin.Int, androidx.collection.remove.T)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)), kotlin.Int, androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArrayCompat<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)\<T\> | `SparseArrayCompat<T>.valueIterator()` Return an iterator over the collection's values. |

#### Extension properties

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseArrayCompat<T>.size()` Returns the number of key/value pairs in the collection. |

#### Top-level functions

|---|---|
| [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap.md.txt)\<K, V\> | `arrayMapOf()` Returns an empty new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap.md.txt). |
| [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap.md.txt)\<K, V\> | `arrayMapOf(vararg pairs: Pair<K, V>)` Returns a new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap.md.txt) with the specified contents, given as a list of pairs where the first component is the key and the second component is the value. |
| [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet.md.txt)\<T\> | `arraySetOf()` Returns an empty new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet.md.txt). |
| [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet.md.txt)\<T\> | `arraySetOf(vararg values: T)` Returns a new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet.md.txt) with the specified contents. |
| [LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache.md.txt)\<K, V\> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache.md.txt) with the given parameters. |

## androidx.core.animation

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.animation.Animator](https://developer.android.com/reference/android/animation/Animator.md.txt)

|---|---|
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener.md.txt) | `Animator.addListener(crossinline onEnd: (animator: Animator) -> Unit = {}, crossinline onStart: (animator: Animator) -> Unit = {}, crossinline onCancel: (animator: Animator) -> Unit = {}, crossinline onRepeat: (animator: Animator) -> Unit = {})` Add a listener to this Animator using the provided actions. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener.md.txt) | `Animator.addPauseListener(crossinline onResume: (animator: Animator) -> Unit = {}, crossinline onPause: (animator: Animator) -> Unit = {})` Add a pause and resume listener to this Animator using the provided actions. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener.md.txt) | `Animator.doOnCancel(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been cancelled. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener.md.txt) | `Animator.doOnEnd(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has ended. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener.md.txt) | `Animator.doOnPause(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has been paused. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener.md.txt) | `Animator.doOnRepeat(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has repeated. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator.AnimatorPauseListener.md.txt) | `Animator.doOnResume(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has resumed after a pause. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator.AnimatorListener.md.txt) | `Animator.doOnStart(crossinline action: (animator: Animator) -> Unit)` Add an action which will be invoked when the animation has started. |

## androidx.core.content

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.content.Context](https://developer.android.com/reference/android/content/Context.md.txt)

|---|---|
| T? | `Context.getSystemService()` Return the handle to a system-level service by class. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Context.withStyledAttributes(set: AttributeSet? = null, attrs: IntArray, @AttrRes defStyleAttr: Int = 0, @StyleRes defStyleRes: Int = 0, block: TypedArray.() -> Unit)` Executes [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content$withStyledAttributes(android.content.Context, android.util.AttributeSet, kotlin.IntArray, kotlin.Int, kotlin.Int, kotlin.Function1((android.content.res.TypedArray, kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.md.txt) receiver. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Context.withStyledAttributes(@StyleRes resourceId: Int, attrs: IntArray, block: TypedArray.() -> Unit)` Executes [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content$withStyledAttributes(android.content.Context, kotlin.Int, kotlin.IntArray, kotlin.Function1((android.content.res.TypedArray, kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.md.txt) receiver. |

##### For [android.content.SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SharedPreferences.edit(commit: Boolean = false, action: Editor.() -> Unit)` Allows editing of this preference instance with a call to [apply](https://developer.android.com/reference/android/content/SharedPreferences.Editor.md.txt#apply()) or [commit](https://developer.android.com/reference/android/content/SharedPreferences.Editor.md.txt#commit()) to persist the changes. |

#### Top-level functions

|---|---|
| [ContentValues](https://developer.android.com/reference/android/content/ContentValues.md.txt) | `contentValuesOf(vararg pairs: Pair<String, Any?>)` Returns a new [ContentValues](https://developer.android.com/reference/android/content/ContentValues.md.txt) with the given key/value pairs as elements. |

## androidx.core.content.res

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.content.res.TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `TypedArray.getBooleanOrThrow(@StyleableRes index: Int)` Retrieve the boolean value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getBooleanOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getColorOrThrow(@StyleableRes index: Int)` Retrieve the color value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getColorOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList.md.txt) | `TypedArray.getColorStateListOrThrow(@StyleableRes index: Int)` Retrieve the color state list value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getColorStateListOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `TypedArray.getDimensionOrThrow(@StyleableRes index: Int)` Retrieve the dimension value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getDimensionOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getDimensionPixelOffsetOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel offset value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getDimensionPixelOffsetOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getDimensionPixelSizeOrThrow(@StyleableRes index: Int)` Retrieve the dimension pixel size value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getDimensionPixelSizeOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.md.txt) | `TypedArray.getDrawableOrThrow(@StyleableRes index: Int)` Retrieve the drawable value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getDrawableOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `TypedArray.getFloatOrThrow(@StyleableRes index: Int)` Retrieve the float value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getFloatOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Typeface](https://developer.android.com/reference/android/graphics/Typeface.md.txt) | `TypedArray.getFontOrThrow(@StyleableRes index: Int)` Retrieve the font value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getFontOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getIntOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getIntOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getIntegerOrThrow(@StyleableRes index: Int)` Retrieve the integer value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getIntegerOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `TypedArray.getResourceIdOrThrow(@StyleableRes index: Int)` Retrieves the resource identifier for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getResourceIdOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `TypedArray.getStringOrThrow(@StyleableRes index: Int)` Retrieve the string value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getStringOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)\<[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)\> | `TypedArray.getTextArrayOrThrow(@StyleableRes index: Int)` Retrieve the text array value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getTextArrayOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) | `TypedArray.getTextOrThrow(@StyleableRes index: Int)` Retrieve the text value for the attribute at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$getTextOrThrow(android.content.res.TypedArray, kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/) if not defined. |
| R | `TypedArray.use(block: (TypedArray) -> R)` Executes the given [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.content.res$use(android.content.res.TypedArray, kotlin.Function1((android.content.res.TypedArray, androidx.core.content.res.use.R)))/block) function on this TypedArray and then recycles it. |

## androidx.core.database

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.database.Cursor](https://developer.android.com/reference/android/database/Cursor.md.txt)

|---|---|
| [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)? | `Cursor.getBlobOrNull(index: Int)` Returns the value of the requested column as a nullable byte array. |
| [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)? | `Cursor.getDoubleOrNull(index: Int)` Returns the value of the requested column as a nullable double. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)? | `Cursor.getFloatOrNull(index: Int)` Returns the value of the requested column as a nullable float. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)? | `Cursor.getIntOrNull(index: Int)` Returns the value of the requested column as a nullable integer. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)? | `Cursor.getLongOrNull(index: Int)` Returns the value of the requested column as a nullable long. |
| [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)? | `Cursor.getShortOrNull(index: Int)` Returns the value of the requested column as a nullable short. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)? | `Cursor.getStringOrNull(index: Int)` Returns the value of the requested column as a nullable string. |

## androidx.core.database.sqlite

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.database.sqlite.SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.md.txt)

|---|---|
| T | `SQLiteDatabase.transaction(exclusive: Boolean = true, body: SQLiteDatabase.() -> T)` Run [body](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.database.sqlite$transaction(android.database.sqlite.SQLiteDatabase, kotlin.Boolean, kotlin.Function1((android.database.sqlite.SQLiteDatabase, androidx.core.database.sqlite.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.core.graphics

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `Bitmap.applyCanvas(block: Canvas.() -> Unit)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.md.txt) to draw on this bitmap and executes the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$applyCanvas(android.graphics.Bitmap, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) on the newly created canvas. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Bitmap.contains(p: Point)` Returns true if the specified point is inside the bitmap. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Bitmap.contains(p: PointF)` Returns true if the specified point is inside the bitmap. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Bitmap.get(x: Int, y: Int)` Returns the value of the pixel at the specified location. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `Bitmap.scale(width: Int, height: Int, filter: Boolean = true)` Creates a new bitmap, scaled from this bitmap, when possible. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Bitmap.set(x: Int, y: Int, color: Int)` Writes the specified [color int](https://developer.android.com/reference/android/graphics/Color.md.txt) into the bitmap (assuming it is mutable) at the specified `(x, y)` coordinate. |

##### For [android.graphics.Canvas](https://developer.android.com/reference/android/graphics/Canvas.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipRect: Rect, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.Rect, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.md.txt#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipRect: RectF, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.RectF, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.md.txt#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(left: Int, top: Int, right: Int, bottom: Int, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withClip(android.graphics.Canvas, kotlin.Int, kotlin.Int, kotlin.Int, kotlin.Int, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.md.txt#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(left: Float, top: Float, right: Float, bottom: Float, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withClip(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.md.txt#clipRect(android.graphics.RectF,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withClip(clipPath: Path, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withClip(android.graphics.Canvas, android.graphics.Path, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.clipPath](https://developer.android.com/reference/android/graphics/Canvas.md.txt#clipPath(android.graphics.Path,%20android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withMatrix(matrix: Matrix = Matrix(), block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withMatrix(android.graphics.Canvas, android.graphics.Matrix, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.concat](https://developer.android.com/reference/android/graphics/Canvas.md.txt#concat(android.graphics.Matrix)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withRotation(degrees: Float = 0.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withRotation(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.rotate](https://developer.android.com/reference/android/graphics/Canvas.md.txt#rotate(float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withSave(block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withSave(android.graphics.Canvas, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save()) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withScale(x: Float = 1.0f, y: Float = 1.0f, pivotX: Float = 0.0f, pivotY: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withScale(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.scale](https://developer.android.com/reference/android/graphics/Canvas.md.txt#scale(float,%20float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withSkew(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withSkew(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.skew](https://developer.android.com/reference/android/graphics/Canvas.md.txt#skew(float,%20float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Canvas.withTranslation(x: Float = 0.0f, y: Float = 0.0f, block: Canvas.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$withTranslation(android.graphics.Canvas, kotlin.Float, kotlin.Float, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.md.txt#save())/[Canvas.translate](https://developer.android.com/reference/android/graphics/Canvas.md.txt#translate(float,%20float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.md.txt#restoreToCount(int)). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.md.txt)

|---|---|
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Color.component4()` Returns the fourth component of the color. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.md.txt)! | `Color.convertTo(colorSpace: Named)` Converts the color receiver to a color in the specified color space. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.md.txt)! | `Color.convertTo(colorSpace: ColorSpace)` Converts the color receiver to a color in the specified color space. |
| operator [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) | `Color.plus(c: Color)` Composites two translucent colors together. |

##### For [android.graphics.ImageDecoder.Source](https://developer.android.com/reference/android/graphics/ImageDecoder.Source.md.txt)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `Source.decodeBitmap(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Bitmap from a Source |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.md.txt) | `Source.decodeDrawable(crossinline action: ImageDecoder.(info: ImageInfo, source: Source) -> Unit)` Create a Drawable from a Source |

##### For [android.graphics.Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt)

|---|---|
| operator [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) | `Matrix.times(m: Matrix)` Multiplies this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) by another matrix and returns the result as a new matrix. |
| [FloatArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float-array/) | `Matrix.values()` Returns the 9 values of this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) as a new array of floats. |

##### For [android.graphics.Paint](https://developer.android.com/reference/android/graphics/Paint.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Paint.setBlendMode(blendModeCompat: BlendModeCompat?)` Convenience method to configure the BlendMode of a Paint in a backward compatible way. |

##### For [android.graphics.Path](https://developer.android.com/reference/android/graphics/Path.md.txt)

|---|---|
| infix [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) | `Path.and(p: Path)` Returns the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.md.txt). |
| [Iterable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/)\<[PathSegment](https://developer.android.com/reference/kotlin/androidx/core/graphics/PathSegment.md.txt)\> | `Path.flatten(error: Float = 0.5f)` Flattens (or approximate) the [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) with a series of line segments. |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) | `Path.minus(p: Path)` Returns the difference of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.md.txt). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) | `Path.or(p: Path)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.md.txt). |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) | `Path.plus(p: Path)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.md.txt). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.md.txt) | `Path.xor(p: Path)` Returns the union minus the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.md.txt). |

##### For [android.graphics.Picture](https://developer.android.com/reference/android/graphics/Picture.md.txt)

|---|---|
| [Picture](https://developer.android.com/reference/android/graphics/Picture.md.txt) | `Picture.record(width: Int, height: Int, block: Canvas.() -> Unit)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.md.txt) to record commands in this [Picture](https://developer.android.com/reference/android/graphics/Picture.md.txt), executes the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$record(android.graphics.Picture, kotlin.Int, kotlin.Int, kotlin.Function1((android.graphics.Canvas, kotlin.Unit)))/block) on the newly created canvas and returns this [Picture](https://developer.android.com/reference/android/graphics/Picture.md.txt). |

##### For [android.graphics.Point](https://developer.android.com/reference/android/graphics/Point.md.txt)

|---|---|
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Point.component1()` Returns the x coordinate of this point. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Point.component2()` Returns the y coordinate of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `Point.minus(p: Point)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `Point.minus(xy: Int)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `Point.plus(p: Point)` Offsets this point by the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `Point.plus(xy: Int)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `Point.toPointF()` Returns a [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) representation of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `Point.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt)

|---|---|
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `PointF.component1()` Returns the x coordinate of this point. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `PointF.component2()` Returns the y coordinate of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `PointF.minus(p: PointF)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `PointF.minus(xy: Float)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `PointF.plus(p: PointF)` Offsets this point by the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `PointF.plus(xy: Float)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) | `PointF.toPoint()` Returns a [Point](https://developer.android.com/reference/android/graphics/Point.md.txt) representation of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.md.txt) | `PointF.unaryMinus()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode.md.txt)

|---|---|
| [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.md.txt) | `Mode.toColorFilter(color: Int)` Creates a new [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.md.txt) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode.md.txt) as the alpha compositing or blending mode, and the specified [color](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$toColorFilter(android.graphics.PorterDuff.Mode, kotlin.Int)/color). |
| [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.md.txt) | `Mode.toXfermode()` Creates a new [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.md.txt) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff.Mode.md.txt) as the alpha compositing or blending mode. |

##### For [android.graphics.Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt)

|---|---|
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.and(r: Rect)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component1()` Returns "left", the first component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component2()` Returns "top", the second component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component3()` Returns "right", the third component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Rect.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Rect.contains(p: Point)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Rect.minus(r: Rect)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.minus(xy: Int)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.minus(xy: Point)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.or(r: Rect)` Returns the union of two rectangles as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.plus(r: Rect)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.plus(xy: Int)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.plus(xy: Point)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `Rect.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$times(android.graphics.Rect, kotlin.Int)/factor). |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `Rect.toRectF()` Returns a [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Rect.toRegion()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) representation of this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Rect.xor(r: Rect)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt)

|---|---|
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.and(r: RectF)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component1()` Returns "left", the first component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component2()` Returns "top", the second component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component3()` Returns "right", the third component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `RectF.component4()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `RectF.contains(p: PointF)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `RectF.minus(r: RectF)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.minus(xy: Float)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.minus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.or(r: RectF)` Returns the union of two rectangles as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.plus(r: RectF)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.plus(xy: Float)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.plus(xy: PointF)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.times(factor: Int)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$times(android.graphics.RectF, kotlin.Int)/factor). |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.times(factor: Float)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$times(android.graphics.RectF, kotlin.Float)/factor). |
| [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) | `RectF.toRect()` Returns a [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `RectF.toRegion()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) representation of this rectangle. |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.md.txt) | `RectF.transform(m: Matrix)` Transform this rectangle in place using the supplied [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) and returns this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `RectF.xor(r: RectF)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.Region](https://developer.android.com/reference/android/graphics/Region.md.txt)

|---|---|
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.and(r: Rect)` Return the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.and(r: Region)` Return the intersection of this region and the specified region as a new region. |
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Region.contains(p: Point)` Return true if the region contains the specified [Point](https://developer.android.com/reference/android/graphics/Point.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Region.forEach(action: (rect: Rect) -> Unit)` Performs the given action on each rect in this region. |
| operator [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)\<[Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt)\> | `Region.iterator()` Returns an [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/) over the rects in this region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.minus(r: Rect)` Return the difference of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.minus(r: Region)` Return the difference of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.not()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.or(r: Rect)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.or(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.plus(r: Rect)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.plus(r: Region)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.unaryMinus()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.xor(r: Rect)` Return the union minus the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.md.txt) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.md.txt) | `Region.xor(r: Region)` Return the union minus the intersection of this region and the specified region as a new region. |

##### For [android.graphics.Shader](https://developer.android.com/reference/android/graphics/Shader.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Shader.transform(block: Matrix.() -> Unit)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$transform(android.graphics.Shader, kotlin.Function1((android.graphics.Matrix, kotlin.Unit)))/block) in calls to [Shader.getLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.md.txt#getLocalMatrix(android.graphics.Matrix)) and [Shader.setLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.md.txt#setLocalMatrix(android.graphics.Matrix)). |

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|---|---|
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component1()` Return the alpha component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component2()` Return the red component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component3()` Return the green component of a color int. |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.component4()` Return the blue component of a color int. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.convertTo(colorSpace: Named)` Converts the color int receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.convertTo(colorSpace: ColorSpace)` Converts the color int receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) | `Int.toColor()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) instance from a color int. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Int.toColorLong()` Converts the specified ARGB [color int](https://developer.android.com/reference/android/graphics/Color.md.txt) to an RGBA [color long](https://developer.android.com/reference/android/graphics/Color.md.txt) in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace.Named.md.txt#SRGB) color space. |

##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

|---|---|
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component1()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component2()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component3()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.component4()` Returns the fourth component of the color. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Long.convertTo(colorSpace: Named)` Converts the color long receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `Long.convertTo(colorSpace: ColorSpace)` Converts the color long receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) | `Long.toColor()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) instance from a [color long](https://developer.android.com/reference/android/graphics/Color.md.txt). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Long.toColorInt()` Converts the specified [color long](https://developer.android.com/reference/android/graphics/Color.md.txt) to an ARGB [color int](https://developer.android.com/reference/android/graphics/Color.md.txt). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `String.toColorInt()` Return a corresponding [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) color of this [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/). |

#### Extension properties

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.alpha()` Return the alpha component of a color int. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.blue()` Return the blue component of a color int. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.green()` Return the green component of a color int. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Int.luminance()` Returns the relative luminance of a color int, assuming sRGB encoding. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Int.red()` Return the red component of a color int. |

##### For [kotlin.Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)

|---|---|
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.alpha()` Return the alpha component of a color long. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.blue()` Return the blue component of a color long. |
| [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace.md.txt) | `Long.colorSpace()` Returns the color space encoded in the specified color long. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.green()` Return the green component of a color long. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Long.isSrgb()` Indicates whether the color is in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace.Named.md.txt#SRGB) color space. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Long.isWideGamut()` Indicates whether the color is in a [wide-gamut](https://developer.android.com/reference/android/graphics/ColorSpace.md.txt) color space. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.luminance()` Returns the relative luminance of a color. |
| [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `Long.red()` Return the red component of a color long. |

#### Top-level functions

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888)` Returns a mutable bitmap with the specified [width](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config)/width) and [height](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config)/height). |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `createBitmap(width: Int, height: Int, config: Config = Bitmap.Config.ARGB_8888, hasAlpha: Boolean = true, colorSpace: ColorSpace = ColorSpace.get(ColorSpace.Named.SRGB))` Returns a mutable bitmap with the specified [width](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config, kotlin.Boolean, android.graphics.ColorSpace)/width) and [height](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$createBitmap(kotlin.Int, kotlin.Int, android.graphics.Bitmap.Config, kotlin.Boolean, android.graphics.ColorSpace)/height). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) | `rotationMatrix(degrees: Float, px: Float = 0.0f, py: Float = 0.0f)` Creates a rotation matrix, defined by a rotation angle in degrees around the pivot point located at the coordinates ([px](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$rotationMatrix(kotlin.Float, kotlin.Float, kotlin.Float)/px), [py](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$rotationMatrix(kotlin.Float, kotlin.Float, kotlin.Float)/py)). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) | `scaleMatrix(sx: Float = 1.0f, sy: Float = 1.0f)` Creates a scale matrix with the scale factor [sx](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$scaleMatrix(kotlin.Float, kotlin.Float)/sx) and [sy](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$scaleMatrix(kotlin.Float, kotlin.Float)/sy) respectively on the `x` and `y` axis. |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.md.txt) | `translationMatrix(tx: Float = 0.0f, ty: Float = 0.0f)` Creates a translation matrix with the translation amounts [tx](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$translationMatrix(kotlin.Float, kotlin.Float)/tx) and [ty](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.graphics$translationMatrix(kotlin.Float, kotlin.Float)/ty) respectively on the `x` and `y` axis. |

## androidx.core.graphics.drawable

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) | `Bitmap.toAdaptiveIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) from this adaptive [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt). |
| [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.md.txt) | `Bitmap.toDrawable(resources: Resources)` Create a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.md.txt) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt). |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) | `Bitmap.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.md.txt)

|---|---|
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.md.txt) | `Color.toDrawable()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.md.txt) from this [Color](https://developer.android.com/reference/android/graphics/Color.md.txt) (via [Color.toArgb](https://developer.android.com/reference/android/graphics/Color.md.txt#toArgb())). |

##### For [android.graphics.drawable.Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.md.txt)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `Drawable.toBitmap(@Px width: Int = intrinsicWidth, @Px height: Int = intrinsicHeight, config: Config? = null)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) representation of this [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Drawable.updateBounds(@Px left: Int = bounds.left, @Px top: Int = bounds.top, @Px right: Int = bounds.right, @Px bottom: Int = bounds.bottom)` Updates this drawable's bounds. |

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.md.txt)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) | `Uri.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) from this [Uri](https://developer.android.com/reference/android/net/Uri.md.txt). |

##### For [kotlin.ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) | `ByteArray.toIcon()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.md.txt) from this [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/). |

##### For [kotlin.Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)

|---|---|
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.md.txt) | `Int.toDrawable()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.md.txt) from this color value. |

## androidx.core.location

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.location.Location](https://developer.android.com/reference/android/location/Location.md.txt)

|---|---|
| operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) | `Location.component1()` Returns the latitude of this [Location](https://developer.android.com/reference/android/location/Location.md.txt). |
| operator [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/) | `Location.component2()` Returns the longitude of this [Location](https://developer.android.com/reference/android/location/Location.md.txt). |

## androidx.core.net

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.md.txt)

|---|---|
| [File](https://developer.android.com/reference/java/io/File.md.txt) | `Uri.toFile()` Creates a [File](https://developer.android.com/reference/java/io/File.md.txt) from the given [Uri](https://developer.android.com/reference/android/net/Uri.md.txt). |

##### For [java.io.File](https://developer.android.com/reference/java/io/File.md.txt)

|---|---|
| [Uri](https://developer.android.com/reference/android/net/Uri.md.txt) | `File.toUri()` Creates a Uri from the given file. |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|---|---|
| [Uri](https://developer.android.com/reference/android/net/Uri.md.txt) | `String.toUri()` Creates a Uri from the given encoded URI string. |

## androidx.core.os

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.os.Handler](https://developer.android.com/reference/android/os/Handler.md.txt)

|---|---|
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.md.txt) | `Handler.postAtTime(uptimeMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postAtTime](https://developer.android.com/reference/android/os/Handler.md.txt#postAtTime(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.md.txt) | `Handler.postDelayed(delayInMillis: Long, token: Any? = null, crossinline action: () -> Unit)` Version of [Handler.postDelayed](https://developer.android.com/reference/android/os/Handler.md.txt#postDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |

#### Top-level functions

|---|---|
| [Bundle](https://developer.android.com/reference/android/os/Bundle.md.txt) | `bundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [Bundle](https://developer.android.com/reference/android/os/Bundle.md.txt) with the given key/value pairs as elements. |
| [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.md.txt) | `persistableBundleOf(vararg pairs: Pair<String, Any?>)` Returns a new [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.md.txt) with the given key/value pairs as elements. |
| T | `trace(sectionName: String, block: () -> T)` Wrap the specified [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.os$trace(kotlin.String, kotlin.Function0((androidx.core.os.trace.T)))/block) in calls to [Trace.beginSection](https://developer.android.com/reference/android/os/Trace.md.txt#beginSection(java.lang.String)) (with the supplied [sectionName](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.os$trace(kotlin.String, kotlin.Function0((androidx.core.os.trace.T)))/sectionName)) and [Trace.endSection](https://developer.android.com/reference/android/os/Trace.md.txt#endSection()). |

## androidx.core.text

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.text.Spannable](https://developer.android.com/reference/android/text/Spannable.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.clearSpans()` Clear all spans from this text. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.set(start: Int, end: Int, span: Any)` Add [span](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/span) to the range [start](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/start)...[end](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$set(android.text.Spannable, kotlin.Int, kotlin.Int, kotlin.Any)/end) of the text. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Spannable.set(range: IntRange, span: Any)` Add [span](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$set(android.text.Spannable, kotlin.ranges.IntRange, kotlin.Any)/span) to the [range](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$set(android.text.Spannable, kotlin.ranges.IntRange, kotlin.Any)/range) of the text. |

##### For [android.text.SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt)

|---|---|
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.backgroundColor(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$backgroundColor(android.text.SpannableStringBuilder, kotlin.Int, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [BackgroundColorSpan](https://developer.android.com/reference/android/text/style/BackgroundColorSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.bold(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$bold(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a bold [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.color(color: Int, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$color(android.text.SpannableStringBuilder, kotlin.Int, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [ForegroundColorSpan](https://developer.android.com/reference/android/text/style/ForegroundColorSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.inSpans(vararg spans: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Array((kotlin.Any)), kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in [spans](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Array((kotlin.Any)), kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/spans). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.inSpans(span: Any, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Any, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in [span](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$inSpans(android.text.SpannableStringBuilder, kotlin.Any, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/span). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.italic(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$italic(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in an italic [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.scale(proportion: Float, builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$scale(android.text.SpannableStringBuilder, kotlin.Float, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [RelativeSizeSpan](https://developer.android.com/reference/android/text/style/RelativeSizeSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.strikeThrough(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$strikeThrough(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [StrikethroughSpan](https://developer.android.com/reference/android/text/style/StrikethroughSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.subscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$subscript(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [SubscriptSpan](https://developer.android.com/reference/android/text/style/SubscriptSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.superscript(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$superscript(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in a [SuperscriptSpan](https://developer.android.com/reference/android/text/style/SuperscriptSpan.md.txt). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) | `SpannableStringBuilder.underline(builderAction: SpannableStringBuilder.() -> Unit)` Wrap appended text in [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$underline(android.text.SpannableStringBuilder, kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) in an [UnderlineSpan](https://developer.android.com/reference/android/text/style/UnderlineSpan.md.txt). |

##### For [android.text.Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt)

|---|---|
| [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/)\<out T\> | `Spanned.getSpans(start: Int = 0, end: Int = length)` Get all spans that are instance of T. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `Spanned.toHtml(option: Int = TO_HTML_PARAGRAPH_LINES_CONSECUTIVE)` Returns a string of HTML from the spans in this [Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt). |

##### For [kotlin.CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `CharSequence.isDigitsOnly()` Returns whether the given [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) contains only digits. |
| [Spannable](https://developer.android.com/reference/android/text/Spannable.md.txt) | `CharSequence.toSpannable()` Returns a new [Spannable](https://developer.android.com/reference/android/text/Spannable.md.txt) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannableString](https://developer.android.com/reference/android/text/SpannableString.md.txt). |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt) | `CharSequence.toSpanned()` Returns a new [Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt) from [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/), or the source itself if it is already an instance of [SpannedString](https://developer.android.com/reference/android/text/SpannedString.md.txt). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `CharSequence.trimmedLength()` Returns the length that the specified [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/) would have if spaces and ASCII control characters were trimmed from the start and end, as by [String.trim](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim.html). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|---|---|
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `String.htmlEncode()` Html-encode the string. |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt) | `String.parseAsHtml(flags: Int = FROM_HTML_MODE_LEGACY, imageGetter: ImageGetter? = null, tagHandler: TagHandler? = null)` Returns a [Spanned](https://developer.android.com/reference/android/text/Spanned.md.txt) from parsing this string as HTML. |

#### Extension properties

##### For [java.util.Locale](https://developer.android.com/reference/java/util/Locale.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Locale.layoutDirection()` Returns layout direction for a given locale. |

#### Top-level functions

|---|---|
| [SpannedString](https://developer.android.com/reference/android/text/SpannedString.md.txt) | `buildSpannedString(builderAction: SpannableStringBuilder.() -> Unit)` Builds new string by populating a newly created [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.md.txt) using the provided [builderAction](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.text$buildSpannedString(kotlin.Function1((android.text.SpannableStringBuilder, kotlin.Unit)))/builderAction) and then converting it to [SpannedString](https://developer.android.com/reference/android/text/SpannedString.md.txt). |

## androidx.core.transition

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.md.txt)

|---|---|
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.addListener(crossinline onEnd: (transition: Transition) -> Unit = {}, crossinline onStart: (transition: Transition) -> Unit = {}, crossinline onCancel: (transition: Transition) -> Unit = {}, crossinline onResume: (transition: Transition) -> Unit = {}, crossinline onPause: (transition: Transition) -> Unit = {})` Add a listener to this Transition using the provided actions. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.doOnCancel(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been cancelled. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.doOnEnd(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has ended. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.doOnPause(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has been paused. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.doOnResume(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has resumed after a pause. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition.TransitionListener.md.txt) | `Transition.doOnStart(crossinline action: (transition: Transition) -> Unit)` Add an action which will be invoked when this transition has started. |

## androidx.core.util

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.util.AtomicFile](https://developer.android.com/reference/android/util/AtomicFile.md.txt)

|---|---|
| [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/) | `AtomicFile.readBytes()` Gets the entire content of this file as a byte array. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/) | `AtomicFile.readText(charset: Charset = Charsets.UTF_8)` Gets the entire content of this file as a String using UTF-8 or specified [charset](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$readText(android.util.AtomicFile, java.nio.charset.Charset)/charset). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.tryWrite(block: (out: FileOutputStream) -> Unit)` Perform the write operations inside [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$tryWrite(android.util.AtomicFile, kotlin.Function1((java.io.FileOutputStream, kotlin.Unit)))/block) on this file. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.writeBytes(array: ByteArray)` Sets the content of this file as an [array](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$writeBytes(android.util.AtomicFile, kotlin.ByteArray)/array) of bytes. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AtomicFile.writeText(text: String, charset: Charset = Charsets.UTF_8)` Sets the content of this file as [text](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$writeText(android.util.AtomicFile, kotlin.String, java.nio.charset.Charset)/text) encoded using UTF-8 or specified [charset](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$writeText(android.util.AtomicFile, kotlin.String, java.nio.charset.Charset)/charset). |

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.contains(key: Long)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$contains(android.util.LongSparseArray((androidx.core.util.contains.T)), kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.containsKey(key: Long)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsKey(android.util.LongSparseArray((androidx.core.util.containsKey.T)), kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsValue(android.util.LongSparseArray((androidx.core.util.containsValue.T)), androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.forEach(action: (key: Long, value: T) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$forEach(android.util.LongSparseArray((androidx.core.util.forEach.T)), kotlin.Function2((kotlin.Long, androidx.core.util.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `LongSparseArray<T>.getOrDefault(key: Long, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)), kotlin.Long, androidx.core.util.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)), kotlin.Long, androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `LongSparseArray<T>.getOrElse(key: Long, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)), kotlin.Long, kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `LongSparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.md.txt)\<T\> | `LongSparseArray<T>.plus(other: LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.LongSparseArray((androidx.core.util.plus.T)), android.util.LongSparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.putAll(other: LongSparseArray<T>)` Update this collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$putAll(android.util.LongSparseArray((androidx.core.util.putAll.T)), android.util.LongSparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `LongSparseArray<T>.remove(key: Long, value: T)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)), kotlin.Long, androidx.core.util.remove.T)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)), kotlin.Long, androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `LongSparseArray<T>.set(key: Long, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)\<T\> | `LongSparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.Pair](https://developer.android.com/reference/android/util/Pair.md.txt)

|---|---|
| operator F | `Pair<F, S>.component1()` Returns the first component of the pair. |
| operator S | `Pair<F, S>.component2()` Returns the second component of the pair. |
| [Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)\<F, S\> | `Pair<F, S>.toKotlinPair()` Returns this [Pair](https://developer.android.com/reference/android/util/Pair.md.txt) as a [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/). |

##### For [android.util.Range](https://developer.android.com/reference/android/util/Range.md.txt)

|---|---|
| infix [Range](https://developer.android.com/reference/android/util/Range.md.txt)\<T\> | `Range<T>.and(other: Range<T>)` Return the intersection of this range and [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$and(android.util.Range((androidx.core.util.and.T)), android.util.Range((androidx.core.util.and.T)))/other). |
| operator [Range](https://developer.android.com/reference/android/util/Range.md.txt)\<T\> | `Range<T>.plus(value: T)` Return the smallest range that includes this and [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)), androidx.core.util.plus.T)/value). |
| operator [Range](https://developer.android.com/reference/android/util/Range.md.txt)\<T\> | `Range<T>.plus(other: Range<T>)` Return the smallest range that includes this and [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)), android.util.Range((androidx.core.util.plus.T)))/other). |
| [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)\<T\> | `Range<T>.toClosedRange()` Returns this [Range](https://developer.android.com/reference/android/util/Range.md.txt) as a [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/). |

##### For [android.util.Size](https://developer.android.com/reference/android/util/Size.md.txt)

|---|---|
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Size.component1()` Returns "width", the first component of this [Size](https://developer.android.com/reference/android/util/Size.md.txt). |
| operator [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Size.component2()` Returns "height", the second component of this [Size](https://developer.android.com/reference/android/util/Size.md.txt). |

##### For [android.util.SizeF](https://developer.android.com/reference/android/util/SizeF.md.txt)

|---|---|
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `SizeF.component1()` Returns "width", the first component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.md.txt). |
| operator [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/) | `SizeF.component2()` Returns "height", the second component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.md.txt). |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.contains(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$contains(android.util.SparseArray((androidx.core.util.contains.T)), kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.containsKey(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsKey(android.util.SparseArray((androidx.core.util.containsKey.T)), kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.containsValue(value: T)` Returns true if the collection contains [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsValue(android.util.SparseArray((androidx.core.util.containsValue.T)), androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.forEach(action: (key: Int, value: T) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$forEach(android.util.SparseArray((androidx.core.util.forEach.T)), kotlin.Function2((kotlin.Int, androidx.core.util.forEach.T, kotlin.Unit)))/action) for each key/value entry. |
| T | `SparseArray<T>.getOrDefault(key: Int, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)), kotlin.Int, androidx.core.util.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)), kotlin.Int, androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `SparseArray<T>.getOrElse(key: Int, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)), kotlin.Int, kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseArray<T>.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseArray](https://developer.android.com/reference/android/util/SparseArray.md.txt)\<T\> | `SparseArray<T>.plus(other: SparseArray<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.SparseArray((androidx.core.util.plus.T)), android.util.SparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.putAll(other: SparseArray<T>)` Update this collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$putAll(android.util.SparseArray((androidx.core.util.putAll.T)), android.util.SparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseArray<T>.remove(key: Int, value: T)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)), kotlin.Int, androidx.core.util.remove.T)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)), kotlin.Int, androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseArray<T>.set(key: Int, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)\<T\> | `SparseArray<T>.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.contains(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$contains(android.util.SparseBooleanArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.containsKey(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsKey(android.util.SparseBooleanArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.containsValue(value: Boolean)` Returns true if the collection contains [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsValue(android.util.SparseBooleanArray, kotlin.Boolean)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.forEach(action: (key: Int, value: Boolean) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$forEach(android.util.SparseBooleanArray, kotlin.Function2((kotlin.Int, kotlin.Boolean, kotlin.Unit)))/action) for each key/value entry. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.getOrDefault(key: Int, defaultValue: Boolean)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.getOrElse(key: Int, defaultValue: () -> Boolean)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseBooleanArray, kotlin.Int, kotlin.Function0((kotlin.Boolean)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseBooleanArray, kotlin.Int, kotlin.Function0((kotlin.Boolean)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseBooleanArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.md.txt) | `SparseBooleanArray.plus(other: SparseBooleanArray)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.SparseBooleanArray, android.util.SparseBooleanArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.putAll(other: SparseBooleanArray)` Update this collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$putAll(android.util.SparseBooleanArray, android.util.SparseBooleanArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseBooleanArray.remove(key: Int, value: Boolean)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseBooleanArray, kotlin.Int, kotlin.Boolean)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseBooleanArray.set(key: Int, value: Boolean)` Allows the use of the index operator for storing values in the collection. |
| [BooleanIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-boolean-iterator/) | `SparseBooleanArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.contains(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$contains(android.util.SparseIntArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.containsKey(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsKey(android.util.SparseIntArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.containsValue(value: Int)` Returns true if the collection contains [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsValue(android.util.SparseIntArray, kotlin.Int)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.forEach(action: (key: Int, value: Int) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$forEach(android.util.SparseIntArray, kotlin.Function2((kotlin.Int, , kotlin.Unit)))/action) for each key/value entry. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.getOrDefault(key: Int, defaultValue: Int)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/defaultValue) when not present. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.getOrElse(key: Int, defaultValue: () -> Int)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseIntArray, kotlin.Int, kotlin.Function0((kotlin.Int)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseIntArray, kotlin.Int, kotlin.Function0((kotlin.Int)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseIntArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.md.txt) | `SparseIntArray.plus(other: SparseIntArray)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.SparseIntArray, android.util.SparseIntArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.putAll(other: SparseIntArray)` Update this collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$putAll(android.util.SparseIntArray, android.util.SparseIntArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseIntArray.remove(key: Int, value: Int)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/key) only if it is mapped to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseIntArray, kotlin.Int, kotlin.Int)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseIntArray.set(key: Int, value: Int)` Allows the use of the index operator for storing values in the collection. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseIntArray.valueIterator()` Return an iterator over the collection's values. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.contains(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$contains(android.util.SparseLongArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.containsKey(key: Int)` Returns true if the collection contains [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsKey(android.util.SparseLongArray, kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.containsValue(value: Long)` Returns true if the collection contains [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$containsValue(android.util.SparseLongArray, kotlin.Long)/value). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.forEach(action: (key: Int, value: Long) -> Unit)` Performs the given [action](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$forEach(android.util.SparseLongArray, kotlin.Function2((kotlin.Int, kotlin.Long, kotlin.Unit)))/action) for each key/value entry. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SparseLongArray.getOrDefault(key: Int, defaultValue: Long)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/key), or [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrDefault(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/defaultValue) when not present. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SparseLongArray.getOrElse(key: Int, defaultValue: () -> Long)` Return the value corresponding to [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseLongArray, kotlin.Int, kotlin.Function0((kotlin.Long)))/key), or from [defaultValue](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$getOrElse(android.util.SparseLongArray, kotlin.Int, kotlin.Function0((kotlin.Long)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.isEmpty()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.isNotEmpty()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-int-iterator/) | `SparseLongArray.keyIterator()` Return an iterator over the collection's keys. |
| operator [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.md.txt) | `SparseLongArray.plus(other: SparseLongArray)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$plus(android.util.SparseLongArray, android.util.SparseLongArray)/other). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.putAll(other: SparseLongArray)` Update this collection by adding or replacing entries from [other](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$putAll(android.util.SparseLongArray, android.util.SparseLongArray)/other). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SparseLongArray.remove(key: Int, value: Long)` Removes the entry for [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/key) only if it is set to [value](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$remove(android.util.SparseLongArray, kotlin.Int, kotlin.Long)/value). |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SparseLongArray.set(key: Int, value: Long)` Allows the use of the index operator for storing values in the collection. |
| [LongIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-long-iterator/) | `SparseLongArray.valueIterator()` Return an iterator over the collection's values. |

##### For [kotlin.Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.md.txt) | `Double.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.md.txt) instance representing given [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/). |

##### For [kotlin.Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.md.txt) | `Float.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.md.txt) instance representing given [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/). |

##### For [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/)

|---|---|
| [Pair](https://developer.android.com/reference/android/util/Pair.md.txt)\<F, S\> | `Pair<F, S>.toAndroidPair()` Returns this [kotlin.Pair](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/) as an Android [Pair](https://developer.android.com/reference/android/util/Pair.md.txt). |

##### For [kotlin.Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.md.txt) | `Short.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.md.txt) instance representing given [Short](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/). |

##### For [kotlin.String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.md.txt) | `String.toHalf()` Returns a [Half](https://developer.android.com/reference/android/util/Half.md.txt) instance representing given [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/). |

##### For [kotlin.ranges.ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/)

|---|---|
| [Range](https://developer.android.com/reference/android/util/Range.md.txt)\<T\> | `ClosedRange<T>.toRange()` Returns this [ClosedRange](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/-closed-range/) as a [Range](https://developer.android.com/reference/android/util/Range.md.txt). |

#### Extension properties

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `LongSparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseArray<T>.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseBooleanArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseIntArray.size()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SparseLongArray.size()` Returns the number of key/value entries in the collection. |

#### Top-level functions

|---|---|
| [LruCache](https://developer.android.com/reference/android/util/LruCache.md.txt)\<K, V\> | `lruCache(maxSize: Int, crossinline sizeOf: (key: K, value: V) -> Int = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: Boolean, key: K, oldValue: V, newValue: V?) -> Unit = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/android/util/LruCache.md.txt) with the given parameters. |
| infix [Range](https://developer.android.com/reference/android/util/Range.md.txt)\<T\> | `T.rangeTo(that: T)` Creates a range from this [Comparable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-comparable/) value to [that](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.util$rangeTo(androidx.core.util.rangeTo.T, androidx.core.util.rangeTo.T)/that). |

## androidx.core.view

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.contains(item: MenuItem)` Returns `true` if [item](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$contains(android.view.Menu, android.view.MenuItem)/item) is found in this menu. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.forEach(action: (item: MenuItem) -> Unit)` Performs the given action on each item in this menu. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.forEachIndexed(action: (index: Int, item: MenuItem) -> Unit)` Performs the given action on each item in this menu, providing its sequential index. |
| operator [MenuItem](https://developer.android.com/reference/android/view/MenuItem.md.txt) | `Menu.get(index: Int)` Returns the menu at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$get(android.view.Menu, kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.isEmpty()` Returns true if this menu contains no items. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Menu.isNotEmpty()` Returns true if this menu contains one or more items. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)\<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.md.txt)\> | `Menu.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the items in this menu. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Menu.minusAssign(item: MenuItem)` Removes [item](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$minusAssign(android.view.Menu, android.view.MenuItem)/item) from this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnAttach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is attached to a window. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnDetach(crossinline action: (view: View) -> Unit)` Performs the given action when this view is detached from a window. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is laid out. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.doOnNextLayout(crossinline action: (view: View) -> Unit)` Performs the given action when this view is next laid out. |
| [OneShotPreDrawListener](https://developer.android.com/reference/kotlin/androidx/core/view/OneShotPreDrawListener.md.txt) | `View.doOnPreDraw(crossinline action: (view: View) -> Unit)` Performs the given action when the view tree is about to be drawn. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) | `View.drawToBitmap(config: Config = Bitmap.Config.ARGB_8888)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.md.txt) representation of this [View](https://developer.android.com/reference/android/view/View.md.txt). |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.md.txt) | `View.postDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postDelayed](https://developer.android.com/reference/android/view/View.md.txt#postDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.md.txt) | `View.postOnAnimationDelayed(delayInMillis: Long, crossinline action: () -> Unit)` Version of [View.postOnAnimationDelayed](https://developer.android.com/reference/android/view/View.md.txt#postOnAnimationDelayed(java.lang.Runnable,%20long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.setPadding(@Px size: Int)` Sets the view's padding. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updateLayoutParams(block: LayoutParams.() -> Unit)` Executes [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$updateLayoutParams(android.view.View, kotlin.Function1((android.view.ViewGroup.LayoutParams, kotlin.Unit)))/block) with the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updateLayoutParams(block: T.() -> Unit)` Executes [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$updateLayoutParams(android.view.View, kotlin.Function1((androidx.core.view.updateLayoutParams.T, kotlin.Unit)))/block) with a typed version of the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updatePadding(@Px left: Int = paddingLeft, @Px top: Int = paddingTop, @Px right: Int = paddingRight, @Px bottom: Int = paddingBottom)` Updates this view's padding. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `View.updatePaddingRelative(@Px start: Int = paddingStart, @Px top: Int = paddingTop, @Px end: Int = paddingEnd, @Px bottom: Int = paddingBottom)` Updates this view's relative padding. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.contains(view: View)` Returns `true` if [view](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$contains(android.view.ViewGroup, android.view.View)/view) is found in this view group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.forEach(action: (view: View) -> Unit)` Performs the given action on each view in this view group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.forEachIndexed(action: (index: Int, view: View) -> Unit)` Performs the given action on each view in this view group, providing its sequential index. |
| operator [View](https://developer.android.com/reference/android/view/View.md.txt) | `ViewGroup.get(index: Int)` Returns the view at [index](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$get(android.view.ViewGroup, kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.isEmpty()` Returns true if this view group contains no views. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `ViewGroup.isNotEmpty()` Returns true if this view group contains one or more views. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)\<[View](https://developer.android.com/reference/android/view/View.md.txt)\> | `ViewGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the views in this view group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.minusAssign(view: View)` Removes [view](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$minusAssign(android.view.ViewGroup, android.view.View)/view) from this view group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `ViewGroup.plusAssign(view: View)` Adds [view](https://developer.android.com/kotlin/ktx/extensions-list#androidx.core.view$plusAssign(android.view.ViewGroup, android.view.View)/view) to this view group. |

##### For [android.view.ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.setMargins(@Px size: Int)` Sets the margins in the ViewGroup's MarginLayoutParams. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.updateMargins(@Px left: Int = leftMargin, @Px top: Int = topMargin, @Px right: Int = rightMargin, @Px bottom: Int = bottomMargin)` Updates the margins in the [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.md.txt)'s [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `MarginLayoutParams.updateMarginsRelative(@Px start: Int = marginStart, @Px top: Int = topMargin, @Px end: Int = marginEnd, @Px bottom: Int = bottomMargin)` Updates the relative margins in the ViewGroup's MarginLayoutParams. |

#### Extension properties

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.md.txt)

|---|---|
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)\<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.md.txt)\> | `Menu.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the items in this menu. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `Menu.size()` Returns the number of items in this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isGone()` Returns true when this view's visibility is [View.GONE](https://developer.android.com/reference/android/view/View.md.txt#GONE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isInvisible()` Returns true when this view's visibility is [View.INVISIBLE](https://developer.android.com/reference/android/view/View.md.txt#INVISIBLE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `View.isVisible()` Returns true when this view's visibility is [View.VISIBLE](https://developer.android.com/reference/android/view/View.md.txt#VISIBLE), false otherwise. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginBottom()` Returns the bottom margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginEnd()` Returns the end margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginLeft()` Returns the left margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginRight()` Returns the right margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginStart()` Returns the start margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `View.marginTop()` Returns the top margin if this view's [LayoutParams](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.md.txt) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams.md.txt), otherwise 0. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.md.txt)

|---|---|
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)\<[View](https://developer.android.com/reference/android/view/View.md.txt)\> | `ViewGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the child views in this view group. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `ViewGroup.size()` Returns the number of views in this view group. |

## androidx.core.widget

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.19.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.19.1")
}
```

#### Extension functions

##### For [android.widget.TextView](https://developer.android.com/reference/android/widget/TextView.md.txt)

|---|---|
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.md.txt) | `TextView.addTextChangedListener(crossinline beforeTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline onTextChanged: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit = { _, _, _, _ -> }, crossinline afterTextChanged: (text: Editable?) -> Unit = {})` Add a text changed listener to this TextView using the provided actions |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.md.txt) | `TextView.doAfterTextChanged(crossinline action: (text: Editable?) -> Unit)` Add an action which will be invoked after the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.md.txt) | `TextView.doBeforeTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked before the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.md.txt) | `TextView.doOnTextChanged(crossinline action: (text: CharSequence?, start: Int, count: Int, after: Int) -> Unit)` Add an action which will be invoked when the text is changing. |

## androidx.dynamicanimation.animation

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.dynamicanimation:dynamicanimation-ktx:"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.dynamicanimation:dynamicanimation-ktx:")
}
```

#### Extension functions

##### For [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation.md.txt)

|---|---|
| [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation.md.txt) | `SpringAnimation.withSpringForceProperties(func: SpringForce.() -> Unit)` Updates or applies spring force properties like [SpringForce.mDampingRatio](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce.md.txt#getDampingRatio()), [SpringForce.mFinalPosition](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce.md.txt#getFinalPosition()) and stiffness on SpringAnimation. |

#### Top-level functions

|---|---|
| [FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation.md.txt) | `flingAnimationOf(setter: (Float) -> Unit, getter: () -> Float)` Creates [FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation.md.txt) for a property that can be accessed via the provided setter and getter. |
| [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation.md.txt) | `springAnimationOf(setter: (Float) -> Unit, getter: () -> Float, finalPosition: Float = Float.NaN)` Creates [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation.md.txt) for a property that can be accessed via the provided setter and getter. |

## androidx.fragment.app

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.fragment:fragment-ktx:1.9.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.fragment:fragment-ktx:1.9.1")
}
```

#### Extension functions

##### For [android.view.View](https://developer.android.com/reference/android/view/View.md.txt)

|---|---|
| F | `View.findFragment()` Find a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt) associated with a [View](https://developer.android.com/reference/android/view/View.md.txt). |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt)

|---|---|
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)\<VM\> | `Fragment.activityViewModels(noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access parent activity's [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt), if [factoryProducer](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$activityViewModels(androidx.fragment.app.Fragment, kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory.md.txt) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt) first time. |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)\<VM\> | `Fragment.createViewModelLazy(viewModelClass: KClass<VM>, storeProducer: () -> ViewModelStore, factoryProducer: () -> ViewModelProvider.Factory = null)` Helper method for creation of [ViewModelLazy](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelLazy.md.txt), that resolves `null` passed as [factoryProducer](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$createViewModelLazy(androidx.fragment.app.Fragment, kotlin.reflect.KClass((androidx.fragment.app.createViewModelLazy.VM)), kotlin.Function0((androidx.lifecycle.ViewModelStore)), kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) to default factory. |
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)\<VM\> | `Fragment.viewModels(noinline ownerProducer: () -> ViewModelStoreOwner = { this }, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt) by **default** scoped to this [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt): |

##### For [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt)

|---|---|
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) | `FragmentTransaction.add(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.md.txt), inflating the Fragment's view into the container view specified by [containerViewId](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$add(androidx.fragment.app.FragmentTransaction, kotlin.Int, kotlin.String, android.os.Bundle)/containerViewId), to later retrieve via [FragmentManager.findFragmentById](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.md.txt#findFragmentById(int)). |
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) | `FragmentTransaction.add(tag: String, args: Bundle? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.md.txt) without adding the Fragment to any container view. |
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) | `FragmentTransaction.replace(@IdRes containerViewId: Int, tag: String? = null, args: Bundle? = null)` Replace an existing fragment that was added to a container. |

##### For [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.commit(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$commit(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.commitNow(allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$commitNow(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `FragmentManager.transaction(now: Boolean = false, allowStateLoss: Boolean = false, body: FragmentTransaction.() -> Unit)` Run [body](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app$transaction(androidx.fragment.app.FragmentManager, kotlin.Boolean, kotlin.Boolean, kotlin.Function1((androidx.fragment.app.FragmentTransaction, kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.md.txt) which is automatically committed if it completes without exception. |

## androidx.fragment.app.testing

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.fragment:fragment-testing:1.9.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.fragment:fragment-testing:1.9.1")
}
```

#### Top-level functions

|---|---|
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario.md.txt)\<F!\> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity.md.txt) using given [FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory.md.txt) and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario.md.txt)\<F!\> | `launchFragment(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity.md.txt) using [instantiate](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app.testing$launchFragment(android.os.Bundle, kotlin.Int, kotlin.Function0((androidx.fragment.app.testing.launchFragment.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario.md.txt)\<F!\> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: FragmentFactory? = null)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity.md.txt) and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario.md.txt)\<F!\> | `launchFragmentInContainer(fragmentArgs: Bundle? = null, @StyleRes themeResId: Int = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity.md.txt) using [instantiate](https://developer.android.com/kotlin/ktx/extensions-list#androidx.fragment.app.testing$launchFragmentInContainer(android.os.Bundle, kotlin.Int, kotlin.Function0((androidx.fragment.app.testing.launchFragmentInContainer.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |

## androidx.lifecycle

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.11.0"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.lifecycle:lifecycle-livedata-core-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.11.0")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.11.0")
}
```

#### Extension functions

##### For [kotlinx.coroutines.flow.Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<T\> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT)` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<T\> | `Flow<T>.asLiveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration)` Creates a LiveData that has values collected from the origin [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/). |

##### For [org.reactivestreams.Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary.md.txt#(org.reactivestreams.Publisher).toLiveData())

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<T\> | `Publisher<T>.toLiveData()` Creates an observable [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt) stream from a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary.md.txt#(org.reactivestreams.Publisher).toLiveData()). |

##### For [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)

|---|---|
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)\<T\> | `LiveData<T>.asFlow()` Creates a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) containing values dispatched by originating [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt): at the start a flow collector receives the latest value held by LiveData and then observes LiveData updates. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<X\> | `LiveData<X>.distinctUntilChanged()` Creates a new [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt) object does not emit a value until the source `this` LiveData value has been changed. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<Y\> | `LiveData<X>.map(crossinline transform: (X) -> Y)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt) mapped from `this` LiveData by applying [transform](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$map(androidx.lifecycle.LiveData((androidx.lifecycle.map.X)), kotlin.Function1((androidx.lifecycle.map.X, androidx.lifecycle.map.Y)))/transform) to each value set on `this` LiveData. |
| [Observer](https://developer.android.com/reference/kotlin/androidx/lifecycle/Observer.md.txt)\<T\> | `LiveData<T>.observe(owner: LifecycleOwner, crossinline onChanged: (T) -> Unit)` Adds the given [onChanged](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)), androidx.lifecycle.LifecycleOwner, kotlin.Function1((androidx.lifecycle.observe.T, kotlin.Unit)))/onChanged) lambda as an observer within the lifespan of the given [owner](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)), androidx.lifecycle.LifecycleOwner, kotlin.Function1((androidx.lifecycle.observe.T, kotlin.Unit)))/owner) and returns a reference to observer. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<Y\> | `LiveData<X>.switchMap(crossinline transform: (X) -> LiveData<Y>)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt) mapped from the input `this` `LiveData` by applying [transform](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$switchMap(androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.X)), kotlin.Function1((androidx.lifecycle.switchMap.X, androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.Y)))))/transform) to each value set on `this`. |
| Publisher\<T\> | `LiveData<T>.toPublisher(lifecycle: LifecycleOwner)` Adapts the given [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt) stream to a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary.md.txt#(org.reactivestreams.Publisher).toLiveData()). |

##### For [ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.md.txt)

|---|---|
| VM | `ViewModelProvider.get()` Returns an existing ViewModel or creates a new one in the scope (usually, a fragment or an activity), associated with this `ViewModelProvider`. |

##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)

|---|---|
| suspend T | `LifecycleOwner.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#CREATED) state. |
| suspend T | `LifecycleOwner.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#RESUMED) state. |
| suspend T | `LifecycleOwner.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#STARTED) state. |

##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt)

|---|---|
| suspend T | `Lifecycle.whenCreated(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#CREATED) state. |
| suspend T | `Lifecycle.whenResumed(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#RESUMED) state. |
| suspend T | `Lifecycle.whenStarted(block: suspend CoroutineScope.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State.md.txt#STARTED) state. |
| suspend T | `Lifecycle.whenStateAtLeast(minState: Lifecycle.State, block: suspend CoroutineScope.() -> T)` Runs the given [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/block) on a [CoroutineDispatcher](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/) that executes the [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/block) on the main thread and suspends the execution unless the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt)'s state is at least [minState](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle, androidx.lifecycle.Lifecycle.State, kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope, androidx.lifecycle.whenStateAtLeast.T)))/minState). |

#### Extension properties

##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt)

|---|---|
| [LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope.md.txt) | `Lifecycle.coroutineScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt). |

##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)

|---|---|
| [LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope.md.txt) | `LifecycleOwner.lifecycleScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.md.txt)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.md.txt). |

##### For [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt)

|---|---|
| [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) | `ViewModel.viewModelScope()` [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) tied to this [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt). |

#### Top-level functions

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<T\> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeoutInMs: Long = DEFAULT_TIMEOUT, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext, kotlin.Long, kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)), kotlin.Unit)))/block) that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope.md.txt). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<T\> | `liveData(context: CoroutineContext = EmptyCoroutineContext, timeout: Duration, block: suspend LiveDataScope<T>.() -> Unit)` Builds a LiveData that has values yielded from the given [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext, java.time.Duration, kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)), kotlin.Unit)))/block) that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope.md.txt). |

## androidx.navigation

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-runtime-ktx:2.10.2"
    implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
    implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-runtime-ktx:2.10.2")
    implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
    implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
}
```

#### Extension functions

##### For [android.app.Activity](https://developer.android.com/reference/android/app/Activity.md.txt)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) | `Activity.findNavController(@IdRes viewId: Int)` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) given the id of a View and its containing [Activity](https://developer.android.com/reference/android/app/Activity.md.txt). |
| [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy.md.txt)\<Args\> | `Activity.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Activity's extras as an Args instance. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.md.txt)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) | `View.findNavController()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) associated with a [View](https://developer.android.com/reference/android/view/View.md.txt). |

##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.activity(@IdRes id: Int, builder: ActivityNavigatorDestinationBuilder.() -> Unit)` Construct a new [ActivityNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Destination.md.txt) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.navigation(@IdRes id: Int, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a nested [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) |

##### For [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavGraph.contains(@IdRes id: Int)` Returns `true` if a destination with `id` is found in this navigation graph. |
| operator [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination.md.txt) | `NavGraph.get(@IdRes id: Int)` Returns the destination with `id`. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.minusAssign(node: NavDestination)` Removes `node` from this navigation graph. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.plusAssign(node: NavDestination)` Adds a destination to this NavGraph. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraph.plusAssign(other: NavGraph)` Add all destinations from another collection to this one. |

##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt)

|---|---|
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) | `NavController.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) |

##### For [NavHost](https://developer.android.com/reference/kotlin/androidx/navigation/NavHost.md.txt)

|---|---|
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) | `NavHost.createGraph(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) |

##### For [NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.md.txt)

|---|---|
| operator T | `NavigatorProvider.get(name: String)` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.md.txt) by name. |
| operator T | `NavigatorProvider.get(clazz: KClass<T>)` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.md.txt) using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name.md.txt). |
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) | `NavigatorProvider.navigation(@IdRes id: Int = 0, @IdRes startDestination: Int, builder: NavGraphBuilder.() -> Unit)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.md.txt) |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavigatorProvider.plusAssign(navigator: Navigator<out NavDestination>)` Register a navigator using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name.md.txt). |
| operator [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.md.txt)\<out [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination.md.txt)!\>? | `NavigatorProvider.set(name: String, navigator: Navigator<out NavDestination>)` Register a [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.md.txt) by name. |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt)

|---|---|
| [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/)\<VM\> | `Fragment.navGraphViewModels(@IdRes navGraphId: Int, noinline factoryProducer: () -> ViewModelProvider.Factory = null)` Returns a property delegate to access a [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.md.txt) scoped to a navigation graph present on the {@link NavController} back stack: |

#### Top-level functions

|---|---|
| [ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras.md.txt) | `ActivityNavigatorExtras(activityOptions: ActivityOptionsCompat? = null, flags: Int = 0)` Create a new [ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras.md.txt) instance with a specific [ActivityOptionsCompat](https://developer.android.com/reference/kotlin/androidx/core/app/ActivityOptionsCompat.md.txt) instance and/or any `Intent.FLAG_ACTIVITY_` flags. |
| [NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions.md.txt) | `navOptions(optionsBuilder: NavOptionsBuilder.() -> Unit)` Construct a new [NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions.md.txt) |

## androidx.navigation.fragment

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-fragment-ktx:2.10.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-fragment-ktx:2.10.2")
}
```

#### Extension functions

##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.dialog(@IdRes id: Int)` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination.md.txt) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.dialog(@IdRes id: Int, builder: DialogFragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination.md.txt) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.fragment(@IdRes id: Int)` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination.md.txt) |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavGraphBuilder.fragment(@IdRes id: Int, builder: FragmentNavigatorDestinationBuilder.() -> Unit)` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination.md.txt) |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) | `Fragment.findNavController()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) given a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.md.txt) |
| [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy.md.txt)\<Args\> | `Fragment.navArgs()` Returns a [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/) delegate to access the Fragment's arguments as an Args instance. |

#### Top-level functions

|---|---|
| [FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras.md.txt) | `FragmentNavigatorExtras(vararg sharedElements: Pair<View, String>)` Create a new [FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras.md.txt) instance with the given shared elements |

## androidx.navigation.ui

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-ui-ktx:2.10.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-ui-ktx:2.10.2")
}
```

#### Extension functions

##### For [android.view.MenuItem](https://developer.android.com/reference/android/view/MenuItem.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `MenuItem.onNavDestinationSelected(navController: NavController)` Attempt to navigate to the [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination.md.txt) associated with this [MenuItem](https://developer.android.com/reference/android/view/MenuItem.md.txt). |

##### For [androidx.appcompat.app.AppCompatActivity](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity.md.txt#getSupportActionBar()) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppCompatActivity.setupActionBarWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity.md.txt#getSupportActionBar()) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

##### For [androidx.appcompat.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Toolbar.setupWithNavController(navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `Toolbar.setupWithNavController(navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

##### For [com.google.android.material.appbar.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, drawerLayout: DrawerLayout?)` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `CollapsingToolbarLayout.setupWithNavController(toolbar: Toolbar, navController: NavController, configuration: AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

##### For [com.google.android.material.bottomnavigation.BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `BottomNavigationView.setupWithNavController(navController: NavController)` Sets up a [BottomNavigationView](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

##### For [com.google.android.material.navigation.NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView.md.txt)

|---|---|
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `NavigationView.setupWithNavController(navController: NavController)` Sets up a [NavigationView](https://developer.android.com/reference/com/google/android/material/navigation/NavigationView.md.txt) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavController.navigateUp(drawerLayout: DrawerLayout?)` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `NavController.navigateUp(appBarConfiguration: AppBarConfiguration)` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt). |

#### Top-level functions

|---|---|
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration.md.txt) | `AppBarConfiguration(navGraph: NavGraph, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI.md.txt) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar.md.txt). |
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration.md.txt) | `AppBarConfiguration(topLevelMenu: Menu, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI.md.txt) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar.md.txt). |
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration.md.txt) | `AppBarConfiguration(topLevelDestinationIds: Set<Int>, drawerLayout: DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> Boolean = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI.md.txt) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.md.txt), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/com/google/android/material/appbar/CollapsingToolbarLayout.md.txt), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/ActionBar.md.txt). |

## androidx.paging

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.paging:paging-common-ktx:2.1.2"
    implementation "androidx.paging:paging-runtime-ktx:2.1.2"
    implementation "androidx.paging:paging-rxjava2-ktx:2.1.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.paging:paging-common-ktx:2.1.2")
    implementation("androidx.paging:paging-runtime-ktx:2.1.2")
    implementation("androidx.paging:paging-rxjava2-ktx:2.1.2")
}
```

#### Extension functions

##### For [Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory.md.txt)

|---|---|
| Flowable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toFlowable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder.md.txt). |
| Flowable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toFlowable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder.md.txt). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toLiveData(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder.md.txt). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData.md.txt)\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toLiveData(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchExecutor: Executor = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder.md.txt). |
| Observable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toObservable(config: PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder.md.txt). |
| Observable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\>\> | `DataSource.Factory<Key, Value>.toObservable(pageSize: Int, initialLoadKey: Key? = null, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder.md.txt). |

#### Top-level functions

|---|---|
| [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config.md.txt) | `Config(pageSize: Int, prefetchDistance: Int = pageSize, enablePlaceholders: Boolean = true, initialLoadSizeHint: Int = pageSize * PagedList.Config.Builder.DEFAULT_INITIAL_PAGE_MULTIPLIER, maxSize: Int = PagedList.Config.MAX_SIZE_UNBOUNDED)` Constructs a [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config.md.txt), convenience for [PagedList.Config.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config.Builder.md.txt). |
| [PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt)\<Value\> | `PagedList(dataSource: DataSource<Key, Value>, config: PagedList.Config, notifyExecutor: Executor, fetchExecutor: Executor, boundaryCallback: PagedList.BoundaryCallback<Value>? = null, initialKey: Key? = null)` Constructs a [PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.md.txt), convenience for [PagedList.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Builder.md.txt). |

## androidx.palette.graphics

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.palette:palette-ktx:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.palette:palette-ktx:1.1.0")
}
```

#### Extension functions

##### For [Palette](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette.md.txt)

|---|---|
| operator [Palette.Swatch](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette.Swatch.md.txt)? | `Palette.get(target: Target)` Returns the selected swatch for the given target from the palette, or `null` if one could not be found. |

## androidx.preference

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.preference:preference-ktx:1.2.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.preference:preference-ktx:1.2.1")
}
```

#### Extension functions

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.md.txt)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.contains(preference: Preference)` Returns `true` if `preference` is found in this preference group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.forEach(action: (preference: Preference) -> Unit)` Performs the given action on each preference in this preference group. |
| [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.forEachIndexed(action: (index: Int, preference: Preference) -> Unit)` Performs the given action on each preference in this preference group, providing its sequential index. |
| operator T? | `PreferenceGroup.get(key: CharSequence)` Returns the preference with `key`, or `null` if no preference with `key` is found. |
| operator [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference.md.txt) | `PreferenceGroup.get(index: Int)` Returns the preference at `index`. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.isEmpty()` Returns true if this preference group contains no preferences. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `PreferenceGroup.isNotEmpty()` Returns true if this preference group contains one or more preferences. |
| operator [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/)\<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference.md.txt)\> | `PreferenceGroup.iterator()` Returns a [MutableIterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-iterator/) over the preferences in this preference group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.minusAssign(preference: Preference)` Removes `preference` from this preference group. |
| operator [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `PreferenceGroup.plusAssign(preference: Preference)` Adds `preference` to this preference group. |

#### Extension properties

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.md.txt)

|---|---|
| [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/)\<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference.md.txt)\> | `PreferenceGroup.children()` Returns a [Sequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/) over the preferences in this preference group. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `PreferenceGroup.size()` Returns the number of preferences in this preference group. |

## androidx.room

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.room:room-ktx:2.8.5"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.room:room-ktx:2.8.5")
}
```

#### Extension functions

##### For [RoomDatabase](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.md.txt)

|---|---|
| suspend R | `RoomDatabase.withTransaction(block: suspend () -> R)` Calls the specified suspending [block](https://developer.android.com/kotlin/ktx/extensions-list#androidx.room$withTransaction(androidx.room.RoomDatabase, kotlin.coroutines.SuspendFunction0((androidx.room.withTransaction.R)))/block) in a database transaction. |

## androidx.sqlite.db

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.sqlite:sqlite-ktx:2.7.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.sqlite:sqlite-ktx:2.7.1")
}
```

#### Extension functions

##### For [SupportSQLiteDatabase](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase.md.txt)

|---|---|
| T | `SupportSQLiteDatabase.transaction(exclusive: Boolean = true, body: SupportSQLiteDatabase.() -> T)` Run [body](https://developer.android.com/kotlin/ktx/extensions-list#androidx.sqlite.db$transaction(androidx.sqlite.db.SupportSQLiteDatabase, kotlin.Boolean, kotlin.Function1((androidx.sqlite.db.SupportSQLiteDatabase, androidx.sqlite.db.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.work

#### Dependency

#### Extension functions

##### For [com.google.common.util.concurrent.ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)

|---|---|
| suspend R | `ListenableFuture<R>.await()` Awaits for the completion of the [ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html) without blocking a thread. |

##### For [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation.md.txt)

|---|---|
| suspend [Operation.State.SUCCESS](https://developer.android.com/reference/kotlin/androidx/work/Operation.State.SUCCESS.md.txt)! | `Operation.await()` Awaits an [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation.md.txt) without blocking a thread. |

##### For [Data](https://developer.android.com/reference/kotlin/androidx/work/Data.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `Data.hasKeyWithValueOfType(key: String)` Returns true if the instance of [Data](https://developer.android.com/reference/kotlin/androidx/work/Data.md.txt) has a value corresponding to the given [key](https://developer.android.com/kotlin/ktx/extensions-list#androidx.work$hasKeyWithValueOfType(androidx.work.Data, kotlin.String)/key) with an expected type T. |

##### For [Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder.md.txt)

|---|---|
| [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder.md.txt) | `OneTimeWorkRequest.Builder.setInputMerger(@NonNull inputMerger: KClass<out InputMerger>)` Sets an [InputMerger](https://developer.android.com/reference/kotlin/androidx/work/InputMerger.md.txt) on the [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder.md.txt). |

#### Top-level functions

|---|---|
| [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder.md.txt) | `OneTimeWorkRequestBuilder()` Creates a [OneTimeWorkRequest](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.md.txt) with the given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker.md.txt). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker.md.txt). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) | `PeriodicWorkRequestBuilder(repeatInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker.md.txt). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) | `PeriodicWorkRequestBuilder(repeatInterval: Long, repeatIntervalTimeUnit: TimeUnit, flexTimeInterval: Long, flexTimeIntervalUnit: TimeUnit)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker.md.txt). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) | `PeriodicWorkRequestBuilder(repeatInterval: Duration, flexTimeInterval: Duration)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder.md.txt) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker.md.txt). |
| [Data](https://developer.android.com/reference/kotlin/androidx/work/Data.md.txt) | `workDataOf(vararg pairs: Pair<String, Any?>)` Converts a list of pairs to a [Data](https://developer.android.com/reference/kotlin/androidx/work/Data.md.txt) object. |

## androidx.work.testing

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.work:work-testing:2.12.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.work:work-testing:2.12.0")
}
```

#### Top-level functions

|---|---|
| [TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder.md.txt)\<W\> | `TestListenableWorkerBuilder(context: Context, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder.md.txt). |
| [TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder.md.txt)\<W\> | `TestWorkerBuilder(context: Context, executor: Executor, inputData: Data = Data.EMPTY, tags: List<String> = emptyList(), runAttemptCount: Int = 1, triggeredContentUris: List<Uri> = emptyList(), triggeredContentAuthorities: List<String> = emptyList())` Builds an instance of [TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder.md.txt). |

## com.google.android.play.core.ktx

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "com.google.android.play:core-ktx:1.8.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("com.google.android.play:core-ktx:1.8.1")
}
```

#### Extension functions

##### For [com.google.android.play.core.appupdate.AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.md.txt)

|---|---|
| suspend [AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.md.txt) | `AppUpdateManager.requestAppUpdateInfo()` Requests the update availability for the current app |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `AppUpdateManager.requestCompleteUpdate()` For a flexible update flow, triggers the completion of the update. |
| Flow\<[AppUpdateResult](https://developer.android.com/reference/com/google/android/play/core/ktx/AppUpdateResult.md.txt)\> | `AppUpdateManager.requestUpdateFlow()` Entry point for monitoring the availability and progress of updates. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateManager.startUpdateFlowForResult(appUpdateInfo: AppUpdateInfo, appUpdateType: Int, fragment: Fragment, requestCode: Int)` A version of [AppUpdateManager.startUpdateFlowForResult](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.md.txt#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo,%20int,%20android.app.Activity,%20int)) that accepts an AndroidX Fragment for returning the result. |

##### For [com.google.android.play.core.splitinstall.SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt)

|---|---|
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestCancelInstall(sessionId: Int)` Suspend version of [SplitInstallManager.cancelInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#cancelInstall(int)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredInstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#deferredInstall(java.util.List<java.lang.String>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredLanguageInstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#deferredLanguageInstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredLanguageUninstall(languages: List<Locale>)` Suspend version of [SplitInstallManager.deferredLanguageUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#deferredLanguageUninstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/) | `SplitInstallManager.requestDeferredUninstall(moduleNames: List<String>)` Suspend version of [SplitInstallManager.deferredUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#deferredUninstall(java.util.List<java.lang.String>)) |
| suspend [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallManager.requestInstall(modules: List<String> = listOf(), languages: List<String> = listOf())` Initiates installation of the requested modules/languages. |
| Flow\<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.md.txt)\> | `SplitInstallManager.requestProgressFlow()` Creates and returns a buffered [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) that will deliver all progress events for ongoing split installations. |
| suspend [SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.md.txt) | `SplitInstallManager.requestSessionState(sessionId: Int)` Suspend version of [SplitInstallManager.getSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#getSessionState(int)) |
| suspend [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)\<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.md.txt)\> | `SplitInstallManager.requestSessionStates()` Suspend version of [SplitInstallManager.getSessionStates](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#getSessionStates()) |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SplitInstallManager.startConfirmationDialogForResult(sessionState: SplitInstallSessionState, fragment: Fragment, requestCode: Int)` A version of [SplitInstallManager.startConfirmationDialogForResult](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.md.txt#startConfirmationDialogForResult(com.google.android.play.core.splitinstall.SplitInstallSessionState,%20android.app.Activity,%20int)) that accepts an AndroidX Fragment for returning the result. |

#### Extension properties

##### For [com.google.android.play.core.appupdate.AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.md.txt)

|---|---|
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `AppUpdateInfo.installStatus()` Returns the progress status of the update. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateInfo.isFlexibleUpdateAllowed()` Returns `true` if flexible update is allowed. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `AppUpdateInfo.isImmediateUpdateAllowed()` Returns `true` if immediate update is allowed. |

##### For [com.google.android.play.core.install.InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState.md.txt)

|---|---|
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `InstallState.hasTerminalStatus()` This signifies that this is a terminal status (there will be no more updates) and should be handled accordingly (success, cancellation or failure). |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `InstallState.installErrorCode()` Returns the error code for an install, or {@link InstallErrorCode#NO_ERROR}. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `InstallState.installStatus()` Returns the status of an install. |
| [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)! | `InstallState.packageName()` Returns the package name for the app being installed. |

##### For [com.google.android.play.core.splitinstall.SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.md.txt)

|---|---|
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SplitInstallSessionState.bytesDownloaded()` The bytes downloaded by this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.errorCode()` The error code of this update. |
| [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/) | `SplitInstallSessionState.hasTerminalStatus()` Signifies that this update is terminal, meaning there will be no more updates for this session. |
| [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)\<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)\> | `SplitInstallSessionState.languages()` The languages included by this update. |
| [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)\<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)\> | `SplitInstallSessionState.moduleNames()` The modules included by this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.sessionId()` The session id of this update. |
| [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/) | `SplitInstallSessionState.status()` The status code of this update. |
| [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/) | `SplitInstallSessionState.totalBytesToDownload()` The total bytes to download by this update. |

#### Top-level functions

|---|---|
| [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.md.txt) | `SplitInstallStateUpdatedListener(onRequiresConfirmation: (SplitInstallSessionState) -> Unit, onInstalled: (SplitInstallSessionState) -> Unit, onFailed: (SplitInstallSessionState) -> Unit = {}, onPending: (SplitInstallSessionState) -> Unit = {}, onDownloaded: (SplitInstallSessionState) -> Unit = {}, onDownloading: (SplitInstallSessionState) -> Unit = {}, onInstalling: (SplitInstallSessionState) -> Unit = {}, onCanceling: (SplitInstallSessionState) -> Unit = {}, onCanceled: (SplitInstallSessionState) -> Unit = {}, onNonTerminalStatus: (SplitInstallSessionState) -> Unit = {}, onTerminalStatus: (SplitInstallSessionState) -> Unit = {})` A convenience function for creating a [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.md.txt). |