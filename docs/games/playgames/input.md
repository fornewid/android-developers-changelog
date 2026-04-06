---
title: https://developer.android.com/games/playgames/input
url: https://developer.android.com/games/playgames/input
source: md.txt
---

This topic covers design considerations and best practices for handling user
input in Google Play Games on PC.

Google Play Games on PC relies on a mouse and keyboard for player input rather
than a touchscreen. When designing your mouse and keyboard experience, focus on
building the best user experience for desktop or laptop PC users. To get
started, see our guide on
[Android app input compatibility for Chromebooks](https://developer.android.com/topic/arc/input-compatibility).

## Best practices

We recommend the following best practices for designing and building player
interactions.

- All targets should be clickable with a mouse.
- All scrollable surfaces scroll on mouse wheel events.
- Highlight clickable surfaces when hovered, and use your best judgment to improve UI discovery without overwhelming the user.
- Provide hotkeys for users to quickly bring up controls.
- Replace touch-based controls (for example, thumb joysticks or on-screen buttons) with mouse-based controls and hotkeys.
- For actions in your mobile game that require multi-touch gestures, ensure the same actions are supported with a keyboard or mouse control (for example, using the scroll wheel of the mouse to replace a two-finger pinch).

For additional details and best practices, see our guide on
[optimizing your ChromeOS Android app for mouse and keyboard](https://developer.android.com/topic/arc/optimizing#keyboard).

### Internationalization considerations

When designing a game for an international audience, it is important that you
test your game with your keyboard layout set to each language supported by your
game. Failure to do so may block players from using features such as in-game
chat. You can change your input locale
[in your system settings](https://support.microsoft.com/en-us/windows/manage-the-input-and-display-language-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2)
and the changes will apply automatically to Google Play Games on PC. On
mobile, many issues in your engine may be hidden by the fact that you're
receiving text from a virtual keyboard. Common issues on PC include:

- Incorrect handling of "alternative graphic" (AltGr) keycodes. In many locales this is used to type diacritical marks such as accents or special locale-specific symbols such as regional currency glyphs.
- Incorrect handling of ["input method extension" (IME)](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager) inputs. This method is commonly used to support non-Latin alphabets by allowing users to combine several keystrokes into a single character.

[`GameTextInput`](https://developer.android.com/games/agdk/add-support-for-text-input) and
[`EditText`](https://developer.android.com/reference/android/widget/EditText) are already aware of
international keyboard layouts and input methods.

### Recommended input mappings

The following list includes actions many games have in common, and the typical
implementation developers use on Google Play Games on PC:

- Use the enter key to send messages or submit text in text entry fields.
- Menus and dialogs should be cancellable with the escape key.
- Use the enter key to progress through story elements and dialog boxes.
- Use the scroll wheel to scroll text vertically.
- Use the scroll wheel to zoom in or out, especially if you use a two-finger pinch in your mobile build.
- Use W, A, S, and D navigate around a map that you'd normally use a click and drag motion on.

Even though these actions are common, you should still explicitly present them
to the player with the [Input SDK](https://developer.android.com/games/playgames/input-sdk) to make sure they're
properly discoverable.

## Compatibility mode

Google Play Games on PC places your game into "input compatibility mode" by
default. This means that when you press the left mouse button, your game is
given a touch event. See the [mouse input](https://developer.android.com/games/playgames/input-mouse) guide for more
information.

## Tutorials and user education

In some cases, users can benefit from in-game tutorials that teach them the
controls to the game, in addition to being able to view the mouse and keyboard
controls. We recommend including in-game tutorials and educational features with
the correct controls for mouse and keyboard, and removing tutorials relevant to
touch-based controls for the PC version of your game.