---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/physical-buttons
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/physical-buttons
source: md.txt
---

# Physical buttons

Wear OS watches may have different hardware button configurations. This guide goes over the best use cases for each of these button types.

## Button types

The following are the most common button types on Wear OS devices.

### OS buttons

![](https://developer.android.com/static/wear/images/design/buttons_1.png)  
OS buttons are reserved for system actions: turning power on and off, and launching apps. All Wear OS watches have a power button and a launcher button.

### Multifunction buttons

![](https://developer.android.com/static/wear/images/design/buttons_11.png)  
Buttons on the watch face or screen are OS-configurable and user-configurable. Any other buttons can be mapped to actions. Buttons can be mapped to convenient actions based on where they are located on the watch.

## Press states

You can interact with Wear OS buttons in the following ways.

<br />

### Single press

![User presses the button and releases it quickly animation](https://developer.android.com/static/wear/images/design/buttons_10.gif)

**Figure 1.**User presses the button and releases it quickly.  

### Press and hold

![User presses the button and holds it for 500ms or longer animation](https://developer.android.com/static/wear/images/design/buttons_7.gif)

**Figure 2.**User presses the button and holds it for 500ms or longer.

<br />

## Multifunction button mapping

Your app can assign multifunction buttons to actions if doing so fits your app's use case. Apps are not required to assign actions to multifunction buttons.

Use multifunction buttons in your app if one of the following conditions applies:

- Your app has obvious, binary actions (such as play/pause).
- The user primarily uses your app without the user looking at the display.

<br />

![Fitness app multifunction button example](https://developer.android.com/static/wear/images/design/buttons_5.png)

**Figure 3.**This fitness app has assigned a pause/resume action to a multifunction button, which allows the user to perform the action without looking at the screen.  
![Messaging app multifunction button example](https://developer.android.com/static/wear/images/design/buttons_4.png)

**Figure 4.**This messaging app includes a reply action, which requires multiple steps and can't be completed with a single button press.

<br />

### Binary actions

Binary actions help users understand what will happen each time they press a button. For example, "start" and "stop" on a stopwatch constitute a binary action, and represent a good use case for multifunction buttons.  
![](https://developer.android.com/static/wear/images/design/buttons_12.png)  
**Figure 5.**Pressing the multifunction button starts the clock, and pressing it again stops the clock.

### Multifunction buttons as alternatives

Make multifunction button actions accessible via on-screen UI elements, as some watches don't have multifunction buttons. But you can use multifunction buttons as alternatives for on-screen buttons.  
![](https://developer.android.com/static/wear/images/design/buttons_2.png)  
**Figure 6.**Use a multifunction button as an alternative for a start/stop action and show it as an on-screen button.

Don't use a multifunction button for an action that can't be performed using on-screen UI elements.  
![](https://developer.android.com/static/wear/images/design/buttons_6.png)  
**Figure 7.**This stopwatch app uses the multifunction button to restart the stopwatch, but this isn't clear and intuitive.

### Focus on simplicity and immediacy

Pressing a multifunction button immediately conducts its assigned action. To prevent users from needing to look at the screen, use multifunction buttons for actions that can be completed with a single press.  
![](https://developer.android.com/static/wear/images/design/buttons_3.png)  
check_circle

### Do

Use multifunction buttons for actions that can be completed with a single press.  
![](https://developer.android.com/static/wear/images/design/buttons_8.png)  
cancel

### Don't

Use a multifunction button for complex actions.

In this music app the user can quickly pause a song, which is a good example of using the multifunction button. However, in this messaging app, pressing the button begins the action of replying, but the user may need to review the message before completing the action. This means that this is not a good interaction for a multifunction button.

### Reversible

Make button actions reversible. Don't use a multifunction button to trigger a destructive action, such as deleting data or halting an ongoing activity. For example, pressing the multifunction button in this map app performs an action to "Stop navigation," which can cause a user to lose directions at critical times.  
![](https://developer.android.com/static/wear/images/design/buttons_9.png)  
cancel

### Don't

Use a multifunction button to trigger a destructive action, such as deleting data or halting an ongoing activity.