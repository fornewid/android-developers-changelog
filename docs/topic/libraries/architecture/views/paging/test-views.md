---
title: https://developer.android.com/topic/libraries/architecture/views/paging/test-views
url: https://developer.android.com/topic/libraries/architecture/views/paging/test-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/topic/libraries/architecture/paging/test)

Implementing the Paging library in your app should be paired with a robust
testing strategy. You should test data loading components such as
[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) and [`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator) to ensure that they work as
expected. You should also write end-to-end tests to verify that all of the
components in your Paging implementation work correctly together without
unexpected side effects.

This guide explains how to test the Paging library in the [data layer](https://developer.android.com/topic/architecture#data-layer) of
your app as well as how to write end-to-end tests for your entire Paging
implementation.

## Data layer tests

Write unit tests for the components in your data layer to ensure that they load
the data from your data sources appropriately. Provide [fake](https://developer.android.com/training/testing/fundamentals/test-doubles) versions of
dependencies to verify that the components being tested function correctly in
isolation. One of the components that you need to test in the repository layer
is the `RemoteMediator`.

### `RemoteMediator` tests

The goal of the `RemoteMediator` unit tests is to verify that the `load()`
function returns the correct [`MediatorResult`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator.MediatorResult). Tests for side effects, such
as data being inserted into the database, are better suited for [integration
tests](https://developer.android.com/topic/libraries/architecture/views/paging/test-views#end-to-end-tests).

The first step is to determine what dependencies your `RemoteMediator`
implementation needs. The following example demonstrates a `RemoteMediator`
implementation that requires a Room database, a Retrofit interface, and a search
string:

### Java (RxJava)

    public class PageKeyedRemoteMediator
      extends RxRemoteMediator<Integer, RedditPost> {

      @NonNull
      private RedditDb db;
      @NonNull
      private RedditPostDao postDao;
      @NonNull
      private SubredditRemoteKeyDao remoteKeyDao;
      @NonNull
      private RedditApi redditApi;
      @NonNull
      private String subredditName;

      public PageKeyedRemoteMediator(
        @NonNull RedditDb db,
        @NonNull RedditApi redditApi,
        @NonNull String subredditName
        ) {
          this.db = db;
          this.postDao = db.posts();
          this.remoteKeyDao = db.remoteKeys();
          this.redditApi = redditApi;
          this.subredditName = subredditName;
          ...
        }
      }

### Java (Guava/LiveData)

    public class PageKeyedRemoteMediator
      extends ListenableFutureRemoteMediator<Integer, RedditPost> {

      @NonNull
      private RedditDb db;
      @NonNull
      private RedditPostDao postDao;
      @NonNull
      private SubredditRemoteKeyDao remoteKeyDao;
      @NonNull
      private RedditApi redditApi;
      @NonNull
      private String subredditName;
      @NonNull
      private Executor bgExecutor;

      public PageKeyedRemoteMediator(
        @NonNull RedditDb db,
        @NonNull RedditApi redditApi,
        @NonNull String subredditName,
        @NonNull Executor bgExecutor
      ) {
        this.db = db;
        this.postDao = db.posts();
        this.remoteKeyDao = db.remoteKeys();
        this.redditApi = redditApi;
        this.subredditName = subredditName;
        this.bgExecutor = bgExecutor;
        ...
      }
    }

You can provide the Retrofit interface and the search string as demonstrated in
the [PagingSource tests](https://developer.android.com/topic/libraries/architecture/paging/test#pagingsource-tests) section of [Test your Paging implementation](https://developer.android.com/topic/libraries/architecture/paging/test).
Providing a mock version of the Room database is very involved, so it can be
easier to provide an [in-memory implementation](https://developer.android.com/training/data-storage/room/testing-db#android) of the database instead of a
full mock version. Because creating a Room database requires a [`Context`](https://developer.android.com/reference/android/content/Context)
object, you must place this `RemoteMediator` test in the `androidTest` directory
and execute it with the AndroidJUnit4 test runner so that it has access to a
test application context. For more information about instrumented tests, see
[Build instrumented unit tests](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests).

Define tear-down functions to ensure that state does not leak between test
functions. This ensures consistent results between test runs.

### Java (RxJava)

    @RunWith(AndroidJUnit4.class)
    public class PageKeyedRemoteMediatorTest {
      static PostFactory postFactory = new PostFactory();
      static List<RedditPost> mockPosts = new ArrayList<>();
      static MockRedditApi mockApi = new MockRedditApi();
      private RedditDb mockDb = RedditDb.Companion.create(
        ApplicationProvider.getApplicationContext(),
        true
      );

      static {
        for (int i=0; i<3; i++) {
          RedditPost post = postFactory.createRedditPost(DEFAULT_SUBREDDIT);
          mockPosts.add(post);
        }
      }

      @After
      public void tearDown() {
        mockDb.clearAllTables();
        // Clear the failure message after each test run.
        mockApi.setFailureMsg(null);
        // Clear out posts after each test run.
        mockApi.clearPosts();
      }
    }

### Java (Guava/LiveData)

    @RunWith(AndroidJUnit4.class)
    public class PageKeyedRemoteMediatorTest {
      static PostFactory postFactory = new PostFactory();
      static List<RedditPost> mockPosts = new ArrayList<>();
      static MockRedditApi mockApi = new MockRedditApi();

      private RedditDb mockDb = RedditDb.Companion.create(
        ApplicationProvider.getApplicationContext(),
        true
      );

      static {
        for (int i=0; i<3; i++) {
          RedditPost post = postFactory.createRedditPost(DEFAULT_SUBREDDIT);
          mockPosts.add(post);
        }
      }

      @After
      public void tearDown() {
        mockDb.clearAllTables();
        // Clear the failure message after each test run.
        mockApi.setFailureMsg(null);
        // Clear out posts after each test run.
        mockApi.clearPosts();
      }
    }

The next step is to test the `load()` function. In this example, there are three
cases to test:

- The first case is when `mockApi` returns valid data. The `load()` function should return `MediatorResult.Success`, and the `endOfPaginationReached` property should be `false`.
- The second case is when `mockApi` returns a successful response, but the returned data is empty. The `load` function should return `MediatorResult.Success`, and the `endOfPaginationReached` property should be `true`.
- The third case is when `mockApi` throws an exception when fetching the data. The `load()` function should return `MediatorResult.Error`.

Follow these steps to test the first case:

1. Set up the `mockApi` with the post data to return.
2. Initialize the `RemoteMediator` object.
3. Test the `load` function.

### Java (RxJava)

    @Test
    public void refreshLoadReturnsSuccessResultWhenMoreDataIsPresent()
      throws InterruptedException {

      // Add mock results for the API to return.
      for (RedditPost post: mockPosts) {
        mockApi.addPost(post);
      }

      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );
      remoteMediator.loadSingle(LoadType.REFRESH, pagingState)
        .test()
        .await()
        .assertValueCount(1)
        .assertValue(value -> value instanceof RemoteMediator.MediatorResult.Success &&
          ((RemoteMediator.MediatorResult.Success) value).endOfPaginationReached() == false);
    }

### Java (Guava/LiveData)

    @Test
    public void refreshLoadReturnsSuccessResultWhenMoreDataIsPresent()
      throws InterruptedException, ExecutionException {

      // Add mock results for the API to return.
      for (RedditPost post: mockPosts) {
        mockApi.addPost(post);
      }

      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT,
        new CurrentThreadExecutor()
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );

      RemoteMediator.MediatorResult result =
        remoteMediator.loadFuture(LoadType.REFRESH, pagingState).get();

      assertThat(result, instanceOf(RemoteMediator.MediatorResult.Success.class));
      assertFalse(((RemoteMediator.MediatorResult.Success) result).endOfPaginationReached());
    }

The second test requires the `mockApi` to return an empty result. Because you
clear the data from the `mockApi` after each test run, it will return an empty
result by default.

### Java (RxJava)

    @Test
    public void refreshLoadSuccessAndEndOfPaginationWhenNoMoreData()
      throws InterruptedException() {

      // To test endOfPaginationReached, don't set up the mockApi to return post
      // data here.
      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );
      remoteMediator.loadSingle(LoadType.REFRESH, pagingState)
        .test()
        .await()
        .assertValueCount(1)
        .assertValue(value -> value instanceof RemoteMediator.MediatorResult.Success &&
          ((RemoteMediator.MediatorResult.Success) value).endOfPaginationReached() == true);
    }

### Java (Guava/LiveData)

    @Test
    public void refreshLoadSuccessAndEndOfPaginationWhenNoMoreData()
      throws InterruptedException, ExecutionException {

      // To test endOfPaginationReached, don't set up the mockApi to return post
      // data here.
      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT,
        new CurrentThreadExecutor()
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );

      RemoteMediator.MediatorResult result =
        remoteMediator.loadFuture(LoadType.REFRESH, pagingState).get();

      assertThat(result, instanceOf(RemoteMediator.MediatorResult.Success.class));
      assertTrue(((RemoteMediator.MediatorResult.Success) result).endOfPaginationReached());
    }

The final test requires the `mockApi` to throw an exception so that the test can
verify that the `load()` function correctly returns `MediatorResult.Error`.

### Java (RxJava)

    @Test
    public void refreshLoadReturnsErrorResultWhenErrorOccurs()
      throws InterruptedException {

      // Set up failure message to throw exception from the mock API.
      mockApi.setFailureMsg("Throw test failure");
      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );
      remoteMediator.loadSingle(LoadType.REFRESH, pagingState)
        .test()
        .await()
        .assertValueCount(1)
        .assertValue(value -> value instanceof RemoteMediator.MediatorResult.Error);
    }

### Java (Guava/LiveData)

    @Test
    public void refreshLoadReturnsErrorResultWhenErrorOccurs()
      throws InterruptedException, ExecutionException {

      // Set up failure message to throw exception from the mock API.
      mockApi.setFailureMsg("Throw test failure");
      PageKeyedRemoteMediator remoteMediator = new PageKeyedRemoteMediator(
        mockDb,
        mockApi,
        SubRedditViewModel.DEFAULT_SUBREDDIT,
        new CurrentThreadExecutor()
      );
      PagingState<Integer, RedditPost> pagingState = new PagingState<>(
        new ArrayList(),
        null,
        new PagingConfig(10),
        10
      );
      RemoteMediator.MediatorResult result =
        remoteMediator.loadFuture(LoadType.REFRESH, pagingState).get();

      assertThat(result, instanceOf(RemoteMediator.MediatorResult.Error.class));
    }

## End-to-end tests

Unit tests provide assurance that individual Paging components work in
isolation, but end-to-end tests provide more confidence that the application
works as a whole. These tests will still need some mock dependencies, but
generally they will cover most of your app code.

The example in this section uses a mock API dependency to avoid using the
network in tests. The mock API is configured to return a consistent set of test
data, resulting in repeatable tests. Decide which dependencies to swap out for
mock implementations based on what each dependency does, how consistent its
output is, and how much fidelity you need from your tests.

Write your code in a way that lets you easily swap in mock versions of your
dependencies. The following example uses a basic [service locator
implementation](https://developer.android.com/training/dependency-injection#di-alternatives) to provide and change dependencies as needed. In larger
apps, using a dependency injection library like [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) can help manage
more-complex dependency graphs.

### Kotlin

    class RedditActivityTest {

      companion object {
        private const val TEST_SUBREDDIT = "test"
      }

      private val postFactory = PostFactory()
      private val mockApi = MockRedditApi().apply {
        addPost(postFactory.createRedditPost(DEFAULT_SUBREDDIT))
        addPost(postFactory.createRedditPost(TEST_SUBREDDIT))
        addPost(postFactory.createRedditPost(TEST_SUBREDDIT))
      }

      @Before
      fun init() {
        val app = ApplicationProvider.getApplicationContext<Application>()
        // Use a controlled service locator with a mock API.
        ServiceLocator.swap(
          object : DefaultServiceLocator(app = app, useInMemoryDb = true) {
            override fun getRedditApi(): RedditApi = mockApi
          }
        )
      }
    }

### Java (RxJava)

    public class RedditActivityTest {

      public static final String TEST_SUBREDDIT = "test";

      private static PostFactory postFactory = new PostFactory();
      private static MockRedditApi mockApi = new MockRedditApi();

      static {
        mockApi.addPost(postFactory.createRedditPost(DEFAULT_SUBREDDIT));
        mockApi.addPost(postFactory.createRedditPost(TEST_SUBREDDIT));
        mockApi.addPost(postFactory.createRedditPost(TEST_SUBREDDIT));
      }

      @Before
      public void setup() {
        Application app = ApplicationProvider.getApplicationContext();
        // Use a controlled service locator with a mock API.
        ServiceLocator.Companion.swap(
          new DefaultServiceLocator(app, true) {
            @NotNull
            @Override
            public RedditApi getRedditApi() {
              return mockApi;
            }
          }
        );
      }
    }

### Java (Guava/LiveData)

    public class RedditActivityTest {

      public static final String TEST_SUBREDDIT = "test";

      private static PostFactory postFactory = new PostFactory();
      private static MockRedditApi mockApi = new MockRedditApi();

      static {
        mockApi.addPost(postFactory.createRedditPost(DEFAULT_SUBREDDIT));
        mockApi.addPost(postFactory.createRedditPost(TEST_SUBREDDIT));
        mockApi.addPost(postFactory.createRedditPost(TEST_SUBREDDIT));
      }

      @Before
      public void setup() {
        Application app = ApplicationProvider.getApplicationContext();
        // Use a controlled service locator with a mock API.
        ServiceLocator.Companion.swap(
          new DefaultServiceLocator(app, true) {
            @NotNull
            @Override
            public RedditApi getRedditApi() {
              return mockApi;
            }
          }
        );
      }
    }

After you set up the test structure, the next step is to verify that the data
returned by the `Pager` implementation is correct. One test should ensure that
the `Pager` object loads the default data when the page first loads, and another
test should verify that the `Pager` object correctly loads additional data based
on user input.

In the following example, the test verifies that the `Pager` object updates the
`RecyclerView.Adapter` with the correct number of items returned from the API
when the user enters a different subreddit to search.

### Kotlin

    @Test
    fun loadsTheDefaultResults() {
        ActivityScenario.launch(RedditActivity::class.java)

        onView(withId(R.id.list)).check { view, noViewFoundException ->
            if (noViewFoundException != null) {
                throw noViewFoundException
            }

            val recyclerView = view as RecyclerView
            assertEquals(1, recyclerView.adapter?.itemCount)
        }
    }

    @Test
    // Verify that the default data is swapped out when the user searches for a
    // different subreddit.
    fun loadsTheTestResultsWhenSearchingForSubreddit() {
      ActivityScenario.launch(RedditActivity::class.java )

      onView(withId(R.id.list)).check { view, noViewFoundException ->
        if (noViewFoundException != null) {
          throw noViewFoundException
        }

        val recyclerView = view as RecyclerView
        // Verify that it loads the default data first.
        assertEquals(1, recyclerView.adapter?.itemCount)
      }

      // Search for test subreddit instead of default to trigger new data load.
      onView(withId(R.id.input)).perform(
        replaceText(TEST_SUBREDDIT),
        pressKey(KeyEvent.KEYCODE_ENTER)
      )

      onView(withId(R.id.list)).check { view, noViewFoundException ->
        if (noViewFoundException != null) {
          throw noViewFoundException
        }

        val recyclerView = view as RecyclerView
        assertEquals(2, recyclerView.adapter?.itemCount)
      }
    }

### Java (RxJava)

    @Test
    public void loadsTheDefaultResults() {
      ActivityScenario.launch(RedditActivity.class);

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        assertEquals(1, recyclerView.getAdapter().getItemCount());
      });
    }

    @Test
    // Verify that the default data is swapped out when the user searches for a
    // different subreddit.
    public void loadsTheTestResultsWhenSearchingForSubreddit() {
      ActivityScenario.launch(RedditActivity.class);

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        // Verify that it loads the default data first.
        assertEquals(1, recyclerView.getAdapter().getItemCount());
      });

      // Search for test subreddit instead of default to trigger new data load.
      onView(withId(R.id.input)).perform(
        replaceText(TEST_SUBREDDIT),
        pressKey(KeyEvent.KEYCODE_ENTER)
      );

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        assertEquals(2, recyclerView.getAdapter().getItemCount());
      });
    }

### Java (Guava/LiveData)

    @Test
    public void loadsTheDefaultResults() {
      ActivityScenario.launch(RedditActivity.class);

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        assertEquals(1, recyclerView.getAdapter().getItemCount());
      });
    }

    @Test
    // Verify that the default data is swapped out when the user searches for a
    // different subreddit.
    public void loadsTheTestResultsWhenSearchingForSubreddit() {
      ActivityScenario.launch(RedditActivity.class);

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        // Verify that it loads the default data first.
        assertEquals(1, recyclerView.getAdapter().getItemCount());
      });

      // Search for test subreddit instead of default to trigger new data load.
      onView(withId(R.id.input)).perform(
        replaceText(TEST_SUBREDDIT),
        pressKey(KeyEvent.KEYCODE_ENTER)
      );

      onView(withId(R.id.list)).check((view, noViewFoundException) -> {
        if (noViewFoundException != null) {
          throw noViewFoundException;
        }

        RecyclerView recyclerView = (RecyclerView) view;
        assertEquals(2, recyclerView.getAdapter().getItemCount());
      });
    }

Instrumented tests should verify that the data displays correctly in the UI. Do
this either by verifying that the correct number of items exists in the
`RecyclerView.Adapter`, or by iterating through the individual row views and
verifying that the data is formatted correctly.