---
title: https://developer.android.com/develop/ui/views/layout/use-window-size-classes
url: https://developer.android.com/develop/ui/views/layout/use-window-size-classes
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use window size classes in Compose. [Window size classes in Compose →](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Window size classes are a set of opinionated viewport breakpoints that help you
design, develop, and test responsive/adaptive layouts. The breakpoints balance
layout simplicity with the flexibility of optimizing your app for unique cases.

Window size classes categorize the display area available to your app as
*compact* , *medium* , *expanded* , *large* , or *extra large*. Available width and
height are classified separately, so at any point in time, your app has two
window size classes---one for width, one for height. Available width is
usually more important than available height due to the ubiquity of vertical
scrolling, so the width window size class is likely more relevant to your app's
UI.
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/window-size-classes/window_size_classes_width.png) **Figure 1.** Representations of width-based window size classes. ![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/window-size-classes/window_size_classes_height.png) **Figure 2.** Representations of height-based window size classes.

As visualized in the figures, the breakpoints allow you to continue thinking
about layouts in terms of devices and configurations. Each size class breakpoint
represents a majority case for typical device scenarios, which can be a helpful
frame of reference as you think about the design of your breakpoint-based
layouts.

| Size class | Breakpoint | Device representation |
|---|---|---|
| Compact width | width \< 600dp | 99.96% of phones in portrait |
| Medium width | 600dp ≤ width \< 840dp | 93.73% of tablets in portrait, most large unfolded inner displays in portrait |
| Expanded width | 840dp ≤ width \< 1200dp | 97.22% of tablets in landscape, most large unfolded inner displays in landscape are at least expanded width |
| Large width | 1200dp ≤ width \< 1600dp | Large tablet displays |
| Extra-large width | width ≥ 1600dp | Desktop displays |
| Compact height | height \< 480dp | 99.78% of phones in landscape |
| Medium height | 480dp ≤ height \< 900dp | 96.56% of tablets in landscape, 97.59% of phones in portrait |
| Expanded height | height ≥ 900dp | 94.25% of tablets in portrait |

> [!NOTE]
> **Note:** Most apps can build an adaptive UI by considering only the width window size class. However, also consider the height window size class for scenarios such as phones or open flippables in landscape orientation; the window width is typically medium, but window height is compact, in which case two pane layouts are not practical.

Although visualizing size classes as physical devices can be useful, window size
classes are explicitly not determined by the size of the device screen. Window
size classes are not intended for *isTablet*‑type logic. Rather, window
size classes are determined by the window size available to your application
regardless of the type of device the app is running on, which has two important
implications:

- **Physical devices do not guarantee a specific window size class.** The
  screen space available to your app can differ from the screen size of the
  device for many reasons. On mobile devices, split‑screen mode can
  partition the screen between two applications. On ChromeOS, Android apps can
  be presented in desktop‑type windows that are arbitrarily resizable.
  Foldables can have two different‑sized screens individually accessed
  by folding or unfolding the device.

- **The window size class can change throughout the lifetime of your app.**
  While your app is running, device orientation changes, multitasking, and
  folding/unfolding can change the amount of screen space available. As a
  result, the window size class is dynamic, and your app's UI should adapt
  accordingly.

