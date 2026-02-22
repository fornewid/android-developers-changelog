---
title: https://developer.android.com/training/testing/espresso/lists
url: https://developer.android.com/training/testing/espresso/lists
source: md.txt
---

# Espresso lists

Espresso offers mechanisms to scroll to or act on a particular item for two types of lists: adapter views and recycler views.

When dealing with lists, especially those created with a`RecyclerView`or an`AdapterView`object, the view that you're interested in might not even be on the screen because only a small number of children are displayed and are recycled as you scroll. The`scrollTo()`method can't be used in this case because it requires an existing view.

## Interact with adapter view list items

Instead of using the`onView()`method, start your search with`onData()`and provide a matcher against the data that is backing the view you'd like to match. Espresso will do all the work of finding the row in the`Adapter`object and making the item visible in the viewport.

### Match data using a custom view matcher

The activity below contains a`ListView`, which is backed by a`SimpleAdapter`that holds data for each row in a`Map<String, Object>`object.

![The list activity currently shown on the screen contains a list with 23 items. Each item has a number, stored as a String, mapped to a different number, which is stored as an Object instead.](https://developer.android.com/static/images/training/testing/list-showing-all-rows.png)

Each map has two entries: a key`"STR"`that contains a String, such as`"item: x"`, and a key`"LEN"`that contains an`Integer`, which represents the length of the content. For example:  

```
{"STR" : "item: 0", "LEN": 7}
```

The code for a click on the row with "item: 50" looks like this:  

### Kotlin

```kotlin
onData(allOf(`is`(instanceOf(Map::class.java)), hasEntry(equalTo("STR"),
        `is`("item: 50")))).perform(click())
```

### Java

```java
onData(allOf(is(instanceOf(Map.class)), hasEntry(equalTo("STR"), is("item: 50"))))
    .perform(click());
```

Note that Espresso scrolls through the list automatically as needed.

Let's take apart the`Matcher<Object>`inside`onData()`. The`is(instanceOf(Map.class))`method narrows the search to any item of the`AdapterView`, which is backed by a`Map`object.

In our case, this aspect of the query matches every row of the list view, but we want to click specifically on an item, so we narrow the search further with:  

### Kotlin

```kotlin
hasEntry(equalTo("STR"), `is`("item: 50"))
```

### Java

```java
hasEntry(equalTo("STR"), is("item: 50"))
```

This`Matcher<String, Object>`will match any Map that contains an entry with the key`"STR"`and the value`"item: 50"`. Because the code to look up this is long and we want to reuse it in other locations, let's write a custom`withItemContent`matcher for that:  

### Kotlin

```kotlin
return object : BoundedMatcher<Object, Map>(Map::class.java) {
    override fun matchesSafely(map: Map): Boolean {
        return hasEntry(equalTo("STR"), itemTextMatcher).matches(map)
    }

    override fun describeTo(description: Description) {
        description.appendText("with item content: ")
        itemTextMatcher.describeTo(description)
    }
}
```

### Java

```java
return new BoundedMatcher<Object, Map>(Map.class) {
    @Override
    public boolean matchesSafely(Map map) {
        return hasEntry(equalTo("STR"), itemTextMatcher).matches(map);
    }

    @Override
    public void describeTo(Description description) {
        description.appendText("with item content: ");
        itemTextMatcher.describeTo(description);
    }
};
```

You use a`BoundedMatcher`as a base because to only match objects of type`Map`. Override the`matchesSafely()`method, putting in the matcher found earlier, and match it against a`Matcher<String>`that you can pass as an argument. This allows you to call`withItemContent(equalTo("foo"))`. For code brevity, you can create another matcher that already calls the`equalTo()`and accepts a`String`object:  

### Kotlin

```kotlin
fun withItemContent(expectedText: String): Matcher<Object> {
    checkNotNull(expectedText)
    return withItemContent(equalTo(expectedText))
}
```

### Java

```java
public static Matcher<Object> withItemContent(String expectedText) {
    checkNotNull(expectedText);
    return withItemContent(equalTo(expectedText));
}
```

Now the code to click on the item is simple:  

### Kotlin

```kotlin
onData(withItemContent("item: 50")).perform(click())
```

### Java

```java
onData(withItemContent("item: 50")).perform(click());
```

For the full code of this test, take a look at the`testClickOnItem50()`method within the[`AdapterViewTest`](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/AdapterViewTest.java)class and[this custom`LongListMatchers`](https://github.com/android/android-test/blob/461ca02299807020c0b317b1805eb709d3c25147/testapps/ui_testapp/javatests/androidx/test/ui/app/LongListMatchers.java)matcher on GitHub.

### Match a specific child view

The sample above issues a click in the middle of the entire row of a`ListView`. But what if we want to operate on a specific child of the row? For example, we would like to click on the second column of the row of the`LongListActivity`, which displays the String.length of the content in the first column:

![In this example, it would be beneficial to extract just the length of a particular piece of content. This process involves determining the value of the second column in a row.](https://developer.android.com/static/images/training/testing/list-highlighting-one-col.png)

Just add an`onChildView()`specification to your implementation of`DataInteraction`:  

### Kotlin

```kotlin
onData(withItemContent("item: 60"))
    .onChildView(withId(R.id.item_size))
    .perform(click())
```

### Java

```java
onData(withItemContent("item: 60"))
    .onChildView(withId(R.id.item_size))
    .perform(click());
```
| **Note:** This sample uses the`withItemContent()`matcher from the sample above. Take a look at the`testClickOnSpecificChildOfRow60()`method in the[`AdapterViewTest`](https://github.com/android/android-test/blob/7e834ce37faf52f2a65a73b0a6d83ab148707cbb/testapps/ui_testapp/javatests/androidx/test/ui/app/AdapterViewTest.java)class on GitHub.

## Interact with recycler view list items

`RecyclerView`objects work differently than`AdapterView`objects, so`onData()`cannot be used to interact with them.

To interact with RecyclerViews using Espresso, you can use the`espresso-contrib`package, which has a collection of[`RecyclerViewActions`](https://developer.android.com/reference/androidx/test/espresso/contrib/RecyclerViewActions)that can be used to scroll to positions or to perform actions on items:

- `scrollTo()`- Scrolls to the matched View, if it exists.
- `scrollToHolder()`- Scrolls to the matched View Holder, if it exists.
- `scrollToPosition()`- Scrolls to a specific position.
- `actionOnHolderItem()`- Performs a View Action on a matched View Holder.
- `actionOnItem()`- Performs a View Action on a matched View.
- `actionOnItemAtPosition()`- Performs a ViewAction on a view at a specific position.

The following snippets feature some examples from the[RecyclerViewSample](https://github.com/android/testing-samples/tree/main/ui/espresso/RecyclerViewSample)sample:  

### Kotlin

```kotlin
@Test(expected = PerformException::class)
fun itemWithText_doesNotExist() {
    // Attempt to scroll to an item that contains the special text.
    onView(ViewMatchers.withId(R.id.recyclerView))
        .perform(
            // scrollTo will fail the test if no item matches.
            RecyclerViewActions.scrollTo(
                hasDescendant(withText("not in the list"))
            )
        )
}
```

### Java

```java
@Test(expected = PerformException.class)
public void itemWithText_doesNotExist() {
    // Attempt to scroll to an item that contains the special text.
    onView(ViewMatchers.withId(R.id.recyclerView))
            // scrollTo will fail the test if no item matches.
            .perform(RecyclerViewActions.scrollTo(
                    hasDescendant(withText("not in the list"))
            ));
}
```  

### Kotlin

```kotlin
@Test fun scrollToItemBelowFold_checkItsText() {
    // First, scroll to the position that needs to be matched and click on it.
    onView(ViewMatchers.withId(R.id.recyclerView))
        .perform(
            RecyclerViewActions.actionOnItemAtPosition(
                ITEM_BELOW_THE_FOLD,
                click()
            )
        )

    // Match the text in an item below the fold and check that it's displayed.
    val itemElementText = "${activityRule.activity.resources
        .getString(R.string.item_element_text)} ${ITEM_BELOW_THE_FOLD.toString()}"
    onView(withText(itemElementText)).check(matches(isDisplayed()))
}
```

### Java

```java
@Test
public void scrollToItemBelowFold_checkItsText() {
    // First, scroll to the position that needs to be matched and click on it.
    onView(ViewMatchers.withId(R.id.recyclerView))
            .perform(RecyclerViewActions.actionOnItemAtPosition(ITEM_BELOW_THE_FOLD,
            click()));

    // Match the text in an item below the fold and check that it's displayed.
    String itemElementText = activityRule.getActivity().getResources()
            .getString(R.string.item_element_text)
            + String.valueOf(ITEM_BELOW_THE_FOLD);
    onView(withText(itemElementText)).check(matches(isDisplayed()));
}
```  

### Kotlin

```kotlin
@Test fun itemInMiddleOfList_hasSpecialText() {
    // First, scroll to the view holder using the isInTheMiddle() matcher.
    onView(ViewMatchers.withId(R.id.recyclerView))
        .perform(RecyclerViewActions.scrollToHolder(isInTheMiddle()))

    // Check that the item has the special text.
    val middleElementText = activityRule.activity.resources
            .getString(R.string.middle)
    onView(withText(middleElementText)).check(matches(isDisplayed()))
}
```

### Java

```java
@Test
public void itemInMiddleOfList_hasSpecialText() {
    // First, scroll to the view holder using the isInTheMiddle() matcher.
    onView(ViewMatchers.withId(R.id.recyclerView))
            .perform(RecyclerViewActions.scrollToHolder(isInTheMiddle()));

    // Check that the item has the special text.
    String middleElementText =
            activityRule.getActivity().getResources()
            .getString(R.string.middle);
    onView(withText(middleElementText)).check(matches(isDisplayed()));
}
```

## Additional resources

For more information about using Espresso lists in Android tests, consult the following resources.

### Samples

- [DataAdapterSample](https://github.com/android/testing-samples/tree/main/ui/espresso/DataAdapterSample): Showcases the`onData()`entry point for Espresso, for lists and`AdapterView`objects.