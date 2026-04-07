---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-5-pathway-2/android-basics-kotlin-unit-5-pathway-2
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-5-pathway-2/android-basics-kotlin-unit-5-pathway-2
source: md.txt
---

# Use Room for data persistence

# Use Room for data persistence

<br />

Return to pathway  
1.

   ## Which of the following is false about the`@Query`annotation?

   The`@Query`annotation is used with a method in the DAO.  
   The`@Query`annotation corresponds to a`SELECT`query.  
   The`@Query`annotation can pass arguments into a SQL statement by preceding their name with a colon.  
   The`@Query`annotation can only be used with a suspend function.  
2.

   ## Which of the following are true about the DAO?

   Choose as many answers as you see fit.  
   DAO functions use annotations like`@Insert`and`@Update`that correspond to an operation on the database.  
   DAO functions are typically called directly from a fragment.  
   DAO functions can return a flow.  
   Instances of DAO classes are referenced in the`AppDatabase`class.  
3.

   ## Why do you need to use the`synchronized()`function when creating the database?

   Choose as many answers as you see fit.  
   `synchronized()`is used to avoid race conditions.  
   `synchronized()`ensures only one thread can enter the block of code at once.  
   Doing so allows multiple copies of the database to be created.  
   Calling`synchronized()`allows this code to be safely accessed from multiple threads at once.  
4.

   ## Which of the following is false about the`AppDatabase`class?

   `AppDatabase`is an abstract class that inherits from`RoomDatabase`.  
   The`AppDatabase`holds a reference to the view models.  
   The`@Database`annotation specifies the entities (tables) in the database.  
   The`getDatabase()`function can create a new database, pre-populated from a file.  
5.

   ## The`@Insert`and`@Delete`annotations can be used without providing a SQL statement.

   True  
   False  
6.

   ## Which of the following is true about the`ViewModel`in an app using Room?

   Choose as many answers as you see fit.  
   The`ViewModel`interacts with the DAO.  
   The`ViewModel`updates the UI on the main thread.  
   The`ViewModel`exposes data from the database to your app's UI.  
   The`ViewModel`is held by a reference in the`AppDatabase`class.  
7.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   To handle conflicts when inserting into a database, you can pass an ___, such as`IGNORE`, to the`@Insert`annotation.  
8.

   ## The`ViewModel`factory is a class that inherits from ___ and is responsible for creating instances of the`ViewModel`class.

   `ViewModelFactory`  
   `ViewModelFactory.Provider`  
   `ViewModelProvider.Factory`  
   `ViewModelProvider`  
9.

   ## True or False: In a Room app, the`Application`class allows other objects to access the`AppDatabase`class.

   True  
   False  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.