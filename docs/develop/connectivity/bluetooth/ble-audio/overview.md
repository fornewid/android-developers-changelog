---
title: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/overview
url: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/overview
source: md.txt
---

> [!NOTE]
> **Note:** [`isLeAudioSupported()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#isLeAudioSupported()) and [`isLeAudioBroadcastSourceSupported()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#isLeAudioBroadcastSourceSupported()) will return `True` if the device supports BLE Audio.

[Video](https://www.youtube.com/watch?v=cXl9fUyW6FM)

Bluetooth Low Energy Audio (LEA) ensures that users can receive high fidelity audio without sacrificing battery life, and lets them seamlessly switch between different use cases. Android 13 (API level 33) includes built-in support for LEA.

Most LEA headsets will be dual mode until the LEA source device market share grows. Users should be able to pair and set up both transports on their dual mode headsets.

## Use cases

You may want to integrate LEA for the following use cases:

- Sharing audio: Users can simultaneously share multiple audio streams to one or more audio sink devices. Audio is synchronized between the source device and connected devices.

- Broadcast Audio: Users can broadcast audio to friends and family, while also connecting to public broadcasts for information, entertainment, or accessibility.

- LC3 audio codec support: This is the default audio codec and replaces the SBC codec used for A2DP (media) and mSBC in HFP (voice). LC3 is more efficient, reconfigurable, and higher quality.

- Audio sampling improvements: Headsets can maintain high output audio quality when using microphones. Bluetooth classic lowers audio quality when using Bluetooth microphones. With BLE Audio, input and output sampling can reach 32 kHz.

- Stereo microphone: Hearables can record audio with stereo microphones for spatial audio enhancements.

- Hearing Aid Profile (HAP) support: HAP offers users greater accessibility and usage than previous ASHA protocols. Users can use their hearing aids for phone calls and VoIP applications.

- Enhanced Attribute protocol (EATT) support: EATT allows developers to send multiple commands at once to paired hearables.

## Key scenarios

There are four main categories of use cases:

1. Conversational: Dialer and VoIP applications that require low-latency communication routing offer high quality audio and less battery usage.

2. Gaming: Concurrent microphone and high fidelity playback allows for games to stream high quality audio to hearables. A gaming app can access BLE audio input when a game arms the Bluetooth microphone as ready to use. Then, when a player starts a live conversation with a peer player, the game app can use the microphone data without delay.

3. Media: Media applications are allowed to set the audio manager's preferred device. The user can override this by changing their preferred device from within the system's settings.

4. Accessibility: Hearing aids that support BLE Audio can now use the microphone, allowing users to continually use their hearing aids for a call.

## BLE Audio APIs and methods

The following APIs and methods are required to support BLE Audio hearables:

### AudioManager

- [`setCommunicationDevice()`](https://developer.android.com/reference/android/media/AudioManager#setCommunicationDevice(android.media.AudioDeviceInfo)) selects the audio device that should be used for communication use cases, for instance voice or video calls. This method can be used by voice or video chat applications to select a different audio device other than the one selected by default by the platform. This API replaces the following deprecated APIs: [`startBluetoothSco()`](https://developer.android.com/reference/android/media/AudioManager#startBluetoothSco()), [`stopBluetoothSco()`](https://developer.android.com/reference/android/media/AudioManager#stopBluetoothSco()), and [`setSpeakerphoneOn()`](https://developer.android.com/reference/android/media/AudioManager#setSpeakerphoneOn(boolean)).
- [`clearCommunicationDevice()`](https://developer.android.com/reference/android/media/AudioManager#clearCommunicationDevice()) is called after your app finishes a call or session to help ensure the user has a great experience when moving between different applications.

### BluetoothProfile

- [`BluetoothLeAudio`](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudio) controls the bluetooth service via proxy object.

### Telecom InCallService

- [`InCallService#requestCallEndpointChange()`](https://developer.android.com/reference/android/telecom/InCallService#requestCallEndpointChange(android.telecom.CallEndpoint,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Cjava.lang.Void,android.telecom.CallEndpointException%3E)) replaces the deprecated [`InCallService.setAudioRoute()`](https://developer.android.com/reference/android/telecom/InCallService#setAudioRoute(int)) and [`InCallService.requestBluetoothAudio()`](https://developer.android.com/reference/android/telecom/InCallService#requestBluetoothAudio(android.bluetooth.BluetoothDevice)) APIs, to allow apps request audio routing to a specific [`CallEndpoint`](https://developer.android.com/reference/android/telecom/CallEndpoint). Clients should not define their own [`CallEndpoint`](https://developer.android.com/reference/android/telecom/CallEndpoint) when requesting a change. Instead, the new endpoint should be one of the valid endpoints provided by [`InCallService.onAvailableCallEndpointsChanged(java.util.List)`](https://developer.android.com/reference/android/telecom/InCallService#onAvailableCallEndpointsChanged(java.util.List%3Candroid.telecom.CallEndpoint%3E)).
- [`CallEndpoint.TYPE_BLUETOOTH`](https://developer.android.com/reference/android/telecom/CallEndpoint#TYPE_BLUETOOTH) directs the audio stream through Bluetooth.
- These forementioned [`InCallService`](https://developer.android.com/reference/android/telecom/InCallService) APIs are designed to be used by the default phone app on an Android phone, or other calling surfaces like wearables, automobiles, or other bluetooth devices that may want to influence audio routing.

### Telecom CallControl

- The new [`CallControl`](https://developer.android.com/reference/android/telecom/CallControl) class is introduced in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels) to replace [`Connection`](https://developer.android.com/reference/android/telecom/Connection) and [`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService) for VoIP applications only.
- [`CallControl.requestCallEndpointChange()`](https://developer.android.com/reference/android/telecom/CallControl#requestCallEndpointChange(android.telecom.CallEndpoint,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Cjava.lang.Void,android.telecom.CallException%3E)) also requests a [`CallEndpoint`](https://developer.android.com/reference/android/telecom/CallEndpoint) change. This API replaces the deprecated [`Connection.requestBluetoothAudio()`](https://developer.android.com/reference/android/telecom/Connection#requestBluetoothAudio(android.bluetooth.BluetoothDevice)) and [`Connection.setAudioRoute()`](https://developer.android.com/reference/android/telecom/Connection#setAudioRoute(int)) APIs.
- Besides the updated Telecom platform APIs, the [Telecom Jetpack library](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom) is highly recommended when building voice and/or video calling applications. This library can greatly simplify the integration process and improve VoIP calling across all Android surfaces.

### Audio Device Info

- [`AudioDeviceInfo.TYPE_BLE_HEADSET`](https://developer.android.com/reference/android/media/AudioDeviceInfo#TYPE_BLE_HEADSET) describes the audio device type as a LEA device. Used for identifying if the hearable device is a LEA device.

### Audio Recorder

- [`setPreferredDevice()`](https://developer.android.com/reference/android/media/AudioRecord#setPreferredDevice(android.media.AudioDeviceInfo)) sets the preferred device for audio routing to use. The user can override this in the system settings.

### Bluetooth Adapter

- [`isLeAudioSupported()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#isLeAudioSupported%28%29) returns if the platform's hardware supports LEA.
- [`isLeAudioBroadcastSourceSupported()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#isLeAudioBroadcastSourceSupported()) returns if the platform's hardware supports LEA.

## Guides based on use case

Below are guidelines for implementing LEA based on specific use cases.

### Voice communication applications

Voice communication applications have the choice of managing audio routing and
device state by self managing their state or by using the Telecom API which does
the audio routing and state logic for you.

- Self-Managed: For applications that are currently using [`startBluetoothSco()`](https://developer.android.com/reference/android/media/AudioManager#startBluetoothSco()),
  [`stopBluetoothSco()`](https://developer.android.com/reference/android/media/AudioManager#stopBluetoothSco()),
  and [`setSpeakerphoneOn()`](https://developer.android.com/reference/android/media/AudioManager#setSpeakerphoneOn(boolean))
  or want to self-manage the audio routing state, follow the
  [Audio Manager self-managed call guide](https://developer.android.com/develop/connectivity/bluetooth/ble-audio/audio-manager).

- Managed: Use the [Telecom Jetpack library](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom)
  or [Telecom platform APIs](https://developer.android.com/develop/connectivity/bluetooth/ble-audio/overview#telecom) to create an audio or video
  calling application.

This two solutions make you quickly and easily control audio routing and switch
between Bluetooth devices. For more information, see the
[Telecom managed calls guide](https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls).

### Audio recording applications

- Media Recorder: When recording audio using the Media Recorder, you can now record in stereo if the bluetooth hearable supports LEA. Check out the [Audio recording guide](https://developer.android.com/develop/connectivity/bluetooth/ble-audio/audio-recording).

## LE Audio (LEA) headset recommendations

As more LEA headsets are released, we have discovered issues in real-world
testing that degrade the user experience. The specification does not cover all
of these issues. The following table provides a list of recommendations that
LEA headset manufacturers should follow to improve end-to-end experience for
Android users.

| Description | Context |
|---|---|
| Support **Cross Transport Key Derivation (CTKD)** for dual-mode headsets: - Support key derivation for both Classic-to-LE pairing and LE-to-Classic pairing. | Most new LEA headsets will be dual-mode until the LEA source device market share grows. It's important that users are able to pair their dual-mode headsets seamlessly and to set up both transports. This is also important for Google Fast Pair. |
| Support **Targeted Announcements (TAs)** if you want your LEA headsets to reliably reconnect to the source devices. LE audio earbuds should use TAs to request an incoming connection from the central devices. Will be added to upcoming BT SIG. | Unlike in BR/EDR's paging model where a connection can be initiated by either the phone or the headset, a connection in LEA must be initiated by the central device. Currently, many headsets do not use TAs, which means that the central device might not be able to reconnect to the peripheral without adding it to an Allowlist. However, an allowlist workaround might prevent the headset from connecting to a different central device. Therefore, it's important for LEA headsets to support TAs properly so that the central device can reliably reconnect without workarounds that might break multi-point connections. |
| **Optimized discoverability for dual mode earbuds** - **Primary earbud - BR/EDR component** should advertise using its public address and enable inquiry and page scan with its name available through EIR, and set LE audio bit 14 to 1 in the Major Service Classes of Class of Device (CoD). - **Primary earbud - LE component**: The primary earbud should perform a Connectable and Discoverable (either Limited or General) advertisement using the same Public Address as the BR/EDR Component, and the same Complete Local Name as the BR/EDR component, with its Appearance Category set as an appropriate Appearance Category that matches the remote device type with the expectation that the central device will use this information to adjust its UI and audio routing policies. - **Secondary Earbud - LE only** : The secondary earbud should perform a Connectable, Non-Discoverable advertisement with its Appearance Category set as an appropriate Appearance Category that matches the remote device type with the expectation that the central device will use this information to adjust its UI and audio routing policies The earbuds should dynamically elect a leader from the CSIP group to be the primary device. If the earbud is dual mode, the primary device must be dual mode to ensure that both LE and Classic functionalities work correctly after pairing. | This prevents dual-mode LEA earbuds from appearing as duplicate entries in Bluetooth settings, which might confuse users and compromise the LEA pairing experience. The dynamic leader election is especially important for dual-mode devices that are paired incrementally. For example, if only one earbud is available at initial pairing, then it should present itself as a dual-mode device. When a user pairs with the second earbud later on, they only need to pair with the LE component, and CSIP will make sure they are grouped together on Android. Identity address is recommended during pairing because the BR/EDR component already exposes the device's public address to nearby devices. |
| Support **Enhanced Attribute Protocol (EATT)**. | Reduces pairing and connection latency. |
| Support **Robust GATT caching.** | Reduces connection latency, especially for TWS buds. |
| Support **connection subrating**. | Allows for more flexible packet scheduling and potential battery savings. |
| Ensure that during pre- and post-processing for both playback and capture, **the signal processing pipeline can operate at 16, 24, 32, and 48 kHz as well as supporting higher frequencies**. | Takes advantage of the higher sampling rates supported for LEA call or VoIP capture paths and media playback. |
| Support **LE Power Control** | Better power management |

### Context Type support

| Description | Context |
|---|---|
| Use all of the context types specified in [Assigned Numbers 6.12.3](https://www.bluetooth.com/specifications/assigned-numbers/) unless the headset explicitly does not support a given context type. | For example, if context type "Game" is not supported, then Android will send game sounds. In particular, note that the "Unspecified" context type doesn't mean "any context type", and it doesn't cover unsupported context types. |
| When the central device interacts with the peripheral device's ASCS, the peripheral must connect to the central device's MCS and TBS. The central device might not always use LE audio as the streaming route because it might fall back to using A2DP or HFP. The peripheral device can use ASCS interaction as an indication of whether the central device will use LE audio for streaming. A few examples of ASCS interactions are read, write, and register for notification. |

> [!NOTE]
> **Note:** In keeping with the specification, headsets can remove context types from the Available Context Types at any time and to all the connected devices, even a device which is currently streaming a given context type. It is recommended that the headset does not remove the currently streaming context type from the Available Context Types on the device which is streaming that context type.