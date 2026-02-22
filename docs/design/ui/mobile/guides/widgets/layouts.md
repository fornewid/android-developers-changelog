---
title: https://developer.android.com/design/ui/mobile/guides/widgets/layouts
url: https://developer.android.com/design/ui/mobile/guides/widgets/layouts
source: md.txt
---

# Canonical widget layouts

Craft effective widget layouts by first identifying your core content. Your layout dictates how information and interactive elements are organized within your widget. Android offers several prebuilt layouts for toolbars, text, list and grid-type widgets to streamline this process.
| **Note:** View detailed layout specs in our[Figma Widget Canonical Builder](https://goo.gle/widget-canonical), and find the code samples using Jetpack Glance in the[Android Platform Samples GitHub repository](https://github.com/android/platform-samples/tree/main/samples/user-interface/appwidgets/src/main/java/com/example/platform/ui/appwidgets/glance).

## Text

Text layouts are ideal for displaying concise information. Enhance the visual appeal of your widget by optionally including an image alongside the text.  
**Text only**

Ideal for titles, status updates, short descriptions, or any scenario where a single line of text effectively conveys the message. Refer to the[Canonical layout sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/appwidgets/src/main/java/com/example/platform/ui/appwidgets/glance)for guidance on dynamically scaling text content based on widget size.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Text_only.jpg)  
**Text and image**

Include an image for added visual impact. For more information, see[Breakpoints](https://developer.android.com/design/ui/mobile/guides/widgets/sizing#breakpoints)to learn how to adapt this layout for different screen sizes.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Text_and_Image.jpg)

## Toolbars

Use toolbar layouts to provide users with quick access to frequently used tasks in your app, in a flexible layout that adapts across widget sizes.  
**Search Toolbar**

A search toolbar layout is intentionally designed to draw focus to search as a primary action in the toolbar. Additional handy buttons can provide quick access to frequently used functions.

![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Search_Toolbar.jpg)  
**Toolbar**

Toolbars presents app branding followed by buttons for the most used tasks that are ideal for toggleable settings or task links. When resizing, less commonly used options can be hidden in favor of more common actions. Use[Breakpoints](https://developer.android.com/design/ui/mobile/guides/widgets/sizing#breakpoints)to add a new minimum 48dp tappable button when there's room.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Toolbar.jpg)

<br />

## Lists

Use list layouts to organize multiple items in a clear, scannable format. This is ideal for news headlines, to-do lists or messages. Organize content into a structured, easily scannable list. Choose between containerized or containerless presentation based on your content needs.  
**Text and image list**

Easily scannable text and image lists are perfect for showcasing multiple content types, such as news headlines, playlists with album art, or messages.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Text_Image.jpg)  
**Checklist**

The checklist layout is perfect for displaying tasks, providing clear tap targets for users to easily mark items as done.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Checklist.jpg)  
**Action list**

Provide intuitive control grouping with action lists, where visual on/off states offer immediate feedback on item statuses.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_Action_List.jpg)

## Grid

Present images in a compact, flexible, visually rich grid with optional labels. Use columns and rows that adapt to different screen sizes.  
**Image only**

Create visually impactful, scrollable image galleries using image-only grids. Rows and columns automatically adapt to various screen sizes for optimal presentation.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Image_Only.jpg)  
**Image and text**

You can also incorporate text labels and descriptions, enriching your image grid content with additional context and information.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Image_and_Text.jpg)