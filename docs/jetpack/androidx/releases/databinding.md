---
title: Databinding  |  Jetpack  |  Android Developers
url: https://developer.android.com/jetpack/androidx/releases/databinding
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Get started](https://developer.android.com/get-started/overview)
* [Jetpack](https://developer.android.com/jetpack)
* [Libraries](https://developer.android.com/jetpack/androidx/explorer)

Stay organized with collections

Save and categorize content based on your preferences.



# Databinding

[User Guide](/topic/libraries/data-binding)  [Code Sample](https://github.com/android/databinding-samples)  [Codelab](https://codelabs.developers.google.com/codelabs/android-databinding)

API Reference  
[android.databinding](/reference/android/databinding/package-summary)

Bind UI components in your layouts to data sources in your app using a declarative format.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
| --- | --- | --- | --- | --- |
| September 5, 2019 | [3.5.0](/jetpack/androidx/releases/databinding#3.5.0) | - | - | [3.6.0-alpha10](/jetpack/androidx/releases/databinding#3.6.0-alpha10) |

The databinding library is bundled with
[the Android Gradle plugin](/studio/releases/gradle-plugin).
You do not need to declare a dependency on the
library, but you must enable it.

To enable data binding, set the `dataBinding` build option to `true` in your
module's `build.gradle` file, as shown below:

```
android {
    ...
    buildFeatures {
        dataBinding true
    }
}
```

**Note:** You must enable data binding for all modules that depend on libraries
that use data binding, even if the module doesn't directly use data binding.

For more information about data binding,
see the guide to the [data binding library](/topic/libraries/data-binding),
and the Android Studio [release notes](/studio/releases)

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:192721%20status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192721&template=1096850)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.