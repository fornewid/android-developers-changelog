---
title: https://developer.android.com/design/ui/cars/guides/templates/tab-template
url: https://developer.android.com/design/ui/cars/guides/templates/tab-template
source: md.txt
---

# Tab template

The Tab template acts as a container for other templates and allows switching among views.

This capability is particularly useful for organizing content or views that users will want to frequently switch between, such as available devices, settings, and more.

Tab template includes the following:

- Tab bar with app icon and up to 4 tabs. Each tab must provide both an icon and a title.
- Embedded template, which can be any of the following types:
  - [List](https://developer.android.com/design/ui/cars/guides/templates/list-template)
  - [Grid](https://developer.android.com/design/ui/cars/guides/templates/grid-template)
  - [Search](https://developer.android.com/design/ui/cars/guides/templates/search-template)
  - [Pane](https://developer.android.com/design/ui/cars/guides/templates/pane-template)
  - [Message](https://developer.android.com/design/ui/cars/guides/templates/message-template)
  - [Navigation](https://developer.android.com/design/ui/cars/guides/templates/navigation-template)
  - Sectioned Item

Each tab corresponds to one embedded template. Only one tab can be active at any given time.
| **Note:** Headers from embedded templates are ignored because the space that would normally be used for the header is used for the tab bar.
![Example of tab template](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-1.png)Example of the Tab template

## Anatomy of the tab template

![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-2.png)Tab template with a list embedded![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-3.png)Tab template with a grid embedded  
![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-4.png)Tab template with a pane embedded![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-5.png)Tab template with a message embedded  
![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-6.png)Tab template with navigation template embedded![](https://developer.android.com/static/images/design/ui/cars/templates/tab-template-7.png)Tab template with Search template embedded

## Tab template UX requirements

|------------|---------------------------------------------------------|
| MUST       | Provide icons for each tab.                             |
| MUST       | Include at least 2 and no more than 4 tabs.             |
| SHOULD     | Use short tab labels to avoid truncation.               |
| SHOULD NOT | Rely on a header or action strip in embedded templates. |

## Resources

|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type          | Link                                                                                                                                                                                                         |
| API reference | ` `[TabTemplate](https://developer.android.com/reference/androidx/car/app/model/TabTemplate)`, `[TabTemplate.Builder](https://developer.android.com/reference/androidx/car/app/model/TabTemplate.Builder)` ` |