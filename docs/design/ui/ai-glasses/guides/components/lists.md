---
title: https://developer.android.com/design/ui/ai-glasses/guides/components/lists
url: https://developer.android.com/design/ui/ai-glasses/guides/components/lists
source: md.txt
---

Lists are containers of elements with built-in scrolling and focus.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists.png)

### Principles

**Clear Organization**: Lists should present information in a clear and easily scannable vertical arrangement.

**Consistent Item Presentation**: List items should follow a consistent visual structure.

**Focusability \& Navigation**: In interfaces relying on directional navigation, lists must clearly indicate the currently focused item.

**Interactivity**: List items often represent selectable or actionable elements.

## Usage \& Placement

Lists can contain various sibling content with repeatable elements. Unlike stacks, lists fill the app view container.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_selectable.png)Lists can show one or more selectable items within a view.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_scrim.png)**Use scrims to indicate overflow content**

When a list contains more items than will fit within a view, a black scrim is used near the list's bounds.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_title.png)**Lists can use a title if necessary**

A static or sticky title can be used in a list for clarity.

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_dont.png)  
cancel

### Don't

Have more than one list per view, this is overwhelming visually and focus wise.

<br />

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_depth.png)**Use depth to indicate focus**

List items move between 0 and +4 depth for unfocused and focused states.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_actionable.png)**List items can be actionable**

Items in a list can act as actions. Keep the action to the list item

## Anatomy

List is composed of a scrolling container and consistently spaced list items. Lists should vertically scroll, with minimal overshoot, when the number of items exceeds the viewport.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_anatomy.png)**A.**Container - scrollable area

**B.**List item

**C.**System bars

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_lists_item.png)List Item: Each individual element within the list.

**A.**Shape

**B.**Border

**C.**Leading icon

**D.**Text content

**E.**Trailing indicator

## Customization

The majority of customization happens with list items.

<br />

|              Properties              | Customization |                                                                                                  Defaults                                                                                                  |
|--------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List item: Shape                     | Yes           | 40 dp                                                                                                                                                                                                      |
| List item: Leading and Trailing icon | Yes           | Medium Symbol Icon                                                                                                                                                                                         |
| List item: Padding values            | Yes           | 2d dp, 20 dp                                                                                                                                                                                               |
| List item: Content                   | Yes           | Single-line: One Text composable for the primary label using Body Small Double-line: A Column containing two Text composables for a primary and secondary label Primary: Title Small Secondary: Body Small |
| List: verticalArrangement            | Yes           | 20 dp                                                                                                                                                                                                      |

<br />