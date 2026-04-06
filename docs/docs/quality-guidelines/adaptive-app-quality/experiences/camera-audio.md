---
title: Camera • audio  |  App quality  |  Android Developers
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Camera • audio Stay organized with collections Save and categorize content based on your preferences.



Premium devices often serve as hubs for content creation and communication.
Enable users to seamlessly switch between built-in and external camera and audio
hardware for a versatile and professional user experience.

## Guidelines

Enable camera and audio hardware selection.

### Camera

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Camera\_Switcher | [T-Camera\_Switcher](#T-Camera_Switcher) | App includes a camera switcher to toggle between the device's built-in cameras and external cameras. |

### Audio

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Audio\_Switcher | [T-Audio\_Switcher](#T-Audio_Switcher) | Apps using the microphone or speaker include an audio switcher to toggle between the device's built-in audio devices and external peripherals, for example, headphones or USB microphones. |
| Audio\_Background\_Playback | [T-Audio\_Background\_Playback](#T-Audio_Background_Playback) | App supports [background playback](/media/platform/mediaplayer/background) whether the app is visible or not to the user.   * Not visible — The app is in the background hidden by other apps or the lock screen * Visible — The app can be seen by the user but the app is not in focus, for example, in split-screen mode or desktop windowing mode   Non-visible background apps must use a foreground service to prevent the system from killing the app process once the app has lost focus. Visible but unfocused apps don't require a foreground service to ensure the app process continues to run. Always use a foreground service with your audio app to ensure it continues playing in all device states, including when the device is locked. If the app is not visible, it must also display a persistent, non‑dismissible notification in the status bar or on the lock screen to inform the user that the app is running. See [Playing nicely with media controls](https://android-developers.googleblog.com/2020/08/playing-nicely-with-media-controls). Restricting audio background playback to premium subscription tiers is in compliance with this quality guideline. |

## Tests

To ensure your app provides a professional and versatile camera and audio
experience, complete the following tests.

### Camera

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Camera\_Switcher | [Camera\_Switcher](#Camera_Switcher) | Connect an external camera. Use the app's camera switcher to toggle between the device's built-in cameras and the external camera. Verify that the camera preview updates correctly for each selected camera. |

### Audio

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Audio\_Switcher | [Audio\_Switcher](#Audio_Switcher) | Connect an external audio device, such as headphones or a USB microphone. Use the app's audio switcher to toggle between the device's built-in audio and the external peripheral. Verify that audio input and output are correctly routed to the selected device. |
| T-Audio\_Background\_Playback | [Audio\_Background\_Playback](#Audio_Background_Playback) | Initiate audio playback. Interact with another *non‑audio* app as the foreground app. Verify that your app continues playing without stutters or pauses. If your app is not visible, verify that a notification is displayed in the status bar.  Lock your device and wait for at least a minute to verify that the system doesn't kill the process to save battery. Verify that the app provides a lock screen notification. Use the play and pause buttons directly from the lock screen notification to confirm that the foreground service is communicating with the app.  Unlock the screen. Verify that the app continues playback. For non‑visible apps, verify that a notification appears in the status bar.  Refocus the app as the foreground app and verify that playback continues without stutters or pauses. |