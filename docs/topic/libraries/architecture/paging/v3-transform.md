---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-transform
url: https://developer.android.com/topic/libraries/architecture/paging/v3-transform
source: md.txt
---

# Transform data streams

When you[work with paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data), you often need to transform the data stream as you load it. For example, you might need to filter a list of items, or convert items to a different type before you present them in the UI. Another common use case for data stream transformation is[adding list separators](https://developer.android.com/topic/libraries/architecture/paging/v3-transform#separators).

More generally, applying transformations directly to the data stream allows you to keep your repository constructs and UI constructs separate.

This page assumes that you are familiar with[basic use of the Paging library](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data).

## Apply basic transformations

Because[`PagingData`](https://developer.android.com/reference/kotlin/androidx/paging/PagingData)is encapsulated in a reactive stream, you can apply transform operations on the data incrementally between loading the data and presenting it.

In order to apply transformations to each`PagingData`object in the stream, place the transformations inside a[`map()`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/map.html)operation on the stream:  

### Kotlin

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  // Map the outer stream so that the transformations are applied to
  // each new generation of PagingData.
  .map { pagingData ->
    // Transformations in this block are applied to the items
    // in the paged data.
}
```

### Java

```java
PagingRx.getFlowable(pager) // Type is Flowable<PagingData<User>>.
  // Map the outer stream so that the transformations are applied to
  // each new generation of PagingData.
  .map(pagingData -> {
    // Transformations in this block are applied to the items
    // in the paged data.
  });
```

### Java

```java
// Map the outer stream so that the transformations are applied to
// each new generation of PagingData.
Transformations.map(
  // Type is LiveData<PagingData<User>>.
  PagingLiveData.getLiveData(pager),
  pagingData -> {
    // Transformations in this block are applied to the items
    // in the paged data.
  });
```

### Convert data

The most basic operation on a stream of data is converting it to a different type. Once you have access to the`PagingData`object, you can perform a`map()`operation on each individual item in the paged list within the`PagingData`object.

One common use case for this is to map a network or database layer object onto an object specifically used in the UI layer. The example below demonstrates how to apply this type of map operation:  

### Kotlin

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.map { user -> UiModel(user) }
  }
```

### Java

```java
// Type is Flowable<PagingData<User>>.
PagingRx.getFlowable(pager)
  .map(pagingData ->
    pagingData.map(UiModel.UserModel::new)
  )
```

### Java

```java
Transformations.map(
  // Type is LiveData<PagingData<User>>.
  PagingLiveData.getLiveData(pager),
  pagingData ->
    pagingData.map(UiModel.UserModel::new)
)
```

Another common data conversion is taking an input from the user, such as a query string, and converting it to the request output to display. Setting this up requires listening for and capturing the user's query input, performing the request, and pushing the query result back to the UI.

You can listen for the query input using a stream API. Keep the stream reference in your`ViewModel`. The UI layer should not have direct access to it; instead, define a function to notify the ViewModel of the user's query.  

### Kotlin

```kotlin
private val queryFlow = MutableStateFlow("")

fun onQueryChanged(query: String) {
  queryFlow.value = query
}
```

### Java

```java
private BehaviorSubject<String> querySubject = BehaviorSubject.create("");

public void onQueryChanged(String query) {
  queryFlow.onNext(query)
}
```

### Java

```java
private MutableLiveData<String> queryLiveData = new MutableLiveData("");

public void onQueryChanged(String query) {
  queryFlow.setValue(query)
}
```

When the query value changes in the data stream, you can perform operations to convert the query value to the desired data type and return the result to the UI layer. The specific conversion function depends on the language and framework used, but they all provide similar functionality.  

### Kotlin

```kotlin
val querySearchResults = queryFlow.flatMapLatest { query ->
  // The database query returns a Flow which is output through
  // querySearchResults
  userDatabase.searchBy(query)
}
```

### Java

```java
Observable<User> querySearchResults =
  querySubject.switchMap(query -> userDatabase.searchBy(query));
```

### Java

```java
LiveData<User> querySearchResults = Transformations.switchMap(
  queryLiveData,
  query -> userDatabase.searchBy(query)
);
```

Using operations like`flatMapLatest`or`switchMap`ensures that only the latest results are returned to the UI. If the user changes their query input before the database operation completes, these operations discard the results from the old query and launch the new search immediately.

### Filter data

Another common operation is filtering. You can filter data based on criteria from the user, or you can remove data from the UI if it should be hidden based on other criteria.

You need to place these filter operations inside the`map()`call because the filter applies to the`PagingData`object. Once the data is filtered out of the`PagingData`, the new`PagingData`instance is passed to the UI layer to display.  

### Kotlin

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.filter { user -> !user.hiddenFromUi }
  }
```

### Java

```java
// Type is Flowable<PagingData<User>>.
PagingRx.getFlowable(pager)
  .map(pagingData ->
    pagingData.filter(user -> !user.isHiddenFromUi())
  )
}
```

### Java

```java
Transformations.map(
  // Type is LiveData<PagingData<User>>.
  PagingLiveData.getLiveData(pager),
  pagingData ->
    pagingData.filter(user -> !user.isHiddenFromUi())
)
```

## Add list separators

The Paging library supports dynamic list separators. You can improve list readability by inserting separators directly into the data stream as`RecyclerView`list items. As a result, separators are fully-featured`ViewHolder`objects, enabling interactivity, accessibility focus, and all of the other features provided by a`View`.

There are three steps involved in inserting separators into your paged list:

1. Convert the UI model to accommodate the separator items.
2. Transform the data stream to dynamically add the separators between loading the data and presenting the data.
3. Update the UI to handle separator items.

| **Note:** If you don't need your list separators to be interactive or implement accessibility focus, it is simpler to use[`RecyclerView.ItemDecoration`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.ItemDecoration)to create static list separators instead.

### Convert the UI model

The Paging library inserts list separators into the`RecyclerView`as actual list items, but the separator items must be distinguishable from the data items in the list to enable them to bind to a different`ViewHolder`type with a distinct UI. The solution is to create a[Kotlin sealed class](https://kotlinlang.org/docs/reference/sealed-classes.html)with subclasses to represent your data and your separators. Alternatively, you can create a base class that is extended by your list item class and your separator class.

Suppose that you want to add separators to a paged list of`User`items. The following snippet shows how to create a base class where the instances can be either a`UserModel`or a`SeparatorModel`:  

### Kotlin

```kotlin
sealed class UiModel {
  class UserModel(val id: String, val label: String) : UiModel() {
    constructor(user: User) : this(user.id, user.label)
  }

