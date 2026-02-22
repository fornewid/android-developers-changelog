---
title: https://developer.android.com/training/wearables/watch-face-designer/advanced
url: https://developer.android.com/training/wearables/watch-face-designer/advanced
source: md.txt
---

This page explains more advanced use cases for Watch Face Designer, including
how to add support for subdials, [complications](https://developer.android.com/training/wearables/complications), and color themes. To learn
more about getting started, view the [basics](https://developer.android.com/training/wearables/watch-face-designer/basics) guide.

## Subdials

You can create analog watch hands that rotate within a subsection of the watch
face, just like a [subdial](https://www.watchtime.com/brands/glashutte-original/little-helpers-a-closer-look-at-subdials) on a real wristwatch.

To do so, complete the following steps:

1. [Create an empty frame](https://help.figma.com/hc/articles/360041539473-Frames-in-Figma-Design) that covers the area where you've
   placed the subdial in your design:

   ![](https://developer.android.com/static/wear/images/design/watch-face-designer/subdial-container.png) **Figure 1**: Empty frame covering a subdial slot
2. Design your second hand inside of this frame:

   ![A good default for the hand is pointing from the center to the top
   of the subdial](https://developer.android.com/static/wear/images/design/watch-face-designer/seconds-in-container.png) **Figure 2**: Second hand design sitting in a containing frame
3. Select the subdial frame that contains the second hand. Then, in the
   **Watch Face Designer** , set **Rotate around** to "Layer center:"

   ![Rotation behavior appears in the left middle of the window](https://developer.android.com/static/wear/images/design/watch-face-designer/rotate-around.png) **Figure 3**: After selecting the containing frame (left), choose second hand rotation behavior (right)

## Complications

To add a complication slot, [add a frame to your watch face](https://help.figma.com/hc/articles/360041539473-Frames-in-Figma-Design).
Inside this frame, design what the complication slot will look like when it's
empty. This forms the base design for the other types of complications, such as
icons and text.

There are many different kinds of complications. Your watch face provides
templates for each type, and the apps on a user's watch decide which template to
use and which data to provide for themselves. The user chooses which app goes in
which complication slot.

Select your frame containing the design for the complication slot. Then, in the
**Watch Face Designer** , change **Behavior** to "Complication slot." This
process creates a [component](https://help.figma.com/hc/articles/360038662654-Guide-to-components-in-Figma), with one variant (an empty
design).
![Behavior dropdown appears near the top-left corner of the window](https://developer.android.com/static/wear/images/design/watch-face-designer/complication-slot.png) **Figure 4**: After selecting the containing frame (left), choose the "complication slot" behavior (right)

### Apply complication slot types

Because it's not that useful to include a complication slot that only supports
the "empty" type, add another type. In the Watch Face Designer window, press
**+ Support a new type** and select "Short text." Short text is a complication
type supported by most apps, which shows two small labels alongside an icon.
![Complication types supported appears near the top middle part of the
window](https://developer.android.com/static/wear/images/design/watch-face-designer/short-text.png) **Figure 5**: Add support for a "short text" complication type

This step creates another variant for us to represent our design for this
complication type. Select the "Short text" row to jump to it.

When editing layers inside a complication template, a "Behavior" option appears.
This option is similar to the one on watch faces, but here you can select
behaviors that are specific to the type of complication that you're editing.

For this example, layers inside a short text complication can either be your
app's title, its text, or a *single-color* icon. Single-color means that the
icon inherits the color that you set for it in Figma.

After you [make a rectangle](https://help.figma.com/hc/articles/360040450133-Shape-tools) where you want your app's icon to
appear on the watch face, navigate to the **Watch Face Designer** window and set
**Behavior** to "Single-color icon:"
![Behavior dropdown appears near the top-left corner of the window](https://developer.android.com/static/wear/images/design/watch-face-designer/icon-role.png) **Figure 6**: Change appearance of a complication slot to show a single-color icon

Next, create two [text layers](https://help.figma.com/hc/articles/360039956434-Guide-to-text-in-Figma-Design). These layers represent two more
"short text" slots: one for the title and one for the text:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/template.png) **Figure 7**: Two text layers shown in a complication slot layout

The preview shows how the complication is coming together. This example shows
how a complication might look if the calendar app were assigned to this slot.

To show text in all-uppercase characters, as shown in the following image, use
the [text case feature](https://help.figma.com/hc/articles/360039956634-Explore-text-properties#letter-case) in Figma's **Typography** menu.
!['Case' appears near the middle. 'Uppercase' is the second
option from left](https://developer.android.com/static/wear/images/design/watch-face-designer/capital.png) **Figure 8** : The **Typography** panel in Figma, shown with "Uppercase" selected

Note that, unlike with [digital time](https://developer.android.com/training/wearables/watch-face-designer/basics#digital-time), there is no arbitrary font export for
complication text. Complications are always drawn using the Wear OS device's
system font, which can vary but is typically Roboto.

To add support for additional types of complications, or customize related
settings like **Default app** or whether the slot appears when the watch is in
[ambient mode](https://developer.android.com/training/wearables/always-on), select the complication slot within your watch face:
!['Default app' and 'Always on' both appear near the bottom-left corner](https://developer.android.com/static/wear/images/design/watch-face-designer/default-app.png) **Figure 9** : Watch Face Designer supports additional customization for complication slots, including setting a **Default app** and toggling whether the complication should appear in **Always-on** (system ambient) mode

## Color themes

Within your watch face, you can include multiple options for color themes. The
user can then choose the theme that they want, using the watch face picker on
their watch.

Watch Face Designer includes support for color themes using [Figma
styles](https://help.figma.com/hc/articles/360039238753-Styles-in-Figma-Design).

Consider the case where, given the following watch face, you want to let the
user customize the colors of the watch hands and dial:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/bauhaus.png) **Figure 10**: The "Bauhaus" sample watch face, which provides support for changing the color of the watch hands and dial

### Create the first style

To create a color style that's customizable on the watch, create a new style:

1. Deselect everything on the canvas.
2. In the right sidebar, next to **Styles** , select the **+** button.

You must name it in a specific way:  

    Watch Face Name/Element Family Name/Descriptive Color Name/Specific Element Name

| **Note:** Figma uses forward slashes (`/`) to represent folders in styles.

In this case, the sample watch face's name is `Bauhaus`, so the color starts
with that, followed by `Hands`, which is the element that users can customize.
Then, give a descriptive color name, such as `Charcoal`, and specify which
specific element -- hour hand -- should have its color changed.

Putting this all together, the final name is: `Bauhaus/Hands/Charcoal/Hours`:
!['Name' appears near the middle of the dialog](https://developer.android.com/static/wear/images/design/watch-face-designer/creating-style.png) **Figure 11** : The **Create new color
style** dialog, where you can add user-customizable color styles to a watch face

Follow a similar process to create a custom color theme for the minute hand:
![The Minutes element appears underneath the Hours element](https://developer.android.com/static/wear/images/design/watch-face-designer/creating-charcoal.png) **Figure 12** : Applying the **Charcoal** style to another element within the watch face

Finally, assign these colors to the actual hands that appear on the watch face:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/assigning-styles.png) **Figure 13** : Assigning the `Bauhaus/Hands/Charcoal/Minutes` theme to the watch face's minute hand

### Add another style

Create a new style by changing the `Theme Name` part of the style. The following
example adds a new style called `Rust` (`Bauhaus/Hands/Rust/Hours`):
![The new color theme appears underneath the first color theme](https://developer.android.com/static/wear/images/design/watch-face-designer/creating-rust.png) **Figure 14** : A new color theme for the watch face's hands called **Rust**

The user can then switch between the "Charcoal" and "Rust" color themes on their
device, and your watch face's hour and minute hands get recolored accordingly:
![Each color theme appears as an item in a list. The element name
appears in the screen title](https://developer.android.com/static/wear/images/design/watch-face-designer/hands.png) ![](https://developer.android.com/static/wear/images/design/watch-face-designer/customized.png)

<br />

**Figure 15** : The user-facing configuration screen for selecting a color theme for the watch face's hands (left), as well as the effect of selecting **Rust** from this list (right).

### Apply to other elements

Follow similar steps to make other elements of our watch face themable. These
themes can be mix-and-matched, and you can use any number of color styles to
create complex swappable themes:
![Styles are organized by element family, then by color theme name,
then by specific elements](https://developer.android.com/static/wear/images/design/watch-face-designer/all-styles.png) **Figure 16**: A more complete list of styles

With the preceding set of styles, you've provided two options for the
hands---`Rust` and `Charcoal`---and three options for the dial---`Light`, `Dark`, and
`Duotone`:
![Each color theme appears as an item in a list. The element name
appears in the screen title](https://developer.android.com/static/wear/images/design/watch-face-designer/dial-options.png) **Figure 17**: User-facing configuration screen for choosing among the supported color themes for the watch face's dial