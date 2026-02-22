---
title: Voice input  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/voice-input
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Voice input Stay organized with collections Save and categorize content based on your preferences.




The voice input feature lets apps access the car's microphone to gather audio
input for purposes such as creating an in-app assistant.

## How voice input works

1. The user requests voice input (via the microphone icon in the action strip,
   in this case).
2. An overlay appears, signaling that recording is in process.
3. Users can stop the recording by dismissing the overlay, or they can stop
   talking, at which point the app should stop recording.

![Navigation template with voice input icon](/static/images/design/ui/cars/components/voice-input.png)


A voice input icon appears to inform the user that they can
provide voice input.

A voice input icon appears to inform the user that they can provide voice input.

For a sample flow showing this process, see
[Communicate with the app by voice](/design/ui/cars/guides/ux-requirements/communicate-app-by-voice).

## Best practices

* **Get permission first.** Make sure the user has granted permission for your
  app to access the car's microphone (ideally before the drive starts).
* **Provide an entry point.** Give the user a way to start voice input, such
  as a microphone icon in the action strip. Then, wait for them to initiate
  the process.
* **Brand the experience.** When creating an in-app assistant, make clear that
  it's an assistant specific to your app.
* **Stop when the user does.** When the user is done talking, stop recording.