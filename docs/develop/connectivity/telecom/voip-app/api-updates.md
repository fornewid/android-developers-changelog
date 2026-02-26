---
title: https://developer.android.com/develop/connectivity/telecom/voip-app/api-updates
url: https://developer.android.com/develop/connectivity/telecom/voip-app/api-updates
source: md.txt
---

Android 14 introduced API updates accompanied by user experience changes to
audio routing behavior for Bluetooth LE Audio (LEA) devices, including hearing
aids. These changes impacted how VoIP apps manage audio output selection. This
document provides essential information for developers to adapt their VoIP apps
to these changes and ensure a seamless user experience.

## Behavior change in Android 14

- **LEA device routing:** LEA devices are now enabled by default on Pixel phones and AOSP. However, to actively recognize and select LEA devices as audio output, apps must use the new APIs introduced in API level 31.
- **Hearing aid routing:** Previously, audio would always default to hearing aids, even if the user explicitly selected the earpiece. In Android 14, hearing aids are now presented as one of the available audio output options, requiring explicit selection by the user.

## Rationale for the change

- Prior to Android 12, there was no API to explicitly use hearing aids for calls, leading to audio always defaulting to hearing aids when connected.
- This made it difficult for users to switch from hearing aids to earpieces without disconnecting their hearing aids.
- The same issue applied to Bluetooth LE Audio headsets.

To address these challenges, Android 14 introduced changes to provide VoIP apps
with more control over audio routing and ensure consistent behavior across
Bluetooth accessories.

## Key changes in Android 14

- **Generic APIs for route selection:** Android 12 introduced [`AudioManager.setCommunicationDevice`](https://developer.android.com/develop/connectivity/telecom/voip-app/reference/android/media/AudioManager#getCommunicationDevice()) to allow apps to specify audio routes, including hearing aids and LEA devices. However, in Android 12 and 13, hearing aids were not visible as devices, limiting the usefulness of this API.
- **Hearing aid visibility:** In Android 14, hearing aids are now visible as devices, enabling apps to provide UI elements for users to select their preferred audio output.
- **API Deprecations:** Several APIs related to audio routing have been deprecated in Android 14. Developers must migrate to the new APIs introduced in API level 31 to manage audio output selection effectively.

## Required developer actions

- **Highly Recommended:** Migrate to [Telecom Jetpack Library](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom). If possible, migrate your VoIP app to the Telecom Jetpack library for streamlined audio routing management.
- Use [`setCommunicationDevice()`](https://developer.android.com/reference/android/media/AudioManager#getCommunicationDevice()) or the latest APIs (listed below) if migration is not feasible.

## Deprecated APIs and their replacements

| Deprecated in Android 14 | New APIs |
|---|---|
| [AudioManager.isBluetoothScoOn()](https://developer.android.com/reference/android/media/AudioManager#isBluetoothScoOn()) | [AudioManager.getCommunicationDevice()](https://developer.android.com/reference/android/media/AudioManager#getCommunicationDevice()) |
| [AudioManager.isSpeakerphoneOn()](https://developer.android.com/reference/android/media/AudioManager#isSpeakerphoneOn()) | [AudioManager.getCommunicationDevice()](https://developer.android.com/reference/android/media/AudioManager#getCommunicationDevice()) |
| [AudioManager.setSpeakerphoneOn()](https://developer.android.com/reference/android/media/AudioManager#setSpeakerphoneOn(boolean)) | [AudioManager.setCommunicationDevice()](https://developer.android.com/reference/android/media/AudioManager#setCommunicationDevice(android.media.AudioDeviceInfo)) |
| [AudioManager.startBluetoothSco()](https://developer.android.com/reference/android/media/AudioManager#startBluetoothSco()) | [AudioManager.setCommunicationDevice()](https://developer.android.com/reference/android/media/AudioManager#setCommunicationDevice(android.media.AudioDeviceInfo)) |
| [AudioManager.stopBluetoothSco()](https://developer.android.com/reference/android/media/AudioManager#stopBluetoothSco()) | [AudioManager.clearCommunicationDevice()](https://developer.android.com/reference/android/media/AudioManager#clearCommunicationDevice()) |
| [Connection.getCallAudioState()](https://developer.android.com/reference/android/telecom/Connection#getCallAudioState()) | **Jetpack:** [CallControlScope.getAvailableEndpoints()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getAvailableEndpoints()) [CallControlScope.getCurrentCallEndpoint()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getCurrentCallEndpoint()) [CallControlScope#isMuted()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getIsMuted()) **Platform:** [CallEventCallback.onAvailableCallEndpointsChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onAvailableCallEndpointsChanged(java.util.List%3Candroid.telecom.CallEndpoint%3E)) [CallEventCallback.onCallEndpointChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onCallEndpointChanged(android.telecom.CallEndpoint)) [CallEventCallback.onMuteStateChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onMuteStateChanged(boolean)) |
| [Connection.onCallAudioStateChanged()](https://developer.android.com/reference/android/telecom/Connection#onCallAudioStateChanged(android.telecom.CallAudioState)) | **Jetpack:** [CallControlScope.getAvailableEndpoints()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getAvailableEndpoints()) [CallControlScope.getCurrentCallEndpoint()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getCurrentCallEndpoint()) [CallControlScope#isMuted()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getIsMuted()) **Platform:** [CallEventCallback.onAvailableCallEndpointsChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onAvailableCallEndpointsChanged(java.util.List%3Candroid.telecom.CallEndpoint%3E)) [CallEventCallback.onCallEndpointChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onCallEndpointChanged(android.telecom.CallEndpoint)) [CallEventCallback.onMuteStateChanged()](https://developer.android.com/reference/android/telecom/CallEventCallback#onMuteStateChanged(boolean)) |
| [Connection.requestBluetoothAudio()](https://developer.android.com/reference/android/telecom/Connection#requestBluetoothAudio()) | **Jetpack:** [CallControlScope#requestEndpointChange()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#requestEndpointChange(androidx.core.telecom.CallEndpointCompat)) **Platform:** [CallControl#requestCallEndpointChange()](https://developer.android.com/reference/android/telecom/CallControl#requestCallEndpointChange(android.telecom.CallEndpoint,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Cjava.lang.Void,android.telecom.CallException%3E)) |
| [Connection.setAudioRoute()](https://developer.android.com/reference/android/telecom/Connection#setAudioRoute(int)) | **Jetpack:** [CallControlScope#requestEndpointChange()](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#requestEndpointChange(androidx.core.telecom.CallEndpointCompat)) **Platform:** [CallControl#requestCallEndpointChange()](https://developer.android.com/reference/android/telecom/CallControl#requestCallEndpointChange(android.telecom.CallEndpoint,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver%3Cjava.lang.Void,android.telecom.CallException%3E)) |