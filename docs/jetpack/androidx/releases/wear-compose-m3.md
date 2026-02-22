---
title: https://developer.android.com/jetpack/androidx/releases/wear-compose-m3
url: https://developer.android.com/jetpack/androidx/releases/wear-compose-m3
source: md.txt
---

<br />

# Wear Compose Material 3

API Reference  
[androidx.wear.compose.material3](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary)  
Write Jetpack Compose applications for Wear OS devices by providing functionality to support different device sizes and navigation gestures using the Material 3 Expressive design system.  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| August 27, 2025 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/wear-compose#1.5.0) | - | - | - |

| **Note:** This library supersedes the `androidx.wear.compose:compose-material` library. This library implements Material 3 Expressive design for Wear OS and is recommended for developers to use. Don't mix objects from this library with objects in the [Compose Material 3](https://developer.android.com/jetpack/androidx/releases/compose-material3) mobile library.

## Declaring dependencies

To add a dependency on Wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.wear.compose:compose-foundation:1.5.0"

    // For Wear Material Design UX guidelines and specifications
    implementation "androidx.wear.compose:compose-material3:1.5.0"

    // For integration between Wear Compose and Androidx Navigation libraries
    implementation "androidx.wear.compose:compose-navigation:1.5.0"

    // For Wear preview annotations
    implementation("androidx.wear.compose:compose-ui-tooling:1.5.0")
    
    // NOTE: DO NOT INCLUDE dependencies on androidx.wear.compose:compose-material
    // or androidx.compose.material:material.
    // androidx.wear.compose:compose-material3 is designed as a replacement,
    // not an addition, to both of these other libraries.
    // If there are features from that you feel are missing from
    // androidx.wear.compose:compose-material3, please raise a bug to let us know.
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.wear.compose:compose-foundation:1.5.0")

    // For Wear Material Design UX guidelines and specifications
    implementation("androidx.wear.compose:compose-material3:1.5.0")

    // For integration between Wear Compose and Androidx Navigation libraries
    implementation("androidx.wear.compose:compose-navigation:1.5.0")
    
    // For Wear preview annotations
    implementation("androidx.wear.compose:compose-ui-tooling:1.5.0")

    // NOTE: DO NOT INCLUDE dependencies on androidx.wear.compose:compose-material
    // or androidx.compose.material:material.
    // androidx.wear.compose:compose-material3 is designed as a replacement,
    // not an addition, to both of these other libraries.
    // If there are features from that you feel are missing from
    // androidx.wear.compose:compose-material3, please raise a bug to let us know.
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1077552+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1077552&template=1598429)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

<br />

## Wear Compose Material3 Version 1.5

### Version 1.5.0

August 27, 2025

`androidx.wear.compose:compose-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9bb311be04ba2343c1638d5cb466dd6c8ac83a0c..ac0232628e5809ea2a906b356273e36e7c734bd5/wear/compose).

**Important changes since 1.4.0**

First release of the Wear Compose Material 3 library, which supports the new Material 3 Expressive design system. This release includes:

- Updated `MaterialTheme` and dynamic color theming.
- New `AppScaffold, ScreenScaffold`, `HorizontalPagerScaffold`, and `VerticalPagerScaffold` components to lay out the structure of the screen and coordinate `ScrollIndicator`,`TimeText`,`HorizontalPageIndicator`, and `VerticalPageIndicator` animations.
- Shape morphing `IconButton`, `TextButton`, `IconToggleButton`, and `TextToggleButton`, with variations that animate when pressed or checked.
- `EdgeButton`, which has a special shape designed for the bottom of the screen.
- `ButtonGroup` implements an expressive group of buttons, in a row that shape-morphs when touched.
- `AlertDialog` and `ConfirmationDialog` with variations for additional dialog content.
- `TimePicker` and `DatePicker` components.
- Progress indicators include `CircularProgressIndicator` (with segmented variation), `ArcProgressIndicator`, and `LinearProgressIndicator`.

In addition, Wear Compose Foundation 1.5.0 includes the following:

- `TransformingLazyColumn`, a lazy, vertically scrolling list that supports scaling and morphing animations.
- Support for paging in Wear Compose Foundation with `HorizontalPager` and `VerticalPager`.
- Hierarchical Focus Groups - used to annotate composables in an application to keep track of the active part of the composition and coordinate focus.

Read about more about ([Material 3 Expressive for Wear OS](https://android-developers.googleblog.com/2025/08/introducing-material-3-expressive-for-wear-os.html))

### Version 1.5.0-rc02

August 13, 2025

`androidx.wear.compose:compose-*:1.5.0-rc02` is released. Version 1.5.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/28fb1203e01e0641625f00bce1005f140dd5c198..9bb311be04ba2343c1638d5cb466dd6c8ac83a0c/wear/compose).

**Bug Fixes**

- Fixed a bug in `TimePicker` where long, internationalised strings for the period (AM/PM) could break the layout. ([I0fa81](https://android-review.googlesource.com/#/q/I0fa81d6d1bc0ea9c3f222f8be07247f71e9d7bf7))

### Version 1.5.0-rc01

July 30, 2025

`androidx.wear.compose:compose-*:1.5.0-rc01` is released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..28fb1203e01e0641625f00bce1005f140dd5c198/wear/compose).

**Bug Fixes**

- `TimePicker` is now fully driven by the user's locale, using `DateFormat.getBestDateTimePattern` to determine the order and content of its pickers and separators. This fixes incorrect column ordering for CJK languages, resolves RTL layout issues in languages like Arabic, uses localized separators, and supports both 0-11 and 1-12 hour formats based on the locale ([I5d543](https://android-review.googlesource.com/#/q/I5d5437ecd195af1c0306f8d06554a700153d6d34))
- `DatePicker` now displays a numeric month in some locales, such as CJK, to avoid mixing numeric and linguistic formats (e.g., 2025 \| 07 \| 02 instead of 2025 \| 7月 \| 02). This change applies a heuristic that checks if the locale uses linguistic suffixes for the year and, if so, switches the month format from textual (MMM) to numeric (MM) for consistency. ([Ia93fe](https://android-review.googlesource.com/#/q/Ia93fe26435d110c341074108ba73dc11a8343834))
- The vertical space for the heading in the Picker component is now constant, preventing a visible shift when a picker column is selected, especially in `Talkback` mode. ([I7f8b7](https://android-review.googlesource.com/#/q/I7f8b76d8a59c88e20dc96248ec30f3b8aa4f1494))
- Fixed an accessibility bug caused by `HorizontalPageIndicator` and `VerticalPageIndicator` being drawn full screen. The page indicators are no longer full-screen, and will be positioned automatically when used with `HorizontalPagerScaffold` or `VerticalPagerScaffold`. When not using a pager scaffold, specify the alignment explicitly using `modifier = Modifier.align(Alignment.BottomCenter)` with `HorizontalPageIndicator` and `modifier =Modifier.align(Alignment.CenterEnd)` with `VerticalPageIndicator`. ([I3a0ad](https://android-review.googlesource.com/#/q/I3a0ad217842220f2b14b02264750ab0d9a5da1da))
- The swipe direction in `SwipeToReveal` is now consistent for both LTR and RTL `LayoutDirections`. ([I6d427](https://android-review.googlesource.com/#/q/I6d42771b5865d6fe51cfc1954baef581584d7a4a))
- Reinstated `SwipeToReveal` vertical centering for actions. If `hasPartiallyRevealedState = true`, `RevealState` should be reset to `RevealValue.Covered` by the caller when scrolling occurs. ([I6473d](https://android-review.googlesource.com/#/q/I6473d355cbf845fb4e707e4004a9dc6c3f07a485))
- `SwipeDismissableNavHost` now correctly clips content for API 36 onwards. ([Ib9a44](https://android-review.googlesource.com/#/q/Ib9a444c322e2e2d8e742f578a47967a4cbcc2ffb))

### Version 1.5.0-beta06

July 16, 2025

`androidx.wear.compose:compose-*:1.5.0-beta06` is released. Version 1.5.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/wear/compose).

**Bug Fixes**

- Fix `EdgeButton` animation when `LazyColumn` or `ScalingLazyColumn` have `reverseLayout = true`. ([I46a1a](https://android-review.googlesource.com/#/q/I46a1a10fde27a640469d8712fbf6893293507b08))
- Fixed a bug in `ScreenScaffold` where touch-to-explore was not working under Talkback if a `ScrollIndicator/PageIndicator` was provided. ([I6dcee](https://android-review.googlesource.com/#/q/I6dcee875e99665133102526ddbed79b60c4562b0))
- `TransformingLazyColumn` now allows for custom morphing from `TransformationSpec` by reading `itemHeight` value provided by `TransformationSpec` in the background painter. ([I6a599](https://android-review.googlesource.com/#/q/I6a5998e29f2394a79c77d81a2c3f9d61ae5c3c6c))
- Animated enabled/disabled color transitions for `IconButton`, to be consistent with `IconToggleButton`. ([Ife10a](https://android-review.googlesource.com/#/q/Ife10ab316ba981d305782a210767a54a2c4c3b76))
- Removed the minimum section clamping in `CircularProgressIndicator` to avoid a noticeable jump to the minimum dot size when animating. As part of this change, the `targetProgress` parameter in `drawCircularProgressIndicator` is now unused. ([I33309](https://android-review.googlesource.com/#/q/I333099e618dba74a4ead2dafafa3793e216c2306))
- Picker now has the semantic role `ValuePicker` which can be used by screen readers to make pickers more accessible. Picker also has updated accessibility click labels which differentiate between adjusting the value in read-only mode and selecting the current value otherwise. ([I33309](https://android-review.googlesource.com/#/q/I333099e618dba74a4ead2dafafa3793e216c2306))

### Version 1.5.0-beta05

July 2, 2025

`androidx.wear.compose:compose-*:1.5.0-beta05` is released. Version 1.5.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..1b437892629a2cdedb46d9b7232575987b2cc6b5/wear/compose).

**Bug Fixes**

- Updated the documentation to clarify usage of `Modifier.edgeSwipeToDismiss` ([I78cb5](https://android-review.googlesource.com/#/q/I78cb5ec2bdc7cb20e955d97dbc6d465fc1523074))
- Addressed bug where multiple revealed items could be shown with `SwipeToReveal` in lazy lists ([I1d4f6](https://android-review.googlesource.com/#/q/I1d4f68415a7f96e5bccc8619f447867a6e97f60a))
- Container shapes in `TransformingLazyColumn` are now scaled, in order to avoid clipping the contents. ([I9221a](https://android-review.googlesource.com/#/q/I9221a2976ef58f6656077fe023b277760365bbd5))
- The `TimePicker` and `DatePicker` label for hour/minute/second or year/month/day now has heading semantics for screen readers ([I77d8b](https://android-review.googlesource.com/#/q/I77d8b950fe9adf767f202c37b96bc8c0c2ec0c0d))
- Removed the pause between loops in the indeterminate `CircularProgressIndicator` ([Iaf0bb](https://android-review.googlesource.com/#/q/Iaf0bb3a7202936972cf249400bafdf979e94e39c))
- Fixed an animation bug in `TransformingLazyColumn` when items are removed. ([I73034](https://android-review.googlesource.com/#/q/I73034d099ab0f2b723e20edd82a824efd5404cc9))
- Corrected handling of anchor items in `TransformingLazyColumn` when items are removed. ([I841a8](https://android-review.googlesource.com/#/q/I841a80455ce4993ad58e513ee91d32d3be4fc128))
- `PickerGroup` now animates the Pickers horizontally when autocentering is turned on and the selected (centered) picker is changed. ([Ic82c4](https://android-review.googlesource.com/#/q/Ic82c477503c828d34fed47f53e6dde223e0f2d7))

### Version 1.5.0-beta04

June 18, 2025

`androidx.wear.compose:compose-*:1.5.0-beta04` is released. Version 1.5.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/wear/compose).

**Bug Fixes**

- Fix layout bug in `TransformingLazyColumn`, where content that fits within the screen is now aligned correctly from the top of the screen ([I80115](https://android-review.googlesource.com/#/q/I80115d62a9f5437691058b039d1ed054da1ea3c4))
- Fixed an issue with `TransformingLazyColumn` where the bottom item was incorrectly scaled when scrolling to the very bottom of a list with an `EdgeButton`. The scroll progress now follows a gradient descent when restoring the layout. ([Iea375](https://android-review.googlesource.com/#/q/Iea3754059e5e2dbae9a02543c33b13a578c2274c))
- `TransformingLazyColumn` now reads the item height inside the background painter, which allows custom `TransformationSpecs` to implement morphing. ([I022f0](https://android-review.googlesource.com/#/q/I022f01d0cf3eabcd88be0fbb82d6007d26c867dd))
- `SwipeToReveal` now vertically centers the revealed actions correctly. ([I4419b](https://android-review.googlesource.com/#/q/I4419bb5234fff78dfdac131b5b9f3b5df3f22daa))
- Fixed a bug in `SwipeToReveal` that prevented it working correctly with swipe-to-dismiss if both views and compose were in use on the screen. ([I5dc0e](https://android-review.googlesource.com/#/q/I5dc0e98678bf8ab8424aefc5a12c5ceb7d029632))
- Fixed a bug where `SwipeToReveal` actions were drawn with a vertical offset when scrolling. ([I29444](https://android-review.googlesource.com/#/q/I2944450c06cf584077d5d21dc2a3b66f0e01e611))
- `AlertDialog`, `ConfirmationDialog`, `OpenOnPhoneDialog` and `SwipeToReveal` now round up paddings and sizes that are calculated as a percentage of the screen size. ([I76367](https://android-review.googlesource.com/#/q/I76367694089b4499dd4f5b7b160ce165b4e568c6))
- `ButtonDefaults.outlinedButtonBorder` now updates following enabled/disabled state changes size([If2ddd](https://android-review.googlesource.com/#/q/If2dddbbfd6d48103e4b6c056d1bc79f26442397a))
- Fixed a bug in `EdgeButton` height that occurred on complex screens with Pager and `ScreenScaffold`. ([I946e3](https://android-review.googlesource.com/#/q/I946e3cd808e5416a235277d0626e18ac9edb7fca))
- Fixed a race condition that could cause Placeholder animations to stop. ([I53530](https://android-review.googlesource.com/#/q/I53530213901cb972d67fcfb269a762ee55fec164))
- Improved `HorizontalPageIndicator` and `VerticalPageIndicator` performance by drawing to Canvas. ([Ifae1e](https://android-review.googlesource.com/#/q/Ifae1e63d3d37dfe7f4453b3ff7f5bf7458c43dea))
- Refined the shape of EdgeButton to smooth the transitions between the ellipsis and circles that make up the outline. ([I7721e](https://android-review.googlesource.com/#/q/I7721e8cff081c7b2a971ca0c0b6d05f1ffa690ea))
- Fixed a bug in `LevelIndicator` that caused animations to stop, due to unnecessary recompositions. ([I45d08](https://android-review.googlesource.com/#/q/I45d08fb2a3d821130ce953f3d782b71f49e99ec7))

### Version 1.5.0-beta03

June 4, 2025

`androidx.wear.compose:compose-*:1.5.0-beta03` is released. Version 1.5.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..786176dc2284c87a0e620477608e0aca9adeff15/wear/compose).

**API Changes**

- `OpenOnPhoneDialog` now announces only the message text under TalkBack, and skips the icon semantics. The `OpenOnPhoneDialogDefaults` have been updated to remove the `iconContentDescription` and the `contentDescription` parameter from `icon()`. Also, `ConfirmationDialogDefaults` now has modifier parameters on `SuccessIcon` and `FailureIcon` composables. ([Id2ae2](https://android-review.googlesource.com/#/q/Id2ae2a01db6a94ce63a448693922d92beac10c01))

**Bug Fixes**

- Changed the order in which we apply the effect of `SurfaceTransformation` parameters. Before, the transformations applied to Wear Material3 components were done as follows: background painter, container transformation, content transformation. Now, the first 2 are inverted, and we apply any passed in modifier between them, so it is affected by container transformations. This fixes cases like using a placeholder shimmer effect with elements in a TLC using the transformation parameter. ([I786cf](https://android-review.googlesource.com/#/q/I786cfe1468d88d9c0f36b200d69362b46abdad55))
- `RevealState.Saver` was added to be used to restore the state of `SwipeToReveal` when activity or process is recreated. `rememberRevealState` function now uses this Saver by default. ([Ie0ecb](https://android-review.googlesource.com/#/q/Ie0ecb5568107b73d31ab34f0b47156478cbe06a5))
- `SwipeToReveal` primary and secondary actions buttons should default to `ButtonDefault.Height` (fixed bug where these were filling the maximum height for taller buttons). ([Ibfba1](https://android-review.googlesource.com/#/q/Ibfba1e8afb8b2886bc9f4264fe39789c4e8759d7))
- Changed `SwipeToReveal` to reset the last component interacted with, when the swipe right gesture is performed. ([Ia8450](https://android-review.googlesource.com/#/q/Ia8450d487b714a753af628bb8d2d8a5a42d65a73))
- `SwipeToReveal` was changed to settle on the `Revealing` state when the end position of the swipe is in between the revealing and revealed anchors, and is closer to the Revealing anchor. ([If4458](https://android-review.googlesource.com/#/q/If445848ae32cce0a0d28ca35360967ed07b1bf42))
- Now `ButtonGroup`'s content is properly inverted in a RTL layout ([Ib378d](https://android-review.googlesource.com/#/q/Ib378dab6a641f32bb97adefb9b3440703f747707))
- `AnimatedText` now supports RTL text direction ([I4533c](https://android-review.googlesource.com/#/q/I4533cbdc3ce9b1118920e933e2aa89524d9d68a5))
- `TransformingLazyColumn` now resizes items correctly when the bottom item is removed ([Idacab](https://android-review.googlesource.com/#/q/Idacab201ec5dbb09886cd08666785f1850117aee))
- `TransformingLazyColumn` now makes just one measuring pass, which improves performance by reducing frame times. ([I501a1](https://android-review.googlesource.com/#/q/I501a1ac8048d0b718919a4be042e66e84a22d2de))

### Version 1.5.0-beta02

May 20, 2025

`androidx.wear.compose:compose-*:1.5.0-beta02` is released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/wear/compose).

**Bug Fixes**

- Updated baseline profiles for foundation, material \& material3 libraries. ([I53f06](https://android-review.googlesource.com/#/q/I53f068ee058a7a0134eb09b5b9fd68b794ffb3a3))
- Fixed a bug in `TransformingLazyColumn`, where items resized when the bottom item was removed. ([Idacab](https://android-review.googlesource.com/#/q/Idacab201ec5dbb09886cd08666785f1850117aee))
- Fixed a bug with `TransformingLazyColumn`, when the list got stuck at the top or bottom of the list. ([I49d00](https://android-review.googlesource.com/#/q/I49d007b6c0dffc93bb9f06795f9bbc2bc1b619b7))
- `OpenOnPhoneDialog` under TalkBack should announce the curved text, rather than the icon content description. ([I4efe8](https://android-review.googlesource.com/#/q/I4efe8bb83ee1a7cbbbef09461033f2bd6918fdbe))
- Fixed a bug in `SwipeToReveal` that would report the wrong anchor in `RevealState.currentValue` when `hasPartiallyRevealedState` is set to false. ([I9c7cf](https://android-review.googlesource.com/#/q/I9c7cf5ddac9d1b4004ad4390914658eb52fa4a1e))
- `SwipeToReveal` undo buttons are now `ButtonDefaults.Height` by default. ([I1f6c8](https://android-review.googlesource.com/#/q/I1f6c8d47786a1f8ae0894a15fd4b281da86b7b35))
- `BasicSwipeToDismissBox` performance has been improved by eliminating use of Canvas for drawing scrims. ([I68f2c](https://android-review.googlesource.com/#/q/I68f2ccabc036aa778d10485dc19b19b39ac4c5a0))
- Fixed an accessibility bug in Slider, where the announced percentage did not match the value after updates ([I91146](https://android-review.googlesource.com/#/q/I91146a5f4c935076540c871fcad45f401bb4693b))
- Fixed a bug on `placeholderShimmer` implementation. ([Iee39b](https://android-review.googlesource.com/#/q/Iee39b2621d06d1219772bc350108dfbfea582c10)
- `TransformingLazyColumn` performance has been improved, by optimizing `ScrollProgress` calculation by 30%. ([I4c4cb](https://android-review.googlesource.com/#/q/I4c4cbc0971eb75fe1e4b62c89a298e1ae9f48e2b))

### Version 1.5.0-beta01

May 7, 2025

`androidx.wear.compose:compose-*:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/wear/compose).

