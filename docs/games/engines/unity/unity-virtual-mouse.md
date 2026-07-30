---
title: https://developer.android.com/games/engines/unity/unity-virtual-mouse
url: https://developer.android.com/games/engines/unity/unity-virtual-mouse
source: md.txt
---

When developing Android games for a wide range of form factors---including
foldables, tablets, and large screens---players often connect external
controllers or gamepads. For UI screens originally designed for touch or mouse
interactions, navigating menus with a controller can be challenging.

While redesigning your UI architecture around standard D-pad navigation
generally provides a better user experience, it might not always be feasible
for existing projects. As an alternative option, the Unity Input System
provides the [`VirtualMouseInput`](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.UI.VirtualMouseInput.html) component. This component
lets you drive a virtual, on-screen software cursor using a connected gamepad
or controller.

## About VirtualMouseInput

The `VirtualMouseInput` component is a high-level utility in the Unity Input
System package that bridges gamepad inputs to on-screen cursor control, UI
pointer interactions, and simulated touchscreen events. When active, it:

- **Creates a virtual mouse device:** It registers a software-simulated mouse in the Unity Input System alongside any physical pointing devices.
- **Maps gamepad controls to cursor actions:** You can bind analog sticks or D-pads to move the cursor across the screen, and map controller buttons (such as Button South / A) to simulate left, right, or middle mouse clicks.
- **Integrates with Unity UI:** By working seamlessly with the `InputSystemUIInputModule`, standard UI elements like buttons, toggles, and sliders respond to the virtual cursor exactly as they would to a hardware mouse or touch interaction.
- **Drives a visual cursor:** It lets you assign a UI `Graphic` (such as an `Image` component) that automatically tracks and renders the virtual cursor's position on screen.

## Combine virtual mouse with TouchSimulation

If your game was originally designed exclusively for touchscreens and relies on
direct touch scripts or APIs, a virtual mouse will not automatically trigger
your existing touch detection logic because it registers as a mouse device
rather than a touchscreen device.

To support gamepad-driven cursor interaction without rewriting your legacy touch
handling code, you can use the Unity Input System's
[`TouchSimulation`](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.EnhancedTouch.TouchSimulation.html) feature alongside `VirtualMouseInput`:

- **How it works:** When enabled using `TouchSimulation.Enable()`, the Input System automatically converts clicks and pointer movements from any active mouse device---including the software-simulated mouse created by `VirtualMouseInput`---into simulated touchscreen events.
- **Resulting data flow:** Your gamepad stick and button interactions drive the virtual mouse, which `TouchSimulation` then translates into single-touch events (`Touchscreen`). Your existing touch detection scripts can process these events seamlessly without code modification.
- **Considerations:** `TouchSimulation` is limited to single-touch pointer emulation. If your gameplay relies on complex multi-touch gestures such as pinch-to-zoom or two-finger rotation, you must configure dedicated input action bindings for your gamepad controls.

For complete technical details, properties, and usage documentation, refer to
the official [`UnityEngine.InputSystem.UI.VirtualMouseInput`](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.UI.VirtualMouseInput.html)
and [`UnityEngine.InputSystem.EnhancedTouch.TouchSimulation`](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/api/UnityEngine.InputSystem.EnhancedTouch.TouchSimulation.html)
script references.