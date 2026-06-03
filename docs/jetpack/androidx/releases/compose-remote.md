---
title: https://developer.android.com/jetpack/androidx/releases/compose-remote
url: https://developer.android.com/jetpack/androidx/releases/compose-remote
source: md.txt
---

# remote compose

Remote Compose is a framework to create UI for remote surfaces

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| May 19, 2026 | - | - | - | [1.0.0-alpha11](https://developer.android.com/jetpack/androidx/releases/compose-remote#1.0.0-alpha11) |

## Declaring dependencies

To add a dependency on compose-remote, you must add the Google Maven repository to your
project. Read
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.remote:remote-core:1.0.0-alpha11"

    // Use to create Remote Compose documents
    implementation "androidx.compose.remote:remote-creation:1.0.0-alpha11"
    implementation "androidx.compose.remote:remote-creation-core:1.0.0-alpha11"
    implementation "androidx.compose.remote:remote-creation-android:1.0.0-alpha11"
    implementation "androidx.compose.remote:remote-creation-jvm:1.0.0-alpha11"
    implementation "androidx.compose.remote:remote-creation-compose:1.0.0-alpha11"

    // Use to render a Remote Compose document
    implementation "androidx.compose.remote:remote-player-core:1.0.0-alpha11"
    implementation "androidx.compose.remote:remote-player-view:1.0.0-alpha11"

    implementation "androidx.compose.remote:remote-tooling-preview:1.0.0-alpha11"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.remote:remote-core:1.0.0-alpha11")

    // Use to create Remote Compose documents
    implementation("androidx.compose.remote:remote-creation:1.0.0-alpha11")
    implementation("androidx.compose.remote:remote-creation-core:1.0.0-alpha11")
    implementation("androidx.compose.remote:remote-creation-android:1.0.0-alpha11")
    implementation("androidx.compose.remote:remote-creation-jvm:1.0.0-alpha11")
    implementation("androidx.compose.remote:remote-creation-compose:1.0.0-alpha11")

    // Use to render a Remote Compose document
    implementation("androidx.compose.remote:remote-player-core:1.0.0-alpha11")
    implementation("androidx.compose.remote:remote-player-view:1.0.0-alpha11")

    implementation("androidx.compose.remote:remote-tooling-preview:1.0.0-alpha11")
}
```

For more information about dependencies, see
[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1984647+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1984647&template=2233909)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha11

May 19, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e29a10982f4299b1fa812e229d76792092a62814..b5d2acb5ad0a36c9d2aba8feb4c7951165f30fbe/compose/remote).

**API Changes**

- Expose `RemoteInt` static factory. ([Ic0096](https://android-review.googlesource.com/#/q/Ic009609d00b699eabc71f96bc49df7c5fa481123), [b/484137042](https://issuetracker.google.com/issues/484137042))
- Expose `RemoteState` static factories ([I544f0](https://android-review.googlesource.com/#/q/I544f0fc816ce073606a98911261876de43e76cd1), [b/484137042](https://issuetracker.google.com/issues/484137042))
- `RemoteLong` now supports a limited subset of arithmetic operators (addition, subtraction, multiplication and a truncating conversion to `RemoteInt`). ([I1d416](https://android-review.googlesource.com/#/q/I1d41634d0e1107ed87593e45de59d53c2cab0a5f))
- Update `RemoteText` to use `RemoteFontFamily` instead of `FontFamily` ([Ib76b6](https://android-review.googlesource.com/#/q/Ib76b66464b97b40f914639aef783a3e26a6a6964), [b/502907551](https://issuetracker.google.com/issues/502907551))
- Modifiers alpha, rotate and scale were added. ([I5d682](https://android-review.googlesource.com/#/q/I5d682270235fa1f9f656d6ad1d43ca56660c70f2), [b/505427444](https://issuetracker.google.com/issues/505427444))

### Version 1.0.0-alpha010

May 06, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha010` is released. Version 1.0.0-alpha010 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/df4b49eda6f6834b6bc4c8aa30a581fa577a511e..5ec3fd7563f4f9b2ba745aac0ad7770cc4cd087f/compose/remote).

**Features**

