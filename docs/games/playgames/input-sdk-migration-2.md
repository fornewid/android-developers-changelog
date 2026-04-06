---
title: Upgrade Input SDK for Java and Kotlin to version 1.1  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/input-sdk-migration-2
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Upgrade Input SDK for Java and Kotlin to version 1.1 Stay organized with collections Save and categorize content based on your preferences.




This guide explains how to upgrade your game from the 1.0.0-beta
Input SDK for Java and Kotlin to 1.1.1-beta. See the
[Unity upgrade guide](/games/playgames/input-sdk-migration-unity-2) for Unity
specific instructions.

## Release Notes

Google Play Games on PC supports remapping of keyboard controls based
on the key bindings your game provides using the Input SDK.

Users access this feature by opening
[the overlay](/games/playgames/input-sdk-start#the-overlay), selecting controls,
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
[unsupported configuration](#remapping-exceptions) is detected.

If you want to control the input remapping experience, or if the remapping
feature is disabled for your game, perform the following steps to resolve:

* Upgrade to Input SDK `1.1.1-beta`.
* Update any keybindings to avoid the
  [unsupported configurations](#remapping-exceptions).
* Update your `InputMap` to set the remapping feature *enabled*.

If you want to opt-out of the remapping feature for your game while still
displaying the read-only version of your key bindings, follow these steps:

* Upgrade to Input SDK `1.1.1-beta`.
* Update your `InputMap` to set the remapping feature to *disabled*.

You can upgrade your version of the Input SDK to
`1.1.1-beta` to take advantage of advanced remapping features
in Google Play Games on PC by using `InputContexts` to define controls for
different scenes of your game, add callbacks to listen for remapping events,
define a set of reserved keys that the user cannot remap to, and deactivate the
remapping feature per `InputAction`, `InputGroup` or `InputMap`.

Consider the following exceptions while upgrading to the new SDK version:

### Unsupported configurations

Input remapping is disabled if the following conditions are not met:

* An `InputAction` utilizing multiple keys must be composed of a modifier
  and non-modifier key. For example, Shift + A is valid but A +
  B, Ctrl + Alt, and Shift + A + Tab are not.
* Two or more `InputAction` or `InputGroup` objects cannot share the same
  unique ID.

## Upgrade

Input SDK 1.1.1-beta is backward compatible with Input SDK
1.0.0-beta. Games using previous implementations of the Input SDK
still support basic remapping, unless they use an
[unsupported configuration](#remapping-exceptions). If your game is using an
earlier version of the Input SDK, consider reading the
[upgrade guide from 0.0.4 to 1.0.0-beta](/games/playgames/input-sdk-migration).

Upgrading to 1.1.1-beta enables new features including:

* [Triggering scene control changes](/games/playgames/input-sdk-starg#input-contexts).
* [Receiving notifications of key mapping events](/games/playgames/input-sdk-start#remapping-restrictions).
* Disabling remapping per Action, Group, Context, or Map.

### Upgrade dependency

If you are using Gradle to import the Input SDK, upgrade to the newest version:

```
// build.gradle
dependencies {
   ...
   implementation 'com.google.android.libraries.play.games:inputmapping:1.1.1-beta'
   ...
}
```

### Define static fields

For version `1.1.1-beta` it is a good practice to define your
`InputAction`, `InputGroup`, `InputContext` and `InputMap` objects as static
fields of your `InputMappingProvider` class since these fields are accessible
from other parts of your application:

### Kotlin

```
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
```