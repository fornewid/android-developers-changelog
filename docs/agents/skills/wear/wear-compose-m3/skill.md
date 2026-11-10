---
title: https://developer.android.com/agents/skills/wear/wear-compose-m3/skill
url: https://developer.android.com/agents/skills/wear/wear-compose-m3/skill
source: md.txt
---

## Prerequisites and compatibility

1. **Current Wear OS Compose version in-use:** To find the installed library version, read `gradle/libs.versions.toml` or `build.gradle.kts` directly. Don't run `./gradlew dependencies` or other shell commands to resolve versions.
2. **Wear OS Compose Material3 version:** If an internal tool is available to establish the **latest stable version** `{VERSION}` of `androidx.wear.compose:compose-material3`, use that tool.
   - Otherwise, fetch the [official Maven metadata XML](https://dl.google.com/dl/android/maven2/androidx/wear/compose/compose-material3/maven-metadata.xml) to identify `{VERSION}` (highest number, ignoring `-alpha`, `-beta`, or `-rc`).
3. **Strict compliance:** If a version is listed as stable, you MUST use it, unless overridden by the user. Do not downgrade based on initial "Unresolved reference" errors in the editor or outdated web search results.
4. **Kotlin \& Compose compiler:** Use Kotlin **2.0.0+** with the `org.jetbrains.kotlin.plugin.compose` Gradle plugin.
5. **Min SDK:** Ensure `minSdk` is at least **25**.
6. **Compile SDK \& AGP:** Ensure `compileSdk` and AGP meet the library's AAR metadata floors (`compileSdk >= 35` and `AGP >= 8.6.0` for `1.6.x`; `compileSdk >= 37` and `AGP >= 9.1.0` for `1.7.x`).

## Gotchas

1. **Mandatory sync and validation:** After updating versions in `libs.versions.toml` or `build.gradle.kts`, perform a Gradle sync (or `./gradlew assembleDebug`) before refactoring, and run `./gradlew assembleDebug` after refactoring to verify the build.
2. **Prohibition of guessing (error protocol):** If you encounter an 'Unresolved Reference' or API mismatch after a successful sync, do not attempt to 'fix' it by downgrading the library version.

## Capabilities and tools

### Capability 1: Migration, updates, and adding features

Use this guidance when migrating from an older version of Wear OS Compose or
Horologist, updating an existing Wear Compose Material3 project, or adding
features.

1. Unless otherwise indicated by the developer, use the latest stable version of Wear Compose Material3 from `{VERSION}` (superseding any literal version strings in the migration guide).
2. When migrating from Material 2.5 or Horologist, read the [migration guide](https://developer.android.com/training/wearables/compose/migrate-to-material3.md.txt) and use its official component mappings.
3. Before refactoring any component (for example, `Chip` -\> `Button`), check the parameter names, slot types, and "Expressive" design tokens.
4. Do not use the Horologist Composables, Compose Layout, or Compose Material libraries; replace Horologist components with Wear Compose M3 equivalents (`AppScaffold` -\> M3 `AppScaffold`, `ScreenScaffold` -\> M3 `ScreenScaffold`, `ScalingLazyColumn` -\> `TransformingLazyColumn`, `ResponsiveListHeader` -\> `ListHeader`, `PagerScreen` -\> `HorizontalPagerScaffold`, `Chip` -\> `Button`, `Confirmation` -\> `ConfirmationDialog`).
5. **Always** check against the component guidance in Capability 3.
6. Expect screenshot tests to fail when migrating or updating components: expected defaults for padding and positioning will have changed. Do not seek to artificially match the previous screenshot, but give preference to the Material3 defaults.

### Capability 2: Component samples

Use this table of reference to find canonical samples for Wear Compose
components.
When working with a Wear Compose component, you must use the samples linked
from the table to ensure you know how to correctly use it.

**Important:** Symbols marked with `[alpha]`, `[beta]`, or `[rc]` are only
available in that pre-release track and are **not** in stable `{VERSION}`. Do
not use them unless the project explicitly targets that pre-release version.

#### Material 3 components in `androidx.wear.compose.material3.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AlertDialog`, `AlertDialogDefaults` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt) |
| `AnimatedPage`, `HorizontalPagerScaffold`, `VerticalPagerScaffold` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt) |
| `AnimatedText`, `rememberAnimatedTextFontRegistry` | [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt.md.txt) |
| `AppCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt) |
| `AppScaffold` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ArcProgressIndicator`, `ArcProgressIndicatorDefaults`, `CircularProgressIndicator`, `CircularProgressIndicatorDefaults`, `ProgressIndicatorDefaults`, `SegmentedCircularProgressIndicator`, `drawCircularProgressIndicator` | [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt.md.txt) |
| `Button` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt.md.txt), [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt.md.txt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [FadingExpandingLabelSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/FadingExpandingLabelSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ButtonDefaults` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ButtonGroup` | [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt) |
| `Card` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `CardDefaults` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `CheckboxButton` | [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt.md.txt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt) |
| `ChildButton`, `OutlinedButton` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt) |
| `ColorScheme`, `dynamicColorScheme` | [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt) |
| `CompactButton`, `CompactButtonDefaults` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ConfirmationDialog`, `ConfirmationDialogDefaults`, `FailureConfirmationDialog`, `SuccessConfirmationDialog`, `confirmationDialogCurvedText` | [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt.md.txt) |
| `CurvedTextDefaults` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt) |
| `DatePicker`, `DatePickerType` | [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt.md.txt) |
| `EdgeButton` | [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `EdgeButtonSize` | [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt.md.txt) |
| `FadingExpandingLabel` | [FadingExpandingLabelSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/FadingExpandingLabelSample.kt.md.txt) |
| `FilledIconButton`, `FilledTonalIconButton`, `IconButtonColors`, `IconButtonShapes`, `OutlinedIconButton` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt.md.txt) |
| `FilledTonalButton` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt.md.txt), [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt.md.txt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt) |
| `HorizontalPageIndicator`, `VerticalPageIndicator` | [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt) |
| `Icon` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt.md.txt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt.md.txt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt.md.txt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt.md.txt), [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt.md.txt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt.md.txt), [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt.md.txt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt.md.txt) |
| `IconButton` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt.md.txt), [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt.md.txt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt.md.txt) |
| `IconButtonDefaults` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt.md.txt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt.md.txt) |
| `IconToggleButton`, `IconToggleButtonDefaults` | [IconToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconToggleButtonSample.kt.md.txt) |
| `LevelIndicator` | [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt.md.txt) |
| `LinearProgressIndicator` | [LinearProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LinearProgressIndicatorSample.kt.md.txt) |
| `ListHeader` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ListHeaderDefaults` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ListSubHeader` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt) |
| `LocalOneHandedGestureEnabled`, `OneHandedGestureDefaults`, `OneHandedGestureHorizontalPageIndicator`, `OneHandedGesturePageIndicatorState`, `OneHandedGesturePriority`, `OneHandedGestureScrollIndicator`, `OneHandedGestureScrollIndicatorState`, `OneHandedGestureVerticalPageIndicator` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt) |
| `MaterialTheme` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [LinearProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LinearProgressIndicatorSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt.md.txt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt) |
| `OneHandedGestureAction`, `OneHandedGestureClickIndicator`, `OneHandedGestureClickIndicatorState`, `oneHandedGesture`, `rememberOneHandedGestureConfiguration` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt) |
| `OpenOnPhoneDialog`, `OpenOnPhoneDialogDefaults`, `openOnPhoneDialogCurvedText` | [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt.md.txt) |
| `OutlinedCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `PagerScaffoldDefaults` | [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt) |
| `Picker` | [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt.md.txt) |
| `PickerGroup` | [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt.md.txt) |
| `RadioButton`, `SplitRadioButton` | [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt.md.txt) |
| `ResponsiveTransformationSpec`, `TransformationVariableSpec` | [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt) |
| `RevealValue`, `SwipeToReveal`, `SwipeToRevealDefaults`, `rememberRevealState` | [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt) |
| `ScreenScaffold` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `ScreenScaffoldDefaults`, `ScrollIndicator` | [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt) |
| `ScreenStage`, `scrollAway` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt) |
| `Slider`, `SliderDefaults` | [SliderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SliderSample.kt.md.txt) |
| `SplitCheckboxButton` | [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt.md.txt) |
| `SplitSwitchButton` | [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt.md.txt) |
| `Stepper`, `StepperLevelIndicator`, `rangeSemantics` | [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt.md.txt) |
| `StepperDefaults` | [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt.md.txt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt.md.txt) |
| `SurfaceTransformation` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `SwipeToDismissBox` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt) |
| `SwitchButton` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt.md.txt) |
| `Text` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt.md.txt), [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt.md.txt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt.md.txt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt.md.txt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt.md.txt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt.md.txt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt.md.txt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt.md.txt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt.md.txt), [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt.md.txt), [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt.md.txt), [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt.md.txt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `TextButton` | [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt.md.txt) |
| `TextButtonDefaults` | [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt.md.txt), [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt.md.txt) |
| `TextToggleButton`, `TextToggleButtonDefaults`, `touchTargetAwareSize` | [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt.md.txt) |
| `TimePicker`, `TimePickerType` | [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt.md.txt) |
| `TimeText` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |
| `TimeTextDefaults`, `timeTextCurvedText` | [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |
| `TitleCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt) |
| `TransformationSpec` | [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt) |
| `curvedText` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |
| `firstVisibleItemLayoutItemInfo`, `layoutItemInfoOf`, `rememberTransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `placeholder`, `placeholderShimmer`, `rememberPlaceholderState` | [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt.md.txt) |
| `rememberPickerState` | [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt.md.txt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt.md.txt) |
| `rememberTransformationSpec`, `transformedHeight` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt.md.txt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `timeTextSeparator` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |

#### Foundation components in `androidx.wear.compose.foundation.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AmbientMode`, `LocalAmbientModeManager`, `rememberAmbientModeManager` | [AmbientModeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/AmbientModeSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt) |
| `AmbientTickEffect` | [AmbientModeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/AmbientModeSample.kt.md.txt) |
| `BasicSwipeToDismissBox` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToDismissBoxSample.kt.md.txt) |
| `CurvedAlignment`, `CurvedTextStyle`, `angularGradientBackground`, `angularSize`, `basicCurvedText`, `clearAndSetSemantics`, `curvedColumn`, `padding`, `radialGradientBackground`, `radialSize`, `semantics`, `size` | [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt.md.txt) |
| `CurvedDirection`, `CurvedLayout`, `angularSizeDp`, `background`, `curvedBox`, `curvedComposable`, `curvedRow` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt.md.txt) |
| `CurvedModifier` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt.md.txt), [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |
| `HorizontalPager`, `VerticalPager`, `rememberPagerState` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt.md.txt), [PagerSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/PagerSamples.kt.md.txt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt) |
| `PagerDefaults` | [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt) |
| `RotaryScrollableDefaults` | [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt.md.txt), [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt) |
| `RotarySnapLayoutInfoProvider`, `rotaryScrollable` | [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt.md.txt) |
| `ScrollInfoProvider` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt) |
| `SwipeToDismissValue`, `edgeSwipeToDismiss`, `rememberSwipeToDismissBoxState` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToDismissBoxSample.kt.md.txt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt.md.txt) |
| `TransformingLazyColumn` | [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt.md.txt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `TransformingLazyColumnDefaults` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt) |
| `TransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `TransformingLazyColumnItemScrollProgress` | [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt.md.txt) |
| `expandableButton`, `expandableItem`, `expandableItems`, `rememberExpandableState` | [ExpandableSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ExpandableSample.kt.md.txt) |
| `hierarchicalFocusGroup` | [HierarchicalFocusSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/HierarchicalFocusSample.kt.md.txt) |
| `items` | [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt) |
| `itemsIndexed` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `rememberTransformingLazyColumnState` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt.md.txt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt.md.txt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt.md.txt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt.md.txt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt.md.txt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt.md.txt), [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt.md.txt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt.md.txt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt.md.txt) |
| `requestFocusOnHierarchyActive` | [HierarchicalFocusSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/HierarchicalFocusSample.kt.md.txt), [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt.md.txt) |
| `weight` | [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt.md.txt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt.md.txt) |

#### Navigation 3 components in `androidx.wear.compose.navigation3.*`

| Component / Symbol | Reference Samples |
|---|---|
| `rememberSwipeDismissableSceneStrategy` | [SwipeDismissableSceneStrategySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/navigation3/SwipeDismissableSceneStrategySample.kt.md.txt) |

### Capability 3: Component guidance

**Mandatory**: Use this capability as a checklist against any component use. It
provides more holistic guidance on how to use each component in practice, beyond
the component syntax.

1. `AppScaffold` and `ScreenScaffold`
   - \[ \] Use `AppScaffold` as the outer container, with `ScreenScaffold` children.
   - \[ \] Use only **ONE** `AppScaffold` and any number of `ScreenScaffold`.
2. `ScalingLazyColumn` - Use `TransformingLazyColumn` instead.
3. `TransformingLazyColumn` - You will need the following imports:


   ```kotlin
   import androidx.wear.compose.foundation.lazy.TransformingLazyColumn
   import androidx.wear.compose.foundation.lazy.TransformingLazyColumnDefaults
   import androidx.wear.compose.foundation.lazy.rememberTransformingLazyColumnState
   // ...
   import androidx.wear.compose.material3.lazy.rememberTransformationSpec
   import androidx.wear.compose.material3.lazy.transformedHeight
   ```

   <br />

   **Canonical example**:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   val transformationSpec = rememberTransformationSpec()
   ScreenScaffold(
       scrollState = columnState
   ) { contentPadding ->
       TransformingLazyColumn(
           state = columnState,
           contentPadding = contentPadding
       ) {
           item {
               ListHeader(
                   modifier = Modifier
                       .fillMaxWidth()
                       .transformedHeight(this, transformationSpec)
                       .minimumVerticalContentPadding(ListHeaderDefaults.minimumTopListContentPadding),
                   transformation = SurfaceTransformation(transformationSpec)
               ) {
                   Text(text = "Header")
               }
           }
           // ... other items
           item {
               Button(
                   modifier = Modifier
                       .fillMaxWidth()
                       .transformedHeight(this, transformationSpec)
                       .minimumVerticalContentPadding(ButtonDefaults.minimumVerticalListContentPadding),
                   transformation = SurfaceTransformation(transformationSpec),
                   onClick = { /* ... */ },
                   icon = {
                       Icon(
                           imageVector = Icons.Default.Build,
                           contentDescription = "build",
                       )
                   },
               ) {
                   Text(
                       text = "Build",
                       maxLines = 1,
                       overflow = TextOverflow.Ellipsis,
                   )
               }
           }
       }
   }
   ```

   <br />

   - \[ \] Use `TransformingLazyColumn` instead of `ScalingLazyColumn`.
   - \[ \] You must pass the `contentPadding` parameter from `ScreenScaffold` to the `TransformingLazyColumn`.
   - \[ \] Use the `minimumVerticalContentPadding` modifier to achieve required padding top and bottom.
     - This expects a value from defaults, such as `ButtonDefaults`, `CardDefaults`, `ListHeaderDefaults`.
     - Note: This is a scoped modifier available within `TransformingLazyColumnItemScope`.
   - \[ \] Ensure items morph and scale (apply to components **within** `TransformingLazyColumn`, not the list itself):
     - \[ \] Use `Modifier.transformedHeight(this, transformationSpec)`.
     - \[ \] Use `transformation = SurfaceTransformation(transformationSpec)`.
   - \[ \] If configuring a list for snapping, use `flingBehavior` and `rotaryScrollableBehavior` **together**:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   ScreenScaffold(scrollState = columnState) { contentPadding ->
       TransformingLazyColumn(
           state = columnState,
           flingBehavior = TransformingLazyColumnDefaults.snapFlingBehavior(columnState),
           rotaryScrollableBehavior = RotaryScrollableDefaults.snapBehavior(columnState)
       ) {
           // ...
           // ...
       }
   }
   ```

   <br />

4. `ScreenScaffold`

   - \[ \] Guard the `scrollIndicator` with `!LocalScrollCaptureInProgress.current` (`androidx.compose.ui.platform`).
5. `EdgeButton`

   - \[ \] Do **NOT** use as the final item within a `TransformingLazyColumn`. Instead, use the slot in `ScreenScaffold`.
   - \[ \] When used in a `TransformingLazyColumn`, add the required overscroll behavior:


   ```kotlin
   val columnState = rememberTransformingLazyColumnState()
   ScreenScaffold(
       scrollState = columnState,
       edgeButton = {
           EdgeButton(
               onClick = { /* TODO */ },
               modifier = Modifier.scrollable(
                   columnState,
                   orientation = Orientation.Vertical,
                   reverseDirection = true,
                   // Apply overscroll to the EdgeButton for proper scrolling behavior.
                   overscrollEffect = rememberOverscrollEffect(),
               )
           ) {
               Text("More")
           }
       }
   ) { contentPadding ->
       TransformingLazyColumn(
           contentPadding = contentPadding,
           state = columnState,
       ) {
           // ...
           // ...
       }
   }
   ```

   <br />

6. `Column`

   - \[ \] USE as a direct child of `ScreenScaffold` *if* the screen will **never** scroll, even with the largest system font.
   - \[ \] Use `TransformingLazyColumn` instead for all other cases.
7. Styles

   - \[ \] Do **NOT** hard-code text sizes, use `typography` from `MaterialTheme`.
   - \[ \] Do **NOT** hard-code colors, use `colorScheme` from `MaterialTheme`.
8. Use component defaults:

   - \[ \] Components such as `Button` have a corresponding `ButtonDefaults` object.
   - \[ \] Check for and use the `*Defaults` object for any component when working with padding and styling values, in preference to hard-coded values.
9. Use Wear-specific preview annotations
   (`androidx.wear.compose.ui.tooling.preview`):

   - \[ \] `@WearPreviewDevices`
   - \[ \] `@WearPreviewFontScales`
   - \[ \] Ensure the `androidx.wear.compose:compose-ui-tooling` dependency is included.
10. Ambient mode

    - \[ \] Use `LocalAmbientModeManager` (provided by `CompositionLocalProvider` and `rememberAmbientModeManager()`) instead of `AmbientLifecycleObserver`.
11. Navigation

    - \[ \] When adding navigation fresh, use Navigation3 (`androidx.wear.compose:compose-navigation3`).
    - \[ \] Use `rememberSwipeDismissableSceneStrategy()` / `SwipeDismissableSceneStrategy` (`androidx.wear.compose.navigation3`).
12. Comments

    - \[ \] Where any Kotlin file has been modified, ensure that the existing comments are up to date and accurately reflect any changes to the implementation.
13. `HorizontalPager` or `VerticalPager`

    - \[ \] Use the Composable hierarchy in this order: `AppScaffold`, `HorizontalPagerScaffold`, `HorizontalPager`, `AnimatedPage`, `ScreenScaffold`. Or similarly for `VerticalPager`.