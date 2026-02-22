---
title: https://developer.android.com/courses/quizzes/android-basics-compose-unit-6-pathway-2/android-basics-compose-unit-6-pathway-2
url: https://developer.android.com/courses/quizzes/android-basics-compose-unit-6-pathway-2/android-basics-compose-unit-6-pathway-2
source: md.txt
---

# Use Room for data persistence

# Use Room for data persistence

<br />

Return to pathway  
1.

   ## Which of the following statements is not true about the`@Query`annotation?

   The`@Query`annotation is used with a method in the DAO.  
   The`@Query`annotation corresponds to a`SELECT`query.  
   The`@Query`annotation can pass arguments into a SQL statement by preceding their name with a colon.  
   The`@Query`annotation can only be used with a suspend function.  
2.

   ## Which of the following statements are true about the DAO?

   DAO functions use annotations like`@Insert`and`@Update`that correspond to an operation on the database.  
   DAO functions can return a flow.  
   Instances of DAO classes are referenced in the`AppDatabase`class.  
   All of the above  
3.

   ## The Database class, inheriting from the RoomDatabase class, is responsible for ___.

   Instantiating the database and providing access to the DAO.  
   Representing individual data tables.  
   Defining functions that map to SQL statements, such as`SELECT`queries.  
   Provides data to the UI.  
4.

   ## The purpose of the DAO is to:

   Hold reference to the view models and the database.  
   Define functions that map to SQL statements, such as`SELECT`, and`INSERT`queries.  
   Provide a factory method to create a database instance.  
   Create a new database instance.  
5.

   ## Why do you need to use the`synchronized()`function when you create the database?

   Choose as many answers as you see fit.  
   It lets you create multiple copies of the database.  
   It lets you safely access the code from multiple threads at once.  
   It is used to avoid race conditions.  
   It ensures only one thread can enter the block of code at once.  
6.

   ## You can use the`@Insert`and`@Delete`annotations without providing a SQL statement.

   True  
   False  
7.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   To handle conflicts when inserting into a database, you can pass a(n) ___ parameter, such as`IGNORE`, to the`@Insert`annotation.  
8.

   ## Select all the statements that are true about the Database Inspector:

   Choose as many answers as you see fit.  
   It lets you inspect, query, and modify your app's databases while your app is running.  
   It works with other SQLite libraries that you bundle with your app.  
   It is especially useful for database debugging.  
   It works with plain SQLite and with libraries built on top of SQLite, such as Room.  
9.

   ## Entities represent individual data tables in the Room database.

   True  
   False  
10.

    ## Which of the following statement is not true about the primary key:

    You can use the primary key to uniquely identify every record/entry in your database tables.  
    After you assign the primary key, you cannot modify it.  
    Room generates an incrementing primary key value for each entity by default.  
    The primary key represents the entity object as long as it exists in the database.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.