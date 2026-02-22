---
title: https://developer.android.com/topic/libraries/data-binding/expressions
url: https://developer.android.com/topic/libraries/data-binding/expressions
source: md.txt
---

# Layouts and binding expressions

The expression language lets you write expressions that handle events dispatched by views. The Data Binding Library automatically generates the classes required to bind the views in the layout with your data objects.

Data binding layout files are slightly different and start with a root tag of`layout`, followed by a`data`element and a`view`root element. This view element is what your root is in a non-binding layout file. The following code shows a sample layout file:  

    <?xml version="1.0" encoding="utf-8"?>
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
               android:text="@{user.firstName}"/>
           <TextView android:layout_width="wrap_content"
               android:layout_height="wrap_content"
               android:text="@{user.lastName}"/>
       </LinearLayout>
    </layout>

The`user`variable within`data`describes a property that can be used within this layout:  

    <variable name="user" type="com.example.User" />

Expressions within the layout are written in the attribute properties using the`@{}`syntax. In the following example, the[`TextView`](https://developer.android.com/reference/android/widget/TextView)text is set to the`firstName`property of the`user`variable:  

    <TextView android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:text="@{user.firstName}" />

| **Note:** Keep layout expressions small and simple, as they can't be unit tested and have limited IDE support. To simplify layout expressions, you can use custom[binding adapters](https://developer.android.com/topic/libraries/data-binding/binding-adapters).

## Data objects

Suppose you have a plain object to describe the`User`entity:  

### Kotlin

```kotlin
data class User(val firstName: String, val lastName: String)
```

### Java

```java
public class User {
  public final String firstName;
  public final String lastName;
  public User(String firstName, String lastName) {
      this.firstName = firstName;
      this.lastName = lastName;
  }
}
```

This type of object has data that never changes. It's common in apps to have data that is read once and never changes thereafter. It's also possible to use an object that follows a set of conventions, such as using accessor methods in the Java programming language, as shown in the following example:  

### Kotlin

```kotlin
// Not applicable in Kotlin.
data class User(val firstName: String, val lastName: String)
```

### Java

```java
public class User {
  private final String firstName;
  private final String lastName;
  public User(String firstName, String lastName) {
      this.firstName = firstName;
      this.lastName = lastName;
  }
  public String getFirstName() {
      return this.firstName;
  }
  public String getLastName() {
      return this.lastName;
  }
}
```

From the perspective of data binding, these two classes are equivalent. The expression`@{user.firstName}`used for the[`android:text`](https://developer.android.com/reference/android/widget/TextView#attr_android:text)attribute accesses the`firstName`field in the former class and the`getFirstName()`method in the latter class. It is also resolved to`firstName()`, if that method exists.

## Binding data

A binding class is generated for each layout file. By default, the name of the class is based on the name of the layout file, converted to Pascal case, with the*Binding* suffix added to it. For example, the preceding layout filename is`activity_main.xml`, so the corresponding generated binding class is`ActivityMainBinding`.

This class holds all the bindings from the layout properties---for example, the`user`variable---to the layout's views and knows how to assign values for the binding expressions. We recommend creating the bindings while inflating the layout, as shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    val binding: ActivityMainBinding = DataBindingUtil.setContentView(
            this, R.layout.activity_main)

    binding.user = User("Test", "User")
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);
   ActivityMainBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
   User user = new User("Test", "User");
   binding.setUser(user);
}
```

At runtime, the app displays the**Test** user in the UI. Alternatively, you can get the view using a[`LayoutInflater`](https://developer.android.com/reference/android/view/LayoutInflater), as shown in the following example:  

### Kotlin

```kotlin
val binding: ActivityMainBinding = ActivityMainBinding.inflate(getLayoutInflater())
```

### Java

```java
ActivityMainBinding binding = ActivityMainBinding.inflate(getLayoutInflater());
```

If you are using data binding items inside a[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment),[`ListView`](https://developer.android.com/reference/android/widget/ListView), or[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)adapter, you might prefer to use the[`inflate()`](https://developer.android.com/reference/androidx/databinding/DataBindingUtil#inflate(android.view.LayoutInflater,%20int,%20android.view.ViewGroup,%20boolean,%20android.databinding.DataBindingComponent))methods of the bindings classes or the[`DataBindingUtil`](https://developer.android.com/reference/androidx/databinding/DataBindingUtil)class, as shown in the following code example:  

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

## Expression language

### Common features

The expression language looks a lot like expressions found in managed code. You can use the following operators and keywords in the expression language:

- Mathematical:`+ - / * %`
- String concatenation:`+`
- Logical:`&& ||`
- Binary:`& | ^`
- Unary:`+ - ! ~`
- Shift:`>> >>> <<`
- Comparison:`== > < >= <=`(the`<`needs to be escaped as`&lt;`)
- `instanceof`
- Grouping:`()`
- Literals, such as character, String, numeric,`null`
- Cast
- Method calls
- Field access
- Array access:`[]`
- Ternary operator:`?:`

Here are some examples:  

    android:text="@{String.valueOf(index + 1)}"
    android:visibility="@{age > 13 ? View.GONE : View.VISIBLE}"
    android:transitionName='@{"image_" + id}'

### Missing operations

The following operations are missing from the expression syntax that you can use in managed code:

- `this`
- `super`
- `new`
- Explicit generic invocation

### Null coalescing operator

The null coalescing operator (`??`) chooses the left operand if it isn't`null`or the right if the former is`null`:  

    android:text="@{user.displayName ?? user.lastName}"

This is functionally equivalent to the following:  

    android:text="@{user.displayName != null ? user.displayName : user.lastName}"

### Property references

An expression can reference a property in a class by using the following format, which is the same for fields, getters, and[`ObservableField`](https://developer.android.com/reference/androidx/databinding/ObservableField)objects:  

    android:text="@{user.lastName}"

### Avoid null pointer exceptions

Generated data binding code automatically checks for`null`values and avoids null pointer exceptions. For example, in the expression`@{user.name}`, if`user`is null,`user.name`is assigned its default value of`null`. If you reference`user.age`, where age is of type`int`, then data binding uses the default value of`0`.

### View references

An expression can reference other views in the layout by ID, using the following syntax:  

    android:text="@{exampleText.text}"

| **Note:** The binding class converts IDs to camel case.

In the following example, the`TextView`view references an`EditText`view in the same layout:  

    <EditText
        android:id="@+id/example_text"
        android:layout_height="wrap_content"
        android:layout_width="match_parent"/>
    <TextView
        android:id="@+id/example_output"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@{exampleText.text}"/>

### Collections

You can access common collections, such as arrays, lists, sparse lists, and maps, using the`[]`operator for convenience.  

    <data>
        <import type="android.util.SparseArray"/>
        <import type="java.util.Map"/>
        <import type="java.util.List"/>
        <variable name="list" type="List&lt;String>"/>
        <variable name="sparse" type="SparseArray&lt;String>"/>
        <variable name="map" type="Map&lt;String, String>"/>
        <variable name="index" type="int"/>
        <variable name="key" type="String"/>
    </data>
    ...
    android:text="@{list[index]}"
    ...
    android:text="@{sparse[index]}"
    ...
    android:text="@{map[key]}"

| **Note:** For the XML to be syntactically correct, escape the`<`characters. For example: instead of`List<String>`, write`List&lt;String>`.

You can also refer to a value in the map using the`object.key`notation. For example, you can replace`@{map[key]}`in the preceding example with`@{map.key}`.

### String literals

You can use single quotes to surround the attribute value, which lets you use double quotes in the expression, as shown in the following example:  

    android:text='@{map["firstName"]}'

You can also use double quotes to surround the attribute value. When doing so, string literals must be surrounded with backticks`````, as shown here:  

    android:text="@{map[`firstName`]}"

