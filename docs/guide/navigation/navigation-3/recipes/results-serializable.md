---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/results-serializable
url: https://developer.android.com/guide/navigation/navigation-3/recipes/results-serializable
source: md.txt
---

# Returning a Result (Serializable State-Based)

This recipe demonstrates how to return a result from one screen to a previous screen using a state-based approach that survives configuration changes and process death by leveraging Kotlin Serialization and `rememberSerializable`.

## How it works

This example builds on top of `ResultEventBus` and introduces a custom extension function `conflateAsSerializableState`.

1. **ResultEventBusNavEntryDecorator** : A `NavEntryDecorator` that provides a `ResultEventBus` via `LocalResultEventBus`.
2. **`ResultEventBus`** : A `ResultEventBus` is created and made available to the composables via `LocalResultEventBus`. This EventBus sends and receives the results.
3. **`conflateAsSerializableState`** : A custom extension function on `ResultEventBus` that uses `rememberSerializable` to create a state container, and `ResultEffect` to listen for new results and persist them.
4. **Sending the result** : The screen that produces the result calls `resultBus.sendResult(person)` to send the data back.
5. **Observing the result** : The screen that needs the result calls `LocalResultEventBus.current.conflateAsSerializableState<Person?>(null)` to get a `State` object. The UI observes this state and recomposes whenever the result changes.

This approach is suitable when the result needs to survive configuration changes and process death, whereas the standard `conflateAsState` does not.

### Supporting Nullable Types

The standard `rememberSerializable` function has a generic upper-bound constraint of `T : Any`, which prevents direct preservation of nullable types.

To support nullable types (such as `Person?`), `conflateAsSerializableState` circumvents this restriction by internally wrapping the value in a generic `@Serializable` class, `NullableWrapper`:

    @Serializable
    private data class NullableWrapper<T>(val value: T)

### Serialization of Custom Types

Because this approach uses `rememberSerializable` from the `androidx.compose.runtime.saveable` package, any custom class used as a result (like `Person`) must be marked with Kotlin Serialization's `@Serializable` annotation:

    @Serializable
    data class Person(val name: String, val favoriteColor: String)

The `conflateAsSerializableState` extension function automatically retrieves the appropriate `KSerializer` via the `serializer<T>()` helper when using the reified version:

    @Composable
    inline fun <reified T> ResultEventBus.conflateAsSerializableState(
        defaultValue: T,
        vararg inputs: Any?,
        configuration: SavedStateConfiguration = SavedStateConfiguration.DEFAULT,
    ): State<T>

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/results/serializable)

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.common

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

class HomeViewModel : ViewModel() {
    var person by mutableStateOf<Person?>(null)
}
```

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.common

import androidx.navigation3.runtime.NavKey
import kotlinx.serialization.Serializable

@Serializable
data object Home : NavKey

@Serializable
class PersonDetailsForm : NavKey
```

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.common

import kotlinx.serialization.Serializable

@Serializable
data class Person(val name: String, val favoriteColor: String)
```

```
/*
 * Copyright 2025 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.common

import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.text.input.rememberTextFieldState
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.dropUnlessResumed
import com.example.nav3recipes.content.ContentBlue
import com.example.nav3recipes.content.ContentGreen

@Composable
fun HomeScreen(
    person: Person?,
    onNext: () -> Unit
) {
    ContentBlue("Hello ${person?.name ?: "unknown person"}") {

        if (person != null) {
            Text("Your favorite color is ${person.favoriteColor}")
        }

        Spacer(Modifier.height(16.dp))
        Button(onClick = dropUnlessResumed(block = onNext)) {
            Text("Tell us about yourself")
        }
    }
}

@Composable
fun PersonDetailsScreen(
    onSubmit: (Person) -> Unit
) {
    ContentGreen("About you") {

        val nameTextState = rememberTextFieldState()
        OutlinedTextField(
            state = nameTextState,
            label = { Text("Please enter your name") }
        )

        val favoriteColorTextState = rememberTextFieldState()
        OutlinedTextField(
            state = favoriteColorTextState,
            label = { Text("Please enter your favorite color") }
        )

        Button(
            onClick = dropUnlessResumed {
                val person = Person(
                    name = nameTextState.text.toString(),
                    favoriteColor = favoriteColorTextState.text.toString()
                )
                onSubmit(person)
            },
            enabled = nameTextState.text.isNotBlank() &&
                    favoriteColorTextState.text.isNotBlank()
        ) {
            Text("Submit")
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
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.serializable

import androidx.compose.runtime.Composable
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.runtime.saveable.rememberSerializable
import androidx.navigation3.runtime.result.ResultEffect
import androidx.navigation3.runtime.result.ResultEventBus
import androidx.savedstate.serialization.SavedStateConfiguration
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.serializer

@Serializable
private data class NullableWrapper<T>(val value: T)

/**
 * Reusable extension function on [ResultEventBus] to provide a single [State] that preserves
 * its value across configuration changes and process death using [rememberSerializable].
 *
 * @param T The type of the result value.
 * @param resultKey The unique key associated with this result.
 * @param defaultValue The default initial value to be remembered and saved when no previously saved state exists.
 * @param inputs A set of inputs such that, when any of them have changed, the state will reset and re-initialize with [defaultValue].
 * @param stateSerializer A [KSerializer] used to serialize and deserialize the state value.
 * @param configuration Optional [SavedStateConfiguration] to customize how the serialization is
 *   handled, such as specifying a custom format (e.g., JSON).
 * @return A [State] containing the current value of the result, which updates dynamically when new results are received.
 */
