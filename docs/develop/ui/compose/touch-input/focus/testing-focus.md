---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus
url: https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus
source: md.txt
---

Automating focus navigation tests ensures your app delivers a consistent and
predictable user experience across hardware keyboards, D-pads, and
accessibility tools. Compose provides built-in testing APIs to simulate key
input and verify focus states.

## Set up focus tests

To write focus tests, use `createComposeRule()` from the Compose testing
library:


```kotlin
@RunWith(AndroidJUnit4::class)
class FocusNavigationTest {
    @get:Rule
    val composeTestRule = createComposeRule()
```

<br />

> [!NOTE]
> **Note:** By default, Compose testing environments initialize in touch mode. To configure whether your test environment starts in touch mode or keyboard mode, see the [default input mode configuration](https://developer.android.com/develop/ui/compose/testing/migrate-v2#default-input-mode).

## Verify focus targets

You can verify whether a UI element can receive focus by performing a click or
requesting focus, and then asserting its state using [`assertIsFocused()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).assertIsFocused()) and
[`assertIsNotFocused()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).assertIsNotFocused()).


```kotlin
@Test
fun interactiveElement_isFocusTarget() {
    composeTestRule.setContent {
        AppTheme {
            CardListScreen()
        }
    }

    val firstCard = composeTestRule.onNodeWithTag("card_1")
    val secondCard = composeTestRule.onNodeWithTag("card_2")

    // Focus the first element
    firstCard.performClick()
    firstCard.assertIsFocused()
    secondCard.assertIsNotFocused()
}
```

<br />

## Test one-dimensional focus traversal

Simulate <kbd>Tab</kbd> and <kbd>Shift+Tab</kbd> key presses
using [`performKeyInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).performKeyInput(kotlin.Function1)) to verify that focus advances through the UI
in appearance order. As a best practice,
verify both forward navigation (`Key.Tab`) and reverse navigation
(`Key.Tab` with `Key.ShiftLeft` held down) to ensure two-way traversal
integrity:


```kotlin
@Test
fun tabKey_navigatesInAppearanceOrder() {
    composeTestRule.setContent {
        AppTheme {
            CardListScreen()
        }
    }

    val firstCard = composeTestRule.onNodeWithTag("card_1")
    val secondCard = composeTestRule.onNodeWithTag("card_2")
    val thirdCard = composeTestRule.onNodeWithTag("card_3")

    firstCard.performClick()
    firstCard.assertIsFocused()

    // Press Tab -> Moves to second card
    firstCard.performKeyInput {
        pressKey(Key.Tab)
    }
    secondCard.assertIsFocused()
    firstCard.assertIsNotFocused()

    // Press Tab -> Moves to third card
    secondCard.performKeyInput {
        pressKey(Key.Tab)
    }
    thirdCard.assertIsFocused()

    // Press Shift + Tab -> Moves backward to second card
    thirdCard.performKeyInput {
        withKeyDown(Key.ShiftLeft) {
            pressKey(Key.Tab)
        }
    }
    secondCard.assertIsFocused()
}
```

<br />

## Test two-dimensional directional traversal

Simulate arrow keys or D-pad directional keys using [`Key.DirectionDown`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/Key#DirectionDown()),
[`Key.DirectionUp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/Key#DirectionUp()), [`Key.DirectionRight`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/Key#DirectionRight()), and [`Key.DirectionLeft`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/key/Key#DirectionLeft()).


```kotlin
@Test
fun arrowKeys_moveFocusTwoDimensionallyWithoutWrap() {
    composeTestRule.setContent {
        AppTheme {
            GridLayoutScreen()
        }
    }

    val topLeftButton = composeTestRule.onNodeWithTag("btn_top_left")
    val bottomLeftButton = composeTestRule.onNodeWithTag("btn_bottom_left")

    topLeftButton.performClick()
    topLeftButton.assertIsFocused()

    // Down arrow moves focus downward to bottom-left button
    topLeftButton.performKeyInput {
        pressKey(Key.DirectionDown)
    }
    bottomLeftButton.assertIsFocused()

    // Directional keys do not wrap around: pressing Down on bottom element stays focused
    bottomLeftButton.performKeyInput {
        pressKey(Key.DirectionDown)
    }
    bottomLeftButton.assertIsFocused()
}
```

<br />

## Test text field focus behavior

Verify that single-line text fields advance focus on <kbd>Tab</kbd>, while multi-line
text fields retain focus:


```kotlin
@Test
fun textField_handlesTabAccordingToLineLimits() {
    composeTestRule.setContent {
        AppTheme {
            FormScreen()
        }
    }

    val singleLineNode = composeTestRule.onNodeWithTag("single_line_field")
    val multiLineNode = composeTestRule.onNodeWithTag("multi_line_field")
    val submitButtonNode = composeTestRule.onNodeWithTag("submit_button")

    // Single-line field advances focus on Tab
    singleLineNode.performClick()
    singleLineNode.assertIsFocused()
    singleLineNode.performKeyInput { pressKey(Key.Tab) }
    multiLineNode.assertIsFocused()

    // Multi-line field keeps focus and inserts '\t'
    multiLineNode.performKeyInput { pressKey(Key.Tab) }
    multiLineNode.assertIsFocused()
    submitButtonNode.assertIsNotFocused()

    // Shift + Tab escapes multi-line field to previous target
    multiLineNode.performKeyInput {
        withKeyDown(Key.ShiftLeft) { pressKey(Key.Tab) }
    }
    singleLineNode.assertIsFocused()
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [Focus in text fields](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)