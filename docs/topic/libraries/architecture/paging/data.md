---
title: https://developer.android.com/topic/libraries/architecture/paging/data
url: https://developer.android.com/topic/libraries/architecture/paging/data
source: md.txt
---

# Gather paged data

This guide builds upon the[Paging Library overview](https://developer.android.com/topic/libraries/architecture/paging), discussing how you can customize your app's data-loading solution to meet your app's architecture needs.
| **Caution:** This guide covers an older, deprecated version of the Paging library. For more information about the latest stable version of Paging, see the[Paging 3 guides](https://developer.android.com/topic/libraries/architecture/paging/v3-overview).

## Construct an observable list

Typically, your UI code observes a[`LiveData<PagedList>`](https://developer.android.com/reference/androidx/lifecycle/LiveData)object (or, if you're using[RxJava2](https://github.com/ReactiveX/RxJava), a`Flowable<PagedList>`or`Observable<PagedList>`object), which resides in your app's[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel). This observable object forms a connection between the presentation and contents of your app's list data.

In order to create one of these observable[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)objects, pass in an instance of[`DataSource.Factory`](https://developer.android.com/reference/androidx/paging/DataSource.Factory)to a[`LivePagedListBuilder`](https://developer.android.com/reference/androidx/paging/LivePagedListBuilder)or[`RxPagedListBuilder`](https://developer.android.com/reference/androidx/paging/RxPagedListBuilder)object. A[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource)object loads pages for a single`PagedList`. The factory class creates new instances of`PagedList`in response to content updates, such as database table invalidations and network refreshes. The[Room persistence library](https://developer.android.com/topic/libraries/architecture/room)can provide`DataSource.Factory`objects for you, or you can[build your own](https://developer.android.com/topic/libraries/architecture/paging/data#custom-data-source).

The following code snippet shows how to create a new instance of[`LiveData<PagedList>`](https://developer.android.com/reference/androidx/lifecycle/LiveData)in your app's[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)class using Room's[`DataSource.Factory`](https://developer.android.com/reference/androidx/paging/DataSource.Factory)-building capabilities:

ConcertDao  

### Kotlin

```kotlin
@Dao
interface ConcertDao {
    // The Int type parameter tells Room to use a PositionalDataSource
    // object, with position-based loading under the hood.
    @Query("SELECT * FROM concerts ORDER BY date DESC")
    fun concertsByDate(): DataSource.Factory<Int, Concert>
}
```

### Java

```java
@Dao
public interface ConcertDao {
    // The Integer type parameter tells Room to use a PositionalDataSource
    // object, with position-based loading under the hood.
    @Query("SELECT * FROM concerts ORDER BY date DESC")
    DataSource.Factory<Integer, Concert> concertsByDate();
}
```

ConcertViewModel  

### Kotlin

```kotlin
// The Int type argument corresponds to a PositionalDataSource object.
val myConcertDataSource : DataSource.Factory<Int, Concert> =
       concertDao.concertsByDate()

val concertList = myConcertDataSource.toLiveData(pageSize = 50)
```

### Java

```java
// The Integer type argument corresponds to a PositionalDataSource object.
DataSource.Factory<Integer, Concert> myConcertDataSource =
       concertDao.concertsByDate();

LiveData<PagedList<Concert>> concertList =
        LivePagedListBuilder(myConcertDataSource, /* page size */ 50).build();
```

## Define your own paging configuration

To further configure a[`LiveData<PagedList>`](https://developer.android.com/reference/androidx/lifecycle/LiveData)for advanced cases, you can also define your own paging configuration. In particular, you can define the following attributes:

- **[Page size](https://developer.android.com/reference/androidx/paging/PagedList.Config.Builder#setPageSize(int)):**The number of items in each page.
- **[Prefetch distance](https://developer.android.com/reference/androidx/paging/PagedList.Config.Builder#setPrefetchDistance(int)):**Given the last visible item in an app's UI, the number of items beyond this last item that the Paging Library should attempt to fetch in advance. This value should be several times larger than the page size.
- **[Placeholder presence](https://developer.android.com/reference/androidx/paging/PagedList.Config.Builder#setEnablePlaceholders(boolean)):** Determines whether the UI displays placeholders for list items that haven't finished loading yet. For a discussion about the benefits and drawbacks of using placeholders, learn how to[Provide placeholders in your UI](https://developer.android.com/topic/libraries/architecture/paging/ui#provide-placeholders).

If you'd like more control over when the Paging Library loads a list from your app's database, pass a custom[`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor)object to the[`LivePagedListBuilder`](https://developer.android.com/reference/androidx/paging/LivePagedListBuilder), as shown in the following code snippet:

ConcertViewModel  

### Kotlin

```kotlin
val myPagingConfig = Config(
        pageSize = 50,
        prefetchDistance = 150,
        enablePlaceholders = true
)

// The Int type argument corresponds to a PositionalDataSource object.
val myConcertDataSource : DataSource.Factory<Int, Concert> =
        concertDao.concertsByDate()

val concertList = myConcertDataSource.toLiveData(
        pagingConfig = myPagingConfig,
        fetchExecutor = myExecutor
)
```

### Java

```java
PagedList.Config myPagingConfig = new PagedList.Config.Builder()
        .setPageSize(50)
        .setPrefetchDistance(150)
        .setEnablePlaceholders(true)
        .build();

// The Integer type argument corresponds to a PositionalDataSource object.
DataSource.Factory<Integer, Concert> myConcertDataSource =
        concertDao.concertsByDate();

LiveData<PagedList<Concert>> concertList =
        new LivePagedListBuilder<>(myConcertDataSource, myPagingConfig)
            .setFetchExecutor(myExecutor)
            .build();
```

## Choose the correct data source type

It's important to connect to the data source that best handles your source data's structure:

- Use[`PageKeyedDataSource`](https://developer.android.com/reference/androidx/paging/PageKeyedDataSource)if pages you load embed next/previous keys. For example, if you're fetching social media posts from the network, you may need to pass a`nextPage`token from one load into a subsequent load.
- Use[`ItemKeyedDataSource`](https://developer.android.com/reference/androidx/paging/ItemKeyedDataSource)if you need to use data from item*N* to fetch item*N+1*. For example, if you're fetching threaded comments for a discussion app, you might need to pass the ID of the last comment to get the contents of the next comment.
- Use[`PositionalDataSource`](https://developer.android.com/reference/androidx/paging/PositionalDataSource)if you need to fetch pages of data from any location you choose in your data store. This class supports requesting a set of data items beginning from whatever location you select. For example, the request might return the 50 data items beginning with location 1500.

## Notify when data is invalid

When using the Paging Library, it's up to the**data layer** to notify the other layers of your app when a table or row has become stale. To do so, call[`invalidate()`](https://developer.android.com/reference/androidx/paging/DataSource#invalidate)from the[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource)class that you've chosen for your app.
| **Note:** Your app's UI can trigger this data invalidation functionality using a[swipe to refresh](https://developer.android.com/training/swipe)model.

## Build your own data sources

If you use a custom local data solution, or if you load data directly from a network, you can implement one of the[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource)subclassses. The following code snippet shows a data source that's keyed off of a given concert's start time:  

### Kotlin

```kotlin
class ConcertTimeDataSource() :
        ItemKeyedDataSource<Date, Concert>() {
    override fun getKey(item: Concert) = item.startTime

    override fun loadInitial(
            params: LoadInitialParams<Date>,
            callback: LoadInitialCallback<Concert>) {
        val items = fetchItems(params.requestedInitialKey,
                params.requestedLoadSize)
        callback.onResult(items)
    }

    override fun loadAfter(
            params: LoadParams<Date>,
            callback: LoadCallback<Concert>) {
        val items = fetchItemsAfter(
            date = params.key,
            limit = params.requestedLoadSize)
        callback.onResult(items)
    }
}
```

### Java

```java
public class ConcertTimeDataSource
        extends ItemKeyedDataSource<Date, Concert> {
    @NonNull
    @Override
    public Date getKey(@NonNull Concert item) {
        return item.getStartTime();
    }

    @Override
    public void loadInitial(@NonNull LoadInitialParams<Date> params,
            @NonNull LoadInitialCallback<Concert> callback) {
        List<Concert> items =
            fetchItems(params.key, params.requestedLoadSize);
        callback.onResult(items);
    }

    @Override
    public void loadAfter(@NonNull LoadParams<Date> params,
            @NonNull LoadCallback<Concert> callback) {
        List<Concert> items =
            fetchItemsAfter(params.key, params.requestedLoadSize);
        callback.onResult(items);
    }
```

You can then load this customized data into`PagedList`objects by creating a concrete subclass of[`DataSource.Factory`](https://developer.android.com/reference/androidx/paging/DataSource.Factory). The following code snippet shows how to generate new instances of the custom data source defined in the preceding code snippet:  

### Kotlin

```kotlin
class ConcertTimeDataSourceFactory :
        DataSource.Factory<Date, Concert>() {
    val sourceLiveData = MutableLiveData<ConcertTimeDataSource>()
    var latestSource: ConcertDataSource?
    override fun create(): DataSource<Date, Concert> {
        latestSource = ConcertTimeDataSource()
        sourceLiveData.postValue(latestSource)
        return latestSource
    }
}
```

### Java

```java
public class ConcertTimeDataSourceFactory
        extends DataSource.Factory<Date, Concert> {
    private MutableLiveData<ConcertTimeDataSource> sourceLiveData =
            new MutableLiveData<>();

    private ConcertDataSource latestSource;

    @Override
    public DataSource<Date, Concert> create() {
        latestSource = new ConcertTimeDataSource();
        sourceLiveData.postValue(latestSource);
        return latestSource;
    }
}
```

## Consider how content updates work

As you construct observable[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)objects, consider how content updates work. If you're loading data directly from a[Room database](https://developer.android.com/training/data-storage/room)updates get pushed to your app's UI automatically.

When using a paged network API, you typically have a user interaction, such as "swipe to refresh," serve as a signal for invalidating the[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource)that you've used most recently. You then request a new instance of that data source. This following code snippet demonstrates this behavior:  

### Kotlin

```kotlin
class ConcertActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        // ...
        concertTimeViewModel.refreshState.observe(this, Observer {
            // Shows one possible way of triggering a refresh operation.
            swipeRefreshLayout.isRefreshing =
                    it == MyNetworkState.LOADING
        })
        swipeRefreshLayout.setOnRefreshListener {
            concertTimeViewModel.invalidateDataSource()
        }
    }
}

class ConcertTimeViewModel(firstConcertStartTime: Date) : ViewModel() {
    val dataSourceFactory = ConcertTimeDataSourceFactory(firstConcertStartTime)
    val concertList: LiveData<PagedList<Concert>> =
            dataSourceFactory.toLiveData(
                pageSize = 50,
                fetchExecutor = myExecutor
            )

    fun invalidateDataSource() =
            dataSourceFactory.sourceLiveData.value?.invalidate()
}
```

### Java

```java
public class ConcertActivity extends AppCompatActivity {
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        // ...
        viewModel.getRefreshState()
                .observe(this, new Observer<NetworkState>() {
            // Shows one possible way of triggering a refresh operation.
            @Override
            public void onChanged(@Nullable MyNetworkState networkState) {
                swipeRefreshLayout.isRefreshing =
                        networkState == MyNetworkState.LOADING;
            }
        };

        swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshListener() {
            @Override
            public void onRefresh() {
                viewModel.invalidateDataSource();
            }
        });
    }
}

public class ConcertTimeViewModel extends ViewModel {
    private LiveData<PagedList<Concert>> concertList;
    private DataSource<Date, Concert> mostRecentDataSource;

    public ConcertTimeViewModel(Date firstConcertStartTime) {
        ConcertTimeDataSourceFactory dataSourceFactory =
                new ConcertTimeDataSourceFactory(firstConcertStartTime);
        mostRecentDataSource = dataSourceFactory.create();
        concertList = new LivePagedListBuilder<>(dataSourceFactory, 50)
                .setFetchExecutor(myExecutor)
                .build();
    }

    public void invalidateDataSource() {
        mostRecentDataSource.invalidate();
    }
}
```

## Provide data mapping

The Paging Library supports item-based and page-based transformations of items loaded by a[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource).

In the following code snippet, a combination of concert name and concert date is mapped to a single string containing both the name and date:  

### Kotlin

```kotlin
class ConcertViewModel : ViewModel() {
    val concertDescriptions : LiveData<PagedList<String>>
        init {
            val concerts = database.allConcertsFactory()
                    .map { "${it.name} - ${it.date}" }
                    .toLiveData(pageSize = 50)
        }
}
```

### Java

```java
public class ConcertViewModel extends ViewModel {
    private LiveData<PagedList<String>> concertDescriptions;

    public ConcertViewModel(MyDatabase database) {
        DataSource.Factory<Integer, Concert> factory =
                database.allConcertsFactory().map(concert ->
                    concert.getName() + "-" + concert.getDate());
        concertDescriptions = new LivePagedListBuilder<>(
            factory, /* page size */ 50).build();
    }
}
```

This can be useful if you want to wrap, convert, or prepare items after they're loaded. Because this work is done on the fetch executor, you can do potentially expensive work, such as reading from disk or querying a separate database.
| **Note:** JOIN queries are always more efficient than requerying as part of`map()`.

## Provide feedback

Share your feedback and ideas with us through these resources:

[Issue tracker](https://issuetracker.google.com/issues/new?component=413106&template=1096385):bug:
:   Report issues so we can fix bugs.

## Additional resources

To learn more about the Paging Library, consult the following resources.

### Samples

- [Android Architecture Components Paging sample](https://github.com/android/architecture-components-samples/tree/paging2/PagingSample)
- [Paging With Network Sample](https://github.com/android/architecture-components-samples/tree/paging2/PagingWithNetworkSample)

### Codelabs

- [Android Paging codelab](https://codelabs.developers.google.com/codelabs/android-paging/index.html?index=../../index#0)

### Videos

- [Android Jetpack: manage infinite lists with RecyclerView and Paging (Google I/O '18)](https://www.youtube.com/watch?v=BE5bsyGGLf4)
- [Android Jetpack: Paging](https://www.youtube.com/watch?v=QVMqCRs0BNA)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration)
- [Paging 2 library overview](https://developer.android.com/topic/libraries/architecture/paging)
- [Display paged lists](https://developer.android.com/topic/libraries/architecture/paging/ui)