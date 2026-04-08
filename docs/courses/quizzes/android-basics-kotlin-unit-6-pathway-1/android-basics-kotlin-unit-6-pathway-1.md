---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-6-pathway-1/android-basics-kotlin-unit-6-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-6-pathway-1/android-basics-kotlin-unit-6-pathway-1
source: md.txt
---

# Schedule tasks with WorkManager

# Schedule tasks with WorkManager

<br />

Return to pathway  
1.

   ## Which of the following is true about`WorkManager`

   Tasks are typically chained, but not run in parallel.  
   `WorkManager`is part of Android Jetpack and requires a Gradle dependency to use.  
   `WorkManager`does not necessarily guarantee that a task will be executed.  
   `WorkRequest`is the name of the class responsible for scheduling and running tasks  
2.

   ## Which of the following would not require`WorkManager`?

   Performing a GET request to a web service.  
   Long running tasks such as downloading large amounts of data  
   Scheduling a task to repeat after a set interval.  
   Doing something while the app is in the background.  
3.

   ## A`Worker`represents a task to be scheduled by`WorkManager`while a`WorkRequest`contains the actual code to be executed.

   True  
   False  
4.

   ## Making execution dependent on device state such as storage space and battery life are examples of

   chaining  
   best practices  
   constraints  
   canceling tasks  
5.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   For a single task, you'd create a`OneTimeWorkRequest`, whereas for a task that needs to repeat after a given interval, you'd create a ___.  
6.

   ## In a chain, the output of the last`WorkRequest`becomes the input for the next`WorkRequest`.

   True  
   False  
7.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   The ___`()`method is implemented by subclasses of the`Worker`class and defines the code to be executed by a`WorkRequest`.  
8.

   ## Which of the following are true about unique work chains?

   Choose as many answers as you see fit.  
   An`ExistingWorkPolicy`is required to determine what happens to an in-progress task (kept, replaced, etc.)  
   Tags can be used to get the`WorkInfo`for the request.  
   If no tag is specified, you can still ensure a task is unique by setting the`WorkManager`ID  
   Unique work can be canceled using the`cancelUniqueWork()`method and providing the tag.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.