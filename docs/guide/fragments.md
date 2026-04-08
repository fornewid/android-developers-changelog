---
title: https://developer.android.com/guide/fragments
url: https://developer.android.com/guide/fragments
source: md.txt
---

# Fragments

A[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment)represents a reusable portion of your app's UI. A fragment defines and manages its own layout, has its own lifecycle, and can handle its own input events. Fragments can't live on their own. They must be*hosted* by an activity or another fragment. The fragment's view hierarchy becomes part of, or*attaches to*, the host's view hierarchy.
| **Note:** Some[Android Jetpack](https://developer.android.com/jetpack/androidx/versions)libraries, such as[Navigation](https://developer.android.com/guide/navigation),[`BottomNavigationView`](https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView), and[`ViewPager2`](https://developer.android.com/jetpack/androidx/releases/viewpager2), are designed to work with fragments.

## Modularity

Fragments introduce modularity and reusability into your activity's UI by letting you divide the UI into discrete chunks. Activities are an ideal place to put global elements around your app's user interface, such as a navigation drawer. Conversely, fragments are better suited to define and manage the UI of a single screen or portion of a screen.

Consider an app that responds to various screen sizes. On larger screens, you might want the app to display a static navigation drawer and a list in a grid layout. On smaller screens, you might want the app to display a bottom navigation bar and a list in a linear layout.

Managing these variations in the activity is unwieldy. Separating the navigation elements from the content can make this process more manageable. The activity is then responsible for displaying the correct navigation UI, while the fragment displays the list with the proper layout.
![Two versions of the same screen on different screen sizes.](https://developer.android.com/static/images/guide/fragments/fragment-screen-sizes.png)**Figure 1.**Two versions of the same screen on different screen sizes. On the left, a large screen contains a navigation drawer that is controlled by the activity and a grid list that is controlled by the fragment. On the right, a small screen contains a bottom navigation bar that is controlled by the activity and a linear list that is controlled by the fragment.

Dividing your UI into fragments makes it easier to modify your activity's appearance at runtime. While your activity is in the`STARTED`[lifecycle state](https://developer.android.com/guide/components/activities/activity-lifecycle)or higher, fragments can be added, replaced, or removed. And you can keep a record of these changes in a back stack that is managed by the activity, so that the changes can be reversed.

You can use multiple instances of the same fragment class within the same activity, in multiple activities, or even as a child of another fragment. With this in mind, only provide a fragment with the logic necessary to manage its own UI. Avoid depending on or manipulating one fragment from another.

## Next steps

For more documentation and resources related to fragments, see the following.

### Getting Started

- [Create a fragment](https://developer.android.com/guide/fragments/create)

### Further topics

- [Fragment manager](https://developer.android.com/guide/fragments/fragmentmanager)
- [Fragment transactions](https://developer.android.com/guide/fragments/transactions)
- [Navigate between fragments using animations](https://developer.android.com/guide/fragments/animate)
- [Fragment lifecycle](https://developer.android.com/guide/fragments/lifecycle)
- [Saving state with fragments](https://developer.android.com/guide/fragments/saving-state)
- [Communicate with fragments](https://developer.android.com/guide/fragments/communicate)
- [Working with the AppBar](https://developer.android.com/guide/fragments/appbar)
- [Display dialogs with DialogFragment](https://developer.android.com/guide/fragments/dialogs)
- [Debug your fragments](https://developer.android.com/guide/fragments/debugging)
- [Test your fragments](https://developer.android.com/guide/fragments/test)

### Samples

### Videos

- [Single Activity: Why, when, and how (Android Dev Summit '18)](https://www.youtube.com/watch?v=2k8x8V77CrU)
- [Fragments: Past, present, and future (Android Dev Summit '19)](https://www.youtube.com/watch?v=RS1IACnZLy4)