---
title: Test app feedback  |  Android Enterprise  |  Android Developers
url: https://developer.android.com/work/app-feedback/testing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Enterprise](https://developer.android.com/work)

# Test app feedback Stay organized with collections Save and categorize content based on your preferences.




**Note:** To learn more about how to send feedback from your app,
see [Send feedback to EMMs](/work/app-feedback/overview).
After updating your app to support sending feedback in the form of keyed app states, you can use
the guidance on this page to set up unit tests and send test feedback to a test device policy
controller (DPC).

## Set up unit tests

This section provides examples of how to set up unit tests to check that your app interacts with
keyed app states as expected.

### Step 1: Set up your classes to accept `KeyedAppStatesReporter` as a parameter

Instead of calling `create()` directly, modify your classes to accept
`KeyedAppStatesReporter` as a parameter like in the example `BatteryManager`
class below:

### Kotlin

```
class BatteryManager(val reporter:KeyedAppStatesReporter) {
  fun lowBattery(battery:Int) {
    reporter.setStatesImmediate(
        hashSetOf(KeyedAppState.builder()
           .setKey("battery")
           .setSeverity(KeyedAppState.SEVERITY_INFO)
           .setMessage("Battery is low")
           .setData(battery.toString())
           .build()))
  }
}
```

### Java

```
public class BatteryManager {
    private final KeyedAppStatesReporter reporter;
    public BatteryManager(KeyedAppStatesReporter reporter) {
        this.reporter = reporter;
    }

    public void lowBattery(int battery) {
        final Collection states = new HashSet<>();
        states.add(KeyedAppState.builder()
            .setKey("battery")
            .setSeverity(KeyedAppState.SEVERITY_INFO)
            .setMessage("Battery is low")
            .setData(Integer.toString(battery))
            .build();
        reporter.setStatesImmediate(states);
    }
}
```

Next, use `KeyedAppStatesReporter.create` to get an instance to pass
wherever `BatteryManager` is created.

### Step 2: Add the enterprise feedback testing library to your `build.gradle` file

Add the following dependency to your app's
[`build.gradle`](/studio/build#module-level) file:

```
dependencies {
    testImplementation 'androidx.enterprise:enterprise-feedback-testing:1.0.0'
}
```

### Step 3: Create a `FakeKeyedAppStatesReporter` and pass it into your class

### Kotlin

```
val reporter = FakeKeyedAppStatesReporter();
val batteryManager = BatteryManager(reporter);
```

### Java

```
FakeKeyedAppStatesReporter reporter = new FakeKeyedAppStatesReporter();
BatteryManager batteryManager = new BatteryManager(reporter);
```

### Step 4: Assert interactions with `FakeKeyedAppStatesReporter`

**Note:** To view all the options for verifying expected interactions, see
[`FakeKeyedAppStatesReporter`](https://developer.android.google.cn/reference/androidx/enterprise/feedback/FakeKeyedAppStatesReporter).

For example, to check that no states have been set:

### Kotlin

```
assertThat(reporter.keyedAppStates).isEmpty();
```

### Java

```
assertThat(reporter.getKeyedAppStates()).isEmpty();
```

Or that a particular state has been requested to be uploaded:

### Kotlin

```
assertThat(reporter.uploadedKeyedAppStatesByKey["battery"]).isNotNull()
```

### Java

```
assertThat(reporter.getUploadedKeyedAppStatesByKey().get("battery")).isNotNull();
```

## Send test feedback to Test DPC

A sample [device policy controller](https://developers.google.com/android/work/terminology#device_policy_controller_dpc),
called Test DPC, is capable of receiving app feedback and is available for
download.

### Step 1: Install Test DPC

Install the latest version of [Test DPC](https://play.google.com/store/apps/details?id=com.afwsamples.testdpc)
from the Play Store. Next, set Test DPC as the admin of the device:

```
adb shell dpm set-device-owner com.afwsamples.testdpc/.DeviceAdminReceiver
```

### Step 2: Enable App feedback notifications

In Test DPC's menu, enable **App feedback notifications**.

![enable notifications](/static/images/work/test-dpc-screenshot.png)

Trigger an event that set a keyed app state. If successful, Test DPC will show
the feedback in notifications:

![feedback displayed](/static/images/work/feedback-notification.png)