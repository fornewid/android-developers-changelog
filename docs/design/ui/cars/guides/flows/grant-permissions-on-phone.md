---
title: Grant permissions on the phone  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-on-phone
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Grant permissions on the phone Stay organized with collections Save and categorize content based on your preferences.



When a user tries to open your app but hasn't authorized the necessary
permissions, you can use the Message template to request permissions.

In Android Auto, if you use the method described in
[Request Permissions](/training/cars/apps#permissions),
the permissions dialog will open on the phone if the user is not driving (for
technical details, see [Handle user input](/training/cars/apps#handle-user-input)).

In this case, provide a toast directing the user to the phone.
After the user grants permissions, refresh the car screen
so the user doesn't return to the Message template.

First, the app requests permissions on the car screen.

[](/static/images/design/ui/cars/flows/grant-permissions-phone-1.mp4)

Next, the user confirms permissions on their phone when not driving.

[](/static/images/design/ui/cars/flows/grant-permissions-phone-2.mp4)

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user opens the app. | On your landing template (not shown) | 1 |
| The user selects the option to grant app permissions, then reviews the confirmation toast. | First, use the Message template with two buttons to allow users the chance to grant the permissions that they need: Message template with primary and secondary action buttons Then, display a toast on that same Message template to direct the user to their phone: Message template with two buttons and toast | 2 |
| The user grants permission on their phone. | No template, as this action occurs on the user's phone: User taps on Allow button on phone | 2 (no interaction with app in car) |
| After the user grants permissions, the app returns to the landing template. | Landing template; in this case, the Place List (navigation) template: Place List template with Recents, Favorites, and Saved lists | 1 (step count resets) |