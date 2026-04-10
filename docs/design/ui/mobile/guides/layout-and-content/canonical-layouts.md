---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/canonical-layouts
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/canonical-layouts
source: md.txt
---

Utilize canonical layouts as a starting point, ready-to-use compositions that
help layouts adapt for common use cases and screen sizes. These layouts are
aesthetic and functional, and derived from [Material 3
guidance](https://m3.material.io/foundations/layout/canonical-layouts/feed).
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-22-canonical-layouts.png) **Figure 21:** Canonical layouts

The Android framework includes specialized components that make implementation
of the layouts straightforward and reliable using either [Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)
or [views](https://developer.android.com/develop/ui/views/layout/declaring-layout) APIs.

## List-detail layout

A list-detail layout enables users to explore lists of items that have
descriptive, explanatory, or other supplementary information---the item detail.
For compact screen sizes, only the list or detail view are visible. Displaying a
collection of content in a row-based layout, lists make up the most common form
of layouts for apps. List-detail is ideal for messaging apps, contact managers,
file browsers, or any app where the content can be organized as a list of items
that reveal additional information.

Content can be static or dynamic.

- **Dynamic content** is content that your app serves on-the-fly, and is ideal for showing user-generated content or reflect the user's preference or actions. For example, imagine a photo app with a scrollable list of user-generated photos, which is unique for each user and changes as the user uploads more images. These images are dynamic content.
- **Static content** represents hard-coded content, which is modifiable only by making changes directly to your app's code. Examples of static content are images and text that every user might see.

The [Now in Android](https://www.figma.com/community/file/1164313362327941158) Figma file provides multiple layout
examples. The following example shows a one-dimensional collection of content.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-23-one-dimension-collection.png) **Figure 22:** One dimensional collection of content

Explore [Material 3 Lists](https://m3.material.io/components/lists/overview) for more design guidance on list
components and specs.

## Feed layout

A feed layout arranges equivalent content elements in a configurable grid for
quick, convenient viewing of a large amount of content. Learn more on
[Material 3 guidelines for using cards in a collection](https://m3.material.io/components/cards/guidelines#580b3156-4928-45cc-953e-dec3b65a6323).
Feeds can be list- or grid- based configuration on compact displays, typically in cards or
tiles. Content can be dynamic, meaning it is "fed in" from a dynamic external
source such as an API.

<br />

A grid layout is composed of both rows and columns made up by implied or
explicit containment principles. A grid layout can be more rigidly applied or
staggered to vary the rows and columns. Both should have consistent application
of spacing and logic to avoid confusing users. Explore [Material 3 guidelines
about designing feeds](https://m3.material.io/foundations/layout/canonical-layouts/feed).

You can implement a feed layout in Compose with [Lazy lists or lazy grids](https://developer.android.com/jetpack/compose/lists#lazy),
or in Views with [`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview) or [`CardView`](https://developer.android.com/develop/ui/views/layout/cardview).

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-24-feed-layout.png)
For example, here a photo gallery and podcasts in a grid layout are common feed formats.

## Support pane layout

A mobile view may require supporting content or controls. Typically in the form
of sheets or dialogs, they can help the primary view stay focused and
uncluttered. Check out [M3 guidance for using the supporting pane canonical
layout](https://m3.material.io/foundations/layout/canonical-layouts/supporting-pane#b5f0bc74-9bb4-426b-b846-4b182cde1c76).
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-25-bottom-sheets.png) **Figure 24:** Bottom sheets can act as supporting content to the primary view

Learn about [M3 guidance for bottom sheets](https://m3.material.io/components/bottom-sheets/overview).