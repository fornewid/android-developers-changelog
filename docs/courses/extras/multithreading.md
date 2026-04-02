---
title: https://developer.android.com/courses/extras/multithreading
url: https://developer.android.com/courses/extras/multithreading
source: md.txt
---

# Multi-threading &amp; callbacks primer

The[Developing Android Apps in Kotlin course](https://codelabs.developers.google.com/codelabs/kotlin-android-training-welcome/index.html?index=../..index#0)assumes that you are familiar with the concept and terminology of multi-threading. This page is a high-level introduction and refresher.

Mobile devices have processors, and these days, most devices have multiple hardware processors that each run processes concurrently. This is called*multiprocessing*.

To use processors more efficiently, the operating system can enable an application to create more than one thread of execution within a process. This is called*multi-threading*.

![image](https://developer.android.com/static/courses/extras/images/multi-threading-1.png)

You can think of it as reading multiple books at the same time, switching between books after each chapter, eventually finishing all books, but you can't read more than one book at the exact same time.

It takes a bit of infrastructure to manage all those threads.

![image](https://developer.android.com/static/courses/extras/images/multi-threading-2.png)

The*scheduler*takes into account things such as priorities, and makes sure all the threads get to run and finish. No book is allowed to sit in the shelf forever and gather dust, but if a book is very long, or can wait, it may take a while before it gets sent your way.

The*Dispatcher* sets up threads, that is, it sends you books that you need to read, and specifies a**context**for that to happen in. You can think of the context as a separate, specialized reading room. Some contexts are best for user interface operations, and some are specialized to deal with input/output operations.

The only other thing to know is that a user-facing application usually has a*main thread*that runs in the foreground and can dispatch other threads that may run in the background.

On Android, the main thread is a single thread that handles all updates to the UI. This main thread, also called the*UI thread*, is also the thread that calls all click handlers and other UI and lifecycle callbacks. The UI thread is the default thread. Unless your app explicitly switch threads or uses a class that runs on a different thread, everything your app does is on the main thread.

This creates a potential challenge. The UI thread has to run smoothly to guarantee a great user experience. For your app to display to the user without any visible pauses, the main thread has to update the screen every 16 ms or more often, or at about 60 frames per second. At this speed, humans perceive the change of frames as completely smooth. That's a lot of frames and little time. Therefore, on Android it's essential to avoid blocking the UI thread.*Blocking*in this context means the UI thread is not doing anything at all while it waits for something like a database to finish updating.

![image](https://developer.android.com/static/courses/extras/images/multi-threading-3.png)

Many common tasks take longer than 16 milliseconds, such as fetching data from the internet, reading a large file, or writing data to a database. Therefore, calling code to perform tasks like those from the main thread can cause the app to pause, stutter, or even freeze. And if you block the main thread for too long, the app may even crash and present an "application not responding" (ANR) dialog.

## Callbacks

You have several options for how to get work done off of from the main thread.

One pattern for performing long-running tasks without blocking the main thread is*[callbacks](https://en.wikipedia.org/wiki/Callback_(computer_programming))*. By using callbacks, you can start long-running tasks on a background thread. When the task completes, the callback, supplied as an argument, is called to inform your code of the result on the main thread.

Callbacks are a great pattern, but they have a few drawbacks. Code that heavily uses callbacks can become hard to read and harder to reason about. Because while the code looks sequential, the callback code will run at some asynchronous time in the future. In addition, callbacks don't allow the use of some language features, such as exceptions.

## Coroutines

In Kotlin,*[coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html)*are the solution for handling long-running tasks elegantly and efficiently. Kotlin coroutines let you convert callback-based code to sequential code. Code written sequentially is typically easier to read, and can even use language features such as exceptions. In the end, coroutines and callbacks do exactly the same thing: wait until a result is available from a long-running task and continue execution.