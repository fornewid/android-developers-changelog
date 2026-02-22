---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/dialogs
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/dialogs
source: md.txt
---

# Dialogs

Use a[`Dialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/dialog/package-summary)to focus users' attention on a timely action or piece of information.

![](https://developer.android.com/static/wear/images/components/dialog-hero.png)

## Anatomy

![](https://developer.android.com/static/wear/images/components/dialog.png)  
Dialogs should appear in response to a user task or an action, with relevant or contextual information. Unlike their mobile counterparts, Dialogs in Wear OS occupy the whole screen and are layered over other content.

Dialogs support a swipe-to-dismiss gesture. When the user performs this swipe gesture, the system reveals the parent content in the background.

Dialogs have a single slot for opinionated dialog content, such as an[Alert](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/dialog/package-summary#Alert(kotlin.Function1,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function1,androidx.wear.compose.material.ScalingLazyListState,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1))or[Confirmation](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/dialog/package-summary#Confirmation(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function1,androidx.wear.compose.material.ScalingLazyListState,kotlin.Long,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)).

<br />

![](https://developer.android.com/static/wear/images/components/alert-anatomy.png)  
**Alert**

Use an alert component to get the user's response for important tasks.

Alerts disable all app functionality when they appear, and remain on screen until an action has been taken. Alerts are purposefully interruptive, so use them sparingly.

If the content of the alert is longer than three lines of text, consider left aligning the content to improve its readability. Otherwise the text is center aligned by default.

**A. Title
B. Content (optional)
C. Negative button
D. Positive button
E. Icon (optional)**

<br />

![](https://developer.android.com/static/wear/images/components/confirmation-anatomy.png)  
**Confirmation**

The confirmation component displays a confirmation message to the user for a short period of time. Unlike its Material counterpart, the confirmation component in Wear OS doesn't allow users to provide final confirmation of a choice.

Use this component to capture a user's attention after an action has been executed.

**A. Icon
B. Label**