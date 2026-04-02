---
title: https://developer.android.com/design/ui/cars/guides/templates/search-template
url: https://developer.android.com/design/ui/cars/guides/templates/search-template
source: md.txt
---

# Search template

The Search template presents a search bar, keyboard, and results list to enable users to perform searches, such as searching for destinations.

During drives, users can't access the keyboard, but they can use speech-to-text to perform searches and find previous results.  
Search template include the following:

1. Search bar[header](https://developer.android.com/design/ui/cars/guides/components/header)with optional[action strip](https://developer.android.com/design/ui/cars/guides/components/action-strip)
2. List[rows](https://developer.android.com/design/ui/cars/guides/components/row)for search results (within limits)
3. Keyboard (when parked), which apps can choose to show or hide when the template is first displayed.

Apps can customize the background color of markers with any color. The color used for the map marker is applied to the list marker.
| **Note:** The number of list rows allowed to be shown depends on the vehicle. To retrieve the list row limit for a given vehicle, use the[`ConstraintManager API`](https://developer.android.com/training/cars/apps#constraint-manager).

## Search template examples

![Search template example](https://developer.android.com/static/images/design/ui/cars/templates/search-template-1.png)In a parked state, the keyboard is available for typing search terms.![Search template example](https://developer.android.com/static/images/design/ui/cars/templates/search-template-2.png)In a driving state, the keyboard is unavailable, but users can use speech-to-text to perform searches.

## Search template UX requirements

App developers:

|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MUST   | Update the list when a user enters keywords.                                                                                                                  |
| SHOULD | Provide dynamic content (screen refresh) only to show search results during user input.                                                                       |
| SHOULD | Show a loading indicator for searches that are expected to take longer than one second.                                                                       |
| SHOULD | Either show content or launch a keyboard (if there is no content to show) when opening the template.                                                          |
| MAY    | Display the keyboard as either expanded or collapsed when a user opens the template in a parked state (the keyboard is unavailable during the driving state). |
| MAY    | Provide initial search text.                                                                                                                                  |
| MAY    | Provide hint text on the search bar.                                                                                                                          |
| MAY    | Display a default list of past results or other relevant content.                                                                                             |

## Resources

|---------------|------------------------------------------|
| Type          | Link                                     |
| API reference | `SearchTemplate, SearchTemplate.Builder` |