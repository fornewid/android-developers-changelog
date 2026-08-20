---
title: https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors
url: https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors
source: md.txt
---

# Enable natural input on all form factors

![Desktop computer with keyboard and mouse. Game is on screen, showing touchscreen inputs for direction control and mouse.](https://developer.android.com/static/images/games/multiplatform/game_with_touchscreen_input.png)**Figure 1.**Keyboard, mouse, and touchscreen inputs.

Android devices come in many shapes and sizes. Extend the reach of your game by enabling your players wherever they want to play, whether it's a phone, tablet, PC, TV, car, or XR headset. Here you will learn:

- How[mouse](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#mouse_input)and[keyboard](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#keyboard_input)support can bring your game to players on[PC](https://developer.android.com/games/playgames/overview)and[ChromeOS](https://developer.android.com/chrome-os)as well as improve playability on large screen devices.
- How to meet your most dedicated players where they are with[gamepad](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#gamepad_input)integration.
- How to add[stylus](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#stylus_input)support for precise and responsive gameplay on the go.
- How to support the[TV controller](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#tv_controller_input)and unlock the largest screen your players own: their TV.
- [Design considerations](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#additional_considerations)around when to switch between input methods.
- What cross-form-factor games do to[support players' input preferences](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#how_to_respond_to_user_input).
- And much more.

## Automatic compatibility

Android has automatic nontouch compatibility when possible, for example:

- [`dispatchTouchEvent`](https://developer.android.com/reference/android/view/ViewGroup#dispatchTouchEvent(android.view.MotionEvent))/[`onTouchEvent`](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))respond with motion events even for clicks or stylus input. This means that if you don't check the[tool type](https://developer.android.com/reference/android/view/MotionEvent#getToolType(int)), your touch handling logic should work with the mouse and stylus.
- Some unhandled gamepad and TV controller events are re-emitted as keyboard events.
- PC like form factors such as Play Games and ChromeOS default to generating touches from mouse clicks. Since there may be no touchscreen to fall back on, this provides a base level of compatibility.

- [Mouse](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#mouse_input)and[stylus](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#stylus_input)events are sent to touch callbacks.

- Unhandled[gamepad](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#gamepad_input)and[TV controller](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#tv_controller_input)events are re-emitted as[keyboard](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#keyboard_input)events.

- PC-like form factors such as Play Games and ChromeOS generate touch events rather than mouse events by default to maximize compatibility with games expecting touchscreen input.

For the best user experience, implement direct support for nontouch inputs rather than relying on automatic compatibility.

## Support all form factors

Android runs on an ever growing list of devices. Whether your players unfold their phone into a large screen tablet, power on their Android-enabled TV, open an Android game on their Chromebook, or fire up a quick game in their car when waiting for a charge, you can engage your players in more places and on more displays than ever before. You'll just want to ensure that your game is playable where your players are:

|                                                            Form factor                                                            |     Typical default input     | Touchscreen | Mouse and keyboard | Gamepad | Stylus^[1](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fn1)^ | 5-way D-pad |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------------|--------------------|---------|---------------------------------------------------------------------------------------------------------------------|-------------|
| Phone                                                                                                                             | Touchscreen                   | Yes         | Yes                | Yes     | Yes                                                                                                                 | Yes         |
| Large screen                                                                                                                      | Touchscreen                   | Yes         | Yes                | Yes     | Yes                                                                                                                 | Yes         |
| PC^[2](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fn2)^                   | Mouse and keyboard            | No          | Yes                | Yes     | No                                                                                                                  | No          |
| ChromeOS^[3](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fn3)^             | Touchpad, mouse, and keyboard | Sometimes   | Yes                | Yes     | Yes                                                                                                                 | Yes         |
| TV                                                                                                                                | 5-way D-pad                   | No          | Yes                | Yes     | No                                                                                                                  | Yes         |
| Cars^[4](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fn4)^ (Automotive OS) | Touchscreen                   | Yes         | Yes                | Yes     | No                                                                                                                  | Yes         |
| Watch^[5](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fn5)^                | Touchscreen                   | Yes         | No                 | No      | No                                                                                                                  | No          |

This table is meant to help you prioritize support for new input mechanisms by highlighting the expected input on each form factor. Keep in mind that you should:

- **Avoid having one default input mechanism.**Doing so may inadvertently restrict the reach of your nontouch efforts. For example, although most players want to play ChromeOS games with a mouse and keyboard, some may still want touchscreen support depending on their device profile.
- **Avoid locking input mechanisms to form factors.**Android works with a wide variety of peripherals, and hybrid devices are becoming more popular. Removing keyboard support from your phone build might make your game feel incomplete if the player has a tablet that shipped with a detachable keyboard.

### Mouse input

A player's biggest and most immersive screen may be running Android, whether that's a ChromeOS laptop, Android tablet, or PC. Players often expect to game with a mouse on these devices, and adding support can drive up your player engagement. Android supports the typical features common to desktop operating systems, including:

- Support for left-, right-, and middle-click as well as extra buttons like*back* and*forward*
- Scroll wheel detection
- Either absolute or relative (also known as*pointer capture*) reporting of mouse motion
- The ability to define custom pointer icons

Form factor specific guides exist for:

- [Google Play Games (PC)](https://developer.android.com/games/playgames/input-mouse)
- [ChromeOS](https://chromeos.dev/en/games/optimizing-game-inputs#mouse-capture)
- [Android large screens](https://developer.android.com/guide/topics/large-screens/input-compatibility-large-screens#mouse_and_touchpad)

| **Note:** Because both ChromeOS and Google Play Games (PC) ship on nontouch devices, these form factors have extensive input emulation support. If you decide not to handle mouse input yourself, remember to add`<uses-feature android:name="android.hardware.type.pc" android:required="false" />`to your manifest as explained in the form factor specific guides.

#### Touchpad input

Touchpad input capture on Android differs slightly from mouse support. When calling[`requestPointerCapture()`](https://developer.android.com/reference/android/view/View#requestPointerCapture()), you are requesting raw access to touches on the pad. This means that you receive events for each touch in the same way that you get multitouch events from a touchscreen, except that coordinates are in the touchpad's coordinate space as opposed to that of the display. Android's built-in touchpad gesture detection and palm filtering are disabled in this mode. If, for example, the user is moving one finger on the pad while also resting their thumb in the bottom-left corner ready to click, it is up to your game to determine which finger's movement should be used in your logic (for example, to move the camera).

This means that gamepads with built in touchpads can be used much like a touchscreen for robust gesture-based input.

To determine whether your player is using a mouse or a touchpad during pointer capture, check the source values from either[`InputDevice#getSources()`](https://developer.android.com/reference/android/view/InputDevice#getSources())or[`MotionEvent#getSource()`](https://developer.android.com/reference/android/view/MotionEvent#getSource())for[`InputDevice.SOURCE_TOUCHPAD`](https://developer.android.com/reference/android/view/InputDevice#SOURCE_TOUCHPAD).
| **Note:** Google Play Games on PC and ChromeOS both treat their touchpads as mice.

### Keyboard input

Keyboard support is nearly universal across all Android devices. Depending on the kind of game you develop, the benefits of adding keyboard awareness to your game range from growing your player base by making your game more accessible to making your game more immersive and intuitive to play.

Some common ways to improve your game with keyboard support:

- **Multitouch mechanics must be mapped to the keyboard for nontouch devices.**Games requiring two or more simultaneous touches, such as moving and jumping, benefit from mapping these actions to keyboard presses to improve playability on large screen and nontouch screens.
- **Make menus navigable by keyboard.** Adding button navigation, such as arrow keys and<kbd>Enter</kbd>, to your menus and static gameplay elements enables games to be played on TVs and improves your accessibility on all form factors.
- **Add hotkeys for on-screen actions.**Map anything a player can touch on screen to a keyboard action. Quick access to actions such as selecting units in a strategy game or activating inventory slots in an action game keeps your players immersed in your game.

Remember that although QWERTY keyboards are fairly common, there are many different popular layouts and some characters that are a single keypress in one layout may be a chord in another.

If your game uses the relative position of keys to perform actions, such as using<kbd>W</kbd>,<kbd>A</kbd>,<kbd>S</kbd>, and<kbd>D</kbd>like arrow keys to move, use[`InputDevice.getKeyCodeforKeyLocation()`](https://developer.android.com/reference/android/view/InputDevice#getKeyCodeForKeyLocation(int))to map a QWERTY key's location to a keycode in[`KeyEvent.getKeyCode()`](https://developer.android.com/reference/android/view/KeyEvent#getKeyCode()). If the player's layout ever changes,[`onInputDeviceChanged()`](https://developer.android.com/reference/android/hardware/input/InputManager.InputDeviceListener#onInputDeviceChanged(int))is called.

When adding text entry to a game,[TextInput in GameActivity](https://developer.android.com/games/agdk/game-activity/use-text-input)provides a mechanism to reliably handle IME input, diacritical marks, or other region-specific variations in layout while still using your in-game text rendering engine. This avoids many pitfalls of handling keyboard input directly or using an offscreen`EditText`widget.
| **Warning:** attaching or disconnecting a keyboard is a[configuration change](https://developer.android.com/guide/topics/resources/runtime-changes). This means that you can use the[configuration](https://developer.android.com/reference/android/content/res/Configuration)to detect the presence of a keyboard but also that you should handle this configuration change to avoid having your game restart when plugging in a keyboard.

### Gamepad input

![An image of a typical gamepad. It has a directional pad, four face buttons labelled a, b, x, and y, two analog sticks, and four triggers. There are numbers on the image, but they are not referenced in this page.](https://developer.android.com/static/images/training/game-controller-profiles.png)**Figure 2.**Gamepad inputs.

Gamepads are[formally supported across Android](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers), including connect and disconnect events,[haptic support](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-features#haptics), advanced input support including[gyroscopes](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-features#motion_sensors), and output support like[light color](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-features#lights)when available.

App developers can listen for gamepad inputs through[`View`or`Activity`callbacks](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-input), but game developers are encouraged to use the[Game Controller Library](https://developer.android.com/games/sdk/game-controller)which:

- Is written in C++ to facilitate integration into your own game engine
- Centralizes all gamepad features into one API
- Disambiguates the symbols on a gamepad's face buttons, so your game's labels can match a player's gamepad
- Unifies the reporting of gamepad events in cases where buttons would be analog inputs on some gamepads but binary inputs on others
- Provides limited forward compatibility on older Android devices for newer gamepads

| **Note:** Seamlessly switch between gamepads and other inputs rather than entering a gamepad specific mode. This includes responding to touch events if a player is playing with a gamepad, or letting players play on a TV with a mouse even if gamepad use is more likely.

### Stylus input

![An image showing a drawing app. Brushes are open showing shapes that can be drawn with the stylus.](https://developer.android.com/static/develop/ui/compose/images/touchinput/stylus/hero.png)**Figure 3.**Drawing app with brushes palette.

Android has[advanced stylus support](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input)across most devices, including pressure, orientation, tilt, hover, and palm detection. Stylus events sent to touch callbacks to help compatibility, but it's important to test with a stylus device in case your engine logic filters these events out. Full integration benefits games with small touch targets or games where free-form drawing feels natural.

When rendering lags behind stylus movement, the latency is more obvious than it is when blocked by a finger or disconnected from the screen as with a keyboard, mouse, or gamepad. For this reason, Android provides a low latency pipeline for rendering strokes with as little as 4ms latency from pen motion to display on screen. There are three ways your game can take advantage of this capability, making your game feel directly connected to the real world:

- [The Jetpack Ink library](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/about-ink-api)provides a convenient toolkit for adding responsive stroke rendering to any Android project.
- For games unable or unwilling to rely on a Kotlin component for stroke rendering,[the full C++ source code](https://github.com/google/ink)is available. This allows developers to integrate what they need directly into their technology.
- For games requiring full custom integration, it's possible to[execute custom rendering logic directly on the front buffer](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features#low-latency_graphics)to maximize both responsiveness and control.

### TV Controllers

![An image of the TV controller for Android. Called out are a D-pad, select button, microphone or assistant button, back button, and home button.](https://developer.android.com/static/training/tv/images/tv-nav-controller.png)**Figure 4.**TV controller.

Android TV devices come with a[remote that includes a 5-way D-pad](https://developer.android.com/training/tv/get-started/controllers)that comprises the four cardinal directions and an**OK**button. Applications using Android's built-in widget system support these by default, but developers must test their game's custom widgets to maintain compatibility on TV devices.
| For compatibility reasons, unhandled gamepad events emit the same key press events as the 5-way remote as will the keyboard and arrow keys.

See the[Android TV documentation](https://developer.android.com/training/tv)for more information.

## Additional considerations

To give your players the best experience, design around multiple forms of input and switch between them on the fly. This way a player can quickly jump between different input methods depending on the game mode they're in, or a game can transition between different configurations of one Android-powered device with ease.

With that in mind, note that:

- **Checking for the presence of a kind of input is better than filtering on the form factor**. For example, if you only enable mouse and keyboard support on ChromeOS, players on tablets with detachable keyboards won't benefit from your extra effort.
- **There are considerations outside of form factor that affect the best form of input**. For example, a player's accessibility needs might make a mouse or touchscreen difficult or painful to use but a gamepad or keyboard ideal.
- **Any support is better than no support**. It is ideal to respond to input changes on the fly, but players appreciate some support over none as long as they're able to get to it.
- **The best input may change between runs of your game**. For example, a touchscreen is preferable when playing a game on the go, a gamepad when a phone is plugged into a TV, and a mouse and keyboard when sitting at a desk.

### How to respond to user input

Typical mobile games support one player per device. For the best results, a game responds to all possible inputs and shifts the UI based on what the player is actively using. This way, one version of the game automatically works across all form factors, and players can even mix and match inputs to suit their needs.

Often developers want to have a default input method with built-in delays before shifting the UI. What does this mean?

- Since most players play on touch screens, display touch controls on launch. If a player starts playing with a keyboard or gamepad and doesn't use the touchscreen for some time, fade out the touch layer.
- If a player is using the gamepad and presses a keyboard key, shift in-game hints to show keyboard buttons instead of gamepad buttons.
- When a player is using both keyboard and gamepad at the same time, build in a delay before switching the UI from one set of hints to another to avoid display flickering.
- Check the input source type when processing inputs; keyboard keys and gamepad buttons both emit key down events.
- Try not to mark an input as handled unless your game can handle it. Android re-emits some events to facilitate compatibility on newer form factors, for example, turning the gamepad**A** button into the**OK**button.

### Annotate input support in your manifest

Although not required, it can be best to annotate with manifest feature flags what kind of inputs you handle. Common flags are:

- [`android.hardware.type.pc`](https://developer.android.com/guide/topics/manifest/uses-feature-element#device-ui-hw-features): Disable input[compatibility layers](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#automatic_compatibility)on both ChromeOS and PC to enable developers to directly handle[mouse events](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#mouse_input). Set`android:required="false"`so the game will still be delivered to phones.
- [`android.hardware.gamepad`](https://developer.android.com/guide/topics/manifest/uses-feature-element#gamepad-hw-features): Apps and games receive[gamepad events](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#gamepad_input)whether or not they support gamepads. Defining this manifest flag and setting`android:required="false"`allows your game to be served to Android TV devices with gamepads attached.

*** ** * ** ***

1. Manufacturers can build in stylus support for some devices, but there is no form factor where support is guaranteed. Drawing pads can be plugged into an Android device and show up as a stylus.[↩](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fnref1)

2. Although some PCs have touchscreen and stylus support, the Google Play Games client responds only to mouse events from the host operating system. To maximize compatibility, mouse events appear as touch events in the client by default. See the[Mouse Input](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#mouse_input)section for more information.[↩](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fnref2)

3. ChromeOS devices generally have mouse and keyboard support, but touchscreens are optional. Many touchscreen-enabled devices also support stylus input.[↩](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fnref3)

4. Android Automotive OS refers to cars with Android built in, which can function without an Android phone. Automotive OS is what this chart refers to. Android Auto projects an app from a phone onto the car, and devices that support Android Auto (projection) might not have a touchscreen.[↩](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fnref4)

5. Wear OS devices have limited connectivity. You can scan for bluetooth peripherals, but the OS often fails to connect.[↩](https://developer.android.com/games/develop/multiplatform/enable-natural-input-on-all-form-factors#fnref5)