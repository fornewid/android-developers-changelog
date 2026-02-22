---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/onclick
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/onclick
source: md.txt
---

# &lt;OnClick&gt;

Specifies the action to perform when the user taps on a view. There can be multiple`<OnClick>`nodes for a single[`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition), with each`<OnClick>`specifying a different target view and a different action to perform when the view is tapped.

## Syntax

```xml
<OnClick
    motion:targetId="@id/target_view"
    motion:clickAction="action"/>
```

## Attributes

`motion:targetId`
:   View being monitored. When the user taps this view, the transition occurs.

`motion:ClickAction`
:   Action to perform when the view is tapped. Supported values are the following: