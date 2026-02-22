---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes
source: md.txt
---

> [!NOTE]
> **Note:** For apps that target Android 16 (API level 36), the system ignores screen orientation, aspect ratio, and app resizablility restrictions to improve the layout of apps on form factors with smallest width \>= 600dp. See [App
> orientation, aspect ratio, and
> resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).

Support for different display sizes enables access to your app by the widest
variety of devices and greatest number of users.

To support as many display sizes as possible---whether different device
screens or different app windows in [multi-window mode](https://developer.android.com/guide/topics/ui/multi-window)---design your app
layouts to be responsive and adaptive. Responsive/adaptive layouts provide an
optimized user experience regardless of display size, enabling your app to
accommodate phones, tablets, foldables, ChromeOS devices, portrait and landscape
orientations, and resizable display configurations such as split‑screen
mode and desktop windowing.

Responsive/adaptive layouts change based on available display space. Changes
range from small layout adjustments that fill up space (responsive design) to
completely replacing one layout with another so your app can best accommodate
different display sizes (adaptive design).

As a declarative UI toolkit, Jetpack Compose is ideal for designing and
implementing layouts that dynamically change to render content differently on
different display sizes.

## Make large layout changes for content-level composables explicit

App-level and content-level composables occupy all of the display space
available to your app. For these types of composables, it might make sense to
change the overall layout of your app on large displays.

> [!IMPORTANT]
> **Key terms:**
>
> - **App-level composable:** The single, root composable that occupies all space given to your app and contains all other composables.
> - **content-level composable:** A composable contained within the app-level composable thats occupies all space given to your app. Each content-level composable generally represents a particular destination when navigating through the app.
> - **Individual composables:** All other composables. These could be individual elements, reusable groups of content, or composables hosted within content-level composables.

**Avoid using physical hardware values for making layout decisions.** It might
be tempting to make decisions based on a fixed tangible value (Is the device a
tablet? Does the physical screen have a certain aspect ratio?), but the answers
to these questions may not be useful for determining the space available for
your UI.
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/adaptive-many-screens.png) **Figure 1.** Phone, foldable, tablet, and laptop form factors

On tablets, an app might be running in multi-window mode, which means the app
may be splitting the screen with another app. In desktop windowing mode or on
ChromeOS, an app might be in a resizable window. There might even be more than
one physical screen, such as with a foldable device. In all of these cases, the
physical screen size isn't relevant for deciding how to display content.

