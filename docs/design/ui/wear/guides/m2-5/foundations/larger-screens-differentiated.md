---
title: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/larger-screens-differentiated
url: https://developer.android.com/design/ui/wear/guides/m2-5/foundations/larger-screens-differentiated
source: md.txt
---

# Adaptive and differentiated

![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-header.png)

Apps that are**adaptive and differentiated**create a user experience that isn't possible on devices with smaller screens.

These apps use new layouts, implemented at a key screen size breakpoint, to derive additional value for users of devices with larger screens, enabling a user experience that devices with smaller screens can't match.

## Add value by applying new layouts and templates

Adaptive layout differentiated apps follow[adaptive design practices](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-layouts)but also utilize breakpoints to apply different layouts and create an even richer experience for users of devices with substantially larger screens, as shown in the following examples:
![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-sizes-1.png)Add new glanceable information.![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-sizes-2.png)Add more tappable affordances.![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-sizes-3.png)Increase the information density of graphs and charts.![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-sizes-4.png)Adjust component behavior or design with the use of breakpoints to fill the available space.

## Use breakpoints on Wear OS

Utilizing a breakpoint at 225 dp can help optimize layouts across a range of sizes.

See the[Compose](https://developer.android.com/training/wearables/compose/screen-size#breakpoints)and[Tiles](https://developer.android.com/training/wearables/tiles/screen-size#breakpoints)implementation guidance for differentiated layouts.  
![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-do.png)  
check_circle

### Do

- Think big.
- Design custom layouts and behaviors at 225 dp and larger.  
![](https://developer.android.com/static/wear/images/design/larger-screens-differentiated-dont.png)  
cancel

### Don't

- Settle for less.
- Design for just one device size.
- Let your app be unremarkable.