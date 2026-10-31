---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature
url: https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature
source: md.txt
---

# Dynamic Feature Module Recipe

This recipe demonstrates how to integrate Dynamic Feature Module (DFM) with Navigation 3. Make sure that you're already familiar with [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery#customize_delivery) to proceed with this recipe.

## How it works

This example defines three keys for screens in three different modules and delivery options:

- `Home`: A screen in the main `:app` module that displays buttons to navigate into the screens from the dynamic feature modules.
- `InstallTimeModule.Home`: A screen in the `:dynamicfeature:installtime` module, which is installed at delivery time. For example, this might be used for an asset-rich onboarding module that is needed when the app is first installed, but which can be deleted after the onboarding is complete.
- `OnDemandModule.Home`: A screen in the `:dynamicfeature:ondemand` module, which is installed on-demand. For example, this might be used for a module with a large file size that only a small subset of the userbase is expected to use.

### `DynamicModule`

`DynamicModule` is an abstract class that is used to model a dynamic feature module. Namely, it stores both the `moduleName` and the `entryBuilderClassName` for the corresponding `DynamicModuleEntryBuilder` (described in the next section).

    object ExampleModule : DynamicModule(
        entryBuilderClassName = "com.example.module.ExampleEntryBuilder",
        moduleName = "example"
    ) {
        @Serializable
        data object Screen : AppNavKey
    }

### `DynamicModuleEntryBuilder`

Each dynamic feature module **must** include an implementation of `DynamicModuleEntryBuilder`, which is used to add the entries for that module to the `entryProvider` in the main `:app` module.

    // Inside :example module

    @Suppress("unused")
    class ExampleEntryBuilder : DynamicModuleEntryBuilder {
        override fun EntryProviderScope<NavKey>.build() {
            appEntry<ExampleModule.Screen> {
                ExampleScreen()
            }
        }
    }

    @Composable
    private fun ExampleScreen() {
        // ...
    }

### `buildDynamicEntries()`

An extension function of `EntryProviderScope` which resolves the `DynamicModuleEntryBuilder` for that module and calls it's `build()` function.

    // Inside :app module

    val ALL_DYNAMIC_MODULES_MAP = listOf(
       ExampleModule,
       // ...
    ).associateBy { it.moduleName }

    NavDisplay(
        // ...
        entryProvider = entryProvider {
            // ...
            dynamicFeatureManager.installedModules
                .mapNotNull { ALL_DYNAMIC_MODULES_MAP[it] }
                .forEach { buildDynamicEntries(it) }
        }
    )

### `DynamicFeatureManager`

A class that manages dynamic feature module installation.

To navigate to a key contained within a dynamic feature module, use the `installModule` method, which automatically handles installing the respective module if it isn't already installed and executing a callback when the module is installed. If the module is already installed, this callback is invoked immediately.

    // Inside :app module

    // Initialize the manager
    val dynamicFeatureManager = retainDynamicFeatureManager()

    // E.g. in a Button's onClick
    dynamicFeatureManager.installModule(
        moduleName = ExampleModule.moduleName,
        onModuleInstalled = {
            backStack.add(ExampleModule.Screen)
        }
    )

To monitor the installation progress, attach the manager into `DynamicFeatureDownloadProgressDialog` composable:

    DynamicFeatureDownloadProgressDialog(dynamicFeatureManager)

### Proguard rules

To make sure that the class referred to by the `entryBuilderClassName` can be accessed when R8 minification is turned on, add this rule into `proguard-rules.pro`:

    -keep class * implements com.example.nav3recipes.dynamicfeature.DynamicModuleEntryBuilder {
       public <init>();
    }

## How to test locally

To test if the implementation is working, simply run the app and navigate into the target module's entries. Android Studio will include all the dynamic feature modules on the run configuration by default.

