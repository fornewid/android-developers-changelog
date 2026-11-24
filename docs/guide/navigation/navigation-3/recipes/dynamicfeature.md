---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature
url: https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature
source: md.txt
---

> Documentation index: https://developer.android.com/guide/navigation/navigation-3/llms.txt

# Dynamic Feature Module Recipe

This recipe demonstrates how to integrate Dynamic Feature Modules (DFMs) with Navigation 3 using `androidx.navigation3:navigation3-dynamic-features`. Make sure you are familiar with [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery.md.txt#customize_delivery) before proceeding.

## How it works

This example defines screens across three modules with different delivery modes:

- `Home`: A screen in the base `:app` module with buttons to navigate to each dynamic feature module.
- `InstallTimeHome`: The initial key for `:dynamicfeature:installtime`, which is installed with the app at delivery time.
- `OnDemandHome`: The initial key for `:dynamicfeature:ondemand`, which is downloaded on demand when navigated to. `:dynamicfeature:ondemand` also defines private sub-screen keys (`OnDemandDetail` and `OnDemandSettings`) that `:app` does not depend on.

### `DynamicFeatureNavEntryDecorator`

`rememberDynamicFeatureNavEntryDecorator` creates a `NavEntryDecorator` that drives module installation through `SplitInstallManager` and swaps in the module's destination once installation completes.

Pass it to `NavDisplay` in `entryDecorators` (alongside `rememberSaveableStateHolderNavEntryDecorator()`) and build your `entryProvider` with `dynamicFeatureDecorator.entryProvider`, registering dynamic modules via `dynamicFeatureModule`. See [`DynamicFeatureActivity.kt`](https://developer.android.com/static/guide/navigation/navigation-3/recipes/DynamicFeatureActivity.kt) for the full setup.

Navigating to a dynamic module works the same as any other screen: add its initial key (`InstallTimeHome` or `OnDemandHome`) to the back stack. If the module is not yet installed, `DynamicFeatureNavEntryDecorator` starts installation, renders `loadingContent` (or `defaultLoadingContent`), runs `SplitCompat.install`, and transitions to the module's real entry once installed. If the entry leaves the back stack before installation finishes, the active install session is canceled automatically.

Your `Application` class must extend `SplitCompatApplication` (or call `SplitCompat.install(this)` in `attachBaseContext`) so code and resources of newly downloaded modules can be used immediately without restarting the app (and for `--local-testing` installs).

### `DynamicFeatureModuleEntryProvider`

Each dynamic feature module implements `DynamicFeatureModuleEntryProvider<NavKey>` with a public zero-argument constructor to register its `initialKey` and any internal sub-screen keys:

```kotlin
@Serializable
private sealed interface OnDemandSubKey : NavKey

@Serializable
private data class OnDemandDetail(val id: String) : OnDemandSubKey

class OnDemandModuleEntryProvider : DynamicFeatureModuleEntryProvider<NavKey> {
    override fun EntryProviderScope<NavKey>.buildEntries() {
        entry<OnDemandHome> {
            val navigator = rememberNavigator()
            OnDemandModuleScreen(
                onNavigateToDetail = { id -> navigator.goTo(OnDemandDetail(id)) },
                // ...
            )
        }
        entry<OnDemandDetail> { key ->
            // ...
        }
    }
}
```

### Sharing navigation state via Hilt `@EntryPoint`

Because dynamic feature modules depend on `:app` (reversed dependency direction) and `DynamicFeatureModuleEntryProvider` is instantiated via reflection, `:app` annotates `DynamicFeatureActivity` with `@AndroidEntryPoint` and exposes `@ActivityRetainedScoped` `DynamicFeatureNavigator` through a Hilt `@EntryPoint`. The dynamic feature module adds `implementation(libs.hilt.android)` and retrieves the navigator via `EntryPointAccessors`:

```kotlin
// Inside :app
@EntryPoint
@InstallIn(ActivityComponent::class)
interface DynamicFeatureEntryPoint {
    fun navigator(): DynamicFeatureNavigator
}

// Inside :dynamicfeature:ondemand
@Composable
private fun rememberNavigator(): DynamicFeatureNavigator {
    val activity = checkNotNull(LocalActivity.current)
    return remember(activity) {
        EntryPointAccessors.fromActivity<DynamicFeatureEntryPoint>(activity).navigator()
    }
}
```
> **Note:** `DynamicFeatureNavigator` retains the back stack across configuration changes, but does not survive process death. Back it with `SavedStateHandle` if your app needs to restore the back stack after process death.

### ProGuard rules

`navigation3-dynamic-features` bundles consumer keep rules that keep `DynamicFeatureModuleEntryProvider` implementations and their public zero-argument constructors when R8 minification is enabled, so no manual rules are needed in `proguard-rules.pro`.

## How to test locally

Running the `:app` configuration from Android Studio installs all dynamic feature modules immediately by default.

To simulate on-demand downloading and installation locally, use [bundletool](https://github.com/google/bundletool/releases):
> **Tip:** If you installed `bundletool` via Homebrew (`brew install bundletool`), you can replace `java -jar bundletool.jar` with `bundletool` in the commands below. Pass `--device-id <serial>` if multiple devices or emulators are connected.

1. Build the debug app bundle:

   ```shell
   ./gradlew :app:bundleDebug
   ```
2. Build local-testing APKs from the bundle:

   ```shell
   java -jar bundletool.jar build-apks --local-testing --bundle app/build/outputs/bundle/debug/app-debug.aab --output app-debug.apks --overwrite
   ```
3. Install the APKs onto your connected device or emulator:

   ```shell
   java -jar bundletool.jar install-apks --apks app-debug.apks
   ```
4. Launch **Nav3Recipes** from the device launcher, open **Dynamic Feature Module Navigation** , and tap **Go to On Demand Module Screen** to observe the download progress dialog and transition into the on-demand module.

## Implementation notes

- This recipe does not implement automatic retries for failed installations (`SplitInstallSessionStatus.FAILED` displays an error dialog and removes the entry when dismissed). See [Handle request errors](https://developer.android.com/guide/playcore/feature-delivery/on-demand.md.txt#handle_request_errors) for retry guidance.

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/dynamicfeature)

```
/*
 * Copyright 2026 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.dynamicfeature

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.LoadingIndicator
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.dynamicfeatures.rememberDynamicFeatureNavEntryDecorator
import androidx.navigation3.dynamicfeatures.rememberSplitInstallManager
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import com.google.android.play.core.splitinstall.SplitInstallSessionState
import com.google.android.play.core.splitinstall.model.SplitInstallSessionStatus
import dagger.hilt.android.AndroidEntryPoint
import javax.inject.Inject
import kotlinx.serialization.Serializable

@Serializable
internal data object Home : NavKey

/** Initial nav key of install-time dynamic module. */
@Serializable
data object InstallTimeHome : NavKey

/** Initial nav key of on-demand dynamic module. */
@Serializable
data object OnDemandHome : NavKey

@AndroidEntryPoint
class DynamicFeatureActivity : ComponentActivity() {

    @Inject
    lateinit var navigator: DynamicFeatureNavigator

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val splitInstallManager = rememberSplitInstallManager()
            val dynamicFeatureDecorator = rememberDynamicFeatureNavEntryDecorator<NavKey>(
                splitInstallManager = splitInstallManager,
                defaultLoadingContent = { LoadingIndicator() }
            )

            NavDisplay(
                backStack = navigator.backStack,
                onBack = { navigator.goBack() },
                modifier = Modifier.fillMaxSize(),
                entryDecorators = listOf(
                    rememberSaveableStateHolderNavEntryDecorator(),
                    dynamicFeatureDecorator,
                ),
                entryProvider = dynamicFeatureDecorator.entryProvider {
                    entry<Home> {
                        HomeScreen(
                            onNavigateToInstallTime = {
                                navigator.goTo(InstallTimeHome)
                            },
                            onNavigateToOnDemand = {
                                navigator.goTo(OnDemandHome)
                            },
                        )
                    }

                    dynamicFeatureModule(
                        initialKey = InstallTimeHome,
                        moduleName = "installtime",
                        entryProviderClassName = "com.example.dynamicfeature.installtime.InstallTimeModuleEntryProvider"
                    )

                    dynamicFeatureModule(
                        initialKey = OnDemandHome,
                        moduleName = "ondemand",
                        entryProviderClassName = "com.example.dynamicfeature.ondemand.OnDemandModuleEntryProvider",
                        loadingContent = { state ->
                            val confirmationLauncher = rememberLauncherForActivityResult(
                                contract = ActivityResultContracts.StartIntentSenderForResult()
                            ) { result ->
                                if (result.resultCode == RESULT_CANCELED) {
                                    navigator.backStack.remove(OnDemandHome)
                                }
                            }
                            when (state.status()) {
                                SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION -> {
                                    LaunchedEffect(state.sessionId()) {
                                        splitInstallManager.startConfirmationDialogForResult(
                                            state,
                                            confirmationLauncher,
                                        )
                                    }
                                }
                                SplitInstallSessionStatus.CANCELED -> {
                                    LaunchedEffect(Unit) {
                                        navigator.backStack.remove(OnDemandHome)
                                    }
                                }
                                SplitInstallSessionStatus.FAILED -> {
                                    InstallationFailedDialog(
                                        errorCode = state.errorCode(),
                                        onDismiss = { navigator.backStack.remove(OnDemandHome) },
                                    )
                                }
                                else -> {
                                    InstallingModuleDialog(
                                        state = state,
                                        onCancel = { navigator.backStack.remove(OnDemandHome) },
                                    )
                                }
                            }
                        }
                    )
                }
            )
        }
    }
}

@Composable
fun HomeScreen(
    onNavigateToInstallTime: () -> Unit,
    onNavigateToOnDemand: () -> Unit,
    modifier: Modifier = Modifier,
) {
    ContentGreen(
        title = "Home screen",
        modifier = modifier,
    ) {
        Column {
            Button(onClick = dropUnlessResumed { onNavigateToInstallTime() }) {
                Text(text = "Go to Install Time Module Screen")
            }
            Button(onClick = dropUnlessResumed { onNavigateToOnDemand() }) {
                Text(text = "Go to On Demand Module Screen")
            }
        }
    }
}

@Composable
private fun InstallingModuleDialog(
    state: SplitInstallSessionState,
    onCancel: () -> Unit,
) {
    AlertDialog(
        onDismissRequest = {},
        title = { Text("Installing module...") },
        text = {
            val totalBytes = state.totalBytesToDownload()
            if (state.status() == SplitInstallSessionStatus.DOWNLOADING && totalBytes > 0) {
                LinearProgressIndicator(
                    progress = { state.bytesDownloaded().toFloat() / totalBytes },
                    modifier = Modifier.fillMaxWidth(),
                )
            } else {
                LinearProgressIndicator(modifier = Modifier.fillMaxWidth())
            }
        },
        confirmButton = {},
        dismissButton = {
            TextButton(onClick = onCancel) {
                Text("Cancel")
            }
        },
    )
}

@Composable
private fun InstallationFailedDialog(
    errorCode: Int,
    onDismiss: () -> Unit,
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("Installation failed") },
        text = { Text("Failed to install module (error code: $errorCode).") },
        confirmButton = {
            TextButton(onClick = onDismiss) {
                Text("OK")
            }
        },
    )
}
```

```
/*
 * Copyright 2026 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.dynamicfeature

import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.snapshots.SnapshotStateList
import androidx.navigation3.runtime.NavKey
import dagger.hilt.EntryPoint
import dagger.hilt.InstallIn
import dagger.hilt.android.components.ActivityComponent
import dagger.hilt.android.scopes.ActivityRetainedScoped
import javax.inject.Inject

@ActivityRetainedScoped
class DynamicFeatureNavigator @Inject constructor() {
    val backStack: SnapshotStateList<NavKey> = mutableStateListOf(Home)

    fun goTo(destination: NavKey) {
        backStack.add(destination)
    }

    fun goBack() {
        backStack.removeLastOrNull()
    }
}

@EntryPoint
@InstallIn(ActivityComponent::class)
interface DynamicFeatureEntryPoint {
    fun navigator(): DynamicFeatureNavigator
}
```