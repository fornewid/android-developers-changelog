---
title: https://developer.android.com/training/wearables/views/navigation
url: https://developer.android.com/training/wearables/views/navigation
source: md.txt
---

# Navigation

Try the Compose way  
Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.  
[Handle navigation using Compose on Wear OS →](https://developer.android.com/training/wearables/compose/navigation)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

After designing individual screens for each user journey, you might have a few vertical or single screens. Next, you have to decide how to design these screens to work together and how to implement the navigation.

## Design

Keep your app's hierarchy shallow and linear, as called out in the[app design guidelines](https://developer.android.com/training/wearables/design/apps).

To start, your app's launcher should open the most common user journey. Design each user journey with the most important content at the top. For vertical containers, use the bottom to link to other, less-common user journeys and the settings.
![](https://developer.android.com/static/wear/images/screen_opts_2.png)

**Figure 1.**Keep the most important content at the top of vertical containers.

When users enter one of your screens, make sure they can use the swipe-to-dismiss gesture to navigate down the[back stack](https://developer.android.com/guide/components/tasks-and-back-stack).

## Implement the navigation

When you implement your navigation, you have three options, described in the following sections:

- Activities only, which is the recommended approach
- Activities and fragments
- Jetpack Navigation

### Activities only

Since vertical screens are typically one level deep, you can implement all your screens using activities and without using fragments.

We strongly recommend this approach. It simplifies your code, and activities automatically support[swipe-to-dismiss](https://developer.android.com/training/wearables/apps/exit#swipe-to-dismiss). This also makes implementing[ambient mode](https://developer.android.com/training/wearables/apps/always-on)simpler.

**Note:** Make your activities inherit from a[`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity)if you are not using fragments. The other activity types use mobile-specific UI elements you don't need for Wear OS.

### Activities and fragments

You can use[fragments](https://developer.android.com/guide/fragments)with activities in your Wear OS app. However, we don't recommend this, as there isn't a clear advantage to using fragments to create a shallow and flat architecture.

**Note:** If you are using fragments, make them inherit from[`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity). The other activity types use mobile-specific UI elements you don't need for Wear OS.

Some of the difficulties with using fragments in your Wear OS app include the following:

- You must implement the swipe-to-dismiss yourself. Otherwise, when the user performs a swipe, they exit the entire app.
- If you are using[`AmbientMode`](https://developer.android.com/reference/androidx/wear/ambient/AmbientMode), you must customize it to work properly.`AmbientMode`is set on the activity, so you have to take that into account when implementing fragments.

To support swipe-to-dismiss with fragments, you must wrap the fragment-containing view in the[`SwipeDismissFrameLayout`](https://developer.android.com/reference/androidx/wear/widget/SwipeDismissFrameLayout)class. See[The swipe-to-dismiss gesture](https://developer.android.com/training/wearables/apps/exit#swipe-to-dismiss)for more information. Doing this provides users a consistent experience with your app.

**Note:** When using fragments, use[`FragmentManager.add`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#add(int,%20java.lang.Class<?%20extends%20androidx.fragment.app.Fragment>,%20android.os.Bundle))rather than[`FragmentManager.replace`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#replace(int,%20java.lang.Class<?%20extends%20androidx.fragment.app.Fragment>,%20android.os.Bundle))to support the swipe-to-dismiss gesture. This helps ensure that your previous fragment renders under the top fragment while it is being swiped away.

### Jetpack Navigation

Jetpack Navigation can work on Wear OS, but it has the same drawbacks as fragments. It adds development work and, because a Wear OS app's hierarchy is generally shallow and linear, it doesn't offer many advantages. An activity-only approach is best.

To fully leverage Jetpack Navigation, do the following:

- Make sure every fragment uses a[`SwipeDismissFrameLayout`](https://developer.android.com/reference/kotlin/androidx/wear/widget/SwipeDismissFrameLayout)as its root, and manually use the dismiss action to go back in the navigation graph.
- Implement a custom[`FragmentNavigator`](https://developer.android.com/reference/androidx/navigation/fragment/FragmentNavigator)that renders fragments on top of each other.