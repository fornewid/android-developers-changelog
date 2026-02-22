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
    implementation "androidx.activity:activity-ktx:1.12.4"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.activity:activity-ktx:1.12.4")
}
```

#### Extension functions

##### For [OnBackPressedDispatcher](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedDispatcher)

|---|---|
| [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback) | `https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedDispatcher.https://developer.android.com/reference/kotlin/androidx/activity/package-summary#(androidx.activity.OnBackPressedDispatcher).addCallback(androidx.lifecycle.LifecycleOwner,%20kotlin.Boolean,%20kotlin.Function1)(owner: https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner? = null, enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true, onBackPressed: https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Create and add a new [OnBackPressedCallback](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback) that calls [onBackPressed](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#androidx.activity$addCallback(androidx.activity.OnBackPressedDispatcher,%20androidx.lifecycle.LifecycleOwner,%20kotlin.Boolean,%20kotlin.Function1((androidx.activity.OnBackPressedCallback,%20kotlin.Unit)))/onBackPressed) in [OnBackPressedCallback.handleOnBackPressed](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback#handleOnBackPressed()). |

##### For [ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)

|---|---|
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)\<VM\> | `https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity.https://developer.android.com/reference/kotlin/androidx/activity/package-summary#(androidx.activity.ComponentActivity).viewModels(kotlin.Function0)(noinline factoryProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory = null)` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the ComponentActivity's ViewModel, if [factoryProducer](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#androidx.activity$viewModels(androidx.activity.ComponentActivity,%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) first time. |

## androidx.benchmark

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.4.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.4.1")
}
```

#### Top-level functions

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/benchmark/package-summary#beginTraceSection(kotlin.String)(sectionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` <br /> |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/benchmark/package-summary#endTraceSection()()` <br /> |

## androidx.benchmark.junit4

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.benchmark:benchmark-junit4:1.4.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.benchmark:benchmark-junit4:1.4.1")
}
```

#### Extension functions

##### For [BenchmarkRule](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule.https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/package-summary#(androidx.benchmark.junit4.BenchmarkRule).measureRepeated(kotlin.Function1)(crossinline block: https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule.Scope.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Benchmark a block of code. |

## androidx.collection

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.collection:collection-ktx:1.5.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.collection:collection-ktx:1.5.0")
}
```

