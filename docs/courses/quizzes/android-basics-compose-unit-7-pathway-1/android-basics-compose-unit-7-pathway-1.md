---
title: https://developer.android.com/courses/quizzes/android-basics-compose-unit-7-pathway-1/android-basics-compose-unit-7-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-compose-unit-7-pathway-1/android-basics-compose-unit-7-pathway-1
source: md.txt
---

# Schedule tasks with WorkManager

# Schedule tasks with WorkManager

<br />

Return to pathway  
1.

   ## Which tool helps you visualize, monitor, and debug your app's workers?

   Profiler  
   Background Task Inspector  
   Logcat  
   Device Manager  
2.

   ## Which of the following options are valid terminal work states?

   Choose as many answers as you see fit.  
   CANCELLED  
   DELETED  
   FAILED  
   SUCCEEDED  
3.

   ## Which of the following options are valid types of work requests?

   Choose as many answers as you see fit.  
   `OneTimeWorkRequest`  
   `SingleWorkRequest`  
   `RepeatingWorkRequest`  
   `PeriodicWorkRequest`  
4.

   ## Creating and enqueueing multiple dependent tasks and the order they should run in is called linking.

   True  
   False  
5.

   ## Work constraints are useful in which of the following situations?

   Checking that a valid form of payment is saved on the user's device before the work runs.  
   Checking what time it is before the work runs.  
   Checking that the device is connected to a wifi network before downloading a large amount of app data.  
   Checking that the app was opened a set number of times before the work runs.  
6.

   ## Which of the following options is a way to pass input data to a worker?

   Pass the data in as an argument when calling the`doWork()`function.  
   Use a Data object to pass key/value pairs.  
   Pass data as a String, but it must be less than 140 characters.  
   Assign it to the`worker.inputData`variable.  
7.

   ## After work is enqueued, you can check its status by ___.

   Choose as many answers as you see fit.  
   Name  
   Id  
   Tag  
   Work type  
8.

   ## The Background Task Inspector lets you stop workers during their execution.

   True  
   False  
9.

   ## Which worker builder is recommended to test`CoroutineWorker`s?

   `OneTimeWorkRequestBuilder`  
   `PeriodicWorkRequestBuilder`  
   `TestWorkerBuilder`  
   `TestListenableWorkerBuilder`  
10.

    ## When testing worker implementations, you can call workers directly with`doWork()`instead of enqueuing the worker.

    True  
    False  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.