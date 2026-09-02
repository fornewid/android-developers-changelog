---
title: https://developer.android.com/games/playgames/input-sdk-start
url: https://developer.android.com/games/playgames/input-sdk-start
source: md.txt
---

> [!NOTE]
> **Note:** If you're looking to upgrade from an earlier version, see the [migration guides](https://developer.android.com/games/playgames/input-sdk-migration-guides).

This document describes how to set up and display the Input SDK in
games that support Google Play Games on PC. The tasks include adding the SDK
to your game and generating an input map, which contains the
game‑actions‑to‑user‑input assignments.

## Before you get started

Before you add the Input SDK to your game, you must support
[keyboard and mouse](https://developer.android.com/games/playgames/input) input **using your game engine's
input system**.

The Input SDK provides information to Google Play Games on PC about
what controls your game uses, so they can be displayed to the user. It can also
optionally allow keyboard remapping for users.

Each control is an `InputAction` (e.g. "J" for "Jump") and you organize your
`InputActions` into `InputGroups`. An `InputGroup` might represent a different
mode in your game, such as "Driving" or "Walking" or "Main Menu". You can also
use `InputContexts` to indicate which groups are active at different points of
the game.

You can enable keyboard remapping to be handled for you automatically, but if
you prefer to provide your own control remapping interface then you can disable
Input SDK remapping.

The following sequence diagram describes how the API of the Input SDK works:

![Sequence diagram of a game implementation that calls Input SDK API
and its interaction with the Android
device.](https://developer.android.com/static/images/games/playgames/input-flow.png)

When your game implements the Input SDK your controls are displayed
in the Google Play Games on PC overlay.

### The Google Play Games on PC overlay

The Google Play Games on PC overlay ("the overlay") displays the controls
defined by your game. Users access the overlay at any time by
pressing **Shift + Tab**.

![The Google Play Games on PC overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-1.png)

### Best practices for designing key bindings

When designing your key bindings consider the following best practices:

- Group your `InputActions` into logically related `InputGroups` to improve navigation and discoverability of the controls during gameplay.
- Assign each `InputGroup` to at most one `InputContext`. A fine granuled `InputMap` results in a better experience for navigating your controls in the overlay.
- Create an `InputContext` for each different scene type of your game. Typically, you can use a single `InputContext` for all your "menu-like" scenes. Use different `InputContexts` for any minigames in your game or for alternative controls for a single scene.
- If two actions are designed to use the same key under the same `InputContext`, utilize the label string such as "Interact / Fire".
- If two keys are designed to bind to the same `InputAction` then use 2 different `InputActions` that perform the same action in your game. You may utilize the same label string for both `InputActions`, but its ID must be different.
- If a modifier key is applied to a set of keys, consider having a single `InputAction` with the modifier key instead of multiple `InputActions` that combine the modifier key (example: use **Shift** and **W, A, S, D** instead **Shift + W, Shift + A, Shift + S, Shift + D**).
- Input remapping gets disabled automatically when the user writes into text fields. Follow best practices for implementing Android text fields to ensure that Android can detect text fields in your game and prevent remapped keys from interfering with them. If your game has to use non-conventional text fields you can use `setInputContext()` with an `InputContext` containing an empty list of `InputGroups` to disable remapping manually.
- If your game supports remapping, consider updating your key bindings a sensitive operation that can conflict with the user saved versions. Avoid changing IDs of existing controls when possible.

## The remapping feature

Google Play Games on PC supports keyboard control remapping based on the key
bindings your game provides using the Input SDK. This is optional and
can be entirely disabled. For example, you may wish to provide your own keyboard
remapping interface. To disable remapping for your game you just have to specify
the remapping option disabled for your `InputMap` (see
[Build an InputMap](https://developer.android.com/games/playgames/input-sdk-start#input-map) for more information).

To access this feature users need to open the overlay and then click the action
they want to remap. After every remapping event Google Play Games on PC maps
each user-remapped control to the default controls your game is expecting to
receive, so your game doesn't need to be aware of the player's remapping. You
can optionally update the assets used for displaying the keyboard controls in
your game by adding a callback for remapping events.

![Attempt to remap the key](https://developer.android.com/static/images/games/playgames/input-sdk-2.png)

Google Play Games on PC stores remapped controls locally for each user,
enabling control persistence across gaming sessions. This information is stored
on disk only for the PC platform and does not impact the mobile experience.
Control data is deleted upon the user uninstalling or re-installing Google Play Games on PC. This data is not persistent across multiple PC devices.

To support the remapping feature in your game, avoid the following restrictions:

### Restrictions of remapping

Remapping features can be disabled in your game if the key bindings contain any
of the following cases:

- Multi-key `InputActions` that are not composed by a modifier key + a non-modifier key. For example, **Shift + A** is valid but **A + B** , **Ctrl + Alt** or **Shift + A + Tab** is not.
- The `InputMap` contains `InputActions`, `InputGroups` or `InputContexts` with repeated unique IDs.

> [!NOTE]
> **Note:** Failure to avoid these exceptions may cause delays in your deployment process and result in the remapping feature being disabled for your game.

> [!NOTE]
> **Note:** If your game implements Input SDK v1.0.0-beta and has the remapping feature disabled, migrate to the [latest Input SDK version](https://developer.android.com/games/playgames/(#remapping-listener)) and fix any error you find. If you are using the latest version and still find the remapping feature disabled for your game, contact your Google Play Games on PC advocate.

### Limitations of remapping

When designing your key bindings for remapping consider the following
limitations:

- Remapping to key combinations is not supported. For example, users can't remap **Shift + A** to **Ctrl + B** or **A** to **Shift + A**.
- Remapping is not supported for `InputActions` with mouse buttons. For example, **Shift + Right-click** cannot be remapped.

### Test key remapping on Google Play Games on PC Emulator

You can enable the remapping feature in Google Play Games on PC Emulator at any time
by issuing the following adb command:

    adb shell dumpsys input_mapping_service --set RemappingFlagValue true

The overlay change as in the following image:

![The overlay with key remapping enabled.](https://developer.android.com/static/images/games/playgames/input-sdk-3.png)

## Add the SDK

Install the Input SDK according to your development platform.

### Java and Kotlin

Get the Input SDK for Java or Kotlin by adding a dependency to your
module-level `build.gradle` file:

    dependencies {
      implementation 'com.google.android.libraries.play.games:inputmapping:1.1.1-beta'
      ...
    }

### Unity

The Input SDK is a standard Unity package with several dependencies.

Installing the package with all dependencies is required. There are several ways
to install the packages.

#### Install the `.unitypackage`

[Download the Input SDK unitypackage file](https://developers.google.com/unity/archive#input_sdk)
with all its dependencies. You can install the `.unitypackage` by selecting
**Assets \> Import package \> Custom Package** and locating the file you downloaded.

#### Install using UPM

Alternatively you may install the package using the
[Unity Package Manager](https://docs.unity3d.com/Manual/upm-ui-local.html) by
downloading the `.tgz` and installing its dependencies:

- [com.google.external-dependency-manager-1.2.172](https://developers.google.com/unity/archive#external_dependency_manager_for_unity)
- [com.google.librarywrapper.java-0.2.0](https://github.com/google/library-wrapper-unity-common)
- [com.google.librarywrapper.openjdk8-0.2.0](https://github.com/google/library-wrapper-unity-openjdk8)
- [com.google.android.libraries.play.games.inputmapping-1.1.1-beta](https://github.com/playgameservices/play-games-input-sdk-unity) (or selecting [the tgz from this archive](https://developers.google.com/unity/archive#input_sdk))

#### Install using OpenUPM

You may install the package using
[OpenUPM](https://openupm.com/packages/com.google.android.libraries.play.games.inputmapping/).

    $ openupm add com.google.android.libraries.play.games.inputmapping

### Sample games

For examples of how to integrate with the Input SDK, see
[AGDK Tunnel](https://github.com/android/games-samples/tree/main/agdk/agdktunnel)
for Kotlin or Java games and
[Trivial Kart](https://github.com/android/games-samples/tree/main/trivialkart/trivialkart-unity)
for Unity games.

## Generate your key bindings

> [!NOTE]
> **Note:** you can [detect when your game is running on Google Play Games on PC](https://developer.android.com/games/playgames/pc-compatibility#detect-hpe), although the Input SDK is intelligent enough to detect when it's running on mobile. Alternatively you can define your own **PLAY_GAMES_PC** [preprocessor directive](https://docs.unity3d.com/Manual/PlatformDependentCompilation.html) in Unity.

Register your key bindings by building an `InputMap` and returning it with an
`InputMappingProvider`. The following example outlines an
`InputMappingProvider`:

### Kotlin

```kotlin
class InputSDKProvider : InputMappingProvider {
  override fun onProvideInputMap(): InputMap {
    TODO("Not yet implemented")
  }
}
```

### Java

```java
public class InputSDKProvider implements InputMappingProvider {
    private static final String INPUTMAP_VERSION = "1.0.0";

    @Override
    @NonNull
    public InputMap onProvideInputMap() {
        // TODO: return an InputMap
    }
}
```

### C#

```c#
#if PLAY_GAMES_PC
using Java.Lang;
using Java.Util;
using Google.Android.Libraries.Play.Games.Inputmapping;
using Google.Android.Libraries.Play.Games.Inputmapping.Datamodel;

public class InputSDKProvider : InputMappingProviderCallbackHelper
{
    public static readonly string INPUT_MAP_VERSION = "1.0.0";

    public override InputMap OnProvideInputMap()
    {
        // TODO: return an InputMap
    }
}
#endif
```

### Define your input actions

The `InputAction` class is used to map a key or key combination to a game
action. `InputActions` must have unique IDs across all the `InputActions`.

If you are supporting remapping you can define what `InputActions` can be
remapped. If your game does not support remapping you should set the remapping
option disabled for all your `InputActions`, but the Input SDK is
intelligent enough to turn off remapping if you don't support it in your
`InputMap`.

This example maps the space key to the *Drive* action.

### Kotlin

```kotlin
companion object {
  private val driveInputAction = InputAction.create(
    "Drive",
    InputActionsIds.DRIVE.ordinal.toLong(),
    InputControls.create(listOf(KeyEvent.KEYCODE_SPACE), emptyList()),
    InputEnums.REMAP_OPTION_ENABLED)
}
```

### Java

```java
private static final InputAction driveInputAction = InputAction.create(
    "Drive",
    InputEventIds.DRIVE.ordinal(),
    InputControls.create(
            Collections.singletonList(KeyEvent.KEYCODE_SPACE),
            Collections.emptyList()),
    InputEnums.REMAP_OPTION_ENABLED
);
```

### C#

```c#
private static readonly InputAction driveInputAction = InputAction.Create(
    "Drive",
    (long)InputEventIds.DRIVE,
    InputControls.Create(
        new[] { new Integer(AndroidKeyCode.KEYCODE_SPACE) }.ToJavaList(),
        new ArrayList<Integer>()),
    InputEnums.REMAP_OPTION_ENABLED
);
```

![Single key InputAction displayed in the overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-4.png)

Actions can represent mouse inputs as well. This example sets **Left-click** to
the *Move* action:

### Kotlin

```kotlin
companion object {
  private val mouseInputAction = InputAction.create(
    "Move",
    InputActionsIds.MOUSE_MOVEMENT.ordinal.toLong(),
    InputControls.create(emptyList(), listOf(InputControls.MOUSE_LEFT_CLICK)),
    InputEnums.REMAP_OPTION_DISABLED)
}
```

### Java

```java
private static final InputAction mouseInputAction = InputAction.create(
    "Move",
    InputActionsIds.MOUSE_MOVEMENT.ordinal(),
    InputControls.create(
            Collections.emptyList(),
            Collections.singletonList(InputControls.MOUSE_LEFT_CLICK)
    ),
    InputEnums.REMAP_OPTION_DISABLED
);
```

### C#

```c#
private static readonly InputAction mouseInputAction = InputAction.Create(
    "Move",
    (long)InputEventIds.MOUSE_MOVEMENT,
    InputControls.Create(
        new ArrayList<Integer>(),
        new[] { new Integer((int)PlayMouseAction.MouseLeftClick) }.ToJavaList()
    ),
    InputEnums.REMAP_OPTION_DISABLED
);
```

![Mouse InputAction displayed in the overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-5.png)

Key combinations are specified by passing multiple key codes to your
`InputAction`. In this example space + shift is mapped to
the *Turbo* action, which works even when Space is mapped to *Drive*.

### Kotlin

```kotlin
companion object {
  private val turboInputAction = InputAction.create(
    "Turbo",
    InputActionsIds.TURBO.ordinal.toLong(),
    InputControls.create(
      listOf(KeyEvent.KEYCODE_SHIFT_LEFT, KeyEvent.KEYCODE_SPACE),
      emptyList()),
    InputEnums.REMAP_OPTION_ENABLED)
}
```

### Java

```java
private static final InputAction turboInputAction = InputAction.create(
    "Turbo",
    InputActionsIds.TURBO.ordinal(),
    InputControls.create(
            Arrays.asList(KeyEvent.KEYCODE_SHIFT_LEFT, KeyEvent.KEYCODE_SPACE),
            Collections.emptyList()
    ),
    InputEnums.REMAP_OPTION_ENABLED
);
```

### C#

```c#
private static readonly InputAction turboInputAction = InputAction.Create(
    "Turbo",
    (long)InputEventIds.TURBO,
    InputControls.Create(
        new[]
        {
            new Integer(AndroidKeyCode.KEYCODE_SHIFT_LEFT),
            new Integer(AndroidKeyCode.KEYCODE_SPACE)
        }.ToJavaList(),
        new ArrayList<Integer>()),
    InputEnums.REMAP_OPTION_ENABLED
);
```

![Multi-key InputAction displayed in the overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-6.png)

> [!NOTE]
> **Note:** if supporting remapping, users can remap multi-key actions to single keys.

The Input SDK lets you mix mouse and key buttons together for a
single action. This example indicates that Shift and **Right-click**
pressed together adds a waypoint in this sample game:

### Kotlin

```kotlin
companion object {
  private val addWaypointInputAction = InputAction.create(
    "Add waypoint",
    InputActionsIds.ADD_WAYPOINT.ordinal.toLong(),
    InputControls.create(
      listOf(KeyEvent.KeyEvent.KEYCODE_TAB),
      listOf(InputControls.MOUSE_RIGHT_CLICK)),
    InputEnums.REMAP_OPTION_DISABLED)
}
```

### Java

```java
private static final InputAction addWaypointInputAction = InputAction.create(
    "Add waypoint",
    InputActionsIds.ADD_WAYPOINT.ordinal(),
    InputControls.create(
            Collections.singletonList(KeyEvent.KEYCODE_TAB),
            Collections.singletonList(InputControls.MOUSE_RIGHT_CLICK)
    ),
    InputEnums.REMAP_OPTION_DISABLED
);
```

### C#

```c#
private static readonly InputAction addWaypointInputAction = InputAction.Create(
    "Add waypoint",
    (long)InputEventIds.ADD_WAYPOINT,
    InputControls.Create(
        new[] { new Integer(AndroidKeyCode.KEYCODE_SPACE) }.ToJavaList(),
        new[] { new Integer((int)PlayMouseAction.MouseRightClick) }.ToJavaList()
    ),
    InputEnums.REMAP_OPTION_DISABLED
);
```

![Combination of key + mouse InputAction displayed in the overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-7.png)

InputAction has the following fields:

- `ActionLabel`: the string displayed in the UI to represent this action. Localization is not done automatically, so perform any localization up front.
- `InputControls`: defines the input controls that this action uses. The controls map to consistent glyphs in the overlay.
- `InputActionId`: `InputIdentifier` object that stores number ID and version of the `InputAction` (see [Tracking Key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids) for more information).
- `InputRemappingOption`: one of `InputEnums.REMAP_OPTION_ENABLED` or `InputEnums.REMAP_OPTION_DISABLED`. Defines if the action is enabled to remap. If your game does not support remapping you may skip this field or simply set it disabled.
- `RemappedInputControls`: read-only `InputControls` object used to read the remapped key set by the user on remapping events (used for [getting notified on remapping events](https://developer.android.com/games/playgames/input-sdk-start#remapping-listener)).

`InputControls` represents the inputs associated with an action and contains the
following fields::

- `AndroidKeycodes`: is a list of integers representing keyboard inputs associated with an action. These are defined in the [KeyEvent](https://developer.android.com/reference/android/view/KeyEvent) class or the AndroidKeycode class for Unity.
- `MouseActions`: is a list of `MouseAction` values representing mouse inputs associated with this action.

### Define your input groups

`InputActions` are grouped with logically-related actions using `InputGroups` to
improve navigation and controls discoverability in the overlay. Each
`InputGroup` ID requires to be unique across all `InputGroups` in your game.

By organizing your input actions into groups you make it easier for a player to
find the correct key binding for their current context.

If you are supporting remapping you can define what `InputGroups` can be
remapped. If your game does not support remapping you should set the remapping
option disabled for all your `InputGroups`, but the Input SDK is
intelligent enough to turn off remapping if you don't support it in your
`InputMap`.

### Kotlin

```kotlin
companion object {
  private val menuInputGroup = InputGroup.create(
    "Menu keys",
    listOf(
      navigateUpInputAction,
      navigateLeftInputAction,
      navigateDownInputAction,
      navigateRightInputAction,
      openMenuInputAction,
      returnMenuInputAction),
    InputGroupsIds.MENU_ACTION_KEYS.ordinal.toLong(),
    InputEnums.REMAP_OPTION_ENABLED
  )
}
```

### Java

```java
private static final InputGroup menuInputGroup = InputGroup.create(
    "Menu keys",
    Arrays.asList(
           navigateUpInputAction,
           navigateLeftInputAction,
           navigateDownInputAction,
           navigateRightInputAction,
           openMenuInputAction,
           returnMenuInputAction),
    InputGroupsIds.MENU_ACTION_KEYS.ordinal(),
    REMAP_OPTION_ENABLED
);
```

### C#

```c#
private static readonly InputGroup menuInputGroup = InputGroup.Create(
    "Menu keys",
    new[]
    {
        navigateUpInputAction,
        navigateLeftInputAction,
        navigateDownInputAction,
        navigateRightInputAction,
        openMenuInputAction,
        returnMenuInputAction,
    }.ToJavaList(),
    (long)InputGroupsIds.MENU_ACTION_KEYS,
    InputEnums.REMAP_OPTION_ENABLED
);
```

The following example displays the **Road controls** and the **Menu controls**
input groups in the overlay:

![The overlay displaying an InputMap that contains the Road controls and the
Menu controls input groups.](https://developer.android.com/static/images/games/playgames/input-sdk-8.png)

`InputGroup` has the following fields:

- `GroupLabel`: a string to be displayed in the overlay that can be used to logically group a set of actions. This string is not automatically localized.
- `InputActions`: a list of `InputAction` objects you define in the previous step. All of these actions are visually displayed under the group heading.
- `InputGroupId`: `InputIdentifier` object that stores the number ID and version of the `InputGroup`. See [Tracking Key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids) for more information.
- `InputRemappingOption`: one of `InputEnums.REMAP_OPTION_ENABLED` or `InputEnums.REMAP_OPTION_DISABLED`. If disabled, all the `InputAction` objects belonging to this group will have remapping disabled even if they specify its remapping option enabled. If enabled, all the actions belonging to this group can be remappable unless specified disabled by the individual actions.

> [!NOTE]
> **Note:** each `InputAction` must belong to at most one `InputGroup`.

### Define your input contexts

`InputContexts` allows your game to use a different set of keyboard controls for
different scenes of your game. For example:

- You may specify different sets of inputs for navigating menus versus moving in the game.
- You may specify different sets of inputs depending on the mode of locomotion in your game, such as driving versus walking.
- You may specify different sets of inputs based on the current state of your game, such as navigating an overworld versus playing an individual level.

When using `InputContexts`, the overlay shows first the groups of the context
in use. To enable this behavior, call `setInputContext()` to set the
context whenever your game enters a different scene. The following image
demonstrates this behavior: in the "driving" scene, the **Road controls**
actions are shown at the top of the overlay. When opening the "store" menu, the
"Menu controls" actions are displayed at the top of the overlay.

![InputContexts sorting groups in the overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-9.png)

These overlay updates are achieved by setting a different `InputContext` at
different points in your game. To do this:

1. Group your `InputActions` with logically-related actions using `InputGroups`
2. Assign these `InputGroups` to an `InputContext` for the different parts of your game

`InputGroups` that belong to the same`InputContext`cannot have conflicting
`InputActions` where the same key is used. It is a good practice to assign each
`InputGroup` to a single `InputContext`.

The following sample code demonstrates `InputContext` logic:

### Kotlin

```kotlin
companion object {
  val menuSceneInputContext = InputContext.create(
    "Menu",
    InputIdentifier.create(
      INPUTMAP_VERSION,
      InputContextIds.MENU_SCENE.ordinal.toLong()),
    listOf(basicMenuNavigationInputGroup, menuActionsInputGroup))

  val gameSceneInputContext = InputContext.create(
    "Game",
    InputIdentifier.create(
      INPUTMAP_VERSION,
      InputContextIds.GAME_SCENE.ordinal.toLong()),
    listOf(
      movementInputGroup,
      mouseActionsInputGroup,
      emojisInputGroup,
      gameActionsInputGroup))
}
```

### Java

```java
public static final InputContext menuSceneInputContext = InputContext.create(
        "Menu",
        InputIdentifier.create(
                INPUTMAP_VERSION,
                InputContextIds.MENU_SCENE.ordinal()),
        Arrays.asList(
                basicMenuNavigationInputGroup,
                menuActionsInputGroup
        )
);

public static final InputContext gameSceneInputContext = InputContext.create(
        "Game",
        InputIdentifier.create(
                INPUTMAP_VERSION,
                InputContextIds.GAME_SCENE.ordinal()),
        Arrays.asList(
                movementInputGroup,
                mouseActionsInputGroup,
                emojisInputGroup,
                gameActionsInputGroup
        )
);
```

### C#

```c#
public static readonly InputContext menuSceneInputContext = InputContext.Create(
    "Menu",
    InputIdentifier.Create(
        INPUT_MAP_VERSION,
        (long)InputContextsIds.MENU_SCENE),
    new[]
    {
        basicMenuNavigationInputGroup,
        menuActionsInputGroup
    }.ToJavaList()
);

public static readonly InputContext gameSceneInputContext = InputContext.Create(
    "Game",
    InputIdentifier.Create(
        INPUT_MAP_VERSION,
        (long)InputContextsIds.GAME_SCENE),
    new[]
    {
        movementInputGroup,
        mouseActionsInputGroup,
        emojisInputGroup,
        gameActionsInputGroup
    }.ToJavaList()
);
```

`InputContext` has the following fields:

- `LocalizedContextLabel`: a string describing the groups that belong to the context.
- `InputContextId`: `InputIdentifier` object that stores number ID and version of the `InputContext` (see [Tracking Key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids) for more information).
- `ActiveGroups`: a list of `InputGroups` to be used and displayed at the top of the overlay when this context is active.

### Build an input map

An `InputMap` is a collection of all the `InputGroup` objects available in a
game, and therefore all of the `InputAction` objects a player can expect to
perform.

When reporting your key bindings, you build an `InputMap` with all the
`InputGroups` used in your game.

If your game does not support remapping, set the remapping option disabled and
the reserved keys empty.

The following example builds an `InputMap` used to report a collection of
`InputGroups`.

### Kotlin

```kotlin
companion object {
  val gameInputMap = InputMap.create(
    listOf(
      basicMenuNavigationInputGroup,
      menuActionKeysInputGroup,
      movementInputGroup,
      mouseMovementInputGroup,
      pauseMenuInputGroup),
    MouseSettings.create(true, false),
    InputIdentifier.create(INPUTMAP_VERSION, INPUT_MAP_ID.toLong()),
    InputEnums.REMAP_OPTION_ENABLED,
    // Use ESCAPE as reserved remapping key
    listof(InputControls.create(listOf(KeyEvent.KEYCODE_ESCAPE), emptyList()))
  )
}
```

### Java

```java
public static final InputMap gameInputMap = InputMap.create(
        Arrays.asList(
                basicMenuNavigationInputGroup,
                menuActionKeysInputGroup,
                movementInputGroup,
                mouseMovementInputGroup,
                pauseMenuInputGroup),
        MouseSettings.create(true, false),
        InputIdentifier.create(INPUTMAP_VERSION, INPUT_MAP_ID),
        REMAP_OPTION_ENABLED,
        // Use ESCAPE as reserved remapping key
        Arrays.asList(
                InputControls.create(
                        Collections.singletonList(KeyEvent.KEYCODE_ESCAPE),
                        Collections.emptyList()
                )
        )
);
```

### C#

```c#
public static readonly InputMap gameInputMap = InputMap.Create(
    new[]
    {
        basicMenuNavigationInputGroup,
        menuActionKeysInputGroup,
        movementInputGroup,
        mouseMovementInputGroup,
        pauseMenuInputGroup,
    }.ToJavaList(),
    MouseSettings.Create(true, false),
    InputIdentifier.Create(INPUT_MAP_VERSION, INPUT_MAP_ID),
    InputEnums.REMAP_OPTION_ENABLED,
    // Use ESCAPE as reserved remapping key
    new[]
    {
        InputControls.Create(
            New[] {
            new Integer(AndroidKeyCode.KEYCODE_ESCAPE)
        }.ToJavaList(),
        new ArrayList<Integer>())
    }.ToJavaList()
);
```

`InputMap` has the following fields:

- `InputGroups`: the InputGroups reported by your game. The groups are displayed in order in the overlay, unless specified the current groups in use calling `setInputContext()`.
- `MouseSettings`: The `MouseSettings` object indicate that mouse sensitivity can be adjusted and that the mouse is inverted on the y axis.
- `InputMapId`: `InputIdentifier` object that stores number ID and version of the `InputMap` (see [Tracking Key IDs](https://developer.android.com/games/playgames/input-sdk-start#tracking-key-ids) for more information).
- `InputRemappingOption`: one of `InputEnums.REMAP_OPTION_ENABLED` or `InputEnums.REMAP_OPTION_DISABLED`. Defines if the remapping feature is enabled.
- `ReservedControls`: a list of `InputControls` that users won't be allowed to remap to.

### Track key IDs

`InputAction`, `InputGroup`, `InputContext` and `InputMap` objects contain an
`InputIdentifier` object that stores a unique number ID and a string version ID.
Tracking the string version of your objects is optional but recommended to track
the versions of your `InputMap`. If string version is not provided then the
string is empty. A string version is required for `InputMap` objects.

The following example assigns a string version to `InputActions` or
`InputGroups`:

### Kotlin

```kotlin
class InputSDKProviderKotlin : InputMappingProvider {
  companion object {
    const val INPUTMAP_VERSION = "1.0.0"
    private val enterMenuInputAction = InputAction.create(
      "Enter menu",
      InputControls.create(listOf(KeyEvent.KEYCODE_ENTER), emptyList()),
      InputIdentifier.create(
        INPUTMAP_VERSION, InputActionsIds.ENTER_MENU.ordinal.toLong()),
      InputEnums.REMAP_OPTION_ENABLED
    )

    private val movementInputGroup  = InputGroup.create(
      "Basic movement",
      listOf(
        moveUpInputAction,
        moveLeftInputAction,
        moveDownInputAction,
        mouseGameInputAction),
      InputIdentifier.create(
        INPUTMAP_VERSION, InputGroupsIds.BASIC_MOVEMENT.ordinal.toLong()),
      InputEnums.REMAP_OPTION_ENABLED)
  }
}
```

### Java

```java
public class InputSDKProvider implements InputMappingProvider {
    public static final String INPUTMAP_VERSION = "1.0.0";

    private static final InputAction enterMenuInputAction = InputAction.create(
            "Enter menu",
            InputControls.create(
                    Collections.singletonList(KeyEvent.KEYCODE_ENTER),
                    Collections.emptyList()),
            InputIdentifier.create(
                    INPUTMAP_VERSION, InputActionsIds.ENTER_MENU.ordinal()),
            InputEnums.REMAP_OPTION_ENABLED
    );

    private static final InputGroup movementInputGroup = InputGroup.create(
            "Basic movement",
            Arrays.asList(
                    moveUpInputAction,
                    moveLeftInputAction,
                    moveDownInputAction,
                    moveRightInputAction,
                    mouseGameInputAction
            ),
            InputIdentifier.create(
                    INPUTMAP_VERSION, InputGroupsIds.BASIC_MOVEMENT.ordinal()),
            InputEnums.REMAP_OPTION_ENABLED
    );
}
```

### C#

```c#
#if PLAY_GAMES_PC

using Java.Lang;
using Java.Util;
using Google.Android.Libraries.Play.Games.Inputmapping;
using Google.Android.Libraries.Play.Games.Inputmapping.Datamodel;

public class InputSDKMappingProvider : InputMappingProviderCallbackHelper
{
    public static readonly string INPUT_MAP_VERSION = "1.0.0";

    private static readonly InputAction enterMenuInputAction =
        InputAction.Create(
            "Enter menu",
            InputControls.Create(
                new[] { new Integer(AndroidKeyCode.KEYCODE_SPACE)}.ToJavaList(),
                new ArrayList<Integer>()),
            InputIdentifier.Create(
                INPUT_MAP_VERSION,
                (long)InputEventIds.ENTER_MENU),
            InputEnums.REMAP_OPTION_ENABLED
        );

    private static readonly InputGroup movementInputGroup = InputGroup.Create(
        "Basic movement",
        new[]
        {
            moveUpInputAction,
            moveLeftInputAction,
            moveDownInputAction,
            moveRightInputAction,
            mouseGameInputAction
        }.ToJavaList(),
        InputIdentifier.Create(
            INPUT_MAP_VERSION,
            (long)InputGroupsIds.BASIC_MOVEMENT),
        InputEnums.REMAP_OPTION_ENABLED
    );
}
#endif
```

`InputAction` objects number IDs must be unique across all the `InputActions` in
your `InputMap`. Similarly, `InputGroup` object IDs must be unique across all
`InputGroups` in an `InputMap`. The following sample demonstrates how to use an
`enum` to track your object's unique IDs:

### Kotlin

```kotlin
enum class InputActionsIds {
    NAVIGATE_UP,
    NAVIGATE_DOWN,
    ENTER_MENU,
    EXIT_MENU,
    // ...
    JUMP,
    RUN,
    EMOJI_1,
    EMOJI_2,
    // ...
}

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

enum class InputContextIds {
    MENU_SCENE, // Basic menu navigation, menu actions
    GAME_SCENE, // Basic movement, mouse actions, emojis, game actions
}

const val INPUT_MAP_ID = 0
```

### Java

```java
public enum InputActionsIds {
    NAVIGATE_UP,
    NAVIGATE_DOWN,
    ENTER_MENU,
    EXIT_MENU,
    // ...
    JUMP,
    RUN,
    EMOJI_1,
    EMOJI_2,
    // ...
}

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

public enum InputContextIds {
    MENU_SCENE, // Basic navigation, menu actions
    GAME_SCENE, // Basic movement, mouse actions, emojis, game actions
}

public static final long INPUT_MAP_ID = 0;
```

### C#

```c#
public enum InputActionsIds
{
    NAVIGATE_UP,
    NAVIGATE_DOWN,
    ENTER_MENU,
    EXIT_MENU,
    // ...
    JUMP,
    RUN,
    EMOJI_1,
    EMOJI_2,
    // ...
}

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

public enum InputContextIds
{
    MENU_SCENE, // Basic navigation, menu actions
    GAME_SCENE, // Basic movement, mouse actions, emojis, game actions
}

public static readonly long INPUT_MAP_ID = 0;
```

`InputIdentifier` has the following fields:

- `UniqueId`: a unique number id set to clearly identify a given set of input data uniquely.
- `VersionString`: a human readable version string set to identify a version of input data between 2 versions of input data changes.

### Get notified on remapping events (Optional)

Receive notifications on remap events to be informed of the keys being used in
your game. This allows your game to update the assets shown on the game screen
used to display the action controls.

The following image shows an example of this behavior where after remapping the
keys G, P and S to J, X
and T respectively, the UI elements of the game get updated to
display the keys set by the user.

![UI reacting to remapping events using the InputRemappingListener callback.](https://developer.android.com/static/images/games/playgames/input-sdk-10.png)

This functionality is achieved by registering an `InputRemappingListener`
callback. To implement this feautre, start by registering an
`InputRemappingListener` instance:

### Kotlin

```kotlin
class InputSDKRemappingListener : InputRemappingListener {
  override fun onInputMapChanged(inputMap: InputMap) {
    Log.i(TAG, "Received update on input map changed.")
    if (inputMap.inputRemappingOption() == InputEnums.REMAP_OPTION_DISABLED) {
      return
    }
    for (inputGroup in inputMap.inputGroups()) {
      if (inputGroup.inputRemappingOption() == InputEnums.REMAP_OPTION_DISABLED) {
        continue
      }
      for (inputAction in inputGroup.inputActions()) {
        if (inputAction.inputRemappingOption() != InputEnums.REMAP_OPTION_DISABLED) {
          // Found InputAction remapped by user
          processRemappedAction(inputAction)
        }
      }
    }
  }

  private fun processRemappedAction(remappedInputAction: InputAction) {
    // Get remapped action info
    val remappedControls = remappedInputAction.remappedInputControls()
    val remappedKeyCodes = remappedControls.keycodes()
    val mouseActions = remappedControls.mouseActions()
    val version = remappedInputAction.inputActionId().versionString()
    val remappedActionId = remappedInputAction.inputActionId().uniqueId()
    val currentInputAction: Optional<InputAction>
    currentInputAction = if (version == null || version.isEmpty()
      || version == InputSDKProvider.INPUTMAP_VERSION
    ) {
      getCurrentVersionInputAction(remappedActionId)
    } else {
      Log.i(TAG,
            "Detected version of user-saved input action defers from current version")
      getCurrentVersionInputActionFromPreviousVersion(
        remappedActionId, version)
    }
    if (!currentInputAction.isPresent) {
      Log.e(TAG, String.format(
        "can't find remapped input action with id %d and version %s",
        remappedActionId, if (version == null || version.isEmpty()) "UNKNOWN" else version))
      return
    }
    val originalControls = currentInputAction.get().inputControls()
    val originalKeyCodes = originalControls.keycodes()
    Log.i(TAG, String.format(
      "Found input action with id %d remapped from key %s to key %s",
      remappedActionId,
      keyCodesToString(originalKeyCodes),
      keyCodesToString(remappedKeyCodes)))

    // TODO: make display changes to match controls used by the user
  }

  private fun getCurrentVersionInputAction(inputActionId: Long): Optional<InputAction> {
    for (inputGroup in InputSDKProvider.gameInputMap.inputGroups()) {
      for (inputAction in inputGroup.inputActions()) {
        if (inputAction.inputActionId().uniqueId() == inputActionId) {
          return Optional.of(inputAction)
        }
      }
    }
    return Optional.empty()
  }

  private fun getCurrentVersionInputActionFromPreviousVersion(
    inputActionId: Long, previousVersion: String
  ): Optional<InputAction7gt; {
    // TODO: add logic to this method considering the diff between the current and previous
    //  InputMap.
    return Optional.empty()
  }

  private fun keyCodesToString(keyCodes: List<Int>): String {
    val builder = StringBuilder()
    for (keyCode in keyCodes) {
      if (!builder.toString().isEmpty()) {
        builder.append(" + ")
      }
      builder.append(keyCode)
    }
    return String.format("(%s)", builder)
  }

  companion object {
    private const val TAG = "InputSDKRemappingListener"
  }
}
```

### Java

```java
public class InputSDKRemappingListener implements InputRemappingListener {

    private static final String TAG = "InputSDKRemappingListener";

    @Override
    public void onInputMapChanged(InputMap inputMap) {
        Log.i(TAG, "Received update on input map changed.");
        if (inputMap.inputRemappingOption() ==
                InputEnums.REMAP_OPTION_DISABLED) {
            return;
        }
        for (InputGroup inputGroup : inputMap.inputGroups()) {
            if (inputGroup.inputRemappingOption() ==
                    InputEnums.REMAP_OPTION_DISABLED) {
                continue;
            }
            for (InputAction inputAction : inputGroup.inputActions()) {
                if (inputAction.inputRemappingOption() !=
                        InputEnums.REMAP_OPTION_DISABLED) {
                    // Found InputAction remapped by user
                    processRemappedAction(inputAction);
                }
            }
        }
    }

    private void processRemappedAction(InputAction remappedInputAction) {
        // Get remapped action info
        InputControls remappedControls =
            remappedInputAction.remappedInputControls();
        List<Integer> remappedKeyCodes = remappedControls.keycodes();
        List<Integer> mouseActions = remappedControls.mouseActions();
        String version = remappedInputAction.inputActionId().versionString();
        long remappedActionId = remappedInputAction.inputActionId().uniqueId();
        Optional<InputAction> currentInputAction;
        if (version == null || version.isEmpty()
                    || version.equals(InputSDKProvider.INPUTMAP_VERSION)) {
            currentInputAction = getCurrentVersionInputAction(remappedActionId);
        } else {
            Log.i(TAG, "Detected version of user-saved input action defers " +
                    "from current version");
            currentInputAction =
                    getCurrentVersionInputActionFromPreviousVersion(
                            remappedActionId, version);
        }
        if (!currentInputAction.isPresent()) {
            Log.e(TAG, String.format(
                    "input action with id %d and version %s not found",
                    remappedActionId, version == null || version.isEmpty() ?
                            "UNKNOWN" : version));
            return;
        }
        InputControls originalControls =
                currentInputAction.get().inputControls();
        List<Integer> originalKeyCodes = originalControls.keycodes();

        Log.i(TAG, String.format(
                "Found input action with id %d remapped from key %s to key %s",
                remappedActionId,
                keyCodesToString(originalKeyCodes),
                keyCodesToString(remappedKeyCodes)));

        // TODO: make display changes to match controls used by the user
    }

    private Optional<InputAction> getCurrentVersionInputAction(
            long inputActionId) {
        for (InputGroup inputGroup :
                    InputSDKProvider.gameInputMap.inputGroups()) {
            for (InputAction inputAction : inputGroup.inputActions()) {
                if (inputAction.inputActionId().uniqueId() == inputActionId) {
                    return Optional.of(inputAction);
                }
            }
        }
        return Optional.empty();
    }

    private Optional<InputAction>
            getCurrentVersionInputActionFromPreviousVersion(
                    long inputActionId, String previousVersion) {
        // TODO: add logic to this method considering the diff between your
        // current and previous InputMap.
        return Optional.empty();
    }

    private String keyCodesToString(List<Integer> keyCodes) {
        StringBuilder builder = new StringBuilder();
        for (Integer keyCode : keyCodes) {
            if (!builder.toString().isEmpty()) {
                builder.append(" + ");
            }
            builder.append(keyCode);
        }
        return String.format("(%s)", builder);
    }
}
```

### C#

```c#
#if PLAY_GAMES_PC

using System.Text;
using Java.Lang;
using Java.Util;
using Google.Android.Libraries.Play.Games.Inputmapping;
using Google.Android.Libraries.Play.Games.Inputmapping.Datamodel;
using UnityEngine;

public class InputSDKRemappingListener : InputRemappingListenerCallbackHelper
{
    public override void OnInputMapChanged(InputMap inputMap)
    {
        Debug.Log("Received update on remapped controls.");
        if (inputMap.InputRemappingOption() == InputEnums.REMAP_OPTION_DISABLED)
        {
            return;
        }
        List<InputGroup> inputGroups = inputMap.InputGroups();
        for (int i = 0; i < inputGroups.Size(); i ++)
        {
            InputGroup inputGroup = inputGroups.Get(i);
            if (inputGroup.InputRemappingOption()
                    == InputEnums.REMAP_OPTION_DISABLED)
            {
                continue;
            }
            List<InputAction> inputActions = inputGroup.InputActions();
            for (int j = 0; j < inputActions.Size(); j ++)
            {
                InputAction inputAction = inputActions.Get(j);
                if (inputAction.InputRemappingOption()
                        != InputEnums.REMAP_OPTION_DISABLED)
                {
                    // Found action remapped by user
                    ProcessRemappedAction(inputAction);
                }
            }
        }
    }

    private void ProcessRemappedAction(InputAction remappedInputAction)
    {
        InputControls remappedInputControls =
                remappedInputAction.RemappedInputControls();
        List<Integer> remappedKeycodes = remappedInputControls.Keycodes();
        List<Integer> mouseActions = remappedInputControls.MouseActions();
        string version = remappedInputAction.InputActionId().VersionString();
        long remappedActionId = remappedInputAction.InputActionId().UniqueId();
        InputAction currentInputAction;
        if (string.IsNullOrEmpty(version)
                || string.Equals(
                version, InputSDKMappingProvider.INPUT_MAP_VERSION))
        {
            currentInputAction = GetCurrentVersionInputAction(remappedActionId);
        }
        else
        {
            Debug.Log("Detected version of used-saved input action defers" +
                " from current version");
            currentInputAction =
                GetCurrentVersionInputActionFromPreviousVersion(
                    remappedActionId, version);
        }
        if (currentInputAction == null)
        {
            Debug.LogError(string.Format(
                "Input Action with id {0} and version {1} not found",
                remappedActionId,
                string.IsNullOrEmpty(version) ? "UNKNOWN" : version));
            return;
        }
        InputControls originalControls = currentInputAction.InputControls();
        List<Integer> originalKeycodes = originalControls.Keycodes();

        Debug.Log(string.Format(
            "Found Input Action with id {0} remapped from key {1} to key {2}",
            remappedActionId,
            KeyCodesToString(originalKeycodes),
            KeyCodesToString(remappedKeycodes)));
        // TODO: update HUD according to the controls of the user
    }

    private InputAction GetCurrentVersionInputAction(
            long inputActionId)
    {
        List<InputGroup> inputGroups =
            InputSDKMappingProvider.gameInputMap.InputGroups();
        for (int i = 0; i < inputGroups.Size(); i++)
        {
            InputGroup inputGroup = inputGroups.Get(i);
            List<InputAction> inputActions = inputGroup.InputActions();
            for (int j = 0; j < inputActions.Size(); j++)
            {
                InputAction inputAction = inputActions.Get(j);
                if (inputAction.InputActionId().UniqueId() == inputActionId)
                {
                    return inputAction;
                }
            }
        }
        return null;
    }

    private InputAction GetCurrentVersionInputActionFromPreviousVersion(
            long inputActionId, string version)
    {
        // TODO: add logic to this method considering the diff between your
        // current and previous InputMap.
        return null;
    }

    private string KeyCodesToString(List<Integer> keycodes)
    {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < keycodes.Size(); i ++)
        {
            Integer keycode = keycodes.Get(i);
            if (builder.Length > 0)
            {
                builder.Append(" + ");
            }
            builder.Append(keycode.IntValue());
        }
        return string.Format("({0})", builder.ToString());
    }
}
#endif
```

The `InputRemappingListener` is notified at launch time after loading the
user-saved remapped controls, and after every time the user remaps their keys.

> [!NOTE]
> **Note:** you can have at most one remapping listener registered in your application.

### Initialization

If you are using `InputContexts` set the context on each
transition to a new scene, including the first context used for your initial
scene. You need to set the `InputContext` after you have registered your
`InputMap`.

If you are using `InputRemappingListeners` to be notified on remapping events
register your `InputRemappingListener` before registering your
`InputMappingProvider`, otherwise your game can miss important events during
launch time.

The following sample demonstrates how to initialize the API:

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    if (isGooglePlayGamesOnPC()) {
        val inputMappingClient = Input.getInputMappingClient(this)
        // Register listener before registering the provider
        inputMappingClient.registerRemappingListener(InputSDKRemappingListener())
        inputMappingClient.setInputMappingProvider(
                InputSDKProvider())
        // Set the context after you have registered the provider.
        inputMappingClient.setInputContext(InputSDKProvider.menuSceneInputContext)
    }
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    if (isGooglePlayGamesOnPC()) {
        InputMappingClient inputMappingClient =
                Input.getInputMappingClient(this);
        // Register listener before registering the provider
        inputMappingClient.registerRemappingListener(
                new InputSDKRemappingListener());
        inputMappingClient.setInputMappingProvider(
                new InputSDKProvider());
        // Set the context after you have registered the provider
        inputMappingClient.setInputContext(InputSDKProvider.menuSceneInputContext);
    }
}
```

### C#

```c#
#if PLAY_GAMES_PC
using Google.Android.Libraries.Play.Games.Inputmapping;
using Google.Android.Libraries.Play.Games.InputMapping.ExternalType.Android.Content;
using Google.LibraryWrapper.Java;
#endif

public class GameManager : MonoBehaviour
{
#if PLAY_GAMES_PC
    private InputSDKMappingProvider _inputMapProvider =
        new InputSDKMappingProvider();
    private InputMappingClient _inputMappingClient;
#endif

    public void Awake()
    {
#if PLAY_GAMES_PC
        Context context = (Context)Utils.GetUnityActivity().GetRawObject();
        _inputMappingClient = Google.Android.Libraries.Play.Games.Inputmapping
            .Input.GetInputMappingClient(context);
        // Register listener before registering the provider.
        _inputMappingClient.RegisterRemappingListener(
            new InputSDKRemappingListener());
        _inputMappingClient.SetInputMappingProvider(_inputMapProvider);
        // Register context after you have registered the provider.
       _inputMappingClient.SetInputContext(
           InputSDKMappingProvider.menuSceneInputContext);
#endif
    }
}
```

### Clean up

Unregister your `InputMappingProvider` instance and any `InputRemappingListener`
instances when your game is closed, although the Input SDK is smart
enough to avoid leaking resources if you don't:

### Kotlin

```kotlin
override fun onDestroy() {
    if (isGooglePlayGamesOnPC()) {
        val inputMappingClient = Input.getInputMappingClient(this)
        inputMappingClient.clearInputMappingProvider()
        inputMappingClient.clearRemappingListener()
    }

    super.onDestroy()
}
```

### Java

```java
@Override
protected void onDestroy() {
    if (isGooglePlayGamesOnPC()) {
        InputMappingClient inputMappingClient =
                Input.getInputMappingClient(this);
        inputMappingClient.clearInputMappingProvider();
        inputMappingClient.clearRemappingListener();
    }

    super.onDestroy();
}
```

### C#

```c#
public class GameManager : MonoBehaviour
{
    private void OnDestroy()
    {
#if PLAY_GAMES_PC
        _inputMappingClient.ClearInputMappingProvider();
        _inputMappingClient.ClearRemappingListener();
#endif
    }
}
```

## Test

You can test your Input SDK implementation by manually opening
[the overlay](https://developer.android.com/games/playgames/input-sdk-start#the-overlay) to view the player experience, or via the adb shell
for automated testing and verification.

The Google Play Games on PC Emulator checks the correctness of your input map
against common errors. For scenarios like duplicate unique ids, using different
input maps or failing on the remapping rules (if remapping is enabled), the
overlay shows an error message as below:
![The Input SDK overlay.](https://developer.android.com/static/images/games/playgames/input-sdk-11.png)

Verify your Input SDK implementation using `adb` at the command line.
To get the current input map, use the following `adb shell` command (replace
`MY.PACKAGE.NAME` with the name of your game):

    adb shell dumpsys input_mapping_service --get MY.PACKAGE.NAME

You will see output similar to this if you successfully registered your
`InputMap`:

    Getting input map for com.example.inputsample...
    Successfully received the following inputmap:
    # com.google.android.libraries.play.games.InputMap@d73526e1
    input_groups {
      group_label: "Basic Movement"
      input_actions {
        action_label: "Jump"
        input_controls {
          keycodes: 51
          keycodes: 19
        }
        unique_id: 0
      }
      input_actions {
        action_label: "Left"
        input_controls {
          keycodes: 29
          keycodes: 21
        }
        unique_id: 1
      }
      input_actions {
        action_label: "Right"
        input_controls {
          keycodes: 32
          keycodes: 22
        }
        unique_id: 2
      }
      input_actions {
        action_label: "Use"
        input_controls {
          keycodes: 33
          keycodes: 66
          mouse_actions: MOUSE_LEFT_CLICK
          mouse_actions_value: 0
        }
        unique_id: 3
      }
    }
    input_groups {
      group_label: "Special Input"
      input_actions {
        action_label: "Jump"
        input_controls {
          keycodes: 51
          keycodes: 19
          keycodes: 62
          mouse_actions: MOUSE_LEFT_CLICK
          mouse_actions_value: 0
        }
        unique_id: 4
      }
      input_actions {
        action_label: "Duck"
        input_controls {
          keycodes: 47
          keycodes: 20
          keycodes: 113
          mouse_actions: MOUSE_RIGHT_CLICK
          mouse_actions_value: 1
        }
        unique_id: 5
      }
    }
    mouse_settings {
      allow_mouse_sensitivity_adjustment: true
      invert_mouse_movement: true
    }

## Localization

The Input SDK does not use Android's localization system. As a
result, you must provide localized strings when submitting an `InputMap`. You
may also use your game engine's localization system.

## Proguard

When using Proguard to minify your game, add the following rules to your
proguard configuration file to ensure the SDK doesn't get stripped from your
final package:

    -keep class com.google.android.libraries.play.hpe.** { *; }
    -keep class com.google.android.libraries.play.games.inputmapping.** { *; }

## What's next

After you integrate the Input SDK into your game, you can continue
with any remaining Google Play Games on PC requirements. For more information,
see [Get started with Google Play Games on PC](https://developer.android.com/games/playgames/start).