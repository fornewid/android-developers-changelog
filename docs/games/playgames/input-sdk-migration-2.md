---
title: https://developer.android.com/games/playgames/input-sdk-migration-2
url: https://developer.android.com/games/playgames/input-sdk-migration-2
source: md.txt
---

<br />

This guide explains how to upgrade your game from the 1.0.0-beta
Input SDK for Java and Kotlin to 1.1.1-beta. See the
[Unity upgrade guide](https://developer.android.com/games/playgames/input-sdk-migration-unity-2) for Unity
specific instructions.

## Release Notes

Google Play Games on PC supports remapping of keyboard controls based
on the key bindings your game provides using the Input SDK.

Users access this feature by opening
[the overlay](https://developer.android.com/games/playgames/input-sdk-start#the-overlay), selecting controls,
and then clicking on the action they wish to remap.

Google Play Games on PC maps every user-remapped input onto your game's default
input. This way your game doesn't have to be aware of the player's remapping. If
you need to know the new input for an in-game action, such as displaying the
keyboard controls in your game, you may optionally register a callback to be
notified for remapping events.

Google Play Games on PC stores each user's remapped controls locally so they
are persistent across gaming sessions. Since this is stored locally, it does not
influence the mobile experience and is deleted upon uninstallation of Google Play Games on PC. Control settings are not persisted across multiple
PC devices.

You don't need to upgrade the Input SDK to enable key remapping in
your game, but remapping can be disabled for your game if an
[unsupported configuration](https://developer.android.com/games/playgames/input-sdk-migration-2#remapping-exceptions) is detected.

If you want to control the input remapping experience, or if the remapping
feature is disabled for your game, perform the following steps to resolve:

- Upgrade to Input SDK `1.1.1-beta`.
- Update any keybindings to avoid the [unsupported configurations](https://developer.android.com/games/playgames/input-sdk-migration-2#remapping-exceptions).
- Update your `InputMap` to set the remapping feature *enabled*.

If you want to opt-out of the remapping feature for your game while still
displaying the read-only version of your key bindings, follow these steps:

- Upgrade to Input SDK `1.1.1-beta`.
- Update your `InputMap` to set the remapping feature to *disabled*.

You can upgrade your version of the Input SDK to
`1.1.1-beta` to take advantage of advanced remapping features
in Google Play Games on PC by using `InputContexts` to define controls for
different scenes of your game, add callbacks to listen for remapping events,
define a set of reserved keys that the user cannot remap to, and deactivate the
remapping feature per `InputAction`, `InputGroup` or `InputMap`.

Consider the following exceptions while upgrading to the new SDK version:

### Unsupported configurations

Input remapping is disabled if the following conditions are not met:

- An `InputAction` utilizing multiple keys must be composed of a modifier
  and non-modifier key. For example, Shift + A is valid but A + B, Ctrl + Alt, and Shift + A + Tab are not.

- Two or more `InputAction` or `InputGroup` objects cannot share the same
  unique ID.

## Upgrade

Input SDK 1.1.1-beta is backward compatible with Input SDK
1.0.0-beta. Games using previous implementations of the Input SDK
still support basic remapping, unless they use an
[unsupported configuration](https://developer.android.com/games/playgames/input-sdk-migration-2#remapping-exceptions). If your game is using an
earlier version of the Input SDK, consider reading the
[upgrade guide from 0.0.4 to 1.0.0-beta](https://developer.android.com/games/playgames/input-sdk-migration).

Upgrading to 1.1.1-beta enables new features including:

- [Triggering scene control changes](https://developer.android.com/games/playgames/input-sdk-starg#input-contexts).
- [Receiving notifications of key mapping events](https://developer.android.com/games/playgames/input-sdk-start#remapping-restrictions).
- Disabling remapping per Action, Group, Context, or Map.

### Upgrade dependency

If you are using Gradle to import the Input SDK, upgrade to the newest version:

    // build.gradle
    dependencies {
       ...
       implementation 'com.google.android.libraries.play.games:inputmapping:1.1.1-beta'
       ...
    }

### Define static fields

For version `1.1.1-beta` it is a good practice to define your
`InputAction`, `InputGroup`, `InputContext` and `InputMap` objects as static
fields of your `InputMappingProvider` class since these fields are accessible
from other parts of your application:

<br />

### Kotlin

<br />

    class InputSDKProvider : InputMappingProvider {
        override fun onProvideInputMap(): InputMap { return gameInputMap }

        companion object {
            const val INPUTMAP_VERSION = "1.0.0"

            private val moveUpInputAction = InputAction.create(...)
            private val movementInputGroup = InputGroup.create(...)
            val menuContext = InputContext.create(...)
            val gameInputMap = InputMap.create(...)
        }
    }

<br />

### Java

<br />

    public class MyInputMappingProvider implements InputMappingProvider {
        private static final String INPUTMAP_VERSION = "1.0.0";

        private static final InputAction moveUpInputAction =
            InputAction.create(...);
        private static final InputGroup movementInputGroup = InputGroup.create(...);
        public static final InputContext menuContext = InputContext.create(...);
        public static final InputMap gameInputMap = InputMap.create(...);

        @Override
        public InputMap onProvideInputMap() {
            return gameInputMap;
        }
    }

<br />

<br />

### Update your InputActions

> [!NOTE]
> **Note:** Consider the [best practices](https://developer.android.com/games/playgames/input-sdk-start#input-sdk-best-practices) for keyboard and mouse controls in Android games when you design an `InputAction` and be careful to avoid any of the [unsupported configurations](https://developer.android.com/games/playgames/input-sdk-migration-2#remapping-exceptions).

The `InputAction.create()` method of Input SDK `1.0.0-beta` is
deprecated. An `InputAction` now has a version identifier and can be marked as
remappable or not. An `InputAction` defined using the Input SDK
`1.0.0-beta` `create()` method is remappable by default and lacks versioning
information:

#### InputAction in Input SDK 1.0.0-beta

<br />

### Kotlin

<br />

    val jumpInputAction = InputAction.create(
        "Jump",
        InputEventIds.JUMP.id,
        InputControls.create(
            listOf(KeyEvent.KEYCODE_SPACE),
            emptyList()
        )
    )

<br />

### Java

<br />

    InputAction moveUpInputAction = InputAction.create(
        "Move Up",
        InputEventIds.MOVE_UP.ordinal(),
        InputControls.create(
            Collections.singletonList(KeyEvent.KEYCODE_W),
            Collections.emptyList()
        )
    );

<br />

<br />

#### InputAction in Input SDK 1.1.1-beta

<br />

### Kotlin

<br />

    companion object {
      private val moveUpInputAction = InputAction.create(
        "Move Up",
        InputActionsIds.DRIVE.ordinal.toLong(),
        InputControls.create(listOf(KeyEvent.KEYCODE_W), emptyList()),
        InputEnums.REMAP_OPTION_ENABLED) // This action is remappable
    }

<br />

### Java

<br />

    private static final InputAction moveUpInputAction = InputAction.create(
        "Move Up",
        InputEventIds.MOVE_UP.ordinal(),
        InputControls.create(
                Collections.singletonList(KeyEvent.KEYCODE_W),
                Collections.emptyList()),
        InputEnums.REMAP_OPTION_ENABLED // this action is remappable
    );

<br />

<br />

#### InputAction in Input SDK 1.1.1-beta (with version string)

<br />

### Kotlin

<br />

    private val enterMenuInputAction = InputAction.create(
        "Enter menu",
        InputControls.create(listOf(KeyEvent.KEYCODE_ENTER), emptyList()),
        InputIdentifier.create(
        INPUTMAP_VERSION, InputActionsIds.ENTER_MENU.ordinal.toLong()),
        InputEnums.REMAP_OPTION_ENABLED
    )

<br />

### Java

<br />

    private static final InputAction moveUpInputAction = InputAction.create(
        "Move Up",
        InputControls.create(
                Collections.singletonList(KeyEvent.KEYCODE_W),
                Collections.emptyList()),
        InputIdentifier.create(
                INPUTMAP_VERSION,
                InputEventIds.MOVE_UP.ordinal()),
        InputEnums.REMAP_OPTION_ENABLED // this action is remappable
    );

<br />

<br />

For more information about versioning your key bindings, see
[Tracking key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids).

### Update your InputGroups

In Input SDK `1.1.1-beta` you need to uniquely
identify each `InputGroup`. Each `InputAction` belongs to an `InputGroup` -- a
collection of related actions. This improves navigation and discoverability of
the controls during gameplay. In the same way that `InputAction` must have a
*unique* identifier among all the actions in a single `InputContext`, an
`InputGroup` must have a unique ID across the existing groups.

For the examples in this section, a game has two `InputContext` objects
representing the main menu and gameplay. Appropriate IDs are tracked for each
`InputGroup` in these contexts using the following enumeration:

<br />

### Kotlin

<br />

    enum class InputGroupsIds {
        // Main menu scene
        BASIC_NAVIGATION, // WASD, Enter, Backspace
        MENU_ACTIONS, // C: chat, Space: quick game, S: store
        // Gameplay scene
        BASIC_MOVEMENT, // WASD, space: jump, Shift: run
        MOUSE_ACTIONS, // Left click: shoot, Right click: aim
        EMOJIS, // Emojis with keys 1,2,3,4 and 5
        GAME_ACTIONS, // M: map, P: pause, R: reload
    }

<br />

### Java

<br />

    public enum InputGroupsIds {
        // Main menu scene
        BASIC_NAVIGATION, // WASD, Enter, Backspace
        MENU_ACTIONS, // C: chat, Space: quick game, S: store
        // Gameplay scene
        BASIC_MOVEMENT, // WASD, space: jump, Shift: run
        MOUSE_ACTIONS, // Left click: shoot, Right click: aim
        EMOJIS, // Emojis with keys 1,2,3,4 and 5
        GAME_ACTIONS, // M: map, P: pause, R: reload
    }

<br />

<br />

Like `InputAction`, the `InputGroup.create()` method of the Input SDK
`1.0.0-beta` has been deprecated. You must update your `InputGroup` in your game
with a version identifier and boolean indicating whether the `InputAction`
objects in your groups are remappable. Groups created with the deprecated Input SDK `1.0.0-beta` `create()` method are remappable, have the ID 0,
and the version ID is an empty string (`""`):

#### InputGroup in Input SDK 1.0.0-beta

<br />

### Kotlin

<br />

    val movementInputGroup = InputGroup.create(
        "Basic Movement",
        listOf(
            moveUpInputAction,
            moveLeftInputAction,
            moveDownInputAction,
            moveRightInputAction,
            jumpInputAction,
            runInputAction)
    )

<br />

### Java

<br />

    InputGroup movementInputGroup = InputGroup.create(
        "Basic movement",
        Arrays.asList(
            moveUpInputAction,
            moveLeftInputAction,
            moveDownInputAction,
            moveRightInputAction,
            jumpInputAction,
            runInputAction
        )
    );

<br />

<br />

#### InputGroup in Input SDK 1.1.1-beta

<br />

### Kotlin

<br />

    companion object {
        private val movementInputGroup = InputGroup.create(
            "Basic movement",
            listOf(
                moveUpInputAction,
                moveLeftInputAction,
                moveDownInputAction,
                moveRightInputAction,
                jumpInputAction,
                runInputAction),
            InputGroupsIds.BASIC_MOVEMENT.ordinal.toLong(),
            // All the actions in this groups can't be remapped
            InputEnums.REMAP_OPTION_DISABLED
        )
    }

<br />

### Java

<br />

    private static final InputGroup movementInputGroup = InputGroup.create(
        "Basic movement",
        Arrays.asList(
                moveUpInputAction,
                moveLeftInputAction,
                moveDownInputAction,
                moveRightInputAction,
                jumpInputAction,
                runInputAction
        ),
        InputGroupsIds.BASIC_MOVEMENT.ordinal(),
        // All the actions in this groups can't be remapped
        InputEnums.REMAP_OPTION_DISABLED
    );

<br />

<br />

#### InputGroup in Input SDK 1.1.1-beta (with version string)

<br />

### Kotlin

<br />

    companion object {
        private val movementInputGroup  = InputGroup.create(
            "Basic movement",
            listOf(
                moveUpInputAction,
                moveLeftInputAction,
                moveDownInputAction,
                moveRightInputAction,
                jumpInputAction,
                runInputAction),
            InputIdentifier.create(
                INPUTMAP_VERSION, InputGroupsIds.BASIC_MOVEMENT.ordinal.toLong()),
            // All the actions in this groups can't be remapped
            InputEnums.REMAP_OPTION_DISABLED
        )
    }

<br />

### Java

<br />

    private static final InputGroup movementInputGroup = InputGroup.create(
        "Basic movement",
        Arrays.asList(
                moveUpInputAction,
                moveLeftInputAction,
                moveDownInputAction,
                moveRightInputAction,
                jumpInputAction,
                runInputAction
        ),
        InputIdentifier.create(
                INPUTMAP_VERSION,
                InputGroupsIds.BASIC_MOVEMENT.ordinal()),
        // All the actions in this groups can't be remapped
        InputEnums.REMAP_OPTION_DISABLED
    );

<br />

<br />

For more information about versioning your key bindings, see
[Tracking key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids).

### Update your InputMap

`InputMap.create()` method of Input SDK `1.0.0-beta` is
deprecated. Update your `InputMap` to assign a version identifier, opt out
completely from the remapping feature or assign a list of reserved keys for your
game that you don't want to be used for remapping by the user. Every `InputMap`
defined using the Input SDK `1.0.0-beta` `create()` method is
remappable by default, is identified with the ID `0`, and doesn't have any
reserved keys.

#### InputMap in Input SDK 1.0.0-beta

<br />

### Kotlin

<br />

    val gameInputMap = InputMap.create(
        listOf(movementInputGroup, mouseMovementInputGroup),
        MouseSettings.create(true, false)
    )

<br />

### Java

<br />

    InputMap gameInputMap = InputMap.create(
        Arrays.asList(movementInputGroup, mouseMovementInputGroup),
        MouseSettings.create(true, false)
    );

<br />

<br />

#### InputMap in Input SDK 1.1.1-beta

<br />

### Kotlin

<br />

    companion object {

      const val INPUTMAP_VERSION = "1.0.0"
      const val INPUT_MAP_ID = 0

      val gameInputMap = InputMap.create(
        listOf(movementInputGroup, mouseMovementInputGroup),
        MouseSettings.create(true, false),
        InputIdentifier.create(INPUTMAP_VERSION, INPUT_MAP_ID.toLong()),
        InputEnums.REMAP_OPTION_ENABLED,
        // Use ESCAPE as reserved key
        listof(InputControls.create(listOf(KeyEvent.KEYCODE_ESCAPE), emptyList()))
      )
    }

<br />

### Java

<br />


    public static final String INPUT_MAP_VERSION = "1.0.0-beta";
    public static final long INPUT_MAP_ID = 0;

    public static final InputMap gameInputMap = InputMap.create(
            Arrays.asList(movementInputGroup, mouseMovementInputGroup),
            MouseSettings.create(true, false),
            InputIdentifier.create(INPUTMAP_VERSION, INPUT_MAP_ID),
            InputEnums.REMAP_OPTION_ENABLED,
            // Use ESC key as reserved key
            Arrays.asList(
                    InputControls.create(
                            Collections.singletonList(KeyEvent.KEYCODE_ESCAPE),
                            Collections.emptyList()
                    )
            )
    );

<br />

<br />

## What's next

Continue your upgrade to 1.1.1-beta by
[Assigning different controls for different scenes](https://developer.android.com/games/playgames/input-sdk-start#input-contexts)
using `InputContexts` or updating the UI of your game by
[Getting notified on remapping events](https://developer.android.com/games/playgames/input-sdk-start#remapping-listener) using
`InputRemappingListeners`.

When updating your key-bindings take a look at the
[Best practices for designing your key bindings](https://developer.android.com/games/playgames/input-sdk-start#input-sdk-best-practices)
and consider the [restrictions](https://developer.android.com/games/playgames/input-sdk-start#remapping-restrictions) and
[limitations](https://developer.android.com/games/playgames/input-sdk-start#remapping-limitations) of the remapping feature.