@Composable
fun <T> ResultEventBus.conflateAsSerializableState(
    resultKey: String,
    defaultValue: T,
    vararg inputs: Any?,
    stateSerializer: KSerializer<T>,
    configuration: SavedStateConfiguration = SavedStateConfiguration.DEFAULT,
): State<T> {
    val wrapperSerializer =
        remember(stateSerializer) { NullableWrapper.serializer(stateSerializer) }

    val wrapper = rememberSerializable(
        inputs = inputs,
        stateSerializer = wrapperSerializer,
        configuration = configuration,
    ) {
        mutableStateOf(NullableWrapper(defaultValue))
    }

    // ResultEffect's internal LaunchedEffect does not restart when the onResult lambda changes.
    // If inputs change, rememberSerializable recreates the savedState instance. Using
    // rememberUpdatedState ensures that the ongoing collection coroutine inside ResultEffect
    // always writes to the latest savedState instance without needing to cancel and restart.
    // https://issuetracker.google.com/531709234
    val currentWrapper = rememberUpdatedState(wrapper)
    ResultEffect<T>(resultKey = resultKey, resultEventBus = this) { result ->
        currentWrapper.value.value = NullableWrapper(result)
    }

    // Return a custom State wrapper rather than using derivedStateOf. Since unwrapping NullableWrapper
    // is O(1), an anonymous State avoids the snapshot read-tracking overhead and extra allocations
    // of derivedStateOf while maintaining a stable reference for the caller.
    return remember(wrapper) {
        object : State<T> {
            override val value: T
                get() = wrapper.value.value
        }
    }
}

/**
 * Reified version of [conflateAsSerializableState] using the class name as the key.
 *
 * @warning Do not use this overload for generic types (e.g., [List], [Map]) because
 * JVM type erasure will cause key collisions. Instead, use the version with an explicit `resultKey`.
 */
@Composable
inline fun <reified T> ResultEventBus.conflateAsSerializableState(
    defaultValue: T,
    vararg inputs: Any?,
    configuration: SavedStateConfiguration = SavedStateConfiguration.DEFAULT,
): State<T> = conflateAsSerializableState(
    resultKey = T::class.toString(),
    defaultValue = defaultValue,
    inputs = inputs,
    stateSerializer = serializer<T>(),
    configuration = configuration,
)
```

```
/*
 * Copyright 2026 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.nav3recipes.results.serializable

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.ui.Modifier
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.runtime.result.LocalResultEventBus
import androidx.navigation3.runtime.result.rememberResultEventBusNavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.results.common.Home
import com.example.nav3recipes.results.common.HomeScreen
import com.example.nav3recipes.results.common.Person
import com.example.nav3recipes.results.common.PersonDetailsForm
import com.example.nav3recipes.results.common.PersonDetailsScreen
import com.example.nav3recipes.ui.setEdgeToEdgeConfig

class ResultSerializableActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {
            Scaffold { paddingValues ->
                val backStack = rememberNavBackStack(Home)
                NavDisplay(
                    backStack = backStack,
                    modifier = Modifier.padding(paddingValues),
                    onBack = { backStack.removeLastOrNull() },
                    entryDecorators = listOf(
                        rememberSaveableStateHolderNavEntryDecorator(),
                        rememberResultEventBusNavEntryDecorator()
                    ),
                    entryProvider = entryProvider {
                        entry<Home> {
                            val resultState = LocalResultEventBus
                                .current
                                .conflateAsSerializableState<Person?>(null)
                            val person = resultState.value
                            HomeScreen(
                                person = person,
                                onNext = { backStack.add(PersonDetailsForm()) }
                            )
                        }
                        entry<PersonDetailsForm> {
                            val resultBus = LocalResultEventBus.current
                            PersonDetailsScreen(
                                onSubmit = { person ->
                                    resultBus.sendResult(result = person)
                                    backStack.removeLastOrNull()
                                }
                            )
                        }
                    }
                )
            }
        }
    }
}
```