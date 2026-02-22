---
title: https://developer.android.com/kotlin/ktx
url: https://developer.android.com/kotlin/ktx
source: md.txt
---

# Android KTX
Part of [Android Jetpack](https://developer.android.com/jetpack).

[Video](https://www.youtube.com/watch?v=nKzvYBMdm54)

Android KTX is a set of Kotlin extensions that are included with Android
[Jetpack](https://developer.android.com/jetpack) and other Android libraries. KTX extensions provide concise,
idiomatic Kotlin to Jetpack, Android platform, and other APIs. To do so, these
extensions leverage several Kotlin language features, including the following:

- Extension functions
- Extension properties
- Lambdas
- Named parameters
- Parameter default values
- Coroutines

As an example, when working with
[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences), you must
[create an editor](https://developer.android.com/reference/android/content/SharedPreferences#edit())
before you can make modifications to the preferences data. You must also apply
or commit those changes when you are finished editing, as shown in the following
example:

    sharedPreferences
            .edit()  // create an Editor
            .putBoolean("key", value)
            .apply() // write to disk asynchronously

Kotlin lambdas are a perfect fit for this use case. They allow you to take a
more concise approach by passing a block of code to execute after the editor is
created, letting the code execute, and then letting the `SharedPreferences` API
apply the changes atomically.

Here's an example of one of the Android KTX Core functions,
[`SharedPreferences.edit`](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary#edit),
which adds an edit function to `SharedPreferences`. This function takes an
optional `boolean` flag as its first argument that indicates whether to commit
or apply the changes. It also receives an action to perform on the
`SharedPreferences` editor in the form of a lambda.

    // SharedPreferences.edit extension function signature from Android KTX - Core
    // inline fun SharedPreferences.edit(
    //         commit: Boolean = false,
    //         action: SharedPreferences.Editor.() -> Unit)

    // Commit a new value asynchronously
    sharedPreferences.edit { putBoolean("key", value) }

    // Commit a new value synchronously
    sharedPreferences.edit(commit = true) { putBoolean("key", value) }

The caller can choose whether to commit or apply the changes. The `action`
lambda is itself an anonymous extension function on `SharedPreferences.Editor`
which returns `Unit`, as indicated by its signature. This is why inside the
block, you are able to perform the work directly on the
`SharedPreferences.Editor`.

Finally, the `SharedPreferences.edit()` signature contains the `inline` keyword.
This keyword tells the Kotlin compiler that it should copy and paste (or
*inline* ) the compiled bytecode for the function each time the function is used.
This avoids the overhead of instantiating a new class for every `action` each
time this function is called.

This pattern of passing code using lambdas, applying sensible defaults that can
be overridden, and adding these behaviors to existing APIs using `inline`
extension functions is typical of the enhancements provided by the Android KTX
library.

## Use Android KTX in your project

To start using Android KTX, add the following dependency to your project's
`build.gradle` file:

### Groovy

```groovy
repositories {
    google()
}
```

### Kotlin

```kotlin
repositories {
    google()
}
```

## AndroidX Modules

Android KTX is organized into modules, where each module contains one or more
packages.

You must include a dependency for each module artifact in your app's
`build.gradle` file. Remember to append the version number to the artifact.
You can find the latest version numbers in each artifact's corresponding section
in this topic.

Android KTX contains a [single core module](https://developer.android.com/kotlin/ktx#core) that provides Kotlin
extensions for common framework APIs and several domain-specific extensions.

With the exception of the core module, all KTX module artifacts replace the
underlying Java dependency in your `build.gradle` file. For example, you can
replace a `androidx.fragment:fragment` dependency with
`androidx.fragment:fragment-ktx`. This syntax helps to better manage
versioning and does not add additional dependency declaration requirements.

### Core KTX

The Core KTX module provides extensions for common libraries that are part of
the Android framework. These libraries do not have Java-based dependencies that
you need to add to `build.gradle`.

To include this module, add the following to your app's `build.gradle` file:

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

Here's a list of the packages that are contained in the Core KTX module:

- [androidx.core.animation](https://developer.android.com/reference/kotlin/androidx/core/animation/package-summary)
- [androidx.core.content](https://developer.android.com/reference/kotlin/androidx/core/content/package-summary)
- [androidx.core.content.res](https://developer.android.com/reference/kotlin/androidx/core/content/res/package-summary)
- [androidx.core.database](https://developer.android.com/reference/kotlin/androidx/core/database/package-summary)
- [androidx.core.database.sqlite](https://developer.android.com/reference/kotlin/androidx/core/database/sqlite/package-summary)
- [androidx.core.graphics](https://developer.android.com/reference/kotlin/androidx/core/graphics/package-summary)
- [androidx.core.graphics.drawable](https://developer.android.com/reference/kotlin/androidx/core/graphics/drawable/package-summary)
- [androidx.core.location](https://developer.android.com/reference/kotlin/androidx/core/location/package-summary)
- [androidx.core.net](https://developer.android.com/reference/kotlin/androidx/core/net/package-summary)
- [androidx.core.os](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary)
- [androidx.core.text](https://developer.android.com/reference/kotlin/androidx/core/text/package-summary)
- [androidx.core.transition](https://developer.android.com/reference/kotlin/androidx/core/transition/package-summary)
- [androidx.core.util](https://developer.android.com/reference/kotlin/androidx/core/util/package-summary)
- [androidx.core.view](https://developer.android.com/reference/kotlin/androidx/core/view/package-summary)
- [androidx.core.widget](https://developer.android.com/reference/kotlin/androidx/core/widget/package-summary)

### Collection KTX

The Collection extensions contain utility functions for working with Android's
memory-efficient collection libraries, including `ArrayMap`, `LongSparseArray`,
`LruCache`, and others.

To use this module, add the following to your app's `build.gradle` file:

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

Collection extensions take advantage of Kotlin's operator overloading to
simplify things like collection concatenation, as shown in the following
example:

    // Combine 2 ArraySets into 1.
    val combinedArraySet = arraySetOf(1, 2, 3) + arraySetOf(4, 5, 6)

    // Combine with numbers to create a new sets.
    val newArraySet = combinedArraySet + 7 + 8

### Fragment KTX

The
[Fragment KTX module](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#extension-functions-summary)
provides a number of extensions to simplify the fragment API.

To include this module, add the following to your app's `build.gradle` file:

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

With the Fragment KTX module, you can simplify fragment transactions with
lambdas, for example:

    fragmentManager().commit {
       addToBackStack("...")
       setCustomAnimations(
               R.anim.enter_anim,
               R.anim.exit_anim)
       add(fragment, "...")
    }

You can also bind to a `ViewModel` in one line by using the `viewModels` and
`activityViewModels` property delegates:

    // Get a reference to the ViewModel scoped to this Fragment
    val viewModel by viewModels<MyViewModel>()

    // Get a reference to the ViewModel scoped to its Activity
    val viewModel by activityViewModels<MyViewModel>()

### Lifecycle KTX

Lifecycle KTX defines a `LifecycleScope` for each
[`Lifecycle`](https://developer.android.com/topic/libraries/architecture/lifecycle) object. Any coroutine
launched in this scope is canceled when the `Lifecycle` is destroyed. You can
access the `CoroutineScope` of the `Lifecycle` by using the
`lifecycle.coroutineScope` or `lifecycleOwner.lifecycleScope` properties.

To include this module, add the following to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-runtime-ktx:2.10.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.10.0")
}
```

The following example demonstrates how to use `lifecycleOwner.lifecycleScope` to
create precomputed text asynchronously:

    class MyFragment: Fragment() {
        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            super.onViewCreated(view, savedInstanceState)
            viewLifecycleOwner.lifecycleScope.launch {
                val params = TextViewCompat.getTextMetricsParams(textView)
                val precomputedText = withContext(Dispatchers.Default) {
                    PrecomputedTextCompat.create(longTextContent, params)
                }
                TextViewCompat.setPrecomputedText(textView, precomputedText)
            }
        }
    }

### LiveData KTX

When using LiveData, you might need to calculate values asynchronously. For
example, you might want to retrieve a user's preferences and serve them to your
UI. For these cases, LiveData KTX provides a `liveData` builder function that
calls a `suspend` function and serves the result as a `LiveData` object.

To include this module, add the following to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.10.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.10.0")
}
```

In the following example, `loadUser()` is a suspend function declared elsewhere.
You can use the `liveData` builder function to call `loadUser()` asynchronously,
and then use `emit()` to emit the result:

    val user: LiveData<User> = liveData {
        val data = database.loadUser() // loadUser is a suspend function.
        emit(data)
    }

For more information on using coroutines with `LiveData`, see
[Use Kotlin coroutines with Architecture components](https://developer.android.com/topic/libraries/architecture/coroutines#livedata).

### Navigation KTX

Each component of the Navigation library has its own KTX version that adapts the
API to be more succinct and Kotlin-idiomatic.

To include these modules, add the following to your app's `build.gradle` file:

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

Use the extension functions and property delegation to access destination
arguments and navigate to destinations, as shown in the following example:

    class MyDestination : Fragment() {

        // Type-safe arguments are accessed from the bundle.
        val args by navArgs<MyDestinationArgs>()

        ...
        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            view.findViewById<Button>(R.id.next)
                .setOnClickListener {
                    // Fragment extension added to retrieve a NavController from
                    // any destination.
                    findNavController().navigate(R.id.action_to_next_destination)
                }
         }
         ...

    }

### Palette KTX

The
[Palette KTX module](https://developer.android.com/reference/kotlin/androidx/palette/graphics/package-summary#extension-functions-summary)
offers idiomatic Kotlin support for working with color palettes.

To use this module, add the following to your app's `build.gradle` file:

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

As an example, when working with a `Palette` instance, you can retrieve the
`selected` swatch for a given `target` by using the get operator (`[ ]`):

    val palette = Palette.from(bitmap).generate()
    val swatch = palette[target]

### Reactive Streams KTX

Reactive Streams KTX module lets you create an observable `LiveData` stream from
a `ReactiveStreams` publisher.

To include this module, add the following to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:2.10.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:2.10.0")
}
```

As an example, assume a database with a small list of users. In your app, you
load the database into memory and then display user data in your UI. To achieve
this, you might use [RxJava](https://github.com/ReactiveX/RxJava).
The [`Room`](https://developer.android.com/topic/libraries/architecture/room) Jetpack component can retrieve
the user list as a `Flowable`. In this scenario, you must also manage the Rx
publisher subscription across the life of your fragment or activity.

With `LiveDataReactiveStreams`, however, you can benefit from RxJava and its
rich set of operators and work-scheduling capabilities while also working with
the simplicity of `LiveData`, as shown in the following example:

    val fun getUsersLiveData() : LiveData<List<User>> {
        val users: Flowable<List<User>> = dao.findUsers()
        return LiveDataReactiveStreams.fromPublisher(users)
    }

### Room KTX

Room extensions add coroutines support for database transactions.

To use this module, add the following to your app's `build.gradle` file:

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

Here are a couple of examples where Room now uses coroutines. The first example
uses a `suspend` function to return a list of `User` objects, while the second
utilizes Kotlin's [`Flow`](https://kotlinlang.org/docs/reference/coroutines/flow.html)
to asynchronously return the `User` list. Note that when using `Flow`, you're
also notified of any changes in the tables you're querying.

    @Query("SELECT * FROM Users")
    suspend fun getUsers(): List<User>

    @Query("SELECT * FROM Users")
    fun getUsers(): Flow<List<User>>

### SQLite KTX

SQLite extensions wrap SQL-related code in transactions, eliminating a lot of
boilerplate code.

To use this module, add the following to your app's `build.gradle` file:

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

Here's an example of using the `transaction` extension to perform a database
transaction:

    db.transaction {
        // insert data
    }

### ViewModel KTX

The ViewModel KTX library provides a `viewModelScope()` function that makes it
easier to launch [coroutines](https://developer.android.com/kotlin/coroutines) from your `ViewModel`. The
[`CoroutineScope`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)
is bound to `Dispatchers.Main` and is automatically cancelled
when the `ViewModel` is cleared. You can use `viewModelScope()` instead of
creating a new scope for each `ViewModel`.

To include this module, add the following to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.10.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.10.0")
}
```

As an example, the following `viewModelScope()` function launches a coroutine
that makes a network request in a background thread. The library handles all of
the setup and corresponding scope clearing:

    class MainViewModel : ViewModel() {
        // Make a network request without blocking the UI thread
        private fun makeNetworkRequest() {
            // launch a coroutine in viewModelScope
            viewModelScope.launch  {
                remoteApi.slowFetch()
                ...
            }
        }

        // No need to override onCleared()
    }

### WorkManager KTX

WorkManager KTX provides first-class support for coroutines.

To include this module, add the following to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.work:work-runtime-ktx:2.11.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.work:work-runtime-ktx:2.11.1")
}
```

Instead of extending [`Worker`](https://developer.android.com/reference/androidx/work/Worker), you can now
extend [`CoroutineWorker`](https://developer.android.com/reference/kotlin/androidx/work/CoroutineWorker),
which has a slightly different API. For example, if you wanted to build a simple
`CoroutineWorker` to perform some network operations, you can do the following:

    class CoroutineDownloadWorker(context: Context, params: WorkerParameters)
            : CoroutineWorker(context, params) {

        override suspend fun doWork(): Result = coroutineScope {
            val jobs = (0 until 100).map {
                async {
                    downloadSynchronously("https://www.google.com")
                }
            }

            // awaitAll will throw an exception if a download fails, which
            // CoroutineWorker will treat as a failure
            jobs.awaitAll()
            Result.success()
        }
    }

For more information on using `CoroutineWorker`, see
[Threading in CoroutineWorker](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/coroutineworker).

WorkManager KTX also adds extension functions to `Operations` and
`ListenableFutures` to suspend the current coroutine.

Here's an example that suspends the
[`Operation`](https://developer.android.com/reference/androidx/work/Operation) that's returned by
[`enqueue()`](https://developer.android.com/reference/androidx/work/WorkContinuation#enqueue()):

    // Inside of a coroutine...

    // Run async operation and suspend until completed.
    WorkManager.getInstance()
            .beginWith(longWorkRequest)
            .enqueue().await()

    // Resume after work completes...

## Other KTX modules

You can also include additional KTX modules that exist outside of AndroidX.

### Firebase KTX

Some of the Firebase SDKs for Android have Kotlin extension libraries that
enable you to write idiomatic Kotlin code when using Firebase in your app. For
more information, see the following topics:

- [Firebase Android SDK](https://firebaseopensource.com/projects/firebase/firebase-android-sdk#kotlin_extensions)
- [Firebase Common Kotlin Extensions](https://github.com/firebase/firebase-android-sdk/blob/master/docs/ktx/common.md)

### Google Maps Platform KTX

There are KTX extensions available for Google Maps Platform Android SDKs which
allow you to take advantage of several Kotlin language features such as extension
functions, named parameters and default arguments, destructuring declarations,
and coroutines. For more information, see the following topics:

- [Maps Android KTX](https://developers.google.com/maps/documentation/android-sdk/ktx)
- [Places Android KTX](https://developers.google.com/places/android-sdk/ktx)

### Play Core KTX

Play Core KTX adds support for Kotlin coroutines for one-shot requests and Flow
for monitoring status updates by adding extension functions to
`SplitInstallManager` and `AppUpdateManager` in the Play Core library.

To include this module, add the following to your app's `build.gradle` file:

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

Here's an example of a status-monitoring `Flow`:

    // Inside of a coroutine...

    // Request in-app update status updates.
    manager.requestUpdateFlow().collect { updateResult ->
        when (updateResult) {
            is AppUpdateResult.Available -> TODO()
            is AppUpdateResult.InProgress -> TODO()
            is AppUpdateResult.Downloaded -> TODO()
            AppUpdateResult.NotAvailable -> TODO()
        }
    }

## More information

To learn more about Android KTX, see the [DevBytes video](https://www.youtube.com/watch?v=r_19VZ0xRO8&feature=youtu.be).

To report an issue or suggest a feature, use the
[Android KTX issue tracker](https://issuetracker.google.com/issues/new?component=396204&template=1082185).