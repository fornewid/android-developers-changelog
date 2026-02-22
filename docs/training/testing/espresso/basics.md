---
title: https://developer.android.com/training/testing/espresso/basics
url: https://developer.android.com/training/testing/espresso/basics
source: md.txt
---

This document explains how to complete common automated testing tasks using the
Espresso API.

The Espresso API encourages test authors to think in terms of what a user might
do while interacting with the application - locating UI elements and interacting
with them. At the same time, the framework prevents direct access to activities
and views of the application because holding on to these objects and operating
on them off the UI thread is a major source of test flakiness. Thus, you will
not see methods like `getView()` and `getCurrentActivity()` in the Espresso API.
You can still safely operate on views by implementing your own subclasses of
`ViewAction` and `ViewAssertion`.

## API components

The main components of Espresso include the following:

- **Espresso** -- Entry point to interactions with views (via `onView()` and `onData()`). Also exposes APIs that are not necessarily tied to any view, such as `pressBack()`.
- **ViewMatchers** -- A collection of objects that implement the `Matcher<? super View>` interface. You can pass one or more of these to the `onView()` method to locate a view within the current view hierarchy.
- **ViewActions** -- A collection of `ViewAction` objects that can be passed to the `ViewInteraction.perform()` method, such as `click()`.
- **ViewAssertions** -- A collection of `ViewAssertion` objects that can be passed the `ViewInteraction.check()` method. Most of the time, you will use the matches assertion, which uses a View matcher to assert the state of the currently selected view.

Example:  

### Kotlin

```kotlin
// withId(R.id.my_view) is a ViewMatcher
// click() is a ViewAction
// matches(isDisplayed()) is a ViewAssertion
onView(withId(R.id.my_view))
    .perform(click())
    .check(matches(isDisplayed()))
```

### Java

```java
// withId(R.id.my_view) is a ViewMatcher
// click() is a ViewAction
// matches(isDisplayed()) is a ViewAssertion
onView(withId(R.id.my_view))
    .perform(click())
    .check(matches(isDisplayed()));
```

## Find a view

