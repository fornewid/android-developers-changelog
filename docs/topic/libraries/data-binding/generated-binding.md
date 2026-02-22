---
title: https://developer.android.com/topic/libraries/data-binding/generated-binding
url: https://developer.android.com/topic/libraries/data-binding/generated-binding
source: md.txt
---

# Generated binding classes

The Data Binding Library generates binding classes you can use to access the layout's variables and views. This documentation shows how to create and customize generated binding classes.

The generated binding class links the layout variables with the views within the layout. You can[customize](https://developer.android.com/topic/libraries/data-binding/generated-binding#custom_binding_class_names)the name and package of the binding. All generated binding classes inherit from the[`ViewDataBinding`](https://developer.android.com/reference/androidx/databinding/ViewDataBinding)class.

A binding class is generated for each layout file. By default, the name of the class is the name of the layout file converted to Pascal case with the*Binding* suffix added to it. So, for example, if the layout filename is`activity_main.xml`, the corresponding generated class is`ActivityMainBinding`. This class holds all the bindings from the layout properties to the layout's views and knows how to assign values for the binding expressions.

## Create a binding object

The binding object is created immediately after inflating the layout to make sure the view hierarchy isn't modified before it binds to the views with expressions within the layout. The most common method to bind the object to a layout is to use the static methods on the binding class. You can inflate the view hierarchy and bind the object to it by using the`inflate()`method of the binding class, as shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    val binding: MyLayoutBinding = MyLayoutBinding.inflate(layoutInflater)

    setContentView(binding.root)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    MyLayoutBinding binding = MyLayoutBinding.inflate(getLayoutInflater());

    setContentView(binding.root);
}
```

There is an alternate version of the`inflate()`method that takes a[`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup)object in addition to the[`LayoutInflater`](https://developer.android.com/reference/android/view/LayoutInflater)object , as shown in the following example:  

### Kotlin

```kotlin
val binding: MyLayoutBinding = MyLayoutBinding.inflate(getLayoutInflater(), viewGroup, false)
```

### Java

```java
MyLayoutBinding binding = MyLayoutBinding.inflate(getLayoutInflater(), viewGroup, false);
```

If the layout is inflated using a different mechanism, you can bind it separately, as follows:  

### Kotlin

```kotlin
val binding: MyLayoutBinding = MyLayoutBinding.bind(viewRoot)
```

### Java

```java
MyLayoutBinding binding = MyLayoutBinding.bind(viewRoot);
```

Sometimes you don't know the binding type in advance. In such cases, you can create the binding using the[`DataBindingUtil`](https://developer.android.com/reference/androidx/databinding/DataBindingUtil)class, as demonstrated in the following code snippet:  

### Kotlin

```kotlin
val viewRoot = LayoutInflater.from(this).inflate(layoutId, parent, attachToParent)
val binding: ViewDataBinding? = DataBindingUtil.bind(viewRoot)
```

### Java

```java
View viewRoot = LayoutInflater.from(this).inflate(layoutId, parent, attachToParent);
ViewDataBinding binding = DataBindingUtil.bind(viewRoot);
```

If you are using data binding items inside a[`Fragment`](https://developer.android.com/reference/android/app/Fragment),[`ListView`](https://developer.android.com/reference/android/widget/ListView), or[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)adapter, you might prefer to use the[`inflate()`](https://developer.android.com/reference/androidx/databinding/DataBindingUtil#inflate(android.view.LayoutInflater,%20int,%20android.view.ViewGroup,%20boolean,%20android.databinding.DataBindingComponent))methods of the bindings classes or the[`DataBindingUtil`](https://developer.android.com/reference/androidx/databinding/DataBindingUtil)class, as shown in the following code example:  

### Kotlin

```kotlin
val listItemBinding = ListItemBinding.inflate(layoutInflater, viewGroup, false)
// or
val listItemBinding = DataBindingUtil.inflate(layoutInflater, R.layout.list_item, viewGroup, false)
```

### Java

```java
ListItemBinding binding = ListItemBinding.inflate(layoutInflater, viewGroup, false);
// or
ListItemBinding binding = DataBindingUtil.inflate(layoutInflater, R.layout.list_item, viewGroup, false);
```

## Views with IDs

The Data Binding Library creates an immutable field in the binding class for each view that has an ID in the layout. For example, the Data Binding Library creates the`firstName`and`lastName`fields of type`TextView`from the following layout:  

    <layout xmlns:android="http://schemas.android.com/apk/res/android">
       <data>
           <variable name="user" type="com.example.User"/>
       </data>
       <LinearLayout
           android:orientation="vertical"
           android:layout_width="match_parent"
           android:layout_height="match_parent">
           <TextView android:layout_width="wrap_content"
               android:layout_height="wrap_content"
               android:text="@{user.firstName}"
       android:id="@+id/firstName"/>
           <TextView android:layout_width="wrap_content"
               android:layout_height="wrap_content"
               android:text="@{user.lastName}"
      android:id="@+id/lastName"/>
       </LinearLayout>
    </layout>

The library extracts the views, including the IDs, from the view hierarchy in a single pass. This mechanism can be faster than calling the[`findViewById()`](https://developer.android.com/reference/android/app/Activity#findViewById(int))method for every view in the layout.

IDs aren't as necessary as they are without data binding, but there are still some instances where access to views is necessary from code.

## Variables

The Data Binding Library generates accessor methods for each variable declared in the layout. For example, the following layout generates setter and getter methods in the binding class for the`user`,`image`, and`note`variables:  

    <data>
       <import type="android.graphics.drawable.Drawable"/>
       <variable name="user" type="com.example.User"/>
       <variable name="image" type="Drawable"/>
       <variable name="note" type="String"/>
    </data>

## ViewStubs

Unlike normal views,[`ViewStub`](https://developer.android.com/reference/android/view/ViewStub)objects start as invisible views. When they are made visible or are explicitly inflated, they replace themselves in the layout by inflating another layout.

Because the`ViewStub`disappears from the view hierarchy, the view in the binding object must also disappear to let it be claimed by garbage collection. Because the views are final, a[`ViewStubProxy`](https://developer.android.com/reference/androidx/databinding/ViewStubProxy)object takes the place of the`ViewStub`in the generated binding class, giving you access to the`ViewStub`when it exists and access to the inflated view hierarchy when the`ViewStub`is inflated.

When inflating another layout, a binding must establish for the new layout. Therefore, the`ViewStubProxy`must listen to the`ViewStub`[`OnInflateListener`](https://developer.android.com/reference/android/view/ViewStub.OnInflateListener)and establish the binding when required. Since only one listener can exist at a time, the`ViewStubProxy`lets you set an`OnInflateListener`, which it calls after establishing the binding.

## Immediate binding

When a variable or observable object changes, the binding is scheduled to change before the next frame. There are times, however, when binding must be executed immediately. To force execution, use the[`executePendingBindings()`](https://developer.android.com/reference/android/databinding/ViewDataBinding#executependingbindings)method.

## Dynamic variables

At times, the specific binding class is unknown. For example, a[`RecyclerView.Adapter`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter)operating against arbitrary layouts doesn't know the specific binding class. It must assign the binding value during the call to the[`onBindViewHolder()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onBindViewHolder(VH,int))method.

In the following example, all layouts that the`RecyclerView`binds to have an`item`variable. The`BindingHolder`object has a`getBinding()`method returning the[`ViewDataBinding`](https://developer.android.com/reference/androidx/databinding/ViewDataBinding)base class.  

### Kotlin

```kotlin
override fun onBindViewHolder(holder: BindingHolder, position: Int) {
    item: T = items.get(position)
    holder.binding.setVariable(BR.item, item);
    holder.binding.executePendingBindings();
}
```

### Java

```java
public void onBindViewHolder(BindingHolder holder, int position) {
    final T item = items.get(position);
    holder.getBinding().setVariable(BR.item, item);
    holder.getBinding().executePendingBindings();
}
```
| **Note:** The Data Binding Library generates a class named`BR`in the module package that contains the IDs of the resources used for data binding. In the preceding example, the library automatically generates the`BR.item`variable.

## Background thread

You can change your data model in a background thread as long as it isn't a collection. Data binding localizes each variable or field during evaluation to avoid any concurrency issues.

## Custom binding class names

By default, a binding class is generated based on the name of the layout file, starting with an uppercase letter, removing underscores ( _ ), capitalizing the following letter, and suffixing the word*Binding* . For example, the layout file`contact_item.xml`generates the`ContactItemBinding`class. The class is placed in a`databinding`package under the module package. For example, if the module package is`com.example.my.app`, then the binding class is placed in the`com.example.my.app.databinding`package.

Binding classes can be renamed or placed in different packages by adjusting the`class`attribute of the`data`element. For example, the following layout generates the`ContactItem`binding class in the`databinding`package in the current module:  

    <data class="ContactItem">
        ...
    </data>

You can generate the binding class in a different package by prefixing the class name with a period. The following example generates the binding class in the module package:  

    <data class=".ContactItem">
        ...
    </data>

You can also use the full package name where you want the binding class to be generated. The following example creates the`ContactItem`binding class in the`com.example`package:  

    <data class="com.example.ContactItem">
        ...
    </data>

## Additional resources

To learn more about data binding, see the following additional resources.

- [Android Data Binding Library samples](https://github.com/android/databinding-samples)
- [Data Binding in Android](https://codelabs.developers.google.com/codelabs/android-databinding)
- [Data Binding --- lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
- [Data Binding Library](https://developer.android.com/topic/libraries/data-binding)
- [View binding](https://developer.android.com/topic/libraries/view-binding)