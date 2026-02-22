---
title: https://developer.android.com/jetpack/androidx/releases/preference
url: https://developer.android.com/jetpack/androidx/releases/preference
source: md.txt
---

# Preference

# Preference

[User Guide](https://developer.android.com/guide/topics/ui/settings)[Code Sample](https://github.com/android/user-interface-samples/tree/main/Preferences)  
API Reference  
[androidx.preference](https://developer.android.com/reference/kotlin/androidx/preference/package-summary)  
Build interactive settings screens without needing to interact with device storage or manage the UI.  

| Latest Update |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| July 26, 2023 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/preference#1.2.1) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Preference, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    def preference_version = "1.2.1"

    // Java language implementation
    implementation "androidx.preference:preference:$preference_version"
    // Kotlin
    implementation "androidx.preference:preference-ktx:$preference_version"
}
```

### Kotlin

```kotlin
dependencies {
    val preference_version = "1.2.1"

    // Java language implementation
    implementation("androidx.preference:preference:$preference_version")
    // Kotlin
    implementation("androidx.preference:preference-ktx:$preference_version")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460913+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460913&template=1176948)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.1

July 26, 2023

`androidx.preference:preference:1.2.1`is released.[Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b029f485084a1654dab09979141c9ecab7bbe9d..7f6fe3affdeda13640daa22bb3c6d5dab579483f/preference/preference)

**Bug Fixes**

- `PreferenceHeaderFragmentCompat`now correctly handles the system back button when used within a`ComponentDialog`or when using libraries like Hilt's`@AndroidEntryPoint`that wrap the Fragment's`Context`.
- Preference now depends on Activity 1.5.1. ([Ie5d22](https://android-review.googlesource.com/#/q/Ie5d229c9494d37ad7cceb5b412987d70bcee5e3f))
- `PreferenceHeaderFragmentCompat.onCreateInitialDetailFragment`now propagates`header.extras`as the`Fragment`arguments.

### Version 1.2.0

January 26, 2022

`androidx.preference:preference:1.2.0`and`androidx.preference:preference-ktx:1.2.0`are released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/45c977739a46f49c3eab1fe134b54676db023544..9b029f485084a1654dab09979141c9ecab7bbe9d/preference)

**Important changes since 1.1.0**

- Added`PreferenceHeaderFragmentCompat`for two-pane preference that automatically adapts based on size of the device used, making it suitable for use on phones, foldables, and tablets. The header pane is provided by overriding the`onCreatePreferenceHeader()`method on`PreferenceHeaderFragmentCompat`. Any`<Preference>`in the header`PreferenceFragmentCompat`that uses`app:fragment`will cause that fragment to appear in the second detail pane. The initial detail fragment that should be displayed before any preference is manually selected can be customized by overriding`onCreateInitialDetailFragment()`. The default implementation returns the first preference that has a fragment defined on it.

    class TwoPanePreference : PreferenceHeaderFragmentCompat() {
        override fun onCreatePreferenceHeader(): PreferenceFragmentCompat {
            return PreferenceHeader()
        }
    }

- Added nullability annotations to many of the APIs that previously did not specify`@NonNull`or`@Nullable`. This is a potentially Kotlin source breaking change if the nullability you had chosen in your Kotlin code did not match the nullability that is now defined.

- `PreferenceFragmentCompat`'s now looks for implementations of the`OnPreferenceStartFragmentCallback`,`OnNavigateToScreenListener`, and`OnDisplayPreferenceDialogListener`interface on parent fragments before looking to see if the hosting Context or Activity implement these interfaces.

### Version 1.2.0-rc01

December 15, 2021

`androidx.preference:preference:1.2.0-rc01`and`androidx.preference:preference-ktx:1.2.0-rc01`are released with no changes since`1.2.0-beta01`.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..45c977739a46f49c3eab1fe134b54676db023544/preference)

### Version 1.2.0-beta01

November 17, 2021

`androidx.preference:preference:1.2.0-beta01`and`androidx.preference:preference-ktx:1.2.0-beta01`are released with no changes from Preference 1.2.0-alpha02.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/preference)

### Version 1.2.0-alpha02

November 3, 2021

