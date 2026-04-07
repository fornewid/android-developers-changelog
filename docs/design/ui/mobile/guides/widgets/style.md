---
title: https://developer.android.com/design/ui/mobile/guides/widgets/style
url: https://developer.android.com/design/ui/mobile/guides/widgets/style
source: md.txt
---

Styling widgets effectively is crucial for achieving a visually appealing and
consistent user experience. This section delves into the key concepts and
techniques for defining the color and typography to create the most helpful
and engaging Android widgets.

## Color

Use color to express style and communicate meaning. Setting appropriate colors
for your widget colors are crucial for legibility, personalization, and of
course expressing your app's brand identity.

Use Material color roles and tokens to fulfill accessibility contrast guidelines
and support dynamic color features, such as user-generated color and dark or
light themes.

Explore visual hierarchy through accent roles to create vibrant
contrast in elements or explore a more playful custom theme that expresses your
brand.
![Widget with color tokens called out.](https://developer.android.com/static/images/design/ui/mobile/widgets/widgets_expressive_color.png) Use color to define a visual hierarchy for new content for a more expressive widget.

Refer to [Material Design Color guidance](https://m3.material.io/styles/color/system/overview) to learn more about color roles.

## Shape

The shape of your widget sets the mood of your widget. For rectangular widgets,
use the [system corner radius property](https://developer.android.com/reference/android/R.dimen#system_app_widget_background_radius). This property creates consistency
across different devices and helps prevent widget content from being clipped.

If your widget displays minimal data content, like a photo, weather, or current
song playback then try out making your whole widget an expressive shape to bring
an exciting burst of energy to your user's home screen. If you have more complex
layouts and data, consider using expressive shapes for visual hierarchy,
highlighting new content or a call to action.
![Widgets using different shapes](https://developer.android.com/static/images/design/ui/mobile/widgets/widgets_expressive_shape.png) A widget in an expressive shape and a rectangular widget using expressive shapes for visual hierarchy.

To learn more, see [Implement rounded corners](https://developer.android.com/develop/ui/views/appwidgets#rounded-corner).

## Dynamic themes

Starting in Android 12, a widget can use the device theme colors for buttons,
backgrounds, and other components. This provides visual consistency across
different widgets, home screen icons, and wallpapers, offering Android users a
more cohesive user experience. Using the provided color tokens helps your
widget look integrated across device themes provided by different device
manufacturers and the dynamic themes set by the user.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Dynamic_theme.jpg) Image of a widget with color tokens called out.

## Light and dark theme

A dark theme is a low-light version of the device UI that displays mostly dark
surface colors. Users are increasingly switching to dark theme for better
battery life and eye comfort. If your widget doesn't adapt to dark theme, it
will appear out of place and could potentially frustrate users.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Light_and_Dark.jpg) A widget in light mode on the left screen and dark on the right.

## Typography

Typography helps make writing legible and beautiful. Utilize font sizes and
weights to establish a clear hierarchy, guiding the user's eye to the most
important elements. Pay attention to line spacing and letter spacing (kerning)
to improve readability, especially for smaller text displays within the
restricted space of a widget.

### Hierarchy

Hierarchy is communicated through differences in font weight, size, line height,
and letter spacing. The updated type scale organizes text styles into five roles
that are named to describe their purposes. The five text styles are display,
headline, title, subtitle and body. The new roles are device-agnostic, allowing
easier application across a variety of use cases.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_Typography.jpg) A widget showing the use of different type scales.

Although widgets use system fonts, you can still add expressive details with
dramatic typescales: get bolder with headlines, labels, and data.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/widgets_expressive_type.png) A widget combining expressive techniques and using large expressive type.