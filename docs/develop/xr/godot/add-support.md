---
title: https://developer.android.com/develop/xr/godot/add-support
url: https://developer.android.com/develop/xr/godot/add-support
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

If you have an existing XR project in Godot, you can add support for Android XR
without starting a new, separate project. Some steps are required for all
projects, while others are optional depending on the XR features that your
project uses. Throughout the steps, we've included links to multiple open-source
Godot XR projects that have added support for Android XR, along with relevant
pull requests that showcase the changes that are required to enable certain
features.

## Required steps for all projects

Complete the steps in the following topics no matter what types of XR features
your project supports. Afterwards, review the features outlined in the [list of
optional steps]() to determine whether your project requires additional work.

### Update Godot and the Godot OpenXR Vendors Plugin

[![](https://developer.android.com/static/images/picto-icons/code.svg) Learn by example See a pull request to learn with a real-world example.](https://github.com/m4ym4y/museum-of-all-things/pull/154)

Follow these steps to update your project to the latest required versions and
configure your project's settings for Android XR:

1. Update your Godot version to 4.6.2 or higher. See the documentation on [migrating to a new version](https://docs.godotengine.org/en/stable/tutorials/migrating/index.html) if you need additional help for your project.
2. Download [Godot OpenXR Vendors Plugin](https://godotvr.github.io/godot_openxr_vendors/) version 5.1 or
   higher from the [Asset Store](https://store.godotengine.org/asset/godot-xr/godot-openxr-vendors-plugin/), [Asset Library](https://godotengine.org/asset-library/asset/5014)
   or [the repository on GitHub](https://github.com/GodotVR/godot_openxr_vendors/releases).

3. Configure your project's settings for Android XR:

   1. Add an export preset for Android XR.
   2. Enable **Use Gradle Build**.

   ![Enable the](https://developer.android.com/static/images/develop/xr/godot/use-gradle-build.png)
   1. In the **XR Features** section, select **OpenXR** for the **XR Mode** , and select **Enable AndroidXR Plugin**.

   ![Configure the options in the](https://developer.android.com/static/images/develop/xr/godot/xr-features.png)

### Add support for hand tracking

[![](https://developer.android.com/static/images/picto-icons/code.svg) Learn by example See a pull request to learn with a real-world example.](https://github.com/m4ym4y/museum-of-all-things/pull/153)

While controllers might be available, the primary input method on Android XR
headsets and XR glasses is hand tracking. If possible, you should add hand
tracking support to your Godot project.

#### Add support for hand tracking: Configure project settings

First, follow these steps to set up your project settings to enable hand
tracking and its related OpenXR extensions.

1. Open your project's settings and navigate to the **General \> XR \> OpenXR**.
2. In the **Extensions** section, select **Hand Tracking** and **Hand
   Interaction Profile**.

   ![Configure the options in the](https://developer.android.com/static/images/develop/xr/godot/project-settings-extensions.png)
3. Find the **Meta** subsection in the **Extensions** section, and select
   **Hand Tracking Mesh** and **Hand Tracking Aim**.

   ![Configure the options in the](https://developer.android.com/static/images/develop/xr/godot/project-settings-extensions-meta.png)

   > [!NOTE]
   > **Note:** These two extensions are listed in a **Meta** section because they were contributed to OpenXR by Meta, but they are also supported on Android XR and are required to implement hand tracking.

#### Add support for hand tracking: Add and configure controller nodes

Rather than dynamically modifying the existing `XRController3D` nodes for hand
tracking, add controller nodes for tracking and displaying the hand models, as
well as handling input from the Hand Tracking Aim extension:

1. Add three additional `XRController3D` nodes to your `XROrigin3D` node.

   1. Name one "HandTrackingLeft", and set the tracker property to `/user/hand_tracker/left`.
   2. Name another "HandTrackingRight", and set the tracker property to `/user/hand_tracker/right`.
   3. Name the last "HandTrackingAimLeft", and set the tracker property to `/user/fbhandaim/left`.

   If your project's original `XRController3D` nodes were named
   "XRController3D_left" and "XRController3D_right", your scene would look
   something like this:

   ![What your scene might look like after you've added the controller nodes.](https://developer.android.com/static/images/develop/xr/godot/controller-nodes.png)
2. [Connect the signal](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html#connecting-a-signal-in-the-editor) `tracking_changed` on
   **HandTrackingLeft** and **HandTrackingRight** to individual functions that
   update the visibility of the corresponding controller trackers
   (**XRController3D_left** and **XRController3D_right** in the preceding
   example).

   For example, the function connected to the signal on **HandTrackingLeft**
   could look like:

       func _on_hand_tracking_left_hand_tracking_changed(tracking):
           $XROrigin3D/XRController3D_left.visible = not tracking

3. Enable the **Show When Tracked** property on the hand tracking controller
   nodes.

   Now your project can visually swap between controller models and hand
   tracking models, depending on if the user is using hand tracking or
   controllers.
4. Add some `OpenXRFbHandTrackingMesh` nodes as children to your hand tracking
   controller nodes.

5. Add `XRHandModifier3D` nodes as children to these `OpenXRFbHandTrackingMesh`
   nodes, ensuring the correct **Hand Tracker** property is set, to apply real
   time hand tracking data to the models.

   ![What your scene might look like after you've added the child nodes to your
   controller nodes.](https://developer.android.com/static/images/develop/xr/godot/controller-child-nodes.png)

#### Add support for hand tracking: Set up a Hand Interaction profile on the OpenXR Action Map

Next, you'll set up the **Hand Interaction** profile on the **OpenXR Action
Map**:

1. Open the **OpenXR Action Map** menu at the bottom of the editor.
2. Delete the **Simple Controller** profile to avoid compatibility issues with Galaxy XR controllers.
3. Click **Add Profile** , select **Hand Interaction** , and then click **OK**.
4. Map this profile to one or more action sets however you like.

   > [!TIP]
   > **Tip:** All of the open-source projects that are linked from this guide and use use Hand Interaction mapped Hand Interaction's **Pinch** path to a newly-created "pinch" action in the "godot" action set. For more information, see the action maps of those projects. Starting in Godot 4.7, the Hand Interaction profile will have [more reasonable action map
   > defaults](https://github.com/godotengine/godot/pull/115605).

Depending on your app's requirements, you might also want to adjust [how your
app handles user input with hand tracking](https://developer.android.com/develop/xr/godot/add-support#optional-steps).

#### Add support for hand tracking: Set up a menu gesture for Android XR

Lastly, you can implement a menu gesture for Android XR. This shows an icon when
the player's left hand is in the correct position to perform the menu gesture,
as well as showing or hiding the menu when the user performs the gesture. You'll
use the **HandTrackingAimLeft** node that [you added earlier](https://developer.android.com/develop/xr/godot/add-support#hand-tracking-add-configure-nodes) to handle this.

1. Add a billboarded quad to the left hand tracking node displaying an icon
   that you've chosen (see the **MenuIcon** node in the following image from
   the controller nodes you added earlier).

   ![What your scene might look like after you've added the child nodes to your
   controller nodes.](https://developer.android.com/static/images/develop/xr/godot/controller-child-nodes.png)
2. Connect to the `button_pressed` and `button_released` signals on
   **HandTrackingAimLeft** to functions like this one:

       @onready var menu_icon: MeshInstance3D = $XROrigin3D/HandTrackingLeft/MenuIcon

       func _on_hand_tracking_aim_left_button_pressed(p_name):
         if p_name == "menu_pressed":
       toggle_menu()
         elif p_name == "menu_gesture":
           if OS.has_feature("androidxr"):
             menu_icon.visible = true

       func _on_hand_tracking_aim_left_button_released(p_name):
         if p_name == "menu_gesture":
           menu_icon.visible = false

## Optional steps for certain features

After completing the required steps for your project, you decide whether you
need to do additional work for certain features, depending on your app's
requirements and capabilities. For more information about each of these optional
features, see the following sections.

### Register pinches as button presses

In Android XR, [pinching is used for many foundational system actions](https://developer.android.com/design/ui/xr/guides/foundations#understanding-system), such
as selecting items, scrolling, moving or resizing windows, and moving UI
elements or objects in 2D and 3D space. To align with these patterns and promote
a consistent user experience, your app should register pinches similarly to
button presses on a controller when using hand tracking.

To configure your app this way, use the float values that are provided by the
[Hand Interaction profile that you created](https://developer.android.com/develop/xr/godot/add-support#hand-tracking-hand-interaction-profile) to create a virtual action:

    const PRESSED_THRESHOLD := 0.8
    const RELEASED_THRESHOLD := 0.6

    @onready var left_controller: XRController3D = $XROrigin/XRController3D_left

    func _on_xr_controller_3d_left_input_float_changed(p_name: String, value: float):
        if p_name == "pinch":
            var xr_tracker = XRServer.get_tracker(left_controller.tracker)
            if _left_hand_pinching:
                if value < RELEASED_THRESHOLD:
                    _left_hand_pinching = false
                    xr_tracker.set_input("pinch_pressed", false)
            else:
                if value > PRESSED_THRESHOLD:
                    _left_hand_pinching = true
                    xr_tracker.set_input("pinch_pressed", true)

#### Key points about the code

- Checks if the `float` value is greater than or less than specific thresholds in the `XRController3D` `input_float_changed` signals.
- Creates a virtual action called `pinch_pressed`.

### Use XR Tools functions together with hand tracking

Many Godot XR projects utilize [Godot XR Tools](https://godotvr.github.io/godot-xr-tools/), including some
of the open-source projects that are linked in this page. For some XR Tools
functions to work, such as `FunctionPointer` for menu interactions, you'll need
some additional code to swap the action it's looking for when the user switches
to hand tracking.

For example, when using `FunctionPointer` for menu interactions, update the
`active_button_action` property to the hand-tracking action based on the
`tracking_changed` signal of the `XRController3D` nodes for hand tracking (these
nodes were **HandTrackingLeft** and **HandTrackingRight** in the preceding [hand
tracking setup steps](https://developer.android.com/develop/xr/godot/add-support#hand-tracking-add-configure-nodes)).

    const TRIGGER_POINTER_ACTION = "trigger_click"
    const PINCH_POINTER_ACTION = "pinch_pressed"

    @onready var func_point_left: XRToolsFunctionPointer = %FunctionPointerLeft

    func _on_hand_tracking_left_tracking_changed(tracking: bool) -> void:
        if tracking:
            func_point_left.active_button_action = PINCH_POINTER_ACTION
    else:
    func_point_left.active_button_action = TRIGGER_POINTER_ACTION

#### Key points about the code

- This code relies on a `pinch_pressed` virtual action that [you can create to
  register pinches as button presses](https://developer.android.com/develop/xr/godot/add-support#pinches-button-presses).

### Use hand tracking together with artificial locomotion

If your project uses artificial locomotion, hand tracking support is still
possible. For example, you can build a movement system that lets players draw
paths to traverse with a gesture, or you can allow players to pump their hands
up and down to accelerate, with additional gestures for jumping, climbing, and
gliding.

[The Museum of All Things](https://github.com/m4ym4y/museum-of-all-things), has artificial locomotion using the
thumbsticks on the controllers. Hand tracking locomotion was implemented by
adding "virtual thumbsticks" that the player triggers by pinching in the air,
and moving their hand in the direction that they want that thumbstick to move.

Here are some of the key takeways from the [pull request that implemented this
support](https://github.com/m4ym4y/museum-of-all-things/pull/153):

- An `XRVirtualThumbstick` scene is instantiated when pinch is detected.
- While the pinch is held, the relative distance and direction from the original pinch location is turned to a `Vector2` and mapped virtually to the normal thumbstick input.
- Visual feedback of this input is also given to the player in the form of two billboarded quad meshes, illustrating the thumbstick position.

You can try a similar approach to get your existing thumbstick-driven locomotion
code to work with minimal changes. However, your project might still require a
custom locomotion solution for hand tracking.

### Add passthrough support

You can add passthrough support to your app so that your users can see their
real-world surroundings.

To do this for your app, make the following code changes:

- Set the `environment_blend_mode` of the OpenXR `XRInterface` to `XR_ENV_BLEND_MODE_ALPHA_BLEND`.
- Set the `background_mode` of the `WorldEnvironment` node to `BG_COLOR`.
- Set the `background_color` of the `WorldEnvironment` node to any color that is fully transparent.
- Set the `Viewport transparent_bg` property to `true`.

#### Use the light estimation extension

When enabling passthrough, consider using the Android XR Light Estimation OpenXR
extension. This extension tweaks properties of the `WorldEnvironment` and
`DirectionalLight3D` to better emulate the lighting of a user's real world
environment, so virtual objects blend in better with the real-world lighting
conditions. You can enable this extension in your project's settings.

1. Open your project's settings and navigate to the **General \> XR \> OpenXR**.
2. In the **Androidxr** section, select **Light Estimation**.

   ![Configure the options in the](https://developer.android.com/static/images/develop/xr/godot/project-settings-androidxr.png)
3. Add an `OpenXRAndroidLightEstimation` node to your scene tree and connect it
   to your scene's `WorldEnvironment` and `DirectionalLight3D`.

   ![Options for the](https://developer.android.com/static/images/develop/xr/godot/openxr-android-light-estimation.png)

#### Example: Enable or disable passthrough and light estimation

The following code enables or disables passthrough and light estimation:

    @onready var world_environment = $WorldEnvironment
    @onready var directional_light = $DirectionalLight3D
    @onready var directional_light_orig_transform: Transform3D = directional_light.transform

    func set_passthrough_enabled(p_enabled: bool) -> void:
        var xr_interface = XRServer.find_interface("OpenXR")
        if xr_interface == null:
            return

        var supported_blend_modes = xr_interface.get_supported_environment_blend_modes()
        if not supported_blend_modes.has(XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND):
            return

        # Passthrough
        if p_enabled:
            xr_interface.set_play_area_mode(XRInterface.XR_PLAY_AREA_STAGE)
            xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND
            world_environment.environment.background_mode = Environment.BG_COLOR
            world_environment.environment.background_color = Color(0.0, 0.0, 0.0, 0.0)
            get_viewport().transparent_bg = true
        else:
            xr_interface.set_play_area_mode(XRInterface.XR_PLAY_AREA_ROOMSCALE)
            xr_interface.environment_blend_mode = XRInterface.XR_ENV_BLEND_MODE_OPAQUE
            world_environment.environment.background_mode = Environment.BG_SKY
            get_viewport().transparent_bg = false

        # Light Estimation
        if OS.has_feature("androidxr"):
            var light_estimation = Engine.get_singleton("OpenXRAndroidLightEstimationExtension")
            if p_enabled and light_estimation.is_light_estimation_supported():
                light_estimation.start_light_estimation()
            elif light_estimation.is_light_estimation_started():
                light_estimation.stop_light_estimation()
                directional_light.transform = directional_light_orig_transform

##### Key points about the code

- When disabling light estimation, the original direction of the `DirectionalLight3D` must be restored manually.
- For a full example of a project using passthrough and Light Estimation, check out [Expedition to Blobotopia](https://gitlab.com/snopek-games/expedition-to-blobotopia) on GitLab.