#### Extension functions

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).contains(kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$contains(androidx.collection.LongSparseArray((androidx.collection.contains.T)),%20kotlin.Long)/key). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$forEach(androidx.collection.LongSparseArray((androidx.collection.forEach.T)),%20kotlin.Function2((kotlin.Long,%20androidx.collection.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).getOrDefault(kotlin.Long,%20androidx.collection.getOrDefault.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)),%20kotlin.Long,%20androidx.collection.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.LongSparseArray((androidx.collection.getOrDefault.T)),%20kotlin.Long,%20androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).getOrElse(kotlin.Long,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.LongSparseArray((androidx.collection.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).isNotEmpty()()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).plus(androidx.collection.LongSparseArray)(other: https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$plus(androidx.collection.LongSparseArray((androidx.collection.plus.T)),%20androidx.collection.LongSparseArray((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).remove(kotlin.Long,%20androidx.collection.remove.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)),%20kotlin.Long,%20androidx.collection.remove.T)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.LongSparseArray((androidx.collection.remove.T)),%20kotlin.Long,%20androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).set(kotlin.Long,%20androidx.collection.set.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).contains(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$contains(androidx.collection.SparseArrayCompat((androidx.collection.contains.T)),%20kotlin.Int)/key). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$forEach(androidx.collection.SparseArrayCompat((androidx.collection.forEach.T)),%20kotlin.Function2((kotlin.Int,%20androidx.collection.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).getOrDefault(kotlin.Int,%20androidx.collection.getOrDefault.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)),%20kotlin.Int,%20androidx.collection.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrDefault(androidx.collection.SparseArrayCompat((androidx.collection.getOrDefault.T)),%20kotlin.Int,%20androidx.collection.getOrDefault.T)/defaultValue) when not present. |
| T | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).getOrElse(kotlin.Int,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.collection.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$getOrElse(androidx.collection.SparseArrayCompat((androidx.collection.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.collection.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).isNotEmpty()()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).keyIterator()()` Return an iterator over the collection's keys. |
| operator [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).plus(androidx.collection.SparseArrayCompat)(other: https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$plus(androidx.collection.SparseArrayCompat((androidx.collection.plus.T)),%20androidx.collection.SparseArrayCompat((androidx.collection.plus.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).remove(kotlin.Int,%20androidx.collection.remove.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)),%20kotlin.Int,%20androidx.collection.remove.T)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/collection/package-summary#androidx.collection$remove(androidx.collection.SparseArrayCompat((androidx.collection.remove.T)),%20kotlin.Int,%20androidx.collection.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).set(kotlin.Int,%20androidx.collection.set.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).valueIterator()()` Return an iterator over the collection's values. |

#### Extension properties

##### For [LongSparseArray](https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/LongSparseArray<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.LongSparseArray).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

##### For [SparseArrayCompat](https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/kotlin/androidx/collection/SparseArrayCompat<T>.https://developer.android.com/reference/kotlin/androidx/collection/package-summary#(androidx.collection.SparseArrayCompat).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

#### Top-level functions

|---|---|
| [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap)\<K, V\> | `https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arrayMapOf()()` Returns an empty new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap). |
| [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap)\<K, V\> | `https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arrayMapOf(kotlin.Pair)(vararg pairs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<K, V>)` Returns a new [ArrayMap](https://developer.android.com/reference/kotlin/androidx/collection/ArrayMap) with the specified contents, given as a list of pairs where the first component is the key and the second component is the value. |
| [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arraySetOf()()` Returns an empty new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet). |
| [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet)\<T\> | `https://developer.android.com/reference/kotlin/androidx/collection/package-summary#arraySetOf(androidx.collection.arraySetOf.T)(vararg values: T)` Returns a new [ArraySet](https://developer.android.com/reference/kotlin/androidx/collection/ArraySet) with the specified contents. |
| [LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache)\<K, V\> | `https://developer.android.com/reference/kotlin/androidx/collection/package-summary#lruCache(kotlin.Int,%20kotlin.Function2,%20kotlin.Function1,%20kotlin.Function4)(maxSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, crossinline sizeOf: (key: K, value: V) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: K, oldValue: V, newValue: V?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/kotlin/androidx/collection/LruCache) with the given parameters. |

## androidx.core.animation

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.animation.Animator](https://developer.android.com/reference/android/animation/Animator.html)

|---|---|
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).addListener(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1)(crossinline onEnd: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onStart: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onCancel: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onRepeat: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {})` Add a listener to this Animator using the provided actions. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).addPauseListener(kotlin.Function1,%20kotlin.Function1)(crossinline onResume: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onPause: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {})` Add a pause and resume listener to this Animator using the provided actions. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnCancel(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has been cancelled. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnEnd(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has ended. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnPause(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has been paused. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnRepeat(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has repeated. |
| [AnimatorPauseListener](https://developer.android.com/reference/android/animation/Animator/AnimatorPauseListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnResume(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has resumed after a pause. |
| [AnimatorListener](https://developer.android.com/reference/android/animation/Animator/AnimatorListener.html) | `https://developer.android.com/reference/android/animation/Animator.html.https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary#(android.animation.Animator).doOnStart(kotlin.Function1)(crossinline action: (animator: https://developer.android.com/reference/android/animation/Animator.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the animation has started. |

## androidx.core.content

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.content.Context](https://developer.android.com/reference/android/content/Context.html)

|---|---|
| T? | `https://developer.android.com/reference/android/content/Context.html.https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#(android.content.Context).getSystemService()()` Return the handle to a system-level service by class. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/content/Context.html.https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#(android.content.Context).withStyledAttributes(android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(set: https://developer.android.com/reference/android/util/AttributeSet.html? = null, attrs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html, @AttrRes defStyleAttr: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, @StyleRes defStyleRes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, block: https://developer.android.com/reference/android/content/res/TypedArray.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Executes [block](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#androidx.core.content$withStyledAttributes(android.content.Context,%20android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.content.res.TypedArray,%20kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html) receiver. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/content/Context.html.https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#(android.content.Context).withStyledAttributes(kotlin.Int,%20kotlin.IntArray,%20kotlin.Function1)(@StyleRes resourceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, attrs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html, block: https://developer.android.com/reference/android/content/res/TypedArray.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Executes [block](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#androidx.core.content$withStyledAttributes(android.content.Context,%20kotlin.Int,%20kotlin.IntArray,%20kotlin.Function1((android.content.res.TypedArray,%20kotlin.Unit)))/block) on a [TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html) receiver. |

##### For [android.content.SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/content/SharedPreferences.html.https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#(android.content.SharedPreferences).edit(kotlin.Boolean,%20kotlin.Function1)(commit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false, action: https://developer.android.com/reference/android/content/SharedPreferences/Editor.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Allows editing of this preference instance with a call to [apply](https://developer.android.com/reference/android/content/SharedPreferences/Editor.html#apply()) or [commit](https://developer.android.com/reference/android/content/SharedPreferences/Editor.html#commit()) to persist the changes. |

#### Top-level functions

|---|---|
| [ContentValues](https://developer.android.com/reference/android/content/ContentValues.html) | `https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#contentValuesOf(kotlin.Pair)(vararg pairs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Returns a new [ContentValues](https://developer.android.com/reference/android/content/ContentValues.html) with the given key/value pairs as elements. |

## androidx.core.content.res

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.content.res.TypedArray](https://developer.android.com/reference/android/content/res/TypedArray.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getBooleanOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the boolean value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getBooleanOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getColorOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the color value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getColorOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getColorStateListOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the color state list value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getColorStateListOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getDimensionOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the dimension value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getDimensionPixelOffsetOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the dimension pixel offset value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionPixelOffsetOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getDimensionPixelSizeOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the dimension pixel size value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDimensionPixelSizeOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getDrawableOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the drawable value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getDrawableOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getFloatOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the float value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getFloatOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Typeface](https://developer.android.com/reference/android/graphics/Typeface.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getFontOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the font value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getFontOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getIntOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the integer value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getIntOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getIntegerOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the integer value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getIntegerOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getResourceIdOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieves the resource identifier for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getResourceIdOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getStringOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the string value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getStringOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)\<[CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)\> | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getTextArrayOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the text array value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getTextArrayOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).getTextOrThrow(kotlin.Int)(@StyleableRes index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Retrieve the text value for the attribute at [index](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$getTextOrThrow(android.content.res.TypedArray,%20kotlin.Int)/index) or throws [IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) if not defined. |
| R | `https://developer.android.com/reference/android/content/res/TypedArray.html.https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#(android.content.res.TypedArray).use(kotlin.Function1)(block: (https://developer.android.com/reference/android/content/res/TypedArray.html) -> R)` Executes the given [block](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary#androidx.core.content.res$use(android.content.res.TypedArray,%20kotlin.Function1((android.content.res.TypedArray,%20androidx.core.content.res.use.R)))/block) function on this TypedArray and then recycles it. |

## androidx.core.database

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.database.Cursor](https://developer.android.com/reference/android/database/Cursor.html)

|---|---|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getBlobOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable byte array. |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getDoubleOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable double. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getFloatOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable float. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getIntOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable integer. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getLongOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable long. |
| [Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getShortOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable short. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)? | `https://developer.android.com/reference/android/database/Cursor.html.https://developer.android.com/reference/kotlin/androidx/core/database/package-summary#(android.database.Cursor).getStringOrNull(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the requested column as a nullable string. |

## androidx.core.database.sqlite

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.database.sqlite.SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html)

|---|---|
| T | `https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html.https://developer.android.com/reference/kotlin/androidx/core/database/sqlite/package-summary#(android.database.sqlite.SQLiteDatabase).transaction(kotlin.Boolean,%20kotlin.Function1)(exclusive: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true, body: https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html.() -> T)` Run [body](https://developer.android.com/reference/kotlin/androidx/core/database/sqlite/package-summary#androidx.core.database.sqlite$transaction(android.database.sqlite.SQLiteDatabase,%20kotlin.Boolean,%20kotlin.Function1((android.database.sqlite.SQLiteDatabase,%20androidx.core.database.sqlite.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.core.graphics

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).applyCanvas(kotlin.Function1)(block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.html) to draw on this bitmap and executes the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$applyCanvas(android.graphics.Bitmap,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) on the newly created canvas. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).contains(android.graphics.Point)(p: https://developer.android.com/reference/android/graphics/Point.html)` Returns true if the specified point is inside the bitmap. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).contains(android.graphics.PointF)(p: https://developer.android.com/reference/android/graphics/PointF.html)` Returns true if the specified point is inside the bitmap. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).get(kotlin.Int,%20kotlin.Int)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the value of the pixel at the specified location. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).scale(kotlin.Int,%20kotlin.Int,%20kotlin.Boolean)(width: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, height: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, filter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true)` Creates a new bitmap, scaled from this bitmap, when possible. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Bitmap).set(kotlin.Int,%20kotlin.Int,%20kotlin.Int)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, color: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Writes the specified [color int](https://developer.android.com/reference/android/graphics/Color.html) into the bitmap (assuming it is mutable) at the specified `(x, y)` coordinate. |

##### For [android.graphics.Canvas](https://developer.android.com/reference/android/graphics/Canvas.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withClip(android.graphics.Rect,%20kotlin.Function1)(clipRect: https://developer.android.com/reference/android/graphics/Rect.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.Rect,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withClip(android.graphics.RectF,%20kotlin.Function1)(clipRect: https://developer.android.com/reference/android/graphics/RectF.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.RectF,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withClip(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(left: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withClip(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1)(left: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipRect](https://developer.android.com/reference/android/graphics/Canvas.html#clipRect(android.graphics.RectF, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withClip(android.graphics.Path,%20kotlin.Function1)(clipPath: https://developer.android.com/reference/android/graphics/Path.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withClip(android.graphics.Canvas,%20android.graphics.Path,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.clipPath](https://developer.android.com/reference/android/graphics/Canvas.html#clipPath(android.graphics.Path, android.graphics.Region.Op)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withMatrix(android.graphics.Matrix,%20kotlin.Function1)(matrix: https://developer.android.com/reference/android/graphics/Matrix.html = Matrix(), block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withMatrix(android.graphics.Canvas,%20android.graphics.Matrix,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.concat](https://developer.android.com/reference/android/graphics/Canvas.html#concat(android.graphics.Matrix)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withRotation(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1)(degrees: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, pivotX: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, pivotY: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withRotation(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.rotate](https://developer.android.com/reference/android/graphics/Canvas.html#rotate(float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withSave(kotlin.Function1)(block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withSave(android.graphics.Canvas,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save()) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withScale(kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 1.0f, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 1.0f, pivotX: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, pivotY: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withScale(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.scale](https://developer.android.com/reference/android/graphics/Canvas.html#scale(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withSkew(kotlin.Float,%20kotlin.Float,%20kotlin.Function1)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withSkew(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.skew](https://developer.android.com/reference/android/graphics/Canvas.html#skew(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Canvas.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Canvas).withTranslation(kotlin.Float,%20kotlin.Float,%20kotlin.Function1)(x: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, y: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$withTranslation(android.graphics.Canvas,%20kotlin.Float,%20kotlin.Float,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) in calls to [Canvas.save](https://developer.android.com/reference/android/graphics/Canvas.html#save())/[Canvas.translate](https://developer.android.com/reference/android/graphics/Canvas.html#translate(float, float)) and [Canvas.restoreToCount](https://developer.android.com/reference/android/graphics/Canvas.html#restoreToCount(int)). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.html)

|---|---|
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).component1()()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).component2()()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).component3()()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).component4()()` Returns the fourth component of the color. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.html)! | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).convertTo(android.graphics.ColorSpace.Named)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace/Named.html)` Converts the color receiver to a color in the specified color space. |
| infix [Color](https://developer.android.com/reference/android/graphics/Color.html)! | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).convertTo(android.graphics.ColorSpace)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace.html)` Converts the color receiver to a color in the specified color space. |
| operator [Color](https://developer.android.com/reference/android/graphics/Color.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Color).plus(android.graphics.Color)(c: https://developer.android.com/reference/android/graphics/Color.html)` Composites two translucent colors together. |

##### For [android.graphics.ImageDecoder.Source](https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.ImageDecoder.Source).decodeBitmap(kotlin.Function3)(crossinline action: https://developer.android.com/reference/android/graphics/ImageDecoder.html.(info: https://developer.android.com/reference/android/graphics/ImageDecoder/ImageInfo.html, source: https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Create a Bitmap from a Source |
| [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html) | `https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.ImageDecoder.Source).decodeDrawable(kotlin.Function3)(crossinline action: https://developer.android.com/reference/android/graphics/ImageDecoder.html.(info: https://developer.android.com/reference/android/graphics/ImageDecoder/ImageInfo.html, source: https://developer.android.com/reference/android/graphics/ImageDecoder/Source.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Create a Drawable from a Source |

##### For [android.graphics.Matrix](https://developer.android.com/reference/android/graphics/Matrix.html)

|---|---|
| operator [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `https://developer.android.com/reference/android/graphics/Matrix.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Matrix).times(android.graphics.Matrix)(m: https://developer.android.com/reference/android/graphics/Matrix.html)` Multiplies this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) by another matrix and returns the result as a new matrix. |
| [FloatArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float-array/index.html) | `https://developer.android.com/reference/android/graphics/Matrix.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Matrix).values()()` Returns the 9 values of this [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) as a new array of floats. |

##### For [android.graphics.Paint](https://developer.android.com/reference/android/graphics/Paint.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/Paint.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Paint).setBlendMode(androidx.core.graphics.BlendModeCompat)(blendModeCompat: https://developer.android.com/reference/kotlin/androidx/core/graphics/BlendModeCompat?)` Convenience method to configure the BlendMode of a Paint in a backward compatible way. |

##### For [android.graphics.Path](https://developer.android.com/reference/android/graphics/Path.html)

|---|---|
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).and(android.graphics.Path)(p: https://developer.android.com/reference/android/graphics/Path.html)` Returns the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| [Iterable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html)\<[PathSegment](https://developer.android.com/reference/kotlin/androidx/core/graphics/PathSegment)\> | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).flatten(kotlin.Float)(error: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.5f)` Flattens (or approximate) the [Path](https://developer.android.com/reference/android/graphics/Path.html) with a series of line segments. |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.html) | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).minus(android.graphics.Path)(p: https://developer.android.com/reference/android/graphics/Path.html)` Returns the difference of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).or(android.graphics.Path)(p: https://developer.android.com/reference/android/graphics/Path.html)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| operator [Path](https://developer.android.com/reference/android/graphics/Path.html) | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).plus(android.graphics.Path)(p: https://developer.android.com/reference/android/graphics/Path.html)` Returns the union of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |
| infix [Path](https://developer.android.com/reference/android/graphics/Path.html) | `https://developer.android.com/reference/android/graphics/Path.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Path).xor(android.graphics.Path)(p: https://developer.android.com/reference/android/graphics/Path.html)` Returns the union minus the intersection of two paths as a new [Path](https://developer.android.com/reference/android/graphics/Path.html). |

##### For [android.graphics.Picture](https://developer.android.com/reference/android/graphics/Picture.html)

|---|---|
| [Picture](https://developer.android.com/reference/android/graphics/Picture.html) | `https://developer.android.com/reference/android/graphics/Picture.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Picture).record(kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(width: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, height: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, block: https://developer.android.com/reference/android/graphics/Canvas.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a new [Canvas](https://developer.android.com/reference/android/graphics/Canvas.html) to record commands in this [Picture](https://developer.android.com/reference/android/graphics/Picture.html), executes the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$record(android.graphics.Picture,%20kotlin.Int,%20kotlin.Int,%20kotlin.Function1((android.graphics.Canvas,%20kotlin.Unit)))/block) on the newly created canvas and returns this [Picture](https://developer.android.com/reference/android/graphics/Picture.html). |

##### For [android.graphics.Point](https://developer.android.com/reference/android/graphics/Point.html)

|---|---|
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).component1()()` Returns the x coordinate of this point. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).component2()()` Returns the y coordinate of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).minus(android.graphics.Point)(p: https://developer.android.com/reference/android/graphics/Point.html)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).minus(kotlin.Int)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).plus(android.graphics.Point)(p: https://developer.android.com/reference/android/graphics/Point.html)` Offsets this point by the specified point and returns the result as a new point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).plus(kotlin.Int)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).toPointF()()` Returns a [PointF](https://developer.android.com/reference/android/graphics/PointF.html) representation of this point. |
| operator [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/Point.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Point).unaryMinus()()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PointF](https://developer.android.com/reference/android/graphics/PointF.html)

|---|---|
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).component1()()` Returns the x coordinate of this point. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).component2()()` Returns the y coordinate of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).minus(android.graphics.PointF)(p: https://developer.android.com/reference/android/graphics/PointF.html)` Offsets this point by the negation of the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).minus(kotlin.Float)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Offsets this point by the negation of the specified amount on both X and Y axis and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).plus(android.graphics.PointF)(p: https://developer.android.com/reference/android/graphics/PointF.html)` Offsets this point by the specified point and returns the result as a new point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).plus(kotlin.Float)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Offsets this point by the specified amount on both X and Y axis and returns the result as a new point. |
| [Point](https://developer.android.com/reference/android/graphics/Point.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).toPoint()()` Returns a [Point](https://developer.android.com/reference/android/graphics/Point.html) representation of this point. |
| operator [PointF](https://developer.android.com/reference/android/graphics/PointF.html) | `https://developer.android.com/reference/android/graphics/PointF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PointF).unaryMinus()()` Returns a new point representing the negation of this point. |

##### For [android.graphics.PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html)

|---|---|
| [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.html) | `https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PorterDuff.Mode).toColorFilter(kotlin.Int)(color: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates a new [PorterDuffColorFilter](https://developer.android.com/reference/android/graphics/PorterDuffColorFilter.html) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html) as the alpha compositing or blending mode, and the specified [color](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$toColorFilter(android.graphics.PorterDuff.Mode,%20kotlin.Int)/color). |
| [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.html) | `https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.PorterDuff.Mode).toXfermode()()` Creates a new [PorterDuffXfermode](https://developer.android.com/reference/android/graphics/PorterDuffXfermode.html) that uses this [PorterDuff.Mode](https://developer.android.com/reference/android/graphics/PorterDuff/Mode.html) as the alpha compositing or blending mode. |

##### For [android.graphics.Rect](https://developer.android.com/reference/android/graphics/Rect.html)

|---|---|
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).and(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).component1()()` Returns "left", the first component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).component2()()` Returns "top", the second component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).component3()()` Returns "right", the third component of the rectangle. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).component4()()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).contains(android.graphics.Point)(p: https://developer.android.com/reference/android/graphics/Point.html)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).minus(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).minus(kotlin.Int)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).minus(android.graphics.Point)(xy: https://developer.android.com/reference/android/graphics/Point.html)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).or(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Returns the union of two rectangles as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).plus(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).plus(kotlin.Int)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).plus(android.graphics.Point)(xy: https://developer.android.com/reference/android/graphics/Point.html)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).times(kotlin.Int)(factor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.Rect,%20kotlin.Int)/factor). |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).toRectF()()` Returns a [RectF](https://developer.android.com/reference/android/graphics/RectF.html) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).toRegion()()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.html) representation of this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Rect.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Rect).xor(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.RectF](https://developer.android.com/reference/android/graphics/RectF.html)

|---|---|
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).and(android.graphics.RectF)(r: https://developer.android.com/reference/android/graphics/RectF.html)` Returns the intersection of two rectangles as a new rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).component1()()` Returns "left", the first component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).component2()()` Returns "top", the second component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).component3()()` Returns "right", the third component of the rectangle. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).component4()()` Returns "bottom", the fourth component of the rectangle. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).contains(android.graphics.PointF)(p: https://developer.android.com/reference/android/graphics/PointF.html)` Returns true if the specified point is inside the rectangle. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).minus(android.graphics.RectF)(r: https://developer.android.com/reference/android/graphics/RectF.html)` Returns the difference of this rectangle and the specified rectangle as a new region. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).minus(kotlin.Float)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Returns a new rectangle representing this rectangle offset by the negation of the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).minus(android.graphics.PointF)(xy: https://developer.android.com/reference/android/graphics/PointF.html)` Returns a new rectangle representing this rectangle offset by the negation of the specified point. |
| infix [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).or(android.graphics.RectF)(r: https://developer.android.com/reference/android/graphics/RectF.html)` Returns the union of two rectangles as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).plus(android.graphics.RectF)(r: https://developer.android.com/reference/android/graphics/RectF.html)` Performs the union of this rectangle and the specified rectangle and returns the result as a new rectangle. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).plus(kotlin.Float)(xy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Returns a new rectangle representing this rectangle offset by the specified amount on both X and Y axis. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).plus(android.graphics.PointF)(xy: https://developer.android.com/reference/android/graphics/PointF.html)` Returns a new rectangle representing this rectangle offset by the specified point. |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).times(kotlin.Int)(factor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.RectF,%20kotlin.Int)/factor). |
| operator [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).times(kotlin.Float)(factor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Returns a new rectangle representing this rectangle's components each scaled by [factor](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$times(android.graphics.RectF,%20kotlin.Float)/factor). |
| [Rect](https://developer.android.com/reference/android/graphics/Rect.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).toRect()()` Returns a [Rect](https://developer.android.com/reference/android/graphics/Rect.html) representation of this rectangle. |
| [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).toRegion()()` Returns a [Region](https://developer.android.com/reference/android/graphics/Region.html) representation of this rectangle. |
| [RectF](https://developer.android.com/reference/android/graphics/RectF.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).transform(android.graphics.Matrix)(m: https://developer.android.com/reference/android/graphics/Matrix.html)` Transform this rectangle in place using the supplied [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) and returns this rectangle. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/RectF.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.RectF).xor(android.graphics.RectF)(r: https://developer.android.com/reference/android/graphics/RectF.html)` Returns the union minus the intersection of two rectangles as a new region. |

##### For [android.graphics.Region](https://developer.android.com/reference/android/graphics/Region.html)

|---|---|
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).and(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Return the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).and(android.graphics.Region)(r: https://developer.android.com/reference/android/graphics/Region.html)` Return the intersection of this region and the specified region as a new region. |
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).contains(android.graphics.Point)(p: https://developer.android.com/reference/android/graphics/Point.html)` Return true if the region contains the specified [Point](https://developer.android.com/reference/android/graphics/Point.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).forEach(kotlin.Function1)(action: (rect: https://developer.android.com/reference/android/graphics/Rect.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each rect in this region. |
| operator [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)\<[Rect](https://developer.android.com/reference/android/graphics/Rect.html)\> | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).iterator()()` Returns an [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html) over the rects in this region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).minus(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Return the difference of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).minus(android.graphics.Region)(r: https://developer.android.com/reference/android/graphics/Region.html)` Return the difference of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).not()()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).or(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).or(android.graphics.Region)(r: https://developer.android.com/reference/android/graphics/Region.html)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).plus(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Return the union of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).plus(android.graphics.Region)(r: https://developer.android.com/reference/android/graphics/Region.html)` Return the union of this region and the specified region as a new region. |
| operator [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).unaryMinus()()` Returns the negation of this region as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).xor(android.graphics.Rect)(r: https://developer.android.com/reference/android/graphics/Rect.html)` Return the union minus the intersection of this region and the specified [Rect](https://developer.android.com/reference/android/graphics/Rect.html) as a new region. |
| infix [Region](https://developer.android.com/reference/android/graphics/Region.html) | `https://developer.android.com/reference/android/graphics/Region.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Region).xor(android.graphics.Region)(r: https://developer.android.com/reference/android/graphics/Region.html)` Return the union minus the intersection of this region and the specified region as a new region. |

##### For [android.graphics.Shader](https://developer.android.com/reference/android/graphics/Shader.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/Shader.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(android.graphics.Shader).transform(kotlin.Function1)(block: https://developer.android.com/reference/android/graphics/Matrix.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$transform(android.graphics.Shader,%20kotlin.Function1((android.graphics.Matrix,%20kotlin.Unit)))/block) in calls to [Shader.getLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.html#getLocalMatrix(android.graphics.Matrix)) and [Shader.setLocalMatrix](https://developer.android.com/reference/android/graphics/Shader.html#setLocalMatrix(android.graphics.Matrix)). |

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|---|---|
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).component1()()` Return the alpha component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).component2()()` Return the red component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).component3()()` Return the green component of a color int. |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).component4()()` Return the blue component of a color int. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).convertTo(android.graphics.ColorSpace.Named)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace/Named.html)` Converts the color int receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).convertTo(android.graphics.ColorSpace)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace.html)` Converts the color int receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).toColor()()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.html) instance from a color int. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).toColorLong()()` Converts the specified ARGB [color int](https://developer.android.com/reference/android/graphics/Color.html) to an RGBA [color long](https://developer.android.com/reference/android/graphics/Color.html) in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace/Named.html#SRGB) color space. |

##### For [kotlin.Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)

|---|---|
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).component1()()` Returns the first component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).component2()()` Returns the second component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).component3()()` Returns the third component of the color. |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).component4()()` Returns the fourth component of the color. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).convertTo(android.graphics.ColorSpace.Named)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace/Named.html)` Converts the color long receiver to a color long in the specified color space. |
| infix [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).convertTo(android.graphics.ColorSpace)(colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace.html)` Converts the color long receiver to a color long in the specified color space. |
| [Color](https://developer.android.com/reference/android/graphics/Color.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).toColor()()` Creates a new [Color](https://developer.android.com/reference/android/graphics/Color.html) instance from a [color long](https://developer.android.com/reference/android/graphics/Color.html). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).toColorInt()()` Converts the specified [color long](https://developer.android.com/reference/android/graphics/Color.html) to an ARGB [color int](https://developer.android.com/reference/android/graphics/Color.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.String).toColorInt()()` Return a corresponding [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) color of this [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html). |

#### Extension properties

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).alpha:kotlin.Int()` Return the alpha component of a color int. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).blue:kotlin.Int()` Return the blue component of a color int. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).green:kotlin.Int()` Return the green component of a color int. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).luminance:kotlin.Float()` Returns the relative luminance of a color int, assuming sRGB encoding. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Int).red:kotlin.Int()` Return the red component of a color int. |

##### For [kotlin.Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)

|---|---|
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).alpha:kotlin.Float()` Return the alpha component of a color long. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).blue:kotlin.Float()` Return the blue component of a color long. |
| [ColorSpace](https://developer.android.com/reference/android/graphics/ColorSpace.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).colorSpace:android.graphics.ColorSpace()` Returns the color space encoded in the specified color long. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).green:kotlin.Float()` Return the green component of a color long. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).isSrgb:kotlin.Boolean()` Indicates whether the color is in the [sRGB](https://developer.android.com/reference/android/graphics/ColorSpace/Named.html#SRGB) color space. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).isWideGamut:kotlin.Boolean()` Indicates whether the color is in a [wide-gamut](https://developer.android.com/reference/android/graphics/ColorSpace.html) color space. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).luminance:kotlin.Float()` Returns the relative luminance of a color. |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#(kotlin.Long).red:kotlin.Float()` Return the red component of a color long. |

#### Top-level functions

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)(width: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, height: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, config: https://developer.android.com/reference/android/graphics/Bitmap/Config.html = Bitmap.Config.ARGB_8888)` Returns a mutable bitmap with the specified [width](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)/width) and [height](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)/height). |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace)(width: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, height: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, config: https://developer.android.com/reference/android/graphics/Bitmap/Config.html = Bitmap.Config.ARGB_8888, hasAlpha: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true, colorSpace: https://developer.android.com/reference/android/graphics/ColorSpace.html = ColorSpace.get(ColorSpace.Named.SRGB))` Returns a mutable bitmap with the specified [width](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace)/width) and [height](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$createBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config,%20kotlin.Boolean,%20android.graphics.ColorSpace)/height). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#rotationMatrix(kotlin.Float,%20kotlin.Float,%20kotlin.Float)(degrees: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, px: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, py: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f)` Creates a rotation matrix, defined by a rotation angle in degrees around the pivot point located at the coordinates ([px](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$rotationMatrix(kotlin.Float,%20kotlin.Float,%20kotlin.Float)/px), [py](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$rotationMatrix(kotlin.Float,%20kotlin.Float,%20kotlin.Float)/py)). |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#scaleMatrix(kotlin.Float,%20kotlin.Float)(sx: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 1.0f, sy: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 1.0f)` Creates a scale matrix with the scale factor [sx](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$scaleMatrix(kotlin.Float,%20kotlin.Float)/sx) and [sy](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$scaleMatrix(kotlin.Float,%20kotlin.Float)/sy) respectively on the `x` and `y` axis. |
| [Matrix](https://developer.android.com/reference/android/graphics/Matrix.html) | `https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#translationMatrix(kotlin.Float,%20kotlin.Float)(tx: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f, ty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = 0.0f)` Creates a translation matrix with the translation amounts [tx](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$translationMatrix(kotlin.Float,%20kotlin.Float)/tx) and [ty](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary#androidx.core.graphics$translationMatrix(kotlin.Float,%20kotlin.Float)/ty) respectively on the `x` and `y` axis. |

## androidx.core.graphics.drawable

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.graphics.Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.Bitmap).toAdaptiveIcon()()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this adaptive [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |
| [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.Bitmap).toDrawable(android.content.res.Resources)(resources: https://developer.android.com/reference/android/content/res/Resources.html)` Create a [BitmapDrawable](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.html) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `https://developer.android.com/reference/android/graphics/Bitmap.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.Bitmap).toIcon()()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html). |

##### For [android.graphics.Color](https://developer.android.com/reference/android/graphics/Color.html)

|---|---|
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) | `https://developer.android.com/reference/android/graphics/Color.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.Color).toDrawable()()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) from this [Color](https://developer.android.com/reference/android/graphics/Color.html) (via [Color.toArgb](https://developer.android.com/reference/android/graphics/Color.html#toArgb())). |

##### For [android.graphics.drawable.Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html)

|---|---|
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/android/graphics/drawable/Drawable.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.drawable.Drawable).toBitmap(kotlin.Int,%20kotlin.Int,%20android.graphics.Bitmap.Config)(@Px width: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = intrinsicWidth, @Px height: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = intrinsicHeight, config: https://developer.android.com/reference/android/graphics/Bitmap/Config.html? = null)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) representation of this [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/graphics/drawable/Drawable.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.graphics.drawable.Drawable).updateBounds(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int)(@Px left: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bounds.left, @Px top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bounds.top, @Px right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bounds.right, @Px bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bounds.bottom)` Updates this drawable's bounds. |

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.html)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `https://developer.android.com/reference/android/net/Uri.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(android.net.Uri).toIcon()()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [Uri](https://developer.android.com/reference/android/net/Uri.html). |

##### For [kotlin.ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)

|---|---|
| [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(kotlin.ByteArray).toIcon()()` Create an [Icon](https://developer.android.com/reference/android/graphics/drawable/Icon.html) from this [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html). |

##### For [kotlin.Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

|---|---|
| [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html.https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary#(kotlin.Int).toDrawable()()` Create a [ColorDrawable](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html) from this color value. |

## androidx.core.location

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.location.Location](https://developer.android.com/reference/android/location/Location.html)

|---|---|
| operator [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `https://developer.android.com/reference/android/location/Location.html.https://developer.android.com/reference/kotlin/androidx/core/location/package-summary#(android.location.Location).component1()()` Returns the latitude of this [Location](https://developer.android.com/reference/android/location/Location.html). |
| operator [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `https://developer.android.com/reference/android/location/Location.html.https://developer.android.com/reference/kotlin/androidx/core/location/package-summary#(android.location.Location).component2()()` Returns the longitude of this [Location](https://developer.android.com/reference/android/location/Location.html). |

## androidx.core.net

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.net.Uri](https://developer.android.com/reference/android/net/Uri.html)

|---|---|
| [File](https://developer.android.com/reference/java/io/File.html) | `https://developer.android.com/reference/android/net/Uri.html.https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#(android.net.Uri).toFile()()` Creates a [File](https://developer.android.com/reference/java/io/File.html) from the given [Uri](https://developer.android.com/reference/android/net/Uri.html). |

##### For [java.io.File](https://developer.android.com/reference/java/io/File.html)

|---|---|
| [Uri](https://developer.android.com/reference/android/net/Uri.html) | `https://developer.android.com/reference/java/io/File.html.https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#(java.io.File).toUri()()` Creates a Uri from the given file. |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|---|---|
| [Uri](https://developer.android.com/reference/android/net/Uri.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html.https://developer.android.com/reference/kotlin/androidx/core/net/package-summary#(kotlin.String).toUri()()` Creates a Uri from the given encoded URI string. |

## androidx.core.os

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.os.Handler](https://developer.android.com/reference/android/os/Handler.html)

|---|---|
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `https://developer.android.com/reference/android/os/Handler.html.https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#(android.os.Handler).postAtTime(kotlin.Long,%20kotlin.Any,%20kotlin.Function0)(uptimeMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html? = null, crossinline action: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Version of [Handler.postAtTime](https://developer.android.com/reference/android/os/Handler.html#postAtTime(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `https://developer.android.com/reference/android/os/Handler.html.https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#(android.os.Handler).postDelayed(kotlin.Long,%20kotlin.Any,%20kotlin.Function0)(delayInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html? = null, crossinline action: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Version of [Handler.postDelayed](https://developer.android.com/reference/android/os/Handler.html#postDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |

#### Top-level functions

|---|---|
| [Bundle](https://developer.android.com/reference/android/os/Bundle.html) | `https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#bundleOf(kotlin.Pair)(vararg pairs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Returns a new [Bundle](https://developer.android.com/reference/android/os/Bundle.html) with the given key/value pairs as elements. |
| [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.html) | `https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#persistableBundleOf(kotlin.Pair)(vararg pairs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Returns a new [PersistableBundle](https://developer.android.com/reference/android/os/PersistableBundle.html) with the given key/value pairs as elements. |
| T | `https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#trace(kotlin.String,%20kotlin.Function0)(sectionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: () -> T)` Wrap the specified [block](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#androidx.core.os$trace(kotlin.String,%20kotlin.Function0((androidx.core.os.trace.T)))/block) in calls to [Trace.beginSection](https://developer.android.com/reference/android/os/Trace.html#beginSection(java.lang.String)) (with the supplied [sectionName](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#androidx.core.os$trace(kotlin.String,%20kotlin.Function0((androidx.core.os.trace.T)))/sectionName)) and [Trace.endSection](https://developer.android.com/reference/android/os/Trace.html#endSection()). |

## androidx.core.text

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.text.Spannable](https://developer.android.com/reference/android/text/Spannable.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/text/Spannable.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.Spannable).clearSpans()()` Clear all spans from this text. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/text/Spannable.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.Spannable).set(kotlin.Int,%20kotlin.Int,%20kotlin.Any)(start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, end: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, span: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Add [span](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/span) to the range [start](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/start)...[end](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.Int,%20kotlin.Int,%20kotlin.Any)/end) of the text. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/text/Spannable.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.Spannable).set(kotlin.ranges.IntRange,%20kotlin.Any)(range: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-int-range/index.html, span: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Add [span](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.ranges.IntRange,%20kotlin.Any)/span) to the [range](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$set(android.text.Spannable,%20kotlin.ranges.IntRange,%20kotlin.Any)/range) of the text. |

##### For [android.text.SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html)

|---|---|
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).backgroundColor(kotlin.Int,%20kotlin.Function1)(color: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$backgroundColor(android.text.SpannableStringBuilder,%20kotlin.Int,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [BackgroundColorSpan](https://developer.android.com/reference/android/text/style/BackgroundColorSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).bold(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$bold(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a bold [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).color(kotlin.Int,%20kotlin.Function1)(color: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$color(android.text.SpannableStringBuilder,%20kotlin.Int,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [ForegroundColorSpan](https://developer.android.com/reference/android/text/style/ForegroundColorSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).inSpans(kotlin.Any,%20kotlin.Function1)(vararg spans: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Array((kotlin.Any)),%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in [spans](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Array((kotlin.Any)),%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/spans). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).inSpans(kotlin.Any,%20kotlin.Function1)(span: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Any,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in [span](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$inSpans(android.text.SpannableStringBuilder,%20kotlin.Any,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/span). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).italic(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$italic(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in an italic [StyleSpan](https://developer.android.com/reference/android/text/style/StyleSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).scale(kotlin.Float,%20kotlin.Function1)(proportion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$scale(android.text.SpannableStringBuilder,%20kotlin.Float,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [RelativeSizeSpan](https://developer.android.com/reference/android/text/style/RelativeSizeSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).strikeThrough(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$strikeThrough(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [StrikethroughSpan](https://developer.android.com/reference/android/text/style/StrikethroughSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).subscript(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$subscript(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [SubscriptSpan](https://developer.android.com/reference/android/text/style/SubscriptSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).superscript(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$superscript(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in a [SuperscriptSpan](https://developer.android.com/reference/android/text/style/SuperscriptSpan.html). |
| [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) | `https://developer.android.com/reference/android/text/SpannableStringBuilder.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.SpannableStringBuilder).underline(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Wrap appended text in [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$underline(android.text.SpannableStringBuilder,%20kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) in an [UnderlineSpan](https://developer.android.com/reference/android/text/style/UnderlineSpan.html). |

##### For [android.text.Spanned](https://developer.android.com/reference/android/text/Spanned.html)

|---|---|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)\<out T\> | `https://developer.android.com/reference/android/text/Spanned.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.Spanned).getSpans(kotlin.Int,%20kotlin.Int)(start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, end: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = length)` Get all spans that are instance of T. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `https://developer.android.com/reference/android/text/Spanned.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(android.text.Spanned).toHtml(kotlin.Int)(option: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = TO_HTML_PARAGRAPH_LINES_CONSECUTIVE)` Returns a string of HTML from the spans in this [Spanned](https://developer.android.com/reference/android/text/Spanned.html). |

##### For [kotlin.CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.CharSequence).isDigitsOnly()()` Returns whether the given [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) contains only digits. |
| [Spannable](https://developer.android.com/reference/android/text/Spannable.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.CharSequence).toSpannable()()` Returns a new [Spannable](https://developer.android.com/reference/android/text/Spannable.html) from [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html), or the source itself if it is already an instance of [SpannableString](https://developer.android.com/reference/android/text/SpannableString.html). |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.CharSequence).toSpanned()()` Returns a new [Spanned](https://developer.android.com/reference/android/text/Spanned.html) from [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html), or the source itself if it is already an instance of [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.CharSequence).trimmedLength()()` Returns the length that the specified [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html) would have if spaces and ASCII control characters were trimmed from the start and end, as by [String.trim](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/trim.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|---|---|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.String).htmlEncode()()` Html-encode the string. |
| [Spanned](https://developer.android.com/reference/android/text/Spanned.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(kotlin.String).parseAsHtml(kotlin.Int,%20android.text.Html.ImageGetter,%20android.text.Html.TagHandler)(flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = FROM_HTML_MODE_LEGACY, imageGetter: https://developer.android.com/reference/android/text/Html/ImageGetter.html? = null, tagHandler: https://developer.android.com/reference/android/text/Html/TagHandler.html? = null)` Returns a [Spanned](https://developer.android.com/reference/android/text/Spanned.html) from parsing this string as HTML. |

#### Extension properties

##### For [java.util.Locale](https://developer.android.com/reference/java/util/Locale.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/java/util/Locale.html.https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#(java.util.Locale).layoutDirection:kotlin.Int()` Returns layout direction for a given locale. |

#### Top-level functions

|---|---|
| [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html) | `https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#buildSpannedString(kotlin.Function1)(builderAction: https://developer.android.com/reference/android/text/SpannableStringBuilder.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Builds new string by populating a newly created [SpannableStringBuilder](https://developer.android.com/reference/android/text/SpannableStringBuilder.html) using the provided [builderAction](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary#androidx.core.text$buildSpannedString(kotlin.Function1((android.text.SpannableStringBuilder,%20kotlin.Unit)))/builderAction) and then converting it to [SpannedString](https://developer.android.com/reference/android/text/SpannedString.html). |

## androidx.core.transition

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)

|---|---|
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).addListener(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1)(crossinline onEnd: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onStart: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onCancel: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onResume: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, crossinline onPause: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {})` Add a listener to this Transition using the provided actions. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).doOnCancel(kotlin.Function1)(crossinline action: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when this transition has been cancelled. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).doOnEnd(kotlin.Function1)(crossinline action: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when this transition has ended. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).doOnPause(kotlin.Function1)(crossinline action: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when this transition has been paused. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).doOnResume(kotlin.Function1)(crossinline action: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when this transition has resumed after a pause. |
| [TransitionListener](https://developer.android.com/reference/android/transition/Transition/TransitionListener.html) | `https://developer.android.com/reference/android/transition/Transition.html.https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary#(android.transition.Transition).doOnStart(kotlin.Function1)(crossinline action: (transition: https://developer.android.com/reference/android/transition/Transition.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when this transition has started. |

## androidx.core.util

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.util.AtomicFile](https://developer.android.com/reference/android/util/AtomicFile.html)

|---|---|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | `https://developer.android.com/reference/android/util/AtomicFile.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.AtomicFile).readBytes()()` Gets the entire content of this file as a byte array. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | `https://developer.android.com/reference/android/util/AtomicFile.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.AtomicFile).readText(java.nio.charset.Charset)(charset: https://developer.android.com/reference/java/nio/charset/Charset.html = Charsets.UTF_8)` Gets the entire content of this file as a String using UTF-8 or specified [charset](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$readText(android.util.AtomicFile,%20java.nio.charset.Charset)/charset). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/AtomicFile.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.AtomicFile).tryWrite(kotlin.Function1)(block: (out: https://developer.android.com/reference/java/io/FileOutputStream.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Perform the write operations inside [block](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$tryWrite(android.util.AtomicFile,%20kotlin.Function1((java.io.FileOutputStream,%20kotlin.Unit)))/block) on this file. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/AtomicFile.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.AtomicFile).writeBytes(kotlin.ByteArray)(array: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Sets the content of this file as an [array](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeBytes(android.util.AtomicFile,%20kotlin.ByteArray)/array) of bytes. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/AtomicFile.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.AtomicFile).writeText(kotlin.String,%20java.nio.charset.Charset)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, charset: https://developer.android.com/reference/java/nio/charset/Charset.html = Charsets.UTF_8)` Sets the content of this file as [text](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeText(android.util.AtomicFile,%20kotlin.String,%20java.nio.charset.Charset)/text) encoded using UTF-8 or specified [charset](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$writeText(android.util.AtomicFile,%20kotlin.String,%20java.nio.charset.Charset)/charset). |

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).contains(kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.LongSparseArray((androidx.core.util.contains.T)),%20kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).containsKey(kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.LongSparseArray((androidx.core.util.containsKey.T)),%20kotlin.Long)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).containsValue(androidx.core.util.android.util.LongSparseArray.containsValue.T)(value: T)` Returns true if the collection contains [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.LongSparseArray((androidx.core.util.containsValue.T)),%20androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.LongSparseArray((androidx.core.util.forEach.T)),%20kotlin.Function2((kotlin.Long,%20androidx.core.util.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).getOrDefault(kotlin.Long,%20androidx.core.util.android.util.LongSparseArray.getOrDefault.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Long,%20androidx.core.util.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.LongSparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Long,%20androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).getOrElse(kotlin.Long,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.LongSparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Long,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).isEmpty()()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).isNotEmpty()()` Return true when the collection contains elements. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)\<T\> | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).plus(android.util.LongSparseArray)(other: https://developer.android.com/reference/android/util/LongSparseArray.html<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.LongSparseArray((androidx.core.util.plus.T)),%20android.util.LongSparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).putAll(android.util.LongSparseArray)(other: https://developer.android.com/reference/android/util/LongSparseArray.html<T>)` Update this collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.LongSparseArray((androidx.core.util.putAll.T)),%20android.util.LongSparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).remove(kotlin.Long,%20androidx.core.util.android.util.LongSparseArray.remove.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)),%20kotlin.Long,%20androidx.core.util.remove.T)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.LongSparseArray((androidx.core.util.remove.T)),%20kotlin.Long,%20androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).set(kotlin.Long,%20androidx.core.util.android.util.LongSparseArray.set.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)\<T\> | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [android.util.Pair](https://developer.android.com/reference/android/util/Pair.html)

|---|---|
| operator F | `https://developer.android.com/reference/android/util/Pair.html<F, S>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Pair).component1()()` Returns the first component of the pair. |
| operator S | `https://developer.android.com/reference/android/util/Pair.html<F, S>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Pair).component2()()` Returns the second component of the pair. |
| [Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)\<F, S\> | `https://developer.android.com/reference/android/util/Pair.html<F, S>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Pair).toKotlinPair()()` Returns this [Pair](https://developer.android.com/reference/android/util/Pair.html) as a [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html). |

##### For [android.util.Range](https://developer.android.com/reference/android/util/Range.html)

|---|---|
| infix [Range](https://developer.android.com/reference/android/util/Range.html)\<T\> | `https://developer.android.com/reference/android/util/Range.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Range).and(android.util.Range)(other: https://developer.android.com/reference/android/util/Range.html<T>)` Return the intersection of this range and [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$and(android.util.Range((androidx.core.util.and.T)),%20android.util.Range((androidx.core.util.and.T)))/other). |
| operator [Range](https://developer.android.com/reference/android/util/Range.html)\<T\> | `https://developer.android.com/reference/android/util/Range.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Range).plus(androidx.core.util.android.util.Range.plus.T)(value: T)` Return the smallest range that includes this and [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)),%20androidx.core.util.plus.T)/value). |
| operator [Range](https://developer.android.com/reference/android/util/Range.html)\<T\> | `https://developer.android.com/reference/android/util/Range.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Range).plus(android.util.Range)(other: https://developer.android.com/reference/android/util/Range.html<T>)` Return the smallest range that includes this and [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.Range((androidx.core.util.plus.T)),%20android.util.Range((androidx.core.util.plus.T)))/other). |
| [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html)\<T\> | `https://developer.android.com/reference/android/util/Range.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Range).toClosedRange()()` Returns this [Range](https://developer.android.com/reference/android/util/Range.html) as a [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html). |

##### For [android.util.Size](https://developer.android.com/reference/android/util/Size.html)

|---|---|
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/Size.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Size).component1()()` Returns "width", the first component of this [Size](https://developer.android.com/reference/android/util/Size.html). |
| operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/Size.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.Size).component2()()` Returns "height", the second component of this [Size](https://developer.android.com/reference/android/util/Size.html). |

##### For [android.util.SizeF](https://developer.android.com/reference/android/util/SizeF.html)

|---|---|
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/util/SizeF.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SizeF).component1()()` Returns "width", the first component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.html). |
| operator [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) | `https://developer.android.com/reference/android/util/SizeF.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SizeF).component2()()` Returns "height", the second component of this [SizeF](https://developer.android.com/reference/android/util/SizeF.html). |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).contains(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseArray((androidx.core.util.contains.T)),%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).containsKey(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseArray((androidx.core.util.containsKey.T)),%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).containsValue(androidx.core.util.android.util.SparseArray.containsValue.T)(value: T)` Returns true if the collection contains [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseArray((androidx.core.util.containsValue.T)),%20androidx.core.util.containsValue.T)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseArray((androidx.core.util.forEach.T)),%20kotlin.Function2((kotlin.Int,%20androidx.core.util.forEach.T,%20kotlin.Unit)))/action) for each key/value entry. |
| T | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).getOrDefault(kotlin.Int,%20androidx.core.util.android.util.SparseArray.getOrDefault.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Int,%20androidx.core.util.getOrDefault.T)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseArray((androidx.core.util.getOrDefault.T)),%20kotlin.Int,%20androidx.core.util.getOrDefault.T)/defaultValue) when not present. |
| T | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).getOrElse(kotlin.Int,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: () -> T)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseArray((androidx.core.util.getOrElse.T)),%20kotlin.Int,%20kotlin.Function0((androidx.core.util.getOrElse.T)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).isEmpty()()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).isNotEmpty()()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)\<T\> | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).plus(android.util.SparseArray)(other: https://developer.android.com/reference/android/util/SparseArray.html<T>)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseArray((androidx.core.util.plus.T)),%20android.util.SparseArray((androidx.core.util.plus.T)))/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).putAll(android.util.SparseArray)(other: https://developer.android.com/reference/android/util/SparseArray.html<T>)` Update this collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseArray((androidx.core.util.putAll.T)),%20android.util.SparseArray((androidx.core.util.putAll.T)))/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).remove(kotlin.Int,%20androidx.core.util.android.util.SparseArray.remove.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)),%20kotlin.Int,%20androidx.core.util.remove.T)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseArray((androidx.core.util.remove.T)),%20kotlin.Int,%20androidx.core.util.remove.T)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).set(kotlin.Int,%20androidx.core.util.android.util.SparseArray.set.T)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: T)` Allows the use of the index operator for storing values in the collection. |
| [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)\<T\> | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).contains(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseBooleanArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).containsKey(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseBooleanArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).containsValue(kotlin.Boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns true if the collection contains [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseBooleanArray,%20kotlin.Boolean)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseBooleanArray,%20kotlin.Function2((kotlin.Int,%20kotlin.Boolean,%20kotlin.Unit)))/action) for each key/value entry. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).getOrDefault(kotlin.Int,%20kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).getOrElse(kotlin.Int,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Boolean)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Boolean)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).isEmpty()()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).isNotEmpty()()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).plus(android.util.SparseBooleanArray)(other: https://developer.android.com/reference/android/util/SparseBooleanArray.html)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseBooleanArray,%20android.util.SparseBooleanArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).putAll(android.util.SparseBooleanArray)(other: https://developer.android.com/reference/android/util/SparseBooleanArray.html)` Update this collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseBooleanArray,%20android.util.SparseBooleanArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).remove(kotlin.Int,%20kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseBooleanArray,%20kotlin.Int,%20kotlin.Boolean)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).set(kotlin.Int,%20kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Allows the use of the index operator for storing values in the collection. |
| [BooleanIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-boolean-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).contains(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseIntArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).containsKey(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseIntArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).containsValue(kotlin.Int)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseIntArray,%20kotlin.Int)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseIntArray,%20kotlin.Function2((kotlin.Int,%20,%20kotlin.Unit)))/action) for each key/value entry. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).getOrDefault(kotlin.Int,%20kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/defaultValue) when not present. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).getOrElse(kotlin.Int,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Int)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Int)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).isEmpty()()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).isNotEmpty()()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).plus(android.util.SparseIntArray)(other: https://developer.android.com/reference/android/util/SparseIntArray.html)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseIntArray,%20android.util.SparseIntArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).putAll(android.util.SparseIntArray)(other: https://developer.android.com/reference/android/util/SparseIntArray.html)` Update this collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseIntArray,%20android.util.SparseIntArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).remove(kotlin.Int,%20kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/key) only if it is mapped to [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseIntArray,%20kotlin.Int,%20kotlin.Int)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).set(kotlin.Int,%20kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Allows the use of the index operator for storing values in the collection. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).contains(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$contains(android.util.SparseLongArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).containsKey(kotlin.Int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns true if the collection contains [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsKey(android.util.SparseLongArray,%20kotlin.Int)/key). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).containsValue(kotlin.Long)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Returns true if the collection contains [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$containsValue(android.util.SparseLongArray,%20kotlin.Long)/value). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).forEach(kotlin.Function2)(action: (key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given [action](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$forEach(android.util.SparseLongArray,%20kotlin.Function2((kotlin.Int,%20kotlin.Long,%20kotlin.Unit)))/action) for each key/value entry. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).getOrDefault(kotlin.Int,%20kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/key), or [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrDefault(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/defaultValue) when not present. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).getOrElse(kotlin.Int,%20kotlin.Function0)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, defaultValue: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Return the value corresponding to [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Long)))/key), or from [defaultValue](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$getOrElse(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Function0((kotlin.Long)))/defaultValue) when not present. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).isEmpty()()` Return true when the collection contains no elements. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).isNotEmpty()()` Return true when the collection contains elements. |
| [IntIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-int-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).keyIterator()()` Return an iterator over the collection's keys. |
| operator [SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).plus(android.util.SparseLongArray)(other: https://developer.android.com/reference/android/util/SparseLongArray.html)` Creates a new collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$plus(android.util.SparseLongArray,%20android.util.SparseLongArray)/other). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).putAll(android.util.SparseLongArray)(other: https://developer.android.com/reference/android/util/SparseLongArray.html)` Update this collection by adding or replacing entries from [other](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$putAll(android.util.SparseLongArray,%20android.util.SparseLongArray)/other). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).remove(kotlin.Int,%20kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Removes the entry for [key](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/key) only if it is set to [value](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$remove(android.util.SparseLongArray,%20kotlin.Int,%20kotlin.Long)/value). |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).set(kotlin.Int,%20kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Allows the use of the index operator for storing values in the collection. |
| [LongIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-long-iterator/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).valueIterator()()` Return an iterator over the collection's values. |

##### For [kotlin.Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.Double).toHalf()()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html). |

##### For [kotlin.Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.Float).toHalf()()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html). |

##### For [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html)

|---|---|
| [Pair](https://developer.android.com/reference/android/util/Pair.html)\<F, S\> | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<F, S>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.Pair).toAndroidPair()()` Returns this [kotlin.Pair](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html) as an Android [Pair](https://developer.android.com/reference/android/util/Pair.html). |

##### For [kotlin.Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.Short).toHalf()()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [Short](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-short/index.html). |

##### For [kotlin.String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

|---|---|
| [Half](https://developer.android.com/reference/android/util/Half.html) | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.String).toHalf()()` Returns a [Half](https://developer.android.com/reference/android/util/Half.html) instance representing given [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html). |

##### For [kotlin.ranges.ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html)

|---|---|
| [Range](https://developer.android.com/reference/android/util/Range.html)\<T\> | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(kotlin.ranges.ClosedRange).toRange()()` Returns this [ClosedRange](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.ranges/-closed-range/index.html) as a [Range](https://developer.android.com/reference/android/util/Range.html). |

#### Extension properties

##### For [android.util.LongSparseArray](https://developer.android.com/reference/android/util/LongSparseArray.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/LongSparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.LongSparseArray).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseArray](https://developer.android.com/reference/android/util/SparseArray.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseArray.html<T>.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseArray).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseBooleanArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseBooleanArray).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseIntArray](https://developer.android.com/reference/android/util/SparseIntArray.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseIntArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseIntArray).size:kotlin.Int()` Returns the number of key/value pairs in the collection. |

##### For [android.util.SparseLongArray](https://developer.android.com/reference/android/util/SparseLongArray.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/util/SparseLongArray.html.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(android.util.SparseLongArray).size:kotlin.Int()` Returns the number of key/value entries in the collection. |

#### Top-level functions

|---|---|
| [LruCache](https://developer.android.com/reference/android/util/LruCache.html)\<K, V\> | `https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#lruCache(kotlin.Int,%20kotlin.Function2,%20kotlin.Function1,%20kotlin.Function4)(maxSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, crossinline sizeOf: (key: K, value: V) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = { _, _ -> 1 }, crossinline create: (key: K) -> V? = { null as V? }, crossinline onEntryRemoved: (evicted: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, key: K, oldValue: V, newValue: V?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = { _, _, _, _ -> })` Creates an [LruCache](https://developer.android.com/reference/android/util/LruCache.html) with the given parameters. |
| infix [Range](https://developer.android.com/reference/android/util/Range.html)\<T\> | `T.https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#(androidx.core.util.rangeTo.T).rangeTo(androidx.core.util.rangeTo.T)(that: T)` Creates a range from this [Comparable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparable/index.html) value to [that](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary#androidx.core.util$rangeTo(androidx.core.util.rangeTo.T,%20androidx.core.util.rangeTo.T)/that). |

## androidx.core.view

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).contains(android.view.MenuItem)(item: https://developer.android.com/reference/android/view/MenuItem.html)` Returns `true` if [item](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$contains(android.view.Menu,%20android.view.MenuItem)/item) is found in this menu. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).forEach(kotlin.Function1)(action: (item: https://developer.android.com/reference/android/view/MenuItem.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each item in this menu. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).forEachIndexed(kotlin.Function2)(action: (index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, item: https://developer.android.com/reference/android/view/MenuItem.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each item in this menu, providing its sequential index. |
| operator [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).get(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the menu at [index](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$get(android.view.Menu,%20kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).isEmpty()()` Returns true if this menu contains no items. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).isNotEmpty()()` Returns true if this menu contains one or more items. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)\<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)\> | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).iterator()()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the items in this menu. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).minusAssign(android.view.MenuItem)(item: https://developer.android.com/reference/android/view/MenuItem.html)` Removes [item](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$minusAssign(android.view.Menu,%20android.view.MenuItem)/item) from this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).doOnAttach(kotlin.Function1)(crossinline action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action when this view is attached to a window. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).doOnDetach(kotlin.Function1)(crossinline action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action when this view is detached from a window. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).doOnLayout(kotlin.Function1)(crossinline action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action when this view is laid out. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).doOnNextLayout(kotlin.Function1)(crossinline action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action when this view is next laid out. |
| [OneShotPreDrawListener](https://developer.android.com/reference/kotlin/androidx/core/view/OneShotPreDrawListener) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).doOnPreDraw(kotlin.Function1)(crossinline action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action when the view tree is about to be drawn. |
| [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).drawToBitmap(android.graphics.Bitmap.Config)(config: https://developer.android.com/reference/android/graphics/Bitmap/Config.html = Bitmap.Config.ARGB_8888)` Return a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) representation of this [View](https://developer.android.com/reference/android/view/View.html). |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).postDelayed(kotlin.Long,%20kotlin.Function0)(delayInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, crossinline action: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Version of [View.postDelayed](https://developer.android.com/reference/android/view/View.html#postDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Runnable](https://developer.android.com/reference/java/lang/Runnable.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).postOnAnimationDelayed(kotlin.Long,%20kotlin.Function0)(delayInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, crossinline action: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Version of [View.postOnAnimationDelayed](https://developer.android.com/reference/android/view/View.html#postOnAnimationDelayed(java.lang.Runnable, long)) which re-orders the parameters, allowing the action to be placed outside of parentheses. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).setPadding(kotlin.Int)(@Px size: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets the view's padding. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).updateLayoutParams(kotlin.Function1)(block: https://developer.android.com/reference/android/view/ViewGroup/LayoutParams.html.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Executes [block](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$updateLayoutParams(android.view.View,%20kotlin.Function1((android.view.ViewGroup.LayoutParams,%20kotlin.Unit)))/block) with the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).updateLayoutParams(kotlin.Function1)(block: T.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Executes [block](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$updateLayoutParams(android.view.View,%20kotlin.Function1((androidx.core.view.updateLayoutParams.T,%20kotlin.Unit)))/block) with a typed version of the View's layoutParams and reassigns the layoutParams with the updated version. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).updatePadding(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int)(@Px left: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingLeft, @Px top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingTop, @Px right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingRight, @Px bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingBottom)` Updates this view's padding. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).updatePaddingRelative(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int)(@Px start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingStart, @Px top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingTop, @Px end: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingEnd, @Px bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = paddingBottom)` Updates this view's relative padding. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).contains(android.view.View)(view: https://developer.android.com/reference/android/view/View.html)` Returns `true` if [view](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$contains(android.view.ViewGroup,%20android.view.View)/view) is found in this view group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).forEach(kotlin.Function1)(action: (view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each view in this view group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).forEachIndexed(kotlin.Function2)(action: (index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, view: https://developer.android.com/reference/android/view/View.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each view in this view group, providing its sequential index. |
| operator [View](https://developer.android.com/reference/android/view/View.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).get(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the view at [index](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$get(android.view.ViewGroup,%20kotlin.Int)/index). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).isEmpty()()` Returns true if this view group contains no views. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).isNotEmpty()()` Returns true if this view group contains one or more views. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)\<[View](https://developer.android.com/reference/android/view/View.html)\> | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).iterator()()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the views in this view group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).minusAssign(android.view.View)(view: https://developer.android.com/reference/android/view/View.html)` Removes [view](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$minusAssign(android.view.ViewGroup,%20android.view.View)/view) from this view group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).plusAssign(android.view.View)(view: https://developer.android.com/reference/android/view/View.html)` Adds [view](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#androidx.core.view$plusAssign(android.view.ViewGroup,%20android.view.View)/view) to this view group. |

##### For [android.view.ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup.MarginLayoutParams).setMargins(kotlin.Int)(@Px size: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets the margins in the ViewGroup's MarginLayoutParams. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup.MarginLayoutParams).updateMargins(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int)(@Px left: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = leftMargin, @Px top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = topMargin, @Px right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = rightMargin, @Px bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bottomMargin)` Updates the margins in the [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)'s [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup.MarginLayoutParams).updateMarginsRelative(kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int)(@Px start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = marginStart, @Px top: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = topMargin, @Px end: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = marginEnd, @Px bottom: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = bottomMargin)` Updates the relative margins in the ViewGroup's MarginLayoutParams. |

#### Extension properties

##### For [android.view.Menu](https://developer.android.com/reference/android/view/Menu.html)

|---|---|
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)\<[MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)\> | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).children:kotlin.sequences.Sequence()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the items in this menu. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/Menu.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.Menu).size:kotlin.Int()` Returns the number of items in this menu. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).isGone:kotlin.Boolean()` Returns true when this view's visibility is [View.GONE](https://developer.android.com/reference/android/view/View.html#GONE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).isInvisible:kotlin.Boolean()` Returns true when this view's visibility is [View.INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE), false otherwise. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).isVisible:kotlin.Boolean()` Returns true when this view's visibility is [View.VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE), false otherwise. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginBottom:kotlin.Int()` Returns the bottom margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginEnd:kotlin.Int()` Returns the end margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginLeft:kotlin.Int()` Returns the left margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginRight:kotlin.Int()` Returns the right margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginStart:kotlin.Int()` Returns the start margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.View).marginTop:kotlin.Int()` Returns the top margin if this view's [LayoutParams](https://developer.android.com/reference/kotlin/androidx/core/view) is a [ViewGroup.MarginLayoutParams](https://developer.android.com/reference/android/view/ViewGroup/MarginLayoutParams.html), otherwise 0. |

##### For [android.view.ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)

|---|---|
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)\<[View](https://developer.android.com/reference/android/view/View.html)\> | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).children:kotlin.sequences.Sequence()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the child views in this view group. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/android/view/ViewGroup.html.https://developer.android.com/reference/kotlin/androidx/core/view/package-summary#(android.view.ViewGroup).size:kotlin.Int()` Returns the number of views in this view group. |

## androidx.core.widget

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.17.0")
}
```

#### Extension functions

##### For [android.widget.TextView](https://developer.android.com/reference/android/widget/TextView.html)

|---|---|
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `https://developer.android.com/reference/android/widget/TextView.html.https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#(android.widget.TextView).addTextChangedListener(kotlin.Function4,%20kotlin.Function4,%20kotlin.Function1)(crossinline beforeTextChanged: (text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html?, start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, count: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, after: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = { _, _, _, _ -> }, crossinline onTextChanged: (text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html?, start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, count: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, after: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = { _, _, _, _ -> }, crossinline afterTextChanged: (text: https://developer.android.com/reference/android/text/Editable.html?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {})` Add a text changed listener to this TextView using the provided actions |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `https://developer.android.com/reference/android/widget/TextView.html.https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#(android.widget.TextView).doAfterTextChanged(kotlin.Function1)(crossinline action: (text: https://developer.android.com/reference/android/text/Editable.html?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked after the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `https://developer.android.com/reference/android/widget/TextView.html.https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#(android.widget.TextView).doBeforeTextChanged(kotlin.Function4)(crossinline action: (text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html?, start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, count: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, after: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked before the text changed. |
| [TextWatcher](https://developer.android.com/reference/android/text/TextWatcher.html) | `https://developer.android.com/reference/android/widget/TextView.html.https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary#(android.widget.TextView).doOnTextChanged(kotlin.Function4)(crossinline action: (text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html?, start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, count: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, after: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Add an action which will be invoked when the text is changing. |

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

##### For [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation)

|---|---|
| [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation.https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#(androidx.dynamicanimation.animation.SpringAnimation).withSpringForceProperties(kotlin.Function1)(func: https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringForce.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Updates or applies spring force properties like [SpringForce.mDampingRatio](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation), [SpringForce.mFinalPosition](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation) and stiffness on SpringAnimation. |

#### Top-level functions

|---|---|
| [FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) | `https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#flingAnimationOf(kotlin.Function1,%20kotlin.Function0)(setter: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html, getter: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Creates [FlingAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/FlingAnimation) for a property that can be accessed via the provided setter and getter. |
| [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) | `https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary#springAnimationOf(kotlin.Function1,%20kotlin.Function0,%20kotlin.Float)(setter: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html, getter: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html, finalPosition: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html = Float.NaN)` Creates [SpringAnimation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/SpringAnimation) for a property that can be accessed via the provided setter and getter. |

## androidx.fragment.app

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.fragment:fragment-ktx:1.8.9"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.fragment:fragment-ktx:1.8.9")
}
```

#### Extension functions

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|---|---|
| F | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(android.view.View).findFragment()()` Find a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) associated with a [View](https://developer.android.com/reference/android/view/View.html). |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

|---|---|
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)\<VM\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.Fragment).activityViewModels(kotlin.Function0)(noinline factoryProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory = null)` Returns a property delegate to access parent activity's [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel), if [factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$activityViewModels(androidx.fragment.app.Fragment,%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) is specified then [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory) returned by it will be used to create [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) first time. |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)\<VM\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.Fragment).createViewModelLazy(kotlin.reflect.KClass,%20kotlin.Function0,%20kotlin.Function0)(viewModelClass: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<VM>, storeProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore, factoryProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory = null)` Helper method for creation of [ViewModelLazy](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelLazy), that resolves `null` passed as [factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$createViewModelLazy(androidx.fragment.app.Fragment,%20kotlin.reflect.KClass((androidx.fragment.app.createViewModelLazy.VM)),%20kotlin.Function0((androidx.lifecycle.ViewModelStore)),%20kotlin.Function0((androidx.lifecycle.ViewModelProvider.Factory)))/factoryProducer) to default factory. |
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)\<VM\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.Fragment).viewModels(kotlin.Function0,%20kotlin.Function0)(noinline ownerProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner = { this }, noinline factoryProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory = null)` Returns a property delegate to access [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) by **default** scoped to this [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment): |

##### For [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction)

|---|---|
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentTransaction).add(kotlin.Int,%20kotlin.String,%20android.os.Bundle)(@IdRes containerViewId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, tag: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null, args: https://developer.android.com/reference/android/os/Bundle.html? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager), inflating the Fragment's view into the container view specified by [containerViewId](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$add(androidx.fragment.app.FragmentTransaction,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle)/containerViewId), to later retrieve via [FragmentManager.findFragmentById](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#findFragmentById(kotlin.Int)). |
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentTransaction).add(kotlin.String,%20android.os.Bundle)(tag: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, args: https://developer.android.com/reference/android/os/Bundle.html? = null)` Add a fragment to the associated [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager) without adding the Fragment to any container view. |
| [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentTransaction).replace(kotlin.Int,%20kotlin.String,%20android.os.Bundle)(@IdRes containerViewId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, tag: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null, args: https://developer.android.com/reference/android/os/Bundle.html? = null)` Replace an existing fragment that was added to a container. |

##### For [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentManager).commit(kotlin.Boolean,%20kotlin.Function1)(allowStateLoss: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false, body: https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Run [body](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$commit(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentManager).commitNow(kotlin.Boolean,%20kotlin.Function1)(allowStateLoss: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false, body: https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Run [body](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$commitNow(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager.https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.FragmentManager).transaction(kotlin.Boolean,%20kotlin.Boolean,%20kotlin.Function1)(now: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false, allowStateLoss: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false, body: https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Run [body](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#androidx.fragment.app$transaction(androidx.fragment.app.FragmentManager,%20kotlin.Boolean,%20kotlin.Boolean,%20kotlin.Function1((androidx.fragment.app.FragmentTransaction,%20kotlin.Unit)))/body) in a [FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction) which is automatically committed if it completes without exception. |

## androidx.fragment.app.testing

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.fragment:fragment-testing:1.8.9"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.fragment:fragment-testing:1.8.9")
}
```

#### Top-level functions

|---|---|
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)\<F!\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragment(android.os.Bundle,%20kotlin.Int,%20androidx.fragment.app.FragmentFactory)(fragmentArgs: https://developer.android.com/reference/android/os/Bundle.html? = null, @StyleRes themeResId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory? = null)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using given [FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory) and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)\<F!\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragment(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0)(fragmentArgs: https://developer.android.com/reference/android/os/Bundle.html? = null, @StyleRes themeResId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#androidx.fragment.app.testing$launchFragment(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0((androidx.fragment.app.testing.launchFragment.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)\<F!\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragmentInContainer(android.os.Bundle,%20kotlin.Int,%20androidx.fragment.app.FragmentFactory)(fragmentArgs: https://developer.android.com/reference/android/os/Bundle.html? = null, @StyleRes themeResId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = R.style.FragmentScenarioEmptyFragmentActivityTheme, factory: https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory? = null)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) and waits for it to reach a resumed state. |
| [FragmentScenario](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)\<F!\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragmentInContainer(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0)(fragmentArgs: https://developer.android.com/reference/android/os/Bundle.html? = null, @StyleRes themeResId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = R.style.FragmentScenarioEmptyFragmentActivityTheme, crossinline instantiate: () -> F)` Launches a Fragment in the Activity's root view container `android.R.id.content`, with given arguments hosted by an empty [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity) using [instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#androidx.fragment.app.testing$launchFragmentInContainer(android.os.Bundle,%20kotlin.Int,%20kotlin.Function0((androidx.fragment.app.testing.launchFragmentInContainer.F)))/instantiate) to create the Fragment and waits for it to reach a resumed state. |

