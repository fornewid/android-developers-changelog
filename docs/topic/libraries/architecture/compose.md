---
title: https://developer.android.com/topic/libraries/architecture/compose
url: https://developer.android.com/topic/libraries/architecture/compose
source: md.txt
---

# Integrate Lifecycle with Compose

The Lifecycle library offers built-in APIs that let you integrate with Jetpack[Compose](https://developer.android.com/jetpack/compose). Key APIs include the following:

- Flows for the current`Lifecycle.State`.
- `LifecycleEffects`that lets you run a block based on a specific`Lifecycle.Event`.

These integrations provide convenient hooks to manage Lifecycles within the Compose hierarchy. This document outlines how you can use them in your app.
| **Note:** The APIs described in this document were introduced in Lifecycle version 2.7.0.

## Collect lifecycle state with flows

Lifecycle exposes a`currentStateFlow`property that provides the current`Lifecycle.State`as a Kotlin`StateFlow`. You can collect this`Flow`as`State`. This allows your app to read changes in the Lifecycle during composition.  

    val lifecycleOwner = LocalLifecycleOwner.current
    val stateFlow = lifecycleOwner.lifecycle.currentStateFlow
    ...
    val currentLifecycleState by stateFlow.collectAsState()

The preceding example is accessible using the`lifecycle-common`module. The`currentStateAsState()`method is available in the`lifecycle-runtime-compose`module, which lets you conveniently read the current Lifecycle state with a single line. The following example demonstrates this:  

    val lifecycleOwner = LocalLifecycleOwner.current
    val currentLifecycleState = lifecycleOwner.lifecycle.currentStateAsState()

## Run code on lifecycle events

There are also`LifecycleEffects`that let you run a block when a particular`Lifecycle.Event`occurs.  

    LifecycleEventEffect(Lifecycle.Event.ON_START) {
      // do something here
    }

| **Warning:** You cannot use this to listen for`Lifecycle.Event.ON_DESTROY`since composition ends before this signal is sent.

In addition to the`LifecycleEventEffect`, you can also use`LifecycleStartEffect`and`LifecycleResumeEffect`. These APIs are tied to specific events. They also offer an additional block within their primary block that helps clean up any code that the event might have kicked off.

### LifecycleStartEffect

The`LifecycleStartEffect`is similar to the`LifecycleEffect`, but it runs only on`Lifecycle.Event.ON_START`events. It also accepts keys that work like other Compose keys. When the key changes, it triggers the block to run again.

When there is a`Lifecycle.Event.ON_STOP`event or the effect exits composition, it executes a`onStopOrDispose`block. This allows for the clean up of any work that was part of the starting block.  

    LifecycleStartEffect {
      // ON_START code is executed here

      onStopOrDispose {
        // do any needed clean up here
      }
    }

| **Note:** The`onStopOrDispose`block is always required and if it is not needed, you should use the`LifecycleEffect`, passing in the`Lifecycle.Event.ON_START`event instead.

### LifecycleResumeEffect

The`LifecycleResumeEffect`works in the same way as the`LifecycleStartedEffect`, but it executes on the`Lifecycle.Event.ON_RESUME`event instead. It also provides an`onPauseOrDispose`block that performs the clean up.  

    LifecycleResumeEffect {
      // ON_RESUME code is executed here

      onPauseOrDispose {
        // do any needed clean up here
      }
    }