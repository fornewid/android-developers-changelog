---
title: https://developer.android.com/develop/ui/views/layout/recyclerview
url: https://developer.android.com/develop/ui/views/layout/recyclerview
source: md.txt
---

# Create dynamic lists with RecyclerView
Part of [Android Jetpack](https://developer.android.com/jetpack).


Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.  
[Lazy Lists and Grids →](https://developer.android.com/jetpack/compose/lists#lazy)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

RecyclerView makes it easy to efficiently display large sets of data. You supply
the data and define how each item looks, and the RecyclerView library
dynamically creates the elements when they're needed.

As the name implies, RecyclerView *recycles* those individual elements. When an
item scrolls off the screen, RecyclerView doesn't destroy its view. Instead,
RecyclerView reuses the view for new items that have scrolled onscreen.
RecyclerView improves performance and your app's responsiveness, and it
reduces power consumption.
| **Note:** RecyclerView is the name of both the class and the library that contains it. On this page, `RecyclerView` in `code font` always means the class in the RecyclerView library.

## Key classes

Several classes work together to build your dynamic list.

- **[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)**
  is the [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup) that contains the views
  corresponding to your data. It's a view itself, so you add `RecyclerView`
  to your layout the way you would add any other UI element.

- Each individual element in the list is defined by a *view holder* object. When
  the view holder is created, it doesn't have any data associated with it. After
  the view holder is created, the `RecyclerView` *binds* it to its data. You
  define the view holder by extending
  [`RecyclerView.ViewHolder`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder).

- The `RecyclerView` requests views, and binds the views to their data,
  by calling methods in the *adapter.* You define the adapter by extending
  [`RecyclerView.Adapter`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter).

- The *layout manager* arranges the individual elements in your list. You can
  use one of the layout managers provided by the RecyclerView library, or you can
  define your own. Layout managers are all based on the library's
  [`LayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)
  abstract class.

You can see how all the pieces fit together in the [RecyclerView sample app
(Kotlin)](https://github.com/android/views-widgets-samples/tree/main/RecyclerViewKotlin/)
or [RecyclerView sample app
(Java)](https://github.com/android/views-widgets-samples/tree/main/RecyclerView/).

## Steps for implementing your RecyclerView

If you're going to use RecyclerView, there are a few things you need to do.
They are explained in detail in the following sections.

1. Decide how the list or grid looks. Ordinarily, you can
   use one of the RecyclerView library's standard layout managers.

2. Design how each element in the list looks and behaves. Based
   on this design, extend the `ViewHolder` class. Your version of `ViewHolder`
   provides all the functionality for your list items. Your view holder is a
   wrapper around a `View`, and that view is managed by `RecyclerView`.

3. Define the `Adapter` that associates your data with the `ViewHolder` views.

There are also [advanced customization
options](https://developer.android.com/guide/topics/ui/layout/recyclerview-custom) that let you tailor your
RecyclerView to your exact needs.

## Plan your layout

The items in your RecyclerView are arranged by a
[`LayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.LayoutManager)
class. The RecyclerView library provides three layout managers, which handle the
most common layout situations:

- [`LinearLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager) arranges the items in a one-dimensional list.
- [`GridLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/GridLayoutManager) arranges the items in a two-dimensional grid:
  - If the grid is arranged vertically, `GridLayoutManager` tries to make all the elements in each row have the same width and height, but different rows can have different heights.
  - If the grid is arranged horizontally, `GridLayoutManager` tries to make all the elements in each column have the same width and height, but different columns can have different widths.
- [`StaggeredGridLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/StaggeredGridLayoutManager) is similar to `GridLayoutManager`, but it does not require that items in a row have the same height (for vertical grids) or items in the same column have the same width (for horizontal grids). The result is that the items in a row or column can end up offset from each other.

You also need to design the layout of the individual items. You need this
layout when you design the view holder, as described in the next section.

## Implement your adapter and view holder

Once you determine your layout, you need to implement your `Adapter` and
`ViewHolder`. These two classes work together to define how your data is
displayed. The `ViewHolder` is a wrapper around a `View` that contains the
layout for an individual item in the list. The `Adapter` creates `ViewHolder`
objects as needed and also sets the data for those views. The process of
associating views to their data is called *binding.*

When you define your adapter, you override three key methods:

- [`onCreateViewHolder()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onCreateViewHolder(android.view.ViewGroup,%20int)):
  `RecyclerView` calls this method whenever it
  needs to create a new `ViewHolder`. The method creates and initializes the
  `ViewHolder` and its associated `View`, but does *not* fill in the view's
  contents---the `ViewHolder` has not yet been bound to specific data.

- [`onBindViewHolder()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onBindViewHolder(VH,%20int)):
  `RecyclerView` calls this method to associate a `ViewHolder` with data. The
  method fetches the appropriate data and uses the data to fill in the view
  holder's layout. For example, if the `RecyclerView` displays a list of names,
  the method might find the appropriate name in the list and fill in the view
  holder's [`TextView`](https://developer.android.com/reference/android/widget/TextView) widget.

- [`getItemCount()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#getItemCount()):
  `RecyclerView` calls this method to get the size of the dataset. For example,
  in an address book app, this might be the total number of addresses.
  RecyclerView uses this to determine when there are no more items that can be
  displayed.

Here's a typical example of a simple adapter with a nested `ViewHolder` that
displays a list of data. In this case, the RecyclerView displays a simple list
of text elements. The adapter is passed an array of strings containing the text
for the `ViewHolder` elements.  

### Kotlin

```kotlin
class CustomAdapter(private val dataSet: Array<String>) :
        RecyclerView.Adapter<CustomAdapter.ViewHolder>() {

    /**
     * Provide a reference to the type of views that you are using
     * (custom ViewHolder)
     */
    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val textView: TextView

        init {
            // Define click listener for the ViewHolder's View
            textView = view.findViewById(R.id.textView)
        }
    }

    // Create new views (invoked by the layout manager)
    override fun onCreateViewHolder(viewGroup: ViewGroup, viewType: Int): ViewHolder {
        // Create a new view, which defines the UI of the list item
        val view = LayoutInflater.from(viewGroup.context)
                .inflate(R.layout.text_row_item, viewGroup, false)

        return ViewHolder(view)
    }

    // Replace the contents of a view (invoked by the layout manager)
    override fun onBindViewHolder(viewHolder: ViewHolder, position: Int) {

        // Get element from your dataset at this position and replace the
        // contents of the view with that element
        viewHolder.textView.text = dataSet[position]
    }

    // Return the size of your dataset (invoked by the layout manager)
    override fun getItemCount() = dataSet.size

}
```

### Java

```java
public class CustomAdapter extends RecyclerView.Adapter<CustomAdapter.ViewHolder> {

    private String[] localDataSet;

    /**
     * Provide a reference to the type of views that you are using
     * (custom ViewHolder)
     */
    public static class ViewHolder extends RecyclerView.ViewHolder {
        private final TextView textView;

        public ViewHolder(View view) {
            super(view);
            // Define click listener for the ViewHolder's View

            textView = (TextView) view.findViewById(R.id.textView);
        }

        public TextView getTextView() {
            return textView;
        }
    }

    /**
     * Initialize the dataset of the Adapter
     *
     * @param dataSet String[] containing the data to populate views to be used
     * by RecyclerView
     */
    public CustomAdapter(String[] dataSet) {
        localDataSet = dataSet;
    }

    // Create new views (invoked by the layout manager)
    @Override
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup, int viewType) {
        // Create a new view, which defines the UI of the list item
        View view = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.text_row_item, viewGroup, false);

        return new ViewHolder(view);
    }

    // Replace the contents of a view (invoked by the layout manager)
    @Override
    public void onBindViewHolder(ViewHolder viewHolder, final int position) {

        // Get element from your dataset at this position and replace the
        // contents of the view with that element
        viewHolder.getTextView().setText(localDataSet[position]);
    }

    // Return the size of your dataset (invoked by the layout manager)
    @Override
    public int getItemCount() {
        return localDataSet.length;
    }
}
```

The layout for the each view item is defined in an XML layout file, as usual.
In this case, the app has a `text_row_item.xml` file like this:  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="@dimen/list_item_height"
        android:layout_marginLeft="@dimen/margin_medium"
        android:layout_marginRight="@dimen/margin_medium"
        android:gravity="center_vertical">

        <TextView
            android:id="@+id/textView"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/element_text"/>
    </FrameLayout>

## Next steps

The following code snippet shows how you can use the `RecyclerView`.  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val dataset = arrayOf("January", "February", "March")
        val customAdapter = CustomAdapter(dataset)

        val recyclerView: RecyclerView = findViewById(R.id.recycler_view)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = customAdapter

    }

}
```

### Java

```java
RecyclerView recyclerView = findViewById(R.id.recycler_view);
recyclerView.layoutManager = new LinearLayoutManager(this)
recyclerView.setAdapter(customAdapter);
```

The library also offers many ways to customize your implementation. For more
information, see [Advanced RecyclerView
customization](https://developer.android.com/guide/topics/ui/layout/recyclerview-custom).

## Enable edge-to-edge display

Follow these steps to enable an edge-to-edge display for a `RecyclerView`:

- Set up a backward compatible edge-to-edge display by calling [`enableEdgeToEdge()`](https://developer.android.com/develop/ui/views/layout/edge-to-edge#enable-edge-to-edge-display).
- If the list items initially overlap the system bars, apply insets on the `RecyclerView`. You can do this by setting [`android:fitsSystemWindows`](https://developer.android.com/reference/android/view/View#attr_android:fitsSystemWindows) to `true` or by using [`ViewCompat.setOnApplyWindowInsetsListener`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setOnApplyWindowInsetsListener(android.view.View,androidx.core.view.OnApplyWindowInsetsListener)).
- Allow the list items to draw under the system bars while scrolling by setting [`android:clipToPadding`](https://developer.android.com/reference/android/view/ViewGroup#attr_android:clipToPadding) to `false` on the `RecyclerView`.

The following video shows a `RecyclerView` with edge-to-edge display disabled
(left) and enabled (right):
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/develop/ui/views/images/edge-to-edge/recycler-view-e2e.mp4) and watch it with a video player.

Example inset code:  

### Kotlin

```kotlin
ViewCompat.setOnApplyWindowInsetsListener(
  findViewById(R.id.my_recycler_view)
  ) { v, insets ->
      val innerPadding = insets.getInsets(
          WindowInsetsCompat.Type.systemBars()
                  or WindowInsetsCompat.Type.displayCutout()
          // If using EditText, also add
          // "or WindowInsetsCompat.Type.ime()" to
          // maintain focus when opening the IME
      )
      v.setPadding(
          innerPadding.left,
          innerPadding.top,
          innerPadding.right,
          innerPadding.bottom)
      insets
  }
  
```

### Java

```java
ViewCompat.setOnApplyWindowInsetsListener(
  activity.findViewById(R.id.my_recycler_view),
  (v, insets) -> {
      Insets innerPadding = insets.getInsets(
              WindowInsetsCompat.Type.systemBars() |
                      WindowInsetsCompat.Type.displayCutout()
              // If using EditText, also add
              // "| WindowInsetsCompat.Type.ime()" to
              // maintain focus when opening the IME
      );
      v.setPadding(
              innerPadding.left,
              innerPadding.top,
              innerPadding.right,
              innerPadding.bottom
      );
      return insets;
  }
);
  
```

The `RecyclerView` XML:  

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/my_recycler_view"
        android:clipToPadding="false"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

## Additional resources

For more information about testing on Android, consult the following resources.

### Sample apps

- [RecyclerView sample app
  (Kotlin)](https://github.com/android/views-widgets-samples/tree/main/RecyclerViewKotlin/)

- [RecyclerView sample app
  (Java)](https://github.com/android/views-widgets-samples/tree/main/RecyclerView/)

- [Sunflower demo app](https://github.com/googlesamples/android-sunflower)