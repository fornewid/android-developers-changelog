---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-2-pathway-1/android-basics-kotlin-unit-2-pathway-1
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-2-pathway-1/android-basics-kotlin-unit-2-pathway-1
source: md.txt
---

# Get user input in an app: Part 1

# Get user input in an app: Part 1

<br />

Return to pathway  
1.

   ## Which of the following is true about class inheritance?

   Class inheritance lets you reuse code and makes your program easier to maintain.  
   Properties and functions of the parent class(es) are available to the child class.  
   You can define additional properties and functions that are specific to subclasses.  
   You can override parent class members in subclasses.  
   All of the above  
2.

   ## Which of the following are true about abstract classes?

   Choose as many answers as you see fit.  
   They can be extended by subclasses and implementations can be provided for abstract members of the class.  
   They have an implementation for all of their properties and functions.  
   They may have abstract properties or abstract functions.  
   They can be instantiated.  
   They are not fully implemented and cannot be instantiated.  
   They need to be marked with the`open`keyword to be extended.  
3.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   The ___ is called when you create an instance of a class.  
4.

   ## How do you mark a property to be used only inside its current class?

   Use the`override`keyword.  
   Use the`val`keyword.  
   Use the`private`keyword.  
   Use the`closed`keyword.  
   It is not possible to do this.  
5.

   ## Select all answers that are true for this XML layout when displayed on the screen. (You can sketch this out on a piece of paper first, if that helps.)

   ```kotlin
   &ltandroidx.constraintlayout.widget.ConstraintLayout
       android:layout_width="match_parent"
       android:layout_height="match_parent"&gt
       &ltTextView
           android:id="@+id/textViewA"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:text="A"
           app:layout_constraintStart_toStartOf="parent"
           app:layout_constraintTop_toTopOf="parent" /&gt
       &ltTextView
           android:id="@+id/textViewB"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:text="B"
           app:layout_constraintEnd_toEndOf="parent"
           app:layout_constraintTop_toTopOf="parent" /&gt
   &lt/androidx.constraintlayout.widget.ConstraintLayout&gt
   ```

   Choose as many answers as you see fit.  
   `TextView A`appears vertically stacked on top of`TextView B`.  
   The starting edge of`TextView A`is aligned to the starting edge of the parent view.  
   The starting edge of`TextView B`is aligned to the starting edge of the parent view.  
   `TextView B`is horizontally and vertically centered within the parent.  
   The tops of`TextView A`and`TextView B`are aligned to top of the parent view.  
   The width of`TextView A`matches the width of the parent`ConstraintLayout`.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.