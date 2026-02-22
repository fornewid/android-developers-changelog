---
title: https://developer.android.com/studio/test/managed-devices
url: https://developer.android.com/studio/test/managed-devices
source: md.txt
---

Build-managed devices improve consistency, performance, and reliability for
your automated instrumented tests. This feature, available for API levels 27 and
higher, lets you configure virtual or remote physical test devices in your
project's Gradle files. The Android Gradle plugin uses the configurations to
fully manage---that is, create, deploy, and tear down---those devices when executing
your automated tests.

This feature grants the Android Gradle plugin visibility into not only the tests
you're running, but also the lifecycle of the devices, thus improving the
quality of your testing experience in the following ways:

- Handles device-related issues in order to ensure your tests are executed
- For virtual devices, uses emulator snapshots to improve device startup time and memory usage and restore devices to a clean state between tests
- Caches test results and reruns only tests that are likely to provide different results
- Provides a consistent environment for running your tests between local and remote test runs

## Create a virtual build-managed device

You can specify a virtual device that you want to use for testing your
app in your module-level build file. The following code sample creates a Pixel 2
running API level 30 as a build-managed device.

### Kotlin

```kotlin
android {
  testOptions {
    managedDevices {
      localDevices {
        create("pixel2api30") {
          // Use device profiles you typically see in Android Studio.
          device = "Pixel 2"
          // Use only API levels 27 and higher.
          apiLevel = 30
          // To include Google services, use "google".
          systemImageSource = "aosp"
        }
      }
    }
  }
}
```

### Groovy

```groovy
android {
  testOptions {
    managedDevices {
      localDevices {
        pixel2api30 {
          // Use device profiles you typically see in Android Studio.
          device = "Pixel 2"
          // Use only API levels 27 and higher.
          apiLevel = 30
          // To include Google services, use "google".
          systemImageSource = "aosp"
        }
      }
    }
  }
}
```

> [!TIP]
> **Tip:** If you're using Android Studio to edit you build configuration, you can see available devices and their compatible API levels as autocomplete suggestions.

## Define groups of devices

To help you scale your tests across multiple device configurations, such as
different API levels and form factors, you can define multiple build-managed
devices and add them to a named group. The Android Gradle plugin can then
execute your tests across all the devices in the group in parallel.

The example below shows two devices added to a device group called
`phoneAndTablet`.

### Kotlin

```kotlin
testOptions {
  managedDevices {
    localDevices {
      create("pixel2api29") { ... }
      create("nexus9api30") { ... }
    }
    groups {
      create("phoneAndTablet") {
        targetDevices.add(devices["pixel2api29"])
        targetDevices.add(devices["nexus9api30"])
      }
    }
  }
}
```

### Groovy

```groovy
testOptions {
  managedDevices {
    localDevices {
      pixel2api29 { ... }
      nexus9api30 { ... }
    }
    groups {
      phoneAndTablet {
        targetDevices.add(devices.pixel2api29)
        targetDevices.add(devices.nexus9api30)
      }
    }
  }
}
```

## Run your tests

To run your tests using the build-managed devices you configured, use the
following command. `device-name` is the name of the device you configured in
your Gradle build script (such as `pixel2api30`), and `BuildVariant` is the
build variant of your app you want to test, such as `Debug`.

### Linux and macOS

```
./gradlew device-nameBuildVariantAndroidTest
```

### Windows

```
gradlew device-nameBuildVariantAndroidTest
```

