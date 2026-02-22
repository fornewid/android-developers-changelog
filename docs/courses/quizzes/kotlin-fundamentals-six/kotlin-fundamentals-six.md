---
title: https://developer.android.com/courses/quizzes/kotlin-fundamentals-six/kotlin-fundamentals-six
url: https://developer.android.com/courses/quizzes/kotlin-fundamentals-six/kotlin-fundamentals-six
source: md.txt
---

# Kotlin Fundamentals: Architecture components quiz

# Kotlin Fundamentals: Architecture components quiz

<br />

Return to pathway  
1.

   ## To avoid losing data during a device configuration change, store app data in which of these options?

   ViewModel  
   LiveData  
   Fragment  
   Activity  
2.

   ## A ViewModel should never contain any references to fragments, activities, or views. True or false?

   True  
   False  
3.

   ## When is a ViewModel destroyed?

   When the associated UI controller is destroyed and recreated during a device-orientation change.  
   When there's a configuration change.  
   When the associated UI controller is finished (if it's an activity) or detached (if it's a fragment).  
   When the callback onCleared() is called.  
4.

   ## How do you encapsulate the LiveData stored in a ViewModel so that external objects can read data without being able to update it?

   Inside the ViewModel, change the data type of the property to be LiveData and make it private. Use a backing property to expose a read-only property of type MutableLiveData.  
   Inside the ViewModel, change the data type of the property to be MutableLiveData and make it private. Use a backing property to expose a read-only property of type LiveData.  
   Inside the UI controller, change the data type of the property to MutableLiveData. Use a backing property to expose a read-only property of type LiveData.  
   Inside the ViewModel, change the data type of the property to LiveData.  
5.

   ## LiveData updates a UI controller (such as a fragment) if the UI controller is in which of the following states?

   Resumed  
   In the background  
   Paused  
   Stopped  
6.

   ## In the LiveData observer pattern, what's the observable item (what is observed)?

   The observer method  
   The data in a LiveData object instance  
   The UI controller  
   The ViewModel  
7.

   ## Which of the following statements is NOT true about listener bindings?

   Listener bindings are binding expressions that run when an event happens.  
   Listener bindings work with all versions of the Android Gradle plugin.  
   Listener bindings are written as lambda expressions.  
   Listener bindings are similar to method references, but they let you run arbitrary data-binding expressions.  
8.

   ## Assume your app includes this string resourceHello %s. Which of the following is the correct syntax for formatting the string, using the data-binding expression?

   android:text= "@{@string/generic_name(user.name)}"  
   android:text= "@{string/generic_name(user.name)}"  
   android:text= "@{@generic_name(user.name)}"  
   android:text= "@{@string/generic_name,user.name}"  
9.

   ## When is a listener-binding expression evaluated and run?

   When the data held by the LiveData is changed  
   When an activity is re-created by a configuration change  
   When an event such as onClick() occurs  
   When the activity goes into the background  
10.

    ## The Transformations.map() method provides an easy way to perform data manipulations on the LiveData and returns ___.

    A ViewModel object  
    A LiveData object  
    A formatted String  
    A RoomDatabase object  
11.

    ## What are the parameters for the Transformations.map() method?

    A source LiveData and a function to be applied to the value stored in LiveData  
    Only a source LiveData  
    No parameters  
    ViewModel and a function to be applied  
12.

    ## The lambda function passed into the Transformations.map() method is executed in which thread?

    Main thread  
    Background thread  
    UI thread  
    In a coroutine  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.