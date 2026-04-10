---
title: https://developer.android.com/courses/quizzes/kotlin-fundamentals-four/kotlin-fundamentals-four
url: https://developer.android.com/courses/quizzes/kotlin-fundamentals-four/kotlin-fundamentals-four
source: md.txt
---

# Kotlin Fundamentals: Navigation quiz

# Kotlin Fundamentals: Navigation quiz

<br />

Return to pathway  
1.

   ## Which of the following statements about fragments are true?

   Choose as many answers as you see fit.  
   You can use a fragment in more than one activity.  
   One activity can have multiple fragments.  
   Use thetag to define the place in a layout file where a fragment is to be inserted.  
   After you define a fragment class, the fragment is automatically added to the activity_main.xml layout file.  
2.

   ## How do you enable your project to use navigation components?

   Make sure every Activity class extends the NavigationActivity class.  
   Use the NavigationController class as the launch activity.  
   Addto the Android manifest file.  
   Add dependencies for navigation-fragment-ktx and navigation-ui-ktx in the build.gradle file (module level).  
3.

   ## Which of the following statements about the NavHostFragment are true?

   Choose as many answers as you see fit.  
   As the user moves between destinations defined in the navigation graph, the NavHostFragment swaps the fragments in and out as necessary.  
   You can click the NavHostFragment in the Project view to open the navigation graph.  
   You add the NavHostFragment to the main activity layout by adding awhose android:name attribute is androidx.navigation.fragment.NavHostFragment.  
   You must create a single NavHostFragment subclass and implement the onNavigate() method to handle different kinds of navigation (such as button clicks).  
4.

   ## Where do you define the items for a menu?

   It depends on where the menu will be shown. For a navigation drawer menu, add an \&ltitem\> tag for each menu item in the menu.xml file in res \> drawer folder. For the options menu, add an \&ltitem\> tag for each menu item in the menu.xml file in res \> options folder.  
   In the layout file for the fragment or activity that displays the menu, add a \&ltmenu\> tag that contains \&ltitem\> tags for each item.  
   In a menu_name.xml file in the res \> menu folder, add an \&ltitem\> tag for each menu item. Create separate XML files for each separate menu.  
   In the AndroidManifest.xml file, add a \&ltmenus\> tag that contains a \&ltmenu\> tag for each menu. For each \&ltmenu\> tag, add an \&ltitem\> tag for each menu item.  
5.

   ## What do you need to do to add a navigation drawer to your app? You can assume that your project has a navigation graph and that you already defined the menu items for the drawer.

   Choose as many answers as you see fit.  
   Use DrawerLayout as the root view in the relevant layout file, and add a NavigationView as a child to that root view.  
   Use Navigation as the root view in the relevant layout file and add a NavigationView as a child to that root view.  
   In the NavigationView element in the layout, set the app:menu attribute to the navigation drawer menu resource ID.  
   In the navigation graph XML file, make sure that the navigation menu has an ID.  
6.

   ## If you pass arguments from Fragment A to Fragment B without using Safe Args to make sure your arguments are type-safe, which of the following problems can occur that might cause the app to crash when the app runs?

   Choose as many answers as you see fit.  
   Fragment B requests data that Fragment A doesn't send to it.  
   Fragment A might send data that Fragment B hasn't requested.  
   Fragment A might send data that's a different type than Fragment B needs. For example, fragment A might send a string, but Fragment B requests an integer.  
   Fragment A uses different argument names than Fragment B requests.  
7.

   ## What does the Safe Args Gradle plugin do?

   Choose as many answers as you see fit.  
   Generates simple object and builder classes for type-safe access to arguments specified for destinations and actions  
   Creates Navigation classes that you can edit to simplify the passing of parameters between fragments  
   Make it so you don't need to use Android Bundles in your code  
   Generates a method for each action that you've defined in the navigation graph  
   Prevents your code from using the wrong key when extracting data from a Bundle  
8.

   ## What's an implicit intent?

   A task that your app initiates in one fragment of your app and gets completed in another fragment.  
   A task that your app always completes by showing the user a chosen dialog.  
   A task that your app initiates without knowing which app or activity will handle the task.  
   An implicit intent is the same thing as the action that you set between destinations in the navigation graph.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.