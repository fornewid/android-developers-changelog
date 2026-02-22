---
title: https://developer.android.com/design/ui/cars/guides/foundations/overview
url: https://developer.android.com/design/ui/cars/guides/foundations/overview
source: md.txt
---

# Overview

Designing an app with the Android for Cars App Library involves sequencing templates into task flows and customizing them for the goals of your app and users.

Use the library to create apps in the following categories:

- [Communication apps](https://developer.android.com/design/ui/cars/guides/app-types/communication), such as VoIP calling
- [Navigation apps](https://developer.android.com/design/ui/cars/guides/app-types/navigation-apps)
- [Media apps](https://developer.android.com/design/ui/cars/guides/app-types/media-apps)
- Other driving-related apps, such as point-of-interest, IoT, and weather

To understand the design process at a high level, see the following process. For details of your role and the app library's role in creating the experience for users, see[Who handles what](https://developer.android.com/design/ui/cars/guides/foundations/overview#who-handles-what).

### Process steps

Designing with the Android for Cars App Library involves the following steps, in general:

1. **[Define user tasks](https://developer.android.com/design/ui/cars/guides/foundations/define-user-tasks)**. Figure out which tasks are important for users to perform with your app in vehicles.
2. **[Plan task flows](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows)**. Choose a sequence of templates to lead users through each task.
3. **[Consider driving state](https://developer.android.com/design/ui/cars/guides/ux-requirements/driving-state)**. Make strategic use of parked-only templates and task-flow strategies.
4. **[Plan communications](https://developer.android.com/design/ui/cars/guides/components/plan-communications)**. Choose appropriate communication options for all scenarios in which your app communicates with users.
5. **[Customize your app](https://developer.android.com/design/ui/cars/guides/foundations/customize-app)**. Customize the content of each template to reflect your users' needs, and customize styling to reflect your app's brand.

| **Note:** Throughout the design process, refer to the[UX requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview)to make sure you are following UX requirements and recommendations.

### Who handles what

When you create an app with the Android for Cars App Library, the app library takes care of many aspects of the app experience, including optimizing it for driving in all compatible cars.

|                                                                                 What the library handles                                                                                 |                                                                                                         What app developers handle                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input: Handling user input to templates through mechanisms available in specific cars, such as touchscreen or rotary                                                                     | Voice input: Processing recorded audio                                                                                                                                                                                                      |
| Screen sizing: Adapting content to screen sizes                                                                                                                                          | User flows: Creating customized sequences of templates that address critical user journeys                                                                                                                                                  |
| Screen transitions:[Motion](https://developers.google.com/cars/design/android-auto/design-system/motion)transition between screens                                                       | Metadata: Providing metadata such as list items and locations to be pinned on maps                                                                                                                                                          |
| Consistent, driving-optimized UI: Ensuring that the UI and interaction patterns are familiar and consistent across apps                                                                  | Branding elements: Providing app iconography, imagery, and custom[accent colors](https://developers.google.com/cars/design/create-apps/apps-for-drivers/customize-app#colors)(with light and dark variants)                                 |
| Light and dark mode (except as noted below): Adjusting template features to appropriate mode for ambient light conditions                                                                | Maps (navigation apps only): Drawing and updating maps (light-themed or dark-themed, as instructed) including a[map for cluster display](https://developers.google.com/cars/design/create-apps/sample-flows/view-map-in-cluster)if required |
| UX restrictions based on driving state: Limiting text or disabling certain features, such as the keyboard, while the user is driving                                                     |                                                                                                                                                                                                                                             |
| Maps for non-navigation apps: Drawing the map in the[Place List (map)](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/place-list-map-template)template |                                                                                                                                                                                                                                             |