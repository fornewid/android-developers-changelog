---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-2/android-basics-kotlin-unit-3-pathway-2
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-2/android-basics-kotlin-unit-3-pathway-2
source: md.txt
---

# Introduction to the Navigation component

# Introduction to the Navigation component

<br />

Return to pathway  
1.

   ## True or False:`onCreateView()`is only called once for a fragment's entire lifecycle.

   True  
   False  
2.

   ## Which of the following is a benefit of using fragments?

   Navigation between fragments allows for more sophisticated user interface patterns, such as tab bars.  
   Using multiple fragments within an activity allows for an adaptive layout across multiple screen sizes.  
   The same fragments can be reused across multiple activities.  
   All of the above  
3.

   ## In the fragment lifecycle, which of the following tasks should be performed in`onViewCreated()`?

   Choose as many answers as you see fit.  
   Inflating the layout  
   Binding view objects to properties in your fragment  
   Configuring the options menu  
   Setting properties of individual views, such as a recycler view's adapter  
4.

   ## In the fragment lifecycle, which of the following tasks should be performed in`onCreateView()`?

   Inflating the layout  
   Binding view objects to properties in your fragment  
   Configuring the options menu  
   Setting properties of individual views, such as a recycler view's adapter  
5.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   The ___ method needs to be overridden in the host activity to ensure your app's fragment-based navigation responds to the app's "Up" button.  
6.

   ## Given the code for navigating between two fragments in a note-taking app, a list of books and a list of notes, which of the following is true about the navigation graph file?

   ```kotlin
   val action = BooksListFragmentsDirections.actionBooksListToNotesList(bookIndex = index)
   holder.view.findNavController().navigate(action)
   ```
   A: Both the books list and notes list are destinations.  
   B: The books list fragment has an argument called`bookIndex`.  
   C: There's an action defined on the navigation graph that goes from the books list to the notes list.  
   D: A, B, and C are true.  
   E: Only A and C are true.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.