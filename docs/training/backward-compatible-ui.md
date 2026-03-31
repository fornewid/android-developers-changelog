---
title: Create backward-compatible UIs  |  Views  |  Android Developers
url: https://developer.android.com/training/backward-compatible-ui
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create backward-compatible UIs Stay organized with collections Save and categorize content based on your preferences.



This class demonstrates how to use UI components and APIs available in newer versions of Android in a backward-compatible way, ensuring that your application still runs on previous versions of the platform.

Throughout this class, the new [Action Bar Tabs](/guide/topics/ui/actionbar#Tabs) feature introduced in Android 3.0 (API level 11) serves as the guiding example, but you can apply these techniques to other UI components and API features.

## Lessons

**[Abstract the new APIs](/training/backward-compatible-ui/abstracting)**
:   Determine which features and APIs your application needs. Learn how to define application-specific, intermediary Java interfaces that abstract the implementation of the UI component to your application.

**[Proxy to the new APIs](/training/backward-compatible-ui/new-implementation)**
:   Learn how to create an implementation of your interface that uses newer APIs.

**[Create an implementation with older APIs](/training/backward-compatible-ui/older-implementation)**
:   Learn how to create a custom implementation of your interface that uses older APIs.

**[Use the version-aware component](/training/backward-compatible-ui/using-component)**
:   Learn how to choose an implementation to use at runtime, and begin using the interface in your application.

### You should also read

* [How to have your (Cup)cake and eat it too](http://android-developers.blogspot.com/2010/07/how-to-have-your-cupcake-and-eat-it-too.html)