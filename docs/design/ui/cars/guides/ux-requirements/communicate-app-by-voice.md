---
title: Communicate with the app by voice  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/communicate-app-by-voice
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Communicate with the app by voice Stay organized with collections Save and categorize content based on your preferences.




To support building features such as an in-app digital assistant, the Android
for Cars App Library now lets you use the car's microphone to record
[voice input](/design/ui/cars/guides/components/plan-communications) from the driver.

When recording is in progress, an indicator appears on the screen. The
recording is sent directly to the app (not saved within the library)
for processing and follow-up actions.

![](/static/images/design/ui/cars/foundations/voice-actions-1.png)


In this example, the microphone icon is shown in the top right
corner of the screen.

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user taps the app's microphone button (on the action strip) to start voice input. | Navigation template Navigation template during the user's journey with microphone,       volume, and settings buttons in the action strip | 1 |
| While the user is talking, a visual indicator signals that recording is in progress. | Navigation template Navigation template during the user's journey with voice overlay **Note:** Because the content of the template does not change, this is considered a refresh and does not add to the step count. | 1 |
| A toast message tells the user that the app has understood and responded to the user's spoken instructions. | Navigation template (refresh) Navigation template during the user's journey with toast message **Note:** Because the content of the template does not change, this is considered a refresh and does not add to the step count. | 1 |