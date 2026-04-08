---
title: https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands
url: https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands
source: md.txt
---

When the user gives focus to an editable text component, such as a `TextField`,
and the device has a hardware keyboard attached,
all input is handled by the system.
You can provide keyboard shortcuts by handling key events.
| **Note:** Key events can be handled by implementing the [`KeyEvent.Callback`](https://developer.android.com/reference/android/view/KeyEvent.Callback) interface on an `Activity` class. Refer to [Handle keyboard actions](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/commands) in views for details.

## Default keyboard shortcuts

The following keyboard shortcuts are available out of the box.

| Keyboard shortcut | Action | Composables supporting the shortcut |
|---|---|---|
| <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Left arrow</kbd>/<kbd>Right arrow</kbd> | Select text to beginning/end of word | `BasicTextField`, `TextField` |
| <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Up arrow</kbd>/<kbd>Down arrow</kbd> | Select text to beginning/end of paragraph | `BasicTextField`, `TextField` |
| <kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>Up arrow</kbd>/<kbd>Down arrow</kbd> or <kbd>Shift</kbd>+<kbd>Meta</kbd>+<kbd>Left arrow</kbd>/<kbd>Right arrow</kbd> | Select text to beginning/end of text | `BasicTextField`, `TextField` |
| <kbd>Shift</kbd>+<kbd>Left arrow</kbd>/<kbd>Right arrow</kbd> | Select characters | `BasicTextField`, `TextField` |
| <kbd>Ctrl</kbd>+<kbd>A</kbd> | Select all | `BasicTextField`, `TextField` |
| <kbd>Ctrl</kbd>+<kbd>C</kbd>/<kbd>Ctrl</kbd>+<kbd>X</kbd>/<kbd>Ctrl</kbd>+<kbd>V</kbd> | Copy/cut/paste | `BasicTextField`, `TextField` |
| <kbd>Ctrl</kbd>+<kbd>Z</kbd>/<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> | Undo/redo | `BasicTextField`, `TextField` |
| <kbd>PageDown</kbd>/<kbd>PageUp</kbd> | Scroll | `LazyColumn`, the `verticalScroll` modifier, the `scrollable` modifier |

| **Note:** The Meta key is not present on all keyboards. On macOS keyboards, the Meta key is the Command key; on Windows keyboards, the Windows key; and on ChromeOS keyboards, the Search key.

## Key events

In Compose, you can handle an individual keystroke with
the [`onKeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/package-summary#(androidx.compose.ui.Modifier).onKeyEvent(kotlin.Function1)) modifier.
The modifier accepts a lambda that's called
when the modified component receives a key event.
A key event is described as a [`KeyEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent) object.
You can get the information of each key event by referring to the object
in the lambda passed to the `onKeyEvent` modifier.

A keystroke sends two key events.
One is triggered when the user presses the key;
the other is triggered when the key is released.
You can distinguish the two key events
by referring to the [`type`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).type()) attribute of the `KeyEvent` object.

The return value of the `onKeyEvent` lambda indicates
whether the key event is handled or not.
Return `true` if your app handles the key event,
which stops propagation of the event.

The following snippet shows how to call a `doSomething()` function
when the user releases the <kbd>S</kbd> key on the `Box` component:  

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

### Modifier keys

A `KeyEvent` object has the following attributes which indicate
whether modifier keys are pressed or not:

- [`isAltPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isAltPressed())
- [`isCtrlPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isCtrlPressed())
- [`isMetaPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isMetaPressed())
- [`isShiftPressed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/KeyEvent#(androidx.compose.ui.input.key.KeyEvent).isShiftPressed()))

Be specific in describing the key events your app handles.
The following snippet calls a `doSomething()` function
only if the user releases just the <kbd>S</kbd> key.
If the user presses any modifier key,
such as the <kbd>Shift</kbd> key, the app does not call the function.  

    Box(
      modifier = Modifier.focusable().onKeyEvent{
         if(
           it.type == KeyEventType.KeyUp &&
           it.key == Key.S &&
           !it.isAltPressed &&
           !it.isCtrlPressed &&
           !it.isMetaPressed &&
           !it.isShiftPressed
         ) {
           doSomething()
           true
         } else {
           false
         }
      }
    )  {
        Text("Press S key with a modifier key")
    }

### Spacebar and Enter key click events

The <kbd>Spacebar</kbd> and <kbd>Enter</kbd> key trigger click events as well.
For example, users can toggle (play or pause) media playback
with the <kbd>Spacebar</kbd> or the <kbd>Enter</kbd> key
by handling click events as follows:  

    MoviePlayer(
       modifier = Modifier.clickable { togglePausePlay() }
    )

The [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)) modifier intercepts key events
and calls the `onClick()` callback when the <kbd>Spacebar</kbd> or
<kbd>Enter</kbd> key is pressed.
That's why the `togglePausePlay()` function is called
by pressing the <kbd>Spacebar</kbd> or <kbd>Enter</kbd> key in the snippet.