`androidx.preference:preference:1.2.0-alpha02`and`androidx.preference:preference-ktx:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca6054a5e12fcf05ba5e20bf93403afdab093986..f07d12061370a603549747200c79b60239706330/preference)

**API Changes**

- Added nullability annotations to many of the APIs that previously did not specify`@NonNull`or`@Nullable`. ([I04252](https://android-review.googlesource.com/#/q/I04252b54e80c7fcac6d652387f20ec7004b64b84),[Ie2cc0](https://android-review.googlesource.com/#/q/Ie2cc00f2df7720824d01bda67ee2b7747b4f3086))
- Removed the`openPreference()`API from`PreferenceHeaderFragmentCompat`- this method is called for you and should not be called manually. ([Ia6989](https://android-review.googlesource.com/#/q/Ia69899cc01b3c4692123cd9451e70104fdaaf577))

**Behavior Changes**

- PreferenceFragmentCompat callbacks for`OnNavigateToScreenListener`, and`OnDisplayPreferenceDialogListener`now follow the same pattern as`OnPreferenceTreeClickListener`and look up the parent fragment hierarchy for valid listeners before looking to see if the hosting Context or Activity implement these interfaces. ([I7ae6c](https://android-review.googlesource.com/#/q/I7ae6c1bc71c02be900d733e29f41a7f5dd72a605))

### Version 1.2.0-alpha01

October 27, 2021

`androidx.preference:preference:1.2.0-alpha01`and`androidx.preference:preference-ktx:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca6054a5e12fcf05ba5e20bf93403afdab093986/preference)

**New Features**

