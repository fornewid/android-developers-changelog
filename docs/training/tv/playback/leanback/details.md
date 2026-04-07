---
title: https://developer.android.com/training/tv/playback/leanback/details
url: https://developer.android.com/training/tv/playback/leanback/details
source: md.txt
---

Build better with Compose  
Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.  
[Compose for TV →](https://developer.android.com/training/tv/playback/compose)  
![](https://developer.android.com/static/images/android-compose-tv-logo.png)
| **Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
| Android TV OS](https://developer.android.com/training/tv/playback/compose) instead.


The media browsing interface classes provided by the deprecated
[androidx.leanback library](https://developer.android.com/training/tv/get-started/create#leanback) include classes for displaying additional information about a media
item, such as a description or reviews. They also include classes for taking action on that item,
such as purchasing it or playing its content.


This guide discusses how to create a presenter class for media item details and how to extend
the [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment) class to implement a details view
for a media item when the user selects it.


**Note:** The implementation example shown here uses an additional activity to
contain the [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment). However, it's possible to
avoid creating a second activity by replacing the [BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment) with a [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment) within the *same* activity using
fragment transactions. For more information on using fragment transactions, see [Create a fragment](https://developer.android.com/training/basics/fragments/fragment-ui).

## Build a details presenter


In the media browsing framework provided by the Leanback UI toolkit, you use presenter
objects to control the display of data on screen, including media item details.
For this purpose, the framework
provides the [AbstractDetailsDescriptionPresenter](https://developer.android.com/reference/androidx/leanback/widget/AbstractDetailsDescriptionPresenter)
class, which is a nearly complete implementation of the presenter for media item
details. All you have to do is implement the [onBindDescription()](https://developer.android.com/reference/androidx/leanback/widget/AbstractDetailsDescriptionPresenter#onBindDescription(androidx.leanback.widget.AbstractDetailsDescriptionPresenter.ViewHolder,java.lang.Object)))
method to bind the view fields to your data objects, as shown in the
following code sample:  

### Kotlin

```kotlin
class DetailsDescriptionPresenter : AbstractDetailsDescriptionPresenter() {

    override fun onBindDescription(viewHolder: AbstractDetailsDescriptionPresenter.ViewHolder, itemData: Any) {
        val details = itemData as MyMediaItemDetails
        // In a production app, the itemData object contains the information
        // needed to display details for the media item:
        // viewHolder.title.text = details.shortTitle

        // Here we provide static data for testing purposes:
        viewHolder.apply {
            title.text = itemData.toString()
            subtitle.text = "2014   Drama   TV-14"
            body.text = ("Lorem ipsum dolor sit amet, consectetur "
                    + "adipisicing elit, sed do eiusmod tempor incididunt ut labore "
                    + " et dolore magna aliqua. Ut enim ad minim veniam, quis "
                    + "nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
                    + "commodo consequat.")
        }
    }
}
```

### Java

```java
public class DetailsDescriptionPresenter
        extends AbstractDetailsDescriptionPresenter {

    @Override
    protected void onBindDescription(ViewHolder viewHolder, Object itemData) {
        MyMediaItemDetails details = (MyMediaItemDetails) itemData;
        // In a production app, the itemData object contains the information
        // needed to display details for the media item:
        // viewHolder.getTitle().setText(details.getShortTitle());

        // Here we provide static data for testing purposes:
        viewHolder.getTitle().setText(itemData.toString());
        viewHolder.getSubtitle().setText("2014   Drama   TV-14");
        viewHolder.getBody().setText("Lorem ipsum dolor sit amet, consectetur "
                + "adipisicing elit, sed do eiusmod tempor incididunt ut labore "
                + " et dolore magna aliqua. Ut enim ad minim veniam, quis "
                + "nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
                + "commodo consequat.");
    }
}
```

## Extend the details fragment


When using the [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment) class for displaying
your media item details, extend that class to provide additional content, such as a preview
image and actions for the media item. You can also provide additional content, such as a list of
related media items.


The following example code demonstrates how to use the presenter class shown in the
previous section to add a preview image and actions for the media item being viewed. This example
also shows the addition of a related media items row, which appears below the details listing.  

### Kotlin

```kotlin
private const val TAG = "MediaItemDetailsFragment"

class MediaItemDetailsFragment : DetailsSupportFragment() {
    private lateinit var rowsAdapter: ArrayObjectAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        Log.i(TAG, "onCreate")
        super.onCreate(savedInstanceState)

        buildDetails()
    }

    private fun buildDetails() {
        val selector = ClassPresenterSelector().apply {
            // Attach your media item details presenter to the row presenter:
            FullWidthDetailsOverviewRowPresenter(DetailsDescriptionPresenter()).also {
                addClassPresenter(DetailsOverviewRow::class.java, it)
            }
            addClassPresenter(ListRow::class.java, ListRowPresenter())
        }
        rowsAdapter = ArrayObjectAdapter(selector)

        val res = activity.resources
        val detailsOverview = DetailsOverviewRow("Media Item Details").apply {

            // Add images and action buttons to the details view
            imageDrawable = res.getDrawable(R.drawable.jelly_beans)
            addAction(Action(1, "Buy $9.99"))
            addAction(Action(2, "Rent $2.99"))
        }
        rowsAdapter.add(detailsOverview)

        // Add a related items row
        val listRowAdapter = ArrayObjectAdapter(StringPresenter()).apply {
            add("Media Item 1")
            add("Media Item 2")
            add("Media Item 3")
        }
        val header = HeaderItem(0, "Related Items")
        rowsAdapter.add(ListRow(header, listRowAdapter))

        adapter = rowsAdapter
    }
}
```

### Java

```java
public class MediaItemDetailsFragment extends DetailsSupportFragment {
    private static final String TAG = "MediaItemDetailsFragment";
    private ArrayObjectAdapter rowsAdapter;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        Log.i(TAG, "onCreate");
        super.onCreate(savedInstanceState);

        buildDetails();
    }

    private void buildDetails() {
        ClassPresenterSelector selector = new ClassPresenterSelector();
        // Attach your media item details presenter to the row presenter:
        FullWidthDetailsOverviewRowPresenter rowPresenter =
            new FullWidthDetailsOverviewRowPresenter(
                new DetailsDescriptionPresenter());

        selector.addClassPresenter(DetailsOverviewRow.class, rowPresenter);
        selector.addClassPresenter(ListRow.class,
                new ListRowPresenter());
        rowsAdapter = new ArrayObjectAdapter(selector);

        Resources res = getActivity().getResources();
        DetailsOverviewRow detailsOverview = new DetailsOverviewRow(
                "Media Item Details");

        // Add images and action buttons to the details view
        detailsOverview.setImageDrawable(res.getDrawable(R.drawable.jelly_beans));
        detailsOverview.addAction(new Action(1, "Buy $9.99"));
        detailsOverview.addAction(new Action(2, "Rent $2.99"));
        rowsAdapter.add(detailsOverview);

        // Add a related items row
        ArrayObjectAdapter listRowAdapter = new ArrayObjectAdapter(
                new StringPresenter());
        listRowAdapter.add("Media Item 1");
        listRowAdapter.add("Media Item 2");
        listRowAdapter.add("Media Item 3");
        HeaderItem header = new HeaderItem(0, "Related Items", null);
        rowsAdapter.add(new ListRow(header, listRowAdapter));

        setAdapter(rowsAdapter);
    }
}
```

### Create a details activity


Fragments like the [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment) must be contained
within an activity to be used for display. Creating an activity for your details
view---separate from the browse activity---lets you invoke your details view using an
[Intent](https://developer.android.com/reference/android/content/Intent). This
section explains how to build an activity to contain your implementation of the detail view for
your media items.


Create the details activity by building a layout that references your implementation of
the `DetailsSupportFragment`:  

```xml
<!-- file: res/layout/details.xml -->

<fragment xmlns:android="http://schemas.android.com/apk/res/android"
    android:name="com.example.android.mediabrowser.MediaItemDetailsFragment"
    android:id="@+id/details_fragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
/>
```


Next, create an activity class that uses the layout shown in the previous code example:  

### Kotlin

```kotlin
class DetailsActivity : FragmentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.details)
    }
}
```

### Java

```java
public class DetailsActivity extends FragmentActivity
{
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.details);
    }
}
```


Finally, add this new activity to the manifest. Remember to apply the Leanback theme to ensure
that the user interface is consistent with the media browse activity.  

```xml
<application>
  ...
  <activity android:name=".DetailsActivity"
    android:exported="true"
    android:theme="@style/Theme.Leanback"/>

</application>
```

### Define a listener for clicked items


After you implement the [DetailsSupportFragment](https://developer.android.com/reference/androidx/leanback/app/DetailsSupportFragment),
modify your main media browsing view to move to your details view when a user clicks a media
item. To enable this behavior, add an
[OnItemViewClickedListener](https://developer.android.com/reference/androidx/leanback/widget/OnItemViewClickedListener) object to the
[BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment) that fires an intent to start the item
details activity.


The following example shows how to implement a listener to start the details view when a user
clicks a media item in the main media browsing activity:  

### Kotlin

```kotlin
class BrowseMediaActivity : FragmentActivity() {
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Create the media item rows
        buildRowsAdapter()

        // Add a listener for selected items
        browseFragment.onItemViewClickedListener = OnItemViewClickedListener { _, item, _, _ ->
            println("Media Item clicked: ${item}")
            val intent = Intent(this@BrowseMediaActivity, DetailsActivity::class.java).apply {
                // Pass the item information
                extras.putLong("id", item.getId())
            }
            startActivity(intent)
        }
    }
}
```

### Java

```java
public class BrowseMediaActivity extends FragmentActivity {
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // Create the media item rows
        buildRowsAdapter();

        // Add a listener for selected items
        browseFragment.OnItemViewClickedListener(
            new OnItemViewClickedListener() {
                @Override
                public void onItemClicked(Object item, Row row) {
                    System.out.println("Media Item clicked: " + item.toString());
                    Intent intent = new Intent(BrowseMediaActivity.this,
                            DetailsActivity.class);
                    // Pass the item information
                    intent.getExtras().putLong("id", item.getId());
                    startActivity(intent);
                }
            });
    }
}
```