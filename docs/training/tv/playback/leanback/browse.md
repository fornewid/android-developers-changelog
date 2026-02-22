---
title: https://developer.android.com/training/tv/playback/leanback/browse
url: https://developer.android.com/training/tv/playback/leanback/browse
source: md.txt
---

Build better with Compose  
Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.  
[Compose for TV →](https://developer.android.com/training/tv/playback/compose)  
![](https://developer.android.com/static/images/android-compose-tv-logo.png)
| **Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
| Android TV OS](https://developer.android.com/training/tv/playback/compose) instead.


A media app that runs on a TV needs to let users browse its content offerings, make a
selection, and start playing content. The content browsing experience
must be simple and intuitive as well as visually pleasing and engaging.


This guide discusses how to use the classes provided by the deprecated
[androidx.leanback library](https://developer.android.com/training/tv/get-started/create#leanback) to implement a user interface for browsing music or videos from your
app's media catalog.


**Note:** The implementation example shown here uses
[BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment)
rather than the deprecated [BrowseFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseFragment)
class. `BrowseSupportFragment` extends the [AndroidX](https://developer.android.com/jetpack/androidx)
[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment) class,
helping to ensure consistent behavior across devices and Android versions.
![App main screen](https://developer.android.com/static/images/tv/app-browse.png)

**Figure 1.**
The Leanback sample app's browse fragment displays video catalog data.

## Create a media browse layout


The [BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment)
class in the Leanback UI toolkit
lets you create a primary layout for browsing categories and rows of media items with a
minimum of code. The following example shows how to create a layout that contains a
`BrowseSupportFragment` object:  

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/main_frame"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <fragment
        android:name="com.example.android.tvleanback.ui.MainFragment"
        android:id="@+id/main_browse_fragment"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</FrameLayout>
```

The application's main activity sets this view, as shown in the following example:  

### Kotlin

```kotlin
class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)
    }
...
```

### Java

```java
public class MainActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }
...
```

The `BrowseSupportFragment` methods populate the view with the
video data and UI elements and set layout parameters such as the icon and title and
whether category headers are enabled.
For more information about setting up UI elements, see the [Set UI
elements](https://developer.android.com/training/tv/playback/leanback/browse#set-ui) section. For more information about hiding the headers, see the [Hide or disable headers](https://developer.android.com/training/tv/playback/leanback/browse#hide-heads) section.

The application's subclass that implements the `BrowseSupportFragment`
methods also sets up event listeners for user actions on the UI elements and prepares
the background manager, as shown in the following example:  

### Kotlin

```kotlin
class MainFragment : BrowseSupportFragment(),
        LoaderManager.LoaderCallbacks<HashMap<String, List<Movie>>> {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        loadVideoData()
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        prepareBackgroundManager()
        setupUIElements()
        setupEventListeners()
    }
    ...
    private fun prepareBackgroundManager() {
        backgroundManager = BackgroundManager.getInstance(activity).apply {
            attach(activity?.window)
        }
        defaultBackground = resources.getDrawable(R.drawable.default_background)
        metrics = DisplayMetrics()
        activity?.windowManager?.defaultDisplay?.getMetrics(metrics)
    }

    private fun setupUIElements() {
        badgeDrawable = resources.getDrawable(R.drawable.videos_by_google_banner)
        // Badge, when set, takes precedent over title
        title = getString(R.string.browse_title)
        headersState = BrowseSupportFragment.HEADERS_ENABLED
        isHeadersTransitionOnBackEnabled = true
        // Set header background color
        brandColor = ContextCompat.getColor(requireContext(), R.color.fastlane_background)

        // Set search icon color
        searchAffordanceColor = ContextCompat.getColor(requireContext(), R.color.search_opaque)
    }

    private fun loadVideoData() {
        VideoProvider.setContext(activity)
        videosUrl = getString(R.string.catalog_url)
        loaderManager.initLoader(0, null, this)
    }

    private fun setupEventListeners() {
        setOnSearchClickedListener {
            Intent(activity, SearchActivity::class.java).also { intent ->
                startActivity(intent)
            }
        }

        onItemViewClickedListener = ItemViewClickedListener()
        onItemViewSelectedListener = ItemViewSelectedListener()
    }
    ...
```

### Java

```java
public class MainFragment extends BrowseSupportFragment implements
        LoaderManager.LoaderCallbacks<HashMap<String, List<Movie>>> {
}
...
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        loadVideoData();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        prepareBackgroundManager();
        setupUIElements();
        setupEventListeners();
    }
...
    private void prepareBackgroundManager() {
        backgroundManager = BackgroundManager.getInstance(getActivity());
        backgroundManager.attach(getActivity().getWindow());
        defaultBackground = getResources()
            .getDrawable(R.drawable.default_background);
        metrics = new DisplayMetrics();
        getActivity().getWindowManager().getDefaultDisplay().getMetrics(metrics);
    }

    private void setupUIElements() {
        setBadgeDrawable(getActivity().getResources()
            .getDrawable(R.drawable.videos_by_google_banner));
        // Badge, when set, takes precedent over title
        setTitle(getString(R.string.browse_title));
        setHeadersState(HEADERS_ENABLED);
        setHeadersTransitionOnBackEnabled(true);
        // Set header background color
        setBrandColor(ContextCompat.getColor(requireContext(), R.color.fastlane_background));
        // Set search icon color
        setSearchAffordanceColor(ContextCompat.getColor(requireContext(), R.color.search_opaque));
    }

    private void loadVideoData() {
        VideoProvider.setContext(getActivity());
        videosUrl = getString(R.string.catalog_url);
        getLoaderManager().initLoader(0, null, this);
    }

    private void setupEventListeners() {
        setOnSearchClickedListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getActivity(), SearchActivity.class);
                startActivity(intent);
            }
        });

        setOnItemViewClickedListener(new ItemViewClickedListener());
        setOnItemViewSelectedListener(new ItemViewSelectedListener());
    }
