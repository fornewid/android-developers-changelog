---
title: https://developer.android.com/training/dependency-injection/hilt-testing
url: https://developer.android.com/training/dependency-injection/hilt-testing
source: md.txt
---

One of the benefits of using dependency injection frameworks like Hilt is that
it makes testing your code easier.

## Unit tests

Hilt isn't necessary for unit tests, since when testing a class that uses
constructor injection, you don't need to use Hilt to instantiate that class.
Instead, you can directly call a class constructor by passing in fake or mock
dependencies, just as you would if the constructor weren't annotated:  

### Kotlin

```kotlin
@ActivityScoped
class AnalyticsAdapter @Inject constructor(
  private val service: AnalyticsService
) { ... }

class AnalyticsAdapterTest {

  @Test
  fun `Happy path`() {
    // You don't need Hilt to create an instance of AnalyticsAdapter.
    // You can pass a fake or mock AnalyticsService.
    val adapter = AnalyticsAdapter(fakeAnalyticsService)
    assertEquals(...)
  }
}
```

### Java

```java
@ActivityScope
public class AnalyticsAdapter {

  private final AnalyticsService analyticsService;

  @Inject
  AnalyticsAdapter(AnalyticsService analyticsService) {
    this.analyticsService = analyticsService;
  }
}

public final class AnalyticsAdapterTest {

  @Test
  public void happyPath() {
    // You don't need Hilt to create an instance of AnalyticsAdapter.
    // You can pass a fake or mock AnalyticsService.
    AnalyticsAdapter adapter = new AnalyticsAdapter(fakeAnalyticsService);
    assertEquals(...);
  }
}
```

## End-to-end tests

For integration tests, Hilt injects dependencies as it would in your production
code. Testing with Hilt requires no maintenance because Hilt automatically
generates a new set of components for each test.

### Adding testing dependencies

To use Hilt in your tests, include the `hilt-android-testing` dependency in your
project:  

### Groovy

```groovy
dependencies {
    // For Robolectric tests.
    testImplementation 'com.google.dagger:hilt-android-testing:2.57.1'
    // ...with Kotlin.
    kaptTest 'com.google.dagger:hilt-android-compiler:2.57.1'
    // ...with Java.
    testAnnotationProcessor 'com.google.dagger:hilt-android-compiler:2.57.1'


    // For instrumented tests.
    androidTestImplementation 'com.google.dagger:hilt-android-testing:2.57.1'
    // ...with Kotlin.
    kaptAndroidTest 'com.google.dagger:hilt-android-compiler:2.57.1'
    // ...with Java.
    androidTestAnnotationProcessor 'com.google.dagger:hilt-android-compiler:2.57.1'
}
```

### Kotlin