- Add `EnforceCleanRecomposition` flag ([I6e4408](https://android-review.googlesource.com/#/q/I6e440881d4de7ef752442b23f4b12f6ffd6b43f0)). As a step towards supporting recomposition in `RemoteCompose`, we have prevented anything from writing to the document before the composition has finished. This prevents documents from being partially written during recomposition. If this behavior causes issues with existing code, it can be disabled by setting `isEnforceCleanRecompositionEnabled` to `false`.

**API Changes**

- A testing library for Remote Compose is added. ([I78746](https://android-review.googlesource.com/#/q/I78746942783763478acff95ea9d635368b22e4f5), [b/504687418](https://issuetracker.google.com/issues/504687418))

**Bug Fixes**

- Fix background clipping when using a `RemoteColor` (instead of static color) as the background color ([If70842](https://android-review.googlesource.com/#/q/If708420fcc1d160ca4fbdc0a4e856e2d6a6a6964), [b/505116577](https://issuetracker.google.com/issues/505116577))
- Support providing an explicit size for bitmaps loaded from URI. Previously the size would be calculated as 1x1, and that pixel would be scaled to the container size ([Id4fff](https://android-review.googlesource.com/#/q/Id4fff053338a3746406ba8cdf9e48c3797e8da2f), [b/487936996](https://issuetracker.google.com/issues/487936996))
- Prevent crash bug on devices that don't have `SensorManager` ([I1fc947](https://android-review.googlesource.com/#/q/I1fc9477f982831193ca5d8f29b60c97a52842472),[b/498302479](https://issuetracker.google.com/issues/498302479))
- Fix `TIME_FROM` expressions not using the provided clock (preventing reliable tests for duration expressions) ([I5f816](https://android-review.googlesource.com/#/q/I5f81682686005816b1668c475df9cac010dc461d), [b/501405389](https://issuetracker.google.com/issues/501405389))

### Version 1.0.0-alpha09

April 22, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/951845221205b7a428a9d779107760fc929863ee..fa102f7428ce722bf997f7388ba3e80223f1db3c/compose/remote).

**API Changes**

- Modifier clickable changed to not accept null value for action parameter. Action.Empty should be used instead. ([I21be9](https://android-review.googlesource.com/#/q/I21be9ccd0c402e176cbb5998ba4e73b76851d4d8), [b/498881738](https://issuetracker.google.com/issues/498881738))
- Padding modifier parameters were changed from left/right to start/end. ([Id781c](https://android-review.googlesource.com/#/q/Id781cdd4c631488e0934555dcbbb0d7c54989741), [b/500760020](https://issuetracker.google.com/issues/500760020))
- Modifier `onTouchDown(varargs action)` and `onTouchUp(varargs action)` were changed to `onTouchDown/onTouchUp(action)`. Use `CombinedAction` for a list of actions. ([I8af9d](https://android-review.googlesource.com/#/q/I8af9d304b14795ec579527b7d636c923378763bb), [b/498881738](https://issuetracker.google.com/issues/498881738))
- Modifier `clickable(varargs action)` was changed to `clickable(action)`. Use `CombinedAction` for a list of actions. ([I8432d](https://android-review.googlesource.com/#/q/I8432da06a6ca0c39c297cc6f65bf4b4d67967630), [b/498881738](https://issuetracker.google.com/issues/498881738))

**Bug Fixes**

- Fix `MatrixExpression.write` ([Id3c52](https://android-review.googlesource.com/#/q/Id3c52536a1a746d7577e7fa1d129eb3949b11722))

### Version 1.0.0-alpha08

April 08, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4f1927c2c3b66d0c3a6b9118974d818d2dc5a06a..f1f39f6b54f6a8f12b26c7dae6526eb225d8c805/compose/remote).

**New Features**

- Promote the `CoreText`, `TextStyle`, `TextTransform` and `ColorTheme` Operations to the baseline AndroidX and Widgets Profiles ([I69671](https://android-review.googlesource.com/#/q/I69671b3aff85e495b61d9e162db1077abcb783cf), [b/494482597](https://issuetracker.google.com/issues/494482597))
  - `CoreText` provides richer capabilities for rendering text, including adaptive text resizing, and improved control over text layout features like line breaking and overflow behavior.
  - `TextStyle` allows common text styling attributes to be captured in the document once, and referenced by multiple text runs.
  - `TextTransform` enables text transformations - for example, uppercasing text.
- Reverse rendering of items in horizontal layout when layout direction is RTL and not using Absolute horizontal arrangement. ([I2d38e](https://android-review.googlesource.com/#/q/I2d38e8a6a2b1cb39b7251afd77ffead21c807c75))

**API Changes**

- Prefer `toRemoteString(DecimalFormat)` as the developer API. ([Ia4925](https://android-review.googlesource.com/#/q/Ia49252351b49f0ee3ad1622f6cbd5908d408dad7), [b/493924433](https://issuetracker.google.com/issues/493924433))
- Modifier `clip(shape, size)` was removed. Modifier `clip(shape)` should be used instead. ([I76301](https://android-review.googlesource.com/#/q/I76301e0330583ab49e051a7e51482ae298de92a2))

**Bug Fixes**

- Update `TextLookup` to track array element changes. This ensures that expressions will be reevaluated if an element they look up in an array has changed ([I162c7](https://android-review.googlesource.com/#/q/I162c73eb1562dbbb6568abd320ac3201a763c9dc))

### Version 1.0.0-alpha07

March 25, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a508f033de883ba2853b9f9ae1853eec7010638..cef2ecc0ae575dbc48d99750710fd5b7aec1f8ba/compose/remote).

**New Features**

- Implement non-linear font scaling ([73b23c0](https://android-review.googlesource.com/#/q/73b23c0f3122c2a51ef13763c2bf13dd34f3df54))
- Make layouts aware of `LayoutDirection` ([81f984b](https://android-review.googlesource.com/#/q/81f984bd9616fe40b17ab64c26be238477ff7489))

**API Changes**

- Expose `RemoteSpacer` as public API ([I1a540](https://android-review.googlesource.com/#/q/I1a5408204bd804b725c2a0135f0afc19fbaf6649))
- Make `RemoteBrush` `applyTo` and typeface API public ([I87ce9](https://android-review.googlesource.com/#/q/I87ce999db9c9f25067dbebe5496a0a624481141f), [b/493249631](https://issuetracker.google.com/issues/493249631))
- Omit alignment and placement parameters from `drawTextOnCircle` ([I7fd16](https://android-review.googlesource.com/#/q/I7fd16219208da609750747ed62d4d6997722cf18), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose semantics modifier functions ([Ice73b](https://android-review.googlesource.com/#/q/Ice73b23ac5a078903c163531891631ac3e6b8034))
- Expose `RemoteImageVector` and `painterRemoteVector` ([If8f38](https://android-review.googlesource.com/#/q/If8f3812874e92db7ee2186545ed8d6e4a33a24c1), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemoteTimeDefaults` as a public API in `remote-creation-compose` ([Iddc74](https://android-review.googlesource.com/#/q/Iddc7465ef1508099c629141b9290482a665f60ef), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Make `RemoteArrangement.spacedBy` methods public ([I36e86](https://android-review.googlesource.com/#/q/I36e86045bc31807cfe57dbb7f1b72cbf07033a8e))
- Expose more `RemoteDrawScope` API ([I1dde7](https://android-review.googlesource.com/#/q/I1dde7631d93a84b899cf03d217673449dbe70ea4))
- Expose `RemotePainter` types in API ([I1ec8e](https://android-review.googlesource.com/#/q/I1ec8e43cf0262efce24549257f56cbda3daa2fbd))
- Expose `RemoteBrush` API ([I4b074](https://android-review.googlesource.com/#/q/I4b0741cf3abcea0861f4123783f42acb1daf1ffa))
- Minimal public API for `RemoteCanvas` ([I00853](https://android-review.googlesource.com/#/q/I008533c52d0d2bc4306c27a9d5bc1ea07be71b4c), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose RC semantics Modifiers ([I8b175](https://android-review.googlesource.com/#/q/I8b175b970612fdc639bcf1e39f31e056bf702315), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemoteFloat.asRemoteDp()` ([I28b36](https://android-review.googlesource.com/#/q/I28b361187b51f6b0b15a5223cd7af98f50270da0), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemoteFloat` operations ([I85fb5](https://android-review.googlesource.com/#/q/I85fb5db1d481753f137b13f601493711a0994ed6), [b/446824085](https://issuetracker.google.com/issues/446824085))
- `RemoteArrangement.CenterHorizontally` was removed and is replaced by `RemoteArrangement.Center`. ([I2f907](https://android-review.googlesource.com/#/q/I2f9077cb5bf0947e80b28ba6a04744d239199d0f), [b/471212869](https://issuetracker.google.com/issues/471212869), [b/471153933](https://issuetracker.google.com/issues/471153933))
- Change `RemoteBox` alignment to accept a single `RemoteAlignment`. ([I0bfbf](https://android-review.googlesource.com/#/q/I0bfbf28c95045d517cdd1bd99377895fbca0a376), [b/471212869](https://issuetracker.google.com/issues/471212869))

### Version 1.0.0-alpha06

March 11, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c129dd3005b507bbf2c535f70d7329ed14d6804b..1a508f033de883ba2853b9f9ae1853eec7010638/compose/remote).

**New Features**

- Add a new experimental operation for `TextStyle`. `TextStyle` enables commonly used typography styling to be written to the document once, and reused by several text runs ([bfc6487](https://android-review.googlesource.com/#/q/Iee502480ea5a68e0021e777028f77230ee473d0c))

**API Changes**

- Expose `RemoteTextStyle` merge ([I971ce](https://android-review.googlesource.com/#/q/I971cef03b78c66e2cb9577b04081c0e878bd5315), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemotePainter` as public API ([I252c1](https://android-review.googlesource.com/#/q/I252c112a5379185b30116f523726941eacc23123), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `Border/Clip` Modifiers and `RemoteShape`. ([Id26dd](https://android-review.googlesource.com/#/q/Id26dd4c3ac5617ce391b71a8eb6a70c7712c30d7), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemoteColor` APIs in `remote-creation-compose` ([I4ab00](https://android-review.googlesource.com/#/q/I4ab002dc1de755cb3284ef0fe1f2c047d605bb9d), [b/446824085](https://issuetracker.google.com/issues/446824085))
- Expose `RemoteText` API ([I6b019](https://android-review.googlesource.com/#/q/I6b019c35f925af55d13ea32f7cc6e34ee19388e0))
- Expose `RemoteImage` API ([Ided31](https://android-review.googlesource.com/#/q/Ided3150fdcf6fada8f0f9e019421a733421be30f))
- Expose `RemoteBoolean`, `RemoteString`, and `RemoteFloat` APIs ([Id9ee6](https://android-review.googlesource.com/#/q/Id9ee6a32db042b4dfde15e26bde8fd333488e2e6))
- Remote Composable from `WidthIn` annotation ([I80784](https://android-review.googlesource.com/#/q/I8078494aa5de54d000d97f9b40e076c72454ac56))

**Bug Fixes**

- Moves libraries to use Java 11 target. This means produced bytecode will be Java 11 (class file version 55) and might require desugaring to use the library ([If4c2a](https://android-review.googlesource.com/#/q/If4c2a6fdda1278f42ea080fa365e8b437b2c2ae6), [b/457821470](https://issuetracker.google.com/issues/457821470))
  - Ensure length and textlookup update correctly. Previously the length of `RemoteStrings` would be calculated on the first frame, and not updated afterwards ([e49cb53](https://android-review.googlesource.com/#/q/I04122ee502170ae46aee4b83cbe4aa5669fe14a1))
  - Support `TextFromFloat` for numbers with large fractional components. Previously large "digitsAfter" values could result in the float evaluating to 0 ([5080bc54](https://android-review.googlesource.com/#/q/Ib4f9819a138824a4dc88b524f32bbc1d152da78b))

### Version 1.0.0-alpha05

February 25, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdf076c6abd0f3125cb0302756fcb77fe981ab7c..c129dd3005b507bbf2c535f70d7329ed14d6804b/compose/remote).

**New Features**

- Introduced `fillParentMaxWidth` and `fillParentMaxHeight`. ([4c6d77c](https://android-review.googlesource.com/#/q/I13a63fdcd07bb44e3b78072bc98889e133656a2d))

**API Changes**

- Expose common Remote Composable and Modifier types ([Id1d40](https://android-review.googlesource.com/#/q/Id1d40acae7af63f9acb99438adaa992035fd3c01))
- Expose types for `RemoteState` ([I22429](https://android-review.googlesource.com/#/q/I22429108472ff50e5694c80f1e4c42c4009cea61), [b/465453482](https://issuetracker.google.com/issues/465453482))

**Bug Fixes**

- Fixes for scrolling ([0a25299](https://android-review.googlesource.com/#/q/Iaee130c182a8c66604bdc006329add5f705cb77f))
- Fixes for touch slop ([0192b69](https://android-review.googlesource.com/#/q/I43622c0b1565fdbe113a3b826ac780e7dd2ac732))
- Set density earlier in the rendering process, so it is applied correctly on the first frame (often captured in screenshot tests) ([f775399](https://android-review.googlesource.com/#/q/Id590ac87459094cbd90c49fd2c7f96459e92a93c))

### Version 1.0.0-alpha04

February 11, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/compose/remote).

**New Features**

- Enable using the `RemoteApplier` by default, which prevents using non-Remote Composable functions when creating a Remote UI. This can be disabled by changing `isRemoteApplierEnabled` in `RemoteComposeCreationComposeFlags`. ([67a405f](https://android-review.googlesource.com/#/q/I10b57b6fee4d9f3cba75be4cab6976123a8c347e))
- Add Glyph spacing for bitmap fonts ([0852657](https://android-review.googlesource.com/#/q/I96311972f59b562c44845860e67c39c8346a826d))
- Rotate with pivot in `RemoteCanvas` ([9a292b3](https://android-review.googlesource.com/#/q/I96311972f59b562c44845860e67c39c8346a826d))
- Add `RemoteSpacer` ([12beb72](https://android-review.googlesource.com/#/q/I603e0995d933a68220fd72b595a42c98329db31a))
- Avoid `java.time` dependency, allowing the `minSdk` of the creation libraries to be lowered to 23 ([59e30d0](https://android-review.googlesource.com/#/q/I7edfc82475f2472673844d9eb5ca0a5214518e2f))
- `FlowLayout` ([7efef02](https://android-review.googlesource.com/#/q/I176532d6d4bddfcf360787f83dcef4b3f0833ef8))

**Bug Fixes**

- Fix evaluation for non global `ColorExpression` and computed String. ([c08d0bd](https://android-review.googlesource.com/#/q/I2085fcf66281fe05f2c37140786c614902ca03d5))

**External Contribution**

- `androidx.compose.ui.graphics.NativePaint` typealias is deprecated, use `android.graphics.Paint` directly instead ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))
- Replace `Paint.asFrameworkPaint()` to `Paint.nativePaint` extension to avoid exposing platform type into `commonMain` sourceset via `typealias` ([I6303c](https://android-review.googlesource.com/#/q/I6303c742f80887649d1a77e837ab0ff93ddff212), [b/477394763](https://issuetracker.google.com/issues/477394763))

### Version 1.0.0-alpha03

January 28, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8ae214f288619313e8689cd4ab8286c7705c1000..715e22619094effc2ba1fd528cd9a07b1f5d0046/compose/remote).

**New Features**

- Support for different shapes \& `RemoteColors` in `BorderModifier` [0afd343](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3914200)
- Add `CombinedAction` to support multiple actions on click events [10e16a2](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3908363)

**API Changes**

- Migrated the APIs of `RemoteColor` and `RemoteBitmap` to use Compose types, rather than exposing Android types directly [a9bfbb8](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3917393)
- Introduce a `RemoteDensity` type, to allow determining whether to evaluate Density on the Player (when producing a document for a remote device), or to inline the expressions (to optimize document size when on the same device) [54352bb](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3914002)
- `RemoteState constantValueOrNull` rename ([I6ad5c](https://android-review.googlesource.com/#/q/I6ad5caf6e8af50642e3a7696ae7ceeefce89f11f), [b/467050397](https://issuetracker.google.com/issues/467050397))

### Version 1.0.0-alpha02

January 14, 2026

`androidx.compose.remote:remote-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..8ae214f288619313e8689cd4ab8286c7705c1000/compose/remote).

**New Features**

- Add min/max font size for CoreText. [I7bd3c](https://android-review.git.corp.google.com/#/q/I7bd3cbacdfcb70b62feada52cc74ff4853360775)

**API Changes**

- Expose minimal public API for Glance Wear infra. ([I7b4b9](https://android-review.googlesource.com/#/q/I7b4b99bb71b0b874acfbb77cbec7e7ec2eb85403), [b/467532762](https://issuetracker.google.com/issues/467532762))
- Return `CapturedDocument` from `captureSingleRemoteDocument` ([I5a283](https://android-review.googlesource.com/#/q/I5a2832bcd1eb4b54e82a413452d1146565925b81), [b/467532762](https://issuetracker.google.com/issues/467532762))

**Bug Fixes**

- Fix scrolling position after relayout + add support for edge effects ([6d4551](https://android-review.git.corp.google.com/#/q/I5c2d35e07c193d7b147753387eb1d47cc0765be9))

### Version 1.0.0-alpha01

December 17, 2025

`androidx.compose.remote:remote-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3/compose/remote).

- Remote Compose is a framework to create UI for remote surfaces.