---
title: https://developer.android.com/training/testing/espresso/accessibility-checking
url: https://developer.android.com/training/testing/espresso/accessibility-checking
source: md.txt
---

# Accessibility checking

Testing for accessibility lets you experience your app from the perspective of your entire user base, including users with accessibility needs. This form of testing can reveal opportunities to make your app more powerful and versatile.

This page describes how to add accessibility checks to your existing Espresso tests. For more information about accessibility, see the[Accessibility guides](https://developer.android.com/guide/topics/ui/accessibility).

## Enable checks

You can enable and configure accessibility testing using the[`AccessibilityChecks`](https://developer.android.com/reference/androidx/test/espresso/accessibility/AccessibilityChecks)class:  

### Kotlin

```kotlin
import androidx.test.espresso.accessibility.AccessibilityChecks

@RunWith(AndroidJUnit4::class)
@LargeTest
class MyWelcomeWorkflowIntegrationTest {
    init {
        AccessibilityChecks.enable()
    }
}
```

### Java

```java
import androidx.test.espresso.accessibility.AccessibilityChecks;

@RunWith(AndroidJUnit4.class)
@LargeTest
public class MyWelcomeWorkflowIntegrationTest {
    @BeforeClass
    public void enableAccessibilityChecks() {
        AccessibilityChecks.enable();
    }
}
```

By default, the checks run when you perform any view action defined in[`ViewActions`](https://developer.android.com/reference/androidx/test/espresso/action/ViewActions). Each check includes the view on which the action is performed as well as all descendant views. You can evaluate the entire view hierarchy of a screen during each check by passing`true`into[`setRunChecksFromRootView()`](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/integrations/espresso/AccessibilityValidator.java#L82), as shown in the following code snippet:  

### Kotlin

```kotlin
AccessibilityChecks.enable().setRunChecksFromRootView(true)
```

### Java

```java
AccessibilityChecks.enable().setRunChecksFromRootView(true);
```

## Suppress subsets of results

After Espresso runs accessibility checks on your app, you might find several opportunities to improve your app's accessibility that you cannot address immediately. In order to stop Espresso tests from continually failing because of these results, you can ignore them temporarily. The Accessibility Test Framework (ATF) provides this functionality using the[`setSuppressingResultMatcher()`](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/integrations/espresso/AccessibilityValidator.java#L95)method, which instructs Espresso to suppress all results that satisfy the given matcher expression.

When you make changes to your app that address one aspect of accessibility, it's beneficial for Espresso to show results for as many other aspects of accessibility as possible. For this reason, it's best to suppress only specific known opportunities for improvement.

When you temporarily suppress accessibility test findings that you plan to address later, it's important to not accidentally suppress similar findings. For this reason, use matchers that are narrowly scoped. To do so, choose a[matcher](http://hamcrest.org/JavaHamcrest/tutorial#a-tour-of-common-matchers)so that Espresso suppresses a given result only if it satisfies**each**of the following accessibility checks:

1. Accessibility checks of a certain type, such as those that check for touch target size.
2. Accessibility checks that evaluate a particular UI element, such as a button.

The[ATF defines several matchers](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckResultUtils.java)to help you define which results to show in your Espresso tests. The following example suppresses the results of checks that relate to a single`TextView`element's color contrast. The element's ID is`countTV`.  

### Kotlin

```kotlin
AccessibilityChecks.enable().apply {
        setSuppressingResultMatcher(
                allOf(
                    matchesCheck(TextContrastCheck::class.java),
                    matchesViews(withId(R.id.countTV))
                )
        )
}
```

### Java

```java
AccessibilityValidator myChecksValidator =
    AccessibilityChecks.enable()
        .setSuppressingResultMatcher(
            allOf(
                matchesCheck(TextContrastCheck.class),
                matchesViews(withId(R.id.countTV))));
```