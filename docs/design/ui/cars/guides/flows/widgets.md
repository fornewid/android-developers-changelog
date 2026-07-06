---
title: https://developer.android.com/design/ui/cars/guides/flows/widgets
url: https://developer.android.com/design/ui/cars/guides/flows/widgets
source: md.txt
---

Widgets are coming to cars, beginning with Android Auto and followed by cars
with Google built-in. Optimize your existing widget to work well on cars, making
them safe, glanceable, and functional for drivers.

Start preparing your widgets to ensure your widgets provide a high-quality
experience on vehicle screens.

## Prepare your widgets

High-quality mobile widgets typically translate well to the car environment.
Follow these principles to make a high-quality widget:

- Build your widgets with [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance).
- Make your widgets [responsive](https://developer.android.com/develop/ui/compose/glance/build-ui#sizemode.exact), because car displays come in various sizes and grid configurations. Test your widgets across different layouts to ensure that your widget adjusts correctly.
- Include both light and dark themes in your widget to ensure it is clearly visible during the day and the night.
- Implement [dynamic theming](https://developer.android.com/design/ui/mobile/guides/styles/themes) so your widget feels like an integrated part of the vehicle's system.
- Ensure your widget completely fills the grid bounds (WL-1 widget quality guideline).

## Build for glanceability

Widgets on cars work best when they are glanceable. Take the following actions
to ensure your widgets are glanceable:

- Design your widget to be glanceable, because widgets on cars don't support manual [scrolling](https://developer.android.com/develop/ui/compose/glance/build-ui#use-scrollable).
- If your widget uses a scrollable [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable) offer an alternative version of your widget that delivers all necessary information on one surface. Otherwise, the car platform displays only the first few items in that list.
- If you use the scrollable segmented list designed for auto, designate the first page for your most valuable and personalized content by placing it in the first position of any scrollable collection. This ensures that it is visible to the driver.

## See also

- [Widget quality guidelines](https://developer.android.com/docs/quality-guidelines/widget-quality)
- [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance)