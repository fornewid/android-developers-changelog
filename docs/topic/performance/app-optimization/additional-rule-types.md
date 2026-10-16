---
title: https://developer.android.com/topic/performance/app-optimization/additional-rule-types
url: https://developer.android.com/topic/performance/app-optimization/additional-rule-types
source: md.txt
---

R8 lets you add rules that affect the optimization of your app, apart from keep
rules. Add these rules in the same `proguard-rules.pro` file where you maintain
your keep rules.

The rules fall into the following categories:

- Assumptions
  - `-assumevalues`
  - `-assumenosideeffects`
- Other optimizations
  - `-convertchecknotnull`
  - `-maximumremovedandroidloglevel`

> [!NOTE]
> **Note:** For more rule types, see [Add keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules), [Troubleshooting rules](https://developer.android.com/topic/performance/app-optimization/troubleshooting-rules), and [Global options](https://developer.android.com/topic/performance/app-optimization/global-options).

## Assumptions

These rules tell R8 that it can make specific assumptions about specific code
behavior at runtime.

> [!WARNING]
> **Warning:** Assumptions instruct R8 to force further optimizations on your code, beyond what the code is analyzed to do. Use assumptions with caution, because forcing optimizations can break your app. Make sure to [test the optimization](https://developer.android.com/topic/performance/app-optimization/test-the-optimization) thoroughly when using these rules.

### `-assumevalues`

The `-assumevalues` rule tells R8 that the value of a field, or a method's
return value, is always a specific constant or falls within a defined range at
runtime. `-assumevalues` is intended for things like flag values which at
build time are known to have specific values at runtime.

R8's standard static analysis might not be able to determine the runtime values
of members. With `-assumevalues`, you tell R8 to assume the specified
value or range when optimizing the code. This lets R8 perform aggressive
optimizations.

The syntax for `-assumevalues` is similar to the syntax for keeping a
[`member_specification`](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#member-spec), but additionally includes a `return clause` as
follows:

    <member_specification> return <value> | <range>

The `<value>` and `<range>` arguments support the following values and types:

- Special values: `true, false, null, @NonNull`
- Primitive values: `int`
- String constants
- Static field references (including enum fields)

> [!NOTE]
> **Note:** Using `@NonNull` requires R8 version 9.0.24 or higher (available in AGP 9.0.0), and using String constants requires R8 version 9.1.13-dev (available in AGP 9.1.0) or higher.

To define a range, use the inclusive `min..max` format. For example, the
following snippet shows that the variable `CUSTOM_VAL` accepts 26 to
2147483647:

    -assumevalues public class com.example.Foo {
        public static int CUSTOM_VAL return 26..2147483647;
    }

> [!NOTE]
> **Note:** Apps don't need to add an `-assumevalues` rule for `android.os.Build.SDK_INT` because the compiler does this implicitly based on the `minSdk` in your build configuration.

You can use this rule in the following situations:

- **For libraries**: To ensure that when apps are optimized all the local debugging hooks are removed from public library code.
- **For apps** : To remove things like debug code from a release app. It's preferable to use build variants and variants of specific source sets or constants, but if variant source sets don't work for your case, or if you need a stronger guarantee that the code paths are fully removed, use `-assumevalues`.

The following example shows a class where R8 removes debug tools from
the optimized version of an app:

    package com.example;

    public class MyConfig {
        // This field is initialized to false but is overwritten by a resource
        // value or other mechanism in the final build process. R8's static analysis
        // might see the initial 'false' but the runtime value is known to be
        // 'true'.
        public static final boolean IS_OPTIMIZED_VERSION = false;
    }

    // In another class:
    public void initFeatures() {
        if (MyConfig.IS_OPTIMIZED_VERSION) {
            System.out.println("Starting optimized features...");
            android.util.Log.d(TAG, "Starting optimized features...");
            initOptimizedService();
        } else {
            android.util.Log.d(TAG, "Starting debug/logging features...");
            initDebugTools();
        }
    }

The following rule shows how to tell R8 that the variable
`IS_OPTIMIZED_VERSION` is always expected to be set to `true`.

    -assumevalues class com.example.MyConfig {
        public static final boolean IS_OPTIMIZED_VERSION return true;
    }

### `-assumenosideeffects`

The `-assumenosideeffects` rule tells R8 that it can assume that
specified members have no side effects. R8 can completely remove calls to such
methods that have no return values or that return a fixed value.

The syntax for `-assumenosideeffects` is similar to the syntax for keeping a
[`member_specification`](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#member-spec).

The following sample shows how to tell R8 that all
`public static` methods named `log` within the `DebugLogger` class should have
no side effects, which lets it remove calls to these methods.

    -assumenosideeffects class com.example.DebugLogger {
        public static void log(...);
    }

> [!NOTE]
> **Note:** A typical use for `-assumenosideeffects` is to deactivate portions of your app that shouldn't be present in a release build, such as logging or debugging features only useful for local debugging.

## Other optimizations

These are some more advanced optimizations that are not enabled by default. When
enabling them you allow R8 to optimize code as instructed, in addition to
default optimizations.

### `-convertchecknotnull`

You can use the `-convertchecknotnull` rule to optimize null checks. This
applies to any method which takes an object parameter and throws if the object
is null, similar to a standard Kotlin assertion. The exception type and message
aren't necessarily the same, but the conditional crashing behavior is.

If a `-convertchecknotnull` rule matches a given method, each call to that
method is replaced by a call to `getClass()` on the first argument. The calls to
`getClass()` serve as a replacement null check and let R8 remove any extra
arguments of the original null check, such as expensive string allocations.

> [!NOTE]
> **Note:** This rule is available in AGP 9.0 and higher.

The syntax for `-convertchecknotnull` is as follows:

    -convertchecknotnull <class_specification> {
       <member_specification>;
    }

For example, if you have class `Preconditions` with the method `checkNotNull` as
follows:

    class Preconditions {
        fun <T> checkNotNull(value: T?): T {
            if (value == null) {
                throw NullPointerException()
            } else {
                return value
            }
        }
    }

Use the following rule:

    -convertchecknotnull class com.example.package.Preconditions {
      void checkNotNull(java.lang.Object);
    }

The rule converts all calls to `checkNotNull()` to calls to `getClass` on the
first argument. In this example, a call to `checkNotNull(bar)` is replaced by
`bar.getClass()`. If `bar` were `null`, `bar.getClass()` would throw a
`NullPointerException`, achieving a similar null-checking effect but more
efficiently.

### `-maximumremovedandroidloglevel`

This rule type removes Android logging statements (like
`Log.w`(...) and `Log.isLoggable(...)`) at or below a certain log
level.

The syntax for `maximumremovedandroidloglevel` is as follows:

    -maximumremovedandroidloglevel <log_level> [<class_specification>]

If you don't provide the optional `class_specification`, R8 applies log removal
to the entire app.

The log levels are as follows:

|---|---|
| **Log label** | **Log level** |
| VERBOSE | 2 |
| DEBUG | 3 |
| INFO | 4 |
| WARNING | 5 |
| ERROR | 6 |
| ASSERT | 7 |

For example, if you have the following code:

    class Foo {
      private static final String TAG = "Foo";
      void logSomething() {
        if (Log.isLoggable(TAG, WARNING)) {
          Log.e(TAG, "Won't be logged");
        }
        Log.w(TAG, "Won't be logged");
        Log.e(TAG, "Will be logged");
      }
    }

With the following rule:

    # A level of 5 corresponds to a log level of WARNING.
    -maximumremovedandroidloglevel 5 class Foo { void logSomething(); }

The optimized code is as follows:

    class Foo {
      private static final String TAG = "Foo";
      void logSomething() {
        Log.e(TAG, "Will be logged");
      }
    }

If you provide multiple maximum log levels for the same method, R8 uses the
minimum level. For example, given the following rules:

    -maximumremovedandroidloglevel 7 class ** { void foo(); }
    -maximumremovedandroidloglevel 4 class ** { void foo(); }

then the maximum removed log level for `foo()` is 4.