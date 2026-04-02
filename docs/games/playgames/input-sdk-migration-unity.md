---
title: https://developer.android.com/games/playgames/input-sdk-migration-unity
url: https://developer.android.com/games/playgames/input-sdk-migration-unity
source: md.txt
---

This guide describes how to migrate your Unity game to use the latest
Input SDK. The *1.0.0-beta* SDK has substantial improvements over the
previous *0.0.4* preview. You should migrate from the earlier previews as soon
as possible. The *0.0.4* SDK will continue to function through March 2023.

## Update references

Classes received the `Play` prefix to avoid naming collisions with Unity.
Whenever you see the an error message similar to:
> error CS0246: The type or namespace name 'InputMappingProvider' could not be
> found (are you missing a using directive or an assembly reference?)

you must add the `Play` prefix to the class name. For example,
`InputMappingProvider` becomes `PlayInputMappingProvider`.

## Update each InputAction

`InputAction` is now constructed with a call to `PlayInputAction.Create` as opposed
to creating a new `struct` with named fields.

Locate any code that calls `new InputAction`:

    var driveAction = new InputAction
    {
        ActionLabel = "Drive",
        UniqueId = (int)InputEventIds.DRIVE,
        InputControls = new InputControls
        {
            AndroidKeycodes = new[] { AndroidKeyCode.KEYCODE_SPACE }
        }
    };

And replace it with a call to `PlayInputAction.Create`:

    var driveAction = PlayInputAction.Create(
        "Drive",
        (int)InputEventIds.DRIVE,
        PlayInputControls.Create(
            new[] { AndroidKeyCode.KEYCODE_SPACE },
            null
        )
    );

## Update each InputGroup

Like `InputAction`, `InputGroup` now has an `PlayInputGroup.Create` call rather
than requiring that you manually fill out a `struct`.

This means that you should locate any calls to `new InputGroup`:

    var gameInputGroup = new InputGroup
    {
        GroupLabel = "Game controls",
        InputActions = new List<InputAction>
        {
            driveAction,
            turboAction,
            openGarageAction,
            openStoreAction
        }
    };

And replace it to a call to `PlayInputGroup.Create`:

    var gameInputGroup = PlayInputGroup.Create(
        "Game controls",
        new List<PlayInputAction>
        {
            driveAction,
            turboAction,
            openGarageAction,
            openStoreAction
        }
    );

## Update the InputMap

`InputMap` uses `PlayInputMap.Create` as well instead of constructing a new
struct.

Locate any calls to `new InputMap`:

    return new InputMap
    {
        InputGroups = new List<InputGroup>
        {
            gameInputGroup,
            menuInputGroup
        },
        MouseSettings = new MouseSettings
        {
            AllowMouseSensitivityAdjustment = false,
            InvertMouseMovement = false
        }
    };

And replace it with a call to `PlayInputMap.Create`:

    return PlayInputMap.Create(
        new List<PlayInputGroup>
        {
            gameInputGroup,
            menuInputGroup
        },
        PlayMouseSettings.Create(false, false)
    );

## Rename the PlayInputMappingClient methods

For `PlayInputMappingClient`, `RegisterInputMappingProvider` has been renamed to
`SetInputMappingProvider`.

So locate any calls to `RegisterInputMappingProvider`:

    Input.GetInputMappingClient().RegisterInputMappingProvider(_inputMappingProvider);

And replace them with a call to `SetInputMappingProvider`:

    PlayInputMappingClient inputMappingClient =
        Google.Play.InputMapping.PlayInput.GetInputMappingClient();
    inputMappingClient.SetInputMappingProvider(_inputMapProvider);

`UnregisterInputMappingProvider` has also been renamed to
`ClearInputMappingProvider` and no longer requires your previously registered
`InputMappingProvider` as a parameter.

Locate any calls to `UnregisterInputMappingProvider`:

    Input.GetInputMappingClient().UnregisterInputMappingProvider(_inputMapProvider);

And replace them with `ClearInputMappingProvider`:

    PlayInput.GetInputMappingClient().ClearInputMappingProvider();