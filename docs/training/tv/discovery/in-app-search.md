---
title: https://developer.android.com/training/tv/discovery/in-app-search
url: https://developer.android.com/training/tv/discovery/in-app-search
source: md.txt
---

# Search within TV apps

Users frequently have specific content in mind when using a media app on TV. If your app contains a large catalog of content, browsing for a specific title might not be the most efficient way for users to find what they are looking for. A search interface can help your users get to the content they want faster than browsing.

The[androidx.leanback library](https://developer.android.com/training/tv/get-started/create#leanback)provides a set of classes to enable a standard search interface within your app that is consistent with other search functions on TV and provides features like voice input.

This guide discusses how to provide a search interface in your app using Leanback support library classes.

## Add a search action

When you use the[BrowseFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseFragment)class for a media browsing interface, you can enable a search interface as a standard part of the user interface. The search interface is an icon that appears in the layout when you set[View.OnClickListener](https://developer.android.com/reference/android/view/View.OnClickListener)on the`BrowseFragment`object. The following sample code demonstrates this technique.  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.browse_activity)
    browseFragment = fragmentManager.findFragmentById(R.id.browse_fragment) as BrowseFragment
    browseFragment.setOnSearchClickedListener { view ->
        val intent = Intent(this@BrowseActivity, SearchActivity::class.java)
        startActivity(intent)
    }

    browseFragment.setAdapter(buildAdapter())
}
```

### Java

```java
@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.browse_activity);

    browseFragment = (BrowseFragment)
            getFragmentManager().findFragmentById(R.id.browse_fragment);

    ...

    browseFragment.setOnSearchClickedListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            Intent intent = new Intent(BrowseActivity.this, SearchActivity.class);
            startActivity(intent);
        }
    });

    browseFragment.setAdapter(buildAdapter());
}
```

**Note:** You can set the color of the search icon using the[setSearchAffordanceColor(int)](https://developer.android.com/reference/androidx/leanback/app/BrandedFragment#setSearchAffordanceColor(int))method.

## Add a search input and results

When a user selects the search icon, the system invokes a search activity using the defined intent. For your search activity, use a linear layout containing a[SearchFragment](https://developer.android.com/reference/androidx/leanback/app/SearchFragment). This fragment must also implement the[SearchFragment.SearchResultProvider](https://developer.android.com/reference/androidx/leanback/app/SearchFragment.SearchResultProvider)interface to display the results of a search.

The following code sample shows how to extend the`SearchFragment`class to provide a search interface and results:  

### Kotlin

```kotlin
class MySearchFragment : SearchFragment(), SearchFragment.SearchResultProvider {
    private val rowsAdapter = ArrayObjectAdapter(ListRowPresenter())
    private val handler = Handler()
    private val delayedLoad = SearchRunnable()

    val resultsAdapter: ObjectAdapter
    get() {
        return rowsAdapter
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setSearchResultProvider(this)
        setOnItemClickedListener(getDefaultItemClickedListener())
    }

    fun onQueryTextChange(newQuery: String): Boolean {
        rowsAdapter.clear()
        if (!TextUtils.isEmpty(newQuery)) {
            delayedLoad.setSearchQuery(newQuery)
            handler.removeCallbacks(delayedLoad)
            handler.postDelayed(delayedLoad, SEARCH_DELAY_MS)
        }
        return true
    }

    fun onQueryTextSubmit(query: String): Boolean {
        rowsAdapter.clear()
        if (!TextUtils.isEmpty(query)) {
            delayedLoad.setSearchQuery(query)
            handler.removeCallbacks(delayedLoad)
            handler.postDelayed(delayedLoad, SEARCH_DELAY_MS)
        }
        return true
    }

    companion object {
        private val SEARCH_DELAY_MS = 300
    }
}
```

### Java

```java
public class MySearchFragment extends SearchFragment
        implements SearchFragment.SearchResultProvider {

    private static final int SEARCH_DELAY_MS = 300;
    private ArrayObjectAdapter rowsAdapter;
    private Handler handler = new Handler();
    private SearchRunnable delayedLoad;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        rowsAdapter = new ArrayObjectAdapter(new ListRowPresenter());
        setSearchResultProvider(this);
        setOnItemClickedListener(getDefaultItemClickedListener());
        delayedLoad = new SearchRunnable();
    }

    @Override
    public ObjectAdapter getResultsAdapter() {
        return rowsAdapter;
    }

    @Override
    public boolean onQueryTextChange(String newQuery) {
        rowsAdapter.clear();
        if (!TextUtils.isEmpty(newQuery)) {
            delayedLoad.setSearchQuery(newQuery);
            handler.removeCallbacks(delayedLoad);
            handler.postDelayed(delayedLoad, SEARCH_DELAY_MS);
        }
        return true;
    }

    @Override
    public boolean onQueryTextSubmit(String query) {
        rowsAdapter.clear();
        if (!TextUtils.isEmpty(query)) {
            delayedLoad.setSearchQuery(query);
            handler.removeCallbacks(delayedLoad);
            handler.postDelayed(delayedLoad, SEARCH_DELAY_MS);
        }
        return true;
    }
}
```

The previous example code is meant to be used with a`SearchRunnable`class that runs the search query on a separate thread. This technique keeps potentially slow-running queries from blocking the main user interface thread.