---
title: https://developer.android.com/develop/ui/compose/styles/styles-update
url: https://developer.android.com/develop/ui/compose/styles/styles-update
source: md.txt
---

At Google I/O, we previewed Styles as a new way to customize components.
Following your feedback, we're evolving the API to make the core Styles APIs
less opinionated. Instead of the foundation layer defining visual properties,
property definitions are moving to the design system layer (e.g. Material or
your own design system)---giving design systems more control over what styleable
properties their components support or how to create custom styleable properties (`stylePropertyOf` / `styleLocalOf`). While this change is underway, we've
temporarily removed the initial documentation and skill that we've published,
and the Styles API will remain `@Experimental` in Compose 1.13. We'll share more
when the new API shape is ready for re-evaluation and would love your feedback
on this new direction.