### Resources

An expression can reference app resources with the following syntax:  

    android:padding="@{large? @dimen/largePadding : @dimen/smallPadding}"

You can evaluate format strings and plurals by providing parameters:  

    android:text="@{@string/nameFormat(firstName, lastName)}"
    android:text="@{@plurals/banana(bananaCount)}"

You can pass[property references](https://developer.android.com/topic/libraries/data-binding/expressions#property_reference)and[view references](https://developer.android.com/topic/libraries/data-binding/expressions#view_references)as resource parameters:  

    android:text="@{@string/example_resource(user.lastName, exampleText.text)}"

When a plural takes multiple parameters, pass all parameters:  


      Have an orange
      Have %d oranges

    android:text="@{@plurals/orange(orangeCount, orangeCount)}"

Some resources require explicit type evaluation, as shown in the following table:

|        Type         | Normal reference | Expression reference |
|---------------------|------------------|----------------------|
| `String[]`          | `@array`         | `@stringArray`       |
| `int[]`             | `@array`         | `@intArray`          |
| `TypedArray`        | `@array`         | `@typedArray`        |
| `Animator`          | `@animator`      | `@animator`          |
| `StateListAnimator` | `@animator`      | `@stateListAnimator` |
| `color int`         | `@color`         | `@color`             |
| `ColorStateList`    | `@color`         | `@colorStateList`    |

## Event handling

Data binding lets you write expression handling events that are dispatched from the views---for example, the[`onClick()`](https://developer.android.com/reference/android/view/View.OnClickListener#onClick(android.view.View))method. Event attribute names are determined by the name of the listener method, with a few exceptions. For example,[`View.OnClickListener`](https://developer.android.com/reference/android/view/View.OnClickListener)has a method`onClick()`, so the attribute for this event is`android:onClick`.

There are some specialized event handlers for the click event that need an attribute other than`android:onClick`to avoid a conflict. You can use the following attributes to avoid these type of conflicts:

|                                         Class                                         |                                                                                    Listener setter                                                                                    |        Attribute        |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| [`SearchView`](https://developer.android.com/reference/android/widget/SearchView)     | [`setOnSearchClickListener(View.OnClickListener)`](https://developer.android.com/reference/android/widget/SearchView#setOnSearchClickListener(android.view.View.OnClickListener))     | `android:onSearchClick` |
| [`ZoomControls`](https://developer.android.com/reference/android/widget/ZoomControls) | [`setOnZoomInClickListener(View.OnClickListener)`](https://developer.android.com/reference/android/widget/ZoomControls#setOnZoomInClickListener(android.view.View.OnClickListener))   | `android:onZoomIn`      |
| [`ZoomControls`](https://developer.android.com/reference/android/widget/ZoomControls) | [`setOnZoomOutClickListener(View.OnClickListener)`](https://developer.android.com/reference/android/widget/ZoomControls#setOnZoomOutClickListener(android.view.View.OnClickListener)) | `android:onZoomOut`     |

You can use these two mechanisms, described in detail in the sections that follow, to handle an event:

- [Method references](https://developer.android.com/topic/libraries/data-binding/expressions#method_references): in your expressions, you can reference methods that conform to the signature of the listener method. When an expression evaluates to a method reference, data binding wraps the method reference and owner object in a listener and sets that listener on the target view. If the expression evaluates to`null`, data binding doesn't create a listener and sets a`null`listener instead.
- [Listener bindings](https://developer.android.com/topic/libraries/data-binding/expressions#listener_bindings): these are lambda expressions that are evaluated when the event happens. Data binding always creates a listener, which it sets on the view. When the event is dispatched, the listener evaluates the lambda expression.

### Method references

You can bind events to handler methods directly, similar to the way you can assign[`android:onClick`](https://developer.android.com/reference/android/view/View#attr_android:onClick)to a method in an activity. One advantage compared to the[`View`](https://developer.android.com/reference/android/view/View)`onClick`attribute is that the expression is processed at compile time. So, if the method doesn't exist or its signature is incorrect, you receive a compile time error.

The major difference between method references and listener bindings is that the actual listener implementation is created when the data is bound, not when the event is triggered. If you prefer to evaluate the expression when the event happens, use[listener bindings](https://developer.android.com/topic/libraries/data-binding/expressions#listener_bindings).

To assign an event to its handler, use a normal binding expression, with the value being the method name to call. For example, consider the following example layout data object:  

### Kotlin

```kotlin
class MyHandlers {
    fun onClickFriend(view: View) { ... }
}
```

### Java

```java
public class MyHandlers {
    public void onClickFriend(View view) { ... }
}
```

The binding expression can assign the click listener for a view to the`onClickFriend()`method, as follows:  

    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android">
       <data>
           <variable name="handlers" type="com.example.MyHandlers"/>
           <variable name="user" type="com.example.User"/>
       </data>
       <LinearLayout
           android:orientation="vertical"
           android:layout_width="match_parent"
           android:layout_height="match_parent">
           <TextView android:layout_width="wrap_content"
               android:layout_height="wrap_content"
               android:text="@{user.firstName}"
               android:onClick="@{handlers::onClickFriend}"/>
       </LinearLayout>
    </layout>

| **Note:** The signature of the method in the expression must exactly match the signature of the method in the listener object.

### Listener bindings

Listener bindings are binding expressions that run when an event happens. They are similar to method references, but they let you run arbitrary data binding expressions. This feature is available with Android Gradle Plugin for Gradle version 2.0 and later.

In method references, the parameters of the method must match the parameters of the event listener. In listener bindings, only your return value must match the expected return value of the listener, unless it is expecting`void`. For example, consider the following presenter class that has an`onSaveClick()`method:  

### Kotlin

```kotlin
class Presenter {
    fun onSaveClick(task: Task){}
}
```

### Java

```java
public class Presenter {
    public void onSaveClick(Task task){}
}
```

You can bind the click event to the`onSaveClick()`method as follows:  

    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android">
        <data>
            <variable name="task" type="com.android.example.Task" />
            <variable name="presenter" type="com.android.example.Presenter" />
        </data>
        <LinearLayout android:layout_width="match_parent" android:layout_height="match_parent">
            <Button android:layout_width="wrap_content" android:layout_height="wrap_content"
            android:onClick="@{() -> presenter.onSaveClick(task)}" />
        </LinearLayout>
    </layout>

When a callback is used in an expression, data binding automatically creates the necessary listener and registers it for the event. When the view fires the event, data binding evaluates the given expression. As with regular binding expressions, you get the null and thread safety of data binding while these listener expressions are being evaluated.

In the preceding example, the`view`parameter that is passed to`onClick(View)`isn't defined. Listener bindings provide two choices for listener parameters: you can ignore all parameters to the method or name all of them. If you prefer to name the parameters, you can use them in your expression. For example, you can write the preceding expression as follows:  

    android:onClick="@{(view) -> presenter.onSaveClick(task)}"

If you want to use the parameter in the expression, you can do that as follows:  

### Kotlin

```kotlin
class Presenter {
    fun onSaveClick(view: View, task: Task){}
}
```

### Java

```java
public class Presenter {
    public void onSaveClick(View view, Task task){}
}
```  

    android:onClick="@{(theView) -> presenter.onSaveClick(theView, task)}"

And you can use a lambda expression with more than one parameter:  

### Kotlin

```kotlin
class Presenter {
    fun onCompletedChanged(task: Task, completed: Boolean){}
}
```

### Java

```java
public class Presenter {
    public void onCompletedChanged(Task task, boolean completed){}
}
```  

    <CheckBox android:layout_width="wrap_content" android:layout_height="wrap_content"
          android:onCheckedChanged="@{(cb, isChecked) -> presenter.completeChanged(task, isChecked)}" />

If the event you are listening to returns a value whose type isn't`void`, your expressions must return the same type of value as well. For example, if you want to listen for the touch \& hold (long click) event, your expression must return a boolean.  

### Kotlin

```kotlin
class Presenter {
    fun onLongClick(view: View, task: Task): Boolean { }
}
```

### Java

```java
public class Presenter {
    public boolean onLongClick(View view, Task task) { }
}
```  

    android:onLongClick="@{(theView) -> presenter.onLongClick(theView, task)}"

If the expression can't be evaluated due to`null`objects, data binding returns the default value for that type, such as`null`for reference types,`0`for`int`, or`false`for`boolean`.

If you need to use an expression with a predicate---for example, a ternary---you can use`void`as a symbol:  

    android:onClick="@{(v) -> v.isVisible() ? doSomething() : void}"

#### Avoid complex listeners

Listener expressions are powerful and can make your code easier to read. On the other hand, listeners containing complex expressions make your layouts*harder*to read and maintain. Keep your expressions as simple as passing available data from your UI to your callback method. Implement any business logic inside the callback method that you invoke from the listener expression.

## Imports, variables, and includes

The Data Binding Library provides features such as imports, variables, and includes. Imports make easy-to-reference classes inside your layout files. Variables let you describe a property that can be used in binding expressions. Includes let you reuse complex layouts across your app.

### Imports

Imports let you reference classes inside your layout file, like in managed code. You can use zero or more`import`elements inside the`data`element. The following code example imports the`View`class to the layout file:  

    <data>
        <import type="android.view.View"/>
    </data>

Importing the`View`class lets you reference it from your binding expressions. The following example shows how to reference the[`VISIBLE`](https://developer.android.com/reference/android/view/View#VISIBLE)and[`GONE`](https://developer.android.com/reference/android/view/View#GONE)constants of the`View`class:  

    <TextView
       android:text="@{user.lastName}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:visibility="@{user.isAdult ? View.VISIBLE : View.GONE}"/>

#### Type aliases

When there are class name conflicts, you can rename one of the classes to an alias. The following example renames the`View`class in the`com.example.real.estate`package to`Vista`:  

    <import type="android.view.View"/>
    <import type="com.example.real.estate.View"
            alias="Vista"/>

You can then use`Vista`to reference`com.example.real.estate.View`and`View`to reference`android.view.View`within the layout file.

#### Import other classes

You can use imported types as type references in variables and expressions. The following example shows`User`and`List`used as the type of a variable:  

    <data>
        <import type="com.example.User"/>
        <import type="java.util.List"/>
        <variable name="user" type="User"/>
        <variable name="userList" type="List&lt;User>"/>
    </data>

| **Caution:** Android Studio doesn't yet handle imports, so the autocomplete for imported variables might not work in your IDE. Your app still compiles, and you can work around the IDE issue by using fully qualified names in your variable definitions.

You can use the imported types to cast part of an expression. The following example casts the`connection`property to a type of`User`:  

    <TextView
       android:text="@{((User)(user.connection)).lastName}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>

You can also use imported types when referencing static fields and methods in expressions. The following code imports the`MyStringUtils`class and references its`capitalize`method:  

    <data>
        <import type="com.example.MyStringUtils"/>
        <variable name="user" type="com.example.User"/>
    </data>
    ...
    <TextView
       android:text="@{MyStringUtils.capitalize(user.lastName)}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>

Just as in managed code,`java.lang.*`is imported automatically.

### Variables

You can use multiple`variable`elements inside the`data`element. Each`variable`element describes a property that can be set on the layout to be used in binding expressions within the layout file. The following example declares the`user`,`image`, and`note`variables:  

    <data>
        <import type="android.graphics.drawable.Drawable"/>
        <variable name="user" type="com.example.User"/>
        <variable name="image" type="Drawable"/>
        <variable name="note" type="String"/>
    </data>

The variable types are inspected at compile time, so if a variable implements[`Observable`](https://developer.android.com/reference/androidx/databinding/Observable)or is an[observable collection](https://developer.android.com/topic/libraries/data-binding/observability#observable_Collections), that must be reflected in the type. If the variable is a base class or interface that doesn't implement the`Observable`interface, the variables*aren't*observed.

When there are different layout files for various configurations (for example, landscape or portrait), the variables are combined. There must not be conflicting variable definitions between these layout files.

The generated binding class has a setter and getter for each of the described variables. The variables take the default managed code values until the setter is called---`null`for reference types,`0`for`int`,`false`for`boolean`, etc.

A special variable named`context`is generated for use in binding expressions as needed. The value for`context`is the[`Context`](https://developer.android.com/reference/android/content/Context)object from the root view's[`getContext()`](https://developer.android.com/reference/android/view/View#getContext())method. The`context`variable is overridden by an explicit variable declaration with that name.

### Includes

You can pass variables into an included layout's binding from the containing layout by using the app namespace and the variable name in an attribute. The following example shows included`user`variables from the`name.xml`and`contact.xml`layout files:  

    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:bind="http://schemas.android.com/apk/res-auto">
       <data>
           <variable name="user" type="com.example.User"/>
       </data>
       <LinearLayout
           android:orientation="vertical"
           android:layout_width="match_parent"
           android:layout_height="match_parent">
           <include layout="@layout/name"
               bind:user="@{user}"/>
           <include layout="@layout/contact"
               bind:user="@{user}"/>
       </LinearLayout>
    </layout>

Data binding doesn't support an include as a direct child of a merge element. For example, the following layout isn't supported:  

    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:bind="http://schemas.android.com/apk/res-auto">
       <data>
           <variable name="user" type="com.example.User"/>
       </data>
       <merge><!-- Doesn't work -->
           <include layout="@layout/name"
               bind:user="@{user}"/>
           <include layout="@layout/contact"
               bind:user="@{user}"/>
       </merge>
    </layout>

<br />

<br />

## Additional resources

To learn more about data binding, consult the following additional resources.

### Samples

- [Android Data Binding Library samples](https://github.com/android/databinding-samples)

### Codelabs

- [Data Binding in Android codelab](https://codelabs.developers.google.com/codelabs/android-databinding)

### Blog posts

- [Data Binding --- lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)