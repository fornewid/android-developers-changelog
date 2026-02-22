---
title: https://developer.android.com/design/ui/cars/guides/templates/grid-template
url: https://developer.android.com/design/ui/cars/guides/templates/grid-template
source: md.txt
---

The Grid template presents items in a grid layout and is useful when users rely
primarily on images to make their selections.

This template can be embedded in the [Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template) to provide tabbed
navigation or included in the [Map + Content template](https://developer.android.com/design/ui/cars/guides/templates/map-content-template) to provide a grid on a
map.

The grid template includes the following:

- Optional [header](https://developer.android.com/design/ui/cars/guides/components/header) (header is replaced with tabs when this template is embedded in the [Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template))
- Grid items (see the [note](https://developer.android.com/design/ui/cars/guides/templates/grid-template#grid-note) below), each containing an [icon or a
  large-size image](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:car/app/app/src/main/java/androidx/car/app/model/GridItem.java;l=57-76;drc=dde88842d72774e3c21813e2f8be5c74fe8d5ca1)
  - Primary text for each grid item (optional)
  - Secondary text for each grid item (optional)
  - An image or icon (optional)
  - A badge
- Optional [floating action buttons](https://developer.android.com/design/ui/cars/guides/components/fab)

For more flexibility and to take advantage of the latest features, use the
Sectioned Item template instead of the Grid template. With the Sectioned Item
template, you can mix and match lists and grids to create a custom browsing
structure.

> [!NOTE]
> **Note:** There is a limit on the number of grid items allowed to be shown, but the limit won't be less than 6 and may be higher in some vehicles. To retrieve the item limit for a given vehicle, use the [`ConstraintManager API`](https://developer.android.com/training/cars/apps#constraint-manager).

![](https://developer.android.com/static/images/design/ui/cars/templates/grid-template-2.png) An example of a grid template. ![](https://developer.android.com/static/images/design/ui/cars/templates/grid-template-1.png) Grid template over a map.

<br />

### Grid template UX requirements

|---|---|
| SHOULD | Limit length of primary and secondary text strings to avoid truncation. |
| SHOULD | Have an action associated with each grid item (information-only items are not recommended). |
| SHOULD | Clearly indicate item state (for grid items that have multiple states, such as selected and unselected) by variations in image, icon, or text. |
| SHOULD | Include a header with an optional title and primary and secondary actions. |
| SHOULD NOT | Include both an [action strip](https://developer.android.com/design/ui/cars/guides/components/action-strip) and a [floating action button](https://developer.android.com/design/ui/cars/guides/components/fab) at the same time. |
| MAY | Show a loading spinner instead of the icon or image for a grid item when an action associated with the item is in progress. |

## Resources

|---|---|
| Type | Link |
| API reference | `GridTemplate, GridTemplate.Builder` |