## androidx.lifecycle

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-core-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.10.0"
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.10.0"
}
```

### Kotlin

```kotlin
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

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<T\> | `https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(kotlinx.coroutines.flow.Flow).asLiveData(kotlin.coroutines.CoroutineContext,%20kotlin.Long)(context: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/index.html = EmptyCoroutineContext, timeoutInMs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html = DEFAULT_TIMEOUT)` Creates a LiveData that has values collected from the origin [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<T\> | `https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(kotlinx.coroutines.flow.Flow).asLiveData(kotlin.coroutines.CoroutineContext,%20java.time.Duration)(context: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/index.html = EmptyCoroutineContext, timeout: https://developer.android.com/reference/java/time/Duration.html)` Creates a LiveData that has values collected from the origin [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |

##### For [org.reactivestreams.Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle)

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<T\> | `Publisher<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(org.reactivestreams.Publisher).toLiveData()()` Creates an observable [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) stream from a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle). |

##### For [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)

|---|---|
| [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)\<T\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).asFlow()()` Creates a [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) containing values dispatched by originating [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData): at the start a flow collector receives the latest value held by LiveData and then observes LiveData updates. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<X\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<X>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).distinctUntilChanged()()` Creates a new [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) object does not emit a value until the source `this` LiveData value has been changed. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<Y\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<X>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).map(kotlin.Function1)(crossinline transform: (X) -> Y)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) mapped from `this` LiveData by applying [transform](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$map(androidx.lifecycle.LiveData((androidx.lifecycle.map.X)),%20kotlin.Function1((androidx.lifecycle.map.X,%20androidx.lifecycle.map.Y)))/transform) to each value set on `this` LiveData. |
| [Observer](https://developer.android.com/reference/kotlin/androidx/lifecycle/Observer)\<T\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).observe(androidx.lifecycle.LifecycleOwner,%20kotlin.Function1)(owner: https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner, crossinline onChanged: (T) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Adds the given [onChanged](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)),%20androidx.lifecycle.LifecycleOwner,%20kotlin.Function1((androidx.lifecycle.observe.T,%20kotlin.Unit)))/onChanged) lambda as an observer within the lifespan of the given [owner](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$observe(androidx.lifecycle.LiveData((androidx.lifecycle.observe.T)),%20androidx.lifecycle.LifecycleOwner,%20kotlin.Function1((androidx.lifecycle.observe.T,%20kotlin.Unit)))/owner) and returns a reference to observer. |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<Y\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<X>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).switchMap(kotlin.Function1)(crossinline transform: (X) -> https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<Y>)` Returns a [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) mapped from the input `this` `LiveData` by applying [transform](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$switchMap(androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.X)),%20kotlin.Function1((androidx.lifecycle.switchMap.X,%20androidx.lifecycle.LiveData((androidx.lifecycle.switchMap.Y)))))/transform) to each value set on `this`. |
| Publisher\<T\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData<T>.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LiveData).toPublisher(androidx.lifecycle.LifecycleOwner)(lifecycle: https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` Adapts the given [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) stream to a ReactiveStreams [Publisher](https://developer.android.com/reference/kotlin/androidx/lifecycle). |

##### For [ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider)

|---|---|
| VM | `https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.ViewModelProvider).get()()` Returns an existing ViewModel or creates a new one in the scope (usually, a fragment or an activity), associated with this `ViewModelProvider`. |

##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|---|---|
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LifecycleOwner).whenCreated(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:CREATED) state. |
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LifecycleOwner).whenResumed(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:RESUMED) state. |
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LifecycleOwner).whenStarted(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:STARTED) state. |

##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)

|---|---|
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).whenCreated(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:CREATED) state. |
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).whenResumed(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.RESUMED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:RESUMED) state. |
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).whenStarted(kotlin.coroutines.SuspendFunction1)(block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given block when the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle) is at least in [Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#ENUM_VALUE:STARTED) state. |
| suspend T | `https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).whenStateAtLeast(androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1)(minState: https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State, block: suspend https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html.() -> T)` Runs the given [block](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/block) on a [CoroutineDispatcher](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/index.html) that executes the [block](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/block) on the main thread and suspends the execution unless the [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)'s state is at least [minState](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$whenStateAtLeast(androidx.lifecycle.Lifecycle,%20androidx.lifecycle.Lifecycle.State,%20kotlin.coroutines.SuspendFunction1((kotlinx.coroutines.CoroutineScope,%20androidx.lifecycle.whenStateAtLeast.T)))/minState). |

#### Extension properties

##### For [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)

|---|---|
| [LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).coroutineScope:androidx.lifecycle.LifecycleCoroutineScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)

|---|---|
| [LifecycleCoroutineScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleCoroutineScope) | `https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.LifecycleOwner).lifecycleScope:androidx.lifecycle.LifecycleCoroutineScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)'s [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle). |

