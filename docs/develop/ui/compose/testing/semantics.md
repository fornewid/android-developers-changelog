---
title: Semantics  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/testing/semantics
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Semantics Stay organized with collections Save and categorize content based on your preferences.



UI tests in Compose use *semantics* to interact with the UI hierarchy.
Semantics, as the name implies, give meaning to a piece of UI. In this context,
a "piece of UI" (or element) can mean anything from a single composable to a
full screen. The *semantics tree* is generated alongside the UI hierarchy and
describes the hierarchy.

You can learn more about semantics generally in [Semantics in Compose](/develop/ui/compose/accessibility/semantics).

![Diagram showing a typical UI layout, and the way that layout would map to a corresponding semantic tree](/static/develop/ui/compose/images/testing-semantic-tree.png)

**Figure 1.** A typical UI hierarchy and its semantics tree.

The semantics framework is primarily used for accessibility, so tests take
advantage of the information exposed by semantics about the UI hierarchy.
Developers decide what and how much to expose.

![A button containing a graphic and text](/static/develop/ui/compose/images/testing-button.png)

**Figure 2.** A typical button containing an icon and text.

For example, given a button like this that consists of an icon and a text
element, the default semantics tree only contains the text label "Like". This is
because some composables, such as `Text`, already expose some properties to the
semantics tree. You can add properties to the semantics tree by using a
`Modifier`.

```
MyButton(
    modifier = Modifier.semantics { contentDescription = "Add to favorites" }
)
```

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