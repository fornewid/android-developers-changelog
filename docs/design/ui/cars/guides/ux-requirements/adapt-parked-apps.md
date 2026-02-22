---
title: https://developer.android.com/design/ui/cars/guides/ux-requirements/adapt-parked-apps
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/adapt-parked-apps
source: md.txt
---

# Adapt parked apps

Some tasks, like watching videos or engaging with longer task flows, are only available while parked. This guidance will show you how to design for both scenarios.

Video apps Android Automotive OS (AAOS) lets app developers easily adapt their existing video apps for car screens, creating an experience that drivers and passengers can enjoy while parked.

To learn more about the UX requirements and best practices for designing video apps for cars, see[Video in cars -- UX Guidelines](https://developers.google.com/static/cars/design/create-apps/video-apps/Video-in-Cars-Developers.pdf).
![](https://developer.android.com/static/images/design/ui/cars/foundations/video-overview.png)

For app developers, adapting video apps for the car screen involves the following steps:

- Optimize design for the large screen
- Support landscape and portrait versions
- Use[MediaSession](https://developer.android.com/media/legacy/mediasession)
- Resume video playback from pause

OEMs can customize how these video experiences are presented in their vehicles, and ensure that drivers can't watch videos while driving.

Longer task flows

Some tasks may require too much attention for users to complete while driving. In those cases, use parked-only templates or enable your app to pause the task during the drive and continue it while parked.

The following templates are designed to accommodate parked scenarios:

- [List template](https://developer.android.com/design/ui/cars/guides/templates/list-template)(shows more text when parked than while driving)
- [Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template)(parked only)
- [Sign-in template](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template)(parked only)

To enable[task flows](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#short)longer than 5 steps while parked, use the[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits)feature. This feature can also pause a task after 5 steps while driving and continue it when parked.