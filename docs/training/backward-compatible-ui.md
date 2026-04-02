---
title: https://developer.android.com/training/backward-compatible-ui
url: https://developer.android.com/training/backward-compatible-ui
source: md.txt
---

# Create backward-compatible UIs

This class demonstrates how to use UI components and APIs available in newer versions of Android in a backward-compatible way, ensuring that your application still runs on previous versions of the platform.

Throughout this class, the new[Action Bar Tabs](https://developer.android.com/guide/topics/ui/actionbar#Tabs)feature introduced in Android 3.0 (API level 11) serves as the guiding example, but you can apply these techniques to other UI components and API features.

## Lessons

**[Abstract the new APIs](https://developer.android.com/training/backward-compatible-ui/abstracting)**
:   Determine which features and APIs your application needs. Learn how to define application-specific, intermediary Java interfaces that abstract the implementation of the UI component to your application.

**[Proxy to the new APIs](https://developer.android.com/training/backward-compatible-ui/new-implementation)**
:   Learn how to create an implementation of your interface that uses newer APIs.

**[Create an implementation with older APIs](https://developer.android.com/training/backward-compatible-ui/older-implementation)**
:   Learn how to create a custom implementation of your interface that uses older APIs.

**[Use the version-aware component](https://developer.android.com/training/backward-compatible-ui/using-component)**
:   Learn how to choose an implementation to use at runtime, and begin using the interface in your application.

### You should also read

- [How to have your (Cup)cake and eat it too](http://android-developers.blogspot.com/2010/07/how-to-have-your-cupcake-and-eat-it-too.html)