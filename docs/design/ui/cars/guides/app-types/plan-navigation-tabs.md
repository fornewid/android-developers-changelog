---
title: https://developer.android.com/design/ui/cars/guides/app-types/plan-navigation-tabs
url: https://developer.android.com/design/ui/cars/guides/app-types/plan-navigation-tabs
source: md.txt
---

# Plan navigation tabs

Help minimize distractions for drivers by prioritizing simple and clear top-level navigation for media apps.

Most cars have already established the structure and visual display of app bars. To create tabs in a templated media app, see[Using SectionedItemTemplate inside a TabTemplate](https://developer.android.com/training/cars/apps/media#sectioned-tab).

## Plan your categories

You'll need to decide which top-level content categories to represent as tabs on the app bar, and which icons and labels to supply for each tab. Avoid overly-broad categories that are difficult to browse while driving. Instead, opt for categories that showcase tailored content, such as:

- Frequently used: for example, playlists or channels
- Preferred: for example, favorite artists
- Timely: for example, recent songs
- Curated: for example, recommended for you

| **Note:** Top-level content categories are browsable media items that are the children of the root media item in your content hierarchy. Google provides icons and labels as resources associated with these browsable media items. For details, consult[Build your content hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy).
![Navigation tabs example](https://developer.android.com/static/images/design/ui/cars/app-cuj/navigation-fig-1.png)In this example, the tailored content includes recently-played songs, a way to discover more music, and a list of all of the user's music.

### Navigation tab requirements

It's important to create a simple and consistent navigation model that accommodates all possible screen sizes.

Follow these requirements and recommendations as you design the navigation tabs for your media app:

|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Requirement level | Requirements                                                                                                                         |
| MUST              | - Implement no more than 4 tabs (for AAOS) - Provide a label and a monochrome (preferably white) vector icon for each tab (for AAOS) |
| SHOULD            | - Keep tab labels as short as possible, to prevent their being truncated                                                             |

| **Note:** Be sure to allow car makers to use labels without icons when both won't fit.