---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-migration
url: https://developer.android.com/topic/libraries/architecture/paging/v3-migration
source: md.txt
---

Paging 3 is significantly different from earlier versions of the Paging library.
This version provides enhanced functionality, first-class support for Kotlin
coroutines and `Flow`, and seamless integration with Jetpack Compose.

## Benefits of migrating to Paging 3

Paging 3 includes the following features that were not present in earlier
versions of the library:

- First-class support for Kotlin coroutines and `Flow`.
- Built-in load state and error signals for responsive UI design, including retry and refresh functionality.
- Improvements to the repository layer, including cancellation support and a simplified data source interface.
- Improvements to the presentation layer, list separators, custom page transforms, headers and footers, and loading state items for lazy lists.

## Migrate your app to Paging 3

To fully migrate to Paging 3, you must migrate these major components
from Paging 2:

- `DataSource` classes
- `PagedList`
- Presentation layer (to `LazyPagingItems`)

However, some Paging 3 components are backwards-compatible with previous
versions of Paging. In particular, the `Pager` API can use older
[`DataSource`](https://developer.android.com/reference/kotlin/androidx/paging/DataSource) objects with the `asPagingSourceFactory` method. This means
that you have the following migration options:

- You can migrate your `DataSource` to `PagingSource` but leave the rest of your Paging implementation unchanged.
- You can migrate the entire Paging implementation to fully migrate your app to Paging 3.

The sections on this page explain how to migrate Paging components on each layer
of your app.

### `DataSource` classes

This section describes all of the necessary changes to migrate an older Paging
implementation to use `PagingSource`.

The `PageKeyedDataSource`, `PositionalDataSource`, and `ItemKeyedDataSource`
from Paging 2 are all combined into the `PagingSource` API in Paging 3. The
loading methods from all of the old API classes are combined into a single
`load` method in `PagingSource`. This reduces code duplication because much of
the logic across the loading methods in implementations of the old API classes
is often identical.

All loading method parameters are replaced in Paging 3 with a `LoadParams`
sealed class, which includes subclasses for each load type. If you need to
differentiate among load types in your `load` method, check which
subclass of `LoadParams` was passed in: `LoadParams.Refresh`,
`LoadParams.Prepend`, or `LoadParams.Append`.

To learn more about implementing `PagingSource`, see [Define a data source](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#data-source).

> [!NOTE]
> **Note:** If your current Paging implementation includes custom error handling, consider using the built-in error handling support in `PagingSource` instead. To learn more, see [Handle errors](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#handle-errors).

#### Refresh keys

Implementations of `PagingSource` must define how refreshes resume from the
middle of the loaded paged data. Do this by implementing
[`getRefreshKey`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource#getrefreshkey)
to map the correct initial key using `state.anchorPosition` as the most recently
accessed index.

    // Replaces ItemKeyedDataSource.
    override fun getRefreshKey(state: PagingState<String, User>): String? {
      return state.anchorPosition?.let { anchorPosition ->
        state.getClosestItemToPosition(anchorPosition)?.id
      }
    }

    // Replacing PositionalDataSource.
    override fun getRefreshKey(state: PagingState<Int, User>): Int? {
      return state.anchorPosition
    }

#### List transformations

In lower versions of the Paging library, transformation of the paged data relies
on the following methods:

- `DataSource.map`
- `DataSource.mapByPage`
- `DataSource.Factory.map`
- `DataSource.Factory.mapByPage`

In Paging 3, all transformations are applied as operators on `PagingData`. If
you use any of the methods in the preceding list to transform your paged list,
you must move your transformation logic from the `DataSource` to the
`PagingData` when constructing the `Pager` using your new `PagingSource`.

To learn more about applying transformations to paged data using Paging 3, see
[Transform data streams](https://developer.android.com/topic/libraries/architecture/paging/v3-transform).

### `PagedList`

This section describes all of the necessary changes to migrate an older Paging
implementation to use `Pager` and `PagingData` in Paging 3.

#### `PagedListBuilder` classes

`PagingData` replaces the existing `PagedList` from Paging 2. To migrate to
`PagingData`, you must update the following:

- Paging configuration has moved from `PagedList.Config` to `PagingConfig`.
- Older builder classes have been combined into a single `Pager` class.
- `Pager` exposes an observable `Flow<PagingData>` with its `.flow` property.

    val flow = Pager(
      // Configure how data is loaded by passing additional properties to
      // PagingConfig, such as prefetchDistance.
      PagingConfig(pageSize = 20)
    ) {
      ExamplePagingSource(backend, query)
    }.flow
      .cachedIn(viewModelScope)

To learn more about setting up a reactive stream of `PagingData` objects using
Paging 3, see [Set up a stream of PagingData](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#pagingdata-stream).

#### `BoundaryCallback` for layered sources

In Paging 3, [`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator) replaces `PagedList.BoundaryCallback` as a
handler for paging from network and database.

To learn more about using `RemoteMediator` to page from network and database in
Paging 3, see the [Android Paging codelab](https://codelabs.developers.google.com/codelabs/android-paging).

### `LazyPagingItems`

This section describes all of the necessary changes to migrate an older Paging
implementation to use `LazyPagingItems` from Paging 3.

Paging 3 provides `collectAsLazyPagingItems` to handle the new `PagingData`
flow. To migrate your presentation layer, use the `paging-compose` artifact and
`collectAsLazyPagingItems` to collect `PagingData` items and display them in
`@Composable` functions.

To learn more about `LazyPagingItems`, see [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data).

### List diffing and updates

If you currently use custom list diffing logic, migrate your implementation to
use the `LazyPagingItems` provided in Paging 3 instead. To make sure diffing
happens properly, specify an item key on your lazy list:

    @Composable
    fun UserScreen(viewModel: UserViewModel) {
        // Collects the Flow into a LazyPagingItems object
        val lazyPagingItems = viewModel.pager.flow.collectAsLazyPagingItems()

        UserList(lazyPagingItems)
    }

    @Composable
    fun UserScreen(viewModel: UserViewModel) {
        val lazyPagingItems = viewModel.pager.flow.collectAsLazyPagingItems()

        UserList(lazyPagingItems)
    }

    @Composable
    fun UserList(lazyPagingItems: LazyPagingItems<User>) {
        LazyColumn {
            items(
                count = lazyPagingItems.itemCount,
                // Provide a stable key for each item, similar to DiffUtil in Views
                key = lazyPagingItems.itemKey { user -> user.id } 
            ) { index ->
                val user = lazyPagingItems[index]
                if (user != null) {
                    UserRow(user = user)
                }
            }
        }
    }

For more information on item keys, see [Item keys](https://developer.android.com/develop/ui/compose/lists#item-keys).

### Loading states

In Paging 3, you don't need a separate adapter to display headers or footers for
loading states. The `LazyPagingItems` object exposes a `loadState` property that
you can check directly within your `LazyColumn`.

    LazyColumn {
        // ... items(lazyPagingItems) go here ...

        // Show loading spinner at bottom of list when appending data
        if (lazyPagingItems.loadState.append is LoadState.Loading) {
            item {
                CircularProgressIndicator(modifier = Modifier.fillMaxWidth())
            }
        }
    }

## Additional resources

To learn more about the Paging library, see the following additional resources:

### Documentation

- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)

### Views content

- [Migrate to Paging 3 (Views)](https://developer.android.com/topic/libraries/architecture/views/paging/v3-migration-views)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Gather paged data](https://developer.android.com/topic/libraries/architecture/paging/data)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)