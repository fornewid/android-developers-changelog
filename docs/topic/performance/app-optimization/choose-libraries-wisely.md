---
title: https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely
url: https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely
source: md.txt
---

To enable app optimization, you must use libraries that are compatible with
Android optimization. If a library isn't configured for Android optimization---for
example, if it uses
[reflection](https://en.wikipedia.org/wiki/Reflective_programming)
without bundling associated keep rules---it might not be a good fit for an
Android app. This page explains why some libraries are better suited for app
optimization and provides general tips to help you choose.

## Prefer codegen over reflection

Generally, you should choose libraries that use
[code generation (*codegen*)](https://en.wikipedia.org/wiki/Code_generation_(compiler))
instead of reflection. With codegen, the optimizer can more easily determine
what code is actually used at runtime and what code can be removed. It can be
difficult to tell whether a library uses codegen or reflection, but there are
some signs---see the [tips](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely#tips) for help.

For more information about codegen versus reflection, see
[Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization#use-codegen).

## General tips when choosing libraries

Use these tips to help ensure that your libraries are compatible with app
optimization.

### Check for optimization issues

When considering a new library, look through the library's issue tracker and
online discussions to check if there are issues related to minification or
configuring app optimization. If there are, you should try to look for
alternatives to that library. Keep in mind the following:

- The [AndroidX libraries](https://developer.android.com/jetpack/androidx) and libraries such as [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) work well with app optimization because they use codegen instead of reflection. When they do use reflection, they provide minimal keep rules to keep only the code that is needed.
- Serialization libraries frequently use reflection to avoid boilerplate code when instantiating or serializing objects. Instead of reflection-based approaches (such as Gson for JSON), look for libraries that use codegen to avoid these problems, for example by using [Kotlin Serialization](https://github.com/Kotlin/kotlinx.serialization) instead.
- Libraries that include package-wide keep rules should be avoided if possible. Package-wide keep rules can help resolve errors, but broad keep rules should eventually be refined to keep only the code that is needed. For more information, see [Adopt optimizations incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally).
- Libraries shouldn't require you to copy and paste keep rules from documentation into a file in your project, especially not package-wide keep rules. These rules become a maintenance burden on the app developer in the long term, and are difficult to optimize and change over time.

### Enable optimization after adding a new library

When you add a new library, enable optimization afterwards and check if there
are errors. If there are errors, look for alternatives to that library or write
keep rules. If a library isn't compatible with optimization, file a bug with
that library.

### Rules are additive

Be aware that keep rules are additive. This means that certain rules that a
library dependency includes cannot be removed and might impact the compilation
of other parts of your app. For example, if a library includes a rule to disable
code optimizations, that rule disables optimizations for your entire project.

### Check for use of reflection (advanced)

You might be able to tell if a library uses reflection from inspecting its code.
If the library uses reflection, check that it provides associated keep rules. A
library is probably using reflection if it does the following:

- Uses classes or methods from the `kotlin.reflect` or `java.lang.reflect` packages
- Uses the functions `Class.forName` or `classLoader.getClass`
- Reads annotations at runtime, for example if it stores an annotation value using `val value = myClass.getAnnotation()` or `val value =
  myMethod.getAnnotation()` and then does something with `value`
- Calls methods using the method name as a string, for example:

      // Calls the private `processData` API with reflection
      myObject.javaClass.getMethod("processData", DataType::class.java)
      ?.invoke(myObject, data)

### Filter out bad keep rules (advanced)

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

## Case study: Why Gson breaks with optimizations

Gson is a serialization library that often causes issues with app optimization
because it heavily uses reflection. The following code snippet shows how Gson is
typically used, which can easily cause crashes at runtime. Notice that when you
use Gson to get a list of User objects, you don't call the constructor or pass a
factory to the `fromJson()` function. Constructing or consuming app-defined
classes without either of the following is a sign that a library might be using
open-ended reflection:

- App class implementing a library, or standard interface or class
- Code generation plugin like [KSP](https://github.com/google/ksp)

    class User(val name: String)
    class UserList(val users: List<User>)

    // This code runs in debug mode, but crashes when optimizations are enabled
    Gson().fromJson("""[{"name":"myname"}]""", User::class.java).toString()

When R8 analyzes this code and doesn't see the `UserList` or `User` instantiated
anywhere, it can rename fields, or remove constructors which don't seem to be
used, causing your app to crash. If you are using any other libraries in similar
ways, you should check that they won't interfere with app optimization, and if
they do, avoid them.

Note that [Room](https://developer.android.com/training/data-storage/room) and
[Hilt](https://developer.android.com/training/dependency-injection/hilt-android) both construct app defined
types, but use codegen to avoid the need for reflection.