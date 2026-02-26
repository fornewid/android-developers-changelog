---
title: https://developer.android.com/jetpack/androidx/releases/navigation3
url: https://developer.android.com/jetpack/androidx/releases/navigation3
source: md.txt
---

# navigation3

API Reference  
[androidx.navigation3.runtime](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary)  
[androidx.navigation3.ui](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/package-summary)  
Navigation 3 is a new navigation library designed to work with Compose.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/navigation3#1.0.1) | - | - | [1.1.0-alpha05](https://developer.android.com/jetpack/androidx/releases/navigation3#1.1.0-alpha05) |

## Declaring dependencies

To add a dependency on navigation3, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.navigation3:navigation3-runtime:1.1.0-alpha05"
    implementation "androidx.navigation3:navigation3-ui:1.1.0-alpha05"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigation3:navigation3-runtime:1.1.0-alpha05")
    implementation("androidx.navigation3:navigation3-ui:1.1.0-alpha05")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1750212+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1750212&template=2102223)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Version 1.1

### Version 1.1.0-alpha05

February 25, 2026

`androidx.navigation3:navigation3-*:1.1.0-alpha05` is released. Version 1.1.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..c640b9aa8e30b5db9ee258561ad1fc4bc947e69d/navigation3).

**API Changes**

- `NavDisplay` and `rememberSceneState` now take a `List<SceneStrategy>` instead of the previous single `SceneStrategy` parameter that was chained by the `then` infix. This more closely aligns with the `List<SceneDecoratorStrategy<T>>` that both of these APIs already take. The previous APIs have been deprecated. ([I78b2c](https://android-review.googlesource.com/#/q/I78b2c1c393a72b3f9fea3b615a0f23559e66809b), [b/482108465](https://issuetracker.google.com/issues/482108465))
- Added a metadata #contains operator to check if the metadata map contains the given `NavMetadataKey`. ([Ic30db](https://android-review.googlesource.com/#/q/Ic30dbb34dba4d45f54868e40bd57edeb9f44668d), [b/485311895](https://issuetracker.google.com/issues/485311895))
- Added `NavMetadataKey` `DialogKey` for `DialogSceneStrategy` to use with Metadata DSL. ([Ic7a26](https://android-review.googlesource.com/#/q/Ic7a2685dd0882e1e66e8416de3fc8063de301ba6), [b/483388817](https://issuetracker.google.com/issues/483388817))

### Version 1.1.0-alpha04

February 11, 2026

`androidx.navigation3:navigation3-*:1.1.0-alpha04` is released. Version 1.1.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..628cb9b293c226198b42c59be36a956491f36133/navigation3).

**New Features**

- Navigation3 now provides a new type-safe metadata DSL. The DSL uses a new `MetadataKey` interface that allows for defining the key and value types that they wish to provide to the metadata map. This also added new `NavMetadataKey`s for `NavDisplay` transitions so that they can be used with the new `metadata` DSL to add transitions to `NavDisplay`. ([Ic10ef](https://android-review.googlesource.com/#/q/Ic10ef1857ca440f4579a81995897f677cd664674), [Ic049c](https://android-review.googlesource.com/#/q/Ic049c029a3aff96319dcacb506efebd44b1bd097),[b/476213928](https://issuetracker.google.com/issues/476213928))

**API Changes**

- The `OverlayScene` interface has a new `onRemoved` suspending callback. This callback is invoked after a key associated with the scene is removed from the backstack, but before it leaves composition. This allows exit animations called within `onRemoved` to complete before the overlay scene is removed from composition. ([I29a72](https://android-review.googlesource.com/#/q/I29a728f2bc10ff4c0126ddf912907140a49676f9), [b/440558061](https://issuetracker.google.com/issues/440558061))

**Bug Fixes**

- Fixed an error where passing a `SharedTransitionLayout` into either the `NavDisplay` or `rememberSceneState` and using any `OverlayScene` would cause a crash because using `SharedTransitionLayout` only works with `NavEntries` that are rendered as part of the `AnimatedContent` and `OverlayScene` are rendered in their own windows separately. ([I1bb76](https://android-review.googlesource.com/#/q/I1bb76dd63bc11f84eaeffb3bcb61cd3e8cb795e8), [b/478664101](https://issuetracker.google.com/issues/478664101))

**Dependency Update**

- From `Navigation3` 1.0.1: `Navigation3` now depends on `NavigationEvent` 1.0.2. This fixes an `IllegalStateException` caused by using `NavDisplay` during `AndroidStudio` Previews. ([Id7212](https://android-review.googlesource.com/#/q/Id72127281dd27ad9d53d2fc38704ea81c9a05b20), [b/477149762](https://issuetracker.google.com/issues/477149762))

### Version 1.1.0-alpha03

January 28, 2026

`androidx.navigation3:navigation3-*:1.1.0-alpha03` is released. Version 1.1.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d4384815af3bab6af755069a70ea0c492e015e9f..b0ea337f3538c22dae2295d6a9265ab0c753e301/navigation3).

**New Features**

- You can now dynamically add metadata with consideration for the entry key via the `EntryProvider` DSL. ([I942fb](https://android-review.googlesource.com/#/q/I942fb23e416c3b8c79ef5422ead6ce738200cbb0), [b/474416976](https://issuetracker.google.com/issues/474416976))

### Version 1.1.0-alpha02

January 14, 2026

`androidx.navigation3:navigation3-*:1.1.0-alpha02` is released. Version 1.1.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/navigation3).

**New Features**

- `SceneStrategy` now supports nesting scenes via a new `calculatedScene(Scene)` function. This means that `SceneStrategy`'s can be customized to provide additional functionality to other scenes. ([I5df7c](https://android-review.googlesource.com/#/q/I5df7c23d70804a0b817d333fa54a9f1fe465b612),[b/440333896](https://issuetracker.google.com/issues/440333896))

### Version 1.1.0-alpha01

December 03, 2025

`androidx.navigation3:navigation3-*:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7eee8c24b22a08646c79f7457d72a760c36ccc25..deb96499dfe95073f5c1215c1287787683cb1e92/navigation3).

**API Changes**

- `Navigation3` now supports treating scenes as shared element object. This means that when the scenes change, it is possible to ensure they have a smooth transition. You can enable this by passing a `SharedTransitionScope` to either the `NavDisplay` or to `rememberSceneState`. ([I15868](https://android-review.googlesource.com/#/q/I1586863735423ff93fced01a20048f66bebc3eee))

## Version 1.0

### Version 1.0.1

February 11, 2026

`androidx.navigation3:navigation3-*:1.0.1` is released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7eee8c24b22a08646c79f7457d72a760c36ccc25..add6a0ae146bc8a21394e7a83e0fea2e8dc31b5a/navigation3).

**Dependency Update**

- `Navigation3` now depends on `NavigationEvent` 1.0.2. This fixes an `IllegalStateException` caused by using `NavDisplay` during `AndroidStudio` Previews. ([Id7212](https://android-review.googlesource.com/#/q/Id72127281dd27ad9d53d2fc38704ea81c9a05b20), [b/477149762](https://issuetracker.google.com/issues/477149762))

### Version 1.0.0

November 19, 2025

`androidx.navigation3:navigation3-*:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c211305886d70caa42620facce1b97ed7e47bf5..7eee8c24b22a08646c79f7457d72a760c36ccc25/navigation3).

**Introducing Navigation3!**

- The Navigation3 library is now stable! Navigation3 is the AndroidX Compose first approach to navigation.
- For more information, see our [announcement blog post](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html), visit the [resources](https://goo.gle/nav3), and try [the recipes](https://github.com/android/nav3-recipes).

### Version 1.0.0-rc01

November 05, 2025

`androidx.navigation3:navigation3-*:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..ebd829d61998c48ea35b0e2adbc801d9c5ae36cc/navigation3).

**Bug Fixes**

- `NavDisplay` now sets a `LocalLifecycleOwner` at the `Scene` level that allows scene authors to determine whether all transitions have finished by checking that the `Lifecycle.State` is `RESUMED`. The behavior of the `LocalLifecycleOwner` at the `NavEntry` level is unchanged: it also remains capped at `STARTED` if a transition is in progress and is additionally capped at `CREATED` if that `NavEntry` has been popped from the back stack and is in the process of animating out. ([I03113](https://android-review.googlesource.com/#/q/I03113a4729d59a9d2bc09d4422d41615f60ab935), [b/454045829](https://issuetracker.google.com/issues/454045829))

### Version 1.0.0-beta01

October 22, 2025

`androidx.navigation3:navigation3-*:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7b8a27d59a3cd5d0aa8259755193aadbd5c119da..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/navigation3).

**API Changes**

- `SceneStrategyScope` now only has a no argument public constructor, suitable for testing your `SceneStrategy` and the returned `Scene` in isolation. For more complex use cases, please use `rememberSceneState()`. ([I8440c](https://android-review.googlesource.com/#/q/I8440ca6a5d4c86aa24ffb7646a8d3b9e85ca3db0), [b/451679047](https://issuetracker.google.com/issues/451679047))

**Bug Fixes**

- Fixed infinite loop when chaining `SceneStrategy` with `then`. ([Iba3f0](https://android-review.googlesource.com/#/q/Iba3f0efce620b1cf0afce7c448d72838ce274eab), [b/450323470](https://issuetracker.google.com/issues/450323470))
- Fixed screen flicker when swapping the `backStack` passed to `NavDisplay` and using animations. ([Ief7b5](https://android-review.googlesource.com/#/q/Ief7b5f0a334f15f51fd6ee0d81b0af39c46198f2), [b/450967248](https://issuetracker.google.com/issues/450967248))

### Version 1.0.0-alpha11

October 08, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd..7b8a27d59a3cd5d0aa8259755193aadbd5c119da/navigation3).

**API Changes**

- The `calculateScene` method on `SceneStrategy` is no longer `@Composable`. Instead, consider moving this work to the construction of your `SceneStrategy` method (i.e., in a `rememberMySceneStrategy()` method) that fully allows you to define the lifetime of any `rememberSaveable` values or key `remember` statements off of the correct values. ([If1733](https://android-review.googlesource.com/#/q/If17337d860c1d3a8b048639f2c929e8d4f9a2b10), [b/448709506](https://issuetracker.google.com/issues/448709506))
- The `onBack` parameter for `SceneStrategy.calculateScene` has been moved into the new receiver scope of `SceneStrategyScope` to make it more clear that this is an optional parameter and provide an extension point for future Navigation3 features. ([I3aea3](https://android-review.googlesource.com/#/q/I3aea32521ce10121fbe931885bd9d2f04a75c389), [b/448460407](https://issuetracker.google.com/issues/448460407))
- The `onBack` lambda passed into `NavDisplay` and to your `SceneStrategy` no longer provides a `count: Int` parameter to indicate when multiple entries should be popped. Instead, the `() -> Unit` lambda will now be called multiple times in a row in the rare case where your Scene requests popping multiple entries. ([Idedb5](https://android-review.googlesource.com/#/q/Idedb5b579a9589523bedad8d7ed687ac224d09d1), [b/446989346](https://issuetracker.google.com/issues/446989346))
- Remove the `NavEntryWrapper` class and replace its functionality with a final `NavEntry` class with a new secondary constructor that takes a `NavEntry` with new content. This will allow continued support for wrapping an entry with new content. ([I7da2a](https://android-review.googlesource.com/#/q/I7da2aa71f3dad927b964b9fd34e59d8eb7e252ab), [b/444447130](https://issuetracker.google.com/issues/444447130))
- The `navEntryDecorator` function which creates and returns a `NavEntryDecorator` has been removed and replaced by the `NavEntryDecorator` class which is now made public and open for subclassing. ([If81f8](https://android-review.googlesource.com/#/q/If81f85846a52e8f70708e51932b4ff132ec6222b), [b/444447434](https://issuetracker.google.com/issues/444447434), [b/447381176](https://issuetracker.google.com/issues/447381176))
- `SavedStateNavEntryDecorator` has been renamed to `SaveableStateHolderNavEntryDecorator` since it decorates entries with a `SaveableStateHolder`. The decorator has also been refactored from a function to a class since it is functionally a factory for `NavEntryDecorator`. ([Ie6013](https://android-review.googlesource.com/#/q/Ie60132e292e0d8ffb4c0c7b5ac219c37822e2028), [b/447381176](https://issuetracker.google.com/issues/447381176))
- Custom displays using `SceneState` as an alternative to using `NavDisplay` no longer are required to use the `LocalEntriesToRenderInCurrentScene` composition local, which is now internal. ([Ic40ef](https://android-review.googlesource.com/#/q/Ic40ef603fd633af7aca1a4f3ec945f12764b09cf), [b/414668196](https://issuetracker.google.com/issues/414668196))
- Removed `SceneSetupNavEntryDecorator` and `rememberSceneSetupNavEntryDecorator()` from the public API surface. This functionality now is included by default without requiring you to manually include it. ([Ieae42](https://android-review.googlesource.com/#/q/Ieae4287893db27dbec2fdb463775af35886c010a), [b/444479133](https://issuetracker.google.com/issues/444479133))
- `NavEntry`, `DialogScene`, `SinglePaneScene`, and `SceneState` now all implement equals. ([I96121](https://android-review.googlesource.com/#/q/I96121c5865c3484f00aaf09d4b74a07be90b720a))
- Scene interface has a new metadata field to attach scene-specific metadata for NavDisplay. This allows a Scene to override the metadata on the `NavDisplay`, for instance with transitions. ([I1fd96](https://android-review.googlesource.com/#/q/I1fd96ad077055e27e5b090f3ae948b402902140b), [b/443955625](https://issuetracker.google.com/issues/443955625))
- Simplify `rememberNavBackStack` signature by removing the redundant generic type parameter. The function now accepts `vararg elements: NavKey`. ([I03e45](https://android-review.googlesource.com/#/q/I03e45a8cfbb0bb90671bd12c4efc3520ff20ae7e))
- The default animations for `NavDisplay` are now part of the common API which allows them to be called from all platforms. ([I71af9](https://android-review.googlesource.com/#/q/I71af90046145cb574e65063dd0167b93f5509d2f), [b/447147159](https://issuetracker.google.com/issues/447147159))
- Rename `EntryProviderBuilder` to `EntryProviderScope` to accurately reflect that the class is a Kotlin DSL providing a scope to build `NavEntries`. ([Ia7465](https://android-review.googlesource.com/#/q/Ia74653a4a69625b92621534ca30cf284ec01b9a0))

**Bug Fixes**

- `rememberNavBackStack()` now enforces polymorphic serialization for NavKey and requires a custom `SavedStateConfiguration` that is configured to ensure correct state restoration. KDoc have been updated to reflect the requirement that all NavKey subtypes must be registered in the provided SerializersModule. ([I6de37](https://android-review.googlesource.com/#/q/I6de3767a8052e15bca9fe68d3bd794decb997f77),[I782f2](https://android-review.googlesource.com/#/q/I782f2734974d9c959501654a9c50d0c363b5d9dd), [b/446664383](https://issuetracker.google.com/issues/446664383))

### Version 1.0.0-alpha10

September 24, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/navigation3).

**API Changes**

- Add new `NavDisplay` overload that takes a list of `NavEntry<T>` that has been decorated by `rememberDecoratedNavEntries`. ([I4025b](https://android-review.googlesource.com/#/q/I4025be493bd837d96a56894370b4f4eb0227143a), [b/441940314](https://issuetracker.google.com/issues/441940314))
- Moved `DialogScene` to a new package. ([Ia5840](https://android-review.googlesource.com/#/q/Ia58400aa23e85e37872e3f2cdce661b52379d2a8))
- Remove public API `DecorateNavEntry`. Instead use `rememberDecoratedNavEntries` to wrap a NavEntry with a list of decorators. ([Id8c09](https://android-review.googlesource.com/#/q/Id8c099a0b03f9da15a3f0ef3c49308e45e35aaae))
- Navigation3 UI now provides new default `transitionSpec` properties. ([Ibcabd](https://android-review.googlesource.com/#/q/Ibcabd125b19ad4ecb7044b23cbcf80c714cf2094))
- Added a new `SceneState` object to help manage scenes. This also provides a new `NavDisplay` overload that takes the `SceneState` and the `NavigationEventState`. ([Idfb46](https://android-review.googlesource.com/#/q/Idfb4648b798e71000277448e355a00e0fb1e4fd1), [b/444479133](https://issuetracker.google.com/issues/444479133))
- `NavDisplay` now allows you to customize the transitions based on what `Scene` you are going to and from by looking at the `Transition`'s `currentState` and `targetState`. ([I906cc](https://android-review.googlesource.com/#/q/I906cc1a8305e1d6cabfdfe8a4ac555e330863fbf), [b/443872322](https://issuetracker.google.com/issues/443872322))
- `NavigationEventInfo` is now an `abstract class` instead of an `interface`. Update all custom implementations to inherit from the class (e..g, `data class MyInfo : NavigationEventInfo()`). ([I1e59c](https://android-review.googlesource.com/#/q/I1e59c844ec7c68a2824d0215af228e47fa6bc4e1), [b/444734264](https://issuetracker.google.com/issues/444734264))
- The `navigationevent-compose` handler APIs are updated. `NavigationEventHandler` and `NavigationBackHandler` (and variants) now support a new overload that accepts a hoisted `NavigationEventState`s. The simple overloads (taking `currentInfo`) are preserved and now use this new state model internally. ([Ic3251](https://android-review.googlesource.com/#/q/Ic32511e845d8b2ca72f9d97aa01d1a3c319f5705), [b/444734264](https://issuetracker.google.com/issues/444734264))
- All of the Scene APIs have been moved out of navigation3-ui to navigation3-runtime. This means they are now available on all platforms supported by navigation3-runtime. ([I431d0](https://android-review.googlesource.com/#/q/I431d043c8b1fd6cc52f86e7747093b78f285e2d2), [b/444449993](https://issuetracker.google.com/issues/444449993))
- Added new `rememberDecoratedNavEntries` overload that takes a list of `NavEntry` to decorate. The input entries can be already decorated with other entry decorators. ([I5a034](https://android-review.googlesource.com/#/q/I5a034a05db2f4c5e5510e21711a66f2cbe693a40), [b/444230270](https://issuetracker.google.com/issues/444230270))
- Remove navigation3 wildcard type parameters ([I02540](https://android-review.googlesource.com/#/q/I0254058ade649e023bd4c68e1067cbf8e5c31b09))
- Improved the handling of generics for the `entryProvider` DSL. If you were previously importing `androidx.navigation3.runtime.entry`, this is no longer required. ([I299fc](https://android-review.googlesource.com/#/q/I299fc79a5e1ade5136d8ff6e1184adb1820851fe))
- Restrict the reflection-based `NavBackStackSerializer` overload to Android. This prevents implicit runtime serialization failures on non-Android platforms by enforcing the use of the explicit `SavedStateConfiguration` overload in multiplatform code. ([I73313](https://android-review.googlesource.com/#/q/I733133f455bb8244d5df78f845b74d54fdcb8ad7), [b/420443609](https://issuetracker.google.com/issues/420443609))
- Make `NavigationEvent`'s `swipeEdge` an `@IntDef` ([Icee54](https://android-review.googlesource.com/#/q/Icee542915f6b4c5a37bd663caaec983417498349), [b/443950342](https://issuetracker.google.com/issues/443950342))
- Restrict `NavBackStack` serialization to Android. This prevents runtime failures on non-Android platforms. For multiplatform state saving, use the `rememberNavBackStack` overload with an explicit `SavedStateConfiguration`. ([I1e418](https://android-review.googlesource.com/#/q/I1e4183622beb615f3e2ad0a7b87ef2f42e127f62), [b/420443609](https://issuetracker.google.com/issues/420443609))

**Bug Fixes**

- Fix crash during predictive back when nested `NavDisplay` has a single child entry. ([I2cdc0](https://android-review.googlesource.com/#/q/I2cdc01c8f7fa73b96833520173cb618dfffac819), [b/441933162](https://issuetracker.google.com/issues/441933162))

### Version 1.0.0-alpha09

September 10, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/navigation3).

**API Changes**

- The `DecoratedNavEntryProvider` has been replaced with `rememberDecoratedNavEntries` that creates and return NavEntries decorated with the list of provided decorators ([I0fe1c](https://android-review.googlesource.com/#/q/I0fe1ce4618e337102a3daa01b5bca94a592dd6f8), [b/441328236](https://issuetracker.google.com/issues/441328236))
- `NavBackStack` is now generic over the `NavKey` type. This allows apps and libraries to define custom key types for their back stacks, rather than being restricted to `NavKey`. ([I4d190](https://android-review.googlesource.com/#/q/I4d19087dadab3a6796d15a067cac907597c76e11),[Iad2f4](https://android-review.googlesource.com/#/q/Iad2f46e30ac62e5367304cec20fa5ae3a657402e), [b/420443609](https://issuetracker.google.com/issues/420443609))
- `NavBackStack` is now `@kotlinx.serialization.Serializable`, making it possible to save and restore navigation state across process death and configuration changes without extra boilerplate. ([I2c3cf](https://android-review.googlesource.com/#/q/I2c3cfd6c6af1a7e46233e703ba86629bf5271634), [b/420443609](https://issuetracker.google.com/issues/420443609))
- `RememberNavBackStack` has been moved to `commonMain` to ensure it is provided on all platform targets. ([Id69e7](https://android-review.googlesource.com/#/q/Id69e75758ff2d6078dbd06cdecb1621b42607630), [b/420443609](https://issuetracker.google.com/issues/420443609))

**Bug Fixes**

- `NavDisplay` now correctly moves each individual `NavEntry` to the correct `Lifecycle.State`. ([I30aac](https://android-review.googlesource.com/#/q/I30aac4627d43c1a85f580887a4c36f1543a97e2c), [b/440145700](https://issuetracker.google.com/issues/440145700))
- Fixed an issue where `NavDisplay` would ignore any nested `NavigationEventDispatcherOwner` set via the `NavigationEvent` library's `LocalNavigationEventDispatcherOwner`. ([I6224a](https://android-review.googlesource.com/#/q/I6224a3448b71d2532bf5692e520ccaf540824b8f))

**Dependency Changes**

- Navigation3 now depends on [NavigationEvent Alpha08](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha08).

### Version 1.0.0-alpha08

August 27, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/navigation3).

**New Features**

- Added new Kotlin MultiPlatform (KMP) targets to `Navigation3 Runtime` artifacts. `Navigation3 Runtime` now supports the following platforms in total: JVM (Android and Desktop), Native (Linux, iOS, watchOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([I55078](https://android-review.googlesource.com/#/q/I550788ff38851e1fec7f44a687a1a69734374e4f), [b/424410398](https://issuetracker.google.com/issues/424410398), [b/419294028](https://issuetracker.google.com/issues/419294028), [b/419046226](https://issuetracker.google.com/issues/419046226)). Note: This does not provide KMP targets for `Navigation3 UI` artifact. On other platforms, you will need to implement your own custom `NavDisplay`. If you would like to see it supported, please vote on the Jetbrains issue [here](https://youtrack.jetbrains.com/issue/CMP-7646) and track the progress for additional support there.
- The `NavDisplayInfo` object is now public and can be used to retrieve the list of visible entries from the `NavDisplay`. ([Ibc91f](https://android-review.googlesource.com/#/q/Ibc91ff7504b0e26f9a1ccf43000b786cbf48b74d))

**API Changes**

- Added a new `NavBackStackSerializer` to be used in conjunction with `rememberNavBackStack` to perform state restoration. `rememberNavBackStack()` now also takes a [`SavedStateConfiguration`](https://developer.android.com/reference/androidx/savedstate/serialization/SavedStateConfiguration) that can be used to provide your own configuration. ([I2f4d2](https://android-review.googlesource.com/#/q/I2f4d2073eff82f88b476a9765a0e69729e77179e), [I4cd58](https://android-review.googlesource.com/#/q/I4cd58dca08625e7ecafac9f0a1e479e558604b7e), [b/420443609](https://issuetracker.google.com/issues/420443609))

**Bug Fixes**

- Fixed an issue where navigating would cause incorrect Lifecycle events to fire. ([I8bf6d](https://android-review.googlesource.com/#/q/I8bf6d9491c1bb242a8c2f195204a174f310b7f03), [b/425901162](https://issuetracker.google.com/issues/425901162), [b/434109022](https://issuetracker.google.com/issues/434109022))

**Known Issues**

- There was a bug introduced by [I8bf6d](https://android-review.googlesource.com/#/q/I8bf6d9491c1bb242a8c2f195204a174f310b7f03) that caused Lifecycles to be based on scenes instead of individual entries, which broke Lifecycle for any cases where the `key` provided to the `NavEntry` is not a `String` or your `NavEntry` has not overridden the `contentKey` and set it equal to the `key` (note that doing this enforces that your key can be saved into a `Bundle`). This has been fixed for the next release. ([b/440145700](https://issuetracker.google.com/issues/440145700))

### Version 1.0.0-alpha07

August 13, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b4562c71af5649ad7262ba4c7925899e6e93bdff..c359e97fece91f3767a7d017e9def23c7caf1f53/navigation3).

**MinSdk Update**

- The default minSdk for the AndroidX has been moved from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

**API Changes**

- `SavedStateNavEntryDecorator` now uses the `SaveableStateRegistry` built into `SaveableStateProvider` to save and restore states. ([If8d9a](https://android-review.googlesource.com/#/q/If8d9aebde301f51faa78d4b1f471cf9f7d87f9cb))
- The `predictivePopTransitionSpec` is now provided the swipe edge as a parameter, allowing you to customize the transition based on what edge the user started the Predictive Back gesture from. ([I753a8](https://android-review.googlesource.com/#/q/I753a8ba909347f89506006f66aca23298b2e3237))

**Bug Fixes**

- Fixed an issue that would cause custom scenes to be infinitely recalculated because the most recent scene was not being remembered. ([I7ba84](https://android-review.googlesource.com/#/q/I7ba84a56fe1cfd4f006c9b6c4c3e91b44a2bb2a5), [b/418153031](https://issuetracker.google.com/issues/418153031))

**Dependency update**

- Navigation3 now depends on [Navigation Event `1.0.0-alpha06`](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/navigationevent#1.0.0-alpha06).

### Version 1.0.0-alpha06

July 30, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c920d69612c07600c8d244ef8fe3df5ec775da88..b4562c71af5649ad7262ba4c7925899e6e93bdff/navigation3).

**Dependency Update**

- Navigation3 now depends on [Navigation Event `1.0.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.0-alpha05).

### Version 1.0.0-alpha05

July 2, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..c920d69612c07600c8d244ef8fe3df5ec775da88/navigation3).

**Behavior Changes**

- The `NavEntry`'s state is now strictly based on the current list of decorators passed to the `NavDisplay`. This means that decorators should be swapped along your back stacks in the case of multiple back stacks in order to preserve the state of the NavEntries on the back stack. Otherwise, the states will be cleared as if the entries were popped (instead of a swap). ([I7a759](https://android-review.googlesource.com/#/q/I7a759e37580404cf9c3a35b1c2a8f18b3d20646e), [b/428033667](https://issuetracker.google.com/issues/428033667))

### Version 1.0.0-alpha04

June 18, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4fb12d1b1dc4dcae8ca603c7a5db938cc1abe39c..b454ea392cd18cccb078ef60a3221719164f7bbc/navigation3).

**API Changes**

- `NavEntry.content` is now private. To invoke `NavEntry` content, call the new `NavEntry.Content()` api which no longer requires a `key` parameter to invoke. ([Icd0fd](https://android-review.googlesource.com/#/q/Icd0fd2244c3d29557b0803ef2abb199c18cbdbdc), [b/420991203](https://issuetracker.google.com/issues/420991203))
- `NavEntry.key` is now a private field. The `NavEntry` and its relevant states should be identified by the new `contentKey` field which is generated from the new `contentKeyFactory` lambda and defaults to a saveable hash generated from `NavEntry.key` ([I81a6c](https://android-review.googlesource.com/#/q/I81a6ced3a7bebf561c7206fcdf9402bc80c12752), [b/422001357](https://issuetracker.google.com/issues/422001357), [b/420991203](https://issuetracker.google.com/issues/420991203) [I2d7d4](https://android-review.googlesource.com/#/q/I2d7d4daba257e19bc9abe5ea64540126af18adf0), [b/420991203](https://issuetracker.google.com/issues/420991203), [b/422841812](https://issuetracker.google.com/issues/422841812))

**Dependency Changes**

- Navigation3 now depends on the new `androidx.navigationevent.compose` artifact.

### Version 1.0.0-alpha03

June 4, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3db836162afb266b54eb37d28c7c12231755fc9b..4fb12d1b1dc4dcae8ca603c7a5db938cc1abe39c/navigation3).

**Bug Fixes**

- `Navigation3` will no longer clear decorator states for `backStacks` that have been swapped out and replaced with another `backStack` instance. ([I28a42](https://android-review.googlesource.com/#/q/I28a42b98cc811be99d8380b1cfceee02b42608ab), [b/415076044](https://issuetracker.google.com/issues/415076044))

### Version 1.0.0-alpha02

May 23, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c211305886d70caa42620facce1b97ed7e47bf5..3db836162afb266b54eb37d28c7c12231755fc9b/navigation3).

**Bug Fixes**

- Fixed an issue with the `SavedStateNavEntryDecorator` which caused collisions for different data classes with the same property values. ([b/418070648](https://issuetracker.google.com/418070648), [Iff4775](https://android-review.googlesource.com/#/q/Iff47751d5de26bfee744069461cee38419988699))
- Fixed a missing class issue that would cause crashes when running without declaring explicit dependencies. ([b/419049149](https://issuetracker.google.com/419049149), [I4b4ed](https://android-review.googlesource.com/#/q/I4b4edbf046a62164e56e1871ca9918d9683a2abf))

### Version 1.0.0-alpha01

May 20, 2025

`androidx.navigation3:navigation3-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c211305886d70caa42620facce1b97ed7e47bf5/navigation3).

**New Features**

[Navigation3](https://developer.android.com/guide/navigation/navigation-3) is a new navigation library built specifically to handle Jetpack Compose in-app navigation. The `androidx.navigation3.runtime` artifact provides the building blocks, while the `androidx.navigation3.ui` artifact provides the UI layer via the `NavDisplay` API. Developers can provide their own state directly to the `NavDisplay` composable function, which changes the content based on changes in the developer state.

    @Serialiable object Home : NavKey
    @Serialiable object Chat : NavKey

    val backStack = rememberNavBackStack(Home)

    NavDisplay(backStack, entryProvider = entryProvider {
      entry<Home> {
        Column {
          Text("Home")
          Button(onClick = { backStack.add(Chat) } ) {
            Text("Go to Chat")
          } 
        }
      }
      entry<Chat> { /* My Composable Content */ }
    })

For more information, see the [Navigation3 guide](http://goo.gle/nav3).