---
title: Message template  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/message-template
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Message template Stay organized with collections Save and categorize content based on your preferences.




With the message template, you can present a brief message and optional relevant
actions.

Use this template to communicate error messages, permission prompts, and other
information about UI states.

The Messages template can be embedded in the [Tab template](/design/ui/cars/guides/templates/tab-template) to provide tabbed
navigation, and the [Map + Content template](/design/ui/cars/guides/templates/map-content-template) to display a message on a map.

**Note:** This template is intended for quick messages, with related actions as
secondary. To display a longer message, use the [Long Message template](/design/ui/cars/guides/templates/long-message-template). To
display more detailed information with prominent actions, use the [Pane
template](/design/ui/cars/guides/templates/pane-template).

A message template includes the following:

* Optional [header](/design/ui/cars/guides/components/header) (header is replaced with tabs when this template is
  embedded in the [Tab template](/design/ui/cars/guides/templates/tab-template))
* Up to 2 lines of wrapping text
* Image, icon, or loading spinner (optional)
* Up to 2 [buttons](/design/ui/cars/guides/components/button) in template body (optional), where one can be
  designated as [primary](/design/ui/cars/guides/components/button#primary)

![Example of a message template](/static/images/design/ui/cars/components/message-template-1.png)


Example of a message in tabbed navigation.


![Example of a message template](/static/images/design/ui/cars/components/message-template-2.png)


Example of displaying a message on a map.

## Message template UX requirements

|  |  |
| --- | --- |
| **MUST** | Include message text. |
| **SHOULD** | Designate a [primary](/cars/design/create-apps/apps-for-drivers/components/button#primary) action when providing 2 actions. |
| **SHOULD** | Place the primary action closest to the driver (on the left for left-hand-drive vehicles) when there are 2 actions. |
| **SHOULD** | Include a header with an optional title and primary and secondary actions. |
| **MAY** | Include an image or icon asset. |
| **MAY** | Include up to 2 actions. |
| **MAY** | Use this template to prompt users about app permissions and open related flows on the phone when parked (as shown in [Grant permissions on phone](/cars/design/create-apps/sample-flows/grant-permissions-on-phone)). |