  class SeparatorModel(val description: String) : UiModel()
}
```

### Java

```java
class UiModel {
  private UiModel() {}

  static class UserModel extends UiModel {
    @NonNull
    private String mId;
    @NonNull
    private String mLabel;

    UserModel(@NonNull String id, @NonNull String label) {
      mId = id;
      mLabel = label;
    }

    UserModel(@NonNull User user) {
      mId = user.id;
      mLabel = user.label;
    }

    @NonNull
    public String getId() {
      return mId;
    }

    @NonNull
    public String getLabel() {
      return mLabel;
      }
    }

    static class SeparatorModel extends UiModel {
    @NonNull
    private String mDescription;

    SeparatorModel(@NonNull String description) {
      mDescription = description;
    }

    @NonNull
    public String getDescription() {
      return mDescription;
    }
  }
}
```

### Java

```java
class UiModel {
  private UiModel() {}

  static class UserModel extends UiModel {
    @NonNull
    private String mId;
    @NonNull
    private String mLabel;

    UserModel(@NonNull String id, @NonNull String label) {
      mId = id;
      mLabel = label;
    }

    UserModel(@NonNull User user) {
      mId = user.id;
      mLabel = user.label;
    }

    @NonNull
    public String getId() {
      return mId;
    }

    @NonNull
    public String getLabel() {
      return mLabel;
      }
    }

