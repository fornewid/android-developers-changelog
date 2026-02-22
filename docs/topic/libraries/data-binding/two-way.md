---
title: https://developer.android.com/topic/libraries/data-binding/two-way
url: https://developer.android.com/topic/libraries/data-binding/two-way
source: md.txt
---

# Two-way data binding

Using one-way data binding, you can set a value on an attribute and set a listener that reacts to a change in that attribute:  

```xml
<CheckBox
    android:id="@+id/rememberMeCheckBox"
    android:checked="@{viewmodel.rememberMe}"
    android:onCheckedChanged="@{viewmodel.rememberMeChanged}"
/>
```

Two-way data binding provides a shortcut to this process:  

```xml
<CheckBox
    android:id="@+id/rememberMeCheckBox"
    android:checked="@={viewmodel.rememberMe}"
/>
```

The`@={}`notation, which importantly includes the "=" sign, receives data changes to the property and listen to user updates at the same time.

In order to react to changes in the backing data, you can make your layout variable an implementation of`Observable`, usually[`BaseObservable`](https://developer.android.com/reference/androidx/databinding/BaseObservable), and use a[`@Bindable`](https://developer.android.com/reference/androidx/databinding/Bindable)annotation, as shown in the following code snippet:  

### Kotlin

```kotlin
class LoginViewModel : BaseObservable {
    // val data = ...

    @Bindable
    fun getRememberMe(): Boolean {
        return data.rememberMe
    }

    fun setRememberMe(value: Boolean) {
        // Avoids infinite loops.
        if (data.rememberMe != value) {
            data.rememberMe = value

            // React to the change.
            saveData()

            // Notify observers of a new value.
            notifyPropertyChanged(BR.remember_me)
        }
    }
}
```

### Java

```java
public class LoginViewModel extends BaseObservable {
    // private Model data = ...

    @Bindable
    public Boolean getRememberMe() {
        return data.rememberMe;
    }

    public void setRememberMe(Boolean value) {
        // Avoids infinite loops.
        if (data.rememberMe != value) {
            data.rememberMe = value;

            // React to the change.
            saveData();

            // Notify observers of a new value.
            notifyPropertyChanged(BR.remember_me);
        }
    }
}
```

Because the bindable property's getter method is called`getRememberMe()`, the property's corresponding setter method automatically uses the name`setRememberMe()`.

For more information on using`BaseObservable`and`@Bindable`, see[Work with observable data objects](https://developer.android.com/topic/libraries/data-binding/observability).

## Two-way data binding using custom attributes

The platform provides two-way data binding implementations for[the most common two-way attributes](https://developer.android.com/topic/libraries/data-binding/two-way#two-way-attributes)and change listeners, which you can use as part of your app. If you want to use two-way data binding with custom attributes, you need to work with the[`@InverseBindingAdapter`](https://developer.android.com/reference/androidx/databinding/InverseBindingAdapter)and[`@InverseBindingMethod`](https://developer.android.com/reference/androidx/databinding/InverseBindingMethod)annotations.

For example, if you want to enable two-way data binding on a`"time"`attribute in a custom view called`MyView`, complete the following steps:

1. Annotate the method that sets the initial value and updates when the value changes using`@BindingAdapter`:

   ### Kotlin

   ```kotlin
   @BindingAdapter("time")
   @JvmStatic fun setTime(view: MyView, newValue: Time) {
       // Important to break potential infinite loops.
       if (view.time != newValue) {
           view.time = newValue
       }
   }
   ```

   ### Java

   ```java
   @BindingAdapter("time")
   public static void setTime(MyView view, Time newValue) {
       // Important to break potential infinite loops.
       if (view.time != newValue) {
           view.time = newValue;
       }
   }
   ```
2. Annotate the method that reads the value from the view using`@InverseBindingAdapter`:

   ### Kotlin

   ```kotlin
   @InverseBindingAdapter("time")
   @JvmStatic fun getTime(view: MyView) : Time {
       return view.getTime()
   }
   ```

   ### Java

   ```java
   @InverseBindingAdapter("time")
   public static Time getTime(MyView view) {
       return view.getTime();
   }
   ```

At this point, data binding knows what to do when the data changes (it calls the method annotated with[`@BindingAdapter`](https://developer.android.com/reference/androidx/databinding/BindingAdapter)) and what to call when the view attribute changes (it calls the[`InverseBindingListener`](https://developer.android.com/reference/androidx/databinding/InverseBindingListener)). However, it doesn't know when or how the attribute changes.

For that, you need to set a listener on the view. It can be a custom listener associated with your custom view, or it can be a generic event, such as a loss of focus or a text change. Add the`@BindingAdapter`annotation to the method that sets the listener for changes on the property:  

### Kotlin

```kotlin
@BindingAdapter("app:timeAttrChanged")
@JvmStatic fun setListeners(
        view: MyView,
        attrChange: InverseBindingListener
) {
    // Set a listener for click, focus, touch, etc.
}
```

### Java

```java
@BindingAdapter("app:timeAttrChanged")
public static void setListeners(
        MyView view, final InverseBindingListener attrChange) {
    // Set a listener for click, focus, touch, etc.
}
```

The listener includes an`InverseBindingListener`as a parameter. You use the`InverseBindingListener`to tell the data binding system that the attribute has changed. The system can then start calling the method annotated using`@InverseBindingAdapter`, and so on.
| **Note:** Every two-way binding generates a*synthetic event attribute* . This attribute has the same name as the base attribute, but it includes the suffix`"AttrChanged"`. The synthetic event attribute allows the library to create a method annotated using`@BindingAdapter`to associate the event listener to the appropriate instance of`View`.

In practice, this listener includes some non-trivial logic, including listeners for one-way data binding. For an example, see the adapter for the text attribute change,[`TextViewBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/TextViewBindingAdapter.java#352).

## Converters

If the variable that's bound to a[`View`](https://developer.android.com/reference/android/view/View)object needs to be formatted, translated, or changed somehow before being displayed, it's possible to use a`Converter`object.

For example, take an`EditText`object that shows a date:  

    <EditText
        android:id="@+id/birth_date"
        android:text="@={Converter.dateToString(viewmodel.birthDate)}"
    />

The`viewmodel.birthDate`attribute contains a value of type`Long`, so it needs to be formatted by using a converter.

Because a two-way expression is being used, there also needs to be an*inverse converter* to let the library know how to convert the user-provided string back to the backing data type, in this case`Long`. This process is done by adding the[`@InverseMethod`](https://developer.android.com/reference/androidx/databinding/InverseMethod)annotation to one of the converters and have this annotation reference the inverse converter. An example of this configuration appears in the following code snippet:  

### Kotlin

```kotlin
object Converter {
    @InverseMethod("stringToDate")
    @JvmStatic fun dateToString(
        view: EditText, oldValue: Long,
        value: Long
    ): String {
        // Converts long to String.
    }

    @JvmStatic fun stringToDate(
        view: EditText, oldValue: String,
        value: String
    ): Long {
        // Converts String to long.
    }
}
```

### Java

```java
public class Converter {
    @InverseMethod("stringToDate")
    public static String dateToString(EditText view, long oldValue,
            long value) {
        // Converts long to String.
    }

    public static long stringToDate(EditText view, String oldValue,
            String value) {
        // Converts String to long.
    }
}
```

## Infinite loops using two-way data binding

Be careful not to introduce infinite loops when using two-way data binding. When the user changes an attribute, the method annotated using`@InverseBindingAdapter`is called, and the value is assigned to the backing property. This, in turn, would call the method annotated using`@BindingAdapter`, which would trigger another call to the method annotated using`@InverseBindingAdapter`, and so on.

For this reason, it's important to break possible infinite loops by comparing new and old values in the methods annotated using`@BindingAdapter`.

## Two-way attributes

The platform provides built-in support for two-way data binding when you use the attributes in the following table. For details on how the platform provides this support, see the implementations for the corresponding binding adapters:

|                                           Class                                           |                                          Attribute(s)                                           |                                                                                                             Binding adapter                                                                                                              |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`AdapterView`](https://developer.android.com/reference/android/widget/AdapterView)       | `android:selectedItemPosition` `android:selection`                                              | [`AdapterViewBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/AdapterViewBindingAdapter.java)       |
| [`CalendarView`](https://developer.android.com/reference/android/widget/CalendarView)     | `android:date`                                                                                  | [`CalendarViewBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/CalendarViewBindingAdapter.java)     |
| [`CompoundButton`](https://developer.android.com/reference/android/widget/CompoundButton) | [`android:checked`](https://developer.android.com/reference/android/R.attr#checked)             | [`CompoundButtonBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/CompoundButtonBindingAdapter.java) |
| [`DatePicker`](https://developer.android.com/reference/android/widget/DatePicker)         | `android:year` `android:month` `android:day`                                                    | [`DatePickerBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/DatePickerBindingAdapter.java)         |
| [`NumberPicker`](https://developer.android.com/reference/android/widget/NumberPicker)     | [`android:value`](https://developer.android.com/reference/android/R.attr#value)                 | [`NumberPickerBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/NumberPickerBindingAdapter.java)     |
| [`RadioButton`](https://developer.android.com/reference/android/widget/RadioButton)       | [`android:checkedButton`](https://developer.android.com/reference/android/R.attr#checkedButton) | [`RadioGroupBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/RadioGroupBindingAdapter.java)         |
| [`RatingBar`](https://developer.android.com/reference/android/widget/RatingBar)           | [`android:rating`](https://developer.android.com/reference/android/R.attr#rating)               | [`RatingBarBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/RatingBarBindingAdapter.java)           |
| [`SeekBar`](https://developer.android.com/reference/android/widget/SeekBar)               | [`android:progress`](https://developer.android.com/reference/android/R.attr#progress)           | [`SeekBarBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/SeekBarBindingAdapter.java)               |
| [`TabHost`](https://developer.android.com/reference/android/widget/TabHost)               | `android:currentTab`                                                                            | [`TabHostBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/TabHostBindingAdapter.java)               |
| [`TextView`](https://developer.android.com/reference/android/widget/TextView)             | [`android:text`](https://developer.android.com/reference/android/R.attr#text)                   | [`TextViewBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/TextViewBindingAdapter.java)             |
| [`TimePicker`](https://developer.android.com/reference/android/widget/TimePicker)         | `android:hour` `android:minute`                                                                 | [`TimePickerBindingAdapter`](https://android.googlesource.com/platform/frameworks/data-binding/+/refs/heads/studio-master-dev/extensions/baseAdapters/src/main/java/androidx/databinding/adapters/TimePickerBindingAdapter.java)         |

## Additional resources

To learn more about data binding, consult the following additional resources.

### Samples

- [Android Data Binding Library samples](https://github.com/android/databinding-samples)

### Codelabs

- [Android Data Binding codelab](https://codelabs.developers.google.com/codelabs/android-databinding)

### Blog posts

- [Data Binding --- Lessons Learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Work with observable data objects](https://developer.android.com/topic/libraries/data-binding/observability)
- [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
- [Bind layout views to Architecture Components](https://developer.android.com/topic/libraries/data-binding/architecture)