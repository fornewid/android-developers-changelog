---
title: https://developer.android.com/jetpack/androidx/releases/loader
url: https://developer.android.com/jetpack/androidx/releases/loader
source: md.txt
---

# Loader

# Loader

[User Guide](https://developer.android.com/guide/components/loaders)[Code Sample](https://github.com/android/architecture-components-samples/blob/master/PersistenceContentProviderSample/app/src/main/java/com/example/android/contentprovidersample/MainActivity.java)  
API Reference  
[androidx.loader.app](https://developer.android.com/reference/kotlin/androidx/loader/app/package-summary)  
[androidx.loader.content](https://developer.android.com/reference/kotlin/androidx/loader/content/package-summary)  
Load data for your UI that survives configuration changes.  

|  Latest Update  |                                Stable Release                                 | Release Candidate | Beta Release | Alpha Release |
|-----------------|-------------------------------------------------------------------------------|-------------------|--------------|---------------|
| October 9, 2019 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/loader#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Loader, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.loader:loader:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.loader:loader:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460551+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460551&template=1182829)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

October 9, 2019

`androidx.loader:loader:1.1.0`is released.[Version 1.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/5201bd4b76d8abd612c147be0b4993f15ee133e3..5b6a7fdfd9ce612fa52f3fe95a9f9cb84fe9364c/loader).

**Important changes since 1.0.0**

- **Default Executor Change** : The default Executor for`AsyncTaskLoader`(and, by extension,`CursorLoader`) is now`AsyncTask.THREAD_POOL_EXECUTOR`rather than a custom Executor.
- **Setting a custom Executor** : custom implementations of`AsyncTaskLoader`or its subclasses can now override`getExecutor()`to set a custom Executor.

### Version 1.1.0-rc01

June 5, 2019

`androidx.loader:loader:1.1.0-rc01`is released with no changes from`1.1.0-beta01`.

### Version 1.1.0-beta01

March 13, 2019

`androidx.loader:loader:1.1.0-beta01`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b93a1415db20e4d3789c0f3a116f3d556ee6b603..79285e90f077844e4b3b1a72a4a051389e3c190a/loader).

**Bug fixes**

- Fixed an issue which would cause a`StaleDataException`when restarting loader from`onLoadFinished`([b/123922776](https://issuetracker.google.com/issues/123922776))

### Version 1.1.0-alpha01

December 3, 2018

**New features**

- Added a`getExecutor()`method to`AsyncTaskLoader`to allow you to set a custom Executor ([aosp/810773](https://android-review.googlesource.com/c/platform/frameworks/support/+/810773))

**Behavior changes**

- The default Executor for`AsyncTaskLoader`is now`AsyncTask.THREAD_POOL_EXECUTOR`rather than a custom Executor.