...
```

### Set UI elements

In the previous sample, the private method `setupUIElements()` calls several
[BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment)
methods to style the media catalog browser:

- [setBadgeDrawable()](https://developer.android.com/reference/androidx/leanback/app/BrandedFragment#setBadgeDrawable(android.graphics.drawable.Drawable)) places the specified drawable resource in the upper-right corner of the browse fragment, as shown in figures 1 and 2. This method replaces the title string with the drawable resource, if `setTitle()` is also called. The drawable resource must be 52 dp tall.
- [setTitle()](https://developer.android.com/reference/androidx/leanback/app/BrandedFragment#setTitle(java.lang.CharSequence)) sets the title string in the upper-right corner of the browse fragment, unless `setBadgeDrawable()` is called.
- [setHeadersState()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setHeadersState(int)) and [setHeadersTransitionOnBackEnabled()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setHeadersTransitionOnBackEnabled(boolean)) hide or disable the headers. See the [Hide or disable headers](https://developer.android.com/training/tv/playback/leanback/browse#hide-heads) section for more information.
- [setBrandColor()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setBrandColor(int)) sets the background color for UI elements in the browse fragment, specifically the header section background color, with the specified color value.
- [setSearchAffordanceColor()](https://developer.android.com/reference/androidx/leanback/app/BrandedFragment#setSearchAffordanceColor(int)) sets the color of the search icon with the specified color value. The search icon appears in the upper-left corner of the browse fragment, as shown in figures 1 and 2.

## Customize the header views

The browse fragment shown in figure 1 displays the video category names,
which are the row headers in the video database, in text views. You can also customize the
header to include additional views in a more complex layout. The following sections show how to
include an image view that displays an icon next to the category name, as shown in figure 2.
![App main screen](https://developer.android.com/static/images/tv/custom-head.png)

**Figure 2.** The row headers in the browse fragment with both an icon
and a text label.

The layout for the row header is defined as follows:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="horizontal"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:id="@+id/header_icon"
        android:layout_width="32dp"
        android:layout_height="32dp" />
    <TextView
        android:id="@+id/header_label"
        android:layout_marginTop="6dp"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>
```

