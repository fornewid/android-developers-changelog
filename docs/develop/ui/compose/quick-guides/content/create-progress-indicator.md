---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-progress-indicator
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-progress-indicator
source: md.txt
---

<br />

Progress indicators visually surface the status of an operation. They use motion
to bring to the user's attention how near completion the process is, such as
loading or processing data. They can also signify that processing is taking
place, without reference to how close to completion it might be.

Consider these three use cases where you might use a progress indicator:

- **Loading content**: While fetching content from a network, such as loading an image or data for a user profile.
- **File upload**: Give the user feedback on how long the upload might take.
- **Long processing**: While an app is processing a large amount of data, convey to the user how much of the total is complete.

In Material Design, there are two types of progress indicator:

- [Determinate](https://developer.android.com/develop/ui/compose/quick-guides/content/create-progress-indicator#determinate): Displays exactly how much progress has been made.
- [Indeterminate](https://developer.android.com/develop/ui/compose/quick-guides/content/create-progress-indicator#indeterminate): Animates continually without regard to progress.

Likewise, a progress indicator can take one of the two following forms:

- **Linear**: A horizontal bar that fills from left to right.
- **Circular**: A circle whose stroke grows in length until it encompasses the full circumference of the circle.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-progress-indicator_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create determinate indicators

A determinate indicator reflects exactly how complete an action is. Use either
the [`LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LinearProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp)) or [`CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CircularProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.unit.Dp))
composables and pass a value for the `progress` parameter.

The following snippet provides a relatively detailed example. When the user
presses the button, the app both displays the progress indicator, and launches a
coroutine that gradually increases the value of `progress`. This causes the
progress indicator to iterate up in turn.

> [!NOTE]
> **Note:** The following example uses a coroutine to do the work of iterating the `progress` value because it would otherwise block the UI thread.

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-progress-indicator_51f7a1cc4e08a4e657ed561878d0d7379da8f5e81e6144deab76133d3a300d16.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

When loading is partially complete, the linear indicator in the preceding
example appears as follows:

Likewise, the circular indicator appears as follows:

## Create indeterminate indicators

An indeterminate indicator does not reflect how close to completion an operation
is. Rather, it uses motion to indicate to the user that processing is ongoing,
though without specifying any degree of completion.

To create an indeterminate progress indicator, use the `LinearProgressIndicator`
or `CircularProgressIndicator` composable, but don't pass in a value for
`progress`. The following example demonstrates how you can toggle an
indeterminate indicator with a button press.

> [!NOTE]
> **Note:** This example also demonstrates how you can pass values for the `color` and `trackColor` parameters to customize the appearance of the indicator.

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-progress-indicator_bf46d1d24370ccadeea8873a4ed106e0cdbc9aaf4b199fcf53ed772b164c6a4d.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

The following is an example of this implementation when the indicator is active:

The following is an example of the same implementation but with
`LinearProgressIndicator` instead of `CircularProgressIndicator`.

## Key points

Although there are several composables you can use to create progress indicators
consistent with Material Design, their parameters don't differ greatly.
Among the key parameters you should keep in mind are the following:

- `progress`: The current progress that the indicator displays. Pass a `Float` between `0.0` and `1.0`.
- `color`: The color of the indicator, that is, the part of the component that reflects progress and which fully encompasses the component when progress is complete.
- `trackColor`: The color of the track over which the indicator is drawn.

> [!NOTE]
> **Note:** The APIs for `LinearProgressIndicator` and `CircularProgressIndicator` are essentially the same and the way you use either one is identical.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)