---
title: https://developer.android.com/courses/quizzes/android-development-with-kotlin-6/android-development-with-kotlin-6
url: https://developer.android.com/courses/quizzes/android-development-with-kotlin-6/android-development-with-kotlin-6
source: md.txt
---

# Lesson 6: App navigation

# Lesson 6: App navigation

<br />

Return to pathway  
1.

   ## Which of the following statements about fragments are true? Select all that apply.

   Choose as many answers as you see fit.  
   You can use a`Fragment`in more than one`Activity`.  
   One`Activity`can have multiple fragments.  
   After you define a`Fragment`in a Kotlin class, the fragment is automatically added to the`activity_main.xml`layout file.  
   Use the`<fragment>`tag to define the place in a layout file where a`Fragment`is to be inserted.  
2.

   ## How do you enable your project to use navigation components?

   Make sure every`Activity`class extends the class`NavigationActivity`.  
   Use the`NavigationController`class as the launch activity.  
   Add`uses-navigation`to the`AndroidManifest.xml`file.  
   Add dependencies for`navigation-fragment-ktx`and`navigation-ui-ktx`in the`build.gradle`(module) file.  
3.

   ## Where are the possible navigation routes through your app defined?

   In a file (often called`navigation.xml`) in the`res`\>`layout`folder.  
   In a file (often called`navigation.xml`) in the`app`\>`navigation`folder.  
   In a file (often called`navigation.xml`) in the`res`\>`navigation`folder.  
   In the`AndroidManifest.xml`file, under theelement.  
4.

   ## Which of the following statements about the`NavHostFragment`are true?

   Choose as many answers as you see fit.  
   As the user moves between destinations defined in the navigation graph, the`NavHostFragment`swaps the fragments in and out as necessary.  
   You can click the`NavHostFragment`in the project view to open the navigation graph.  
   You add the`NavHostFragment`to the main layout by adding a fragment whose name is`androidx.navigation.fragment.NavHostFragment`.  
   You must create a single`NavHostFragment`subclass and implement the`onNavigate()`method to handle different kinds of navigation (such as button clicks)  
5.

   ## Where do you set the ID of a fragment to be used in navigation?

   In the fragment layout file, either by setting the ID attribute in the design editor or in the layout XML file in the`res`\>`layout`folder.  
   In the project navigation file, either by setting the ID attribute in the navigation graph or in the`navigation.xml`file in the`res`\>`navigation`folder.  
   You need to set the ID in both the navigation file for the app and the layout file for the fragment.  
   Set the ID variable in the relevant`Fragment`class.  
6.

   ## Where do you define the items for a menu?

   It depends on where the menu will be shown. For a navigation drawer menu, add an`<item>`tag for each menu item in the`menu.xml`file in the`res`\>`drawer`folder. For the options menu, add an`<item>`tag for each menu item in the`menu.xml`file in the`res`\>`options`folder.  
   In the layout file for the fragment or activity that displays the menu, add a`<menu>`tag that contains`<item>`tags for each item.  
   In a`menu_name.xml`file in the`res`\>`menu`folder, add an`<item>`tag for each menu item. Create separate XML files for each separate menu.  
   In the`AndroidManifest.xml`file, add a`<menus>`tag that contains a`<menu>`tag for each menu, that in turn contains an`<item>`tag for each menu item.  
7.

   ## What do you need to do to enable the overflow menu (also known as the options menu)? You can assume you have already defined the menu items.

   Choose as many answers as you see fit.  
   Call`setHasOptionsMenu(true)`in`onCreate()`for an`Activity`or`onCreateView()`for a`Fragment`.  
   Implement`onCreateOptionsMenu()`in the`Activity`or`Fragment`to create the menu.  
   Set the`onClick`attribute in the`menu.xml`file to`onShowOptionsMenu`, unless you are implementing a custom`onClick`listener for the options menu, in which case specify the name of that custom listener instead.  
   Implement`onOptionsItemSelected()`in the`Activity`or`Fragment`to determine what happens when a user selects a menu item in the options menu.  
8.

   ## What does the Safe Args Gradle plugin do? Select all that apply.

   Choose as many answers as you see fit.  
   Generates simple object and builder classes for type-safe access to arguments specified for destinations and actions.  
   Creates`Navigation`classes that you can edit to simplify the passing of parameters between fragments.  
   Generates a method for each action that you have defined in the navigation graph.  
   Prevents your code from using the wrong key when extracting data from a bundle.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.