Instead, make decisions based on the actual portion of the screen allocated to
your app described by the current window metrics provided by the Jetpack
[WindowManager](https://developer.android.com/jetpack/androidx/releases/window) library. For an example of how to use WindowManager in a
Compose app, see the [JetNews](https://github.com/android/compose-samples/tree/main/JetNews) sample.

Making your layouts adaptive to the available display space also reduces the
amount of special handling needed to support platforms like ChromeOS and form
factors like tablets and foldables.

When you've determined the metrics of the space available for your app, convert
the raw size into a window size class as described in [Use window size
classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes). Window size classes are breakpoints designed to balance app logic
simplicity with the flexibility to optimize your app for most display sizes.

Window size classes refer to the overall window of your app, so use the classes
for layout decisions that affect your overall app layout. You can pass window
size classes down as state, or you can perform additional logic to create
derived state to pass down to nested composables.


```kotlin
@Composable
fun MyApp(
    windowSizeClass: WindowSizeClass = currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true).windowSizeClass
) {
    // Decide whether to show the top app bar based on window size class.
    val showTopAppBar = windowSizeClass.isHeightAtLeastBreakpoint(WindowSizeClass.HEIGHT_DP_MEDIUM_LOWER_BOUND)

    // MyScreen logic is based on the showTopAppBar boolean flag.
    MyScreen(
        showTopAppBar = showTopAppBar,
        /* ... */
    )
}
```

<br />

A layered approach confines display size logic to a single location instead of
scattering it across your app in many places that need to be kept in sync. A
single location produces state, which can be explicitly passed down to other
composables just like any other app state. Explicitly passing state simplifies
individual composables because the composables take the window size class or
specified configuration along with other data.

## Flexible nested composables are reusable

Composables are more reusable when they can be placed in a wide variety of
places. If a composable must be placed in a specific location with a specific
size, the composable is unlikely to be reusable in other contexts. This also
means that individual, reusable composables should avoid implicitly depending on
*global* display size information.

Imagine a nested composable that implements a [list-detail layout](https://m3.material.io/foundations/layout/canonical-layouts/list-detail), which may
show either a single pane or two panes side by side:
![An app showing two panes side by side.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/adaptive-list-detail.png) **Figure 2.** App showing a typical list-detail layout---**1** is the list area; **2**, the detail area.

The list-detail decision should be part of the overall layout for the app, so
the decision is passed down from a content-level composable:


```kotlin
@Composable
fun AdaptivePane(
    showOnePane: Boolean,
    /* ... */
) {
    if (showOnePane) {
        OnePane(/* ... */)
    } else {
        TwoPane(/* ... */)
    }
}
```

<br />

What if you instead want a composable to independently change its layout based
on the display space available, for example, a card that shows additional
details if space allows? You want to perform some logic based on some available
display size, but which size specifically?
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/adaptive-card-title-desc.png) **Figure 3.** Narrow card showing just an icon and title, and a wider card showing the icon, title, and short description.

Avoid trying to use the size of the device's actual screen. This won't be
accurate for different types of screens and also won't be accurate if the app
isn't fullscreen.

Because the composable is not a content-level composable, don't use the current
window metrics directly.

If the component is placed with padding (such as with insets), or if the app
includes components such as navigation rails or app bars, the amount of display
space available to the composable may differ significantly from the overall
space available to the app.

Use the width that the composable is actually given to render itself. You have
two options to get that width:

- If you want to change *where* or *how* content is displayed, use a
  collection of modifiers or a [custom layout](https://developer.android.com/develop/ui/compose/layouts/custom) to make the layout
  responsive. This could be as straightforward as having a child fill all of
  the available space, or laying out children with multiple columns if there's
  enough room.

- If you want to change *what* you show, use [`BoxWithConstraints`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#BoxWithConstraints(androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)) as a
  more powerful alternative. `BoxWithConstraints` provides [measurement
  constraints](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/BoxWithConstraintsScope) that you can use to call different composables based on the
  available display space. However, this comes at some expense, as
  `BoxWithConstraints` defers composition until the layout phase, when these
  constraints are known, causing more work to be performed during layout.


```kotlin
@Composable
fun Card(/* ... */) {
    BoxWithConstraints {
        if (maxWidth < 400.dp) {
            Column {
                Image(/* ... */)
                Title(/* ... */)
            }
        } else {
            Row {
                Column {
                    Title(/* ... */)
                    Description(/* ... */)
                }
                Image(/* ... */)
            }
        }
    }
}
```

<br />

## Make all data available for different display sizes

When implementing a composable that takes advantage of extra display space, you
might be tempted to be efficient and load data as a side effect of the current
display size.

However, doing so goes against the principle of unidirectional data flow, where
data can be hoisted and provided to composables to render appropriately. Enough
data should be provided to the composable so that the composable always has
enough content for any display size, even if some portion of the content might
not always be used.


```kotlin
@Composable
fun Card(
    imageUrl: String,
    title: String,
    description: String
) {
    BoxWithConstraints {
        if (maxWidth < 400.dp) {
            Column {
                Image(imageUrl)
                Title(title)
            }
        } else {
            Row {
                Column {
                    Title(title)
                    Description(description)
                }
                Image(imageUrl)
            }
        }
    }
}
```

<br />

Building on the `Card` example, note that the `description` is always passed to
the `Card`. Even though the `description` is only used when the width permits
displaying it, `Card` always requires the `description`, regardless of the
available width.

Always passing sufficient content makes adaptive layouts simpler by making them
less stateful and avoids triggering side effects when switching between display
sizes (which may occur due to a window resize, orientation change, or folding
and unfolding a device).

This principle also allows preserving state across layout changes. By hoisting
information that may not be used at all display sizes, you can preserve app
state as the layout size changes.

For example, you can hoist a `showMore` boolean flag so that the app state is
preserved when display resizing causes the layout to switch between hiding and
showing content:


```kotlin
@Composable
fun Card(
    imageUrl: String,
    title: String,
    description: String
) {
    var showMore by remember { mutableStateOf(false) }

    BoxWithConstraints {
        if (maxWidth < 400.dp) {
            Column {
                Image(imageUrl)
                Title(title)
            }
        } else {
            Row {
                Column {
                    Title(title)
                    Description(
                        description = description,
                        showMore = showMore,
                        onShowMoreToggled = { newValue ->
                            showMore = newValue
                        }
                    )
                }
                Image(imageUrl)
            }
        }
    }
}
```

<br />

## Learn more

To learn more about adaptive layouts in Compose, see the following resources:

**Sample apps**

- [CanonicalLayouts](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts) is a repository of proven design patterns that provide an optimal user experience on large displays
- [JetNews](https://github.com/android/compose-samples/tree/main/JetNews) shows how to design an app that adapts its UI to make use of available display space
- [Reply](https://github.com/android/compose-samples/tree/main/Reply) is an adaptive sample for supporting mobile, tablets, and foldables
- [Now in Android](https://github.com/android/nowinandroid) is an app that uses adaptive layouts to support different display sizes

**Videos**

- [Build Android UIs for any screen size](https://www.youtube.com/watch/ir3LztqbeRI)
- [Form Factors \| Android Dev Summit '22](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc9jBnpl83LH6oZc7nFIVSRq)