    static class SeparatorModel extends UiModel {
    @NonNull
    private String mDescription;

    SeparatorModel(@NonNull String description) {
      mDescription = description;
    }

    @NonNull
    public String getDescription() {
      return mDescription;
    }
  }
}
```

### Transform the data stream

You must apply transformations to the data stream after loading it and before you present it. The transformations should do the following:

- Convert the loaded list items to reflect the new base item type.
- Use the`PagingData.insertSeparators()`method to add the separators.

To learn more about transformation operations, see[Apply basic transformations](https://developer.android.com/topic/libraries/architecture/paging/v3-transform#basic-transformations).

The following example shows transformation operations to update the`PagingData<User>`stream to a`PagingData<UiModel>`stream with separators added:  

### Kotlin

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

### Java

```java
// Map outer stream, so you can perform transformations on each
// paging generation.
PagingRx.getFlowable(pager).map(pagingData -> {
  // First convert items in stream to UiModel.UserModel.
  PagingData<UiModel> uiModelPagingData = pagingData.map(
    UiModel.UserModel::new);

  // Insert UiModel.SeparatorModel, which produces PagingData of
  // generic type UiModel.
  return PagingData.insertSeparators(uiModelPagingData,
    (@Nullable UiModel before, @Nullable UiModel after) -> {
      if (before == null) {
        return new UiModel.SeparatorModel("HEADER");
      } else if (after == null) {
        return new UiModel.SeparatorModel("FOOTER");
      } else if (shouldSeparate(before, after)) {
        return new UiModel.SeparatorModel("BETWEEN ITEMS "
          + before.toString() + " AND " + after.toString());
      } else {
        // Return null to avoid adding a separator between two
        // items.
        return null;
      }
    });
});
```

### Java

```java
// Map outer stream, so you can perform transformations on each
// paging generation.
Transformations.map(PagingLiveData.getLiveData(pager),
  pagingData -> {
    // First convert items in stream to UiModel.UserModel.
    PagingData<UiModel> uiModelPagingData = pagingData.map(
      UiModel.UserModel::new);

    // Insert UiModel.SeparatorModel, which produces PagingData of
    // generic type UiModel.
    return PagingData.insertSeparators(uiModelPagingData,
      (@Nullable UiModel before, @Nullable UiModel after) -> {
        if (before == null) {
          return new UiModel.SeparatorModel("HEADER");
        } else if (after == null) {
          return new UiModel.SeparatorModel("FOOTER");
        } else if (shouldSeparate(before, after)) {
          return new UiModel.SeparatorModel("BETWEEN ITEMS "
            + before.toString() + " AND " + after.toString());
        } else {
          // Return null to avoid adding a separator between two
          // items.
          return null;
        }
      });
  });
```

### Handle separators in the UI

The final step is to change your UI to accommodate the separator item type. Create a layout and a view holder for your separator items and change the list adapter to use`RecyclerView.ViewHolder`as its view holder type so that it can handle more than one type of view holder. Alternatively, you can define a common base class that both your item and separator view holder classes extend.

You must also make the following changes to your list adapter:

- Add cases to the`onCreateViewHolder()`and`onBindViewHolder()`methods to account for separator list items.
- Implement a new comparator.

### Kotlin

```kotlin
class UiModelAdapter :
  PagingDataAdapter<UiModel, RecyclerView.ViewHolder>(UiModelComparator) {

  override fun onCreateViewHolder(
    parent: ViewGroup,
    viewType: Int
  ) = when (viewType) {
    R.layout.item -> UserModelViewHolder(parent)
    else -> SeparatorModelViewHolder(parent)
  }

  override fun getItemViewType(position: Int) {
    // Use peek over getItem to avoid triggering page fetch / drops, since
    // recycling views is not indicative of the user's current scroll position.
    return when (peek(position)) {
      is UiModel.UserModel -> R.layout.item
      is UiModel.SeparatorModel -> R.layout.separator_item
      null -> throw IllegalStateException("Unknown view")
    }
  }

  override fun onBindViewHolder(
    holder: RecyclerView.ViewHolder,
    position: Int
  ) {
    val item = getItem(position)
    if (holder is UserModelViewHolder) {
      holder.bind(item as UserModel)
    } else if (holder is SeparatorModelViewHolder) {
      holder.bind(item as SeparatorModel)
    }
  }
}

