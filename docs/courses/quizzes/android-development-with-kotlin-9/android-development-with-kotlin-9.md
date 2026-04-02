---
title: https://developer.android.com/courses/quizzes/android-development-with-kotlin-9/android-development-with-kotlin-9
url: https://developer.android.com/courses/quizzes/android-development-with-kotlin-9/android-development-with-kotlin-9
source: md.txt
---

# Lesson 9: App architecture (persistence)

# Lesson 9: App architecture (persistence)

<br />

Return to pathway  
1.

   ## How do you indicate that a class represents an entity to store in a Room database?

   Make the class extend`DatabaseEntity`.  
   Annotate the class with`@Entity`.  
   Annotate the class with`@Database`.  
   Make the class extend`RoomEntity`and also annotate the class with`@Room`.  
2.

   ## The DAO (data access object) is an interface that Room uses to map Kotlin functions to database queries. How do you indicate that an interface represents a DAO for a Room database?

   Make the interface extend`RoomDAO`.  
   Make the interface extend`EntityDao`, then implement the`DaoConnection()`method.  
   Annotate the interface with`@Dao`.  
   Annotate the interface with`@RoomConnection`.  
3.

   ## Which of the following annotations can you use in your`@Dao`interface? Choose all that apply.

   Choose as many answers as you see fit.  
   `@Get`  
   `@Update`  
   `@Insert`  
   `@Query`  
4.

   ## Which of the following is not a benefit of using coroutines?

   They run asynchronously.  
   They can be run on a thread other than the main thread.  
   They always make the app run faster.  
   They can use exceptions.  
5.

   ## Which of the following is not true for`Suspend`functions?

   An function annotated with the`Suspend`keyword.  
   A function that can be called inside coroutines.  
   While a`Suspend`function is running, the calling thread is suspended.  
   `Suspend`functions must always run in the background.  
6.

   ## Which of the following statements is NOT true?

   When execution is blocked, no other work can be executed on the blocked thread.  
   When execution is suspended, the thread can do other work while waiting for the offloaded work to complete.  
   Suspending is more efficient, because threads may not be waiting, doing nothing.  
   Whether blocked or suspended, execution is still waiting for the result of the coroutine before continuing.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.