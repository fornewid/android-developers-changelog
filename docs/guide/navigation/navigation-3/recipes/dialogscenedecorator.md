---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/dialogscenedecorator
url: https://developer.android.com/guide/navigation/navigation-3/recipes/dialogscenedecorator
source: md.txt
---

# Dialog Scene Decorator Recipe

This recipe demonstrates one approach to displaying a scene within a dialog. For example, this could be used to display a list-detail settings UI as an overlay when the app is in an expanded window, but as full screen pages otherwise.

## How it works

To display a scene within a dialog, you need to do the following:

1. **Create a dialog `SceneDecorationStrategy`** : This recipe defines the `DialogSceneDecoratorStrategy` as well as the `DialogDecoratorScene` it uses to present an input `Scene` within a dialog. When defining a dialog scene decoration strategy, consider the following:
   1. **When can a scene be displayed within a dialog?** In this recipe, scenes are only displayed in a dialog if the window width is at least expanded.
   2. **What metadata should determine if a scene can be displayed within a dialog?** In this recipe, a scene is displayed in a dialog if the first entry within that scene has the `DialogSceneMetadataKey` metadata. Depending on your use case, another approach such as requiring all entries within the scene to have the same metadata might be more appropriate.
   3. **What is the dismissal behavior of the dialog?** In this recipe, clicking outside the dialog removes all the entries in the scene while a back gesture or press only removes one at a time. The recipe provides configuration for this behavior through the `DialogDecoratorSceneConfiguration` class.
2. **Use your dialog `SceneDecorationStrategy`** : To use your scene decorator strategy, pass it to the `NavDisplay` as part of the `sceneDecoratorStrategies` parameter.
   1. **Caution:** Because `NavDisplay` doesn't decorate `OverlayScene` instances, you might need to pay attention to the position of your dialog scene decoration strategy within the `sceneDecoratorStrategies` list. Decorating a scene with it would prevent decoration by following scene decoration strategies.
   2. **Caution:** When implementing `onDismissAll` using `contentKey`s to identify the entries to dismiss, be aware that by default `contentKey` uses `key.toString()`. In this recipe we use `backStack.removeAll { it.toString() in contentKeys }` which works for simple object keys but may need adjustment for more complex keys or custom `contentKey` implementations.

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/dialogscenedecorator)

```
package com.example.nav3recipes.dialogscenedecorator

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.SharedTransitionLayout
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentBlue
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.content.ContentYellow
import com.example.nav3recipes.scenes.listdetail.ListDetailScene
import com.example.nav3recipes.scenes.listdetail.rememberListDetailSceneStrategy
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable

@Serializable
private data object Main : NavKey

@Serializable
private data object SettingsList : NavKey

@Serializable
private data object SettingsDetail : NavKey

class DialogSceneDecoratorActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setEdgeToEdgeConfig()

        setContent {
            val backStack = rememberNavBackStack(Main)
            val listDetailSceneStrategy = rememberListDetailSceneStrategy<NavKey>()

            val dialogSceneDecoratorStrategy = rememberDialogSceneDecoratorStrategy<NavKey>(
                onDismissAll = { entriesToDismiss ->
                    // Caution: This relies on the default behavior of NavEntry using key.toString()
                    // to define its contentKey property.
                    entriesToDismiss.forEach { entry ->
                        backStack
                            .indexOfLast { it.toString() == entry.contentKey }
                            .takeIf { it >= 0 }
                            ?.let { backStack.removeAt(it) }
                    }
                }
            )

            SharedTransitionLayout {
                NavDisplay(
                    backStack = backStack,
                    onBack = { backStack.removeLastOrNull() },
                    sceneStrategies = listOf(listDetailSceneStrategy),
                    sceneDecoratorStrategies = listOf(dialogSceneDecoratorStrategy),
                    sharedTransitionScope = this,
                    entryProvider = entryProvider {
                        entry<Main> {
                            ContentGreen("Welcome to Nav3") {
                                Button(onClick = dropUnlessResumed {
                                    backStack.add(SettingsList)
                                }) {
                                    Text("Click to open settings")
                                }
                            }
                        }
                        entry<SettingsList>(
                            metadata = DialogSceneDecoratorStrategy.sceneDialog(
                                DialogDecoratorSceneConfiguration(
                                    backDismissalBehavior = DismissalBehavior.Single
                                )
                            ) + ListDetailScene.listPane()
                        ) {
                            ContentBlue(
                                title = "Settings List",
                            ) {
                                Button(onClick = dropUnlessResumed {
                                    if (backStack.last() !is SettingsDetail) {
                                        backStack.add(SettingsDetail)
                                    }
                                }) {
                                    Text("Open detail")
                                }
                            }
                        }
                        entry<SettingsDetail>(
                            metadata = ListDetailScene.detailPane()
                        ) {
                            ContentYellow("Settings Detail")
                        }
                    }
                )
            }
        }
    }
}
```

