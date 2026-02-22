---
title: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner
url: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner
source: md.txt
---

# AndroidJUnitRunner

The[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner)class is a[JUnit](http://junit.org/junit4/)test runner that lets you run instrumented[JUnit 4](https://junit.org/junit4/)tests on Android devices, including those using the[Espresso](https://developer.android.com/training/testing/espresso),[UI Automator](https://developer.android.com/training/testing/ui-automator), and[Compose](https://developer.android.com/jetpack/compose/testing)testing frameworks.
| **Note:** `AndroidJUnitRunner`is not needed for local tests. Read about the difference between instrumented and local tests in[fundamentals of testing](https://developer.android.com/training/testing/fundamentals).

The test runner handles loading your test package and the app under test to a device, running your tests, and reporting test results.

This test runner supports several common testing tasks, including the following:

- [Writing JUnit tests](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#write-junit)
- [Accessing the app's context](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#access-context)
- [Filtering tests](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#filter-tests)
- [Sharding tests](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#shard-tests)

## Write JUnit tests

The following code snippet shows how you might write an instrumented JUnit 4 test to validate that the`changeText`operation in the`ChangeTextBehavior`class works correctly:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
@LargeTest // Optional runner annotation
class ChangeTextBehaviorTest {
 val stringToBeTyped = "Espresso"
 // ActivityTestRule accesses context through the runner
 @get:Rule
 val activityRule = ActivityTestRule(MainActivity::class.java)

 @Test fun changeText_sameActivity() {
 // Type text and then press the button.
 onView(withId(R.id.editTextUserInput))
 .perform(typeText(stringToBeTyped), closeSoftKeyboard())
 onView(withId(R.id.changeTextBt)).perform(click())

 // Check that the text was changed.
 onView(withId(R.id.textToBeChanged))
 .check(matches(withText(stringToBeTyped)))
 }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@LargeTest // Optional runner annotation
public class ChangeTextBehaviorTest {

    private static final String stringToBeTyped = "Espresso";

    @Rule
    public ActivityTestRule<MainActivity>; activityRule =
            new ActivityTestRule<>;(MainActivity.class);

    @Test
    public void changeText_sameActivity() {
        // Type text and then press the button.
        onView(withId(R.id.editTextUserInput))
                .perform(typeText(stringToBeTyped), closeSoftKeyboard());
        onView(withId(R.id.changeTextBt)).perform(click());

        // Check that the text was changed.
        onView(withId(R.id.textToBeChanged))
                .check(matches(withText(stringToBeTyped)));
    }
}
```
| **Note:** Don't mix JUnit 3 and JUnit 4 test code in the same package, because this might cause unexpected results.

## Access the Application's Context

When you use`AndroidJUnitRunner`to run your tests, you can access the context for the app under test by calling the static`ApplicationProvider.getApplicationContext()`method. If you've created a custom subclass of`Application`in your app, this method returns your custom subclass's context.

If you're a tools implementer, you can access low-level testing APIs using the[`InstrumentationRegistry`](https://developer.android.com/reference/androidx/test/InstrumentationRegistry)class. This class includes the[`Instrumentation`](https://developer.android.com/reference/android/app/Instrumentation)object, the target app[`Context`](https://developer.android.com/reference/android/content/Context)object, the test app`Context`object, and the command line arguments passed into your test.

## Filter tests

In your JUnit 4.x tests, you can use annotations to configure the test run. This feature minimizes the need to add boilerplate and conditional code in your tests. In addition to the standard annotations supported by JUnit 4, the test runner also supports[Android-specific annotations](https://developer.android.com/reference/androidx/test/filters/package-summary), including the following:

- **`@RequiresDevice`**: Specifies that the test should run only on physical devices, not on emulators.
- **`@SdkSuppress`** : Suppresses the test from running on a lower Android API level than the given level. For example, to suppress tests on all API levels lower than 23 from running, use the annotation`@SDKSuppress(minSdkVersion=23)`.
- **`@SmallTest`,`@MediumTest`, and`@LargeTest`** : Classify how long a test should take to run, and consequently, how frequently you can run the test. You can use this annotation to filter which tests to run, setting the`android.testInstrumentationRunnerArguments.size`property:

    -Pandroid.testInstrumentationRunnerArguments.size=small

## Shard tests

If you need to parallelize the execution of your tests, sharing them across multiple servers to make them run faster, you can split them into groups, or*shards* . The test runner supports splitting a single test suite into multiple shards, so you can easily run tests belonging to the same shard together as a group. Each shard is identified by an index number. When running tests, use the`-e numShards`option to specify the number of separate shards to create and the`-e shardIndex`option to specify which shard to run.

For example, to split the test suite into 10 shards and run only the tests grouped in the second shard, use the following[adb command](https://developer.android.com/studio/command-line/adb):  

    adb shell am instrument -w -e numShards 10 -e shardIndex 2

## Use Android Test Orchestrator

Android Test Orchestrator allows you to run each of your app's tests within its own invocation of`Instrumentation`. When using AndroidJUnitRunner version 1.0 or higher, you have access to Android Test Orchestrator.

Android Test Orchestrator offers the following benefits for your testing environment:

- **Minimal shared state:** Each test runs in its own`Instrumentation`instance. Therefore, if your tests share app state, most of that shared state is removed from your device's CPU or memory after each test. To remove*all* shared state from your device's CPU and memory after each test, use the`clearPackageData`flag. See the[Enable from Gradle](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-gradle)section for an example.
- **Crashes are isolated:** Even if one test crashes, it takes down only its own instance of`Instrumentation`. This means that the other tests in your suite still run, providing complete test results.

This isolation results in a possible increase in test execution time as the Android Test Orchestrator restarts the application after each test.
| **Note:** The deprecated test instrumentation runner,`InstrumentationTestRunner`, isn't compatible with Android Test Orchestrator. If you use`InstrumentationTestRunner`, you might need to use a different instrumentation runner to use on-device orchestration.

Both Android Studio and Firebase Test Lab have Android Test Orchestrator pre-installed, though you need to[enable the feature in Android Studio](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-android).

### Enable from Gradle

To enable Android Test Orchestrator using the Gradle command-line tool, complete these steps:

- **Step 1** : Modify gradle file. Add the following statements to your project's`build.gradle`file:

    android {
     defaultConfig {
      ...
      testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"

      // The following argument makes the Android Test Orchestrator run its
      // "pm clear" command after each test invocation. This command ensures
      // that the app's state is completely cleared between tests.
      testInstrumentationRunnerArguments clearPackageData: 'true'
     }

     testOptions {
      execution 'ANDROIDX_TEST_ORCHESTRATOR'
     }
    }

    dependencies {
     androidTestImplementation 'androidx.test:runner:1.1.0'
     androidTestUtil 'androidx.test:orchestrator:1.1.0'
    }

- **Step 2**: Run Android Test Orchestrator by executing the following command:

    ./gradlew connectedCheck

### Enable from Android Studio

To enable Android Test Orchestrator in Android Studio, add the statements shown in[Enable from Gradle](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-gradle)to your app's`build.gradle`file.

### Enable from command line

To use Android Test Orchestrator on the command line, run the following commands in a terminal window:  

    DEVICE_API_LEVEL=$(adb shell getprop ro.build.version.sdk)

    FORCE_QUERYABLE_OPTION=""
    if [[ $DEVICE_API_LEVEL -ge 30 ]]; then
       FORCE_QUERYABLE_OPTION="--force-queryable"
    fi

    # uninstall old versions
    adb uninstall androidx.test.services
    adb uninstall androidx.test.orchestrator

    # Install the test orchestrator.
    adb install $FORCE_QUERYABLE_OPTION -r path/to/m2repository/androidx/test/orchestrator/1.4.2/orchestrator-1.4.2.apk

    # Install test services.
    adb install $FORCE_QUERYABLE_OPTION -r path/to/m2repository/androidx/test/services/test-services/1.4.2/test-services-1.4.2.apk

    # Replace "com.example.test" with the name of the package containing your tests.
    # Add "-e clearPackageData true" to clear your app's data in between runs.
    adb shell 'CLASSPATH=$(pm path androidx.test.services) app_process / \
     androidx.test.services.shellexecutor.ShellMain am instrument -w -e \
     targetInstrumentation com.example.test/androidx.test.runner.AndroidJUnitRunner \
     androidx.test.orchestrator/.AndroidTestOrchestrator'

As the command syntax shows, you install Android Test Orchestrator, then use it directly.
**Note:** If you don't know your target instrumentation, you can look it up by running the following command:  

    adb shell pm list instrumentation

### Using different toolchains

If you use a different toolchain to test your app, you can still use Android Test Orchestrator by completing the following steps:

1. Include the necessary[packages](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-gradle)in your app's build file.
2. Enable Android Test Orchestrator[from the command-line](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-command).

### Architecture

The Orchestrator service APK is stored in a process that's separate from the test APK and the APK of the app under test:
![The orchestrator allows you to control JUnit tests](https://developer.android.com/static/training/testing/instrumented-tests/androidx-test-libraries/orchestrator.png)**Figure 1**: Android Test Orchestration APK structure.

Android Test Orchestrator collects JUnit tests at the beginning of your test suite run, but it then executes each test separately, in its own instance of`Instrumentation`.

## More information

To learn more about using AndroidJUnitRunner, see the[API reference](https://developer.android.com/reference/androidx/test/runner/package-summary).

## Additional resources

For more information about using`AndroidJUnitRunner`, consult the following resources.

### Samples

- [AndroidJunitRunnerSample](https://github.com/android/testing-samples/tree/main/runner/AndroidJunitRunnerSample): Showcases test annotations, parameterized tests, and test suite creation.