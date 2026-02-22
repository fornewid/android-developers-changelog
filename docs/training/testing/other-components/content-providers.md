---
title: https://developer.android.com/training/testing/other-components/content-providers
url: https://developer.android.com/training/testing/other-components/content-providers
source: md.txt
---

# Test content providers

If you are implementing a[content provider](https://developer.android.com/guide/topics/providers/content-providers)to store and retrieve data or to make data accessible to other apps, you should test your provider to ensure that it doesn't behave in an unexpected way. This lesson describes how to test public content providers, and is also applicable to providers that you keep private to your own app.

## Create integration tests for content providers

Content providers let you access actual user data, so it's important to ensure that you test the content provider in an isolated testing environment. This approach allows you to only run against data dependencies set explicitly in the test case. It also means that your tests do not modify actual user data. For example, you should avoid writing a test that fails because there was data left over from a previous test. Similarly, your test should avoid adding or deleting actual contact information in a provider.
| **Note:** This document focuses on[`ProviderTestCase2`](https://developer.android.com/reference/android/test/ProviderTestCase2)which is being replaced by the experimental[`ProviderTestRule`](https://developer.android.com/reference/androidx/test/rule/provider/ProviderTestRule).

To test your content provider in isolation, use the`ProviderTestCase2`class. This class allows you to use Android mock object classes such as[`IsolatedContext`](https://developer.android.com/reference/android/test/IsolatedContext)and[`MockContentResolver`](https://developer.android.com/reference/android/test/mock/MockContentResolver)to access file and database information without affecting the actual user data.

Your integration test should be written as a JUnit 4 test class. To learn more about creating JUnit 4 test classes and using JUnit 4 assertions, see[Create a Local Unit Test Class](https://developer.android.com/training/testing/local-tests#test-class).

To create an integration test for your content provider, you must perform these steps:

1. Create your test class as a subclass of`ProviderTestCase2`.
2. Specify the[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner)class that[AndroidX Test](https://developer.android.com/training/testing)provides as your default test runner.
3. Set the[`Context`](https://developer.android.com/reference/android/content/Context)object from the`ApplicationProvider`class. See the snippet below for an example.

### Kotlin

```kotlin
@Throws(Exception::class)
override fun setUp() {
  super.setUp()
  context = ApplicationProvider.getApplicationContext<Context>()
}
```

### Java

```java
@Override
protected void setUp() throws Exception {
  super.setUp();
  setContext(ApplicationProvider.getApplicationContext());
}
```

### How ProviderTestCase2 works

You test a provider with a subclass of`ProviderTestCase2`. This base class extends[`AndroidTestCase`](https://developer.android.com/reference/android/test/AndroidTestCase), so it provides the JUnit testing framework as well as Android-specific methods for testing application permissions. The most important feature of this class is its initialization, which creates the isolated test environment.

#### Initialization

The initialization is done in the constructor for`ProviderTestCase2`, which subclasses call in their own constructors. The`ProviderTestCase2`constructor creates an`IsolatedContext`object that allows file and database operations but stubs out other interactions with the Android system. The file and database operations themselves take place in a directory that is local to the device or emulator and has a special prefix.

The constructor then creates a`MockContentResolver`to use as the resolver for the test.

Lastly, the constructor creates an instance of the provider under test. This is a normal[`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider)object, but it takes all of its environment information from the`IsolatedContext`, so it is restricted to working in the isolated test environment. All of the tests done in the test case class run against this isolated object.

You run integration tests for content providers the same way as instrumented unit tests.

## What to test

Here are some specific guidelines for testing content providers.

- **Test with resolver methods** : Even though you can instantiate a provider object in`ProviderTestCase2`, you should always test with a resolver object using the appropriate URI. Doing so ensures that you are testing the provider by performing the same interaction that a regular application would use.
- **Test a public provider as a contract** : If you intend your provider to be public and available to other applications, you should test it as a contract. Some examples of how to do so are as follows:
  - Test with constants that your provider publicly exposes. For example, look for constants that refer to column names in one of the provider's data tables. These should always be constants publicly defined by the provider.
  - Test all the URIs that your provider offers. Your provider may offer several URIs, each one referring to a different aspect of the data.
  - Test invalid URIs. Your unit tests should deliberately call the provider with an invalid URI, and look for errors. A good provider design is to throw an`IllegalArgumentException`for invalid URIs.
- **Test the standard provider interactions** : Most providers offer six access methods:`query()`,`insert()`,`delete()`,`update()`,`getType()`, and`onCreate()`. Your tests should verify that all of these methods work.
- **Test business logic**: If the content provider implements business logic, you should test it. Business logic includes handling of invalid values, financial or arithmetic calculations, elimination, or combining of duplicates.