Window size classes map to the compact, medium, and expanded breakpoints in the
[Material Design layout guidance](https://m3.material.io/foundations/layout/applying-layout/window-size-classes). Additionally, large and extra-large
breakpoints have been added to better target desktop and connected displays.

Use window size classes to make high‑level application layout decisions,
such as deciding whether to use a specific canonical layout to take advantage of
additional screen space.

You can compute the current
[`WindowSizeClass`](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass)
using the
[`WindowSizeClass#compute()`](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass#compute(kotlin.Float,kotlin.Float))
function provided by the [Jetpack
WindowManager](https://developer.android.com/jetpack/androidx/releases/window) library. The following example
shows how to calculate the window size class and receive updates whenever the
window size class changes:

### Kotlin

```kotlin
class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // ...

        // Replace with a known container that you can safely add a
        // view to where the view won't affect the layout and the view
        // won't be replaced.
        val container: ViewGroup = binding.container

        // Add a utility view to the container to hook into
        // View.onConfigurationChanged(). This is required for all
        // activities, even those that don't handle configuration
        // changes. You can't use Activity.onConfigurationChanged(),
        // since there are situations where that won't be called when
        // the configuration changes. View.onConfigurationChanged() is
        // called in those scenarios.
        container.addView(object : View(this) {
            override fun onConfigurationChanged(newConfig: Configuration?) {
                super.onConfigurationChanged(newConfig)
                computeWindowSizeClasses()
            }
        })

        computeWindowSizeClasses()
    }

    private fun computeWindowSizeClasses() {
        val metrics = WindowMetricsCalculator.getOrCreate().computeCurrentWindowMetrics(this)
        val width = metrics.bounds.width()
        val height = metrics.bounds.height()
        val density = resources.displayMetrics.density
        val windowSizeClass = WindowSizeClass.compute(width/density, height/density)
        // COMPACT, MEDIUM, or EXPANDED
        val widthWindowSizeClass = windowSizeClass.windowWidthSizeClass
        // COMPACT, MEDIUM, or EXPANDED
        val heightWindowSizeClass = windowSizeClass.windowHeightSizeClass

        // Use widthWindowSizeClass and heightWindowSizeClass.
    }
}
```

### Java

```java
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // ...

        // Replace with a known container that you can safely add a
        // view to where the view won't affect the layout and the view
        // won't be replaced.
        ViewGroup container = binding.container;

        // Add a utility view to the container to hook into
        // View.onConfigurationChanged(). This is required for all
        // activities, even those that don't handle configuration
        // changes. You can't use Activity.onConfigurationChanged(),
        // since there are situations where that won't be called when
        // the configuration changes. View.onConfigurationChanged() is
        // called in those scenarios.
        container.addView(new View(this) {
            @Override
            protected void onConfigurationChanged(Configuration newConfig) {
                super.onConfigurationChanged(newConfig);
                computeWindowSizeClasses();
            }
        });

        computeWindowSizeClasses();
    }

    private void computeWindowSizeClasses() {
        WindowMetrics metrics = WindowMetricsCalculator.getOrCreate()
                .computeCurrentWindowMetrics(this);

        int width = metrics.getBounds().width();
        int height = metrics.getBounds().height();
        float density = getResources().getDisplayMetrics().density;
        WindowSizeClass windowSizeClass = WindowSizeClass.compute(width/density, height/density);
        // COMPACT, MEDIUM, or EXPANDED
        WindowWidthSizeClass widthWindowSizeClass = windowSizeClass.getWindowWidthSizeClass();
        // COMPACT, MEDIUM, or EXPANDED
        WindowHeightSizeClass heightWindowSizeClass = windowSizeClass.getWindowHeightSizeClass();

        // Use widthWindowSizeClass and heightWindowSizeClass.
    }
}
```

## Test window size classes

As you make layout changes, test the layout behavior across all window sizes,
especially at the compact, medium, and expanded breakpoint widths.

If you have an existing layout for compact screens, first optimize your layout
for the expanded width size class, since this size class provides the most space
for additional content and UI changes. Then decide what layout makes sense for
the medium width size class; consider adding a specialized layout.

## Next steps

To learn more about how to use window size classes to create responsive/adaptive
layouts, see the following:

- For Compose-based layouts: [Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)

- For view-based layouts: [Responsive/adaptive design with views](https://developer.android.com/develop/ui/views/layout/responsive-adaptive-design-with-views)

To learn more about what makes an app great on all devices and screen sizes,
see:

- [Migrate your UI to responsive layouts](https://developer.android.com/guide/topics/large-screens/migrate-to-responsive-layouts)
- [Large screen app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)