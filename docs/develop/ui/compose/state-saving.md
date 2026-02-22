---
title: https://developer.android.com/develop/ui/compose/state-saving
url: https://developer.android.com/develop/ui/compose/state-saving
source: md.txt
---

Depending on where your state is hoisted to and the logic that is required, you
can use different APIs to store and restore your [UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state). Every app uses a
combination of APIs to best achieve this.

> [!NOTE]
> **Note:** You can see more information on where to hoist your state based on the logic applied in the [Where to hoist state](https://developer.android.com/develop/ui/compose/state-hoisting) documentation.

Any Android app could lose its [UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state) due to activity or process
recreation. This loss of state can occur because of the following events:

- [Configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). The activity is destroyed and recreated unless the configuration change is [handled manually](https://developer.android.com/guide/topics/resources/runtime-changes#HandlingTheChange).
- [System-initiated process death](https://developer.android.com/topic/libraries/architecture/saving-states#ui-dismissal-system). The app is in the background and the device frees up resources (like memory) to be used by other processes.

> [!NOTE]
> **Note:** [System-initiated process death](https://developer.android.com/topic/libraries/architecture/saving-states#ui-dismissal-system) is different from [user-initiated
> process death](https://developer.android.com/topic/libraries/architecture/saving-states#ui-dismissal-user), in which the user explicitly dismisses the activity. In the case of user-initiated process death, the loss of transient state is generally reasonable (for example, losing the animation state or the content of a [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(kotlin.String,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) while filling out a form).

Preserving the state after these events is essential for a positive user
experience. Selecting which state to persist depends on your app's unique user
flows. As a best practice, you should at least preserve user input and
navigation-related state. Examples of this include the scroll position of a
list, the ID of the item the user wants more detail about, the in-progress
selection of user preferences, or input in text fields.

This page summarizes the APIs available to store UI state depending on where
your state is hoisted to and the logic that needs it.

## UI logic

If your state is hoisted in the UI, either in composable functions or plain
state holder classes scoped to the Composition, you can use
[`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)) to retain state across activity and process recreation.

In the following snippet, `rememberSaveable` is used to store a single boolean
UI element state:


```kotlin
@Composable
fun ChatBubble(
    message: Message
) {
    var showDetails by rememberSaveable { mutableStateOf(false) }

    ClickableText(
        text = AnnotatedString(message.content),
        onClick = { showDetails = !showDetails }
    )

    if (showDetails) {
        Text(message.timestamp)
    }
}
```

<br />

<br />

**Figure 1**. Chat message bubble expands and collapses when tapped.

<br />

`showDetails` is a boolean variable that stores if the chat bubble is collapsed
or expanded.

> [!IMPORTANT]
> **Important:** Usually, data stored in saved instance state is transient state that depends on user input or navigation. Examples of this include the scroll position of a list, the ID of the item the user wants more detail about, the in-progress selection of user preferences, or input in text fields.

`rememberSaveable` stores [UI element state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state) in a [`Bundle`](https://developer.android.com/reference/android/os/Bundle) through the
saved instance state mechanism.

It is able to store primitive types to the bundle automatically. If your state
is held in a type that is not primitive, like a data class, you can use
different storing mechanisms, such as using the [`Parcelize`](https://developer.android.com/kotlin/parcelize) annotation,
using Compose APIs like [`listSaver`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#listSaver(kotlin.Function2,kotlin.Function1)) and [`mapSaver`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#mapSaver(kotlin.Function2,kotlin.Function1)), or implementing a
custom saver class extending Compose runtime [`Saver`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/Saver) class. See the [Ways
to store state](https://developer.android.com/develop/ui/compose/state#ways-to-store) documentation to learn more about these methods.

In the following snippet, the [`rememberLazyListState`](https://cs.android.com/androidx/platform/tools/dokka-devsite-plugin/+/master:testData/compose/source/androidx/compose/foundation/lazy/LazyListState.kt;l=49?q=LazyListState) Compose
API stores [`LazyListState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState), which consists of the scroll state of a
[`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) or [`LazyRow`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyRow(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)), using `rememberSaveable`. It uses a
[`LazyListState.Saver`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/src/commonMain/kotlin/androidx/compose/foundation/lazy/LazyListState.kt;l=413?q=LazyListState.kt), which is a custom saver that is able to
store and restore the scroll state. After an activity or process recreation (for
example, after a configuration change like changing device orientation), the
scroll state is preserved.


```kotlin
@Composable
fun rememberLazyListState(
    initialFirstVisibleItemIndex: Int = 0,
    initialFirstVisibleItemScrollOffset: Int = 0
): LazyListState {
    return rememberSaveable(saver = LazyListState.Saver) {
        LazyListState(
            initialFirstVisibleItemIndex, initialFirstVisibleItemScrollOffset
        )
    }
}
```

<br />

### Best practice

`rememberSaveable` uses a [`Bundle`](https://developer.android.com/reference/android/os/Bundle) to store UI state, which is shared by
other APIs that also write to it, like [`onSaveInstanceState()`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) calls in
your activity. However, the size of this `Bundle` is limited, and storing large
objects could lead to [`TransactionTooLarge`](https://developer.android.com/reference/android/os/TransactionTooLargeException) exceptions in runtime. This
can be particularly problematic in single `Activity` apps where the same
`Bundle` is being used across the app.

To avoid this type of crash, *you should not store large complex objects or
lists of objects in the bundle*.

Instead, store the minimum state required, like IDs or keys, and use these to
delegate restoring more complex UI state to other mechanisms, like [persistent
storage](https://developer.android.com/topic/libraries/architecture/saving-states#local).

> [!NOTE]
> **Note:** In some cases, it might be acceptable not to store all UI elements' state.

These design choices depend on the specific use cases for your app and how your
users expect it to behave.

### Verify state restoration

You can verify that the state stored with [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)) in your
Compose elements is correctly restored when the activity or process is
recreated. There are specific APIs to achieve this, such as
[`StateRestorationTester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/StateRestorationTester). Check out the [Testing](https://developer.android.com/develop/ui/compose/testing#verify_state_restoration) documentation to
learn more.

## Business logic

If your [UI element state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state) is hoisted to the `ViewModel` because it is
required by business logic, you can use `ViewModel`'s APIs.

One of the main benefits of using a `ViewModel` in your Android application is
that it handles configuration changes for free. When there is a configuration
change, and the activity is destroyed and recreated, the UI state hoisted to the
`ViewModel` is kept in memory. After the recreation, the old `ViewModel`
instance is attached to the new activity instance.

> [!NOTE]
> **Note:** The `ViewModel`, as the implementation of a screen level state holder, handles the business logic used to produce [screen UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state). You should hoist the UI state to the `ViewModel`, not because it will handle configuration changes for free, but because it makes sense for your architecture.

However, a `ViewModel` instance does not survive system-initiated process death.
To have the UI state survive this, use the [Saved State module for
ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-compose-state), which contains the [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) API.

### Best practice

[`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) also uses the `Bundle` mechanism to store UI state, so
you should only use it to store simple [UI element state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state).

[Screen UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state), which is produced by applying business rules and accessing
layers of your application other than UI, should not be stored in
`SavedStateHandle` due to its potential complexity and size. You can use
different mechanisms to store complex or large data, like [local persistent
storage](https://developer.android.com/topic/libraries/architecture/saving-states#local). After a process recreation, the screen is recreated with the
restored transient state that was stored in `SavedStateHandle` (if any), and the
screen UI state is produced again from the data layer.

> [!NOTE]
> **Note:** For more information on the different ways of saving UI state, see the [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states) documentation.

### `SavedStateHandle` APIs

[`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle) has different APIs to store UI element state, most
notably:

| Compose [`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State) | [`saveable()`](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/compose/package-summary#(androidx.lifecycle.SavedStateHandle).saveable(kotlin.String,androidx.compose.runtime.saveable.Saver,kotlin.Function0)) |
| [`StateFlow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/) | [`getStateFlow()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getStateFlow(kotlin.String,kotlin.Any)) |
|---|---|

#### Compose `State`

Use the `saveable` API of `SavedStateHandle` to read and write UI element
state as `MutableState`, so it survives activity and process recreation with
minimal code setup.

The `saveable` API supports primitive types out of the box and receives a
`stateSaver` parameter to use custom savers, just like `rememberSaveable()`.

In the following snippet, `message` stores the user input types into a
`TextField`:


```kotlin
class ConversationViewModel(
    savedStateHandle: SavedStateHandle
) : ViewModel() {

    var message by savedStateHandle.saveable(stateSaver = TextFieldValue.Saver) {
        mutableStateOf(TextFieldValue(""))
    }
        private set

    fun update(newMessage: TextFieldValue) {
        message = newMessage
    }

    /*...*/
}

val viewModel = ConversationViewModel(SavedStateHandle())

@Composable
fun UserInput(/*...*/) {
    TextField(
        value = viewModel.message,
        onValueChange = { viewModel.update(it) }
    )
}
```

<br />

See the [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-compose-state) documentation for more information on
using the `saveable` API.

> [!CAUTION]
> **Caution:** The [saveable](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-compose-state) API is experimental.

#### `StateFlow`

Use [`getStateFlow()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getStateFlow(kotlin.String,kotlin.Any)) to store UI element state and consume it as a flow
from the [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle). The [`StateFlow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/) is read
only, and the API requires you to specify a key so you can replace the flow to
emit a new value. With the key you configured, you can retrieve the `StateFlow`
and collect the latest value.

In the following snippet, `savedFilterType` is a `StateFlow` variable that
stores a filter type applied to a list of chat channels in a chat app:


```kotlin
private const val CHANNEL_FILTER_SAVED_STATE_KEY = "ChannelFilterKey"

class ChannelViewModel(
    channelsRepository: ChannelsRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val savedFilterType: StateFlow<ChannelsFilterType> = savedStateHandle.getStateFlow(
        key = CHANNEL_FILTER_SAVED_STATE_KEY, initialValue = ChannelsFilterType.ALL_CHANNELS
    )

    private val filteredChannels: Flow<List<Channel>> =
        combine(channelsRepository.getAll(), savedFilterType) { channels, type ->
            filter(channels, type)
        }.onStart { emit(emptyList()) }

    fun setFiltering(requestType: ChannelsFilterType) {
        savedStateHandle[CHANNEL_FILTER_SAVED_STATE_KEY] = requestType
    }

    /*...*/
}

enum class ChannelsFilterType {
    ALL_CHANNELS, RECENT_CHANNELS, ARCHIVED_CHANNELS
}
```

<br />

Every time the user selects a new filter type, `setFiltering` is called. This
saves a new value in `SavedStateHandle` stored with the key
`_CHANNEL_FILTER_SAVED_STATE_KEY_`. `savedFilterType` is a flow emitting the
latest value stored to the key. `filteredChannels` is subscribed to the flow to
perform the channel filtering.

See the [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-stateflow) documentation for more information on the
`getStateFlow()` API.

### Summary

The following table summarizes the APIs covered in this section, and when to use
each to save UI state:

| Event | UI logic | Business logic in a `ViewModel` |
|---|---|---|
| Configuration changes | `rememberSaveable` | Automatic |
| System-initiated process death | `rememberSaveable` | `SavedStateHandle` |

The API to use depends on where the state is held and the logic that it
requires. For state that is used in [UI logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#logic), use `rememberSaveable`. For
state that is used in [business logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#logic), if you hold it in a `ViewModel`,
save it using `SavedStateHandle`.

You should use the bundle APIs (`rememberSaveable` and `SavedStateHandle`) to
store small amounts of UI state. This data is the minimum necessary to restore
the UI back to its previous state, together with other storing mechanisms. For
example, if you store the ID of a profile the user was looking at in the bundle,
you can fetch heavy data, like profile details, from the data layer.

For more information on the different ways of saving UI state, see the general
[Saving UI State documentation](https://developer.android.com/topic/libraries/architecture/saving-states) and the [data layer](https://developer.android.com/topic/architecture/data-layer) page of the
architecture guide.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Where to hoist state](https://developer.android.com/develop/ui/compose/state-hoisting)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Lists and grids](https://developer.android.com/develop/ui/compose/lists)