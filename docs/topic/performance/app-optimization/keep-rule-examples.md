---
title: https://developer.android.com/topic/performance/app-optimization/keep-rule-examples
url: https://developer.android.com/topic/performance/app-optimization/keep-rule-examples
source: md.txt
---

The following examples are based on common scenarios where you use R8 for
optimization, but need advanced guidance to draft keep rules.

## Reflection

In general, for optimum performance, it's not recommended to use reflection.
However, in certain scenarios, it might be unavoidable. The following examples
provide guidance for keep rules in common scenarios that use reflection.

> [!IMPORTANT]
> **Important:** All reflection, whether in apps or libraries, necessitates corresponding keep rules. Apps place these rules in their own configuration, but libraries must include them in their [consumer keep rules file](https://developer.android.com/topic/performance/app-optimization/library-optimization#library-keep-rule-types).

### Reflection with classes loaded by name

Libraries often load classes dynamically by using the class name as a `String`.
However, R8 cannot detect classes that are loaded in this manner, and might
remove the classes it considers unused.

For example, consider the following scenario where you have a library and an app
that uses the library- the code demonstrates a library loader that
instantiates a `StartupTask` interface implemented by an app.

The library code is as follows:

    // The interface for a task that runs once.
    interface StartupTask {
        fun run()
    }

    // The library object that loads and executes the task.
    object TaskRunner {
        fun execute(className: String) {
            // R8 won't retain classes specified by this string value at runtime
            val taskClass = Class.forName(className)
            val task = taskClass.getDeclaredConstructor().newInstance() as StartupTask
            task.run()
        }
    }

The app that uses the library has the following code:

    // The app's task to pre-cache data.
    // R8 will remove this class because it's only referenced by a string.
    class PreCacheTask : StartupTask {
        override fun run() {
            // This log will never appear if the class is removed by R8.
            Log.d("AppTask", "Warming up the cache...")
        }
    }

    fun onCreate() {
        // The library is told to run the app's task by its name.
        TaskRunner.execute("com.example.app.PreCacheTask")
    }

In this scenario, your library should include a consumer keep rules file with
the following keep rules:

    -keep class * implements com.example.library.StartupTask {
        <init>();
    }

Without this rule, R8 removes `PreCacheTask` from the app because the app
doesn't use the class directly, breaking the integration. The rule finds the
classes that implement your library's `StartupTask` interface and preserves
them, along with their no-argument constructor, allowing the library to
successfully instantiate and execute `PreCacheTask`.

### Reflection with `::class.java`

Libraries can load classes by having the app pass the `Class` object directly,
which is a more robust method than loading classes by name. This creates a
strong reference to the class that R8 can detect. However, while this prevents
R8 from removing the class, you still need to use a keep rule to declare that
the class is instantiated reflectively and to protect the members that are
accessed reflectively, like the constructor.

For example, consider the following scenario in which you have a library and an
app that uses the library- the library loader instantiates a `StartupTask`
interface by passing the class reference directly.

The library code is as follows:

    // The interface for a task that runs once.
    interface StartupTask {
        fun run()
    }
    // The library object that loads and executes the task.
    object TaskRunner {
        fun execute(taskClass: Class<out StartupTask>) {
            // The class isn't removed, but its constructor might be.
            val task = taskClass.getDeclaredConstructor().newInstance()
            task.run()
        }
    }

The app that uses the library has the following code:

    // The app's task is to pre-cache data.
    class PreCacheTask : StartupTask {
        override fun run() {
            Log.d("AppTask", "Warming up the cache...")
        }
    }

    fun onCreate() {
        // The library is given a direct reference to the app's task class.
        TaskRunner.execute(PreCacheTask::class.java)
    }

In this scenario, your library should include a consumer keep rules file with
the following keep rules:

    # Allow any implementation of StartupTask to be removed if unused.
    -keep,allowobfuscation,allowshrinking class * implements com.example.library.StartupTask
    # Keep the default constructor, which is called via reflection.
    -keepclassmembers class * implements com.example.library.StartupTask {
        <init>();
    }

These rules are designed to work perfectly with this type of reflection,
allowing for maximum optimization while making sure that the code works
correctly. The rules let R8 obfuscate the class name and shrink, or remove, the
implementation of the `StartupTask` class if the app never uses it. However,
for any implementation, such as the `PrecacheTask` that is used in the example,
they preserve the default constructor (`<init>()`) that your library needs to
call.

- **`-keep,allowobfuscation,allowshrinking class * implements
  com.example.library.StartupTask`** : This rule targets any class that implements your `StartupTask` interface.
  - **`-keep class * implements com.example.library.StartupTask`** : This preserves any class (`*`) that implements your interface.
  - **`,allowobfuscation`** : This instructs R8 that despite keeping the class, it can rename, or obfuscate, it. This is safe because your library doesn't rely on the class's name; it gets the `Class` object directly.
  - **`,allowshrinking`** : This modifier instructs R8 that it can remove the class if it's unused. This helps R8 to safely delete an implementation of `StartupTask` that is never passed to `TaskRunner.execute()`. In short, this rule implies the following: If an app uses a class that implements `StartupTask`, R8 keeps the class. R8 can rename the class to reduce its size and can delete it if the app doesn't use it.
- **`-keepclassmembers class * implements com.example.library.StartupTask {
  <init>(); }`** : This rule targets specific members of the classes that were identified in the first rule---in this case, the constructor.
  - **`-keepclassmembers class * implements
    com.example.library.StartupTask`** : This preserves specific members (methods, fields) of the class that implements `StartupTask` interface, but only if the implemented class itself is being kept.
  - **`{ <init>(); }`** : This is the member selector. `<init>` is the special internal name for a constructor in Java bytecode. This part specifically targets the default, no-argument constructor.
  - This rule is critical because your code calls `getDeclaredConstructor().newInstance()` without any arguments, which reflectively invokes the default constructor. Without this rule, R8 sees that no code directly calls `new PreCacheTask()`, assumes that the constructor is unused, and removes it. This causes your app to crash at runtime with an`InstantiationException`.

> [!NOTE]
> **Note:** Keeping the `run` method is not necessary because the library calls the `run` method directly.

### Reflection based on method annotation

Libraries often define annotations that developers use to tag methods or fields.
The library then uses reflection to find these annotated members at runtime. For
example, the `@OnLifecycleEvent` annotation is used to find the required methods
at runtime.

For example, consider the following scenario in which you have a library and an
app that uses the library- the example demonstrates an event bus that finds and
invokes methods annotated with `@OnEvent`.

The library code is as follows:

    @Retention(AnnotationRetention.RUNTIME)
    @Target(AnnotationTarget.FUNCTION)
    annotation class OnEvent

    class EventBus {
        fun dispatch(listener: Any) {
            // Find all methods annotated with @OnEvent and invoke them
            listener::class.java.declaredMethods.forEach { method ->
                if (method.isAnnotationPresent(OnEvent::class.java)) {
                    try {
                        method.invoke(listener)
                    } catch (e: Exception) { /* ... */ }
                }
            }
        }
    }

The app that uses the library has the following code:

    class MyEventListener {
        @OnEvent
        fun onSomethingHappened() {
            // This method will be removed by R8 without a keep rule
            Log.d(TAG, "Event received!")
        }
    }

    fun onCreate() {
        // Instantiate the listener and the event bus
        val listener = MyEventListener()
        val eventBus = EventBus()

        // Dispatch the listener to the event bus
        eventBus.dispatch(listener)
    }

The library should include a consumer keep rules file that automatically
preserves any methods using its annotations:

    -keepattributes RuntimeVisibleAnnotations
    -keep @interface com.example.library.OnEvent;
    -keepclassmembers class * {
        @com.example.library.OnEvent <methods>;
    }

- **`-keepattributes RuntimeVisibleAnnotations`** : This rule preserves [annotations](https://developer.android.com/topic/performance/app-optimization/global-options#commonly-required-attributes) that are meant to be read at runtime.
- **`-keep @interface com.example.library.OnEvent`** : This rule preserves the `OnEvent` annotation class itself.
- **`-keepclassmembers class * {@com.example.library.OnEvent <methods>;}`** : This rule preserves a class and specific members only if the class is being used and the class contains those members.
  - **`-keepclassmembers`**: This rule preserves a class and specific members only if the class is being used and the class contains those members.
  - **`class *`**: The rule applies to any class.
  - **`@com.example.library.OnEvent <methods>;`** : This preserves any class that has one or more methods (`<methods>`) annotated with `@com.example.library.OnEvent`, and to also preserve the annotated methods themselves.

### Reflection based on class annotations

Libraries can use reflection to scan for classes that have a specific
annotation. In this case, the task runner class finds all the classes
annotated with `ReflectiveExecutor` using reflection and executes the `execute`
method.

For example, consider the following scenario where you have a library and an app
that uses the library.

The library has the following code:

    @Retention(AnnotationRetention.RUNTIME)
    @Target(AnnotationTarget.CLASS)
    annotation class ReflectiveExecutor

    class TaskRunner {
        fun process(task: Any) {
            val taskClass = task::class.java
            if (taskClass.isAnnotationPresent(ReflectiveExecutor::class.java)) {
                val methodToCall = taskClass.getMethod("execute")
                methodToCall.invoke(task)
            }
        }
    }

The app that uses the library has the following code:

    // In consumer app

    @ReflectiveExecutor
    class ImportantBackgroundTask {
        fun execute() {
            // This class will be removed by R8 without a keep rule
            Log.e("ImportantBackgroundTask", "Executing the important background task...")
        }
    }

    // Usage of ImportantBackgroundTask

    fun onCreate(){
        val task = ImportantBackgroundTask()
        val runner = TaskRunner()
        runner.process(task)
    }

Because the library reflectively uses reflection to get specific classes, the
library should include a consumer keep rules file with the following keep rules:

    # Retain annotation metadata for runtime reflection.
    -keepattributes RuntimeVisibleAnnotations

    # Keep the annotation interface itself.
    -keep @interface com.example.library.ReflectiveExecutor

    # Keep the execute method in the classes which are being used
    -keepclassmembers @com.example.library.ReflectiveExecutor class * {
       public void execute();
    }

This configuration is highly efficient because it tells R8 exactly what to
preserve.

### Reflection to support optional dependencies

A common use case for reflection is to create a soft dependency between a core
library and an optional add-on library. The core library can check if the add-on
is included in the app and, if it is, can enable extra features. This lets you
ship add-on modules without forcing the core library to have a direct dependency
on them.

The core library uses reflection (`Class.forName`) to look for a specific class
by its name. If the class is found, the feature is enabled. If not, it fails
gracefully.

For example, consider the following code where a core `AnalyticsManager` checks
for an optional `VideoEventTracker` class to enable video analytics.

The core library has the following code:

    object AnalyticsManager {
        private const val VIDEO_TRACKER_CLASS = "com.example.analytics.video.VideoEventTracker"

        fun initialize() {
            try {
                // Attempt to load the optional module's class using reflection
                Class.forName(VIDEO_TRACKER_CLASS).getDeclaredConstructor().newInstance()
                Log.d(TAG, "Video tracking enabled.")
            } catch (e: ClassNotFoundException) {
                Log.d(TAG,"Video tracking module not found. Skipping.")
            } catch (e: Exception) {
                Log.e(TAG, e.printStackTrace())
            }
        }
    }

The optional video library has the following code:

    package com.example.analytics.video

    class VideoEventTracker {
        // This constructor must be kept for the reflection call to succeed.
        init { /* ... */ }
    }

The developer of the optional library is responsible for providing the necessary
consumer keep rule. This keep rule makes sure that any app using the optional
library preserves the code the core library needs to find.

    # In the video library's consumer keep rules file
    -keep class com.example.analytics.video.VideoEventTracker {
        <init>();
    }

Without this rule, R8 likely removes `VideoEventTracker` from the optional
library since nothing in that module directly uses it. The keep rule preserves
the class and its constructor, letting the core library successfully
instantiate it.

> [!WARNING]
> **Warning:** Not including this rule doesn't crash the app; however, the optional feature won't be available. This kind of bug is difficult to detect during testing.

### Reflection to access private members

Using reflection to access private or protected code that isn't part of a
library's public API can introduce significant problems. Such code is subject to
change without notice, which can lead to unexpected behavior or crashes in your
application.

When you rely on reflection for non-public APIs, you might encounter the
following issues:

- **Blocked updates:** Changes in the private or protected code can prevent you from updating to higher library versions.
- **Missed benefits:** You might miss out on new functionality, important crash fixes, or essential security updates.

### R8 optimizations and reflection

If you must reflect into a library's private or protected code, pay close
attention to R8's optimizations. If there are no direct references to these
members, R8 might assume they are unused and subsequently remove or rename them.
This can lead to runtime crashes, often with misleading error messages such as
`NoSuchMethodException` or `NoSuchFieldException`.

> [!IMPORTANT]
> **Key Point:** You should maintain R8 rules for all members accessed by reflection. This is crucial even if R8 doesn't remove them, as future code changes could lead R8 to attempt removal later.

For example, consider the following scenario that demonstrates how you might
access a private field from a library class.

A library that you don't own has the following code:

    class LibraryClass {
        private val secretMessage = "R8 will remove me"
    }

Your app has the following code:

    fun accessSecretMessage(instance: LibraryClass) {
        // Use Java reflection from Kotlin to access the private field
        val secretField = instance::class.java.getDeclaredField("secretMessage")
        secretField.isAccessible = true
        // This will crash at runtime with R8 enabled
        val message = secretField.get(instance) as String
    }

Add a `-keep` rule in your app to prevent R8 from removing the private field:

    -keepclassmembers class com.example.LibraryClass {
        private java.lang.String secretMessage;
    }

- **`-keepclassmembers`**: This preserves specific members of a class only if the class itself is retained.
- **`class com.example.LibraryClass`**: This targets the exact class containing the field.
- **`private java.lang.String secretMessage;`**: This identifies the specific private field by its name and type.

> [!NOTE]
> **Note:** Don't use a broad rule like `-keep class com.example.LibraryClass { *;
> }`. This stops R8 from performing any optimization on the class, including removing other unused members, making your app larger and less efficient. Always be as specific as possible.

## Java Native Interface (JNI)

R8's optimizations can have issues when working with upcalls from native (C/C++
code) to Java or Kotlin. While the reverse is also true---downcalls from Java or
Kotlin to native code can have issues---the default file
`proguard-android-optimize.txt` includes the following rule to keep the
downcalls working. This rule guards against native methods being trimmed.

    -keepclasseswithmembernames,includedescriptorclasses class * {
      native <methods>;
    }

### Interaction with native code through the Java Native Interface (JNI)

When your app uses JNI to make upcalls from native (C/C++) code to Java or
Kotlin, R8 can't see which methods are called from your native code. If there
are no direct references to these methods in your app, R8 incorrectly assumes
that these methods are unused and removes them, causing your app to crash.

The following example shows a Kotlin class with a method intended to be called
from a native library. The native library instantiates an application type and
passes data from native code to the Kotlin code.

    package com.example.models

    // This class is used in the JNI bridge method signature
    data class NativeData(val id: Int, val payload: String)

    package com.example.app
    // In package com.example.app
    class JniBridge {
        /**
         *   This method is called from the native side.
         *   R8 will remove it if it's not kept.
         */
        fun onNativeEvent(data: NativeData) {
            Log.d(TAG, "Received event from native code: $data")
        }
        // Use 'external' to declare a native method
        external fun startNativeProcess()

        companion object {
            init {
                // Load the native library
                System.loadLibrary("my-native-lib")
            }
        }
    }

In this case, you must inform R8 to prevent the application type from being
optimized. Additionally, if methods called from native code use your own classes
in their signatures as parameters or return types, you must also verify that
those classes are not renamed.

Add the following keep rules to your app:

    -keepclassmembers,includedescriptorclasses class com.example.JniBridge {
        public void onNativeEvent(com.example.model.NativeData);
    }

    -keep class NativeData{
            <init>(java.lang.Integer, java.lang.String);
    }

> [!NOTE]
> **Note:** In such cases, put the Kotlin or Java code used by the JNI call into an isolated package, and then include the package in a keep rule. For more details, [see Adopt optimizations incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally).

These keep rules prevent R8 from removing or renaming the `onNativeEvent` method
and---critically---its parameter type.

- **`-keepclassmembers,includedescriptorclasses class com.example.JniBridge{
  public void onNativeEvent(com.example.model.NativeData);}`** : This preserves specific members of a class only if the class is instantiated in Kotlin or Java code first---it tells R8 that the app is using the class and that it should preserve specific members of the class.
  - **`-keepclassmembers`**: This preserves specific members of a class only if the class is instantiated in Kotlin or Java code first---it tells R8 that the app is using the class and that it should preserve specific members of the class.
  - **`class com.example.JniBridge`**: This targets the exact class containing the field.
  - **`includedescriptorclasses`** : This modifier also preserves any classes found in the method's signature, or descriptor. In this case, it prevents R8 from renaming or removing the `com.example.models.NativeData` class, which is used as a parameter. If `NativeData` were renamed (for example, to `a.a`), the method signature would no longer match what the native code expects, causing a crash.
  - **`public void onNativeEvent(com.example.models.NativeData);`**: This specifies the exact Java signature of the method to preserve.
- **`-keep class NativeData{<init>(java.lang.Integer, java.lang.String);}`** : While `includedescriptorclasses` makes sure that the `NativeData` class itself is preserved, any members (fields or methods) within `NativeData` that are accessed directly from your native JNI code need their own keep rules.
  - **`-keep class NativeData`** : This targets the class named `NativeData` and the block specifies which members inside the `NativeData` class to keep.
  - **`<init>(java.lang.Integer, java.lang.String)`** : This is the constructor's signature. It uniquely identifies the constructor that takes two parameters: the first is an `Integer` and the second is a `String`.

> [!WARNING]
> **Warning:** If you forget this rule, your app crashes with an `UnsatisfiedLinkError` or `NoSuchMethodError` when the native code tries to call the missing method. These crashes can be hard to debug because the error originates outside the Dalvik/ART virtual machine.

## Indirect platform calls

### Transfer data with an implementation of `Parcelable`

The Android framework uses reflection to create instances of your `Parcelable`
objects. In modern Kotlin development, you should use the `kotlin-parcelize`
plugin, which automatically generates the necessary `Parcelable` implementation,
including the `CREATOR` field and methods that the framework needs.

For example, consider the following example where the `kotlin-parcelize` plugin
is used to create a `Parcelable` class:

    import android.os.Parcelable
    import kotlinx.parcelize.Parcelize

    // Add the @Parcelize annotation to your data class
    @Parcelize
    data class UserData(
        val name: String,
        val age: Int
    ) : Parcelable

In this scenario, there isn't a recommended keep rule. The `kotlin-parcelize`
Gradle plugin automatically generates the required keep rules for the classes
you annotate with `@Parcelize`. It handles the complexity for you, making sure
that the generated `CREATOR` and constructors are preserved for the Android
framework's reflection calls.

If you write a `Parcelable` class manually in Kotlin without using `@Parcelize`,
you are responsible for keeping the `CREATOR` field and the constructor that
accepts a `Parcel`. Forgetting to do so causes your app to crash when the
system tries to deserialize your object. Using `@Parcelize` is the standard,
safer practice.

When using the `kotlin-parcelize` plugin, be aware of the following:

- The plugin automatically creates `CREATOR` fields during compilation.
- The `proguard-android-optimize.txt` file contains the necessary `keep` rules to retain these fields for proper functionality.
- App developers must verify that all required `keep` rules are present, especially for any custom implementations or third-party dependencies.

## Popular libraries

Libraries that use reflection or bytecode transformations access code
dynamically at runtime. If R8 removes or renames classes, fields, or methods
that are accessed in this way, your app can crash.

However, popular third-party libraries (such as Gson, Retrofit, and Kotlinx
Serialization) automatically bundle their own R8 consumer keep rules. When
using recent versions of these libraries, you don't need to add manual keep
rules to your project.

> [!NOTE]
> **Note:** Don't copy the rules shown in the following sections into your project. These libraries already contain these keep rules. The snippets are listed here solely to serve as syntax examples.

### Gson

Gson is a JSON serialization and deserialization library that relies heavily on
reflection. When you use [full mode](https://developer.android.com/topic/performance/app-optimization/full-mode) to optimize your app, it strips generic
type signatures, default constructors, and non-annotated fields unless
explicitly instructed otherwise.

To ensure Gson functions correctly, add specific rules to keep non-transient
fields in your data model classes and preserve the `TypeToken` hierarchy:

    # Preserve generic type information required for deserialization
    -keepattributes Signature

    # Keep all non-transient fields in your data model classes for reflection
    -keepclassmembers class com.example.models.** {
        !transient <fields>;
    }

    # Keep TypeToken itself and any anonymous classes extending it
    -keep,allowobfuscation,allowshrinking,allowoptimization class com.google.gson.reflect.TypeToken { *; }
    -keep,allowobfuscation,allowshrinking,allowoptimization class * extends com.google.gson.reflect.TypeToken

Fields marked with the `transient` modifier are ignored by Gson during
serialization and deserialization, which is why the keep rule specifically
targets non-transient fields (`!transient`).

> [!NOTE]
> **Note:** Starting with Gson 2.11.0, the library [bundles the necessary keep
> rules](https://github.com/google/gson/blob/main/gson/src/main/resources/META-INF/proguard/gson.pro) for `TypeToken` and `@SerializedName` fields. If your models use `@SerializedName` and you use Gson 2.11.0 or higher, you don't need to add these rules manually.

### Retrofit

Retrofit is a networking library that inspects service interface methods
annotated with HTTP annotations (such as `@GET` or `@POST`) using reflection to
construct network requests and convert responses.

Retrofit dynamically generates implementations of your API interfaces at runtime
using `Proxy.newProxyInstance()`. Because R8 doesn't see any class statically
implementing these interfaces, it might strip the methods or their generic
return types.

#### Bundled keep rules

Retrofit relies on runtime reflection to inspect generic parameters, method
annotations, and parameter annotations. Without proper configuration, R8 full
mode can thoroughly strip generic signatures from return types, Kotlin
continuations, and response classes, or even replace interface values with null
since Retrofit interfaces are dynamically instantiated with a proxy.

Starting with Retrofit 2.10.0, the library automatically bundles the official
keep rules required to preserve annotation defaults, service method parameters,
and necessary class metadata. For more information, see [Rules used by
Retrofit](https://github.com/square/retrofit/blob/trunk/retrofit/src/main/resources/META-INF/proguard/retrofit2.pro).

#### Preserve generic return types

Retrofit inspects the generic signature of the return type (for example,
`Observable<Data>`) to correctly deserialize the network response. If R8 strips
the generic signature, Retrofit will replace the instantiated object with
`null`.

To prevent R8 full mode from stripping the generic signature of your return
types, use the following conditional rule:

    # Preserve generic type information for Call/Observable return types
    -keepattributes Signature

    # If an interface has a Retrofit HTTP annotation, keep its return type (class <3>)
    -if interface * {
        @retrofit2.http.* public *** *(...);
    }
    -keep,allowoptimization,allowshrinking,allowobfuscation class <3>

The actual data model class being returned (for example, `Data` in
`Observable<Data>`) must also be kept, as it will be constructed reflectively by
the converter (like Gson).

> [!NOTE]
> **Note:** Retrofit starting from [version 2.10.0 bundles rules](https://github.com/square/retrofit/commit/51e81a88ca85f6ac0252de240f7d45af91e2a563) that detect its own HTTP annotations (`@GET`, `@POST`) ([View Retrofit's embedded ProGuard
> rules](https://github.com/square/retrofit/blob/trunk/retrofit/src/main/resources/META-INF/proguard/retrofit2.pro)). It will automatically keep the method signatures it needs to work.

### Coroutines

When you use Kotlin coroutines, the Kotlin compiler transforms `suspend`
functions by appending a `Continuation` parameter to the compiled method
signature.

When libraries like Retrofit reflectively read the generic signature of a
`suspend` function, they rely on that `Continuation` parameter. When using full
mode, the `Signature` attribute is only kept for classes that are explicitly
kept. Since `Continuation` is a synthetic parameter, R8 strips its signature by
default, breaking the reflection.

To prevent signature stripping and ensure runtime compatibility in full mode,
include the following rule:

    # Keep the signature attribute globally
    -keepattributes Signature

    # Explicitly keep the Continuation class so its signature is not stripped
    -keep class kotlin.coroutines.Continuation