---
title: https://developer.android.com/design/ui/mobile/guides/widgets/discovery-promotion
url: https://developer.android.com/design/ui/mobile/guides/widgets/discovery-promotion
source: md.txt
---

# Discovery and promotion

App widgets allow your user to deliver key glanceable content and quick actions from your app on their home screens and similar surfaces. Improving your widget's discoverability ensures users are aware of these powerful extensions of your app.

Users discover and add your widget through the widget picker, as shown from the**Widgets**menu that appears when they long-press on the home screen or on your app icon. On some devices, the widget picker displays a suggestions section that shows quality widgets. Additionally, you can promote your widget from within your app at relevant moments when the widget's functionality is most relevant. This guide describes how to to effectively promote your widgets.

## Sizing

Imagine the widget picker as a shopping window. Your widget's default size is its initial display, making a first impression that can greatly influence selection. Use a size that effectively showcases your widget's functionality without cluttering the view.

For more information on choosing an appropriate default size for your widget, see[Sizing](https://developer.android.com/design/ui/mobile/guides/widgets/sizing).
| **Tip:** Specify the`targetCellWidth`and`targetCellHeight`to one of the sizes discussed in the sizing guidance. Ensure that the minimum sizes specified meets the target cell size across most devices in portrait and landscape orientation.

When designing for the default size, consider different form factors such as phones, tablets and foldables.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Dont.jpg)  
cancel

### Don't

Set the same default sizes across all device sizes, make sure to set specific sizes based of each form factors grid sizes.

Avoid publishing multiple versions of the same widget size solely to offer different colors or shapes. Instead, incorporate a configuration activity within the widget to allow users to customize colors, enhancing flexibility and streamline the widget picker.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_Dont.jpg)  
cancel

### Don't

Provide multiple widgets with the same purpose, instead use a configuration activity to customize shapes.

## Content preview

Drive user adoption of your widget by providing an accurate and informative content preview. By mirroring the actual layout and functionality of the widget in the preview, you provide users with a clear understanding of what they can expect once they add it to their home screen.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_CP_Dont.jpg)  
cancel

### Don't

Leave out a preview, as this will cause the widget preview to show only an image app icon.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Do.jpg)  
check_circle

### Do

Provide quality previews that are accurate to the widget size.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Dont.jpg)  
cancel

### Don't

Provide a preview that isn't accurate to the widget size.
**Tip:** You can specify a layout xml resource for your previews using`android:previewLayout`. For more information, see[Improve widget picker experience](https://developer.android.com/develop/ui/views/appwidgets/enhance#improve-widget-picker-experience).  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_CP_Dont.jpg)  
cancel

### Don't

Change the widget's shape or size when the user initially drops it onto the home screen.

If your widget supports dynamic colors, design your previews to also display in those colors. Craft a clear and concise description for your widget that provides a clear value proposition for the user.

## In-app discovery of your widget

You can proactively surface the option to pin relevant widgets at contextually appropriate moments in your app. When doing so keep the following factors in mind:

- Present the pin widget option when it makes the most sense based on the user's actions within the app. For example, after a user successfully completes a task that has a corresponding widget or When a user repeatedly accesses a feature that could be streamlined with a widget.
- Use subtle visual hints such as an icon or a brief animation to draw attention to the option to pin a widget.
- The widget pinning suggestion should never block or hinder the user's primary actions within your app.

![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_WidgetPinning.gif)

For more information, see[Let users pin a widget](https://developer.android.com/develop/ui/views/appwidgets/discoverability#pin)to configure widget pinning from within your app.