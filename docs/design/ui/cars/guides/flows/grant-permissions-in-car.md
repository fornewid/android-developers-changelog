---
title: https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-in-car
url: https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-in-car
source: md.txt
---

# Grant permissions on the car screen

On Android Automotive OS, the permissions flow is the same as granting permissions on Android Auto, except the user sees permission details on the car screen instead of the phone.  
| **Note:** This sample flow shows how the templates might look in Android Automotive OS (AAOS).

<br />

## Sample flow

|                                     User action                                     |                                                                                                                                Where action is performed                                                                                                                                 | Step count after action |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user opens your app, and they must grant permissions.                           | Landing template (not shown)                                                                                                                                                                                                                                                             | 1                       |
| The user selects the option to grant app permissions.                               | Message template ![Message template with two buttons](https://developer.android.com/static/images/design/ui/cars/flows/grant-permissions-car-1.png)                                                                                                                                      | 2                       |
| The user sees a system permissions dialog on the car screen and grants permissions. | Message template with toast (refresh) ![Toast on Message template](https://developer.android.com/static/images/design/ui/cars/flows/grant-permissions-car-2.png)**Note:**When the Message template updates with the toast, it is considered a refresh and doesn't add to the step count. | 2                       |
| The app returns to the landing template.                                            | Landing template (in this case, the Place List template) ![Place List template with Recents, Favorites, and Saved lists](https://developer.android.com/static/images/design/ui/cars/flows/grant-permissions-car-3.png)                                                                   | 1 (new task)            |