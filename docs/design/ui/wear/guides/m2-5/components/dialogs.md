---
title: Dialogs  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/dialogs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Dialogs Stay organized with collections Save and categorize content based on your preferences.



Use a [`Dialog`](/reference/kotlin/androidx/wear/compose/material/dialog/package-summary) to focus users' attention on a timely action or piece of
information.

![](/static/wear/images/components/dialog-hero.png)

## Anatomy

![](/static/wear/images/components/dialog.png)

Dialogs should appear in response to a user task or an action, with
relevant or contextual information. Unlike their mobile counterparts,
Dialogs in Wear OS occupy the whole screen and are layered over other
content.

Dialogs support a swipe-to-dismiss gesture. When the user performs
this swipe gesture, the system reveals the parent content in the
background.

Dialogs have a single slot for opinionated dialog content, such as an
[Alert](/reference/kotlin/androidx/wear/compose/material/dialog/package-summary#Alert(kotlin.Function1,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function1,androidx.wear.compose.material.ScalingLazyListState,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)) or
[Confirmation](/reference/kotlin/androidx/wear/compose/material/dialog/package-summary#Confirmation(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function1,androidx.wear.compose.material.ScalingLazyListState,kotlin.Long,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)).

![](/static/wear/images/components/alert-anatomy.png)

**Alert**

Use an alert component to get the user's response for important
tasks.

Alerts disable all app functionality when they appear, and remain on
screen until an action has been taken. Alerts are purposefully interruptive,
so use them sparingly.

If the content of the alert is longer than three lines of text, consider
left aligning the content to improve its readability. Otherwise the text
is center aligned by default.

**A. Title  
B. Content (optional)**

![](/static/wear/images/components/confirmation-anatomy.png)

**Confirmation**

The confirmation component displays a confirmation message to the user
for a short period of time. Unlike its Material counterpart, the
confirmation component in Wear OS doesn’t allow users to provide final
confirmation of a choice.

Use this component to capture a user’s attention after an action has been
executed.

**A. Icon  
B. Label**