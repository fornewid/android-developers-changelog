---
title: https://developer.android.com/jetpack/androidx/releases/enterprise
url: https://developer.android.com/jetpack/androidx/releases/enterprise
source: md.txt
---

# Enterprise

# Enterprise

[User Guide](https://developer.android.com/work/overview)[Code Sample](https://github.com/android/enterprise-samples)  
API Reference  
[androidx.enterprise.feedback](https://developer.android.com/reference/kotlin/androidx/enterprise/feedback/package-summary)  
Create enterprise-ready applications.  

|  Latest Update   |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|------------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| January 13, 2021 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/enterprise#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Enterprise Feedback, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    def enterprise_version = "1.1.0"

    implementation "androidx.enterprise:enterprise-feedback:$enterprise_version"
    // For testing enterprise feedback in isolation
    implementation "androidx.enterprise:enterprise-feedback-testing:$enterprise_version"
}
```

### Kotlin

```kotlin
dependencies {
    val enterprise_version = "1.1.0"

    implementation("androidx.enterprise:enterprise-feedback:$enterprise_version")
    // For testing enterprise feedback in isolation
    implementation("androidx.enterprise:enterprise-feedback-testing:$enterprise_version")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:606794+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=606794&template=1250193)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

January 13, 2021

`androidx.enterprise:enterprise-feedback:1.1.0`and`androidx.enterprise:enterprise-feedback-testing:1.1.0`are released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/769082e2b0a4eed4d6ab4189c19bfa1f9cc5753b..55d7bedcdcca20013223c29e0cde8d11c86970ae/enterprise/feedback)

**Major changes since 1.0.0**

- New Features

  - New methods added which allow for callbacks to indicate success or error.
- API Changes

  - Deprecated set and setState methods which do not give feedback on error.
  - Added callback to be triggered when setting states.

### Version 1.1.0-rc01

December 2, 2020

`androidx.enterprise:enterprise-feedback:1.1.0-rc01`and`androidx.enterprise:enterprise-feedback-testing:1.1.0-rc01`are released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..769082e2b0a4eed4d6ab4189c19bfa1f9cc5753b/enterprise/feedback)

### Version 1.1.0-beta01

October 14, 2020

`androidx.enterprise:enterprise-feedback:1.1.0-beta01`and`androidx.enterprise:enterprise-feedback-testing:1.1.0-beta01`are released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..f413b8be76bfa0a4d109a3afb583188c580a2aa6/enterprise/feedback)

No changes since 1.1.0-alpha02

### Version 1.1.0-alpha02

September 2, 2020

`androidx.enterprise:enterprise-feedback:1.1.0-alpha02`and`androidx.enterprise:enterprise-feedback-testing:1.1.0-alpha02`are released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..31022a2dda22705843be1199c786552a6f9f875d/enterprise/feedback)

**New Features**

- New methods added which allow for callbacks to indicate success or error.

**API Changes**

- Deprecate set and setState methods which do not give feedback on error.
- Add callback to be triggered when setting states. ([Ic181e](https://android-review.googlesource.com/#/q/Ic181ef2ee10d00cdb281810b081957682ffe3913))

### Version 1.1.0-alpha01

August 5, 2020

`androidx.enterprise:enterprise-feedback:1.1.0-alpha01`and`androidx.enterprise:enterprise-feedback-testing:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/825d4a371a29f073d46f219936f7ef0f6e5f437d..316f882e649c600372170f013a18515f590f490d/enterprise/feedback)

**API Changes**

- Replaced constants for max field sizes with getters. ([I2e351](https://android-review.googlesource.com/#/q/I2e351b47a2ed16adfc0545fb9b1d7a3343b8bb92),[b/140519786](https://issuetracker.google.com/issues/140519786))

**Bug Fixes**

- Now compatible with apps targeting API 30

## Version 1.0.0

### Version 1.0.0

December 18, 2019

`androidx.enterprise:enterprise-feedback:1.0.0`and`androidx.enterprise:enterprise-feedback-testing:1.0.0`are released.[Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/3d995d2fc12e3103b5bd3a5c414dfa3987f9f76c..825d4a371a29f073d46f219936f7ef0f6e5f437d/enterprise/feedback).

**Major features in 1.0.0**

- `KeyedAppStatesReporter`allows apps to report state changes to EMMs (Enterprise Mobility Management)
- `KeyedAppStatesService`allows Device Policy Managers to receive reported state changes

### Version 1.0.0-rc01

October 9, 2019

`androidx.enterprise:enterprise-feedback:1.0.0-rc01`and`androidx.enterprise:enterprise-feedback:1.0.0-rc01`are released with no changes since`1.1.0-beta01`.[Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c599f151e9be0541562bc4ac98048408eac4425..3d995d2fc12e3103b5bd3a5c414dfa3987f9f76c/enterprise).

### Version 1.0.0-beta01

September 18, 2019

`androidx.enterprise:enterprise-feedback:1.0.0-beta01`and`androidx.enterprise:enterprise-feedback-testing:1.0.0-beta01`are released with no changes since`1.0.0-alpha03`.[Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/254b8b88f073fddd0c1e30b0f9e9893cbf27f4b5..64f11e5722d8a574ccb72bfb042fa89f51129c68/enterprise).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

### Version 1.0.0-alpha03

August 7, 2019

`androidx.enterprise:enterprise-feedback:1.0.0-alpha03`and`androidx.enterprise:enterprise-feedback-testing:1.0.0-alpha03`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/9af0336e86be3d32abf5194cd7208e6bcc8ad693..254b8b88f073fddd0c1e30b0f9e9893cbf27f4b5/enterprise).
| **Note:** This version is dependent on the Java 8 programming language. Please read[Use Java 8 language features](https://developer.android.com/studio/write/java8-support)to learn how to use it in your project.

**API changes**

- `KeyedAppStatesReporter`is no longer a singleton. Use`KeyedAppStatesReporter#create`to create an instance.

### Version 1.0.0-alpha02

June 5, 2019

`androidx.enterprise:enterprise-feedback:1.0.0-alpha02`and`androidx.enterprise:enterprise-feedback-testing:1.0.0-alpha02`are released. This is the first release of`androidx.enterprise:enterprise-feedback-testing`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b0b22bbedaad3ad1f808037a7ada92f0335a71d3..9af0336e86be3d32abf5194cd7208e6bcc8ad693/enterprise/feedback).

**New features**

- New`FakeKeyedAppStatesReporter`to be used in tests.

**API changes**

- Move`getInstance`and`initialize`from`KeyedAppStatesReporter`to new class`SingletonKeyedAppStatesReporter`.
- Rename`set`and`setImmediate`to`setStates`and`setStatesImmediate`.
- Valid severity is enforced in`KeyedAppState#build`.
- Add 'get' prefix to getters on`KeyedAppState`and`ReceivedKeyedAppState`.

### Version 1.0.0-alpha01

March 21, 2019

This the first release of`androidx.enterprise:enterprise-feedback`.

`androidx.enterprise:enterprise-feedback:1.0.0-alpha01`introduces`KeyedAppStatesReporter`and`KeyedAppStatesService`, which allow apps to report state changes to EMMs (Enterprise Mobility Management).

The commits included in this initial release can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b0b22bbedaad3ad1f808037a7ada92f0335a71d3/enterprise).

**Features**

- `KeyedAppStatesReporter`can be used by apps to report state changes.
- `KeyedAppStatesService`can be used by DPCs to receive and handle state changes.