---
title: https://developer.android.com/design/ui/wear/guides/surfaces/tiles/bestpractices
url: https://developer.android.com/design/ui/wear/guides/surfaces/tiles/bestpractices
source: md.txt
---

# Best practices for tiles

![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-hero-updated.png)

## Design on black

Designing on a black background is crucial for Wear OS for two key reasons:

- **Battery efficiency:**Each pixel illuminated on the screen consumes power. By using a black background, you minimize the number of active pixels, extending battery life.
- **Seamless aesthetics:**A black background helps to visually minimize the watch bezel, creating the illusion of a continuous surface that extends to the edge of the device. Containing UI elements within this space further enhances this effect.

<br />

![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOdesignforblack.png)  
check_circle

### Do this

Always set the background color to black.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTforblack.png)  
cancel

### Don't do this

Don't set the background as a full bleed image or block color.

## Include only necessary elements

When opt-ed in (for example, using ProtoLayout Material3 PrimaryLayout), Wear OS will automatically display the permanent app icon, which will automatically display as the user scrolls through the Tile carousel. The app icon should not be designed and added as part of the Tile.

Ensure the app icon provided is monochrome if you are having dynamic theming on your tile. Check Android product icon guidelines about how to create the app icon for your brand.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOleaveouticon-updated.png)  
check_circle

### Do this

Wear OS may display the app icon automatically as the user scrolls through the Tile carousel. There is no need to put the app icon in the Tile design.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTaddicon-updated.png)  
cancel

### Don't do this

Do not add the app icon in the Tile design as it may appear twice/overlapped if also displayed at the system level.

## Hide app titles to ensure minimum tap targets

To ensure enough space for interactive elements on smaller screens, the app title can be hidden when a Tile uses two rows (and a bottom section). This ensures the rows are tall enough (at least 48dp). The title can reappear on larger screens (225dp+).  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-hidetitle-updated.png)  
check_circle

### Do this

On small screens, the app title is hidden to ensure the two rows have a minimum height and tap target of 48dp.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTshowapptitle-updated.png)  
cancel

### Don't do this

If you do not hide the app title on small screen, and have two rows, the height of the components will not adhere to our accessibility standards, and be less than the minimum tap target size. In this example the space for the buttons is smaller than 48dp, so it clips.

## Choose a single primary use-case to highlight

To make sure users know what to do with each Tile - whether it's opening an app, starting an activity, or learning more - we need them to include at least one interactive element in their layout.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOsingleusecase-updated.png)  
check_circle

### Do this

This specific Tile is effective because it provides a small collection of options, and then the ability to see more  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTmultipleusecases-updated.png)  
cancel

### Don't do this

This solution is less helpful to user because it introduces decision paralysis because of too many provided options

## Include (at least) one container

Each tile in the app must contain at least one container element and be fully tappable, linking to a corresponding screen within the app. The Tile's information, whether contained within the container or presented separately, must clearly communicate the linked content or available action.

If buttons are used, they should adhere to standard design conventions and provide a clear indication of their function.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOusecontainers-updated.png)  
check_circle

### Do this

This Tile works well because the user can take action on each of the provided capabilities since they have clear tap affordances  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTusenocontainers-updated.png)  
cancel

### Don't do this

This Tile is less effective because it doesn't make it clear that the user can tap on the content to see additional information

## Make actions instantly understandable

Experiences on the watch don't have the luxury of having ample space to communicate their meaning, so the most effective Tiles have easily predictable interactive components.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOmakeactionsclear-updated.png)  
check_circle

### Do this

A successful TIle takes full advantage the space available to clearly communicate the outcome of each action  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTmakeactionsunclear-updated.png)  
cancel

### Don't do this

The actions in this Tile are unclear---where does the container with the album art take the user, and is that different from the "Play" button?

## Visually prioritize actions

To help users understand the most important action on a Tile, interactive containers should be visually prioritized.

- Use primary colors on primary action buttons.
- Use secondary/tertiary colors on secondary actions

![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOvisuallyprioritize-updated.png)  
check_circle

### Do this

This Tile uses a combination of filled (with primary and secondary color roles) with a clear tertiary bottom button role, using the tonal-fill style  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTmonochrome-updated.png)  
cancel

### Don't do this

This Tile contains too many uses of filled style buttons, additionally all using the primary color role

## Simplify into fewer containers

Tiles should seek to refrain from using more than one interactive component to trigger a specific action, and instead attempt to simplify the overall layout into fewer containers.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOsimplecontainers-updated.png)  
check_circle

### Do this

This tile is using several containers and each container acts as a button to perform a specific action like starting a timer or creating a new one  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTuseextracontainers-updated.png)  
cancel

### Don't do this

The use of 4 containers here is unnecessary since all the information will navigate to the same location

## Use containers for functional purposes

To ensure users can anticipate what each component within a Tile will do, we don't recommend using containers for decorative or structural purposes to avoid taps that don't do anything.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOfunctionalcontainers-updated.png)  
check_circle

### Do this

This solution works because the sole action of the Tile is a creation flow, and all other content is floating on the black background  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONToverusecontainers-updated.png)  
cancel

### Don't do this

This Tile is more confusing because it seems like the user would be able to interact with all the containers

## Show glanceable representations of graphs and charts

Glanceability is key for Wear OS design. With limited screen time (around 7 seconds), prioritize essential information in a clear format, that's easy to understand at a glance.

Remember, the watch complements the phone experience, providing quick access to key details.  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DOsimplecharts-updated.png)  
check_circle

### Do this

Show quick, glanceable representations of numerical or statistical information and allow the user to tap to see more in an app if needed  
![](https://developer.android.com/static/wear/images/design/tiles-bestpractices-DONTdetailedcharts-updated.png)  
cancel

### Don't do this

Show detailed numerical or statistical information on the Tile