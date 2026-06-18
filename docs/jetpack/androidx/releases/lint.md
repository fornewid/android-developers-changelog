---
title: https://developer.android.com/jetpack/androidx/releases/lint
url: https://developer.android.com/jetpack/androidx/releases/lint
source: md.txt
---

# lint

Lint checks to verify usage of Gradle APIs

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| June 17, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/lint#1.0.0) | - | - | - |

## Declaring dependencies

To add a dependency on Lint, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
plugins {
    id("com.android.lint")
}
dependencies {
    lintChecks "androidx.lint:lint-gradle:1.0.0"
}
```

### Kotlin

```kotlin
plugins {
    id("com.android.lint")
}
dependencies {
    lintChecks("androidx.lint:lint-gradle:1.0.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1518777+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1518777&template=1946997)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Lint Version 1.0

### Version 1.0.0

June 17, 2026

`androidx.lint:lint-gradle:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..df2b9da6fcff9fb5520d8564e517dc1f822c5615/lint/lint-gradle).

**Major features of 1.0.0:**

`lint-gradle` ships the following checks to help Gradle plugin authors:

- Eager configuration check to defer creating and configuring objects until they are needed
- Project Isolation violations check
- Likely bugs check for calling `Provider.toString`
- Performance check that flags calls to APIs that are unexpectedly expensive
- Overly broad configuration cache inputs check
- Check to discourage usage of `Property<File>`
- Internal Gradle, Android Gradle Plugin and Kotlin Gradle plugin API usage check
- Call to `withType` without `.configureEach` check
- Usage of `GradleRunner.withPluginClasspath` check

### Version 1.0.0-rc01

May 19, 2026

`androidx.lint:lint-gradle:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bd6858009232f8364f88c4072e8aea21094b5480..706e5869c2c1c5f6db95b3684a2deaa37c96f860/lint).

### Version 1.0.0-beta01

April 22, 2026

`androidx.lint:lint-gradle:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d2ceddae2daa525785f5f17a9460d86c5a959d0b..bd6858009232f8364f88c4072e8aea21094b5480/lint/lint-gradle).

### Version 1.0.0-alpha06

April 08, 2026

`androidx.lint:lint-gradle:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/53e45a278722a68b9218cdc0c1bef1b01bc12998..d2ceddae2daa525785f5f17a9460d86c5a959d0b/lint/lint-gradle).

**New Features**

- Added check for calls to `mustRunAfter` and `shouldRunAfter` as they are expensive due to Gradle having to rearrange the task graphs.
- Added check for calls to `System.getenv()` and `System.getenv("key")` that should be going through Provider API instead
- External contribution from `josh@fueledbycaffeine.com` to add a check to detect string concatenation of Provider

### Version 1.0.0-alpha05

May 20, 2025

`androidx.lint:lint-gradle:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7bbd2bffb18b5a7d6ab44019d31979acc72315a7..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/lint/lint-gradle).

**New Features**

- Add a check to warn about usages of `configurations.create` and `configurations.maybeCreate` as these cause eager realization of that configuration starting with Gradle 8.14 and thus should be replaced with `configurations.register`.
- Add a check to catch usages of internal Kotlin Gradle Plugin APIs
- Add a check to catch usages of `evaluationDependsOn` and `evaluationDependsOnChildren` as it is not safe with Isolated Projects feature.

### Version 1.0.0-alpha04

April 23, 2025

`androidx.lint:lint-gradle:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2ffcbb08c7221e79b12c0ef234bcfb5517d10ece..7bbd2bffb18b5a7d6ab44019d31979acc72315a7/lint/lint-gradle).

**New Features**

- Add a check for accidental `Provider<String>.toString` calls as they are likely bugs.
- Add check to catch uses of methods, properties, fields coming from internal types.

**Bug Fixes**

- Fix `GradleProjectIsolation` check to allow usage of `Project.isolated`.
- Fix `WithTypeWithoutConfigureEach` check to catch uses of `Project.tasks.withType<Task>()` without `configureEach`.
- Fix `InternalGradleApiUsage` check to catch fully qualified usages of internal APIs.

### Version 1.0.0-alpha03

December 11, 2024

`androidx.lint:lint-gradle:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9cd42c5cbf5e69b0223d5b0c357593175182f365..2ffcbb08c7221e79b12c0ef234bcfb5517d10ece/lint/lint-gradle).

**New Features**

- Catch calls to `Provider<>.toString` as it is nearly always a bug to do that.
- Catch calls of Kotlin collection extension functions on `TaskContainer` as these cause eager `Task` creation.
- Catch calls to `ConfigurableFileCollection.from` passing in a `Configuration` as that causes eager resolution of the configuration suggesting to use `project.files(configuration)` or `configuration.incoming.artifactView {}.files`.
- Catch usages of `Property<File>` suggesting to use `RegularFileProperty` or `DirectoryProperty` as it is enforcing the use directory vs file.

### Version 1.0.0-alpha02

September 4, 2024

`androidx.lint:lint-gradle:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..9cd42c5cbf5e69b0223d5b0c357593175182f365/lint/lint-gradle).

**New Features**

- Added a check for discouraged `GradleRunner.withPluginClasspath` API.
- Added checks for APIs that are problematic for lazy configuration by flagging calls to `TaskContainer.withType` without calling `configureEach`.
  - Added checks for APIs that are problematic for Gradle Project Isotation by flagging calls to `Project.getRootProject`, `Project.findProject`, `Project.getParent`, `Project.findProperty`, `Project.getProperties`, `Project.hasProperty`, `Project.property`.

### Version 1.0.0-alpha01

February 21, 2024

`androidx.lint:lint-gradle:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054/lint/lint-gradle)

**New Features**

- An initial set of lint checks for Gradle Plugin authors to help them catch mistakes in their code. They are expected to be used on Gradle projects that apply `java-gradle-plugin`. It will catch uses of internal Gradle and Android Gradle Plugin APIs and eager task configuration.