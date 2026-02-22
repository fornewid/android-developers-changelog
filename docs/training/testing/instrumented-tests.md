---
title: https://developer.android.com/training/testing/instrumented-tests
url: https://developer.android.com/training/testing/instrumented-tests
source: md.txt
---

# Build instrumented tests

Instrumented tests run on Android devices, whether physical or emulated. As such, they can take advantage of the Android framework APIs. Instrumented tests therefore provide more fidelity than local tests, though they run much more slowly.

We recommend using instrumented tests only in cases where you must test against the behavior of a real device.[AndroidX Test](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup)provides several libraries that make it easier to write instrumented tests when necessary.
| **Note:** Instrumented test, also known as*instrumentation* tests, are initialized in a special environment that gives them access to an instance of[Instrumentation](https://developer.android.com/reference/android/app/Instrumentation). This class provides access to the application context and APIs to manipulate the app under test and gives instrumented tests their name.

## Set up your testing environment

In your Android Studio project, you store the source files for instrumented tests in`module-name/src/androidTest/java/`. This directory already exists when you create a new project and contains an example instrumented test.

Before you begin, you should add AndroidX Test APIs, which allow you to quickly build and run instrumented test code for your apps. AndroidX Test includes a JUnit 4 test runner ,[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner), and APIs for functional UI tests such as[Espresso](https://developer.android.com/training/testing/espresso),[UI Automator](https://developer.android.com/training/testing/ui-automator)and[Compose test](https://developer.android.com/jetpack/compose/testing).

You also need to configure the Android testing dependencies for your project to use the test runner and the rules APIs provided by AndroidX Test.

In your app's top-level`build.gradle`file, you need to specify these libraries as dependencies:  

    dependencies {
        androidTestImplementation "androidx.test:runner:$androidXTestVersion"
        androidTestImplementation "androidx.test:rules:$androidXTestVersion"
        // Optional -- UI testing with Espresso
        androidTestImplementation "androidx.test.espresso:espresso-core:$espressoVersion"
        // Optional -- UI testing with UI Automator
        androidTestImplementation "androidx.test.uiautomator:uiautomator:$uiAutomatorVersion"
        // Optional -- UI testing with Compose
        androidTestImplementation "androidx.compose.ui:ui-test-junit4:$compose_version"
    }

You can find the latest versions in the[AndroidX Release Notes](https://developer.android.com/jetpack/androidx/releases/test)and[Compose UI Release Notes](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner).

To use JUnit 4 test classes and have access to features such as test filtering, make sure to specify[AndroidJUnitRunner](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner)as the default test instrumentation runner in your project by including the following setting in your app's module-level`build.gradle`file:  

    android {
        defaultConfig {
            testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        }
    }

## Create an instrumented test class

Your instrumented test class should be a JUnit 4 test class that's similar to the class described in the section on how to[build local tests](https://developer.android.com/training/testing/unit-testing/local-unit-tests#build).

To create an instrumented JUnit 4 test class, specify`AndroidJUnit4`as your default test runner.
| **Note:** If your test suite depends on a mix of JUnit3 and JUnit4 libraries, add the`@RunWith(AndroidJUnit4::class)`annotation at the beginning of your test class definition.

The following example shows how you might write an instrumented test to verify that the[Parcelable](https://developer.android.com/reference/android/os/Parcelable)interface is implemented correctly for the`LogHistory`class:  

### Kotlin

```kotlin
import android.os.Parcel
import android.text.TextUtils.writeToParcel
import androidx.test.filters.SmallTest
import androidx.test.runner.AndroidJUnit4
import com.google.common.truth.Truth.assertThat
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith

const val TEST_STRING = "This is a string"
const val TEST_LONG = 12345678L

// @RunWith is required only if you use a mix of JUnit3 and JUnit4.
@RunWith(AndroidJUnit4::class)
@SmallTest
class LogHistoryAndroidUnitTest {
    private lateinit var logHistory: LogHistory

    @Before
    fun createLogHistory() {
        logHistory = LogHistory()
    }

    @Test
    fun logHistory_ParcelableWriteRead() {
        val parcel = Parcel.obtain()
        logHistory.apply {
            // Set up the Parcelable object to send and receive.
            addEntry(TEST_STRING, TEST_LONG)

            // Write the data.
            writeToParcel(parcel, describeContents())
        }

        // After you're done with writing, you need to reset the parcel for reading.
        parcel.setDataPosition(0)

        // Read the data.
        val createdFromParcel: LogHistory = LogHistory.CREATOR.createFromParcel(parcel)
        createdFromParcel.getData().also { createdFromParcelData: List<Pair<String, Long>> ->

            // Verify that the received data is correct.
            assertThat(createdFromParcelData.size).isEqualTo(1)
            assertThat(createdFromParcelData[0].first).isEqualTo(TEST_STRING)
            assertThat(createdFromParcelData[0].second).isEqualTo(TEST_LONG)
        }
    }
}
```

### Java

```java
import android.os.Parcel;
import android.util.Pair;
import androidx.test.runner.AndroidJUnit4;
import com.google.common.truth.Truth.assertThat;
import java.util.List;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

// @RunWith is required only if you use a mix of JUnit3 and JUnit4.
@RunWith(AndroidJUnit4.class)
public class LogHistoryAndroidUnitTest {

    public static final String TEST_STRING = "This is a string";
    public static final long TEST_LONG = 12345678L;
    private LogHistory mLogHistory;

    @Before
    public void createLogHistory() {
        mLogHistory = new LogHistory();
    }

    @Test
    public void logHistory_ParcelableWriteRead() {
        // Set up the Parcelable object to send and receive.
        mLogHistory.addEntry(TEST_STRING, TEST_LONG);

        // Write the data.
        Parcel parcel = Parcel.obtain();
        mLogHistory.writeToParcel(parcel, mLogHistory.describeContents());

        // After you're done with writing, you need to reset the parcel for reading.
        parcel.setDataPosition(0);

        // Read the data.
        LogHistory createdFromParcel = LogHistory.CREATOR.createFromParcel(parcel);
        List<Pair<String, Long>> createdFromParcelData
                = createdFromParcel.getData();

        // Verify that the received data is correct.
        assertThat(createdFromParcelData.size()).isEqualTo(1);
        assertThat(createdFromParcelData.get(0).first).isEqualTo(TEST_STRING);
        assertThat(createdFromParcelData.get(0).second).isEqaulTo(TEST_LONG);
    }
}
```
| **Note:** Using backticks to name tests in Kotlin is only supported on devices running API 30 and above. For example,``@Test fun `everything works`() { ... }``

## Run instrumented tests

Instrumented tests can be run on real devices or emulators. In the Android Studio guide you can learn how to:

- [Test from Android Studio](https://developer.android.com/studio/test)
- [Test from the command line](https://developer.android.com/studio/test/command-line)

## Additional resources

**UI tests** are usually Instrumented tests that verify the correct behavior of the UI. They use frameworks such as**Espresso** or**Compose Test** . To learn more, read the[UI testing guide](https://developer.android.com/training/testing/ui-tests).

For more information about using Instrumentation tests, consult the following resources.

### Sample

- [Instrumented Unit Tests Code Samples](https://github.com/android/testing-samples/tree/main/unit/BasicUnitAndroidTest)

### Codelabs

- [Android Testing Codelab](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-basics)