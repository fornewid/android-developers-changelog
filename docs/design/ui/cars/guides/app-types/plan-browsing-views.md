---
title: https://developer.android.com/design/ui/cars/guides/app-types/plan-browsing-views
url: https://developer.android.com/design/ui/cars/guides/app-types/plan-browsing-views
source: md.txt
---

# Plan browsing views

Once you've established your top-level content categories, you need to determine how you'll help users find specific songs, podcasts or other media. The goal here is to minimize distraction for drivers by making it easy to quickly find their favorite media while driving.

Use the Car App Templates as guardrails to customize your browsing views and navigation tree. Follow these steps to get started:

1. Determine how many levels deep your content goes. Use as few levels as possible to minimize distraction for drivers.
2. Format your top-level and lower-level browsing views. You can use a list, grid, or combination of both in the sectioned item template.
3. Decide whether to group content into subcategories, which can make your hierarchy flatter.
4. Decide whether to implement search, which is strongly recommended to make browsing easier. If you implement in-app search, you won't need to design the voice and keyboard search interface. Car makers design both the voice search affordance and the keyboards. For details, see[Supporting voice actions](https://developer.android.com/training/cars/media/voice-actions)and[Displaying search results](https://developer.android.com/training/cars/media/create-media-browser/browsable-search).

| **Note:** The content hierarchy of your app is determined by how you define the root media item, its children, the children of those children, and so on. You can apply content styles to browsable media items to specify whether their children display in grid or list views and whether they are grouped under titles. For details, see[Build your content hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy)and[Apply content styles](https://developer.android.com/training/cars/media/create-media-browser/content-styles).

## Browsing view examples

The following examples show some of the ways you can use grids and tabs in your app.
![Browsing view example in landscape mode](https://developer.android.com/static/images/design/ui/cars/app-cuj/browsing-views-1.png)Browsing view example in landscape mode.

<br />

![Browsing view example in portrait mode](https://developer.android.com/static/images/design/ui/cars/app-cuj/browsing-views-2.png)Browsing view example in portrait mode.

<br />

## Browsing view requirements

Follow these requirements and recommendations to help minimize driver distraction and organize your content display for ease of use while driving.

|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement level | Requirements                                                                                                                                  |
| MUST              | - Provide subheader text if you decide to create subcategories within a browsing view                                                         |
| SHOULD            | - Avoid browsable content that extends more than three levels deep from the top level - Decide whether to implement an in-app search function |
| MAY               | - For each browsing view, determine whether to display content in a grid or in a list (list is the default)                                   |