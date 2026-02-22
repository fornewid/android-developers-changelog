---
title: https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally
url: https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally
source: md.txt
---

# Adopt optimizations incrementally

By default, R8 makes a lot of optimizations to improve performance and size, but the optimizations might not work for your app immediately. If you're turning on R8 (or enabling[full mode](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally#use-compat)) in a big app for the first time, try to adopt optimizations incrementally: temporarily turn off obfuscation and enable R8 for portions of code at a time, rather than for all the code in your app. We recommend taking this incremental approach during local development, but you can also use it during internal QA testing or even in production as a gradual rollout. The exact steps you take depend on your desired timeline and confidence in your pre-release testing coverage.

## Limit the optimizations

R8 does many types of optimizations including removing code, rewriting code, and removing resources. Here are some high-level descriptions of the optimization types:

- Code shrinking (or tree shaking): removes unreferenced code
- Obfuscation (or identifier minification): shortens the names of classes and methods
- Optimization: rewrites code, for example inlining

To reduce the chance of errors, you can start by enabling only some of these optimizations.

### Enable tree shaking only

Code shrinking, also known as tree shaking, removes code that appears to be unreferenced. We recommend starting with just tree shaking, since it's the most straightforward.

To enable tree shaking only, add the following to your`proguard-rules.pro`file to turn off the other types of optimizations. Turning off obfuscation is key because it makes stack traces much easier to read.  

    -dontobfuscate // Use temporarily to turn off identifier minification
    -dontoptimize // Use temporarily to turn off optimization

In the end, you wouldn't want to ship this configuration, since it drastically limits the ability for R8 to optimize code, but it's a great starting point when adopting R8 for the first time in a large codebase with problems to fix.

### Use compat mode

By default, R8 runs in[*full mode*](https://r8.googlesource.com/r8/+/refs/heads/master/compatibility-faq.md#r8-full-mode). Full mode imparts significantly improved performance and size savings, but you can temporarily disable it and use*compat mode*instead when enabling minification for the first time.
| **Note:** R8 runs in compat mode by default for Android Gradle plugin versions 7.0 and lower.

To use compat mode, use the following setting in your`gradle.properties`file:  

    android.enableR8.fullMode = false // Use temporarily to disable full mode

### Enable the rest of the optimizations

When you've confirmed that tree shaking works for your app, you can remove the preceding settings to re-enable obfuscation, optimization, and R8 full mode. Note that obfuscation can make debugging more difficult, which is why we recommend addressing tree shaking issues first.

For more information about deobfuscating stack traces, see[Recover the original stack trace](https://developer.android.com/topic/performance/app-optimization/test-and-troubleshoot-the-optimization#recover-original-stack-trace).

## Limit the optimization scope

A fully optimized build optimizes all code across every library and package, so it's common to encounter issues with R8 when you first turn it on. If you find a problem with optimization in one part of the app, don't turn off R8 completely or you'll lose out on benefits everywhere else. Instead, temporarily disable R8 only in the parts of your app that are causing problems.

### Use package-wide keep rules

We recommend using package-wide keep rules as a way to temporarily disable R8 in parts of your app. You should always come back to fix these optimization issues later; this is generally a stop-gap solution to work around problem areas.

For example, if part of your app uses Gson heavily and is causing problems with optimization, the ideal fix is to add more[targeted keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules)or move to a codegen solution. But to unblock optimizing the rest of the app, you can place the code defining your Gson types in a dedicated subpackage, and add a rule like this to your`proguard-rules.pro`file:  

    -keep class com.myapp.json.** { *; }

If some library you're using has[reflection](https://en.wikipedia.org/wiki/Reflective_programming)into internal components, you can similarly add a keep rule for the entire library. You'll need to inspect the library's code or JAR/AAR to find the appropriate package to keep. Again, this isn't recommended to maintain long term, but can unblock the optimization of the rest of the app:  

    -keep class com.somelibrary.** { *; }

| **Note:** Never write a keep rule that keeps all of your app, for example -`keep **`or -`keep com.myapp.**`. These rules prevent optimization across such a wide portion of the app that you'll pay the build cost of R8 with effectively none of the benefit. Instead, always start with library- or package- based keep rules, and try to remove them gradually over time.

### Remove package-wide keep rules

Once your app functions correctly with package-wide keep rules, you should go back and either add[targeted keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules), or remove the reflection usage or library which necessitates the keep rule in the first place.

For example, keeping all rules which extend a certain class is extremely common in AndroidX to keep only relevant classes. Generally, reflection should only target classes or methods which either extend certain abstract classes, implement certain interfaces, or into classes with a specific runtime annotation. Each of these are supported ways to define keep rules so that you don't need package-wide keep rules in your final, fully optimized app.