The 1.5.0-beta01 release of Compose for Wear OS indicates that this release of the library is feature complete and the API is locked (except where marked as experimental).

Wear Compose 1.5.0-beta01 includes the Wear Compose Material3 library, which supports the new UI design system called Material 3 Expressive. It is recommended to upgrade from Material to Material3 to embrace the new visual design in apps, and to benefit from the new components as follows:

- `MaterialTheme` for updated and extended color schemes, typography, and shapes to bring both depth and variety to your designs.
- Dynamic Color Theming which automatically generates a color scheme for your app to match the watch face colors.
- New components automatically adapt to larger screen sizes by default
- Shape Morphing - round button components like `IconButton`, `TextButton`, `IconToggleButton` and `TextToggleButton` support variations that animate when pressed or checked.
- `EdgeButton` - a new edge-hugging button with a special shape designed for the bottom of the screen.
- Scaffolds - introducing `AppScaffold` and `ScreenScaffold` to lay out the structure of the screen and coordinate `ScrollIndicator` and `TimeText` animations.
- Buttons - numerous stadium-shaped buttons are supported with flexible, single-slot containers and multi-slot variations for buttons with icons and labels. `CheckboxButton` and `SwitchButton` are provided when toggle buttons are needed, whilst `RadioButton` is the available selection button ('Split' variations of the toggle and selection buttons are also provided).
- `ButtonGroup` - implements an expressive group of buttons in a row that shape-morph when touched.
- `AlertDialog` variations support ok/cancel buttons or an `EdgeButton`.
- `ConfirmationDialog` is available to display a message with a timeout, supporting special animations for success, failure and open-on-phone variations.
- Pickers - `TimePicker` and `DatePicker` variations are supported as well as the Picker and `PickerGroup` components for building your own picker screens.
- `ProgressIndicators` - circular, and linear progress indicators are supported (the `CircularProgressIndicator` has segmented and indeterminate variations).
- Cards - a number of card variations are available, including `TitleCard` which offers specific layouts for cards with title, time, subtitle or content slots. `TitleCard` can also be given an image background to reinforce the meaning of the information in a card.
- Pagers - `HorizontalPagerScaffold`, `VerticalPagerScaffold` and `AnimatedPage` components coordinate `HorizontalPageIndicator` and `VerticalPagerIndicator` animations. `HorizontalPager` and `VerticalPager` are released in the Wear Compose Foundation library.
- Placeholders - draws a skeleton shape over a component, for situations where no provisional content is available.
- Sliders and Steppers - both sliders and steppers allow users to make a selection from a range of values. Sliders are more compact and can be segmented, whereas Stepper is a full screen component typically paired with a `StepperLevelIndicator`.
- `SwipeToReveal` - used to add additional actions to a composable when it is swiped right-to-left.

In addition, Wear Compose Foundation 1.5.0-beta01 includes these new components:

- `TransformingLazyColumn` - a lazy, vertically scrolling list the supports scaling and morphing animations
- Hierarchical Focus Groups - used to annotate composables in an application, to keep track of the active part of the composition and coordinate focus.
- Pagers - `HorizontalPager` and `VerticalPager` components, built on the Compose Foundation components with Wear-specific enhancements to improve performance and adherence to Wear OS guidelines.

**API Changes**

