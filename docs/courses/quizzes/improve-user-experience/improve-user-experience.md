---
title: https://developer.android.com/courses/quizzes/improve-user-experience/improve-user-experience
url: https://developer.android.com/courses/quizzes/improve-user-experience/improve-user-experience
source: md.txt
---

# Improve the user experience of your Android app

# Improve the user experience of your Android app

<br />

Return to pathway  
1.

   ## What are the edge-to-edge enforcements in Android 15?

   Choose as many answers as you see fit.  
   Three button navigation bar is semi-transparent (translucent)  
   Gesture navigation bar is transparent  
   Status bar is transparent  
   Content will draw behind system bars by default  
   Task bar on large screen devices is transparent  
   System bars are opaque and green by default  
2.

   ## Which of the following are allowed values for non-floating windows?

   LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS  
   LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT  
   LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER  
   LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES  
3.

   ## Which Window APIs are deprecated in Android 15?

   Choose as many answers as you see fit.  
   `setStatusBarContrastEnforced`  
   `setNavigationBarContrastEnforced`  
   `setStatusBarColor`  
   `setNavigationBarColor`  
   `setSystemBarColors`  
4.

   ## What is the primary benefit of implementing predictive back in an Android app?

   It gives users a faster way to navigate back to their home screen.  
   It eliminates the need to use the back button entirely.  
   It enhances user experience by providing visual feedback before navigation changes occur.  
   It helps identify compatibility issues with older Android versions.  
5.

   ## To add predictive back support for Material View Components, which of the following has to be true?

   Choose as many answers as you see fit.  
   Set the`android:enableOnBackInvokedCallback`flag to true in AndroidManifest.xml.  
   Create a custom animation class and apply it to your Activity.  
   Upgrade to Navigation Component version 2.7 or higher.  
   API level is 33+.  
   Implement a custom`onBackPressedDispatcher()`method in your Activity.  
6.

   ## Using Animator and AndroidX transitions helps achieve predictive back support for fragments.

   True  
   False  
7.

   ## Which class is responsible for rendering widgets into remote views?

   GlanceAppWidget  
   GlanceAppReceiver  
   AppWidgetProvider  
   GlanceAppWidgetProvider  
8.

   ## Which of these actions can you take to update the content of an existing widget on the home screen?

   Choose as many answers as you see fit.  
   Modify the view hierarchy directly from the activity, similar to Jetpack Compose.  
   Call the`updateAll()`method on your AppWidget class.  
   Send a broadcast with the APPWIDGET_UPDATE action to trigger a refresh.  
   Update the data in your preferences datastore.  
   Wait for the`updatePeriodMillis`to pass, and the widget host will request an update  
   The widget is automatically updated when your app starts.  
9.

   ## Glance widgets must always define a 'zero state' to prompt the user for initial configuration.

   True  
   False  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.