---
title: Grant permissions on the car screen  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-in-car
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Grant permissions on the car screen Stay organized with collections Save and categorize content based on your preferences.



On Android Automotive OS, the permissions flow is the same as granting
permissions on Android Auto, except the user sees permission
details on the car screen instead of the phone.

[](/static/images/design/ui/cars/flows/grant-permissions-car.mp4)

**Note:** This sample flow shows how the templates might look in Android Automotive
OS (AAOS).

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user opens your app, and they must grant permissions. | Landing template (not shown) | 1 |
| The user selects the option to grant app permissions. | Message template Message template with two buttons | 2 |
| The user sees a system permissions dialog on the car screen and grants permissions. | Message template with toast (refresh) Toast on Message template **Note:** When the Message template updates with the toast, it is considered a refresh and doesn't add to the step count. | 2 |
| The app returns to the landing template. | Landing template (in this case, the Place List template) Place List template with Recents, Favorites, and Saved lists | 1 (new task) |