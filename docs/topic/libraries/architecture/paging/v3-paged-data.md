---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data
url: https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data
source: md.txt
---

# Load and display paged data

The Paging library provides powerful capabilities for loading and displaying paged data from a larger dataset. This guide demonstrates how to use the Paging library to set up a stream of paged data from a network data source and display it in a[`RecyclerView`](https://developer.android.com/guide/topics/ui/layout/recyclerview).

## Define a data source

The first step is to define a[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource)implementation to identify the data source. The`PagingSource`API class includes the[`load()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource#load)method, which you override to indicate how to retrieve paged data from the corresponding data source.

Use the`PagingSource`class directly to use Kotlin coroutines for async loading. The Paging library also provides classes to support other async frameworks:

- To use RxJava, implement[`RxPagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/rxjava2/RxPagingSource)instead.
- To use`ListenableFuture`from Guava, implement[`ListenableFuturePagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/ListenableFuturePagingSource)instead.

| **Note:** To use the Paging library with RxJava or Guava, you must include[additional dependencies](https://developer.android.com/topic/libraries/architecture/paging/v3-overview#setup).

### Select key and value types

`PagingSource<Key, Value>`has two type parameters:`Key`and`Value`. The key defines the identifier used to load the data, and the value is the type of the data itself. For example, if you load pages of`User`objects from the network by passing`Int`page numbers to[Retrofit](https://square.github.io/retrofit/), select`Int`as the`Key`type and`User`as the`Value`type.

### Define the PagingSource

The following example implements a[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource)that loads pages of items by page number. The`Key`type is`Int`and the`Value`type is`User`.  

### Kotlin

```kotlin
class ExamplePagingSource(
    val backend: ExampleBackendService,
    val query: String
) : PagingSource<Int, User>() {
  override suspend fun load(
    params: LoadParams<Int>
  ): LoadResult<Int, User> {
    try {
      // Start refresh at page 1 if undefined.
      val nextPageNumber = params.key ?: 1
      val response = backend.searchUsers(query, nextPageNumber)
      return LoadResult.Page(
        data = response.users,
        prevKey = null, // Only paging forward.
        nextKey = response.nextPageNumber
      )
    } catch (e: Exception) {
      // Handle errors in this block and return LoadResult.Error for
      // expected errors (such as a network failure).
    }
  }

  override fun getRefreshKey(state: PagingState<Int, User>): Int? {
    // Try to find the page key of the closest page to anchorPosition from
    // either the prevKey or the nextKey; you need to handle nullability
    // here.
    //  * prevKey == null -> anchorPage is the first page.
    //  * nextKey == null -> anchorPage is the last page.
    //  * both prevKey and nextKey are null -> anchorPage is the
    //    initial page, so return null.
    return state.anchorPosition?.let { anchorPosition ->
      val anchorPage = state.closestPageToPosition(anchorPosition)
      anchorPage?.prevKey?.plus(1) ?: anchorPage?.nextKey?.minus(1)
    }
  }
}
```

### Java

```java
class ExamplePagingSource extends RxPagingSource<Integer, User> {
  @NonNull
  private ExampleBackendService mBackend;
  @NonNull
  private String mQuery;

  ExamplePagingSource(@NonNull ExampleBackendService backend,
    @NonNull String query) {
    mBackend = backend;
    mQuery = query;
  }

  @NotNull
  @Override
  public Single<LoadResult<Integer, User>> loadSingle(
    @NotNull LoadParams<Integer> params) {
    // Start refresh at page 1 if undefined.
    Integer nextPageNumber = params.getKey();
    if (nextPageNumber == null) {
      nextPageNumber = 1;
    }

    return mBackend.searchUsers(mQuery, nextPageNumber)
      .subscribeOn(Schedulers.io())
      .map(this::toLoadResult)
      .onErrorReturn(LoadResult.Error::new);
  }

  private LoadResult<Integer, User> toLoadResult(
    @NonNull SearchUserResponse response) {
    return new LoadResult.Page<>(
      response.getUsers(),
      null, // Only paging forward.
      response.getNextPageNumber(),
      LoadResult.Page.COUNT_UNDEFINED,
      LoadResult.Page.COUNT_UNDEFINED);
  }

  @Nullable
  @Override
  public Integer getRefreshKey(@NotNull PagingState<Integer, User> state) {
    // Try to find the page key of the closest page to anchorPosition from
    // either the prevKey or the nextKey; you need to handle nullability
    // here.
    //  * prevKey == null -> anchorPage is the first page.
    //  * nextKey == null -> anchorPage is the last page.
    //  * both prevKey and nextKey are null -> anchorPage is the
    //    initial page, so return null.
    Integer anchorPosition = state.getAnchorPosition();
    if (anchorPosition == null) {
      return null;
    }

    LoadResult.Page<Integer, User> anchorPage = state.closestPageToPosition(anchorPosition);
    if (anchorPage == null) {
      return null;
    }

    Integer prevKey = anchorPage.getPrevKey();
    if (prevKey != null) {
      return prevKey + 1;
    }

    Integer nextKey = anchorPage.getNextKey();
    if (nextKey != null) {
      return nextKey - 1;
    }

    return null;
  }
}
```

### Java

```java
class ExamplePagingSource extends ListenableFuturePagingSource<Integer, User> {
  @NonNull
  private ExampleBackendService mBackend;
  @NonNull
  private String mQuery;
  @NonNull
  private Executor mBgExecutor;

  ExamplePagingSource(
    @NonNull ExampleBackendService backend,
    @NonNull String query, @NonNull Executor bgExecutor) {
    mBackend = backend;
    mQuery = query;
    mBgExecutor = bgExecutor;
  }

  @NotNull
  @Override
  public ListenableFuture<LoadResult<Integer, User>> loadFuture(@NotNull LoadParams<Integer> params) {
    // Start refresh at page 1 if undefined.
    Integer nextPageNumber = params.getKey();
    if (nextPageNumber == null) {
      nextPageNumber = 1;
    }

    ListenableFuture<LoadResult<Integer, User>> pageFuture =
      Futures.transform(mBackend.searchUsers(mQuery, nextPageNumber),
      this::toLoadResult, mBgExecutor);

    ListenableFuture<LoadResult<Integer, User>> partialLoadResultFuture =
      Futures.catching(pageFuture, HttpException.class,
      LoadResult.Error::new, mBgExecutor);

    return Futures.catching(partialLoadResultFuture,
      IOException.class, LoadResult.Error::new, mBgExecutor);
  }

  private LoadResult<Integer, User> toLoadResult(@NonNull SearchUserResponse response) {
    return new LoadResult.Page<>(response.getUsers(),
    null, // Only paging forward.
    response.getNextPageNumber(),
    LoadResult.Page.COUNT_UNDEFINED,
    LoadResult.Page.COUNT_UNDEFINED);
  }

  @Nullable
  @Override
  public Integer getRefreshKey(@NotNull PagingState<Integer, User> state) {
    // Try to find the page key of the closest page to anchorPosition from
    // either the prevKey or the nextKey; you need to handle nullability
    // here.
    //  * prevKey == null -> anchorPage is the first page.
    //  * nextKey == null -> anchorPage is the last page.
    //  * both prevKey and nextKey are null -> anchorPage is the
    //    initial page, so return null.
    Integer anchorPosition = state.getAnchorPosition();
    if (anchorPosition == null) {
      return null;
    }

    LoadResult.Page<Integer, User> anchorPage = state.closestPageToPosition(anchorPosition);
    if (anchorPage == null) {
      return null;
    }

    Integer prevKey = anchorPage.getPrevKey();
    if (prevKey != null) {
      return prevKey + 1;
    }

    Integer nextKey = anchorPage.getNextKey();
    if (nextKey != null) {
      return nextKey - 1;
    }

    return null;
  }
}
```

A typical`PagingSource`implementation passes parameters provided in its constructor to the`load()`method to load appropriate data for a query. In the example above, those parameters are:

- `backend`: an instance of the backend service that provides the data
- `query`: the search query to send to the service indicated by`backend`

The[`LoadParams`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.LoadParams)object contains information about the load operation to be performed. This includes the key to be loaded and the number of items to be loaded.

The[`LoadResult`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.LoadResult)object contains the result of the load operation.`LoadResult`is a sealed class that takes one of two forms, depending on whether the`load()`call succeeded:

- If the load is successful, return a`LoadResult.Page`object.
- If the load is not successful, return a`LoadResult.Error`object.

The following figure illustrates how the`load()`function in this example receives the key for each load and provides the key for the subsequent load.
![On each load() call, the ExamplePagingSource takes in the current key and returns the next key to load.](https://developer.android.com/static/topic/libraries/architecture/images/paging3-source-load.svg)**Figure 1.** Diagram showing how`load()`uses and updates the key.

The`PagingSource`implementation must also implement a[`getRefreshKey()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource#getrefreshkey)method that takes a[`PagingState`](https://developer.android.com/reference/kotlin/androidx/paging/PagingState)object as a parameter. It returns the key to pass into the`load()`method when the data is refreshed or invalidated after the initial load. The Paging Library calls this method automatically on subsequent refreshes of the data.

### Handle errors

Requests to load data can fail for a number of reasons, especially when loading over a network. Report errors encountered during loading by returning a`LoadResult.Error`object from the`load()`method.

For example, you can catch and report loading errors in`ExamplePagingSource`from the previous example by adding the following to the`load()`method:  

### Kotlin

```kotlin
catch (e: IOException) {
  // IOException for network failures.
  return LoadResult.Error(e)
} catch (e: HttpException) {
  // HttpException for any non-2xx HTTP status codes.
  return LoadResult.Error(e)
}
```

### Java

```java
return backend.searchUsers(searchTerm, nextPageNumber)
  .subscribeOn(Schedulers.io())
  .map(this::toLoadResult)
  .onErrorReturn(LoadResult.Error::new);
```

### Java

```java
ListenableFuture<LoadResult<Integer, User>> pageFuture = Futures.transform(
  backend.searchUsers(query, nextPageNumber), this::toLoadResult,
  bgExecutor);

ListenableFuture<LoadResult<Integer, User>> partialLoadResultFuture = Futures.catching(
  pageFuture, HttpException.class, LoadResult.Error::new,
  bgExecutor);

return Futures.catching(partialLoadResultFuture,
  IOException.class, LoadResult.Error::new, bgExecutor);
```

For more information on handling Retrofit errors, see the samples in the`PagingSource`API reference.

`PagingSource`collects and delivers`LoadResult.Error`objects to the UI so that you can act on them. For more information on exposing the loading state in the UI, see[Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state).

## Set up a stream of PagingData

Next, you need a stream of paged data from the`PagingSource`implementation. Set up the data stream in your`ViewModel`. The[`Pager`](https://developer.android.com/reference/kotlin/androidx/paging/Pager)class provides methods that expose a reactive stream of[`PagingData`](https://developer.android.com/reference/kotlin/androidx/paging/PagingData)objects from a`PagingSource`. The Paging library supports using several stream types, including`Flow`,`LiveData`, and the`Flowable`and`Observable`types from RxJava.

When you create a`Pager`instance to set up your reactive stream, you must provide the instance with a[`PagingConfig`](https://developer.android.com/reference/kotlin/androidx/paging/PagingConfig)configuration object and a function that tells`Pager`how to get an instance of your`PagingSource`implementation:  

### Kotlin

```kotlin
val flow = Pager(
  // Configure how data is loaded by passing additional properties to
  // PagingConfig, such as prefetchDistance.
  PagingConfig(pageSize = 20)
) {
  ExamplePagingSource(backend, query)
}.flow
  .cachedIn(viewModelScope)
```

### Java

```java
// CoroutineScope helper provided by the lifecycle-viewmodel-ktx artifact.
CoroutineScope viewModelScope = ViewModelKt.getViewModelScope(viewModel);
Pager<Integer, User> pager = Pager<>(
  new PagingConfig(/* pageSize = */ 20),
  () -> ExamplePagingSource(backend, query));

Flowable<PagingData<User>> flowable = PagingRx.getFlowable(pager);
PagingRx.cachedIn(flowable, viewModelScope);
```

### Java

```java
// CoroutineScope helper provided by the lifecycle-viewmodel-ktx artifact.
CoroutineScope viewModelScope = ViewModelKt.getViewModelScope(viewModel);
Pager<Integer, User> pager = Pager<>(
  new PagingConfig(/* pageSize = */ 20),
  () -> ExamplePagingSource(backend, query));

PagingLiveData.cachedIn(PagingLiveData.getLiveData(pager), viewModelScope);
```

The`cachedIn()`operator makes the data stream shareable and caches the loaded data with the provided`CoroutineScope`. This example uses the`viewModelScope`provided by the lifecycle`lifecycle-viewmodel-ktx`artifact.

The`Pager`object calls the`load()`method from the`PagingSource`object, providing it with the[`LoadParams`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.LoadParams)object and receiving the[`LoadResult`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource.LoadResult)object in return.

## Define a RecyclerView adapter

You also need to set up an adapter to receive the data into your`RecyclerView`list. The Paging library provides the`PagingDataAdapter`class for this purpose.

Define a class that extends`PagingDataAdapter`. In the example,`UserAdapter`extends`PagingDataAdapter`to provide a`RecyclerView`adapter for list items of type`User`and using`UserViewHolder`as a[view holder](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.ViewHolder):  

### Kotlin

```kotlin
class UserAdapter(diffCallback: DiffUtil.ItemCallback<User>) :
  PagingDataAdapter<User, UserViewHolder>(diffCallback) {
  override fun onCreateViewHolder(
    parent: ViewGroup,
    viewType: Int
  ): UserViewHolder {
    return UserViewHolder(parent)
  }

  override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
    val item = getItem(position)
    // Note that item can be null. ViewHolder must support binding a
    // null item as a placeholder.
    holder.bind(item)
  }
}
```

### Java

```java
class UserAdapter extends PagingDataAdapter<User, UserViewHolder> {
  UserAdapter(@NotNull DiffUtil.ItemCallback<User> diffCallback) {
    super(diffCallback);
  }

  @NonNull
  @Override
  public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    return new UserViewHolder(parent);
  }

  @Override
  public void onBindViewHolder(@NonNull UserViewHolder holder, int position) {
    User item = getItem(position);
    // Note that item can be null. ViewHolder must support binding a
    // null item as a placeholder.
    holder.bind(item);
  }
}
```

### Java

```java
class UserAdapter extends PagingDataAdapter<User, UserViewHolder> {
  UserAdapter(@NotNull DiffUtil.ItemCallback<User> diffCallback) {
    super(diffCallback);
  }

  @NonNull
  @Override
  public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    return new UserViewHolder(parent);
  }

  @Override
  public void onBindViewHolder(@NonNull UserViewHolder holder, int position) {
    User item = getItem(position);
    // Note that item can be null. ViewHolder must support binding a
    // null item as a placeholder.
    holder.bind(item);
  }
}
```

Your adapter must also define the`onCreateViewHolder()`and`onBindViewHolder()`methods and specify a[`DiffUtil.ItemCallback`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/DiffUtil.ItemCallback). This works the same as it normally does when defining`RecyclerView`list adapters:  

### Kotlin

```kotlin
object UserComparator : DiffUtil.ItemCallback<User>() {
  override fun areItemsTheSame(oldItem: User, newItem: User): Boolean {
    // Id is unique.
    return oldItem.id == newItem.id
  }

  override fun areContentsTheSame(oldItem: User, newItem: User): Boolean {
    return oldItem == newItem
  }
}
```

### Java

```java
class UserComparator extends DiffUtil.ItemCallback<User> {
  @Override
  public boolean areItemsTheSame(@NonNull User oldItem,
    @NonNull User newItem) {
    // Id is unique.
    return oldItem.id.equals(newItem.id);
  }

  @Override
  public boolean areContentsTheSame(@NonNull User oldItem,
    @NonNull User newItem) {
    return oldItem.equals(newItem);
  }
}
```

### Java

```java
class UserComparator extends DiffUtil.ItemCallback<User> {
  @Override
  public boolean areItemsTheSame(@NonNull User oldItem,
    @NonNull User newItem) {
    // Id is unique.
    return oldItem.id.equals(newItem.id);
  }

  @Override
  public boolean areContentsTheSame(@NonNull User oldItem,
    @NonNull User newItem) {
    return oldItem.equals(newItem);
  }
}
```

## Display the paged data in your UI

Now that you have defined a`PagingSource`, created a way for your app to generate a stream of`PagingData`, and defined a`PagingDataAdapter`, you are ready to connect these elements together and display paged data in your activity.

Perform the following steps in your activity's`onCreate`or fragment's`onViewCreated`method:

1. Create an instance of your`PagingDataAdapter`class.
2. Pass the`PagingDataAdapter`instance to the[`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView)list that you want to display your paged data.
3. Observe the`PagingData`stream and pass each generated value to your adapter's`submitData()`method.

### Kotlin

```kotlin
val viewModel by viewModels<ExampleViewModel>()

val pagingAdapter = UserAdapter(UserComparator)
val recyclerView = findViewById<RecyclerView>(R.id.recycler_view)
recyclerView.adapter = pagingAdapter

// Activities can use lifecycleScope directly; fragments use
// viewLifecycleOwner.lifecycleScope.
lifecycleScope.launch {
  viewModel.flow.collectLatest { pagingData ->
    pagingAdapter.submitData(pagingData)
  }
}
```

### Java

```java
ExampleViewModel viewModel = new ViewModelProvider(this)
  .get(ExampleViewModel.class);

UserAdapter pagingAdapter = new UserAdapter(new UserComparator());
RecyclerView recyclerView = findViewById<RecyclerView>(
  R.id.recycler_view);
recyclerView.adapter = pagingAdapter

viewModel.flowable
  // Using AutoDispose to handle subscription lifecycle.
  // See: https://github.com/uber/AutoDispose.
  .to(autoDisposable(AndroidLifecycleScopeProvider.from(this)))
  .subscribe(pagingData -> pagingAdapter.submitData(lifecycle, pagingData));
```

### Java

```java
ExampleViewModel viewModel = new ViewModelProvider(this)
  .get(ExampleViewModel.class);

UserAdapter pagingAdapter = new UserAdapter(new UserComparator());
RecyclerView recyclerView = findViewById<RecyclerView>(
  R.id.recycler_view);
recyclerView.adapter = pagingAdapter

// Activities can use getLifecycle() directly; fragments use
// getViewLifecycleOwner().getLifecycle().
viewModel.liveData.observe(this, pagingData ->
  pagingAdapter.submitData(getLifecycle(), pagingData));
```

The`RecyclerView`list now displays the paged data from the data source and automatically loads another page when necessary.
| **Caution:** The`submitData()`method suspends and does not return until either the`PagingSource`is invalidated or the adapter's refresh method is called. This means that code after the`submitData()`call might execute much later than you intend.

## Additional resources

To learn more about the Paging library, see the following additional resources:

### Codelabs

- [Android Paging Advanced codelab](https://codelabs.developers.google.com/codelabs/android-paging)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)
- [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration)
- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)