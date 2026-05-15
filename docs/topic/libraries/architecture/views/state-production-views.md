---
title: https://developer.android.com/topic/libraries/architecture/views/state-production-views
url: https://developer.android.com/topic/libraries/architecture/views/state-production-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/topic/architecture/ui-layer/state-production)

Fundamentally, state production is the incremental application of changes to the
UI state. State always exists, and it changes as a result of events. The
differences between events and state are summarized in the table below:

|---|---|
| **Events** | **State** |
| Transient, unpredictable, and exist for a finite period. | Always exists. |
| The inputs of state production. | The output of state production. |
| The product of the UI or other sources. | Is consumed by the UI. |

Events can come from:

- **Users**: As they interact with the app's UI.
- **Other sources of state change**: APIs that present app data from UI, domain, or data layers like snackbar timeout events, use cases or repositories respectively.

## State production APIs

There are two main APIs used in state production depending on what stage of the
pipeline you're in:

|---|---|
| **Pipeline Stage** | **API** |
| Input | You should use asynchronous APIs to perform work off the UI thread to keep the UI jank free. For example, Coroutines or Flows in Kotlin, and RxJava or callbacks in the Java Programming Language. |
| Output | You should use observable data holder APIs to invalidate and rerender the UI when state changes. For example, StateFlow or LiveData. Observable data holders guarantee the UI always has a UI state to display on the screen |

Of the two, the choice of asynchronous API for input has a greater influence on
the nature of the state production pipeline than the choice of observable API
for output. This is because the inputs **dictate the kind of processing that may
be applied to the pipeline**.

## State production pipeline assembly

The next sections cover state production techniques best suited for various
inputs, and the output APIs that match. Each state production pipeline is a
combination of inputs and outputs and should be:

- **Lifecycle aware**: In the case where the UI is not visible or active, the state production pipeline should not consume any resources unless explicitly required.
- **Easy to consume**: The UI should be able to easily render the produced UI state. Considerations for the output of the state production pipeline will vary across different View APIs such as the View system or Jetpack Compose.

## Output types in state production pipelines

The choice of the output API for UI state, and the nature of its presentation
depends largely on the API your app uses to render the UI. In Android apps, you
can choose to use Views or Jetpack Compose. Considerations here include:

- Reading state in a [lifecycle aware](https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3) manner.
- Whether state should be [exposed in one or multiple fields](https://developer.android.com/topic/architecture/ui-layer#additional-considerations) from the state holder.

The following table summarizes what APIs to use for your state production
pipeline when using the Views framework:

|---|---|
| **Input** | **Output** |
| One-shot APIs | `StateFlow` or `LiveData` |
| Stream APIs | `StateFlow` or `LiveData` |
| One-shot and stream APIs | `StateFlow` or `LiveData` |