---
title: https://developer.android.com/develop/ui/compose/styles/limitations
url: https://developer.android.com/develop/ui/compose/styles/limitations
source: md.txt
---

This page describes some functional limitations of the Styles API.

## Functional limitations

- **Infinite animation support:** At this time, Styles cannot be used to define infinite animations. To implement these effects, continue using `rememberInfiniteTransition` within Compose.
- **Property scoping:** There is no support for custom properties that extend beyond standard style attributes.
- **Shapes:** Custom shapes are not supported; this will be fixed in future versions. Shape animations are also not supported yet.
- **Interop with View system themes and styles:** There is no support for pulling a style from your existing `themes.xml` or `styles.xml`. Styles will never support this directly.
- **Interop with Ripple/Indication:** Using `pressed` without setting `indication = null` on `clickable` modifier will result in both being shown at once.

## Material integration status

We plan to add styles support to Material components in a future update.

Submit a [bug report](https://issuetracker.google.com/issues/new?component=612128) if you encounter an unsupported use case.