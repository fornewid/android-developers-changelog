---
title: Tabs  |  TV  |  Android Developers
url: https://developer.android.com/design/ui/tv/guides/components/tabs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [TV](https://developer.android.com/design/ui/tv)
* [Guides](https://developer.android.com/design/ui/tv/guides/foundations/design-for-tv)

# Tabs Stay organized with collections Save and categorize content based on your preferences.




Tabs organize content across different screens, data sets, and
interactions. Tabs can be used to switch between views of distinct and
related groups of information.

![Tabs cover](/static/design/ui/tv/guides/components/images/covers/cover-tabs.webp)

## Resources

| Type | Link | Status |
| --- | --- | --- |
| Design | [Design source (Figma)](https://goo.gle/tv-desing-kit) | Available |
| Implementation | [Jetpack Compose](/reference/kotlin/androidx/tv/material3/TabRow.composable#TabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function2,kotlin.Function1)) | Available |

## Highlights

* Tabs can scroll horizontally. A UI can have as many tabs as needed.
* Tabs organize content into categories to help users find
  different types of information quickly.
* Tabs are displayed next to each other as peers, in categories
  of equal importance.

## Variants

There are two types of tab indicators:

![Tabs Pill](/static/design/ui/tv/guides/components/images/tabs/tabs-pill.webp)
![Tabs Underline](/static/design/ui/tv/guides/components/images/tabs/tabs-underline.webp)

1. Pill indicator
2. Bar indicator

Choose the right type according to emphasis. Pill indicator tabs are
recommended for organizing full pages. They display the main content
destinations. Bar indicator tabs are used within a content area to further
separate related content and establish hierarchy.

## Anatomy

![Tabs anatomy](/static/design/ui/tv/guides/components/images/tabs/tabs-anatomy.webp)

1. Icon (optional)
2. Label
3. Active indicator
   1. Pill
   2. Bar
4. Container

## States

![Tabs states](/static/design/ui/tv/guides/components/images/tabs/tabs-states.webp)

1. Default
2. Focused
3. Selected

## Specs

![Tabs anatomy](/static/design/ui/tv/guides/components/images/tabs/tabs-specs.webp)

## Behavior

When moving from one tab to the next the content below also slides left or
right based on the tab movement.

[
](/static/design/ui/tv/guides/components/images/tabs/tab-page-transition.mp4)

[Previous

arrow\_back

Lists](/design/ui/tv/guides/components/lists)