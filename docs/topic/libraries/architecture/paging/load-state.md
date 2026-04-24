---
title: https://developer.android.com/topic/libraries/architecture/paging/load-state
url: https://developer.android.com/topic/libraries/architecture/paging/load-state
source: md.txt
---

The Paging library tracks the state of load requests for paged data and exposes
it through the [`LoadState`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState) class.

A separate `LoadState` signal is provided for each
[`LoadType`](https://developer.android.com/reference/kotlin/androidx/paging/LoadType) and data source type
(either [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) or
[`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator)). The
[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates)
object provided by the listener provides information about the loading state
from all of these signals. You can use this detailed information to display the
appropriate loading indicators to your users.

## Loading states

The Paging library exposes the loading state for use in the UI through the
`LoadState` object. `LoadState` objects take one of three forms depending on the
current loading state:

- If there is no active load operation and no error, then `LoadState` is a [`LoadState.NotLoading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.NotLoading) object. This subclass also includes the [`endOfPaginationReached`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState#endOfPaginationReached()) property, which indicates whether the end of pagination has been reached.
- If there is an active load operation, then `LoadState` is a [`LoadState.Loading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Loading) object.
- If there is an error, then `LoadState` is a [`LoadState.Error`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Error) object.

Access these states through the [`loadState`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems#loadState()) property of your
[`LazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems) wrapper. You can use this state in two ways: handling
the main content visibility (like a full-screen refresh spinner) or inserting
loading items directly into your `LazyColumn` stream (like a footer spinner).

## Access the loading state with a listener

To monitor the loading state in your UI, use the [`loadState`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems#loadState()) property
provided by the [`LazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems) wrapper. This returns a
[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates) object that lets you react to loading behavior for
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

For more information on `LazyPagingItems`, see [Large data-sets (paging)](https://developer.android.com/develop/ui/compose/lists#large-datasets).

## Add loading headers and footers

To display loading indicators at the beginning or end of your list (acting as
headers or footers), add dedicated item blocks specifically for those states
within your `LazyColumn` scope.

You can monitor the prepend state for the header and the append state for the
footer using the [`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates) object.

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
database ([`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource)) and
your network ([`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator)).
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

## React to load state changes

You might need to trigger one-off side effects based on load state changes,
such as scrolling to the top of a list or showing a `Snackbar` when a refresh
completes.

Use `snapshotFlow` inside a `LaunchedEffect` to observe state changes as a
stream. This lets you apply standard `Flow` operators like [`filter`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/filter.html)
and [`distinctUntilChanged`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/distinct-until-changed.html) to isolate specific events.

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

## Additional resources

For further information about the Paging library and loading states, consult
the following resources.

### Documentation

- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)

### Views content

- [Manage and present loading states (Views)](https://developer.android.com/topic/libraries/architecture/views/paging/load-state-views)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)