##### For [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)

|---|---|
| [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) | `https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel.https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.ViewModel).viewModelScope:kotlinx.coroutines.CoroutineScope()` [CoroutineScope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html) tied to this [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel). |

#### Top-level functions

|---|---|
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<T\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#liveData(kotlin.coroutines.CoroutineContext,%20kotlin.Long,%20kotlin.coroutines.SuspendFunction1)(context: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/index.html = EmptyCoroutineContext, timeoutInMs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html = DEFAULT_TIMEOUT, block: suspend https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope<T>.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Builds a LiveData that has values yielded from the given [block](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext,%20kotlin.Long,%20kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)),%20kotlin.Unit)))/block) that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<T\> | `https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#liveData(kotlin.coroutines.CoroutineContext,%20java.time.Duration,%20kotlin.coroutines.SuspendFunction1)(context: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/index.html = EmptyCoroutineContext, timeout: https://developer.android.com/reference/java/time/Duration.html, block: suspend https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope<T>.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Builds a LiveData that has values yielded from the given [block](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#androidx.lifecycle$liveData(kotlin.coroutines.CoroutineContext,%20java.time.Duration,%20kotlin.coroutines.SuspendFunction1((androidx.lifecycle.LiveDataScope((androidx.lifecycle.liveData.T)),%20kotlin.Unit)))/block) that executes on a [LiveDataScope](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveDataScope). |

