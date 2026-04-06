---
title: https://developer.android.com/design/ui/cars/guides/app-types/navigation-apps
url: https://developer.android.com/design/ui/cars/guides/app-types/navigation-apps
source: md.txt
---

# Navigation apps are map-based applications that provide drivers with guidance and directions while on the road. They integrate with the vehicle's center screen and often the instrument cluster to show information relevant to the driver's journey.
![Navigation apps](https://developer.android.com/static/images/design/ui/cars/app-cuj/navigation.png)

The templates in the Android for Cars App Library are driving-optimized and designed for both Android Auto and AAOS. Each template includes navigation-focused features like:

- Place lists
- Route previews
- Travel estimate cards
- Routing cards
- Navigation alerts
- Map interactivity
- Cluster integration

You'll have control over the map layer behind the interactive elements of the template.

## Get started

To learn how to use the templates in the Android for Cars App Library, see[Build apps with templates](https://developer.android.com/design/ui/cars/guides/templates/overview).

For navigation apps, the[Map + Content template](https://developer.android.com/design/ui/cars/guides/templates/map-content-template)and the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template)are especially relevant.
| **Note:** For technical details about how to build this experience, see[Build a navigation app](https://developer.android.com/training/cars/apps/navigation).

## Examples

To see how the templates can be assembled into navigation-oriented experiences, check out the following sample flows:

- [Navigate to a saved location](https://developer.android.com/design/ui/cars/guides/app-types/navigate-to-a-saved-location)
- [Browse locations and start navigation](https://developer.android.com/design/ui/cars/guides/app-types/browse-locations)
- [Access location details and start navigation](https://developer.android.com/design/ui/cars/guides/app-types/access-location-details)
- [Search using past results while driving](https://developer.android.com/design/ui/cars/guides/app-types/search-using-past-results)
- [Respond to a navigation alert](https://developer.android.com/design/ui/cars/guides/app-types/navigation-alerts)
- [Respond to a timed alert](https://developer.android.com/design/ui/cars/guides/app-types/timed-alert)
- [Add a stop while driving](https://developer.android.com/design/ui/cars/guides/app-types/add-stop)
- [Arrive at destination](https://developer.android.com/design/ui/cars/guides/app-types/arrive-at-destination)
- [View a map in the cluster](https://developer.android.com/design/ui/cars/guides/app-types/view-map-in-cluster)

## UX requirements

In addiotion to the global requirements for templated apps, navigation apps must also meet the following requirements.

|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MUST   | Make sure all visual information drawn on maps (such as speed information and route labeling) meets[contrast requirements](https://developers.google.com/cars/design/android-auto/design-system/color#contrast).                                                                                                                   |
| MUST   | Draw[only map content and drive-related content](https://developer.android.com/docs/quality-guidelines/car-app-quality#NF-2)on the surface of the template.                                                                                                                                                                        |
| MUST   | Draw a[light-themed or dark-themed map](https://developer.android.com/docs/quality-guidelines/car-app-quality#MR-1)when instructed to do so.                                                                                                                                                                                       |
| MUST   | Use turn-by-turn (TBT) notifications to show directions when a user is completing a task outside of the Navigation template during active navigation (as shown in[Navigation notifications: TBT and regular](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/navigation-template#notifications)). |
| SHOULD | Make sure text drawn on maps uses a font size of 24dp or larger unless it is paired with a visual element (such as a route or road) or is relatively static on the display.                                                                                                                                                        |
| SHOULD | Clearly indicate if a task will update the route.                                                                                                                                                                                                                                                                                  |
| SHOULD | Meet or exceed minimum size of 36 x 36 dp for images, icons, and map markers.                                                                                                                                                                                                                                                      |
| SHOULD | Refresh duration and distance values during the drive.                                                                                                                                                                                                                                                                             |
| MAY    | Use[navigation alerts](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/navigation-template#alerts)or heads-up notifications (HUNs) to alert users about general navigation-related updates (in addition to turn-by-turn directions), such as traffic ahead.                                       |
| MAY    | Customize background color of TBT notifications.                                                                                                                                                                                                                                                                                   |
| MAY    | Use animations when they aid in driving.                                                                                                                                                                                                                                                                                           |

## Template-specific requirements

Your app must also meet requirements for the specific templates in your task flows. See the requirements for each template below.

- [Grid template](https://developer.android.com/design/ui/cars/guides/templates/grid-template)
- [List template](https://developer.android.com/design/ui/cars/guides/templates/list-template)
- [Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template)
- [Message template](https://developer.android.com/design/ui/cars/guides/templates/message-template)
- [Map + Content template](https://developer.android.com/design/ui/cars/guides/templates/map-content-template)
- [Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template)
- [Pane template](https://developer.android.com/design/ui/cars/guides/templates/pane-template)
- [Search template](https://developer.android.com/design/ui/cars/guides/templates/search-template)
- [Sign-in template](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template)
- [Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template)