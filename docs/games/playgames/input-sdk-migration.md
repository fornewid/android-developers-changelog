---
title: Migrate to the 1.0.0-beta Input SDK  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/input-sdk-migration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Migrate to the 1.0.0-beta Input SDK Stay organized with collections Save and categorize content based on your preferences.



This guide describes how to migrate your game to use the latest
Input SDK. The 1.0.0-beta SDK has substantial improvements over the
previous 0.0.4 preview. You should migrate from the earlier previews as soon as
possible. The 0.0.4 SDK will continue function through March 2023.

## Update the dependency

Delete the 0.0.4 library from your `libs` directory since the library is now
available on maven. Then Find this line in your module-level `build.grade`
file:

```
implementation files('libs/inputmapping-0.0.4.aar')
```

Replace it with the following code:

```
implementation 'com.google.android.libraries.play.games:inputmapping:1.0.0-beta'
```

## Implement the new InputMappingProvider interface

The former abstract class `InputMappingProvider` turned into an interface in
version `1.0.0-beta`. The method `onProvideInputMap()` is still part of the
interface.

### Kotlin

Remove `()` from the class definition since there's no constructor to invoke in
`InputMappingProvider`.

Locate your `InputMappingProvider` implementation:

```
class MyInputMapProvider : InputMappingProvider() {
    override fun onProvideInputMap(): InputMap {
        TODO("Not yet implemented")
    }
}
```

And update it to this:

```
class MyInputMapProvider : InputMappingProvider {
    override fun onProvideInputMap(): InputMap {
        TODO("Not yet implemented")
    }
}
```