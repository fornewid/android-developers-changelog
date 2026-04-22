---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-transform
url: https://developer.android.com/topic/libraries/architecture/paging/v3-transform
source: md.txt
---

When you [work with paged
data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data), you often need to
transform the data stream as you load it. For example, you might need to filter
a list of items, or convert items to a different type before you present them in
the UI. Another common use case for data stream transformation is [adding list
separators](https://developer.android.com/topic/libraries/architecture/paging/v3-transform#separators).

More generally, applying transformations directly to the data stream allows you
to keep your repository constructs and UI constructs separate.

This page assumes that you are familiar with [basic use of the Paging
library](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data).

## Apply basic transformations

Because [`PagingData`](https://developer.android.com/reference/kotlin/androidx/paging/PagingData) is
encapsulated in a reactive stream, you can apply transform operations on the
data incrementally between loading the data and presenting it.

In order to apply transformations to each `PagingData` object in the stream,
place the transformations inside a
[`map()`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/map.html)
operation on the stream:

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  // Map the outer stream so that the transformations are applied to
  // each new generation of PagingData.
  .map { pagingData ->
    // Transformations in this block are applied to the items
    // in the paged data.
}
```

### Convert data

The most basic operation on a stream of data is converting it to a different
type. Once you have access to the `PagingData` object, you can perform a `map()`
operation on each individual item in the paged list within the `PagingData`
object.

One common use case for this is to map a network or database layer object onto
an object specifically used in the UI layer. The example below demonstrates how
to apply this type of map operation:

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.map { user -> UiModel(user) }
  }
```

Another common data conversion is taking an input from the user, such as a query
string, and converting it to the request output to display. Setting this up
requires listening for and capturing the user's query input, performing the
request, and pushing the query result back to the UI.

You can listen for the query input using a stream API. Keep the stream reference
in your `ViewModel`. The UI layer should not have direct access to it; instead,
define a function to notify the ViewModel of the user's query.

```kotlin
private val queryFlow = MutableStateFlow("")

fun onQueryChanged(query: String) {
  queryFlow.value = query
}
```

When the query value changes in the data stream, you can perform operations to
convert the query value to the desired data type and return the result to the UI
layer. The specific conversion function depends on the language and framework
used, but they all provide similar functionality.

```kotlin
val querySearchResults: Flow<User> = queryFlow.flatMapLatest { query ->
  // The database query returns a Flow which is output through
  // querySearchResults
  userDatabase.searchBy(query)
}
```

Using operations like `flatMapLatest` or `switchMap` ensures that only the
latest results are returned to the UI. If the user changes their query input
before the database operation completes, these operations discard the results
from the old query and launch the new search immediately.

### Filter data

Another common operation is filtering. You can filter data based on criteria
from the user, or you can remove data from the UI if it should be hidden based
on other criteria.

You need to place these filter operations inside the `map()` call because the
filter applies to the `PagingData` object. Once the data is filtered out of the
`PagingData`, the new `PagingData` instance is passed to the UI layer to
display.

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.filter { user -> !user.hiddenFromUi }
  }
```

## Add list separators

The Paging library supports dynamic list separators. You can improve list
readability by inserting separators directly into the data stream as
composables in your layout. As a result, separators are fully-featured
composables, enabling full interactivity, styling, and accessibility semantics.

There are three steps involved in inserting separators into your paged list:

1. Convert the UI model to accommodate the separator items. One way to do this is to wrap your data item and separator into a single sealed class. This lets the UI handle multiple item types in the same list.
2. Transform the data stream to dynamically add the separators between loading the data and presenting the data.
3. Update the UI to handle separator items.

> [!NOTE]
> **Note:** For visual dividers that don't require custom data or logic, you can use the `HorizontalDivider` composable directly inside your item layouts or as a standalone element in the list.

### Convert the UI model

The Paging library inserts list separators into the UI as actual
list items, but the separator items must be distinguishable from the data items
in the list to make sure both composable types are rendered distinctly.
The solution is to create a [Kotlin sealed
class](https://kotlinlang.org/docs/reference/sealed-classes.html)
with subclasses to represent your data and your separators. Alternatively, you
can create a base class that is extended by your list item class and your
separator class.

Suppose that you want to add separators to a paged list of `User` items. The
following snippet shows how to create a base class where the instances can be
either a `UserModel` or a `SeparatorModel`:

```kotlin
sealed class UiModel {
  class UserModel(val id: String, val label: String) : UiModel() {
    constructor(user: User) : this(user.id, user.label)
  }

  class SeparatorModel(val description: String) : UiModel()
}
```

### Transform the data stream

You must apply transformations to the data stream after loading it and before
you present it. The transformations should do the following:

- Convert the loaded list items to reflect the new base item type.
- Use the `PagingData.insertSeparators()` method to add the separators.

To learn more about transformation operations, see [Apply basic
transformations](https://developer.android.com/topic/libraries/architecture/paging/v3-transform#basic-transformations).

The following example shows transformation operations to update the
`PagingData<User>` stream to a `PagingData<UiModel>` stream with separators
added:

```kotlin
pager.flow.map { pagingData: PagingData<User> ->
  // Map outer stream, so you can perform transformations on
  // each paging generation.
  pagingData
  .map { user ->
    // Convert items in stream to UiModel.UserModel.
    UiModel.UserModel(user)
  }
  .insertSeparators<UiModel.UserModel, UiModel> { before, after ->
    when {
      before == null -> UiModel.SeparatorModel("HEADER")
      after == null -> UiModel.SeparatorModel("FOOTER")
      shouldSeparate(before, after) -> UiModel.SeparatorModel(
        "BETWEEN ITEMS $before AND $after"
      )
      // Return null to avoid adding a separator between two items.
      else -> null
    }
  }
}
```

### Handle separators in the UI

The final step is to change your UI to accommodate the separator item type.
In a lazy layout, you can handle multiple item types by checking the type of
each emitted `UiModel`. When iterating through your paged data, use a `when`
statement to call the appropriate composable. This lets you provide a distinct
UI for data items and separators.

```kotlin
@Composable fun UserList(pagingItems: LazyPagingItems) {
  LazyColumn {
    items(
      count = pagingItems.itemCount,
      key = { index ->
        val item = pagingItems.peek(index)
        when (item) {
          is UiModel.UserModel -> item.user.id
          is UiModel.SeparatorModel -> item.description
          else -> index
        }
      }
    ) { index ->
      when (val item = pagingItems[index]) {
        is UiModel.UserModel -> UserItemComposable(item.user)
        is UiModel.SeparatorModel -> SeparatorComposable(item.description)
        null -> PlaceholderComposable()
      }
    }
  }
}
```

## Avoid duplicate work

One key issue to avoid is having the app do unnecessary work. Fetching data is
an expensive operation, and data transformations can also take up valuable time.
Once the data is loaded and prepared for display in the UI, it should be saved
in case a configuration change occurs and the UI needs to be recreated.

The `cachedIn()` operation caches the results of any transformations that occur
before it. Typically, you apply this operator in your `ViewModel` before
exposing the `Flow` to your composables.

To manage the cache correctly, pass a `CoroutineScope` to `cachedIn()`, as shown
in the following example using `viewModelScope`.

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.filter { user -> !user.hiddenFromUi }
      .map { user -> UiModel.UserModel(user) }
  }
  .cachedIn(viewModelScope)
```

For more information on using `cachedIn()` with a stream of `PagingData`, see
[Set up a stream of
PagingData](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#pagingdata-stream).

> [!NOTE]
> **Note:** By default you can only use each instance of `PagingData` once. To get around this limitation, consider using the `cachedIn()` operator, which multicasts the stream as part of caching the results. This allows subsequent collections on `Pager.flow` to recollect on the cached `PagingData`. This is especially useful when you work with operators that reuse the most recently emitted `PagingData`, such as Flow's `.combine()` operator.

## Additional resources

To learn more about the Paging library, see the following additional resources:

### Documentation

- [AndroidX Paging Library](https://developer.android.com/jetpack/androidx/releases/paging)

### Views content

- [Transform data streams (Views)](https://developer.android.com/topic/libraries/architecture/views/paging/v3-transform-views)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Test your Paging implementation](https://developer.android.com/topic/libraries/architecture/paging/test)
- [Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state)