## androidx.navigation

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-runtime-ktx:2.9.7"
    implementation "androidx.navigation:navigation-fragment-ktx:2.9.7"
    implementation "androidx.navigation:navigation-ui-ktx:2.9.7"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-runtime-ktx:2.9.7")
    implementation("androidx.navigation:navigation-fragment-ktx:2.9.7")
    implementation("androidx.navigation:navigation-ui-ktx:2.9.7")
}
```

#### Extension functions

##### For [android.app.Activity](https://developer.android.com/reference/android/app/Activity.html)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) | `https://developer.android.com/reference/android/app/Activity.html.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(android.app.Activity).findNavController(kotlin.Int)(@IdRes viewId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) given the id of a View and its containing [Activity](https://developer.android.com/reference/android/app/Activity.html). |
| [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)\<Args\> | `https://developer.android.com/reference/android/app/Activity.html.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(android.app.Activity).navArgs()()` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the Activity's extras as an Args instance. |

##### For [android.view.View](https://developer.android.com/reference/android/view/View.html)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) | `https://developer.android.com/reference/android/view/View.html.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(android.view.View).findNavController()()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) associated with a [View](https://developer.android.com/reference/android/view/View.html). |

##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraphBuilder).activity(kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigatorDestinationBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [ActivityNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraphBuilder).navigation(kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, @IdRes startDestination: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a nested [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraph).contains(kotlin.Int)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns `true` if a destination with `id` is found in this navigation graph. |
| operator [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraph).get(kotlin.Int)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the destination with `id`. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraph).minusAssign(androidx.navigation.NavDestination)(node: https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)` Removes `node` from this navigation graph. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraph).plusAssign(androidx.navigation.NavDestination)(node: https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)` Adds a destination to this NavGraph. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraph).plusAssign(androidx.navigation.NavGraph)(other: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph)` Add all destinations from another collection to this one. |

##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)

|---|---|
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavController.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavController).createGraph(kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, @IdRes startDestination: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavHost](https://developer.android.com/reference/kotlin/androidx/navigation/NavHost)

|---|---|
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavHost.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavHost).createGraph(kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, @IdRes startDestination: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |

##### For [NavigatorProvider](https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider)

|---|---|
| operator T | `https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavigatorProvider).get(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) by name. |
| operator T | `https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavigatorProvider).get(kotlin.reflect.KClass)(clazz: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>)` Retrieves a registered [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name). |
| [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavigatorProvider).navigation(kotlin.Int,%20kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0, @IdRes startDestination: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [NavGraph](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph) |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavigatorProvider).plusAssign(androidx.navigation.Navigator)(navigator: https://developer.android.com/reference/kotlin/androidx/navigation/Navigator<out https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination>)` Register a navigator using the name provided by the [Navigator.Name annotation](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator.Name). |
| operator [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator)\<out [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)!\>? | `https://developer.android.com/reference/kotlin/androidx/navigation/NavigatorProvider.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavigatorProvider).set(kotlin.String,%20androidx.navigation.Navigator)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, navigator: https://developer.android.com/reference/kotlin/androidx/navigation/Navigator<out https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination>)` Register a [Navigator](https://developer.android.com/reference/kotlin/androidx/navigation/Navigator) by name. |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

|---|---|
| [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html)\<VM\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.fragment.app.Fragment).navGraphViewModels(kotlin.Int,%20kotlin.Function0)(@IdRes navGraphId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, noinline factoryProducer: () -> https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory = null)` Returns a property delegate to access a [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) scoped to a navigation graph present on the {@link NavController} back stack: |

#### Top-level functions

|---|---|
| [ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) | `https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#ActivityNavigatorExtras(androidx.core.app.ActivityOptionsCompat,%20kotlin.Int)(activityOptions: https://developer.android.com/reference/kotlin/androidx/core/app/ActivityOptionsCompat? = null, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0)` Create a new [ActivityNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Extras) instance with a specific [ActivityOptionsCompat](https://developer.android.com/reference/kotlin/androidx/core/app/ActivityOptionsCompat) instance and/or any `Intent.FLAG_ACTIVITY_` flags. |
| [NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions) | `https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#navOptions(kotlin.Function1)(optionsBuilder: https://developer.android.com/reference/kotlin/androidx/navigation/NavOptionsBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [NavOptions](https://developer.android.com/reference/kotlin/androidx/navigation/NavOptions) |

## androidx.navigation.fragment

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-fragment-ktx:2.9.7"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-fragment-ktx:2.9.7")
}
```

#### Extension functions

##### For [NavGraphBuilder](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).dialog(kotlin.Int)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).dialog(kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigatorDestinationBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [DialogFragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/DialogFragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).fragment(kotlin.Int)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).fragment(kotlin.Int,%20kotlin.Function1)(@IdRes id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, builder: https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigatorDestinationBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Construct a new [FragmentNavigator.Destination](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Destination) |

##### For [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

|---|---|
| [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.fragment.app.Fragment).findNavController()()` Find a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) given a [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) |
| [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)\<Args\> | `https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.fragment.app.Fragment).navArgs()()` Returns a [Lazy](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-lazy/index.html) delegate to access the Fragment's arguments as an Args instance. |

#### Top-level functions

|---|---|
| [FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) | `https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#FragmentNavigatorExtras(kotlin.Pair)(vararg sharedElements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<https://developer.android.com/reference/android/view/View.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>)` Create a new [FragmentNavigator.Extras](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/FragmentNavigator.Extras) instance with the given shared elements |

