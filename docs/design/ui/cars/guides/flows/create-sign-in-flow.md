---
title: https://developer.android.com/design/ui/cars/guides/flows/create-sign-in-flow
url: https://developer.android.com/design/ui/cars/guides/flows/create-sign-in-flow
source: md.txt
---

# Create a sign-in flow

Sign-in flows designed for the car screen are not as critical on Android Auto because the app is projected from a phone that already has its own sign-in experience. To minimize distraction for drivers, signing in is only available while parked.
| **Tip:** The sign-in flow works seamlessly in both Google built-in and Android Auto if it is developed as described.

You can create a sign-in flow for the car screen using templates from the Car App Library, which are vehicle-optimized.

The design process includes the following tasks:

1. **Choose a primary sign-in method** and any backup methods from the available[sign-in methods](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template#methods).
2. **Plan the task flow** , designing a sequence of templates to lead users through the sign-in task. For example:[sign in to the app while parked](https://developer.android.com/design/ui/cars/guides/flows/sign-in-while-parked).
3. **Validate usability** , ensuring that your planned flow meets the[UX requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview)for the Android for Cars App Library.

To learn more about designing with the templates, see[Templates overview](https://developer.android.com/design/ui/cars/guides/templates/overview).

## Sign-in examples

![Example login page](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-fig-1.png)This example provides two different ways that the user can verify their identity (Android Auto).![Example Google login](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-fig-2.png)This example features Google sign-in, or two other options (AAOS).![Example login page](https://developer.android.com/static/images/design/ui/cars/flows/sign-in-fig-3.png)This example features Google sign-in, or two other options (AAOS).

<br />

## Sign-in requirements

The requirements in this section relate to how sign-in should work, for optimal usability, in Android Automotive OS.

| Requirement level |                                                                                                                                                                                                                                                                                                                                           Requirements                                                                                                                                                                                                                                                                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SHOULD**        | You should: - Present Google sign-in as the primary option if the app and system support it - Present phone sign-in (if supported) as the primary option if the app and system don't support Google sign-in - Keep the length of the PIN for phone sign-in to 8 digits or fewer - For standard sign-in, separate entry of username and password into two steps - Put a label in the input box (*Enter password*) and keep it visible somewhere on screen after user starts typing - Provide users with the ability to show the password (which is generally hidden) while it's being typed - Provide guidance for accessing a forgotten username or password - Provide a way to create an account |
| **MAY**           | You may: - Provide standard app sign-in (username and password) as the primary option if neither Google sign-in nor phone sign-in can be supported - Provide phone sign-in, standard sign-in, or both as backup options when Google sign-in is the primary option - Provide standard sign-in as a backup option when phone sign-in is the primary option                                                                                                                                                                                                                                                                                                                                          |