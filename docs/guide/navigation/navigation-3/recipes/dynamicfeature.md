---
title: App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.





# Dynamic Feature Module Recipe

This recipe demonstrates how to integrate Dynamic Feature Module (DFM) with Navigation3. Make sure that you're already familiar with [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery#customize_delivery) to proceed with this recipe.

## How it works

This example defines three routes on three different modules and delivery options:

* `RegularModuleScreen`: A screen that displays two buttons to navigate into other features, located inside base `:app` module.
* `InstallTimeModuleScreen`: A screen with install time delivery option, located inside `:dynamicfeature:installtime` module.
* `OnDemandModuleScreen`: A screen with on-demand delivery option, located inside `:dynamicfeature:ondemand` module.

### `DynamicFeatureContentProvider<T>`

An interface for communication with `dynamicFeatureEntry()`, every entry on the dynamic feature modules **must** implement this interface with `T` as the key/arguments for the entry.

```
// Inside :example module

@Suppress("unused")
class ExampleContentProvider : DynamicFeatureContentProvider<ExampleKey> {
    @Composable
    override fun Content(key: ExampleKey) {
        ExampleScreen()
    }
}

@Composable
private fun ExampleScreen() {
    // ...
}
```

### `dynamicFeatureEntry()`

A modified `entry` function of `EntryProviderScope` which resolves content from the class name that implements `DynamicFeatureContentProvider` using Reflection.

```
// Inside :app module

NavDisplay(
    // ...
    entryProvider = entryProvider {
        // ...
        dynamicFeatureEntry<ExampleKey>(
            clazzName = "fully.qualified.class.name.of.ExampleContentProvider"
        )
    }
)
```

### `DynamicFeatureManager`

A class that manages dynamic feature module installation, comes with a download state to monitor the download progress.

To install a module, simply invoke the function:

```
// Inside :app module

// Initialize the manager
val dynamicFeatureManager = retainDynamicFeatureManager()

// E.g. in a Button's onClick
dynamicFeatureManager.installModule(moduleName = "example") {
    // action when module is installed
    backStack.add(ExampleKey)
}
```

> Note: every navigation into dynamic feature module entries must be performed through the install module function to avoid skipping download on-demand modules that leads to crash.

To monitor the download progress, attach the manager into `DynamicFeatureDownloadProgressDialog` composable:

```
DynamicFeatureDownloadProgressDialog(dynamicFeatureManager)
```

### Proguard rules

To make sure that the dynamic feature content can be accessed when R8 minification turned on, add this rule into `proguard-rules.pro`:

```
-keep class * implements fully.qualified.class.name.of.DynamicFeatureContentProvider {
   public <init>();
}
```

## How to test locally

To test if the implementation is working, simply run the app and navigate into the target module's entries. Android Studio will include all the dynamic feature modules on the run configuration by default.

To simulate the module downloading and installation, use [bundletool](https://github.com/google/bundletool/releases).

1. Build the project AAB.

```
./gradlew :app:bundleDebug
```

2. Convert the built AAB into APKS with local testing enabled using `bundletool`.

```
java -jar bundletool.jar build-apks --local-testing --bundle <project-path>/app/build/outputs/bundle/debug/app-debug.aab --output app-debug.apks --overwrite
```

3. Install the converted APKS using `bundletool`.

```
java -jar bundletool.jar install-apks --apks app-debug.apks
```

4. Run the app via the launcher icon.

Now you should be able to see the download progress dialog when navigating to an on-demand module entry for the first time.

[![](/static/images/picto-icons/code.svg)

Explore

View the full recipe on GitHub.

arrow\_forward](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/dynamicfeature)

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
import androidx.navigation3.runtime.NavKey
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
            val backStack = rememberNavBackStack(RegularModule)
            val dynamicFeatureManager = retainDynamicFeatureManager()

            DynamicFeatureDownloadProgressDialog(dynamicFeatureManager)

            NavDisplay(
                backStack = backStack,
                modifier = Modifier.fillMaxSize(),
                entryProvider = entryProvider {
                    entry<RegularModule> {
                        RegularModuleScreen(
                            onNavigateToInstallTime = {
                                dynamicFeatureManager.installModule(InstallTimeModule.MODULE_NAME) {
                                    backStack.add(InstallTimeModule)
                                }
                            },
                            onNavigateToOnDemand = {
                                dynamicFeatureManager.installModule(OnDemandModule.MODULE_NAME) {
                                    backStack.add(OnDemandModule)
                                }
                            },
                        )
                    }

                    dynamicFeatureEntry<InstallTimeModule>(InstallTimeModule.CLASS_NAME)

                    dynamicFeatureEntry<OnDemandModule>(OnDemandModule.CLASS_NAME)
                }
            )
        }
    }
}

@Composable
fun RegularModuleScreen(
    onNavigateToInstallTime: () -> Unit,
    onNavigateToOnDemand: () -> Unit,
    modifier: Modifier = Modifier,
) {
    ContentGreen(
        title = "Regular Module screen",
        modifier = modifier,
    ) {
        Column {
            Button(onClick = onNavigateToInstallTime) {
                Text(text = "Go to Install Time Module Screen")
            }
            Button(onClick = onNavigateToOnDemand) {
                Text(text = "Go to On Demand Module Screen")
            }
        }
    }
}

@Serializable
private data object RegularModule : NavKey

