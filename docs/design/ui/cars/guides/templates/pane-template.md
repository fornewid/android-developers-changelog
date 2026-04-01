---
title: Pane template  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/templates/pane-template
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Pane template Stay organized with collections Save and categorize content based on your preferences.




This template is useful for presenting information, such as location and
reservation details, and for taking action based on data.

This template can be embedded in the
[Tab template](/design/ui/cars/guides/templates/tab-template) to provide tabbed navigation, or included in the
[Map + Content template](/design/ui/cars/guides/templates/map-content-template) to provide a pane on a map. When embedded in a
Map + Content template, images aren't displayed.

**Includes:**

* Optional [header](/design/ui/cars/guides/components/header)
* Up to 2
  [buttons](/design/ui/cars/guides/components/button),
  where one can be designated as
  [primary](/design/ui/cars/guides/components/button#primary)
  (optional)
* Up to 4 non-actionable
  [rows](/design/ui/cars/guides/components/row)
  (1 row is mandatory)
* Optional large image (see example)

**Note:** This template highlights actions and information. For quick messages with
less detail, use the Message template. For long messages, use the Long Message
template.

![](/static/images/design/ui/cars/templates/pane-template-1.png)


Location details for a parking app, with two related actions
(Start and No thanks)


![](/static/images/design/ui/cars/templates/pane-template-2.png)


Location details for a cafe, with two actions. Due to size
constraints, the second action button's associated text is hidden and only its
icon is shown.

## Pane template UX requirements

App developers:

|  |  |
| --- | --- |
| MUST | Include at least one row of information. |
| SHOULD | Designate a [primary](/design/ui/cars/guides/components/button#primary) action when providing 2 actions. |
| SHOULD | Make navigation the primary action, when it's included as one of the actions. |
| SHOULD | Provide icons for all actions. |
| SHOULD | Include a header with an optional title and primary and secondary actions. |
| MAY | Include up to 4 rows of information and 2 actions. |

## Resources

|  |  |
| --- | --- |
| Type | Link |
| API reference | `PaneTemplate, PaneTemplate.Builder` |