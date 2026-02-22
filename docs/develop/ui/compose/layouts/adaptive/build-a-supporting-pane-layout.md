---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout
source: md.txt
---

The supporting pane layout keeps the user's focus on the app's main content
while displaying relevant supporting information. For example, the main pane
might show details about a movie, while the supporting pane lists similar
movies, films by the same director, or works featuring the same actors.

For more details, see the [Material 3 supporting pane guidelines](https://m3.material.io/foundations/layout/canonical-layouts/supporting-pane).

## Implement a supporting pane with a scaffold

[`NavigableSupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#NavigableSupportingPaneScaffold(androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldNavigator,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.material3.adaptive.navigation.BackNavigationBehavior,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) is a composable that simplifies
implementing a supporting pane layout in Jetpack Compose. It wraps
[`SupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#SupportingPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) and adds built-in navigation and predictive back
handling.

A supporting pane scaffold supports up to three panes:

- **Main pane**: Displays primary content.
- **Supporting pane**: Provides additional context or tools related to the main pane.
- **Extra pane (optional)**: Used for supplementary content when needed.

The scaffold adapts based on window size:

- **In large windows**, the main and supporting panes appear side by side.
- **In small windows**, only one pane is visible at a time, switching as users
  navigate.

  ![Main content occupying most of the display with supporting content alongside.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/supporting-pane.png) **Figure 1.** Supporting pane layout.

## Add dependencies

`NavigableSupportingPaneScaffold` is part of the [Material 3 adaptive layout
library](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary).

Add the following three, related dependencies to the `build.gradle` file of your
app or module:

### Kotlin

    implementation("androidx.compose.material3.adaptive:adaptive")
    implementation("androidx.compose.material3.adaptive:adaptive-layout")
    implementation("androidx.compose.material3.adaptive:adaptive-navigation")

### Groovy

    implementation 'androidx.compose.material3.adaptive:adaptive'
    implementation 'androidx.compose.material3.adaptive:adaptive-layout'
    implementation 'androidx.compose.material3.adaptive:adaptive-navigation'

- **adaptive** : Low-level building blocks such as [`HingeInfo`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/HingeInfo) and
  [`Posture`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/Posture)

- **adaptive-layout** : Adaptive layouts such as [`ListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState))
  and `SupportingPaneScaffold`

- **adaptive-navigation** : Composables for navigating within and between
  panes, as well as adaptive layouts that support navigation by default such
  as `NavigableListDetailPaneScaffold` and `NavigableSupportingPaneScaffold`

Verify that your project includes
[compose-material3-adaptive version 1.1.0-beta1](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.1.0-beta01) or higher.

## Opt-in to the predictive back gesture

To enable predictive back animations in Android 15 or lower, you must opt-in to
support the predictive back gesture. To opt-in, add
`android:enableOnBackInvokedCallback="true"` to the [`<application>`](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-predictive) tag or
individual [`<activity>`](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-activity-level) tags within your `AndroidManifest.xml` file.

Once your app targets Android 16 (API level 36) or higher, predictive back is
enabled by default.

## Create a navigator

In small windows, only one pane displays at a time, so use a
[`ThreePaneScaffoldNavigator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/ThreePaneScaffoldNavigator) to move to and from panes. Create an instance
of the navigator with [`rememberSupportingPaneScaffoldNavigator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/package-summary#rememberSupportingPaneScaffoldNavigator(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldAdaptStrategies,kotlin.Boolean)).


```kotlin
val scaffoldNavigator = rememberSupportingPaneScaffoldNavigator()
val scope = rememberCoroutineScope()
```

<br />

## Pass the navigator to the scaffold

The scaffold requires a `ThreePaneScaffoldNavigator` which is an interface
representing the state of the scaffold, the [`ThreePaneScaffoldValue`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/ThreePaneScaffoldValue) and a
[`PaneScaffoldDirective`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/PaneScaffoldDirective).


```kotlin
NavigableSupportingPaneScaffold(
    navigator = scaffoldNavigator,
    mainPane = { /*...*/ },
    supportingPane = { /*...*/ },
)
```

<br />

The main pane and supporting pane are composables containing your content. Use
[`AnimatedPane`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/AnimatedPaneOverride#(androidx.compose.material3.adaptive.layout.AnimatedPaneOverrideScope).AnimatedPane()) to apply the default pane animations during navigation. Use
the scaffold value to check whether the supporting pane is hidden; if so,
display a button that calls
[`navigateTo(SupportingPaneScaffoldRole.Supporting)`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/ThreePaneScaffoldNavigator#navigateTo(androidx.compose.material3.adaptive.layout.ThreePaneScaffoldRole,kotlin.Any)) to display the
supporting pane.

For large screens, use the [`ThreePaneScaffoldNavigator.navigateBack()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/ThreePaneScaffoldNavigator#navigateBack(androidx.compose.material3.adaptive.navigation.BackNavigationBehavior))
method to dismiss the supporting pane, passing in the
[`BackNavigationBehavior.PopUntilScaffoldValueChange`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/BackNavigationBehavior#PopUntilScaffoldValueChange()) constant. Calling this
method forces a [recomposition](https://developer.android.com/develop/ui/compose/mental-model#recomposition) of the `NavigableSupportingPaneScaffold`.
During recomposition, check the
[`ThreePaneScaffoldNavigator.currentDestination`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigation/ThreePaneScaffoldNavigator#currentDestination()) property to determine
whether to show the supporting pane.

Here's a complete implementation of the scaffold:


```kotlin
val scaffoldNavigator = rememberSupportingPaneScaffoldNavigator()
val scope = rememberCoroutineScope()
val backNavigationBehavior = BackNavigationBehavior.PopUntilScaffoldValueChange

NavigableSupportingPaneScaffold(
    navigator = scaffoldNavigator,
    mainPane = {
        AnimatedPane(
            modifier = Modifier
                .safeContentPadding()
                .background(Color.Red)
        ) {
            if (scaffoldNavigator.scaffoldValue[SupportingPaneScaffoldRole.Supporting] == PaneAdaptedValue.Hidden) {
                Button(
                    modifier = Modifier
                        .wrapContentSize(),
                    onClick = {
                        scope.launch {
                            scaffoldNavigator.navigateTo(SupportingPaneScaffoldRole.Supporting)
                        }
                    }
                ) {
                    Text("Show supporting pane")
                }
            } else {
                Text("Supporting pane is shown")
            }
        }
    },
    supportingPane = {
        AnimatedPane(modifier = Modifier.safeContentPadding()) {
            Column {
                // Allow users to dismiss the supporting pane. Use back navigation to
                // hide an expanded supporting pane.
                if (scaffoldNavigator.scaffoldValue[SupportingPaneScaffoldRole.Supporting] == PaneAdaptedValue.Expanded) {
                    // Material design principles promote the usage of a right-aligned
                    // close (X) button.
                    IconButton(
                        modifier =  Modifier.align(Alignment.End).padding(16.dp),
                        onClick = {
                            scope.launch {
                                scaffoldNavigator.navigateBack(backNavigationBehavior)
                            }
                        }
                    ) {
                        Icon(Icons.Default.Close, contentDescription = "Close")
                    }
                }
                Text("Supporting pane")
            }

        }
    }
)
```

<br />

> [!NOTE]
> **Note:** By default, `NavigableSupportingPaneScaffold` uses `PopUntilScaffoldValueChange` for `defaultBackBehavior`. If your app requires a different back navigation pattern, you can override this behavior by specifying another [`BackNavigationBehavior`](https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail#backnavigationbehavior_options) option.

## Extract pane composables

Extract the individual panes of a `SupportingPaneScaffold` into their own
composables to make them reusable and testable. Use [`ThreePaneScaffoldScope`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/ThreePaneScaffoldScope)
to access `AnimatedPane` if you want the default animations:


```kotlin
@OptIn(ExperimentalMaterial3AdaptiveApi::class)
@Composable
fun ThreePaneScaffoldPaneScope.MainPane(
    shouldShowSupportingPaneButton: Boolean,
    onNavigateToSupportingPane: () -> Unit,
    modifier: Modifier = Modifier,
) {
    AnimatedPane(
        modifier = modifier.safeContentPadding()
    ) {
        // Main pane content
        if (shouldShowSupportingPaneButton) {
            Button(onClick = onNavigateToSupportingPane) {
                Text("Show supporting pane")
            }
        } else {
            Text("Supporting pane is shown")
        }
    }
}

@OptIn(ExperimentalMaterial3AdaptiveApi::class)
@Composable
fun ThreePaneScaffoldPaneScope.SupportingPane(
    scaffoldNavigator: ThreePaneScaffoldNavigator<Any>,
    modifier: Modifier = Modifier,
    backNavigationBehavior: BackNavigationBehavior = BackNavigationBehavior.PopUntilScaffoldValueChange,
) {
    val scope = rememberCoroutineScope()
    AnimatedPane(modifier = Modifier.safeContentPadding()) {
        Column {
            // Allow users to dismiss the supporting pane. Use back navigation to
            // hide an expanded supporting pane.
            if (scaffoldNavigator.scaffoldValue[SupportingPaneScaffoldRole.Supporting] == PaneAdaptedValue.Expanded) {
                // Material design principles promote the usage of a right-aligned
                // close (X) button.
                IconButton(
                    modifier =  modifier.align(Alignment.End).padding(16.dp),
                    onClick = {
                        scope.launch {
                            scaffoldNavigator.navigateBack(backNavigationBehavior)
                        }
                    }
                ) {
                    Icon(Icons.Default.Close, contentDescription = "Close")
                }
            }
            Text("Supporting pane")
        }

    }
}
```

<br />

Extracting the panes into composables simplifies the use of the
`SupportingPaneScaffold` (compare the following to the complete implementation
of the scaffold in the previous section):


```kotlin
val scaffoldNavigator = rememberSupportingPaneScaffoldNavigator()
val scope = rememberCoroutineScope()

NavigableSupportingPaneScaffold(
    navigator = scaffoldNavigator,
    mainPane = {
        MainPane(
            shouldShowSupportingPaneButton = scaffoldNavigator.scaffoldValue.secondary == PaneAdaptedValue.Hidden,
            onNavigateToSupportingPane = {
                scope.launch {
                    scaffoldNavigator.navigateTo(ThreePaneScaffoldRole.Secondary)
                }
            }
        )
    },
    supportingPane = { SupportingPane(scaffoldNavigator = scaffoldNavigator) },
)
```

<br />

If you need more control over specific aspects of the scaffold, consider using
`SupportingPaneScaffold` instead of `NavigableSupportingPaneScaffold`. This
accepts a [`PaneScaffoldDirective`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/PaneScaffoldDirective) and [`ThreePaneScaffoldValue`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/ThreePaneScaffoldValue) or
[`ThreePaneScaffoldState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/ThreePaneScaffoldState) separately. This flexibility lets you implement
custom logic for pane spacing and determine how many panes should be displayed
simultaneously. You can also enable predictive back support by adding
`ThreePaneScaffoldPredictiveBackHandler`.

> [!NOTE]
> **Note:** If you need custom back navigation logic, use `PredictiveBackHandler` directly instead of `ThreePaneScaffoldPredictiveBackHandler`.

## Add `ThreePaneScaffoldPredictiveBackHandler`

Attach the predictive back handler that takes a scaffold navigator instance and
specify the `backBehavior`. This determines how destinations are popped from the
backstack during back navigation. Then pass the `scaffoldDirective` and
`scaffoldState` to `SupportingPaneScaffold`. Use the overload that accepts a
`ThreePaneScaffoldState`, passing in `scaffoldNavigator.scaffoldState`.

Define the main and supporting panes within `SupportingPaneScaffold`. Use
`AnimatedPane` for default pane animations.

After you implement these steps, your code should look similar to the following:


```kotlin
val scaffoldNavigator = rememberSupportingPaneScaffoldNavigator()
val scope = rememberCoroutineScope()

ThreePaneScaffoldPredictiveBackHandler(
    navigator = scaffoldNavigator,
    backBehavior = BackNavigationBehavior.PopUntilScaffoldValueChange
)

SupportingPaneScaffold(
    directive = scaffoldNavigator.scaffoldDirective,
    scaffoldState = scaffoldNavigator.scaffoldState,
    mainPane = {
        MainPane(
            shouldShowSupportingPaneButton = scaffoldNavigator.scaffoldValue.secondary == PaneAdaptedValue.Hidden,
            onNavigateToSupportingPane = {
                scope.launch {
                    scaffoldNavigator.navigateTo(ThreePaneScaffoldRole.Secondary)
                }
            }
        )
    },
    supportingPane = { SupportingPane(scaffoldNavigator = scaffoldNavigator) },
)
```

<br />