## androidx.navigation.ui

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation:navigation-ui-ktx:2.9.7"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation:navigation-ui-ktx:2.9.7")
}
```

#### Extension functions

##### For [android.view.MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/android/view/MenuItem.html.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(android.view.MenuItem).onNavDestinationSelected(androidx.navigation.NavController)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` Attempt to navigate to the [NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/ui) associated with this [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html). |

##### For [androidx.appcompat.app.AppCompatActivity](https://developer.android.com/reference/kotlin/androidx/navigation/ui)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.appcompat.app.AppCompatActivity).setupActionBarWithNavController(androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout?)` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.appcompat.app.AppCompatActivity).setupActionBarWithNavController(androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, configuration: https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up the ActionBar returned by [AppCompatActivity.getSupportActionBar](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

##### For [androidx.appcompat.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/navigation/ui)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.appcompat.widget.Toolbar).setupWithNavController(androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout?)` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.appcompat.widget.Toolbar).setupWithNavController(androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, configuration: https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.appbar.CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `CollapsingToolbarLayout.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(com.google.android.material.appbar.CollapsingToolbarLayout).setupWithNavController(androidx.appcompat.widget.Toolbar,%20androidx.navigation.NavController,%20androidx.drawerlayout.widget.DrawerLayout)(toolbar: https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar, navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout?)` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `CollapsingToolbarLayout.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(com.google.android.material.appbar.CollapsingToolbarLayout).setupWithNavController(androidx.appcompat.widget.Toolbar,%20androidx.navigation.NavController,%20androidx.navigation.ui.AppBarConfiguration)(toolbar: https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar, navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController, configuration: https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration = AppBarConfiguration(navController.graph))` Sets up a [CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui) and [Toolbar](https://developer.android.com/reference/kotlin/androidx/appcompat/widget/Toolbar) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.bottomnavigation.BottomNavigationView](https://developer.android.com/reference/kotlin/androidx/navigation/ui)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `BottomNavigationView.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(com.google.android.material.bottomnavigation.BottomNavigationView).setupWithNavController(androidx.navigation.NavController)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` Sets up a [BottomNavigationView](https://developer.android.com/reference/kotlin/androidx/navigation/ui) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

