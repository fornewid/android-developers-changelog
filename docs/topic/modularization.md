---
title: https://developer.android.com/topic/modularization
url: https://developer.android.com/topic/modularization
source: md.txt
---

# Guide to Android app modularization

A project with multiple Gradle modules is known as a multi-module project. This guide encompasses best practices and recommended patterns for developing multi-module Android apps.
| **Note:** This page assumes a basic familiarity with the[recommended app architecture](https://developer.android.com/topic/architecture).

## The growing codebase problem

In an ever-growing codebase, scalability, readability, and overall code quality often decrease through time. This comes as a result of the codebase increasing in size without its maintainers taking active measures to enforce a structure that is easily maintainable. Modularization is a means of structuring your codebase in a way that improves maintainability and helps avoid these problems.

## What is modularization?

Modularization is a practice of organizing a codebase into loosely coupled and self contained parts. Each part is a module. Each module is independent and serves a clear purpose. By dividing a problem into smaller and easier to solve subproblems, you reduce the complexity of designing and maintaining a large system.
![](https://developer.android.com/static/topic/modularization/images/1_sample_dep_graph.png)**Figure 1**: Dependency graph of a sample multi-module codebase

## Benefits of modularization

The benefits of modularization are many, though they each center upon improving the maintainability and overall quality of a codebase. The following table summarizes the key benefits.

|          Benefit          |                                                                                                                                                                                                                                   Summary                                                                                                                                                                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reusability               | Modularization enables opportunities for code sharing and building multiple apps from the same foundation. Modules are effectively building blocks. Apps should be a sum of their features where the features are organized as separate modules. The functionality that a certain module provides may or may not be enabled in a particular app. For example, a`:feature:news`can be a part of the full version flavor and wear app but not part of the demo version flavor. |
| Strict visibility control | Modules enable you to easily control what you expose to other parts of your codebase. You can mark everything but your public interface as`internal`or`private`to prevent it from being used outside the module.                                                                                                                                                                                                                                                             |
| Customizable delivery     | [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)uses the advanced capabilities of app bundles, allowing you to deliver certain features of your app conditionally or on demand.                                                                                                                                                                                                                                                        |

The benefits of modularization are only achievable with a modularized codebase. The following benefits might be achieved with other techniques but modularization can help you enforce them even more.

|    Benefit    |                                                                                                                                                                          Summary                                                                                                                                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scalability   | In a tightly coupled codebase a single change can trigger a cascade of alterations in seemingly unrelated parts of code. A properly modularized project will embrace the[separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)principle and therefore limit the coupling. This empowers the contributors through greater autonomy. |
| Ownership     | In addition to enabling autonomy, modules can also be used to enforce accountability. A module can have a dedicated owner who is responsible for maintaining the code, fixing bugs, adding tests, and reviewing changes.                                                                                                                                   |
| Encapsulation | Encapsulation means that each part of your code should have the smallest possible amount of knowledge about other parts. Isolated code is easier to read and understand.                                                                                                                                                                                   |
| Testability   | Testability characterizes how easy it is to[test](https://developer.android.com/training/testing)your code. A testable codebase is one where components can be easily tested in isolation.                                                                                                                                                                 |
| Build time    | Some Gradle functionalities such as incremental build, build cache or parallel build, can leverage modularity to[improve build performance](https://developer.android.com/studio/build/optimize-your-build).                                                                                                                                               |

## Common pitfalls

The granularity of your codebase is the extent to which it is composed of modules. A more granular codebase has more, smaller modules. When designing a modularized codebase, you should decide on a level of granularity. To do so, take into account the size of your codebase and its relative complexity. Going too fine-grained will make the overhead a burden, and going too coarse will lessen the benefits of modularization.

Some common pitfalls are as follows:

- **Too fine-grained** : Every module brings a certain amount of overhead in the form of increased build complexity and[boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code). A complex build configuration makes it difficult to[keep configurations consistent](https://developer.android.com/topic/modularization/patterns#consistent-configuration)across modules. Too much boilerplate code results in a cumbersome codebase that is difficult to maintain. If overhead counteracts scalability improvements, you should consider consolidating some modules.
- **Too coarse-grained**: Conversely, if your modules are growing too large you might end up with yet another monolith and miss the benefits that modularity has to offer. For example, in a small project it's ok to put the data layer inside a single module. But as it grows, it might be necessary to separate repositories and data sources into standalone modules.
- **Too complex**: It doesn't always make sense to modularize your project. A dominating factor is the size of the codebase. If you don't expect your project to grow beyond a certain threshold, the scalability and build time gains won't apply.

## Is modularization the right technique for me?

If you need the benefits of reusability, strict visibility control or to use the[Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery), then modularization is a necessity for you. If you don't, but still want to benefit from improved scalability, ownership, encapsulation, or build times, then modularization is something worth considering.

## Samples

- [Now in Android](https://github.com/android/nowinandroid)- fully functional Android app featuring modularization.
- [Multi module architecture sample](https://github.com/android/architecture-samples/tree/multimodule)