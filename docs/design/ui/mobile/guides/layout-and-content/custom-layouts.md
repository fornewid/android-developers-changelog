---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/custom-layouts
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/custom-layouts
source: md.txt
---

Inputs, content, or other actions may appear relative to each other or
constrained to a parent container. Layouts can be more custom, but make sure to
follow consistent grouping, columns, and spacing.

Authentication is a common relative layout, as shown in the following figure. Where a custom layout is described by how the UI elements in relation to each other.

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-13-containment-boundaries.png)

Layouts can also use a combination of layout types. For example, you might pair a
carousel or horizontal scroll with vertical cards. Or, you could present a
custom chart with vertical list data.

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-27-combo-of-groupings-grids.png)

You can present content in scrolling rows or columns with lazy rows and lazy
columns.

Full-screen layout is another common layout, as used in [immersive mode](https://developer.android.com/design/ui/mobile/guides/layout-and-content/immersive-content).
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-29-full-screen.png) **Figure 27:** Full screen layout, as used in immersive mode

If you're working with Views instead of Compose, you can use
[`ConstraintLayout`](https://developer.android.com/develop/ui/views/layout/constraint-layout) to lay out views according to relationships between
sibling views and the parent layout, allowing for large and complex layouts.
`ConstraintLayout` lets you build entirely by dragging and dropping instead of
editing the XML using the layout editor. Learn more about [building a UI with
Layout Editor](https://developer.android.com/studio/write/layout-editor).

Learn more about [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics) and what makes up a composable.

## Webviews

A Webview is a view that displays in-app web pages. In most cases, we recommend
using a standard web browser, like Chrome, to deliver content to the user. To
learn more about web browsers, read the guide for [invoking a browser with an
intent](https://developer.android.com/guide/components/intents-common#Browser).