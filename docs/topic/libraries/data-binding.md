---
title: https://developer.android.com/topic/libraries/data-binding
url: https://developer.android.com/topic/libraries/data-binding
source: md.txt
---

# Data Binding Library

# Data Binding LibraryPart of[Android Jetpack](https://developer.android.com/jetpack).

The Data Binding Library is a support library that allows you to bind UI components in your layouts to data sources in your app using a declarative format rather than programmatically.

Layouts are often defined in activities with code that calls UI framework methods. For example, the code below calls[findViewById()](https://developer.android.com/reference/android/app/Activity#findViewById(int))to find a[TextView](https://developer.android.com/reference/android/widget/TextView)widget and bind it to the`userName`property of the`viewModel`variable:  

### Kotlin

```kotlin
findViewById<TextView>(R.id.sample_text).apply {
    text = viewModel.userName
}
```

### Java

```java
TextView textView = findViewById(R.id.sample_text);
textView.setText(viewModel.getUserName());
```

The following example shows how to use the Data Binding Library to assign text to the widget directly in the layout file. This removes the need to call any of the Java code shown above. Note the use of`@{}`syntax in the assignment expression:  

    <TextView
        android:text="@{viewmodel.userName}" />

Binding components in the layout file lets you remove many UI framework calls in your activities, making them simpler and easier to maintain. This can also improve your app's performance and help prevent memory leaks and null pointer exceptions.
| **Note:** In many cases,[view binding](https://developer.android.com/topic/libraries/view-binding)can provide the same benefits as data binding with simpler implementation and better performance. If you are using data binding primarily to replace`findViewById()`calls, consider using view binding instead.

## Using the Data Binding Library

Use the following pages to learn how to use the Data Binding Library in your Android apps.

[**Get started**](https://developer.android.com/topic/libraries/data-binding/start)
:   Learn how to get your development environment ready to work with the Data Binding Library, including support for data binding code in Android Studio.

[**Layouts and binding expressions**](https://developer.android.com/topic/libraries/data-binding/expressions)
The expression language allows you to write expressions that connect variables to the views in the layout. The Data Binding Library automatically generates the classes required to bind the views in the layout with your data objects. The library provides features such as imports, variables, and includes that you can use in your layouts.

<br />

<br />

These features of the library coexist seamlessly with your existing layouts. For example, the binding variables that can be used in expressions are defined inside a`data`element that is a sibling of the UI layout's root element. Both elements are wrapped in a`layout`tag, as shown in the following example:

<br />

    <layout xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:app="http://schemas.android.com/apk/res-auto">
        <data>
            <variable
                name="viewmodel"
                type="com.myapp.data.ViewModel" />
        </data>
        <ConstraintLayout... /> <!-- UI layout's root element -->
    </layout>

<br />

<br />

[**Work with observable data objects**](https://developer.android.com/topic/libraries/data-binding/observability)
:   The Data Binding Library provides classes and methods to easily observe data for changes. You don't have to worry about refreshing the UI when the underlying data source changes. You can make your variables or their properties observable. The library allows you to make objects, fields, or collections observable.

[**Generated binding classes**](https://developer.android.com/topic/libraries/data-binding/generated-binding)
:   The Data Binding Library generates binding classes that are used to access the layout's variables and views. This page shows you how to use and customize generated binding classes.

[**Binding adapters**](https://developer.android.com/topic/libraries/data-binding/binding-adapters)
: For every layout expression, there is a binding adapter that makes the framework calls required to set the corresponding properties or listeners. For example, the binding adapter can take care of calling the`setText()`method to set the text property or call the`setOnClickListener()`method to add a listener to the click event. The most common binding adapters, such as the adapters for the`android:text`property used in the examples in this page, are available for you to use in the`android.databinding.adapters`package. For a list of the common binding adapters, see[adapters](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters). You can also create custom adapters, as shown in the following example:  

### Kotlin

```kotlin
@BindingAdapter("app:goneUnless")
fun goneUnless(view: View, visible: Boolean) {
    view.visibility = if (visible) View.VISIBLE else View.GONE
}
```

### Java

```java
@BindingAdapter("app:goneUnless")
public static void goneUnless(View view, Boolean visible) {
    view.visibility = visible ? View.VISIBLE : View.GONE;
}
```

[**Bind layout views to Architecture Components**](https://developer.android.com/topic/libraries/data-binding/architecture)
:   The Android Support Library includes the[Architecture Components](https://developer.android.com/topic/libraries/architecture), which you can use to design robust, testable, and maintainable apps. You can use the Architecture Components with the Data Binding Library to further simplify the development of your UI.

[**Two-way data binding**](https://developer.android.com/topic/libraries/data-binding/two-way)
:   The Data Binding Library supports two-way data binding. The notation used for this type of binding supports the ability to receive data changes to a property and listen to user updates to that property at the same time.

## Additional resources

To learn more about data binding, consult the following additional resources.

### Samples

- [Android Data Binding Library samples](https://github.com/android/databinding-samples)

### Codelabs

- [Android Data Binding codelab](https://codelabs.developers.google.com/codelabs/android-databinding)

### Blog posts

- [Android Data Binding Library --- From Observable Fields to LiveData in two steps](https://medium.com/androiddevelopers/android-data-binding-library-from-observable-fields-to-livedata-in-two-steps-690a384218f2)
- [Data Binding --- Lessons Learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Binding adapters {:#binding-adapters}](https://developer.android.com/topic/libraries/data-binding/binding-adapters)
- [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
- [Generated binding classes {: #binding-classes}](https://developer.android.com/topic/libraries/data-binding/generated-binding)