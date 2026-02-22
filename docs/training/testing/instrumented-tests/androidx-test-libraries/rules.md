---
title: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/rules
url: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/rules
source: md.txt
---

# JUnit4 rules with AndroidX Test

AndroidX Test includes a set of[JUnit rules](https://github.com/junit-team/junit4/wiki/Rules)to be used with the[AndroidJUnitRunner](https://developer.android.com/training/testing/junit-runner). JUnit rules provide more flexibility and reduce the boilerplate code required in tests. For example, they can be used to start a specific activity.

## ActivityScenarioRule

This rule provides functional testing of a single activity. The rule launches the chosen activity before each test annotated with`@Test`, as well as before any method annotated with`@Before`. The rule terminates the activity after the test completes and all methods annotated with`@After`finish. To access the given activity in your test logic, provide a callback runnable to`ActivityScenarioRule.getScenario().onActivity()`.

The following code snippet demonstrates how to incorporate`ActivityScenarioRule`into your testing logic:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class.java)
@LargeTest
class MyClassTest {
  @get:Rule
  val activityRule = ActivityScenarioRule(MyClass::class.java)

  @Test fun myClassMethod_ReturnsTrue() {
    activityRule.scenario.onActivity { ... } // Optionally, access the activity.
   }
}
```

### Java

```java
public class MyClassTest {
    @Rule
    public ActivityScenarioRule&lt;MyClass&gt; activityRule =
            new ActivityScenarioRule(MyClass.class);

    @Test
    public void myClassMethod_ReturnsTrue() { ... }
}
```
| **Note:** in order to test fragments in isolation, you can use the`FragmentScenario`class from the[AndroidX fragment-testing library](https://developer.android.com/guide/fragments/test).

## ServiceTestRule

This rule provides a simplified mechanism to launch your service before the tests and shut it down before and after. You can start or bind the service with one of the helper methods. It automatically stops or unbinds after the test completes and any methods annotated with`@After`have finished.
**Note:** This rule doesn't support`IntentService`. This is because the service is destroyed when`IntentService.onHandleIntent(Intent)`finishes all outstanding commands, so there is no guarantee to establish a successful connection in a timely manner.  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class.java)
@MediumTest
class MyServiceTest {
  @get:Rule
  val serviceRule = ServiceTestRule()

  @Test fun testWithStartedService() {
    serviceRule.startService(
      Intent(ApplicationProvider.getApplicationContext<Context>(),
      MyService::class.java))
    // Add your test code here.
  }

  @Test fun testWithBoundService() {
    val binder = serviceRule.bindService(
      Intent(ApplicationProvider.getApplicationContext(),
      MyService::class.java))
    val service = (binder as MyService.LocalBinder).service
    assertThat(service.doSomethingToReturnTrue()).isTrue()
  }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@MediumTest
public class MyServiceTest {
    @Rule
    public final ServiceTestRule serviceRule = new ServiceTestRule();

    @Test
    public void testWithStartedService() {
        serviceRule.startService(
                new Intent(ApplicationProvider.getApplicationContext(),
                MyService.class));
        // Add your test code here.
    }

    @Test
    public void testWithBoundService() {
        IBinder binder = serviceRule.bindService(
                new Intent(ApplicationProvider.getApplicationContext(),
                MyService.class));
        MyService service = ((MyService.LocalBinder) binder).getService();
        assertThat(service.doSomethingToReturnTrue()).isTrue();
    }
}
```

## Additional resources

For more information about using JUnit rules in Android tests, consult the following resources.

### Documentation

- [Test your fragments](https://developer.android.com/guide/fragments/test)guide, to test fragments in isolation.
- [Testing your Compose layout](https://developer.android.com/jetpack/compose/testing), to test UIs made with Compose.

### Samples

- [BasicSample](https://github.com/android/testing-samples/tree/main/ui/espresso/BasicSample): Simple usage of`ActivityScenarioRule`.