To simulate the module downloading and installation, use [bundletool](https://github.com/google/bundletool/releases).
> **Tip:** If you installed `bundletool` via Homebrew (`brew install bundletool`), you can replace `java -jar bundletool.jar` with just `bundletool` in the commands below.

1. Build the project AAB.

       ./gradlew :app:bundleDebug

2. Convert the built AAB into APKS with local testing enabled using `bundletool`.

       java -jar bundletool.jar build-apks --local-testing --bundle <project-path>/app/build/outputs/bundle/debug/app-debug.aab --output app-debug.apks --overwrite

3. Install the converted APKS using `bundletool`.

       java -jar bundletool.jar install-apks --apks app-debug.apks

4. Run the app via the launcher icon.

Now you should be able to see the download progress dialog when navigating to an on-demand module entry for the first time.

## Implementation notes

`DynamicFeatureManager`

- This recipe only supports a single installation session at any given time. If your app needs to use multiple sessions concurrently, you should adapt the manager to track multiple sessions simultaneously.
- This recipe doesn't implement automatic retries for things like network errors or internal errors. See [Handle request errors](https://developer.android.com/guide/playcore/feature-delivery/on-demand#handle_request_errors) for additional information.
- If your app [accesses resources and assets from a different module](https://developer.android.com/guide/playcore/feature-delivery/on-demand#access_resource_different_module), note that this recipe doesn't automatically reinstall `SplitCompat` after a module has been installed.

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
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.content.ContentGreen
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable

class DynamicFeatureActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val backStack = rememberNavBackStack(Home)
            val dynamicFeatureManager = retainDynamicFeatureManager()

            DynamicFeatureDownloadProgressDialog(dynamicFeatureManager)

            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                modifier = Modifier.fillMaxSize(),
                entryProvider = entryProvider {
                    appEntry<Home> {
                        HomeScreen(
                            onNavigateToInstallTime = {
                                dynamicFeatureManager.installModule(
                                    moduleName = InstallTimeModule.moduleName,
                                    onModuleInstalled = {
                                        backStack.add(InstallTimeModule.Home)
                                    }
                                )
                            },
                            onNavigateToOnDemand = {
                                dynamicFeatureManager.installModule(
                                    moduleName = OnDemandModule.moduleName,
                                    onModuleInstalled = {
                                        backStack.add(OnDemandModule.Home)
                                    }
                                )
                            },
                        )
                    }

                    dynamicFeatureManager.installedModules
                        .mapNotNull { ALL_DYNAMIC_MODULES_MAP[it] }
                        .forEach { buildDynamicEntries(it) }
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

@Serializable
private data object Home : AppNavKey

private val ALL_DYNAMIC_MODULES_MAP = listOf(
    InstallTimeModule,
    OnDemandModule
).associateBy { it.moduleName }

object InstallTimeModule : DynamicModule(
    entryBuilderClassName = "com.example.dynamicfeature.installtime.InstallTimeEntryBuilder",
    moduleName = "installtime",
) {
    @Serializable
    data object Home : AppNavKey {
        override fun toContentKey(): Any {
            return "InstallTimeHome"
        }
    }
}

object OnDemandModule : DynamicModule(
    entryBuilderClassName = "com.example.dynamicfeature.ondemand.OnDemandEntryBuilder",
    moduleName = "ondemand"
) {
    @Serializable
    data object Home : AppNavKey {
        override fun toContentKey(): Any {
            return "OnDemandHome"
        }
    }
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

import android.content.Context
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.IntentSenderRequest
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.Stable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.retain.retain
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import com.google.android.play.core.ktx.bytesDownloaded
import com.google.android.play.core.ktx.errorCode
import com.google.android.play.core.ktx.sessionId
import com.google.android.play.core.ktx.status
import com.google.android.play.core.ktx.totalBytesToDownload
import com.google.android.play.core.splitinstall.SplitInstallManagerFactory
import com.google.android.play.core.splitinstall.SplitInstallRequest
import com.google.android.play.core.splitinstall.SplitInstallSessionState
import com.google.android.play.core.splitinstall.SplitInstallStateUpdatedListener
import com.google.android.play.core.splitinstall.model.SplitInstallSessionStatus

@Composable
fun retainDynamicFeatureManager(): DynamicFeatureManager {
    val applicationContext = LocalContext.current.applicationContext

    val manager = retain {
        DynamicFeatureManager(applicationContext)
    }

    DisposableEffect(manager) {
        onDispose {
            manager.dispose()
        }
    }

    return manager
}

sealed interface InstallStatus {
    data object Idle : InstallStatus
    data class Pending(val sessionId: Int) : InstallStatus
    data class Downloading(val sessionId: Int, val progress: Float) : InstallStatus
    data class Installing(val sessionId: Int) : InstallStatus
    data class RequiresUserConfirmation(val state: SplitInstallSessionState) : InstallStatus
    data class Failed(val sessionId: Int, val errorCode: Int) : InstallStatus
}

@Stable
class DynamicFeatureManager(context: Context) {
    private val splitInstallManager = SplitInstallManagerFactory.create(context)

    // Maintain a single listener for the lifetime of the manager
    private val listener = SplitInstallStateUpdatedListener { state ->
        val sessionId = state.sessionId
        // Capture session ID if we're expecting an install but haven't got the ID yet (race condition)
        if (activeSessionId == null && activeModuleName != null) {
            if (state.moduleNames().contains(activeModuleName)) {
                activeSessionId = sessionId
            }
        }

        if (sessionId == activeSessionId) {
            updateStatus(state)
        }
    }

    private var activeSessionId: Int? = null
    private var activeModuleName: String? = null
    private var onModuleInstalledCallback: (() -> Unit)? = null

    var status by mutableStateOf<InstallStatus>(InstallStatus.Idle)
        private set

    var installedModules: Set<String> by mutableStateOf(splitInstallManager.installedModules.toSet())
        private set

    init {
        splitInstallManager.registerListener(listener)
    }

    fun dispose() {
        splitInstallManager.unregisterListener(listener)
    }

    fun installModule(moduleName: String, onModuleInstalled: () -> Unit) {
        if (splitInstallManager.installedModules.contains(moduleName)) {
            onModuleInstalled()
            return
        }

        // Avoid starting multiple installs if one is already in progress
        if (status !is InstallStatus.Idle && status !is InstallStatus.Failed) return

        activeModuleName = moduleName
        onModuleInstalledCallback = onModuleInstalled
        // Use a placeholder ID to indicate we are waiting for a session
        status = InstallStatus.Pending(-1)

        splitInstallManager.startInstall(
            SplitInstallRequest.newBuilder().addModule(moduleName).build()
        ).addOnSuccessListener { sessionId ->
            if (activeSessionId == null) {
                activeSessionId = sessionId
            }
            // Only update status if it hasn't progressed beyond our placeholder
            if (status is InstallStatus.Pending && (status as InstallStatus.Pending).sessionId == -1) {
                status = InstallStatus.Pending(sessionId)
            }
        }.addOnFailureListener {
            status = InstallStatus.Failed(-1, -1)
            onModuleInstalledCallback = null
        }
    }

    private fun clearSessionState() {
        activeSessionId = null
        activeModuleName = null
        onModuleInstalledCallback = null
    }

    private fun updateStatus(state: SplitInstallSessionState) {
        val sessionId = state.sessionId
        when (state.status) {
            SplitInstallSessionStatus.PENDING -> {
                status = InstallStatus.Pending(sessionId)
            }

            SplitInstallSessionStatus.DOWNLOADING -> {
                val progress = if (state.totalBytesToDownload > 0) {
                    state.bytesDownloaded.toFloat() / state.totalBytesToDownload
                } else 0f
                status = InstallStatus.Downloading(sessionId, progress)
            }

            SplitInstallSessionStatus.DOWNLOADED -> {
                status = InstallStatus.Installing(sessionId)
            }

            SplitInstallSessionStatus.INSTALLING -> {
                status = InstallStatus.Installing(sessionId)
            }

            SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION -> {
                status = InstallStatus.RequiresUserConfirmation(state)
            }

            SplitInstallSessionStatus.INSTALLED -> {
                status = InstallStatus.Idle
                installedModules = splitInstallManager.installedModules.toSet()
                onModuleInstalledCallback?.invoke()
                clearSessionState()
            }

            SplitInstallSessionStatus.FAILED -> {
                status = InstallStatus.Failed(sessionId, state.errorCode)
                clearSessionState()
            }

            SplitInstallSessionStatus.CANCELING -> {
                status = InstallStatus.Pending(sessionId)
            }

            SplitInstallSessionStatus.CANCELED -> {
                status = InstallStatus.Idle
                clearSessionState()
            }

            SplitInstallSessionStatus.UNKNOWN -> {
                status = InstallStatus.Failed(sessionId, -1)
                clearSessionState()
            }
        }
    }

    fun startConfirmationDialogForResult(
        state: SplitInstallSessionState,
        launcher: ActivityResultLauncher<IntentSenderRequest>
    ) {
        splitInstallManager.startConfirmationDialogForResult(state, launcher)
    }

    fun cancelInstallModule() {
        activeSessionId?.let { id ->
            splitInstallManager.cancelInstall(id)
        }
        status = InstallStatus.Idle
        clearSessionState()
    }
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

import androidx.navigation3.runtime.EntryProviderScope
import androidx.navigation3.runtime.NavKey

interface AppNavKey : NavKey {
    // By default, `toString()` is used to generate the `contentKey` for NavEntries.
    // Instead of overriding `toString()`, we provide a dedicated `toContentKey()` function to make
    // it possible to uniquely identify keys for nested objects with the same simple name
    // (e.g., `ModuleA.Home` vs `ModuleB.Home`), without polluting the `toString()` representation.
    fun toContentKey(): Any = this.toString()
}

/**
 * An extension on [EntryProviderScope] specifically for [AppNavKey]s that overrides the default
 * `contentKey` resolution. It explicitly resolves the key via `it.toContentKey()` instead of the default
 * string representation.
 */
inline fun <reified K : AppNavKey> EntryProviderScope<NavKey>.appEntry(
    noinline clazzContentKey: (key: @JvmSuppressWildcards K) -> Any = { it.toContentKey() },
    metadata: Map<String, Any> = emptyMap(),
    noinline content: @androidx.compose.runtime.Composable (K) -> Unit,
) {
    addEntryProvider(K::class, clazzContentKey, { metadata }, content)
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


import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import kotlin.math.roundToInt

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DynamicFeatureDownloadProgressDialog(
    dynamicFeatureManager: DynamicFeatureManager,
    modifier: Modifier = Modifier,
) {
    val status = dynamicFeatureManager.status

    if (status is InstallStatus.Idle) return

    val launcher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.StartIntentSenderForResult()
    ) {
        // The session status will be updated automatically via the
        // SplitInstallStateUpdatedListener in DynamicFeatureManager,
        // so no explicit handling is required here.
    }

    val progress = if (status is InstallStatus.Downloading) status.progress else 0f
    val progressPercentage = "${(progress * 100).roundToInt()}%"

    AlertDialog(
        onDismissRequest = {},
        modifier = modifier,
        title = {
            Text(text = getStatusTitle(status))
        },
        text = {
            Column(
                verticalArrangement = Arrangement.spacedBy(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier.fillMaxWidth(),
            ) {
                if (status is InstallStatus.Downloading) {
                    CircularProgressIndicator(
                        progress = { progress },
                        modifier = Modifier.semantics {
                            contentDescription = "Downloading: $progressPercentage"
                        }
                    )
                    Text(
                        text = progressPercentage,
                        style = MaterialTheme.typography.labelSmall,
                    )
                } else if (status !is InstallStatus.Failed && status !is InstallStatus.RequiresUserConfirmation) {
                    CircularProgressIndicator()
                }

                if (status is InstallStatus.Failed) {
                    Text(
                        text = "Error code: ${status.errorCode}",
                        color = MaterialTheme.colorScheme.error,
                        style = MaterialTheme.typography.bodySmall,
                    )
                }
            }
        },
        confirmButton = {
            if (status is InstallStatus.RequiresUserConfirmation) {
                Button(onClick = {
                    dynamicFeatureManager.startConfirmationDialogForResult(
                        status.state,
                        launcher
                    )
                }) {
                    Text(text = "Confirm Download")
                }
            }
        },
        dismissButton = {
            TextButton(onClick = dynamicFeatureManager::cancelInstallModule) {
                Text(text = "Cancel")
            }
        }
    )
}

private fun getStatusTitle(status: InstallStatus): String {
    return when (status) {
        is InstallStatus.Pending -> "Requesting..."
        is InstallStatus.Downloading -> "Downloading..."
        is InstallStatus.Installing -> "Installing..."
        is InstallStatus.RequiresUserConfirmation -> "Requires Confirmation"
        is InstallStatus.Failed -> "Installation Failed"
        else -> ""
    }
}
```

````
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

import androidx.navigation3.runtime.EntryProviderScope
import androidx.navigation3.runtime.NavKey

/**
 * Base class for defining a dynamic feature module.
 *
 * Caches the [DynamicModuleEntryBuilder] instance to guarantee that the reflection instantiation
 * via [Class.forName] and [Class.newInstance] occurs exactly once per application process lifetime,
 * optimizing performance during recompositions when the `entryProvider` block is re-evaluated.
 */
abstract class DynamicModule(
    val entryBuilderClassName: String,
    val moduleName: String,
) {
    private var dynamicModuleEntryBuilder: DynamicModuleEntryBuilder? = null

    internal fun getDynamicModuleEntryBuilder(): DynamicModuleEntryBuilder {
        return dynamicModuleEntryBuilder ?: (Class.forName(entryBuilderClassName)
            .getConstructor()
            .newInstance() as DynamicModuleEntryBuilder).also { dynamicModuleEntryBuilder = it }
    }
}

/**
 * Interface that every dynamic feature module must implement to register its navigation entries.
 *
 * It is invoked by [buildDynamicEntries] to add the module's routes into the base [EntryProviderScope].
 *
 * **Example:**
 * ```kotlin
 * class ExampleEntryBuilder : DynamicModuleEntryBuilder {
 *     override fun EntryProviderScope<NavKey>.build() {
 *         appEntry<ExampleModule.Screen> {
 *             ExampleScreen()
 *         }
 *     }
 * }
 * ```
 */
fun interface DynamicModuleEntryBuilder {
    fun EntryProviderScope<NavKey>.build()
}

fun EntryProviderScope<NavKey>.buildDynamicEntries(
    module: DynamicModule,
) {
    with(module.getDynamicModuleEntryBuilder()) {
        build()
    }
}
````