@Serializable
data object InstallTimeModule : NavKey {
    const val CLASS_NAME =
        "com.example.dynamicfeature.installtime.DynamicFeatureInstallTimeContentProvider"
    const val MODULE_NAME = "installtime"
}

@Serializable
data object OnDemandModule : NavKey {
    const val CLASS_NAME =
        "com.example.dynamicfeature.ondemand.DynamicFeatureOnDemandContentProvider"
    const val MODULE_NAME = "ondemand"
}

DynamicFeatureActivity.kt
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
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.BasicAlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.retain.retain
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.google.android.play.core.ktx.bytesDownloaded
import com.google.android.play.core.ktx.sessionId
import com.google.android.play.core.ktx.status
import com.google.android.play.core.ktx.totalBytesToDownload
import com.google.android.play.core.splitinstall.SplitInstallManagerFactory
import com.google.android.play.core.splitinstall.SplitInstallRequest
import com.google.android.play.core.splitinstall.SplitInstallStateUpdatedListener
import com.google.android.play.core.splitinstall.model.SplitInstallSessionStatus
import kotlin.math.roundToInt

@Composable
fun retainDynamicFeatureManager(): DynamicFeatureManager {
    val applicationContext = LocalContext.current.applicationContext

    return retain {
        DynamicFeatureManager(applicationContext)
    }
}

class DynamicFeatureManager(context: Context) {
    private val splitInstallManager = SplitInstallManagerFactory.create(context)
    private var listener: SplitInstallStateUpdatedListener? = null

    var sessionId by mutableStateOf<Int?>(null)
        private set

    var downloadState by mutableStateOf<DownloadState?>(null)
        private set

    fun installModule(moduleName: String, onModuleInstalled: () -> Unit) {
        if (splitInstallManager.installedModules.contains(moduleName)) {
            onModuleInstalled()
            return
        }

        listener = SplitInstallStateUpdatedListener { state ->
            if (state.sessionId == sessionId) {
                when (state.status) {
                    SplitInstallSessionStatus.DOWNLOADING -> {
                        downloadState = DownloadState(
                            bytesDownloaded = state.bytesDownloaded,
                            totalBytesToDownload = state.totalBytesToDownload,
                        )
                    }

                    SplitInstallSessionStatus.INSTALLED -> {
                        downloadState = null
                        sessionId = null
                        unregisterListener()
                        onModuleInstalled()
                    }

                    SplitInstallSessionStatus.FAILED, SplitInstallSessionStatus.CANCELED -> {
                        downloadState = null
                        sessionId = null
                        unregisterListener()
                    }

                    else -> {}
                }
            }
        }.also(splitInstallManager::registerListener)

        splitInstallManager.startInstall(
            SplitInstallRequest.newBuilder().addModule(moduleName).build()
        ).addOnSuccessListener {
            sessionId = it
        }
    }

    fun cancelInstallModule() {
        sessionId?.let {
            splitInstallManager.cancelInstall(it).addOnSuccessListener {
                downloadState = null
                sessionId = null
                unregisterListener()
            }
        }
    }

    private fun unregisterListener() {
        listener?.let(splitInstallManager::unregisterListener)
    }

    data class DownloadState(
        val bytesDownloaded: Long,
        val totalBytesToDownload: Long,
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DynamicFeatureDownloadProgressDialog(
    manager: DynamicFeatureManager,
    modifier: Modifier = Modifier,
) {
    val sessionId = manager.sessionId
    val state = manager.downloadState
    val progress = if (state != null) {
        state.bytesDownloaded.toFloat() / state.totalBytesToDownload
    } else {
        0f
    }
    val progressPercentage = "${(progress * 100).roundToInt()}%"

    if (sessionId != null) {
        BasicAlertDialog(
            onDismissRequest = {},
            modifier = modifier,
        ) {
            Surface(shape = MaterialTheme.shapes.large) {
                Column(
                    verticalArrangement = Arrangement.spacedBy(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    modifier = Modifier.padding(16.dp),
                ) {
                    Text(
                        text = "Downloading module...",
                        style = MaterialTheme.typography.titleMedium,
                    )
                    Box(contentAlignment = Alignment.Center) {
                        CircularProgressIndicator(progress = { progress })
                        Text(
                            text = progressPercentage,
                            style = MaterialTheme.typography.labelSmall,
                        )
                    }
                    Button(onClick = manager::cancelInstallModule) {
                        Text(text = "Cancel")
                    }
                }
            }
        }
    }
}

DynamicFeatureManager.kt
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

import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.navigation3.runtime.EntryProviderScope
import androidx.navigation3.runtime.NavKey

fun interface DynamicFeatureContentProvider<T : NavKey> {
    @Composable
    fun Content(key: T)
}

inline fun <reified K : NavKey> EntryProviderScope<NavKey>.dynamicFeatureEntry(
    clazzName: String,
    noinline clazzContentKey: (key: @JvmSuppressWildcards K) -> Any = { it.toString() },
    metadata: Map<String, Any> = emptyMap(),
) {
    entry<K>(
        clazzContentKey = clazzContentKey,
        metadata = metadata,
    ) { key ->
        val provider = remember {
            @Suppress("UNCHECKED_CAST")
            Class.forName(clazzName)
                .getConstructor()
                .newInstance() as DynamicFeatureContentProvider<K>
        }

        provider.Content(key)
    }
}

DynamicFeatureContentProvider.kt
```