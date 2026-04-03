---
title: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press
source: md.txt
---

Many composables have built-in support for taps or clicks and include an
`onClick` lambda. For example, you can create a clickable `Surface` that
includes all Material Design behavior appropriate for interaction with surfaces:


```kotlin
Surface(onClick = { /* handle click */ }) {
    Text("Click me!", Modifier.padding(24.dp))
}
```

<br />

But clicks are not the only way a user can interact with composables. This page
focuses on gestures that involve a single pointer, where the position of
that pointer is not significant for the handling of that event. The following
table lists these types of gestures:

|---|---|
| **Gesture** | **Description** |
| Tap (or click) | Pointer goes down and then up |
| Double tap | Pointer goes down, up, down, up |
| Long-press | Pointer goes down, and is held for a longer time |
| Press | Pointer goes down |

## Respond to tap or click

[`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)) is a commonly used modifier that makes a composable react to
taps or clicks. This modifier also adds additional features, such as support for
focus, mouse and stylus hovering, and a customizable visual indication when
pressed. The modifier responds to "clicks" in the widest sense of the word-- not
only with mouse or finger, but also click events through keyboard input or when
using accessibility services.

Imagine a grid of images, where an image shows full-screen when a user
clicks on it:

You can add the `clickable` modifier to each item in the grid to implement this
behavior:


```kotlin
@Composable
private fun ImageGrid(photos: List<Photo>) {
    var activePhotoId by rememberSaveable { mutableStateOf<Int?>(null) }
    LazyVerticalGrid(columns = GridCells.Adaptive(minSize = 128.dp)) {
        items(photos, { it.id }) { photo ->
            ImageItem(
                photo,
                Modifier.clickable { activePhotoId = photo.id }
            )
        }
    }
    if (activePhotoId != null) {
        FullScreenImage(
            photo = photos.first { it.id == activePhotoId },
            onDismiss = { activePhotoId = null }
        )
    }
}
```

<br />

The `clickable` modifier also adds additional behavior:

- `interactionSource` and `indication`, which draw a ripple by default when a user taps the composable. Learn how to customize these on the [Handling user
  interactions](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions) page.
- Allows accessibility services to interact with the element by setting the semantics information.
- Supports keyboard or joystick interaction by allowing focus and pressing `Enter` or the center of the d-pad to interact.
- Make the element hoverable, so it responds to the mouse or stylus hovering over it.

## Long-press to show a contextual context menu

[`combinedClickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).combinedClickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.String,kotlin.Function0,kotlin.Function0,kotlin.Function0)) lets you add double tap or long-press behavior in
addition to normal click behavior. You can use `combinedClickable` to show a
context menu when a user touches and holds a grid image:


```kotlin
var contextMenuPhotoId by rememberSaveable { mutableStateOf<Int?>(null) }
val haptics = LocalHapticFeedback.current
LazyVerticalGrid(columns = GridCells.Adaptive(minSize = 128.dp)) {
    items(photos, { it.id }) { photo ->
        ImageItem(
            photo,
            Modifier
                .combinedClickable(
                    onClick = { activePhotoId = photo.id },
                    onLongClick = {
                        haptics.performHapticFeedback(HapticFeedbackType.LongPress)
                        contextMenuPhotoId = photo.id
                    },
                    onLongClickLabel = stringResource(R.string.open_context_menu)
                )
        )
    }
}
if (contextMenuPhotoId != null) {
    PhotoActionsSheet(
        photo = photos.first { it.id == contextMenuPhotoId },
        onDismissSheet = { contextMenuPhotoId = null }
    )
}
```

<br />

As a best practice, you should include haptic feedback when the user
long-presses elements, which is why the snippet includes the
`performHapticFeedback` invocation.

## Dismiss a composable by tapping a scrim

In the examples above, `clickable` and `combinedClickable` add useful
functionality to your composables. They show a visual indication on interaction,
respond to hovering, and include focus, keyboard, and accessibility support. But
this extra behavior is not always desirable.

Let's look at the image detail screen. The background should be semi-transparent
and the user should be able to tap that background to dismiss the detail screen:

In this case, that background should not have any visual indication on
interaction, should not respond to hovering, should not be focusable, and its
response to keyboard and accessibility events differ from that of a typical
composable. Instead of trying to adapt the `clickable` behavior, you can drop
down to a lower abstraction level and directly use the `pointerInput` modifier
in combination with the `detectTapGestures` method:


```kotlin
@Composable
private fun Scrim(onClose: () -> Unit, modifier: Modifier = Modifier) {
    val strClose = stringResource(R.string.close)
    Box(
        modifier
            // handle pointer input
            .pointerInput(onClose) { detectTapGestures { onClose() } }
            // handle accessibility services
            .semantics(mergeDescendants = true) {
                contentDescription = strClose
                onClick {
                    onClose()
                    true
                }
            }
            // handle physical keyboard input
            .onKeyEvent {
                if (it.key == Key.Escape) {
                    onClose()
                    true
                } else {
                    false
                }
            }
            // draw scrim
            .background(Color.DarkGray.copy(alpha = 0.75f))
    )
}
```

<br />

As the key of the `pointerInput` modifier you pass the `onClose` lambda. This
automatically re-executes the lambda, making sure the right callback is called
when the user taps the scrim.

## Double tap to zoom

Sometimes `clickable` and `combinedClickable` do not include enough information
to respond to the interaction in the correct way. For example, composables might
need access to the position within the composable's bounds where the interaction
took place.

Let's look at the image detail screen again. A best practice is to make it
possible to zoom in on the image by double tapping:

As you can see in the video, zooming in occurs around the position of the tap
event. The result is different when we zoom in on the left part of the image
versus the right part. We can use the `pointerInput` modifier in combination
with the `detectTapGestures` to incorporate the tap position into our
calculation:


```kotlin
var zoomed by remember { mutableStateOf(false) }
var zoomOffset by remember { mutableStateOf(Offset.Zero) }
Image(
    painter = rememberAsyncImagePainter(model = photo.highResUrl),
    contentDescription = null,
    modifier = modifier
        .pointerInput(Unit) {
            detectTapGestures(
                onDoubleTap = { tapOffset ->
                    zoomOffset = if (zoomed) Offset.Zero else
                        calculateOffset(tapOffset, size)
                    zoomed = !zoomed
                }
            )
        }
        .graphicsLayer {
            scaleX = if (zoomed) 2f else 1f
            scaleY = if (zoomed) 2f else 1f
            translationX = zoomOffset.x
            translationY = zoomOffset.y
        }
)
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Understand gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures)
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material)
- [Kotlin for Jetpack Compose](https://developer.android.com/develop/ui/compose/kotlin)