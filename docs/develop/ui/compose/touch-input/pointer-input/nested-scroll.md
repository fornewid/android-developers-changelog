---
title: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/nested-scroll
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/nested-scroll
source: md.txt
---

[Video](https://www.youtube.com/watch?v=JfYBCKRjFA0)

Nested scrolling is a system where multiple scrolling components contained
within each other work together by reacting to a single scroll gesture and
communicating their scrolling deltas (changes).

The nested scrolling system allows coordination between components that are
scrollable and hierarchically linked (most often by sharing the same parent).
This system links scrolling containers and allows interaction with the scrolling
deltas that are being propagated and shared between.

Compose provides multiple ways of handling nested scrolling between composables.
A typical example of nested scrolling is a list inside another list, and a more
complex case is a [collapsing
toolbar](https://medium.com/androiddevelopers/understanding-nested-scrolling-in-jetpack-compose-eb57c1ea0af0).

## Automatic nested scrolling

Simple nested scrolling requires no action on your part. Gestures that initiate
a scrolling action are propagated from children to parents automatically, such
that when the child can't scroll any further, the gesture is handled by its
parent element.

Automatic nested scrolling is supported and provided out of the box by some of
Compose's components and modifiers:
[`verticalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)),
[`horizontalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).horizontalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)),
[`scrollable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).scrollable(androidx.compose.foundation.gestures.ScrollableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,androidx.compose.foundation.interaction.MutableInteractionSource)),
`Lazy` APIs and `TextField`. This means that when the user scrolls an inner
child of nested components, the previous modifiers propagate the scrolling
deltas to the parents that have nested scrolling support.

The following example shows elements with a
[`verticalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean))
modifier applied to them inside a container that also has a `verticalScroll`
modifier applied to it.


```kotlin
@Composable
private fun AutomaticNestedScroll() {
    val gradient = Brush.verticalGradient(0f to Color.Gray, 1000f to Color.White)
    Box(
        modifier = Modifier
            .background(Color.LightGray)
            .verticalScroll(rememberScrollState())
            .padding(32.dp)
    ) {
        Column {
            repeat(6) {
                Box(
                    modifier = Modifier
                        .height(128.dp)
                        .verticalScroll(rememberScrollState())
                ) {
                    Text(
                        "Scroll here",
                        modifier = Modifier
                            .border(12.dp, Color.DarkGray)
                            .background(brush = gradient)
                            .padding(24.dp)
                            .height(150.dp)
                    )
                }
            }
        }
    }
}
```

<br />

