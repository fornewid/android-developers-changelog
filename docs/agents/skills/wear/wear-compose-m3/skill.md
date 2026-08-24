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
4. **Kotlin version:** For Wear Compose Material3, use Kotlin **2.0.0 or
   higher**.
5. **Compose compiler:**
   - If Kotlin version is **2.0.0+** , the project must use the `org.jetbrains.kotlin.plugin.compose` Gradle plugin.
   - If Kotlin version is **\< 2.0.0** , the project must use `kotlinCompilerExtensionVersion` in `composeOptions`, matching the [Compose to Kotlin Compatibility Map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).
6. **Min SDK:** Ensure `minSdk` is at least **25**.
7. **Sample extraction mandate**: Wear Compose libraries ship with an additional JAR file which contains individual samples for each and every component. You mustn't propose code changes, other than previews or basic changes such as color changes, until the samples in Capability 3 are extracted to the local cache. Library source files are incomplete and NOT a substitute for these samples; bypassing extraction is an environment setup failure.

## Gotchas

1. **Mandatory sync and validation:** After updating versions in `libs.versions.toml` or `build.gradle.kts`, you **must** perform a Gradle sync before refactoring any code. This ensures the environment has resolved the libraries correctly.
2. **Prohibition of guessing (error protocol):** If you encounter an 'Unresolved Reference' or API mismatch after a successful sync, do not attempt to 'fix' it by downgrading the library version.

## Capabilities and tools

### Capability 1: Migration

Use this guidance when migrating from an older version of Wear OS Compose or
Horologist.

