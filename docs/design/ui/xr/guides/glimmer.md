---
title: https://developer.android.com/design/ui/xr/guides/glimmer
url: https://developer.android.com/design/ui/xr/guides/glimmer
source: md.txt
---

**Clear, glanceable design for optical see-through displays.**

Jetpack Compose Glimmer is a Google design system and UI toolkit for optical
see-through (OST) displays, like wired XR glasses.
A design system provides reusable decisions---from color, type, and shape
primitives, to components and guidance.
[![](https://developer.android.com/static/images/picto-icons/design.svg) Design kit Explore our Figma-based library kits. Start building your app's experiences with modern components, styles, and layouts.](https://www.figma.com/community/file/1579881278082580424/jetpack-compose-glimmer-ui)

## Principles

Jetpack Compose Glimmer is one of the first UI frameworks to be optimized for
transparent displays and glasses form-factor. OST displays project light
directly over the physical world rather than using opaque screen displays.
Glimmer helps developers build high-contrast, glanceable UIs that preserve
real-world presence.

### Transparent display first

Optimized, and backed by research and color science, for transparent displays
and the glasses form factor for thoughtful, beautiful, optical see-through
experiences.

![Transparent display first](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_mfg_transparent.png)

### Hardware input

Interaction inputs are designed around the capabilities of wired XR glasses.

### Purpose-built

Styles and components are purpose-built to use out-of-the-box for glasses.
Jetpack Compose Glimmer is optimized for see-through displays and user comfort.
While purpose built, it's not rigid. It provides a way for you to customize the
focus highlights, in addition to type and color.

![Purpose-built](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_mfg_purposebuilt.png)

## Styles

Jetpack Compose Glimmer's design language features a simplified theme for
optimal visibility on glasses. Color and type can be customized for semantic
expression and app cohesion.
Visual design principles emphasize clarity, legibility, and minimal distraction.
While wired glasses have a wider field of view and may have less "real-world"
interference, you should still consider keeping the UI out of the way.

Glimmer comes with a baseline theme that's optimized for OST glasses. Color and
type can be customized for semantic expression and app cohesion.
Black is transparent on an optical-see-through display. Keep this in mind when
designing, as darker colors will appear dull or transparent, but this can also
be used to create depth.

### Color scheme

The glasses color scheme (collection of color tokens or roles to theme the
color of your app) consists of three accent roles, six surface (or neutral
roles), and their on-color counterparts.

![Color scheme](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_colorscheme.png)

### Customize color

Primary color can be customized to use your brand or primary interaction color.
Consider the contrast, saturation, and power usage of the chosen color.

Read more on [Glimmer's color system](https://developer.android.com/design/ui/ai-glasses/guides/styles/color) and best practices.

### Typography

Jetpack Compose Glimmer has an optimized default typescale. Composed of two
roles with three styles each, type roles are based on their purpose and
hierarchy. For more information, see [Glimmer typography](https://developer.android.com/design/ui/ai-glasses/guides/styles/typography).

### Surface and depth

Surfaces contain content. They provide clear focal points within the user's
field of view, which can contain content or actions. More about [surface and
depth](https://developer.android.com/design/ui/ai-glasses/guides/styles/surface-and-depth) is used in Glimmer.

### Components

Components are purpose-built building blocks for building your UI. Your app
should use Jetpack Compose Glimmer for components, as they're optimized for the
unique use cases of OST glasses. For more information, see [Glimmer
components](https://developer.android.com/design/ui/ai-glasses/guides/components/overview).

Ready to implement components? Check out the [Jetpack Compose Glimmer
documentation](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer).

Glimmer components span multiple UX purposes. Some components include buttons
for actions, progress indicators for communication, stacks for containment,
navigation, and voice indicators for input.