---
title: https://developer.android.com/design/ui/cars/guides/templates/message-template
url: https://developer.android.com/design/ui/cars/guides/templates/message-template
source: md.txt
---

# Message template

Messages present a small amount of text and optional relevant actions.

Use the Message template to communicate error messages, permission prompts, and other information about UI states.

This template can be embedded in the[Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template)to provide tabbed navigation. You can also include this template in the[Map + Content template](https://developer.android.com/design/ui/cars/guides/templates/map-content-template)to display a message on a map.  
A message template includes the following:

- Optional[header](https://developer.android.com/design/ui/cars/guides/components/header)(header is replaced with tabs when this template is embedded in the[Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template))
- Up to 2 lines of wrapping text
- Image, icon, or loading spinner (optional)
- Up to 2[buttons](https://developer.android.com/design/ui/cars/guides/components/button)in template body (optional), where one can be designated as[primary](https://developer.android.com/design/ui/cars/guides/components/button#primary)
| **Note:** This template is intended for quick messages, with related actions as secondary. To display a longer message, use the[Long Message template](https://developer.android.com/design/ui/cars/guides/templates/long-message-template). To display more detailed information with prominent actions, use the[Pane template](https://developer.android.com/design/ui/cars/guides/templates/pane-template).

## Message template examples

![Map + X with included Message template with primary and secondary action buttons](https://developer.android.com/static/images/design/ui/cars/templates/map_with_message.png)Message template included in the Map + Content template containing primary and secondary action buttons![Message template with action buttons](https://developer.android.com/static/images/design/ui/cars/templates/message_2_buttons.png)Message with two actions

<br />

## Message template UX requirements

App developers:

|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUST**   | Include message text.                                                                                                                                                                                                                    |
| **SHOULD** | Designate a[primary](https://developer.android.com/design/ui/cars/guides/components/button#primary-buttons)action when providing 2 actions.                                                                                              |
| **SHOULD** | Place the primary action closest to the driver (on the left for left-hand-drive vehicles) when there are 2 actions.                                                                                                                      |
| **SHOULD** | Include a header with an optional title and primary and secondary actions.                                                                                                                                                               |
| **MAY**    | Include an image or icon asset.                                                                                                                                                                                                          |
| **MAY**    | Include up to 2 actions.                                                                                                                                                                                                                 |
| **MAY**    | Use this template to prompt users about app permissions and open related flows on the phone when parked (as shown in[Grant permissions on phone](https://developer.android.com/design/ui/cars/guides/flows/grant-permissions-on-phone)). |

## Resources

|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type          | Link                                                                                                                                                                                                                         |
| API reference | ` `[MessageTemplate](https://developer.android.com/reference/androidx/car/app/model/MessageTemplate)`, `[MessageTemplate.Builder](https://developer.android.com/reference/androidx/car/app/model/MessageTemplate.Builder)` ` |