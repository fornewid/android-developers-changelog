---
title: https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens
url: https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens
source: md.txt
---

On large screen devices, users often interact with apps using a keyboard, mouse,
trackpad, stylus, or gamepad. To enable your app to accept input from external
devices, do the following:

- **Test basic keyboard support** , such as <kbd>Ctrl+Z</kbd> for undo, <kbd>Ctrl+C</kbd> for copy, and <kbd>Ctrl+S</kbd> for save. See [Handle keyboard actions](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands) for a list of default keyboard shortcuts.
- **Test advanced keyboard support** , for example, <kbd>Tab</kbd> key and arrow key keyboard navigation, <kbd>Enter</kbd> key text entry confirmation, and <kbd>Spacebar</kbd> play and pause in media apps.
- **Test basic mouse interactions**, including right-click for context menu, icon changes on hover, and mouse wheel or trackpad scroll events on custom components.
- **Test app-specific input devices** such as a stylus, game controllers, and music app MIDI controllers.
- **Consider advanced input support** that could make the app stand out in desktop environments, for example, touchpad as a cross‑fader for DJ apps, mouse capture for games, and keyboard shortcuts for keyboard‑centric users.

## Keyboard

The way your app responds to keyboard input contributes to the large screen user
experience. There are three kinds of keyboard input: [navigation](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#navigation),
[keystrokes](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#keystrokes), and [shortcuts](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#shortcuts).

### Navigation

Keyboard navigation is rarely implemented in touch‑centric apps, but users
expect it when they're using an app and have their hands on a keyboard. Keyboard
navigation can be essential on phones, tablets, foldables, and desktop devices
for users with accessibility needs.

For many apps, arrow key and <kbd>Tab</kbd> key navigation are handled
automatically by the Android framework. For example, some composables are
focusable by default, such as a [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) or a composable with the
[`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)) modifier; keyboard navigation should generally work without any
additional code. To enable keyboard navigation for custom composables that are
not focusable by default, add the [`focusable`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusable(kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource)) modifier:


```kotlin
var color by remember { mutableStateOf(Green) }
Box(
    Modifier
        .background(color)
        .onFocusChanged { color = if (it.isFocused) Blue else Green }
        .focusable()
) {
    Text("Focusable 1")
}
```

<br />

For more information, see [Making a composable focusable](https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-behavior#making-composable-focusable).

When focus is enabled, the Android framework creates a navigational mapping for
all focusable components based on their position. This usually works as expected
and no further development is needed.

However, Compose doesn't always determine the correct next item for tabbed
navigation for complex composables like tabs and lists, for example, when one of
the composables is a horizontal scrollable that is not fully visible.

To control focus behavior, add the [`focusGroup`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusGroup()) modifier to the parent
composable of a collection of composables. Focus moves to the group, then
through the group before moving to the next focusable component, for example:

    Row {
        Column(Modifier.focusGroup()) {
            Button({}) { Text("Row1 Col1") }
            Button({}) { Text("Row2 Col1") }
            Button({}) { Text("Row3 Col1") }
        }
        Column(Modifier.focusGroup()) {
            Button({}) { Text("Row1 Col2") }
            Button({}) { Text("Row2 Col2") }
            Button({}) { Text("Row3 Col2") }
        }
    }

For more information, see [Provide coherent navigation with focus groups](https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-behavior#provide-coherent).

Test access to every UI element of your app using the keyboard only. Frequently
used elements should be accessible without mouse or touch input.

Remember, keyboard support might be essential for users with accessibility
needs.

### Keystrokes

For text input that would be handled by an on screen virtual keyboard ([IME](https://developer.android.com/guide/topics/text/creating-input-method)),
such as for

a [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors))

, apps should behave as expected on large screen devices with no additional
development work. For keystrokes that cannot be anticipated by the framework,
apps need to handle the behavior themselves. This is especially true for apps
with custom views.

Some examples are chat apps that use the <kbd>Enter</kbd> key to send a message,
media apps that start and stop playback with the <kbd>Spacebar</kbd>, and games
that control movement with the <kbd>w</kbd>, <kbd>a</kbd>, <kbd>s</kbd>, and
<kbd>d</kbd> keys.

You can handle individual keystrokes with the [`onKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/package-summary#(androidx.compose.ui.Modifier).onKeyEvent(kotlin.Function1)) modifier, which
accepts a lambda that's called when the modified component receives a key event.
The [`KeyEvent#type`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).type()) property enables you to determine whether the event is a
key press ([`KeyDown`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEventType#KeyDown())) or key release ([`KeyUp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEventType#KeyUp())):

    Box(
        modifier = Modifier.focusable().onKeyEvent {
            if(
                it.type == KeyEventType.KeyUp &&
                it.key == Key.S
            ) {
                doSomething()
                true
            } else {
                false
            }
        }
    )  {
        Text("Press S key")
    }

Alternatively, you can override the [`onKeyUp()`](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback#onKeyUp(int,%20android.view.KeyEvent)) callback and add the
expected behavior for each received keycode:
`kotlin
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
return when (keyCode) {
KeyEvent.KEYCODE_ENTER -> {
sendChatMessage()
true
}
KeyEvent.KEYCODE_SPACE -> {
playOrPauseMedia()
true
}
else -> super.onKeyUp(keyCode, event)
}
}`

An [`onKeyUp`](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback#onKeyUp(int,%20android.view.KeyEvent)) event occurs when a key is released. Using the callback
prevents apps from needing to process multiple [`onKeyDown`](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback#onKeyDown(int,%20android.view.KeyEvent)) events if a key
is held down or released slowly. Games and apps that need to detect the moment a
key is pressed or whether the user is holding a key down can listen for the
`onKeyDown` event and handle repeated `onKeyDown` events themselves.

> [!NOTE]
> **Note:** Depending on your app's needs, you can override `onKeyUp()` for the entire activity, or you can handle individual keystrokes with the [`onKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/package-summary#(androidx.compose.ui.Modifier).onKeyEvent(kotlin.Function1)) modifier. With `onKeyEvent`, an app can, for example, listen for the <kbd>Enter</kbd> key in a specific `TextField` to implement *send* functionality only when the user is typing in a chat box.

For more information, see [Handle keyboard actions](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands).

### Shortcuts

Common keyboard shortcuts that include the <kbd>Ctrl</kbd>, <kbd>Alt</kbd>,
<kbd>Shift</kbd>, and <kbd>Meta</kbd> keys are expected when using a hardware
keyboard. If an app doesn't implement shortcuts, the experience can feel
frustrating to users. Advanced users also appreciate shortcuts for frequently
used app‑specific tasks. Shortcuts make an app easier to use and
differentiate it from apps that don't have shortcuts.

> [!NOTE]
> **Note:** On macOS keyboards, the <kbd>Meta</kbd> key is the <kbd>Command</kbd> key; on Windows keyboards, the <kbd>Windows</kbd> key; on ChromeOS keyboards, the <kbd>Search</kbd> key.

Some common shortcuts include <kbd>Ctrl+S</kbd> (save), <kbd>Ctrl+Z</kbd>
(undo), and <kbd>Ctrl+Shift+Z</kbd> (redo). For a list of default shortcuts, see
[Handle keyboard actions](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands).

A [`KeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent)) object has the following attributes which indicate whether
modifier keys are pressed:

- [`isAltPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isAltPressed())
- [`isCtrlPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isCtrlPressed())
- [`isMetaPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isMetaPressed())
- [`isShiftPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isShiftPressed())

For example:

    Box(
        Modifier.onKeyEvent {
            if (it.isAltPressed && it.key == Key.A) {
                println("Alt + A is pressed")
                true
            } else {
                false
            }
        }
        .focusable()
    )

For more information, see the following:

- [Modifier keys](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands#modifier_keys)
- [Keyboard Shortcuts Helper](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper)

## Stylus

Many large screen devices come with a stylus. Android apps handle styluses as
touchscreen input. Some devices might also have a USB or Bluetooth drawing
table, like the [Wacom Intuos](https://www.wacom.com/en-us/products/pen-tablets/wacom-intuos). Android apps can receive bluetooth
input but not USB input.

To access stylus [`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent) objects, add the [`pointerInteropFilter`](https://developer.android.com/develop/ui/compose/modifiers-list#Pointer)
modifier to a drawing surface. Implement a [`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) class with a method that
processes motion events; pass the method as the `onTouchEvent` lambda of the
`pointerInteropFilter` modifier:

    @Composable
    @OptIn(ExperimentalComposeUiApi::class)
    fun DrawArea(modifier: Modifier = Modifier) {
       Canvas(modifier = modifier
           .clipToBounds()
           .pointerInteropFilter {
               viewModel.processMotionEvent(it)
           }

       ) {
           // Drawing code here.
       }
    }

The `MotionEvent` object contains information about the event:

- [`MotionEvent#getToolType()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getToolType(kotlin.Int)) returns [`TOOL_TYPE_FINGER`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_finger), [`TOOL_TYPE_STYLUS`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_stylus), or [`TOOL_TYPE_ERASER`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_eraser) depending on the tool that made contact with the display
- [`MotionEvent#getPressure()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getpressure) reports the physical pressure applied to the stylus pen (if supported)
- [`MotionEvent#getAxisValue()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getaxisvalue) with [`MotionEvent.AXIS_TILT`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_tilt) and [`MotionEvent.AXIS_ORIENTATION`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_orientation) provide the physical tilt and orientation of the stylus (if supported)

### Historical points

Android batches input events and delivers them once per frame. A stylus can
report events at much higher frequencies than the display. When creating drawing
apps, check for events that may be in the recent past by using the
`getHistorical` APIs:

- [`MotionEvent#getHistoricalX()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gethistoricalx)
- [`MotionEvent#getHistoricalY()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gethistoricaly)
- [`MotionEvent#getHistoricalPressure()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gethistoricalpressure)
- [`MotionEvent#getHistoricalAxisValue()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gethistoricalaxisvalue)

### Palm rejection

When users draw, write, or interact with your app using a stylus, they sometimes
touch the screen with the palm of their hands. The touch event (set to
[`ACTION_DOWN`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_down) or [`ACTION_POINTER_DOWN`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_pointer_down)) can be reported to your app
before the system recognizes and disregards the inadvertent palm touch.

Android cancels palm touch events by dispatching a [`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent). If your
app receives [`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel), cancel the gesture. If your app receives
[`ACTION_POINTER_UP`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_pointer_up), check whether [`FLAG_CANCELED`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#flag_canceled) is set. If so, cancel
the gesture.

Do not check for just `FLAG_CANCELED`. On Android 13 (API level 33) and higher,
the system sets `FLAG_CANCELED` for `ACTION_CANCEL` events, but the system does
not set the flag on lower Android versions.

#### Android 12

On Android 12 (API level 32) and lower, detection of palm rejection is possible
only for single‑pointer touch events. If a palm touch is the only pointer,
the system cancels the event by setting `ACTION_CANCEL` on the motion event
object. If other pointers are down, the system sets `ACTION_POINTER_UP`, which
is insufficient for detecting palm rejection.

#### Android 13

On Android 13 (API level 33) and higher, if a palm touch is the only pointer,
the system cancels the event by setting `ACTION_CANCEL` and `FLAG_CANCELED` on
the motion event object. If other pointers are down, the system sets
`ACTION_POINTER_UP` and `FLAG_CANCELED`.

Whenever your app receives a motion event with `ACTION_POINTER_UP`, check for
`FLAG_CANCELED` to determine whether the event indicates palm rejection (or
other event cancellation).

> [!NOTE]
> **Note:** One way to prevent extraneous palm and finger touch events in stylus‑enabled apps is to provide a UI control that activates a drawing, writing, or interactive mode that disables touch events and supports stylus events only.

### Note-taking apps

ChromeOS has a special intent that surfaces registered note‑taking apps to
users. To register an app as a note‑taking app, add the following to your
app manifest:

    <intent-filter>
        <action android:name="org.chromium.arc.intent.action.CREATE_NOTE" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>

When an app is registered with the system, the user can select it as the default
note‑taking app. When a new note is requested, the app should create an
empty note ready for stylus input. When the user wishes to annotate an image
(such as a screenshot or downloaded image), the app launches with `ClipData`
containing one or more items with `content://` URIs. The app should create a
note that uses the first attached image as a background image and enter a mode
where the user can draw on the screen with a stylus.

#### Test note-taking intents without a stylus

To test whether an app responds correctly to note‑taking intents without
an active stylus, use the following method to display the note‑taking
options on ChromeOS:

1. [Switch to dev mode and make the device writable](https://developer.android.com/topic/arc/development-environment)
2. Press <kbd>Ctrl+Alt+F2</kbd> to open a terminal
3. Run the command `sudo vi /etc/chrome_dev.conf`
4. Press `i` to edit and add `--ash-enable-palette` to a new line at the end of the file
5. Save by pressing <kbd>Esc</kbd> and then typing <kbd>:</kbd>, <kbd>w</kbd>, <kbd>q</kbd> and pressing <kbd>Enter</kbd>
6. Press <kbd>Ctrl+Alt+F1</kbd> to return to the regular ChromeOS UI
7. Log out, then log back in

A stylus menu should now be on the shelf:

- Tap the stylus button on the shelf and choose **New note**. This should open a blank drawing note.
- Take a screenshot. From the shelf, select **stylus button \> Capture screen** or download an image. There should be the option to **Annotate image** in the notification. This should launch the app with the image ready to be annotated.

## Mouse and touchpad support

Most apps generally need to handle only three large screen--centric events:
[right-click](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#right-click), [hover](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#hover), and [drag and
drop](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#drag_and_drop).

### Right-click

Any actions that cause an app to show a context menu, like touch \& hold on a
list item, should also react to right‑click events.

To handle right‑click events, apps should register a
[`View.OnContextClickListener`](https://developer.android.com/reference/kotlin/android/view/View.OnContextClickListener):

    Box(modifier = Modifier.fillMaxSize()) {
        AndroidView(
            modifier = Modifier.fillMaxSize(),
            factory = { context ->
                val rootView = FrameLayout(context)
                val onContextClickListener =
                    View.OnContextClickListener { view ->
                        showContextMenu()
                        true
                    }
                rootView.setOnContextClickListener(onContextClickListener)
                rootView
            },
        )
    }

For details on constructing context menus, see [Create a contextual menu](https://developer.android.com/guide/topics/ui/menus#context-menu).

### Hover

You can make your app layouts feel polished and easier to use by handling hover
events. This is especially true for custom

components:

The two most common examples of this are:

- Indicating to users whether an element has interactive behavior, such as being clickable or editable, by changing the mouse pointer icon
- Adding visual feedback to items in a large list or grid when the pointer is hovering over them

### Drag and drop

In a multi-window environment, users expect to be able to drag and drop items
between apps. This is true for desktop devices as well as tablets, phones, and
foldables in split‑screen mode.

Consider whether users are likely to drag items into your app. For example,
photo editors should expect to receive photos, audio players should expect to
receive audio files, and drawing programs should expect to receive photos.

To add drag and drop support, see

[Drag and drop](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop)

, and take a look at the [Android on ChromeOS --- Implementing Drag \&
Drop](https://medium.com/androiddevelopers/android-on-chrome-os-implementing-drag-drop-2cc2bdcdc621) blog post.

**Special considerations for ChromeOS**

- Remember to request permission with [`requestDragAndDropPermissions()`](https://developer.android.com/reference/kotlin/android/app/Activity#requestdraganddroppermissions) to access items dragged in from outside the app
- An item must have the [`View.DRAG_FLAG_GLOBAL`](https://developer.android.com/reference/kotlin/android/view/View#drag_flag_global) flag in order to be
  dragged out to other applications

  See [Start a drag event](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop#start-drag)

### Advanced pointer support

Apps that do advanced handling of mouse and touchpad input should implement a

[`pointerInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,androidx.compose.ui.input.pointer.PointerInputEventHandler)) modifier to obtain a [`PointerEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent):


```kotlin
@Composable
private fun LogPointerEvents(filter: PointerEventType? = null) {
    var log by remember { mutableStateOf("") }
    Column {
        Text(log)
        Box(
            Modifier
                .size(100.dp)
                .background(Color.Red)
                .pointerInput(filter) {
                    awaitPointerEventScope {
                        while (true) {
                            val event = awaitPointerEvent()
                            // handle pointer event
                            if (filter == null || event.type == filter) {
                                log = "${event.type}, ${event.changes.first().position}"
                            }
                        }
                    }
                }
        )
    }
}
```

<br />

Examine the `PointerEvent` object to determine the following:

- [`PointerType`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerType): Mouse, stylus, touch, and so forth from [`PointerEvent#changes`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent#changes())
- [`PointerEventType`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEventType): Pointer actions, such as press, move, scroll, and release

## Game controllers

Some large screen Android devices support up to four game controllers. Use the
standard Android game controller APIs to handle game controllers (see [Support
game controllers](https://developer.android.com/training/game-controllers)).

Game controller buttons are mapped to common values following a common mapping.
But not all game controller manufacturers follow the same mapping conventions.
You can provide a much better experience if you allow users to select different
popular controller mappings. See [Process gamepad button presses](https://developer.android.com/training/game-controllers/controller-input#button) for more
information.

## Input translation mode

ChromeOS enables an input translation mode by default. For most Android apps,
this mode helps apps work as expected in a desktop environment. Some examples
include automatically enabling two‑finger scrolling on the touchpad, mouse
wheel scrolling, and mapping raw display coordinates to window coordinates.
Generally, app developers don't need to implement any of these behaviors
themselves.

If an app implements custom input behavior, for example defining a custom
two‑finger touchpad pinch action, or these input translations don't
provide the input events expected by the app, you can disable the input
translation mode by adding the following tag to the Android manifest:

    <uses-feature
        android:name="android.hardware.type.pc"
        android:required="false" />

## Additional resources

- [Input compatibility on ChromeOS](https://chromeos.dev/en/android/input-compatibility)