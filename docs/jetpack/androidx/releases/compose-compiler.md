---
title: https://developer.android.com/jetpack/androidx/releases/compose-compiler
url: https://developer.android.com/jetpack/androidx/releases/compose-compiler
source: md.txt
---

# Compose Compiler

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary)  
(*See the API reference docs for all compose packages*) Transform @Composable functions and enable optimizations with a Kotlin compiler plugin.

> [!NOTE]
> **Note:** The Compose compiler has moved to the Kotlin repository. Future release notes will be available as part of [What's New In Kotlin](https://kotlinlang.org/docs/whatsnew20.html#0). For more information, see the announcement [blog post](https://android-developers.googleblog.com/2024/04/jetpack-compose-compiler-moving-to-kotlin-repository.html).

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| August 7, 2024 | [1.5.15](https://developer.android.com/jetpack/androidx/releases/compose-compiler#1.5.15) | - | - | - |

## Structure

Compose is combination of 7 Maven Group Ids within `androidx`. Each Group
contains a targeted subset of functionality, each with its own set of release
notes.

This table explains the groups and links to each set of release notes.

| Group | Description |
|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | Build animations in their Jetpack Compose applications to enrich the user experience. |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | Transform @Composable functions and enable optimizations with a Kotlin compiler plugin. |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces. |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io. |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI. |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target. |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input. |

## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "19"
    }
}
```

### Kotlin

```kotlin
android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "19"
    }
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:610764+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=610764&template=1424126)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.5

### Version 1.5.15

August 7, 2024

`androidx.compose.compiler:compiler:1.5.15` and `androidx.compose.compiler:compiler-hosted:1.5.15` are released. Version 1.5.15 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/462e8bab0c19f18478ce06c7e61dddd88034c00c..291dc76977cfd0ddfcfd674393615a0972daf029/compose/compiler).

- This compiler release is targeting Kotlin 1.9.25.

### Version 1.5.14

May 14, 2024

`androidx.compose.compiler:compiler:1.5.14` and `androidx.compose.compiler:compiler-hosted:1.5.14` are released. Version 1.5.14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6e0e5c362d12fef35722a836b756a7c4e1d9b7d8..462e8bab0c19f18478ce06c7e61dddd88034c00c/compose/compiler).

This compiler release is targeting Kotlin 1.9.24.

**Bug Fixes**

