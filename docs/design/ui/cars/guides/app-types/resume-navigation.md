---
title: https://developer.android.com/design/ui/cars/guides/app-types/resume-navigation
url: https://developer.android.com/design/ui/cars/guides/app-types/resume-navigation
source: md.txt
---

# Resume navigation after a stop

Keep the task flow short and ensure trip continuity by offering to let users continue navigation after a stop. Use the message template included in the Map + Content template to create this prompt.

## Sample flow

|                                                                 User action                                                                 |                                                                                                                       Where action is performed                                                                                                                       | Step count after action |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user stops somewhere along their route, then shuts off their car.                                                                       | Navigation template ![Navigation template during navigation](https://developer.android.com/static/images/design/ui/cars/app-cuj/resume_navigation_1.png)                                                                                                              | 1                       |
| The user exits the car.                                                                                                                     | No template                                                                                                                                                                                                                                                           | 1                       |
| The user turns on their car again, and may want to continue to their destination. They see a dialog prompting them to continue their drive. | Message template included in the Map + Content template ![Message template included in the Map + Content template with message with primary and secondary action buttons](https://developer.android.com/static/images/design/ui/cars/app-cuj/resume_navigation_2.png) | 1 (new task)            |
| The user continues along their route.                                                                                                       | Navigation template ![Navigation template during navigation](https://developer.android.com/static/images/design/ui/cars/app-cuj/resume_navigation_3.png)                                                                                                              | 1 (new task)            |