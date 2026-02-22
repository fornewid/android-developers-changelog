---
title: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/tiles-principles
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/tiles-principles
source: md.txt
---

# Tiles design principles

Tiles provide quick access to information and actions users need to get things
done. After performing a swipe on the watch face, a user can see how they're
progressing toward their fitness goals, check the weather, and more. Users can
also launch apps and get essential tasks done quickly from tiles.

Users can choose what tiles they want to see on their Wear OS device, both from
the device itself and from the companion app.

## UX design principles

The system-provided tiles use a consistent design language, so users expect
tiles to be each of the following:

- **Immediate:** Tiles are designed to help users quickly complete frequent tasks. Display critical content in a clear information hierarchy so that users can understand the tile's content.
- **Predictable:** Content within each tile should always focus on a user-facing task. This helps users predict what information they will be able to see on the tile, which improves recall.
- **Relevant:** Users take their Wear OS devices wherever they go. Consider how the content in the tile is relevant to the user's current situation and context.

## App icon

| **Note:** The app icon is not displayed in any mocks that follow, since it's not part of the tile layout and might be added at a system level.

The app icon that may appear at the top of the screen is automatically generated
by the system from the [launcher icon](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive). Don't make this icon part of your tile's
layout.  
![](https://developer.android.com/static/wear/images/surfaces/app-icon-do.png)  
check_circle

### Do

Wear OS may display the app icon automatically as the user scrolls through the tile carousel. There is no need to put the app icon in the tile design.  
![](https://developer.android.com/static/wear/images/surfaces/app-icon-dont.png)  
cancel

### Don't

Do not add the app icon in the tile design as it may appear twice or overlapped if also displayed at the system level.

## Design guidance

Keep the following guidelines in mind when creating tiles.

### Focus on a single task

![](https://developer.android.com/static/wear/images/surfaces/tiles-single-task-do.png)  
check_circle

### Do

Focus each tile on a single task, such as **start run.**  
![](https://developer.android.com/static/wear/images/surfaces/tiles-single-task-dont.png)  
cancel

### Don't

Support too many different tasks on a single tile.

### Create separate tiles for each task

If your app supports multiple tasks, consider creating multiple tiles for each
task your app supports. For example, a fitness app could have both a goals tile
and a workout activity tile.

![Step count, workouts this week, and mindfulness tasks](https://developer.android.com/static/wear/images/surfaces/tiles-separate.png)

### Show glanceable representations of graphs and charts

![](https://developer.android.com/static/wear/images/surfaces/tiles-glanceable-do.png)  
check_circle

### Do

Show quick, glanceable representations of numerical or statistical information and allow the user to tap to see more in an app if needed.  
![](https://developer.android.com/static/wear/images/surfaces/tiles-glanceable-dont.png)  
cancel

### Don't

Show detailed numerical or statistical information on the tile.

### Indicate latest data updates

Make it clear to users how recent a tile's data is. If you show cached data,
indicate when it was last updated.

![Middle image shows last session was 45 minutes ago](https://developer.android.com/static/wear/images/surfaces/tiles-data.png)

### Use an appropriate data refresh rate

Choose an appropriate update rate for your tiles, considering the impact on
device battery life. If you're using platform data sources such as heart rate
and step count, Wear OS controls the update rate for you.

![](https://developer.android.com/static/wear/images/surfaces/tiles-data-refresh-rate.gif)

## Empty states

Tiles have two types of empty states. For both, use
[`PrimaryLayout`](https://developer.android.com/reference/androidx/wear/tiles/material/layouts/PrimaryLayout).


![Example of error/permission empty state](https://developer.android.com/static/wear/images/surfaces/tiles-empty-states-1.png)

**Errors or permission**

Tell the user that they need to update their settings or preferences from the
tile.  
![Example of sign in empty state](https://developer.android.com/static/wear/images/surfaces/tiles-empty-states-2.png)

**Sign in**

Provide a clear call to action on a sign-in tile.

<br />

## Show ongoing activities

When an app performs a long-running activity---such as tracking a
workout or playing music---it should show the progress of the
[ongoing activity](https://developer.android.com/training/wearables/notifications/ongoing-activity) in one of more tiles.

If your app also supports tiles that allow users to start these activities,
do the following to minimize user confusion:

- Indicate that an ongoing activity is already in progress.
- If the user taps on such a tile, launch your app and show the in-progress activity. Don't start a new instance of an ongoing activity.

| **Note:** Typically, users can't stop an in-progress activity directly from a tile.

![Each tile includes a call to action button at the bottom, allowing users to open the app](https://developer.android.com/static/wear/images/surfaces/tiles-ongoing-activities.png)

### Required elements

- **Primary data:** The main content that describes the activity.
- **Label:** Displays the status of the activity.

### Optional elements

- **Icon or graphic:** Can be an animation or static image.
- **Bottom compact chip:** Contains a call-to-action.

## Motion on tiles

When you add animations to tiles, help users understand changes:  
![](https://developer.android.com/static/wear/images/surfaces/tiles-motion-do.gif)  
check_circle

### Do

Emphasize if you're updating information on a tile, such as progress toward a step count goal.  
![](https://developer.android.com/static/wear/images/surfaces/tiles-motion-dont.gif)  
cancel

### Don't

Unexpectedly toggle between values.

## Previews

Add a tile preview to help your user see what content is shown in the tile
manager on their Wear OS or handheld device. Each tile can have one
representative preview image. That image should meet the following requirements:

*** ** * ** ***


![Example of tile preview](https://developer.android.com/static/wear/images/surfaces/tiles-previews-1.png)  
**Requirements**

- Export assets at 400px x 400px.
- Provide a circular preview image.
- Use a solid black background.
- Save as a PNG or JPEG.
- Add localized assets for your app's popular languages.

<br />

*** ** * ** ***


![Example of tile preview in tile manager on Wear OS](https://developer.android.com/static/wear/images/surfaces/tiles-previews-2.png)

A tile preview displayed in tile manager on a Wear OS device.  
![Example of tile preview in tile manager on a phone](https://developer.android.com/static/wear/images/surfaces/tiles-previews-3.png)

A tile preview displayed in tile manager on a phone.

<br />

*** ** * ** ***

![](https://developer.android.com/static/wear/images/surfaces/tiles-previews-do.png)  
check_circle

### Do

Emphasize if you're updating information on a tile, such as progress on a step count chart.  
![](https://developer.android.com/static/wear/images/surfaces/tiles-previews-dont.png)  
cancel

### Don't

Show an empty state, show the tile icon in the pagination UI, or place a stroke around the tile.

## Larger screen sizes

To accommodate a variety of Wear OS screen sizes, the ProtoLayout Material
layout templates and Figma design layouts include responsive behavior, allowing
the slots to automatically adapt. Slots are designed to fill the available
width. The main content and secondary label slots hug the content, but the
container holding them fills the available height. Margins are set as
percentages, with additional inner margins added to slots at the bottom and top
of the screen, accounting for fluctuations in the curve of the screen as it
enlarges.

To maximize the larger screen size, use the additional space to provide more
value by allowing users to access additional
information or options. Achieving these layouts requires additional
customization beyond the built-in responsive behavior, such as by creating an
additional layout with more content or by displaying previously hidden slots
after the breakpoint.

Note that the recommended breakpoint is set at the 225dp
screen size.

### Examples of how to design for a larger screen size

#### Add buttons

![Additional workouts shown](https://developer.android.com/static/wear/images/surfaces/tiles-more-buttons.png)

#### Add slots and content

![Show minimum speed in addition to maximum speed](https://developer.android.com/static/wear/images/surfaces/tiles-more-content.png)

#### Add text

![More of the news headline is visible](https://developer.android.com/static/wear/images/surfaces/tiles-more-text.png)