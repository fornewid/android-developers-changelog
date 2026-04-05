---
title: https://developer.android.com/courses/quizzes/android-development-with-kotlin-8/android-development-with-kotlin-8
url: https://developer.android.com/courses/quizzes/android-development-with-kotlin-8/android-development-with-kotlin-8
source: md.txt
---

# Lesson 8: App architecture (UI layer)

# Lesson 8: App architecture (UI layer)

<br />

Return to pathway  
1.

   ## To avoid losing data during a device-configuration change, you should save app data in which class?

   `ViewModel`  
   `LiveData`  
   `Fragment`  
   `Activity`  
2.

   ## A`ViewModel`should never contain any references to fragments, activities, or views. True or false?

   True, it should never contain any references.  
   False, it should contain at least a reference to one of the above.  
3.

   ## When is a`ViewModel`destroyed?

   When the associated UI controller is destroyed and recreated during a device-orientation change.  
   In an orientation change.  
   When the associated UI controller is finished (if it is an activity) or detached (if it is a fragment).  
   When the user presses the Back button.  
4.

   ## What is the`ViewModelFactory`interface for?

   Instantiating a`ViewModel`object.  
   Retaining data during orientation changes.  
   Refreshing the data being displayed on the screen.  
   Receiving notifications when the app data is changed.  
5.

   ## How do you encapsulate the`LiveData`stored in a`ViewModel`so that external objects can read data without being able to update it?

   Inside the`ViewModel`object, change the data type of the data to private`LiveData`. Use a backing property to expose read-only data of the type`MutableLiveData`.  
   Inside the`ViewModel`object, change the data type of the data to private`MutableLiveData`. Use a backing property to expose read-only data of the type`LiveData`.  
   Inside the UI controller, change the data type of the data to private`MutableLiveData`. Use a backing property to expose read-only data of the type`LiveData`.  
   Inside the`ViewModel`object, change the data type of the data to`LiveData`. Use a backing property to expose read-only data of the type`LiveData`.  
6.

   ## `LiveData`updates a UI controller (such as a fragment) if the UI controller is in which of the following states?

   Resumed  
   In the background  
   Paused  
   Stopped  
7.

   ## In the`LiveData`observer pattern, what is the observable item (what is observed)?

   The observer method  
   The data in a`LiveData`object  
   The UI controller  
   The`ViewModel`object  
8.

   ## In which class should you add the data-formatting logic that uses the`Transformations.map()`method to convert`LiveData`to a different value or format?

   `ViewModel`  
   `Fragment`  
   `Activity`  
   `MainActivity`  
9.

   ## The`Transformations.map()`method provides an easy way to perform data manipulations on the`LiveData`and returns ___.

   A`ViewModel`object  
   A`LiveData`object  
   A formatted`String`  
   A`RoomDatabase`object  
10.

    ## What are the parameters for the`Transformations.map()`method?

    A source`LiveData`and a function to be applied to the`LiveData`  
    Only a source`LiveData`  
    No parameters  
    `ViewModel`and a function to be applied  
11.

    ## The lambda function passed into the`Transformations.map()`method is executed in which thread?

    Main thread  
    Background thread  
    UI thread  
    In a coroutine  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.