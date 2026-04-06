---
title: https://developer.android.com/develop/ui/compose/testing/apis
url: https://developer.android.com/develop/ui/compose/testing/apis
source: md.txt
---

There are three main ways to interact with UI elements:

- **Finders** let you select one or multiple elements (or *nodes* in the semantics tree) to make assertions or perform actions on them.
- **Assertions** are used to verify that the elements exist or have certain attributes.
- **Actions** inject simulated user events on the elements, such as clicks or other gestures.

Some of these APIs accept a [`SemanticsMatcher`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsMatcher) to refer to one or more
*nodes* in the semantics tree.

> [!NOTE]
> **Note:** Testing a Compose UI is different from testing a view-based UI. The view-based UI toolkit clearly defines what a view is. A view occupies a rectangular space and has properties, like identifiers, position, margin, and padding. In Compose, because only some composables *emit* UI into the UI hierarchy, you need a different approach to matching UI elements.

### Finders

You can use [`onNode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteractionsProvider#onNode(androidx.compose.ui.test.SemanticsMatcher,kotlin.Boolean)) and [`onAllNodes`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteractionsProvider#onAllNodes(androidx.compose.ui.test.SemanticsMatcher,kotlin.Boolean)) to select one or multiple nodes
respectively, but you can also use convenience finders for the most common
searches, such as [`onNodeWithText`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteractionsProvider).onNodeWithText(kotlin.String,kotlin.Boolean,kotlin.Boolean,kotlin.Boolean)), and
[`onNodeWithContentDescription`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteractionsProvider).onNodeWithContentDescription(kotlin.String,kotlin.Boolean,kotlin.Boolean,kotlin.Boolean)). You can browse the complete list in the
[Compose Testing cheat sheet](https://developer.android.com/develop/ui/compose/testing-cheatsheet).

#### Select a single node

    composeTestRule.onNode(<<SemanticsMatcher>>, useUnmergedTree = false): SemanticsNodeInteraction

    // Example
    composeTestRule
        .onNode(hasText("Button")) // Equivalent to onNodeWithText("Button")

#### Select multiple nodes

    composeTestRule
        .onAllNodes(<<SemanticsMatcher>>): SemanticsNodeInteractionCollection

    // Example
    composeTestRule
        .onAllNodes(hasText("Button")) // Equivalent to onAllNodesWithText("Button")

#### Unmerged tree

Some nodes merge the semantics information of their children. For example, a
button with two text elements merges the text element labels:

    MyButton {
        Text("Hello")
        Text("World")
    }

From a test, use [`printToLog()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).printToLog(kotlin.String,kotlin.Int)) to show the semantics tree:

    composeTestRule.onRoot().printToLog("TAG")

This code prints the following output:

    Node #1 at (...)px
     |-Node #2 at (...)px
       Role = 'Button'
       Text = '[Hello, World]'
       Actions = [OnClick, GetTextLayoutResult]
       MergeDescendants = 'true'

If you need to match a node of what would be the *unmerged* tree, you can set
`useUnmergedTree` to `true`:

    composeTestRule.onRoot(useUnmergedTree = true).printToLog("TAG")

This code prints the following output:

    Node #1 at (...)px
     |-Node #2 at (...)px
       OnClick = '...'
       MergeDescendants = 'true'
        |-Node #3 at (...)px
        | Text = '[Hello]'
        |-Node #5 at (83.0, 86.0, 191.0, 135.0)px
          Text = '[World]'

The `useUnmergedTree` parameter is available in all finders. For example, here
it's used in an `onNodeWithText` finder.

    composeTestRule
        .onNodeWithText("World", useUnmergedTree = true).assertIsDisplayed()

### Assertions

Check assertions by calling `assert()` on the [`SemanticsNodeInteraction`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction)
returned by a finder with one or multiple matchers:

    // Single matcher:
    composeTestRule
        .onNode(matcher)
        .assert(hasText("Button")) // hasText is a SemanticsMatcher

    // Multiple matchers can use and / or
    composeTestRule
        .onNode(matcher).assert(hasText("Button") or hasText("Button2"))

You can also use convenience functions for the most common assertions, such as
[`assertExists`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction#assertExists(kotlin.String)), [`assertIsDisplayed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction#(androidx.compose.ui.test.SemanticsNodeInteraction).assertIsDisplayed()), and [`assertTextEquals`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction#(androidx.compose.ui.test.SemanticsNodeInteraction).assertTextEquals(kotlin.Array,kotlin.Boolean)).
You can browse the complete list in the [Compose Testing cheat sheet](https://developer.android.com/develop/ui/compose/testing-cheatsheet).

There are also functions to check assertions on a collection of nodes:

    // Check number of matched nodes
    composeTestRule
        .onAllNodesWithContentDescription("Beatle").assertCountEquals(4)
    // At least one matches
    composeTestRule
        .onAllNodesWithContentDescription("Beatle").assertAny(hasTestTag("Drummer"))
    // All of them match
    composeTestRule
        .onAllNodesWithContentDescription("Beatle").assertAll(hasClickAction())

### Actions

To inject an action on a node, call a `perform...()` function:

    composeTestRule.onNode(...).performClick()

> [!NOTE]
> **Note:** You cannot chain actions inside a perform function. Instead, make multiple `perform...()` calls.

Here are some examples of actions:

    performClick(),
    performSemanticsAction(key),
    performKeyPress(keyEvent),
    performGesture { swipeLeft() }

You can browse the complete list in the
[Compose Testing cheat sheet](https://developer.android.com/develop/ui/compose/testing-cheatsheet).

### Matchers

A variety of matchers are available for testing your Compose
code.

#### Hierarchical matchers

Hierarchical matchers let you go up or down the semantics tree and perform
matching.

    fun hasParent(matcher: SemanticsMatcher): SemanticsMatcher
    fun hasAnySibling(matcher: SemanticsMatcher): SemanticsMatcher
    fun hasAnyAncestor(matcher: SemanticsMatcher): SemanticsMatcher
    fun hasAnyDescendant(matcher: SemanticsMatcher):  SemanticsMatcher

Here are some examples of these matchers being used:

    composeTestRule.onNode(hasParent(hasText("Button")))
        .assertIsDisplayed()

#### Selectors

An alternative way to create tests is to use *selectors* which can make some
tests more readable.

    composeTestRule.onNode(hasTestTag("Players"))
        .onChildren()
        .filter(hasClickAction())
        .assertCountEquals(4)
        .onFirst()
        .assert(hasText("John"))

You can browse the complete list in the [Compose Testing cheat sheet](https://developer.android.com/develop/ui/compose/testing-cheatsheet).

## Additional Resources

- **[Test apps on Android](https://developer.android.com/training/testing)**: The main Android testing landing page provides a broader view of testing fundamentals and techniques.
- **[Fundamentals of testing](https://developer.android.com/training/testing/fundamentals):** Learn more about the core concepts behind testing an Android app.
- **[Local tests](https://developer.android.com/training/testing/local-tests):** You can run some tests locally, on your own workstation.
- **[Instrumented tests](https://developer.android.com/training/testing/instrumented-tests):** It is good practice to also run instrumented tests. That is, tests that run directly on-device.
- **[Continuous integration](https://developer.android.com/training/testing/continuous-integration):** Continuous integration lets you integrate your tests into your deployment pipeline.
- **[Test different screen sizes](https://developer.android.com/training/testing/different-screens):** With some many devices available to users, you should test for different screen sizes.
- **[Espresso](https://developer.android.com/training/testing/espresso)**: While intended for View-based UIs, Espresso knowledge can still be helpful for some aspects of Compose testing.