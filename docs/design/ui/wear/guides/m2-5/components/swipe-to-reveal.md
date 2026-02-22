---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/swipe-to-reveal
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/swipe-to-reveal
source: md.txt
---

# Swipe to reveal

Allow users to swipe a component to reveal extra actions.

![](https://developer.android.com/static/wear/images/components/swipe-to-reveal-hero.svg)  
The*swipe to reveal*component lets you add extra actions to chips and cards, specifically when they appear in lists. This component lets users quickly get things done without leaving the screen.

Users can partially swipe chips and cards to the left to access these actions, then tap on an action to complete it. Users can also fully swipe chips and cards to the left to quickly commit to the primary action.  
The component has 2 slots for these actions:

1. **Primary**
2. **Secondary (optional)**

## Anatomy

![](https://developer.android.com/static/wear/images/components/swipe-to-reveal-actions.svg)  

### Revealed actions

Developers can customize the actions for their unique use cases. Consider the color and iconography used in these actions to help users understand what they mean.

The revealed actions appear on the same side for all language locales.

1. **Primary action**
2. **Secondary action (optional)**  

### Commit to a primary action

To commit to the primary action, a user can either tap on the button or continue swiping to the left. In this way, the button extends to the entire width of the screen and displays a label. The action fades away after being selected.

The first example shows a**single button option** . The second example shows a**double button option**.  

### Undo action

For destructive actions, add an undo component to let users reverse these actions. Add the undo capability to the primary action.

If added, an undo chip button appears in place of the committed action. After a short period of time, the undo action fades away, and the system completes the committed action.  

### Swipe thresholds

The swipe to reveal component's behavior depends upon how far the user swipes across the screen:

- If the user swipes across less than 50% of the screen, the component snaps back to its starting position, and no action is taken.
- If the user swipes across the screen between 50% and 75% of the full width, the component remains partially visible, and the actions associated with the component appear.
- If the user swipes across more than 75% of the screen, the component disappears, and the system automatically performs the primary action.

<br />

<br />

## Related components

The following material-themed components implement the swipe to reveal behavior:

- [`SwipeToRevealCard`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#SwipeToRevealCard(androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.foundation.RevealState,androidx.compose.ui.Modifier,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealActionColors,androidx.compose.ui.graphics.Shape,kotlin.Function0))
- [`SwipeToRevealChip`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#SwipeToRevealChip(androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.foundation.RevealState,androidx.compose.ui.Modifier,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealAction,androidx.wear.compose.material.SwipeToRevealActionColors,androidx.compose.ui.graphics.Shape,kotlin.Function0))

### On cards

The following screenshots show the swipe to reveal component's appearance when using the`SwipeToRevealCard`class:

![](https://developer.android.com/static/wear/images/components/swipe-to-reveal-examples-cards.svg)

### On chips

The following screenshots show the swipe to reveal component's appearance when using the`SwipeToRevealChip`class:

![](https://developer.android.com/static/wear/images/components/swipe-to-reveal-examples-chips.svg)