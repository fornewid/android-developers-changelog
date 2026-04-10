---
title: https://developer.android.com/games/playgames/input-sdk-migration-unity-2
url: https://developer.android.com/games/playgames/input-sdk-migration-unity-2
source: md.txt
---

This guide explains how to upgrade your game from the 1.0 to the 1.1 Input SDK for Unity. [Click here](https://developer.android.com/games/playgames/input-sdk-migration-2)
for Java and Kotlin instructions.

## Release Notes

Google Play Games on PC supports remapping of keyboard controls based
on the key bindings your game provides using the Input SDK.

Users access this feature by opening
[the overlay](https://developer.android.com/games/playgames/input-sdk-start#the-overlay), selecting *controls*,
and then clicking on the action they wish to remap.

Google Play Games on PC maps every user-remapped input onto your game's default
input. This way your game doesn't have to be aware of the player's remapping. If
you need to know the new input for an in-game action, such as displaying the
keyboard controls in your game, you may optionally register a callback to be
notified for remapping events.

Google Play Games on PC stores user's remapped controls locally to persist
across gaming sessions. Since these settings is stored locally, they does not
influence the mobile experience and are deleted upon uninstallation of Google Play Games on PC. Settings do not persist across multiple PC devices.

You don't need to upgrade the Input SDK to enable key remapping in
your game, but remapping will be disabled for your game if an
[unsupported configuration](https://developer.android.com/games/playgames/input-sdk-migration-unity-2#remapping-exceptions) is detected.

If you want to control the input remapping experience or the remapping feature
is disabled for your game, follow these steps:

- Upgrade to Input SDK `1.1.1-beta`.
- Update any keybindings to avoid the [unsupported configurations](https://developer.android.com/games/playgames/input-sdk-migration-unity-2#remapping-exceptions).
- [Update](https://developer.android.com/games/playgames/input-sdk-migration-unity-2#update-input-map) your `InputMap` to set the remapping feature *enabled*.

If you want to opt-out of the remapping feature for your game while still
displaying the read-only version of your key bindings, follow these steps:

- Upgrade to Input SDK `1.1.1-beta`.
- Update your `InputMap` to set the remapping feature *disabled*.

You can upgrade your version of the Input SDK to
`1.1.1-beta` to take advantage of advanced remapping features
in Google Play Games on PC by using `InputContexts` to define controls for
different scenes of your game, add callbacks to listen for remapping events,
define a set of reserved keys that the user cannot remap to and disable the
remapping feature per `InputAction`, `InputGroup` or `InputMap`.

When upgrading consider the following exceptions:

### Unsupported configurations

Input remapping is disabled if the following conditions aren't met:

- An `InputAction` that utilizes multiples keys must be composed of a modifier
  and non-modifier key. For example, Shift + A is valid but A + B, Ctrl + Alt, and Shift + A + Tab is invalid.

- Two or more `InputAction` or `InputGroup` objects cannot share the same
  unique ID.

### Introducing InputContext

An `InputContext` allows a game to use the same key for different actions in
your game without conflicts. This way, if a game uses space for jumping
during gameplay and for confirming a menu selection, players are able to
individually remap space to enter in menus and
space to up arrow during gameplay.

The following sequence diagram shows how the `setInputContext()` API works at
runtime:

![Diagram showing the flow of the Input SDK when remapping keys.](https://developer.android.com/static/images/games/playgames/input-flow.png)

## Upgrade

Games using previous implementations of the Input SDK still support
basic remapping, unless they use an
[unsupported configuration](https://developer.android.com/games/playgames/input-sdk-migration-unity-2#remapping-exceptions). If your game is using an
older version of the Input SDK, consider reading the
[upgrade guide from 0.0.4 to 1.0.0-beta](https://developer.android.com/games/playgames/input-sdk-migration-unity).

Upgrade to 1.1.1-beta enables new features, including:

- Triggering context changes.
- Receiving notifications of key mapping events
- Disabling remapping per Action, Group, Context, or Map.

### Installation

The Unity plugin v1.1.1-beta is available for your use. You
need to delete any previous versions of the Input SDK installed in your game and
upgrade to the current version.

To add the Input SDK v1.1.1-beta to your game, see
[Adding the SDK](https://developer.android.com/games/playgames/input-sdk-start#adding-the-sdk).

### Define static fields

For version 1.1.1-beta it is a good practice to define your
`InputActions`, `InputGroups`, `InputContexts` and `InputMap` as static fields
of your `InputMappingProvider` class, as these fields will be accessible from
other parts of your application:

    #if PLAY_GAMES_PC
    using Java.Lang;
    using Java.Util;
    using Google.Android.Libraries.Play.Games.Inputmapping;
    using Google.Android.Libraries.Play.Games.Inputmapping.Datamodel;

    public class InputSDKMappingProvider : InputMappingProviderCallbackHelper
    {
        public static readonly string INPUT_MAP_VERSION = "1.0.0";

        private static readonly InputAction driveInputAction =
                InputAction.Create(...);
        private static readonly InputGroup roadInputGroup = InputGroup.Create(...);
        public static readonly InputContext roadControlsContext =
                InputContext.Create(...);
        public static readonly InputMap inputMap = InputMap.Create(...);

        public override InputMap OnProvideInputMap()
        {
            return inputMap;
        }
    }
    #endif

### Update your InputActions

> [!NOTE]
> **Note:** Consider the [best practices](https://developer.android.com/games/playgames/input-sdk-start#input-sdk-best-practices) for keyboard and mouse controls in Android games when you design an `InputAction` and be careful to avoid implementing [unsupported configurations](https://developer.android.com/games/playgames/input-sdk-migration-unity-2#remapping-exceptions).

The `InputAction.create()` method of Input SDK `1.0.0-beta` is
deprecated. An `InputAction` has a version identifier and can be marked as
remappable or not. An `InputAction` defined using the Input SDK
`1.0.0-beta` `create()` method is remappable by default and lacks versioning
information:

#### InputAction in Input SDK 1.0.0-beta

    var driveAction = PlayInputAction.Create(
        "Drive",
        (long)InputEventIds.DRIVE,
        PlayInputControls.Create(
            new[] { AndroidKeyCode.KEYCODE_SPACE },
            new List<PlayMouseAction>()
        )
    );

#### InputAction in Input SDK 1.1.1-beta

    private static readonly InputAction driveInputAction = InputAction.Create(
        "Drive",
        (long)InputEventIds.DRIVE,
        InputControls.Create(
            new[] { new Integer(AndroidKeyCode.KEYCODE_SPACE) }.ToJavaList(),
            new ArrayList<Integer>()),
        InputEnums.REMAP_OPTION_ENABLED
    );

#### InputAction in Input SDK 1.1.1-beta (with version string)

    private static readonly InputAction driveInputAction = InputAction.Create(
        "Drive",
        InputControls.Create(
            new[] { new Integer(AndroidKeyCode.KEYCODE_SPACE) }.ToJavaList(),
            new ArrayList<Integer>()),
        InputIdentifier.Create(
            INPUT_MAP_VERSION, (long)InputEventIds.DRIVE),
        InputEnums.REMAP_OPTION_ENABLED
    );

For more information about versioning your key bindings, see
[Tracking key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids).

### Update your InputGroups

In Input SDK `1.1.1-beta` you need to uniquely
identify each `InputGroup`. Each `InputAction` belongs to an `InputGroup` -- a
collection of related actions. This improves navigation and discoverability of
the controls during gameplay. Just as an `InputAction` must have a *unique*
identifier among all the actions in a single `InputContext`, an `InputGroup`
must have a unique ID across the existing groups.

For the examples in this section, a game has two `InputContext` objects
representing the main menu and gameplay. Appropriate IDs are tracked for each
`InputGroup` in these contexts using the following enumeration:

    public enum InputGroupsIds
    {
        // Main menu scene
        BASIC_NAVIGATION, // WASD, Enter, Backspace
        MENU_ACTIONS, // C: chat, Space: quick game, S: store
        // Gameplay scene
        BASIC_MOVEMENT, // WASD, space: jump, Shift: run
        MOUSE_ACTIONS, // Left click: shoot, Right click: aim
        EMOJIS, // Emojis with keys 1,2,3,4 and 5
        GAME_ACTIONS, // M: map, P: pause, R: reload
    }

Like `InputAction`, the `InputGroup.create()` method of the Input SDK
`1.0.0-beta` has been deprecated. You must update your `InputGroup` in your game
with a version identifier and boolean indicating whether the `InputAction`
objects in your groups are remappable. Groups created with the deprecated Input SDK `1.0.0-beta` `create()` method are remappable, have the ID 0,
and the version ID is an empty string (`""`):

#### InputGroup in Input SDK 1.0.0-beta

    var gameInputGroup = PlayInputGroup.Create(
        "Road controls",
        new List<PlayInputAction>
        {
            driveAction,
            turboAction,
            openGarageAction,
            openPgsAction,
            openStoreAction
        }
    );

#### InputGroup in Input SDK 1.1.1-beta

    private static readonly InputGroup roadInputGroup = InputGroup.Create(
        "Road controls",
        new[]
        {
            driveInputAction,
            turboInputAction,
            openGarageInputAction,
            openPgsInputAction,
            openStoreInputAction,
        }.ToJavaList(),
        (long)InputGroupsIds.ROAD_CONTROLS,
        // All input actions of this group will be remappable unless specified
        // the contrary by the individual input actions.
        InputEnums.REMAP_OPTION_ENABLED
    );

#### InputGroup in Input SDK 1.1.1-beta (with version string)

    private static readonly InputGroup roadInputGroup = InputGroup.Create(
        "Road controls",
        new[]
        {
            driveInputAction,
            turboInputAction,
            openGarageInputAction,
            openPgsInputAction,
            openStoreInputAction,
        }.ToJavaList(),
        InputIdentifier.Create(
            INPUT_MAP_VERSION, (long)InputGroupsIds.ROAD_CONTROLS),
        // All input actions of this group will be remappable unless specified
        // the contrary by the individual input actions.
        InputEnums.REMAP_OPTION_ENABLED
    );

For more information about versioning your key bindings, see
[Tracking key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids).

### Update your InputMap

`InputMap.create()` method of Input SDK `1.0.0-beta` has been
deprecated. Update your `InputMap` to assign a version identifier, opt out
completely from the remapping feature or assign a list of reserved keys for your
game that you don't want to be used for remapping by the user. Every `InputMap`
defined using the Input SDK `1.0.0-beta` `create()` method is
remappable by default, is identified with the ID `0`, and doesn't have any
reserved keys.

#### InputMap in Input SDK 1.0.0-beta

    var gameInputMap = PlayInputMap.Create(
        new List<PlayInputGroup>
        {
            gameInputGroup,
            menuInputGroup
        },
        PlayMouseSettings.Create(false, false)
    );

#### InputMap in Input SDK 1.1.1-beta


    public static readonly string INPUT_MAP_VERSION = "1.0.0";
    public static readonly long INPUT_MAP_ID = 0;

    public static readonly InputMap inputMap = InputMap.Create(
        new[] { roadInputGroup, menuInputGroup }.ToJavaList(),
        MouseSettings.Create(false, false),
        InputIdentifier.Create(INPUT_MAP_VERSION, INPUT_MAP_ID),
        // Use ESC as reserved key
        InputEnums.REMAP_OPTION_ENABLED,
        new[]
        {
            InputControls.Create(new[]
            {
                new Integer(AndroidKeyCode.KEYCODE_ESCAPE)
            }.ToJavaList(),
            new ArrayList<Integer>())
        }.ToJavaList()
    );

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