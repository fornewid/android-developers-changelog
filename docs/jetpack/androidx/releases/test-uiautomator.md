---
title: https://developer.android.com/jetpack/androidx/releases/test-uiautomator
url: https://developer.android.com/jetpack/androidx/releases/test-uiautomator
source: md.txt
---

# Test Uiautomator

API Reference  
[androidx.test.uiautomator](https://developer.android.com/reference/kotlin/androidx/test/uiautomator/package-summary)  
Framework for cross app functional UI testing

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [2.3.0](https://developer.android.com/jetpack/androidx/releases/test-uiautomator#2.3.0) | - | [2.4.0-beta01](https://developer.android.com/jetpack/androidx/releases/test-uiautomator#2.4.0-beta01) | - |

## Declaring dependencies

To add a dependency on test, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement UIAutomator tests
    androidTestImplementation "androidx.test.uiautomator:uiautomator:2.4.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement UIAutomator tests
    androidTestImplementation("androidx.test.uiautomator:uiautomator:2.4.0-beta01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1237242+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1237242&template=1727743)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Test Uiautomator Shell Version 1.0

### Version 1.0.0-alpha03

December 03, 2025

`androidx.test.uiautomator:uiautomator-shell:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..deb96499dfe95073f5c1215c1287787683cb1e92/test/uiautomator/uiautomator-shell).

**API Changes**

- Changed `startActivity` wait to wait for new window ([I35da6](https://android-review.googlesource.com/#/q/I35da611a69d95bdbd58830387f4fe423bbb17f84), [b/440021797](https://issuetracker.google.com/issues/440021797))
- Updated `screenSizePixel` in `RecorderCommands` ([If558c](https://android-review.googlesource.com/#/q/If558cccb893ad6b317ec6817640187d379d585d8), [b/429173157](https://issuetracker.google.com/issues/429173157))

### Version 1.0.0-alpha02

August 13, 2025

`androidx.test.uiautomator:uiautomator-shell:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..c359e97fece91f3767a7d017e9def23c7caf1f53/test/uiautomator/uiautomator-shell).

### Version 1.0.0-alpha01

June 18, 2025

`androidx.test.uiautomator:uiautomator-shell:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb/test/uiautomator/uiautomator-shell).

**New Features**

- First alpha version of the ui-automator shell library to execute shell commands as shell user. This library allows reading stdout, stderr and writing in the stdin of a sh process launched by shell. De facto, it backports `UiAutomation#executeShellCommandRwe` introduced in api 34.

## Version 2.4

### Version 2.4.0-beta01

February 11, 2026

`androidx.test.uiautomator:uiautomator:2.4.0-beta01` and `androidx.test.uiautomator:uiautomator-shell:2.4.0-beta01` are released. Version 2.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/test/uiautomator).

**API Changes**

- Make state-less commands singletons. ([I3394c](https://android-review.googlesource.com/#/q/I3394c1c604eee2b946190f40cc996f472c0f48d9), [b/429173157](https://issuetracker.google.com/issues/429173157))
- Update the `RecorderCommands` API. ([Ie09e8](https://android-review.googlesource.com/#/q/Ie09e80f9670a1506ecbe8b7bed9928cadedeffd8), [b/429173157](https://issuetracker.google.com/issues/429173157))
- Simplify the `RecorderCommands` API to have a well defined lifecycle. ([I30f89](https://android-review.googlesource.com/#/q/I30f8999f2d850a66297566e4e2d930d39fa9e5b2), [b/444305673](https://issuetracker.google.com/issues/444305673))

### Version 2.4.0-alpha07

December 03, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha07` is released. Version 2.4.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..deb96499dfe95073f5c1215c1287787683cb1e92/test/uiautomator/uiautomator).

**API Changes**

- Changed `startActivity` wait to wait for new window. This makes the launch generally synchronous, and allows future versions of Macrobenchmark to configure launch completion detection. ([I35da6](https://android-review.googlesource.com/#/q/I35da611a69d95bdbd58830387f4fe423bbb17f84), [Id6e6f](https://android-review.googlesource.com/#/q/Id6e6fc2468209706c77897ff3bcc762ce2688d43), [b/440021797](https://issuetracker.google.com/issues/440021797))
- Removed api without explicit package name in `UiAutomatorTestScope`. ([I8c285](https://android-review.googlesource.com/#/q/I8c2853b7d5a745da91526514eab2ab19fc1cedde), [b/413417205](https://issuetracker.google.com/issues/413417205))

### Version 2.4.0-alpha06

August 13, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha06` is released. Version 2.4.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..c359e97fece91f3767a7d017e9def23c7caf1f53/test/uiautomator/uiautomator).

**New Features**

- Added window-based APIs for improved multi-window testing, i.e. `UiDevice#findWindow` can now be used to find a specific `UiWindow` according to a `ByWindowSelector` built with `By.Window` factory methods. ([I359c4](https://android-review.googlesource.com/#/q/I359c4b3c36b1c20af4c50ccc3d2e7dbfeb0cd15b), [I40528](https://android-review.googlesource.com/#/q/I40528316751814034580696f01ab78eb696e83bf), [I8c963](https://android-review.googlesource.com/#/q/I8c963f8f32ac280fc1cc361ce7b75d01c658152b))

### Version 2.4.0-alpha05

June 18, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha05` is released. Version 2.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/test/uiautomator/uiautomator).

**API Changes**

- Added `UiObject2#waitForStable` as a shortcut for `UiObject2#accessibilityNodeInfo#waitForStable()`

### Version 2.4.0-alpha04

June 4, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha04` is released. Version 2.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..786176dc2284c87a0e620477608e0aca9adeff15/test/uiautomator/uiautomator).

**API Changes**

- Renamed `onView` to `onElement` to clarify it works with compose ([I53a3b](https://android-review.googlesource.com/#/q/I53a3b4e35ee2fad641bf243ce015bc48fe02c012), [b/419006806](https://issuetracker.google.com/issues/419006806))

**Bug Fixes**

- Fix `waitForStableInActiveWindow` ([290457f1](https://android.googlesource.com/platform/frameworks/support/+/290457f1e7a325b8f837a65f47a46a26cfea4d46), [b/420349130](https://issuetracker.google.com/issues/420349130))

### Version 2.4.0-alpha03

May 20, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha03` is released. Version 2.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5bd5ca55a22a1deb5f07f8c3c02e9db8b59b9729..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/test/uiautomator/uiautomator).

**Bug Fixes**

- Fixed `waitForStableInActiveWindow` throwing NPE in some cases ([Ibf50f](https://android-review.googlesource.com/#/q/Ibf50f93af389bc435cf3d2534a705d91d200b238), [b/417046391](https://issuetracker.google.com/issues/417046391))

### Version 2.4.0-alpha02

May 7, 2025

`androidx.test.uiautomator:uiautomator:2.4.0-alpha02` is released. Version 2.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..5bd5ca55a22a1deb5f07f8c3c02e9db8b59b9729/test/uiautomator/uiautomator).

**New Features**

- Initial shape of new `Uiautomator` Api. `UiAutomatorTestScope` can be created through the factory `uiAutomator` that gives access to the new `onView` apis.
- Initial Lint Rules for warning about usage of `AccessibilityNodeInfo#getText` and suggest usage of `textAsString`.

**API Changes**

- Added `Configurator#setDefaultDisplayId` to set a display ID to restrict all searches to ([Icdf17](https://android-review.googlesource.com/#/q/Icdf17c781faebf3fe3ca2197e6717e75240b3a06)).
- Changed `Searchable` (interface shared by `UiDevice` and `UiObject2`) to public for convenience ([I67f18](https://android-review.googlesource.com/#/q/I67f18bfc4a61c412c5ca2c15073980204a0643a8)).

**Bug Fixes**

- Fixed handling of meta keys in `UiDevice#pressKeyCodes`. ([I73f80](https://android-review.googlesource.com/#/q/I73f809e7f198c83933f12b265b83662b214e02e6)).
- Updated `UiDevice#getWindowRoots` to always return roots in Z order ([I87426](https://android-review.googlesource.com/#/q/I874266f868d541420dde15cce2d240523dbf5276)).
- Fixed issue where certain gestures were incomplete ([I60dd3](https://android-review.googlesource.com/#/q/I60dd322923a2146fcfcaadf881f7701c3457e772), [If4edd](https://android-review.googlesource.com/#/q/If4edd9dfa2e2a84039778b33eb4a1bf3f49e3672)).
- Fixed rare infinite loop when calling `UiDevice#scrollUntil` ([I39989](https://android-review.googlesource.com/#/q/I39989a26744a16dadb4fb339b2a756a6f9964282)).

### Version 2.4.0-alpha01

June 26, 2024

`androidx.test.uiautomator:uiautomator:2.4.0-alpha01` is released. Version 2.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f8d91d904a453dc1b9661cb43ea02b62436a1e6..948119be341fa4affc055418e695d8c4c7e5e2e4/test/uiautomator/uiautomator).

**API Changes**

- Deprecated `Configurator#getKeyInjectionDelay` and `setKeyInjectionDelay` as the parameter is unused now that text is always injected directly rather than by key presses. ([I3bcc5](https://android-review.googlesource.com/#/q/I3bcc58975300f83c2e49b41ece57b7e2f0385265)).

**Bug Fixes**

- Updated the delay between `UiObject2` motion events to account for dynamic refresh rates (i.e. Smooth Display) ([I43f12](https://android-review.googlesource.com/#/q/I43f12c4d40dc21f000983572232796d5d6439330)).
- Reduced flakiness from accessibility node staleness on certain UIs by periodically invalidating the accessibility cache ([I3be25](https://android-review.googlesource.com/#/q/I3be25f8a627766be1fbb2760d2188ae69fda5ae9)).
- Fixed `StaleObjectException`s occurring when calling `toString` or `hashCode` on a stale `UiObject2`. ([I38ea1](https://android-review.googlesource.com/#/q/I38ea13d4040879c0fe896434d760565de99ff50a)).
- Improved `UiWatcher` performance by skipping unnecessary `waitForIdle` calls. ([I8c65e](https://android-review.googlesource.com/#/q/I8c65ead246dee1d1d99562e0f7d934a9fa30db16)).
- Fixed javadoc inaccuracies, especially to clarify when each `Configurator` parameter is used. ([Ie10b1](https://android-review.googlesource.com/#/q/Ie10b14bdc4d5010a360e285374f1835be6f5f8f3), [I71631](https://android-review.googlesource.com/#/q/I7163105da85bf3cb8a2cb7f6f9c1fdfb94ec8f4f)).

## Version 2.3.0

### Version 2.3.0

February 21, 2024

`androidx.test.uiautomator:uiautomator:2.3.0` is released. [Version 2.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6a7f32e3b6350cc12f5fac272e832cc1b445dbb4..4f8d91d904a453dc1b9661cb43ea02b62436a1e6/test/uiautomator/uiautomator)

**Important changes since 2.2.0**

- **Multi-display support** : Added support for finding and operating on objects across multiple displays, and `UiDevice` methods to manage secondary displays ([Ie6544](https://android-review.googlesource.com/#/q/Ie65445d36be6b771543a30263c66252adf8bed84), [I912cd](https://android-review.googlesource.com/#/q/I912cd814a58f9a53a90a6e4edca66e5dbc31c283)).
- **New selectors** :
  - Added `By.displayId` to select objects by their display ID ([I1825b](https://android-review.googlesource.com/#/q/I1825b1715755ebd58b58b3fc3bd3a4dba7224970)).
  - Added `By.hasParent` and `By.hasAncestor` to select objects according to their parents ([I93c36](https://android-review.googlesource.com/#/q/I93c36cf79aec441046904c3a90c64adf7fe65d09)).
  - Added `By.hint` methods to select objects by their hint text ([Idd345](https://android-review.googlesource.com/#/q/Idd34586e5c596f31d477535df2d442327c18374a)).
- **Custom conditions** : Exposed a `Condition` interface to support custom wait conditions, and added corresponding `UiDevice#wait`, `UiObject2#wait`, and `UiObject2#scrollUntil` methods ([27c0ea](https://android-review.googlesource.com/#/q/27c0ea7b5022a7dc93d9dd48134309e2cfacc982), [099d6e](https://android-review.googlesource.com/#/q/099d6e5cd8861faf0bf18c4973ad33c04dacd723)).
- **Bug fixes and reliability**
  - Fixed an issue where the display size calculations were occasionally incorrect and might ignore portions of the screen ([Ifc016](https://android-review.googlesource.com/#/q/Ifc016cd4bd6929705100129fac92d6d355be563d)). Coordinates and offsets used in tests may need to be adjusted.
  - Updated `MotionEvent` injection to improve accuracy ([678ca3](https://android-review.googlesource.com/#/q/678ca3be0081003ecaf9ff1b64375bb90bab4974)) and better emulate user gestures ([454450](https://android-review.googlesource.com/#/q/45445069f33284e8e135c9023c69fd58ce0835c8)).
  - Improved the reliability of scrolls ([I7b059](https://android-review.googlesource.com/#/q/I7b0595c5c55168af434a2957dc4f29df41e3e124)), rotations ([c6cea0](https://android-review.googlesource.com/#/q/c6cea022c21c0e6947636fbbd0fa69639b9ebfc4)), long clicks ([49572b](https://android-review.googlesource.com/#/q/49572b17ec2dcf5392aa804866f2f028b1d29352)), pinches ([3c619a](https://android-review.googlesource.com/#/q/3c619aa35d7dd121e3d0d27fd13bbb5d6f41cc35)), and more.

### Version 2.3.0-rc01

February 7, 2024

`androidx.test.uiautomator:uiautomator:2.3.0-rc01` is released with no changes. [Version 2.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2a18d2fb964100da245733f3af716c8967387769..6a7f32e3b6350cc12f5fac272e832cc1b445dbb4/test/uiautomator/uiautomator)

### Version 2.3.0-beta01

December 13, 2023

`androidx.test.uiautomator:uiautomator:2.3.0-beta01` is released. [Version 2.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3ffd7948030a769c857b8c629e0079c54b730ad..2a18d2fb964100da245733f3af716c8967387769/test/uiautomator/uiautomator)

**API Changes**

- Renamed the `UiObject2` percentage-based margin methods to `setGestureMarginPercentage` and `setGestureMarginsPercentage` for consistency ([I24435](https://android-review.googlesource.com/#/q/I244356db7a2e61a5b2eb43664004119d07a0a7b4))

**Bug Fixes**

- Improved the error thrown when a secondary display is not found or not accessible ([116b23](https://android-review.googlesource.com/#/q/116b230aefac90c63225a14468706537b152e58c))

### Version 2.3.0-alpha05

November 1, 2023

`androidx.test.uiautomator:uiautomator:2.3.0-alpha05` is released. [Version 2.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..e3ffd7948030a769c857b8c629e0079c54b730ad/test/uiautomator/uiautomator)

**API Changes**

- Added `UiObject2#getDrawingOrder` to expose drawing order (z-index) information. ([I5dfa4](https://android-review.googlesource.com/#/q/I5dfa4f12ee03cff473d6cddd76c060f5ee9a701b)).
- Added `UiDevice` methods to get, set, freeze, and unfreeze the rotation of secondary displays. ([I912cd](https://android-review.googlesource.com/#/q/I912cd814a58f9a53a90a6e4edca66e5dbc31c283)).

**Bug Fixes**

- Added retry to `UiObject2#scrollUntil` when the end of scrolling could not be detected ([Ibac6f](https://android-review.googlesource.com/#/q/Ibac6f1ece6f1d786614b6b49d1f5cfe3630d4d12)).
- Fixed issue where `UiDevice` would use a stale `Instrumentation` instance if it was recreated ([I18cae](https://android-review.googlesource.com/#/q/I18cae09e7c29e7c993ba37633664fef5f312a18d)).
- Fixed possible NPE if the display ID cannot be determined when dumping nodes ([Icafcb](https://android-review.googlesource.com/#/q/Icafcb9a4965bf5b45f6553a9c65a7ba2dfe07bda)).
- Added warning when performing clicks/scrolls on non-clickable/scrollable objects ([I4a5d9](https://android-review.googlesource.com/#/q/I4a5d9804da04dc3f3da60c0051147035e4bc8211)).
- Reduced the default `UiObject2` scroll speed to improve reliability ([I5e071](https://android-review.googlesource.com/#/q/I5e071d55a2be2883e8a3a0450d030bb1a4184825)).

### Version 2.3.0-alpha04

July 26, 2023

`androidx.test.uiautomator:uiautomator:2.3.0-alpha04` is released. [Version 2.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6882a779510068fe72f7ec0b5e5471925b33e9be..4aed940027a19667e67d155563fc5fa8b7279313/test/uiautomator/uiautomator)

**API Changes**

- Added `By.hasParent` and `By.hasAncestor` to support finding objects according to their parents ([I93c36](https://android-review.googlesource.com/#/q/I93c36cf79aec441046904c3a90c64adf7fe65d09)).
- Added `UiObject2#getHint` to retrieve an object's hint text, and `By.hint` methods to select objects according to their hint text ([Idd345](https://android-review.googlesource.com/#/q/Idd34586e5c596f31d477535df2d442327c18374a)).
- Added `By.displayId` to support selecting objects according to the display they are on ([I1825b](https://android-review.googlesource.com/#/q/I1825b1715755ebd58b58b3fc3bd3a4dba7224970)).
- Added `UiDevice#getDisplayHeight(int)` and `UiDevice#getDisplayWidth(int)` methods to find the dimensions of a display by its ID ([Ie6544](https://android-review.googlesource.com/#/q/Ie65445d36be6b771543a30263c66252adf8bed84)).
- Re-added `wait(SearchCondition, long)` and `wait(UiObject2Condition, long)` methods for backwards compatibility ([Iebfda](https://android-review.googlesource.com/#/q/Iebfdae01df087edd0962c7050c946b1890789224)).
- Changed `UiDevice#executeShellCommand` to public but discouraged instead of hidden ([Ic48a1](https://android-review.googlesource.com/#/q/Ic48a1113c4a3feba516852ea530686bd5b352a73)).

**Bug Fixes**

- Updated `MotionEvent` injection to reduce flakiness by prioritizing gesture accuracy over speed ([678ca3](https://android-review.googlesource.com/#/q/678ca3be0081003ecaf9ff1b64375bb90bab4974)).
- Added tracing to resource heavy methods to identify performance bottlenecks ([d17de3](https://android-review.googlesource.com/#/q/d17de3c365f196c6049804aad55c8841ce9a8e93)).
- Added a retry mechanism when initiating a UiAutomation connection ([048caf](https://android-review.googlesource.com/#/q/048cafd2a99f368c4b1ccd4bc628629a8d988c29)).
- Fixed a possible NPE from null nodes in `UiDevice#dumpWindowHierarchy` ([b725eb](https://android-review.googlesource.com/#/q/b725eb65c5bdb9d450bf1383a49eef2b885dfc86)).
- Fixed unexpected errors from querying or operating on private displays ([985db6](https://android-review.googlesource.com/#/q/985db6a4df203e07bdd83cfc8585dbb06d78f62a), [7053d4](https://android-review.googlesource.com/#/q/7053d44e6b5adf57f98624495248831de183b7d3)).

### Version 2.3.0-alpha03

April 19, 2023

`androidx.test.uiautomator:uiautomator:2.3.0-alpha03` is released. [Version 2.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..6882a779510068fe72f7ec0b5e5471925b33e9be/test/uiautomator/uiautomator)

**API Changes**

- Exposed a `Condition` interface to allow custom wait conditions instead of relying solely on the built-ins in `Until`, and updated `UiDevice#wait` and `UiObject2#wait` methods to accept this interface ([27c0ea](https://android-review.googlesource.com/#/q/27c0ea7b5022a7dc93d9dd48134309e2cfacc982)).
- Added `UiObject2#scrollUntil` to support scrolling until a condition is met and to reach parity with `UiScrollable` ([099d6e](https://android-review.googlesource.com/#/q/099d6e5cd8861faf0bf18c4973ad33c04dacd723)).
- Added `UiDevice#setOrientationPortrait` and `setOrientationLandscape` to facilitate rotations across device types ([e13cb7](https://android-review.googlesource.com/#/q/e13cb7f29fbd503a37ec523e60702db6c98893d4)).
- Added `UiObject2#setGestureMarginPercent` to support setting margins relative to the object size. ([Ib8c77](https://android-review.googlesource.com/#/q/Ib8c77c47411899f8c5e038c159d043dfc9487648))

**Bug Fixes**

- Fixed `UiScrollable` methods occasionally using invalid coordinates on SDKs 18 to 22 ([b53ece](https://android-review.googlesource.com/#/q/b53eced73f68d3cfa6a32ef25fba6c57c37371a1)).
- Fixed `UiObject2#setText` and `clearText` failing to modify text on SDKs 18 and 19 ([77e41d](https://android-review.googlesource.com/#/q/77e41d4f1065cd94855e1cc9c109f7c186b676a2)).
- Fixed `UiWatcher`s not being executed in the right order ([c85f92](https://android-review.googlesource.com/#/q/c85f92f87646f9c376027b78ad14cf31e596f6c7)).
- Fixed issue where device rotation might not yet be complete after a `UiDevice` orientation change ([c6cea0](https://android-review.googlesource.com/#/q/c6cea022c21c0e6947636fbbd0fa69639b9ebfc4)).
- Improved reliability of long clicks, drags, and pinches ([49572b](https://android-review.googlesource.com/#/q/49572b17ec2dcf5392aa804866f2f028b1d29352), [3c619a](https://android-review.googlesource.com/#/q/3c619aa35d7dd121e3d0d27fd13bbb5d6f41cc35)).

### Version 2.3.0-alpha02

January 11, 2023

`androidx.test.uiautomator:uiautomator:2.3.0-alpha02` is released. [Version 2.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..adf1c279a86ab3886e1666c08e2c3efba783367b/test/uiautomator/uiautomator)

**API Changes**

- Reworked logging throughout the library to provide more information, warn about possible issues, and improve consistency.
- Added `UiDevice#pressKeyCodes` to support pressing multiple keys simultaneously, e.g. pressing POWER and VOLUME_DOWN to take a screenshot ([22e525](https://android-review.googlesource.com/#/q/22e52585b69be2c6c124881fbf3ae4ad8afee955)).
- Added `UiDevice#setCompressedLayoutHierarchy` and deprecated `UiDevice#setCompressedLayoutHeirarchy` to fix a typo in the method name ([4e2f65](https://android-review.googlesource.com/#/q/4e2f65a802478583785fd429cadeb6d224cc0d8c)).
- Marked `UiAutomatorInstrumentationTestRunner` as deprecated as it handles deprecated `UiAutomatorTestCase`s and is no longer necessary ([be6c85](https://android-review.googlesource.com/#/q/be6c85d618040a475492c9e5e56c29726afc3007)).
- Updated delay between `UiObject2` `MotionEvent`s to twice the display refresh rate to better emulate user gestures ([454450](https://android-review.googlesource.com/#/q/45445069f33284e8e135c9023c69fd58ce0835c8)).
- Added support for multiline text and description matching ([1625e6](https://android-review.googlesource.com/#/q/1625e615b9aed44323029da2726a57390956e4ab), [b/255787130](https://issuetracker.google.com/issues/255787130)).

**Bug Fixes**

- Fixed `StaleObjectException`s occasionally being thrown while querying or waiting for objects ([4cbcc0](https://android-review.googlesource.com/#/q/4cbcc08ac347605cf8d0f868738d504147d443bf)).
- Fixed the return values of `UiScrollable#scrollToBeginning`, `scrollToEnd`, `flingToBeginning`, and `flingToEnd` not denoting whether the beginning/end was reached ([d33e06](https://android-review.googlesource.com/#/q/d33e06a5b39fd68dc2e83a51e9b4de9c9210dba4)).
- Fixed `UiScrollable#scrollForward` and `scrollBackward` methods ignoring the configured timeout ([29e4f3](https://android-review.googlesource.com/#/q/29e4f311bbc7a3ef045177c137b2dce0c34a4ea8)).
- Fixed the `BySelector` copy constructor not handling depth selectors ([6c7b91](https://android-review.googlesource.com/#/q/6c7b91d2b375f344d7d3051c428d06a7862674f5)).
- Fixed the handling of invalid percent values in `UiObject#pinchIn` and `pinchOut` ([01b973](https://android-review.googlesource.com/#/q/01b9732dc0d5c5d2cd446189700a0c0d8af63800)).
- Fixed a rare issue where multi-window support was lost if the underlying `UiAutomation` connection was reset ([1bb956](https://android-review.googlesource.com/#/q/1bb956d848661061e7f5aadf95659b869315f187)).

### Version 2.3.0-alpha01

September 7, 2022

`androidx.test.uiautomator:uiautomator:2.3.0-alpha01` is released. [Version 2.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74/test/uiautomator/uiautomator)

**API Changes**

- Annotated the nullness of all public methods.
- Switched `MotionEvent` injection to asynchronous with a short delay for smoother `UiObject2` gestures.
- Reduced the polling interval while waiting from 1000ms to 100ms.
- Updated `UiDevice#wakeUp` and `UiDevice#sleep` to use `KEYCODE_WAKEUP` and `KEYCODE_SLEEP` to support devices that override the power button.
- Added `UiObject2#getDisplayId` and support for finding and managing objects across multiple displays.
- Added `UiObject#click` and `UiObject2#clickAndWait` methods for clicking on a point using its coordinates.

**Bug Fixes**

- Fixed an issue where the display size calculations were occasionally incorrect and might ignore portions of the screen, especially in multi-window mode ([Ifc016c](https://android-review.googlesource.com/#/q/Ifc016cd4bd6929705100129fac92d6d355be563d)).
- Fixed the scaling of screenshots in `UiDevice#takeScreenshot` ([Id80ad6](https://android-review.googlesource.com/#/q/Id80ad6e1d6a05fca8c8158bc5420f7f2af025103)).
- Improved the reliability of `Until.scrollFinished` and `UiObject2#scroll` ([I7b0595](https://android-review.googlesource.com/#/q/I7b0595c5c55168af434a2957dc4f29df41e3e124)).
- Fixed strict mode `IncorrectContextUseViolation` warnings ([Iffa6a0](https://android-review.googlesource.com/#/q/Iffa6a076b96fd78f47dc30a38d12b10a927933a9)).