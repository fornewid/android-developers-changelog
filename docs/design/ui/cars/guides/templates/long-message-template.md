---
title: Long Message template  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/templates/long-message-template
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Long Message template Stay organized with collections Save and categorize content based on your preferences.



The Long Message template presents a long message to be read while the car is
parked, with optional relevant actions.

This template is useful for providing details about a destination or for
presenting legal text (such as terms of service or a privacy policy)
during a sign-in process.

Long Message template includes the following:

* [Header](/design/ui/cars/guides/components/header)
  with optional
  [action strip](/design/ui/cars/guides/components/action-strip)
* Unlimited lines of wrapping text (scrollable)
* Up to 2
  [buttons](/design/ui/cars/guides/components/button) in template body (optional), where one can be designated as
  [primary](/design/ui/cars/guides/components/button#primary-buttons)

**Note:** This template displays its contents only when parked and does
not increase the step count.

## Long Message template examples

![Mock-up of Long Message template with sample privacy policy.](/static/images/design/ui/cars/components/longmessagetemplate1.png)


![Mock-up of Long Message template when in motion.](/static/images/design/ui/cars/components/longmessagetemplate2.png)

When the car is parked, this template can show a
detailed message, such as a privacy policy, or terms of service for the user
to accept when signing in to the app (Android Auto example)

When the user is driving, the long message is not
shown, to prevent driver distraction. For these situations, it's helpful to
provide a button with an alternative option, such as skipping sign-in and
using the app in guest mode.

## Long Message template UX requirements

App developers:

|  |  |
| --- | --- |
| MUST | Include text. |
| SHOULD | Designate a [primary action](/design/ui/cars/guides/components/button#primary) when providing 2 actions. |
| MAY | Include up to 2 actions. |

## Resources

|  |  |
| --- | --- |
| Type | Link |
| API reference | `LongMessageTemplate, LongMessageTemplate.Builder` |