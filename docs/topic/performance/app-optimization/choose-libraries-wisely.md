---
title: https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely
url: https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely
source: md.txt
---

To enable app optimization, you must use libraries that are compatible with
Android optimization. If a library isn't configured for Android optimization---for
example, if it uses [reflection](https://en.wikipedia.org/wiki/Reflective_programming)
without bundling associated keep rules---it might not be a good fit for an Android
app. This page explains why some libraries are better suited for app
optimization and provides general tips to help you choose.

> [!NOTE]
> **Note:** For a complete list of requirements that libraries built for Android must adhere to, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization.md.txt).

## General tips when choosing libraries

Use these tips to help ensure that your libraries are compatible with app
optimization.

### Prefer codegen over reflection

Choose libraries that use [code generation (*codegen*)](https://en.wikipedia.org/wiki/Code_generation_(compiler))
instead of reflection. With codegen, the optimizer can determine what code is
actually used at runtime and what code can be removed. It can be difficult to
tell whether a library uses codegen or reflection, but there are
some signs---see the [tips](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely.md.txt#tips) for help.

For more information about codegen versus reflection, see [Optimization for
library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization#use-codegen).

#### Check for use of reflection (advanced)

You can tell if a library uses reflection by inspecting its code.
If the library uses reflection, check that it provides associated keep rules. A
library likely uses reflection if it does the following:

- Uses classes or methods from the `kotlin.reflect` or `java.lang.reflect` packages.
- Uses the functions `Class.forName` or `classLoader.getClass`.
- Reads annotations at runtime, for example if it stores an annotation value using `val value = myClass.getAnnotation()` or `val value =
  myMethod.getAnnotation()` and then does something with `value`.
- Calls methods using the method name as a string, as in the following
  example:

  ```kotlin
  // Calls the private `processData` API with reflection
  myObject.javaClass.getMethod("processData", DataType::class.java)
  ?.invoke(myObject, data)
  ```

### Check for optimization issues

When considering a new library, look through the library's issue tracker and
online discussions to check if there are issues related to minification or
configuring app optimization. If there are, you should try to look for
alternatives to that library. Keep in mind the following:

- The [AndroidX libraries](https://developer.android.com/jetpack/androidx.md.txt) and libraries such as [Hilt](https://developer.android.com/training/dependency-injection/hilt-android.md.txt) work well with app optimization because they mostly use codegen instead of reflection. When they do use reflection, they provide minimal keep rules to keep only the code that is needed.
- Serialization libraries frequently use reflection to avoid boilerplate code when instantiating or serializing objects. Instead of reflection-based approaches (such as Gson for JSON), look for libraries that use codegen to avoid these problems, for example by using [Kotlin Serialization](https://github.com/Kotlin/kotlinx.serialization) or [Moshi with codegen](https://github.com/square/moshi#codegen).
- If possible, avoid libraries that include package-wide keep rules. Package-wide keep rules can help resolve errors, but broad keep rules should eventually be refined to keep only the code that is needed. For more information, see [Adopt optimizations incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally.md.txt).
- Before publishing an app that uses a third-party library, use the [R8
  Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) to audit its provided keep rules. By reviewing the report, you can verify if the library's keep rules are overly broad, preventing R8 from performing critical optimizations on your codebase. This check ensures that the libraries you select align with your app's performance goals and don't introduce unnecessary configuration bloat.
- Libraries shouldn't require you to copy and paste keep rules from documentation into a file in your project, especially not package-wide keep rules. These rules become a maintenance burden on the app developer in the long term, and are difficult to optimize and change over time.

## Enable optimization after adding a new library

When you add a new library, enable optimization afterwards and check if there
are errors. If there are errors, look for alternatives to that library or write
keep rules. If a library isn't compatible with optimization, file a bug with
that library.

## Filter out bad keep rules (advanced)

Keep rules are additive. This means that certain rules that a library dependency
includes cannot be removed and might affect the compilation of other parts of
your app. For example, if a library includes a rule to disable code
optimizations, that rule disables optimizations for your entire project.

You should avoid libraries with keep rules that retain code that should really
be removed. But if you must use them, you can filter the rules out as shown in
the following code:

    // If you're using AGP 8.4 and higher
    buildTypes {
        release {
            optimization.keepRules {
              it.ignoreFrom("com.somelibrary:somelibrary")
            }
        }
    }

    // If you're using AGP 7.3-8.3
    buildTypes {
        release {
            optimization.keepRules {
              it.ignoreExternalDependencies("com.somelibrary:somelibrary")
            }
        }
    }

> [!CAUTION]
> **Caution:** Instead of filtering a library's consumer rules in production releases, contact the library developer and ask them to narrow the rules. Manually overriding a library's keep rules introduces significant maintenance overhead. If a future library update introduces new reflection or JNI calls and your custom rules don't account for them, your app can crash in production.

### Recommended workflow for broad library rules

If the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer.md.txt) reveals that a library bundles overly
broad keep rules, filter those rules only in local builds, not in production
builds. To test how much the rules affect your app, follow these steps:

1. **Update the library:** Make sure you're using the latest version of the library that the R8 Configuration Analyzer flagged, because newer versions might ship narrower consumer keep rules. To find the latest version, check the library's documentation or its Maven repository. Android Studio also flags newer versions of many dependencies. After updating, run the R8 Configuration Analyzer again to check whether the broad keep rules remain.
2. **Check the potential improvement locally:** Copy the library's bundled consumer rules into your local keep rules file, filter out the bundled rules as shown in [Filter out bad keep rules](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely.md.txt#filter-rules), and narrow down the copied rules. Run the R8 Configuration Analyzer before and after narrowing the rules to compare your app's shrinking, optimization, and obfuscation scores.
3. **Report the findings:** File a bug report with the library maintainer containing the empirical data from your R8 Configuration Analyzer report (for example, demonstrating the specific number of unreferenced classes or methods preserved by their wildcard rule).

> [!NOTE]
> **Note:** If you build games with Unity or Unreal Engine, your game engine manages R8 configuration and plugin keep rules in its build pipeline. For more information, see [Shrink and optimize Unity code with R8](https://developer.android.com/games/engines/unity/unity-r8.md.txt) and [Shrink and
> optimize Unreal Engine code with R8](https://developer.android.com/games/engines/unreal/unreal-r8).

## Case study: Why Gson breaks with optimizations

Gson is a serialization library that often causes issues with app optimization
because it heavily uses reflection. The following code snippet shows how Gson is
typically used, which can cause crashes at runtime. Notice that when you
use Gson to get a list of User objects, you don't call the constructor or pass a
factory to the `fromJson()` function. Constructing or consuming app-defined
classes without either of the following is a sign that a library might be using
open-ended reflection:

- App class implementing a library, or standard interface or class
- Code generation plugin like [KSP](https://github.com/google/ksp)

```kotlin
class User(val name: String)
class UserList(val users: List<User>)

// This code runs in debug mode, but crashes when optimizations are enabled
Gson().fromJson("""[{"name":"myname"}]""", User::class.java).toString()
```

To understand how R8 works on Gson, see the [Gson consumer rules](https://github.com/google/gson/blob/main/gson/src/main/resources/META-INF/proguard/gson.pro). When R8
analyzes this code and doesn't see the `UserList` or `User` instantiated
anywhere, it can rename fields, or remove constructors which don't seem to be
used, causing your app to crash. If you are using any other libraries in similar
ways, you should check that they won't interfere with app optimization, and if
they do, avoid them.

### Use `@SerializedName` with later Gson versions

To define your data models in a manner compatible with Gson's consumer rules,
annotate your fields with `@SerializedName`, as shown in the following snippet:

```kotlin
import com.google.gson.annotations.SerializedName

class User(@SerializedName("name") val name: String)
class UserList(@SerializedName("users") val users: List<User>)
```

By using the `@SerializedName` annotation, you allow R8 to match your model
classes against the [keep rules](https://github.com/google/gson/blob/main/gson/src/main/resources/META-INF/proguard/gson.pro) bundled in Gson version 2.11.0 and higher.
R8 automatically preserves the annotated fields and necessary constructors,
letting you rely on the library's bundled rules without having to maintain
manual ProGuard configurations in your project.

Note that [Room](https://developer.android.com/training/data-storage/room.md.txt), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android.md.txt), and [Moshi with codegen](https://github.com/square/moshi#codegen) construct
app-defined types, but use codegen to avoid the need for reflection.