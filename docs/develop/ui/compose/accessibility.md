---
title: Accessibility in Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/accessibility
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Accessibility in Jetpack Compose Stay organized with collections Save and categorize content based on your preferences.



Developing with accessibility in mind means making your apps usable for
everyone, including people with accessibility needs, who may use Android devices
in many different ways. Compose provides a foundation for building more
accessible UIs with its declarative APIs and tools that help make your apps
more inclusive.

There are several key and supporting concepts in Compose accessibility:

* [**API defaults**](/develop/ui/compose/accessibility/api-defaults): Learn how Compose handles accessibility
  by default and how to leverage semantics and patterns to support accessibility
  from the start, and use them for custom components.
* [**Semantics**](/develop/ui/compose/accessibility/semantics): Understand the system of representing the
  meaning and role of UI elements for accessibility services, and how to choose
  appropriate semantics to represent properties like content types,
  descriptions, and states.
* [**Modify traversal order**](/develop/ui/compose/accessibility/traversal): Modify the order in which
  accessibility services navigate through elements on screen, which can be
  customized for better user experience.
* [**Support user-scalable content**](/develop/ui/compose/accessibility/scalable-content): Allow users to adjust the size of text
  and UI elements in your app to fit their needs.
* [**Merging and clearing**](/develop/ui/compose/accessibility/merging-clearing): Understand semantic merging and
  clearing strategies and APIs, and when it is appropriate to hide semantics
  from accessibility services.
* [**Inspect and debug**](/develop/ui/compose/accessibility/inspect-debug): Inspect your composables'
  accessibility semantics with tools and debug unexpected behaviors when using
  Android's assistive technologies.
* [**Testing**](/develop/ui/compose/accessibility/testing): Detect common accessibility issues and automate
  some aspects of testing with Compose accessibility checks.

**Important:** For more information about accessibility in Android generally, see
the [accessibility guides](/guide/topics/ui/accessibility).

## Additional resources

* **[Accessibility in Jetpack Compose codelab](/codelabs/jetpack-compose-accessibility):** Codelab for learning more
  about supporting accessibility in Compose.
* **[What's new in accessibility for developers](https://www.youtube.com/watch?v=6LsaP6oKxMY):** IO '22 talk.
* **[Build accessible apps](/guide/topics/ui/accessibility):** Essential
  concepts and techniques common to all Android app development.
* **[Make apps more accessible](/guide/topics/ui/accessibility/apps):** Key
  steps you can take to make your app more accessible.
* **[Principles for improving app
  accessibility](/guide/topics/ui/accessibility/principles):** Key principles
  to keep in mind when working to make your app more accessible.
* **[Testing for Accessibility](/guide/topics/ui/accessibility/testing):**
  Testing principles and tools for Android accessibility.