Use a [Presenter](https://developer.android.com/reference/androidx/leanback/widget/Presenter) and implement the
abstract methods to create, bind, and unbind the view holder. The following
example shows how to bind the viewholder with two views, an
[ImageView](https://developer.android.com/reference/android/widget/ImageView) and a [TextView](https://developer.android.com/reference/android/widget/TextView).  

### Kotlin

```kotlin
class IconHeaderItemPresenter : Presenter() {

    override fun onCreateViewHolder(viewGroup: ViewGroup): Presenter.ViewHolder {
        val view = LayoutInflater.from(viewGroup.context).run {
            inflate(R.layout.icon_header_item, null)
        }

        return Presenter.ViewHolder(view)
    }


    override fun onBindViewHolder(viewHolder: Presenter.ViewHolder, o: Any) {
        val headerItem = (o as ListRow).headerItem
        val rootView = viewHolder.view

        rootView.findViewById<ImageView>(R.id.header_icon).apply {
            rootView.resources.getDrawable(R.drawable.ic_action_video, null).also { icon ->
                setImageDrawable(icon)
            }
        }

        rootView.findViewById<TextView>(R.id.header_label).apply {
            text = headerItem.name
        }
    }

    override fun onUnbindViewHolder(viewHolder: Presenter.ViewHolder) {
        // no-op
    }
}
```

### Java

```java
public class IconHeaderItemPresenter extends Presenter {
    @Override
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup) {
        LayoutInflater inflater = LayoutInflater.from(viewGroup.getContext());

        View view = inflater.inflate(R.layout.icon_header_item, null);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(ViewHolder viewHolder, Object o) {
        HeaderItem headerItem = ((ListRow) o).getHeaderItem();
        View rootView = viewHolder.view;

        ImageView iconView = (ImageView) rootView.findViewById(R.id.header_icon);
        Drawable icon = rootView.getResources().getDrawable(R.drawable.ic_action_video, null);
        iconView.setImageDrawable(icon);

        TextView label = (TextView) rootView.findViewById(R.id.header_label);
        label.setText(headerItem.getName());
    }

    @Override
    public void onUnbindViewHolder(ViewHolder viewHolder) {
    // no-op
    }
}
```

Your headers must be focusable so that the D-pad can be used to
scroll through them. There are two ways to manage this:

- Set your view to be focusable in [onBindViewHolder()](https://developer.android.com/reference/androidx/leanback/widget/RowHeaderPresenter#onBindViewHolder(androidx.leanback.widget.Presenter.ViewHolder, java.lang.Object)):  

  ### Kotlin

  ```kotlin
  override fun onBindViewHolder(viewHolder: Presenter.ViewHolder, o: Any) {
      val headerItem = (o as ListRow).headerItem
      val rootView = viewHolder.view

      rootView.focusable = View.FOCUSABLE
      // ...
  }
  ```

  ### Java

  ```java
  @Override
  public void onBindViewHolder(ViewHolder viewHolder, Object o) {
      HeaderItem headerItem = ((ListRow) o).getHeaderItem();
      View rootView = viewHolder.view;
      rootView.setFocusable(View.FOCUSABLE) // Allows the D-Pad to navigate to this header item
      // ...
  }
  ```
- Set your layout to be focusable:  

  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
     ...
     android:focusable="true">
  ```

Finally, in the [BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment) implementation that displays the
catalog browser, use the [setHeaderPresenterSelector()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setHeaderPresenterSelector(androidx.leanback.widget.PresenterSelector))
method to set the presenter for the row header, as shown in the following example.  

### Kotlin

```kotlin
setHeaderPresenterSelector(object : PresenterSelector() {
    override fun getPresenter(o: Any): Presenter {
        return IconHeaderItemPresenter()
    }
})
```

### Java

```java
setHeaderPresenterSelector(new PresenterSelector() {
    @Override
    public Presenter getPresenter(Object o) {
        return new IconHeaderItemPresenter();
    }
});
```

For a complete example, see the
[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback)
.

### Hide or disable headers

Sometimes you don't want the row headers to appear, such as when there aren't enough
categories to require a scrollable list. Call the [BrowseSupportFragment.setHeadersState()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setHeadersState(int))
method during the fragment's [onActivityCreated()](https://developer.android.com/reference/android/app/Fragment#onActivityCreated(android.os.Bundle))
method to hide or disable the row headers. The `setHeadersState()`
method sets the initial state of the headers in the browse fragment, given one of the following
constants as a parameter:

- [HEADERS_ENABLED](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#HEADERS_ENABLED()): when the browse fragment activity is created, headers are enabled and shown by default. The headers appear as shown in figures 1 and 2 on this page.
- [HEADERS_HIDDEN](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#HEADERS_HIDDEN()): when the browse fragment activity is created, headers are enabled and hidden by default. The header section of the screen is collapsed, as shown in [a figure](https://developer.android.com/training/tv/playback/card#collapsed) in [Provide a card view](https://developer.android.com/training/tv/playback/card). The user can select the collapsed header section to expand it.
- [HEADERS_DISABLED](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#HEADERS_DISABLED()): when the browse fragment activity is created, headers are disabled by default and are never displayed.

If either `HEADERS_ENABLED` or `HEADERS_HIDDEN` is set, you can call
[setHeadersTransitionOnBackEnabled()](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment#setHeadersTransitionOnBackEnabled(boolean))
to support moving back to the row header from a selected content item in the row. This is enabled by
default if you don't call the method. To handle the back movement yourself,
pass `false` to `setHeadersTransitionOnBackEnabled()`
and implement your own back stack handling.

## Display media lists


The [BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment)
class lets you
define and display browsable media content categories and media items from
a media catalog using adapters and presenters. Adapters let you connect
to local or online data sources that contain your media catalog information.
Adapters use presenters to create views and bind data to those views for
displaying an item on screen.


The following example code shows an implementation of a [Presenter](https://developer.android.com/reference/androidx/leanback/widget/Presenter) for displaying string data:  

### Kotlin

```kotlin
private const val TAG = "StringPresenter"

class StringPresenter : Presenter() {

    override fun onCreateViewHolder(parent: ViewGroup): Presenter.ViewHolder {
        val textView = TextView(parent.context).apply {
            isFocusable = true
            isFocusableInTouchMode = true
            background = parent.resources.getDrawable(R.drawable.text_bg)
        }
        return Presenter.ViewHolder(textView)
    }

    override fun onBindViewHolder(viewHolder: Presenter.ViewHolder, item: Any) {
        (viewHolder.view as TextView).text = item.toString()
    }

    override fun onUnbindViewHolder(viewHolder: Presenter.ViewHolder) {
        // no op
    }
}
```

### Java

```java
public class StringPresenter extends Presenter {
    private static final String TAG = "StringPresenter";

    public ViewHolder onCreateViewHolder(ViewGroup parent) {
        TextView textView = new TextView(parent.getContext());
        textView.setFocusable(true);
        textView.setFocusableInTouchMode(true);
        textView.setBackground(
                parent.getResources().getDrawable(R.drawable.text_bg));
        return new ViewHolder(textView);
    }

    public void onBindViewHolder(ViewHolder viewHolder, Object item) {
        ((TextView) viewHolder.view).setText(item.toString());
    }

    public void onUnbindViewHolder(ViewHolder viewHolder) {
        // no op
    }
}
```


Once you have constructed a presenter class for your media items, you can build
an adapter and attach it to the `BrowseSupportFragment`
to display those items on screen for browsing by the user. The following example
code demonstrates how to construct an adapter to display categories and items
in those categories using the `StringPresenter` class shown in the
previous code example:  

### Kotlin

```kotlin
private const val NUM_ROWS = 4
...
private lateinit var rowsAdapter: ArrayObjectAdapter

override fun onCreate(savedInstanceState: Bundle?) {
    ...
    buildRowsAdapter()
}

private fun buildRowsAdapter() {
    rowsAdapter = ArrayObjectAdapter(ListRowPresenter())
    for (i in 0 until NUM_ROWS) {
        val listRowAdapter = ArrayObjectAdapter(StringPresenter()).apply {
            add("Media Item 1")
            add("Media Item 2")
            add("Media Item 3")
        }
        HeaderItem(i.toLong(), "Category $i").also { header ->
            rowsAdapter.add(ListRow(header, listRowAdapter))
        }
    }
    browseSupportFragment.adapter = rowsAdapter
}
```

### Java

```java
private ArrayObjectAdapter rowsAdapter;
private static final int NUM_ROWS = 4;

@Override
protected void onCreate(Bundle savedInstanceState) {
    ...
    buildRowsAdapter();
}

private void buildRowsAdapter() {
    rowsAdapter = new ArrayObjectAdapter(new ListRowPresenter());

    for (int i = 0; i < NUM_ROWS; ++i) {
        ArrayObjectAdapter listRowAdapter = new ArrayObjectAdapter(
                new StringPresenter());
        listRowAdapter.add("Media Item 1");
        listRowAdapter.add("Media Item 2");
        listRowAdapter.add("Media Item 3");
        HeaderItem header = new HeaderItem(i, "Category " + i);
        rowsAdapter.add(new ListRow(header, listRowAdapter));
    }

    browseSupportFragment.setAdapter(rowsAdapter);
}
```


This example shows a static implementation of the adapters. A typical media browsing application
uses data from an online database or web service. For an example of a browsing application that
uses data retrieved from the web, see the
[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback)
.

## Update the background


To add visual interest to a media-browsing app on TV, you can update the background
image as users browse through content. This technique can make interaction with your app more
cinematic and enjoyable.


The Leanback UI toolkit provides a [BackgroundManager](https://developer.android.com/reference/androidx/leanback/app/BackgroundManager)
class for changing the background of your TV app activity. The following example shows how to
create a simple method for updating the background within your TV app activity:  

### Kotlin

```kotlin
protected fun updateBackground(drawable: Drawable) {
    BackgroundManager.getInstance(this).drawable = drawable
}
```

### Java

```java
protected void updateBackground(Drawable drawable) {
    BackgroundManager.getInstance(this).setDrawable(drawable);
}
```


Many media-browsing apps automatically update the background as the user navigates
through media listings. To do this, you can set up a selection listener to automatically
update the background based on the user's current selection. The following example shows how
to set up an [OnItemViewSelectedListener](https://developer.android.com/reference/androidx/leanback/widget/OnItemViewSelectedListener) class to
catch selection events and update the background:  

### Kotlin

```kotlin
protected fun clearBackground() {
    BackgroundManager.getInstance(this).drawable = defaultBackground
}

protected fun getDefaultItemViewSelectedListener(): OnItemViewSelectedListener =
        OnItemViewSelectedListener { _, item, _, _ ->
            if (item is Movie) {
                item.getBackdropDrawable().also { background ->
                    updateBackground(background)
                }
            } else {
                clearBackground()
            }
        }
```

### Java

```java
protected void clearBackground() {
    BackgroundManager.getInstance(this).setDrawable(defaultBackground);
}

protected OnItemViewSelectedListener getDefaultItemViewSelectedListener() {
    return new OnItemViewSelectedListener() {
        @Override
        public void onItemSelected(Presenter.ViewHolder itemViewHolder, Object item,
                RowPresenter.ViewHolder rowViewHolder, Row row) {
            if (item instanceof Movie ) {
                Drawable background = ((Movie)item).getBackdropDrawable();
                updateBackground(background);
            } else {
                clearBackground();
            }
        }
    };
}
```


**Note:** The previous implementation is a simple example for purposes of
illustration. When creating this function in your own app, run the
background update action in a separate thread for better performance. Also, if you
plan to update the background in response to users scrolling through items, add
a time to delay a background image update until the user settles on an item. This technique avoids
excessive background image updates.