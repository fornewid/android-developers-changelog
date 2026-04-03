---
title: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-4/android-basics-kotlin-unit-3-pathway-4
url: https://developer.android.com/courses/quizzes/android-basics-kotlin-unit-3-pathway-4/android-basics-kotlin-unit-3-pathway-4
source: md.txt
---

# Advanced navigation app examples

# Advanced navigation app examples

<br />

Return to pathway  
1.

   ## True or False: You can use the same ViewModel for multiple Activities or Fragments to share data.

   True  
   False  
2.

   ## What is the correct way to access the shared view model using the Kotin property delegate approach?

   `val viewModel: OrderViewModel by viewModels()`  
   `val viewModel: OrderViewModel by activityViewModels()`  
   `val viewModel: OrderViewModel by sharedViewModels()`  
   `val viewModel: OrderViewModel by fragmentViewModels()`  
3.

   ## Fill-in-the-blanks

   Enter one or more words to complete the sentence.  
   Use a LiveData ___ to return a different LiveData instance based on the value of another instance.  
4.

   ## How can the`apply`function in Kotlin be used to configure an object?

   It can directly apply the object.  
   It can apply a set of assignments to the object.  
   It can apply new instances from the object.  
   It is not recommended to use`apply`to configure an object.  
5.

   ## Using a data binding layout expression, what's the correct syntax for adding an attribute to the button in this layout in order to bind a click listener to it?

   ```kotlin
   &ltButton
       android:id="@+id/next_button"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="@string/next" /&gt
   ```
   `android:onClick="@{detailFragment.next()}"`  
   `android:onClick="@{(Int) -> detailFragment()}"`  
   `android:click="@{() -> detailFragment.next()}"`  
   `android:onClick="@{() -> detailFragment.next()}"`  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.