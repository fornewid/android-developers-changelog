---
title: https://developer.android.com/jetpack/androidx/releases/dynamicanimation
url: https://developer.android.com/jetpack/androidx/releases/dynamicanimation
source: md.txt
---

# Dynamicanimation

# Dynamicanimation

[User Guide](https://developer.android.com/guide/topics/graphics/spring-animation)[Code Sample](https://github.com/android/animation-samples/tree/main/Motion#list--oscillation)  
API Reference  
[androidx.dynamicanimation.animation](https://developer.android.com/reference/kotlin/androidx/dynamicanimation/animation/package-summary)  
Create smooth animations with a physics-based animation API.  

| Latest Update |                                     Stable Release                                      | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| April 9, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/dynamicanimation#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on DynamicAnimation, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Java language implementation
    implementation "androidx.dynamicanimation:dynamicanimation:1.1.0"

    // Kotlin
    implementation "androidx.dynamicanimation:dynamicanimation-ktx:"
}
```

### Kotlin

```kotlin
dependencies {
    // Java language implementation
    implementation("androidx.dynamicanimation:dynamicanimation:1.1.0")

    // Kotlin
    implementation("androidx.dynamicanimation:dynamicanimation-ktx:")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460912+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460912&template=1422624)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

April 9, 2025

`androidx.dynamicanimation:dynamicanimation:1.1.0`and`androidx.dynamicanimation:dynamicanimation-ktx:1.1.0`are released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b82591147dfcbb8a7c0b9d03b0ff7ae5c648ad83..d5923c378c00b537f3421786eb3a50e6f6868386/dynamicanimation).

**API Changes**

- `DynamicAnimation`library is now stable.

### Version 1.1.0-rc01

March 26, 2025

`androidx.dynamicanimation:dynamicanimation:1.1.0-rc01`and`androidx.dynamicanimation:dynamicanimation-ktx:1.1.0-rc01`are released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8870a8ee99ec618927a9edb4b6e74b8570381149..b82591147dfcbb8a7c0b9d03b0ff7ae5c648ad83/).

### Version 1.1.0-beta01

March 12, 2025

`androidx.dynamicanimation:dynamicanimation:1.1.0-beta01`is released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce2902e01f920f17637879b6c918ffe987d2f35b..8870a8ee99ec618927a9edb4b6e74b8570381149/dynamicanimation/dynamicanimation).

**API Changes**

- Hide AnimationHandler class visibility. ([I8072e](https://android-review.googlesource.com/#/q/I8072eb333158a2f8a05590e1bb01dd59ddef9183))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I70783](https://android-review.googlesource.com/#/q/I707835de5ef50bb485fbb79d26600153ca22f6e2),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.1.0-alpha03

December 4, 2019

`androidx.dynamicanimation:dynamicanimation:1.1.0-alpha03`is released with no notable public changes since`1.1.0-alpha02`.[Version 1.1.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/668764cd97f4074bc1f309fa4b55467402332773..ce2902e01f920f17637879b6c918ffe987d2f35b/dynamic-animation).

### Version 1.1.0-alpha02

July 2, 2019

`androidx.dynamicanimation:dynamicanimation:1.1.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/21e165dc2f0fe0acc7ced317d75f4e92155a8e35..668764cd97f4074bc1f309fa4b55467402332773/dynamic-animation).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

**Bug fixes**

- Fixed a bug in the handling of pending position when canceled ([aosp/978170](https://android-review.googlesource.com/c/978170))

### Version 1.1.0-alpha01

April 3, 2019

`androidx.dynamicanimation:dynamicanimation:1.1.0-alpha01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/3478ef7cbc6b27d8c1497d76c3ffff688771380e..21e165dc2f0fe0acc7ced317d75f4e92155a8e35/dynamic-animation).

## Dynamicanimation-Ktx Version 1.0.0

### Version 1.0.0-beta01

March 12, 2025

`androidx.dynamicanimation:dynamicanimation-ktx:1.0.0-beta01`is released. Version 1.0.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce2902e01f920f17637879b6c918ffe987d2f35b..8870a8ee99ec618927a9edb4b6e74b8570381149/dynamicanimation/dynamicanimation-ktx).

### DynamicAnimation-Ktx Version 1.0.0-alpha03

December 4, 2019

`androidx.dynamicanimation:dynamicanimation-ktx:1.0.0-alpha03`is released with no notable public changes since`1.0.0-alpha02`.[Version 1.0.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/21e165dc2f0fe0acc7ced317d75f4e92155a8e35..ce2902e01f920f17637879b6c918ffe987d2f35b/dynamic-animation/ktx).

### DynamicAnimation-Ktx Version 1.0.0-alpha02

April 3, 2019

`androidx.dynamicanimation:dynamicanimation-ktx:1.0.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/5d65a6a77b8fd846a20fa35c246f377fdfda0e3b..21e165dc2f0fe0acc7ced317d75f4e92155a8e35/dynamic-animation/ktx).

**API changes**

- Changed`springAnimationOf`and`flingAnimationOf`to take in a setter and a getter instead of a target and a`FloatPropertyCompat`to instantiate a`SpringAnimation`and a`FlingAnimation`respectively.

### Dynamicanimation-Ktx Version 1.0.0-alpha01

February 7, 2019

`androidx.dynamicanimation:dynamicanimation-ktx:1.0.0-alpha01`is released. This is the first release of dynamic-animation-ktx.

**New features**

- New Kotlin API for creating`SpringAnimations`and`FlingAnimations`