To run your tests on a [group](https://developer.android.com/studio/test/managed-devices#define-groups) of build-managed devices, use
the following command.

### Linux and macOS

```
./gradlew group-nameGroupBuildVariantAndroidTest
```

```
./gradlew group-nameGroupBuildVariantAndroidTest
```

### Windows

```
gradlew group-nameGroupBuildVariantAndroidTest
```

The test output includes a path to an HTML file that has the test report. You
can also import test results into Android Studio for further analysis by
clicking **Run \> Test History** in the IDE.

> [!NOTE]
> **Note:** When using build-managed devices on servers that don't support hardware rendering, such as GitHub Actions, you need to specify the following flag: `-Pandroid.testoptions.manageddevices.emulator.gpu=swiftshader_indirect`. If you use PowerShell, you have to surround the flag with quotes.

## Enable test sharding

Build-managed devices support test sharding, which lets you split your test
suite across a number of identical virtual device instances, called *shards*,
that run in parallel. Using test sharding can help reduce overall test execution
time at the cost of additional computational resources.

To set the number of shards you want to use in a given test run, set the
following in your `gradle.properties` file:

    android.experimental.androidTest.numManagedDeviceShards=<number_of_shards>

> [!WARNING]
> **Warning:** Depending on the number of shards you specify, enabling this feature can be resource intensive. If Gradle is unable to provision the devices requested, the test run might fail with a timeout error. If the issue persists, try requesting fewer devices by reducing either the number of unique devices or shards per device.

When running your tests using this option, build-managed devices provision the
number of shards you specify for each device profile in the test run. So, for
example, if you deployed your tests to a device group of three devices and set
`numManagedDeviceShards` to two, build-managed devices will provision a total
of six virtual devices for your test run.

When your tests are complete, Gradle outputs test results in a `.proto` file
for each shard used in the test run.

## Use Automated Test Devices

Build-managed devices support a type of emulator device called the Automated
Test Device (ATD), which is optimized to reduce CPU and memory resources when
running your instrumented tests. ATDs improve runtime performance in a few ways:

- Remove pre-installed apps that are typically not useful for testing your app
- Disable certain background services that are typically not useful for testing your app
- Disable hardware rendering

> [!WARNING]
> **Warning:** Screenshot tests that depend on hardware rendering currently aren't supported when using ATDs.

Before getting started, make sure you
[update the Android Emulator](https://developer.android.com/studio/releases/emulator) to the latest
available version. Then, specify an "-atd" image when defining a build-managed
device in your module-level build file, as shown below:

### Kotlin

```kotlin
android {
  testOptions {
    managedDevices {
      localDevices {
        create("pixel2api30") {
          // Use device profiles you typically see in Android Studio.
          device = "Pixel 2"
          // ATDs currently support only API level 30.
          apiLevel = 30
          // You can also specify "google-atd" if you require Google Play Services.
          systemImageSource = "aosp-atd"
        }
      }
    }
  }
}
```

### Groovy

```groovy
android {
  testOptions {
    managedDevices {
      localDevices {
        pixel2api30 {
          // Use device profiles you typically see in Android Studio.
          device = "Pixel 2"
          // ATDs currently support only API level 30.
          apiLevel = 30
          // You can also specify "google-atd" if you require Google Play Services.
          systemImageSource = "aosp-atd"
        }
      }
    }
  }
}
```

You can also [create device groups](https://developer.android.com/studio/test/managed-devices#define-groups) as you can with other
build-managed devices. To further leverage the performance improvements, you
can also use ATDs with [test sharding](https://developer.android.com/studio/test/managed-devices#test-sharding) to reduce the total test
execution time of your test suite.

### What's removed from ATD images?

In addition to operating in a headless mode, ATDs also optimize performance by
removing or disabling apps and services that are typically not required for
testing your app's code. The table below provides an overview of the components
we've removed or disabled in ATD images and descriptions of why they might not
be useful.

| What's removed in ATD images | Why you might not need this when running automated tests |
|---|---|
| Google product apps: - Mail - Maps - Chrome - Messages - Play Store, and others | Your automated tests should focus on your own app's logic while assuming that other apps or the platform will function correctly. With [Espresso-Intents](https://developer.android.com/training/testing/espresso/intents), you can match and validate your outgoing intents or even provide stub responses in place of actual intent responses. |
| Settings apps and services: - CarrierConfig - EmergencyInfo - OneTimeInitializer - PhotoTable (screensavers) - Provision - Settings app - StorageManager - Telephony APN Configuration - WallpaperCropper - WallpaperPicker | These apps present a GUI for end-users to change platform settings, set up their device, or manage device storage. This is typically outside the scope of app-level automated testing. <br /> **Note:** [Settings provider](https://developer.android.com/reference/android/provider/Settings) is still available in the ATD image. |
| Settings apps and services: - CarrierConfig - EmergencyInfo - OneTimeInitializer - PhotoTable (screensavers) - Provision - Settings app - StorageManager - Telephony APN Configuration - WallpaperCropper - WallpaperPicker | These apps present a GUI for end-users to change platform settings, set up their device, or manage device storage. This is typically outside the scope of app-level automated testing. <br /> **Note:** [Settings provider](https://developer.android.com/reference/android/provider/Settings) is still available in the ATD image. |
| SystemUI | Your automated tests should focus on your own app's logic while assuming that other apps or the platform will function correctly. |
| AOSP apps and services: - Browser2 - Calendar - Camera2 - Contacts - Dialer - DeskClock - Gallery2 - LatinIME - Launcher3QuickStep - Music - QuickSearchBox - SettingsIntelligence | These apps and services are typically outside the scope of automated tests for your app's code. |

## Use Firebase Test Lab devices

You can run your automated instrumented tests at scale on [Firebase Test
Lab](https://firebase.google.com/docs/test-lab/) devices when using
build-managed devices. Test Lab lets you run your tests simultaneously on a
wide range of Android devices, both physical and virtual. These tests run in
remote Google data centers. With support from build-managed devices, the build
system can fully manage running tests against these Test Lab devices based on
your configurations.

> [!NOTE]
> **Note:** For information about Firebase Test Lab usage and associated costs (if any), see [Usage levels, quotas, and pricing for Test Lab](https://firebase.google.com/docs/test-lab/usage-quotas-pricing).

### Get started

The following steps describe how to start using Firebase Test Lab devices with
build-managed devices. These steps use the gcloud CLI to provide user
credentials, which might not apply to all development environments. For more
information about what authentication process to use for your needs, see [How
Application Default Credentials
works](https://cloud.google.com/docs/authentication/application-default-credentials).

1. To create a Firebase project, go to the
   [Firebase console](https://console.firebase.google.com/). Click
   **Add project** and follow the on-screen prompts to create a project.
   Remember your project ID.

   > [!NOTE]
   > **Note:** Enabling Google Analytics is optional, and not needed to use Firebase Test Lab. Unless you plan to use one of the listed services that depend on Google Analytics, we recommend that you *not* enable Google Analytics when prompted in the project creation workflow.

2. To install the Google Cloud CLI, follow the steps at
   [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

3. Configure your local environment.

   1. Link to your Firebase project in gcloud:

      ```
      gcloud config set project FIREBASE_PROJECT_ID
      ```
   2. Authorize the use of your user credentials for API access. We recommend
      authorizing by passing a
      [service account JSON file](https://firebase.google.com/docs/admin/setup#initialize_the_sdk_in_non-google_environments) to Gradle using the
      [DSL](https://developer.android.com/studio/test/managed-devices#ftl-gmd-dsl) in the module-level build script:

      ### Kotlin

      ```kotlin
      firebaseTestLab {
        ...
        serviceAccountCredentials.set(file(SERVICE_ACCOUNT_JSON_FILE))
      }
      ```

      ### Groovy

      ```groovy
      firebaseTestLab {
        ...
        serviceAccountCredentials = file(SERVICE_ACCOUNT_JSON_FILE)
      }
      ```

      Alternatively, you can authorize manually by using the following terminal
      command:

      ```
      gcloud auth application-default login
      ```
   3. Optional: Add your Firebase project as the quota project. This step is
      only needed if you exceed the
      [no-cost quota for Test Lab](https://firebase.google.com/pricing#test-lab).

      ```
      gcloud auth application-default set-quota-project FIREBASE_PROJECT_ID
      ```

      > [!NOTE]
      > **Note:** To access quota beyond the no-cost threshold, your Firebase project must be on the [Blaze pricing plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#switch-between-pricing-plans). You can upgrade to the Blaze pricing plan in the Firebase console.

4. Enable required APIs.

   In the
   [Google Developers Console API Library page](https://console.developers.google.com/apis/library),
   enable the [**Cloud Testing API**](https://console.cloud.google.com/apis/library/testing.googleapis.com)
   and [**Cloud Tool Results API**](https://console.cloud.google.com/apis/library/toolresults.googleapis.com)
   by typing these API names into the search box at the top of the console, and then clicking **Enable API**
   on the overview page for each API.
5. Configure your Android project.

   1. Add the Firebase Test Lab plugin in the top-level build script:

      ### Kotlin

      ```kotlin
      plugins {
        ...
        id("com.google.firebase.testlab") version "0.0.1-alpha05" apply false
      }
      ```

      ### Groovy

      ```groovy
      plugins {
        ...
        id 'com.google.firebase.testlab' version '0.0.1-alpha05' apply false
      }
      ```
   2. Enable custom device types in the `gradle.properties` file:

      ```groovy
      android.experimental.testOptions.managedDevices.customDevice=true
      ```
   3. Add the Firebase Test Lab plugin in the module-level build script:

      ### Kotlin

      ```kotlin
      plugins {
       ...
       id "com.google.firebase.testlab"
      }
      ```

      ### Groovy

      ```groovy
      plugins {
       ...
       id 'com.google.firebase.testlab'
      }
      ```

### Specify a Test Lab device

You can specify a Firebase Test Lab device for Gradle to use for testing your
app in the module-level build script. The following code sample creates a
Pixel 3 running API level 30 as a build-managed Test Lab device called
`ftlDevice`. The `firebaseTestLab {}` block is available when you apply the
`com.google.firebase.testlab` plugin to your module.

### Kotlin

```kotlin
firebaseTestLab {
  managedDevices {
    create("ftlDevice") {
      device = "Pixel3"
      apiLevel = 30
    }
  }
  ...
}
```

### Groovy

```groovy
firebaseTestLab {
  managedDevices {
    ftlDevice {
      device = "Pixel3"
      apiLevel = 30
    }
  }
  ...
}
```

To define a group of build-managed devices including Firebase Test Lab devices,
see [Define groups of devices](https://developer.android.com/studio/test/managed-devices#define-groups).

To run your tests, use the [same commands used to run other build-managed
devices](https://developer.android.com/studio/test/managed-devices#run-tests). Note that Gradle doesn't run tests in parallel or support
other Google Cloud CLI configurations for Test Lab devices.

### Optimize test runs with smart sharding

Testing on build-managed Test Lab devices supports smart sharding. Smart
sharding automatically distributes your tests across shards such that each shard
runs for approximately the same time, reducing manual allocation efforts and
overall test run duration. Smart sharding uses your test history, or information
about how long your tests have taken to run previously, to distribute tests in
an optimal way. Note that you need version 0.0.1-alpha05 of the Gradle plugin
for Firebase Test Lab to use smart sharding.

To enable smart sharding, specify the amount of time tests within each shard
should take. You should set the target shard time duration to at least five
minutes less than `timeoutMinutes` to avoid the situation where shards are
canceled before tests can finish.

```kotlin
firebaseTestLab {
  ...
  testOptions {
    targetedShardDurationMinutes = 2
  }
}
```

To learn more, read about the
[Firebase Test Lab device DSL options](https://developer.android.com/studio/test/managed-devices#ftl-gmd-dsl).

### Updated DSL for Test Lab devices

There are more DSL options you can configure to help customize your test runs or
migrate from other solutions you may already be using. See some of these options
as described in the following code snippet.

```kotlin
firebaseTestLab {
  ...

  /**
   * A path to a JSON file that contains service account credentials to access to
   * a Firebase Test Lab project.
   */
  serviceAccountCredentials.set(file("your_service_account_credentials.json"))


  testOptions {
    fixture {
      /**
       * Whether to grant permissions on the device before tests begin.
       * Available options are "all" or "none".
       *
       * Default value is "all".
       */
      grantedPermissions = "all"

      /**
       * Map of files to push to the device before starting the test.
       *
       * The key is the location on the device.
       * The value is the location of the file, either local or in Google Cloud.
       */
      extraDeviceFiles["/sdcard/dir1/file1.txt"] = "local/file.txt"
      extraDeviceFiles["/sdcard/dir2/file2.txt"] = "gs://bucket/file.jpg"

      /**
       * The name of the network traffic profile.
       *
       * Specifies network conditions to emulate when running tests.
       *
       * Default value is empty.
       */
      networkProfile = "LTE"
    }

    execution {
      /**
       * The maximum time to run the test execution before cancellation,
       * measured in minutes. Does not include the setup or teardown of device,
       * and is handled server-side.
       *
       * The maximum possible testing time is 45 minutes on physical devices
       * and 60 minutes on virtual devices.
       *
       * Defaults to 15 minutes.
       */
       timeoutMinutes = 30

      /**
       * Number of times the test should be rerun if tests fail.
       * The number of times a test execution should be retried if one
       * or more of its test cases fail.
       *
       * The max number of times is 10.
       *
       * The default number of times is 0.
       */
      maxTestReruns = 2

      /**
       * Ensures only a single attempt is made for each execution if
       * an infrastructure issue occurs. This doesn't affect `maxTestReruns`.
       * Normally, two or more attempts are made by Firebase Test Lab if a
       * potential infrastructure issue is detected. This is best enabled for
       * latency sensitive workloads. The number of execution failures might be
       * significantly greater with `failFast` enabled.
       *
       * Defaults to false.
       */
      failFast = false

      /**
       * The number of shards to split the tests across.
       *
       * Default to 0 for no sharding.
       */
      numUniformShards = 20
    }

    /**
     * For smart sharding, the target length of time each shard should takes in
     * minutes. Maxes out at 50 shards for physical devices and 100 shards for
     * virtual devices.
     *
     * Only one of numUniformShards or targetedShardDurationMinutes can be set.
     *
     * Defaults to 0 for no smart sharding.
     */
     targetedShardDurationMinutes = 15
    }

    results {
      /**
       * The name of the Google storage bucket to store the test results ihttps://firebase.google.com/docs/projects/iam/permissions#test-lab
       *
       * If left unspecified, the default bucket is used.
       *
       * Please refer to Firebase Test Lab permissions for required permissions
       * for using the bucket.
       */
      cloudStorageBucket = "bucketLocationName"

      /**
       * Name of test results for the Firebase console history list.
       * All tests results with the same history name are grouped
       * together in the Firebase console in a time-ordered test history list.
       *
       * Defaults to the application label in the APK manifest.
       */
      resultsHistoryName = "application-history"

      /**
       * List of paths to copy from the test device's storage to the test
       * results folder. These must be absolute paths under /sdcard or
       * /data/local/tmp.
       */
      directoriesToPull.addAll(
        "/sdcard/path/to/something"
      )

      /**
       * Whether to enable video recording during the test.
       *
       * Disabled by default.
       */
      recordVideo = false

      /**
       * Whether to enable performance metrics. If enabled, monitors and records
       * performance metrics such as CPU, memory, and network usage.
       *
       * Defaults to false.
       */
      performanceMetrics = true
  }
}
```