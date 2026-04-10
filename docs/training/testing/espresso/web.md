---
title: https://developer.android.com/training/testing/espresso/web
url: https://developer.android.com/training/testing/espresso/web
source: md.txt
---

Espresso-Web is an entry point to work with Android WebView UI components.
Espresso-Web reuses Atoms from the popular [WebDriver API](http://www.seleniumhq.org/docs/03_webdriver.jsp) to examine and control the behavior of a WebView.

> [!NOTE]
> **Note:** If you aren't familiar with Espresso, you should first read the main [Espresso documentation](https://developer.android.com/training/testing/espresso).

## When to use Espresso-Web

Use Espresso-Web to test your hybrid apps, especially the integration of your
app's native UI components with its `https://developer.android.com/reference/android/webkit/WebView`
UI components. You can use the Espresso-Web API in conjunction with other
Espresso APIs to fully interact with web elements inside `WebView` objects.

If you need to test only the `https://developer.android.com/reference/android/webkit/WebView` itself, and not the
interactions between the `WebView` and native components in your app, consider
writing a general web test using a framework like [WebDriver](http://www.seleniumhq.org/docs/03_webdriver.jsp). If you use a web testing framework, you don't
need to use an Android device or a Java Virtual Machine, which makes your tests
run more quickly and reliably. That being said, Espresso-Web allows you to reuse
your custom WebDriver atoms, which gives you a lot of flexibility, especially
when writing tests that you plan to run against both standalone web apps and
apps that include an Android UI.

## How it works

Similarly to Espresso's [`onData()`](https://developer.android.com/reference/androidx/test/espresso/Espresso#onData(org.hamcrest.Matcher%3C?%20extends%20java.lang.Object%3E))
method, a `https://developer.android.com/reference/android/webkit/WebView` interaction comprises several Atoms.
`WebView` interactions use a combination of the Java programming language and a
JavaScript bridge to do their work. Because there is no chance of introducing
race conditions by exposing data from the JavaScript environment---everything
Espresso sees on the Java-based side is an isolated copy---returning data from
[`Web.WebInteraction`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction)
objects is fully supported, allowing you to verify all data that's returned from
a request.

### What is a WebDriver Atom?

The WebDriver framework uses Atoms to find and manipulate web elements
programmatically. Atoms are used by WebDriver to allow browser manipulation. An
Atom is conceptually similar to a
[`ViewAction`](https://developer.android.com/reference/androidx/test/espresso/ViewAction), a self-contained
unit that performs an action in your UI. You expose Atoms using a list of
defined methods, such as `findElement()` and `getElement()`, to drive the
browser from the user's point of view. However, if you use the WebDriver
framework directly, Atoms need to be properly orchestrated, requiring logic that
is quite verbose.

Within Espresso, the classes [`Web`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web)
and [`Web.WebInteraction`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction)
wrap this boilerplate and give an Espresso-like feel to interacting with WebView
objects. So in a context of a `https://developer.android.com/reference/android/webkit/WebView`, Atoms are used as
a substitution to traditional Espresso [`ViewMatchers`](https://developer.android.com/reference/androidx/test/espresso/matcher/ViewMatchers) and [`ViewActions`](https://developer.android.com/reference/androidx/test/espresso/action/ViewActions).

The API then looks quite simple:

### Kotlin

```kotlin
onWebView()
    .withElement(Atom)
    .perform(Atom)
    .check(WebAssertion)
```

### Java

```java
onWebView()
    .withElement(Atom)
    .perform(Atom)
    .check(WebAssertion);
```

To learn more, read [Selenium's documentation on Atoms](https://github.com/SeleniumHQ/selenium/wiki/Automation-Atoms).

## Implement WebView

Follow the guidance shown in the following sections to work with
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) in your app's tests.

### Packages

To include Espresso-Web in your project, complete the following steps:

1. Open your app's `build.gradle` file. This is usually not the top-level `build.gradle` file but `app/build.gradle`.
2. Add the following line inside dependencies:

   ### Groovy

   ```groovy
       androidTestImplementation 'androidx.test.espresso:espresso-web:3.6.1'
       
   ```

   ### Kotlin

   ```kotlin
       androidTestImplementation('androidx.test.espresso:espresso-web:3.6.1')
       
   ```
3. Espresso-Web is only compatible with Espresso 2.2 or higher and
   version 0.3 or higher of the testing library, so make sure you update those
   lines as well:

   ### Groovy

   ```groovy
       androidTestImplementation 'androidx.test:runner:1.6.1'
       androidTestImplementation 'androidx.test:rules:1.6.1'
       androidTestImplementation 'androidx.test.espresso:espresso-core:3.6.1'
       
   ```

   ### Kotlin

   ```kotlin
       androidTestImplementation('androidx.test:runner:1.6.1')
       androidTestImplementation('androidx.test:rules:1.6.1')
       androidTestImplementation('androidx.test.espresso:espresso-core:3.6.1')
       
   ```

### Common API usage

The [`onWebView()`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web#onWebView(org.hamcrest.Matcher%3Candroid.view.View%3E))
method is the main entry point when working with WebView on Android using
Espresso. You use this method to perform Espresso-Web tests, such as the
following:

### Kotlin

```kotlin
onWebView()
    .withElement(findElement(Locator.ID, "link_2")) // similar to onView(withId(...))
    .perform(webClick()) // Similar to perform(click())

    // Similar to check(matches(...))
    .check(webMatches(getCurrentUrl(), containsString("navigation_2.html")))
```

### Java

```java
onWebView()
    .withElement(findElement(Locator.ID, "link_2")) // similar to onView(withId(...))
    .perform(webClick()) // Similar to perform(click())

    // Similar to check(matches(...))
    .check(webMatches(getCurrentUrl(), containsString("navigation_2.html")));
```

In this example, Espresso-Web locates a DOM element whose ID is `"link_2"` and
clicks on it. The tool then verifies that the WebView sends a GET request
containing the `"navigation_2.html"` string.

### JavaScript support

When executing your tests, the system performs all WebView interactions using
JavaScript. Therefore, to support JavaScript evaluation, the WebView under test
must have JavaScript enabled.

You can force JavaScript to be enabled by calling
[`forceJavascriptEnabled()`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#forceJavascriptEnabled())
as an [action in your activity under
test](https://developer.android.com/guide/components/activities/testing#trigger-actions), as shown in the
following code snippet.

> [!NOTE]
> **Note:** Enabling JavaScript may cause the WebView under test to be reloaded. This is necessary to ensure that [AndroidJUnitRunner](https://developer.android.com/training/testing/junit-runner) loads all needed test infrastructure, including JavaScript interactions.

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @get:Rule val activityScenarioRule =
        activityScenarioRule<MyWebViewActivity>()

    @Test fun testWebViewInteraction() {
        onWebView().forceJavascriptEnabled()
    }
}
```

### Common web interactions

Common interactions with `Web.WebInteraction` objects include the following:

- `https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#withElement(androidx.test.espresso.web.model.ElementReference)`
  references a DOM element within the WebView.

  Example:

  ### Kotlin

  ```kotlin
  onWebView().withElement(findElement(Locator.ID, "teacher"))
  ```

  ### Java

  ```java
  onWebView().withElement(findElement(Locator.ID, "teacher"));
  ```
- [`withContextualElement()`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#withcontextualelement) references a scoped DOM element
  within the WebView, relative to another DOM element. You should call
  `withElement()` first to establish the reference
  `Web.WebInteraction` object (DOM element).

  Example:

  ### Kotlin

  ```kotlin
  .withElement(findElement(Locator.ID, "teacher"))
      .withContextualElement(findElement(Locator.ID, "person_name"))
  ```

  ### Java

  ```java
  .withElement(findElement(Locator.ID, "teacher"))
      .withContextualElement(findElement(Locator.ID, "person_name"));
  ```
- [`check()`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#check) evaluates a condition, making sure that it resolves
  to `true`.

  Example:

  ### Kotlin

  ```kotlin
  onWebView()
      .withElement(findElement(Locator.ID, "teacher"))
      .withContextualElement(findElement(Locator.ID, "person_name"))
      .check(webMatches(getText(), containsString("Socrates")))
  ```

  ### Java

  ```java
  onWebView()
      .withElement(findElement(Locator.ID, "teacher"))
      .withContextualElement(findElement(Locator.ID, "person_name"))
      .check(webMatches(getText(), containsString("Socrates")));
  ```
- [`perform()`](https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#perform) executes an action within a WebView, such as
  clicking on an element.

  Example:

  ### Kotlin

  ```kotlin
  onWebView()
      .withElement(findElement(Locator.ID, "teacher"))
      .perform(webClick())
  ```

  ### Java

  ```java
  onWebView()
      .withElement(findElement(Locator.ID, "teacher"))
      .perform(webClick());
  ```
- `https://developer.android.com/reference/androidx/test/espresso/web/sugar/Web.WebInteraction#reset()`
  reverts the WebView to its initial state. This is necessary when a prior
  action, such as a click, introduces a navigation change that makes
  ElementReference and WindowReference objects inaccessible.

  **Note:** Although using `reset()` is useful when
  making assertions against multi-page workflows, such as form submissions,
  your tests should usually be limited in scope and focus on a single page.

  Example:

  ### Kotlin

  ```kotlin
  onWebView()
      .withElement(...)
      .perform(...)
      .reset()
  ```

  ### Java

  ```java
  onWebView()
      .withElement(...)
      .perform(...)
      .reset();
  ```

### Example

The following example tests whether, after entering text into a WebView and
selecting a **Submit** button, the same text appears within a different element in
the same WebView:

### Kotlin

```kotlin
const val MACCHIATO = "Macchiato"

@RunWith(AndroidJUnit4::class)
class MyEspressoWebTestSuite {

    @Test fun typeTextInInput_clickButton_SubmitsForm() {
        // Create an intent that displays a web form.
        val webFormIntent = Intent()
        // ...

        // Lazily launch the Activity with a custom start Intent per test.
        ActivityScenario.launchActivity(webFormIntent)

        // Selects the WebView in your layout. If you have multiple WebView
        // objects, you can also use a matcher to select a given WebView,
        // onWebView(withId(R.id.web_view)).
        onWebView()
            // Find the input element by ID.
            .withElement(findElement(Locator.ID, "text_input"))

            // Clear previous input and enter new text into the input element.
            .perform(clearElement())
            .perform(DriverAtoms.webKeys(MACCHIATO))

            // Find the "Submit" button and simulate a click using JavaScript.
            .withElement(findElement(Locator.ID, "submitBtn"))
            .perform(webClick())

            // Find the response element by ID, and verify that it contains the
            // entered text.
            .withElement(findElement(Locator.ID, "response"))
            .check(webMatches(getText(), containsString(MACCHIATO)))
    }
}
```

### Java

```java
public static final String MACCHIATO = "Macchiato";

@Test
public void typeTextInInput_clickButton_SubmitsForm() {
    // Create an intent that displays a web form.
    Intent webFormIntent = new Intent();
    // ...

    // Lazily launch the Activity with a custom start Intent per test.
    ActivityScenario.launchActivity(webFormIntent);

    // Selects the WebView in your layout. If you have multiple WebView objects,
    // you can also use a matcher to select a given WebView,
    // onWebView(withId(R.id.web_view)).
    onWebView()
        // Find the input element by ID.
        .withElement(findElement(Locator.ID, "text_input"))

        // Clear previous input and enter new text into the input element.
        .perform(clearElement())
        .perform(DriverAtoms.webKeys(MACCHIATO))

        // Find the "Submit" button and simulate a click using JavaScript.
        .withElement(findElement(Locator.ID, "submitBtn"))
        .perform(webClick())

        // Find the response element by ID, and verify that it contains the
        // entered text.
        .withElement(findElement(Locator.ID, "response"))
        .check(webMatches(getText(), containsString(MACCHIATO)));
}
```

## Additional resources

For more information about using Espresso-Web in Android tests, consult the
following resources.

### Samples

- [WebBasicSample](https://github.com/android/testing-samples/tree/main/ui/espresso/WebBasicSample): Use Espresso-Web to interact with `WebView` objects.