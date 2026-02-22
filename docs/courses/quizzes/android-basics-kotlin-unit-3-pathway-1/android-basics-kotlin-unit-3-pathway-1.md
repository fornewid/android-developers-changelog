---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-1/android-basics-kotlin-unit-3-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-1/android-basics-kotlin-unit-3-pathway-1
source: md.txt
---

# Navigate between screens

# Navigate between screens

<br />

Return to pathway  
1.

   ## Which of the following is false about collections and higher order functions in Kotlin?

   Lists, maps, and sets can all use higher order functions.  
   Lists are unordered, while maps and sets are ordered data types.  
   Like the elements in a set, the keys in a map must be unique. However, multiple keys can map to the same value.  
   Higher order functions such as map and filter can take lambda functions as parameters.  
2.

   ## Given the following code, what is the result of`oneWordCities[1]`?

   ```kotlin
   val cities = listOf("Jeddah", "Bengaluru", "Shenzhen", "Abu Dhabi", "Mountain View", "Tripoli", "Bengaluru", "Lima", "Mandalay", "Tripoli")
   val oneWordCities = cities.toSet().toList().filter { !it.contains(" ")}.sorted()
   ```
   Tripoli  
   Abu Dhabi  
   Jeddah  
   Bengaluru  
3.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   A(n) ___ is a piece of data passed between activities when launching an intent.  
4.

   ## If you open an app, and then leave the app using the back button, in which order were the following activity lifecycle methods called?

   `onStart(), onCreate(), onDestroy(), onStop()`  
   `onDestroy(), onStart(), onCreate(), onStop()`  
   `onCreate(), onStart(), onStop(), onDestroy()`  
   `onStart(), onCreate(), onStop(), onDestroy()`  
5.

   ## Which activity lifecycle method would be called if a dialog appears onscreen, partially obscuring an activity?

   `onPause()`because the activity is still displayed, but no longer has focus.  
   `onStop()`because the activity does not need to respond to user input while the dialog is onscreen.  
   `onResume()`because the activity needed to respond to user input to display the dialog.  
   `onDestroy()`because the activity does not need to exist so long as it doesn't have focus.  
6.

   ## Which of the following is true about the lifecycle of a single activity?

   Choose as many answers as you see fit.  
   `onStart()`can be called multiple times, while`onCreate()`can only be called once.  
   `onStop()`can be called multiple times, while`onPause()`can only be called once.  
   `onDestroy()`is called when the app enters the background.  
   `onResume()`is called when the activity gains focus.  
7.

   ## Which of the following is false about intents?

   Both implicit and explicit intents allow your app to launch another activity.  
   Explicit intents require you to specify the class of the activity you want to show.  
   Intents are performed using the`startActivity()`method.  
   An implicit intent always results in the system asking the user which app to open.  
8.

   ## An activity contains the following code in`onCreate()`. What will happen when this code is executed, if the`intent`property is`null`?

   ```kotlin
   val message = intent.extras?.getString("message"
   ).toString()
   ```
   The app will crash because it attempted to access the extras property on a null object.  
   The app will crash because it attempted to access a null object.  
   The app will not crash because the extras property is accessed unsafely using`?`.  
   The app will not crash because the extras property is accessed safely using`?`.  
9.

   ## Which of the following tasks can be performed in`onCreate()`?

   Choose as many answers as you see fit.  
   Configuring views, such as setting the layout manager of a recycler view.  
   Determining the items to be shown in the options menu.  
   Setting the`onClickListener`for items in the options menu.  
   Getting extras from the intent that launched the activity.  
10.

    ## In which method should you handle what happens when a button in the app bar is pressed?

    `onCreateOptionsMenu()`  
    `openOptionsMenu()`  
    `onOptionsItemSelected()`  
    `onPrepareOptionsMenu()`  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.