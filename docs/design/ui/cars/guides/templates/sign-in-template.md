---
title: https://developer.android.com/design/ui/cars/guides/templates/sign-in-template
url: https://developer.android.com/design/ui/cars/guides/templates/sign-in-template
source: md.txt
---

# Sign-in template

The Sign-in template offers multiple ways for users to sign into your app while parked.  
Search template include the following:

1. Search bar[header](https://developer.android.com/design/ui/cars/guides/components/header)with optional[action strip](https://developer.android.com/design/ui/cars/guides/components/action-strip)
2. List[rows](https://developer.android.com/design/ui/cars/guides/components/row)for search results (within limits)
3. Keyboard (when parked), which apps can choose to show or hide when the template is first displayed.

Apps can customize the background color of markers with any color. The color used for the map marker is applied to the list marker.
| **Note:** This template displays its contents only when parked and does not increase the step count.

## Sign-in methods

The Sign-in template supports the following sign-in methods:

- Provider sign-in
- Username and password
- PIN code
- QR Code

![Example of provider sign-in](https://developer.android.com/static/images/design/ui/cars/templates/sign-in-provider.png)**Provider sign-in method**: This method lets users sign in using a provider, with no input required. In this example (for Android Auto), Google is the provider for the primary sign-in option, with PIN code and email sign-in offered as secondary options.![User name and password example](https://developer.android.com/static/images/design/ui/cars/templates/sign-in_username.png)**Username/password method**: This method lets users enter authentication information in a single, mandatory form field. This field can be used to enter a username or password. In this example (for Android Auto), the other methods are offered as secondary options.  
![QR code sign-in example](https://developer.android.com/static/images/design/ui/cars/templates/sign-in_qr_code.png)**QR code method**: This method displays a mandatory PIN code (up to 12 characters in length) provided by the app and instructions for where the user should enter it. The code can be refreshed as needed if it times out. (Android Auto example)![Example of sign-in pin](https://developer.android.com/static/images/design/ui/cars/templates/sign-in_pin.png)**PIN method**: This method displays a mandatory PIN code (up to 12 characters in length) provided by the app and instructions for where the user should enter it. The code can be refreshed as needed if it times out. (Android Auto example)

<br />

## Sign-in example templates

![Example of parked sign-in](https://developer.android.com/static/images/design/ui/cars/templates/sign-in-template-6.png)When the car is parked, the user can access the keyboard to type a username or password. (Android Auto example)![Example of driving sign-in](https://developer.android.com/static/images/design/ui/cars/templates/sign-in-template-5.png)To prevent driver distraction, the sign-in content is not shown while the user is driving. For these situations, it's helpful to provide a button with an alternative option, such as skipping sign-in and using the app in guest mode. (Android Auto example)

<br />

## Sign-in template UX requirements

|--------|---------------------------------------------------------------------------------------|
| MUST   | Include a sign-in method when using this template.                                    |
| SHOULD | Use input fields only for user sign-in, not for collecting other types of user input. |
| SHOULD | Prioritize the shortest flow (using the fewest clicks).                               |
| SHOULD | Prioritize the most popular method.                                                   |
| MAY    | Use actions to let users switch sign-in methods.                                      |

## Resources

|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type              | Link                                                                                                                                                                                                                     |
| API reference     | [SignInTemplate](https://developer.android.com/reference/androidx/car/app/model/signin/SignInTemplate)`, `[SignInTemplate.Builder](https://developer.android.com/reference/androidx/car/app/model/signin/SignInTemplate) |
| Developer's Guide | [Add a sign-in flow](https://developer.android.com/training/cars/apps#sign-in)                                                                                                                                           |