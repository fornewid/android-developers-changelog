---
title: https://developer.android.com/topic/libraries/architecture/paging/load-state
url: https://developer.android.com/topic/libraries/architecture/paging/load-state
source: md.txt
---

The Paging library tracks the state of load requests for paged data and exposes
it through the [`LoadState`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.md.txt) class.

A separate `LoadState` signal is provided for each
[`LoadType`](https://developer.android.com/reference/kotlin/androidx/paging/LoadType.md.txt) and data source type
(either [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.md.txt) or
[`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator.md.txt)). The
[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates.md.txt)
object provided by the listener provides information about the loading state
from all of these signals. You can use this detailed information to display the
appropriate loading indicators to your users.

## Loading states

The Paging library exposes the loading state for use in the UI through the
`LoadState` object. `LoadState` objects take one of three forms depending on the
current loading state:

- If there is no active load operation and no error, then `LoadState` is a [`LoadState.NotLoading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.NotLoading.md.txt) object. This subclass also includes the [`endOfPaginationReached`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.md.txt#endOfPaginationReached()) property, which indicates whether the end of pagination has been reached.
- If there is an active load operation, then `LoadState` is a [`LoadState.Loading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Loading.md.txt) object.
- If there is an error, then `LoadState` is a [`LoadState.Error`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Error.md.txt) object.

Access these states through the [`loadState`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems.md.txt#loadState()) property of your
[`LazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems.md.txt) wrapper. You can use this state in two ways: handling
the main content visibility (like a full-screen refresh spinner) or inserting
loading items directly into your `LazyColumn` stream (like a footer spinner).

## Access the loading state with a listener

To monitor the loading state in your UI, use the [`loadState`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems.md.txt#loadState()) property
provided by the [`LazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems.md.txt) wrapper. This returns a
[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates.md.txt) object that lets you react to loading behavior for
refresh, append, or prepend events.

In the following example, the UI displays a loading spinner or an error message
depending on the current state of the refresh (initial) load:

```kotlin
@Composable
fun UserListScreen(viewModel: UserViewModel) {
  val pagingItems = viewModel.flow.collectAsLazyPagingItems()

  Box(modifier = Modifier.fillMaxSize()) {
    // Show the list content
    LazyColumn {
      items(pagingItems.itemCount) { index ->
        UserItem(pagingItems[index])
      }
    }

    // Handle the loading state
    when (val state = pagingItems.loadState.refresh) {
      is LoadState.Loading -> {
        CircularProgressIndicator(modifier = Modifier.align(Alignment.Center))
      }
      is LoadState.Error -> {
        ErrorButton(
          message = state.error.message ?: "Unknown error",
          onClick = { pagingItems.retry() },
          modifier = Modifier.align(Alignment.Center)
        )
      }
      else -> {} // No separate view needed for success/not loading
    }
  }
}
```

For more information on `LazyPagingItems`, see [Large data-sets (paging)](https://developer.android.com/develop/ui/compose/lists.md.txt#large-datasets).

## Add loading headers and footers

To display loading indicators at the beginning or end of your list (acting as
headers or footers), add dedicated item blocks specifically for those states
within your `LazyColumn` scope.

You can monitor the prepend state for the header and the append state for the
footer using the [`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates.md.txt) object.

In the following example, the list displays a progress bar or a retry button at
the bottom of the list when more data is being fetched:

> [!NOTE]
> **Note:** The following example only works if placeholders are disabled. Otherwise, the load state items will be displayed at the end of placeholders.

```kotlin
@Composable
fun UserList(viewModel: UserViewModel) {
  val pagingItems = viewModel.pager.flow.collectAsLazyPagingItems()

  LazyColumn {
    // 1. Header (Prepend state)
    // Useful if you support bidirectional paging or jumping to the middle
    item {
      val prependState = pagingItems.loadState.prepend
      if (prependState is LoadState.Loading) {
        LoadingItem()
      } else if (prependState is LoadState.Error) {
        ErrorItem(
          message = prependState.error.message ?: "Error",
          onClick = { pagingItems.retry() }
        )
      }
    }

    // 2. Main Data
    items(pagingItems.itemCount) { index ->
      UserItem(pagingItems[index])
    }

    // 3. Footer (Append state)
    // Shows when the user scrolls to the bottom and more data is loading
    item {
      val appendState = pagingItems.loadState.append
      if (appendState is LoadState.Loading) {
        LoadingItem()
      } else if (appendState is LoadState.Error) {
        ErrorItem(
          message = appendState.error.message ?: "Error",
          onClick = { pagingItems.retry() }
        )
      }
    }
  }
}

@Composable
fun LoadingItem() {
  Box(modifier = Modifier.fillMaxWidth().padding(16.dp), contentAlignment = Alignment.Center) {
    CircularProgressIndicator()
  }
}

@Composable
fun ErrorItem(message: String, onClick: () -> Unit) {
  Column(
    modifier = Modifier.fillMaxWidth().padding(16.dp),
    horizontalAlignment = Alignment.CenterHorizontally
  ) {
    Text(text = message, color = Color.Red)
    Button(onClick = onClick) { Text("Retry") }
  }
}
```

## Access additional loading state information

As shown in the earlier examples, calling `pagingItems.loadState.refresh` is
convenient. However, it obscures the difference between loading from your local
database ([`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.md.txt)) and
your network ([`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator.md.txt)).
This can cause the UI to briefly show a loading spinner even when cached data
is immediately available.

For precise control, like showing a loading spinner only when the local database
is empty and a network sync is active, access the `source` and `mediator`
properties directly within your composable.

```kotlin
val loadState = pagingItems.loadState

val isSyncing = loadState.mediator?.refresh is LoadState.Loading

val isLocalEmpty = loadState.source.refresh is LoadState.NotLoading &&
                   pagingItems.itemSnapshotList.items.isEmpty()

if (isSyncing && isLocalEmpty) {
    FullScreenLoading()
} else {
    UserList(pagingItems)

    if (isSyncing) {
        TopOverlaySpinner()
    }
}
```

Because `pagingItems.loadState` emits a new `CombinedLoadStates` object whenever
`prepend` or `append` changes during scrolling, wrap the refresh check in
[`derivedStateOf`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary.md.txt#derivedStateOf(kotlin.Function0)) with `remember(pagingItems)`. This prevents scroll-edge
updates from recomposing a parent scope that only toggles a full-screen refresh
indicator:

```kotlin
val showFullScreenLoading by remember(pagingItems) {
  derivedStateOf {
    // Avoid recomposing on prepend or append updates while scrolling, and
    // avoid covering existing items during a background refresh.
    pagingItems.loadState.source.refresh is LoadState.Loading &&
      pagingItems.itemCount == 0
  }
}

if (showFullScreenLoading) {
  Box(
    modifier = Modifier.fillMaxSize(),
    contentAlignment = Alignment.Center
  ) {
    CircularProgressIndicator()
  }
}
```

## React to load state changes

You might need to trigger one-off side effects based on load state changes,
such as scrolling to the top of a list or showing a `Snackbar` when a refresh
completes or fails.

Use `snapshotFlow` inside a `LaunchedEffect` to observe state changes as a
stream. This lets you apply standard `Flow` operators like [`filter`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/filter.html),
[`distinctUntilChanged`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/distinct-until-changed.html), and [`distinctUntilChangedBy`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/distinct-until-changed-by.html) to isolate
specific events.

```kotlin
val listState = rememberLazyListState()

LaunchedEffect(pagingItems) {
  // 1. Convert the state to a Flow
  snapshotFlow { pagingItems.loadState.refresh }
    // 2. Filter for the specific event (Refresh completed successfully)
    .distinctUntilChanged()
    .filter { it is LoadState.NotLoading }
    .collect {
      // 3. Trigger the side effect
      listState.animateScrollToItem(0)
    }
}
```

Similarly, you can use `distinctUntilChangedBy` on `loadState` to display an
error `Snackbar` only when the `refresh` state transitions to
`LoadState.Error`:

```kotlin
val snackbarHostState = remember { SnackbarHostState() }

// Key on pagingItems rather than loadState so state updates do not restart the
// coroutine and reset distinctUntilChangedBy.
LaunchedEffect(pagingItems) {
  snapshotFlow { pagingItems.loadState }
    // Ignore prepend and append updates so scrolling does not re-trigger the
    // refresh error Snackbar.
    .distinctUntilChangedBy { it.refresh }
    .filter { it.refresh is LoadState.Error }
    .collect { loadState ->
      val error = (loadState.refresh as LoadState.Error).error
      val result = snackbarHostState.showSnackbar(
        message = "Data failed to load: ${error.localizedMessage ?: "Unknown error"}",
        actionLabel = "Retry"
      )
      if (result == SnackbarResult.ActionPerformed) {
        pagingItems.retry()
      }
    }
}
```

## Additional resources

For further information about the Paging library and loading states, consult
the following resources.

### Documentation

- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data.md.txt)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db.md.txt)

### Views content

- [Manage and present loading states (Views)](https://developer.android.com/topic/libraries/architecture/views/paging/load-state-views.md.txt)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview.md.txt)