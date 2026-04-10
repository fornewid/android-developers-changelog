---
title: https://developer.android.com/guide/navigation/backstack/dialog
url: https://developer.android.com/guide/navigation/backstack/dialog
source: md.txt
---

# Dialog destinations

This document outlines how the use of[dialog destinations](https://developer.android.com/guide/navigation/design)can introduce unique considerations for how you need to manage your back stack.

## Overview

One or more dialog destinations can only exist on the top of the back stack. This is because when the user navigates to a destination that is not a dialog destination, the`NavController`automatically pops all dialog destinations off the top of the stack. This ensures that the current destination is always fully visible over other destinations on the back stack.

Destinations can be either[hosted destinations](https://developer.android.com/guide/navigation/design),[activity destinations](https://developer.android.com/guide/navigation/design/activity-destinations), or[dialog destination](https://developer.android.com/guide/navigation/design/dialog-destinations).
| **Note:** Dialog destinations implement the[`FloatingWindow`](https://developer.android.com/reference/androidx/navigation/FloatingWindow)interface. As such, they overlay other destinations on the back stack.

## Example

If the back stack consists solely of[hosted destinations](https://developer.android.com/guide/navigation/design)that fill the navigation host, and the user navigates to a dialog destination, then the back stack might look similar to figure 2:
![a back stack with a dialog destination on top](https://developer.android.com/static/images/guide/navigation/backstack-1.png)**Figure 2.**A back stack with a dialog destination on top.

If the user then navigates to another dialog destination, it is then added to the top of the back stack, as shown in figure 3:
![a back stack with two dialog destinations on top](https://developer.android.com/static/images/guide/navigation/backstack-2.png)**Figure 3.** A back stack with two`Dialog`destinations on top.

If the user then navigates to a non-floating destination, any dialog destinations are first popped from the top of the back stack before navigating to the new destination, as shown in figure 4:
![the dialog destinations are popped, and the new destination is added](https://developer.android.com/static/images/guide/navigation/backstack-3.png)**Figure 4.** The`Dialog`destinations are popped, and the new destination is added.