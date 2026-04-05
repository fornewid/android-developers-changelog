---
title: https://developer.android.com/develop/ui/compose/accessibility/testing
url: https://developer.android.com/develop/ui/compose/accessibility/testing
source: md.txt
---

An essential way of testing accessibility is a form of manual testing: by
turning accessibility services, like TalkBack or Switch Access, on, and checking
if everything works as expected. This provides direct insight into how users
with accessibility needs might experience your application.

In conjunction with manual verification, you should also use automated testing
to flag any potential issues that could impact user experience as you make
continual changes to your app.

[Existing Compose testing APIs](https://developer.android.com/develop/ui/compose/testing) allow you to write automated tests that
interact with semantic elements and to [assert the properties](https://developer.android.com/develop/ui/compose/testing/apis#assertions) defined in
your UI.

## Accessibility checks

For automated accessibility testing, you can also use the
[Accessibility Test Framework](https://github.com/google/Accessibility-Test-Framework-for-Android)---the same underlying framework that powers
Accessibility Scanner and accessibility checks in Espresso---to perform some
accessibility-related checks automatically, starting with Compose 1.8.0.

To enable the checks, add the `ui-test-junit4-accessibility` dependency,
call [`enableAccessibilityChecks()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#(androidx.compose.ui.test.ComposeUiTest).enableAccessibilityChecks(com.google.android.apps.common.testing.accessibility.framework.integrations.espresso.AccessibilityValidator)) in the [`AndroidComposeTestRule`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/AndroidComposeTestRule),
and trigger an action or [`tryPerformAccessibilityChecks`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/ui/ui-test/src/androidMain/kotlin/androidx/compose/ui/test/Actions.android.kt;drc=808c430f1ac6028d33902e3d685720f2b96f7aee;l=27):


```kotlin
@Rule
@JvmField
val composeTestRule = createAndroidComposeRule<ComponentActivity>()

@Test
fun noAccessibilityLabel() {
    composeTestRule.setContent {
        Box(
            modifier = Modifier
                .size(50.dp, 50.dp)
                .background(color = Color.Gray)
                .clickable { }
                .semantics {
                    contentDescription = ""
                }
        )
    }

    composeTestRule.enableAccessibilityChecks()

    // Any action (such as performClick) will perform accessibility checks too:
    composeTestRule.onRoot().tryPerformAccessibilityChecks()
}
```

<br />

This specific test fails with an exception and a message that the item may not
have a label readable by accessibility services.

Other available checks look for accessibility issues with color contrast,
small touch target size, or elements' traversal order.

If you're mixing Views with Compose and you're already using an
`AccessibilityValidator`, or you need to configure one, you can set it in the
rule:


```kotlin
@Test
fun lowContrastScreen() {
    composeTestRule.setContent {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(color = Color(0xFFFAFBFC)),
            contentAlignment = Alignment.Center
        ) {
            Text(text = "Hello", color = Color(0xFFB0B1B2))
        }
    }

    // Optionally, set AccessibilityValidator manually
    val accessibilityValidator = AccessibilityValidator()
        .setThrowExceptionFor(
            AccessibilityCheckResult.AccessibilityCheckResultType.WARNING
        )

    composeTestRule.enableAccessibilityChecks(accessibilityValidator)

    composeTestRule.onRoot().tryPerformAccessibilityChecks()
}
```

<br />

In combination with manual testing, automated tests using both Compose APIs as
well as the Accessibility Test Framework can help you detect possible problems
early on in the development process.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Accessibility in Compose](https://developer.android.com/develop/ui/compose/testing)
- \[Material Design 2 in Compose\]\[19\]
- [Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing/apis#assertions)