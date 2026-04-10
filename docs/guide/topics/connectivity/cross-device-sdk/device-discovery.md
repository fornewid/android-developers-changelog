---
title: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/device-discovery
url: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/device-discovery
source: md.txt
---

# Device discovery API

Almost every multidevice experience begins with finding available devices. To simplify this common task, we offer the Device Discovery API.  
![Dialog box with sharing options to nearby users](https://developer.android.com/static/images/develop/connectivity/cross-device-sdk/device-discovery.png)**Figure 1**: Share with nearby users.

<br />

## Launch the device selection dialog

Device discovery uses a system dialog to let the user select a target device. To initiate the device selection dialog, you first need to get a device discovery client and register a result receiver. Note that similar to`registerForActivityResult`, this receiver must be registered unconditionally as part of the activity or fragment initialization path.
**Note:** If a user receives a request from an uninstalled app, they'll need to install it and try the request again. In the future, we hope to take advantage of Play Store APIs to continue the existing intent.  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  devicePickerLauncher = Discovery.create(this).registerForResult(this, handleDevices)
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  devicePickerLauncher = Discovery.create(this).registerForResult(this, handleDevices);
}
```

In the code snippet above, we have an undefined`handleDevices`object. After the user chooses the devices to connect to, and once the SDK successfully connects to the other devices, this callback receives the list of`Participants`selected.  

### Kotlin

```kotlin
handleDevices = OnDevicePickerResultListener { participants -> participants.forEach {
    // Use participant info
  }
}
```

### Java

```java
handleDevices = participants -> {
   for (Participant participant : participants) {
      // Use participant info
   }
}
```

After the device picker is registered, launch it using the`devicePickerLauncher`instance.`DevicePickerLauncher.launchDevicePicker`takes two parameters -- a list of device filters (see section below) and a`startComponentRequest`. The`startComponentRequest`is used to indicate which activity should be started on the receiving device, and the reason for the request that is shown to the user.  

### Kotlin

```kotlin
devicePickerLauncher.launchDevicePicker(
  listOf(),
  startComponentRequest {
    action = "com.example.crossdevice.MAIN"
    reason = "I want to say hello to you"
  },
)
```

### Java

```java
devicePickerLauncher.launchDevicePickerFuture(
    Collections.emptyList(),
    new StartComponentRequest.Builder()
        .setAction("com.example.crossdevice.MAIN")
        .setReason("I want to say hello to you")
        .build());
```

## Accept connection requests

When the user selects a device in the device picker, a dialog appears on the receiving device to ask the user to accept the connection. Once accepted, the target activity is launched, which can be handled in`onCreate`and`onNewIntent`.  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  handleIntent(getIntent())
}

override fun onNewIntent(intent: Intent) {
  super.onNewIntent(intent)
  handleIntent(intent)
}

private fun handleIntent(intent: Intent) {
  val participant = Discovery.create(this).getParticipantFromIntent(intent)
  // Accept connection from participant (see below)
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  handleIntent(getIntent());
}

@Override
public void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  handleIntent(intent);
}

private void handleIntent(Intent intent) {
  Participant participant = Discovery.create(this).getParticipantFromIntent(intent);
  // Accept connection from participant (see below)
}
```

## Device filters

| **Note:** This feature will be available in a later version of the developer preview.

When discovering devices, it's common to want to filter these devices to only show the ones relevant to the use case at hand. For example:

- Filtering to only devices with camera to help scan a QR code
- Filtering to only TVs for a big screen viewing experience

For this developer preview, we are starting with the ability to filter to devices owned by the same user.

You can specify the device filter using class`DeviceFilter`:  

### Kotlin

```kotlin
val deviceFilters = listOf(DeviceFilter.trustRelationshipFilter(MY_DEVICES_ONLY))
```

### Java

```java
List<DeviceFilter> deviceFilters =
    Arrays.asList(DeviceFilter.trustRelationshipFilter(MY_DEVICES_ONLY));
```

Once you define the device filters, you can initiate device discovery.  

### Kotlin

```kotlin
devicePickerLauncher.launchDevicePicker(deviceFilters, startComponentRequest)
```

### Java

```java
Futures.addCallback(
    devicePickerLauncher.launchDevicePickerFuture(deviceFilters, startComponentRequest),
    new FutureCallback<Void>() {
      @Override
      public void onSuccess(Void result) {
        // do nothing, result will be returned to handleDevices callback
      }

      @Override
      public void onFailure(Throwable t) {
        // handle error
      }
    },
    mainExecutor);
```

Notice that the`launchDevicePicker`is an asynchronous function that uses the`suspend`keyword.