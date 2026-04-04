---
title: Autofill framework  |  Identity  |  Android Developers
url: https://developer.android.com/identity/autofill
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Autofill framework Stay organized with collections Save and categorize content based on your preferences.




The autofill framework is available in Android 8.0 (API level 26) and higher.

Some apps, such as password managers, can fill out the views in other apps with
data provided by the user. Apps that fill out other apps' views are called
*autofill services*. The autofill framework manages the communication between an
app and an autofill service.

Filling out forms is a time-consuming and error-prone task. The autofill
framework improves the user experience by providing the following benefits:

* **Saving time spent filling in fields.** Autofill saves users from re-typing
  information.
* **Minimizing user input errors.** Typing is prone to errors, especially on
  mobile devices. Minimizing the need to type information minimizes typos.

**Note:** Autofill works well with [Credential Manager](/identity/sign-in/credential-manager) and [passkeys](https://developers.google.com/identity/passkeys) to
provide increased security and a smoother workflow.

## Components

The autofill framework contains the following high-level components:

* **Autofill services:** apps such as password managers that save and store
  user information that can be used in views across multiple apps.
* **Autofill clients:** apps that provide views that need to be filled out or
  that hold the user's data.
* **Android system:** the OS that defines the workflow and provides the
  infrastructure that makes services and clients work together.

For a detailed explanation of the autofill workflow, see the
[`AutofillService`](/reference/android/service/autofill/AutofillService) and
[`AutofillManager`](/reference/android/view/autofill/AutofillManager) reference
documentation.

## Guides

To learn more about how to use the autofill framework, see the following guides:

[Optimize your app for autofill](/guide/topics/text/autofill-optimize)
:   Check that your app is configured for use with the autofill framework.

[Build autofill services](/guide/topics/text/autofill-services)
:   Implement your own autofill service.

[Integrate autofill with keyboards](/guide/topics/text/ime-autofill)
:   Enable keyboards and other IMEs to use autofill, and enable your autofill
    provider to support IME integration.