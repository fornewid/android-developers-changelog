---
title: https://developer.android.com/develop/ui/views/layout/custom-views/create-view
url: https://developer.android.com/develop/ui/views/layout/custom-views/create-view
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose. [Custom Layouts in Compose →](https://developer.android.com/jetpack/compose/layouts/custom) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

A well-designed custom view is like any other well-designed class. It encapsulates a
specific set of
functionality with a simple interface, uses CPU and memory efficiently, and so on. In
addition to being a
well-designed class, a custom view must do the following:

- Conform to Android standards.
- Provide custom styleable attributes that work with Android XML layouts.
- Send accessibility events.
- Be compatible with multiple Android platforms.

The Android framework provides a set of base classes and XML tags to help you create a view that
meets all of these
requirements. This lesson discusses how to use the Android framework to create the core
functionality of a view
class.


You can find additional
information in [Custom view components](https://developer.android.com/guide/topics/ui/custom-components).

## Subclass a view

All the view classes defined in the Android framework extend
`https://developer.android.com/reference/android/view/View`. Your
custom view can also
extend `View` directly, or you can
save time by extending one of the
existing view
subclasses, such as `https://developer.android.com/reference/android/widget/Button`.

To allow Android Studio to interact with your view, at a minimum you must provide a constructor that takes a
`https://developer.android.com/reference/android/content/Context` and an `https://developer.android.com/reference/android/util/AttributeSet` object as parameters.
This constructor allows the layout editor to create and edit an instance of your view.

### Kotlin

```kotlin
class PieChart(context: Context, attrs: AttributeSet) : View(context, attrs)
```

### Java

```java
class PieChart extends View {
    public PieChart(Context context, AttributeSet attrs) {
        super(context, attrs);
    }
}
```

## Define custom attributes

To add a built-in `View` to your user interface, specify it in an XML element and
control its
appearance and behavior with element attributes. You can also add and style custom
views using XML. To
enable this behavior in your custom view, do the following:

- Define custom attributes for your view in a `<declare-styleable>
  ` resource element.
- Specify values for the attributes in your XML layout.
- Retrieve attribute values at runtime.
- Apply the retrieved attribute values to your view.

This section discusses how to define custom attributes and specify their values.
The next section covers
retrieving and applying the values at runtime.

To define custom attributes, add `<declare-styleable>
` resources to your project. It's customary to put these resources into a
`res/values/attrs.xml` file. Here's
an example of a `attrs.xml` file:

```xml
<resources>
   <declare-styleable name="PieChart">
       <attr name="showText" format="boolean" />
       <attr name="labelPosition" format="enum">
           <enum name="left" value="0"/>
           <enum name="right" value="1"/>
       </attr>
   </declare-styleable>
</resources>
```

This code declares two custom attributes, `showText` and `labelPosition`,
that belong to a styleable
entity named `PieChart`. The name of the styleable entity is, by convention, the same
name as the
name of the class
that defines the custom view. Although it's not necessary to follow this convention,
many popular code
editors depend on this naming convention to provide statement completion.

Once you define custom attributes, you can use them in layout XML files just like built-in
attributes. The only
difference is that your custom attributes belong to a different namespace. Instead of belonging
to the `http://schemas.android.com/apk/res/android` namespace, they belong to `http://schemas.android.com/apk/res/[your package name]`. For example, here's how to use the
attributes defined for
`PieChart`:


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:custom="http://schemas.android.com/apk/res-auto">
 <com.example.customviews.charting.PieChart
     custom:showText="true"
     custom:labelPosition="left" />
</LinearLayout>
```

To avoid having to repeat the long namespace URI, the sample uses an
`xmlns` directive. This directive assigns the alias `custom` to
the namespace `http://schemas.android.com/apk/res/com.example.customviews`.
You can choose any alias you want for your namespace.

Notice the name of the XML tag that adds the custom view to the layout. It is the fully
qualified name of the
custom view class. If your view class is an inner class, further qualify it
with the name of the view's outer class.
For instance, the
`PieChart` class has an inner class called `PieView`. To use the
custom attributes from this class, you
use the tag `com.example.customviews.charting.PieChart$PieView`.

## Apply custom attributes

When a view is created from an XML layout, all the attributes in the XML tag are read
from the resource
bundle and passed into the view's constructor as an
`https://developer.android.com/reference/android/util/AttributeSet`.
Although it's
possible to read values from the `AttributeSet` directly, doing so
has some disadvantages:

- Resource references within attribute values are not resolved.
- Styles are not applied.

Instead, pass the `AttributeSet` to
`https://developer.android.com/reference/android/content/res/Resources.Theme#obtainStyledAttributes(android.util.AttributeSet, int[], int, int)`.
This method passes back a
`https://developer.android.com/reference/android/content/res/TypedArray`
array of
values that are
already dereferenced and styled.

The Android resource compiler does a lot of work for you to make calling
`obtainStyledAttributes()`
easier. For each `<declare-styleable>`
resource in the `res/` directory, the generated `R.java` defines both an array of attribute
IDs and a set of
constants that define the index for each attribute in the array. You use the predefined
constants to read
the attributes from the `TypedArray`. Here's how
the `PieChart` class
reads its attributes:

### Kotlin

```kotlin
init {
    context.theme.obtainStyledAttributes(
            attrs,
            R.styleable.PieChart,
            0, 0).apply {

        try {
            mShowText = getBoolean(R.styleable.PieChart_showText, false)
            textPos = getInteger(R.styleable.PieChart_labelPosition, 0)
        } finally {
            recycle()
        }
    }
}
```

### Java

```java
public PieChart(Context context, AttributeSet attrs) {
   super(context, attrs);
   TypedArray a = context.getTheme().obtainStyledAttributes(
        attrs,
        R.styleable.PieChart,
        0, 0);

   try {
       mShowText = a.getBoolean(R.styleable.PieChart_showText, false);
       textPos = a.getInteger(R.styleable.PieChart_labelPosition, 0);
   } finally {
       a.recycle();
   }
}
```

Note that `TypedArray` objects
are a shared resource
and must be recycled after use.

## Add properties and events

Attributes are a powerful way of controlling the behavior and appearance of views, but
they can only be read
when the view is initialized. To provide dynamic behavior, expose a property getter and
setter pair for each
custom attribute. The following snippet shows how `PieChart` exposes a property
called `showText`:

### Kotlin

```kotlin
fun isShowText(): Boolean {
    return mShowText
}

fun setShowText(showText: Boolean) {
    mShowText = showText
    invalidate()
    requestLayout()
}
```

### Java

```java
public boolean isShowText() {
   return mShowText;
}

public void setShowText(boolean showText) {
   mShowText = showText;
   invalidate();
   requestLayout();
}
```

Notice that `setShowText` calls `https://developer.android.com/reference/android/view/View#invalidate()`
and `https://developer.android.com/reference/android/view/View#requestLayout()`. These calls are crucial
to ensure that the view behaves reliably. You need
to invalidate the view after any change to its properties that might change its
appearance, so that the
system knows it needs to be redrawn. Likewise, you need to request a new layout if
a property changes in a way
that might affect the size or shape of the view. Forgetting these method calls can cause
hard-to-find
bugs.

Custom views must also support event listeners to communicate important events. For
instance, `PieChart`
exposes a custom event called `OnCurrentItemChanged` to notify listeners that
the user rotated the
pie chart to focus on a new pie slice.

It's easy to forget to expose properties and events, especially when you're the only user
of the custom view.
Taking time to carefully define your view's interface reduces future maintenance
costs.
A good rule to follow is to always expose any property that affects the visible
appearance or behavior of
your custom view.

## Design for accessibility

Your custom view must support a wide range of users. This includes users with
disabilities that
prevent them from seeing or using a touchscreen. To support users with disabilities,
do the following:

- Label your input fields using the `android:contentDescription` attribute.
- Send accessibility events by calling `https://developer.android.com/reference/android/view/accessibility/AccessibilityEventSource#sendAccessibilityEvent(int)` when appropriate.
- Support alternate controllers, such as a D-pad or trackball.

For more information about creating accessible views, see
[Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps#custom-views).