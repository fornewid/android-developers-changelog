---
title: https://developer.android.com/design/ui/cars/guides/templates/place-list-map-template
url: https://developer.android.com/design/ui/cars/guides/templates/place-list-map-template
source: md.txt
---

# Place list (map) template

The Place List template presents an ordered list of locations (or containers for sublists), overlaid on a map provided by the app library.
**Note:** This template is for point-of-interest apps  
**Place list (map) template includes:**

- [Header](https://developer.android.com/design/ui/cars/guides/components/header)(in card) with optional refresh button for users to request a list update (doesn't add to[step count](https://developer.android.com/cars/design/create-apps/apps-for-drivers/plan-task-flows#steps-refreshes))
- [Action strip](https://developer.android.com/design/ui/cars/guides/components/action-strip)(optional)
- Base map (full-screen, not drawn by apps)
- [List rows](https://developer.android.com/design/ui/cars/guides/components/row)within limits\*
- [Markers](https://developer.android.com/design/ui/cars/guides/templates/place-list-map-template#markers)

### Markers

Use markers to link list items with locations on the map or to identify an anchor location. You can designate markers as tappable (as with any area on a map) to allow users to tap a marker to trigger an action such as displaying information about that marker.  
Types of markers:

1. **Map marker**: on map, labeled with one of the following: text (up to 3 letters), an icon, or an image
2. **List marker**(not shows): On list, marker that corresponds to map marker, with matching metadata and image or icon asset
3. **Anchor marker**(optional): On map, used to show center of search area

Apps can customize the background color of markers with any color. The color used for the map marker is applied to the list marker.
![](https://developer.android.com/static/images/design/ui/cars/templates/place-list-map-template-markers.png)Customize your markers to match your app's branding

<br />

### Place List (map) template examples

![](https://developer.android.com/static/images/design/ui/cars/templates/place-list-2.png)Location list with corresponding numbered map markers and an anchor marker in the center (shown in light blue).

## Place list (map) template UX requirements

App developers:

|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MUST   | Show duration or distance for each list item (except for browsable items).                                                                                                                      |
| MUST   | Associate an action with each list row (information-only rows are not allowed).                                                                                                                 |
| SHOULD | Include at least one location or browsable list item (container) on the list.                                                                                                                   |
| SHOULD | Show a corresponding marker on the map for each location on the list.                                                                                                                           |
| SHOULD | Limit locations to those that are closest or most relevant.                                                                                                                                     |
| SHOULD | Consider supporting[content refresh](https://developer.android.com/training/cars/apps/poi#refresh-content)for the list, so users can update it after driving out of range of the original list. |

## Resources

|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type              | Link                                                                                                                                                                                                                                             |
| API reference     | ` `[PlaceListMapTemplate](https://developer.android.com/reference/androidx/car/app/model/PlaceListMapTemplate)`, `[PlaceListMapTemplate.Builder](https://developer.android.com/reference/androidx/car/app/model/PlaceListMapTemplate.Builder)` ` |
| Developer's guide | [Access the map templates](https://developer.android.com/training/cars/apps/poi#access-map-templates)                                                                                                                                            |