```
package com.example.nav3recipes.dialogscenedecorator

import androidx.activity.compose.BackHandler
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.adaptive.currentWindowAdaptiveInfo
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import androidx.compose.ui.window.SecureFlagPolicy
import androidx.navigation3.runtime.NavEntry
import androidx.navigation3.runtime.NavMetadataKey
import androidx.navigation3.runtime.get
import androidx.navigation3.runtime.metadata
import androidx.navigation3.scene.OverlayScene
import androidx.navigation3.scene.Scene
import androidx.navigation3.scene.SceneDecoratorStrategy
import androidx.navigation3.scene.SceneDecoratorStrategyScope
import androidx.window.core.layout.WindowSizeClass

fun DialogProperties.copy(
    dismissOnBackPress: Boolean = this.dismissOnBackPress,
    dismissOnClickOutside: Boolean = this.dismissOnClickOutside,
    securePolicy: SecureFlagPolicy = this.securePolicy,
    usePlatformDefaultWidth: Boolean = this.usePlatformDefaultWidth,
    decorFitsSystemWindows: Boolean = this.decorFitsSystemWindows,
    windowTitle: String = this.windowTitle
): DialogProperties = DialogProperties(
    dismissOnBackPress = dismissOnBackPress,
    dismissOnClickOutside = dismissOnClickOutside,
    securePolicy = securePolicy,
    usePlatformDefaultWidth = usePlatformDefaultWidth,
    decorFitsSystemWindows = decorFitsSystemWindows,
    windowTitle = windowTitle
)

enum class DismissalBehavior {
    All, Single
}

/**
 * Configuration for the [DialogDecoratorScene].
 *
 * @property dialogProperties The [DialogProperties] used to configure the dialog.
 * @property backDismissalBehavior Whether all entries in the scene should be dismissed when the
 * back button is pressed. This configuration only applies if the
 * [DialogProperties.dismissOnBackPress] is set to `true`.
 *
 */
class DialogDecoratorSceneConfiguration(
    val dialogProperties: DialogProperties = DialogProperties(),
    val backDismissalBehavior: DismissalBehavior = DismissalBehavior.Single,
    val shape: Shape = RoundedCornerShape(16.dp),
) {
    fun toDialogProperties(): DialogProperties {
        // If the desired behavior is to not dismiss all, the DialogProperties passed to the Dialog
        // needs to be configured to not handle the back press itself.
        if (dialogProperties.dismissOnBackPress && backDismissalBehavior != DismissalBehavior.All) {
            return dialogProperties.copy(dismissOnBackPress = false)
        }

        return dialogProperties
    }

    fun shouldDismissSingleOnBackPress() =
        dialogProperties.dismissOnBackPress && backDismissalBehavior == DismissalBehavior.Single
}

/**
 * [DialogDecoratorScene] is an [OverlayScene] used by [DialogSceneDecoratorStrategy] to present
 * another [Scene] within a [Dialog].
 *
 * @property scene The [Scene] to be displayed within the dialog.
 * @property overlaidEntries The [NavEntry]s that are overlaid by the dialog.
 * @property dialogDecoratorSceneConfiguration The [DialogDecoratorSceneConfiguration] used to
 * configure the dialog scene.
 * @property onBack The callback to be invoked when a back event should be handled
 * @property onDismissAll The callback to be invoked when the entire dialog stack should be dismissed
 **/
class DialogDecoratorScene<T : Any>(
    private val scene: Scene<T>,
    override val overlaidEntries: List<NavEntry<T>>,
    private val dialogDecoratorSceneConfiguration: DialogDecoratorSceneConfiguration,
    private val onBack: () -> Unit,
    private val onDismissAll: () -> Unit
) : OverlayScene<T>, Scene<T> by scene {

    override val content: @Composable () -> Unit = {
        Dialog(
            onDismissRequest = onDismissAll,
            properties = dialogDecoratorSceneConfiguration.toDialogProperties()
        ) {
            Surface(
                shape = dialogDecoratorSceneConfiguration.shape
            ) {
                scene.content()
            }

            // Because back events are dispatched to the currently focused window, this back handler
            // must be contained within the dialog's content to receive the events.
            BackHandler(dialogDecoratorSceneConfiguration.shouldDismissSingleOnBackPress()) {
                onBack()
            }
        }
    }
}

@Composable
fun <T : Any> rememberDialogSceneDecoratorStrategy(
    windowSizeClass: WindowSizeClass = currentWindowAdaptiveInfo().windowSizeClass,
    onDismissAll: ((List<NavEntry<T>>) -> Unit)
): DialogSceneDecoratorStrategy<T> = remember(windowSizeClass, onDismissAll) {
    DialogSceneDecoratorStrategy(windowSizeClass, onDismissAll = onDismissAll)
}

/**
 * A [SceneDecoratorStrategy] that wraps a [Scene] in a [DialogDecoratorScene] if the first
 * [NavEntry] within it has been marked with the [DialogSceneMetadataKey] and the window width
 * is at least [WindowSizeClass.WIDTH_DP_EXPANDED_LOWER_BOUND].
 *
 * If you only need to display a single [NavEntry] in a [Dialog], using
 * [androidx.navigation3.scene.DialogSceneStrategy] instead may be preferable.
 *
 * @property windowSizeClass The current [WindowSizeClass] used to determine if dialogs should be used.
 * @property windowWidthDpBreakpoint the width in dp at or above which a dialog should be displayed.
 * @property onDismissAll callback invoked to dismiss all dialog entries, receives the entries that
 * are currently in the dialog.
 */
class DialogSceneDecoratorStrategy<T : Any>(
    private val windowSizeClass: WindowSizeClass,
    private val windowWidthDpBreakpoint: Int = WindowSizeClass.WIDTH_DP_EXPANDED_LOWER_BOUND,
    private val onDismissAll: (List<NavEntry<T>>) -> Unit
) : SceneDecoratorStrategy<T> {

    override fun SceneDecoratorStrategyScope<T>.decorateScene(scene: Scene<T>): Scene<T> {
        if (!windowSizeClass.isWidthAtLeastBreakpoint(windowWidthDpBreakpoint)) return scene

        val dialogDecoratorSceneConfiguration =
            scene.entries.firstOrNull()?.metadata[DialogSceneMetadataKey] ?: return scene

        // This is critical to ensure that the scenes rendered beneath the dialog don't contain
        // any entries that are in the dialog.
        val overlaidEntries = scene.previousEntries.dropLastWhile { it in scene.entries }

        return DialogDecoratorScene(
            scene,
            overlaidEntries,
            dialogDecoratorSceneConfiguration,
            onBack,
            onDismissAll = { onDismissAll.invoke(scene.entries) })
    }

    companion object {
        object DialogSceneMetadataKey : NavMetadataKey<DialogDecoratorSceneConfiguration>

        fun sceneDialog(dialogDecoratorSceneConfiguration: DialogDecoratorSceneConfiguration = DialogDecoratorSceneConfiguration()): Map<String, Any> =
            metadata {
                put(DialogSceneMetadataKey, dialogDecoratorSceneConfiguration)
            }
    }
}
```