---
title: https://developer.android.com/develop/ui/compose/tooling/editor-actions
url: https://developer.android.com/develop/ui/compose/tooling/editor-actions
source: md.txt
---

Android Studio has features inside the editor area to improve your productivity
with Jetpack Compose.

## Live templates

Android Studio comes with these Compose-related live templates, which allow you
to enter code snippets for fast insertion by typing the corresponding template
abbreviation:

- `comp` to set up a `@Composable` function
- `prev` to create a `@Preview` composable function
- `paddp` to add a `padding` Modifier in dp
- `weight` to add a `weight` Modifier
- `W`, `WR`, `WC` to surround the current composable with a `Box`, `Row`, or `Column`container

## Gutter icons

Gutter icons are contextual actions visible on the sidebar, next to the line
numbers. Android Studio introduces several gutter icons specific to Jetpack
Compose to ease your developer experience.

### Deploy preview

You can deploy a `@Preview` to the emulator or physical device directly from the
gutter icon:

![The user clicking a preview function's deploy gutter icon, and deploying the
preview to the
device](https://developer.android.com/static/develop/ui/compose/images/tooling-preview-deploy-gutter-icon.gif)

### Color picker

Whenever a color is defined inside or outside a composable, its preview is shown
on the gutter. You can change the color via the color picker by clicking on it
like this:

![The user clicking a color in the gutter, bringing up a color
picker](https://developer.android.com/static/develop/ui/compose/images/tooling-color-picker.gif)

### Image resource picker

Whenever a drawable, vector, or image is defined inside or outside a composable,
its preview is shown on the gutter. You can change it via the image resource
picker by clicking on it like this:

![The user clicking an icon in the gutter, bringing up the resource
picker](https://developer.android.com/static/develop/ui/compose/images/tooling-resource-picker.gif)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics)
- [Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers)
- [Lists and grids](https://developer.android.com/develop/ui/compose/lists)