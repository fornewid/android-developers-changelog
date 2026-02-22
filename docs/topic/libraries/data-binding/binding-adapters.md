---
title: https://developer.android.com/topic/libraries/data-binding/binding-adapters
url: https://developer.android.com/topic/libraries/data-binding/binding-adapters
source: md.txt
---

Binding adapters are responsible for making the appropriate framework calls to
set values. One example is setting a property value, like calling the
[`setText()`](https://developer.android.com/reference/android/widget/TextView#setText(int)) method. Another
example is setting an event listener, like calling the
[`setOnClickListener()`](https://developer.android.com/reference/android/view/View#setOnClickListener(android.view.View.OnClickListener))
method.

The Data Binding Library lets you specify the method called to set a value,
provide your own binding logic, and specify the type of the returned object by
using adapters.

## Set attribute values

Whenever a bound value changes, the generated binding class must call a setter
method on the view with the binding expression. You can let the Data Binding
Library automatically determine the method, or you can explicitly declare the
method or provide custom logic to select a method.

### Automatic method selection

For an attribute named `example`, the library automatically finds the method
`setExample(arg)` that accepts compatible types as the argument. The namespace
of the attribute isn't considered. Only the attribute name and type are used
when searching for a method.

For example, given the `android:text="@{user.name}"` expression, the library
looks for a `setText(arg)` method that accepts the type returned by
`user.getName()`. If the return type of `user.getName()` is `String`, the
library looks for a `setText()` method that accepts a `String` argument. If the
expression returns an `int`, the library searches for a `setText()` method that
accepts an `int` argument. The expression must return the correct type. You can
cast the return value if necessary.

Data binding works even if no attribute exists with the given name. You can
create attributes for any setter by using data binding. For example, the support
class
[`DrawerLayout`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout)
doesn't have attributes, but it has plenty of setters. The following layout
automatically uses the
[`setScrimColor(int)`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout#setScrimColor(int))
and
[`addDrawerListener(DrawerListener)`](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout#addDrawerListener(androidx.drawerlayout.widget.DrawerLayout.DrawerListener))
methods as the setter for the `app:scrimColor` and `app:drawerListener`
attributes, respectively:

    <androidx.drawerlayout.widget.DrawerLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:scrimColor="@{@color/scrim}"
        app:drawerListener="@{fragment.drawerListener}">

### Specify a custom method name

Some attributes have setters that don't match by name. In these situations, an
attribute can be associated with the setter using the
[`BindingMethods`](https://developer.android.com/reference/androidx/databinding/BindingMethods)
annotation. The annotation is used with a class and can contain multiple
[`BindingMethod`](https://developer.android.com/reference/androidx/databinding/BindingMethod)
annotations, one for each renamed method. Binding methods are annotations that
you can add to any class in your app.

In the following example, the `android:tint` attribute is associated with the
[`setImageTintList(ColorStateList)`](https://developer.android.com/reference/android/widget/ImageView#setImageTintList(android.content.res.ColorStateList))
method---not with the `setTint()` method:

### Kotlin

```kotlin
@BindingMethods(value = [
    BindingMethod(
        type = android.widget.ImageView::class,
        attribute = "android:tint",
        method = "setImageTintList")])
```

### Java

```java
@BindingMethods({
       @BindingMethod(type = "android.widget.ImageView",
                      attribute = "android:tint",
                      method = "setImageTintList"),
})
```

Typically, you don't need to rename setters in Android framework classes. The
attributes are already implemented using the name convention to automatically
find matching methods.

### Provide custom logic

Some attributes need custom binding logic. For example, there is no associated
setter for the `android:paddingLeft` attribute. Instead, the `setPadding(left,
top, right, bottom)` method is provided. A static binding adapter method with
the [`BindingAdapter`](https://developer.android.com/reference/androidx/databinding/BindingAdapter)
annotation lets you customize how a setter for an attribute is called.

The attributes of the Android framework classes already have `BindingAdapter`
annotations. The following example shows the binding adapter for the
`paddingLeft` attribute:

### Kotlin

```kotlin
@BindingAdapter("android:paddingLeft")
fun setPaddingLeft(view: View, padding: Int) {
    view.setPadding(padding,
                view.getPaddingTop(),
                view.getPaddingRight(),
                view.getPaddingBottom())
}
```

### Java

```java
@BindingAdapter("android:paddingLeft")
public static void setPaddingLeft(View view, int padding) {
  view.setPadding(padding,
                  view.getPaddingTop(),
                  view.getPaddingRight(),
                  view.getPaddingBottom());
}
```

The parameter types are important. The first parameter determines the type of
the view that is associated with the attribute. The second parameter determines
the type accepted in the binding expression for the given attribute.

Binding adapters are also useful for other types of customization. For example,
a custom loader can be called from a worker thread to load an image.

You can also have adapters that receive multiple attributes, as shown in the
following example:

### Kotlin

```kotlin
@BindingAdapter("imageUrl", "error")
fun loadImage(view: ImageView, url: String, error: Drawable) {
    Picasso.get().load(url).error(error).into(view)
}
```

### Java

```java
@BindingAdapter({"imageUrl", "error"})
public static void loadImage(ImageView view, String url, Drawable error) {
  Picasso.get().load(url).error(error).into(view);
}
```

You can use the adapter in your layout, as shown in the following example. Note
that `@drawable/venueError` refers to a resource in your app. Surrounding the
resource with `@{}` makes it a valid binding expression.

    <ImageView app:imageUrl="@{venue.imageUrl}" app:error="@{@drawable/venueError}" />

| **Note:** The Data Binding Library ignores custom namespaces for matching purposes.

The adapter is called if `imageUrl` and `error` are used for an
[`ImageView`](https://developer.android.com/reference/android/widget/ImageView) object, `imageUrl` is a
string, and `error` is a
[`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable). If you want
the adapter to be called when any of the attributes are set, set the optional
[`requireAll`](https://developer.android.com/reference/androidx/databinding/BindingAdapter#requireAll())
flag of the adapter to `false`, as shown in the following example:

### Kotlin

```kotlin
@BindingAdapter(value = ["imageUrl", "placeholder"], requireAll = false)
fun setImageUrl(imageView: ImageView, url: String?, placeHolder: Drawable?) {
    if (url == null) {
        imageView.setImageDrawable(placeholder);
    } else {
        MyImageLoader.loadInto(imageView, url, placeholder);
    }
}
```

### Java

```java
@BindingAdapter(value={"imageUrl", "placeholder"}, requireAll=false)
public static void setImageUrl(ImageView imageView, String url, Drawable placeHolder) {
  if (url == null) {
    imageView.setImageDrawable(placeholder);
  } else {
    MyImageLoader.loadInto(imageView, url, placeholder);
  }
}
```
| **Note:** Your binding adapters override the default data binding adapters when there is a conflict.

Binding adapter methods can take the old values in their handlers. A method
taking old and new values must declare all old values for the attributes first,
followed by the new values, as shown in the following example:

### Kotlin

```kotlin
@BindingAdapter("android:paddingLeft")
fun setPaddingLeft(view: View, oldPadding: Int, newPadding: Int) {
    if (oldPadding != newPadding) {
        view.setPadding(newPadding,
                    view.getPaddingTop(),
                    view.getPaddingRight(),
                    view.getPaddingBottom())
    }
}
```

### Java

```java
@BindingAdapter("android:paddingLeft")
public static void setPaddingLeft(View view, int oldPadding, int newPadding) {
  if (oldPadding != newPadding) {
      view.setPadding(newPadding,
                      view.getPaddingTop(),
                      view.getPaddingRight(),
                      view.getPaddingBottom());
   }
}
```

Event handlers can only be used with interfaces or abstract classes with one
abstract method, as shown in the following example:

### Kotlin

```kotlin
@BindingAdapter("android:onLayoutChange")
fun setOnLayoutChangeListener(
        view: View,
        oldValue: View.OnLayoutChangeListener?,
        newValue: View.OnLayoutChangeListener?
) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        if (oldValue != null) {
            view.removeOnLayoutChangeListener(oldValue)
        }
        if (newValue != null) {
            view.addOnLayoutChangeListener(newValue)
        }
    }
}
```

### Java

```java
@BindingAdapter("android:onLayoutChange")
public static void setOnLayoutChangeListener(View view, View.OnLayoutChangeListener oldValue,
       View.OnLayoutChangeListener newValue) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
    if (oldValue != null) {
      view.removeOnLayoutChangeListener(oldValue);
    }
    if (newValue != null) {
      view.addOnLayoutChangeListener(newValue);
    }
  }
}
```

Use this event handler in your layout as follows:

    <View android:onLayoutChange="@{() -> handler.layoutChanged()}"/>

When a listener has multiple methods, it must be split into multiple listeners.
For example,
[`View.OnAttachStateChangeListener`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener)
has two methods:
[`onViewAttachedToWindow(View)`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener#onViewAttachedToWindow(android.view.View))
and
[`onViewDetachedFromWindow(View)`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener#onViewDetachedFromWindow(android.view.View)).
The library provides two interfaces to differentiate the attributes and handlers
for them:

### Kotlin

```kotlin
// Translation from provided interfaces in Java:
@TargetApi(Build.VERSION_CODES.HONEYCOMB_MR1)
interface OnViewDetachedFromWindow {
    fun onViewDetachedFromWindow(v: View)
}

@TargetApi(Build.VERSION_CODES.HONEYCOMB_MR1)
interface OnViewAttachedToWindow {
    fun onViewAttachedToWindow(v: View)
}
```

### Java

```java
@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
public interface OnViewDetachedFromWindow {
  void onViewDetachedFromWindow(View v);
}

@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
public interface OnViewAttachedToWindow {
  void onViewAttachedToWindow(View v);
}
```

Because changing one listener can affect the other, you need an adapter that
works for either attribute or for both. You can set `requireAll` to `false` in
the annotation to specify that not every attribute must be assigned a binding
expression, as shown in the following example:

### Kotlin

```kotlin
@BindingAdapter(
        "android:onViewDetachedFromWindow",
        "android:onViewAttachedToWindow",
        requireAll = false
)
fun setListener(view: View, detach: OnViewDetachedFromWindow?, attach: OnViewAttachedToWindow?) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR1) {
        val newListener: View.OnAttachStateChangeListener?
        newListener = if (detach == null && attach == null) {
            null
        } else {
            object : View.OnAttachStateChangeListener {
                override fun onViewAttachedToWindow(v: View) {
                    attach.onViewAttachedToWindow(v)
                }

                override fun onViewDetachedFromWindow(v: View) {
                    detach.onViewDetachedFromWindow(v)
                }
            }
        }

        val oldListener: View.OnAttachStateChangeListener? =
                ListenerUtil.trackListener(view, newListener, R.id.onAttachStateChangeListener)
        if (oldListener != null) {
            view.removeOnAttachStateChangeListener(oldListener)
        }
        if (newListener != null) {
            view.addOnAttachStateChangeListener(newListener)
        }
    }
}
```

### Java

```java
@BindingAdapter({"android:onViewDetachedFromWindow", "android:onViewAttachedToWindow"}, requireAll=false)
public static void setListener(View view, OnViewDetachedFromWindow detach, OnViewAttachedToWindow attach) {
    if (VERSION.SDK_INT >= VERSION_CODES.HONEYCOMB_MR1) {
        OnAttachStateChangeListener newListener;
        if (detach == null && attach == null) {
            newListener = null;
        } else {
            newListener = new OnAttachStateChangeListener() {
                @Override
                public void onViewAttachedToWindow(View v) {
                    if (attach != null) {
                        attach.onViewAttachedToWindow(v);
                    }
                }
                @Override
                public void onViewDetachedFromWindow(View v) {
                    if (detach != null) {
                        detach.onViewDetachedFromWindow(v);
                    }
                }
            };
        }

        OnAttachStateChangeListener oldListener = ListenerUtil.trackListener(view, newListener,
                R.id.onAttachStateChangeListener);
        if (oldListener != null) {
            view.removeOnAttachStateChangeListener(oldListener);
        }
        if (newListener != null) {
            view.addOnAttachStateChangeListener(newListener);
        }
    }
}
```

The above example is slightly complicated because the
[`View`](https://developer.android.com/reference/android/view/View) class uses the
[`addOnAttachStateChangeListener()`](https://developer.android.com/reference/android/view/View#addOnAttachStateChangeListener(android.view.View.OnAttachStateChangeListener))
and
[`removeOnAttachStateChangeListener()`](https://developer.android.com/reference/android/view/View#removeOnAttachStateChangeListener(android.view.View.OnAttachStateChangeListener))
methods instead of a setter method for
[`OnAttachStateChangeListener`](https://developer.android.com/reference/android/view/View.OnAttachStateChangeListener).
The `android.databinding.adapters.ListenerUtil` class helps keep track of these
listeners so that they can be removed in the binding adapter.

## Object conversions

### Automatic object conversion

When an [`Object`](https://developer.android.com/reference/java/lang/Object) is returned from a binding
expression, the library selects the method used to set the value of the
property. The `Object` is cast to a parameter type of the chosen method. This
behavior is convenient in apps using the
[`ObservableMap`](https://developer.android.com/reference/androidx/databinding/ObservableMap) class to
store data, as shown in the following example:

    <TextView
       android:text='@{userMap["lastName"]}'
       android:layout_width="wrap_content"
       android:layout_height="wrap_content" />

| **Note:** You can also refer to a value in the map using the `object.key` notation. For example, you can replace `@{userMap["lastName"]}` in the previous example with `@{userMap.lastName}`.

The `userMap` object in the expression returns a value, which is automatically
cast to the parameter type found in the `setText(CharSequence)` method used to
set the value of the `android:text` attribute. If the parameter type is
ambiguous, cast the return type in the expression.

### Custom conversions

In some situations, a custom conversion is required between specific types. For
example, the `android:background` attribute of a view expects a `Drawable`, but
the `color` value specified is an integer. The following example shows an
attribute that expects a `Drawable`, but an integer is provided instead:

    <View
       android:background="@{isError ? @color/red : @color/white}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>

Whenever a `Drawable` is expected and an integer is returned, convert the `int`
to a [`ColorDrawable`](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable).
To perform the conversion, use a static method with a
[`BindingConversion`](https://developer.android.com/reference/androidx/databinding/BindingConversion)
annotation, as follows:

### Kotlin

```kotlin
@BindingConversion
fun convertColorToDrawable(color: Int) = ColorDrawable(color)
```

### Java

```java
@BindingConversion
public static ColorDrawable convertColorToDrawable(int color) {
    return new ColorDrawable(color);
}
```

However, the value types provided in the binding expression must be consistent.
You can't use different types in the same expression, as shown in the following
example:

    // The @drawable and @color represent different value types in the same
    // expression, which causes a build error.
    <View
       android:background="@{isError ? @drawable/error : @color/white}"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"/>

<br />

<br />

## Additional resources

To learn more about data binding, see the following resources.

### Samples

- [Android Data Binding Library samples](https://github.com/android/databinding-samples)

### Codelabs

- [Data Binding in Android](https://codelabs.developers.google.com/codelabs/android-databinding)

### Blog posts

- [Data Binding --- lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Data Binding Library](https://developer.android.com/topic/libraries/data-binding)
- [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
- [View binding](https://developer.android.com/topic/libraries/view-binding)