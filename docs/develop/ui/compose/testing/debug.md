---
title: https://developer.android.com/develop/ui/compose/testing/debug
url: https://developer.android.com/develop/ui/compose/testing/debug
source: md.txt
---

The main way to solve problems in your tests is to look at the semantics tree.
Print the tree by calling `composeTestRule.onRoot().printToLog()` at
any point in your test. This function prints a log like this:  

    Node #1 at (...)px
     |-Node #2 at (...)px
       OnClick = '...'
       MergeDescendants = 'true'
        |-Node #3 at (...)px
        | Text = 'Hi'
        |-Node #5 at (83.0, 86.0, 191.0, 135.0)px
          Text = 'There'

These logs contain valuable information for tracking bugs down.

## Additional Resources

- **[Test apps on Android](https://developer.android.com/training/testing)**: The main Android testing landing page provides a broader view of testing fundamentals and techniques.
- **[Fundamentals of testing](https://developer.android.com/training/testing/fundamentals):** Learn more about the core concepts behind testing an Android app.
- **[Local tests](https://developer.android.com/training/testing/local-tests):** You can run some tests locally, on your own workstation.
- **[Instrumented tests](https://developer.android.com/training/testing/instrumented-tests):** It is good practice to also run instrumented tests. That is, tests that run directly on-device.
- **[Continuous integration](https://developer.android.com/training/testing/continuous-integration):** Continuous integration lets you integrate your tests into your deployment pipeline.
- **[Test different screen sizes](https://developer.android.com/training/testing/different-screens):** With some many devices available to users, you should test for different screen sizes.
- **[Espresso](https://developer.android.com/training/testing/espresso)**: While intended for View-based UIs, Espresso knowledge can still be helpful for some aspects of Compose testing.