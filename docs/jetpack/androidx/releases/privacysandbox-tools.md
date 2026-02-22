---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools
source: md.txt
---

# privacysandbox

# privacysandbox-tools

API Reference  
[androidx.privacysandbox.tools](https://developer.android.com/reference/kotlin/androidx/privacysandbox/tools/package-summary)  
A library to utilize the Privacy Sandbox functionality in Android  

| Latest Update  | Stable Release | Release Candidate | Beta Release |                                                Alpha Release                                                |
|----------------|----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| March 26, 2025 | -              | -                 | -            | [1.0.0-alpha13](https://developer.android.com/jetpack/androidx/releases/privacysandbox-tools#1.0.0-alpha13) |

## Declaring dependencies

To add a dependency on privacysandbox-tools, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement privacysandbox libraries

    implementation "androidx.privacysandbox.tools:tools:1.0.0-alpha13"
    Implementation "androidx.privacysandbox.tools:tools-apicompiler:1.0.0-alpha13"
    implementation "androidx.privacysandbox.tools:tools-apigenerator:1.0.0-alpha13"
    implementation "androidx.privacysandbox.tools:tools-core:1.0.0-alpha13"
    implementation "androidx.privacysandbox.tools:tools-testing:1.0.0-alpha13"
    implementation "androidx.privacysandbox.tools:tools-apipackager:1.0.0-alpha13"
    
    
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement privacysandbox libraries
    
    implementation("androidx.privacysandbox.tools:tools:1.0.0-alpha13")
    implementation("androidx.privacysandbox.tools:tools-apicompiler:1.0.0-alpha13")
    implementation("androidx.privacysandbox.tools:tools-apigenerator:1.0.0-alpha13")
    implementation("androidx.privacysandbox.tools:tools-core:1.0.0-alpha13")
    implementation("androidx.privacysandbox.tools:tools-testing:1.0.0-alpha13")
    implementation("androidx.privacysandbox.tools:tools-apipackager:1.0.0-alpha13")

}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1276143+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1276143&template=1756612)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha13

March 26, 2025

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha13`is released. Version 1.0.0-alpha13 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..78132378b67c86698d1ade3dc368c9f15d738a71/privacysandbox/tools).

**New Features**

- Added support for the`SessionData`parameter in`openSession`, which replaces`SessionConstants`.
- Removed the generation of`SandboxedSdkProviderCompat.getView()`, which is now deprecated.

### Version 1.0.0-alpha12

February 26, 2025

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha12`is released. Version 1.0.0-alpha12 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..fd7408b73d9aac0f18431c22580d9ab612278b1e/privacysandbox/tools).

**New Features**

- `@PrivacySandboxInterface-annotated`interfaces can now extend the`SharedUiAdapter`interface introduced in`androidx.privacysandbox.ui:ui-core:1.0.0-alpha14`, similarly to`SandboxedUiAdapter`. An interface may only extend one UI adapter type.

### Version 1.0.0-alpha11

January 29, 2025

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha11`is released. Version 1.0.0-alpha11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa/privacysandbox/tools).

**New Features**

- Added support for the updated`SessionConstants`parameter in`SandboxedUiAdapter.openSession`. ([I65886](https://android-review.googlesource.com/#/q/I65886a9b8669870929cabedd5e77659e0b53ddba))

### Version 1.0.0-alpha10

October 2, 2024

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha10`is released. Version 1.0.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/privacysandbox/tools).

**New Features**

- Add support for SDK-defined constants using`const val`in annotated interfaces and annotated values.

**API Changes**

- Disallow objects in the apicompiler (these were previously silently ignored)

**Bug Fixes**

- Fix crash when there are source directories ending in .class

### Version 1.0.0-alpha09

June 26, 2024

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha09`is released. Version 1.0.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..948119be341fa4affc055418e695d8c4c7e5e2e4/privacysandbox/tools).

**New Features**

- Add support for enum classes annotated with`@PrivacySandboxValue`.
- Support for Privacy Sandbox UI alpha 09.

### Version 1.0.0-alpha08

March 20, 2024

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha08`is released. Version 1.0.0-alpha08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..a57d7d17753695012b58c9ce7ad55a8d39157e62/privacysandbox/tools).

