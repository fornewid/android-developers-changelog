---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-2-pathway-3/android-basics-kotlin-unit-2-pathway-3
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-2-pathway-3/android-basics-kotlin-unit-2-pathway-3
source: md.txt
---

# Display a scrollable list

# Display a scrollable list

<br />


Return to pathway  
1.

   ## Before running the below code, `simpleList` should be initialized as a ___ list.

   ```kotlin
   println(simpleList)
   simpleList.add(-5)
   simpleList.remove(4)
   println(simpleList)
   ```
   Int  
   scrollable  
   sorted  
   mutable  
2.

   ## Which of the following statements are valid?


   Choose as many answers as you see fit.  
   `val list = listOf(1, 2, 5)`  
   `val oddNumbers = mutableListOf("1", "9", "15")`  
   `val listValues: MutableList&ltBoolean>`  
   `val fruits = list("apple", "banana", "pear")`  
   `val words: List&ltString> = listOf("jump", "run", "skip")`  
3.

   ## Why does a `RecyclerView` need an Adapter?

   To adapt data to display on a specific device type  
   To create a new `ViewGroup`  
   To adapt data from a data source into JSON  
   To create new `ViewHolders` and bind data to them  
4.

   ## Which of the following are advantages to using `RecyclerView`?


   Choose as many answers as you see fit.  
   `RecyclerView` comes with built-in layout managers.  
   `RecyclerView` lets you use packages to organize your code.  
   `RecyclerView` helps save processing time, which can help scrolling through a list smoother.  
   `RecyclerView` is designed to be efficient for lists by reusing views that have scrolled off the screen.  
   `RecyclerView` automatically incorporates Material Design components.  
5.

   ## Which of the following is true about packages?


   Choose as many answers as you see fit.  
   You can use packages to organize your code.  
   In order to use a class from another package, you have to explicitly import it in your code.  
   The package name is usually structured from specific to general.  
   It is good practice to use packages to group classes by functionality.  
6.

   ## What should you do to ensure that the correct type of resource ID is passed in to a constructor?

   Use an Adapter to force the type.  
   Only use a `stringResourceId` or `imageResourceId`.  
   Use resource annotations.  
   Use a naming convention to pass the ID in the form `R.&lttype>`.  
   None of the above  
7.

   ## Fill-in-the-blanks


   Enter one or more words to complete the sentence.  

   In the below code, ___ should be written in the `for` loop, so that the output returned is the list of numbers 1 through 3, with each number printed on a new line.  

   ```kotlin
   val numbers = listOf(1, 2, 3)
   for (_______) {
     println(num)
   }
   ```  

Submit answers


*error_outline* An error occurred when grading the quiz. Please try again.