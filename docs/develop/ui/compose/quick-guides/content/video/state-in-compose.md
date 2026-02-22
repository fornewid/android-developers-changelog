---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/video/state-in-compose
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/state-in-compose
source: md.txt
---

<br />

Learn how to establish and manage state in your Compose-based app and how
to configure the UI to react to changes in state. See how to create observable
states, how to retain state across recompositions or configuration changes, and
how to structure your composables for optimal data flow.  

## Key points

- If your app's state is internal to a composable, use [`remember`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remember(kotlin.Function0)) to persist the state across re-composition.
- Use [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)) to persist the state across configuration changes.
- *State hoisting* is a programming pattern where you move the state to the caller of a composable. Where possible, use state hoisting to make the composable more reusable and testable.
- Use the [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) class to hold an exposed state in an observable state holder, better encapsulating the state and creating a single source of truth for the UI.

## Resources

- [Codelab: State in Jetpack Compose](https://developer.android.com/codelabs/jetpack-compose-state#0)

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Compose basics (video collection)

This series of videos introduces various Compose APIs, quickly showing you what's available and how to use them.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/compose-basics)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)