In the vast majority of cases, the `onView()` method takes a hamcrest matcher
that is expected to match one --- and only one --- view within the current view
hierarchy. Matchers are powerful and will be familiar to those who have used
them with Mockito or JUnit. If you are not familiar with hamcrest matchers, we
suggest you start with a quick look at [this
presentation](https://www.slideshare.net/shaiyallin/hamcrest-matchers).

Often the desired view has a unique `R.id` and a simple `withId` matcher will
narrow down the view search. However, there are many legitimate cases when you
cannot determine `R.id` at test development time. For example, the specific view
may not have an `R.id` or the `R.id` is not unique. This can make normal
instrumentation tests brittle and complicated to write because the normal way to
access the view---with `findViewById()`--- does not work. Thus, you may
need to access private members of the Activity or Fragment holding the view or
find a container with a known `R.id` and navigate to its content for the
particular view.

Espresso handles this problem cleanly by allowing you to narrow down the view
using either existing `ViewMatcher` objects or your own custom ones.

Finding a view by its `R.id` is as simple as calling `onView()`:  

### Kotlin

```kotlin
onView(withId(R.id.my_view))
```

### Java

```java
onView(withId(R.id.my_view));
```

Sometimes, `R.id` values are shared between multiple views. When this happens an
attempt to use a particular `R.id` gives you an exception, such as
`AmbiguousViewMatcherException`. The exception message provides you with a text
representation of the current view hierarchy, which you can search for and find
the views that match the non-unique `R.id`:  

```
java.lang.RuntimeException:
androidx.test.espresso.AmbiguousViewMatcherException
This matcher matches multiple views in the hierarchy: (withId: is <123456789>)

...

+--->SomeView{id=123456789, res-name=plus_one_standard_ann_button,
visibility=VISIBLE, width=523, height=48, has-focus=false, has-focusable=true,
window-focus=true, is-focused=false, is-focusable=false, enabled=true,
selected=false, is-layout-requested=false, text=,
root-is-layout-requested=false, x=0.0, y=625.0, child-count=1}
****MATCHES****
|
+--->OtherView{id=123456789, res-name=plus_one_standard_ann_button,
visibility=VISIBLE, width=523, height=48, has-focus=false, has-focusable=true,
window-focus=true, is-focused=false, is-focusable=true, enabled=true,
selected=false, is-layout-requested=false, text=Hello!,
root-is-layout-requested=false, x=0.0, y=0.0, child-count=1}
****MATCHES****
```

Looking through the various attributes of the views, you may find uniquely
identifiable properties. In the example above, one of the views has the text
`"Hello!"`. You can use this to narrow down your search by using combination
matchers:  

### Kotlin

```kotlin
onView(allOf(withId(R.id.my_view), withText("Hello!")))
```

### Java

```java
onView(allOf(withId(R.id.my_view), withText("Hello!")));
```

You can also choose not to reverse any of the matchers:  

### Kotlin

```kotlin
onView(allOf(withId(R.id.my_view), not(withText("Unwanted"))))
```

### Java

```java
onView(allOf(withId(R.id.my_view), not(withText("Unwanted"))));
```

See [`ViewMatchers`](https://developer.android.com/reference/androidx/test/espresso/matcher/ViewMatchers)
for the view matchers provided by Espresso.

### Considerations

- In a well-behaved application, all views that a user can interact with should either contain descriptive text or have a content description. See [Making apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps) for more details. If you are not able to narrow down a search using `withText()` or `withContentDescription()`, consider treating it as an accessibility bug.
- Use the least descriptive matcher that finds the one view you're looking for. Do not over-specify as this will force the framework to do more work than is necessary. For example, if a view is uniquely identifiable by its text, you need not specify that the view is also assignable from `TextView`. For a lot of views the `R.id` of the view should be sufficient.
- If the target view is inside an `AdapterView`---such as `ListView`, `GridView`, or `Spinner`---the `onView()` method might not work. In these cases, you should use `onData()` instead.

## Perform an action on a view

When you have found a suitable matcher for the target view, it is possible to
perform instances of `ViewAction` on it using the perform method.

For example, to click on the view:  

### Kotlin

```kotlin
onView(...).perform(click())
```

### Java

```java
onView(...).perform(click());
```

You can execute more than one action with one perform call:  

### Kotlin

```kotlin
onView(...).perform(typeText("Hello"), click())
```

### Java

```java
onView(...).perform(typeText("Hello"), click());
```

If the view you are working with is located inside a `ScrollView` (vertical or
horizontal), consider preceding actions that require the view to be
displayed---such as `click()` and `typeText()`---with `scrollTo()`. This
ensures that the view is displayed before proceeding to the other action:  

### Kotlin

```kotlin
onView(...).perform(scrollTo(), click())
```

### Java

```java
onView(...).perform(scrollTo(), click());
```
| **Note:** The `scrollTo()` method will have no effect if the view is already displayed so you can safely use it in cases when the view is displayed due to larger screen size, such as when your tests run on both smaller and larger screen resolutions.

See [`ViewActions`](https://developer.android.com/reference/androidx/test/espresso/action/ViewActions)
for the view actions provided by Espresso.

## Check view assertions

Assertions can be applied to the currently selected view with the `check()`
method. The most used assertion is the `matches()` assertion. It uses a
`ViewMatcher` object to assert the state of the currently selected view.

For example, to check that a view has the text `"Hello!"`:  

### Kotlin

```kotlin
onView(...).check(matches(withText("Hello!")))
```

### Java

```java
onView(...).check(matches(withText("Hello!")));
```
| **Note:** Do not put "assertions" into the `onView()` argument. Instead, clearly specify what you are checking inside the check block.

If you want to assert that `"Hello!"` is content of the view, the following is considered bad practice:  

### Kotlin

```kotlin
// Don't use assertions like withText inside onView.
onView(allOf(withId(...), withText("Hello!"))).check(matches(isDisplayed()))
```

### Java

```kotlin
// Don't use assertions like withText inside onView.
onView(allOf(withId(...), withText("Hello!"))).check(matches(isDisplayed()));
```

On the other hand, if you want to assert that a view with the text `"Hello!"` is
visible---for example after a change of the views visibility flag---the
code is fine.
| **Note:** Be sure to pay attention to the difference between asserting that a view is not displayed and asserting that a view is not present in the view hierarchy.

### View assertion simple test

In this example, `SimpleActivity` contains a `Button` and a `TextView`. When the
button is clicked, the content of the `TextView` changes to `"Hello Espresso!"`.

Here's how to test this with Espresso:

#### Click on the button

The first step is to look for a property that helps to find the button. The
button in the `SimpleActivity` has a unique `R.id`, as expected.  

### Kotlin

```kotlin
onView(withId(R.id.button_simple))
```

### Java

```java
onView(withId(R.id.button_simple));
```

Now to perform the click:  

### Kotlin

```kotlin
onView(withId(R.id.button_simple)).perform(click())
```

### Java

```java
onView(withId(R.id.button_simple)).perform(click());
```

#### Verify the TextView text

The `TextView` with the text to verify has a unique `R.id` too:  

### Kotlin

```kotlin
onView(withId(R.id.text_simple))
```

### Java

```java
onView(withId(R.id.text_simple));
```

Now to verify the content text:  

### Kotlin

```kotlin
onView(withId(R.id.text_simple)).check(matches(withText("Hello Espresso!")))
```

### Java

```java
onView(withId(R.id.text_simple)).check(matches(withText("Hello Espresso!")));
```

## Check data loading in adapter views

`AdapterView` is a special type of widget that loads its data dynamically from
an Adapter. The most common example of an `AdapterView` is `ListView`. As
opposed to static widgets like `LinearLayout`, only a subset of the
`AdapterView` children may be loaded into the current view hierarchy. A simple
`onView()` search would not find views that are not currently loaded.

Espresso handles this by providing a separate `onData()` entry point which is
able to first load the adapter item in question, bringing it into focus prior to
operating on it or any of its children.
| **Note:** You may choose to bypass the `onData()` loading action for items in adapter views that are initially displayed on screen because they are already loaded. However, it is safer to always use `onData()`.

**Warning:** Custom implementations of
`AdapterView` can have problems with the `onData()`
method if they break inheritance contracts, particularly the
`getItem()` API. In such cases, the best course of action is to
refactor your application code. If you cannot do so, you can implement a
matching custom `AdapterViewProtocol`. For more information, take a
look at the default
[`AdapterViewProtocols`](https://developer.android.com/reference/androidx/test/espresso/action/AdapterViewProtocols) class provided by Espresso.

### Adapter view simple test

This simple test demonstrates how to use `onData()`. `SimpleActivity` contains a
`Spinner` with a few items that represent types of coffee beverages. When an
item is selected, there is a `TextView` that changes to `"One %s a day!"`, where
`%s` represents the selected item.

The goal of this test is to open the `Spinner`, select a specific item, and
verify that the `TextView` contains the item. As the `Spinner` class is based
on`AdapterView`, it is recommended to use `onData()` instead of `onView()` for
matching the item.

#### Open the item selection

### Kotlin

```kotlin
onView(withId(R.id.spinner_simple)).perform(click())
```

### Java

```java
onView(withId(R.id.spinner_simple)).perform(click());
```

#### Select an item

For the item selection, the `Spinner` creates a `ListView` with its contents.
This view can be very long, and the element might not be contributed to the view
hierarchy. By using `onData()` we force our desired element into the view
hierarchy. The items in the `Spinner` are strings, so we want to match an item
that is equal to the String `"Americano"`:  

### Kotlin

```kotlin
onData(allOf(`is`(instanceOf(String::class.java)),
        `is`("Americano"))).perform(click())
```

### Java

```java
onData(allOf(is(instanceOf(String.class)), is("Americano"))).perform(click());
```

#### Verify text is correct

### Kotlin

```kotlin
onView(withId(R.id.spinnertext_simple))
    .check(matches(withText(containsString("Americano"))))
```

### Java

```kotlin
onView(withId(R.id.spinnertext_simple))
    .check(matches(withText(containsString("Americano"))));
```

## Debugging

Espresso provides useful debugging information when a test fails:

### Logging

Espresso logs all view actions to logcat. For example:  

```
ViewInteraction: Performing 'single click' action on view with text: Espresso
```

### View hierarchy

Espresso prints the view hierarchy in the exception message when `onView()`
fails.

- If `onView()` does not find the target view, a `NoMatchingViewException` is thrown. You can examine the view hierarchy in the exception string to analyze why the matcher did not match any views.
- If `onView()` finds multiple views that match the given matcher, an `AmbiguousViewMatcherException` is thrown. The view hierarchy is printed and all views that were matched are marked with the `MATCHES` label:

```
java.lang.RuntimeException:
androidx.test.espresso.AmbiguousViewMatcherException
This matcher matches multiple views in the hierarchy: (withId: is <123456789>)

...

+--->SomeView{id=123456789, res-name=plus_one_standard_ann_button,
visibility=VISIBLE, width=523, height=48, has-focus=false, has-focusable=true,
window-focus=true, is-focused=false, is-focusable=false, enabled=true,
selected=false, is-layout-requested=false, text=,
root-is-layout-requested=false, x=0.0, y=625.0, child-count=1}
****MATCHES****
|
+--->OtherView{id=123456789, res-name=plus_one_standard_ann_button,
visibility=VISIBLE, width=523, height=48, has-focus=false, has-focusable=true,
window-focus=true, is-focused=false, is-focusable=true, enabled=true,
selected=false, is-layout-requested=false, text=Hello!,
root-is-layout-requested=false, x=0.0, y=0.0, child-count=1}
****MATCHES****
```

When dealing with a complicated view hierarchy or unexpected behavior of widgets
it is always helpful to use the
[Hierarchy Viewer](https://developer.android.com/studio/profile/hierarchy-viewer) in Android Studio for
an explanation.

### Adapter view warnings

Espresso warns users about presence of `AdapterView` widgets. When an `onView()`
operation throws a `NoMatchingViewException` and `AdapterView` widgets are
present in the view hierarchy, the most common solution is to use `onData()`.
The exception message will include a warning with a list of the adapter views.
You may use this information to invoke `onData()` to load the target view.

## Additional resources

For more information about using Espresso in Android tests, consult the
following resources.

### Samples

- [CustomMatcherSample](https://github.com/android/testing-samples/tree/main/ui/espresso/CustomMatcherSample): Shows how to extend Espresso to match the hint property of an `EditText` object.
- [RecyclerViewSample](https://github.com/android/testing-samples/tree/main/ui/espresso/RecyclerViewSample): `RecyclerView` actions for Espresso.
- [(more...)](https://developer.android.com/training/testing/espresso/additional-resources#samples)