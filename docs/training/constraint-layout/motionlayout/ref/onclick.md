---
title: <OnClick>  |  Android Developers
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/onclick
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# <OnClick> Stay organized with collections Save and categorize content based on your preferences.




Specifies the action to perform when the user taps on a view. There can be
multiple `<OnClick>` nodes for a single
[`<Transition>`](/training/constraint-layout/motionlayout/ref/transition), with
each `<OnClick>` specifying a different target view and a different action to
perform when the view is tapped.

## Syntax

```
<OnClick
    motion:targetId="@id/target_view"
    motion:clickAction="action"/>
```

## Attributes

`motion:targetId`
:   View being monitored. When the user taps this view, the transition
    occurs.

`motion:ClickAction`
:   Action to perform when the view is tapped. Supported values are the
    following:

    * `transitionToStart`
    :   Animate from the current layout to the layout specified by the
        `<Transition>` element's
        `motion::constraintSetStart` attribute.
    * `transitionToEnd`
    :   Animate from the current layout to the layout specified by the
        `<Transition>` element's
        `motion:constraintSetEnd` attribute.
    * `jumpToStart`
    :   Jump from the current layout to the layout specified by the
        `<Transition>` element's
        `motion::constraintSetStart` attribute.
    * `jumpToEnd`
    :   Jump from the current layout to the layout specified by the
        `<Transition>` element's
        `motion:constraintSetEnd` attribute.
    * `toggle`
    :   If the layout is in the starting state, animate to the end. Otherwise,
        animate to the start.