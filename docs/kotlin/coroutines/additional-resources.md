---
title: https://developer.android.com/kotlin/coroutines/additional-resources
url: https://developer.android.com/kotlin/coroutines/additional-resources
source: md.txt
---

# Additional resources for Kotlin coroutines and flow

Use these additional resources to learn even more about Kotlin coroutines and flow. These resources are grouped by topic.

## Basics

- [First things first](https://medium.com/androiddevelopers/coroutines-first-things-first-e6187bf3bb21): This article teaches basic coroutine concepts, including`CoroutineScope`,`Job`, and`CoroutineContext`.
- [The ABC of coroutines](https://youtu.be/bM7PVVL_5GM): Learn about the most common classes and functions used when working with coroutines.
- [Coroutines in Android (series - 1st article linked)](https://medium.com/androiddevelopers/coroutines-on-android-part-i-getting-the-background-3e0e54d20bb): This post is the first in a series that teaches you about Kotlin coroutines.
- [Understand Kotlin Coroutines on Android](https://www.youtube.com/watch?v=BOHK_w09pVA): This Google I/O 2019 talk gives an overview of using Kotlin coroutines on Android.
- [Coroutines codelab](https://developer.android.com/codelabs/kotlin-coroutines): This codelab shows you how to use Kotlin coroutines to manage background threads and simplify your async code.
- [Coroutines: how to manage async tasks in Kotlin](https://youtu.be/6manrgTPzyA): Learn about the state of coroutines in Android as of 2020.

## Cancellation

- [Cancellation in coroutines](https://medium.com/androiddevelopers/cancellation-in-coroutines-aa6b90163629): This article talks about about the ins and outs of coroutine cancellation.
- [Coroutines: Gotta catch 'em all](https://www.youtube.com/watch?v=w0kfnydnFWI): Learn best practices for handling cancellation and exceptions in Kotlin coroutines.

## Exceptions

- [Exceptions in coroutines](https://medium.com/androiddevelopers/exceptions-in-coroutines-ce8da1ec060c): Learn how exceptions are propagated in coroutines and how to handle them.
- [Coroutines: Gotta catch 'em all](https://www.youtube.com/watch?v=w0kfnydnFWI): Learn best practices for handling cancellation and exceptions in Kotlin coroutines.

## Scopes

- [Easy coroutines in Android: viewModelScope](https://medium.com/androiddevelopers/easy-coroutines-in-android-viewmodelscope-25bffb605471): This article describes`viewModelScope`, an extension property that adds coroutines support to the`ViewModel`class.
- [Patterns for work that shouldn't be cancelled](https://medium.com/androiddevelopers/coroutines-patterns-for-work-that-shouldnt-be-cancelled-e26c40f142ad): This article describes how to trigger coroutines that shouldn't be cancelled using an`applicationScope`or`externalScope`.

## Flow

- [Going with the Flow](https://youtu.be/emk9_tVVLcc): Learn about the flow API and its benefits.
- [Advanced Coroutines with Kotlin Flow and LiveData](https://developer.android.com/codelabs/advanced-kotlin-coroutines): Learn how to use Kotlin coroutines with`LiveData`and flow in an Android app.
- [Lessons learnt using Coroutines Flow in the Android Dev Summit 2019 app](https://medium.com/androiddevelopers/lessons-learnt-using-coroutines-flow-4a6b285c0d06): This article highlights best practices and other lessons learned when adding flow support to the Android Dev Summit 2019 app.
- [Things to know about Flow's shareIn and stateIn operators](https://medium.com/androiddevelopers/things-to-know-about-flows-sharein-and-statein-operators-20e6ccb2bc74): This article talks about how the`stateIn`and`shareIn`operators can be used to improve performance, or even as a caching mechanism.
- [Migrating from LiveData to Kotlin Flow](https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb): This article talks about what's the equivalent Flow code for some of the most common LiveData patterns you can have in your app. This helps if you're interested in migrating from LiveData to Flow.

## Testing

- [Testing coroutines on Android](https://youtu.be/KMb0Fs8rCRs): Learn about the best practices to test your coroutines.
- [Testing codelab - Coroutines section](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-survey#3): Learn about testing ViewModels that use coroutines by replacing`Dispatchers.Main`with a`TestCoroutineDispatcher`.
- [Testing two consecutive LiveData emissions in Coroutines](https://medium.com/androiddevelopers/testing-two-consecutive-livedata-emissions-in-coroutines-5680b693cbf8): Learn how to use`TestCoroutineDispatcher`to pause and resume the execution of coroutines.

## Libraries, Jetpack, and Coroutines

- [LiveData with Coroutines and Flow](https://www.youtube.com/watch?v=B8ppnjGPAGE): This talk from the 2019 Android Dev Summit covers how to use the`liveData`coroutine builder along with testing patterns and antipatterns to make clean, efficient, and solid reactive UIs.
- [Building a Kotlin extensions library](https://developer.android.com/codelabs/building-kotlin-extensions-library): Learn how to build a Kotlin extensions library that adds coroutines and flow support to existing classes.
- [Simplifying APIs with coroutines and Flow](https://medium.com/androiddevelopers/simplifying-apis-with-coroutines-and-flow-a6fb65338765): Learn how to simplify your libraries with coroutine adapters, create your own, and see how they work under the hood.

## Coroutines in the view layer

- [Suspending over Views](https://medium.com/androiddevelopers/suspending-over-views-19de9ebd7020): This post talks about how coroutines can make UI programming easier.

## Under the hood

- [Suspend functions - Kotlin Vocabulary](https://youtu.be/IQf-vtIC-Uc): Learn why coroutines are important and how they work under the hood.
- [The suspend modifier under the hood](https://medium.com/androiddevelopers/the-suspend-modifier-under-the-hood-b7ce46af624f): Learn how the compiler transforms your code to suspend and resume the execution of your coroutines.