1. Unless otherwise indicated by the developer, use the latest stable version of Wear Compose Material3 from `{VERSION}`.
2. Read the [migration guide](https://developer.android.com/training/wearables/compose/migrate-to-material3).
3. Use the official component mappings from the migration guide.
4. Before refactoring any component (for example, `Chip` -\> `Button`), check the parameter names, slot types, and "Expressive" design tokens.
5. Do not use the Horologist Composables, Compose Layout, or Compose Material libraries.
6. **Always** check against the component guidance in Capability 4.
7. Expect screenshot tests to fail when a migration has been performed: Even when migrating to very similar components, expected defaults for padding and positioning will have changed. Do not seek to artificially match the pre-migration screenshot, but give preference to the Material3 defaults.

### Capability 2: Adding Wear OS Compose Material3 features or updating the app

Use this guidance when the developer asks to update a project which is using an
earlier version of Wear OS Compose Material3, or when they ask to add further
features.

1. Unless otherwise indicated by the developer, use the latest stable version of Wear Compose Material3 from `{VERSION}`.
2. Do not use the Horologist Composables, Compose Layout, or Compose Material libraries.
3. **Always** check against the component guidance in Capability 4.
4. Expect screenshot tests to fail when a migration has been performed: Even when migrating to very similar components, expected defaults for padding and positioning will have changed. Do not seek to artificially match the pre-migration screenshot, but give preference to the Material3 defaults.

### Capability 3: Component samples

Use this table of reference to find canonical samples for Wear Compose
components.
When working with a Wear Compose component, you must use the samples linked
from the table to ensure you know how to correctly use it.

#### Material 3 components in `androidx.wear.compose.material3.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AlertDialog`, `AlertDialogDefaults` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt) |
| `AnimatedPage`, `HorizontalPagerScaffold`, `VerticalPagerScaffold` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt) |
| `AnimatedText`, `rememberAnimatedTextFontRegistry` | [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt) |
| `AppCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt) |
| `AppScaffold` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ArcProgressIndicator`, `ArcProgressIndicatorDefaults`, `CircularProgressIndicator`, `CircularProgressIndicatorDefaults`, `ProgressIndicatorDefaults`, `SegmentedCircularProgressIndicator`, `drawCircularProgressIndicator` | [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt) |
| `Button` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt), [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [FadingExpandingLabelSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/FadingExpandingLabelSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ButtonDefaults` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ButtonGroup` | [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt) |
| `Card` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `CardDefaults` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `CheckboxButton` | [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt) |
| `ChildButton`, `OutlinedButton` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt) |
| `ColorScheme`, `dynamicColorScheme` | [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt) |
| `CompactButton`, `CompactButtonDefaults` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ConfirmationDialog`, `ConfirmationDialogDefaults`, `FailureConfirmationDialog`, `FavoriteIcon`, `SuccessConfirmationDialog`, `confirmationDialogCurvedText` | [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt) |
| `CurvedTextDefaults` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt) |
| `DatePicker`, `DatePickerType` | [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt) |
| `EdgeButton` | [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `EdgeButtonSize` | [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt) |
| `FadingExpandingLabel` | [FadingExpandingLabelSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/FadingExpandingLabelSample.kt) |
| `FilledIconButton`, `FilledTonalIconButton`, `IconButtonColors`, `IconButtonShapes`, `OutlinedIconButton` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt) |
| `FilledTonalButton` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt), [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt) |
| `HeadphoneIcon`, `Stepper`, `StepperLevelIndicator`, `rangeSemantics` | [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt) |
| `HorizontalPageIndicator`, `VerticalPageIndicator` | [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt) |
| `Icon` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt), [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt), [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt) |
| `IconButton` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt), [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt) |
| `IconButtonDefaults` | [IconButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconButtonSample.kt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt) |
| `IconToggleButton`, `IconToggleButtonDefaults`, `WifiOffIcon`, `WifiOnIcon` | [IconToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/IconToggleButtonSample.kt) |
| `LevelIndicator` | [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt) |
| `LinearProgressIndicator` | [LinearProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LinearProgressIndicatorSample.kt) |
| `ListHeader` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ListHeaderDefaults` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ListSubHeader` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt) |
| `LocalOneHandedGestureEnabled`, `OneHandedGestureDefaults`, `OneHandedGestureHorizontalPageIndicator`, `OneHandedGesturePageIndicatorState`, `OneHandedGesturePriority`, `OneHandedGestureScrollIndicator`, `OneHandedGestureScrollIndicatorState`, `OneHandedGestureVerticalPageIndicator` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt) |
| `MaterialTheme` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [LinearProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LinearProgressIndicatorSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [ProgressIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ProgressIndicatorSample.kt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt) |
| `OneHandedGestureAction`, `OneHandedGestureClickIndicator`, `OneHandedGestureClickIndicatorState`, `oneHandedGesture`, `rememberOneHandedGestureConfiguration` | [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt) |
| `OpenOnPhoneDialog`, `OpenOnPhoneDialogDefaults`, `openOnPhoneDialogCurvedText` | [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt) |
| `OutlinedCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `PagerScaffoldDefaults` | [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt) |
| `Picker` | [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt) |
| `PickerGroup` | [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt) |
| `RadioButton`, `SplitRadioButton` | [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt) |
| `ResponsiveTransformationSpec`, `TransformationVariableSpec` | [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt) |
| `RevealValue`, `SwipeToReveal`, `SwipeToRevealDefaults`, `rememberRevealState` | [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt) |
| `ScreenScaffold` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `ScreenScaffoldDefaults`, `ScrollIndicator` | [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt) |
| `ScreenStage`, `scrollAway` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt) |
| `Slider`, `SliderDefaults` | [SliderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SliderSample.kt) |
| `SplitCheckboxButton` | [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt) |
| `SplitSwitchButton` | [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt) |
| `StepperDefaults`, `VolumeDownIcon`, `VolumeUpIcon` | [LevelIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/LevelIndicatorSample.kt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt) |
| `SurfaceTransformation` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `SwipeToDismissBox` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt) |
| `SwitchButton` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt) |
| `Text` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [AnimatedTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AnimatedTextSample.kt), [ButtonGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonGroupSample.kt), [ButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ButtonSample.kt), [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [CheckboxButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CheckboxButtonSample.kt), [ConfirmationDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ConfirmationDialogSample.kt), [DatePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DatePickerSample.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [EdgeButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/EdgeButtonSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [OpenOnPhoneDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OpenOnPhoneDialogSample.kt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt), [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt), [RadioButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/RadioButtonSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [StepperSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/StepperSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [SwitchButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwitchButtonSample.kt), [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt), [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt), [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `TextButton` | [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt) |
| `TextButtonDefaults` | [TextButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextButtonSample.kt), [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt) |
| `TextToggleButton`, `TextToggleButtonDefaults`, `touchTargetAwareSize` | [TextToggleButtonSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TextToggleButtonSample.kt) |
| `TimePicker`, `TimePickerType` | [TimePickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimePickerSample.kt) |
| `TimeText` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |
| `TimeTextDefaults`, `timeTextCurvedText` | [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |
| `TitleCard` | [CardSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CardSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt) |
| `TransformationSpec` | [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt) |
| `curvedText` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |
| `firstVisibleItemLayoutItemInfo`, `layoutItemInfoOf`, `rememberTransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `placeholder`, `placeholderShimmer`, `rememberPlaceholderState` | [PlaceholderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PlaceholderSample.kt) |
| `rememberPickerState` | [PickerGroupSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerGroupSample.kt), [PickerSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PickerSample.kt) |
| `rememberTransformationSpec`, `transformedHeight` | [AlertDialogSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/AlertDialogSample.kt), [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `timeTextSeparator` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |

#### Foundation components in `androidx.wear.compose.foundation.*`

| Component / Symbol | Reference Samples |
|---|---|
| `AmbientMode`, `LocalAmbientModeManager`, `rememberAmbientModeManager` | [AmbientModeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/AmbientModeSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt) |
| `AmbientTickEffect` | [AmbientModeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/AmbientModeSample.kt) |
| `AutoCenteringParams`, `ScalingLazyColumnDefaults`, `ScalingLazyListAnchorType` | [ScalingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ScalingLazyColumnSample.kt) |
| `BasicSwipeToDismissBox` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToDismissBoxSample.kt) |
| `CurvedAlignment`, `CurvedTextStyle`, `angularGradientBackground`, `angularSize`, `basicCurvedText`, `clearAndSetSemantics`, `curvedColumn`, `padding`, `radialGradientBackground`, `radialSize`, `semantics`, `size` | [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt) |
| `CurvedDirection`, `CurvedLayout`, `angularSizeDp`, `background`, `curvedBox`, `curvedComposable`, `curvedRow` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt) |
| `CurvedModifier` | [CurvedTextSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/CurvedTextSamples.kt), [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |
| `ExperimentalWearFoundationApi`, `RevealValue`, `SwipeToReveal`, `rememberRevealState` | [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToRevealSample.kt) |
| `HorizontalPager`, `VerticalPager`, `rememberPagerState` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [PageIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PageIndicatorSample.kt), [PagerSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/PagerSamples.kt), [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt) |
| `ItemEdge`, `TransformingLazyColumnDefaults` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt) |
| `PagerDefaults` | [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt) |
| `RotaryScrollableDefaults` | [PagerScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/PagerScaffoldSample.kt), [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt), [ScalingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ScalingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt) |
| `RotarySnapLayoutInfoProvider`, `rotaryScrollable` | [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt) |
| `ScalingLazyColumn` | [ExpandableSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ExpandableSample.kt), [HierarchicalFocusSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/HierarchicalFocusSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [ScalingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ScalingLazyColumnSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToRevealSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt) |
| `ScrollInfoProvider` | [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt) |
| `SwipeToDismissValue`, `edgeSwipeToDismiss`, `rememberSwipeToDismissBoxState` | [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToDismissBoxSample.kt), [SwipeToDismissBoxSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToDismissBoxSample.kt) |
| `TransformingLazyColumn` | [DynamicColorSchemeSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/DynamicColorSchemeSample.kt), [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `TransformingLazyColumnFirstLayoutItemProvider` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `TransformingLazyColumnItemScrollProgress` | [TransformationSpecSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformationSpecSample.kt) |
| `expandableButton`, `expandableItems` | [ExpandableSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ExpandableSample.kt) |
| `expandableItem`, `rememberExpandableState` | [ExpandableSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ExpandableSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/SwipeToRevealSample.kt) |
| `hierarchicalFocusGroup` | [HierarchicalFocusSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/HierarchicalFocusSample.kt) |
| `items` | [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt) |
| `itemsIndexed` | [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `rememberScalingLazyListState` | [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [ScalingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/ScalingLazyColumnSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt) |
| `rememberTransformingLazyColumnState` | [ListHeaderSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ListHeaderSample.kt), [OneHandedGestureSamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/OneHandedGestureSamples.kt), [ScaffoldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScaffoldSample.kt), [ScrollAwaySample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollAwaySample.kt), [ScrollIndicatorSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/ScrollIndicatorSample.kt), [SurfaceTransformationSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SurfaceTransformationSample.kt), [SwipeToRevealSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/SwipeToRevealSample.kt), [TransformingLazyColumnNotificationsSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnNotificationsSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/TransformingLazyColumnSample.kt), [TransformingLazyColumnSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TransformingLazyColumnSample.kt) |
| `requestFocusOnHierarchyActive` | [HierarchicalFocusSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/HierarchicalFocusSample.kt), [RotarySamples](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/RotarySamples.kt) |
| `weight` | [CurvedWorldSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/foundation/CurvedWorldSample.kt), [TimeTextSample](https://developer.android.com/agents/skills/wear/wear-compose-m3/references/material3/TimeTextSample.kt) |

### Capability 4: Component guidance

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
     - This expects a value from defaults, such as `ButtonDefaults`, `CardDefaults`, \`ListHeaderDefaults.
     - Note: This is a scoped modifier available within `TransformingLazyColumnItemScope`.
   - \[ \] Ensure the list morphs and scales.
   - \[ \] Use `transformedHeight` modifier.
   - \[ \] Use `transform = SurfaceTransform(...)`.
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

   - \[ \] Guard the `scrollIndicator` with `!LocalScrollCaptureInProgress.current`.
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

   - \[ \] USE as a direct child of `ScreenScaffold` *if* the screen is will **never** scroll, even with the largest system font.
   - \[ \] Use `TransformingLazyColumn` instead for all other cases.
7. Styles

   - \[ \] Do **NOT** hard-code text sizes, use `typography` from `MaterialTheme`.
   - \[ \] Do **NOT** hard-code colors, use `colorScheme` from `MaterialTheme`.
8. Use component defaults:

   - \[ \] Components such as `Button` have a corresponding `ButtonDefaults` object.
   - \[ \] Check for and use the `*Defaults` object for any component when working with padding and styling values, in preference to hard-coded values.
9. Use Wear specific previews:

   - \[ \] `WearPreviewDevices`
   - \[ \] `WearPreviewFontScales`
10. Ambient mode

    - \[ \] Use `LocalAmbientModeManager` instead of `AmbientLifecycleObserver`.
11. Navigation

    - \[ \] When adding navigation fresh, use Navigation3.
    - \[ \] For Navigation3 in Wear OS, use `SwipeDismissableSceneStrategy()` from the Wear Compose `compose-navigation3` library.
12. Comments

    - \[ \] Where any Kotlin file has been modified, ensure that the existing comments are up to date and accurately reflect any changes to the implementation.
13. `HorizontalPager` or `VerticalPager`

    - \[ \] Use the Composable hierarchy in this order: `AppScaffold`, `HorizontalPagerScaffold`, `HorizontalPager`, `AnimatedPage`, `ScreenScaffold`. Or similarly for `VerticalPager`.