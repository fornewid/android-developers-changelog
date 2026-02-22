---
title: https://developer.android.com/design/ui/cars/guides/ux-requirements/overview
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/overview
source: md.txt
---

# UX requirements

Make sure your app meets design requirements for usability in cars.

This section lists (or provides links to) all of the UX requirements you'll need. UX requirements are expressed as instructions that you MUST, SHOULD, or MAY follow. At a high level, you can understand these labels as follows:

|--------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| MUST   | Required (enforced either in the API or in[Android app quality for cars)](https://developer.android.com/docs/quality-guidelines/car-app-quality) |
| SHOULD | Recommended                                                                                                                                      |
| MAY    | Optional                                                                                                                                         |

## UX requirements for templated apps

Here are the requirements based on the type of app you're designing:

- [General requirements (applies to all templated apps)](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview#general)
- [Navigation app requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview#navigation)
- [Weather app requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview#weather)
- [Template-specific requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview#templates)

### General requirements

|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUST**       | Keep task flows to 5 steps or fewer in length.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **MUST**       | Get user permission to access the car microphone before recording audio for voice input.                                                                                                                                                                                                                                                                                                                                                                    |
| **MUST**       | Use the appropriate method (as stated in[Using the Android for Cars App Library](https://developer.android.com/training/cars/navigation#handle-user-input)) to direct Android Auto users to the phone for actions that are not allowed while driving, instructing them to look at their phone screens only when it's safe to do so (see[Grant permissions on phone](https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-on-phone)). |
| **MUST NOT**   | End 5-step task flows with a list-based template unless the[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits)feature is enabled (5th step must be one of these: Navigation, Message, or Pane).                                                                                                                                                                                         |
| **SHOULD**     | Keep task flows short (2 to 3 steps in length).                                                                                                                                                                                                                                                                                                                                                                                                             |
| **SHOULD**     | Show content (or action strip buttons) for at least 8 seconds before removing that content in an auto-transition between steps.                                                                                                                                                                                                                                                                                                                             |
| **SHOULD**     | Ask users to grant any necessary permissions when they first open the app.                                                                                                                                                                                                                                                                                                                                                                                  |
| **SHOULD**     | Provide 2 accent colors, if possible, to better accommodate dark and light backgrounds.                                                                                                                                                                                                                                                                                                                                                                     |
| **SHOULD**     | Provide a back button or other exit mechanism in places where no other actions are available, such as loading screens and actionless Message and Pane templates.                                                                                                                                                                                                                                                                                            |
| **SHOULD**     | Show useful content when opening a template, rather than an empty state with no options for users.                                                                                                                                                                                                                                                                                                                                                          |
| **SHOULD**     | Provide shortcuts to earlier steps (for example, when task flows exceed 3 screens).                                                                                                                                                                                                                                                                                                                                                                         |
| **SHOULD**     | Provide a user entry point, such as a microphone icon, if your app allows voice input (audio recording).                                                                                                                                                                                                                                                                                                                                                    |
| **SHOULD**     | Stop recording audio when the user stops providing the input.                                                                                                                                                                                                                                                                                                                                                                                               |
| **SHOULD**     | Refresh content only for the purposes noted in[Limiting driver distraction](https://developer.android.com/design/ui/cars/guides/foundations/define-user-tasks#limit-distraction)or where explicitly permitted in guidance for specific templates or app types.                                                                                                                                                                                              |
| **SHOULD NOT** | Use auto-transitions to complete tasks without user action (that is, don't use them back-to-back).                                                                                                                                                                                                                                                                                                                                                          |
| **SHOULD NOT** | Create buttons with states, such as toggles, in places where actions are supported (toggles are supported only in list rows).                                                                                                                                                                                                                                                                                                                               |
| **MAY**        | Update a list row or grid item's image, icon, or secondary text to reflect changes.                                                                                                                                                                                                                                                                                                                                                                         |

### Purchase flows only

|--------------|-------------------------------------------------------------------------------------------------------------|
| **SHOULD**   | Provide shortcuts wherever possible, such as allowing users to repeat previous transactions ("book again"). |
| **MUST NOT** | Allow users to set up payment methods.                                                                      |
| **MUST NOT** | Ask users to commit to recurring payments.                                                                  |
| **MUST NOT** | Allow users to select multiple items for purchase in a single flow.                                         |

### POI apps only

|--------|-----------------------------------------------------------------------------------------|
| SHOULD | Provide a way to launch a navigation app in order to navigate to the point of interest. |

## Navigation apps

|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUST**       | Make sure all visual information drawn on maps (such as speed information and route labeling) meets[contrast requirements](https://developers.google.com/cars/design/android-auto/design-system/color#contrast).                                                                                                |
| **MUST**       | [Draw](https://developer.android.com/training/cars/apps/navigation#drawing-the-map)only map content and drive-related content on the surface of the template.                                                                                                                                                   |
| **MUST**       | Draw a light-themed or dark-themed map when instructed to do so.                                                                                                                                                                                                                                                |
| **SHOULD**     | Make sure text drawn on maps uses a font size of 24dp or larger unless it is paired with a visual element (such as a route or road) or is relatively static on the display.                                                                                                                                     |
| **SHOULD**     | Clearly indicate if a task will update the route.                                                                                                                                                                                                                                                               |
| **SHOULD**     | Meet or exceed minimum size of 36 x 36 dp for images, icons, and map markers.                                                                                                                                                                                                                                   |
| **SHOULD**     | Use turn-by-turn (TBT) notifications to show directions when a user is completing a task outside of the Navigation template during active navigation (as shown in[Navigation notifications: TBT and regular](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#notifications)). |
| **SHOULD**     | Refresh duration and distance values during the drive.                                                                                                                                                                                                                                                          |
| **SHOULD NOT** | Create multi-stop journeys, since templates are not optimized for this type of interactivity.                                                                                                                                                                                                                   |
| **MAY**        | Use[navigation alerts](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#alerts)or heads-up notifications (HUNs) to alert users about general navigation-related updates (in addition to turn-by-turn directions), such as traffic ahead.                                       |
| **MAY**        | Customize background color of TBT notifications.                                                                                                                                                                                                                                                                |
| **MAY**        | Use animations when they aid in driving.                                                                                                                                                                                                                                                                        |

## Weather apps

|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUST**     | Make sure all visual information drawn on maps or icons (such as radar, temperature indicator, condition icons) meets[contrast requirements](https://developers.google.com/cars/design/android-auto/design-system/color#contrast). |
| **MUST**     | Draw only map content and weather-related content on the surface of the template.                                                                                                                                                  |
| **MUST**     | Draw a light-themed or dark-themed map when instructed to do so.                                                                                                                                                                   |
| **MUST**     | Ensure weather indicators don't overlap with each other or are unreadable due to density/size of indicators.                                                                                                                       |
| **MUST NOT** | Use weather animations on the surface of the template when the user is driving.                                                                                                                                                    |
| **MUST NOT** | Show more than 5 unique weather map annotations in a given view (for example: Temperature markers, wind speed markers, humidity, radar overlay, lightning indicators, road conditions all in the same view).                       |
| **MUST NOT** | Show complex map legends with more than 3 unique items, or more than 3 unique colors (gradients don't apply) while the user is driving.                                                                                            |
| **MUST NOT** | Allow users to configure time intervals or dates of forecast information.                                                                                                                                                          |
| **SHOULD**   | Make sure text drawn on maps uses a font size of 24dp or larger unless it is paired with a visual element (such as a route or road) or is relatively static on the display.                                                        |
| **SHOULD**   | Meet or exceed the minimum size of 36 x 36 dp for images, icons, and map markers.                                                                                                                                                  |
| **MAY**      | Show forecast information for upcoming times, such as Hours, AM/PM, or Days.                                                                                                                                                       |
| **MAY**      | Use heads-up notifications (HUNs) to alert users about important weather updates related to imminent weather conditions, or conditions along the user's route.                                                                     |
| **MAY**      | Use weather-related animations when the user is not driving.                                                                                                                                                                       |
| **MAY**      | Use animations when they are related to movement of the map by the user or the user's location.                                                                                                                                    |

## Template-specific requirements

Use the template-specific requirements to make sure each template in your task flows meets UX requirements and recommendations.

Learn more about the requirements for each template:

- [Grid template](https://developer.android.com/design/ui/cars/guides/templates/grid-template#requirements)
- [List template](https://developer.android.com/design/ui/cars/guides/templates/list-template#requirements)
- [Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template#requirements)
- [Message template](https://developer.android.com/design/ui/cars/guides/templates/message-template#requirements)
- [Map + Content template](https://developer.android.com/design/ui/cars/guides/templates/map-content-template#requirements)
- [Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#requirements)
- [Pane template](https://developer.android.com/design/ui/cars/guides/templates/pane-template#requirements)
- [Place List (map) template](https://developer.android.com/design/ui/cars/guides/templates/place-list-map-template#requirements)
- [Search template](https://developer.android.com/design/ui/cars/guides/templates/search-template#requirements)
- [Sign-in template](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template#requirements)
- [Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template#requirements)