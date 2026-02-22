---
title: https://developer.android.com/design/ui/ai-glasses/guides/interaction/earcons
url: https://developer.android.com/design/ui/ai-glasses/guides/interaction/earcons
source: md.txt
---

Earcons, audio icons, provide brief audio cues or feedback to the user. Glasses provide earcons for common interactions.

Due to their cognitive load to learn, similar to visual icons, make sure to use thoughtfully, avoiding contradicting established sounds provided by the system.

- Avoid earcons that need explanation that could be replaced by natural language phrase.
- Avoid creating custom earcons that mimic system sounds, as they could confuse your users.
- Users commonly learn earcons in context of an action.
- Earcons should be simplified and intuitive.
- Earcons are less descriptive compared to audio alerts.

### System earcons

Common system-wide sounds are provided by default. These can include:

- Finger press
- Notification alerts
- Sleep
- Disconnection
- Volume
- Camera capture

### App earcons

The following are sounds your app should consider including, as they are not provided by default:

|   Action    |                                                            Use                                                            |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| App open    | An earcon to greet your user as your app opens. A verbal greeting is appropriate if your app is primarily conversational. |
| Swipe       | For unique swipe actions                                                                                                  |
| Mic muted   | Microphone has been muted                                                                                                 |
| Mic unmuted | Microphone is unmuted                                                                                                     |
| App Exit    | User exits app. Provide a summary of their activity before closing the app to wrap up their session.                      |