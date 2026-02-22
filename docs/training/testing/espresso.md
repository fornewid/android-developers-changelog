---
title: https://developer.android.com/training/testing/espresso
url: https://developer.android.com/training/testing/espresso
source: md.txt
---

# Espresso

Use Espresso to write concise, beautiful, and reliable Android UI tests.

The following code snippet shows an example of an Espresso test:

<br />

### Kotlin

```kotlin
@Test
fun greeterSaysHello() {
    onView(withId(R.id.name_field)).perform(typeText("Steve"))
    onView(withId(R.id.greet_button)).perform(click())
    onView(withText("Hello Steve!")).check(matches(isDisplayed()))
}
```

### Java

```java
@Test
public void greeterSaysHello() {
    onView(withId(R.id.name_field)).perform(typeText("Steve"));
    onView(withId(R.id.greet_button)).perform(click());
    onView(withText("Hello Steve!")).check(matches(isDisplayed()));
}
```

<br />

![](https://developer.android.com/static/images/training/testing/espresso.png)

The core API is small, predictable, and easy to learn and yet remains open for customization. Espresso tests state expectations, interactions, and assertions clearly without the distraction of boilerplate content, custom infrastructure, or messy implementation details getting in the way.

Espresso tests run optimally fast! It lets you leave your waits, syncs, sleeps, and polls behind while it manipulates and asserts on the application UI when it is at rest.

## Target audience

Espresso is targeted at developers, who believe that automated testing is an integral part of the development lifecycle. While it can be used for black-box testing, Espresso's full power is unlocked by those who are familiar with the codebase under test.

## Synchronization capabilities

Each time your test invokes[`onView()`](https://developer.android.com/reference/androidx/test/espresso/Espresso#onView(org.hamcrest.Matcher%3Candroid.view.View%3E)), Espresso waits to perform the corresponding UI action or assertion until the following synchronization conditions are met:

- The message queue doesn't have any messages that Espresso needs to immediately process.
- There are no instances of[AsyncTask](https://developer.android.com/reference/android/os/AsyncTask)currently executing a task.
- All developer-defined[idling resources](https://developer.android.com/training/testing/espresso/idling-resource)are idle.

By performing these checks, Espresso substantially increases the likelihood that only one UI action or assertion can occur at any given time. This capability gives you more reliable and dependable test results.

## Packages

- `espresso-core`- Contains core and basic`View`matchers, actions, and assertions. See[Basics](https://developer.android.com/training/testing/espresso/basics)and[Recipes](https://developer.android.com/training/testing/espresso/recipes).
- [`espresso-web`](https://developer.android.com/training/testing/espresso/web)- Contains resources for`WebView`support.
- [`espresso-idling-resource`](https://developer.android.com/training/testing/espresso/idling-resource)- Espresso's mechanism for synchronization with background jobs.
- `espresso-contrib`- External contributions that contain`DatePicker`,`RecyclerView`and`Drawer`actions, accessibility checks, and`CountingIdlingResource`.
- [`espresso-intents`](https://developer.android.com/training/testing/espresso/intents)- Extension to validate and stub intents for hermetic testing.
- `espresso-remote`- Location of Espresso's[multi-process](https://developer.android.com/training/testing/espresso/multiprocess)functionality.

You can learn more about the latest versions by reading the[release notes](https://developer.android.com/topic/libraries/testing-support-library/release-notes).

## Additional resources

For more information about using Espresso in Android tests, consult the following resources.

### Samples

- [Espresso Code Samples](https://github.com/googlesamples/android-testing)includes a full selection of Espresso samples.
- [BasicSample](https://github.com/android/testing-samples/tree/main/ui/espresso/BasicSample): Basic Espresso sample.
- [(more...)](https://developer.android.com/training/testing/espresso/additional-resources#samples)