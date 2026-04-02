---
title: https://developer.android.com/develop/ui/views/layout/immersive
url: https://developer.android.com/develop/ui/views/layout/immersive
source: md.txt
---

Some content is best experienced in fullscreen without any indicators on the
status bar or the navigation bar. Some examples are videos, games, image
galleries, books, and presentation slides. This is referred to as
*immersive mode*. This page shows how you can engage users more deeply with
content in fullscreen.
![](https://developer.android.com/static/design/media/fullscreen_landing.png) **Figure 1.** Example of immersive mode.

Immersive mode helps users avoid accidental exits during a game and
delivers an immersive experience for enjoying images, videos, and books.
However, be mindful of how often users jump in and out of apps to check notifications,
to conduct impromptu searches, or to take other actions. Because immersive mode
causes users to lose easy access to system navigation, use immersive mode only
when the benefit to the user experience goes beyond simply using extra screen
space.

Use [`WindowInsetsControllerCompat.hide()`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#hide(int))
to hide the system bars and [`WindowInsetsControllerCompat.show()`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#show(int))
to bring them back.

The following snippet shows an example of configuring a button to hide and show
the system bars.

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    ...

    val windowInsetsController =
        WindowCompat.getInsetsController(window, window.decorView)
    // Configure the behavior of the hidden system bars.
    windowInsetsController.systemBarsBehavior =
        WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE

    // Add a listener to update the behavior of the toggle fullscreen button when
    // the system bars are hidden or revealed.
    ViewCompat.setOnApplyWindowInsetsListener(window.decorView) { view, windowInsets ->
        // You can hide the caption bar even when the other system bars are visible.
        // To account for this, explicitly check the visibility of navigationBars()
        // and statusBars() rather than checking the visibility of systemBars().
        if (windowInsets.isVisible(WindowInsetsCompat.Type.navigationBars())
            || windowInsets.isVisible(WindowInsetsCompat.Type.statusBars())) {
            binding.toggleFullscreenButton.setOnClickListener {
                // Hide both the status bar and the navigation bar.
                windowInsetsController.hide(WindowInsetsCompat.Type.systemBars())
            }
        } else {
            binding.toggleFullscreenButton.setOnClickListener {
                // Show both the status bar and the navigation bar.
                windowInsetsController.show(WindowInsetsCompat.Type.systemBars())
            }
        }
        ViewCompat.onApplyWindowInsets(view, windowInsets)
    }
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    ...

    WindowInsetsControllerCompat windowInsetsController =
            WindowCompat.getInsetsController(getWindow(), getWindow().getDecorView());
    // Configure the behavior of the hidden system bars.
    windowInsetsController.setSystemBarsBehavior(
            WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
    );

    // Add a listener to update the behavior of the toggle fullscreen button when
    // the system bars are hidden or revealed.
    ViewCompat.setOnApplyWindowInsetsListener(
        getWindow().getDecorView(),
        (view, windowInsets) -> {
        // You can hide the caption bar even when the other system bars are visible.
        // To account for this, explicitly check the visibility of navigationBars()
        // and statusBars() rather than checking the visibility of systemBars().
        if (windowInsets.isVisible(WindowInsetsCompat.Type.navigationBars())
                || windowInsets.isVisible(WindowInsetsCompat.Type.statusBars())) {
            binding.toggleFullscreenButton.setOnClickListener(v -> {
                // Hide both the status bar and the navigation bar.
                windowInsetsController.hide(WindowInsetsCompat.Type.systemBars());
            });
        } else {
            binding.toggleFullscreenButton.setOnClickListener(v -> {
                // Show both the status bar and the navigation bar.
                windowInsetsController.show(WindowInsetsCompat.Type.systemBars());
            });
        }
        return ViewCompat.onApplyWindowInsets(view, windowInsets);
    });
}
```

Optionally, you can specify the type of system bars to hide and determine
their behavior when a user interacts with them.

#### Specify which system bars to hide

To specify the type of system bars to hide, pass one of the following parameters
to `WindowInsetsControllerCompat.hide()`.

- Use [`WindowInsetsCompat.Type.systemBars()`](https://developer.android.com/reference/kotlin/androidx/core/view/WindowInsetsCompat.Type#systembars) to
  hide both system bars.

- Use [`WindowInsetsCompat.Type.statusBars()`](https://developer.android.com/reference/kotlin/androidx/core/view/WindowInsetsCompat.Type#statusbars) to
  hide only the status bar.

- Use [`WindowInsetsCompat.Type.navigationBars()`](https://developer.android.com/reference/kotlin/androidx/core/view/WindowInsetsCompat.Type#navigationbars) to
  hide only the navigation bar.

#### Specify behavior of hidden system bars

Use [`WindowInsetsControllerCompat.setSystemBarsBehavior()`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#setSystemBarsBehavior(int))
to specify how hidden system bars behave when the user interacts with them.

- Use [`WindowInsetsControllerCompat.BEHAVIOR_SHOW_BARS_BY_TOUCH`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#BEHAVIOR_SHOW_BARS_BY_TOUCH())
  to reveal hidden system bars on *any* user interactions on the corresponding
  display.

- Use [`WindowInsetsControllerCompat.BEHAVIOR_SHOW_BARS_BY_SWIPE`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#BEHAVIOR_SHOW_BARS_BY_SWIPE())
  to reveal hidden system bars on any system gestures, such as swiping from
  the edge of the screen where the bar is hidden from.

- Use [`WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat#BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE())
  to temporarily reveal hidden system bars with system gestures, such as
  swiping from the edge of the screen where the bar is hidden from. These
  transient system bars overlay your app's content, might have some degree of
  transparency, and are automatically hidden after a short timeout.