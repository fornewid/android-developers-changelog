---
title: Test your service  |  Test your app on Android  |  Android Developers
url: https://developer.android.com/training/testing/other-components/services
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Test your app on Android](https://developer.android.com/training/testing)

# Test your service Stay organized with collections Save and categorize content based on your preferences.




If you are implementing a local [`Service`](/reference/android/app/Service) as a component of your app, you
can create [instrumented tests](/training/testing/unit-testing/instrumented-unit-tests) to verify that its behavior is correct.

[AndroidX Test](/training/testing) provides an API for testing your `Service` objects in
isolation. The [`ServiceTestRule`](/reference/androidx/test/rule/ServiceTestRule) class is a JUnit 4 rule that starts your
service before your unit test methods run, and shuts down the service after
tests complete. To learn more about JUnit 4 rules, see the [JUnit
documentation](https://github.com/junit-team/junit/wiki/Rules).

**Note:** The `ServiceTestRule` class does not support testing of
[`IntentService`](/reference/android/app/IntentService) objects. If you need to test an `IntentService`
object, you should encapsulate the logic in a separate class and create a
corresponding unit test instead.

## Set up your testing environment

Before building your integration test for the service, make sure to configure
your project for instrumented tests, as described in [Set up project for
AndroidX Test](/training/testing/set-up-project).

## Create an integration test for services

Your integration test should be written as a JUnit 4 test class. To learn more
about creating JUnit 4 test classes and using JUnit 4 assertion methods, see
[Create an instrumented test class](/training/testing/unit-testing/instrumented-unit-tests#create-instrumented).

Create a `ServiceTestRule` instance in your test by using the `@Rule`
annotation.

### Kotlin

```
@get:Rule
val serviceRule = ServiceTestRule()
```

### Java

```
@Rule
public final ServiceTestRule serviceRule = new ServiceTestRule();
```

The following example shows how you might implement an integration test for a
service. The test method `testWithBoundService()` verifies that the app binds
successfully to a local service and that the service interface behaves
correctly.

### Kotlin

```
@Test
@Throws(TimeoutException::class)
fun testWithBoundService() {
  // Create the service Intent.
  val serviceIntent = Intent(
      ApplicationProvider.getApplicationContext<Context>(),
      LocalService::class.java
  ).apply {
    // Data can be passed to the service via the Intent.
    putExtra(SEED_KEY, 42L)
  }

  // Bind the service and grab a reference to the binder.
  val binder: IBinder = serviceRule.bindService(serviceIntent)

  // Get the reference to the service, or you can call
  // public methods on the binder directly.
  val service: LocalService = (binder as LocalService.LocalBinder).getService()

  // Verify that the service is working correctly.
  assertThat(service.getRandomInt(), `is`(any(Int::class.java)))
}
```

### Java

```
@Test
public void testWithBoundService() throws TimeoutException {
  // Create the service Intent.
  Intent serviceIntent =
      new Intent(ApplicationProvider.getApplicationContext(),
        LocalService.class);

  // Data can be passed to the service via the Intent.
  serviceIntent.putExtra(LocalService.SEED_KEY, 42L);

  // Bind the service and grab a reference to the binder.
  IBinder binder = serviceRule.bindService(serviceIntent);

  // Get the reference to the service, or you can call
  // public methods on the binder directly.
  LocalService service =
      ((LocalService.LocalBinder) binder).getService();

  // Verify that the service is working correctly.
  assertThat(service.getRandomInt()).isAssignableTo(Integer.class);
}
```

## Additional resources

To learn more about this topic, consult the following additional resources.

### Samples

* [Service Test Code Samples](https://github.com/android/testing-samples/tree/main/integration/ServiceTestRuleSample)