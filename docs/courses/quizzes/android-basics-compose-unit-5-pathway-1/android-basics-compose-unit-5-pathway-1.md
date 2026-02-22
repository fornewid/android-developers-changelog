---
title: https://developer.android.com/courses/quizzes/android-basics-compose-unit-5-pathway-1/android-basics-compose-unit-5-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-compose-unit-5-pathway-1/android-basics-compose-unit-5-pathway-1
source: md.txt
---

# Get data from the internet

# Get data from the internet

<br />

Return to pathway  
1.

   ## With concurrent programming, code might execute in an order different from how it was written.

   True  
   False  
2.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   The ___ thread is responsible for displaying the user interface responding to user input.  
3.

   ## Which of the following statements are true about coroutine contexts?

   Choose as many answers as you see fit.  
   `Dispatchers.Default`is the best choice for long running tasks involving reading and writing large amounts of data.  
   `Dispatchers.Main`can be used for updating the UI but not for long-running tasks.  
   A`Job`controls the lifecycle of a coroutine.  
   `Dispatchers.IO`is optimized for network I/O, among other background tasks.  
4.

   ## `launch()`and`async()`are extension functions of a ___, which keeps track of any coroutines it creates.

   `CoroutineScope`  
   `Job`  
   `Dispatcher`  
   `CoroutineContext`  
5.

   ## Which of the following statements are true about structured concurrency and its best practices?

   Choose as many answers as you see fit.  
   If a coroutine is canceled, child coroutines should also be canceled.  
   A parent scope can complete before one or more of its children are completed.  
   A failure should propagate downward without canceling the parent coroutine.  
   Coroutines must be launched from a coroutine scope.  
6.

   ## Which of the following statements are true about web services?

   Choose as many answers as you see fit.  
   GET, POST, and DELETE are all examples of HTTP operations.  
   A URL is a type of URI but not all URIs are URLs.  
   RESTful services always provide a formatted XML response.  
   Retrofit is a third-party library for handling JSON from a web service.  
7.

   ## Retrofit is a third-party library that enables your app to make requests to a(n) ___ web service.

   XML  
   Socket  
   RESTful  
   JSON  
8.

   ## One recommended way to perform a Retrofit network request is with a coroutine launched in the`viewModelScope`.

   True  
   False  
9.

   ## To enable your app to make connections to the Internet, add the '`android.permission.INTERNET`' permission in the ___ file.

   `MainActivity`  
   `build.gradle`  
   Android manifest  
   `ViewModel`  
10.

    ## The process of turning a JSON result into usable data, as is done with Gson, is called JSON ___.

    Serialization  
    Encoding  
    Converting  
    Parsing  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.