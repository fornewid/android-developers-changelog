---
title: https://developer.android.com/training/testing/espresso/recipes
url: https://developer.android.com/training/testing/espresso/recipes
source: md.txt
---

This document describes how to set up a variety of common Espresso tests.

## Match a view next to another view

A layout could contain certain views that are not unique by themselves. For example, a repeating call button in a table of contacts could have the same`R.id`, contain the same text, and have the same properties as other call buttons within the view hierarchy.

For example, in this activity, the view with text`"7"`repeats across multiple rows:

![A list activity showing 3 copies of the same view element inside a 3-item list](https://developer.android.com/static/images/training/testing/repeated-view.png)

Often, the non-unique view will be paired with some unique label that's located next to it, such as a name of the contact next to the call button. In this case, you can use the`hasSibling()`matcher to narrow down your selection:  

### Kotlin

```kotlin
onView(allOf(withText("7"), hasSibling(withText("item: 0"))))
    .perform(click())
```

### Java

```java
onView(allOf(withText("7"), hasSibling(withText("item: 0"))))
    .perform(click());
```

## Match a view that is inside an action bar

The`ActionBarTestActivity`has two different action bars: a normal action bar and a contextual action bar that is created from a options menu. Both action bars have one item that is always visible and two items that are only visible in overflow menu. When an item is clicked, it changes a TextView to the content of the clicked item.

Matching visible icons on both of the action bars is straightforward, as shown in the following code snippet:  

### Kotlin

```kotlin
fun testClickActionBarItem() {
    // We make sure the contextual action bar is hidden.
    onView(withId(R.id.hide_contextual_action_bar))
        .perform(click())

    // Click on the icon - we can find it by the r.Id.
    onView(withId(R.id.action_save))
        .perform(click())

    // Verify that we have really clicked on the icon
    // by checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Save")))
}
```

### Java

```java
public void testClickActionBarItem() {
    // We make sure the contextual action bar is hidden.
    onView(withId(R.id.hide_contextual_action_bar))
        .perform(click());

    // Click on the icon - we can find it by the r.Id.
    onView(withId(R.id.action_save))
        .perform(click());

    // Verify that we have really clicked on the icon
    // by checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Save")));
}
```

![The save button is on the action bar, at the top of the activity](https://developer.android.com/static/images/training/testing/save-button-clicked.png)

The code looks identical for the contextual action bar:  

### Kotlin

```kotlin
fun testClickActionModeItem() {
    // Make sure we show the contextual action bar.
    onView(withId(R.id.show_contextual_action_bar))
        .perform(click())

    // Click on the icon.
    onView((withId(R.id.action_lock)))
        .perform(click())

    // Verify that we have really clicked on the icon
    // by checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Lock")))
}
```

### Java

```java
public void testClickActionModeItem() {
    // Make sure we show the contextual action bar.
    onView(withId(R.id.show_contextual_action_bar))
        .perform(click());

    // Click on the icon.
    onView((withId(R.id.action_lock)))
        .perform(click());

    // Verify that we have really clicked on the icon
    // by checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Lock")));
}
```

![The lock button is on the action bar, at the top of the activity](https://developer.android.com/static/images/training/testing/lock-button-clicked.png)

Clicking on items in the overflow menu is a bit trickier for the normal action bar as some devices have a hardware overflow menu button, which opens the overflowing items in an options menu, and some devices have a software overflow menu button, which opens a normal overflow menu. Luckily, Espresso handles that for us.

For the normal action bar:  

### Kotlin

```kotlin
fun testActionBarOverflow() {
    // Make sure we hide the contextual action bar.
    onView(withId(R.id.hide_contextual_action_bar))
        .perform(click())

    // Open the options menu OR open the overflow menu, depending on whether
    // the device has a hardware or software overflow menu button.
    openActionBarOverflowOrOptionsMenu(
            ApplicationProvider.getApplicationContext<Context>())

    // Click the item.
    onView(withText("World"))
        .perform(click())

    // Verify that we have really clicked on the icon by checking
    // the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("World")))
}
```

### Java

```java
public void testActionBarOverflow() {
    // Make sure we hide the contextual action bar.
    onView(withId(R.id.hide_contextual_action_bar))
        .perform(click());

    // Open the options menu OR open the overflow menu, depending on whether
    // the device has a hardware or software overflow menu button.
    openActionBarOverflowOrOptionsMenu(
            ApplicationProvider.getApplicationContext());

    // Click the item.
    onView(withText("World"))
        .perform(click());

    // Verify that we have really clicked on the icon by checking
    // the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("World")));
}
```

![The overflow menu button is visible, and a list appears beneath the action bar near the top of the screen](https://developer.android.com/static/images/training/testing/software-menu-selected.png)

This is how this looks on devices with a hardware overflow menu button:

![There is no overflow menu button, and a list appears near the bottom of the screen](https://developer.android.com/static/images/training/testing/hardware-menu-selected.png)

For the contextual action bar it is really easy again:  

### Kotlin

```kotlin
fun testActionModeOverflow() {
    // Show the contextual action bar.
    onView(withId(R.id.show_contextual_action_bar))
        .perform(click())

    // Open the overflow menu from contextual action mode.
    openContextualActionModeOverflowMenu()

    // Click on the item.
    onView(withText("Key"))
        .perform(click())

    // Verify that we have really clicked on the icon by
    // checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Key")))
    }
}
```

### Java

```java
public void testActionModeOverflow() {
    // Show the contextual action bar.
    onView(withId(R.id.show_contextual_action_bar))
        .perform(click());

    // Open the overflow menu from contextual action mode.
    openContextualActionModeOverflowMenu();

    // Click on the item.
    onView(withText("Key"))
        .perform(click());

    // Verify that we have really clicked on the icon by
    // checking the TextView content.
    onView(withId(R.id.text_action_bar_result))
        .check(matches(withText("Key")));
    }
}
```

![The overflow menu button appears in the action bar, and the list of options appear underneath the action bar, near the top of the screen](https://developer.android.com/static/images/training/testing/contextual-menu-selected.png)

To see the full code for these samples, view the[`ActionBarTest.java`](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/ActionBarTest.java)sample on GitHub.

## Assert that a view is not displayed

After performing a series of actions, you will certainly want to assert the state of the UI under test. Sometimes, this may be a negative case, such as when something is not happening. Keep in mind that you can turn any hamcrest view matcher into a`ViewAssertion`by using`ViewAssertions.matches()`.

In the example below, we take the`isDisplayed()`matcher and reverse it using the standard`not()`matcher:  

### Kotlin

```kotlin
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.isDisplayed
import androidx.test.espresso.matcher.ViewMatchers.withId
import org.hamcrest.Matchers.not

onView(withId(R.id.bottom_left))
    .check(matches(not(isDisplayed())))
```

### Java

```java
import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.assertion.ViewAssertions.matches;
import static androidx.test.espresso.matcher.ViewMatchers.isDisplayed;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static org.hamcrest.Matchers.not;

onView(withId(R.id.bottom_left))
    .check(matches(not(isDisplayed())));
```

The above approach works if the view is still part of the hierarchy. If it is not, you will get a`NoMatchingViewException`and you need to use`ViewAssertions.doesNotExist()`.

## Assert that a view is not present

If the view is gone from the view hierarchy---which can happen when an action caused a transition to another activity---you should use`ViewAssertions.doesNotExist()`:  

### Kotlin

```kotlin
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.assertion.ViewAssertions.doesNotExist
import androidx.test.espresso.matcher.ViewMatchers.withId

onView(withId(R.id.bottom_left))
    .check(doesNotExist())
```

### Java

```java
import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.assertion.ViewAssertions.doesNotExist;
import static androidx.test.espresso.matcher.ViewMatchers.withId;

onView(withId(R.id.bottom_left))
    .check(doesNotExist());
```

## Assert that a data item is not in an adapter

To prove a particular data item is not within an`AdapterView`you have to do things a little differently. We have to find the`AdapterView`we're interested in and interrogate the data its holding. We don't need to use`onData()`. Instead, we use`onView()`to find the`AdapterView`and then use another matcher to work on the data inside the view.

First the matcher:  

### Kotlin

```kotlin
private fun withAdaptedData(dataMatcher: Matcher<Any>): Matcher<View> {
    return object : TypeSafeMatcher<View>() {

        override fun describeTo(description: Description) {
            description.appendText("with class name: ")
            dataMatcher.describeTo(description)
        }

        public override fun matchesSafely(view: View) : Boolean {
            if (view !is AdapterView<*>) {
                return false
            }

            val adapter = view.adapter
            for (i in 0 until adapter.count) {
                if (dataMatcher.matches(adapter.getItem(i))) {
                    return true
                }
            }

            return false
        }
    }
}
```

### Java

```java
private static Matcher<View> withAdaptedData(final Matcher<Object> dataMatcher) {
    return new TypeSafeMatcher<View>() {

        @Override
        public void describeTo(Description description) {
            description.appendText("with class name: ");
            dataMatcher.describeTo(description);
        }

        @Override
        public boolean matchesSafely(View view) {
            if (!(view instanceof AdapterView)) {
                return false;
            }

            @SuppressWarnings("rawtypes")
            Adapter adapter = ((AdapterView) view).getAdapter();
            for (int i = 0; i < adapter.getCount(); i++) {
                if (dataMatcher.matches(adapter.getItem(i))) {
                    return true;
                }
            }

            return false;
        }
    };
}
```

Then the all we need is`onView()`to find the`AdapterView`:  

### Kotlin

```kotlin
fun testDataItemNotInAdapter() {
    onView(withId(R.id.list))
          .check(matches(not(withAdaptedData(withItemContent("item: 168")))))
    }
}
```

### Java

```java
@SuppressWarnings("unchecked")
public void testDataItemNotInAdapter() {
    onView(withId(R.id.list))
          .check(matches(not(withAdaptedData(withItemContent("item: 168")))));
    }
}
```

And we have an assertion that will fail if an item that is equal to "item: 168" exists in an adapter view with the ID list.

For the full sample, look at the`testDataItemNotInAdapter()`method within the[`AdapterViewTest.java`](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/AdapterViewTest.java)class on GitHub.

## Use a custom failure handler

Replacing the default`FailureHandler`in Espresso with a custom one allows for additional or different error handling, such as taking a screenshot or passing along extra debug information.

The`CustomFailureHandlerTest`example demonstrates how to implement a custom failure handler:  

### Kotlin

```kotlin
private class CustomFailureHandler(targetContext: Context) : FailureHandler {
    private val delegate: FailureHandler

    init {
        delegate = DefaultFailureHandler(targetContext)
    }

    override fun handle(error: Throwable, viewMatcher: Matcher<View>) {
        try {
            delegate.handle(error, viewMatcher)
        } catch (e: NoMatchingViewException) {
            throw MySpecialException(e)
        }

    }
}
```

### Java

```java
private static class CustomFailureHandler implements FailureHandler {
    private final FailureHandler delegate;

    public CustomFailureHandler(Context targetContext) {
        delegate = new DefaultFailureHandler(targetContext);
    }

    @Override
    public void handle(Throwable error, Matcher<View> viewMatcher) {
        try {
            delegate.handle(error, viewMatcher);
        } catch (NoMatchingViewException e) {
            throw new MySpecialException(e);
        }
    }
}
```

This failure handler throws a`MySpecialException`instead of a`NoMatchingViewException`and delegates all other failures to the`DefaultFailureHandler`. The`CustomFailureHandler`can be registered with Espresso in the`setUp()`method of the test:  

### Kotlin

```kotlin
@Throws(Exception::class)
override fun setUp() {
    super.setUp()
    getActivity()
    setFailureHandler(CustomFailureHandler(
            ApplicationProvider.getApplicationContext<Context>()))
}
```

### Java

```java
@Override
public void setUp() throws Exception {
    super.setUp();
    getActivity();
    setFailureHandler(new CustomFailureHandler(
            ApplicationProvider.getApplicationContext()));
}
```

For more information, see the[`FailureHandler`](https://developer.android.com/reference/androidx/test/espresso/FailureHandler)interface and[`Espresso.setFailureHandler()`](https://developer.android.com/reference/androidx/test/espresso/Espresso#setFailureHandler(androidx.test.espresso.FailureHandler)).

## Target non-default windows

Android supports multiple windows. Normally, this is transparent to the users and the app developer, yet in certain cases multiple windows are visible, such as when an auto-complete window gets drawn over the main application window in the search widget. To simplify things, by default Espresso uses a heuristic to guess which`Window`you intend to interact with. This heuristic is almost always good enough; however, in rare cases, you'll need to specify which window an interaction should target. You can do this by providing your own root window matcher, or`Root`matcher:  

### Kotlin

```kotlin
onView(withText("South China Sea"))
    .inRoot(withDecorView(not(`is`(getActivity().getWindow().getDecorView()))))
    .perform(click())
```

### Java

```java
onView(withText("South China Sea"))
    .inRoot(withDecorView(not(is(getActivity().getWindow().getDecorView()))))
    .perform(click());
```

As is the case with[`ViewMatchers`](https://developer.android.com/reference/androidx/test/espresso/matcher/ViewMatchers), we provide a set of pre-provided[`RootMatchers`](https://developer.android.com/reference/androidx/test/espresso/matcher/RootMatchers). Of course, you can always implement your own`Matcher`object.

Take a look at the[MultipleWindowTest sample](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/MultipleWindowTest.java)on GitHub.

## Match a header or footer in a list view

Headers and footers are added to`ListViews`using the`addHeaderView()`and`addFooterView()`methods. To ensure`Espresso.onData()`knows what data object to match, make sure to pass a preset data object value as the second parameter to`addHeaderView()`and`addFooterView()`. For example:  

### Kotlin

```kotlin
const val FOOTER = "FOOTER"
...
val footerView = layoutInflater.inflate(R.layout.list_item, listView, false)
footerView.findViewById<TextView>(R.id.item_content).text = "count:"
footerView.findViewById<TextView>(R.id.item_size).text
        = data.size.toString
listView.addFooterView(footerView, FOOTER, true)
```

### Java

```java
public static final String FOOTER = "FOOTER";
...
View footerView = layoutInflater.inflate(R.layout.list_item, listView, false);
footerView.findViewById<TextView>(R.id.item_content).setText("count:");
footerView.findViewById<TextView>(R.id.item_size).setText(String.valueOf(data.size()));
listView.addFooterView(footerView, FOOTER, true);
```

Then, you can write a matcher for the footer:  

### Kotlin

```kotlin
import org.hamcrest.Matchers.allOf
import org.hamcrest.Matchers.instanceOf
import org.hamcrest.Matchers.`is`

fun isFooter(): Matcher<Any> {
    return allOf(`is`(instanceOf(String::class.java)),
            `is`(LongListActivity.FOOTER))
}
```

### Java

```java
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.is;

@SuppressWarnings("unchecked")
public static Matcher<Object> isFooter() {
    return allOf(is(instanceOf(String.class)), is(LongListActivity.FOOTER));
}
```

And loading the view in a test is trivial:  

### Kotlin

```kotlin
import androidx.test.espresso.Espresso.onData
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.sample.LongListMatchers.isFooter

fun testClickFooter() {
    onData(isFooter())
        .perform(click())

    // ...
}
```

### Java

```java
import static androidx.test.espresso.Espresso.onData;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.sample.LongListMatchers.isFooter;

public void testClickFooter() {
    onData(isFooter())
        .perform(click());

    // ...
}
```

Take a look at the full code sample, found in the`testClickFooter()`method of[`AdapterViewTest.java`](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/AdapterViewTest.java)on GitHub.