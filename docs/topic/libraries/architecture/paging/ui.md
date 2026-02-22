---
title: https://developer.android.com/topic/libraries/architecture/paging/ui
url: https://developer.android.com/topic/libraries/architecture/paging/ui
source: md.txt
---

This guide builds upon the[Paging Library overview](https://developer.android.com/topic/libraries/architecture/paging), describing how you can present lists of information to users in your app's UI, particularly when this information changes.
| **Caution:** This guide covers an older, deprecated version of the Paging library. For more information about the latest stable version of Paging, see the[Paging 3 guides](https://developer.android.com/topic/libraries/architecture/paging/v3-overview).

## Connect your UI to your view model

You can connect an instance of[`LiveData<PagedList>`](https://developer.android.com/reference/androidx/lifecycle/LiveData)to a[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter), as shown in the following code snippet:  

### Kotlin

```kotlin
class ConcertActivity : AppCompatActivity() {
    private val adapter = ConcertAdapter()

    // Use the 'by viewModels()' Kotlin property delegate
    // from the activity-ktx artifact
    private val viewModel: ConcertViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState);
        viewModel.concerts.observe(this, Observer { adapter.submitList(it) })
    }
}
```

### Java

```java
public class ConcertActivity extends AppCompatActivity {
    private ConcertAdapter adapter = new ConcertAdapter();
    private ConcertViewModel viewModel;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        viewModel = new ViewModelProvider(this).get(ConcertViewModel.class);
        viewModel.concertList.observe(this, adapter::submitList);
    }
}
```

As data sources provide new instances of[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList), the activity sends these objects to the adapter. The[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter)implementation defines how updates are computed, and it automatically handles paging and list diffing. Therefore, your[`ViewHolder`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder)only needs to bind to a particular provided item:  

### Kotlin

```kotlin
class ConcertAdapter() :
        PagedListAdapter<Concert, ConcertViewHolder>(DIFF_CALLBACK) {
    override fun onBindViewHolder(holder: ConcertViewHolder, position: Int) {
        val concert: Concert? = getItem(position)

        // Note that "concert" is a placeholder if it's null.
        holder.bindTo(concert)
    }

    companion object {
        private val DIFF_CALLBACK = ... // See https://developer.android.com/topic/libraries/architecture/paging/ui#implement-diffing-callback section.
    }
}
```

### Java

```java
public class ConcertAdapter
        extends PagedListAdapter<Concert, ConcertViewHolder> {
    protected ConcertAdapter() {
        super(DIFF_CALLBACK);
    }

    @Override
    public void onBindViewHolder(@NonNull ConcertViewHolder holder,
            int position) {
        Concert concert = getItem(position);

        // Note that "concert" can be null if it's a placeholder.
        holder.bindTo(concert);
    }

    private static DiffUtil.ItemCallback<Concert> DIFF_CALLBACK
            = ... // See https://developer.android.com/topic/libraries/architecture/paging/ui#implement-diffing-callback section.
}
```

The[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter)handles page load events using a[`PagedList.Callback`](https://developer.android.com/reference/androidx/paging/PagedList.Callback)object. As the user scrolls, the`PagedListAdapter`calls[`PagedList.loadAround()`](https://developer.android.com/reference/androidx/paging/PagedList#loadaround)to provide hints to the underlying[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)as to which items it should fetch from the[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource).
| **Note:** [`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)is content-immutable. This means that, although new content can be loaded into an instance of`PagedList`, the loaded items themselves cannot change once loaded. As such, if content in a`PagedList`updates, the[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter)object receives a completely new`PagedList`that contains the updated information.

## Implement the diffing callback

The following sample shows a manual implementation of[`areContentsTheSame()`](https://developer.android.com/reference/androidx/recyclerview/widget/DiffUtil.ItemCallback#arecontentsthesame), which compares relevant object fields:  

### Kotlin

```kotlin
private val DIFF_CALLBACK = object : DiffUtil.ItemCallback<Concert>() {
    // The ID property identifies when items are the same.
    override fun areItemsTheSame(oldItem: Concert, newItem: Concert) =
            oldItem.id == newItem.id

    // If you use the "==" operator, make sure that the object implements
    // .equals(). Alternatively, write custom data comparison logic here.
    override fun areContentsTheSame(
            oldItem: Concert, newItem: Concert) = oldItem == newItem
}
```

### Java

```java
private static DiffUtil.ItemCallback<Concert> DIFF_CALLBACK =
        new DiffUtil.ItemCallback<Concert>() {

    @Override
    public boolean areItemsTheSame(Concert oldItem, Concert newItem) {
        // The ID property identifies when items are the same.
        return oldItem.getId() == newItem.getId();
    }

    @Override
    public boolean areContentsTheSame(Concert oldItem, Concert newItem) {
        // Don't use the "==" operator here. Either implement and use .equals(),
        // or write custom data comparison logic here.
        return oldItem.equals(newItem);
    }
};
```

Because your adapter includes your definition of comparing items, the adapter automatically detects changes to these items when a new`PagedList`object is loaded. As a result, the adapter triggers efficient item animations within your`RecyclerView`object.

## Diffing using a different adapter type

If you choose not to inherit from[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter)---such as when you're using a library that provides its own adapter---you can still use the Paging Library adapter's diffing functionality by working directly with an[`AsyncPagedListDiffer`](https://developer.android.com/reference/androidx/paging/AsyncPagedListDiffer)object.

## Provide placeholders in your UI

In cases where you want your UI to display a list before your app has finished fetching data, you can show placeholder list items to your users. The[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)handles this case by presenting the list item data as`null`until the data is loaded.
| **Note:** By default, the Paging Library enables this placeholder behavior.

Placeholders have the following benefits:

- **Support for scrollbars:** The[`PagedList`](https://developer.android.com/reference/androidx/paging/PagedList)provides the number of list items to the[`PagedListAdapter`](https://developer.android.com/reference/androidx/paging/PagedListAdapter). This information allows the adapter to draw a scrollbar that conveys the full size of the list. As new pages load, the scrollbar doesn't jump because your list doesn't change size.
- **No loading spinner necessary:**Because the list size is already known, there's no need to alert users that more items are loading. The placeholders themselves convey that information.

Before adding support for placeholders, though, keep the following preconditions in mind:

- **Requires a countable data set:** Instances of[`DataSource`](https://developer.android.com/reference/androidx/paging/DataSource)from the[Room persistence library](https://developer.android.com/topic/libraries/architecture/room)can efficiently count their items. If you're using a custom local storage solution or a[network-only data architecture](https://developer.android.com/topic/libraries/architecture/paging#network-only-data-arch), however, it might be expensive or even impossible to determine how many items comprise your data set.
- **Requires adapter to account for unloaded items:** The adapter or presentation mechanism that you use to prepare the list for inflation needs to handle null list items. For example, when binding data to a[`ViewHolder`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.ViewHolder), you need to provide default values to represent unloaded data.
- **Requires same-sized item views:**If list item sizes can change based on their content, such as social networking updates, crossfading between items doesn't look good. We strongly suggest disabling placeholders in this case.

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
- [Paging 2 library overview](https://developer.android.com/topic/libraries/architecture/paging)
- [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration)
- [Gather paged data](https://developer.android.com/topic/libraries/architecture/paging/data)