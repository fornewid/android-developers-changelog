---
title: https://developer.android.com/games/large-screen/foldables
url: https://developer.android.com/games/large-screen/foldables
source: md.txt
---

> Documentation index: https://developer.android.com/games/llms.txt

Games that achieve Tier 1 (Differentiated) on foldables build upon
[Tier 2 (Optimized)](https://developer.android.com/games/large-screen/tier-2.md.txt) to deliver an optimal gaming experience designed
for the physical and thermal characteristics of foldable hardware. Tier 1 for
foldables focuses on sustained frame-rate performance and proactive thermal
management inside an ultra-thin split chassis, modern Vulkan 1.1 and higher
rendering efficiency (or ANGLE where the engine doesn't support Vulkan), and
sub-second cover-to-inner display transitions that expand the camera field of
view (FOV) across 1:1 and 4:3 inner screens without cropping.

![Depiction of the three quality tiers as layers stacked vertically with the top tier highlighted.](https://developer.android.com/static/images/docs/quality-guidelines/tier-1/tier_1_header.png)

## Expected player experience

A Tier 1 game on foldables delivers sustained high-frame-rate performance and
expansive visual immersion on the unfolded inner display without hitting a
thermal throttling cliff. Because an unfolded foldable renders roughly twice the
pixel count of a standard phone inside a 4.5 mm to 5 mm split chassis,
Tier 1 games use Vulkan 1.1 and higher rendering (or ANGLE if the engine doesn't
natively support Vulkan) and dynamic thermal management---such as the
[Android Dynamic Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf.md.txt)---to sustain smooth
60 FPS gameplay (up to 120 FPS where supported) over extended sessions
of 10 minutes or more without overheating or sudden frame drops.

Unfolding from the compact cover screen to the 1:1 or 4:3 inner display, or
folding back to the cover screen, transitions in under one second with no
black-screen delay where applicable, or smoothly pauses gameplay so players can
find a comfortable hold on their phone. The transition expands the game's FOV to
show more of the game world rather than less, while keeping heads-up display
(HUD) touch controls anchored comfortably in the lower thumb arcs and clear of
the physical hinge crease.

### Do

Follow these best practices to provide a Tier 1 experience on foldables:

- Sustain target frame rates (60 FPS across all games, and provide a user option for 120 FPS on 120 Hz displays where supported) over 10-minute unfolded gameplay sessions without thermal throttling cliffs by using Vulkan 1.1 and higher rendering (or ANGLE where the engine doesn't support Vulkan) and dynamic thermal adaptation such as ADPF.
- Tailor the camera FOV (expanding horizontal and vertical framing rather than zooming in and cropping on 1:1 and 4:3 displays), high-density textures, and thumb-arc HUD ergonomics when transitioning seamlessly between the compact outer cover screen and the expansive unfolded inner display.
- Support adaptive refresh rates from 30 Hz to 120 Hz on low-temperature polycrystalline oxide (LTPO) displays, automatic render-resolution step-down when folded to the cover screen, and smooth side-by-side companion split-screen on the unfolded inner display.

### Don't

Avoid the following common issues:

- Allow unfolded high-resolution rendering to trigger severe thermal throttling, frame-rate collapse, or uncomfortable surface temperatures during 10-minute gameplay sessions.
- Continue rendering at full inner-screen resolution when folded to the cover screen.
- Zoom in and crop the peripheral game world (Vert- or Hor- camera cropping) when unfolding to a 1:1 or 4:3 inner display, or place interactive UI elements directly along the physical hinge crease whenever possible.

## Guidelines

The following sections describe the Tier 1 quality guidelines for games on
foldable devices.

### Sustained performance, thermals, and unfolded presentation

The following table describes the sustained performance, thermal management, and
unfolded presentation guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Foldables_Sustained_Performance_And_Thermals` | [`T-Foldables_Thermal_Sustainability`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Thermal_Sustainability) | The game maintains thermal stability and consistent frame pacing across extended gameplay sessions (10 minutes or more) on the unfolded inner display without triggering severe thermal throttling cliffs, frame-rate collapse, or uncomfortable surface temperatures: - **Proactive thermal management (ADPF)** : integrate the [Android Dynamic Performance Framework](https://developer.android.com/games/optimize/adpf.md.txt) or equivalent engine-level dynamic resolution and quality scaling to step down the rendering workload before the foldable chassis reaches `THERMAL_STATUS_SEVERE`, preventing sudden frame-rate cliffs and keeping surface temperatures comfortable. |
| `Foldables_Frame_Rate_And_High_Refresh` | [`T-Foldables_Frame_Rate`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Frame_Rate) | The game targets and sustains 60 FPS during active gameplay on the unfolded inner display, and provides a user option for 120 FPS high-refresh-rate rendering on 120 Hz foldable inner displays where supported. |
| `Foldables_Cover_Screen_Resolution_Scaling` | [`T-Foldables_Cover_Screen_Scaling`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Cover_Screen_Scaling) | When folded to the outer cover screen, the game steps down its internal render target to match the cover display resolution rather than continuing to render at full unfolded inner-display resolution, preventing unnecessary GPU load, battery drain, and heat generation in the folded state. |
| `Foldables_Hinge_Ergonomics_And_Thumb_Zones` | [`T-Foldables_Hinge_Ergonomics`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Hinge_Ergonomics) | When the foldable device is held in **book posture** (half-opened with a vertical hinge crease) or fully unfolded on the inner display, the game isn't required to force a 50/50 split layout, which can feel cramped on smaller foldables. However, the game must avoid splitting interactive UI rows or buttons across the physical hinge crease and must anchor virtual joysticks and primary touch controls within comfortable lower-left and lower-right thumb arcs. |
| `Foldables_Cover_To_Inner_Transition` | [`T-Foldables_Cover_To_Inner`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Cover_To_Inner) | The game dynamically tailors UI density and camera framing between the compact **folded outer cover screen** and the expansive **unfolded inner display**: - **Sub-second open and close continuity**: physical fold and unfold transitions between the compact cover screen (approximately 20:9 or 21:9) and the unfolded inner display (1:1 or 4:3) complete in under one second with no black-screen delays or loading spinners. - **Expansive FOV without camera cropping (Hor+ and Vert+)**: unfolding to the 1:1 or 4:3 inner display expands or preserves the visible camera FOV rather than zooming in and cropping the sides of a widescreen viewport (avoiding Vert- or Hor- cropping), and delivers high-density, tablet-grade textures. |
| `Foldables_Vulkan_And_Shader_Efficiency` | [`T-Foldables_Vulkan_And_Shader_Efficiency`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Vulkan_And_Shader_Efficiency) | The game uses Vulkan 1.1 and higher as its primary rendering API on high-resolution foldable panels (`FEATURE_VULKAN_DEQP_LEVEL >= 20240301`), rendering at least 90% of gameplay frames in Vulkan (fewer than 10% in OpenGL ES, or opting into ANGLE over Vulkan for legacy engines earlier than Unity 2023 and Unreal 4.25). The game uses pipeline cache pre-warming and precompiled shader caches to eliminate live shader compilation hitches during active gameplay. |

### Multitasking and multi-instance

The following table describes the multitasking and multi-instance guidelines:

| Guideline ID | Test IDs | Description |
|---|---|---|
| `Foldables_Multitasking_Scenarios` | [`T-Foldables_Companion_Split`](https://developer.android.com/games/large-screen/foldables.md.txt#T-Foldables_Companion_Split) | The game runs smoothly in side-by-side split-screen mode on the unfolded inner display (for example, alongside a walkthrough video, voice chat app, or strategy guide), dynamically adapting its HUD to fit the half-screen foldable aspect ratio (approximately 8:9 or 9:8) while maintaining stable frame pacing and thermal balance. |

## Tests

To confirm that your game meets the Tier 1 (Differentiated) requirements on
foldable devices, run the following verification tests.

### Sustained performance, thermals, and unfolded presentation

The following table describes the sustained performance, thermal management, and
unfolded presentation tests:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Foldables_Thermal_Sustainability` | [`Foldables_Sustained_Performance_And_Thermals`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Sustained_Performance_And_Thermals) | Play active gameplay on the unfolded inner display for 10 minutes with thermal and frame-timing telemetry enabled. Verify that the game maintains stable frame pacing without triggering severe thermal throttling cliffs or critical overheating, using ADPF thermal callbacks or dynamic resolution and quality scaling as recommended. |
| `T-Foldables_Frame_Rate` | [`Foldables_Frame_Rate_And_High_Refresh`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Frame_Rate_And_High_Refresh) | Record frame-timing telemetry during active unfolded gameplay and verify that the game sustains 60 FPS (and supports 120 FPS on 120 Hz foldable displays where enabled) with the following metrics: - **Average FPS**: at least 55 FPS. - **Low 10% (P90) FPS**: at least 50 FPS. - **Low 1% (P99) FPS**: at least 30 FPS. Active gameplay excludes loading screens, menus, lobbies, and cutscenes. |
| `T-Foldables_Cover_Screen_Scaling` | [`Foldables_Cover_Screen_Resolution_Scaling`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Cover_Screen_Resolution_Scaling) | Fold the device to the outer cover screen during active gameplay and verify through GPU or display profiling that the internal render target steps down to match the cover display resolution rather than rendering at full inner-screen resolution. |
| `T-Foldables_Hinge_Ergonomics` | [`Foldables_Hinge_Ergonomics_And_Thumb_Zones`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Hinge_Ergonomics_And_Thumb_Zones) | Hold the foldable device in book posture and fully unfolded on the inner display. Verify that no interactive buttons or UI rows are bisected by the physical hinge crease and that virtual joysticks and primary touch controls sit within comfortable lower-left and lower-right thumb arcs. |
| `T-Foldables_Cover_To_Inner` | [`Foldables_Cover_To_Inner_Transition`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Cover_To_Inner_Transition) | Start a gameplay session on the folded outer cover screen (approximately 20:9 or 21:9), and then unfold the device to the inner display (1:1 or 4:3) and fold it back again. Verify that the transition completes in under one second with no black-screen delay, and verify that the unfolded camera preserves or expands the FOV (Hor+ and Vert+) rather than zooming in and cropping the game world. |
| `T-Foldables_Vulkan_And_Shader_Efficiency` | [`Foldables_Vulkan_And_Shader_Efficiency`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Vulkan_And_Shader_Efficiency) | Run the game on a foldable reference device with GPU profiling enabled. Verify that at least 90% of gameplay frames render using Vulkan 1.1 and higher (or using ANGLE translating OpenGL ES to Vulkan if the game engine doesn't natively support Vulkan), pre-warmed shader caches prevent compilation hitches during gameplay and fold or unfold transitions, and the display refresh rate steps down in static menus and idle states on LTPO panels. |

### Multitasking and multi-instance

The following table describes the multitasking and multi-instance test:

| Test ID | Guideline IDs | Description |
|---|---|---|
| `T-Foldables_Companion_Split` | [`Foldables_Multitasking_Scenarios`](https://developer.android.com/games/large-screen/foldables.md.txt#Foldables_Multitasking_Scenarios) | With the foldable device unfolded, open the game side by side with a companion app in split-screen mode. Drag the split-screen divider to resize the game window and verify that the HUD adapts cleanly and gameplay remains smooth and responsive. |