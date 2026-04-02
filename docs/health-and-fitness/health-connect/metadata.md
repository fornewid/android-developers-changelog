---
title: https://developer.android.com/health-and-fitness/health-connect/metadata
url: https://developer.android.com/health-and-fitness/health-connect/metadata
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12) and
> later.

There are changes to metadata in Health Connect for
developers who upgrade to release 1.1.0-alpha12 or later.
| **Warning:** Updating Jetpack versions without implementing these changes will break your Health Connect integration.

## Library information

The [Google Maven Android gradle plugin](https://developer.android.com/build/dependencies#google-maven) artifact ID
identifies the Health Connect library to which you will need to upgrade.
Add this Health Connect SDK dependency to your module-level
`build.gradle` file:  

    dependencies {
      implementation "androidx.health.connect:connect-client:1.1.0-alpha12"
    }

## Metadata changes

Two metadata changes have been introduced to the **Health Connect Jetpack SDK**
as of version 1.1.0-alpha12 to help verify that additional useful metadata
exists in the ecosystem. If `metadata` is not included in your
`Record` constructor, you might see a **Constructor internal** error.

### Specify the recording method

You must specify metadata details whenever
a `Record()` type object is instantiated.

When writing data to **Health Connect** , you must specify one of four recording
methods by using one of the corresponding [factory methods](https://developer.android.com/health-and-fitness/health-connect/metadata#metadata-methods)
to instantiate `Metadata`:

| Recording method | Description |
|---|---|
| `RECORDING_METHOD_UNKNOWN` | The recording method cannot be verified. |
| `RECORDING_METHOD_MANUAL_ENTRY` | The user entered the data. |
| `RECORDING_METHOD_AUTOMATICALLY_RECORDED` | A device or sensor recorded the data. |
| `RECORDING_METHOD_ACTIVELY_RECORDED` | The user initiated the start or end of the recording session on a device. |

For example:  

    StepsRecord(
        startTime = Instant.ofEpochMilli(1234L),
        startZoneOffset = null,
        endTime = Instant.ofEpochMilli(1236L),
        endZoneOffset = null,
        metadata = Metadata.manualEntry(),
        Count = 10,
    )

### Device type

You must specify a device type for all
automatically and actively recorded data. For more details, see the
[`Device` class in the Jetpack documentation](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:health/connect/connect-client/src/main/java/androidx/health/connect/client/records/metadata/Device.kt). Current device
types include:

| Device type | Description |
|---|---|
| `TYPE_UNKNOWN` | The device type is unknown. |
| `TYPE_WATCH` | The device type is a watch. |
| `TYPE_PHONE` | The device type is a phone. |
| `TYPE_SCALE` | The device type is a scale. |
| `TYPE_RING` | The device type is a ring. |
| `TYPE_HEAD_MOUNTED` | The device type is a head-mounted device. |
| `TYPE_FITNESS_BAND` | The device type is a fitness band. |
| `TYPE_CHEST_STRAP` | The device type is a chest strap. |
| `TYPE_SMART_DISPLAY` | The device type is a smart display. |

Some `Device.type` values are only available on later versions of Health
Connect. When the extended device types feature isn't available, these types
are treated as `Device.TYPE_UNKNOWN`.

| Extended device types | Description |
|---|---|
| `TYPE_CONSUMER_MEDICAL_DEVICE` | The device type is medical device. |
| `TYPE_GLASSES` | The device type is a pair of smart glasses or eyewear. |
| `TYPE_HEARABLE` | The device type is a hearable device. |
| `TYPE_FITNESS_MACHINE` | The device type is a stationary machine. |
| `TYPE_FITNESS_EQUIPMENT` | The device type is a fitness equipment. |
| `TYPE_PORTABLE_COMPUTER` | The device type is a portable computer. |
| `TYPE_METER` | The device type is a measurement meter. |

To determine whether a user's device supports Extended Device Types on Health Connect, check the availability of `FEATURE_EXTENDED_DEVICE_TYPES` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_EXTENDED_DEVICE_TYPES
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

See [Check for feature availability](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability) to learn more. **Note:** If known, provide the \`manufacturer\` and \`model\` of the device in addition to device type. Doing so helps with attribution in reader applications, so users can understand which device or application recorded their data.

For example:  

    // Watch
    private val WATCH_DEVICE = Device(
        manufacturer = "Google",
        model = "Pixel Watch",
        type = Device.TYPE_WATCH
    )

    // Phone
    private val PHONE_DEVICE = Device(
        manufacturer = "Google",
        model = "Pixel 8",
        type = Device.TYPE_PHONE
    )

    // Ring
    private val RING_DEVICE = Device(
        manufacturer = "Oura",
        model = "Ring Gen3",
        type = Device.TYPE_RING
    )

    // Scale
    private val SCALE_DEVICE = Device(
        manufacturer = "Withings",
        model = "Body Comp",
        type = Device.TYPE_SCALE
    )

### Snippets updated

Health Connect guides have been updated wherever new snippets are needed
to adhere to the new metadata requirements. For some examples, refer to the
[Write Data](https://developer.android.com/health-and-fitness/guides/health-connect/develop/write-data) page.

### New metadata methods

Metadata can no longer be directly instantiated, so use one of the
factory methods to get a new instance of metadata. The factory methods verify
that device information is provided when a device or sensor was used to
record the data. For manually entered data, providing device information
remains optional.
Each function has three signature variants:

- `activelyRecorded`

  - `fun activelyRecorded(device: Device): Metadata.`
  - `fun activelyRecorded(clientRecordId: String, clientRecordVersion: Long = 0, device: Device): Metadata`
  - `fun activelyRecordedWithId(id: String, device: Device): Metadata`
- `autoRecorded`

  - `fun autoRecorded(device: Device): Metadata`
  - `fun autoRecorded(clientRecordId: String, clientRecordVersion: Long = 0, device: Device): Metadata`
  - `fun autoRecordedWithId(id: String, device: Device): Metadata`
- `manualEntry`

  - `fun manualEntry(device: Device? = null): Metadata`
  - `fun manualEntry(clientRecordId: String, clientRecordVersion: Long = 0, device: Device? = null): Metadata`
  - `fun manualEntryWithId(id: String, device: Device? = null): Metadata`
- `unknownRecordingMethod`

  - `fun unknownRecordingMethod(device: Device? = null): Metadata`
  - `fun unknownRecordingMethod(clientRecordId: String, clientRecordVersion: Long = 0, device: Device? = null): Metadata`
  - `fun unknownRecordingMethodWithId(id: String, device: Device? = null): Metadata`

For more information, see the [Android Open Source Project](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:health/connect/connect-client/src/main/java/androidx/health/connect/client/records/metadata/Metadata.kt).

### Testing data

Use the [Testing Library](https://developer.android.com/health-and-fitness/guides/health-connect/test/unit-tests) and
[`MetadataTestHelper`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:health/connect/connect-testing/src/main/java/androidx/health/connect/client/testing/MetadataTestHelper.kt) to mock expected metadata
values:  

    private val TEST_METADATA =
        Metadata.unknownRecordingMethod(
            clientRecordId = "clientId",
            clientRecordVersion = 1L,
            device = Device(type = Device.TYPE_UNKNOWN),
        ).populatedWithTestValues(id = "test")

This simulates the behavior of the Health Connect implementation,
which automatically populates these values during record insertion.

For the testing library, you need to add this Health Connect SDK dependency to
your module-level `build.gradle` file:  

    dependencies {
      testImplementation "androidx.health.connect:connect-testing:1.0.0-alpha02"
    }

## Upgrade the library

The main steps you need to perform are:

1. Upgrade your library to 1.1.0-alpha12.

2. When building the library, compilation errors will be thrown where
   new metadata is needed. To resolve these errors and complete migration,
   verify you make the following changes:

   - It is mandatory to specify a recording method when constructing a `Record`. This is done by using one of the factory methods provided in `Metadata`, such as `Metadata.manualEntry()` or `Metadata.activelyRecorded(device = Device(...))`.
   - For data recorded by a device, it is mandatory to specify a device type, such as `Device.TYPE_WATCH` or `Device.TYPE_PHONE`.
3. If your app writes extended device types, gate them behind
   `FEATURE_EXTENTED_DEVICE_TYPES` to avoid unexpected `TYPE_UNKNOWN` on devices
   where the feature isn't available.