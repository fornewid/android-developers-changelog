---
title: https://developer.android.com/courses/quizzes/android-development-with-kotlin-10/android-development-with-kotlin-10
url: https://developer.android.com/courses/quizzes/android-development-with-kotlin-10/android-development-with-kotlin-10
source: md.txt
---

# Lesson 10: Advanced RecyclerView use cases

# Lesson 10: Advanced RecyclerView use cases

<br />

Return to pathway  
1.

   ## How does`RecyclerView`display items? Select all that apply.

   Choose as many answers as you see fit.  
   Displays items in a list or a grid.  
   Scrolls vertically or horizontally.  
   Scrolls diagonally on larger devices such as tablets.  
   Allows custom layouts when a list or a grid is not enough for the use case.  
2.

   ## What are the benefits of using`RecyclerView`? Select all that apply.

   Choose as many answers as you see fit.  
   Efficiently displays large lists.  
   Automatically updates the data.  
   Minimizes the need for refreshes when an item is updated, deleted, or added to the list.  
   Reuses the view when scrolling to automatically display the next item on screen.  
3.

   ## What are some of the reasons for using adapters? Select all that apply.

   Choose as many answers as you see fit.  
   Separation of concerns makes it easier to change and test code.  
   `RecyclerView`is agnostic to the data that is being displayed.  
   Data processing layers do not have to concern themselves with how data will be displayed.  
   The app will run faster.  
4.

   ## Which of the following are true of`ViewHolder`? Select all that apply.

   Choose as many answers as you see fit.  
   The`ViewHolder`layout is defined in XML layout files.  
   There is one`ViewHolder`for each unit of data in the dataset.  
   You can have more than one`ViewHolder`in a`RecyclerView`.  
   The`Adapter`binds data to the`ViewHolder`.  
5.

   ## Which of the following are necessary to use`DiffUtil`? Select all that apply.

   Choose as many answers as you see fit.  
   Extend the`ItemCallBack`class.  
   Override`areItemsTheSame()`.  
   Override`areContentsTheSame()`.  
   Use data binding to track the differences between items.  
6.

   ## Which of the following are true about binding adapters?

   Choose as many answers as you see fit.  
   A binding`Adapter`is a function annotated with`@BindingAdapter`.  
   Using a binding`Adapter`allows you to separate data formatting from the view holder.  
   You must use a`RecyclerViewAdapter`if you want to use binding adapters.  
   Binding adapters are a good solution when you need to transform complex data.  
7.

   ## Which of the following are layout managers provided by Android? Select all that apply.

   Choose as many answers as you see fit.  
   `LinearLayoutManager`  
   `GridLayoutManager`  
   `CircularLayoutManager`  
   `StaggeredGridLayoutManager`  
8.

   ## What is a span in`GridLayoutManager`?

   The size of a grid created by`GridLayoutManager`.  
   The width of a column in the grid.  
   The dimensions of an item in a grid.  
   The number of columns in a grid that has a vertical orientation.  
9.

   ## Where do you add the`android:onClick`attribute to make items in a`RecyclerView`respond to clicks? Select all that apply.

   Choose as many answers as you see fit.  
   In the layout file that displays the`RecyclerView`, add it to`<androidx.recyclerview.widget.RecyclerView>`  
   Add it to the layout file for an item in the row. If you want the entire item to be clickable, add it to the parent view that contains the items in the row.  
   Add it to the layout file for an item in the row. If you want a single`TextView`in the item to be clickable, add it to the`<TextView>`.  
   Always add it to the layout file for the`MainActivity`.  
10.

    ## Which of the following statements is true about`ViewHolder`?

    An`Adapter`can use multiple`ViewHolder`classes to hold headers and various types of data.  
    You can have exactly one view holder for data, and one view holder for a header.  
    A`RecyclerView`supports multiple types of headers, but the data has to be uniform.  
    When adding a header, you subclass`RecyclerView`to insert the header at the correct position.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.