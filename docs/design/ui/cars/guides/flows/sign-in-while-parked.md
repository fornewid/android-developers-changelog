---
title: https://developer.android.com/design/ui/cars/guides/flows/sign-in-while-parked
url: https://developer.android.com/design/ui/cars/guides/flows/sign-in-while-parked
source: md.txt
---

# Sign-in to the app while parked

Use the[Sign-in template](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template)to prompt the user to sign in using one of the following 4[sign-in methods](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template#methods):

- **PIN method**: Displays a mandatory PIN code provided by the app and instructions for where the user should enter it.
- **Provider sign-in method:**Lets users sign in using a provider (such as Google), with no input required.
- **Username/password method:**Lets users enter authentication information in a single, mandatory form field.
- **QR code method (shown below):**Lets users sign in by scanning a QR Code.

Add the[Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template)to provide details such as the full text of a privacy policy or terms of service. These templates are both parked-only templates, so they don't increment the step count.

**Note:**This sample flow shows how the templates might look in Android Auto.

## Sample flow

|                                        User action                                         |                                                                                                      Where action is performed                                                                                                       | Step count after action |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user taps a button to sign in to the app.                                              | Landing template (not shown)                                                                                                                                                                                                         | 1                       |
| To sign in, the user sees a QR Code that they must capture on their phone.                 | Sign-in template (parked-only template) ![Sign-in with QR code](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-parked-3.png)                                                                               | 1                       |
| The user scans the QR Code, which takes them to the sign-in process on their phone screen. | No template (task continues on phone)                                                                                                                                                                                                | 1 (task paused)         |
| The user reads the app's privacy policy (if required).                                     | Long Message template (parked-only) ![Long Message with two buttons](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-parked-2.png)                                                                          | 1                       |
| The app returns to the landing template.                                                   | Landing template (in this case, List template included in the Map + Content template) ![List template included in the Map + Content template](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-parked-3.png) | 1 (new task)            |