object UiModelComparator : DiffUtil.ItemCallback<UiModel>() {
  override fun areItemsTheSame(
    oldItem: UiModel,
    newItem: UiModel
  ): Boolean {
    val isSameRepoItem = oldItem is UiModel.UserModel
      && newItem is UiModel.UserModel
      && oldItem.id == newItem.id

    val isSameSeparatorItem = oldItem is UiModel.SeparatorModel
      && newItem is UiModel.SeparatorModel
      && oldItem.description == newItem.description

    return isSameRepoItem || isSameSeparatorItem
  }

  override fun areContentsTheSame(
    oldItem: UiModel,
    newItem: UiModel
  ) = oldItem == newItem
}
```

### Java

```java
class UiModelAdapter extends PagingDataAdapter<UiModel, RecyclerView.ViewHolder> {
  UiModelAdapter() {
    super(new UiModelComparator(), Dispatchers.getMain(),
      Dispatchers.getDefault());
  }

  @NonNull
  @Override
  public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent,
    int viewType) {
    if (viewType == R.layout.item) {
      return new UserModelViewHolder(parent);
    } else {
      return new SeparatorModelViewHolder(parent);
    }
  }

  @Override
  public int getItemViewType(int position) {
    // Use peek over getItem to avoid triggering page fetch / drops, since
    // recycling views is not indicative of the user's current scroll position.
    UiModel item = peek(position);
    if (item instanceof UiModel.UserModel) {
      return R.layout.item;
    } else if (item instanceof UiModel.SeparatorModel) {
      return R.layout.separator_item;
    } else {
      throw new IllegalStateException("Unknown view");
    }
  }

  @Override
  public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder,
    int position) {
    if (holder instanceOf UserModelViewHolder) {
      UserModel userModel = (UserModel) getItem(position);
      ((UserModelViewHolder) holder).bind(userModel);
    } else {
      SeparatorModel separatorModel = (SeparatorModel) getItem(position);
      ((SeparatorModelViewHolder) holder).bind(separatorModel);
    }
  }
}

class UiModelComparator extends DiffUtil.ItemCallback<UiModel> {
  @Override
  public boolean areItemsTheSame(@NonNull UiModel oldItem,
    @NonNull UiModel newItem) {
    boolean isSameRepoItem = oldItem instanceof UserModel
      && newItem instanceof UserModel
      && ((UserModel) oldItem).getId().equals(((UserModel) newItem).getId());

    boolean isSameSeparatorItem = oldItem instanceof SeparatorModel
      && newItem instanceof SeparatorModel
      && ((SeparatorModel) oldItem).getDescription().equals(
      ((SeparatorModel) newItem).getDescription());

    return isSameRepoItem || isSameSeparatorItem;
  }

  @Override
  public boolean areContentsTheSame(@NonNull UiModel oldItem,
    @NonNull UiModel newItem) {
    return oldItem.equals(newItem);
  }
}
```

### Java

```java
class UiModelAdapter extends PagingDataAdapter<UiModel, RecyclerView.ViewHolder> {
  UiModelAdapter() {
    super(new UiModelComparator(), Dispatchers.getMain(),
      Dispatchers.getDefault());
  }