- Added`PreferenceHeaderFragmentCompat`for two-pane preference ([I9a2d8](https://android-review.googlesource.com/#/q/I9a2d87178737bb0dd2df8e4f6173f8cc690eb20c))

**Behavior Changes**

- Preference callbacks for OnPreferenceDisplayDialogCallback, OnPreferenceStartScreenCallback, and OnPreferenceStartFragmentCallback can now be implemented in a non-Activity Context. getContext() is checked to see if it implements these callbacks before checking getActivity(). If getContext() returns an Activity (the common case), then there is no behavior change.

- `PreferenceFragmentCompat`'s call to`onPreferenceTreeClick`now looks for implementations of the`OnPreferenceStartFragmentCallback`interface on parent fragments before considering the Activity's implementation. ([c64eed](https://android-review.googlesource.com/#/q/c64eed7505e6ec59172a0b2c98e7d69430d63f12))

## Version 1.1

### Version 1.1.1

April 15, 2020

`androidx.preference:preference:1.1.1`and`androidx.preference:preference-ktx:1.1.1`are released.[Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41ca691cb0eed48244912c1a1f7e9a253174e48b..f448aa7c34aae443fab98c12399bb8e848e3bbdb/preference)

**Bug Fixes**

- `PreferenceDialogFragmentCompat`will no longer throw an`IllegalStateException`when inflating a`FragmentContainerView`from xml. ([b/150051716](https://issuetracker.google.com/issues/150051716))

**Dependency updates**

- Preference now depends on[Fragment`1.2.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.4). ([aosp/1277317](https://android-review.googlesource.com/1277317))
- The`preference-ktx`dependency now depends on`androidx.core:core-ktx:1.1.0`and`androidx.fragment:fragment-ktx:1.2.4`, mirroring the dependencies of the main`preference`artifact and ensuring that upgrading`preference-ktx`updates both the main and`-ktx`artifacts of transitive dependencies. ([aosp/1277319](https://android-review.googlesource.com/1277319))

### Version 1.1.0

September 5, 2019

`androidx.preference:preference:1.1.0`and`androidx.preference:preference-ktx:1.1.0`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/9dfdadc6f6c3d72afe18252007bf44b9c6535386..41ca691cb0eed48244912c1a1f7e9a253174e48b/preference).

If this is the first`1.1.*`release you are updating to, here is a concise list of larger changes since the last stable release,`1.0.0`. You may also find the[Settings guide](https://developer.android.com/guide/topics/ui/settings),[sample app](https://github.com/android/user-interface-samples/tree/main/Preferences), and[Android Dev Summit talk](https://www.youtube.com/watch?v=PS9jhuHECEQ)useful.

**Important changes since 1.0.0**

- `PreferenceFragment`and other classes using framework Fragments have been deprecated; you should use`PreferenceFragmentCompat`and other \*compat classes instead.
- You can now set a`SummaryProvider`on a Preference to dynamically configure its summary whenever the Preference is updated, or becomes visible to the user. See the[guide](https://developer.android.com/guide/topics/ui/settings/customize-your-settings#dynamically_update_summaries)for more information.
- Added`EditTextPreference.OnBindEditTextListener`interface. This allows customizing the`EditText`displayed in the corresponding dialog after the dialog has been bound. This is a direct replacement for using attributes such as`android:inputType`directly on the`EditTextPreference`, which is not supported in the AndroidX library. See the[guide](https://developer.android.com/guide/topics/ui/settings/customize-your-settings#customize_an_edittextpreference_dialog)for more information.
- Added`Preference.setCopyingEnabled()`When set, long pressing on the Preference will show a context menu that allows copying the summary of the Preference.
- Updated`SeekBarPreference`styling to match Material specifications. See the detailed[changelog](https://developer.android.com/jetpack/androidx/releases/preference#1.1.0-alpha04)for other changes to`SeekBarPreference`.
- A large amount of bug fixes, style updates, API level compatibility fixes, and general QOL improvements.

### Version 1.1.0-rc01

July 2, 2019

`androidx.preference:preference:1.1.0-rc01`and`androidx.preference:preference-ktx:1.1.0-rc01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/5470bb0c38e4c47f1beec4ddc938aea793e21610..9dfdadc6f6c3d72afe18252007bf44b9c6535386/preference).

**API changes**

- Deprecate`Preference#onInitializeAccessibilityNodeInfo`
- This method proxied accessibility node info for a specific Preference - but this is the wrong layer for this customization. If you would like to adjust accessibility information, you should instead override onBindViewHolder, and add accessibility information to the view directly.

### Version 1.1.0-beta01

June 5, 2019

`androidx.preference:preference:1.1.0-beta01`and`androidx.preference:preference-ktx:1.1.0-beta01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311..5470bb0c38e4c47f1beec4ddc938aea793e21610/preference).

**Important changes since 1.1.0**

If this is the first 1.1.\* release you are updating to, here is a concise list of larger changes since the last stable release, 1.1.0. You may also find the[Settings guide](https://developer.android.com/guide/topics/ui/settings),[sample app](https://github.com/android/user-interface-samples/tree/main/Preferences), and[Android Dev Summit talk](https://www.youtube.com/watch?v=PS9jhuHECEQ)useful.

- PreferenceFragment and other classes using framework Fragments have been deprecated - you should use PreferenceFragmentCompat and other \*compat classes instead.
- You can now set a SummaryProvider on a Preference to dynamically configure its summary whenever the Preference is updated, or becomes visible to the user. See the[guide](https://developer.android.com/guide/topics/ui/settings/customize-your-settings#dynamically_update_summaries)for more information.
- Added`EditTextPreference.OnBindEditTextListener`interface. This allows customizing the EditText displayed in the corresponding dialog after the dialog has been bound. This is a direct replacement for using attributes such as android:inputType directly on the EditTextPreference, which is not supported in the AndroidX library. See the[guide](https://developer.android.com/guide/topics/ui/settings/customize-your-settings#customize_an_edittextpreference_dialog)for more information.
- Added`Preference.setCopyingEnabled()`When set, long pressing on the Preference will show a context menu that allows copying the summary of the Preference.
- Updated SeekBarPreference styling to match Material specifications. See the detailed[changelog](https://developer.android.com/jetpack/androidx/releases/preference#1.1.0-alpha04)for other changes to SeekBarPreference.
- A large amount of bug fixes, style updates, API level compatibility fixes, and general QOL improvements.

**API changes since 1.1.0-alpha05**

- Removes getOnBindEditTextListener from public API, you should only need to use setOnBindEditTextListener when interacting with this API.

Please file bugs[here](https://issuetracker.google.com/issues/new?component=460913)if you run into any issues, or if you have suggestions for new features!

### Version 1.1.0-alpha05

May 7, 2019

`androidx.preference:preference:1.1.0-alpha05`and`androidx.preference:preference-ktx:1.1.0-alpha05`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/968f440307eb94a35ed10a2d281749b2312b6e40..fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311/preference).

**New features**

- Updated the styling for unselectable Preferences - the title and summary now share the same color to make it clear that they cannot be interacted with, and are only used for displaying information.
- Note: you may want to consider adding`enableCopying="true"`to your unselectable Preferences, so you can long press to copy the summary.

**Bug fixes**

- Fixed a regression where PreferenceCategory and other unselectable Preferences would have a ripple effect when selected
- Fixed an accessibility issue where TalkBack did not see DropDownPreference as clickable
- Fixed some RTL layout issues
- Updated some nullable annotations in PreferenceFragmentCompat to match Fragment

### Version 1.1.0-alpha04

March 13, 2019

`androidx.preference:preference:1.1.0-alpha04`and`androidx.preference:preference-ktx:1.1.0-alpha04`are released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/eb8080404ca0086bdb1ad89235f849e25e6a6997..968f440307eb94a35ed10a2d281749b2312b6e40/preference).

**New features**

The`SeekBarPreference`update!

- Styling updated to match Material Specifications
  - The value label is now hidden by default although it can still be shown with`app:showSeekBarValue="true"`or`setShowSeekBarValue(true)`. This label is not part of Material spec, but we understand that it is heavily used so we will continue to support it - even though we don't recommend using it.
  - The value label now updates while the SeekBar is being dragged, instead of when it is released. Note that this does not mean that the value internally is updated, see below for a new API that enables that functionality.
  - Note: Although it is supported, you should avoid setting a summary on a SeekBarPreference, as it is not intended and not part of the Material spec.
- Adds support for continuous updates, allowing the SeekBar to update its saved value while the SeekBar is being dragged. This can be enabled from XML or programmatically, with`app:updatesContinuously="true"`or`setUpdatesContinuously(true)`. This will fire whenever the SeekBar's position on screen changes.

**API changes**

- Adds missing nullability annotations to`findPreference()`

**Bug fixes**

- Fixed a bug where context menu listeners were not being correctly removed if copying is not enabled

### Version 1.1.0-alpha03

February 7, 2019

#### androidx.preference:preference 1.1.0-alpha03

`androidx.preference:preference 1.1.0-alpha03`and`androidx.preference:preference-ktx 1.1.0-alpha03`are released with the following changes.

**Bug fixes**

- Fixed an issue where the copy/paste popup would sometimes not show in EditTextPreference's dialog
- Fixed an issue where the underlying adapter was not unregistered properly, causing memory leaks under specific conditions ([b/121006469](https://issuetracker.google.com/121006469))
- Fixed some dialog related crashes that occurred during configuration change ([b/122167543](https://issuetracker.google.com/122167543))
- Fixed SummaryProvider not working for MultiSelectListPreference ([b/123022772](https://issuetracker.google.com/123022772))

### Version 1.1.0-alpha02

December 17, 2018

Please also check out the recently updated[Settings guide](https://developer.android.com/guide/topics/ui/settings)and[sample app](https://github.com/android/user-interface-samples/tree/main/Preferences).

**New features**

- Added`EditTextPreference.OnBindEditTextListener`interface This allows customizing the EditText displayed in the corresponding dialog after the dialog has been bound. For example, setting a custom input type / length or adding a TextWatcher.

- Added`Preference.setCopyingEnabled()`When set, long pressing on the Preference will show a context menu that allows copying the summary of the Preference. This can be used to allow copying of static information such as user-specific IDs / application version information.

- preferenceTheme is now applied to the activity theme This means that when creating a Preference from code, you no longer need to use the context from`PreferenceManager#getContext()`- you can just use your Fragment/Activity context.

**API changes**

- Refactored`findPreference()`to return`<T extends Preference>`This means that you do not need to explicitly cast Preferences when using findPreference(). For example,`EditTextPreference preference = findPreference("edit_text")`is now valid code.

### Version 1.1.0-alpha01

November 5, 2018

**New features**

- You can now set a SummaryProvider on a Preference to dynamically configure its summary whenever the Preference is updated, or becomes visible to the user.
- Added default SummaryProvider implementations for ListPreference and EditTextPreference, which when set will automatically update the summary of the Preference to reflect its saved value, or 'Not Set' if no value has been saved. These can be set with app:useSimpleSummaryProvider="true"
- Added PreferenceGroup#removePreferenceRecursively which recursively finds and removes a Preference from the group, or a nested group lower down in the hierarchy.

**API changes**

- PreferenceFragment and other classes using framework Fragments have been deprecated - you should use PreferenceFragmentCompat and other compat classes instead.

**Bug fixes**

- Fixed iconSpaceReserved not working correctly with PreferenceCategories.
- Fixed PreferenceCategories not using colorAccent for their title's color below API 21.
- Fixed some SeekBarPreference layout inconsistencies below API 21.