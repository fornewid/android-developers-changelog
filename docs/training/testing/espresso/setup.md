---
title: https://developer.android.com/training/testing/espresso/setup
url: https://developer.android.com/training/testing/espresso/setup
source: md.txt
---

This guide covers installing Espresso using the SDK Manager and building it
using Gradle. Android Studio is recommended.

## Set up your test environment

To avoid flakiness, we highly recommend that you turn off system animations on
the virtual or physical devices used for testing. On your device, under
**Settings \> Developer options**, disable the following 3 settings:

- Window animation scale
- Transition animation scale
- Animator duration scale

## Add Espresso dependencies

To add Espresso dependencies to your project, complete the following steps:

1. Open your app's `build.gradle` file. This is usually not the top-level `build.gradle` file but `app/build.gradle`.
2. Add the following lines inside dependencies:

### Groovy

```groovy
androidTestImplementation 'androidx.test.espresso:espresso-core:3.6.1'
androidTestImplementation 'androidx.test:runner:1.6.1'
androidTestImplementation 'androidx.test:rules:1.6.1'
```

### Kotlin

```kotlin
androidTestImplementation('androidx.test.espresso:espresso-core:3.6.1')
androidTestImplementation('androidx.test:runner:1.6.1')
androidTestImplementation('androidx.test:rules:1.6.1')
```

[View the complete set of Gradle dependencies](https://developer.android.com/studio/build/dependencies).

## Set the instrumentation runner

Add to the same `build.gradle` file the following line in
`android.defaultConfig`:  

### Groovy

```groovy
testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
```

### Kotlin

```kotlin
testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
```

## Example Gradle build file

### Groovy

```groovy
plugins {
  id 'com.android.application'
}

android {
    compileSdkVersion 36

    defaultConfig {
        applicationId "com.my.awesome.app"
        minSdkVersion 23
        targetSdkVersion 36
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
}

dependencies {
    androidTestImplementation 'androidx.test:runner:1.6.1'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.6.1'
}
```

### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android {
    compileSdkVersion(36)

    defaultConfig {
        applicationId = "com.my.awesome.app"
        minSdkVersion(23)
        targetSdkVersion(36)
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }
}

dependencies {
    androidTestImplementation('androidx.test:runner:1.6.1')
    androidTestImplementation('androidx.test.espresso:espresso-core:3.6.1')
}
```

## Analytics

In order to make sure we are on the right track with each new release, the test
runner collects analytics. More specifically, it uploads a hash of the package
name of the application under test for each invocation. This allows us to
measure both the count of unique packages using Espresso as well as the volume
of usage.

If you do not wish to upload this data, you can opt out by including the
`disableAnalytics` argument in your instrumentation command:  

```bash
adb shell am instrument -e disableAnalytics true
```

## Add the first test

Android Studio creates tests by default in
`src/androidTest/java/com.example.package/`.

Example JUnit4 test using Rules:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
@LargeTest
class HelloWorldEspressoTest {

    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test fun listGoesOverTheFold() {
        onView(withText("Hello world!")).check(matches(isDisplayed()))
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@LargeTest
public class HelloWorldEspressoTest {

    @Rule
    public ActivityScenarioRule<MainActivity> activityRule =
            new ActivityScenarioRule<>(MainActivity.class);

    @Test
    public void listGoesOverTheFold() {
        onView(withText("Hello world!")).check(matches(isDisplayed()));
    }
}
```

## Run tests

You can run your tests in Android Studio or from the command line.

### In Android Studio

To create a test configuration in Android Studio, complete the following steps:

1. Open **Run \> Edit Configurations**.
2. Add a new Android Tests configuration.
3. Choose a module.
4. Add a specific instrumentation runner: `androidx.test.runner.AndroidJUnitRunner`
5. Run the newly created configuration.

### From the command line

Execute the following Gradle command:  

```bash
./gradlew connectedAndroidTest
```