---
title: https://developer.android.com/topic/performance/app-optimization/keep-rules-overview
url: https://developer.android.com/topic/performance/app-optimization/keep-rules-overview
source: md.txt
---

# About keep rules

When you[enable app optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization)with the default settings, R8 performs extensive optimizations in order to maximize your performance benefits. R8 makes substantial modifications to the code including renaming, moving, and removing classes, fields and methods. If you observe that these modifications cause errors, you need to specify which parts of the code R8*shouldn't*modify by declaring those in keep rules.
| **Note:** Keep rules that are narrowly scoped allow for maximum optimization. Use keep rules that are as specific as possible if rules are necessary, or consider a change in libraries if usage of a library is causing problems with R8 optimizations.

## Common scenarios that require keep rules

R8 identifies and preserves all direct calls in your code. However, R8 cannot see indirect code usages, which can cause it to remove code that your app needs, causing crashes. Use keep rules to tell R8 to preserve such indirectly used code. A few common situations where you are likely to need keep rules are as follows:

- Code accessed by reflection: R8 can't identify when classes, fields or methods are accessed with reflection. For example, R8 cannot identify a method looked up by its name using`Class.getDeclaredMethod()`or an annotation retrieved with`Class.getAnnotation()`. In these cases, R8 might rename these methods and annotations or remove them entirely, leading to a`ClassNotFoundException`or a`NoSuchMethodException`at runtime.
- Code called from Java Native Interface (JNI): When native (C or C++) code calls a Java or Kotlin method, or Java or Kotlin code calls C++ code with JNI, the call is based on a dynamic string lookup of the method's name. R8 can't see the dynamic string-based method call, and so its optimizations might break your code.

This is not an exhaustive list of scenarios that require keep rules, but these scenarios cover most of the cases where you might need keep rules.
| **Note:** In modern Android development, you should limit the use of reflection and avoid calls from native code into your Java or Kotlin code where possible because these code patterns can impact performance. When selecting dependencies for your app, choose libraries that are compatible with R8 optimization. To learn more, see[Choose libraries wisely](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely).

## How to add keep rules to your app

You should add your rules to a`proguard-rules.pro`file located in the app module's root directory---the file might already be there, but if it isn't, create it. To apply the rules in the file, you must declare the file in your module-level`build.gradle.kts`(or`build.gradle`) file as shown in the following code:  

### Kotlin

```kotlin
android {
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true

            proguardFiles(
                // File with default rules provided by the Android Gradle Plugin
                getDefaultProguardFile("proguard-android-optimize.txt"),

                // File with your custom rules
                "proguard-rules.pro"
            )
           // ...
        }
    }
    // ...
}
```

### Groovy

```groovy
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true

            proguardFiles(
                // File with default rules provided by the Android Gradle Plugin
                getDefaultProguardFile('proguard-android-optimize.txt'),

                // File with your custom rules.
                'proguard-rules.pro'
            )
           // ...
        }
    }
    // ...
}
```

By default, your build file also includes the`proguard-android-optimize.txt`file. This file includes rules that are required for most Android projects, so you should let it remain in the build file. This file is based on, and shares content with, the[`proguard-common.txt`](https://cs.android.com/android-studio/platform/tools/base/+/mirror-goog-studio-main:build-system/gradle-core/src/main/resources/com/android/build/gradle/proguard-common.txt)file.
| **Warning:** You might find that older Android projects still use`proguard-android.txt`instead of`proguard-android-optimize.txt`as their default R8 configuration. If your project uses the`proguard-android.txt`file as its default R8 configuration, you should migrate to the`proguard-android-optimize.txt`file. The`proguard-android.txt`file has legacy configurations that prevent most optimizations.

Larger apps typically have code in multiple library modules. In such cases, it's often better to put the keep rules alongside the code they apply to within the specific library module. The crucial difference in maintaining keep rules for libraries lies in how you declare these rules within your library module's`build.gradle.kts`(or`build.gradle`) file. See[Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization)to learn more.
| **Note:** To learn how to optimize resources, see[Customize which resources to keep](https://developer.android.com/topic/performance/app-optimization/customize-which-resources-to-keep).

## Add a keep rule

When you add keep rules, you can include global options as well as define your own keep rules.

- **Global options** : Global options are general directives that affect how R8 operates on your entire codebase. To learn more, see[Global options](https://developer.android.com/topic/performance/app-optimization/global-options).
- **Keep rules** : Keep rules need to be designed carefully, to make sure you get the right balance between maximizing code optimization without inadvertently breaking your app. To learn how to write keep rules, see[Add keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules).

| **Note:** Keep rules are additive-they are merged from all sources. You can see which rules are applied to confirm that the consolidated keep rules are having the intended effect. To learn more, see[Check which rules are applied](https://developer.android.com/topic/performance/app-optimization/test-and-troubleshoot-the-optimization#check-which-rules-are-applied).

## Keep rules for library authors

After learning about the global options and syntax for keep rules, see[Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization)for further details.