### Unconsumed key events

Unconsumed key events are propagated from the component
where the event occurred to the enclosing outer component.
In the example below, the `InnerComponent` consumes key events
when the <kbd>S</kbd> key is released,
and so the `OuterComponent` does not receive any key events triggered
by releasing the <kbd>S</kbd> key.
That's why the `actionB()` function is never called.

Other key events on `InnerComponent`, such as releasing the <kbd>D</kbd> key,
can be handled by the `OuterComponent`.
The `actionC()` function is called because the key event for
releasing the <kbd>D</kbd> key is propagated to the `OuterComponent`.  

    OuterComponent(
        modifier = Modifier.onKeyEvent {
            when {
               it.type == KeyEventType.KeyUp && it.key == Key.S -> {
                   actionB() // This function is never called.
                   true
               }
               it.type == KeyEventType.KeyUp && it.key == Key.D -> {
                   actionC()
                   true
               }
               else -> false
            }
        }
    ) {
        InnerComponent(
            modifier = Modifier.onKeyEvent {
                if(it.type == KeyEventType.KeyUp && it.key == Key.S) {
                    actionA()
                    true
                } else {
                    false
                }
            }
        )
    }

## `onKeyPreviewEvent` modifier

In some use cases, you want to intercept a key event
before it triggers the default action.
Adding custom shortcuts to a `TextField` is a typical one.
The following snippet enables users to move to the next focusable component by
pressing the <kbd>tab</kbd> key.  

    val focusManager = LocalFocusManager.current
    var textFieldValue by remember { mutableStateOf(TextFieldValue()) }

    TextField(
        textFieldValue,
        onValueChange = {
            textFieldValue = it
        },
        modifier = Modifier.onPreviewKeyEvent {
            if (it.type == KeyEventType.KeyUp && it.key == Key.Tab) {
                focusManager.moveFocus(FocusDirection.Next)
                true
            } else {
                false
            }
        }
    )

By default, the `TextField` component adds a tab character
every time users press the <kbd>Tab</kbd> key,
even if the key event is handled with the `onKeyEvent` modifier.
To move the keyboard focus without adding any tab characters,
handle the key event
before triggering the actions associated with the key event, as in the snippet.
The [`onKeyPreviewEvent()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/package-summary#(androidx.compose.ui.Modifier).onPreviewKeyEvent(kotlin.Function1)) lambda intercepts the key event
by returning `true`.

The parent component can intercept the key event happening on its children.
In the following snippet, the `previewSKey()` function is called
when users press the <kbd>S</kbd> key,
instead of calling the `actionForPreview()` function.  

    Column(
      modifier = Modifier.onPreviewKeyEvent{
        if(it.key == Key.S){
          previewSKey()
          true
        }else{
          false
        }
      }
    ) {
      Box(
        modifier = Modifier
            .focusable()
            .onPreviewKeyEvent {
                actionForPreview(it)
                false
            }
            .onKeyEvent {
                actionForKeyEvent(it)
                true
            }
      ) {
        Text("Press any key")
      }
    }

The `onPreviewKeyEvent()` lambda for the `Box` component is not triggered
when users press the <kbd>Tab</kbd> key either.
The `onPreviewKeyEvent()` lambda is called on the parent component first,
then `onPreviewKeyEvent()` in the child component is called.
You can implement screen-wide keyboard shortcuts by utilizing this behavior.

## Additional resources

- [Keyboard Shortcuts Helper](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper): System screen that enables users to search for the keyboard shortcuts your app offers.