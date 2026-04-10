---
title: https://developer.android.com/develop/ui/views/layout/webapps/understand-window-insets
url: https://developer.android.com/develop/ui/views/layout/webapps/understand-window-insets
source: md.txt
---

WebView manages content alignment using two viewports: the [layout viewport](https://developer.mozilla.org/en-US/docs/Glossary/Layout_viewport)
(the page size) and the [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport) (the part of the page the user
actually sees). While the layout viewport is generally static, the visual
viewport changes dynamically when users zoom, scroll, or when system UI elements
(such as the software keyboard) appear.

## Feature compatibility

WebView support for window insets has evolved over time to align web content
behavior with native Android app expectations:

| Milestone | Feature added | Scope |
|---|---|---|
| M136 | `displayCutout()` and `systemBars()` support through CSS safe-area-insets. | Fullscreen WebViews only. |
| M139 | `ime()` (input method editor, which is a keyboard) support through visual viewport resizing. | All WebViews. |
| M144 | `displayCutout()` and `systemBars()` support. | All WebViews (regardless of fullscreen state). |

For more information, see [`WindowInsetsCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat).

## Core mechanics

WebView handles insets through two primary mechanisms:

- **Safe areas (`displayCutout`, `systemBars`):** WebView forwards these
  dimensions to web content through CSS safe-area-inset-\* variables. This
  enables developers to prevent their own interactive elements (like navigation
  bars) from being obscured by notches or status bars.

- **Visual viewport resizing using the input method editor (IME):** Starting in
  M139, the input method editor (IME) directly resizes the visual viewport. This
  resizing mechanism is also based on the WebView-Window intersection. For
  example, in Android multitasking mode, if the bottom of a WebView extends
  200dp below the bottom of the window, the visual viewport is 200dp smaller
  than the size of the WebView. This visual viewport resizing (for both IME and
  WebView-Window intersection) is only applied to the bottom of the WebView.
  This mechanism doesn't support resizing for left, right, or top overlap. This
  means that docked keyboards appearing on those edges don't trigger a visual
  viewport resize.

Previously, the visual viewport remained fixed, often hiding input fields behind
the keyboard. By resizing the viewport, the visible portion of the page becomes
scrollable by default, ensuring users can reach obscured content.

## Bounds and overlap logic

WebView should receive non-zero inset values only when system UI elements (bars,
display cutouts, or the keyboard) directly overlap with the WebView's screen
bounds. If a WebView doesn't overlap with these UI elements (such as, if a
WebView is centered on the screen and doesn't touch the system bars), it should
receive those insets as zero.

To override this default logic and provide the web content with the complete
system dimensions regardless of overlap, use the
`setOnApplyWindowInsetsListener` method and return the original, unmodified
`windowInsets` object from the listener. Providing complete system dimensions
can help ensure design consistency by enabling web content to align with the
device hardware regardless of the WebView's current position. This ensures a
smooth transition as the WebView moves or expands to touch the screen edges.

### Kotlin

    ViewCompat.setOnApplyWindowInsetsListener(myWebView) { _, windowInsets ->
        // By returning the original windowInsets object, we override the default
        // behavior that zeroes out system insets (like system bars or display
        // cutouts) when they don't directly overlap the WebView's screen bounds.
        windowInsets
    }

### Java

    ViewCompat.setOnApplyWindowInsetsListener(myWebView, (v, windowInsets) -> {
      // By returning the original windowInsets object, we override the default
      // behavior that zeroes out system insets (like system bars or display
      // cutouts) when they don't directly overlap the WebView's screen bounds.
      return windowInsets;
    });

> [!CAUTION]
> **Caution:** Returning the original `windowInsets` object overrides WebView's default bounds-checking, but can cause double-padding if your native UI also applies padding based on window insets. To know how to avoid this, see [Implement inset handling](https://developer.android.com/develop/ui/views/layout/webapps/understand-window-insets#inset-handling).

## Manage resize events

Because keyboard visibility now triggers a visual viewport resize, web code
might see more frequent resize events. Developers must ensure their code doesn't
react to these resize events by clearing element focus. Doing so creates a loop
of focus loss and keyboard dismissal that prevents user input:

1. The user focuses on an input element.
2. The keyboard appears, triggering a resize event.
3. The website's code clears focus in response to the resize.
4. The keyboard hides because the focus was lost.

To mitigate this behavior, review web-side listeners to ensure that viewport
changes don't unintentionally trigger the `blur()` JavaScript function or
focus-clearing behaviors.

## Implement inset handling

WebView's default settings work automatically for most apps. However, if your
app uses custom layouts (for example, if you add your own padding to account for
the status bar or keyboard), you can use the following approaches to improve how
the web content and native UI work together. If your native UI applies padding
to a container based on [`WindowInsets`](https://developer.android.com/reference/android/view/WindowInsets), you must manage these insets
correctly before they reach the WebView to avoid double-padding.

Double-padding is a situation where the native layout and the web content apply
the same inset dimensions, resulting in redundant spacing. For example, imagine
a phone with a 40px status bar. Both the native view and the WebView see the
40px inset. Both add 40px of padding, resulting in the user seeing an 80px gap
at the top.

## The *Zeroing* approach

To prevent double-padding, you must ensure that after a native view uses an
inset dimension for padding, you reset that dimension to zero using
`Insets.NONE` on a new `WindowInsets` object before passing the modified object
down the view hierarchy to the WebView.

When applying padding to a parent view, you should generally use the zeroing
approach by setting `Insets.NONE` instead of `WindowInsetsCompat.CONSUMED`.
Returning `WindowInsetsCompat.CONSUMED` might work in certain situations.
However, it can run into issues if your app's handler changes insets or adds its
own padding. The zeroing approach doesn't have these limitations.

### Avoid ghost padding by zeroing insets

If you consume the insets when the app has previously passed non-consumed
insets, or if the insets change (like the keyboard hiding), consuming them
prevents the WebView from receiving the necessary update notification. This can
cause the WebView to retain ghost padding from a previous state (for example,
keeping keyboard padding after the keyboard is hidden).

The following example shows a broken interaction between the app and WebView:

1. **Initial state:** The app initially passes non-consumed insets (for example, `displayCutout()` or `systemBars()`) to the WebView, which internally applies padding to the web content.
2. **State change and error:** If the app changes state (for example, the keyboard hides) and the app chooses to handle the resulting insets by returning `WindowInsetsCompat.CONSUMED`.
3. **Notification blocked:** Consuming the insets prevents the Android system from sending the necessary update notification down the view hierarchy to the WebView.
4. **Ghost padding:** Because the WebView doesn't receive the update, it retains the padding from the previous state, causing ghost padding (for example, keeping keyboard padding after the keyboard is hidden).

Instead, use the [`WindowInsetsCompat.Builder`](https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat.Builder) to set the handled types to
zero before passing the object to the child views. This informs the WebView that
those specific insets have already been accounted for while enabling the
notification to continue down the view hierarchy.

### Kotlin

    ViewCompat.setOnApplyWindowInsetsListener(rootView) { view, windowInsets ->
        // 1. Identify the inset types you want to handle natively
        val types = WindowInsetsCompat.Type.systemBars() or WindowInsetsCompat.Type.displayCutout()

        // 2. Extract the dimensions and apply them as padding to the native container
        val insets = windowInsets.getInsets(types)
        view.setPadding(insets.left, insets.top, insets.right, insets.bottom)

        // 3. Return a new WindowInsets object with the handled types set to NONE (zeroed).
        // This informs the WebView that these areas are already padded, preventing
        // double-padding while still allowing the WebView to update its internal state.
        WindowInsetsCompat.Builder(windowInsets)
            .setInsets(types, Insets.NONE)
            .build()
    }

### Java

    ViewCompat.setOnApplyWindowInsetsListener(rootView, (view, windowInsets) -> {
      // 1. Identify the inset types you want to handle natively
      int types = WindowInsetsCompat.Type.systemBars() | WindowInsetsCompat.Type.displayCutout();

      // 2. Extract the dimensions and apply them as padding to the native container
      Insets insets = windowInsets.getInsets(types);
      rootView.setPadding(insets.left, insets.top, insets.right, insets.bottom);

      // 3. Return a new Insets object with the handled types set to NONE (zeroed).
      // This informs the WebView that these areas are already padded, preventing
      // double-padding while still allowing the WebView to update its internal
      // state.
      return new WindowInsetsCompat.Builder(windowInsets)
        .setInsets(types, Insets.NONE)
        .build();
    });

## How to opt out

To disable these modern behaviors and return to legacy viewport handling, do the
following:

1. **Intercept insets:** Use [`setOnApplyWindowInsetsListener`](https://developer.android.com/reference/android/view/View.OnApplyWindowInsetsListener) or override
   [`onApplyWindowInsets`](https://developer.android.com/reference/android/view/View#onApplyWindowInsets(android.view.WindowInsets)) in a `WebView` subclass.

2. **Clear insets:** Return a consumed set of insets (for example,
   `WindowInsetsCompat.CONSUMED`) from the start. This action prevents the inset
   notification from propagating to the WebView altogether, effectively
   disabling modern viewport resizing and forcing the WebView to retain its
   initial visual viewport size.

> [!NOTE]
> **Note:** If you opt out, you must manually manage layout resizing. Failure to do so can prevent the [`scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView) JavaScript function from functioning correctly, causing the keyboard to cover active input fields.