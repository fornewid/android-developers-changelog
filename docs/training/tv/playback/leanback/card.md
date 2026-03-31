---
title: Provide a card view  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/leanback/card
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Provide a card view Stay organized with collections Save and categorize content based on your preferences.



Build better with Compose

Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.

[Compose for TV →](https://developer.android.com/training/tv/playback/compose)

![](/static/images/android-compose-tv-logo.png)

**Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
Android TV OS](/training/tv/playback/compose) instead.

This guide focuses on creating the card views for your media items and presenting them in the
browse fragment using the deprecated Leanback UI toolkit. The implementation
of the catalog browser in a browse fragment is detailed in the
[Browse Fragment guide](/training/tv/playback/leanback/browse).

The `BaseCardView`
class and subclasses display the metadata associated with a media item. The
`ImageCardView`
class used in this lesson displays an image for the content along with the media item's title.

See also the sample implementation in the deprecated
[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback)
.

![App card view](/static/images/tv/card-view.png)

**Figure 1.** The Leanback sample app image card view when selected.

## Create a card presenter

A `Presenter` generates views and binds objects to them
on demand. In the browse fragment where your app presents its content to the user, you create a
`Presenter` for the content cards and pass it to the adapter
that adds the content to the screen. In the following code, the `CardPresenter` is created
in the `onLoadFinished()`
callback of the `LoaderManager`:

### Kotlin

```
override fun onLoadFinished(loader: Loader<HashMap<String, List<Movie>>>, data: HashMap<String, List<Movie>>) {
    rowsAdapter = ArrayObjectAdapter(ListRowPresenter())
    val cardPresenter = CardPresenter()

    var i = 0L

    data.entries.forEach { entry ->
        val listRowAdapter = ArrayObjectAdapter(cardPresenter).apply {
            entry.value.forEach { movie ->
                add(movie)
            }
        }

        val header = HeaderItem(i, entry.key)
        i++
        rowsAdapter.add(ListRow(header, listRowAdapter))
    }

    val gridHeader = HeaderItem(i, getString(R.string.more_samples))

    val gridRowAdapter = ArrayObjectAdapter(GridItemPresenter()).apply {
        add(getString(R.string.grid_view))
        add(getString(R.string.error_fragment))
        add(getString(R.string.personal_settings))
    }
    rowsAdapter.add(ListRow(gridHeader, gridRowAdapter))

    adapter = rowsAdapter

    updateRecommendations()
}
```

### Java

```
@Override
public void onLoadFinished(Loader<HashMap<String, List<Movie>>> arg0,
                           HashMap<String, List<Movie>> data) {

    rowsAdapter = new ArrayObjectAdapter(new ListRowPresenter());
    CardPresenter cardPresenter = new CardPresenter();

    int i = 0;

    for (Map.Entry<String, List<Movie>> entry : data.entrySet()) {
        ArrayObjectAdapter listRowAdapter = new ArrayObjectAdapter(cardPresenter);
        List<Movie> list = entry.getValue();

        for (int j = 0; j < list.size(); j++) {
            listRowAdapter.add(list.get(j));
        }
        HeaderItem header = new HeaderItem(i, entry.getKey());
        i++;
        rowsAdapter.add(new ListRow(header, listRowAdapter));
    }

    HeaderItem gridHeader = new HeaderItem(i, getString(R.string.more_samples));

    GridItemPresenter gridPresenter = new GridItemPresenter();
    ArrayObjectAdapter gridRowAdapter = new ArrayObjectAdapter(gridPresenter);
    gridRowAdapter.add(getString(R.string.grid_view));
    gridRowAdapter.add(getString(R.string.error_fragment));
    gridRowAdapter.add(getString(R.string.personal_settings));
    rowsAdapter.add(new ListRow(gridHeader, gridRowAdapter));

    setAdapter(rowsAdapter);

    updateRecommendations();
}
```

## Create a card view

In this step, you build the card presenter with a view holder for the card view that describes
your media content items. Note that each presenter must create only one view type. If you have two
card view types, then you need two card presenters.

In the `Presenter`, implement an
`onCreateViewHolder()`
callback that creates a view holder that can be used to display a content item:

### Kotlin

```
private const val CARD_WIDTH = 313
private const val CARD_HEIGHT = 176

class CardPresenter : Presenter() {

    private lateinit var mContext: Context
    private lateinit var defaultCardImage: Drawable

    override fun onCreateViewHolder(parent: ViewGroup): Presenter.ViewHolder {
        mContext = parent.context
        defaultCardImage = mContext.resources.getDrawable(R.drawable.movie)
        ...
```

### Java

```
@Override
public class CardPresenter extends Presenter {

    private Context context;
    private static int CARD_WIDTH = 313;
    private static int CARD_HEIGHT = 176;
    private Drawable defaultCardImage;

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent) {
        context = parent.getContext();
        defaultCardImage = context.getResources().getDrawable(R.drawable.movie);
...
```

In the `onCreateViewHolder()` method,
create a card view for content items. The following sample uses an
`ImageCardView`.

When a card is selected, the default behavior expands it to a larger size. If you want to designate
a different color for the selected card, call `setSelected()`
as shown here:

### Kotlin

```
    ...
    val cardView = object : ImageCardView(context) {
        override fun setSelected(selected: Boolean) {
            val selected_background = context.resources.getColor(R.color.detail_background)
            val default_background = context.resources.getColor(R.color.default_background)
            val color = if (selected) selected_background else default_background
            findViewById<View>(R.id.info_field).setBackgroundColor(color)
            super.setSelected(selected)
        }
    }
    ...
```

### Java

```
...
    ImageCardView cardView = new ImageCardView(context) {
        @Override
        public void setSelected(boolean selected) {
            int selected_background = context.getResources().getColor(R.color.detail_background);
            int default_background = context.getResources().getColor(R.color.default_background);
            int color = selected ? selected_background : default_background;
            findViewById(R.id.info_field).setBackgroundColor(color);
            super.setSelected(selected);
        }
    };
...
```

When the user opens your app, the `Presenter.ViewHolder`
displays the `CardView` objects for your content items. You need to set these to receive
focus from the D-pad controller by calling `setFocusable(true)`
and `setFocusableInTouchMode(true)`,
as shown in the following code:

### Kotlin

```
    ...
    cardView.isFocusable = true
    cardView.isFocusableInTouchMode = true
    return ViewHolder(cardView)
}
```

### Java

```
...
    cardView.setFocusable(true);
    cardView.setFocusableInTouchMode(true);
    return new ViewHolder(cardView);
}
```

When the user selects the `ImageCardView`, it expands
to reveal its text area with the background color you specify, as shown in figure 1.

[Previous

arrow\_back

Create a catalog browser](/training/tv/playback/leanback/browse)

[Next

Build a details view

arrow\_forward](/training/tv/playback/leanback/details)