##### For [com.google.android.material.navigation.NavigationView](https://developer.android.com/reference/kotlin/androidx/navigation/ui)

|---|---|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `NavigationView.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(com.google.android.material.navigation.NavigationView).setupWithNavController(androidx.navigation.NavController)(navController: https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` Sets up a [NavigationView](https://developer.android.com/reference/kotlin/androidx/navigation/ui) for use with a [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

##### For [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavController.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.navigation.NavController).navigateUp(androidx.drawerlayout.widget.DrawerLayout)(drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout?)` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/navigation/NavController.https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#(androidx.navigation.NavController).navigateUp(androidx.navigation.ui.AppBarConfiguration)(appBarConfiguration: https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration)` Handles the Up button by delegating its behavior to the given [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController). |

#### Top-level functions

|---|---|
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration(androidx.navigation.NavGraph,%20androidx.drawerlayout.widget.DrawerLayout,%20kotlin.Function0)(navGraph: https://developer.android.com/reference/kotlin/androidx/navigation/NavGraph, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/navigation/ui). |
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration(android.view.Menu,%20androidx.drawerlayout.widget.DrawerLayout,%20kotlin.Function0)(topLevelMenu: https://developer.android.com/reference/android/view/Menu.html, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/navigation/ui). |
| [AppBarConfiguration](https://developer.android.com/reference/kotlin/androidx/navigation/ui/AppBarConfiguration) | `https://developer.android.com/reference/kotlin/androidx/navigation/ui/package-summary#AppBarConfiguration(kotlin.collections.Set,%20androidx.drawerlayout.widget.DrawerLayout,%20kotlin.Function0)(topLevelDestinationIds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>, drawerLayout: https://developer.android.com/reference/kotlin/androidx/drawerlayout/widget/DrawerLayout? = null, noinline fallbackOnNavigateUpListener: () -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = { false })` Configuration options for [NavigationUI](https://developer.android.com/reference/kotlin/androidx/navigation/ui/NavigationUI) methods that interact with implementations of the app bar pattern such as [android.support.v7.widget.Toolbar](https://developer.android.com/reference/kotlin/androidx/navigation/ui), [android.support.design.widget.CollapsingToolbarLayout](https://developer.android.com/reference/kotlin/androidx/navigation/ui), and [android.support.v7.app.ActionBar](https://developer.android.com/reference/kotlin/androidx/navigation/ui). |

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

##### For [Factory](https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory)

|---|---|
| Flowable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toFlowable(androidx.paging.PagedList.Config,%20androidx.paging.toFlowable.Key,%20androidx.paging.PagedList.BoundaryCallback,%20io.reactivex.Scheduler,%20io.reactivex.Scheduler,%20io.reactivex.BackpressureStrategy)(config: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Flowable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toFlowable(kotlin.Int,%20androidx.paging.toFlowable.Key,%20androidx.paging.PagedList.BoundaryCallback,%20io.reactivex.Scheduler,%20io.reactivex.Scheduler,%20io.reactivex.BackpressureStrategy)(pageSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null, backpressureStrategy: BackpressureStrategy = BackpressureStrategy.LATEST)` Constructs a `Flowable<PagedList>`, from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toLiveData(androidx.paging.PagedList.Config,%20androidx.paging.toLiveData.Key,%20androidx.paging.PagedList.BoundaryCallback,%20java.util.concurrent.Executor)(config: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchExecutor: https://developer.android.com/reference/java/util/concurrent/Executor.html = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toLiveData(kotlin.Int,%20androidx.paging.toLiveData.Key,%20androidx.paging.PagedList.BoundaryCallback,%20java.util.concurrent.Executor)(pageSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchExecutor: https://developer.android.com/reference/java/util/concurrent/Executor.html = ArchTaskExecutor.getIOThreadExecutor())` Constructs a `LiveData<PagedList>`, from this `DataSource.Factory`, convenience for [LivePagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/LivePagedListBuilder). |
| Observable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toObservable(androidx.paging.PagedList.Config,%20androidx.paging.toObservable.Key,%20androidx.paging.PagedList.BoundaryCallback,%20io.reactivex.Scheduler,%20io.reactivex.Scheduler)(config: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder). |
| Observable\<[PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\>\> | `https://developer.android.com/reference/kotlin/androidx/paging/DataSource.Factory<Key, Value>.https://developer.android.com/reference/kotlin/androidx/paging/package-summary#(androidx.paging.DataSource.Factory).toObservable(kotlin.Int,%20androidx.paging.toObservable.Key,%20androidx.paging.PagedList.BoundaryCallback,%20io.reactivex.Scheduler,%20io.reactivex.Scheduler)(pageSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, initialLoadKey: Key? = null, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, fetchScheduler: Scheduler? = null, notifyScheduler: Scheduler? = null)` Constructs a `Observable<PagedList>` from this `DataSource.Factory`, convenience for [RxPagedListBuilder](https://developer.android.com/reference/kotlin/androidx/paging/RxPagedListBuilder). |

#### Top-level functions

|---|---|
| [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config) | `https://developer.android.com/reference/kotlin/androidx/paging/package-summary#Config(kotlin.Int,%20kotlin.Int,%20kotlin.Boolean,%20kotlin.Int,%20kotlin.Int)(pageSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, prefetchDistance: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = pageSize, enablePlaceholders: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true, initialLoadSizeHint: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = pageSize * PagedList.Config.Builder.DEFAULT_INITIAL_PAGE_MULTIPLIER, maxSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = PagedList.Config.MAX_SIZE_UNBOUNDED)` Constructs a [PagedList.Config](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config), convenience for [PagedList.Config.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config.Builder). |
| [PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList)\<Value\> | `https://developer.android.com/reference/kotlin/androidx/paging/package-summary#PagedList(androidx.paging.DataSource,%20androidx.paging.PagedList.Config,%20java.util.concurrent.Executor,%20java.util.concurrent.Executor,%20androidx.paging.PagedList.BoundaryCallback,%20androidx.paging.PagedList.Key)(dataSource: https://developer.android.com/reference/kotlin/androidx/paging/DataSource<Key, Value>, config: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Config, notifyExecutor: https://developer.android.com/reference/java/util/concurrent/Executor.html, fetchExecutor: https://developer.android.com/reference/java/util/concurrent/Executor.html, boundaryCallback: https://developer.android.com/reference/kotlin/androidx/paging/PagedList.BoundaryCallback<Value>? = null, initialKey: Key? = null)` Constructs a [PagedList](https://developer.android.com/reference/kotlin/androidx/paging/PagedList), convenience for [PagedList.Builder](https://developer.android.com/reference/kotlin/androidx/paging/PagedList.Builder). |

## androidx.palette.graphics

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.palette:palette-ktx:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.palette:palette-ktx:1.0.0")
}
```

#### Extension functions

##### For [Palette](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette)

|---|---|
| operator [Palette.Swatch](https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette.Swatch)? | `https://developer.android.com/reference/kotlin/androidx/palette/graphics/Palette.https://developer.android.com/reference/kotlin/androidx/palette/graphics/package-summary#(androidx.palette.graphics.Palette).get(androidx.palette.graphics.Target)(target: https://developer.android.com/reference/kotlin/androidx/palette/graphics/Target)` Returns the selected swatch for the given target from the palette, or `null` if one could not be found. |

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

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup)

|---|---|
| operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).contains(androidx.preference.Preference)(preference: https://developer.android.com/reference/kotlin/androidx/preference/Preference)` Returns `true` if `preference` is found in this preference group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).forEach(kotlin.Function1)(action: (preference: https://developer.android.com/reference/kotlin/androidx/preference/Preference) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each preference in this preference group. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).forEachIndexed(kotlin.Function2)(action: (index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, preference: https://developer.android.com/reference/kotlin/androidx/preference/Preference) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Performs the given action on each preference in this preference group, providing its sequential index. |
| operator T? | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).get(kotlin.CharSequence)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)` Returns the preference with `key`, or `null` if no preference with `key` is found. |
| operator [Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).get(kotlin.Int)(index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the preference at `index`. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).isEmpty()()` Returns true if this preference group contains no preferences. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).isNotEmpty()()` Returns true if this preference group contains one or more preferences. |
| operator [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)\<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)\> | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).iterator()()` Returns a [MutableIterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html) over the preferences in this preference group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).minusAssign(androidx.preference.Preference)(preference: https://developer.android.com/reference/kotlin/androidx/preference/Preference)` Removes `preference` from this preference group. |
| operator [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).plusAssign(androidx.preference.Preference)(preference: https://developer.android.com/reference/kotlin/androidx/preference/Preference)` Adds `preference` to this preference group. |

#### Extension properties

##### For [PreferenceGroup](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup)

|---|---|
| [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html)\<[Preference](https://developer.android.com/reference/kotlin/androidx/preference/Preference)\> | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).children:kotlin.sequences.Sequence()` Returns a [Sequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/-sequence/index.html) over the preferences in this preference group. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/kotlin/androidx/preference/PreferenceGroup.https://developer.android.com/reference/kotlin/androidx/preference/package-summary#(androidx.preference.PreferenceGroup).size:kotlin.Int()` Returns the number of preferences in this preference group. |

## androidx.room

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.room:room-ktx:2.8.4"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.room:room-ktx:2.8.4")
}
```

#### Extension functions

##### For [RoomDatabase](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase)

|---|---|
| suspend R | `https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.https://developer.android.com/reference/kotlin/androidx/room/package-summary#(androidx.room.RoomDatabase).withTransaction(kotlin.coroutines.SuspendFunction0)(block: suspend () -> R)` Calls the specified suspending [block](https://developer.android.com/reference/kotlin/androidx/room/package-summary#androidx.room$withTransaction(androidx.room.RoomDatabase,%20kotlin.coroutines.SuspendFunction0((androidx.room.withTransaction.R)))/block) in a database transaction. |

## androidx.slice.builders

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.slice:slice-builders-ktx:1.0.0-alpha08"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.slice:slice-builders-ktx:1.0.0-alpha08")
}
```

#### Extension functions

##### For [GridRowBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl)

|---|---|
| [GridRowBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.GridRowBuilderDsl).cell(kotlin.Function1)(buildCell: https://developer.android.com/reference/kotlin/androidx/slice/builders/CellBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [GridRowBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.GridRowBuilderDsl).seeMoreCell(kotlin.Function1)(buildCell: https://developer.android.com/reference/kotlin/androidx/slice/builders/CellBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |

##### For [ListBuilderDsl](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl)

|---|---|
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).gridRow(kotlin.Function1)(buildGrid: https://developer.android.com/reference/kotlin/androidx/slice/builders/GridRowBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).header(kotlin.Function1)(buildHeader: https://developer.android.com/reference/kotlin/androidx/slice/builders/HeaderBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).inputRange(kotlin.Function1)(buildInputRange: https://developer.android.com/reference/kotlin/androidx/slice/builders/InputRangeBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).range(kotlin.Function1)(buildRange: https://developer.android.com/reference/kotlin/androidx/slice/builders/RangeBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).row(kotlin.Function1)(buildRow: https://developer.android.com/reference/kotlin/androidx/slice/builders/RowBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |
| [ListBuilder](https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilder) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#(androidx.slice.builders.ListBuilderDsl).seeMoreRow(kotlin.Function1)(buildRow: https://developer.android.com/reference/kotlin/androidx/slice/builders/RowBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` <br /> |

#### Top-level functions

|---|---|
| [Slice](https://developer.android.com/reference/kotlin/androidx/slice/Slice) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#list(android.content.Context,%20android.net.Uri,%20kotlin.Long,%20kotlin.Function1)(context: https://developer.android.com/reference/android/content/Context.html, uri: https://developer.android.com/reference/android/net/Uri.html, ttl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, addRows: https://developer.android.com/reference/kotlin/androidx/slice/builders/ListBuilderDsl.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Reduces verbosity required to build a Slice in Kotlin. |
| [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#tapSliceAction(android.app.PendingIntent,%20androidx.core.graphics.drawable.IconCompat,%20kotlin.Int,%20kotlin.CharSequence)(pendingIntent: https://developer.android.com/reference/android/app/PendingIntent.html, icon: https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/IconCompat, imageMode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = ICON_IMAGE, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)` Factory method to build a tappable [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction). |
| [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction) | `https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary#toggleSliceAction(android.app.PendingIntent,%20androidx.core.graphics.drawable.IconCompat,%20kotlin.CharSequence,%20kotlin.Boolean)(pendingIntent: https://developer.android.com/reference/android/app/PendingIntent.html, icon: https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/IconCompat? = null, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html, isChecked: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Factory method to build a toggleable [SliceAction](https://developer.android.com/reference/kotlin/androidx/slice/builders/SliceAction). |

## androidx.sqlite.db

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.sqlite:sqlite-ktx:2.6.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.sqlite:sqlite-ktx:2.6.2")
}
```

#### Extension functions

##### For [SupportSQLiteDatabase](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase)

|---|---|
| T | `https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase.https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary#(androidx.sqlite.db.SupportSQLiteDatabase).transaction(kotlin.Boolean,%20kotlin.Function1)(exclusive: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = true, body: https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteDatabase.() -> T)` Run [body](https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary#androidx.sqlite.db$transaction(androidx.sqlite.db.SupportSQLiteDatabase,%20kotlin.Boolean,%20kotlin.Function1((androidx.sqlite.db.SupportSQLiteDatabase,%20androidx.sqlite.db.transaction.T)))/body) in a transaction marking it as successful if it completes without exception. |

## androidx.work

#### Dependency

#### Extension functions

##### For [com.google.common.util.concurrent.ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html)

|---|---|
| suspend R | `https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html<R>.https://developer.android.com/reference/kotlin/androidx/work/package-summary#(com.google.common.util.concurrent.ListenableFuture).await()()` Awaits for the completion of the [ListenableFuture](https://guava.dev/releases/27.0.1-jre/api/docs/com/google/common/util/concurrent/ListenableFuture.html) without blocking a thread. |

##### For [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation)

|---|---|
| suspend [Operation.State.SUCCESS](https://developer.android.com/reference/kotlin/androidx/work/Operation.State.SUCCESS)! | `https://developer.android.com/reference/kotlin/androidx/work/Operation.https://developer.android.com/reference/kotlin/androidx/work/package-summary#(androidx.work.Operation).await()()` Awaits an [Operation](https://developer.android.com/reference/kotlin/androidx/work/Operation) without blocking a thread. |

##### For [Data](https://developer.android.com/reference/kotlin/androidx/work/Data)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/kotlin/androidx/work/Data.https://developer.android.com/reference/kotlin/androidx/work/package-summary#(androidx.work.Data).hasKeyWithValueOfType(kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns true if the instance of [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) has a value corresponding to the given [key](https://developer.android.com/reference/kotlin/androidx/work/package-summary#androidx.work$hasKeyWithValueOfType(androidx.work.Data,%20kotlin.String)/key) with an expected type T. |

##### For [Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder)

|---|---|
| [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder.https://developer.android.com/reference/kotlin/androidx/work/package-summary#(androidx.work.OneTimeWorkRequest.Builder).setInputMerger(kotlin.reflect.KClass)(@NonNull inputMerger: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<out https://developer.android.com/reference/kotlin/androidx/work/InputMerger>)` Sets an [InputMerger](https://developer.android.com/reference/kotlin/androidx/work/InputMerger) on the [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder). |

#### Top-level functions

|---|---|
| [OneTimeWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#OneTimeWorkRequestBuilder()()` Creates a [OneTimeWorkRequest](https://developer.android.com/reference/kotlin/androidx/work/OneTimeWorkRequest) with the given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder(kotlin.Long,%20java.util.concurrent.TimeUnit)(repeatInterval: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, repeatIntervalTimeUnit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder(java.time.Duration)(repeatInterval: https://developer.android.com/reference/java/time/Duration.html)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder(kotlin.Long,%20java.util.concurrent.TimeUnit,%20kotlin.Long,%20java.util.concurrent.TimeUnit)(repeatInterval: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, repeatIntervalTimeUnit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html, flexTimeInterval: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, flexTimeIntervalUnit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker). |
| [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#PeriodicWorkRequestBuilder(java.time.Duration,%20java.time.Duration)(repeatInterval: https://developer.android.com/reference/java/time/Duration.html, flexTimeInterval: https://developer.android.com/reference/java/time/Duration.html)` Creates a [PeriodicWorkRequest.Builder](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder) with a given [ListenableWorker](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker). |
| [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) | `https://developer.android.com/reference/kotlin/androidx/work/package-summary#workDataOf(kotlin.Pair)(vararg pairs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Converts a list of pairs to a [Data](https://developer.android.com/reference/kotlin/androidx/work/Data) object. |

## androidx.work.testing

#### Dependency

### Groovy

```groovy
dependencies {
    implementation "androidx.work:work-testing:2.11.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.work:work-testing:2.11.1")
}
```

#### Top-level functions

|---|---|
| [TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder)\<W\> | `https://developer.android.com/reference/kotlin/androidx/work/testing/package-summary#TestListenableWorkerBuilder(android.content.Context,%20androidx.work.Data,%20kotlin.collections.List,%20kotlin.Int,%20kotlin.collections.List,%20kotlin.collections.List)(context: https://developer.android.com/reference/android/content/Context.html, inputData: https://developer.android.com/reference/kotlin/androidx/work/Data = Data.EMPTY, tags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList(), runAttemptCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 1, triggeredContentUris: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://developer.android.com/reference/android/net/Uri.html> = emptyList(), triggeredContentAuthorities: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList())` Builds an instance of [TestListenableWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestListenableWorkerBuilder). |
| [TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder)\<W\> | `https://developer.android.com/reference/kotlin/androidx/work/testing/package-summary#TestWorkerBuilder(android.content.Context,%20java.util.concurrent.Executor,%20androidx.work.Data,%20kotlin.collections.List,%20kotlin.Int,%20kotlin.collections.List,%20kotlin.collections.List)(context: https://developer.android.com/reference/android/content/Context.html, executor: https://developer.android.com/reference/java/util/concurrent/Executor.html, inputData: https://developer.android.com/reference/kotlin/androidx/work/Data = Data.EMPTY, tags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList(), runAttemptCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 1, triggeredContentUris: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://developer.android.com/reference/android/net/Uri.html> = emptyList(), triggeredContentAuthorities: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList())` Builds an instance of [TestWorkerBuilder](https://developer.android.com/reference/kotlin/androidx/work/testing/TestWorkerBuilder). |

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

##### For [com.google.android.play.core.appupdate.AppUpdateManager](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html)

|---|---|
| suspend [AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateManager).requestAppUpdateInfo()()` Requests the update availability for the current app |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateManager).requestCompleteUpdate()()` For a flexible update flow, triggers the completion of the update. |
| Flow\<[AppUpdateResult](https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/AppUpdateResult)\> | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateManager).requestUpdateFlow()()` Entry point for monitoring the availability and progress of updates. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateManager).startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo,%20kotlin.Int,%20androidx.fragment.app.Fragment,%20kotlin.Int)(appUpdateInfo: https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html, appUpdateType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, fragment: Fragment, requestCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` A version of [AppUpdateManager.startUpdateFlowForResult](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager.html#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo, int, android.app.Activity, int)) that accepts an AndroidX Fragment for returning the result. |

##### For [com.google.android.play.core.splitinstall.SplitInstallManager](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html)

|---|---|
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestCancelInstall(kotlin.Int)(sessionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Suspend version of [SplitInstallManager.cancelInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#cancelInstall(int)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestDeferredInstall(kotlin.collections.List)(moduleNames: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>)` Suspend version of [SplitInstallManager.deferredInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredInstall(java.util.List<java.lang.String>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestDeferredLanguageInstall(kotlin.collections.List)(languages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://developer.android.com/reference/java/util/Locale.html>)` Suspend version of [SplitInstallManager.deferredLanguageInstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredLanguageInstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestDeferredLanguageUninstall(kotlin.collections.List)(languages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://developer.android.com/reference/java/util/Locale.html>)` Suspend version of [SplitInstallManager.deferredLanguageUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredLanguageUninstall(java.util.List<java.util.Locale>)) |
| suspend [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestDeferredUninstall(kotlin.collections.List)(moduleNames: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>)` Suspend version of [SplitInstallManager.deferredUninstall](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#deferredUninstall(java.util.List<java.lang.String>)) |
| suspend [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestInstall(kotlin.collections.List,%20kotlin.collections.List)(modules: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = listOf(), languages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = listOf())` Initiates installation of the requested modules/languages. |
| Flow\<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)\> | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestProgressFlow()()` Creates and returns a buffered [Flow](https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx) that will deliver all progress events for ongoing split installations. |
| suspend [SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestSessionState(kotlin.Int)(sessionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Suspend version of [SplitInstallManager.getSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#getSessionState(int)) |
| suspend [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)\<[SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)\> | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).requestSessionStates()()` Suspend version of [SplitInstallManager.getSessionStates](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#getSessionStates()) |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallManager).startConfirmationDialogForResult(com.google.android.play.core.splitinstall.SplitInstallSessionState,%20androidx.fragment.app.Fragment,%20kotlin.Int)(sessionState: https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html, fragment: Fragment, requestCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` A version of [SplitInstallManager.startConfirmationDialogForResult](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager.html#startConfirmationDialogForResult(com.google.android.play.core.splitinstall.SplitInstallSessionState, android.app.Activity, int)) that accepts an AndroidX Fragment for returning the result. |

#### Extension properties

##### For [com.google.android.play.core.appupdate.AppUpdateInfo](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html)

|---|---|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateInfo).installStatus:kotlin.Int()` Returns the progress status of the update. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateInfo).isFlexibleUpdateAllowed:kotlin.Boolean()` Returns `true` if flexible update is allowed. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.appupdate.AppUpdateInfo).isImmediateUpdateAllowed:kotlin.Boolean()` Returns `true` if immediate update is allowed. |

##### For [com.google.android.play.core.install.InstallState](https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html)

|---|---|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.install.InstallState).hasTerminalStatus:kotlin.Boolean()` This signifies that this is a terminal status (there will be no more updates) and should be handled accordingly (success, cancellation or failure). |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.install.InstallState).installErrorCode:kotlin.Int()` Returns the error code for an install, or {@link InstallErrorCode#NO_ERROR}. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.install.InstallState).installStatus:kotlin.Int()` Returns the status of an install. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)! | `https://developer.android.com/reference/com/google/android/play/core/install/InstallState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.install.InstallState).packageName:kotlin.String()` Returns the package name for the app being installed. |

##### For [com.google.android.play.core.splitinstall.SplitInstallSessionState](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html)

|---|---|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).bytesDownloaded:kotlin.Long()` The bytes downloaded by this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).errorCode:kotlin.Int()` The error code of this update. |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).hasTerminalStatus:kotlin.Boolean()` Signifies that this update is terminal, meaning there will be no more updates for this session. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)\<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)\> | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).languages:kotlin.collections.List()` The languages included by this update. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)\<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)\> | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).moduleNames:kotlin.collections.List()` The modules included by this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).sessionId:kotlin.Int()` The session id of this update. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).status:kotlin.Int()` The status code of this update. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html.https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#(com.google.android.play.core.splitinstall.SplitInstallSessionState).totalBytesToDownload:kotlin.Long()` The total bytes to download by this update. |

#### Top-level functions

|---|---|
| [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.html) | `https://developer.android.com/reference/kotlin/com/google/android/play/core/ktx/package-summary#SplitInstallStateUpdatedListener(kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1,%20kotlin.Function1)(onRequiresConfirmation: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html, onInstalled: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html, onFailed: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onPending: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onDownloaded: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onDownloading: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onInstalling: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onCanceling: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onCanceled: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onNonTerminalStatus: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {}, onTerminalStatus: (https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html = {})` A convenience function for creating a [SplitInstallStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener.html). |