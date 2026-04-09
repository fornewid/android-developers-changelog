---
title: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/canonical-adaptive-layouts
url: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/canonical-adaptive-layouts
source: md.txt
---

# Canonical adaptive design layouts

These canonical layouts are proven, versatile app layouts that provide an
optimal user experience on devices with larger screen sizes.

Tiles
-----

Tiles provide quick access to information and actions users need to get things
done. With a swipe from the watch face, a user can see how they are progressing
towards their fitness goals, check the weather, and more. Launch an app or get
essential tasks done quickly from tiles.

### Customization through use of our components and styling

You can apply your brand's styling to certain components. This includes the
primary color, app icon, font, icons, and any visual asset that applies to your
tile's experience.

### Build for responsive layouts (fixed height screens and percentage margins)

To adapt our code and design layouts to larger screen sizes, we have updated
them to have built-in responsive behavior, including percentage-based margins
and padding. If you are using our templates, you can inherit these updates
automatically through the Tiles API, and only need to supply layouts where you
have added additional content or components after a screen size breakpoint. For
full guidance and recommendations on how to take advantage of a larger screen
size, view our Tiles guidance.

The margins have been set to percentage values, based on the screen size,
in order for rows to fill the available space but not extend too far and get
clipped by the curved screen at the top and bottom. Tiles have a fixed screen
height, so we've adjusted the padding to maximize the limited screen real estate
without creating unwanted clipping.

The two main templates---the Primary Layout and Edge Content Layout (with a
progress ring)---have different margins, but all design layouts are built to map
to one of these. There are three main sections for each tile, and slots that
allocate to each of these. There may in some cases be additional built-in
margins and padding to help content fill the available space while maintaining
its glanceable, balanced design.

See [Build responsive layouts using ProtoLayout](/training/wearables/tiles/screen-size#responsive-layouts) for implementation
guidance.

### Create differentiated experiences

Having four main canonical layouts, with 80+ permutations built into them,
allows for practically limitless customization. Tiles are built on a slot-based
system, so you can replace a slot from the canonical layout with any content of
your choosing. In this case, maintain responsive behavior and follow our design
recommendations.

These customizations should be limited, and should not break the structure of
the tile template. This is to maintain consistency when users scroll through the
tiles carousel on their Wear OS devices.

See [Provide differentiated experiences in Tiles through breakpoints](/training/wearables/tiles/screen-size#breakpoints) for
implementation guidance.

### Add value after the size breakpoint on larger screen sizes

In order to best use the additional space on larger screen sizes, add a size
breakpoint at 225dp. This breakpoint makes it possible to reveal additional
content, include more buttons or data, or change the layout to better suit the
larger screen.

Scrolling and non-scrolling app layouts
---------------------------------------

When designing for adaptive layouts on a round screen, scrolling and
non-scrolling views each have unique requirements for scaling UI elements and
maintaining a balanced layout and composition.
| **Note:** While scrolling views need to be constrained mostly in the vertical direction, non-scrolling views need to be constrained both vertically and horizontally. This generally makes non-scrolling views more challenging to build, and more at-risk of broken layouts on devices with larger screen sizes.

### Non-scrolling app layouts

#### Canonical layouts and full-screen components (including media and fitness)

Non-scrolling app view layouts include media players, pickers, switchers, and
special fitness or tracking screens using progress indicators. You can restrict
the height of any screen, which ensures the user is focused on one task or set
of controls, rather than needing to browse through a list of options. To
accommodate devices with smaller screen sizes, design with the limited size in
mind, ensuring glanceability and embracing the circular screen where relevant.

#### Guidelines for responsiveness (percentage margins)

Define all margins in percentages, and define vertical constraints such that the
main content in the middle can stretch to fill the available display area.

It's best to break a non-scrolling screen into a top, middle, and bottom section
when designing. This way, you can add inner margins to the top and bottom
section to avoid clipping, but allow your middle section to take advantage of
the full width of the screen. Consider the use of the rotary scroll button to
control elements of the screen when its size is limited, as tapping interactions
alone may not provide the best experience.

See [Non-scrolling layouts in Horologist](/training/wearables/compose/screen-size#custom-screens) for implementation guidance.

#### Create differentiated experiences

Non-scrolling layouts are customizable, but are more limited in how much content
can be added to the screen and what kind of components work best. Using
IconButtons instead of Chips makes better use of the limited space, and visual
graphics like ProgressIndicators and large data points help communicate key
information in a graphical way.

All elements that hug the screen's bezel automatically grow with the screen
size, so they become even more impactful.

#### How to add value after the breakpoint on larger screen sizes

When creating a responsive design for larger screen sizes, non-scrolling app
layouts gain the most from the additional screen real estate. Existing elements
can grow to fill the additional space, improving usability, and components and
content can appear after a screen size breakpoint.

Several examples of this behavior appear in the following list:

- Media players can gain additional buttons or larger controls.
- Confirmation dialogs can gain an illustration or more information.
- Fitness screens can gain additional metrics, and elements could grow in size.

See [Provide differentiated experiences in Wear Compose through
breakpoints](/training/wearables/compose/screen-size#breakpoints) for implementation guidance.

### Scrolling app layouts

#### Canonical layouts

Scrolling app view layouts include lists (ScalingLazyColumn) and dialogs. These
layouts make up the majority of app screens, and they represent a collection of
components which need to adapt to larger screen sizes.

Check that the components are responsive---that is, that they fill the available
width and adopt the ScalingLazyColumn adjustments when more of the screen's
height is available. These layouts are built responsively already, and we have
some additional recommendations to take further advantage of the expanded real
estate.

See [Build responsive layouts using Horologist](/training/wearables/compose/screen-size#responsive-layouts) for implementation
guidance.

#### Guidelines for responsiveness (percentage margins)

All top, bottom, and side margins should be defined in percentages to avoid
clipping and provide proportional scaling of elements. Consider that the
PositionIndicator appears when the user scrolls, and it automatically hugs the
screen's bezel no matter its size.

#### Create differentiated experiences

Scrolling views are highly customizable, with the ability to add any combination
of components in any order.

The top and bottom margins can change depending on which components sit at the
top and bottom. This is to prevent content from being clipped by the growing
curve of the screen.

#### Add value after the breakpoint on large screens

As scrolling layouts will automatically show more of what was previously hidden
below the screen fold, there isn't much you need to do to add value. Each
component fills the available width, and in some cases, a component might gain
additional rows of text (such as cards), or components stretch to fill the
available width (such as icon buttons).