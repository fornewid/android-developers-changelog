---
title: https://developer.android.com/develop/ui/views/text-and-emoji/magnifier
url: https://developer.android.com/develop/ui/views/text-and-emoji/magnifier
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use text in Compose. [Modifier.magnifier() →](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).magnifier(kotlin.Function1,kotlin.Function1,kotlin.Float,androidx.compose.foundation.MagnifierStyle,kotlin.Function1)) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Available in Android 9 (API level 28) and later, the magnifier widget is a
virtual magnifying glass that displays an enlarged copy of a `View` through an
overlay pane that represents the lens. The feature improves the text insertion
and selection user experience. When applying the magnifier to text, a user can
precisely position the cursor or the selection handles by viewing the magnified
text in a pane that follows their finger.

Figure 1 shows how the magnifier facilitates selecting text. The magnifier APIs
aren't tied to text, and you can use this widget in a variety of use cases, such
as reading small text or enlarging hard-to-see place names on maps.
![An image showing how the magnifier appears after grabbing the right selection handle](https://developer.android.com/static/develop/ui/views/text-and-emoji/images/magnifier-1.png) **Figure 1.** Magnifying text. When the user drags the right selection handle, the magnifier pops up to help with accurate placement.

The magnifier is already integrated with platform widgets such as `TextView`,
`EditText`, and `WebView`. It provides consistent text manipulation across apps.
The widget comes with a simple API and can be used to magnify any `View`
depending on your app's context.

## API usage

You can use the magnifier programmatically on an arbitrary view as follows:

### Kotlin

```kotlin
val view: View = findViewById(R.id.view)
val magnifier = Magnifier.Builder(view).build()
magnifier.show(view.width / 2.0f, view.height / 2.0f)
```

### Java

```java
View view = findViewById(R.id.view);
Magnifier magnifier = new Magnifier.Builder(view).build();
magnifier.show(view.getWidth() / 2, view.getHeight() / 2);
```

Assuming the view hierarchy has the first layout, the magnifier displays on the
screen and contains a region centered on the given coordinates within the view.
The pane appears above the center point of the content being copied. The
magnifier persists indefinitely until the user dismisses it.

> [!NOTE]
> **Note:** The arguments of [`show()`](https://developer.android.com/reference/android/widget/Magnifier#show(float,%20float)) are relative to the top-left corner of the view being magnified.

The following code snippet shows how to change the background of the magnified
view:

### Kotlin

```kotlin
view.setBackgroundColor(...)
```

### Java

```java
view.setBackgroundColor(...);
```

Assuming the background color is visible within the magnifier, the magnifier's
content is stale, as a region of the view with the old background still
displays. To refresh the content, use the
[`update()`](https://developer.android.com/reference/android/widget/Magnifier#update()) method, as follows:

### Kotlin

```kotlin
view.post { magnifier.update() }
```

### Java

```java
view.post(magnifier::update);
```

> [!NOTE]
> **Note:** Post the update operation to make sure that by the time this executes, the view with the new background color is already drawn. This is because the magnifier content always stays a frame behind the magnified view.

When finished, close the magnifier by calling the
[`dismiss()`](https://developer.android.com/reference/android/widget/Magnifier#dismiss()) method:

### Kotlin

```kotlin
magnifier.dismiss()
```

### Java

```java
magnifier.dismiss();
```

## Magnify on user interaction

A common use case for the magnifier is to let the user enlarge a view region by
touching it, as shown in figure 2.
**Figure 2.** The magnifier follows the user's touch. It is applied to a `ViewGroup` that contains an \`ImageView\` to the left and a `TextView` to the right.

You can do this by updating the magnifier according to the touch events received
by the view, as follows:

### Kotlin

```kotlin
imageView.setOnTouchListener { v, event ->
  when (event.actionMasked) {
    MotionEvent.ACTION_DOWN, MotionEvent.ACTION_MOVE -> {
      val viewPosition = IntArray(2)
      v.getLocationOnScreen(viewPosition)
      magnifier.show(event.rawX - viewPosition[0], event.rawY - viewPosition[1])
    }
    MotionEvent.ACTION_CANCEL, MotionEvent.ACTION_UP -> {
      magnifier.dismiss()
    }
  }
  true
}
```

### Java

```java
imageView.setOnTouchListener(new View.OnTouchListener() {
    @Override
    public boolean onTouch(View v, MotionEvent event) {
        switch (event.getActionMasked()) {
            case MotionEvent.ACTION_DOWN:
                // Fall through.
            case MotionEvent.ACTION_MOVE: {
                final int[] viewPosition = new int[2];
                v.getLocationOnScreen(viewPosition);
                magnifier.show(event.getRawX() - viewPosition[0],
                               event.getRawY() - viewPosition[1]);
                break;
            }
            case MotionEvent.ACTION_CANCEL:
                // Fall through.
            case MotionEvent.ACTION_UP: {
                magnifier.dismiss();
            }
        }
        return true;
    }
});
```

> [!NOTE]
> **Note:** The magnifier never displays magnified content that doesn't belong to the view, even when the view is included in scrollable containers and partially masked. When the coordinates passed to `show()` imply copying outside content, they are coerced inside the visible region of the view.

## Additional considerations when magnifying text

For the platform text widgets, it's important to understand specific magnifier
behaviors and to enable the magnifier for your custom text view consistently
across the Android platform. Consider the following:

- The magnifier is triggered immediately when the user grabs an insertion or selection handle.
- The magnifier always smoothly follows the user's finger horizontally, while vertically it is fixed to the center of the current text line.
- When moving horizontally, the magnifier moves only between the left and right bounds of the current line. Moreover, when the user's touch leaves these bounds and the horizontal distance between the touch and the closest bound is larger than half of the original width of the magnifier content, the magnifier is dismissed, as the cursor is no longer visible inside the magnifier.
- The magnifier is never triggered when the text font is too large. Text is considered too large when the difference between the font's descent and ascent is larger than the height of the content that fits in the magnifier. Triggering the magnifier in this case doesn't add value.