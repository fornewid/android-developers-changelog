---
title: https://developer.android.com/design/ui/cars/guides/ux-requirements/communicate-app-by-voice
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/communicate-app-by-voice
source: md.txt
---

# Communicate with the app by voice

To support building features such as an in-app digital assistant, the Android for Cars App Library now lets you use the car's microphone to record[voice input](https://developer.android.com/design/ui/cars/guides/components/plan-communications)from the driver.  
When recording is in progress, an indicator appears on the screen. The recording is sent directly to the app (not saved within the library) for processing and follow-up actions.
![](https://developer.android.com/static/images/design/ui/cars/foundations/voice-actions-1.png)In this example, the microphone icon is shown in the top right corner of the screen.

<br />

## Sample flow

|                                                 User action                                                 |                                                                                                                                              Where action is performed                                                                                                                                              | Step count after action |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user taps the app's microphone button (on the action strip) to start voice input.                       | Navigation template ![Navigation template during the user's journey with microphone, volume, and settings buttons in the action strip](https://developer.android.com/static/images/design/ui/cars/foundations/voice-1.png)                                                                                          | 1                       |
| While the user is talking, a visual indicator signals that recording is in progress.                        | Navigation template ![Navigation template during the user's journey with voice overlay](https://developer.android.com/static/images/design/ui/cars/foundations/voice-2.png)**Note:**Because the content of the template does not change, this is considered a refresh and does not add to the step count.           | 1                       |
| A toast message tells the user that the app has understood and responded to the user's spoken instructions. | Navigation template (refresh) ![Navigation template during the user's journey with toast message](https://developer.android.com/static/images/design/ui/cars/foundations/voice-3.png)**Note:**Because the content of the template does not change, this is considered a refresh and does not add to the step count. | 1                       |