- Updated the Hierarchical Focus API - renamed `Modifier.hierarchicalFocus` to `Modifier.hierarchicalFocusGroup` and removed the callback parameter; removed the overload of `Modifier.hierarchicalFocusRequester` with a `FocusRequester` parameter; created a new `CompositionLocal`, `LocalScreenIsActive` so that components can inform and check which screen is the active one. ([I5ff7c](https://android-review.googlesource.com/#/q/I5ff7cecc4f8e50d3f1a198dae621b3e9545e41e9)).
- Deprecated `SwipeToReveal` from Wear Compose Foundation in favor of `SwipeToReveal` APIs in Wear Compose Material and Wear Compose Material3. Please replace Wear Foundation `SwipeToReveal` imports with Wear Compose Material/ Wear Compose Material3 imports to continue using the APIs. ([Ia147d](https://android-review.googlesource.com/#/q/Ia147d058572f6f1082826b1848993177443780af)).
- Wear Compose Material3 `SwipeToReveal` dependencies on Foundation were moved to the material3 package, e.g. `RevealValue`, `RevealDirection`, `RevealActionType`, `RevealState`, `rememberRevealState`. Developers should change their imports of these classes and functions from `androidx.wear.compose.foundation` to `androidx.wear.compose.material3`. ([I640e6](https://android-review.googlesource.com/#/q/I640e68aa8a8a55a08c052c01b16cdfefaecb1fa0)).
- Updated the Wear Compose Material3 `SwipeToReveal` API as follows: added `primaryAction`, `onFullSwipe`, `secondaryAction`, `undoPrimaryAction`, `undoSecondaryAction` and `hasPartiallyRevealedState` parameters to the `SwipeToReveal` composable; removed the ability to customize `positionalThreshold` and `animationSpec` from `RevealState`; removed `lastActionType`, `revealThreshold` and width from `RevealState`; changed the `RevealState` constructor to accept a `RevealDirection` instead of anchors; removed `createRevealAnchors`, anchors, and `bidirectionalAnchors` functions; `SwipeToRevealScope` functions `primaryAction`, `secondaryAction`, `undoPrimaryAction` and `undoSecondaryAction` were renamed to `PrimaryActionButton`, `SecondaryActionButton`, `UndoActionButton` and made into Composable functions; marked `RevealActionType` as internal. ([I885d0](https://android-review.googlesource.com/#/q/I885d03e3744af23ae8cf63118f7417df273bb888)).
- Further updated `SwipeToReveal` API as follows: renamed `onFullSwipe` to `onSwipePrimaryAction`; renamed `SwipeToRevealNonAnchoredSample` to indicate the use of the `hasPartiallyRevealedState` parameter; removed `actionButtonHeight`, since the default is the Button's default height and the larger height can be set using a modifier; removed the `SmallActionButtonHeight` from `SwipeToRevealDefaults`; made the value parameter in `RevealValue` and `RevealDirection` constructors private. ([I465ce](https://android-review.googlesource.com/#/q/I465cede795a2c3042680176a8fda9c60cd1942d6)).

**Bug Fixes**

- Fixed `ScreenScaffold`'s `EdgeButton` handling so that, after a `TransformingLazyColumn` item is removed, the `EdgeButton` is animated into place. ([I6d366](https://android-review.googlesource.com/#/q/I6d366fcdafa605cb89259bc650087b98109d60ca)).
- Updated Wear Compose dependencies on Compose libraries to version 1.8.0. ([I2ef3f](https://android-review.googlesource.com/#/q/I2ef3fd8f7d7f5a31cfc25c5be0bcc169034a6ee1)).
- Updated the motion of the indeterminate `CircularProgressIndicator` so that it no longer regresses temporarily. ([Ieddb1](https://android-review.googlesource.com/#/q/Ieddb15c3e5b73c6e372ec91e5e34d18c98a7db79)).
- Fixed a `SwipeDismissableNavHost` bug - the focus was not switching correctly after swiping back, causing rotary input to fail (this was for API 36+, which uses predictive back). ([Ieddb1](https://android-review.googlesource.com/#/q/Ieddb15c3e5b73c6e372ec91e5e34d18c98a7db79)).
- Amended documentation for the Hierarchical Focus API ([Idf2ff](https://android-review.googlesource.com/#/q/Idf2fff47b1ba1164e4c36ec108f6a897f492cd6b)).
- Updated the documentation for Button and Card to state how `containerPainter` and `disabledContainerPainter` override `containerColor` and `disabledContainerColor` ([I4a453](https://android-review.googlesource.com/#/q/I4a4534cdc6d5b7e0e86e4182a5be6ee5d3fffdb2)).
- Reverted a change to `TimeText` in the previous [release](https://android-review.googlesource.com/#/q/I1cc5dbfe12675efd77c3fc332f1015d92a64f492) which moved the `BroadcastReceiver` to a worker thread, because it caused issues for apps that manage their own threading during navigation. ([I34d02](https://android-review.googlesource.com/#/q/I34d0292abaa91f7e69524818a130c9c5aa527cfa)).
- Updated the Picker samples to remove unnecessary remember calls and instead use `rememberUpdatedState` in Picker to remember the latest `contentDescription` lambda function. ([Icb5b1](https://android-review.googlesource.com/#/q/Icb5b1bd19f4cff6eeb0d1a57bcef688111bb6602)).
- Updated text styles in `TimePicker` and `DatePicker` so that font changes no longer result in truncation. ([I26194](https://android-review.googlesource.com/#/q/I261945c46f8fe90854c0fae3927de05fe7d5b8d3)).
- `ListHeader` and `ListSubHeader` now default text alignment to center-aligned and start-aligned respectively. ([I78339](https://android-review.googlesource.com/#/q/I78339a880e04108644517e536e287f07fa1fd55a)).
- Updated Foundation and Material Swipe to Reveal samples and demos to announce custom accessibility actions (the custom actions must be added as semantics on the content, not on the `SwipeToReveal` composable itself). ([Ie92a3](https://android-review.googlesource.com/#/q/Ie92a32ca21171abaf215289255651beb0b31e3f8)).
- Updated the default `MaxLines` set on the `EdgeButton` content according to its size - it is now 1 for extra small, 2 for small and medium, and 3 for large. ([Ie35f6](https://android-review.googlesource.com/#/q/Ie35f687595255ec4c8daacaad91dbe0d4111b4a2)).
- Simplified `LocalReduceMotion` so that the observer is only registered once, to improve performance. ([Ib1979](https://android-review.googlesource.com/#/q/Ib197945afc7955a58b76b9c56325b98f12ee46e1)).
- Minimized the number of redraws in `ScrollIndicator`, to improve performance. ([Ia7a67](https://android-review.googlesource.com/#/q/Ia7a67feab96c1f654c9051eb464b4e1ddcf39aab)).
- Fixed a bug in `TransformingLazyColumn`, where the top visible item in the list did not scale correctly when EdgeButton achieved its full height. ([I30580](https://android-review.googlesource.com/#/q/I30580339d0fa8d3940c62b6b9640570adf77235b)).

## Wear Compose Material3 Version 1.0

### Version 1.0.0-alpha37

April 23, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha37` is released. Version 1.0.0-alpha37 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/wear/compose/compose-material3).

**API Changes**

- Removed `scrollTransform` from the public API surface. Use the combination of `transformedHeight` and `graphicsLayer` modifiers if you need to get the same functionality. ([Ie181d](https://android-review.googlesource.com/#/q/Ie181dbca319aa0c676435e96dfea6203ff7b0e36))
- Replaced `ImageButton` and `ImageCard` composables with `Button` and `Card/TitleCard` overloads respectively. Renamed `imageButtonColors` to `buttonWithContainerPainterColors` and `imageCardColors` to `cardWithContainerPainterColors`. Added public `ButtonDefaults.scrimBrush` and `CardDefaults.scrimBrush`. Renamed button `imageBackgroundGradientStartColor` and `imageBackgroundGradientEndColor` to `scrimGradientStartColor` and `scrimGradientEndColor`. Renamed `CardDefaults.ImageContentPadding` to `CardDefaults.CardWithContainerPainterContentPadding` ([I7b8b6](https://android-review.googlesource.com/#/q/I7b8b6e861e4cab02dfb5e10288a45a1d4f7a03e6))
- `Picker` and `PickerGroup` now take the `contentDescription` as a lambda to avoid unnecessary recompositions. ([I002dd](https://android-review.googlesource.com/#/q/I002ddc35c8177181e6f06e90cf4c0f48a7b474af))

**Bug Fixes**

- Fixed an issue where indeterminate `CircularProgressIndicator` would wobble during animation if width is not equal to height. ([I76bfe](https://android-review.googlesource.com/#/q/I76bfeaa09cd88a407a30428c7c2a084451f7f6a6))
- Fixed an issue with edge button layout on invalid size. Now prevents updating the layout of the edge button when the height is NaN. ([I32b93](https://android-review.googlesource.com/#/q/I32b936d214a77c8181087c4e8bce0a7f2377ce61))
- Increased the max sweep angle in `OpenOnPhoneDialog` so that the default 'Check your phone' text is not clipped with the largest font size. ([I90af9](https://android-review.googlesource.com/#/q/I90af92234d23fe4352c35759124204993f0ec808))

### Version 1.0.0-alpha36

April 9, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha36` is released. Version 1.0.0-alpha36 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..4c37298a97c16270c139eb812ddadaba03e23a52/wear/compose/compose-material3).

**API Changes**

- Replaced `ButtonDefaults.imageBackgroundButtonColors` with `ImageButton`, `ButtonDefaults.imageButtonColors`, `ButtonDefaults.containerPainter` and `ButtonDefaults.disabledContainerPainter`. And similar changes for Card. The painters are removed from `ButtonColors` and `CardColors`. ([I8c6a1](https://android-review.googlesource.com/#/q/I8c6a141bdaa046953bf5c354808905f019f04a9f))
- Updated placeholders to simplify the API. We now provide two Modifiers, `Modifier.placeholderShimmer` to apply a shimmer effect at the component level, and `Modifier.placeholder` to apply a mask on top of unloaded content ([Iaee7a](https://android-review.googlesource.com/#/q/Iaee7a9eabf64ed21d6b61aa92c8f03e4839c3ea2))

**Bug Fixes**

- Integrated overscroll into the `ScrollIndicator`. ([Icfb7f](https://android-review.googlesource.com/#/q/Icfb7f4d02ccbf592b21c02d956b4ce09b39d4023))
- Address blank backgrounds and missing dialogs when launching material3 dialogs. ([Ice597](https://android-review.googlesource.com/#/q/Ice59724a2d7f43d84bbfa0abbfd70588629cfb8b))
- Fixed issues in `FadingExpandingLabel` when text spans multiple lines. ([I04eb7](https://android-review.googlesource.com/#/q/I04eb73accbba82348bce40827edd882d6e8861fd))
- Updated padding between primary and secondary labels on buttons. ([I99b7b](https://android-review.googlesource.com/#/q/I99b7babb8e35d15a9fef843a38f8f1cc07575989))
- `ArcLarge` has been reduced from `20sp` to `18sp`, and letter spacings on `ArcLarge` and `ArcSmall` have been updated. `ConfirmationDialog`/`OpenOnPhoneDialog` now use the default `ArcLarge` instead of overriding it to `18sp`. ([Id39a8](https://android-review.googlesource.com/#/q/Id39a8d0270ce2e81c7fa8b4465e8182dbfd25994))

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.0.0-alpha35

March 26, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha35` is released. Version 1.0.0-alpha35 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/wear/compose/compose-material3).

**API Changes**

- `AlertDialog` top padding is now reduced by default when an icon is provided - this makes best use of the screen size available. ([Ief06c](https://android-review.googlesource.com/#/q/Ief06c6cf25b0f651d2c5a6274af54d253b626339))
- `PagerScaffoldDefaults.FadeOutAnimation` has been renamed to `PagerScaffoldDefaults.FadeOutAnimationSpec`. The page parameter on `AnimatedPage` has been renamed to `pageIndex`. ([I701f2](https://android-review.googlesource.com/#/q/I701f2cd0e28156c4fa7ceddcf885c74e508d73b4))
- Updated naming for `TransformingLazyColumn`'s `SurfaceTransformation` - `applyTransformation` split into `applyContainerTransformation` and `applyContentTransformation`, and renamed `createBackgroundPainter` to `createContainerPainter`. Further naming updates to `TransformationSpec` and `ResponsiveTransformationSpec`. ([I1c534](https://android-review.googlesource.com/#/q/I1c534b3cca373c0d035627c998b4a0f5c6f518d4))
- The `AppScaffold backgroundColor` has been renamed to `containerColor`. ([I4e63f](https://android-review.googlesource.com/#/q/I4e63f7cf6ab024cfd9fc96e66070ea7a13532aa9))

**Bug Fixes**

- Fixed an issue in `FadingExpandingLabel` where the text did not always expand correctly. ([I0e773](https://android-review.googlesource.com/#/q/I0e7738ed93920bb0a33cdec51c653b3416f2a58b))
- `ArcLarge` has been reduced from 20sp to 18sp, and letter spacings on `ArcLarge` and `ArcSmall` have been updated. `ConfirmationDialog/OpenOnPhoneDialog` now use the default `ArcLarge` instead of overriding it to 18sp. ([Id39a8](https://android-review.googlesource.com/#/q/Id39a8d0270ce2e81c7fa8b4465e8182dbfd25994))
- Updated the heading animation for `DatePicker` and `TimePicker` based, so that the fade-out and fade-in animation act as one Spring animation. ([I68963](https://android-review.googlesource.com/#/q/I6896359fa8a5637e7489c467fb0817b3c2a492f3))
- Optimized `PagerScaffold` by avoiding the reading of `currentPageOffsetFraction` in the `AnimatedPage` composable. ([I433ef](https://android-review.googlesource.com/#/q/I433ef5bd0eb79664e7d040ed421b9f6f4d71ba61))
- All type scales have been updated to have proportional numerals by default, because that is seen as the most frequent use case and defaulting to tabular resulted in too much spacing between certain number pairings. `TimePicker` and `DatePicker` continue to apply `FontFeatureSetting=tnum` for tabular numerals. ([I88929](https://android-review.googlesource.com/#/q/I88929c00e50727b2dd3cc9de5b27698f6f9f1f1a))
- Corrected the initial RSB input focus for `TimePicker` and `DatePicker`. ([I1c773](https://android-review.googlesource.com/#/q/I1c7732e851ce85f1085e64176ad2862feee3f0d9))
- Updated the default text on `OpenOnPhoneDialog` to "Check your phone". ([I00a3f](https://android-review.googlesource.com/#/q/I00a3f264337bb2186a7d143605f5d6b3bcc9ffa5))
- Updated weights for `ArcLarge` and `ArcMedium` from 600 to 599 to workaround an issue where weight 600 is treated as bold ([I2a51d](https://android-review.googlesource.com/#/q/I2a51df05b2517af0f11c50b203832c7ae5258a05))
- Update `SwipeToReveal` paddings between content and action buttons, and also the padding between the icon and text of the action buttons. ([Ic46cb](https://android-review.googlesource.com/#/q/Ic46cb9adb55f67734983b88880ff17fd8b4e37a6))

### Version 1.0.0-alpha34

March 12, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha34` is released. Version 1.0.0-alpha34 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/wear/compose/compose-material3).

**API Changes**

- `PagerScaffold` no longer emits a `Pager` component - instead this must be provided via the `content` Composable. `AnimatedPage` and `snapWithSpringFlingBehaviour` are now public and can be used along with Wear Foundation `Pager` to achieve previous M3 `PagerScaffold` behaviour. (See updated samples). ([Ia4724](https://android-review.googlesource.com/#/q/Ia4724b64f9c922ce8b28a0a437c9437c08951d7b))
- Updated `PagerState`, removing the Compose Foundation `PagerState` as the base class and adding `currentPage`, `currentPageOffsetFraction` and `pageCount` properties. Updated the `GestureInclusion` interface, renaming the method to `ignoreGestureStart`. ([I4ae07](https://android-review.googlesource.com/#/q/I4ae07629b92378473247bd20f37b03b07ef8541a))
- `LevelIndicator` sweep angle parameters are now annotated with `FloatRange(0, 360)` ([I7e636](https://android-review.googlesource.com/#/q/I7e636d88d159e6841ef8cc78d3cd9c79b6f810e6))
- We have added `CurvedModifier.clearAndSetSemantics` to provide a means by which curved semantics can be turned off. `CurvedText` continues to default the content description to the text, but `timeTextCurvedText` and `timeTextSeparator` do not now announce their contents. ([I4b568](https://android-review.googlesource.com/#/q/I4b568e3cced9e028b6efefce3c9f6150172ee05b))
- Added a background and default content color parameters to `AppScaffold`. ([I56652](https://android-review.googlesource.com/#/q/I5665220b825c7c2e887c27a8b347c49e0d40c85d))
- `HorizontalPager`'s default handling of swipe gestures has been renamed to `PagerDefaults.gestureInclusion`. The default behavior is now to only ignore swipe gestures that start on the left edge of the first page, and only then when Talkback is turned off. In other cases, the default behavior is that swipe gestures will not be ignored by the pager, so they will not be available to swipe-to-dismiss handlers. ([Iee486](https://android-review.googlesource.com/#/q/Iee486edeae3111a069959bc5f516ff20f4652747))
- Added a `SurfaceTransformation` parameter to button, card and list header components, so that they can apply different background and content transformations when used in containers that change items appearance based on their position, such as `TransformingLazyColumn`. ([Iabe3f](https://android-review.googlesource.com/#/q/Iabe3f396c8c0135e5d2d2587c617e1b71ad42d2e))
- We have updated 'public const val' properties in our Wear Compose Material3 API to 'public val', to avoid the values being inlined. ([Ib0f32](https://android-review.googlesource.com/#/q/Ib0f3289c949f7053088ce71ff21fd67fd001e5fd))
- Added support for an edge-swipe zone to `SwipeToReveal`. Foundation `SwipeToReveal`'s default behavior is now to disallow swiping when the gesture starts from the edge. Material3 `SwipeToReveal'`s default behavior is now to disallow swiping when the gesture starts from the edge, when the `SwipeDirection` is set to single direction. ([I32ef0](https://android-review.googlesource.com/#/q/I32ef0e9e201fc71cb5c9830c766a933a84b99c74))
- Added `FadingExpandingLabel` composable, which allows it to fade in text with animation line by line. ([Ic60fa](https://android-review.googlesource.com/#/q/Ic60fa9c3283eb74cc194af448a4a13a08b455415))
- `TransformingLazyColumn` now uses empty `contentPadding` by default instead of putting first and last items into center. ([I77ab7](https://android-review.googlesource.com/#/q/I77ab73d6005a2013cfc14cf2f4399d4a61427507))
- Removed `SwipeToReveal`'s `rememberRevealState` from the Wear Compose Material3 library. ([I8c0e0](https://android-review.googlesource.com/#/q/I8c0e0f7a8732a4303cab637858ba7481cb5cae6b))

**Bug Fixes**

- Wear Compose libraries have been updated to the Kotlin 2.0 compiler. ([I2de79](https://android-review.googlesource.com/#/q/I2de793d3fa8fb38c7b55f6e26700df5d8a3c3dfc))
- Support for non-round `ScrollIndicator` and `PageIndicator` has been removed from Material3. Square screen support is also no longer part of the Wear OS requirements, see the [Getting Started guide](https://developer.android.com/design/ui/wear/guides/foundations/getting-started) for more information. ([I9a852](https://android-review.googlesource.com/#/q/I9a852eb2312d4cd892f28836211db0aa79b3e9e4))
- The `CurvedTextStyle` used in `ConfirmationDialogDefaults` and `OpenOnPhoneDialogDefaults` has been updated to use `ArcLarge` typography with size `18sp` and letter spacing `1.8sp`. ([Ic9ced](https://android-review.googlesource.com/#/q/Ic9cedecdf1f5d22fec104f56db63dbccd15dde0d))
- `Card`, `ListHeader`, `RadioButton`, `CheckboxButton`, `SwitchButton` no longer constrain the height of its contents by default. Where necessary, use `Modifier.height(IntrinsicSize.Min)` to restore the previous behavior if needed. ([I80bb8](https://android-review.googlesource.com/#/q/I80bb803f65d08f41a71e2b4d794cea6db6c2b24c))
- We have updated the default `TimeText` and `ScrollIndicator` colors to include more gray tones, because using `OnBackground` (white) directly carried too much visual weight when competing with other content on screen like titles. ([I8b36f](https://android-review.googlesource.com/#/q/I8b36f5580924c0182ae558f92c8301dd033d4b1a))
- We have reduced the timeout for animating the `TimeText` and `ScrollIndicator` in scaffold components to 2 seconds. ([I52021](https://android-review.googlesource.com/#/q/I52021e681c055083503d8d55c0731898745209f3))
- We have updated the motion of Dialog so that the scale of the background of the Dialog is synchronised with swiping to dismiss. ([I925a9](https://android-review.googlesource.com/#/q/I925a9679ecc8f67397902c2f2ea23c8fa142c5ff))
- Add demo of M3 `SwipeToReveal` using `edgeSwipeToDismiss` modifier. ([I02b07](https://android-review.googlesource.com/#/q/I02b0702c8938b0c0cdb8a5037e71390726f43e74))
- We have added a heading to `DatePicker` and `TimePicker` under TalkBack so that the user is informed to scroll to set date/time. ([Id738d](https://android-review.googlesource.com/#/q/Id738d0351026170504486670a1d885ced362ef58))
- `AnimatedText` now follows the reduce motion setting. ([Ib6578](https://android-review.googlesource.com/#/q/Ib6578b921e414ad057850c1cf6b48dce8b3633b5))
- The optimisation to use `AppScaffold` for display Dialog content has been improved to allow multiple dialogs to be displayed on top of each other ([I1209c](https://android-review.googlesource.com/#/q/I1209c2bdf8bde521c1530dd0a0251b20998d35d2))

### Version 1.0.0-alpha33

February 26, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha33` is released. Version 1.0.0-alpha33 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c9a90c7caa35af354574d7b598d32c9ae22b39de..fd7408b73d9aac0f18431c22580d9ab612278b1e/wear/compose/compose-material3).

**API Changes**

- We have removed the label parameter from `SwipeToRevealScope`'s `primaryAction` and `secondaryAction`. Custom action semantics should be added to the content of the `SwipeToReveal` component directly, by the developer. ([Ia67f3](https://android-review.googlesource.com/#/q/Ia67f3a1a96e6bdf3787716a6c35685da9f3f5704))
- We have removed the 'Button' prefixes from sizes, text styles and color functions in `IconToggleButtonDefaults` and `TextToggleButtonDefaults` ([I5471d](https://android-review.googlesource.com/#/q/I5471df6897fcd89d8266813408e702b24528f24a))
- We have removed the experimental `LocalMinimumInteractiveComponentEnforcement` ([I4ad8a](https://android-review.googlesource.com/#/q/I4ad8a126a765b814d37e5ca379cbb959e3de60fd))
- We have replaced the `PickerGroupScope` DSL with a composable. As such, we removed the `pickerGroupItem` method from `PickerGroupScope`, and instead added `@Composable PickerGroupItem` that should be used to add a Picker to `PickerGroup`. We also updated the type of `PickerGroup` 'content' parameter to `@Composable PickerGroupScope.() -> Unit`. ([Ic6aec](https://android-review.googlesource.com/#/q/Ic6aec8993bc2ca066610d9034091ef52ccc14fd3))
- We have added a `LevelIndicator` overload for fractional values and added a Stepper prefix to those overloads that include a range parameter (which are suitable for use with the Stepper component). ([If4234](https://android-review.googlesource.com/#/q/If4234a153ae6219d01e688efa6b58a7e11c4526e))
- We have added `TransformingLazyColumn`'s `TransformationSpec` to the API, which allows the definition of the exact transformations happening to the items as they are being scrolled through the TLC. ([I21856](https://android-review.googlesource.com/#/q/I21856ef3b85e81a5a493c56f80623a47e49fe661))
- We have updated `IconButtonShapes`, `IconToggleButtonShapes`, `TextButtonShapes` and `TextToggleButtonShapes` to be consistent with the compose/material3 classes ([I5a081](https://android-review.googlesource.com/#/q/I5a08132ae2f23ce7ebcac564976d375f432b5c2b))
- We have added an `overscrollEffect` parameter added to `ScalingLazyColumn`, `TransformingLazyColumn` and `ScreenScaffold`. ([I0cee8](https://android-review.googlesource.com/#/q/I0cee8f98e15b7eb79eb9d08314adb2cae465d85a))
- We have renamed the `swipeDirection` parameter to `revealDirection` in `rememberRevealState`. ([I7472f](https://android-review.googlesource.com/#/q/I7472fa6a6bcb115431b15e4468d8ea986ef9a750))
- Wear Pager now has its own `PagerScope` instead of using Compose `PagerScope`. ([I9195b](https://android-review.googlesource.com/#/q/I9195b6dfac15785f72d54e0e125f614c2756a7fe))
- We have removed the `LinearProgressIndicatorContent` composable, please use `LinearProgressIndicator` directly so that changes to values are animated by default. ([I2c4ad](https://android-review.googlesource.com/#/q/I2c4ad48dc4b5996995affc7642a9c6298b99d99c))
- We have removed the `CircularProgressIndicatorStatic` composable and added a public `DrawScope` function `drawCircularProgressIndicator` with the same functionality. Please use `CircularProgressIndicator` directly so that changes are animated by default, but build your own composable from `drawCircularProgressIndicator` if custom animations are needed. ([Ie762f](https://android-review.googlesource.com/#/q/Ie762f09bf0f8b7a1fb26c1abbf1bce0291855ae0))
- We have reordered the parameters in `DrawScope.drawCircularProgressIndicator` to move up the `targetProgress` parameter. ([I8ab92](https://android-review.googlesource.com/#/q/I8ab92f0c95c61c67a0b9f3d29ae6d01cff7b5b44))
- The `OpenOnPhoneDialog` api was updated for better clarity and consistency with other Dialogs. The `show` parameter was renamed to `visible` and `curvedText` is now provided by the caller instead of having a default value. ([Idec2d](https://android-review.googlesource.com/#/q/Idec2d959e1a9c3bab7ad193c159d68be8a23c194))
- We have renamed `openOnPhoneCurvedText` to `openOnPhoneDialogCurvedText` ([I65bdd](https://android-review.googlesource.com/#/q/I65bdd89b778cfdfdbba6f9247b0edbfd166ed66a))
- We have added `ScrollIndicatorColors` for providing custom colors to `ScrollIndicator`. ([I9eb8c](https://android-review.googlesource.com/#/q/I9eb8ce449509ca2310279224d39ac9a7938726d7))
- Allow the configuration of the color used to draw a background behind `TimeText`. ([I9f5d9](https://android-review.googlesource.com/#/q/I9f5d98496c28d202f618617f4e84386f1c836c11))
- Updated `ArcLarge`, `ArcMedium` and `ArcSmall` typographies to be `CurvedTextStyle` ([Iffc41](https://android-review.googlesource.com/#/q/Iffc417da1c28b8e67fb17beddbec064dab79c29e))
- We have removed `ScreenScaffoldDefaults.contentPaddingWithEdgeButton`. ([Ia923e](https://android-review.googlesource.com/#/q/Ia923ee458b8e84788c8e1a04509a3f5847a03c8e))
- We have added `errorDim` to the `ColorScheme`, for high priority errors or emergency actions such as safety alerts, failed dialog overlays or stop buttons. ([I70998](https://android-review.googlesource.com/#/q/I70998edcd786ed6aef967df3f3a6cd3dc137da25))

**Bug Fixes**

- We have pinned `wear.compose.material3` to version 1.15.0 of `androidx.core.core` ([I132e9](https://android-review.googlesource.com/#/q/I132e92684b62227e5a676bd5fc160bf2e199d056))
- We have improved Dialog's performance by using the `AppScaffold` to layer dialogs over other screen content ([I1b9a4](https://android-review.googlesource.com/#/q/I1b9a418bca6f619ed3d63b339006f56554cc4d18))
- Reduced `EdgeButton`'s internal vertical padding. ([I1a5bb](https://android-review.googlesource.com/#/q/I1a5bbce39d93c540587ea17649bc79f2b1a895ff))
- We have added Button semantics to Slider buttons. ([I80cc6](https://android-review.googlesource.com/#/q/I80cc6b76399a179f33888e889fab3c4e147eb459))

### Version 1.0.0-alpha32

January 29, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha32` is released. Version 1.0.0-alpha32 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..c9a90c7caa35af354574d7b598d32c9ae22b39de/wear/compose/compose-material3).

**API Changes**

- On `CurvedTextStyle`, we have split letter spacing into clockwise letter spacing and counter clockwise letter spacing. This is required because clockwise letters fan out from the baseline whereas counter-clockwise letters fan in (so larger letter spacing is needed) ([I4b848](https://android-review.googlesource.com/#/q/I4b848bfc0b7603e5110798b6fa5c7c925d461e77))
- We have updated `IconButtonShapes`, `IconToggleButtonShapes`, `TextButtonShapes` and `TextToggleButtonShapes` to improve consistency across Material3 libraries. This change also introduces shape caching to reduce the number of allocations. ([I049fc](https://android-review.googlesource.com/#/q/I049fc4f322281710114b23fac428c772fde23952))
- We have removed the `pressedShapeCornerSizeFraction` parameter from the `variantAnimatedShape` method in `IconToggleButton` and `TextToggleButton` ([I58a65](https://android-review.googlesource.com/#/q/I58a6502478362e0aafdd287712f8a648659a1e7c))
- We are introducing improvements to curved text rendering (including `TimeText`) that are incompatible with non-round screens. Non-round screen support is also no longer part of the Wear OS requirements, see the [Getting Started guide](https://developer.android.com/design/ui/wear/guides/foundations/getting-started) for more information. ([I1cc1c](https://android-review.googlesource.com/#/q/I1cc1c7fb6f0d77bd51190a933556dd046ce179cf))
- We have updated `ButtonGroup`'s `ButtonGroupScope`, replacing the DSL-based `ButtonGroupItem` with `Modifier.weight`, `Modifier.minWidth` and `Modifier.enlargeOnPress`. ([I16c3c](https://android-review.googlesource.com/#/q/I16c3c2c9bccc7871b337f39d36c90875396fd530))
- In the `ButtonGroup` API, we have updated the new modifier-based `ButtonGroupScope`: `enlargeOnPress` is now called `animateWidth`, and it takes an `InteractionSource`, rather than `MutableInteractionSource` because it is not necessary to mutate it. We have also added public constant `ButtonGroupDefaults.DefaultMinWidth`, the default minimum width of buttons in a `ButtonGroup`. ([Ie27ec](https://android-review.googlesource.com/#/q/Ie27ec626de18bf944c727f4fb342a5f98024aa7d))
- We have updated `ListHeaderDefaults.contentColor` to start with a lowercase letter as it is a composable property ([I125a5](https://android-review.googlesource.com/#/q/I125a5e4185f253bf5001b7c57afceb40097a524f))
- We have added a content description parameter to `SliderDefaults.DecreaseIcon` and `SliderDefaults.IncreaseIcon`, with suitable default values ([I2e1a7](https://android-review.googlesource.com/#/q/I2e1a715f294a477636e7ad4cbace002a88e1f9e5))
- We have renamed the `spacing` parameter in `Picker` and `PickerGroup` to `verticalSpacing` ([Ib75cc](https://android-review.googlesource.com/#/q/Ib75cc51725e2215dbe7e71e7d4dcb3c49322716b))
- We have removed `ConfirmationDialogDefaults.successText` and `failureText` because it is expected that callers of `ConfirmationDialog` will provide strings with more context. Also renamed `confirmationCurvedText` to `confirmationDialogCurvedText`. Finally, renamed the Dialog `show` parameter to visible for consistency with other recent updates to dialogs. ([I10074](https://android-review.googlesource.com/#/q/I100744310090e84c5c68e994ca257fdf79d3431c))
- `IconButton` renamed `disabledImageOpacity` to `DisabledImageOpacity`. ([I5f94a](https://android-review.googlesource.com/#/q/I5f94a733a11dd685355e12be0c95d8c9ddc257df))

**Bug Fixes**

- We have fixed a bug in `EdgeButton` animation so that the correct size is used in each frame ([Id3b58](https://android-review.googlesource.com/#/q/Id3b585de3b160013f4690d9edfd9f1b51a18c427))
- Fixed an issue with `animateContentSize` not working with `Button`. ([Ib18a0](https://android-review.googlesource.com/#/q/Ib18a0fccadfec00160612b9491036eb153b151de))
- We have changed the Title Large type scale to have font size `18dp` ([Ic9d52](https://android-review.googlesource.com/#/q/Ic9d52e7563e79219c26e61460ebbc98b6ad90bbf))
- We have updated `AlertDialog` spacing and icon size ([Iac28c](https://android-review.googlesource.com/#/q/Iac28cf56e885b8244af3338717a4e81e5235925b))
- We have fixed inconsistencies in large screen breakpoints (screens at and above 225dp are large screen) ([I36474](https://android-review.googlesource.com/#/q/I364740bdaa47854557dcf9247e5ec8fb2ad04315))
- Fixed a minor bug in button positioning ([I952c2](https://android-review.googlesource.com/#/q/I952c26fd830a5f2fed8675e28a215c2d37948bfa))

### Version 1.0.0-alpha31

January 15, 2025

`androidx.wear.compose:compose-material3:1.0.0-alpha31` is released. Version 1.0.0-alpha31 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/wear/compose/compose-material3).

**API Changes**

- We have updated all Wear Compose libraries to 'explicit API' mode. ([Iebf9f](https://android-review.googlesource.com/#/q/Iebf9ff548336a522274175ab9911ad2643f5cc75))
- We have updated the `ScreenScaffold` and `EdgeButton` APIs, so that it is easier to specify content paddings on screens that include an `EdgeButton`. In the new API the `EdgeButton`'s `size` is only passed to the `EdgeButton`, and the `ScreenScaffold` takes an `edgeButtonSpacing` parameter for the spacing between `EdgeButton` and list content. ([I424fd](https://android-review.googlesource.com/#/q/I424fde25849e97a3f500d09642209159893505c9))
- In `DatePicker`, we have renamed parameters `minDate` to `maxDate`, and `minValidDate` to `maxValidDate`. In `DatePickerColors`, we have renamed parameter `selectedPickerContentColor` to `activePickerContentColor`, and `unselectedPickerContentColor` to `inactivePickerContentColor` ([Iba17b](https://android-review.googlesource.com/#/q/Iba17bb5dd0dadc7927774097c5afac2d46ab53b7))
- We have updated the `ArcProgressIndicator` defaults to `strokeWidth=6dp` and recommended `diameter = 81.24%` of screen height ([I6f248](https://android-review.googlesource.com/#/q/I6f248aabb032146489e3c8ea7f7a52cb14474070))
- We have updated the Confirmation API to reflect its usage as a dialog. The composable is now called `ConfirmationDialog`, with associated updates to the naming of colors and defaults classes. We have also renamed the `show` parameter to `visible` for compatibility with other Compose animation APIs. In addition, we have made `ConfirmationDialogContent`, `SuccessConfirmationDialogContent`, `FailureConfirmationDialogContent` available for situations where developers need to customize the intro/outro dialog animations. ([Iaeb33](https://android-review.googlesource.com/#/q/Iaeb33d3e9bb5c802ddb4b4c10ff564681772bb83))
- We have updated `CircularProgressIndicatorContent` to `CircularProgressIndicatorStatic` (the non-animated variation of `CircularProgressIndicator`) so that it can now be used to build `CircularProgressIndicator` with custom animations. ([I1346f](https://android-review.googlesource.com/#/q/I1346f787f2d5c7394b5db88f6c89cfa749409713))
- We have fixed the parameter ordering on the `ArcProgressIndicator`, putting the modifier parameter first ([I4656a](https://android-review.googlesource.com/#/q/I4656a4de5af568844527bef6d2a2cca3576d6cc9))
- Improved the `SwipeToReveal` API to receive a text slot parameter for the labels of the actions (except secondary action) and to remove label parameters from undo action ([I5b3db](https://android-review.googlesource.com/#/q/I5b3db2932d289be8ce084714390d62c1f52fdf67))

**Bug Fixes**

- We have fixed a bug where `LongPress` haptics were triggered more than once in `Button`, `Card`, `IconButton`, `TextButton` ([Ia8b0f](https://android-review.googlesource.com/#/q/Ia8b0f52581934fbf3448df6609111c3ebfb55c94))
- Changes to the UX of `AlertDialog` - on large screens the confirm and dismiss buttons are now smaller. There is also increased spacing below the confirm and dismiss buttons. ([I4f066](https://android-review.googlesource.com/#/q/I4f06620d79f6265e012791fb080d65d7cd9e4a89))
- We have changed the animation specs of the action button label of the `SwipeToReveal` component. ([Ib87fb](https://android-review.googlesource.com/#/q/Ib87fb2557d31964bd1451bed9aced2bdf0c53f07))
- Changed `SwipeToReveal` to expand the container at the same time that the text is displayed. ([I44cf8](https://android-review.googlesource.com/#/q/I44cf8bd1cb93e02cac49b6399685164b70956174))
- Improved `SwipeToReveal` to perform haptic feedback when the swipe passes the threshold where the primary action is committed. ([I23efe](https://android-review.googlesource.com/#/q/I23efe779286f40922b7d620aa245d96429ca838d))
- We have updated `SwipeToReveal` to display ellipsis on text overflow by default, for primary and undo actions. ([I71f5a](https://android-review.googlesource.com/#/q/I71f5ad74e5c3dc78d84bf909fff3b7db90aeb6a9))
- We have fixed an issue causing jitter on `ButtonGroup` animations. ([I63f8f](https://android-review.googlesource.com/#/q/I63f8f7ab52153a29f56ffb8db007d300a08fbca9))
- We have added text semantics to `AnimatedText` ([I6063c](https://android-review.googlesource.com/#/q/I6063cbed541e794cc5bdaf1490fe30f906cbbbdf))
- Dialog now resets background scaling when the dialog is removed from the composition (without this fix, the launching screen may have been left in a scaled down state) ([Id24ac](https://android-review.googlesource.com/#/q/Id24ac4160b58c23d4cd09c8027e0654087742951))
- We have added a shape morph animation to the buttons in the Stepper component ([Id6ed3](https://android-review.googlesource.com/#/q/Id6ed3477bd40807821e793477d067e89f513828c))

### Version 1.0.0-alpha30

December 11, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha30` is released. Version 1.0.0-alpha30 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/wear/compose/compose-material3).

**API Changes**

- The `scrollTransform` modifier for `TransformingLazyColumn` was refactored which triggered an API change. ([I0c6dc](https://android-review.googlesource.com/#/q/I0c6dc9a7ab2a12a3ebf33f822179145a9ba4c7d9))
- We have updated `IconToggleButtonShapes` and `TextToggleButtonShapes` to have two different shape parameters `uncheckedPressed` and `checkedPressed` ([I85dbd](https://android-review.googlesource.com/#/q/I85dbd069e3de01b50deac5d923bebfc2d081e6fd))
- Invalid month/day options are now visible in the `DatePicker`, with a new `invalidPickerContentColor`, when using `minDate` or `maxDate`. ([If4541](https://android-review.googlesource.com/#/q/If4541e0c2d64ab0a94e11a1bda6efa1277f8ddbc))
- We have updated the `Stepper` API to provide `increaseIcon` and `decreaseIcon` slots - the content for these can be built as usual from the Icon composable. ([Id35da](https://android-review.googlesource.com/#/q/Id35dad8eb3829a80c6acf46d7a7ae9650bcbfbac))
- We have updated `dynamicColorScheme` by removing the optional `defaultColorScheme` parameter and now returning nullable `ColorScheme`. This means that the caller must explicitly handle the fallback case when a dynamic color scheme is not provided. ([I6d62e](https://android-review.googlesource.com/#/q/I6d62ea8d01175b2a95772b771a469bed96071231))
- We have updated the icon sizes in `ButtonDefaults` for use with `CompactButton`. A `CompactButton` containing only an icon should use `ButtonDefaults.SmallIconSize = 24.dp`, whereas a `CompactButton` containing both icon and text should use `ButtonDefaults.ExtraSmallIconSize = 20.dp`. It is recommended that `CompactButton` wrap its content (rather than filling the max width) and samples have been updated to show that. ([I0582c](https://android-review.googlesource.com/#/q/I0582cad17c66743a1df5d87adbe2cf89b6fda8fb))
- We have added `EdgeButtonDefaults` with recommended icon sizes for the 4 different `EdgeButtonSizes`. Also, updated the `EdgeButton` layout so that it has slightly larger bottom padding than top padding, which improves appearance for both Icon and Text content. ([Id772a](https://android-review.googlesource.com/#/q/Id772a6ba9f0259c50daad54a8a701fcfd3d3d68f))
- We have added motion to `LinearProgressIndicator` and exposed `LinearProgressIndicatorContent` which provides the visual content without animations. ([Idee99](https://android-review.googlesource.com/#/q/Idee9941c34444a2a695a0ab2171306085b7d5abd))
- We have added a new `CircularProgressIndicatorContent` composable to display the visual content of `CircularProgressIndicator` without animations. ([Ie33d4](https://android-review.googlesource.com/#/q/Ie33d4492d0d1f15dac976716760d6e118c5f5e8e))
- `TransformingLazyColumn` newly provides the composition local `LocalTransformingLazyColumnItemScope` which `Card`s, `Button`s and `ListHeader`s now use to automatically morph when placed inside a `TransformingLazyColumn`. Callers can disable automatic morphing using the new `TransformExclusion` wrapper. ([I1652f](https://android-review.googlesource.com/#/q/I1652f87699096f3de1cef247d714099a105647a2))
- We have updated the type of `ButtonDefaults.shape` to `RoundedCornerShape` ([Iccdf2](https://android-review.googlesource.com/#/q/Iccdf254dc1f3eb838d7098638666fcbf1ebdfb85))

**Bug Fixes**

- We have fixed a bug to respect existing alpha on background for `TimeText` ([I1eb60](https://android-review.googlesource.com/#/q/I1eb60d1ba1b165c5cb65c2c2400ac860cb8b884c))
- We have set `TextMotion` to `Animated` by default in our typography, to avoid text jitter due to snapping letter glyphs to pixel boundaries during scaling operations. ([I626fa](https://android-review.googlesource.com/#/q/I626fa13dd827e62311e51e7ccd49eda3e53e06f7))
- We have updated the appearance of the `ScrollIndicator` by increasing width and gap size, to improve visibility. ([Ied7cb](https://android-review.googlesource.com/#/q/Ied7cbcd23d60b53b57d338ad5033b8de8208e688))
- We have fixed a bug on `Modifier.scrollTransform` when adding/removing/moving items. ([I6830f](https://android-review.googlesource.com/#/q/I6830fe9d9df3645a822eb3e1b352aad1a1def2d6))
- We have fixed a round button animation issue for short taps (previously, the minimum animation duration was not always observed). ([I757a7](https://android-review.googlesource.com/#/q/I757a7bd0f4c8b07572b8a5d24d5660cde6648ff6))
- We have updated the sweep angle for `LevelIndicator` to 20% (i.e. 72 degrees). ([Idde5c](https://android-review.googlesource.com/#/q/Idde5c5cfcda06eab99079a285eb8132ff4f13751))
- We have fixed `ScrollIndicator` positioning when `ScalingLazyColumn` was used with `AutoCenteringParams`. ([I387dd](https://android-review.googlesource.com/#/q/I387dd3de162e485d0c5658dbb383a888dc9ed05c))
- We have updated the colors and typography for `ListHeader` and `ListSubHeader`. Also the colors for the toggle controls on `CheckboxButton` and `SwitchButton`. ([I39817](https://android-review.googlesource.com/#/q/I3981715cfd1073a43a574d61ed7249c6a02221e3))
- We have fixed `ScrollIndicator` positioning in `LazyColumn` and `ScalingLazyColumn` with `ContentPadding`. ([I2bc51](https://android-review.googlesource.com/#/q/I2bc51a0d5b12916e3d560bf9b2e9119601fb21a9))
- We have fixed a bug seen in `OpenOnPhoneDialog` progress animation by using the new `CircularProgressIndicatorContent`. ([I3e443](https://android-review.googlesource.com/#/q/I3e44325b2c452fd2f86b26affcd727ed416e2973))
- We have updated the `HorizontalPagerScaffold` and `VerticalPagerScaffold` to disable animations when reduce motion is enabled ([Iaaf68](https://android-review.googlesource.com/#/q/Iaaf681ea58b2869a5911a6878af82061bc939b64))
- We have implemented a separate animation for circular progress indicators when progress reaches over 100%. ([I47135](https://android-review.googlesource.com/#/q/I4713589deb69b42502b799d921ef38a2ffc04ec0))
- We have fixed a bug where `EdgeButton` could be drawn with an incorrect shape in Pager components ([I91db9](https://android-review.googlesource.com/#/q/I91db9e462a13e348e4b3a7ca1a6610fcbb4c9898))

### Version 1.0.0-alpha29

November 13, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha29` is released. Version 1.0.0-alpha29 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/wear/compose/compose-material3).

**API Changes**

- We have updated `TimeText` to provide default content that shows the time. ([Id23b3](https://android-review.googlesource.com/#/q/Id23b37f88d2ad6696cd61d8d9cfa4c04fd634049))
- We have simplified the `ScrollInfoProvider` for `PagerState` by removing the `orientation` parameter, which is no longer needed. The new behavior is for `TimeText` to remain in place for both horizontal and vertical paging. ([I71767](https://android-review.googlesource.com/#/q/I71767df0f68f4109e8ac79aa37a075ff4b3179a3))
- `LocalHapticFeedback` now provides a default `HapticFeedback` implementation when the Vibrator API indicates that haptics are supported. The following have been added to the `HapticFeedbackType` - `Confirm`, `ContextClick`, `GestureEnd`, `GestureThresholdActivate`, `Reject`, `SegmentFrequentTick`, `SegmentTick`, `ToggleOn`, `ToggleOff`, `VirtualKey`. Wear Compose long-clickable components such as `Button`, `IconButton`, `TextButton`, and `Card` now perform the `LONG_PRESS` haptic when a long-click handler has been supplied. ([I5083d](https://android-review.googlesource.com/#/q/I5083db2ce3619189c0a3793de9f535d996029c75))

**Bug Fixes**

- We have updated the motion for Confirmations. ([I04bff](https://android-review.googlesource.com/#/q/I04bff60587cdf8dcfd8dc23635382782e0bd4d6f))
- We have updated the minimum API dependency to 1.7.4 for Compose libraries. ([I88b46](https://android-review.googlesource.com/#/q/I88b4613796d9c9ccccf3f3a1cf0efd3ad6ce2f41))
- New motion was added for the `OpenOnPhone` dialog. ([I1e10a](https://android-review.googlesource.com/#/q/I1e10ae52bb6b2da225d203a116a9ce08675b3837))
- We have fixed a bug in the `LevelIndicator` so that it is now correctly displayed with the level is zero. ([Ie95a4](https://android-review.googlesource.com/#/q/Ie95a40b1e91275ba029319abcf239ec7a97083a5))
- We have updated the `HorizontalPageIndicator` and `VerticalPageIndicator` animations. ([I5c8f3](https://android-review.googlesource.com/#/q/I5c8f3f73ff70f71f6821de7a018c1cf084548091))
- We have added a shrink-to-dot animation to the indeterminate `ArcProgressIndicator`. ([I9fd51](https://android-review.googlesource.com/#/q/I9fd5148d52540ba920d39dd7c1fa187a98382b7c))

### Version 1.0.0-alpha28

October 30, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha28` is released. Version 1.0.0-alpha28 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/wear/compose/compose-material3).

**API Changes**

- We have added an arc variation on the indeterminate circular progress indicator ([I2efc1](https://android-review.googlesource.com/#/q/I2efc1df6f9cde6bbee25505b0a45c43246de6986))
- We have made public the `AlertDialogContent` and `Dialog` composables that make up the `AlertDialog` API, so that it is possible to add customization if necessary (such as customizing `AlertDialog` animation whilst keeping the recommended content layout). In addition, we have added `Modifier` and `Color` parameters to the `EdgeButton`, `ConfirmButton` and `DismissButton` members of `AlertDialogDefaults`. ([I4eb71](https://android-review.googlesource.com/#/q/I4eb71abb2f29170154475aa707c915b55b2fec0e))
- We have updated the `Placeholder` API as follows: renamed `PlaceholderState.startPlaceholderAnimation` to `PlaceholderState.animatePlaceholder`, `PlaceholderState.isShowContent` to `PlaceholderState.isHidden`, and `PlaceholderDefaults.shape` to `PlaceholderDefaults.Shape`; renamed the `painter` parameter in `painterWithPlaceholderOverlayBackgroundBrush` to `originalPainter`; changed visibility of `PlaceholderState.placeholderProgression` from public to internal and renamed it to `placeholderShimmerProgression`; added placeholder animation duration constants to `PlaceholderDefaults`. ([Ie5a59](https://android-review.googlesource.com/#/q/Ie5a59415e93c4ff0c8f87940ab48990d250941e1))
- We have updated the `EdgeButton` API as follows: renamed the parameter on `ScreenScaffold` from `bottomButton` to `edgeButton`; made `EdgeButtonSize` a value class. ([Ieef15](https://android-review.googlesource.com/#/q/Ieef158ef737bf89a3acc22ff7cadf7929672167e))
- We have changed the visibility of `copy()` to public in wear material3 Colors classes ([I0287f](https://android-review.googlesource.com/#/q/I0287ff4d034bcb64d8ac96e804e288a8d161b7af))

**Bug Fixes**

- Added minimum animation duration for `IconToggleButton` and `TextToggleButton` on click ([Ieb333](https://android-review.googlesource.com/#/q/Ieb333b849bcf0bd44ce3834cef71428d0aa14055))
- Added minimum duration on `IconButton` and `TextButton` shape animation ([Iebcee](https://android-review.googlesource.com/#/q/Iebcee6af7d6620af372cb081012085ad8a9bd40b))
- Corrected the repeat option state of `DatePicker`. ([I3587c](https://android-review.googlesource.com/#/q/I3587c44541f655b48bc5240dc47c8a276c7aa38d))
- Added motion for Alert and Confirmation dialogs. ([I173b1](https://android-review.googlesource.com/#/q/I173b19c21fe1386c0336530ad8b9c881a401e20c))

### Version 1.0.0-alpha27

October 16, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha27` is released. Version 1.0.0-alpha27 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/wear/compose/compose-material3).

**API Changes**

- We have updated the `ScreenScaffold` and `ScrollIndicator` following the renaming of Wear Compose Foundation `LazyColumn` to `TransformingLazyColumn`. ([I0608b](https://android-review.googlesource.com/#/q/I0608b1772ce548b97328f4fa888dfd44cb1306ae))
- `EdgeButton`'s `preferredHeight` parameter has been renamed to `buttonSize` and its value can only be chosen from 4 constants in the newly introduced `EdgeButtonSize` value class. ([Icdd70](https://android-review.googlesource.com/#/q/Icdd7064874afdd8c68bd9e97cd936c7b54145559))
- We have changed the naming of `ListSubheader` to `ListSubHeader` and added publicly accessible default values for `ListHeader` and `ListSubHeader`. ([I96730](https://android-review.googlesource.com/#/q/I9673008ab833ca249d445ac3fc240ca8f25e473f))
- We have added new `HorizontalPagerScaffold` and `VerticalPagerScaffold` components for Wear which provide new animations and coordination between time text and page indicator components. ([Iff7d0](https://android-review.googlesource.com/#/q/Iff7d026c30a147ca7a40b372dc99cece2ad30665))
- We have added rotary support to `HorizontalPagerScaffold` and `VerticalPagerScaffold`, enabling users to navigate pagers using rotary input devices. ([I9770d](https://android-review.googlesource.com/#/q/I9770d94d93d745228694c50c58360c66a4b82257))
- We have made `MotionScheme` API changes to simplify the usage and improve consistency. Removed inlined remember functions and moved the built-in Motion Schemes to a dedicated MotionScheme companion object. Renamed the `standardMotionScheme` and the `expressiveMotionScheme` to standard and expressive. ([I5fd45](https://android-review.googlesource.com/#/q/I5fd45ba14b76e5ef417e88b6696183236b83c500))
- We have added support for a dynamic color scheme based on system colors. ([I073e9](https://android-review.googlesource.com/#/q/I073e9acdbe246030c7359dc41b8c64bf08ce7199))
- We have updated the Stepper to the latest UX specs. ([I622bb](https://android-review.googlesource.com/#/q/I622bb721b385543e3b9654a049dd42d649176988))

**Bug Fixes**

- We have updated typography and paddings for Card components. ([I3ae48](https://android-review.googlesource.com/#/q/I3ae48efdb6d3c694c95788cefd2af968fd6fe9e5))
- We have changed the padding in `AlertDialog` between Confirm/Dismiss buttons and the rest of the content from 8dp to 12dp according to UX specs ([Ie55f0](https://android-review.googlesource.com/#/q/Ie55f06be54c05b2a5bd229c44729c1358419f4a0))
- We have updated the color opacity for the Slider component. ([Idb383](https://android-review.googlesource.com/#/q/Idb383cb774b5d612aaa0d0f63e596625cfaa2d4d))

### Version 1.0.0-alpha26

October 2, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha26` is released. Version 1.0.0-alpha26 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/wear/compose/compose-material3).

**API Changes**

- We have updated the API and appearance of `HorizontalPageIndicator` and added `VerticalPageIndicator` for use with `VerticalPager` ([Ic9309](https://android-review.googlesource.com/#/q/Ic9309eb67f73b9d48fcd35087a6452e11f23fa2e))
- `AlertDialog` now supports the ability to omit the default bottom button from the button stack variation, for custom layouts in which EdgeButton is not required. ([I34fa9](https://android-review.googlesource.com/#/q/I34fa93b55b1041959a6a06f63ee270446992e2be))
- We have added a `SwipeToReveal` component for Wear Material 3 ([Ic38b2](https://android-review.googlesource.com/#/q/Ic38b2a0ead09beaf2314b17eb0c02dd2b0f22419))
- We have added support for bi-directional swiping in `SwipeToReveal`, for rare cases where the current screen does not support swipe to dismiss. The default is still to swipe-to-reveal only on right-to-left swipes and it is strongly advised to respect the default behavior to avoid conflict with swipe to dismiss. ([Ifac04](https://android-review.googlesource.com/#/q/Ifac04be22f302315ff1cd2160a44c24c82f29612))
- We have renamed `EdgeButton`'s `buttonHeight` parameter to `preferredHeight`. ([I4fab3](https://android-review.googlesource.com/#/q/I4fab3926384cdff5a82574acfcc8a5ade290539e))
- The Kotlin version has been updated to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))
- We have renamed `OpenOnPhoneDialogDefaults.Icon` to `OpenOnPhoneDialogDefaults.OpenOnPhoneIcon` to avoid clashing with `Icon`([I0f391](https://android-review.googlesource.com/#/q/I0f391a8945723bc6647ff3f7d6fda97e9e453883))
- We have added support for `ScrollIndicator` in `LazyColumn`. ([Ia546a](https://android-review.googlesource.com/#/q/Ia546a61ed40616d774509a31bce9dc4c6a8ee3f5))
- We have updated default values for `TextToggleButton` and `IconToggleButton`. ([I7aaa9](https://android-review.googlesource.com/#/q/I7aaa9980b8e5d21d8bc44882feebb3a6ee479c1f))
- We have simplified the `Picker` and `PickerGroup` API. ([Id0653](https://android-review.googlesource.com/#/q/Id065352238dc9318d7bbb738fd7d7020e9358cdc))
- We have added `CardDefaults.Shape` and `CardDefaults.Height`, which (being tokens) were otherwise private to developers using the library. ([I1594a](https://android-review.googlesource.com/#/q/I1594a5907bee183eb2183dec2e85e791c6dda3be), [b/347649765](https://issuetracker.google.com/issues/347649765))
- We have renamed the progress parameter for the binary segmented circular progress indicator to `segmentValue`. ([Ib72d9](https://android-review.googlesource.com/#/q/Ib72d913de07f54a9f7d31fa2c2339a9a4af1491b))
- We have updated the colors and layout for Slider. ([Ic3eec](https://android-review.googlesource.com/#/q/Ic3eec615ce17a02b8cb92f253f12fd547ecfdf27))

**Bug Fixes**

- We have updated the `openOnPhone` icon animation ([I66f85](https://android-review.googlesource.com/#/q/I66f856678de177954c078bfbcf23727befd17939))
- We are now using Google Symbols icons in `Slider`, `TimePicker` and `DatePicker`. ([I46c7c](https://android-review.googlesource.com/#/q/I46c7ca7f34ae6ed28b76ab28a8c86376a2755d4c))
- We have updated the paddings in `Confirmation` and `OpenOnPhoneDialog`. ([Iaa82e](https://android-review.googlesource.com/#/q/Iaa82ee494777b09e4316c486189680c45079518e))

### Version 1.0.0-alpha25

September 18, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha25` is released. Version 1.0.0-alpha25 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..0431b84980e97d6bafdfda7c9038bc4d9529564f/wear/compose/compose-material3).

**API Changes**

- We have added an Indeterminate circular progress indicator. ([I427a7](https://android-review.googlesource.com/#/q/I427a7af6d8e9f7de6465e18f010f4b6880ef0b5a))
- We have added support for progress overflow (\>100% progress) for both the `CircularProgressIndicator` and the `SegmentedCircularProgressIndicator`. When the progress exceeds 1.0, this will be indicated by the new `overflowTrack` color. ([Iaaa3d](https://android-review.googlesource.com/#/q/Iaaa3d4da94307062cd92916be09130bae63afe6a))
- The round `IconToggleButton` and `TextToggleButton` now support a new shape animation variation, in which different shapes represent checked, unchecked and pressed states. The earlier animated shape variation for the just pressed state continues to be supported. ([I29f03](https://android-review.googlesource.com/#/q/I29f033f2f3601c03972252865b8e2da24fb1d630))
- We have removed support for using `EdgeButton` with `Column`, due to the need to specify the `EdgeButton` height explicitly in `ScreenScaffold`. ([Ie353d](https://android-review.googlesource.com/#/q/Ie353de35ca447165e315638190a30bfb533436ce))
- We have added support for the Wear Compose `LazyColumn` with our `ScreenScaffold` (and added an implementation of `ScrollInfoProvider` for `LazyColumnState`). ([Ib8d29](https://android-review.googlesource.com/#/q/Ib8d2946c22fe8279d08b0f8fc9029cdf5b8e0423))
- We have combined `LocalTextMaxLines`, `LocalTextAlign`, `LocalTextOverflow` into a single `LocalTextConfiguration` composition local to provide a more scalable solution going forwards. ([I5edbc](https://android-review.googlesource.com/#/q/I5edbc2caf74415a7a40b69c8710e059e7d168324))
- We have added arc-large as an additional typescale, reserved for short header text strings at the very top or bottom of the screen, like in Confirmation overlays. ([I60e3e](https://android-review.googlesource.com/#/q/I60e3e7a03658230a4f075df55b0e2d2ff0263dc4))
- We have added defaults to Button for recommended large and extra large icon sizes and content padding. ([I84675](https://android-review.googlesource.com/#/q/I846759e195384b56656feb0244a86ca3bdc7248c))

**Bug Fixes**

- We have updated the colors for `IconButton` and `TextButton`. ([I48324](https://android-review.googlesource.com/#/q/I483249cc4f80973e2587dac253f4ae93b6c8d078))
- We have changed the base Button overloads to be vertically center-aligned for consistency with other overloads. To restore the previous behavior, use `Modifier.align` from the `RowScope`. ([I66e57](https://android-review.googlesource.com/#/q/I66e572d7a2c0f41343cb94276f5bcab1b194b18b))

### Version 1.0.0-alpha24

September 4, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha24` is released. Version 1.0.0-alpha24 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/wear/compose/compose-material3).

**API Changes**

- We have added a Motion scheme into the Material3 theme. This will be used by components across the library to apply animation specifications such as springs for expressive motion. ([I54ff3](https://android-review.googlesource.com/#/q/I54ff3a7cf0cb4d7315a065f691bf2f9d4a4520a7))
- We have added `AppScaffold` and `ScreenScaffold` components to the Material3 library, which include functionality to coordinate layering and transitions of `TimeText` and `ScrollIndicator`. `AppScaffold` provides a top level of scaffold components that sit on top of all screens. As such, adding `TimeText` to the `AppScaffold` allows it to remain in place while swiping between screens. Screens can themselves override or hide the time text. `ScreenScaffold` provides a slot for the `ScrollIndicator` and automatically animates the scroll indicator when scrolling, including timeout to hide the scroll indicator after inactivity. ([I047d6](https://android-review.googlesource.com/#/q/I047d639623ce9c54af9dabd86728107c8e1af422))
- We have added `ScrollIndicator` featuring the new Material3 design. It has a fixed thumb size based on initial list contents, in order to avoid size variations when lazy content is loaded into the list. ([Ic228d](https://android-review.googlesource.com/#/q/Ic228d48ed349dabb9c1fa02b949f07e3a6a4781b))
- We have changed the `ScrollAway` API such that `ScreenStage` is a value class instead of an enum class, to allow for additional stages to be added as needed going forwards. ([I48c93](https://android-review.googlesource.com/#/q/I48c9398b577d42c9792009018d8f494e2a33b479))
- We have added `EdgeButton`, a distinctive Wear-specific button with a shape that follows the curvature of the bottom of the screen ([I16369](https://android-review.googlesource.com/#/q/I16369a6d41fadde897bce87ddd0300caae90fd89))
- We have added a new slot to the `ScreenScaffold` for a bottom button (such as `EdgeButton`), that will be shown and resized depending on the scrolling content ([I032eb](https://android-review.googlesource.com/#/q/I032eb44f3a38f8de3b6c6082babf837ad7df2a2a))
- We have added `Modifier.scrollTransform` and `Modifier.targetMorphingHeight` to add Material3 motion effects to items in `LazyColumn`. ([Ie229a](https://android-review.googlesource.com/#/q/Ie229a1aa8b3411881367fbe1f0c1ee3a57c39c91))
- We have added `SegmentedCircularProgressIndicator` as a variation on `CircularProgressIndicator`. The segmented variation either shows a single progress value across all segments or shows each segment as being on/off. ([I6e059](https://android-review.googlesource.com/#/q/I6e05980ba823f00f8b7640129bbd4fa1c8fcfdd8))
- We have added `LinearProgressIndicator` as an alternative to the existing `CircularProgressIndicator`. ([I89182](https://android-review.googlesource.com/#/q/I891827cc47667308393cfc7766b2d117806ab7f2))
- We have added `AlertDialog`, providing layouts for presenting important prompts to the user. Variations are included for either a pair of confirm/dismiss buttons or a single bottom button (typically an EdgeButton) below a stack of options. Both variations have slots for icon, title and additional text to provide further details. ([Ieb873](https://android-review.googlesource.com/#/q/Ieb873637e1ce1a554a9ae01c7ab7a72c63650c19))
- We have added `OpenOnPhoneDialog`, which should be used to indicate an action that will continue on the user's phone. `OpenOnPhoneDialog` is dismissed after a specified timeout. ([I978fd](https://android-review.googlesource.com/#/q/I978fdd711362f808cac89da4c15fce337ed100bc))
- We have added `Confirmation`, a dialog component that has slots for an icon and either curved or linear text. Specific variations are provided for success/failure messages. Confirmations are automatically dismissed after a timeout. ([Ib43e8](https://android-review.googlesource.com/#/q/Ib43e8d613847d334bcb079c07806612526f63983))
- We have added a background to `TimeText` to mitigate issues where the underlying content and the `TimeText` overlapped, and obscured the time. ([Ia11fd](https://android-review.googlesource.com/#/q/Ia11fd1c2a41630620c30d4c46b7e8c54fd659691))
- We have added `LevelIndicator`, which shows the value of a setting such as volume, and can be used with the existing `Stepper` component to construct a volume screen. `LevelIndicator` is similar to `ScrollIndicator`, but is displayed on the opposite side of the screen and has a wider stroke width and different indicator color by default. ([I8a4ac](https://android-review.googlesource.com/#/q/I8a4ac3d8ee7e06a1d73642aeee731ecc29298220))
- We have added `TimePicker`, with layouts for 24 hour time (with or without seconds), or 12 hour time with am/pm selection. ([Ia5124](https://android-review.googlesource.com/#/q/Ia5124f9e5aab57c5f7a530e5ed55184f86fe579d))
- We have added `DatePicker`, with configuration for column ordering (i.e. day-month-year, month-day-year or year-month-day) and optional min/max dates. ([Ibf13b](https://android-review.googlesource.com/#/q/Ibf13b15b750dc02e7c838f5d1791ad446464d5a7))
- We have added a weight parameter to the `TimeText`'s `text` function. In cases where TimeText is made up of more than one text element, this allows control over how the space is distributed. ([I36700](https://android-review.googlesource.com/#/q/I3670007378ce6d66d0d79424a1a95b5b2ac8ca76))
- We have added `RadioButton` and `SplitRadioButton` - these components simplify the previous API by combining both the (Split)`SelectableButton` and the child radio control ([If7ae8](https://android-review.googlesource.com/#/q/If7ae8389f0315715c3ba00cd97530eca47f15d0d))
- We have added `CheckboxButton` and `SplitCheckboxButton` - these components simplify the previous API by combining both the (Split)`ToggleButton` and the child Checkbox control ([Ia8f70](https://android-review.googlesource.com/#/q/Ia8f709ffee3fa93d697c945836d59391f4f25bd0))
- We have added `SwitchButton` and `SplitSwitchButton` - these components simplify the previous API by combining both the `(Split)ToggleButton` and the child Switch control ([I0d349](https://android-review.googlesource.com/#/q/I0d3491ce1fb05d1fb83dee2538e7613d7938815c))
- We have updated `AnimatedText` documentation to explain overshooting behavior. ([Iff30a](https://android-review.googlesource.com/#/q/Iff30ada5cd37d6818cc3fbbf34abb6302734f11b))
- We have added `ButtonGroup`to combine 2 or 3 buttons such that button presses produce a coordinated animation. ([Ie27db](https://android-review.googlesource.com/#/q/Ie27db2fd01522caa9e8800b7296aaa4335dc14f3))
- We have added optional shape animation for `IconButton` and `TextButton` when pressed. ([Iffca5](https://android-review.googlesource.com/#/q/Iffca57bcabad6283f2192fc42101f968caa00e4b))
- We have added an additional color variation, `FilledVariant`, to `Button`, `IconButton`, `TextButton`, `CompactButton` and `EdgeButton` ([I65fc3](https://android-review.googlesource.com/#/q/I65fc3acf7589eacfc2280b028d83d1e352a100cc))
- We have added the `forcedSize` parameter to `ImageWithScrimPainter`, such that Button image backgrounds now maintain their component size by default. Setting the `forcedSize = null` adopts the `Painter.instrinsicSize` instead. ([Ic57af](https://android-review.googlesource.com/#/q/Ic57af1323c60a68ab6df859c3ecc348163417981))
- We have added long-click to Buttons ([Ib613d](https://android-review.googlesource.com/#/q/Ib613d75052d7b4d5d85cc1e7dca009505e427f9c))
- Long click support has also been added to `IconButton` and `TextButton`. ([I38891](https://android-review.googlesource.com/#/q/I38891ea0c0179d3c6ec380b1af4d00aa216dd347))
- Long click support has been added to Cards. ([I305d5](https://android-review.googlesource.com/#/q/I305d5005e98ece7424af6d9c690c5c844836ab5e))
- We have added `LocalTextMaxLines`, `LocalTextAlign`, `LocalTextOverflow` as `CompositionLocals` and used them as parameter defaults on `Text`. The composition locals can now be used by components such as `CheckboxButton`, `SwitchButton`, `RadioButton` to implement UX guidance, but the parameters can be overridden by developers if necessary. ([Iab841](https://android-review.googlesource.com/#/q/Iab841d8adde34a4aa92920e4372ce3493a8d638a))
- We have added `Placeholder` to help in masking the content of components like buttons \& cards until the data is loaded. ([I1a532](https://android-review.googlesource.com/#/q/I1a5328e0f4fd379b41cbbcea0e44025d3b5ffb2e))
- We have added `IconToggleButtonColors` and `TextToggleButtonColors` to replace the now removed `ToggleButtonColors`. ([Ie0bf1](https://android-review.googlesource.com/#/q/Ie0bf11419433e68e344e3c8de46d14eba2cb490f))

**Bug Fixes**

- We have updated `Button`, `FilledTonalButton`, `OutlinedButton`, `ChildButton`, `CompactButton` to use the new `CompositionLocals` `LocalTextMaxLines`, `LocalTextAlign`, `LocalTextOverflow` to implement UX guidance - these parameters can be overridden by developers on Text directly if necessary ([Ie51f7](https://android-review.googlesource.com/#/q/Ie51f7257db279c736766c451402e7bc94cbc46d2))
- We have changed the default stroke width of the `LevelIndicator` to `6dp` to differentiate it from the `ScrollIndicator` which has a stroke width of `4dp`. ([If6f63](https://android-review.googlesource.com/#/q/If6f63990d09de3fa3f00d542eaf404985a2bc68f))
- We have fixed an issue in `TimeText` so that larger sweep angles are supported. ([Ie489f](https://android-review.googlesource.com/#/q/Ie489f0eb36f7f3c0365759baf827a60810d1e8d0))
- Fixed an issue during `EdgeButton` recomposition. ([I4cdca](https://android-review.googlesource.com/#/q/I4cdca0c8de8e08928489e9f6d523301a4de3bc75))
- Corrected layouts of split toggle buttons when customized content padding is provided. ([Ia33d3](https://android-review.googlesource.com/#/q/Ia33d396d38c2103b22d832152533cf2132660a0d))
- Rounded up small progress values to at least the line width of the progress indicator. ([I3bd84](https://android-review.googlesource.com/#/q/I3bd849c3f8c27ea5ba63317907196f2343bdfa47))

### Version 1.0.0-alpha23

May 14, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha23` is released. Version 1.0.0-alpha23 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/wear/compose/compose-material3).

**API Changes**

- We have updated `ToggleButton` and `RadioButton` APIs such that disabled colors can be configured. ([If13a7](https://android-review.googlesource.com/#/q/If13a7869e543030d12c2abf38ceee2a23e7fe4bf))
- We have added a new `CircularProgressIndicator` for Material3. ([Ib3bd7](https://android-review.googlesource.com/#/q/Ib3bd7e32752ec8fceaa6bb1d5e52fdc7027a9528))

**Bug Fixes**

- We have fixed a bug where selectable buttons announced double tap to toggle when already selected. ([I7ed88](https://android-review.googlesource.com/#/q/I7ed88da3c5f36e6c7484e43d1b245fa5273620ca))

### Version 1.0.0-alpha22

May 1, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha22` is released. Version 1.0.0-alpha22 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..fbd1ac175922f44c69a13545d194066ee428b342/wear/compose/compose-material3).

**API Changes**

- We have updated the Material3 `ColorScheme`. ([I7b2b8](https://android-review.googlesource.com/#/q/I7b2b8f5feb5f6504ddc7d8690e93c3fe90799de2))
- We have updated the Material3 Switch - as well as some color changes, the tick now matches that used for the Checkbox. ([Icac7b](https://android-review.googlesource.com/#/q/Icac7bdbe6bbc1297ca2a76705f0ab7e8d26a7ebc))

**Bug Fixes**

- Update all integration demos to use new `rotaryScrollable` modifier. ([I25090](https://android-review.googlesource.com/#/q/I250903329c8a3115c5ccd1fa9fa7878295209abf))

### Version 1.0.0-alpha21

April 17, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha21` is released. Version 1.0.0-alpha21 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/wear/compose/compose-material3).

- This release was triggered due to a technical issue in the previous release that resulted in missing source jars. There are no new commits in this release.

### Version 1.0.0-alpha20

April 3, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha20` is released. Version 1.0.0-alpha20 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..02b55f664eba38e42e362e1af3913be1df552d55/wear/compose/compose-material3).

**Bug Fixes**

- We have adjusted the Ripple pressed and focused state alphas for contrast. ([I59f0a](https://android-review.googlesource.com/#/q/I59f0ad2674e88f9a23eae8fa265c764de2cc82ce))
- We have added spacing between primary and secondary labels in `Button`, `ToggleButton` and `RadioButton`, following the latest changes to typography styles and line heights. ([I2c0ba](https://android-review.googlesource.com/#/q/I2c0ba50b84bf3e00d5c85ecc36a6e98fc6c19651))

### Version 1.0.0-alpha19

March 6, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha19` is released. Version 1.0.0-alpha19 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/wear/compose/compose-material3).

**API Changes**

- We have added `TimeText` to the Wear Compose Material3 library. This component shows the current time (and additional status) at the top of the screen. The new, concise Material3 API avoids duplication between linear and curved content. ([I4d7c3](https://android-review.googlesource.com/#/q/I4d7c3330f94a055cff326b2f71e4e7b252bb3a5c))
- We have updated parameter names from `onSelected` to `onSelect` for `RadioButton`. ([I1a971](https://android-review.googlesource.com/#/q/I1a971db9ef5b7cc4c218edc8973d87cfb4602c1c))
- Tokenize `RadioButton` and `SplitRadioButton` and also refactor the existing methods to reduce the amount of `CompositionLocal` lookup by adding cached instances of colors, and making methods of `RadioButtonColors` and `SplitRadioButtonColors` internal. ([I02b33](https://android-review.googlesource.com/#/q/I02b33fe3153a7fe596d5f83b0c6464b4eb9de282))

### Version 1.0.0-alpha18

February 21, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha18` is released. [Version 1.0.0-alpha18 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/wear/compose/compose-material3)

**API Changes**

- We have refactored the defaults pattern for `CardColors`, `ToggleButtonColors` and `SplitToggleButtonColors` by creating cached instances internally and reducing the usage of `CompositionLocal`. ([If3fec](https://android-review.googlesource.com/#/q/If3fece36743a67fda21bb2c11533d70093568802))

### Version 1.0.0-alpha17

February 7, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha17` is released. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..ca2a8cf8da3a3502fccc593974f8085653e38261/wear/compose/compose-material3)

**API Changes**

- We have updated the Button API to use `buttonColors` by default and removed the duplicate `filledButtonColors`. ([I4fe3b](https://android-review.googlesource.com/#/q/I4fe3b136aeb435d35c629e4fa0ab32bd2931b72f))
- We have refactored default patterns for `ButtonColors`, `IconButtonColors` and `TextButtonColors` by creating a cached instance internally and reducing the usage of `CompositionLocal`. ([I5f51c](https://android-review.googlesource.com/#/q/I5f51c87cd5538f78a37318366580883fe8f9d63f))
- We have removed the overhead of `rememberUpdatedState` in Component specific color classes and marked accessor methods inside color classes as internal. ([If6571](https://android-review.googlesource.com/#/q/If657116447ba9a8c7079ca01a96d80e46af44367))

**Bug Fixes**

- We have updated `Modifier.minimumInteractiveComponentSize` to use `Modifier.node`. ([Iba6b7](https://android-review.googlesource.com/#/q/Iba6b72447e6ce95f323e77769ad65e6d8b962d84))

### Version 1.0.0-alpha16

January 24, 2024

`androidx.wear.compose:compose-material3:1.0.0-alpha16` is released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a8915c4ac4e4bfead52d6b42aaffaa87966ab38b..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/wear/compose/compose-material3)

**New Features**

- We have added `CompactButton`, which can use the same filled, filled tonal and outlined colors as Button.([I05df0](https://android-review.googlesource.com/#/q/I05df080969e73641c71515ef7ae7627fb93360d7))

**API Changes**

- We have added `RadioButton`/`SplitRadioButton` as containers for selection controls, such as the Radio control. This differs from the existing `ToggleButton` in that `RadioButton` is selectable (and operates within a selection group) whereas `ToggleButton` is toggleable (and is independent). ([I61275](https://android-review.googlesource.com/#/q/I612758b8625c45756e6a56d31c1008daac45fba3))
- We are removing `LocalContentAlpha` from the Wear Compose Material3 library for consistency with the Compose Material3 library. ([I49a0a](https://android-review.googlesource.com/#/q/I49a0a24345a87de25aba78733c6351ede53c921d))
- Wear material and wear material3 components exposing a `MutableInteractionSource` in their API have been updated to now expose a nullable `MutableInteractionSource` that defaults to null. There are no semantic changes here: passing null means that you do not wish to hoist the `MutableInteractionSource`, and it will be created inside the component if needed. Changing to null allows for some components to never allocate a `MutableInteractionSource`, and allows for other components to only lazily create an instance when they need to, which improves performance across these components. If you are not using the `MutableInteractionSource` you pass to these components, it is recommended that you pass null instead. It is also recommended that you make similar changes in your own components. ([Ib90fc](https://android-review.googlesource.com/#/q/Ib90fc2736d2311e467d7c2a3fef4df757afaf525), [b/298048146](https://issuetracker.google.com/issues/298048146))
- Adds new ripple API in `wear:compose-material` and `wear:compose-material3` libraries which replaces the deprecated `rememberRipple`. Also adds a temporary `CompositionLocal`, `LocalUseFallbackRippleImplementation`, to revert Material components to using the deprecated `rememberRipple/RippleTheme` APIs. This will be removed in the next stable release, and is only intended to be a temporary migration aid for cases where you are providing a custom `RippleTheme`. See developer.android.com for migration information and more background information behind this change. ([af92b21](https://android.googlesource.com/platform/frameworks/support/+/af92b215fa235f565a4b2e2612f195d67adf9a99))
- We have made minor improvements to the `HorizontalPageIndicator` api and its documentation. ([I60efc](https://android-review.googlesource.com/#/q/I60efcf96f5260a27de394682c5df2ace50e67c93))
- We have updated `ColorScheme` to be immutable, making individual color updates less efficient, but making more common usage of colors more efficient. The reasoning behind this change is that the majority of apps wouldn't have updating individual colors as a main use case. This is still possible but it will recompose more than before, in turn we significantly decrease the amount of state subscriptions through all of material code and will impact initialization and runtime cost of more standard use cases. ([Ibc2d6](https://android-review.googlesource.com/#/q/Ibc2d6d36f4bdd817c06f686cd1e3c210c2544b82))
- Updated `ToggleButton` and `SplitToggleButton` APIs to allow disabled colors to be customized. In addition, Material Design tokens are now used for color and typography values. ([If087c](https://android-review.googlesource.com/#/q/If087ca889ffa3fce5fac10cc813551838b6cfd03))
- Updated Button image background colors to use Material Design tokens. ([Iba215](https://android-review.googlesource.com/#/q/Iba21513fbc8f65a628cfa600785607db9f952bed))
- We have changed the `Checkbox`, `Switch` and `RadioButton` components to be display-only, by removing the click handling. These components are expected to be used in `(Split)ToggleButton` which handles the click, so the components are now more clearly indicated as display-only (and are not intended for standalone use on Wear). ([I2322e](https://android-review.googlesource.com/#/q/I2322ed56b42d364dfaa98e7ba72ff62b4fb5b9c3))

**Bug Fixes**

- We have added tokens for motion values of durations and easings in Wear Compose Material 3. ([I437cd](https://android-review.googlesource.com/#/q/I437cdff8bf33081b3d0930f4ca1d0631695cbb34))
- We have fixed a bug in the `ToggleButton`, `SplitToggleButton`, `Checkbox`, `Switch` and `RadioButton` so that accessibility announcements are not repeated (previously, semantic roles were duplicated). ([Ica281](https://android-review.googlesource.com/#/q/Ica281335ebabdf52577720e5cda72420adb90cbd))
- We have removed the materialcore layer for `CompactButton` to improve performance. ([7902858](https://android.googlesource.com/platform/frameworks/support/+/7902858b7a46c87a4f24f5da0111ed2a5d244bfc))

### Version 1.0.0-alpha15

November 15, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha15` is released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/wear/compose/compose-material3)

**API Changes**

- We have renamed the Foundation level `SwipeToDismissBox` to `BasicSwipeToDismissBox`. This makes the distinction clearer between the Foundation level component and the Material3 level `SwipeToDismissBox`. The latter pulls colors from the `MaterialTheme` to be used in scrims and delegates the remaining implementation to the `BasicSwipeToDismissBox`. ([Ibecfc](https://android-review.googlesource.com/#/q/Ibecfc1720eadd2d8e5e1c1cfd6832300775bffb1))

**Bug Fixes**

- We have removed the material-core layer for Material3 Button to improve performance. ([I55555](https://android-review.googlesource.com/#/q/I5555573520638dd3c7f0d202e048ae6fffde19e5))

### Version 1.0.0-alpha14

October 18, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha14` is released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/wear/compose/compose-material3)

**API Changes**

- We have removed the `indicatorStyle` parameter from the Material3 `HorizontalPageIndicator` - instead, it will follow the device screen shape (linear or round). ([I83728](https://android-review.googlesource.com/#/q/I83728bf6fd56805a7281e98e08cde5f58553a156))
- We have separated the colors for `SplitToggleButton` from those for `ToggleButton`, by adding a new `SplitToggleButtonColors` class. ([I78bee](https://android-review.googlesource.com/#/q/I78bee267eeca5a62c18874b7a8ae225685f08dbe))

### Version 1.0.0-alpha13

October 4, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha13` is released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..1f7407d4293384a1b91bc142880e3525048b3443/wear/compose/compose-material3)

**API Changes**

- We have added an optional Subtitle field to `TitleCard`. ([Ifc45a](https://android-review.googlesource.com/#/q/Ifc45a6b445b95d7e323336d84ff9626afc31d4b2))
- We have added Material Design color tokens for `TextButton`. ([I769dc](https://android-review.googlesource.com/#/q/I769dcd5878be96e2bea0d9768b56b767cbf38765))

### Version 1.0.0-alpha12

September 20, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/wear/compose/compose-material3)

**API Changes**

- We have updated `IconButton` to use Material Design tokens. ([I3f137](https://android-review.googlesource.com/#/q/I3f13723c96d2ed657344b417c93866d58bceddeb))
- We have updated `IconToggleButton` to use Material Design tokens. ([I7d263](https://android-review.googlesource.com/#/q/I7d2637fed5145b454c3eb53f539fd54ed8c9091c))
- We have made public the constructors of `CheckboxColors`, `RadioButtonColors`, `SwitchColors`. ([I82b73](https://android-review.googlesource.com/#/q/I82b735520ebd2b76aa11ba7d9730c854aee180cc))

### Version 1.0.0-alpha11

September 6, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/wear/compose/compose-material3)

**Bug Fixes**

- We update updated the typography for Material3 Cards to `TitleMedium`. ([I597bd](https://android-review.googlesource.com/#/q/I597bd10236b298339794f24ceef31a6dbd2a91c3))
- We have updated the typography and alignment for our Material3 `ListHeader` and `ListSubheader`. ([Ib5ceb](https://android-review.googlesource.com/#/q/Ib5ceb8b15ce694a6ce27a3598c696a640bb76566))

### Version 1.0.0-alpha10

August 23, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..3315f1ef094c312203fe26841287902916fbedf5/wear/compose/compose-material3)

**New Features**

- Add `HorizontalPageIndicator` in Wear Material3 library. ([Ifee99](https://android-review.googlesource.com/#/q/Ifee996864667def4d04905328cb5e6667037842a))

**API Changes**

- Update Buttons code to use Material3 design tokens. ([I92fe4](https://android-review.googlesource.com/#/q/I92fe413630961837831ba51d626ca9ac6dc8cece))
- Declaring Wear Material 3 Stepper and Slider APIs as experimental as the details of the user interface are still being finalized. ([I84d54](https://android-review.googlesource.com/#/q/I84d54e4f0e0e91d703307b95ecb4367d6375a5fc))
- We have removed the `ExtraSmall` sizes from the round `TextButton` and `TextToggleButton` as that size only applies to the `IconButton`. ([Ibc7d5](https://android-review.googlesource.com/#/q/Ibc7d5366929a19d5183cd6329e629ee89a82b9cb))

**Bug Fixes**

- We have updated the guidance on typography for TextToggleButton to use LabelLarge for LargeButtonSize ([Ib10fa](https://android-review.googlesource.com/#/q/Ib10fa3e188aab47cf2f8c32ccd8e2f56622f440c))
- We have updated the guidance on typography for TextButton to use LabelLarge for LargeButtonSize ([I8f3a7](https://android-review.googlesource.com/#/q/I8f3a798c57e3998730c8e30a7059c24ebd607e81))
- We have set the Card's minimum touch target to be 48dp for accessibility. ([Ieb9b1](https://android-review.googlesource.com/#/q/Ieb9b14d7e5f4b3611d7cdfc5e81d755e686dcccc))
- Add AppCard with image demo, removing AppCard with Background demo ([Id735f](https://android-review.googlesource.com/#/q/Id735f4325a0fa132244f52ec79102440eef7fa38))
- Fix a bug in round buttons where modifiers were not chained correctly. ([I5e162](https://android-review.googlesource.com/c/platform/frameworks/support/+/2697934))

### Version 1.0.0-alpha09

August 9, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/wear/compose/compose-material3)

**New Features**

- We have added `ToggleButton` for material3 ([I6bed6](https://android-review.googlesource.com/#/q/I6bed63f4227567f813e0d0741abd4e3652e8626e))

**API Changes**

- We have turned on the `FloatRange` annotation as API constraints , which were previously stated in comments. ([Icb401](https://android-review.googlesource.com/#/q/Icb401745b75b2cdda25fa4bdfbe2f1707f8da08e))
- We have updated the typography for Wear Material3 to adhere to the latest Material3 guidelines. ([I1bad6](https://android-review.googlesource.com/#/q/I1bad6d47fa6a655efd6d3aa5dfa77f71e28a0fde))

**Bug Fixes**

- We have updated the colors for `Button`, `IconButton` and `TextButton` in line with Material3 design. ([Ib2495](https://android-review.googlesource.com/#/q/Ib24954145bc5440092cc2ac7dd18d3bc4fd4b756))
- We have fixed checkbox tick visibility in disabled states. ([Ib25bf](https://android-review.googlesource.com/#/q/Ibd820b96a260ce863a6a3d49bcd86f7a948c6620))

### Version 1.0.0-alpha08

July 26, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/wear/compose/compose-material3)

**New Features**

- We have added the following selection controls for Material3 - `Switch`, `Checkbox`, `RadioButton`. ([Ib918c](https://android-review.googlesource.com/#/q/Ib918caf8afcc96b280efc3b99ea31ad7e870522b))
- We have added `IconToggleButton` and `TextToggleButton` to Material3, a circular toggle button with a single slot for icon and text respectively. For different sizes of `ToggleButton`, we recommend using `Modifier.touchTargetAwareSize` with the sizes provided in respective toggle buttons. ([I9f015](https://android-review.googlesource.com/#/q/I9f0157a37ca42988afc898eddff84d2b4a048926))
- We have added `ListHeader` and `ListSubheader` to our Material3 components. ([Ibaefe](https://android-review.googlesource.com/#/q/Ibaefe0204c4afbfd5dfa80565b1cce99cdd47391))
- We have added Material3 `SwipeToDismissBox`, which calls the new Foundation `SwipeToDismissBox` and supplies default color values from its theme. ([I275fb](https://android-review.googlesource.com/#/q/I275fbd752435e183fd99594ae16bca5a8c92f864))
- We have added the Material3 `InlineSlider` to Wear Compose. It allows users to make a selection from a range of values. The range of selections is shown as a bar between the minimum and maximum values of the range, from which users may select a single value. `InlineSlider` is ideal for adjusting settings such as volume or brightness. ([I7085f](https://android-review.googlesource.com/#/q/I7085f3340fcc76556fadb06ff81c598ae84eacdc))

**API Changes**

- We have updated the Shapes in Wear Material 3 theme to use `RoundedCornerShape` based instead of Shape. ([Idb133](https://android-review.googlesource.com/#/q/Idb133928caec559027d0151d96e86f955edccb4a))
- We have made the height constants for Button public ([Idbfde](https://android-review.googlesource.com/#/q/Idbfdecfdc391dd2591724d3e6ba9c34f0e20878a))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b), [b/287516207](https://issuetracker.google.com/issues/287516207))
- We have updated `InlineSliderColors` in Wear Compose Material 3 to have public constructor and public properties. ([I6b632](https://android-review.googlesource.com/#/q/I6b6326d898fc4d96078ecab413e21306c8f7c37d))
- We have updated all color classes in Wear Compose Material 3 to have public constructors and public properties. ([I17702](https://android-review.googlesource.com/#/q/I177024b33ad10c324871c75c25e64ecef480e895))
- We have made Button horizontal and vertical padding constants public. ([Ieeaf7](https://android-review.googlesource.com/#/q/Ieeaf7e002e40394df0b591e8ff1e8d92e55a061f))

**Bug Fixes**

- Button will now adjust its height to accommodate content that has grown due to large fonts for accessibility, when required ([Iaf302](https://android-review.googlesource.com/#/q/Iaf3026bfb19a261821878927b0e0e3aaacca57c1))
- We have updated a number of Button demos to address accessibility issues. ([I61ce9](https://android-review.googlesource.com/#/q/I61ce9c80437224e210d39be789d775163f140ca8))
- `Stepper` and `InlineSlider` now support repeated clicks on long press so that you can quickly increase/decrease value of `Stepper` and `InlineSlider` by holding the + or - buttons ([I27359](https://android-review.googlesource.com/#/q/I2735993c5721f8a4142b3ca09bca42364da69059))

### Version 1.0.0-alpha07

June 21, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df792c9ff86d87f538bab5d7f9dd9f56e2437b15..3b5b931546a48163444a9eddc533489fcddd7494/wear/compose/compose-material3)

**New Features**

- We have added the `Stepper` component to our Compose for Wear OS Material 3 library. This is similar to the previous Material version, but omits range semantics by default, following developer feedback. We provide `Modifier.rangeSemantics` the cases where range semantics are required. ([Ic39fd](https://android-review.googlesource.com/#/q/Ic39fddeb8f959bdff6aee0ee6b2cbe6c906feab8))
- We have added `curvedText` to our Compose for Wear OS Material 3 library. ([Ia8ae3](https://android-review.googlesource.com/#/q/Ia8ae307dd9ac16d3d11af599c56918204a30dc0d))

**Bug Fixes**

- We have update `wear.compose.foundation` to be an API dependency of `wear.compose.material3` ([I72004](https://android-review.googlesource.com/#/q/I72004e7a328438e2f0bc8822e0b8e45b5d7225e8), [b/285404743](https://issuetracker.google.com/issues/285404743))

### Version 1.0.0-alpha06

June 7, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/06ba27a6a7d155acd0b8eea379b0948333901d86..df792c9ff86d87f538bab5d7f9dd9f56e2437b15/wear/compose/compose-material3)

**Bug Fixes**

- We have updated `TextButton` to use the `toDisabledColor` extension function for correct disabled alpha values. ([I814c8](https://android-review.googlesource.com/#/q/I814c880d60429e2085db31836f13c50a94282235))

### Version 1.0.0-alpha05

May 24, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..06ba27a6a7d155acd0b8eea379b0948333901d86/wear/compose/compose-material3)

**New Features**

- We have added `TextButton` to Material3, a circular button with a single slot for text. For different sizes of `TextButton`, we recommend using `Modifier.touchTargetAwareSize` and `ExtraSmallButtonSize`, `SmallButtonSize`, `DefaultButtonSize` and `LargeButtonSizeIcon` provided in `TextButtonDefaults`. The default `TextButton` has no border and a transparent background for low emphasis actions. For actions that require high emphasis, use `filledTextButtonColors`; for a medium-emphasis, outlined `TextButton`, set the border to `ButtonDefaults.outlinedButtonBorder`; for a middle ground between outlined and filled, use `filledTonalTextButtonColors`. ([I667e4](https://android-review.googlesource.com/#/q/I667e4b7c85311f677de8332fc537f84148b18378))
- We have added `Card`, `OutlinedCard`, `AppCard` and `TitleCard` into the Wear Compose Material3 library. `AppCard` and `TitleCard` can also be given the outlined appearance using `CardDefaults.outlinedCardColors` and `CardDefaults.outlinedCardBorder`([I80e72](https://android-review.googlesource.com/#/q/I80e721a921d396fbbf5dc27b4bafd836fc188cb1))

**API Changes**

- We have moved the Button label parameter to the end to support trailing lambda syntax and removed the role parameter (as this can be overridden using `Modifier.semantics`). `ButtonColors` constructors are now public. ([Ie1b6d](https://android-review.googlesource.com/#/q/Ie1b6d55ea940e98ab1d41f863587df4b6554433a))

### Version 1.0.0-alpha04

May 10, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/wear/compose/compose-material3)

**New Features**

- We have added `IconButton` to Material3, a circular button with a single slot for icon/image. There are four variations: `IconButton`, `FilledIconButton`, `FilledTonalIconButton` and `OutlinedIconButton`. For different sizes of `IconButton`, we recommend using `Modifier.touchTargetAwareSize` and `ExtraSmallButtonSize`, `SmallButtonSize`, `DefaultButtonSize` and `LargeButtonSizeIcon` provided in `IconButtonDefaults`. We also provide `IconButtonDefaults.iconSizeFor` to determine the recommended icon size for a given button size. ([I721d4](https://android-review.googlesource.com/#/q/I721d46af2b1d2d17185cbcf530e831f03a53e47e))

### Version 1.0.0-alpha03

April 19, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/wear/compose/compose-material3)

**API Changes**

- We have added the Material 3 Button component - this is our stadium-shaped button and was formerly named Chip in the Wear Compose Material library (it has been renamed to Button for consistency with the Compose Material 3 library). The default Button has a filled background and there are button variations for `FilledTonal` (muted background), Outlined (transparent with a thin border) and Child (transparent background and no border, used for supplementary actions with the lowest amount of prominence). Round buttons for simple icon and text content will follow in a future release.([Ia6942](https://android-review.googlesource.com/#/q/Ia69423e823d0b307a1b0a4782dcdd58659731c77))

### Version 1.0.0-alpha02

April 5, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/wear/compose/compose-material3)

**Bug Fixes**

- We have added a `DefaultTextStyle` to Wear Compose Material 3 which defaults the `PlatformTextStyle.includeFontPadding` to true (the current setting). This will allow us to synchronize turning off font padding by default with the Compose libraries in the future (see [Fix font padding in Compose for background](https://medium.com/androiddevelopers/fixing-font-padding-in-compose-text-768cd232425b)). ([I7e461](https://android-review.googlesource.com/q/I7e461cf9492e85077b05a9eb79dc108da1a81015))

### Version 1.0.0-alpha01

March 22, 2023

`androidx.wear.compose:compose-material3:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553/wear/compose/compose-material3)

**New Features**

- Material 3 is the next evolution of Material Design and includes updated theming and redesigned components. Material 3 on Wear Compose is designed to be cohesive with the Material 3 Compose library on Android. This first alpha release contains early, functional implementations of the following:

  - Material theme - configures the color scheme, typography and shapes consistently across components in the library. The Material3 theme has revised colors which support accessible contrast. ([I84005](https://android-review.googlesource.com/#/q/I8400524e8aaa1d3231571a1e29ba75850cc7f9ab))
  - Text/Icon - building blocks for Wear Compose apps ([I8e06a](https://android.googlesource.com/platform/frameworks/support/+/2b07cd3007cc2a2afd2e730e46cd584ccafab343))
- We will continue to develop Wear Material (`androidx.wear.compose:compose-material`) and Wear Material 3 (`androidx.wear.compose:compose-material3`) in parallel. Future material3 releases will extend the widget set to include other familiar components from Compose for Wear OS, such as buttons, pickers, and sliders.

- The Wear Material and Wear Material 3 libraries are mutually exclusive and should not be mixed in the same app, primarily because they reference different themes which would lead to unexpected inconsistencies.