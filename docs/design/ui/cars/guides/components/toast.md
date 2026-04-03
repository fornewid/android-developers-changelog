---
title: https://developer.android.com/design/ui/cars/guides/components/toast
url: https://developer.android.com/design/ui/cars/guides/components/toast
source: md.txt
---

# Toasts

A toast is a short, informational message that an app displays briefly near the bottom of the screen.

Only one toast can be displayed at a time. The toast tells a user about an action the app has taken or will take. It does not require any user action or response. After 8 seconds, the toast disappears automatically.

Toasts are related to dialogs (and are in the Dialog family of components), but they differ in purpose and priority.

|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------|
| **Component**                                                                        | **Purpose**                                                                                                        | **Priority** |
| Toast                                                                                | Displays an informative message. Doesn't require user interaction. Disappears after 8 seconds.                     | Low          |
| [Dialog](https://developer.android.com/cars/design/automotive-os/components/dialogs) | Displays information and task options that require user interaction. A dialog retains focus until a user responds. | High         |

| **Note:** Toasts are based on the Toast component in the Car UI Library. To use the Toast component, you must[add the Car UI Library as a dependency](https://source.android.com/devices/automotive/hmi/car_ui/integrate)to your app.

## Anatomy

A toast appears briefly in front of other screen content. It consists of a background and a text message.
![Example of Toast component with numbered callouts to background and message area](https://developer.android.com/static/images/design/ui/cars/components/toast-anatomy.png)1. Toast background  
2. Toast message area  

## Specs

Here are the specifications for toasts:

### Toast -- padding around message text

![](https://developer.android.com/static/images/design/ui/cars/components/toast-specs.png)

### Toast -- bottom placement on screen

![](https://developer.android.com/static/images/design/ui/cars/components/toast-specs-2.png)

## Customization

OEMs can modify the appearance of toasts to reflect their brand by:

- Providing custom fonts
- Changing toast dimensions and placement

| **Note:** To customize toasts, OEMs must use runtime overlays, explained in the[Car UI Library Integration Guide](https://source.android.com/devices/automotive/hmi/car_ui).

[Design system](https://developer.android.com/cars/design/automotive-os/design-system/overview)provides guidance for customizing components using layout, typography, and sizing.

## Examples

Here are some examples of toasts:

### Toast message format

![](https://developer.android.com/static/images/design/ui/cars/components/toast-example-rev.png)

### Toast placement (near bottom of the screen)

![](https://developer.android.com/static/images/design/ui/cars/components/toast-example-2-rev.png)