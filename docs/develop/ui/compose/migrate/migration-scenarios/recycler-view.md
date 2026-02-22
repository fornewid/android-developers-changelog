---
title: https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/recycler-view
url: https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/recycler-view
source: md.txt
---

[`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview) is a View component that makes it easy to efficiently display
large sets of data. Instead of creating views for each item in the data set,
`RecyclerView` improves the performance of your app by keeping a small pool of
views and recycling through them as you scroll through those items.

In Compose, you can use [Lazy lists](https://developer.android.com/develop/ui/compose/lists#lazy) to accomplish the same thing. This page
describes how you can migrate your `RecyclerView` implementation to use Lazy lists
in Compose.

## Migration steps

To migrate your `RecyclerView` implementation to Compose, follow these steps:

1. Comment out or remove the `RecyclerView` from your UI hierarchy and add a
   `ComposeView` to replace it if none is present in the hierarchy yet. This
   is the container for the Lazy list that you'll add:

             <FrameLayout
                 android:layout_width="match_parent"
                 android:layout_height="match_parent">

         <!--    <androidx.recyclerview.widget.RecyclerView-->
         <!--            android:id="@+id/recycler_view"-->
         <!--            android:layout_width="match_parent"-->
         <!--            android:layout_height="match_parent />"-->

                 <androidx.compose.ui.platform.ComposeView
                     android:id="@+id/compose_view"
                     android:layout_width="match_parent"
                     android:layout_height="match_parent" />

             </FrameLayout>

2. Determine what type of Lazy list composable you need based on your
   `RecyclerView`'s layout manager (see table below). The composable you select
   will be the top-level composable of the `ComposeView` you added in the
   previous step.

   | `LayoutManager` | Composable |
   |---|---|
   | `LinearLayoutManager` | `LazyColumn` or `LazyRow` |
   | `GridLayoutManager` | `LazyVerticalGrid` or `LazyHorizontalGrid` |
   | `StaggeredGridLayoutManager` | `LazyVerticalStaggeredGrid` or `LazyHorizontalStaggeredGrid` |


   ```kotlin
   // recyclerView.layoutManager = LinearLayoutManager(context)
   composeView.setContent {
       LazyColumn(Modifier.fillMaxSize()) {
           // We use a LazyColumn since the layout manager of the RecyclerView is a vertical LinearLayoutManager
       }
   }
   ```

   <br />

3. Create a corresponding composable for each view type in your
   `RecyclerView.Adapter` implementation. Each view type typically maps to a
   `ViewHolder` subclass, though this may not always be the case. These
   composables will be used as the UI representation for different types of
   elements in your list:


   ```kotlin
   @Composable
   fun ListItem(data: MyData, modifier: Modifier = Modifier) {
       Row(modifier.fillMaxWidth()) {
           Text(text = data.name)
           // ... other composables required for displaying `data`
       }
   }
   ```

   <br />

   The logic in your `RecyclerView.Adapter`'s `onCreateViewHolder()` and
   `onBindViewHolder()` methods will be replaced by these composables and the
   state that you provide them with. In Compose, there is no separation between
   creating a composable for an item and binding data into it---these concepts are
   coalesced.
4. Within the `content` slot of the Lazy list (the trailing lambda parameter),
   use the `items()` function (or an equivalent overload) to iterate through the
   data for your list. In the `itemContent` lambda, invoke the appropriate
   composable item for your data:


   ```kotlin
   val data = listOf<MyData>(/* ... */)
   composeView.setContent {
       LazyColumn(Modifier.fillMaxSize()) {
           items(data) {
               ListItem(it)
           }
       }
   }
   ```

   <br />

> [!TIP]
> **Tip:** Provide additional parameters to `items()` to optimize your list: use the `key` parameter to provide a unique key for the underlying data so that scroll position will be maintained when items change, or use the `contentType` parameter to specify a content type for the underlying data (this is a similar concept to `RecyclerView`'s view types) so you can reuse item compositions more efficiently.

## Common use cases

### Item decorations

`RecyclerView` has the concept of an `ItemDecoration`, which you can use to add a
special drawing for items in the list. For example, you can add an
`ItemDecoration` to add dividers between items:


```kotlin
val itemDecoration = DividerItemDecoration(recyclerView.context, LinearLayoutManager.VERTICAL)
recyclerView.addItemDecoration(itemDecoration)
```

<br />

Compose does not have an equivalent concept of item decorations. Instead, you
can add any UI decorations in the list directly in the composition. For example,
to add dividers to the list, you can use the `Divider` composable after each
item:


```kotlin
LazyColumn(Modifier.fillMaxSize()) {
    itemsIndexed(data) { index, d ->
        ListItem(d)
        if (index != data.size - 1) {
            HorizontalDivider()
        }
    }
}
```

<br />

### Item animations

An `ItemAnimator` can be set on a `RecyclerView` to animate the appearance of
items as changes are made to the adapter. By default, `RecyclerView` uses
[`DefaultItemAnimator`](https://developer.android.com/reference/androidx/recyclerview/widget/DefaultItemAnimator) which provides basic animations on remove, add, and
move events.

Lazy lists have a similar concept through the `animateItemPlacement` modifier.
See [Item animations](https://developer.android.com/develop/ui/compose/lists#item-animations) to learn more.

## Additional resources

For more information about migrating a `RecyclerView` to Compose, see the
following resources:

- [Lists and Grids](https://developer.android.com/develop/ui/compose/lists#item-animations): Documentation for how to implement lists and grids in Compose.
- [Jetpack Compose Interop: Using Compose in a RecyclerView](https://medium.com/androiddevelopers/jetpack-compose-interop-using-compose-in-a-recyclerview-569c7ec7a583): Blog post for efficiently using Compose within a `RecyclerView`.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Lists and grids](https://developer.android.com/develop/ui/compose/lists)
- [Migrate `CoordinatorLayout` to Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/coordinator-layout)
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)