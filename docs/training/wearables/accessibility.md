---
title: https://developer.android.com/training/wearables/accessibility
url: https://developer.android.com/training/wearables/accessibility
source: md.txt
---

As you create an app on Wear OS, start by following accessibility principles and
guidance from our [Accessibility guide for Android apps](https://developer.android.com/guide/topics/ui/accessibility). Then ensure you app
is accessible on Wear OS as well.

Wear OS apps have some additional considerations when it comes to accessibility
due to the following factors:

- Different input types on Wear OS, such as rotary input.
- Additional UI surfaces such as tiles and complications.
- Small screen sizes, which require different [TalkBack](https://support.google.com/accessibility/android/answer/6283677) implementations.

As with other accessibility work, make sure to thoroughly test each experience
with assistive technologies such as a screen reader. This lets you experience
your app from the perspective of your users and discover usability issues that
you otherwise might miss. For more information, see [Test your app's
accessibility](https://developer.android.com/guide/topics/ui/accessibility/testing).

## Support the user's preferred font size

In system settings, users can adjust the font size for text elements that appear
in Wear OS apps. For example, on Google Pixel Watch devices, these settings are
[located in the **Settings \> Accessibility** menu](https://support.google.com/googlepixelwatch/answer/12658379).

When testing your app, set the font size to different values, and make sure that
your app's text content behaves as you expect. You can use techniques such as
the following to make your app's text more accessible:

- If you use [autosizing text](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/TextAutoSize), set explicit values for [`minFontSize`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/TextAutoSize#StepBased(androidx.compose.ui.unit.TextUnit,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.unit.TextUnit)) and [`maxFontSize`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/TextAutoSize#StepBased(androidx.compose.ui.unit.TextUnit,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.unit.TextUnit)).
- Use an ellipsis to show that text overflows its container. The Material text element [uses an overflow ellipsis by default](https://developer.android.com/reference/androidx/wear/protolayout/material/Text.Builder#setOverflow(int)).

## Enable rotary input

Most Wear OS devices contain a physical rotating side button (RSB), rotating
bezel or touch bezel. This is called a rotary input. You can use the rotary
input to adjust the volume of media apps, scroll content up or down, and more.

Wear OS devices are smaller than mobile devices, which presents additional
challenges. Users with dexterity challenges may find accuracy on a small screen
difficult. Screen reader users may also find it difficult to use two-finger
interactions for scrolling. Using rotary input assists users with these
challenges by providing a more convenient way to scroll rather than using the
two-finger interaction.

For more information, see [Rotary input](https://developer.android.com/training/wearables/user-input/rotary-input).

## Optimize your app for Talkback

TalkBack is Android's built-in screen reader. When TalkBack is on, users can
interact with their Android-powered device without seeing the screen. Test your
app to ensure that all user journeys can be navigated using screen readers such
as TalkBack. For more information, see [TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback).

TalkBack on Wear OS is similar to TalkBack on mobile with a few additional
considerations, detailed in the following sections.

### Use built-in components

Wear OS provides many built-in UI components that already follow accessibility
best practices. For example, the [`PickerGroup`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#PickerGroup(kotlin.Array,androidx.compose.ui.Modifier,androidx.wear.compose.material.PickerGroupState,kotlin.Function1,kotlin.Boolean,kotlin.Boolean,androidx.wear.compose.material.TouchExplorationStateProvider,kotlin.Function1)) element uses a focus
coordinator object to assign focus to the correct `Picker` element.

Use these built-in components in your app to improve its
usability for everyone.

### Use content descriptions for tiles and complications

Wear OS provides different UI surfaces, such as tiles and complications.

[Watch face complications](https://developer.android.com/training/wearables/watch-faces/complications) display highly glanceable information from apps
directly on the watch face, such as the date or weather forecasts. [Tiles](https://developer.android.com/training/articles/wear-tiles)
provide quick access to the information and actions needed to get things done.
With a swipe from the watch face, a user can check the weather, set a
timer, and more.

Similarly to [Compose](https://developer.android.com/jetpack/compose/accessibility#describe-visual) visual elements, you can set a `contentDescription`
for tiles and complications. `contentDescriptions` define the text that Talkback
uses to describe any content that does not have a textual representation.
When using content descriptions for tiles and complications, keep in mind the
following:

- Avoid adding extra words to the description that don't provide user value, such as complication and tile.
- Avoid adding words beyond the information that is displayed. For example the description of a complication is displaying the date **December 13th** should be **December 13th** without words like **Day** and **Date**.

#### Set the content descriptions for Tiles

Use the [`contentDescription`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/LayoutModifier#(androidx.wear.protolayout.modifiers.LayoutModifier).contentDescription(kotlin.String,androidx.wear.protolayout.expression.DynamicBuilders.DynamicString)) modifier to set the current content
description for the Tile that Talkback verbalizes.

Also make sure to set the content description for any elements within the tiles,
like [Buttons](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).button(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,kotlin.Function1,androidx.wear.protolayout.material3.ButtonStyle,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)).

#### Set the content descriptions for complications

There are different [types](https://developer.android.com/training/wearables/watch-faces/adding-complications#types-fields) of complications such as
`SmallImageComplication` and `ShortTextComplication. contentDescription` is set
on the Builder, for example see the [`SmallImageComplicationData.Builder`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/SmallImageComplicationData.Builder#Builder(androidx.wear.watchface.complications.data.SmallImage,androidx.wear.watchface.complications.data.ComplicationText)).

### Understand list behaviors

Due to the small screen size on wearable devices, TalkBack makes several
assumptions about list behavior on Wear OS.

#### List Announcements

In other form factors, when a user is focused on a list, Talkback adds **in
list** to its announcements so that a user understands where they are. If they
navigate out of the list, Talkback adds **out of list** to its
announcements. But on Wear OS, TalkBack assumes that there is only one list
possible per UI due to the small screen size. So, it has removed support for
in-list and out-of-list announcements to avoid redundant wording. Don't expect
in-list and out-of-list announcements to be read out on Wear OS.

#### Vertical list announcing

When reading items from a vertical list, Talkback avoids reading out items that
are too small or are almost off of the screen. Specifically, TalkBack uses the
following two conditions:

1. Elements near the top or the bottom of the screen.
2. Elements less than 32dp in height.

Work effectively with Talkback by ensuring that items are at least 32dp in
height, the first item in the list has padding from the top, and the last item
has padding from the bottom.

These guidelines don't apply to horizontal lists.

## Set minimum touch targets

Touch targets are the parts of the screen that respond to user input. They can
extend beyond the visual bounds of an element. For example, an element such as
an icon may appear to be 24dp x 24dp, but the padding surrounding it can
make up the full 48 x 48 dp touch target.

The [recommended touch target size](https://support.google.com/accessibility/android/answer/7101858) for interactive elements on Android
devices is 48dp x 48dp. Due to the small screen size on Wear OS, there
are some situations where 40dp x 40dp is allowed.

For more information about how to implement touch targets, see [Accessibility in
Compose](https://developer.android.com/jetpack/compose/accessibility#minimum-target-sizes).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Picker](https://developer.android.com/design/ui/wear/guides/components/pickers)
- [Loading images {:#loading-images}](https://developer.android.com/develop/ui/compose/graphics/images/loading)
- [Key steps to improve Compose accessibility](https://developer.android.com/develop/ui/compose/accessibility/key-steps)