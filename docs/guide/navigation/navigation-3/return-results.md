---
title: Return results  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/return-results
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Return results Stay organized with collections Save and categorize content based on your preferences.





Starting in Navigation 3 [1.2.0](/jetpack/androidx/releases/navigation3#navigation3_version_12_2), you can return
results from destinations using the [`ResultEventBus`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEventBus)
API.

`ResultEventBus` provides two communication models:

* **Event-based results**: For transient, one-time events (such as showing a
  confirmation snackbar or triggering a side effect) using
  [`ResultEffect`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEffect.composable).
* **State-based results**: For observing the latest result as Compose `State`
  using [`conflateAsState`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEventBus#conflateAsState(kotlin.Any)).

**Caution:** `ResultEventBus` is an in-memory communication bus. Results aren't
saved across process death or activity recreation automatically. If a result
must survive process death, persist the value using
[`rememberSaveable`](/reference/kotlin/androidx/compose/runtime/saveable/rememberSaveable.composable), a `SavedStateHandle` inside a
scoped `ViewModel`, or by embedding the data in a [`NavKey`](/reference/kotlin/androidx/navigation3/runtime/NavKey). For
one implementation, see the [Serializable result recipe](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/results/serializable).

## Set up the result event bus

To make `ResultEventBus` available to your composable destinations, add the
[`rememberResultEventBusNavEntryDecorator`](/reference/kotlin/androidx/navigation3/runtime/result/rememberResultEventBusNavEntryDecorator.composable) to the list
of decorators passed to your [`NavDisplay`](/reference/kotlin/androidx/navigation3/ui/NavDisplay.composable). This provides each
destination's content with a [`LocalResultEventBus`](/reference/kotlin/androidx/navigation3/runtime/result/LocalResultEventBus)
composition local.

```
NavDisplay(
    /* ... */
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        rememberResultEventBusNavEntryDecorator()
    )
)

ResultSnippets.kt
```

## Result keys

`ResultEventBus` identifies and routes each result using a key. Senders and
receivers match results by using the same key.

You can specify result keys in two ways:

* **Explicit keys**: You can specify an explicit key (such as
  `resultKey = "pickup_address"`). Use explicit keys when returning common
  types (such as `String`, `Boolean`, or primitives), or when multiple
  destinations return different instances of the same data type.
* **Type-derived keys**: When you don't specify an explicit key,
  `ResultEventBus` automatically generates a key using the `toString`
  representation of the result type's `KClass` (such as
  `Contact::class.toString()`). Use type-derived keys for distinct,
  domain-specific data types.

**Caution:** Type-derived keys don't receive events sent with explicit keys, even if
the payload data type is the same. For example, an observer listening by type
(`ResultEffect<Address>`) won't receive `Address` results sent with an explicit
key (`resultKey = "pickup_address"`). Senders and receivers must both use
explicit keys or both use type-derived keys.

## Return results from a destination

To keep screen composables reusable and testable, don't access
`LocalResultEventBus` directly inside your screen UI. Instead, expose callback
lambdas from your screen. In your `entryProvider`, handle the callback by
sending the result using
[`LocalResultEventBus.current`](/reference/kotlin/androidx/navigation3/runtime/result/LocalResultEventBus) and navigating back.

You can send results using an explicit [result key](#result-keys):

```
import androidx.compose.runtime.Composable
import androidx.navigation3.runtime.result.LocalResultEventBus

entry<AddressPickerRoute> {
    val resultBus = LocalResultEventBus.current

    AddressPickerScreen(
        onAddressSelected = { selectedAddress: Address ->
            resultBus.sendResult(
                resultKey = "pickup_address",
                result = selectedAddress
            )
            navigator.goBack()
        }
    )
}

ResultSnippets.kt
```

You can also send results using a type-derived key:

```
import androidx.compose.runtime.Composable
import androidx.navigation3.runtime.result.LocalResultEventBus

entry<ContactPickerRoute> {
    val resultBus = LocalResultEventBus.current

    ContactPickerScreen(
        onContactSelected = { selectedContact: Contact ->
            resultBus.sendResult(result = selectedContact)
            navigator.goBack()
        }
    )
}

ResultSnippets.kt
```

## Receive results

Destinations can consume results using either event-based effects or
state-based observables.

| API | Behavior | Recommended use cases |
| --- | --- | --- |
| [`ResultEffect`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEffect.composable) | **Queued**: Processes all results emitted for the key in order. | One-time events and side effects (such as displaying a snackbar or forwarding to a `ViewModel`). |
| [`conflateAsState`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEventBus#conflateAsState(kotlin.Any)) | **Conflated**: Drops intermediate results and retains only the latest result as Compose `State`. | Lightweight UI state modifiers (such as active filter tags or selection overrides). |

### Handle one-time events with `ResultEffect`

Use [`ResultEffect`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEffect.composable) when handling one-time events such as
triggering analytics, displaying a snackbar, or forwarding a result to a
`ViewModel`.

`ResultEffect` maintains a queue for incoming results. If multiple results are
sent for a given key, `ResultEffect` processes each result in the order it was
sent. Additionally, `ResultEffect` runs in a coroutine scope, which lets you
call suspending functions directly inside the effect body.

You can listen for results associated with an explicit
[result key](#result-keys):

```
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation3.runtime.result.ResultEffect

@Composable
fun RideSummaryScreen(
    onOpenAddressPicker: (key: String) -> Unit,
    viewModel: RideSummaryViewModel = viewModel()
) {
    ResultEffect<Address>(resultKey = "pickup_address") { address ->
        viewModel.onPickupAddressSelected(address)
    }

    ResultEffect<Address>(resultKey = "destination_address") { address ->
        viewModel.onDestinationAddressSelected(address)
    }

    RideSummaryContent(
        pickupAddress = viewModel.pickupAddress,
        destinationAddress = viewModel.destinationAddress,
        onPickPickup = { onOpenAddressPicker("pickup_address") },
        onPickDestination = { onOpenAddressPicker("destination_address") }
    )
}

ResultSnippets.kt
```

You can also listen for results using a type-derived key:

```
import androidx.compose.material3.SnackbarHostState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation3.runtime.result.ResultEffect

@Composable
fun ComposeMessageScreen(
    onPickContact: () -> Unit,
    snackbarHostState: SnackbarHostState = remember { SnackbarHostState() },
    viewModel: ComposeMessageViewModel = viewModel()
) {
    ResultEffect<Contact> { contact ->
        // Suspending calls are supported directly in the effect body
        snackbarHostState.showSnackbar("Selected ${contact.name}")
        viewModel.onRecipientSelected(contact)
    }

    ComposeMessageContent(
        recipient = viewModel.recipient,
        onPickContact = onPickContact
    )
}

ResultSnippets.kt
```

When navigating between destinations, `ResultEffect` executes through the
following lifecycle sequence:

1. **Sender emits**: The sender destination sends a result using
   `resultBus.sendResult(resultKey = "pickup_address", address)` and pops the
   back stack.
2. **Receiver enters composition**: The receiver destination becomes the
   active screen, and `ResultEffect` starts listening for results.
3. **Receiver processes results**: `ResultEffect` receives and executes its
   effect body for each result sent for that key, processing all emissions in
   the order they were sent.
4. **Receiver leaves composition**: When the receiver destination is popped
   from the back stack, `ResultEffect` leaves composition and stops listening
   for results.

### Observe latest results as state with `conflateAsState`

When you only need the latest result value to directly modify or filter local UI
state and want Compose to automatically recompose whenever the result updates,
call [`conflateAsState`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEventBus#conflateAsState(kotlin.Any)) on `ResultEventBus`.

**Tip:** Use `conflateAsState` for lightweight, optional UI modifiers, such as a
selected filter or tag. For primary screen data backed by repositories, use
`ResultEffect` to update a `ViewModel`.

You can observe results associated with an explicit
[result key](#result-keys):

```
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.graphics.Color
import androidx.navigation3.runtime.result.LocalResultEventBus

@Composable
fun ThemePreviewScreen(
    onOpenColorPicker: (key: String) -> Unit
) {
    val resultBus = LocalResultEventBus.current

    val primaryColor by resultBus.conflateAsState<Color>(
        resultKey = "primary_color",
        defaultValue = MaterialTheme.colorScheme.primary
    )

    val accentColor by resultBus.conflateAsState<Color>(
        resultKey = "accent_color",
        defaultValue = MaterialTheme.colorScheme.tertiary
    )

    ThemePreviewContent(
        primaryColor = primaryColor,
        accentColor = accentColor,
        onPickPrimary = { onOpenColorPicker("primary_color") },
        onPickAccent = { onOpenColorPicker("accent_color") }
    )
}

ResultSnippets.kt
```

You can also observe results using a type-derived key:

```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.navigation3.runtime.result.LocalResultEventBus

@Composable
fun FilterableProductListScreen(
    initialFilter: ProductFilter = ProductFilter.All,
    onOpenFilterPicker: () -> Unit
) {
    val resultBus = LocalResultEventBus.current

    // Observe latest filter result as Compose State, starting with initialFilter
    val activeFilter by resultBus.conflateAsState<ProductFilter>(
        defaultValue = initialFilter
    )

    ProductListContent(
        activeFilter = activeFilter,
        onOpenFilterPicker = onOpenFilterPicker
    )
}

ResultSnippets.kt
```

## Hoist `ResultEventBus`

By default, `rememberResultEventBusNavEntryDecorator` creates and remembers
its own `ResultEventBus` internally using
[`rememberResultEventBus`](/reference/kotlin/androidx/navigation3/runtime/result/rememberResultEventBus.composable).

You can explicitly create and hoist a `ResultEventBus` when you need to:

* Pass the `ResultEventBus` instance directly into non-composable components
  or dependency injection graphs.
* Send or observe results from top-level app scaffolding (such as an app bar
  or navigation drawer) outside the destination hierarchy.

To hoist `ResultEventBus`, create it using `rememberResultEventBus` and pass
it to `rememberResultEventBusNavEntryDecorator(resultEventBus)`:

```
import androidx.compose.runtime.Composable
import androidx.navigation3.runtime.result.rememberResultEventBus
import androidx.navigation3.runtime.result.rememberResultEventBusNavEntryDecorator
import androidx.navigation3.ui.NavDisplay

// Hoist the ResultEventBus at the top level
val resultEventBus = rememberResultEventBus()

// Pass the hoisted bus to the decorator
val resultEventBusNavEntryDecorator =
    rememberResultEventBusNavEntryDecorator<NavKey>(
        resultEventBus = resultEventBus
    )

NavDisplay(
    /* ... */
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        resultEventBusNavEntryDecorator
    )
)

ResultSnippets.kt
```

## Manage and clear results

When a destination consumes a one-time result, clear it from the event bus using
[`removeResult`](/reference/kotlin/androidx/navigation3/runtime/result/ResultEventBus#removeResult()). This prevents the bus from re-delivering
past events to new observers when destinations re-enter composition:

```
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation3.runtime.result.LocalResultEventBus
import androidx.navigation3.runtime.result.ResultEffect

@Composable
fun NotificationSettingsScreen(
    viewModel: NotificationViewModel = viewModel()
) {
    val resultBus = LocalResultEventBus.current

    ResultEffect<ConfirmationResult>(resultKey = "confirm_permission") { confirmation ->
        viewModel.onPermissionConfirmed(confirmation)

        // Clear the result after consumption to prevent re-delivery
        resultBus.removeResult(resultKey = "confirm_permission")
    }
}

ResultSnippets.kt
```

You can clear results by explicit key (`resultBus.removeResult(resultKey)`) or
by type-derived key (`resultBus.removeResult<T>()`). For details on key
matching, see [Result keys](#result-keys).

## Recipes

For complete runnable code examples demonstrating different result-passing
strategies, see the following recipes:

* [Event-based result recipe](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/results/event)
* [State-based result recipe](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/results/state)
* [Serializable result recipe](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/results/serializable)