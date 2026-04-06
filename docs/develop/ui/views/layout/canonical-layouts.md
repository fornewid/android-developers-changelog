---
title: https://developer.android.com/develop/ui/views/layout/canonical-layouts
url: https://developer.android.com/develop/ui/views/layout/canonical-layouts
source: md.txt
---

Canonical layouts are proven, versatile layouts that provide an optimal user
experience on a variety of form factors.

![Depiction of large screen devices showing the canonical layouts.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/canonical-layouts/canonical_layouts_header.png)

The canonical layouts support small screen phones as well as tablets, foldables,
and ChromeOS devices. Derived from [Material Design guidance](https://m3.material.io/foundations/layout/canonical-layouts/overview), the layouts are
aesthetic as well as functional.

The Android framework includes specialized components that make implementation
of the layouts straightforward and reliable.

The canonical layouts create engaging, productivity‑enhancing UIs that
form the foundation of great apps.

If you're already familiar with the adaptive app canonical layouts but aren't
sure which Android APIs to use, jump to the [Applicability](https://developer.android.com/develop/ui/views/layout/canonical-layouts#applicability)
section for help determining which layout is right for your app's use cases.

## List-detail

![Wireframe of list-detail layout.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/canonical-layouts/list-detail_wireframe.png)

The list-detail layout enables users to explore lists of items that have
descriptive, explanatory, or other supplementary information---the item
detail.

The layout divides the app window into two side-by-side panes: one for the list,
one for the detail. Users select items from the list to display the item detail.
Deep links in the detail reveal additional content in the detail pane.

Expanded-width displays (see [Use window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes)) accommodate both the
list and detail at the same time. Selection of a list item updates the detail
pane to show the related content for the selected item.

Medium- and compact-width displays show either the list or the detail, depending
on user interaction with the app. When just the list is visible, selection of a
list item displays the detail in place of the list. When just the detail is
visible, pressing the back button redisplays the list.

Configuration changes such as device orientation changes or app window size
changes can change the display's window size class. A list‑detail layout
responds accordingly, preserving app state:

- If an expanded-width display showing both the list and detail panes narrows to medium or compact, the detail pane remains visible and the list pane is hidden
- If a medium- or compact-width display has just the detail pane visible and the window size class widens to expanded, the list and detail are shown together, and the list indicates that the item corresponding to the content in the detail pane is selected
- If a medium- or compact-width display has just the list pane visible and widens to expanded, the list and a placeholder detail pane are shown together

List-detail is ideal for [messaging apps](https://developer.android.com/large-screens/gallery/social#media), [contact managers](https://developer.android.com/large-screens/gallery/productivity#items-and-overviews), [interactive
media browsers](https://developer.android.com/large-screens/gallery/media#easy-exploration) or any app where the content can be organized as a list of
items that reveal additional information.
Your browser doesn't support the video tag. **Figure 1.** Messaging app showing a list of conversations and the details of a selected conversation.

### Implementation

A list-detail layout can be created with a variety of technologies, including
Compose, views, and activity embedding (for legacy apps). See the
[Applicability](https://developer.android.com/develop/ui/views/layout/canonical-layouts#applicability) section for help deciding which technology is
most suitable for your app.

The [`SlidingPaneLayout`](https://developer.android.com/reference/androidx/slidingpanelayout/widget/SlidingPaneLayout) library is designed for implementation of
list‑detail layouts based on views or fragments.

First, declare a `SlidingPaneLayout` as the root element of your XML layout.
Next, add the two child elements---either views or fragments---that
represent the list and detail content.

Implement a communication methodology to pass data between the list-detail views
or fragments. [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) is recommended because of its ability to store
business logic and survive configuration changes.

`SlidingPaneLayout` automatically determines whether to display the list and
detail together or individually. In a window that has enough horizontal space to
accommodate both, the list and detail appear side by side. In a window that
lacks sufficient space, either the list or detail is displayed depending on the
user's interaction with the app.

For an example implementation, see the [List-detail with sliding pane](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts/list-detail-sliding-pane)
sample.

#### Activity embedding

Use activity embedding to enable legacy, multiple-activity apps to display two
activities side by side on the same screen or stacked (one overlaying the
other). If your app implements the list and detail of a list‑detail layout
in separate activities, activity embedding enables you to create a
list‑detail layout with minimal or no code refactoring.

Implement activity embedding by specifying a task window split using an XML
configuration file. The split defines the primary activity, which initiates the
split, and a secondary activity. Specify a minimum display width for the split
using the window size class breakpoints. When the display width falls below the
minimum breakpoint, the activities are displayed one overlaying the other. For
example, if the minimum display width is 600dp, the activities are displayed one
overlaying the other on compact displays, but side by side on medium and
expanded displays.

Activity embedding is supported on Android 12L (API level 32) and higher, but
may also be available on lower API levels if implemented by device
manufacturers. When activity embedding is not available on a device, the
fallback behavior results in the list activity or the detail activity occupying
the entire app window based on user interaction with the app.

For more information, see [Activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding).

For an example implementation, see the [List-detail with activity
embedding](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts/list-detail-activity-embedding) sample.

## Feed

![Wireframe of feed layout.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/canonical-layouts/feed_wireframe.png)

A feed layout arranges equivalent content elements in a configurable grid for
quick, convenient viewing of a large amount of content.

Size and position establish relationships among the content elements.

Content groups are created by making elements the same size and positioning them
together. Attention is drawn to elements by making them larger than nearby
elements.

Cards and lists are common components of feed layouts.

A feed layout supports displays of almost any size because the grid can adapt
from a single, scrolling column to a multi‑column scrolling feed of
content.

Feeds are especially well suited for [news and social media apps](https://developer.android.com/large-screens/gallery/social#posts).
Your browser doesn't support the video tag. **Figure 2.** Social media app showing posts in cards of varying sizes.

### Implementation

A [`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView) efficiently renders a large number of items in a single
column. A [`GridLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/GridLayoutManager) lays out items in a grid, allowing
configuration of the item sizes and spans.

Configure the grid columns based on the size of the available display area to
set the minimum allowable width for items.

The `GridLayoutManager` default spanning strategy, which is one span per item,
can be overridden by creating a custom [`SpanSizeLookup`](https://developer.android.com/reference/androidx/recyclerview/widget/GridLayoutManager.SpanSizeLookup). Adjust the span to
emphasize some items over others.

On compact-width displays that have enough space for only one column, use
[`LinearLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager) instead of `GridLayoutManager`.

For an example implementation, see the [Feed with views](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts/feed-view)
sample.

<br />

## Supporting pane

![Wireframe of supporting pane layout.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/canonical-layouts/supporting_pane_wireframe.png)

Supporting pane layout organizes app content into primary and secondary display
areas.

The primary display area occupies the majority of the app window (typically
about two thirds) and contains the main content. The secondary display area is a
pane that takes up the remainder of the app window and presents content that
supports the main content.

Supporting pane layouts work well on expanded-width displays (see [Use window
size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes)) in landscape orientation. Medium- or compact‑width
displays support showing both the primary and secondary display areas if the
content is adaptable to narrower display spaces, or if the additional content
can be initially hidden in a bottom or side sheet accessible by means of a
control such as a menu or button.

A supporting pane layout differs from a list‑detail layout in the
relationship of the primary and secondary content. Secondary pane content is
meaningful only in relation to the primary content; for example, a supporting
pane tool window is irrelevant by itself. The supplementary content in the
detail pane of a list‑detail layout, however, is meaningful even without
the primary content, for example, the description of a product from a product
listing.

Use cases for supporting pane include:

- **Productivity apps:** A [document or spreadsheet accompanied by reviewer
  comments](https://developer.android.com/large-screens/gallery/productivity#reviews-and-comments) in a supporting pane
- **Media apps:** A [streaming video complemented by a list of related videos](https://developer.android.com/large-screens/gallery/media#media-exploration) in a supporting pane, or the depiction of an album of music supplemented with a playlist
- **Tools and settings:** A [media editing tool](https://developer.android.com/large-screens/gallery/social#tools) with palettes, effects, and other settings in a support pane

Your browser doesn't support the video tag. **Figure 3.** Shopping app with product descriptions in a supporting pane.

### Implementation

A supporting pane layout is implemented using a helper layout such as
[`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout) or [`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout). Establish the window size classes
that divide the amount of horizontal display space available for your app into
three categories: compact (\< 600dp), medium (\>= 600dp), and expanded
(\>= 840dp).

For each window size class, define layouts as follows:

- **Compact:** In the app resources `layout` folder, place content that renders the supporting pane below the main content or inside a bottom sheet
- **Medium:** In the `layout-w600dp` folder, provide supporting pane content that results in the main content and supporting pane rendering side by side, splitting the horizontal display space equally
- **Expanded:** In the `layout-w840dp` folder, include supporting pane content that results in the main content and supporting pane rendering side by side; however, the supporting pane takes up only 30% of the horizontal space, leaving the remaining 70% for the main content

Use a [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) for communication between the main content and the
supporting pane whether using views, fragments, or a combination.

For implementation examples, see the following samples:

- [Supporting pane with views](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts/supporting-pane-views)
- [Supporting pane with fragments](https://github.com/android/user-interface-samples/tree/main/CanonicalLayouts/supporting-pane-fragments)

## Applicability

The canonical layouts create multifaceted presentations of content for easy access and deep exploration. Use the following flowchart to determine which layout and implementation strategy is best for your app's use cases.

For examples of the canonical layouts implemented in different types of apps, see the [large screen gallery](https://developer.android.com/large-screens/gallery).
![](https://developer.android.com/static/images/develop/ui/views/canonical_layouts_flowchart.png) **Figure 4.** Large screen canonical layout decision tree.

## Additional resources

- Material Design --- [Canonical layouts](https://m3.material.io/foundations/layout/canonical-layouts/overview)