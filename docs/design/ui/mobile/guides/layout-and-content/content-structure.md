---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure
source: md.txt
---

Build up a flexible flow and rhythm with structure and containment methods for
your content.

## 1. Base structure

**To begin creating a solid structure with consistent guardrails, add margins and
columns to your layouts.**

*Margins* provide spacing on the left and right edges of the screen and content.
A standard margin value for compact sizing is 16 dp, but margins should adapt to
accommodate larger screens. Your app's body content and actions must stay within
and align with these margins.

You can also ensure inset safe zones or insets at this step. System bar insets
prevent crucial actions from falling under system bars. See [Draw your content
behind the system bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars#draw-content) for details.
![](https://developer.android.com/static/images/design/ui/mobile/content-structure_safe-areas.png) **Figure 8:** Margins (1) and system bar inset (2)

Use *columns* to build a flexible grid structure for consistent alignment, and
to provide vertical definition to a layout by dividing content within the body
area. Content goes in the areas of the screen containing columns. These columns
lend structure to your layout, providing convenient structure to arrange
elements.
![](https://developer.android.com/static/images/design/ui/mobile/content-structure_columns.png) **Figure 9:** Mobile screens are often divided into four columns

Use a *column grid* to align content with an underlying [grid](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units)
but retain flexible sizing. The column grid can accommodate different form
factors by changing the column sizes and number of columns as needed by the
screen size at certain points while allowing content to also scale. Avoid being
too granular with the column grid, this is what the baseline grid is for:
providing consistent spacing units.

Be careful of establishing an accompanying grid of rows as it can restrict
horizontal content scaling across orientations and form factors, typically
establishing padding rules will provide the needed visual consistency.  
**Place content**


Starting to add copy to the layout structure.
Margins protect content from the screen's edges. Columns provide a
consistent spacing and alignment structure.
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/images/design/ui/mobile/layout-basics-video-2.mp4) and watch it with a video player.

## 2. Apply containment

**Use containment to visually group elements.**

*Containment* refers to using white space and visible elements together to
create a visual grouping. A container is a shape that represents an enclosed
area. In a single layout, you can group together elements that share similar
content or functionality and separate them from other elements using open space,
typography, and dividers.

You can group similar items together with white space or visible division to
help guide the user through content.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-11-breaking-content-into-groupings.png) **Figure 10:** Breaking content into two larger groupings of header and primary copy

*Implicit containment* uses white space to visually group content to create
container boundaries while *explicit containment* uses objects like divider
lines and cards to group content together.

The following figure shows an example of using implicit containment to contain
the header and primary copy. The column grid is used to align and create
groupings. Highlights are explicitly contained within cards. Using iconography
and type hierarchy for greater visual separation.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-12-implicit-containment.png) **Figure 11:** Example of implicit containment

## 3. Position content

Android has multiple ways to handle content elements in their respective
containers that can help position them appropriately, including gravity,
spacing, and scaling.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-13-containment-boundaries.png) **Figure 12:** Layout example showing containment boundaries and position of elements

*Gravity* is a standard for placing an object within a potentially larger
container for specific use cases. The following figure shows examples of
positioning objects start and center (1), top and
center horizontal (2), bottom left
(3), and end and right
(1).
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-14-positional.png) **Figure 13:** Positioning gravity of child content and parent views

## 4. Scale content

**Scaling is crucial to accommodate dynamic content, device orientation, and
screen sizes. Elements can remain fixed or be scaled.**

Noting how images are displayed within their containers with scaling and
position is important to ensure it appears how you want the image to look
despite the device context, otherwise the image's primary focus could appear cut
off, images could be too small or large for the layout, or other undesirable
effects.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-15-center-cropped-image.png) **Figure 14:** Center-cropped image, which ensures the plant is centered within the container regardless of device size

Content that is not notated can appear differently than you expect or want.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-16-make-sure-to-notate.png) **Figure 15:** Content that is not notated can appear in unexpected ways

### Pinned content

Many elements have built in interactions, scrolling, and positioning with slots
or scaffolds. Some elements can be modified to stay fixed instead of reacting to
scrolling, for example floating action buttons (FABs) that house critical
actions.

### Alignment

Use [`AlignmentLine`](https://developer.android.com/jetpack/compose/layouts/alignment-lines) to create custom alignment lines, which parent layouts
can use to align and position their children.  
![](https://developer.android.com/static/images/design/ui/mobile/content-structure_alignment_do.png)  
check_circle

### Do

Establish consistent spacing between like elements.  
![](https://developer.android.com/static/images/design/ui/mobile/content-structure_alignment_dont.png)  
cancel

### Don't

disrupt readability by inconsistently spacing like elements, which can make designs appear haphazard.

## Component layout

[Material 3 components](https://m3.material.io/components) provide their own configurations and
states for interaction and content.

Compose provides convenient layouts for combining Material Components into
common screen patterns. Composables such as [Scaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#scaffold) provide slots for
various components and other screen elements. [Read more about Material
Components and Layout](https://developer.android.com/jetpack/compose/layouts/material#scaffold).