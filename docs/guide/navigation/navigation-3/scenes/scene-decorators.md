---
title: Modify scenes with scene decorators  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/scenes/scene-decorators
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Modify scenes with scene decorators Stay organized with collections Save and categorize content based on your preferences.



Scene decorators let you modify the scene calculated by your app's [scene
strategy](/guide/navigation/navigation-3/scenes#understand-scene). In effect, they are used for a second phase of constructing the
content that's displayed by a [`NavDisplay`](/reference/kotlin/androidx/navigation3/ui/package-summary#top-level-functions-summary).

This approach lets you encapsulate specific functionality, such as displaying
common UI components, into individual scene decorators.

For example, consider a productivity app that has three top-level routes: an
email inbox, a direct message inbox, and a calendar view. Such an app could use
two scene decorators, one for adding a top app bar that displays information and
controls for the current top-level route and another for adding a persistent
navigation bar or rail to navigate between the routes.

## Create a scene decorator strategy

Scene decorators follow a similar pattern as scene strategies. To define a scene
decorator, implement the [`SceneDecoratorStrategy`](/reference/kotlin/androidx/navigation3/scene/SceneDecoratorStrategy) interface. This interface
has a method, [`decorateScene`](/reference/kotlin/androidx/navigation3/scene/SceneDecoratorStrategy#(androidx.navigation3.scene.SceneDecoratorStrategyScope).decorateScene(androidx.navigation3.scene.Scene)), which is analogous to the
[`calculateScene`](/reference/kotlin/androidx/navigation3/scene/SceneStrategy#(androidx.navigation3.scene.SceneStrategyScope).calculateScene(kotlin.collections.List)) method of the [`SceneStrategy`](/reference/kotlin/androidx/navigation3/scene/SceneStrategy) interface.
`decorateScene` determines whether it can decorate the scene:

* If your scene decorator strategy **shouldn't** decorate the input scene, it
  returns the input scene as-is.
* If it **should** decorate the input scene, it returns a new `Scene`. In
  general, the returned scene takes the input scene as a parameter and calls
  the input scene's [`content`](/reference/kotlin/androidx/navigation3/scene/Scene#content()) method within its own [`content`](/reference/kotlin/androidx/navigation3/scene/Scene#content())
  method.

To determine if and how the input scene should be decorated, your scene
decorator strategy can consider the metadata of both the input `Scene` and
the entries contained within that scene.

```
class MySceneDecoratorStrategy<T : Any> : SceneDecoratorStrategy<T> {


    override fun SceneDecoratorStrategyScope<T>.decorateScene(scene: Scene<T>): Scene<T> {
        // `shouldDecorate` determines if the scene should be decorated based on scene.metadata,
        // scene.entries.metadata, or any other relevant state.
        return if (shouldDecorate(scene)) {
            MyDecoratingScene(scene)
        } else {
            scene
        }
    }

}

class MyDecoratingScene<T : Any>(scene: Scene<T>) : Scene<T> {

    // ...

    override val content = @Composable {
        scene.content()
    }
}

SceneDecoratorSnippets.kt
```

**Warning:** `NavDisplay` doesn't decorate `Scene` instances that implement
[`OverlayScene`](/reference/kotlin/androidx/navigation3/scene/OverlayScene). This is because the content of an `OverlayScene` is
expected to be rendered in a separate window, so any wrapping content would
never be rendered.

## Use scene decorator strategies

To use scene decorator strategies, supply them to your `NavDisplay` using the
`sceneDecoratorStrategies` parameter. When decorating scenes, `NavDisplay` calls
the `decorateScene` method of each strategy in succession, passing the output of
each call as the input to the next.

```
NavDisplay(
    // ...
    sceneDecoratorStrategies = listOf(firstSceneDecoratorStrategy, secondSceneDecoratorStrategy)
)

SceneDecoratorSnippets.kt
```

## Common patterns for scene decorators

When implementing scene decorators, the following are some common patterns to be
aware of:

### Copy properties

In many cases, the scene returned by decorating a scene should contain the same
entries and have the same previous entries as the scene it's decorating.
Additionally, it should likely inherit (or modify) the metadata of the scene
it's decorating, rather than use the [default behavior](/reference/kotlin/androidx/navigation3/scene/Scene#metadata()). The following code
demonstrates an example of how to do this:

```
class CopyingScene<T : Any>(scene: Scene<T>) : Scene<T> {
    override val entries = scene.entries
    override val previousEntries = scene.previousEntries
    override val metadata = scene.metadata

    // ...
}

SceneDecoratorSnippets.kt
```

### Maintain animations

As detailed in [Animate between destinations](/guide/navigation/navigation-3/animate-destinations), `NavDisplay` automatically
animates transitions between scenes when a key derived from the class of the
current scene and its `key` property changes.

When introducing scene decorators to your app, the class of the scene returned
after scene decoration can remain the same, even when the class of the scene
returned during [scene calculation](/guide/navigation/navigation-3/scenes#understand-scene) changes. When this happens and
decorating scenes directly copy the `key` of the scene they're decorating, the
built-in animations no longer happen because the derived key doesn't change.

To maintain built-in animation support, decorating scenes should use a key
derived from the class and `key` of the scene returned by `calculateScene`.

```
class DerivedKeyScene<T : Any>(scene: Scene<T>) : Scene<T> {
    override val key = scene::class to scene.key

    // ...
}

SceneDecoratorSnippets.kt
```

**Tip:** Derive this key in the first strategy in the `sceneDecoratorStrategies`
list; then, any subsequent decorating scenes can directly copy the `key` of
their input scene.