**New Features**

- Interfaces annotated with`@PrivacySandboxCallback`can now have methods that return values as long as the method suspends.([I16063](https://android-review.googlesource.com/#/q/I16063ea9054c5ed77768c0e631c80f45cfdcbd04))
- Bundles are now accepted as valid parameters and return types in annotated interfaces and values. ([I52995](https://android-review.googlesource.com/#/q/I52995e422051e15849b0e0888e5e7ac89ea475ae))

### Version 1.0.0-alpha07

February 7, 2024

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha07`is released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..ca2a8cf8da3a3502fccc593974f8085653e38261/privacysandbox/tools)

**API Changes**

- Support the new SDK Activity launcher interfaces. The new interfaces live in`androidx.privacysandbox.activity.core`. The old ones in`androidx.privacysandbox.ui.core`are no longer supported. ([Ia9079](https://android-review.googlesource.com/#/q/Ia90797eb47a98f520a0fcd666a43408ebe2f2c8a))

### Version 1.0.0-alpha06

September 6, 2023

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha06`is released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/privacysandbox/tools)

**Bug Fixes**

- Use non-android Guava dependencies to avoid classpath clashes in Bazel.
- Fix crash when API compiler is called from Bazel. ([I24c9d](https://android-review.googlesource.com/#/q/I24c9df4d3732046213e68ee1f6f1cbe649aacc96))

### Version 1.0.0-alpha05

August 9, 2023

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha05`is released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..5d7dd999525725bd038a00ca4e89e0fef624a6da/privacysandbox/tools)

**New Features**

- Generated`SandboxedUiAdapters`now have the new`windowInputToken`set. This makes this release compatible with`androidx.privacysandbox.ui:ui-core:1.0.0-alpha05`.

### Version 1.0.0-alpha04

May 24, 2023

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/67e516f07658def8ef5c6da4f6cb750104b6de43..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/privacysandbox/tools)

**New Features**

- `CancellationExceptions`are now propagated to apps, so SDKs can now cancel their coroutines as expected.
- `SdkActivityLaunchers`can now be used in SDK APIs, so apps can send launchers to SDKs in the Privacy Sandbox. Note that this functionality is only available in developer previews at the moment.

**Bug Fixes**

- Non-suspend functions declared by SDKs will now run in the main thread by default. They used to run in Binder threads.
- Services can no longer inherit from UI interface adapters.
- Fixed an issue where defining a UI adapter property in a data class would cause a compilation error.

### Version 1.0.0-alpha03

March 8, 2023

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03191478ed5c4864f09db2696577a3b7c9937051..67e516f07658def8ef5c6da4f6cb750104b6de43/privacysandbox/tools)

**New Features**

- Added support for Privacy Sandbox UI API integration

**API Changes**

- Changed target kotlin version to 1.8.0

### Version 1.0.0-alpha02

December 7, 2022

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8e4324d8f0eadf8e1a1d8327c5d7c8217420966e..03191478ed5c4864f09db2696577a3b7c9937051/privacysandbox/tools)

- These tools are aimed to enhance the integration with the[Privacy Sandbox SDK Runtime APIs](https://developer.android.com/design-for-safety/privacy-sandbox/guides/sdk-runtime). These tools will help with auto-generating boilerplate code to define and interact with the client-facing interfaces of the runtime-enabled SDK.

**New Features**- Adds support for defining client-facing SDK interfaces that accept callbacks and data value objects as parameters and return types - Propagate SDK exceptions to clients - Support for SDK Runtime backward compatibility generation

**API Changes**

- Adding`@JvmDefaultWithCompatibility`annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.0.0-alpha01

November 9, 2022

`androidx.privacysandbox.tools:tools-*:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8e4324d8f0eadf8e1a1d8327c5d7c8217420966e/privacysandbox/tools)

**New Features**

- This is a new Jetpack library that contains apis for utilizing the[Privacy Sandbox](https://developer.android.com/design-for-safety/privacy-sandbox)functionality. Please file bugs at our[issue tracker component](https://issuetracker.google.com/issues/new?component=1276143&template=1756612).