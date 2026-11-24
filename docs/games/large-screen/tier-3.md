---
title: https://developer.android.com/games/large-screen/tier-3
url: https://developer.android.com/games/large-screen/tier-3
source: md.txt
---

> Documentation index: https://developer.android.com/games/llms.txt

Games that are Tier 3 (Ready) render full screen across their supported layout
orientations and anchor aspect ratios when display bounds match on large screens
and foldables. They handle dynamic configuration changes---such as folding,
unfolding, rotation, and window resizing---without losing state or
offsetting touch inputs, and they support multi-window and multi-resume
continuity. When the window orientation or aspect ratio differs, the game
renders clean letterboxes or pillarboxes.

![Depiction of the three quality tiers as layers stacked vertically with the bottom tier highlighted.](https://developer.android.com/static/images/docs/quality-guidelines/tier-3/tier_3_header.png)

The guidelines on this page apply directly to foldables and tablets. Other form
factors, such as desktops, TVs, car displays, and XR, have additional
form-factor-specific requirements. Games distributed on those devices must also
meet the Tier 3 requirements for each form factor where you distribute them.

## Expected player experience

A Tier 3 game feels natural, stable, and uninterrupted on any large screen or
foldable device. Players can launch the game on an unfolded foldable or tablet
and play immediately without system compatibility overrides, cropped heads-up
display (HUD) buttons, or stretched graphics. If a player unfolds their phone
mid-match, rotates the device, or resizes the window in split-screen mode, the
game transitions smoothly without crashing, restarting the level, losing audio
sync, or shifting touch hit-boxes. The game must also meet the Tier 3
requirements for each form factor where you distribute the game.

### Do

Follow these best practices to provide a Tier 3 experience:

- Render full screen across supported foldable and tablet anchor aspect ratios: 1:1, 10:9, and 4:3 in landscape (1:1, 9:10, and 3:4 in portrait) for unfolded foldable inner screens, and 16:10 in landscape (10:16 in portrait) for tablets and folded passport-style foldable cover screens. For portrait-only games, support rotating to landscape on both unfolded foldables and tablets (rendering full screen on 1:1 and 10:9 inner screens, and cleanly pillarboxing on 4:3 and 16:10 displays). For landscape-only games, support rotating to portrait on unfolded foldable inner screens (rendering full screen on 1:1 and 9:10 inner screens, and cleanly letterboxing on 3:4 inner screens), while portrait rotation isn't required on tablets (10:16) or folded cover screens.
- Preserve active gameplay state, camera viewport, audio sync, and accurate touch hit-boxes across folding and unfolding, device rotation, and multi-window resizing.
- Support multi-window split-screen and multi-resume focus transitions, including camera preview and media projection continuity where applicable.

### Don't

Avoid the following common issues:

- Rely on OS or manufacturer compatibility mode letterboxing. Instead, declare `android:resizeableActivity="true"`.
- Let HUD buttons, health bars, or menus get clipped by camera cutouts, gesture bars, or multi-window split-screen control headers.
- Restart the activity, drop multiplayer connections, or desync touch coordinates when the device folds, unfolds, rotates, or resizes.
- Stretch or compress the game viewport, characters, or UI elements (non-uniform aspect-ratio scaling) to fill the screen instead of adapting the camera field of view (FOV) or cleanly letterboxing or pillarboxing.

## Guidelines

The following sections describe the Tier 3 quality guidelines for games on
large screens and foldables.

### Display and aspect ratios

The following table describes the display and aspect ratio guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Landscape_Display` | [`T-Landscape_Display`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Landscape_Display) | Games displayed in landscape render full screen without letterboxing or pillarboxing across foldable and tablet landscape aspect ratios (1:1, 10:9, 4:3, and 16:10): - **Foldable inner displays (unfolded)**: 1:1, 10:9, and 4:3. - **Foldable passport-style cover displays (folded)**: 16:10. - **Tablets**: 16:10. The game declares `android:resizeableActivity="true"` so it doesn't run in OS compatibility mode. |
| `Landscape_Rotation` | [`T-Landscape_Rotation`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Landscape_Rotation) | On unfolded foldable inner displays, landscape-only games support rotating to portrait orientation (rotating right-side up when the unfolded foldable is rotated): - **Square and near-square inner displays (1:1 and 9:10)**: the game rotates and renders full screen in both orientations. - **Rectangular inner displays (3:4)**: the game rotates right-side up and cleanly letterboxes itself (without relying on OS or manufacturer compatibility overrides) if it doesn't support a vertical portrait layout. - **Tablets (10:16) and folded cover screens**: landscape-only games aren't required to support portrait orientation, where narrow vertical dimensions would shrink a horizontal game viewport into a small strip. |
| `Portrait_Display` | [`T-Portrait_Display`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Portrait_Display) | Games displayed in portrait render full screen without letterboxing or pillarboxing across foldable and tablet portrait aspect ratios (1:1, 9:10, 3:4, and 10:16): - **Foldable inner displays (unfolded)**: 1:1, 9:10, and 3:4. - **Foldable passport-style cover displays (folded)**: 10:16. - **Tablets**: 10:16. The game declares `android:resizeableActivity="true"` so it doesn't run in OS compatibility mode. |
| `Portrait_Rotation` | [`T-Portrait_Rotation`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Portrait_Rotation) | On both unfolded foldables and tablets, portrait-only games don't lock orientation on unfolded foldables and support rotating to landscape orientation (rotating right-side up when the device is rotated): - **Square and near-square inner displays (1:1 and 10:9)**: the game rotates and renders full screen in both orientations. - **Rectangular landscape displays (4:3 unfolded passport-style foldables and 16:10 tablets)**: the game rotates right-side up and cleanly pillarboxes itself (without relying on OS or manufacturer compatibility overrides) if it doesn't support a horizontal landscape layout. |
| `Insets_And_Cutouts` | [`T-Insets_And_Cutouts`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Insets_And_Cutouts) | The game queries and respects actual visible window insets---even after requesting immersive full-screen mode---so game controls, HUDs, and UI elements aren't obscured by mobile status, navigation, or gesture bars, display cutouts (such as notches and punch holes), multi-window split-screen control headers, or persistent bottom taskbars and Kids mode navigation bars. |

### Configuration and continuity

The following table describes the configuration and continuity guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Config_Changes` | [`T-Config_State`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Config_State) | The game supports configuration changes---such as device rotation, folding and unfolding (including sequential transitions such as rotating after unfolding), multi-window resizing, and display changes---without crashes, ANRs, level restarts, visual artifacts, or touch mapping offsets where visual UI buttons desync from their touch hit-boxes. The game preserves active game state and player progress: - Active gameplay session and camera viewport are maintained. - Scroll position of scrollable menus and inventories is maintained. - Text typed into text fields is retained and keyboard state is restored. - Cutscene and audio playback resumes where it left off, and audio playback remains smooth and in sync with gameplay and video. |

### Multi-window mode and multi-resume

The following table describes the multi-window mode and multi-resume guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Multi-Window_Functionality` | [`T-Multi-Window_Functionality`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Multi-Window_Functionality) | The game is fully functional and playable in multi-window split-screen mode, including when running in a 50/50 split-screen window. |
| `Multi-Resume` | [`T-Multi-Window_Focus`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Multi-Window_Focus), [`T-Multi-Window_Resources`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Multi-Window_Resources) | The game supports multi-resume and window focus transitions in multi-window scenarios: - **Focus and state continuity** : when visible in multi-window or desktop windowing mode but not the top focused window, the game handles paused, resumed, and unfocused lifecycle states (`onWindowFocusChanged`, `onTopResumedActivityChanged`, `onPause`, and `onResume`) without crashing, freezing (ANR), or losing its rendering surface. Single-player or offline games pause cleanly or continue updating the UI without freezing, and online or multiplayer games maintain network connectivity without dropping the active session. - **Audio and exclusive hardware resources**: the game mutes or ducks audio appropriately when unfocused, and cleanly relinquishes exclusive hardware resources (such as cameras or microphones used for voice chat) when losing focus, regaining them when focus returns. |

### Camera preview and media projection

The following guidelines apply only to games that use the device camera or
`MediaProjection` APIs:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Camera_Preview` | [`T-Camera_Preview`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Camera_Preview) | *If the game displays a camera preview (for example, AR gameplay, QR scanning, or avatar and profile photo capture)*: the game provides a camera preview in landscape and portrait orientations, folded and unfolded device states, and multi-window mode, with proper proportions and orientation (no stretching, cropping, or inversion). The game doesn't enforce a hard manifest requirement on a rear- or world-facing camera (setting `android:required="false"` on `android.hardware.camera` or using `android.hardware.camera.any`), falls back gracefully to any available camera (such as a front-facing webcam on laptops and Googlebooks) as a sensible default, and lets players switch cameras when multiple cameras are available. |
| `Media_Projection` | [`T-Media_Projection`](https://developer.android.com/games/large-screen/tier-3.md.txt#T-Media_Projection) | *If the game uses `MediaProjection` (for example, in-game clip recording, replay capture, or livestreaming)*: the game supports media projection in landscape and portrait orientations, folded and unfolded device states, and multi-window mode. The projection is properly proportioned and in the correct orientation. |

## Tests

To confirm that your game meets the Tier 3 (Ready) requirements, run the
following verification tests.

### Display and aspect ratios

The following table describes the display and aspect ratio tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Landscape_Display` | [`Landscape_Display`](https://developer.android.com/games/large-screen/tier-3.md.txt#Landscape_Display) | On foldable and tablet devices, test the game in landscape orientation across the core foldable and tablet landscape aspect ratios (1:1, 10:9, and 4:3 for unfolded foldable inner displays; 16:10 for tablets and folded passport-style cover displays). Verify that if the game supports landscape, it fills the entire window without letterboxing or pillarboxing and doesn't run in OS compatibility mode. |
| `T-Landscape_Rotation` | [`Landscape_Rotation`](https://developer.android.com/games/large-screen/tier-3.md.txt#Landscape_Rotation) | If the game is landscape-only, rotate the unfolded foldable 90 degrees to portrait orientation and verify that the game rotates right-side up: on square and near-square inner displays (1:1 and 9:10) it continues rendering full screen, and on 3:4 inner displays it cleanly letterboxes itself with centered framing and working touch targets (portrait rotation isn't required on 10:16 tablets or folded cover screens). |
| `T-Portrait_Display` | [`Portrait_Display`](https://developer.android.com/games/large-screen/tier-3.md.txt#Portrait_Display) | On foldable and tablet devices, test the game in portrait orientation across the core foldable and tablet portrait aspect ratios (1:1, 9:10, and 3:4 for unfolded foldable inner displays; 10:16 for tablets and folded passport-style cover displays). Verify that if the game supports portrait, it fills the entire window without letterboxing or pillarboxing and doesn't run in OS compatibility mode. |
| `T-Portrait_Rotation` | [`Portrait_Rotation`](https://developer.android.com/games/large-screen/tier-3.md.txt#Portrait_Rotation) | If the game is portrait-only, rotate the unfolded foldable or tablet 90 degrees to landscape orientation and verify that the game rotates right-side up: on square and near-square inner displays (1:1 and 10:9) it continues rendering full screen, and on rectangular landscape displays (4:3 and 16:10) it cleanly pillarboxes itself with centered framing and working touch targets. |
| `T-Insets_And_Cutouts` | [`Insets_And_Cutouts`](https://developer.android.com/games/large-screen/tier-3.md.txt#Insets_And_Cutouts) | Launch the game across phone, foldable (folded and unfolded), and tablet displays in all supported orientations (including multi-window split-screen and modes with persistent bottom bars such as taskbars or Kids mode). Verify that no interactive game controls, HUD buttons, or critical text are obscured by status, navigation, or gesture bars, display cutouts, persistent bottom bars, or split-screen control headers. |

### Configuration and continuity

The following table describes the configuration and continuity tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Config_State` | [`Config_Changes`](https://developer.android.com/games/large-screen/tier-3.md.txt#Config_Changes) | During active gameplay (and on screens with scrollable menus, audio or cutscene playback, or text entry fields), rotate the device between landscape and portrait orientations, fold and unfold the device, resize the game window in multi-window mode, and minimize and restore the window. Verify the following: - The game doesn't crash, freeze (ANR), or restart the current level or session. - Active gameplay state, scroll positions, cutscene playback (with smooth, in-sync audio), and text typed into input fields are retained. - Touch input hit-boxes match the visual position of all on-screen buttons with zero touch mapping offset. |

### Multi-window mode and multi-resume

The following table describes the multi-window mode and multi-resume tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Multi-Window_Functionality` | [`Multi-Window_Functionality`](https://developer.android.com/games/large-screen/tier-3.md.txt#Multi-Window_Functionality) | Open the game in multi-window mode. Check that the game is fully playable across window sizes, orientations, and folded or unfolded states. **Unity games** : open an app other than your Unity game and place it in split-screen mode. Open your Unity game alongside it. Go to the **Home** screen to hide the app pair, and then open the **Recents** screen and select the split-screen app pair. Verify that the Unity game resumes its activity cleanly with the correct layout and accessible UI elements. |
| `T-Multi-Window_Focus` | [`Multi-Resume`](https://developer.android.com/games/large-screen/tier-3.md.txt#Multi-Resume) | Open the game in multi-window or desktop windowing mode alongside a second app and click into the second app to make it the top focused window, testing focus loss and return. Verify that the game doesn't crash, freeze (ANR), or lose its graphics surface when unfocused; single-player or offline gameplay pauses cleanly (or continues updating without freezing); online or multiplayer gameplay maintains its network connection without disconnecting; and game audio mutes or ducks appropriately. |
| `T-Multi-Window_Resources` | [`Multi-Resume`](https://developer.android.com/games/large-screen/tier-3.md.txt#Multi-Resume) | *If the game uses the camera or microphone*: open the camera or enable voice chat in the game while in multi-window mode, and then switch focus to the second app. Verify that the unfocused game relinquishes the camera or microphone and regains access when returned to focus. |

### Camera preview and media projection

The following table describes the camera preview and media projection tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Camera_Preview` | [`Camera_Preview`](https://developer.android.com/games/large-screen/tier-3.md.txt#Camera_Preview) | *If applicable*: open the game full screen and in multi-window mode, and start the camera from within the game, including on a device with only a front-facing camera, and switch cameras where multiple exist. Rotate the device, fold and unfold the device, and resize the window. Verify that the camera preview defaults cleanly and displays in the proper orientation and proportions in all states. |
| `T-Media_Projection` | [`Media_Projection`](https://developer.android.com/games/large-screen/tier-3.md.txt#Media_Projection) | *If applicable*: open the game full screen and in multi-window mode, and start a media projection. Rotate the device, fold and unfold the device, and resize the window. Verify that the media projection is in the proper orientation and proportions in all states. |