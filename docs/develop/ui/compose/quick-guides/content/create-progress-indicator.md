---
title: Create a progress indicator  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-progress-indicator
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a progress indicator Stay organized with collections Save and categorize content based on your preferences.



Progress indicators visually surface the status of an operation. They use motion
to bring to the user's attention how near completion the process is, such as
loading or processing data. They can also signify that processing is taking
place, without reference to how close to completion it might be.

Consider these three use cases where you might use a progress indicator:

* **Loading content**: While fetching content from a network, such as loading
  an image or data for a user profile.
* **File upload**: Give the user feedback on how long the upload might take.
* **Long processing**: While an app is processing a large amount of data,
  convey to the user how much of the total is complete.

In Material Design, there are two types of progress indicator:

* [Determinate](#determinate): Displays exactly how much progress has been made.
* [Indeterminate](#indeterminate): Animates continually without regard to progress.

Likewise, a progress indicator can take one of the two following forms:

* **Linear**: A horizontal bar that fills from left to right.
* **Circular**: A circle whose stroke grows in length until it encompasses the
  full circumference of the circle.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create determinate indicators

A determinate indicator reflects exactly how complete an action is. Use either
the [`LinearProgressIndicator`](/reference/kotlin/androidx/compose/material3/LinearProgressIndicator.composable#LinearProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp)) or [`CircularProgressIndicator`](/reference/kotlin/androidx/compose/material3/CircularProgressIndicator.composable#CircularProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp))
composables and pass a value for the `progress` parameter.

The following snippet provides a relatively detailed example. When the user
presses the button, the app both displays the progress indicator, and launches a
coroutine that gradually increases the value of `progress`. This causes the
progress indicator to iterate up in turn.

**Note:** The following example uses a coroutine to do the work of iterating the
`progress` value because it would otherwise block the UI thread.


### Results

When loading is partially complete, the linear indicator in the preceding
example appears as follows:

[

](/static/develop/ui/compose/images/components/linear-indicator-determinate.mp4)

Likewise, the circular indicator appears as follows:

[

](/static/develop/ui/compose/images/components/circular-indicator-determinate.mp4)

## Create indeterminate indicators

An indeterminate indicator does not reflect how close to completion an operation
is. Rather, it uses motion to indicate to the user that processing is ongoing,
though without specifying any degree of completion.

To create an indeterminate progress indicator, use the `LinearProgressIndicator`
or `CircularProgressIndicator` composable, but don't pass in a value for
`progress`. The following example demonstrates how you can toggle an
indeterminate indicator with a button press.

**Note:** This example also demonstrates how you can pass values for the `color` and
`trackColor` parameters to customize the appearance of the indicator.


### Results

The following is an example of this implementation when the indicator is active:

[

](/static/develop/ui/compose/images/components/circular-indicator.mp4)

The following is an example of the same implementation but with
`LinearProgressIndicator` instead of `CircularProgressIndicator`.

[

](/static/develop/ui/compose/images/components/linear-indicator.mp4)

## Key points

Although there are several composables you can use to create progress indicators
consistent with Material Design, their parameters don't differ greatly.
Among the key parameters you should keep in mind are the following:

* `progress`: The current progress that the indicator displays. Pass a `Float`
  between `0.0` and `1.0`.
* `color`: The color of the indicator, that is, the part of the
  component that reflects progress and which fully encompasses the component
  when progress is complete.
* `trackColor`: The color of the track over which the indicator is drawn.

**Note:** The APIs for `LinearProgressIndicator` and `CircularProgressIndicator` are
essentially the same and the way you use either one is identical.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a
visually pleasing form that's easy for users to consume.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)