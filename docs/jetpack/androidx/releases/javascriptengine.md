---
title: https://developer.android.com/jetpack/androidx/releases/javascriptengine
url: https://developer.android.com/jetpack/androidx/releases/javascriptengine
source: md.txt
---

# JavascriptEngine

API Reference  
[androidx.javascriptengine](https://developer.android.com/reference/kotlin/androidx/javascriptengine/package-summary)  
Enable your Android app to evaluate JavaScript.  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 2, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/javascriptengine#1.0.0) | - | - | - |

## Declaring dependencies

To add a dependency on JavascriptEngine, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.javascriptengine:javascriptengine:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.javascriptengine:javascriptengine:1.0.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1225213+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1225213&template=1720664)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0

July 2, 2025

`androidx.javascriptengine:javascriptengine:1.0.0` is released with no notable changes since the last rc release. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82c11d1adf6b4e2a93f8c52f42398ae45d6fe7ae..87de50e190d7e843166cedd9df75192e999fe84b/javascriptengine/javascriptengine).

### Version 1.0.0-rc01

March 26, 2025

`androidx.javascriptengine:javascriptengine:1.0.0-rc01` is released with no notable changes since the last beta. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e3ffd7948030a769c857b8c629e0079c54b730ad..82c11d1adf6b4e2a93f8c52f42398ae45d6fe7ae/javascriptengine/javascriptengine).

### Version 1.0.0-beta01

November 1, 2023

`androidx.javascriptengine:javascriptengine:1.0.0-beta01` is released with no notable changes since hte last alpha. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..e3ffd7948030a769c857b8c629e0079c54b730ad/javascriptengine/javascriptengine)

### Version 1.0.0-alpha07

October 18, 2023

`androidx.javascriptengine:javascriptengine:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/javascriptengine/javascriptengine)

**New Features**

- New API introduced to allow apps to register callbacks to handle isolate crashes.

**API Changes**

- Rename `DEFAULT_MAX_HEAP_SIZE` to `AUTOMATIC_MAX_HEAP_SIZE`. ([I6d303](https://android-review.googlesource.com/#/q/I6d303f359434c90c338f0ded308356ee61f11ca3))
- Rename `FileDescriptorIoException` to `DataInputException`. ([Iba4eb](https://android-review.googlesource.com/#/q/Iba4ebd392f3e4ca7c0a4831a1a76fa5635a78596))
- Rename `DEFAULT_ISOLATE_HEAP_SIZE` to `DEFAULT_MAX_HEAP_SIZE`. ([Iaa16f](https://android-review.googlesource.com/#/q/Iaa16f8fc099012b135f13197fa8e4a012cd57f5f))
- Remove non-functional console `getSource` and `getTrace` methods. ([I4b7a2](https://android-review.googlesource.com/#/q/I4b7a2102ee682e52f23b4ec54dbd5647038fb551))
- Unhide `FileDescriptorIoException` ([Ic44e6](https://android-review.googlesource.com/#/q/Ic44e678260c450190fcac70d4ceb8886f667ea52))
- Allow apps to register callbacks to handle isolate crashes. ([Iad25f](https://android-review.googlesource.com/#/q/Iad25f63f60fa8fc8be6d60af89e40c97ab2b469d))

### Version 1.0.0-alpha06

October 4, 2023

`androidx.javascriptengine:javascriptengine:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..1f7407d4293384a1b91bc142880e3525048b3443/javascriptengine/javascriptengine)

**New Features**

- New API introduced to evaluate JavaScript from a `ParcelFileDescriptor/AssetFileDescriptor` without the need to convert the source into a String. `JavaScriptIsolate` class is made thread-safe.

**API Changes**

- Change `provideNamedData` to throw exception instead of returning false. ([I8909a](https://android-review.googlesource.com/#/q/I8909ad16dd777c5458855a86e817360d6a7f81d1))
- Adding APIs for evaluating JavaScript through Afds and Pfds ([I03e3a](https://android-review.googlesource.com/#/q/I03e3a8e00a990e1205853e8d8e825f605c4ebbd4))
- Make `MemoryLimitExceededException` and `SandboxDeadException` subclass `IsolateTerminatedException` ([Icf359](https://android-review.googlesource.com/#/q/Icf359de9cc83d63b376bf77b31c7873b04ba59dc))
- Removing public facing API `evaluateJavaScriptAsync(@NonNull byte[] code)` ([I4b3ac](https://android-review.googlesource.com/#/q/I4b3ac9406ada38bb5845ec3e230e3d42013ae4f9))

**Bug Fixes**

- Make `JavaScriptIsolate` thread safe. ([Ib28e0](https://android-review.googlesource.com/#/q/Ib28e00f5b7744bb4557786246d588b9273a30596))

### Version 1.0.0-alpha05

April 5, 2023

`androidx.javascriptengine:javascriptengine:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1ab1efa5be7608eac6f3d4ba7f0aae6df7df2f3e..a200cb82769634cecdb118ec4f0bfdf0b086e597/javascriptengine/javascriptengine)

**API Changes**

- Evaluation and result are no longer bound by Binder limits ([I13b1d](https://android-review.googlesource.com/#/q/I13b1d446c96925918ecd751243d8feb5d1f56faf))
- Add callback for handling isolate console messages ([I11725](https://android-review.googlesource.com/#/q/I11725004167d148c3e3b001fd0799fb4f2030253), [Ic1c11](https://android-review.googlesource.com/#/q/Ic1c110e9f7fe9cb146bd711aebefb9505a473142))

### Version 1.0.0-alpha04

February 22, 2023

`androidx.javascriptengine:javascriptengine:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..1ab1efa5be7608eac6f3d4ba7f0aae6df7df2f3e/javascriptengine/javascriptengine)

**Bug Fixes**

- Fixes a rare case of `NullPointerException` caused when the sandboxed process dies.

### Version 1.0.0-alpha03

December 7, 2022

`androidx.javascriptengine:javascriptengine:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..4a2f5e696614339c1ac21f706c1a17c0285780e7/javascriptengine/javascriptengine)

**New Features**

- Contain out of memory crashes to the responsible isolate instead of crashing the entire sandbox. Once the isolate goes out of memory, it cannot be used for further evaluation.
- Currently, the resources that the isolate holds are not freed till the sandbox is closed. This resource freeing behavior might change in later versions of the library.

**API Changes**

- Throw `MemoryLimitExceededException` when an evaluation leads to isolate going out of memory.([I336ca](https://android-review.googlesource.com/#/q/I336cae281670ed2a75e57a67cb2103cc8a722147))

### Version 1.0.0-alpha02

October 5, 2022

`androidx.javascriptengine:javascriptengine:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/javascriptengine/javascriptengine)

**New Features**

- Add `JavaScriptSandbox#isSupported` for checking whether the system supports JavaScript sandboxes.

**API Changes**

- Throw `SandboxUnsupportedException` when `JavaScriptSandbox` cannot be created due to lack of system support. ([I0dcd6](https://android-review.googlesource.com/#/q/I0dcd6f577ce55fdede9cad8c3dfb48905169f8e5))

### Version 1.0.0-alpha01

August 10, 2022

`androidx.javascriptengine:javascriptengine:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c/javascriptengine/javascriptengine)

**New Features**

- We've added experimental support for `JavaScriptSandbox` and `JavaScriptIsolate` to enable clients to evaluate JavaScript in a safe and restricted environment. This is an area of active development; the APIs are subject to change without notice.

- Please file feature requests and bugs our [JavascriptEngine component](https://issuetracker.google.com/issues/new?component=1225213&template=1720664)!