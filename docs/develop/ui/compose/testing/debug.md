---
title: Debug tests  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/testing/debug
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Debug tests Stay organized with collections Save and categorize content based on your preferences.




The main way to solve problems in your tests is to look at the semantics tree.
Print the tree by calling `composeTestRule.onRoot().printToLog()` at
any point in your test. This function prints a log like this:

```
Node #1 at (...)px
 |-Node #2 at (...)px
   OnClick = '...'
   MergeDescendants = 'true'
    |-Node #3 at (...)px
    | Text = 'Hi'
    |-Node #5 at (83.0, 86.0, 191.0, 135.0)px
      Text = 'There'
```

These logs contain valuable information for tracking bugs down.

## Additional Resources

* **[Test apps on Android](/training/testing)**: The main Android testing
  landing page provides a broader view of testing fundamentals and techniques.
* **[Fundamentals of testing](/training/testing/fundamentals):** Learn more
  about the core concepts behind testing an Android app.
* **[Local tests](/training/testing/local-tests):** You can run some tests
  locally, on your own workstation.
* **[Instrumented tests](/training/testing/instrumented-tests):** It is good
  practice to also run instrumented tests. That is, tests that run directly
  on-device.
* **[Continuous integration](/training/testing/continuous-integration):**
  Continuous integration lets you integrate your tests into your deployment
  pipeline.
* **[Test different screen sizes](/training/testing/different-screens):** With
  some many devices available to users, you should test for different screen
  sizes.
* **[Espresso](/training/testing/espresso)**: While intended for View-based
  UIs, Espresso knowledge can still be helpful for some aspects of Compose
  testing.