```kotlin
dependencies {
    // For Robolectric tests.
    testImplementation("com.google.dagger:hilt-android-testing:2.57.1")
    // ...with Kotlin.
    kaptTest("com.google.dagger:hilt-android-compiler:2.57.1")
    // ...with Java.
    testAnnotationProcessor("com.google.dagger:hilt-android-compiler:2.57.1")


    // For instrumented tests.
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.57.1")
    // ...with Kotlin.
    kaptAndroidTest("com.google.dagger:hilt-android-compiler:2.57.1")
    // ...with Java.
    androidTestAnnotationProcessor("com.google.dagger:hilt-android-compiler:2.57.1")
}
```
| **Note:** If you use [Jetpack
| integrations](https://developer.android.com/training/dependency-injection/hilt-jetpack), you must also include the annotation processors for the integrated libraries with `kaptTest` or `kaptAndroidTest` for Kotlin, or with `testAnnotationProcessor` or `androidTestAnnotationProcessor` for Java.

### UI test setup

You must annotate any UI test that uses Hilt with `@HiltAndroidTest`. This
annotation is responsible for generating the Hilt components for each test.

Also, you need to add the `HiltAndroidRule` to the test class. It manages the
components' state and is used to perform injection on your test:  

### Kotlin

```kotlin
@HiltAndroidTest
class SettingsActivityTest {

  @get:Rule
  var hiltRule = HiltAndroidRule(this)

  // UI tests here.
}
```

### Java

```java
@HiltAndroidTest
public final class SettingsActivityTest {

  @Rule
  public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

  // UI tests here.
}
```
| **Note:** If you have other rules in your test, see [Multiple TestRule objects in
| your instrumented test](https://developer.android.com/training/dependency-injection/hilt-testing#multiple-testrules).

Next, your test needs to know about the `Application` class that Hilt
automatically generates for you.

#### Test application

You must execute instrumented tests that use Hilt in an `Application` object
that supports Hilt. The library provides `HiltTestApplication` for use in tests.
If your tests need a different base application, see [Custom application for
tests](https://developer.android.com/training/dependency-injection/hilt-testing#custom-application).

You must set your test application to run in your [instrumented
tests](https://developer.android.com/training/testing/ui-testing) or [Robolectric
tests](http://robolectric.org/). The following instructions aren't
specific to Hilt, but are general guidelines on how to specify a custom
application to run in tests.

##### Set the test application in instrumented tests

To use the Hilt test application in [instrumented
tests](https://developer.android.com/training/testing/ui-testing), you need to configure a new test runner.
This makes Hilt work for all of the instrumented tests in your project. Perform
the following steps:

1. Create a custom class that extends [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) in the `androidTest` folder.
2. Override the `newApplication` function and pass in the name of the generated Hilt test application.

### Kotlin

```kotlin
// A custom runner to set up the instrumented application class for tests.
class CustomTestRunner : AndroidJUnitRunner() {

    override fun newApplication(cl: ClassLoader?, name: String?, context: Context?): Application {
        return super.newApplication(cl, HiltTestApplication::class.java.name, context)
    }
}
```

### Java

```java
// A custom runner to set up the instrumented application class for tests.
public final class CustomTestRunner extends AndroidJUnitRunner {

  @Override
  public Application newApplication(ClassLoader cl, String className, Context context)
      throws ClassNotFoundException, IllegalAccessException, InstantiationException {
    return super.newApplication(cl, HiltTestApplication.class.getName(), context);
  }
}
```

Next, configure this test runner in your Gradle file as described in the
[instrumented unit test
guide](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#setup). Make sure
you use the full classpath:  

### Groovy

```groovy
android {
    defaultConfig {
        // Replace com.example.android.dagger with your class path.
        testInstrumentationRunner "com.example.android.dagger.CustomTestRunner"
    }
}
```

### Kotlin

```kotlin
android {
    defaultConfig {
        // Replace com.example.android.dagger with your class path.
        testInstrumentationRunner = "com.example.android.dagger.CustomTestRunner"
    }
}
```

##### Set the test application in Robolectric tests

If you use Robolectric to test your UI layer, you can specify which application
to use in the `robolectric.properties` file:

`application = dagger.hilt.android.testing.HiltTestApplication`

Alternatively, you can configure the application on each test individually by
using Robolectric's `@Config` annotation:  

### Kotlin

```kotlin
@HiltAndroidTest
@Config(application = HiltTestApplication::class)
class SettingsActivityTest {

  @get:Rule
  var hiltRule = HiltAndroidRule(this)

  // Robolectric tests here.
}
```

### Java

```java
@HiltAndroidTest
@Config(application = HiltTestApplication.class)
class SettingsActivityTest {

  @Rule public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

  // Robolectric tests here.
}
```

If you use an Android Gradle Plugin version lower than 4.2, enable
transforming `@AndroidEntryPoint` classes in local unit tests by applying the
following configuration in your module's `build.gradle` file:  

### Groovy

```groovy
hilt {
    enableTransformForLocalTests = true
}
```

### Kotlin

```kotlin
hilt {
    enableTransformForLocalTests = true
}
```

More information about `enableTransformForLocalTests` in the [Hilt
documentation](https://dagger.dev/hilt/gradle-setup#gradle-plugin-local-tests).

### Testing features

Once Hilt is ready to use in your tests, you can use several features to
customize the testing process.

#### Inject types in tests

To inject types into a test, use `@Inject` for field injection. To tell Hilt to
populate the `@Inject` fields, call `hiltRule.inject()`.

See the following example of an instrumented test:  

### Kotlin

```kotlin
@HiltAndroidTest
class SettingsActivityTest {

  @get:Rule
  var hiltRule = HiltAndroidRule(this)

  @Inject
  lateinit var analyticsAdapter: AnalyticsAdapter

  @Before
  fun init() {
    hiltRule.inject()
  }

  @Test
  fun `happy path`() {
    // Can already use analyticsAdapter here.
  }
}
```

### Java

```java
@HiltAndroidTest
public final class SettingsActivityTest {

  @Rule public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

  @Inject AnalyticsAdapter analyticsAdapter;

  @Before
  public void init() {
    hiltRule.inject();
  }

  @Test
  public void happyPath() {
    // Can already use analyticsAdapter here.
  }
}
```

#### Replace a binding

If you need to inject a fake or mock instance of a dependency, you need to tell
Hilt not to use the binding that it used in production code and to use a
different one instead. To replace a binding, you need to replace the module that
contains the binding with a test module that contains the bindings that you want
to use in the test.

For example, suppose your production code declares a binding for
`AnalyticsService` as follows:  

### Kotlin

```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class AnalyticsModule {

  @Singleton
  @Binds
  abstract fun bindAnalyticsService(
    analyticsServiceImpl: AnalyticsServiceImpl
  ): AnalyticsService
}
```

### Java

```java
@Module
@InstallIn(SingletonComponent.class)
public abstract class AnalyticsModule {

  @Singleton
  @Binds
  public abstract AnalyticsService bindAnalyticsService(
    AnalyticsServiceImpl analyticsServiceImpl
  );
}
```

To replace the `AnalyticsService` binding in tests, create a new Hilt module in
the `test` or `androidTest` folder with the fake dependency and annotate it
with `@TestInstallIn`. All the tests in that folder are injected with the fake
dependency instead.  

### Kotlin

```kotlin
@Module
@TestInstallIn(
    components = [SingletonComponent::class],
    replaces = [AnalyticsModule::class]
)
abstract class FakeAnalyticsModule {

  @Singleton
  @Binds
  abstract fun bindAnalyticsService(
    fakeAnalyticsService: FakeAnalyticsService
  ): AnalyticsService
}
```

### Java

```java
@Module
@TestInstallIn(
    components = SingletonComponent.class,
    replaces = AnalyticsModule.class
)
public abstract class FakeAnalyticsModule {

  @Singleton
  @Binds
  public abstract AnalyticsService bindAnalyticsService(
    FakeAnalyticsService fakeAnalyticsService
  );
}
```

#### Replace a binding in a single test

To replace a binding in a single test instead of all tests, uninstall a Hilt
module from a test using the `@UninstallModules` annotation and create a new
test module inside the test.

Following the `AnalyticsService` example from the previous version, begin by telling
Hilt to ignore the production module by using the `@UninstallModules` annotation
in the test class:  

### Kotlin

```kotlin
@UninstallModules(AnalyticsModule::class)
@HiltAndroidTest
class SettingsActivityTest { ... }
```

### Java

```java
@UninstallModules(AnalyticsModule.class)
@HiltAndroidTest
public final class SettingsActivityTest { ... }
```

Next, you must replace the binding. Create a new module within the test class
that defines the test binding:  

### Kotlin

```kotlin
@UninstallModules(AnalyticsModule::class)
@HiltAndroidTest
class SettingsActivityTest {

  @Module
  @InstallIn(SingletonComponent::class)
  abstract class TestModule {

    @Singleton
    @Binds
    abstract fun bindAnalyticsService(
      fakeAnalyticsService: FakeAnalyticsService
    ): AnalyticsService
  }

  ...
}
```

### Java

```java
@UninstallModules(AnalyticsModule.class)
@HiltAndroidTest
public final class SettingsActivityTest {

  @Module
  @InstallIn(SingletonComponent.class)
  public abstract class TestModule {

    @Singleton
    @Binds
    public abstract AnalyticsService bindAnalyticsService(
      FakeAnalyticsService fakeAnalyticsService
    );
  }
  ...
}
```

This only replaces the binding for a single test class. If you want to replace
the binding for all test classes, use the `@TestInstallIn` annotation from the
section above. Alternatively, you can put the test binding in the `test` module
for Robolectric tests, or in the `androidTest` module for instrumented tests.
The recommendation is to use `@TestInstallIn` whenever possible.
| **Warning:** You cannot uninstall modules that are not annotated with `@InstallIn`. Attempting to do so causes a compilation error.
| **Warning:** `@UninstallModules` can only uninstall `@InstallIn` modules, not `@TestInstallIn` modules. Attempting to do so causes a compilation error.
| **Note:** As Hilt creates new components for tests that use `@UninstallModules`, it can significantly impact unit test build times. Use it when necessary and prefer using `@TestInstallIn` when the bindings need to be replaced in all test classes.

#### Binding new values

Use the `@BindValue` annotation to easily bind fields in your test into the Hilt
dependency graph. Annotate a field with `@BindValue` and it will be bound under
the declared field type with any qualifiers that are present for that field.

In the `AnalyticsService` example, you can replace `AnalyticsService` with a
fake by using `@BindValue`:  

### Kotlin

```kotlin
@UninstallModules(AnalyticsModule::class)
@HiltAndroidTest
class SettingsActivityTest {

  @BindValue @JvmField
  val analyticsService: AnalyticsService = FakeAnalyticsService()

  ...
}
```

### Java

```java
@UninstallModules(AnalyticsModule.class)
@HiltAndroidTest
class SettingsActivityTest {

  @BindValue AnalyticsService analyticsService = FakeAnalyticsService();

  ...
}
```

This simplifies both replacing a binding and referencing a binding in your test
by allowing you to do both at the same time.

`@BindValue` works with qualifiers and other testing annotations. For example,
if you use testing libraries such as
[Mockito](https://site.mockito.org/), you could use it in a
Robolectric test as follows:  

### Kotlin

```kotlin
...
class SettingsActivityTest {
  ...

  @BindValue @ExampleQualifier @Mock
  lateinit var qualifiedVariable: ExampleCustomType

  // Robolectric tests here
}
```

### Java

```java
...
class SettingsActivityTest {
  ...
  @BindValue @ExampleQualifier @Mock ExampleCustomType qualifiedVariable;

  // Robolectric tests here
}
```

If you need to add a [multibinding](https://dagger.dev/dev-guide/multibindings),
you can use the `@BindValueIntoSet` and `@BindValueIntoMap` annotations in place
of `@BindValue`. `@BindValueIntoMap` requires you to also annotate the field
with a map key annotation.

## Special cases

Hilt also provides features to support nonstandard use cases.

### Custom application for tests

If you cannot use `HiltTestApplication` because your test application needs to
extend another application, annotate a new class or interface with
`@CustomTestApplication`, passing in the value of the base class you want the
generated Hilt application to extend.

`@CustomTestApplication` will generate an `Application` class ready for testing
with Hilt that extends the application you passed as a parameter.  

### Kotlin

```kotlin
@CustomTestApplication(BaseApplication::class)
interface HiltTestApplication
```

### Java

```java
@CustomTestApplication(BaseApplication.class)
interface HiltTestApplication { }
```

In the example, Hilt generates an `Application` named
`HiltTestApplication_Application` that extends the `BaseApplication` class. In
general, the name of the generated application is the name of the annotated
class appended with `_Application`. You must set the generated Hilt test
application to run in your [instrumented tests](https://developer.android.com/training/testing/ui-testing) or
[Robolectric tests](http://robolectric.org/) as described in [Test
application](https://developer.android.com/training/dependency-injection/hilt-testing#test-application).
| **Note:** Because `HiltTestApplication_Application` is code that Hilt generates at runtime, the IDE might highlight it in red until you run your tests.

### Multiple TestRule objects in your instrumented test

If you have other `TestRule` objects in your test, there are multiple ways to
ensure that all of the rules work together.

You can wrap the rules together as follows:  

### Kotlin

```kotlin
@HiltAndroidTest
class SettingsActivityTest {

  @get:Rule
  var rule = RuleChain.outerRule(HiltAndroidRule(this)).
        around(SettingsActivityTestRule(...))

  // UI tests here.
}
```

### Java

```java
@HiltAndroidTest
public final class SettingsActivityTest {

  @Rule public RuleChain rule = RuleChain.outerRule(new HiltAndroidRule(this))
        .around(new SettingsActivityTestRule(...));

  // UI tests here.
}
```

Alternatively, you can use both rules at the same level as long as the
`HiltAndroidRule` executes first. Specify the execution order using the
`order` attribute in the `@Rule` annotation. This only works in JUnit version
4.13 or higher:  

### Kotlin

```kotlin
@HiltAndroidTest
class SettingsActivityTest {

  @get:Rule(order = 0)
  var hiltRule = HiltAndroidRule(this)

  @get:Rule(order = 1)
  var settingsActivityTestRule = SettingsActivityTestRule(...)

  // UI tests here.
}
```

### Java

```java
@HiltAndroidTest
public final class SettingsActivityTest {

  @Rule(order = 0)
  public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

  @Rule(order = 1)
  public SettingsActivityTestRule settingsActivityTestRule = new SettingsActivityTestRule(...);

  // UI tests here.
}
```

### launchFragmentInContainer

It is not possible to use `launchFragmentInContainer` from the
`androidx.fragment:fragment-testing` library with Hilt, because it relies on an
activity that is not annotated with `@AndroidEntryPoint`.

Use the
[`launchFragmentInHiltContainer`](https://github.com/android/architecture-samples/blob/views-hilt/app/src/androidTest/java/com/example/android/architecture/blueprints/todoapp/HiltExt.kt#L37)
code from the
[`architecture-samples`](https://github.com/android/architecture-samples) GitHub
repository instead.

### Use an entry point before the singleton component is available

The `@EarlyEntryPoint` annotation provides an escape hatch when a Hilt entry
point needs to be created before the singleton component is available in a
Hilt test.

More information about `@EarlyEntryPoint` in the
[Hilt documentation](https://dagger.dev/hilt/early-entry-point).