---
title: https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper
url: https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper
source: md.txt
---

Keyboard Shortcuts Helper enables users to discover keyboard shortcuts for the
platform and open apps. Publish your app's shortcuts in Keyboard Shortcuts Helper
to improve user productivity and ease of use.

Users press <kbd>Meta+/</kbd> to open the keyboard shortcuts screen, which is
available on [Android 7.0](https://developer.android.com/about/versions/nougat/android-7.0#keyboard_shortcuts_helper) (API level 24) and higher.
![Application open on a device showing system shortcuts.](https://developer.android.com/static/images/develop/ui/touch-input/keyboard-input/keyboard_shortcut_helper.png) **Figure 1.** Keyboard Shortcuts Helper. **Note:** The Meta key is not present on all keyboards. On macOS keyboards, the Meta key is the Command key; on Windows keyboards, the Windows key; and on ChromeOS keyboards, the Search key.

## Provide shortcuts to Keyboard Shortcuts Helper

You can provide available keyboard shortcut lists to
Keyboard Shortcuts Helper by overriding the
[`onProvideKeyboardShortcuts()`](https://developer.android.com/reference/kotlin/android/view/Window.Callback#onprovidekeyboardshortcuts) window callback.
The following snippet demonstrates an implementation of
`onProvideKeyboardShortcuts()` to add a group of four shortcuts:  

    class MainActivity : ComponentActivity() {
        // Activity codes such as overridden onStart method.

        override fun onProvideKeyboardShortcuts(
            data: MutableList<KeyboardShortcutGroup>?,
            menu: Menu?,
            deviceId: Int
        ) {
            val shortcutGroup = KeyboardShortcutGroup(
                "Cursor movement",
                listOf(
                    KeyboardShortcutInfo("Up", KeyEvent.KEYCODE_P, KeyEvent.META_CTRL_ON),
                    KeyboardShortcutInfo("Down", KeyEvent.KEYCODE_N, KeyEvent.META_CTRL_ON),
                    KeyboardShortcutInfo("Forward", KeyEvent.KEYCODE_F, KeyEvent.META_CTRL_ON),
                    KeyboardShortcutInfo("Backward", KeyEvent.KEYCODE_B, KeyEvent.META_CTRL_ON),
                )
            )
            data?.add(shortcutGroup)
        }
    }

[`KeyboardShortcutInfo`](https://developer.android.com/reference/kotlin/android/view/KeyboardShortcutInfo) describes a keyboard shortcut.
The list of keyboard shortcuts are wrapped as a
[`KeyboardShortcutGroup`](https://developer.android.com/reference/kotlin/android/view/KeyboardShortcutGroup) object.
Apps notify available keyboard shortcuts to Keyboard Shortcuts Helper by adding
the `KeyboardShortcutGroup` objects to the mutable list passed
as the first parameter of the method.

## Organize keyboard shortcuts with groups

Keyboard Shortcuts Helper displays keyboard shortcuts in separate groups
so users can find shortcuts by use case or for screens of
your app. [Figure 2](https://developer.android.com/static/images/develop/ui/touch-input/keyboard-input/keyboard_shortcut_group.png) shows the keyboard shortcuts
categorized into two groups: cursor movement and message editing.
![Application open on a device showing shortcut groups.](https://developer.android.com/static/images/develop/ui/touch-input/keyboard-input/keyboard_shortcut_group.png) **Figure 2.** Categories in Keyboard Shortcuts Helper.

Your app registers two or more groups of keyboard shortcuts by creating a
`KeyboardShortcutGroup` object for each group.
In the following snippet, two `KeyboardShortCutGroup` objects are added to the
mutable list passed to the `onProvideKeyboardShortcuts()` method.
The objects are displayed as categories in Keyboard Shortcuts Helper as
[figure 2](https://developer.android.com/static/images/develop/ui/touch-input/keyboard-input/keyboard_shortcut_group.png) shows.  

    override fun onProvideKeyboardShortcuts(
        data: MutableList<KeyboardShortcutGroup>?,
        menu: Menu?,
        deviceId: Int
    ) {
        val cursorMovement = KeyboardShortcutGroup(
            "Cursor movement",
            listOf(
                KeyboardShortcutInfo("Up", KeyEvent.KEYCODE_P, KeyEvent.META_CTRL_ON),
                KeyboardShortcutInfo("Down", KeyEvent.KEYCODE_N, KeyEvent.META_CTRL_ON),
                KeyboardShortcutInfo("Forward", KeyEvent.KEYCODE_F, KeyEvent.META_CTRL_ON),
                KeyboardShortcutInfo("Backward", KeyEvent.KEYCODE_B, KeyEvent.META_CTRL_ON),
            )
        )

        val messageEdit = KeyboardShortcutGroup(
            "Message editing",
            listOf(
                KeyboardShortcutInfo("Select All", KeyEvent.KEYCODE_A, KeyEvent.META_CTRL_ON),
                KeyboardShortcutInfo("Send a message", KeyEvent.KEYCODE_ENTER, KeyEvent.META_SHIFT_ON)
            )
        )

        data?.add(cursorMovement)
        data?.add(messageEdit)
    }

## Open Keyboard Shortcuts Helper from code

Apps display the keyboard shortcuts screen by
calling the [`requestShowKeyboardShortcuts()`](https://developer.android.com/reference/kotlin/android/app/Activity#requestshowkeyboardshortcuts)
method. In the following snippet, Keyboard Shortcuts Helper opens when users tap
or click the button or press the <kbd>Enter</kbd> key.  

    val activity = LocalActivity.current

    Button(onClick = { activity.requestShowKeyboardShortcuts() }) {
        Text(text = "Show keyboard shortcuts")
    }