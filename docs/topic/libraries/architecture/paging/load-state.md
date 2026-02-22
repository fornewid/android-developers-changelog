---
title: https://developer.android.com/topic/libraries/architecture/paging/load-state
url: https://developer.android.com/topic/libraries/architecture/paging/load-state
source: md.txt
---

# Manage and present loading states

The Paging library tracks the state of load requests for paged data and exposes it through the[`LoadState`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState)class. Your app can register a listener with the[`PagingDataAdapter`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter)to receive information about the current state and update the UI accordingly. These states are provided from the adapter because they are synchronous with the UI. This means that your listener receives updates when the page load has been applied to the UI.

A separate`LoadState`signal is provided for each[`LoadType`](https://developer.android.com/reference/kotlin/androidx/paging/LoadType)and data source type (either[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource)or[`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator)). The[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates)object provided by the listener provides information about the loading state from all of these signals. You can use this detailed information to display the appropriate loading indicators to your users.

## Loading states

The Paging library exposes the loading state for use in the UI through the`LoadState`object.`LoadState`objects take one of three forms depending on the current loading state:

- If there is no active load operation and no error, then`LoadState`is a[`LoadState.NotLoading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.NotLoading)object. This subclass also includes the[`endOfPaginationReached`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState#endOfPaginationReached())property, which indicates whether the end of pagination has been reached.
- If there is an active load operation, then`LoadState`is a[`LoadState.Loading`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Loading)object.
- If there is an error, then`LoadState`is a[`LoadState.Error`](https://developer.android.com/reference/kotlin/androidx/paging/LoadState.Error)object.

There are two ways to use`LoadState`in your UI: using a listener, or using a special list adapter to present the loading state directly in the[`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView)list.

## Access the loading state with a listener

To get the loading state for general use in your UI, use the[`loadStateFlow`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter#loadstateflow)stream or the[`addLoadStateListener()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter#addloadstatelistener)method provided by your`PagingDataAdapter`. These mechanisms provide access to a`CombinedLoadStates`object that includes information about the`LoadState`behavior for each load type.

In the following example, the`PagingDataAdapter`displays different UI components depending on the current state of the refresh load:  

### Kotlin

```kotlin
// Activities can use lifecycleScope directly, but Fragments should instead use
// viewLifecycleOwner.lifecycleScope.
lifecycleScope.launch {
  pagingAdapter.loadStateFlow.collectLatest { loadStates ->
    progressBar.isVisible = loadStates.refresh is LoadState.Loading
    retry.isVisible = loadState.refresh !is LoadState.Loading
    errorMsg.isVisible = loadState.refresh is LoadState.Error
  }
}
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  progressBar.setVisibility(loadStates.refresh instanceof LoadState.Loading
    ? View.VISIBLE : View.GONE);
  retry.setVisibility(loadStates.refresh instanceof LoadState.Loading
    ? View.GONE : View.VISIBLE);
  errorMsg.setVisibility(loadStates.refresh instanceof LoadState.Error
    ? View.VISIBLE : View.GONE);
});
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  progressBar.setVisibility(loadStates.refresh instanceof LoadState.Loading
    ? View.VISIBLE : View.GONE);
  retry.setVisibility(loadStates.refresh instanceof LoadState.Loading
    ? View.GONE : View.VISIBLE);
  errorMsg.setVisibility(loadStates.refresh instanceof LoadState.Error
    ? View.VISIBLE : View.GONE);
});
```
| **Note:** Updates from`loadStateFlow`and`addLoadStateListener()`are guaranteed to be synchronous with updates to the UI. This means that if you receive a`LoadState.NotLoading`object, then you can be sure that loading has completed and the UI has been updated accordingly.

For more information on`CombinedLoadStates`, see[Access additional loading state information](https://developer.android.com/topic/libraries/architecture/paging/load-state#additional-info).

## Present the loading state with an adapter

The Paging library provides another list adapter called[`LoadStateAdapter`](https://developer.android.com/reference/kotlin/androidx/paging/LoadStateAdapter)for the purpose of presenting the loading state directly in the displayed list of paged data. This adapter provides access to the current load state of the list, which you can pass to a custom view holder that displays the information.

First, create a view holder class that keeps references to the loading and error views on your screen. Create a`bind()`function that accepts a`LoadState`as a parameter. This function should toggle the view visibility based on the load state parameter:  

### Kotlin

```kotlin
class LoadStateViewHolder(
  parent: ViewGroup,
  retry: () -> Unit
) : RecyclerView.ViewHolder(
  LayoutInflater.from(parent.context)
    .inflate(R.layout.load_state_item, parent, false)
) {
  private val binding = LoadStateItemBinding.bind(itemView)
  private val progressBar: ProgressBar = binding.progressBar
  private val errorMsg: TextView = binding.errorMsg
  private val retry: Button = binding.retryButton
    .also {
      it.setOnClickListener { retry() }
    }

  fun bind(loadState: LoadState) {
    if (loadState is LoadState.Error) {
      errorMsg.text = loadState.error.localizedMessage
    }

    progressBar.isVisible = loadState is LoadState.Loading
    retry.isVisible = loadState is LoadState.Error
    errorMsg.isVisible = loadState is LoadState.Error
  }
}
```

### Java

```java
class LoadStateViewHolder extends RecyclerView.ViewHolder {
  private ProgressBar mProgressBar;
  private TextView mErrorMsg;
  private Button mRetry;

  LoadStateViewHolder(
    @NonNull ViewGroup parent,
    @NonNull View.OnClickListener retryCallback) {
    super(LayoutInflater.from(parent.getContext())
      .inflate(R.layout.load_state_item, parent, false));

    LoadStateItemBinding binding = LoadStateItemBinding.bind(itemView);
    mProgressBar = binding.progressBar;
    mErrorMsg = binding.errorMsg;
    mRetry = binding.retryButton;
  }

  public void bind(LoadState loadState) {
    if (loadState instanceof LoadState.Error) {
      LoadState.Error loadStateError = (LoadState.Error) loadState;
      mErrorMsg.setText(loadStateError.getError().getLocalizedMessage());
    }
    mProgressBar.setVisibility(loadState instanceof LoadState.Loading
      ? View.VISIBLE : View.GONE);
    mRetry.setVisibility(loadState instanceof LoadState.Error
      ? View.VISIBLE : View.GONE);
    mErrorMsg.setVisibility(loadState instanceof LoadState.Error
      ? View.VISIBLE : View.GONE);
  }
}
```

### Java

```java
class LoadStateViewHolder extends RecyclerView.ViewHolder {
  private ProgressBar mProgressBar;
  private TextView mErrorMsg;
  private Button mRetry;

  LoadStateViewHolder(
    @NonNull ViewGroup parent,
    @NonNull View.OnClickListener retryCallback) {
    super(LayoutInflater.from(parent.getContext())
      .inflate(R.layout.load_state_item, parent, false));

    LoadStateItemBinding binding = LoadStateItemBinding.bind(itemView);
    mProgressBar = binding.progressBar;
    mErrorMsg = binding.errorMsg;
    mRetry = binding.retryButton;
  }

  public void bind(LoadState loadState) {
    if (loadState instanceof LoadState.Error) {
      LoadState.Error loadStateError = (LoadState.Error) loadState;
      mErrorMsg.setText(loadStateError.getError().getLocalizedMessage());
    }
    mProgressBar.setVisibility(loadState instanceof LoadState.Loading
      ? View.VISIBLE : View.GONE);
    mRetry.setVisibility(loadState instanceof LoadState.Error
      ? View.VISIBLE : View.GONE);
    mErrorMsg.setVisibility(loadState instanceof LoadState.Error
      ? View.VISIBLE : View.GONE);
  }
}
```

Next, create a class that implements`LoadStateAdapter`, and define the[`onCreateViewHolder()`](https://developer.android.com/reference/kotlin/androidx/paging/LoadStateAdapter#onCreateViewHolder(android.view.ViewGroup,androidx.paging.LoadState))and[`onBindViewHolder()`](https://developer.android.com/reference/kotlin/androidx/paging/LoadStateAdapter#onBindViewHolder(androidx.recyclerview.widget.RecyclerView.ViewHolder,androidx.paging.LoadState))methods. These methods create an instance of your custom view holder and bind the associated load state.  

### Kotlin

```kotlin
// Adapter that displays a loading spinner when
// state is LoadState.Loading, and an error message and retry
// button when state is LoadState.Error.
class ExampleLoadStateAdapter(
  private val retry: () -> Unit
) : LoadStateAdapter<LoadStateViewHolder>() {

  override fun onCreateViewHolder(
    parent: ViewGroup,
    loadState: LoadState
  ) = LoadStateViewHolder(parent, retry)

  override fun onBindViewHolder(
    holder: LoadStateViewHolder,
    loadState: LoadState
  ) = holder.bind(loadState)
}
```

### Java

```java
// Adapter that displays a loading spinner when
// state is LoadState.Loading, and an error message and retry
// button when state is LoadState.Error.
class ExampleLoadStateAdapter extends LoadStateAdapter<LoadStateViewHolder> {
  private View.OnClickListener mRetryCallback;

  ExampleLoadStateAdapter(View.OnClickListener retryCallback) {
    mRetryCallback = retryCallback;
  }

  @NotNull
  @Override
  public LoadStateViewHolder onCreateViewHolder(@NotNull ViewGroup parent,
    @NotNull LoadState loadState) {
    return new LoadStateViewHolder(parent, mRetryCallback);
  }

  @Override
  public void onBindViewHolder(@NotNull LoadStateViewHolder holder,
    @NotNull LoadState loadState) {
    holder.bind(loadState);
  }
}
```

### Java

```java
// Adapter that displays a loading spinner when
// state is LoadState.Loading, and an error message and retry
// button when state is LoadState.Error.
class ExampleLoadStateAdapter extends LoadStateAdapter<LoadStateViewHolder> {
  private View.OnClickListener mRetryCallback;

  ExampleLoadStateAdapter(View.OnClickListener retryCallback) {
    mRetryCallback = retryCallback;
  }

  @NotNull
  @Override
  public LoadStateViewHolder onCreateViewHolder(@NotNull ViewGroup parent,
    @NotNull LoadState loadState) {
    return new LoadStateViewHolder(parent, mRetryCallback);
  }

  @Override
  public void onBindViewHolder(@NotNull LoadStateViewHolder holder,
    @NotNull LoadState loadState) {
    holder.bind(loadState);
  }
}
```

### Display the loading state as a header or footer

To display the loading progress in a header and a footer, call the[`withLoadStateHeaderAndFooter()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter#withloadstateheaderandfooter)method from your`PagingDataAdapter`object:  

### Kotlin

```kotlin
pagingAdapter
  .withLoadStateHeaderAndFooter(
    header = ExampleLoadStateAdapter(adapter::retry),
    footer = ExampleLoadStateAdapter(adapter::retry)
  )
```

### Java

```java
pagingAdapter
  .withLoadStateHeaderAndFooter(
    new ExampleLoadStateAdapter(pagingAdapter::retry),
    new ExampleLoadStateAdapter(pagingAdapter::retry));
```

### Java

```java
pagingAdapter
  .withLoadStateHeaderAndFooter(
    new ExampleLoadStateAdapter(pagingAdapter::retry),
    new ExampleLoadStateAdapter(pagingAdapter::retry));
```

You can instead call[`withLoadStateHeader()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter#withloadstateheader)or[`withLoadStateFooter()`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter#withloadstatefooter)if you want the`RecyclerView`list to display the loading state only in the header or only in the footer.

## Access additional loading state information

The`CombinedLoadStates`object from`PagingDataAdapter`provides information on the load states for your`PagingSource`implementation and also for your`RemoteMediator`implementation, if one exists.

For convenience, you can use the[`refresh`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates#refresh()),[`append`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates#append()), and[`prepend`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates#prepend())properties from`CombinedLoadStates`to access a`LoadState`object for the appropriate load type. These properties generally defer to the load state from the`RemoteMediator`implementation if one exists; otherwise, they contain the appropriate load state from the`PagingSource`implementation. For more detailed information on the underlying logic, see the reference documentation for[`CombinedLoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates).  

### Kotlin

```kotlin
lifecycleScope.launch {
  pagingAdapter.loadStateFlow.collectLatest { loadStates ->
    // Observe refresh load state from RemoteMediator if present, or
    // from PagingSource otherwise.
    refreshLoadState: LoadState = loadStates.refresh
    // Observe prepend load state from RemoteMediator if present, or
    // from PagingSource otherwise.
    prependLoadState: LoadState = loadStates.prepend
    // Observe append load state from RemoteMediator if present, or
    // from PagingSource otherwise.
    appendLoadState: LoadState = loadStates.append
  }
}
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  // Observe refresh load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState refreshLoadState = loadStates.refresh;
  // Observe prepend load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState prependLoadState = loadStates.prepend;
  // Observe append load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState appendLoadState = loadStates.append;
});
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  // Observe refresh load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState refreshLoadState = loadStates.refresh;
  // Observe prepend load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState prependLoadState = loadStates.prepend;
  // Observe append load state from RemoteMediator if present, or
  // from PagingSource otherwise.
  LoadState appendLoadState = loadStates.append;
});
```

However, it is important to remember that only the`PagingSource`load states are guaranteed to be synchronous with UI updates. Because the`refresh`,`append`, and`prepend`properties can potentially take the load state from either`PagingSource`or`RemoteMediator`, they are not guaranteed to be synchronous with UI updates. This can cause UI issues where the loading appears to finish before any of the new data has been added to the UI.

For this reason, the convenience accessors work well for displaying the load state in a header or footer, but for other use cases you might need to specifically access the load state from either`PagingSource`or`RemoteMediator`.`CombinedLoadStates`provides the[`source`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates#source())and[`mediator`](https://developer.android.com/reference/kotlin/androidx/paging/CombinedLoadStates#mediator())properties for this purpose. These properties each expose a[`LoadStates`](https://developer.android.com/reference/kotlin/androidx/paging/LoadStates)object that contains the`LoadState`objects for`PagingSource`or`RemoteMediator`respectively:  

### Kotlin

```kotlin
lifecycleScope.launch {
  pagingAdapter.loadStateFlow.collectLatest { loadStates ->
    // Directly access the RemoteMediator refresh load state.
    mediatorRefreshLoadState: LoadState? = loadStates.mediator.refresh
    // Directly access the RemoteMediator append load state.
    mediatorAppendLoadState: LoadState? = loadStates.mediator.append
    // Directly access the RemoteMediator prepend load state.
    mediatorPrependLoadState: LoadState? = loadStates.mediator.prepend
    // Directly access the PagingSource refresh load state.
    sourceRefreshLoadState: LoadState = loadStates.source.refresh
    // Directly access the PagingSource append load state.
    sourceAppendLoadState: LoadState = loadStates.source.append
    // Directly access the PagingSource prepend load state.
    sourcePrependLoadState: LoadState = loadStates.source.prepend
  }
}
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  // Directly access the RemoteMediator refresh load state.
  LoadState mediatorRefreshLoadState = loadStates.mediator.refresh;
  // Directly access the RemoteMediator append load state.
  LoadState mediatorAppendLoadState = loadStates.mediator.append;
  // Directly access the RemoteMediator prepend load state.
  LoadState mediatorPrependLoadState = loadStates.mediator.prepend;
  // Directly access the PagingSource refresh load state.
  LoadState sourceRefreshLoadState = loadStates.source.refresh;
  // Directly access the PagingSource append load state.
  LoadState sourceAppendLoadState = loadStates.source.append;
  // Directly access the PagingSource prepend load state.
  LoadState sourcePrependLoadState = loadStates.source.prepend;
});
```

### Java

```java
pagingAdapter.addLoadStateListener(loadStates -> {
  // Directly access the RemoteMediator refresh load state.
  LoadState mediatorRefreshLoadState = loadStates.mediator.refresh;
  // Directly access the RemoteMediator append load state.
  LoadState mediatorAppendLoadState = loadStates.mediator.append;
  // Directly access the RemoteMediator prepend load state.
  LoadState mediatorPrependLoadState = loadStates.mediator.prepend;
  // Directly access the PagingSource refresh load state.
  LoadState sourceRefreshLoadState = loadStates.source.refresh;
  // Directly access the PagingSource append load state.
  LoadState sourceAppendLoadState = loadStates.source.append;
  // Directly access the PagingSource prepend load state.
  LoadState sourcePrependLoadState = loadStates.source.prepend;
});
```

## Chain operators on LoadState

Because the`CombinedLoadStates`object provides access to all changes in load state, it is important to filter the load state stream based on specific events. This ensures that you update your UI at the appropriate time to avoid stutters and unnecessary UI updates.

For example, suppose that you want to display an empty view, but only after the initial data load completes. This use case requires that you verify that a data refresh load has started, then wait for the`NotLoading`state to confirm that the refresh has completed. You must filter out all signals except for the ones you need:  

### Kotlin

```kotlin
lifecycleScope.launchWhenCreated {
  adapter.loadStateFlow
    // Only emit when REFRESH LoadState for RemoteMediator changes.
    .distinctUntilChangedBy { it.refresh }
    // Only react to cases where REFRESH completes, such as NotLoading.
    .filter { it.refresh is LoadState.NotLoading }
    // Scroll to top is synchronous with UI updates, even if remote load was
    // triggered.
    .collect { binding.list.scrollToPosition(0) }
}
```

### Java

```java
PublishSubject<CombinedLoadStates> subject = PublishSubject.create();
Disposable disposable =
  subject.distinctUntilChanged(CombinedLoadStates::getRefresh)
  .filter(
    combinedLoadStates -> combinedLoadStates.getRefresh() instanceof LoadState.NotLoading)
  .subscribe(combinedLoadStates -> binding.list.scrollToPosition(0));

pagingAdapter.addLoadStateListener(loadStates -> {
  subject.onNext(loadStates);
});
```

### Java

```java
LiveData<CombinedLoadStates> liveData = new MutableLiveData<>();
LiveData<LoadState> refreshLiveData =
  Transformations.map(liveData, CombinedLoadStates::getRefresh);
LiveData<LoadState> distinctLiveData =
  Transformations.distinctUntilChanged(refreshLiveData);

distinctLiveData.observeForever(loadState -> {
  if (loadState instanceof LoadState.NotLoading) {
    binding.list.scrollToPosition(0);
  }
});
```

This example waits until the refresh load state is updated, but only triggers when the state is`NotLoading`. This ensures that the remote refresh has fully finished before any UI updates happen.

Stream APIs make this type of operation possible. Your app can specify the load events it needs and handle the new data when the appropriate criteria are met.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)
- [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)