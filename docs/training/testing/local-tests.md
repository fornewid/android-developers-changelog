---
title: https://developer.android.com/training/testing/local-tests
url: https://developer.android.com/training/testing/local-tests
source: md.txt
---

# Build local unit tests

A*local*test runs directly on your own workstation, rather than an Android device or emulator. As such, it uses your local Java Virtual Machine (JVM), rather than an Android device to run tests. Local tests enable you to evaluate your app's logic more quickly. However, not being able to interact with the Android framework creates a limitation in the types of tests you can run.

A*unit* test verifies the behavior of a small section of code, the*unit under test*. It does so by executing that code and checking the result.

Unit tests are usually simple but their setup can be problematic when the*unit under test*is not designed with testability in mind:

- The code that you want to verify needs to be*accessible*from a test. For example, you can't test a private method directly. Instead, you test the class using its public APIs.
- In order to run unit tests in*isolation* , the dependencies of the unit under tests must be replaced by components that you control, such as fakes or other[test doubles](https://developer.android.com/training/testing/fundamentals/test-doubles). This is especially problematic if your code depends on the Android framework.

To learn about common unit testing strategies in Android, read[What to test](https://developer.android.com/training/testing/fundamentals/what-to-test).

## Local tests location

By default, the source files for local unit tests are placed in`module-name/src/test/`. This directory already exists when you create a new project using Android Studio.

## Adding testing dependencies

You also need to configure the testing dependencies for your project to use the standard APIs provided by the[JUnit](https://junit.org/)testing framework.

To do so, open your app's module's`build.gradle`file and specify the following libraries as dependencies. Use the`testImplementation`function to indicate that they apply to the local test source set, and not the application:  

    dependencies {
      // Required -- JUnit 4 framework
      testImplementation "junit:junit:$jUnitVersion"
      // Optional -- Robolectric environment
      testImplementation "androidx.test:core:$androidXTestVersion"
      // Optional -- Mockito framework
      testImplementation "org.mockito:mockito-core:$mockitoVersion"
      // Optional -- mockito-kotlin
      testImplementation "org.mockito.kotlin:mockito-kotlin:$mockitoKotlinVersion"
      // Optional -- Mockk framework
      testImplementation "io.mockk:mockk:$mockkVersion"
    }

| **Note:** `testImplementation`adds dependencies for local tests and`androidTestImplementation`adds dependencies for Instrumented tests.

## Create a local unit test class

You write your local unit test class as a[JUnit 4](https://junit.org/junit4/)test class.

To do so, create a class that contains one or more test methods, usually in`module-name/src/test/`. A test method begins with the`@Test`annotation and contains the code to exercise and verify a single aspect of the component that you want to test.

The following example demonstrates how to implement a local unit test class. The test method`emailValidator_correctEmailSimple_returnsTrue()`attempts to verify`isValidEmail()`,which is a method within the app. The test function will return true if`isValidEmail()`also returns true.  

### Kotlin

```kotlin
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class EmailValidatorTest {
  @Test fun emailValidator_CorrectEmailSimple_ReturnsTrue() {
    assertTrue(EmailValidator.isValidEmail("name@email.com"))
  }

}
```

### Java

```java
import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

class EmailValidatorTest {
  @Test
  public void emailValidator_CorrectEmailSimple_ReturnsTrue() {
    assertTrue(EmailValidator.isValidEmail("name@email.com"));
  }
}
```

You should create readable tests that evaluate whether the components in your app return the expected results. We recommend you use an assertions library such as[junit.Assert](http://junit.org/javadoc/latest/org/junit/Assert.html),[Hamcrest](https://github.com/hamcrest), or[Truth](https://truth.dev/). The snippet above is an example of how to use`junit.Assert`.

## Mockable Android library

When you execute local unit tests, the[Android Gradle Plug-in](https://developer.android.com/studio/releases/gradle-plugin)includes a library that contains all the APIs of the Android framework, correct to the version used in your project. The library holds all the public methods and classes of those APIs, but the code inside the methods has been removed. If any of the methods are accessed, the test throws an exception.

This allows local tests to be built when referencing classes in the Android framework such as`Context`. More importantly, it allows you to use a mocking framework with Android classes.
| **Note:** A mock is a type of test double that has expectations about its interactions, and whose behavior you can define. See[Test doubles](https://developer.android.com/training/testing/fundamentals/test-doubles).

### Mocking Android dependencies

A typical problem is to find that a class is using a string resource. You can obtain string resources by calling the`getString()`method in the`Context`class. However, a local test can't use`Context`or any of its methods as they belong to the Android framework. Ideally, the call to`getString()`would be moved out from the class, but this is not always practical. The solution is to create a mock or a stub of`Context`that always returns the same value when its`getString()`method is invoked.

With the Mockable Android library and mocking frameworks such as[Mockito](https://github.com/mockito/mockito)or[MockK](https://mockk.io/), you can program the behavior of mocks of the Android classes in your unit tests.

To add a mock object to your local unit test using Mockito, follow this programming model:

1. Include the Mockito library dependency in your`build.gradle`file, as described in[Set up your testing environment](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup#add-gradle).
2. At the beginning of your unit test class definition, add the`@RunWith(MockitoJUnitRunner.class)`annotation. This annotation tells the Mockito test runner to validate that your usage of the framework is correct and simplifies the initialization of your mock objects.
3. To create a mock object for an Android dependency, add the`@Mock`annotation before the field declaration.
4. To stub the behavior of the dependency, you can specify a condition and return value when the condition is met by using the`when()`and`thenReturn()`methods.

The following example shows how you might create a unit test that uses a mock[`Context`](https://developer.android.com/reference/android/content/Context)object in Kotlin created with[Mockito-Kotlin](https://github.com/mockito/mockito-kotlin).  

    import android.content.Context
    import org.junit.Assert.assertEquals
    import org.junit.Test
    import org.junit.runner.RunWith
    import org.mockito.Mock
    import org.mockito.junit.MockitoJUnitRunner
    import org.mockito.kotlin.doReturn
    import org.mockito.kotlin.mock

    private const val FAKE_STRING = "HELLO WORLD"

    @RunWith(MockitoJUnitRunner::class)
    class MockedContextTest {

      @Mock
      private lateinit var mockContext: Context

      @Test
      fun readStringFromContext_LocalizedString() {
        // Given a mocked Context injected into the object under test...
        val mockContext = mock<Context> {
            on { getString(R.string.name_label) } doReturn FAKE_STRING
        }

        val myObjectUnderTest = ClassUnderTest(mockContext)

        // ...when the string is returned from the object under test...
        val result: String = myObjectUnderTest.getName()

        // ...then the result should be the expected one.
        assertEquals(result, FAKE_STRING)
      }
    }

To learn more about using the Mockito framework, see the[Mockito API reference](https://github.com/mockito/mockito-kotlin)and the`SharedPreferencesHelperTest`class in the[sample code](https://github.com/android/testing-samples/tree/main/unit/BasicSample). Also try the[Android Testing Codelab](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-basics).
| **Caution:** Complex mocks should be avoided. Instead, you can use different types of test doubles such as fakes, or[Robolectric](http://robolectric.org/)shadows if they are Android classes. Also, consider using the real implementation of the dependency in an instrumentation test.

### Error: "Method ... not mocked"

The Mockable Android library throws an exception if you try to access any of its methods with the`Error: "Method ... not mocked`message.

If the exceptions thrown are problematic for your tests, you can change the behavior so that methods instead return either null or zero, depending on the return type. To do so, add the following configuration in your project's top-level`build.gradle`file in Groovy:  

    android {
      ...
      testOptions {
        unitTests.returnDefaultValues = true
      }

| **Caution:** Take care when setting the`returnDefaultValues`property to`true`. The null/zero return values can introduce regressions to your tests, which are hard to debug and might allow failing tests to pass. Only use it as a last resort.