![Two nested vertical scrolling UI elements, responding to gestures inside and outside the inner element](https://developer.android.com/static/develop/ui/compose/images/gestures-simple-nested-scroll.gif) **Figure 1.** Two nested vertical scrolling UI elements, responding to gestures inside and outside the inner element.

## Using the `nestedScroll` modifier

If you need to create an advanced coordinated scroll between multiple elements,
the
[`nestedScroll`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/package-summary#(androidx.compose.ui.Modifier).nestedScroll(androidx.compose.ui.input.nestedscroll.NestedScrollConnection,androidx.compose.ui.input.nestedscroll.NestedScrollDispatcher))
modifier gives you more flexibility by defining a nested scrolling hierarchy. As
mentioned in the previous section, some components have built-in nested scroll
support. However, for composables that aren't scrollable automatically, such as
`Box` or `Column`, scroll deltas on such components won't propagate in the
nested scroll system and the deltas won't reach the `NestedScrollConnection` nor
the parent component. To resolve this, you can use `nestedScroll` to confer such
support to other components, including custom components.

## Nested scrolling cycle

Nested scroll cycle is the flow of scroll deltas that are dispatched up and down
the hierarchy tree through all components (or nodes) that are part of the nested
scrolling system, for example by using scrollable components and modifiers, or
`nestedScroll`.

### Phases of nested scrolling cycle

When a trigger event (for example, a gesture) is detected by a scrollable
component, before the actual scrolling action is even triggered, the generated
deltas are sent to the nested scroll system and go through three phases:
pre-scroll, node consumption, and post-scroll.
![Phases of nested scrolling
cycle](https://developer.android.com/static/develop/ui/compose/images/pointer-input/nested-scrolling-phases-example.jpeg) **Figure 2.** Phases of the nested scrolling cycle.

In the first, pre-scroll phase, the component that received the trigger event
deltas will dispatch those events up, through the hierarchy tree, to the topmost
parent. The delta events will then bubble down, meaning that deltas will be
propagated from the root-most parent down towards the child that started the
nested scroll cycle.
![Pre-scroll phase - dispatching
up](https://developer.android.com/static/develop/ui/compose/images/pointer-input/prescroll-phase.jpeg) **Figure 3.** Pre-scroll phase: dispatching up.

This gives the nested scroll parents (composables using `nestedScroll` or
scrollable modifiers) the opportunity to do something with the delta before the
node itself can consume it.
![Pre-scroll phase - bubbling
down](https://developer.android.com/static/develop/ui/compose/images/pointer-input/prescroll-phase-2.jpeg) **Figure 4.** Pre-scroll phase - bubbling down.

In the node consumption phase, the node itself will use whatever delta was not
used by its parents. This is when the scrolling movement is actually done and is
visible.
![Node consumption
phase](https://developer.android.com/static/develop/ui/compose/images/pointer-input/node-consumption.jpeg) **Figure 5.** Node consumption phase.

During this phase, the child may choose to consume all or part of the remaining
scroll. Anything left will be sent back up to go through the post-scroll phase.

Finally, in the post-scroll phase, anything that the node itself didn't consume
will be sent up again to its ancestors for consumption.
![Post-scroll phase - dispatching
up](https://developer.android.com/static/develop/ui/compose/images/pointer-input/post-scroll.jpeg) **Figure 6.** Post-scroll phase - dispatching up.

The post-scroll phase works in a similar way as the pre-scroll phase, where any
of the parents may choose to consume or not.
![Post-scroll phase - bubbling
down](https://developer.android.com/static/develop/ui/compose/images/pointer-input/post-scroll-2.jpeg) **Figure 7.** Post-scroll phase - bubbling down.

Similarly to scroll, when a drag gesture finishes, the user's intention may be
translated into a velocity that is used to fling (scroll using an animation) the
scrollable container. The fling is also part of the nested scroll cycle, and the
velocities generated by the drag event go through similar phases: pre-fling,
node consumption, and post-fling. Note that fling animation is only associated
with touch gesture and won't be triggered by other events, such as a11y or
hardware scroll.

### Participate in the nested scrolling cycle

Participation in the cycle means intercepting, consuming, and reporting the
consumption of deltas along the hierarchy. Compose provides a set of tools to
influence how the nested scrolling system works and how to interact directly
with it, for example when you need to do something with the scroll deltas before
a scrollable component even starts scrolling.

If the nested scroll cycle is a system acting on a chain of nodes, the
[`nestedScroll`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/package-summary#(androidx.compose.ui.Modifier).nestedScroll(androidx.compose.ui.input.nestedscroll.NestedScrollConnection,androidx.compose.ui.input.nestedscroll.NestedScrollDispatcher))
modifier is a way of intercepting and inserting into these changes, and
influencing the data (scroll deltas) that are propagated in the chain. This
modifier can be placed anywhere in the hierarchy, and it communicates with
nested scroll modifier instances up the tree so it can share information through
this channel. The building blocks of this modifier are `NestedScrollConnection`
and `NestedScrollDispatcher`.

[`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollConnection)
provides a way to respond to the phases of the nested scroll cycle and influence
the nested scroll system. It's composed of four callback methods, each
representing one of the consumption phases: pre/post-scroll and pre/post-fling:


```kotlin
val nestedScrollConnection = object : NestedScrollConnection {
    override fun onPreScroll(available: Offset, source: NestedScrollSource): Offset {
        println("Received onPreScroll callback.")
        return Offset.Zero
    }

    override fun onPostScroll(
        consumed: Offset,
        available: Offset,
        source: NestedScrollSource
    ): Offset {
        println("Received onPostScroll callback.")
        return Offset.Zero
    }
}
```

<br />

Each callback also gives information about the delta being propagated:
`available` delta for that particular phase, and `consumed` delta consumed in
the previous phases. If at any point you want to stop propagating deltas up the
hierarchy, you can use the nested scroll connection to do so:


```kotlin
val disabledNestedScrollConnection = remember {
    object : NestedScrollConnection {
        override fun onPostScroll(
            consumed: Offset,
            available: Offset,
            source: NestedScrollSource
        ): Offset {
            return if (source == NestedScrollSource.SideEffect) {
                available
            } else {
                Offset.Zero
            }
        }
    }
}
```

<br />

All callbacks provide information on the
[`NestedScrollSource`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollSource)
type.

[`NestedScrollDispatcher`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollDispatcher)
initializes the nested scroll cycle. Using a dispatcher and calling its methods
triggers the cycle. Scrollable containers have a built-in dispatcher that sends
deltas captured during gestures into the system. For this reason, most use cases
of customizing nested scrolling involve using `NestedScrollConnection` instead
of a dispatcher, to react to already existing deltas rather than send new ones.
See
[`NestedScrollDispatcherSample`](https://cs.android.com/androidx/platform/tools/dokka-devsite-plugin/+/master:testData/compose/samples/ui/samples/NestedScrollSamples.kt;l=100)
for more usages.

## Resize an image on scroll

As the user scrolls, you can create a dynamic visual effect where the image
changes size based on the scroll position.

### Resize an image based on scroll position

This snippet demonstrates resizing an image within a [`LazyColumn`](https://developer.android.com/develop/ui/compose/lists) based on
vertical scroll position. The image shrinks as the user scrolls down, and grows
as they scroll up, remaining within the defined minimum and maximum size bounds:


```kotlin
@Composable
fun ImageResizeOnScrollExample(
    modifier: Modifier = Modifier,
    maxImageSize: Dp = 300.dp,
    minImageSize: Dp = 100.dp
) {
    var currentImageSize by remember { mutableStateOf(maxImageSize) }
    var imageScale by remember { mutableFloatStateOf(1f) }

    val nestedScrollConnection = remember {
        object : NestedScrollConnection {
            override fun onPreScroll(available: Offset, source: NestedScrollSource): Offset {
                // Calculate the change in image size based on scroll delta
                val delta = available.y
                val newImageSize = currentImageSize + delta.dp
                val previousImageSize = currentImageSize

                // Constrain the image size within the allowed bounds
                currentImageSize = newImageSize.coerceIn(minImageSize, maxImageSize)
                val consumed = currentImageSize - previousImageSize

                // Calculate the scale for the image
                imageScale = currentImageSize / maxImageSize

                // Return the consumed scroll amount
                return Offset(0f, consumed.value)
            }
        }
    }

    Box(Modifier.nestedScroll(nestedScrollConnection)) {
        LazyColumn(
            Modifier
                .fillMaxWidth()
                .padding(15.dp)
                .offset {
                    IntOffset(0, currentImageSize.roundToPx())
                }
        ) {
            // Placeholder list items
            items(100, key = { it }) {
                Text(
                    text = "Item: $it",
                    style = MaterialTheme.typography.bodyLarge
                )
            }
        }

        Image(
            painter = ColorPainter(Color.Red),
            contentDescription = "Red color image",
            Modifier
                .size(maxImageSize)
                .align(Alignment.TopCenter)
                .graphicsLayer {
                    scaleX = imageScale
                    scaleY = imageScale
                    // Center the image vertically as it scales
                    translationY = -(maxImageSize.toPx() - currentImageSize.toPx()) / 2f
                }
        )
    }
}
```

<br />

### Key points about the code

- This code uses a [`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)) to intercept scroll events.
- [`onPreScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).horizontalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)) calculates the change in image size based on the scroll delta.
- The `currentImageSize` state variable stores the current size of the image, constrained between `minImageSize` and `maxImageSize. imageScale` derives from the `currentImageSize`.
- The [`LazyColumn`](https://developer.android.com/develop/ui/compose/lists) offsets based on the `currentImageSize`.
- The [`Image`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/ScrollState) uses a [`graphicsLayer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#rememberScrollState(kotlin.Int)) modifier to apply the calculated scale.
- The `translationY` within the `graphicsLayer` ensures the image remains centered vertically as it scales.

### Result

The preceding snippet results in a scaling image effect on scroll:
**Figure 8.** A scaling image effect on scroll.

## Nested scrolling interop

When you try to nest scrollable `View` elements in scrollable composables, or
the other way around, you might encounter issues. Most noticeable ones would
happen when you scroll the child and reach its start or end bounds and expect
the parent to take the scrolling over. However, this expected behaviour either
might not happen or might not work as expected.

This issue is a result of the expectations built in scrollable composables.
Scrollable composables have a "nested-scroll-by-default" rule, which means that
any scrollable container must participate in the nested scroll chain, both as a
parent via
[`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollConnection),
and as a child via
[`NestedScrollDispatcher`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollDispatcher).
The child would then drive a nested scroll for the parent when the child is at
the bound. As an example, this rule allows Compose `Pager` and Compose `LazyRow`
to work well together. However, when interoperability scrolling is being done
with `ViewPager2` or `RecyclerView`, since these don't implement
[`NestedScrollingParent3`](https://developer.android.com/reference/kotlin/androidx/core/view/NestedScrollingParent3),
the continuous scrolling from child to parent is not possible.

To enable nested scrolling interop API between scrollable `View` elements and
scrollable composables, nested in both directions, you can use the nested
scrolling interop API to mitigate these issues, in the following scenarios.

### A cooperating parent `View` containing a child `ComposeView`

A cooperating parent `View` is one that already implements
[`NestedScrollingParent3`](https://developer.android.com/reference/kotlin/androidx/core/view/NestedScrollingParent3)
and therefore is able to receive scrolling deltas from a cooperating nested
child composable. `ComposeView` would act as a child in this case and would
need to (indirectly) implement
[`NestedScrollingChild3`](https://developer.android.com/reference/kotlin/androidx/core/view/NestedScrollingChild3).
One example of a cooperating parent is
`androidx.coordinatorlayout.widget.CoordinatorLayout`.

If you need nested scrolling interoperability between scrollable `View` parent
containers and nested scrollable child composables, you can use
[`rememberNestedScrollInteropConnection()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#rememberNestedScrollInteropConnection()).

[`rememberNestedScrollInteropConnection()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#rememberNestedScrollInteropConnection())
allows and remembers the
[`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollConnection)
that enables nested scroll interoperability between a `View` parent that
implements
[`NestedScrollingParent3`](https://developer.android.com/reference/kotlin/androidx/core/view/NestedScrollingParent3)
and a Compose child. This should be used in conjunction with a
[`nestedScroll`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/package-summary#(androidx.compose.ui.Modifier).nestedScroll(androidx.compose.ui.input.nestedscroll.NestedScrollConnection,androidx.compose.ui.input.nestedscroll.NestedScrollDispatcher))
modifier. Since nested scrolling is enabled by default on the Compose side, you
can use this connection to enable both nested scroll on the `View` side and add
the necessary glue logic between `Views` and composables.

A frequent use case is using `CoordinatorLayout`, `CollapsingToolbarLayout` and
a child composable, shown in this example:

```xml
<androidx.coordinatorlayout.widget.CoordinatorLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.google.android.material.appbar.AppBarLayout
        android:id="@+id/app_bar"
        android:layout_width="match_parent"
        android:layout_height="100dp"
        android:fitsSystemWindows="true">

        <com.google.android.material.appbar.CollapsingToolbarLayout
            android:id="@+id/collapsing_toolbar_layout"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:fitsSystemWindows="true"
            app:layout_scrollFlags="scroll|exitUntilCollapsed">

            <!--...-->

        </com.google.android.material.appbar.CollapsingToolbarLayout>

    </com.google.android.material.appbar.AppBarLayout>

    <androidx.compose.ui.platform.ComposeView
        android:id="@+id/compose_view"
        app:layout_behavior="@string/appbar_scrolling_view_behavior"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</androidx.coordinatorlayout.widget.CoordinatorLayout>
```

In your Activity or Fragment, you need to set up your child composable and the
required
[`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollConnection):


```kotlin
open class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        findViewById<ComposeView>(R.id.compose_view).apply {
            setContent {
                val nestedScrollInterop = rememberNestedScrollInteropConnection()
                // Add the nested scroll connection to your top level @Composable element
                // using the nestedScroll modifier.
                LazyColumn(modifier = Modifier.nestedScroll(nestedScrollInterop)) {
                    items(20) { item ->
                        Box(
                            modifier = Modifier
                                .padding(16.dp)
                                .height(56.dp)
                                .fillMaxWidth()
                                .background(Color.Gray),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(item.toString())
                        }
                    }
                }
            }
        }
    }
}
```

<br />

### A parent composable containing a child `AndroidView`

This scenario covers the implementation of nested scrolling interop API on the
Compose side - when you have a parent composable containing a child
`AndroidView`. The `AndroidView` implements
[`NestedScrollDispatcher`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollDispatcher),
since it acts as a child to a Compose scrolling parent, as well as
[`NestedScrollingParent3`](https://developer.android.com/reference/kotlin/androidx/core/view/NestedScrollingParent3)
, since it acts as a parent to a `View` scrolling child. Compose parent will
then be able to receive nested scroll deltas from a nested scrollable child
`View`.

The following example shows how you can achieve nested scrolling interop in this
scenario, along with a Compose collapsing toolbar:

    @Composable
    private fun NestedScrollInteropComposeParentWithAndroidChildExample() {
        val toolbarHeightPx = with(LocalDensity.current) { ToolbarHeight.roundToPx().toFloat() }
        val toolbarOffsetHeightPx = remember { mutableStateOf(0f) }

        // Sets up the nested scroll connection between the Box composable parent
        // and the child AndroidView containing the RecyclerView
        val nestedScrollConnection = remember {
            object : NestedScrollConnection {
                override fun onPreScroll(available: Offset, source: NestedScrollSource): Offset {
                    // Updates the toolbar offset based on the scroll to enable
                    // collapsible behaviour
                    val delta = available.y
                    val newOffset = toolbarOffsetHeightPx.value + delta
                    toolbarOffsetHeightPx.value = newOffset.coerceIn(-toolbarHeightPx, 0f)
                    return Offset.Zero
                }
            }
        }

        Box(
            Modifier
                .fillMaxSize()
                .nestedScroll(nestedScrollConnection)
        ) {
            TopAppBar(
                modifier = Modifier
                    .height(ToolbarHeight)
                    .offset { IntOffset(x = 0, y = toolbarOffsetHeightPx.value.roundToInt()) }
            )

            AndroidView(
                { context ->
                    LayoutInflater.from(context)
                        .inflate(R.layout.view_in_compose_nested_scroll_interop, null).apply {
                            with(findViewById<RecyclerView>(R.id.main_list)) {
                                layoutManager = LinearLayoutManager(context, VERTICAL, false)
                                adapter = NestedScrollInteropAdapter()
                            }
                        }.also {
                            // Nested scrolling interop is enabled when
                            // nested scroll is enabled for the root View
                            ViewCompat.setNestedScrollingEnabled(it, true)
                        }
                },
                // ...
            )
        }
    }

    private class NestedScrollInteropAdapter :
        Adapter<NestedScrollInteropAdapter.NestedScrollInteropViewHolder>() {
        val items = (1..10).map { it.toString() }

        override fun onCreateViewHolder(
            parent: ViewGroup,
            viewType: Int
        ): NestedScrollInteropViewHolder {
            return NestedScrollInteropViewHolder(
                LayoutInflater.from(parent.context)
                    .inflate(R.layout.list_item, parent, false)
            )
        }

        override fun onBindViewHolder(holder: NestedScrollInteropViewHolder, position: Int) {
            // ...
        }

        class NestedScrollInteropViewHolder(view: View) : ViewHolder(view) {
            fun bind(item: String) {
                // ...
            }
        }
        // ...
    }

This example shows how you can use the API with a `scrollable` modifier:

    @Composable
    fun ViewInComposeNestedScrollInteropExample() {
        Box(
            Modifier
                .fillMaxSize()
                .scrollable(rememberScrollableState {
                    // View component deltas should be reflected in Compose
                    // components that participate in nested scrolling
                    it
                }, Orientation.Vertical)
        ) {
            AndroidView(
                { context ->
                    LayoutInflater.from(context)
                        .inflate(android.R.layout.list_item, null)
                        .apply {
                            // Nested scrolling interop is enabled when
                            // nested scroll is enabled for the root View
                            ViewCompat.setNestedScrollingEnabled(this, true)
                        }
                }
            )
        }
    }

And finally, this example shows how nested scrolling interop API is used with
[`BottomSheetDialogFragment`](https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialogFragment)
to achieve a successful drag and dismiss behaviour:

    class BottomSheetFragment : BottomSheetDialogFragment() {

        override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
        ): View {
            val rootView: View = inflater.inflate(R.layout.fragment_bottom_sheet, container, false)

            rootView.findViewById<ComposeView>(R.id.compose_view).apply {
                setContent {
                    val nestedScrollInterop = rememberNestedScrollInteropConnection()
                    LazyColumn(
                        Modifier
                            .nestedScroll(nestedScrollInterop)
                            .fillMaxSize()
                    ) {
                        item {
                            Text(text = "Bottom sheet title")
                        }
                        items(10) {
                            Text(
                                text = "List item number $it",
                                modifier = Modifier.fillMaxWidth()
                            )
                        }
                    }
                }
                return rootView
            }
        }
    }

Note that
[`rememberNestedScrollInteropConnection()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#rememberNestedScrollInteropConnection())
will install a
[`NestedScrollConnection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/NestedScrollConnection)
in the element you attach it to. `NestedScrollConnection` is responsible for
transmitting the deltas from the Compose level to the `View` level. This enables
the element to participate in nested scrolling, but it doesn't enable
scrolling of elements automatically. To composables that aren't scrollable
automatically, such as `Box` or `Column`, scroll deltas on such components won't
propagate in the nested scroll system and the deltas won't reach the
`NestedScrollConnection` provided by `rememberNestedScrollInteropConnection()`,
therefore those deltas won't reach the parent `View` component. To resolve this,
make sure you also set scrollable modifiers to these types of nested
composables. You can refer to the previous section on [nested
scrolling](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll#nestedscroll-modifier) for more detailed
information.

### A non-cooperating parent `View` containing a child `ComposeView`

A non-cooperating View is one that does not implement the necessary
`NestedScrolling` interfaces on the `View` side. Note that this means that
nested scrolling interoperability with these `Views` doesn't work out of the
box. Non-cooperating `Views` are `RecyclerView` and `ViewPager2`.

## Additional resources

- [Create a button to enable snap scrolling](https://developer.android.com/develop/ui/compose/quick-guides/content/enable-snap-scrolling)
- [Create a parallax scrolling effect](https://developer.android.com/develop/ui/compose/quick-guides/content/parallax-scrolling)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Understand gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures)
- [Migrate `CoordinatorLayout` to Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/coordinator-layout)
- [Using Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose)