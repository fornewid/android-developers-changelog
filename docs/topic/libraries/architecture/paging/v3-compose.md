---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-compose
url: https://developer.android.com/topic/libraries/architecture/paging/v3-compose
source: md.txt
---

This guide explains how to implement Paging 3 with Jetpack Compose, covering
implementations both with and without a Room database. Pagination is a strategy
for managing large datasets by loading and displaying them in small, manageable
chunks, called pages, rather than loading everything at once.

Any app that features an infinite scrolling feed (such as a social media
timeline, a large catalog of ecommerce products, or an extensive email inbox)
requires robust data pagination. Because users typically only view a small
portion of a list, and mobile devices have limited screen sizes, loading the
entire dataset isn't efficient. It wastes system resources and can cause jank or
app freezes, worsening the user experience. To solve this, you can use [lazy
loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading). While components like [`LazyList`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary) in Compose handle lazy loading
on the UI side, loading data lazily from the disk or network further enhances
performance.

The Paging 3 library is the recommended solution for handling data pagination.
If you are migrating from Paging 2, see [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration) for guidance.

## Prerequisites

Before proceeding, familiarize yourself with the following:

- Networking on Android (we use [Retrofit](https://github.com/square/retrofit) in this document, but Paging 3 works with any library, such as [Ktor](https://ktor.io/)).
- The Compose UI toolkit.

## Set up dependencies

Add the following dependencies to your app-level `build.gradle.kts` file.

    dependencies {
      val paging_version = "3.4.0"

      // Paging Compose
      implementation("androidx.paging:paging-compose:$paging_version")

      // Networking dependencies used in this guide
      val retrofit = "3.0.0"
      val kotlinxSerializationJson = "1.9.0"
      val retrofitKotlinxSerializationConverter = "1.0.0"
      val okhttp = "4.12.0"

      implementation("com.squareup.retrofit2:retrofit:$retrofit")
      implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:$kotlinxSerializationJson")
      implementation("com.jakewharton.retrofit:retrofit2-kotlinx-serialization-converter:$retrofitKotlinxSerializationConverter")
      implementation(platform("com.squareup.okhttp3:okhttp-bom:$okhttp"))
      implementation("com.squareup.okhttp3:okhttp")
      implementation("com.squareup.okhttp3:logging-interceptor")
    }

## Define the `Pager` class

The `Pager` class is the primary entry point for pagination. It constructs a
reactive stream of `PagingData`. You should instantiate the `Pager` and reuse
it within your `ViewModel`.

The `Pager` requires a `PagingConfig` to determine how to fetch and present
data.

    // Configs for pagination
    val PAGING_CONFIG = PagingConfig(
        pageSize = 50, // Items requested from data source
        enablePlaceholders = false,
        initialLoadSize = 50,
        prefetchDistance = 10 // Items from the end that trigger the next fetch
    )

You can implement `Pager` in two ways: without a database (network only) or with
a database (using Room).

## Implement without a database

When not using a database, you need a `PagingSource<Key, Value>` to handle
on-demand data loading. In this example, the key is `Int` and the value is a
`Product`.

You must implement two abstract methods in your `PagingSource`:

- **`load`** : A suspending function that receives `LoadParams`. Use this to
  fetch data for `Refresh`, `Append`, or `Prepend` requests.

- **`getRefreshKey`** : Provides the key used to reload data if the pager is
  invalidated. This method calculates the key based on the user's
  current scroll position (`state.anchorPosition`).

The following code example shows how to implement the
`ProductPagingSource` class, which is necessary for defining the data
fetching logic when using Paging 3 without a local database.

    class ProductPagingSource : PagingSource<Int, Product>() {
        override fun getRefreshKey(state: PagingState<Int, Product>): Int {

    // This is called when the Pager needs to load new data after invalidation
          // (for example, when the user scrolls quickly or the data stream is
          // manually refreshed).

          // It tries to calculate the page key (offset) that is closest to the
          // item the user was last viewing (`state.anchorPosition`).

            return ((state.anchorPosition ?: 0) - state.config.initialLoadSize / 2).coerceAtLeast(0)
        }

        override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Product> {
            return when (params) {
                    // Case 1: The very first load or a manual refresh. Start from
                    // offset 0.
                is LoadParams.Refresh<Int> -> {
                    fetchProducts(0, params.loadSize)
                }
                    // Case 2: User scrolled to the end of the list. Load the next
                    // 'page' using the stored key.
                is LoadParams.Append<Int> -> {
                    fetchProducts(params.key, params.loadSize)
                }
                    // Case 3: Loading backward. Not supported in this
                    // implementation.
                is LoadParams.Prepend<Int> -> LoadResult.Invalid()
            }
        }
    // Helper function to interact with the API service and map the response
    //  into a [LoadResult.Page] or [LoadResult.Error].
        private suspend fun fetchProducts(key: Int, limit: Int): LoadResult<Int, Product> {
            return try {
                val response = productService.fetchProducts(limit, key)

                LoadResult.Page(
                    data = response.products,
                    prevKey = null,
                    nextKey = (key + response.products.size).takeIf { nextKey ->
                        nextKey < response.total
                    }
                )
            } catch (e: Exception) {
                    // Captures network failures or JSON parsing errors to display
                    // in the UI.
                LoadResult.Error(e)
            }
        }
    }

In your `ViewModel` class, create the `Pager`:

    val productPager = Pager(
        //  Configuration: Defines page size, prefetch distance, and placeholders.
        config = PAGING_CONFIG,
        //  Initial State: Start loading data from the very first index (offset 0).
        initialKey = 0,
        //  Factory: Creates a new instance of the PagingSource whenever the
        // data is invalidated (for example, calling pagingSource.invalidate()).
        pagingSourceFactory = { ProductPagingSource() }
    ).flow.cachedIn(viewModelScope)

> [!NOTE]
> **Note:** The `.cachedIn(viewModelScope)` operator is crucial. It ensures state persistence by keeping the loaded `PagingData` in memory as long as the `ViewModel` exists. Without this, configuration changes (like screen rotation) can cause the app to forget the loaded data and restart the download.

## Implement with a database

When using Room, the database generates the `PagingSource` class automatically.
However, the database doesn't know when to fetch more data from the network. To
handle this, implement a [`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator).

The `RemoteMediator.load()` method provides the `loadType` (`Append`, `Prepend`,
or `Refresh`) and the state. It returns a `MediatorResult` indicating success or
failure, and whether the end of pagination has been reached.

    @OptIn(ExperimentalPagingApi::class)
    @OptIn(ExperimentalPagingApi::class)
    class ProductRemoteMediator : RemoteMediator<Int, Product>() {
        override suspend fun load(
            loadType: LoadType,
            state: PagingState<Int, Product>
        ): MediatorResult {
            return try {
                // Get the count of loaded items to calculate the skip value
                val skip = when (loadType) {
                    LoadType.REFRESH -> 0
                    LoadType.PREPEND -> return MediatorResult.Success(endOfPaginationReached = true)
                    LoadType.APPEND -> {
                        InMemoryDatabaseProvider.INSTANCE.productDao().getCount()
                    }
                }

                val response = productService.fetchProducts(
                    state.config.pageSize,
                    skip
                )

                InMemoryDatabaseProvider.INSTANCE.productDao().apply {
                    insertAll(response.products)
                }

                MediatorResult.Success(
                    endOfPaginationReached = response.skip + response.limit >= response.total
                )
            } catch (e: Exception) {
                MediatorResult.Error(e)
            }
        }
    }

In your `ViewModel`, the implementation simplifies significantly because Room
handles the `PagingSource` class:

    val productPager = ProductRepository().fetchProducts().flow.cachedIn(viewModelScope)

## Network setup

The previous examples rely on a network service. This section provides the
Retrofit and Serialization setup used to fetch data from the
`api.example.com/products` endpoint.

### Data classes

The following code example shows how to define the two data classes,
`ProductResponse` and `Product`, which are used with
[`kotlinx.serialization`](https://github.com/Kotlin/kotlinx.serialization) to parse the paginated JSON response from the
network service.

    @Serializable
    data class ProductResponse(
        val products: List<Product>,
        val total: Int,
        val skip: Int,
        val limit: Int
    )

    @Serializable
    data class Product(
        val id: Int,
        var title: String = "",
        // ... other fields (description, price, etc.)
        val thumbnail: String = ""
    )

### Retrofit service

The following code example shows how to define the Retrofit service interface
(`ProductService`) for the network-only implementation, specifying the
endpoint (`@GET("/products")`) and the necessary pagination parameters (`limit`)
and (`skip`) required by the Paging 3 library to fetch data pages.

    interface ProductService {
        @GET("/products")
        suspend fun fetchProducts(
            @Query("limit") limit: Int,
            @Query("skip") skip: Int
        ): ProductResponse
    }

    // Setup logic (abbreviated)
    val jsonConverter = Json { ignoreUnknownKeys = true }
    val retrofit = Retrofit.Builder()
        .baseUrl("https://api.example.com")
        .addConverterFactory(jsonConverter.asConverterFactory("application/json".toMediaType()))
        // ... client setup
        .build()

## Consume data in Compose

After you set up your `Pager`, you can display the data in your UI.

1. **Collect the flow** : Use `collectAsLazyPagingItems()` to convert the flow
   into a state-aware lazy paging items object.

       val productPagingData = mainViewModel.productPager.collectAsLazyPagingItems()

   The resulting `LazyPagingItems` object provides item counts and indexed
   access, enabling it to be directly consumed by the `LazyColumn` method for
   rendering the list items.
2. **Bind to `LazyColumn`** : Pass the data to a `LazyColumn` list. If you are
   migrating from [`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview) list, you might be familiar with using
   `withLoadStateHeaderAndFooter` to display loading spinners or error retry
   buttons at the top or bottom of your list.

   In Compose, you don't need a special adapter for this. You can achieve the
   exact same behavior by conditionally adding an `item {}` block before or
   after your main `items {}` block, reacting directly to the `prepend` (header)
   and `append` (footer) load states.

       LazyColumn {
           // --- HEADER (Equivalent to loadStateHeader) ---
           // Reacts to 'prepend' states when scrolling towards the top
           if (productPagingData.loadState.prepend is LoadState.Loading) {
               item {
                   Box(modifier = Modifier.fillMaxWidth(), contentAlignment =
                   Alignment.Center) {
                       CircularProgressIndicator(modifier = Modifier.padding(16.dp))
                   }
               }
           }
           if (productPagingData.loadState.prepend is LoadState.Error) {
               item {
                   ErrorHeader(onRetry = { productPagingData.retry() })
               }
           }

           // --- MAIN LIST ITEMS ---
           items(count = productPagingData.itemCount) { index ->
               val product = productPagingData[index]
               if (product != null) {
                   UserPagingListItem(product = product)
               }
           }

           // --- FOOTER (Equivalent to loadStateFooter) ---
           // Reacts to 'append' states when scrolling towards the bottom
           if (productPagingData.loadState.append is LoadState.Loading) {
               item {
                   Box(modifier = Modifier.fillMaxWidth(), contentAlignment =
                   Alignment.Center) {
                       CircularProgressIndicator(modifier = Modifier.padding(16.dp))
                   }
               }
           }
           if (productPagingData.loadState.append is LoadState.Error) {
               item {
                  ErrorFooter(onRetry = { productPagingData.retry() })
               }
           }
       }

For more information about how Compose's features let you effectively display
collections of items, see [Lists and grids](https://developer.android.com/develop/ui/compose/lists).

## Handle load states

The `PagingData` object integrates loading state information. You can use this
to show loading spinners or error messages for different states (`refresh`,
`append`, or `prepend`).

To prevent unnecessary recompositions and ensure the UI only reacts to
meaningful transitions in the loading lifecycle, you should filter your state
observations. Because `loadState` updates frequently with internal changes,
reading it directly for complex state changes can cause stutters.

You can optimize this by using `snapshotFlow` to observe the state and applying
Flow operators like the `distinctUntilChangedBy` property. This is particularly
useful when displaying empty states or triggering side-effects, such as an error
Snackbar:

    val snackbarHostState = remember { SnackbarHostState() }

    LaunchedEffect(productPagingData.loadState) {
        snapshotFlow { productPagingData.loadState }
            // Filter out updates that don't change the refresh state
            .distinctUntilChangedBy { it.refresh }
            // Only react when the state is an Error
            .filter { it.refresh is LoadState.Error }
            .collect { loadState ->
                val error = (loadState.refresh as LoadState.Error).error
                snackbarHostState.showSnackbar(
                    message = "Data failed to load: ${error.localizedMessage}",
                    actionLabel = "Retry"
                )
            }
    }

When checking the refresh state to show a full-screen loading spinner, use
`derivedStateOf` to prevent unnecessary recompositions.

Furthermore, if you are using a [`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator) (such as in the Room
database implementation earlier), explicitly inspect the loading state of the
underlying data source (`loadState.source.refresh`) rather than the convenience
`loadState.refresh` property. The convenience property might report that the
network fetch is complete before the database has finished adding the new items
to the UI. Checking the `source` guarantees the UI is completely in sync with
the local database, preventing the loader from disappearing too early.

    // Safely check the refresh state for a full-screen spinner
    // without triggering unnecessary recompositions
    val isRefreshing by remember {
        derivedStateOf { productPagingData.loadState.source.refresh is LoadState.Loading }
    }
    if (isRefreshing) {
        // Show UI for refreshing (for example, full screen spinner)
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            CircularProgressIndicator()
        }
    }

You can also check for `LoadState.Error` to display retry buttons or error
messages to the user. We recommend using `LoadState.Error` because it exposes
the underlying exception and enables the built-in `retry()` function for user
recovery.

    if (refreshState is LoadState.Error) {
       val e = refreshState as LoadState.Error

       // This composable should ideally replace the entire list if the initial load
       // fails.
       ErrorScreen(
           message = "Data failed to load: ${e.error.localizedMessage}",
           onClickRetry = { productPagingData.retry() }
       )
    }

## Test your implementation

Testing your pagination implementation ensures that data loads correctly,
transformations are applied as expected, and the UI reacts properly to state
changes. The Paging 3 library provides a dedicated testing artifact
(`androidx.paging:paging-testing`) to simplify this process.

First, add the testing dependency to your `build.gradle` file:

    testImplementation("androidx.paging:paging-testing:$paging_version")

## Test the data layer

To test your [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) directly, use `TestPager`. This utility
handles the underlying mechanics of Paging 3 and lets you independently verify
edge cases, such as initial loads (Refresh), appending, or prepending data
without needing a full `Pager` setup.

    @Test
    fun testProductPagingSource() = runTest {
        val pagingSource = ProductPagingSource(mockApiService)

        // Create a TestPager to interact with the PagingSource
        val pager = TestPager(
            config = PAGING_CONFIG,
            pagingSource = pagingSource
        )

        // Trigger an initial load
        val result = pager.refresh() as PagingSource.LoadResult.Page

        // Assert the data size and edge cases like next/prev keys
        assertEquals(50, result.data.size)
        assertNull(result.prevKey)
        assertEquals(50, result.nextKey)
    }

## Test `ViewModel` logic and transformations

If your `ViewModel` applies data transformations (such as `.map` operations) to
the `PagingData` flow, you can test this logic using `asPagingSourceFactory` and
`asSnapshot()`.

The `asPagingSourceFactory` extension converts a static list into a
`PagingSource`, making it simpler to mock the repository layer. The
`asSnapshot()` extension collects the `PagingData` stream into a standard Kotlin
`List`, letting you run standard assertions on the transformed data.

    @Test
    fun testViewModelTransformations() = runTest {
        // 1. Mock your initial data using asPagingSourceFactory
        val mockProducts = listOf(Product(1, "A"), Product(2, "B"))
        val pagingSourceFactory = mockProducts.asPagingSourceFactory()

        // 2. Pass the mocked factory to your ViewModel or Pager
        val pager = Pager(
            config = PagingConfig(pageSize = 10),
            pagingSourceFactory = pagingSourceFactory
        )

        // 3. Apply your ViewModel transformations (for example, mapping to a UI
        //    model)
        val transformedFlow = pager.flow.map { pagingData ->
            pagingData.map { product -> product.title.uppercase() }
        }

        // 4. Extract the data as a List using asSnapshot()
        val snapshot: List<String> = transformedFlow.asSnapshot(this)

        // 5. Verify the transformation
        assertEquals(listOf("A", "B"), snapshot)
    }

## UI tests to verify states and recompositions

When testing the UI, verify that your Compose components render the data
correctly and react to load states appropriately. You can pass static
`PagingData` using `PagingData.from()` and `flowOf()` to simulate data streams.
Additionally, you can use a `SideEffect` to track recomposition counts during
your tests to ensure your Compose components aren't recomposing unnecessarily.

The following example demonstrates how to simulate a loading state, transition
to a loaded state, and verify both the UI nodes and the recomposition count:

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun testProductList_loadingAndDataStates() {
        val context = InstrumentationRegistry.getInstrumentation().targetContext

        // Create a MutableStateFlow to emit different PagingData states over time
        val pagingDataFlow = MutableStateFlow(PagingData.empty<Product>())
        var recompositionCount = 0

        composeTestRule.setContent {
            val lazyPagingItems = pagingDataFlow.collectAsLazyPagingItems()

            // Track recompositions of this composable
            SideEffect { recompositionCount++ }

            ProductListScreen(lazyPagingItems = lazyPagingItems)
        }

        // 1. Simulate initial loading state
        pagingDataFlow.value = PagingData.empty(
            sourceLoadStates = LoadStates(
                refresh = LoadState.Loading,
                prepend = LoadState.NotLoading(endOfPaginationReached = false),
                append = LoadState.NotLoading(endOfPaginationReached = false)
            )
        )

        // Verify that the loading indicator is displayed
        composeTestRule.onNodeWithTag("LoadingSpinner").assertIsDisplayed()

        // 2. Simulate data loaded state
        val mockItems = listOf(
            Product(id = 1, title = context.getString(R.string.product_a_title)),
            Product(id = 2, title = context.getString(R.string.product_b_title))
        )

        pagingDataFlow.value = PagingData.from(
            data = mockItems,
            sourceLoadStates = LoadStates(
                refresh = LoadState.NotLoading(endOfPaginationReached = false),
                prepend = LoadState.NotLoading(endOfPaginationReached = false),
                append = LoadState.NotLoading(endOfPaginationReached = false)
            )
        )

        // Wait for the UI to settle and verify the items are displayed
        composeTestRule.waitForIdle()
        composeTestRule.onNodeWithText(context.getString(R.string.product_a_title)).assertIsDisplayed()
        composeTestRule.onNodeWithText(context.getString(R.string.product_b_title)).assertIsDisplayed()

        // 3. Verify recomposition counts
        // Assert that recompositions are within expected limits (for example,
        // initial composition + updating to load state + updating to data state)
        assert(recompositionCount <= 3) {
            "Expected less than or equal to 3 recompositions, but got $recompositionCount"
        }
    }