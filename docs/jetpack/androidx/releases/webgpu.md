---
title: https://developer.android.com/jetpack/androidx/releases/webgpu
url: https://developer.android.com/jetpack/androidx/releases/webgpu
source: md.txt
---

# webgpu

API Reference  
[androidx.webgpu](https://developer.android.com/reference/kotlin/androidx/webgpu/package-summary)  
A modern GPU API for graphics and compute from Kotlin.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | - | - | - | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/webgpu#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on Webgpu, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.webgpu:webgpu:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.webgpu:webgpu:1.0.0-alpha04")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1960262+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1960262&template=1960262)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

# Version 1.0

### Version 1.0.0-alpha04

February 11, 2026

`androidx.webgpu:webgpu:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9e043e4456c5738c6b53a773cf7765e52c0a7898..109ce75edc35d51a0e01eee5396841d7a29fd865/webgpu/webgpu).

**New Features**

- **Builder Pattern** : Introduced static Builder classes for all descriptor and state objects (e.g., `GPUDeviceDescriptor.Builder`, `GPURenderPipelineDescriptor.Builder`) to simplify object construction and improve Java interoperability.
- **Expanded Test Suite**: Added more tests, including for the new color conversion extensions, to improve library stability.
- **Documentation**: Substantially improved KDoc and Javadoc throughout the library, providing clearer definitions for API types and flags.

\*\* API Changes \*\*

- **Constructor Updates**: Public constructors for descriptor classes have been updated to support the Builder pattern; many overloaded constructors were removed to streamline the API.
- **Dawn Update**: Updated the internal Dawn source commit to dc741dd to stay synchronized with the upstream WebGPU implementation.

- Important Note: The documentation provided in this library release has been generated utilizing Google Gemini and may contain errors.

**Bug Fixes**

- Fixed incorrect default value for mask in`GPUMultisampleState` ([I41e86f0b](https://android-review.googlesource.com/#/q/I41e86f0ba42591b7ba21060710075eadf5e57eb3), [b/379441904](https://issuetracker.google.com/issues/475874978))

### Version 1.0.0-alpha03

January 14, 2026

`androidx.webgpu:webgpu:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/434a88bd0a6aa4e97ec8165cd891d4ba44d5b51d..02cfb092c18aaffda8d52b7d0608647f8bfbe48e/webgpu/webgpu).

**New Features**

- Expanded Test Suite: Added more comprehensive tests to improve library stability.
- Color Conversion Extension: Added extension functions to easily convert Android Color values into `GPUColor`.
- Unified Callback Interface: A new `GPURequestCallback` interface has been added to handle asynchronous operations more consistently across the library.
- Metadata: The library AAR now includes a `dawn_build_metadata.json` file in its assets. This file contains the specific Dawn Git SHA-1 commit used for the build.

**API Changes**

- Callback Consolidation: Several specific callback interfaces have been removed in favor of the new generic `GPURequestCallback`.

### Version 1.0.0-alpha02

December 17, 2025

`androidx.webgpu:webgpu:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..11732adebaa15eb538ab4c59c170144e8fe55185/webgpu/webgpu).

**New Features**

- Expanded Test Suite: Added more comprehensive tests to improve library stability.
- Minimum SDK Update: The library is now applicable for `minSdk` 24 and higher.

**API Changes**

- Structure Renaming: All structures are now prefixed with "GPU" for consistency with existing objects. For example, `BindGroupDescriptor` has been renamed to `GPUBindGroupDescriptor`.
- Global Method Wrapping: Global functions have been moved into a public GPU object for better clarity and organization within the Kotlin API.
- Exception Handling Refactor: Internalized the `getException` function by moving it into the `WebGpuRuntimeException` companion object. This prevents developers from accessing the internal exception creation logic while maintaining a clean public API surface.

### Version 1.0.0-alpha01

December 03, 2025

`androidx.webgpu:webgpu:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e5374362234b8b9ce9542cb16c0f4ab200471ec/webgpu/webgpu).

**New Features**

- This is the initial alpha version of the WebGPU for Android Applications library. It is intended at this stage for developer preview. The API is expected to be finalized over the next few releases.