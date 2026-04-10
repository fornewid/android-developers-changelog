---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-4-pathway-1/android-basics-kotlin-unit-4-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-4-pathway-1/android-basics-kotlin-unit-4-pathway-1
source: md.txt
---

# Coroutines

# Coroutines

<br />

Return to pathway  
1.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   The ___ thread, sometimes called the UI thread, is responsible for updating the screen in an Android app.  
2.

   ## Which of the following are some of the pitfalls of directly using threads in your code?

   Choose as many answers as you see fit.  
   Race conditions  
   Inconsistent output  
   Unresponsive UI  
   `Thread`is deprecated  
3.

   ## Which statement below is true about coroutines?

   Once started, a coroutine cannot be canceled.  
   A coroutine always runs on the main thread.  
   A coroutine may or may not execute.  
   Coroutines avoid the need to create new threads, by running every task on the same thread.  
4.

   ## True or False: If a function already calls a`suspend`function, then it does not need to be marked as a suspend function itself.

   True  
   False  
5.

   ## Which of the following are`suspend`functions?.

   Choose as many answers as you see fit.  
   `async()`  
   The lambda passed into`async()`  
   `runBlocking()`  
   The lambda passed into`runBlocking()`  
6.

   ## Which statement below is false about`async()`and`runBlocking()`?

   Both functions take a CoroutineScope (a`suspend`function) as a parameter.  
   Both functions return a Deferred  
   You'll typically not use runBlocking in Android app code.  
   When using async, you need to use await() to access the returned value.  
7.

   ## True or False: In most apps, you would create coroutines using the global scope.

   True  
   False  
8.

   ## What is responsible for determining which thread is used behind the scenes by a coroutine?

   `CoroutineScope`  
   `Dispatcher`  
   `Job`  
   `GlobalScope`  
9.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   A ___ is similar to a promise or future in other languages and serves as a placeholder for a return value.  
10.

    ## True or False: A`Job`is a cancelable unit of work performed by a coroutine.

    True  
    False  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.