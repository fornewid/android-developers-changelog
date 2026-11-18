---
title: https://developer.android.com/games/large-screen/tier-2
url: https://developer.android.com/games/large-screen/tier-2
source: md.txt
---

> Documentation index: https://developer.android.com/games/llms.txt

Games that are Tier 2 (Optimized) build upon [Tier 3 (Ready)](https://developer.android.com/games/large-screen/tier-3.md.txt) to deliver
an enhanced experience across tablets and foldables. They feature proportional
UI scaling and high-resolution graphics tailored for larger displays, styled
visual framing when letterboxing is used, and full start-to-finish playability
using external controllers, keyboards, and mice regardless of which form factors
you distribute the game on.

![Depiction of the three quality tiers as layers stacked vertically with the middle tier highlighted.](https://developer.android.com/static/images/docs/quality-guidelines/tier-2/tier_2_header.png)

The guidelines on this page apply directly to foldables and tablets. Other form
factors, such as desktops, TVs, car displays, and XR, have additional
form-factor-specific requirements. Games targeting Tier 2 on those devices must
also meet the Tier 2 requirements for each form factor where you distribute
them.

## Expected player experience

A Tier 2 game looks, feels, and plays like it was built for a larger canvas and
physical peripherals. Graphics, 3D scenes, UI icons, and text render crisply at
high resolution without mobile blurriness, and gameplay stays visually smooth
even when rendering more pixels on an unfolded foldable or tablet.

On-screen heads-up display (HUD) controls stay comfortably near the outer edges,
clear of the foldable hinge crease. Dialogs use bounded widths instead of
stretching edge to edge, and any letterboxed or pillarboxed framing uses styled
thematic artwork rather than plain black bars. Players can play the entire game
from start to finish using a controller or a keyboard and mouse---with
smooth 360-degree mouse camera rotation, hover states, scroll-wheel zoom, and
seamless audio and controller switching mid-game.

### Do

Follow these best practices to provide a Tier 2 experience:

- Deliver high-resolution 2D and 3D assets and crisp, legible full-screen text, while maintaining smooth user-perceived frame pacing (at least 30 FPS, or 60 FPS and higher for action and high-refresh-rate titles) on larger displays.
- Scale HUD overlays and on-screen touch controls proportionally near the screen edges (clear of the center fold crease), keep modals and dialogs at bounded widths, and render full screen across expanded aspect ratios for other form factors and additional foldable and tablet models (16:9, 21:9, and 6:5 in landscape; 9:16, 9:21, and 5:6 in portrait).
- Replace plain black bars with styled thematic borders, artwork, or an extended background canvas when letterboxing or pillarboxing.
- Support full start-to-finish playability with hardware game controllers and with a keyboard, mouse, and trackpad regardless of which form factors you distribute the game on, including Pointer Capture for 3D camera-look games and seamless controller, keyboard, and audio peripheral hot-plugging without restarts.

### Don't

Avoid the following common issues:

- Upscale low-resolution phone textures that look blurry or pixelated on tablets, unfolded foldables, and laptops, or allow larger display resolutions to cause severe frame drops or stutter.
- Stretch dialogs, menus, or HUD bars edge to edge across wide screens, or leave oversized mobile touch buttons obscuring the center viewport.
- Leave plain black bars when pillarboxing a portrait game in landscape or letterboxing a landscape game in portrait.
- Require players to fall back to touch input to navigate menus, complete tutorials, or play core gameplay loops when a controller or keyboard and mouse is connected, unless exempted by core genre mechanics.

## Guidelines

The following sections describe the Tier 2 quality guidelines for games on
large screens and foldables.

### User interface and visual presentation

The following table describes the user interface and visual presentation
guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `High_Resolution_Graphics` | [`T-High_Resolution_Graphics`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-High_Resolution_Graphics) | Graphics, 2D UI textures, fonts, icons, and 3D scenes display at high resolution on large screens without noticeable blurring, pixelation, aliasing, or aspect-ratio stretching, and all in-game text is crisp and clearly legible in full-screen mode. |
| `UI_Scaling` | [`T-UI_Scaling`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-UI_Scaling) | On-screen controls, in-game UI overlays, menus, and dialogs scale proportionally across large screens and multi-window sizes: - On-screen touch controls and UI overlays remain comfortably positioned and sized near the screen edges---and kept clear of the center fold crease on unfolded foldables---without becoming oversized or obscuring the active gameplay view. - Dialogs, modals, and settings menus use bounded widths rather than stretching edge to edge across wide displays. |
| `Expanded_Aspect_Ratios` | [`T-Expanded_Aspect_Ratios`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Expanded_Aspect_Ratios) | In addition to the core foldable and tablet aspect ratios in Tier 3 (1:1, 10:9, 4:3, and 16:10 in landscape; 1:1, 9:10, 3:4, and 10:16 in portrait), the game renders full screen without letterboxing or pillarboxing across expanded aspect ratios for other form factors and additional foldable and tablet models in its supported orientations: - **Landscape aspect ratios** : - **Additional foldables and tablets**: 6:5 (older foldables), 21:9 (widescreen folded cover screens), and 16:9 tablets. - **TV**: 16:9. - **Auto**: 16:9 (Android Auto) and 4:3 (Android Automotive OS). - **XR (2D spatial windows)**: 16:10. - **Googlebooks and desktop**: 16:10 (built-in display), with dynamic window resizing to 16:9 and 21:9 (widescreen connected displays). - **Portrait aspect ratios** : - **Additional foldables and tablets**: 5:6 (older foldables), 9:21 (widescreen folded cover screens), and 9:16 tablets. - **Auto**: 9:16 (Android Auto) and 10:16 (Android Automotive OS). - **TV**: 9:16 (using styled pillarboxing when displayed inside a 16:9 landscape window). |
| `Styled_Letterboxing` | [`T-Styled_Letterboxing`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Styled_Letterboxing) | When a single-orientation game is pillarboxed or letterboxed in the opposite orientation, or when letterboxed on an out-of-anchor window size (such as 50/50 split-screen), the game replaces plain black bars with **styled thematic borders, artwork, or an extended non-interactive background canvas**. |
| `Smooth_Frame_Pacing` | [`T-Smooth_Frame_Pacing`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Smooth_Frame_Pacing) | The game maintains smooth, consistent user-perceived frame pacing (at least 30 FPS, or 60 FPS and higher for action and high-refresh-rate titles) during active gameplay and UI transitions on large screens and unfolded foldables, dynamically adapting rendering resolution or graphics quality as needed so larger display resolutions don't cause visible stutter, judder, or thermal slowdown. |

### Controller

The following table describes the controller guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Controller_Support` | [`T-Controller_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Controller_Support) | Regardless of which form factors the game is distributed on (including phones, foldables, and tablets), the game is playable from start to finish with a hardware game controller (such as Xbox Wireless, Sony DualSense, or Nintendo Switch Pro controllers) across initial onboarding, menus, settings, and all gameplay mechanics, without needing to fall back to touch input (unless core genre mechanics, such as location-based AR, ambient sensors, multi-touch rhythm charts, freehand vector drawing, password input, or rapid drag-and-drop, can't be replicated on a controller). The game declares controller support (`android.hardware.gamepad` with `android:required="false"`) in the app manifest. |
| `Controller_Prompts_And_Hot_Swapping` | [`T-Controller_Prompts_And_Hot_Swap`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Controller_Prompts_And_Hot_Swap) | Connecting or disconnecting a controller mid-session transitions cleanly without crashing, freezing, or requiring an app restart. While controller input is active, the game hides redundant on-screen touch joysticks and action buttons, and displays relevant controller button glyphs. |

### Keyboard, mouse, and trackpad

The following table describes the keyboard, mouse, and trackpad guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Keyboard_Mouse_Support` | [`T-Keyboard_Mouse_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Keyboard_Mouse_Support) | The game is playable from start to finish with a keyboard, mouse or trackpad, or both across all gameplay mechanics and settings menus without needing to fall back to touch input (unless core genre mechanics, such as location-based AR, ambient sensors, or multi-touch rhythm charts, can't be replicated on a keyboard and mouse). |
| `Keyboard_Input_2Handed_Touch` | [`T-Keyboard_Mouse_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Keyboard_Mouse_Support) | If the mobile version of the game requires two hands to play using touch, the game must support keyboard input (or mouse and keyboard). |
| `Keyboard_Input_Multi_Touch` | [`T-Keyboard_Mouse_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Keyboard_Mouse_Support) | If the mobile version of the game requires multiple fingers touching the screen at the same time to play (for example, a game that requires a two-finger swipe to complete a level), then the game must support keyboard input or an alternative mouse input on desktop. |
| `Keyboard_Input_Swiping` | [`T-Keyboard_Mouse_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Keyboard_Mouse_Support) | If the game requires frequent swiping to play, then the game must support keyboard input. Note: Infrequent horizontal swiping can be acceptable provided the timing and accuracy of the swipes aren't critical to gameplay. |
| `Keyboard_Hotplugging_Support` | [`T-Keyboard_Hotplugging_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Keyboard_Hotplugging_Support) | The game handles the `keyboard` and `keyboardHidden` configuration changes so that the `Activity` doesn't restart and any UI associated with text entry remains functional. |
| `No_Virtual_Keyboards` | [`T-No_Virtual_Keyboards`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-No_Virtual_Keyboards) | When a physical keyboard is present, the game **must** use the keyboard for text input and **must not** show an on-screen keyboard for text input. |
| `Content_Zoom` | [`T-Content_Zoom`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Content_Zoom) | The game **must** support trackpad pinch-to-zoom and the mouse scroll wheel for any in-game interactions that use pinch-to-zoom on mobile. Examples include in-game maps or zooming in on images. The game must not *require* on-screen touch pinch-to-zoom. |
| `Content_Scroll` | [`T-Content_Scroll`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Content_Scroll) | In scrollable areas (such as lists, menus, and inventory selection), two-finger trackpad scrolling, mouse scroll wheel, and **Shift**+scroll actions must scroll content smoothly. |
| `Custom_Cursors` | [`T-Custom_Cursors`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Custom_Cursors) | If appropriate, the game **may** support custom cursors (such as crosshairs). Custom cursors **must not** duplicate existing Android cursors (that is, two cursors must not appear at the same time). Custom cursors **must** offer precision and performance and **must not** introduce lag. Custom cursors **must** respond accurately to system-level mouse sensitivity settings and transition cleanly between entering and leaving the window when the game is in windowed mode. |
| `Menu_Navigation` | [`T-Menu_Navigation`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Menu_Navigation) | Players must be able to navigate all menus and gameplay using only a keyboard and mouse or trackpad. |
| `Enter_Key` | [`T-Enter_Key`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Enter_Key) | When entering text, the **Enter** key should perform the appropriate submit action. For example, when entering text in chat, pressing **Enter** should send the message. This avoids requiring players to switch between the keyboard (to enter text) and the mouse (to submit it). |
| `Back_Key` | [`T-Back_Key`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Back_Key) | Some keyboards support a **Back** key. The game **must** handle the **Back** key and edge-swipe back gesture logically, and prompt before quitting the game. In submenus, the keyboard **Back** key should return to the previous screen or menu. On the main menu or during gameplay, pressing the **Back** key must display a confirmation prompt before leaving the game. |
| `Mouse_Capture` | [`T-Mouse_Capture`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Mouse_Capture) | Games that capture the mouse **must** meet all of the following requirements: - The game **must** offer mouse sensitivity settings. - The game **must** support mouse capture while windowed, including releasing mouse capture when the window moves to the background. - The game **must** switch cleanly between full-screen and windowed modes. - The game **must** release the mouse appropriately to let players click menu items or use the mouse in-game to press buttons. - The game **must not** depend on on-screen touch controls when the mouse is captured (keyboard controls are acceptable). |
| `FPS_Mouse_Capture` | [`T-Mouse_Capture`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Mouse_Capture) | If the game features a first-person view where the player controls the camera, the game **must** capture the mouse to control the camera, similar to a native desktop gaming experience. |
| `Secondary_Actions` | [`T-Secondary_Actions`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Secondary_Actions) | The game **should** support secondary click (right-click, two-finger tap, or long press) for secondary actions where appropriate for gameplay. This behavior might not be suitable for all games, but is expected behavior for some genres (for example, in a first-person shooter (FPS), right-clicking is typically expected to aim). These actions must work for both a trackpad and a mouse. |
| `Hover_States` | [`T-Hover_States`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Hover_States) | The game **should** provide tooltips when the mouse is positioned over actionable UI items that don't already have clear descriptions. |

### Audio

The following table describes the audio guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Audio_Peripheral_Switching` | [`T-Audio_Peripheral_Switching`](https://developer.android.com/games/large-screen/tier-2.md.txt#T-Audio_Peripheral_Switching) | The game routes audio seamlessly, keeping audio smooth and in sync with gameplay without muting, crashing, or requiring a restart when external audio peripherals (such as USB-C, 3.5 mm, or Bluetooth headphones and headsets) are connected or disconnected during active gameplay. |

## Tests

To confirm that your game meets the Tier 2 (Optimized) requirements, run the
following verification tests.

### User interface and visual presentation

The following table describes the user interface and visual presentation tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-High_Resolution_Graphics` | [`High_Resolution_Graphics`](https://developer.android.com/games/large-screen/tier-2.md.txt#High_Resolution_Graphics) | Inspect gameplay scenes, UI icons, and text on large tablets, unfolded foldables, and large screens in full-screen mode. Verify that all graphics and UI elements render sharply without blurring, pixelation, or stretching, and that all text is crisp and clearly legible. |
| `T-UI_Scaling` | [`UI_Scaling`](https://developer.android.com/games/large-screen/tier-2.md.txt#UI_Scaling) | Run the game on phones, foldable phones (folded and unfolded), and tablets in both full-screen and multi-window modes. Verify the following: - On-screen controls and UI overlays scale proportionally, stay anchored near the screen edges clear of the center fold crease on unfolded foldables, and don't obscure the active gameplay view. - Menus, modals, and dialogs use bounded widths without stretching edge to edge across wide screens. |
| `T-Expanded_Aspect_Ratios` | [`Expanded_Aspect_Ratios`](https://developer.android.com/games/large-screen/tier-2.md.txt#Expanded_Aspect_Ratios) | Test the game in its supported orientations across the expanded aspect ratios for additional form factors and foldable or tablet models: in landscape across 16:9 (TV, Android Auto, and external monitors), 16:10 (XR 2D window and Googlebooks), 21:9 (widescreen monitors and widescreen cover screens), 6:5 (older foldables), and 4:3 (Android Automotive OS), including resizing a landscape window from 16:10 to 16:9 and 21:9; and in portrait across 9:16 (Android Auto and TV), 10:16 (Android Automotive OS), 9:21, and 5:6. Verify that the active gameplay viewport and UI fill the window without letterboxing, pillarboxing, stretching, or UI distortion. |
| `T-Styled_Letterboxing` | [`Styled_Letterboxing`](https://developer.android.com/games/large-screen/tier-2.md.txt#Styled_Letterboxing) | If the game pillarboxes or letterboxes itself (for example, a portrait-only game rotated to landscape on an unfolded foldable or tablet), verify that the framing area displays styled thematic borders, artwork, or an extended background canvas rather than plain black bars. |
| `T-Smooth_Frame_Pacing` | [`Smooth_Frame_Pacing`](https://developer.android.com/games/large-screen/tier-2.md.txt#Smooth_Frame_Pacing) | Play through active gameplay scenes and UI transitions and verify that gameplay and camera movement remain visually smooth and responsive (at least 30 FPS, or 60 FPS and higher where supported) without noticeable frame drops, stutter, or thermal slowdown. |

### Controller

The following table describes the controller tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Controller_Support` | [`Controller_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#Controller_Support) | Pair a standard controller (Xbox, DualSense, or Switch Pro) using both a cable and Bluetooth. Play the game from initial launch through onboarding, menus, settings, and core gameplay loops without touching the screen. Verify complete start-to-finish playability and verify that `android.hardware.gamepad` is declared with `android:required="false"` in the manifest. |
| `T-Controller_Navigation` | `Controller_Navigation_And_Conventions` | Navigate through all menus, lobbies, inventories, and dialogs using the D-pad and thumbsticks. Verify a clear visual focus indicator on selected items, confirm that **A** or **Cross** selects items, **B** or **Circle** dismisses menus and overlays, and **Start** , **Menu** , or **Options** opens and closes the in-game pause menu. |
| `T-Controller_Prompts_And_Hot_Swap` | [`Controller_Prompts_And_Hot_Swapping`](https://developer.android.com/games/large-screen/tier-2.md.txt#Controller_Prompts_And_Hot_Swapping) | Connect and disconnect a controller mid-session during active gameplay. Verify that the game transitions cleanly without crashing or restarting, hides on-screen touch joysticks and action buttons while controller input is active, and displays controller button glyphs. |

### Keyboard, mouse, and trackpad

The following table describes the keyboard, mouse, and trackpad tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Keyboard_Mouse_Support` | [`Keyboard_Mouse_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#Keyboard_Mouse_Support), [`Keyboard_Input_2Handed_Touch`](https://developer.android.com/games/large-screen/tier-2.md.txt#Keyboard_Input_2Handed_Touch), [`Keyboard_Input_Multi_Touch`](https://developer.android.com/games/large-screen/tier-2.md.txt#Keyboard_Input_Multi_Touch), [`Keyboard_Input_Swiping`](https://developer.android.com/games/large-screen/tier-2.md.txt#Keyboard_Input_Swiping) | Connect an external keyboard and mouse or trackpad. Play the game from initial launch through menus, settings, and core gameplay loops without touching the screen. Verify complete start-to-finish playability using a keyboard, mouse, or both across all core gameplay mechanics and menus. Verify that basic taps, drags, and menu scrolling respond 1:1 to primary mouse clicks and trackpad interactions, and verify that any gameplay mechanics requiring two-handed touch, simultaneous multi-finger gestures (such as a two-finger swipe), or rapid swiping have working keyboard or mouse alternatives. |
| `T-Keyboard_Hotplugging_Support` | [`Keyboard_Hotplugging_Support`](https://developer.android.com/games/large-screen/tier-2.md.txt#Keyboard_Hotplugging_Support) | While the game is running, connect and disconnect an external keyboard (wired or wireless). Verify that the game continues running uninterrupted without crashing or restarting. When toggled during text entry, verify that the UI gracefully handles the presence and disappearance of the virtual keyboard and remains functional both with and without a physical keyboard. |
| `T-No_Virtual_Keyboards` | [`No_Virtual_Keyboards`](https://developer.android.com/games/large-screen/tier-2.md.txt#No_Virtual_Keyboards) | While focused on an editable text field within the game: - Connect an external keyboard and confirm that any virtual keyboard disappears. The editable text field should continue to work with the external keyboard. - Disconnect the external keyboard and confirm that a virtual keyboard appears and can be used to edit the text field. |
| `T-Content_Zoom` | [`Content_Zoom`](https://developer.android.com/games/large-screen/tier-2.md.txt#Content_Zoom) | *If applicable*: use the mouse scroll wheel, two-finger trackpad scroll, or trackpad pinch gestures (when pointer capture isn't active) to zoom in and out of game cameras or maps. |
| `T-Content_Scroll` | [`Content_Scroll`](https://developer.android.com/games/large-screen/tier-2.md.txt#Content_Scroll) | *If applicable*: use the mouse scroll wheel or two-finger trackpad scroll to scroll content smoothly across the screen. |
| `T-Custom_Cursors` | [`Custom_Cursors`](https://developer.android.com/games/large-screen/tier-2.md.txt#Custom_Cursors) | If the mouse icon changes in the game, verify that you can move the mouse out of the window without getting stuck at the window border. Verify that moving your finger across a trackpad in-game moves the mouse the same distance as the OS when maintaining the same speed and distance. |
| `T-Menu_Navigation` | [`Menu_Navigation`](https://developer.android.com/games/large-screen/tier-2.md.txt#Menu_Navigation) | Navigate through all menus, inventories, and chat fields (for example, by using **Tab** , arrow keys or **WASD** , or function keys), verifying that the currently focused menu item is clearly visible. Press **Esc** inside modals, submenus, text fields, and active gameplay to verify that overlays close, text focus cancels, and active gameplay pauses or opens the pause menu. |
| `T-Enter_Key` | [`Enter_Key`](https://developer.android.com/games/large-screen/tier-2.md.txt#Enter_Key) | Use the **Enter** key of an external keyboard to send or submit data, such as when entering text. |
| `T-Back_Key` | [`Back_Key`](https://developer.android.com/games/large-screen/tier-2.md.txt#Back_Key) | Use the **Back** key on keyboards that support it, or the **Esc** key of an external keyboard, to perform a back function. Verify that the key performs the following actions where applicable: - Closes modals, dialogs, and menus. - Clears search text or removes search focus. - Cancels keyboard focus. - Dismisses on-screen controls. - Deselects all selected items. - Cancels renaming or editing without saving. - Exits the game after prompting the player before quitting. |
| `T-Mouse_Capture` | [`Mouse_Capture`](https://developer.android.com/games/large-screen/tier-2.md.txt#Mouse_Capture), [`FPS_Mouse_Capture`](https://developer.android.com/games/large-screen/tier-2.md.txt#FPS_Mouse_Capture) | *If the game features 3D, first-person, or third-person camera-look mechanics*: verify that the mouse cursor is captured (`requestPointerCapture()`) during active gameplay so camera rotation is continuous without stopping at screen edges, and verify that pointer capture is released (`releasePointerCapture()`) immediately when pressing **Esc**, opening the pause or settings menu, or switching window focus. |
| `T-Secondary_Actions` | [`Secondary_Actions`](https://developer.android.com/games/large-screen/tier-2.md.txt#Secondary_Actions) | *If applicable*: use the secondary mouse button (right-click) or two-finger trackpad tap to trigger secondary actions (for example, aiming in an FPS game) or open context menus. |
| `T-Hover_States` | [`Hover_States`](https://developer.android.com/games/large-screen/tier-2.md.txt#Hover_States) | Hover the mouse or trackpad cursor over actionable buttons and inventory items to verify that hover states or tooltips appear. |

### Audio

The following table describes the audio tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Audio_Peripheral_Switching` | [`Audio_Peripheral_Switching`](https://developer.android.com/games/large-screen/tier-2.md.txt#Audio_Peripheral_Switching) | Connect and disconnect USB or Bluetooth headphones or headsets during active gameplay and cutscene playback. Verify that game audio routes seamlessly to the active output device and back without muting, stuttering, or crashing. |