- Ensure that inline body is realized when source information is off. ([Idddb8](https://android-review.googlesource.com/#/q/Idddb882db6bf455032b12cf8a5a0d7d2bac85568))

### Version 1.5.13

May 1, 2024

`androidx.compose.compiler:compiler:1.5.13` and `androidx.compose.compiler:compiler-hosted:1.5.13` are released. Version 1.5.13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9b988d2bbe6909f45877b210d4f6af6a6466eb81..6e0e5c362d12fef35722a836b756a7c4e1d9b7d8/compose/compiler).

**New features**

- Strong skipping is no longer considered experimental and is safe for use in production. It will become the default behavior in an upcoming release. ([I6c8c4](https://android-review.googlesource.com/#/q/I6c8c46634b89933d39b1ac80ee83931fbe9f9a48))

**Bug Fixes**

- Fix binary compatibility for `@Composable` functions with value class parameters that have a default value and are wrapping a non-primitive value. ([I89465](https://android-review.googlesource.com/#/q/I894651168d0521cdc639d4f4c415b28c4e5d348f)
- Upstreamed fixes for JS and Native compilation from Compose multiplatform. See the commit range above for full details.

### Version 1.5.12

April 17, 2024

`androidx.compose.compiler:compiler:1.5.12` and `androidx.compose.compiler:compiler-hosted:1.5.12` are released. Version 1.5.12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f6e363daac4aaf96476850f7f1e834f58be9044b..9b988d2bbe6909f45877b210d4f6af6a6466eb81/compose/compiler).

**Bug Fixes**

- Fixes an issue with incremental compilation with Kotlin 1.9.23. ([Ifca55](https://android.googlesource.com/platform/frameworks/support/+/e7b0a60b6724bd39e1718dc14e3498b6fad92d60))
- Fix non-nullable types in value parameters for non-primitive inline classes. ([Ie6bb5](https://android.googlesource.com/platform/frameworks/support/+/13c32b7d5ed5b6258a795db1d983612294d1d7c6))

### Version 1.5.11

March 20, 2024

`androidx.compose.compiler:compiler:1.5.11` and `androidx.compose.compiler:compiler-hosted:1.5.11` are released. Version 1.5.11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/20b0ae439b314dda07878d2777ee5d4851dec7e6..f6e363daac4aaf96476850f7f1e834f58be9044b/compose/compiler).

**Notes**

- Starting with this version, the compiler will now call [`startReplaceGroup`](https://android-review.googlesource.com/#/q/Iad90f02440e8f7c258ff493afa6cad1c6369be7a) instead of `startReplacableGroup` when a module is compiled with a runtime that contains this method. `startReplaceGroup` was introduced in the runtime in [Compose Runtime `1.7.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.7.0-alpha03). Calls to `startRestartGroup` are only generated when targeting 1.7.0-alpha03 or later versions of the runtime.

- Calling `startReplaceGroup` instead of `startReplaceableGroup` allows the runtime to detect changes more efficiently but may affect the order in which changes are detected by the `Composer` and sent to the `Applier`. This may result in subtle changes in behavior if an `Applier` relies on the order these operations are detected.

**New Features**

- Support for Kotlin 1.9.23

**Bug Fixes**

- Fix nested external generic types being inferred Unstable. ([I3437f](https://android-review.googlesource.com/q/I3437fad769ba3eee58a299584ac4e352a3173b0f), [b/327643787](https://issuetracker.google.com/issues/327643787))
- Support multiple stability configuration files. ([I8db14](https://android-review.googlesource.com/#/q/I8db1452cf033d493255ae54d0a708be636a47eea), [b/325326744](https://issuetracker.google.com/issues/325326744))
- Compose Compiler now correctly transforms overridden functions by recursively walking through base classes/overrides. ([I2c9f9](https://developer.android.com/jetpack/androidx/releases/android-review.googlesource.com/q/I2c9f96f279736034e968bd20032c50e6de39f096), [b/316196500](https://issuetracker.google.com/issues/316196500))
- Ensure that function reference memoization doesn't try to capture implicit parents of local declarations when they are not used directly. ([Ib1267](https://android-review.googlesource.com/q/Ib12675dcc8d38ec1ecb2a8ccf9e4d1ed6f7065b1))
- Fix code generation for composable crossinline lambda (hard to encounter this bug without "nonSkippingGroupOptimization" enabled). ([Icb2fd](https://android-review.googlesource.com/q/Icb2fd2f5a946144cc105737c4a4051f02a901b78), [b/325502738](https://issuetracker.google.com/issues/325502738))

### Version 1.5.10

February 21, 2024

`androidx.compose.compiler:compiler:1.5.10` and `androidx.compose.compiler:compiler-hosted:1.5.10` are released. [Version 1.5.10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/876ebcfc9227cb4d4f4bc6a3563ad90f82066609..20b0ae439b314dda07878d2777ee5d4851dec7e6/compose/compiler)

**Bug Fixes**

- Support live literals inside init blocks. ([b/320397488](https://issuetracker.google.com/issues/320397488))
- Use dispatcher parameter to check if the function is inside local class ([b/323123439](https://issuetracker.google.com/issues/323123439))

### Version 1.5.9

February 7, 2024

`androidx.compose.compiler:compiler:1.5.9` and `androidx.compose.compiler:compiler-hosted:1.5.9` are released. [Version 1.5.9 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eb8970d76d3965442bd4c5375a036598585080cc..876ebcfc9227cb4d4f4bc6a3563ad90f82066609/compose/compiler)

**Bug Fixes**

- Fix composable calls in anonymous object initializer. ([b/320261458](https://issuetracker.google.com/issues/320261458), [96315c](https://android.googlesource.com/platform/frameworks/support/+/96315cb808d0cbccbf70ab760c0ab5b70f729e9b))
- Count recursive local declarations as captures. ([b/318745941](https://issuetracker.google.com/issues/318745941), [e7b4b0](https://android.googlesource.com/platform/frameworks/support/+/e7b4b06e67951ab47157d06ff314a5c8b2e8fdc6))
- Fix Intrinsic remember changes behavior related to Java method refs by forceing .changed for function types with intrinsic remember. ([b/319810819](https://issuetracker.google.com/issues/319810819), [77128e](https://android.googlesource.com/platform/frameworks/support/+/77128e08f24eba21d3a0e416ac238917a235dd8c))
- Added an experimental optimization that will remove the groups around functions that are not skippable such as explicitly marked as `@NonSkippableComposable` and functions that are implicitly not skippable such inline functions and functions that return a non-Unit value such as `remember`.
- This optimization can be enabled by passing plugin option, `-P plugin:androidx.compose.compiler.plugins.kotlin:nonSkippingGroupOptimization=true` to the Kotlin compiler. ([I1688f](https://android-review.googlesource.com/#/q/I1688f5dbf178696231c9c375c1299cd4a45a9fcd))

### Version 1.5.8

January 10, 2024

`androidx.compose.compiler:compiler:1.5.8` and `androidx.compose.compiler:compiler-hosted:1.5.8` are released. [Version 1.5.8 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f492f14dbbb4d25d9371bd8171f4308ec5f241c8..8520f5084641b3c918f3c2728363d1d2466ffc4a/compose/compiler)

**New Features**

- Support for Kotlin 1.9.22

**Bug Fixes**

- Fix bug where Compose Compiler build threw exceptions when built using Java21. Users who are using Compose Compiler from Google Maven (i.e., not building it themselves) were never impacted by this bug. ([b/316644294](https://issuetracker.google.com/issues/316644294))
- Fix bug where `COMPOSABLE_EXPECTED` error was being reported for some callers of non-inlined lambdas. ([b/309364913](https://issuetracker.google.com/issues/309364913))
- Add a compilation error for default parameters in open functions (previously only it was restricted only for abstract functions). Compose does not support substitution of default parameters from overridden functions at the moment, and overriding a composable function with default parameters was failing at runtime. Use `@Suppress("ABSTRACT_COMPOSABLE_DEFAULT_PARAMETER_VALUE")` to suppress, but note that overriding such function without providing a default value for parameter will result in a crash at runtime.([b/317490247](https://issuetracker.google.com/issues/317490247))
- Fixed bug in intrinsic remember which prevented values from propagating correctly. ([b/316327367](https://issuetracker.google.com/issues/316327367))

**External Contribution**

- Fix documentation typo. ([aosp/288106](https://android-review.googlesource.com/c/platform/frameworks/support/+/2881069))

### Version 1.5.7

December 19, 2023

`androidx.compose.compiler:compiler:1.5.7` and `androidx.compose.compiler:compiler-hosted:1.5.7` are released. [Version 1.5.7 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/756b7ad84884595dc9fae5ab1aa29cd329d89308..f492f14dbbb4d25d9371bd8171f4308ec5f241c8/compose/compiler)

**Bug Fixes**

- Fix compose runtime crash when `remember()` key parameter invokes a Composable function ([b/315855015](https://issuetracker.google.com/issues/315855015))
- Fix Compose runtime crash when `return@` is used. ([b/315821171](https://issuetracker.google.com/issues/315821171))
- Avoid using absolute paths in memoization keys which allows better build cache utilization. ([b/313937484](https://issuetracker.google.com/issues/313937484))

### Version 1.5.6

December 6, 2023

`androidx.compose.compiler:compiler:1.5.6` and `androidx.compose.compiler:compiler-hosted:1.5.6` are released. [Version 1.5.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1935aef1c3b3c4893c4ed900ed41552093c37e86..756b7ad84884595dc9fae5ab1aa29cd329d89308/compose/compiler)

**New Features**

- Support for Kotlin 1.9.21

**Bug Fixes**

- Enable intrinsic remember - the compiler transform that inlines remember in Compose compiler plugin and replaces `.equals` comparisons with int comparisons of the parameter meta for stable params. This results in less slots being used and less comparisons being done at runtime. The option can be disabled by providing compiler plugin argument: -P `plugin:androidx.compose.compiler.plugins.kotlin:intrinsicRemember=false`. ([If675f](https://android-review.googlesource.com/#/q/If675f9fc1cd7e197f7fcc6094124b011cca12922))
- Fix memoization of adapted function references and inline arguments. ([b/312738720](https://issuetracker.google.com/issues/312738720))
- Realize groups when exiting inline function call ([b/312242547](https://issuetracker.google.com/issues/312242547))

**External Contribution**

- Fix k/native and k/wasm runtime crash due to missing return statement in Composable functions when it's the last statement and returns a null const ([aosp/2835716](https://android-review.googlesource.com/c/platform/frameworks/support/+/2835716))

### Version 1.5.5

November 29, 2023

`androidx.compose.compiler:compiler:1.5.5` and `androidx.compose.compiler:compiler-hosted:1.5.5` are released. [Version 1.5.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e858b16810125048c66293684afdfc08f57e4ebc..1935aef1c3b3c4893c4ed900ed41552093c37e86/compose/compiler)

**Bug Fixes**

- Fixes a crash during lookup of overridden composable types ([Ib6d2c](https://android-review.googlesource.com/#/q/Ib6d2c0ec3e18716f345a61b4df465cb64d268fec), [b/297665426](https://issuetracker.google.com/issues/297665426))
  - Add `stabilityConfigurationPath` to known parameters (previously bug prevented usage of configuration file flag). ([b/309765121](https://issuetracker.google.com/issues/309765121))
  - Memoization fixes ([I081d1](https://android-review.googlesource.com/#/q/I081d18a5a35fd7296a655c5e3491d45c15ada5c1), [I4d7bf](https://android-review.googlesource.com/#/q/I4d7bf3061e60eaa6fd3af60662d6a7b02c1a83b2))
  - Recomposition fix by accounting for Uncertain param state in intrinsic remember ([b/263402091](https://issuetracker.google.com/issues/263402091))
  - Fix debugging line information for intrinsic remember ([Ic8cf5](https://android-review.googlesource.com/#/q/Ic8cf5e99bb56bd0fe6c3e6a8d0cf04c41ff4794b))
  - Fix crash (IR lowering failed) during overridden composable types lookup at compile time ([b/297665426](https://issuetracker.google.com/issues/297665426))

**External Contribution**

- Memoize stable function references with arguments ([I4d7bf](https://android-review.googlesource.com/#/q/I4d7bf3061e60eaa6fd3af60662d6a7b02c1a83b2), [b/302680514](https://issuetracker.google.com/issues/302680514))

### Version 1.5.4

November 7, 2023

`androidx.compose.compiler:compiler:1.5.4` and `androidx.compose.compiler:compiler-hosted:1.5.4` are released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/738409b08051e4780768b4e7163348898f8d6c03..e858b16810125048c66293684afdfc08f57e4ebc/compose/compiler)

**Dependency Updates**

- Compose Compiler is now compatible with Kotlin 1.9.20

**New Features**

- Add an experimental option to enable strong skipping mode. Strong skipping mode allows composables with unstable parameters to be skipped. Additionally, lambdas with unstable captures are memoized. This feature is experimental and not considered ready for production use. ([22421e](https://android-review.googlesource.com/c/platform/frameworks/support/+/2671135))
- Add flag to enable/disable source/trace information. ([4d45f09](https://android-review.googlesource.com/c/platform/frameworks/support/+/2810413))
- Allow configuring the stability of external classes via a configuration file. ([If40eb](https://android-review.googlesource.com/#/q/If40eb860d19ece10d8385ce2fd518bd5d271f620))

**Bug Fixes**

- Fix early exit from composable functions when source information is not collected. ([fe6267](https://android-review.googlesource.com/c/platform/frameworks/support/+/2737893))
- Fix continue from composable functions. ([948362](https://android-review.googlesource.com/c/platform/frameworks/support/+/2762445))
- Fix resolution when composable functions are invoked from within a function invocation that has multiple overloads that are dependent on expression return type. ([2d36d0](https://android-review.googlesource.com/c/platform/frameworks/support/+/2769286))
- Fix memoization when function reference does not have dispatch receiver. ([fc2326](https://android-review.googlesource.com/c/platform/frameworks/support/+/2770269))
- Fix dirty check which was preventing recomposition of lambdas in some situations. ([db3699](https://android-review.googlesource.com/c/platform/frameworks/support/+/2779188))
- Fix stability when incrementally compiling across modules. ([7d3e127](https://android-review.googlesource.com/c/platform/frameworks/support/+/2766125))
- Reduce scope of `@DontMemoize` to lambda expressions only. ([7a7fa52](https://android-review.googlesource.com/c/platform/frameworks/support/+/2804275))
- Fix Variables not captured correctly when using a Composable fun interface as a lambda. ([5ae3556](https://android-review.googlesource.com/c/platform/frameworks/support/+/2810414))

**External Contribution**

- Use structural equality symbol for numeric and null comparison ([c612a0](https://android-review.googlesource.com/c/platform/frameworks/support/+/2668595))

### Version 1.5.3

August 29, 2023

`androidx.compose.compiler:compiler:1.5.3`, `androidx.compose.compiler:compiler-daemon:1.5.3`, and `androidx.compose.compiler:compiler-hosted:1.5.3` are released. [Version 1.5.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ff1732b8405b315a030ae84e4e03416f36e75fad..738409b08051e4780768b4e7163348898f8d6c03/compose/compiler)

**Dependency Update**

- Kotlin version is updated to 1.9.10

### Version 1.5.2

August 23, 2023

`androidx.compose.compiler:compiler:1.5.2`, `androidx.compose.compiler:compiler-daemon:1.5.2`, and `androidx.compose.compiler:compiler-hosted:1.5.2` are released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2afaef8594bfa39e6e31140fbecae2a2c71eaf29..ff1732b8405b315a030ae84e4e03416f36e75fad/compose/compiler)

**Bug Fixes**

- Insert line numbers for return statements in constant-returning composable functions. ([I42d89](https://android-review.googlesource.com/#/q/I42d8958b996a6dd58d66d1d1068398b5032d9fe6))
- Fix a memory leak caused by switching to the new compiler plugin entrypoint. ([4f0a101](https://android-review.googlesource.com/#/q/Id70013d2d31276cf1cb062d7a7af8fafd870e3f0))
- Stop transforming non-composable fun interfaces in Compose compiler. This causes fun interfaces to be handled the same way as lambdas, including memoization rules. ([28b3ce9](https://android-review.googlesource.com/#/q/Ieabb4a9df24f77e9b5e7e41adf360c50cede604f))
- Use vararg argument type for inferring stability on call site. ([bc83645](https://android-review.googlesource.com/#/q/I0eda18303ecb655e3d0bac60ed006d41bd2e39e8))

### Version 1.5.1

July 26, 2023

`androidx.compose.compiler:compiler:1.5.1`, `androidx.compose.compiler:compiler-daemon:1.5.1`, and `androidx.compose.compiler:compiler-hosted:1.5.1` are released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da73ca08c9fa56221ac7d21a156934ddffa94a78..2afaef8594bfa39e6e31140fbecae2a2c71eaf29/compose/compiler)

**Bug Fixes**

- Fixed composition trace event markers in `@ReadOnlyComposable` functions with early returns which caused trace corruption.

### Version 1.5.0

July 18, 2023

`androidx.compose.compiler:compiler:1.5.0`, `androidx.compose.compiler:compiler-daemon:1.5.0`, and `androidx.compose.compiler:compiler-hosted:1.5.0` are released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a0c8102678bd6a0e2f5cf2df3d220b4fe85cba5e..da73ca08c9fa56221ac7d21a156934ddffa94a78/compose/compiler)

**Experimental K2 support**

- Compose compiler 1.5.0 provides experimental support for [K2 compiler](https://kotlinlang.org/docs/whatsnew19.html#try-the-k2-compiler-in-your-project). Some Compose features are not supported with K2 yet and will be coming in the future versions of the compiler.

**Important changes since 1.4.0**

- Kotlin version is updated to 1.9.0.
- [Named arguments](https://kotlinlang.org/docs/functions.html#named-arguments) for `@Composable` lambda calls have been deprecated. This feature is relying on internal compiler APIs and will not be supported by K2.
- Added a diagnostic to verify `@Composable` annotation on expect/actual calls. Both declarations are expected to have matching annotations.

## Version 1.4.8

### Version 1.4.8

June 28, 2023

`androidx.compose.compiler:compiler:1.4.8`, `androidx.compose.compiler:compiler-daemon:1.4.8`, and `androidx.compose.compiler:compiler-hosted:1.4.8` are released. [Version 1.4.8 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2fe7d40c0deea40f58e95e1e709fc55c5d5ad477..a0c8102678bd6a0e2f5cf2df3d220b4fe85cba5e/compose/compiler)

**New Features**

- Target Kotlin compiler version is bumped to 1.8.22.

**Bug Fixes**

- Improved error message for `@Composable` overrides. Now it correctly points out annotation mismatch.
- Warn about redundant `@Composable` annotation on inline lambdas that should not be marked as composable. This feature will not be supported with K2 compiler.

## Version 1.4.7

### Version 1.4.7

May 3, 2023

`androidx.compose.compiler:compiler:1.4.7`, `androidx.compose.compiler:compiler-daemon:1.4.7`, and `androidx.compose.compiler:compiler-hosted:1.4.7` are released. [Version 1.4.7 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/08777402b2ebfe081ca6468dd4c394377f43402e..2fe7d40c0deea40f58e95e1e709fc55c5d5ad477/compose/compiler)

**New Features**

- Support for Kotlin 1.8.21
- Added primitive versions of the `State` API, allowing Int, Long, Float, and Double values to be tracked in `State` objects without incurring penalties for autoboxing.

## Version 1.4.6

### Version 1.4.6

April 19, 2023

`androidx.compose.compiler:compiler:1.4.6`, `androidx.compose.compiler:compiler-daemon:1.4.6`, and `androidx.compose.compiler:compiler-hosted:1.4.6` are released. [Version 1.4.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3cde0d90f0756a2f75099eb822fba35ceb9dc06c..08777402b2ebfe081ca6468dd4c394377f43402e/compose/compiler)

**Bug Fixes**

- Compose Compiler now depends on Java11 (instead of Java17 required by Compose Compiler version 1.4.5) to better support users who are still using older versions of Java.

## Version 1.4.5

### Version 1.4.5

April 12, 2023

`androidx.compose.compiler:compiler:1.4.5`, `androidx.compose.compiler:compiler-daemon:1.4.5`, and `androidx.compose.compiler:compiler-hosted:1.4.5` are released. [Version 1.4.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b503ebce2f56c805dbbb22c3f88cd6c633a2e102..3cde0d90f0756a2f75099eb822fba35ceb9dc06c/compose/compiler)

**NOTE**
This build of Compose Compiler requires your build environment to use Java 17+. Based on user feedback, we will drop this requirement back to Java 11 and follow-up with another release (1.4.6) to better support users who are using older Java versions.

**New Features**

Support for Kotlin 1.8.20

**Bug Fixes**

- Propagate requirement of composable invoke operator override to classes and interfaces that are extending lambda interfaces with corresponding annotations.[f8f2f78a1a769c2373201027f12700e772e4e97e](https://android.googlesource.com/platform/frameworks/support/+/f8f2f78a1a769c2373201027f12700e772e4e97e)
- Allows usage of `@Composable` annotation on `getValue` operator and marks generated getter for delegate as composable in IR to ensure it is correctly transformed later. [f174f6ee60ca957d5cb6d19a5bd02a88267cdf40](https://android.googlesource.com/platform/frameworks/support/+/f174f6ee60ca957d5cb6d19a5bd02a88267cdf40)
- Fix internal compose runtime error (Expected `applyChanges()` to have been called) for inline functions.[b/274786923](https://issuetracker.google.com/issues/274786923)
- Avoid capturing `ProcessCancelledException` as it has a special meaning in the IDE.[b/274725600](https://issuetracker.google.com/issues/274725600)

**External Contribution**

- Improved support for Composable functions in Kotlin/Native.[f52b6aeed22400dd4f4a4f05559a9aa42642402c](https://android.googlesource.com/platform/frameworks/support/+/f52b6aeed22400dd4f4a4f05559a9aa42642402c)

## Version 1.4.4

### Version 1.4.4

March 22, 2023

`androidx.compose.compiler:compiler:1.4.4`, `androidx.compose.compiler:compiler-daemon:1.4.4`, and `androidx.compose.compiler:compiler-hosted:1.4.4` are released. [Version 1.4.4 contains these commits.](https://android.googlesource.com/platform/framewb503ebce2f56c805dbbb22c3f88cd6c633a2e102orks/support/+log/ef5fd7d4cad1b79f433169767b5e323565a00ad0../compose/compiler)

**Bug Fixes**

- Fix Composable inline lambda returns ([72172b](https://android.googlesource.com/platform/frameworks/support/+/dea72172bafc5dd895caced9545a05f99f04ff19))
- Allow composables to return `Nothing` (Do not generate an error when using TODO in a composable function) [3aea8d](https://android.googlesource.com/platform/frameworks/support/+/3aea8d75cbebba0233fac4cdb76e86e56f7c412c))

## Version 1.4.3

### Version 1.4.3

February 22, 2023

`androidx.compose.compiler:compiler:1.4.3` is released. [Version 1.4.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a1e56ae375f430c2b4fdbabf9796b7b45462272..ef5fd7d4cad1b79f433169767b5e323565a00ad0/compose/compiler)

**Bug Fixes**

- Fixes conditional composable calls in arguments of composable calls ([Ie93edb](https://android-review.googlesource.com/#/q/Ie93edb78b8427e56b4bef15b872a919b8bac0664))

## Version 1.4.2

### Version 1.4.2

February 8, 2023

`androidx.compose.compiler:compiler:1.4.2` is released. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5b8d5be6df46a7cc3f76f51dc54a825107ad0e93..4a1e56ae375f430c2b4fdbabf9796b7b45462272/compose/compiler)

**New Features**

- Support for Kotlin 1.8.10

**Bug Fixes**

- Add groups in the body of unskippable lambdas to avoid recomposition bug.

## Version 1.4.1

### Version 1.4.1

February 8, 2023

`androidx.compose.compiler:compiler:1.4.1` is released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7fff9039d5075dd1dd995e252c732eed7e4fe3fe..5b8d5be6df46a7cc3f76f51dc54a825107ad0e93/compose/compiler)

**Bug Fixes**

- Disable intrinsic remember optimization which had previously introduced a few code generation bugs.
- Disable intrinsic remember in functions containing a vararg parameter.
- Fix erroneous skipping in composables with default parameters
- Add defensive fallback error message if checking Kotlin compatibility fails.
- Remove skipping code generation from inline lambda

### Version 1.4.0

January 17, 2023

`androidx.compose.compiler:compiler:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c950703bd4594e7a5cf41004d1395cb44ade44a3..7fff9039d5075dd1dd995e252c732eed7e4fe3fe/compose/compiler)

**Important changes since 1.3.0**

- Support for Kotlin 1.8.0
- Turned off intrinsic remember
- The ui tooling data class `Group` now has a field, `isInline`, that indicates if the group is for a call to an inline composable function. If `isInline` is `true` then the call is to an inline composable function. However, the value might be false for calls to inline composable functions that are from modules that are compiled with a version of the compose compiler plugin that doesn't generate the inline function information.
- `ImmutableCollection` and their Persistent siblings are now considered stable.
- New param in `AnimatedContent` for tooling label
- Fixed faulty code generation for inline lambda

### Version 1.4.0-alpha02

November 11, 2022

`androidx.compose.compiler:compiler:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..c950703bd4594e7a5cf41004d1395cb44ade44a3/compose/compiler)

**New Features**

- Added support for Kotlin `1.7.21`

### Version 1.4.0-alpha01

November 9, 2022

`androidx.compose.compiler:compiler:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31382b61f1af46fc43d9a781645ca9eed1b56874..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/compiler)

**Bug Fixes**

- Fix ability to return early from inline composable functions ([b/255350755](https://issuetracker.google.com/issues/255350755))
- Fix bug in decoy lowering which broke Kotlin/JS support in Compose ([6a40f8](https://android-review.googlesource.com/c/platform/frameworks/support/+/2265412)).

## Version 1.3

### Version 1.3.2

October 4, 2022

`androidx.compose.compiler:compiler:1.3.2` is released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce1a4d490897c8f3abec98164b4aab15e6ea9d8d..31382b61f1af46fc43d9a781645ca9eed1b56874/compose/compiler)

**New Feature**

- This version includes an update to Kotlin 1.7.20

### Version 1.3.1

September 7, 2022

`androidx.compose.compiler:compiler:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ebb3487237935f82b9c7fe593e85aa9cd8f7d33e..ce1a4d490897c8f3abec98164b4aab15e6ea9d8d/compose/compiler)

**Bug Fixes**

- Fix `IllegalStateException` where Compose Compiler was erroneously marking unit types as composable in some circumstances. ([b/237863365](https://developer.android.com/issuetracker.google.com/issues/237863365))
- Users must now specify their preferred Kotlin version when suppressing compiler version check ([I9e5e2](https://android-review.googlesource.com/#/q/I9e5e22f25ac4759a23a9761ede5489a7b710e06c))

### Version 1.3.0

August 10, 2022

`androidx.compose.compiler:compiler:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ebb3487237935f82b9c7fe593e85aa9cd8f7d33e/compose/compiler)

### Version 1.3.0-rc02

August 3, 2022

`androidx.compose.compiler:compiler:1.3.0-rc02` is released. [Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..997bd961ea59ee8d9eb306712e881c227048e1da/compose/compiler)

### Version 1.3.0-rc01

July 27, 2022

`androidx.compose.compiler:compiler:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c444afe8de5e9b93062fa1504674285b5db72ba1..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/compiler)

### Version 1.3.0-beta01

July 20, 2022

`androidx.compose.compiler:compiler:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b9dc511beb3d0b4b6289338b7dcc23852cd60d4e..c444afe8de5e9b93062fa1504674285b5db72ba1/compose/compiler)

**New Features**

- Added support for Kotlin `1.7.10`

## Version 1.2

### Version 1.2.0

June 29, 2022

`androidx.compose.compiler:compiler:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..b9dc511beb3d0b4b6289338b7dcc23852cd60d4e/compose/compiler)

**Important changes since 1.1.0**

- Support for Kotlin 1.7.0
- Check out our blog post explaining our [new Compose Compiler Versioning strategy](https://android-developers.googleblog.com/2022/06/independent-versioning-of-Jetpack-Compose-libraries.html) in Compose.

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.compiler:compiler:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/compiler)

**Bug Fixes**

- Removed composable Trace Event code generation ([aosp/2127922](https://android-review.googlesource.com/c/platform/frameworks/support/+/2127922))

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.compiler:compiler:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/compiler)

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.compiler:compiler:1.2.0-beta03` is released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/compiler)

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.compiler:compiler:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/compiler)

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.compiler:compiler:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/compiler)

- This is the first beta release of 1.2! There are no changes since the last alpha.

**New Features**

- Added support for Kotlin `1.6.21`

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/compiler)

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/compiler)

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/compiler)

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/compiler)

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/compiler)

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/compiler)

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/compiler)

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.compiler:compiler:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/compiler)

**New Features**

- Added support for Kotlin `1.6.10`.

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.compiler:compiler:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/compiler)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.compiler:compiler:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/compiler)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
- Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of `48x48dp`, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.compiler:compiler:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/34f387b12323c3d92df36491123fe089602fe520..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/compiler)

**Bug Fixes**

- Updated to support Compose Material 1.1.0-rc03

### Version 1.1.0-rc02

December 16, 2021

`androidx.compose.compiler:compiler:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..34f387b12323c3d92df36491123fe089602fe520/compose/compiler)

**Dependency updates**

- Compose Compiler `1.1.0-rc02` is compatible with Kotlin `1.6.10`.

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.compiler:compiler:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/compiler)

**Dependency changes**

- Compose Compiler `1.1.0-rc01` is compatible with Kotlin `1.6.0`.
- A compatible `1.6.10` build is available through [androidx.dev](https://androidx.dev/) SNAPSHOTs with `buildId` 8003490. The following dependency snippet will
  configure SNAPSHOTs for the Compose Compiler:

  Add the following snippet to the root `build.gradle` file for your project:

      buildscript {
          repositories {
              google()
              jcenter()
              maven { url 'https://androidx.dev/snapshots/builds/8003490/artifacts/repository' }
          }
      }

  Add the following snippet to the `build.gradle` file for your app or module
  that uses Compose:

      android {
          composeOptions {
              kotlinCompilerExtensionVersion = "1.2.0-SNAPSHOT"
          }
      }

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.compiler:compiler:1.1.0-beta04` is released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/compiler)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.compiler:compiler:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/compiler)

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.compiler:compiler:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/compiler-hosted)

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.compiler:compiler:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/compiler-hosted)

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/compiler/compiler-hosted)

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/compiler/compiler-hosted)

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/compiler/compiler-hosted)

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/compiler/compiler-hosted)

**New Features**

- The Compose Compiler now supports older versions of the Compose Runtime (1.0). Prior to this change, the Compose Compiler was only compatible with the Compose Runtime of the same version or later. After this change, the Compose Compiler is compatible with an older version of the Compose Runtime (1.0). ([aosp/1796968](https://android-review.googlesource.com/c/platform/frameworks/support/+/1796968))
- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/compiler/compiler-hosted)

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.compiler:compiler:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/compiler/compiler-hosted)

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.compiler:compiler:1.0.5` is released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/compiler)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.compiler:compiler:1.0.4` is released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/compiler/compiler-hosted)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.compiler:compiler:1.0.3` is released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/compiler/compiler-hosted)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.compiler:compiler:1.0.2` is released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/compiler/compiler-hosted)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.compiler:compiler:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/compiler/compiler-hosted)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.compiler:compiler:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/compiler/compiler)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.compiler:compiler:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/compiler)

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.compiler:compiler:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/compiler/compiler)

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.compiler:compiler:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/compiler/compiler)

### Version 1.0.0-beta08

June 2, 2021

`androidx.compose.compiler:compiler:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/compiler/compiler)

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.compiler:compiler:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/compiler/compiler)

> [!NOTE]
> **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
> `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.compiler:compiler:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/compiler/compiler)

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.compiler:compiler:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/compose/compiler/compiler)

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.compiler:compiler:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/compiler/compiler)

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.compiler:compiler:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/compiler/compiler)

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.compiler:compiler:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/compiler/compiler)

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.compiler:compiler:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/compiler/compiler)

This is the first release of Compose 1.0.0 Beta.

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.compiler:compiler:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/compiler/compiler)

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.compiler:compiler:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/compiler/compiler)

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.compiler:compiler:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/compiler/compiler)

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/compiler/compiler)

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/compiler/compiler)

> [!NOTE]
> **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

### Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/compiler/compiler)

**New Features**

- **Stability Inference \& Propagation** . The Compose Compiler Plugin will analyze types it compiles to infer whether or not it is eligible for certain optimizations by the runtime. This inferred result is then synthesized as metadata onto the class to be utilized by the compiler in other modules. Furthermore, the runtime result of these inferences is passed along in metadata passed to composable calls during composition. This necessitated a different metadata protocol for composable functions, which means that composable functions compiled with the alpha07 compiler will not be binary compatible with composable functions compiled with any earlier compiler version. ([aosp/1431988](https://android-review.googlesource.com/c/platform/frameworks/support/+/1431988))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/compiler/compiler)

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/compiler/compiler)

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.compiler:compiler:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/compiler/compiler)

> [!NOTE]
> **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

`androidx.compose:compose-compiler` has been refactored to `androidx.compose.compiler:compiler`.
This is the first release in the new group.