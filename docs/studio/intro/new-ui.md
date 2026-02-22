---
title: https://developer.android.com/studio/intro/new-ui
url: https://developer.android.com/studio/intro/new-ui
source: md.txt
---

# New UI in Android Studio

Android Studio Ladybug Feature Drop introduces the New UI from the[IntelliJ Platform 2024.2 update](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/)as the default theme. The New UI brings a streamlined design and enhanced features, making it easier for both new and experienced developers to navigate their workflow more efficiently.

## Key design changes

The New UI brings a host of improvements to enhance your workflow and provides a more consistent environment. It has been designed to reduce visual complexity, provide easy access to essential features, and progressively disclose advanced features as needed, resulting in a cleaner look and feel. The following sections explain the biggest changes you'll see in the New UI in Android Studio.

### Themes and icons

The updated light and dark themes offer improved color contrast and more consistent design for a visually appealing experience. You can now easily toggle between themes based on your preference.  

### Light

![](https://developer.android.com/static/studio/images/new-ui/light-theme.png)**Figure 1.** The**Light**theme for the New UI.

### Light with Light Header

![](https://developer.android.com/static/studio/images/new-ui/light-with-light-theme.png)**Figure 2.** The**Light with Light Header**theme for the New UI.

### Dark

![](https://developer.android.com/static/studio/images/new-ui/dark-theme.png)**Figure 3.** The**Dark**theme for the New UI.

The New UI also features a modernized set of icons that are cleaner, more legible, and easier to distinguish, providing a more visually consistent experience across the IDE.
![](https://developer.android.com/static/studio/images/new-ui/themes-and-icons.png)**Figure 4.**The icon set for the New UI.

### Simplified main toolbar

The New UI features a decluttered main toolbar that prioritizes the most-used actions, such as selecting the running device, managing version control, and switching projects. This lets you spend less time searching for tools and more time coding.
![](https://developer.android.com/static/studio/images/new-ui/classic-toolbar.png)**Figure 5.**The Classic UI.

<br />

![](https://developer.android.com/static/studio/images/new-ui/new-toolbar.png)**Figure 6.**The New UI, featuring a simplified main toolbar.

Customize the main toolbar with your essential actions in**Settings \> Appearance \& Behavior \> Menus and Toolbars**.
![](https://developer.android.com/static/studio/images/new-ui/custom-toolbar.png)**Figure 7.**Settings to customize your main toolbar.

#### Widgets for Git and projects

The main toolbar now includes two new menu widgets:

- A**Project Widget**for browsing recent projects or creating a new one.

![](https://developer.android.com/static/studio/images/new-ui/project-widget.png)**Figure 8.**The location of the Project Widget in the main toolbar.

- A**Git Widget**for version control management and commonly-used Git actions. The Git Widget has moved to the top of the status bar, but you can move it back to its previous location in the bottom right.

![](https://developer.android.com/static/studio/images/new-ui/git-widget.png)**Figure 9.**The location of the Git Widget in the main toolbar.

#### Run configurations and profiling actions

Run configurations and profiling actions are streamlined into a new**Run Widget**, with profiling actions being moved to an overflow menu.
![](https://developer.android.com/static/studio/images/new-ui/classic-run-config.png)**Figure 10.**Run configurations in the Classic UI.

<br />

![](https://developer.android.com/static/studio/images/new-ui/classic-profiling-actions.png)**Figure 11.**Profiling actions in the Classic UI.

<br />

![](https://developer.android.com/static/studio/images/new-ui/run-widget.png)**Figure 12.**The location of the Run Widget in the New UI.

### Redesigned tool windows

Tool windows are now better organized and docked to the sides of the main window. The tool window bar has been streamlined to only display a selection of tool window icons, with the rest accessible from an overflow menu. This new tool window layout is more intuitive and offers flexible options to customize your workspace.

Access hidden tool windows using the**More tool windows**button. Once selected, the tool window opens and its button appears on the default toolbar.
Alas, your browser doesn't support HTML5 video. That's okay! You can still[download the video](https://developer.android.com/static/studio/images/new-ui/tool-windows-overflow.mp4)and watch it with a video player.**Figure 13.**The location of the tool windows overflow menu in the new UI.

#### Vertical and horizontal splits

Split your workspace by dragging tool window icons. Drop them below the sidebar separator for a vertical split, or to the opposite sidebar for a horizontal split.
Alas, your browser doesn't support HTML5 video. That's okay! You can still[download the video](https://developer.android.com/static/studio/images/new-ui/vertical-split.mp4)and watch it with a video player.**Figure 14.**A vertical split.

<br />

Alas, your browser doesn't support HTML5 video. That's okay! You can still[download the video](https://developer.android.com/static/studio/images/new-ui/horizontal-split.mp4)and watch it with a video player.**Figure 15.**A horizontal split.

### New location for UI Tool Controls

UI Tool Controls (Code/Split/Design) for both Compose and view-based previews now reside outside the editor tabs, offering easier access.
![](https://developer.android.com/static/studio/images/new-ui/classic-ui-tool.png)**Figure 16.**UI Tool Controls in the Classic UI.![](https://developer.android.com/static/studio/images/new-ui/new-ui-tool.png)**Figure 17.**UI Tool Controls in the New UI.

### Navigation bar

The navigation bar displays the full path to your selected file. You can move the navigation bar to the top of the window by going to**View \> Appearance \> Navigation Bar**in the main menu.
![](https://developer.android.com/static/studio/images/new-ui/new-nav-bar.png)**Figure 18.**The navigation bar in the New UI.

### Compact Mode

Designed for smaller screens, this mode makes the IDE more compact. Toolbars and headers are shorter, icons and buttons are smaller, and there's less space between elements.  

### On

![](https://developer.android.com/static/studio/images/new-ui/compact-full.png)**Figure 19.**Android Studio window in Compact Mode.![](https://developer.android.com/static/studio/images/new-ui/compact-toolbar.png)**Figure 20.**Toolbar height in Compact Mode.

### Off

![](https://developer.android.com/static/studio/images/new-ui/default-full.png)**Figure 19a.**Android Studio window in the default mode.![](https://developer.android.com/static/studio/images/new-ui/default-toolbar.png)**Figure 20a.**Toolbar height in the default mode.

You can enable Compact Mode in either of the following ways:

- Navigate to**View \> Appearance \> Compact Mode**.
- Open the IDE settings, select**Appearance and Behavior \> Appearance** , and enable the**Compact mode**option.

## Continued support for Classic UI

Developers who prefer the Classic UI can access it through a plugin available on the[JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24468-classic-ui). IntelliJ will continue to support the Classic UI plugin for at least one year to help ensure a smooth transition for all developers.

To learn more, see the[announcement blog post from JetBrains](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/#how-long-will-we-continue-to-support-the-old-ui).