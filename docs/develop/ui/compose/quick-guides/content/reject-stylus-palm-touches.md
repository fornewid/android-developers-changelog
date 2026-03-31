---
title: Reject stylus palm touches  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/reject-stylus-palm-touches
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Reject stylus palm touches Stay organized with collections Save and categorize content based on your preferences.




When users draw, write, or interact with an app using a stylus, they sometimes
touch the screen with the palm of their hands. The touch event might be reported
to your app before the system recognizes and dismisses the event as an
accidental palm touch.

Your app must identify extraneous touch events and ignore them. Android 13 and
higher API levels indicate palm touches differently from all other API levels.

## Results

Your app is able to identify and reject palm touches for multi-pointer events on
Android 13 and higher API levels and for single-pointer events on all API
levels.

## Version compatibility

Set your project's `minSDK` to API level 33 for multi‑pointer events.
Single‑pointer events are supported on API levels.

### Dependencies

None.

## Identify and ignore palm touches

Android cancels a palm touch by dispatching a [`MotionEvent`](/reference/kotlin/android/view/MotionEvent) object to your
app.

* Examine `MotionEvent` objects dispatched to your app. Use the `MotionEvent`
  APIs to determine event properties (actions and flags):

  + **Single-pointer events** — Check for [`ACTION_CANCEL`](/reference/kotlin/android/view/MotionEvent#action_cancel). On
    Android 13 and higher, also check for [`FLAG_CANCELED`](/reference/kotlin/android/view/MotionEvent#flag_canceled).
  + **Multi-pointer events** — On Android 13 and higher, check for
    [`ACTION_POINTER_UP`](/reference/kotlin/android/view/MotionEvent#action_pointer_up) and `FLAG_CANCELED`.
* Ignore motion events that have the `ACTION_CANCEL` and
  `ACTION_POINTER_UP`/`FLAG_CANCELED` properties.

**Warning:** Android 12 (API level 32) and lower provide only `ACTION_POINTER_UP`
for non-primary multi-pointer events. `FLAG_CANCELED` is not set for cancelable
events such as palm touches. As a result, apps cannot determine whether the
touch was intended or not on Android 12 and lower.

### 1. Acquire motion event objects

Add an [`OnTouchListener`](/reference/kotlin/android/view/View.OnTouchListener) to your app:

### Kotlin

```
val myView = findViewById&lt;View&gt;(R.id.myView).apply {
    setOnTouchListener { view, event ->
        // Process motion event.
    }
}
```

### Java

```
View myView = findViewById(R.id.myView);
myView.setOnTouchListener( (view, event) -> {
    // Process motion event.
});
```

### 2. Determine the event action and flags

Check for `ACTION_CANCEL`, which indicates a single-pointer event on all API
levels. On Android 13 and higher, check `ACTION_POINTER_UP` for `FLAG_CANCELED.`

### Kotlin

```
val myView = findViewById&lt;View&gt;(R.id.myView).apply {
    setOnTouchListener { view, event ->
        when (event.actionMasked) {
            MotionEvent.ACTION_CANCEL -> {
                //Process canceled single-pointer motion event for all SDK versions.
            }
            MotionEvent.ACTION_POINTER_UP -> {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU &&
                   (event.flags and MotionEvent.FLAG_CANCELED) == MotionEvent.FLAG_CANCELED) {
                    //Process canceled multi-pointer motion event for Android 13 and higher.
                }
            }
        }
        true
    }
}
```

### Java

```
View myView = findViewById(R.id.myView);
myView.setOnTouchListener( (view, event) -> {
    switch (event.getActionMasked()) {
        case MotionEvent.ACTION_CANCEL:
            // Process canceled single-pointer motion event for all SDK versions.
        case MotionEvent.ACTION_UP:
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU &&
               (event.getFlags() & MotionEvent.FLAG_CANCELED) == MotionEvent.FLAG_CANCELED) {
                //Process canceled multi-pointer motion event for Android 13 and higher.
            }
    }
    return true;
});
```

### 3. Undo the gesture

After you've identified a palm touch, you can undo the onscreen effects of the
gesture.

Your app must keep a history of user actions so that unintended inputs such as
palm touches can be undone. For an example of how to maintain history, see
[Implement a basic drawing app](/codelabs/large-screens/advanced-stylus-support#2) in the [Enhance stylus support in an Android
app](/codelabs/large-screens/advanced-stylus-support) codelab.

## Key points

* [`MotionEvent`](/reference/kotlin/android/view/MotionEvent): Represents touch and movement events. Contains the
  information necessary to determine whether an event should be disregarded.
* [`OnTouchListener#onTouch()`](/reference/kotlin/android/view/View.OnTouchListener#ontouch): Receives `MotionEvent` objects.
* [`MotionEvent#getActionMasked()`](/reference/kotlin/android/view/MotionEvent#getactionmasked): Returns the action associated with a
  motion event.
* [`ACTION_CANCEL`](/reference/kotlin/android/view/MotionEvent#action_cancel): `MotionEvent` constant that indicates a gesture should
  be undone.
* [`ACTION_POINTER_UP`](/reference/kotlin/android/view/MotionEvent#action_pointer_up): `MotionEvent` constant that indicates a pointer
  other than the first pointer has gone up (that is, has relinquished contact
  with the device screen).
* [`FLAG_CANCELED`](/reference/kotlin/android/view/MotionEvent#flag_canceled): `MotionEvent` constant that indicates that the pointer
  going up caused an unintentional touch event. Added to `ACTION_POINTER_UP`
  and `ACTION_CANCEL` events on Android 13 (API level 33) and higher.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader
Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Optimize for large screens

Enable your app to support an optimized user experience on tablets, foldables, and ChromeOS devices.

[Quick guide collection](/quick-guides/collections/optimize-for-large-screens)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)