  @NonNull
  @Override
  public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent,
    int viewType) {
    if (viewType == R.layout.item) {
      return new UserModelViewHolder(parent);
    } else {
      return new SeparatorModelViewHolder(parent);
    }
  }

  @Override
  public int getItemViewType(int position) {
    // Use peek over getItem to avoid triggering page fetch / drops, since
    // recycling views is not indicative of the user's current scroll position.
    UiModel item = peek(position);
    if (item instanceof UiModel.UserModel) {
      return R.layout.item;
    } else if (item instanceof UiModel.SeparatorModel) {
      return R.layout.separator_item;
    } else {
      throw new IllegalStateException("Unknown view");
    }
  }

  @Override
  public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder,
    int position) {
    if (holder instanceOf UserModelViewHolder) {
      UserModel userModel = (UserModel) getItem(position);
      ((UserModelViewHolder) holder).bind(userModel);
    } else {
      SeparatorModel separatorModel = (SeparatorModel) getItem(position);
      ((SeparatorModelViewHolder) holder).bind(separatorModel);
    }
  }
}

class UiModelComparator extends DiffUtil.ItemCallback<UiModel> {
  @Override
  public boolean areItemsTheSame(@NonNull UiModel oldItem,
    @NonNull UiModel newItem) {
    boolean isSameRepoItem = oldItem instanceof UserModel
      && newItem instanceof UserModel
      && ((UserModel) oldItem).getId().equals(((UserModel) newItem).getId());

    boolean isSameSeparatorItem = oldItem instanceof SeparatorModel
      && newItem instanceof SeparatorModel
      && ((SeparatorModel) oldItem).getDescription().equals(
      ((SeparatorModel) newItem).getDescription());

    return isSameRepoItem || isSameSeparatorItem;
  }

  @Override
  public boolean areContentsTheSame(@NonNull UiModel oldItem,
    @NonNull UiModel newItem) {
    return oldItem.equals(newItem);
  }
}
```

## Avoid duplicate work

One key issue to avoid is having the app do unnecessary work. Fetching data is an expensive operation, and data transformations can also take up valuable time. Once the data is loaded and prepared for display in the UI, it should be saved in case a configuration change occurs and the UI needs to be recreated.

The`cachedIn()`operation caches the results of any transformations that occur before it. Therefore,`cachedIn()`should be the last call in your ViewModel.  

### Kotlin

```kotlin
pager.flow // Type is Flow<PagingData<User>>.
  .map { pagingData ->
    pagingData.filter { user -> !user.hiddenFromUi }
      .map { user -> UiModel.UserModel(user) }
  }
  .cachedIn(viewModelScope)
```

### Java

```java
// CoroutineScope helper provided by the lifecycle-viewmodel-ktx artifact.
CoroutineScope viewModelScope = ViewModelKt.getViewModelScope(viewModel);
PagingRx.cachedIn(
  // Type is Flowable<PagingData<User>>.
  PagingRx.getFlowable(pager)
    .map(pagingData -> pagingData
      .filter(user -> !user.isHiddenFromUi())
      .map(UiModel.UserModel::new)),
  viewModelScope);
}
```

### Java

```java
// CoroutineScope helper provided by the lifecycle-viewmodel-ktx artifact.
CoroutineScope viewModelScope = ViewModelKt.getViewModelScope(viewModel);
PagingLiveData.cachedIn(
  Transformations.map(
    // Type is LiveData<PagingData<User>>.
    PagingLiveData.getLiveData(pager),
    pagingData -> pagingData
      .filter(user -> !user.isHiddenFromUi())
      .map(UiModel.UserModel::new)),
  viewModelScope);
```

For more information on using`cachedIn()`with a stream of`PagingData`, see[Set up a stream of PagingData](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#pagingdata-stream).
| **Note:** You can use each instance of`PagingData`only once within`submitData()`. To get around this limitation, consider using the`cachedIn()`operator, which multicasts the stream as part of caching the results. This allows subsequent observers to receive new valid instances of`PagingData`. This is especially useful when you work with operators that reuse the most recently emitted`PagingData`, such as Flow's`.combine()`operator.

## Additional resources

To learn more about the Paging library, see the following additional resources:

### Codelabs

- [Android Paging codelab](https://codelabs.developers.google.com/codelabs/android-paging)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Test your Paging implementation](https://developer.android.com/topic/libraries/architecture/paging/test)
- [Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state)