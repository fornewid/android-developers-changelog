---
title: https://developer.android.com/design/ui/cars/guides/app-types/customize-playback-controls
url: https://developer.android.com/design/ui/cars/guides/app-types/customize-playback-controls
source: md.txt
---

# Customize playback controls

Once you've decided how to organize your app content for navigating and browsing, consider whether you want a queue or any custom controls for playing the content.

Car makers and Google take care of implementing and styling the playback view, minimized control bar, and queue. They also provide a basic set of playback controls, including:

- **Play/Pause**
- **Next**(If supported by your app)
- **Previous**(If supported by your app)
- **Overflow**

However, if you want to customize the queue or provide additional playback actions, you need to decide:

- Whether to display thumbnails for queue items
- Whether to display an icon or elapsed time for the currently playing item in the queue
- Whether to include previously played items in the queue
- Which custom actions you want on the control bar, and whether they should replace the car makers'**Next** and**Previous**controls
- What the icons representing the relevant states of each action (such as available and disabled) will look like

| **Note:** Custom actions display in the order in which they are added to the`PlaybackState`. Their icons are specified as icon resources. For details, consult[Add custom playback actions](https://developer.android.com/training/cars/media#custom-icons).

## Playback view examples

![Currently playing song](https://developer.android.com/static/images/design/ui/cars/app-cuj/customize-playback-controls-1.png)Playback view displays the currently playing song.

<br />

![Overflow menu on the right](https://developer.android.com/static/images/design/ui/cars/app-cuj/customize-playback-controls-2.png)The user has opened the overflow menu on the right side of the screen, which offers more functionality.  
![Playback controls in a media app](https://developer.android.com/static/images/design/ui/cars/app-cuj/customize-playback-controls-3.png)A sample view of playback controls in a media app.

<br />

### Playback control requirements

When designing playback controls, prioritize the following:

- **Consistent app UI**: App developers should make custom media playback controls in cars consistent with users' experiences on other apps and devices
- **Readability**: Text can appear smaller when paired with iconography, so text in icons should be maximized within the available space.

These requirements and recommendations will help you create effective controls.

|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement level | Requirements                                                                                                                                                                                                                                  |
| MUST              | - Provide[monochrome vector icons](https://developer.android.com/training/cars/media#custom-action-icons)for any custom actions you add, and change them dynamically to indicate state                                                        |
| SHOULD            | - If using text or numbers in an icon,[use the maximum space](https://developers.google.com/cars/design/design-foundations/visual-principles#make_content_easy_to_read)in the bounding box to make the text as large and readable as possible |
| MAY               | - Provide up to 6[customactions](https://developer.android.com/training/cars/media#custom-action-icons)(or up to 8, if not using**Next** and**Previous**)                                                                                     |

<br />

## Queue

You should also provide your user with a quick and easy way to browse the queue of upcoming media. The queue of upcoming media can include artists and thumbnails, as shown in the following examples.
![Queue in portrait mode](https://developer.android.com/static/images/design/ui/cars/app-cuj/customize-playback-controls-4.png)Queue in portrait mode

<br />

![Queue in landscape mode](https://developer.android.com/static/images/design/ui/cars/app-cuj/customize-playback-controls-5.png)Queue in landscape mode

<br />

### Queue requirements

To help minimize distractions while driving, make sure users can see what's currently playing at a glance.

|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement level | Requirements                                                                                                                                                                                                                                                             |
| SHOULD            | - Provide an indicator for the currently playing queue item - Include previously played items in the queue To learn more about progress indicators and the queue, review[Enable playback control](https://developer.android.com/training/cars/media#implement_callback). |
| MAY               | - [Provide thumbnails](https://developer.android.com/training/cars/media#display-artwork)for queue items                                                                                                                                                                 |