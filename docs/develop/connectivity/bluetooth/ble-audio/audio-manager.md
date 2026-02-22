---
title: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/audio-manager
url: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/audio-manager
source: md.txt
---

# Audio Manager self-managed call guide

This guide covers communication applications, such as Voice over Internet Protocol (VoIP), that want to self-manage their audio and hearable device state.
| **Note:** Starting in Android 13 (API level 33), applications must migrate from[`AudioManager#startBluetoothSco()`](https://developer.android.com/reference/android/media/AudioManager#startBluetoothSco())to[`AudioManager#setCommunicationDevice()`](https://developer.android.com/reference/android/media/AudioManager#setCommunicationDevice(android.media.AudioDeviceInfo))to support upcoming BLE audio headsets. This change is backward-compatible with Hands-Free Profile (HFP) devices.

## Register audio callback

First, create an`AudioDeviceCallback`, which notifies your app when audio devices connect or disconnect from the device.  

### Kotlin

```kotlin
val audioDeviceCallback: AudioDeviceCallback = object : AudioDeviceCallback() {
  override fun onAudioDevicesAdded(addedDevices: Array) {}
  override fun onAudioDevicesRemoved(removedDevices: Array) {}
}

audioManager.registerAudioDeviceCallback(audioDeviceCallback)
```

### Java

```java
final AudioDeviceCallback audioDeviceCallback = new AudioDeviceCallback() {
  @Override
  public void onAudioDevicesAdded(AudioDeviceInfo[] addedDevices) {
  }

  @Override
  public void onAudioDevicesRemoved(AudioDeviceInfo[] removedDevices) {
    // Handle device removal
  }
};

audioManager.registerAudioDeviceCallback(audioDeviceCallback);
```

## Check for active communication device

The audio manager lets you know which communication device is currently active.  

### Kotlin

```kotlin
val currentCommunicationDevice: AudioDeviceInfo? = audioManager.communicationDevice
```

### Java

```java
AudioDeviceInfo currentCommunicationDevice = audioManager.getCommunicationDevice();
```

Listening for when a communication device has changed lets your app know when routing is applied and the device that you selected is active.  

### Kotlin

```kotlin
val listener =
  OnCommunicationDeviceChangedListener { device -> // Handle changes
    currentCommunicationDevice = device
  }
audioManager.addOnCommunicationDeviceChangedListener(executor, listener)
```

### Java

```java
AudioManager.OnCommunicationDeviceChangedListener listener = 
      new AudioManager.OnCommunicationDeviceChangedListener() {
  @Override
  void onCommunicationDeviceChanged(AudioDeviceInfo device) {
      // Handle changes
      currentCommunicationDevice = device;
  }
};
AudioManager.addOnCommunicationDeviceChangedListener(executor, listener);
```

## Find BLE audio device

Use[`getAvailableCommuncationDevices()`](https://developer.android.com/reference/android/media/AudioManager#getAvailableCommunicationDevices())to see which devices are available for a VoIP call. Use`AudioDeviceInfo`to see if the device is a BLE headset. This example looks for the first device that supports BLE Audio, but you might also consider finding all supported devices and allowing users to choose.  

### Kotlin


    // Get list of currently available devices
    val devices = audioManager.availableCommunicationDevices

    // User choose one of the devices, let's say, TYPE_BLE_HEADSET
    val userSelectedDeviceType = AudioDeviceInfo.TYPE_BLE_HEADSET

    //for the device from the list
    var selectedDevice: AudioDeviceInfo? = null
    for (device in devices) {
      if (device.type == userSelectedDeviceType) {
        selectedDevice = device
        break
      }
    }

### Java


    // Get list of currently available devices
    List<AudioDeviceInfo> devices = audioManager.getAvailableCommunicationDevices();

    // User choose one of the devices, for example, TYPE_BLE_HEADSET
    int userSelectedDeviceType = AudioDeviceInfo.TYPE_BLE_HEADSET;

    // Filter for the device from the list
    AudioDeviceInfo selectedDevice = null;
    for (AudioDeviceInfo device : devices) {
        if (device.getType() == userSelectedDeviceType) {
            selectedDevice = device;
            break;
        }
    }

## Set communication device

After you find a compatible device, use`setCommunicationDevice`to set the device you wish to route to. Checking the result informs your app if the audio manager is trying to set the device or if it encountered an error.  

### Kotlin


    val result = audioManager.setCommunicationDevice(selectedDevice)
    if (!result) {
      // Handle error.
    }
    // Wait for currentCommunicationDevice to become selectedDevice with a timeout (e.g. 30s)

### Java


    boolean result = audioManager.setCommunicationDevice(selectedDevice);
    if (!result) {
      // Handle error.
    }
    // Wait for currentCommunicationDevice to become selectedDevice with a timeout (e.g. 30s)

| **Note:** Once you set a communication device, wait a maximum of 30 seconds. Unless an error occurs,`AudioDeviceCallback`is called within 30 seconds. If an error occurs, call`clearCommuncationDevice()`, and then call`setCommunicationDevice()`.

Now that the BLE Audio device has been set, when placing a call, the audio stream will have the correct audio routing.

## End the session

After your app finishes a call or session, clear the active communication device. This helps ensure the user has a great experience when moving between different applications.  

### Kotlin


    // Clear the selection, ready for next call
    audioManager.clearCommunicationDevice()

### Java


    // Clear the selection, ready for next call
    audioManager.clearCommunicationDevice();