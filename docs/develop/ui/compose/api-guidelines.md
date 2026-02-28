---
title: https://developer.android.com/develop/ui/compose/api-guidelines
url: https://developer.android.com/develop/ui/compose/api-guidelines
source: md.txt
---

[Video](https://www.youtube.com/watch?v=JvbyGcqdWBA)

If you're writing Compose code for your app or building Compose libraries and
APIs, follow best practices to make your code scalable, more performant, and
consistent with the rest of the ecosystem.

The following documents provide guidelines for anyone writing code that uses
Compose:

- [API Guidelines for Jetpack Compose](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/compose/docs/compose-api-guidelines.md): Outlines patterns, best practices, and prescriptive style guidelines for any system using the Jetpack Compose compiler plugin and runtime. It includes the following topics:
  - Kotlin style guidelines for Compose, based on the [Kotlin Coding
    Conventions](https://kotlinlang.org/docs/coding-conventions.html)
  - Guidance for `@Composable` functions and APIs that build on the Compose runtime capabilities
  - Guidelines for APIs that use and extend the Compose UI toolkit
  - Patterns for addressing use cases when designing a Compose API
- [API Guidelines for `@Composable` components in Jetpack Compose](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/compose/docs/compose-component-api-guidelines.md): Provides a set of guidelines and recommendations for creating and using `@Composable` UI components, including the following topics:
  - Creating and layering components
  - Naming a new component
  - Expressing component dependencies
  - Parameters in `@Composable` components
  - Following correct patterns for creating component-related classes and functions
  - Documenting `@Composable` components
  - Improving accessibility for components
  - Updating component APIs while retaining backwards compatibility

## Audience

These guidelines are written for the following three audiences:

- **Developers building apps based on Jetpack Compose**. You are in this group if you use Jetpack Compose in some part of your app.
- **Developers working on Jetpack Compose framework development** . You are in this group if you make contributions to the [`androidx.compose` libraries](https://developer.android.com/jetpack/androidx/releases/compose).
- **Developers creating libraries based on Jetpack Compose**. You are in this group if you create Compose APIs or libraries of Compose UI elements. These libraries of Compose components may be publicly available or local to your company or team.

Depending on the group you're in, you have different strictness levels for each
style guideline. For example, Jetpack Compose framework development generally
adheres most strictly to these guidelines.

For more information about the requirements for each developer audience, see
[RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## Contribute to framework and guidelines

We welcome contributions to select libraries in the `androidx` codebase and the
style guidelines ([Compose API guidelines](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/compose/docs/compose-api-guidelines.md) and
[`@Composable` components guidelines](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/compose/docs/compose-component-api-guidelines.md)) themselves.

To contribute, follow the instructions in the `androidx` [contribution
guide](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/CONTRIBUTING.md).