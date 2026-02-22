---
title: https://developer.android.com/courses/quizzes/kotlin-fundamentals-seven/kotlin-fundamentals-seven
url: https://developer.android.com/courses/quizzes/kotlin-fundamentals-seven/kotlin-fundamentals-seven
source: md.txt
---

# Kotlin Fundamentals: Databases and RecyclerView quiz

# Kotlin Fundamentals: Databases and RecyclerView quiz

<br />

Return to pathway  
1.

   ## How can you verify that your database is working as expected?

   Choose as many answers as you see fit.  
   Write instrumented unit tests.  
   Wait until the app displays the data.  
   Replace the calls to the methods in the DAO interface by calls to equivalent methods in the Entity class.  
   Run the verifyDatabase() function provided by the Room library.  
2.

   ## How do you indicate that a class represents an entity to store in a Room database?

   Make the class extend DatabaseEntity.  
   Annotate the class with @Entity.  
   Annotate the class with @Database.  
   Make the class extend RoomEntity and also annotate the class with @Room.  
3.

   ## Which of the following is not true of coroutines?

   They are non blocking.  
   They run asynchronously.  
   They can be run on a thread other than the main thread.  
   They always make app runs faster.  
   They propagate exceptions.  
   They can be written and read as linear code.  
4.

   ## Which of the following statements is not true?

   When execution is blocked, no other work can be executed on the blocked thread.  
   When execution is suspended, the thread can do other work while waiting for the offloaded work to complete.  
   Suspending saves memory over blocking while supporting many concurrent operations.  
   Whether blocked or suspended, execution is still waiting for the result of the coroutine before continuing.  
5.

   ## How does RecyclerView display items?

   Choose as many answers as you see fit.  
   It displays items in a list or a grid.  
   It scrolls vertically or horizontally.  
   It scrolls diagonally on larger devices, such as tablets.  
   It allows custom layouts when a list or a grid is not enough for the use case.  
6.

   ## Which of the following are necessary to use DiffUtil?

   Choose as many answers as you see fit.  
   Extend the ItemCallback class.  
   Override areItemsTheSame().  
   Override areContentsTheSame().  
   Use data binding to track the differences between items.  
7.

   ## Which of the following are layout managers provided by Android?

   Choose as many answers as you see fit.  
   LinearLayoutManager  
   GridLayoutManager  
   CircularLayoutManager  
   StaggeredGridLayoutManager  
8.

   ## Where do you add the`android:onClick`attribute to make items in a RecyclerView respond to clicks?

   In the layout file that displays the RecyclerView, add it to theelement.  
   Add it to the layout file for an item in the row. If you want the entire item to be clickable, add it to the parent view that contains the items in the row.  
   Add the android:onClick attribute onto the RecyclerView.Adapter.  
   Always add it to the layout file for the MainActivity.  
9.

   ## Which of the following statements is true about ViewHolder?

   An adapter can use multiple ViewHolder classes to hold headers and various types of data.  
   You can have exactly one view holder for data and one view holder for a header.  
   A RecyclerView supports multiple types of headers, but the data has to be uniform.  
   When adding a header, you subclass RecyclerView to insert the header at the correct position.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.