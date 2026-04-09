---
title: https://developer.android.com/topic/performance/app-optimization/optimize-specified-packages
url: https://developer.android.com/topic/performance/app-optimization/optimize-specified-packages
source: md.txt
---

You can optimize specific packages by using R8 with `packageScope`. This is
designed as an optional first step for apps that don't yet use R8 and is not
recommended for apps that already use R8.
| **Note:** `packageScope` is only compatible with R8 in [full mode](https://developer.android.com/topic/performance/app-optimization/full-mode), and not compatibility mode.

## Consider whether to use `packageScope`

If your app already uses R8, don't use `packageScope`, because it is a
suboptimal configuration in terms of performance and app size. Instead, enhance
your app's R8 configuration with improved [keep rules](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview) or, if using
compatibility mode, by migrating to R8's full mode.

Apps that don't yet use R8, but are adopting R8, can use `packageScope` to
manage the transition incrementally. Because R8 applies powerful optimizations
that can alter app behavior, scoping these optimizations to specific packages
that are safe to optimize---such as AndroidX and Kotlin---lets you realize
performance gains with minimal risk. After your app is stable, you can gradually
expand these optimizations to the rest of your codebase and dependencies,
testing for stability at each stage.

## Prerequisites

Using R8 with `packageScope` requires Android Gradle Plugin 9.0 or later.

## Configure the optimization

To enable optimization with `packageScope`, complete the following steps.

### Choose libraries to optimize

Identify the libraries to optimize. We recommend starting with the AndroidX and
Kotlin libraries `androidx.**`, `kotlin.**`, and `kotlinx.**` because these are
stable libraries that have been configured for R8 compatibility.

### Enable support for using R8 with packageScope

Add the following to your project's `gradle.properties` file:  

    android.r8.gradual.support=true

### Set up the optimization block

In your module-level `build.gradle.kts` (or `build.gradle`) file, add an
`optimization` block to your release build configuration. Inside this block, use
`packageScope` to list the specific packages you want to optimize. In your
`build.gradle.kts` file, wrap your package list in `setOf()`.  

### Kotlin

```kotlin
android {
  buildTypes {
    release {
      proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"),"proguard-rules.pro")
      optimization {
        enable = true
        packageScope = setOf("androidx.**","kotlin.**", "kotlinx.**")
      }
    }
  }
}
```

### Groovy

```groovy
android {
  buildTypes {
    release {
      proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
      optimization {
        enable = true
        packageScope = ["androidx.**", "kotlin.**", "kotlinx.**"]
      }
    }
  }
}
```

### Test the optimization

After applying or updating the `packageScope` declaration, thoroughly [test your
app](https://developer.android.com/topic/performance/app-optimization/test-the-optimization) to verify that no unexpected crashes or behavioral changes have
occurred.

## Transition from optimizing specified packages to optimizing your entire app

To maximize optimization benefits, you should aim to gradually transition from
using `packageScope` to using R8 on your entire app. This process involves
incrementally expanding your optimization coverage:

1. **Start with stable libraries** . Begin by only including widely used, stable libraries that are compatible with R8's optimizations in the `packageScope` list. Start with the AndroidX and Kotlin libraries `androidx.**`, `kotlin.**`, and `kotlinx.**`.
2. **Incrementally add packages** . Gradually add new package prefixes to the `packageScope`:
   1. **Assess dependencies** . Review your app's libraries. Good candidates to add to the `packageScope` list include official Google libraries (for example, `com.google.**`) and other robust libraries like `OkHttp` (for example, `okhttp3.**` and `okio.**`). Prioritize libraries that don't involve heavy reflection, serialization, or native code calls (JNI).
   2. **Prioritize based on package size** . Use **Android Studio's APK
      Analyzer** to identify the biggest contributors to your app size. 1. Build a release AAB or APK with R8 turned off. 1. Open it in the Analyzer and inspect the `dex` files. 1. Sort packages by size. The largest packages offer the highest return on investment (ROI) for optimization. Targeting these first gives you the most significant size reduction early in the process, as long as these libraries don't have overly broad keep rules. See [Choose libraries wisely](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely) for more information.
3. **Verify behavior changes** . After adding each new package prefix, conduct comprehensive [testing](https://developer.android.com/topic/performance/app-optimization/test-the-optimization) to detect and resolve any regressions or unexpected behaviors.
4. **Add app packages last** . If your app packages don't use a lot of reflection, include the app packages in `packageScope` and add keep rules incrementally as needed. If your app packages use a lot of reflection, include the packages in `packageScope` and add package-wide keep rules for the required packages. Iterate over the keep rules to refine them.
5. **Move to using R8 in your entire app** . After the majority of your app's dependencies are included in the `packageScope` declaration and your app is stable, remove the `packageScope` to optimize your entire app in full mode.