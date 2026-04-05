---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-3/android-basics-kotlin-unit-3-pathway-3
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-3/android-basics-kotlin-unit-3-pathway-3
source: md.txt
---

# Architecture components

# Architecture components

<br />

Return to pathway  
1.

   ## Which of the following are reasons to use a ViewModel?

   Choose as many answers as you see fit.  
   A ViewModel and its data can survive orientation changes in an Activity/Fragment.  
   A ViewModel allows you to separate code that updates the UI from code that doesn't need to rely on the UI or its lifecycle.  
   A ViewModel prevents your data from updating the UI automatically.  
2.

   ## A ViewModel is destroyed after which of the following ?

   always after`onStop`  
   always after`onDestroy`  
   after`onDestroy`, if it not a configuration change  
3.

   ## True or False: You should execute time-consuming tasks and I/O requests in your Activity/Fragment.

   True  
   False  
4.

   ## Why should you initialize and store LiveData in your ViewModel instead of a UI Controller?

   Both the ViewModel and LiveData are lifecycle aware.  
   To ensure that the LiveData isn't destroyed when the UI Controller is destroyed.  
   To hide or separate implementation details making your app more flexible.  
   All of the above  
5.

   ## Which of the following allows you to use`observe`for changes?

   a LiveData object  
   any mutable object  
   any property in a ViewModel  
   any property in a ViewModel or LiveData object  
6.

   ## True or False: It's OK for a ViewModel to directly reference a`View`or`LifecycleOwner`class.

   True  
   False  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.