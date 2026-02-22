---
title: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup
url: https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup
source: md.txt
---

# Set up project for AndroidX Test

AndroidX Test is a collection of Jetpack libraries that lets you run tests against Android apps. It also provides a series of tools to help you write these tests.

For example, AndroidX Test provides JUnit4 rules to start activities and interact with them in JUnit4 tests. It also contains UI Testing frameworks such as Espresso, UI Automator and the Robolectric simulator.

## Add AndroidX Test libraries

In order to use AndroidX Test, you must modify your app project's dependencies within your development environment.

### Add Gradle dependencies

To modify your app project's dependencies, complete the following steps:

- **Step 1** : Open the`build.gradle`file for your Gradle module.
- **Step 2**: In the repositories section, make sure Google's Maven repository appears:

      allprojects {
        repositories {
          jcenter()
          google()
        }
      }

- **Step 3** : For each AndroidX Test package you want to use, add its package name to the dependencies section. For example, to add the`espresso-core`package, add the following lines:

### Groovy

```groovy
dependencies {
        ...
        androidTestImplementation "androidx.test.espresso:espresso-core:$espressoVersion"
    }
```

### Kotlin

```kotlin
dependencies {
        ...
        androidTestImplementation('androidx.test.espresso:espresso-core:$espressoVersion')
    }
```

These are the most common AndroidX Test dependencies available:  

### Groovy

```groovy
dependencies {
    // Core library
    androidTestImplementation "androidx.test:core:$androidXTestVersion0"

    // AndroidJUnitRunner and JUnit Rules
    androidTestImplementation "androidx.test:runner:$testRunnerVersion"
    androidTestImplementation "androidx.test:rules:$testRulesVersion"

    // Assertions
    androidTestImplementation "androidx.test.ext:junit:$testJunitVersion"
    androidTestImplementation "androidx.test.ext:truth:$truthVersion"

    // Espresso dependencies
    androidTestImplementation "androidx.test.espresso:espresso-core:$espressoVersion"
    androidTestImplementation "androidx.test.espresso:espresso-contrib:$espressoVersion"
    androidTestImplementation "androidx.test.espresso:espresso-intents:$espressoVersion"
    androidTestImplementation "androidx.test.espresso:espresso-accessibility:$espressoVersion"
    androidTestImplementation "androidx.test.espresso:espresso-web:$espressoVersion"
    androidTestImplementation "androidx.test.espresso.idling:idling-concurrent:$espressoVersion"

    // The following Espresso dependency can be either "implementation",
    // or "androidTestImplementation", depending on whether you want the
    // dependency to appear on your APK'"s compile classpath or the test APK
    // classpath.
    androidTestImplementation "androidx.test.espresso:espresso-idling-resource:$espressoVersion"
}
```

### Kotlin

```kotlin
dependencies {
    // Core library
    androidTestImplementation("androidx.test:core:$androidXTestVersion")

    // AndroidJUnitRunner and JUnit Rules
    androidTestImplementation("androidx.test:runner:$testRunnerVersion")
    androidTestImplementation("androidx.test:rules:$testRulesVersion")

    // Assertions
    androidTestImplementation("androidx.test.ext:junit:$testJunitVersion")
    androidTestImplementation("androidx.test.ext:truth:$truthVersion")

    // Espresso dependencies
    androidTestImplementation( "androidx.test.espresso:espresso-core:$espressoVersion")
    androidTestImplementation( "androidx.test.espresso:espresso-contrib:$espressoVersion")
    androidTestImplementation( "androidx.test.espresso:espresso-intents:$espressoVersion")
    androidTestImplementation( "androidx.test.espresso:espresso-accessibility:$espressoVersion")
    androidTestImplementation( "androidx.test.espresso:espresso-web:$espressoVersion")
    androidTestImplementation( "androidx.test.espresso.idling:idling-concurrent:$espressoVersion")

    // The following Espresso dependency can be either "implementation",
    // or "androidTestImplementation", depending on whether you want the
    // dependency to appear on your APK"s compile classpath or the test APK
    // classpath.
    androidTestImplementation( "androidx.test.espresso:espresso-idling-resource:$espressoVersion")
}
```

The[Release Notes](https://developer.android.com/jetpack/androidx/releases/test)page contains a table with the latest versions per artifact.
| **Note:** It's important to ensure these testing dependencies point to the correct source set. Usually AndroidX Test is needed in instrumentation tests only, so you would use`androidTestImplementation()`. However, in cases such as with`espresso-idling-resource`, the APIs are used from production code, requiring you to use the implementation function.

Refer to the[Package Index](https://developer.android.com/reference/androidx/test/packages)or[Class Index](https://developer.android.com/reference/androidx/test/classes)for specific reference documentation on these libraries.

## Projects using deprecated classes

| **Warning:** If you build instrumentation tests using Gradle, you receive additional support. When auto-generating the test manifest, the Android Gradle Plugin adds the following libraries and manifest elements to your project automatically so you don't need to take these steps.

If your app uses tests that rely on deprecated JUnit3-based`android.test`classes , such as[`InstrumentationTestCase`](https://developer.android.com/reference/android/test/InstrumentationTestCase)and[`TestSuiteLoader`](https://developer.android.com/reference/junit/runner/TestSuiteLoader), add the following lines in the`android`section of the file:  

    android {
        ...
        useLibrary 'android.test.runner'

        useLibrary 'android.test.base'
        useLibrary 'android.test.mock'
      }

| **Note:** You only need to include the libraries that contain the classes used in your app. For a list of the classes that appear in each library, see[JUnit-based libraries](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup).

### Add manifest declarations

To run tests that rely on deprecated JUnit3-based`android.test`classes, add the necessary[`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element)elements to your test app's manifest. For example, if you add tests that depend on the`android.test.runner`library, add the following element to your app's manifest:  

    <!-- You don't need to include android:required="false" if your app's

       minSdkVersion is 28 or higher. -->

    <uses-library android:name="android.test.runner"

           android:required="false" />

To determine the library that contains a given JUnit-based class, see[JUnit-based libraries](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup).
| **Caution:** Avoid deprecated classes where possible. Use supported JUnit-based classes in their place.

#### Considerations when using deprecated classes and targeting Android 9 or

higher

The guidance in this section applies only if you target Android 9 (API level 28) or higher*and*the minimum SDK version for your app is set to Android 9.

The`android.test.runner`library implicitly depends on the`android.test.base`and`android.test.mock`libraries. If your app only uses classes from`android.test.base`or`android.test.mock`, you can include the libraries by themselves:  

    <!-- For both of these declarations, you don't need to include
       android:required="false" if your app's minSdkVersion is 28
       or higher. -->

    <uses-library android:name="android.test.base"
           android:required="false" />
    <uses-library android:name="android.test.mock"
           android:required="false" />