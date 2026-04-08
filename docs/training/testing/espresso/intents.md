---
title: https://developer.android.com/training/testing/espresso/intents
url: https://developer.android.com/training/testing/espresso/intents
source: md.txt
---

Espresso-Intents is an extension to Espresso, which enables validation and
stubbing of [intents](https://developer.android.com/reference/android/content/Intent) sent out by the
application under test. It's like [Mockito](http://site.mockito.org), but for Android Intents.

If your app delegates functionality to other apps or the platform, you can use
Espresso-Intents to focus on your own app's logic while assuming that other apps
or the platform will function correctly. With Espresso-Intents, you can match
and validate your outgoing intents or even provide stub responses in place of
actual intent responses.

## Include Espresso-Intents in your project

In your app's `app/build.gradle` file, add the following line inside
`dependencies`:

### Groovy

```groovy
androidTestImplementation 'androidx.test.espresso:espresso-intents:3.6.1'
```

### Kotlin

```kotlin
androidTestImplementation('androidx.test.espresso:espresso-intents:3.6.1')
```

Espresso-Intents is only compatible with Espresso 2.1+ and version 0.3+ of
Android testing libraries, so make sure you update those lines as well:

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

## Write test rules

Before writing an Espresso-Intents test, set up an `IntentsTestRule`. This is an
extension of the class `ActivityTestRule` and makes it easy to use
Espresso-Intents APIs in functional UI tests. An `IntentsTestRule` initializes
Espresso-Intents before each test annotated with `@Test` and releases
Espresso-Intents after each test run.

The following code snippet is an example of an `IntentsTestRule`:

### Kotlin

```kotlin
@get:Rule
val intentsTestRule = IntentsTestRule(MyActivity::class.java)
```

### Java

```java
@Rule
public IntentsTestRule<MyActivity> intentsTestRule =
    new IntentsTestRule<>(MyActivity.class);
```

## Match

Espresso-Intents provides the ability to intercept outgoing intents based on
certain matching criteria, which are defined using Hamcrest Matchers. Hamcrest
allows you to:

- **Use an existing intent matcher:** Easiest option, which should almost always be preferred.
- **Implement your own intent matcher:** Most flexible option. More details are available in the section entitled "Writing custom matchers" within the [Hamcrest tutorial](https://code.google.com/archive/p/hamcrest/wikis/Tutorial.wiki).

Espresso-Intents offers the [`intended()`](https://developer.android.com/reference/androidx/test/espresso/intent/Intents#intended(org.hamcrest.Matcher%3Candroid.content.Intent%3E,%20androidx.test.espresso.intent.VerificationMode))
and [`intending()`](https://developer.android.com/reference/androidx/test/espresso/intent/Intents#intending(org.hamcrest.Matcher%3Candroid.content.Intent%3E)) methods for intent validation and
stubbing, respectively. Both take a Hamcrest `Matcher<Intent>` object as an
argument.

The following code snippet shows intent validation that uses existing intent
matchers that matches an outgoing intent that starts a browser:

### Kotlin

```kotlin
assertThat(intent).hasAction(Intent.ACTION_VIEW)
assertThat(intent).categories().containsExactly(Intent.CATEGORY_BROWSABLE)
assertThat(intent).hasData(Uri.parse("www.google.com"))
assertThat(intent).extras().containsKey("key1")
assertThat(intent).extras().string("key1").isEqualTo("value1")
assertThat(intent).extras().containsKey("key2")
assertThat(intent).extras().string("key2").isEqualTo("value2")
```

### Java

```java
assertThat(intent).hasAction(Intent.ACTION_VIEW);
assertThat(intent).categories().containsExactly(Intent.CATEGORY_BROWSABLE);
assertThat(intent).hasData(Uri.parse("www.google.com"));
assertThat(intent).extras().containsKey("key1");
assertThat(intent).extras().string("key1").isEqualTo("value1");
assertThat(intent).extras().containsKey("key2");
assertThat(intent).extras().string("key2").isEqualTo("value2");
```

## Validate intents

Espresso-Intents records all intents that attempt to launch activities from the
application under test. Using the `intended()` method, which is similar to
`Mockito.verify()`, you can assert that a given intent has been seen. However,
Espresso-Intents doesn't stub out responses to intents unless you [explicitly configure](https://developer.android.com/training/testing/espresso/intents#stubbing)
it to do so.

The following code snippet is an example test that validates, but doesn't stub
out responses to, an outgoing intent that launches an external "phone" activity:

### Kotlin

```kotlin
@Test fun validateIntentSentToPackage() {
    // User action that results in an external "phone" activity being launched.
    user.clickOnView(system.getView(R.id.callButton))

    // Using a canned RecordedIntentMatcher to validate that an intent resolving
    // to the "phone" activity has been sent.
    intended(toPackage("com.android.phone"))
}
```

### Java

```java
@Test
public void validateIntentSentToPackage() {
    // User action that results in an external "phone" activity being launched.
    user.clickOnView(system.getView(R.id.callButton));

    // Using a canned RecordedIntentMatcher to validate that an intent resolving
    // to the "phone" activity has been sent.
    intended(toPackage("com.android.phone"));
}
```

## Stubbing

Using the `intending()` method, which is similar to `Mockito.when()`, you can
provide a stub response for activities that are launched with
`startActivityForResult()`. This is particularly useful for external activities
because you cannot manipulate the user interface of an external activity nor
control the `ActivityResult` returned to the activity under test.

The following code snippets implement an example
`activityResult_DisplaysContactsPhoneNumber()` test, which verifies that when a
user launches a "contact" activity in the app under test, the contact phone
number is displayed:

1. Build the result to return when a particular activity is launched. The
   example test intercepts all Intents sent to "contacts" and stubs out their
   responses with a valid `ActivityResult`, using the result code
   `RESULT_OK`

   ### Kotlin

   ```kotlin
   val resultData = Intent()
   val phoneNumber = "123-345-6789"
   resultData.putExtra("phone", phoneNumber)
   val result = Instrumentation.ActivityResult(Activity.RESULT_OK, resultData)
   ```

   ### Java

   ```java
   Intent resultData = new Intent();
   String phoneNumber = "123-345-6789";
   resultData.putExtra("phone", phoneNumber);
   ActivityResult result =
       new ActivityResult(Activity.RESULT_OK, resultData);
   ```
2. Instruct Espresso to provide the stub result object in response to all
   invocations of the "contacts" intent:

   ### Kotlin

   ```kotlin
   intending(toPackage("com.android.contacts")).respondWith(result)
   ```

   ### Java

   ```java
   intending(toPackage("com.android.contacts")).respondWith(result);
   ```
3. Verify that the action used to launch the activity produces the expected
   stub result. In this case, the example test checks that the phone number
   "123-345-6789" is returned and
   displayed when the "contacts activity" is launched:

   ### Kotlin

   ```kotlin
   onView(withId(R.id.pickButton)).perform(click())
   onView(withId(R.id.phoneNumber)).check(matches(withText(phoneNumber)))
   ```

   ### Java

   ```java
   onView(withId(R.id.pickButton)).perform(click());
   onView(withId(R.id.phoneNumber)).check(matches(withText(phoneNumber)));
   ```

Here is the complete `activityResult_DisplaysContactsPhoneNumber()` test:

### Kotlin

```kotlin
@Test fun activityResult_DisplaysContactsPhoneNumber() {
    // Build the result to return when the activity is launched.
    val resultData = Intent()
    val phoneNumber = "123-345-6789"
    resultData.putExtra("phone", phoneNumber)
    val result = Instrumentation.ActivityResult(Activity.RESULT_OK, resultData)

    // Set up result stubbing when an intent sent to "contacts" is seen.
    intending(toPackage("com.android.contacts")).respondWith(result)

    // User action that results in "contacts" activity being launched.
    // Launching activity expects phoneNumber to be returned and displayed.
    onView(withId(R.id.pickButton)).perform(click())

    // Assert that the data we set up above is shown.
    onView(withId(R.id.phoneNumber)).check(matches(withText(phoneNumber)))
}
```

### Java

```java
@Test
public void activityResult_DisplaysContactsPhoneNumber() {
    // Build the result to return when the activity is launched.
    Intent resultData = new Intent();
    String phoneNumber = "123-345-6789";
    resultData.putExtra("phone", phoneNumber);
    ActivityResult result =
        new ActivityResult(Activity.RESULT_OK, resultData);

    // Set up result stubbing when an intent sent to "contacts" is seen.
    intending(toPackage("com.android.contacts")).respondWith(result);

    // User action that results in "contacts" activity being launched.
    // Launching activity expects phoneNumber to be returned and displayed.
    onView(withId(R.id.pickButton)).perform(click());

    // Assert that the data we set up above is shown.
    onView(withId(R.id.phoneNumber)).check(matches(withText(phoneNumber)));
}
```

## Additional resources

For more information about using Espresso-Intents in Android tests, consult
the following resources.

### Samples

- [IntentsBasicSample](https://github.com/android/testing-samples/tree/main/ui/espresso/IntentsBasicSample): Basic usage of `intended()` and `intending()`.
- [IntentsAdvancedSample](https://github.com/android/testing-samples/tree/main/ui/espresso/IntentsAdvancedSample): Simulates a user fetching a bitmap using the camera.