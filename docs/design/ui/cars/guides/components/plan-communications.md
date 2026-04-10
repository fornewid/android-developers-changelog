---
title: https://developer.android.com/design/ui/cars/guides/components/plan-communications
url: https://developer.android.com/design/ui/cars/guides/components/plan-communications
source: md.txt
---

# Plan communications

There are multiple ways for your app to communicate with drivers. Learn which method is best for each use case so you can choose the right one every time.

Your app can communicate with users through:

- Toasts
- Notifications
- Navigation alerts
- Message-oriented templates
- [Voice input](https://developer.android.com/design/ui/cars/guides/components/plan-communications#voice-input)

For voice input, follow[best practices](https://developer.android.com/design/ui/cars/guides/components/plan-communications#best-practices)to protect user privacy and brand the experience.

## Communication methods

Choose the most appropriate communication method for each use case. See the following examples for inspiration:

|                                                                     Communication method                                                                     |                                                                                                Format                                                                                                |                                       Example use case                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [Message template](https://developer.android.com/design/ui/cars/guides/templates/message-template)                                                           | Brief message with icon or image + up to 4 actions                                                                                                                                                   | Error message                                                                                 |
| [Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template)                                                 | Long, scrollable message to be read while parked                                                                                                                                                     | Legal text for permissions                                                                    |
| [Toast](https://developer.android.com/guide/topics/ui/notifiers/toasts)                                                                                      | Dialog showing very brief text                                                                                                                                                                       | Telling the user to continue a flow on the phone when parked                                  |
| [Voice input](https://developers.google.com/cars/design/create-apps/apps-for-drivers/plan-communications#voice)                                              | Input provided through microphone and recorded by the app                                                                                                                                            | User makes a request of the app while driving                                                 |
| [Navigation alerts](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/navigation-template#alerts)                             | Brief message with optional actions on the[Navigation template](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/navigation-template)(doesn't block navigation info) | Suggesting a change in route                                                                  |
| [Heads-up notifications (HUNs)](https://developers.google.com/cars/design/android-auto/product-experience/system-ui/notifications#heads-up_notification_hun) | Temporary notification card with brief text + up to 2 actions, able to deep-link to relevant parts of the app                                                                                        | Highly important update worth disrupting other tasks (use outside of the Navigation template) |

More about notifications:

- Vehicle OEMs can decide whether to display navigation HUNs in the AAOS version of your app.
- For details about types of notifications used by navigation apps, see[Navigation notifications: Turn-by-turn (TBT) and regular](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#notifications).
- For technical details about displaying notifications in Android for Cars, see[Display notifications](https://developer.android.com/training/cars/apps#display-notifications).
- For additional details relevant to AAOS, visit[Notifications on Android Automotive OS](https://developer.android.com/training/cars/notifications).

## Voice input details

The voice input feature lets apps access the car's microphone to gather audio input for in-app voice assistants.purposes such as creating their own in-app assistant.

### How it works

1. The user requests voice input (via the microphone icon in the action strip, in this case).
2. An overlay appears, signaling that recording is in process.
3. Users can stop the recording by dismissing the overlay, or they can stop talking, at which point the app should stop recording.

For a sample flow showing this process, see[Communicate with the app by voice](https://developer.android.com/design/ui/cars/guides/ux-requirements/communicate-app-by-voice).
![Navigation template with voice input icon](https://developer.android.com/static/images/design/ui/cars/components/voice-input.png)A voice input icon informs the user that they can provide voice input.

### Best practices

Keep these best practices in mind as you plan communication methods for your app:

- **Get permission first.**Make sure the user has granted permission for your app to access the car's microphone (ideally before the drive starts).
- **Provide an entry point.**Give the user a way to start voice input, such as a microphone icon in the action strip. Then, wait for them to initiate the process.
- **Brand the experience.**Make it clear that your in-app assistant is specific to your app.
- **Stop recording when the user stops talking.**