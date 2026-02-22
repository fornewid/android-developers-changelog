---
title: https://developer.android.com/topic/performance/app-optimization/full-mode
url: https://developer.android.com/topic/performance/app-optimization/full-mode
source: md.txt
---

R8 provides two modes, compatibility mode and full mode. Full mode gives you
powerful optimizations that improve your app performance.

This guide is for Android developers who want to use R8's most powerful
optimizations. It explores the key differences between compatibility and full
mode and provides the explicit configurations needed to migrate your project
safely and avoid common runtime crashes.
| **Note:** R8 full mode has been the default since Android Gradle Plugin (AGP) 8.0. For more information, see [AGP and R8 version behavior changes](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#agp-r8-behavior-changes).

### Enable full mode

To enable full mode, remove the following line from your `gradle.properties`
file:  

    android.enableR8.fullMode=false // Remove this line to enable full mode

| **Note:** After you have enabled full mode, we recommend you perform a thorough test of your app. The R8 optimizer uses more powerful optimizations, which are more likely to affect your app's behavior.

### Retain classes associated with attributes

Attributes are metadata stored within compiled class files that aren't part of
the executable code. However, they can be needed for certain types of
reflection. Common examples include `Signature` (which preserves generic type
information after type erasure), `InnerClasses` and `EnclosingMethod`
(for reflecting on class structure) and runtime-visible annotations.

The following code shows what a `Signature` attribute looks like for a field in
bytecode. For a field:  

    List<User> users;

The compiled class file would contain the following bytecode:  

    .field public static final users:Ljava/util/List;
        .annotation system Ldalvik/annotation/Signature;
            value = {
                "Ljava/util/List<",
                "Lcom/example/package/User;",
                ">;"
            }
        .end annotation
    .end field

Libraries that heavily use reflection (like Gson) often rely on these attributes
to dynamically inspect and understand your code's structure. By default in R8's
full mode, attributes are retained only if the associated class, field, or
method is explicitly kept.

The following example demonstrates why attributes are necessary and what keep
rules you need to add when migrating from compatibility to full mode.
| **Note:** For the specific purpose of this example, Gson is used to demonstrate behavior changes in keep rules for attributes. However, this is for illustrative purposes only and does not represent a best practice. Avoid using Gson as it relies heavily on reflection. For more information about reflection, see [Optimization for libraries](https://developer.android.com/topic/performance/app-optimization/library-optimization#use-codegen).

Consider the following example where we deserialize a list of users using the
Gson library.  


    import com.google.gson.Gson
    import com.google.gson.reflect.TypeToken

    data class User(
        @SerializedName("username")
        var username: String? = null,
        @SerializedName("age")
        var age: Int = 0
    )

    fun GsonRemoteJsonListExample() {
        val gson = Gson()

        // 1. The JSON string for a list of users returned from remote
        val jsonOutput = """[{"username":"alice","age":30}, {"username":"bob","age":25}]"""

        // 2. Deserialize the JSON string into a List<User>
        // We must use TypeToken for generic types like List
        val listType = object : TypeToken<List<User>>() {}.type
        val deserializedList: List<User> = gson.fromJson(jsonOutput, listType)

        // Print the list
        println("First user from list: ${deserializedList}")
    }

During compilation, Java's type erasure removes generic type arguments. This
means that at runtime, both `List<String>` and `List<User>` appear as a raw
`List`. Therefore, libraries like Gson, which rely on reflection, cannot
determine the specific object types the `List` was declared to contain when
deserializing a JSON list, which can lead to runtime issues.

To preserve type information, Gson uses `TypeToken`. Wrapping `TypeToken`
retains the necessary deserialization information.

The Kotlin expression `object:TypeToken<List<User>>() {}.type` creates an
anonymous inner class that extends `TypeToken` and captures the generic type
information. In this example, the anonymous class is named
`$GsonRemoteJsonListExample$listType$1`.

The Java programming language saves the generic signature of a superclass as
metadata, known as the `Signature` attribute, within the compiled class file.
`TypeToken` then uses this `Signature` metadata to recover the type at runtime.
This allows Gson to use reflection to read the `Signature` and successfully
discover the full `List<User>` type it needs for deserialization.
| **Note:** For this example to work, you must instruct R8 to preserve the `Signature` attribute using the `-keepattributes Signature` rule. This rule is a prerequisite for both R8 compatibility mode and R8 full mode, as it preserves the generic type information necessary for deserialization.

When R8 is enabled in compatibility mode, it retains the `Signature` attribute
for classes, including anonymous inner classes like
`$GsonRemoteJsonListExample$listType$1`, even if specific keep rules are not
explicitly defined. As a result, R8 compatibility mode does not require any
further explicit keep rules for this example to work as expected.  

    // keep rule for compatibility mode
    -keepattributes Signature

When R8 is enabled in full mode, the `Signature` attribute of the anonymous
inner class `$GsonRemoteJsonListExample$listType$1` is stripped. Without this
type information in the `Signature`, Gson cannot find the correct application
type, which results in an `IllegalStateException`. The keep rules necessary to
prevent this are:  

    // keep rule required for full mode
    -keepattributes Signature
    -keep,allowobfuscation,allowshrinking,allowoptimization class com.google.gson.reflect.TypeToken
    -keep,allowobfuscation,allowshrinking,allowoptimization class * extends com.google.gson.reflect.TypeToken

- `-keepattributes Signature`: This rule instructs R8 to retain the attribute
  that Gson needs to read. In full mode, R8 only retains the `Signature`
  attribute for classes, fields, or methods that are explicitly
  matched by a `keep` rule.

- `-keep,allowobfuscation,allowshrinking,allowoptimization class
  com.google.gson.reflect.TypeToken`: This rule is necessary because
  `TypeToken` wraps the type of the object being deserialized. After type
  erasure, an anonymous inner class is created to retain the generic type
  information. Without explicitly keeping `com.google.gson.reflect.TypeToken`,
  R8 in full mode won't include this class type in the `Signature`
  attribute needed for deserialization.

- `-keep,allowobfuscation,allowshrinking,allowoptimization class * extends
  com.google.gson.reflect.TypeToken`: This rule retains the type information
  of anonymous classes that extend `TypeToken`, such as
  `$GsonRemoteJsonListExample$listType$1` in this example. Without this rule,
  R8 in full mode strips the necessary type information, causing
  deserialization to fail.

Starting with Gson version 2.11.0, the library [bundles necessary keep
rules](https://github.com/google/gson/blob/gson-parent-2.11.0/gson/src/main/resources/META-INF/proguard/gson.pro) required for deserialization in full mode. When you build
your app with R8 enabled, R8 automatically finds and applies these rules from
the library. This provides the protection your app needs without you having to
manually add or maintain these specific rules in your project.

It is important to understand that the rules shared earlier
only solve the problem of discovering the generic type (e.g., `List<User>`).
R8 also renames the fields of classes. If you don't use `@SerializedName`
annotations on your data models, Gson will fail to deserialize JSON because
the field names will no longer match the JSON keys.
| **Note:** For Gson versions 2.11 and higher, the rules for keeping fields annotated with `@SerializedName` are bundled within the Gson [library's consumer ProGuard
| files](https://github.com/google/gson/blob/gson-parent-2.11.0/gson/src/main/resources/META-INF/proguard/gson.pro). Because this example uses `@SerializedName` annotations on the fields, you don't need to specify additional keep rules for the models.

However, if you are using a Gson version older than 2.11, or if your models
don't use the `@SerializedName` annotation, you must add explicit keep rules for
those models.

### Retain the default constructor

In R8 full mode, the no-args/default constructor is not implicitly kept, even
when the class itself is retained. If you are creating an instance of a class
using `class.getDeclaredConstructor().newInstance()` or `class.newInstance()`,
you must explicitly retain the no-args constructor in full mode. In contrast,
compatibility mode always retains the no-args constructor.

Consider an example where an instance of `PrecacheTask` is created using
reflection to dynamically call its `run` method. While this scenario doesn't
require additional rules in compatibility mode, in full mode, the default
constructor of `PrecacheTask` would be removed. Therefore, a specific keep
rule is required.  

    // In library
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

    // In app
    class PreCacheTask : StartupTask {
        override fun run() {
            Log.d("Pre cache task", "Warming up the cache...")
        }
    }

    fun runTaskRunner() {
        // The library is given a direct reference to the app's task class.
        TaskRunner.execute(PreCacheTask::class.java)
    }

    # Full mode keep rule
    # default constructor needs to be specified

    -keep class com.example.fullmoder8.PreCacheTask {
        <init>();
    }

### Access modification is enabled by default

In compatibility mode, R8 does not alter the visibility of methods and fields
within a class. However, in full mode, R8 enhances optimization by changing the
visibility of your methods and fields, for example, from private to public.
This enables more inlining.

This optimization can cause issues if your code uses reflection that
specifically relies on members having particular visibility. R8 won't
recognize this indirect usage, potentially leading to app crashes. To prevent
this, you must add specific `-keep` rules to preserve the members, which will
also preserve their original visibility.
| **Note:** When compiling a library or an app, R8 won't change the visibility of members within classes that you explicitly `-keep`.

For more information, see this [example](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples#reflection-to-access-private-members) to understand why accessing private
members using reflection is not advised and the keep rules to retain those
fields/methods.