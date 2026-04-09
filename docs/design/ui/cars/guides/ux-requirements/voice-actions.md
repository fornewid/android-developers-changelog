---
title: https://developer.android.com/design/ui/cars/guides/ux-requirements/voice-actions
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/voice-actions
source: md.txt
---

# Plan voice actions

To support building features such as an in-app digital assistant, the Android for Cars App Library lets you use the car's microphone to record voice input from the driver. Supporting voice actions helps users complete tasks by talking to Google Assistant, so they can keep their eyes on the road.

When recording is in progress, an indicator appears on the screen. The recording is sent directly to the app (not saved within the library) for processing and follow-up actions.
![](https://developer.android.com/static/images/design/ui/cars/foundations/voice-actions-1.png)

Google and car makers control how users invoke Google Assistant, typically using a hotword ("Hey, Google" or "Hey, G"), steering wheel button, or onscreen affordance. Once invoked, Google Assistant can recognize a variety of request types, including the following:

- Play, pause, or skip app-supported categories of media
- Read and respond to messages
- Make a call
- Get driving directions
- And much more

To optimize the voice experience for users, you need to:

- **Decide which voice action categories to support.**Possible categories for voice actions in a media app could include genre, artist, album, playlist, and title. Choose categories that make sense for your app.

- **Anticipate non-specific requests.**Decide how you want your app to respond to requests that don't ask for specific content, such as "Play some music" or "Send a text message."

| **Note:** For details about how to build support for voice actions into your app, consult Support voice actions and Google Assistant and media apps.

## Voice action requirements

| Requirement level |                                    Requirements                                     |
|-------------------|-------------------------------------------------------------------------------------|
| SHOULD            | Support voice actions for all media categories that are appropriate for their apps. |

## Sample flow

|                                                 User action                                                 |                                                                                                                                              Where action is performed                                                                                                                                              | Step count after action |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user taps the app's microphone button (on the action strip) to start voice input.                       | Navigation template ![Navigation template during the user's journey with microphone, volume, and settings buttons in the action strip](https://developer.android.com/static/images/design/ui/cars/foundations/voice-1.png)                                                                                          | 1                       |
| While the user is talking, a visual indicator signals that recording is in progress.                        | Navigation template ![Navigation template during the user's journey with voice overlay](https://developer.android.com/static/images/design/ui/cars/foundations/voice-2.png)**Note:**Because the content of the template does not change, this is considered a refresh and does not add to the step count.           | 1                       |
| A toast message tells the user that the app has understood and responded to the user's spoken instructions. | Navigation template (refresh) ![Navigation template during the user's journey with toast message](https://developer.android.com/static/images/design/ui/cars/foundations/voice-3.png)**Note:**Because the content of the template does not change, this is considered a refresh and does not add to the step count. | 1                       |