---
title: https://developer.android.com/design/ui/cars/guides/flows/create-settings
url: https://developer.android.com/design/ui/cars/guides/flows/create-settings
source: md.txt
---

# Create settings (optional)

Settings for the car screen are not essential on Android Auto, as the app is projected from a phone that already has its own settings experience. However, if you would like to add settings UI to your app, you can do so using the following templates and it will work on Android Auto and AAOS.

When designing car screen settings using Car App Library templates, follow these steps:

1. **Select essential settings:**Include only the settings necessary for using the app while driving.
2. **Organize settings for easy navigation:** Use the[List template](https://developer.android.com/design/ui/cars/guides/templates/list-template)and display all settings on one screen.
3. **Design dialogs and error flows:** Use templates like the[Message template](https://developer.android.com/design/ui/cars/guides/templates/message-template).
4. **Ensure usability:** Check that your settings meet the[UX requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview)for the Car App Library.

To learn more about designing with the templates, see[Templates overview](https://developer.android.com/design/ui/cars/guides/templates/overview).
| **Note:** To implement a settings function in your app, you need to declare a Settings activity in your app's manifest file. For details, se[Add a Settings activity](https://developer.android.com/training/cars/media/automotive-os#settings-activity).

## Settings examples

In AAOS, the app bar in the Media App template includes an option for a Settings control, which users can select to bring up an overlay with your app settings screen.
![Settings view](https://developer.android.com/static/images/design/ui/cars/flows/settings-portrait.png)Example Settings overlay on AAOS (portrait)

## Settings requirements

| Requirement level |                                                                                                                                                                                            Requirements                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SHOULD**        | App developers should: - Keep settings simple and easy to navigate - Include only settings that are necessary for app use (such as account info, app preferences, and sign-in/sign-out) or relevant to listening to media in the car (for example, turning off explicit content) - Make all settings accessible from a single screen, if possible - Avoid use of dialogs beyond simple confirmation |