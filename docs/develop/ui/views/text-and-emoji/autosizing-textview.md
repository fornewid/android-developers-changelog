---
title: https://developer.android.com/develop/ui/views/text-and-emoji/autosizing-textview
url: https://developer.android.com/develop/ui/views/text-and-emoji/autosizing-textview
source: md.txt
---

# Autosize TextViews

With Android 8.0 (API level 26) and higher, you can instruct a[TextView](https://developer.android.com/reference/android/widget/TextView)to let the text size expand or contract automatically to fill its layout based on the`TextView`'s characteristics and boundaries. This setting makes it easier to optimize text size on different screens with dynamic content.

Support Library 26.0 fully supports the autosizing`TextView`feature on devices running Android versions 8.0 (API level 26) or lower. The`android.support.v4.widget`package contains the`TextViewCompat`class to access features in a backward-compatible fashion.

## Set up TextView autosize

You can either use the framework or Support Library to set up the autosizing of`TextView`programmatically or in XML. To set the XML attributes, you can also use the**Properties**window in Android Studio.

There are three ways you can set up the autosizing of`TextView`, described in the sections that follow:

- [Default](https://developer.android.com/develop/ui/views/text-and-emoji/autosizing-textview#default)
- [Granularity](https://developer.android.com/develop/ui/views/text-and-emoji/autosizing-textview#granularity)
- [Preset sizes](https://developer.android.com/develop/ui/views/text-and-emoji/autosizing-textview#preset-sizes)

**Note** : If you set autosizing in an XML file, we do not recommended using the value "wrap_content" for the`layout_width`or`layout_height`attributes of a`TextView`. Doing so might produce unexpected results.

### Default

The default setting lets the autosizing of`TextView`scale uniformly on horizontal and vertical axes.

- To define the default setting programmatically, call the[`setAutoSizeTextTypeWithDefaults(int autoSizeTextType)
  `](https://developer.android.com/reference/android/widget/TextView#setAutoSizeTextTypeWithDefaults(int))method. Provide`AUTO_SIZE_TEXT_TYPE_NONE`to turn off the autosizing feature or`AUTO_SIZE_TEXT_TYPE_UNIFORM`to scale the horizontal and the vertical axes uniformly.
- **Note** : The default dimensions for uniform scaling are`minTextSize = 12sp`,`maxTextSize = 112sp`, and`granularity = 1px.`
- To define the default setting in XML, use the`android`namespace and set the[`autoSizeTextType`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoSizeTextType)attribute to*none* or*uniform*.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView
    android:layout_width="match_parent"
    android:layout_height="200dp"
    android:autoSizeTextType="uniform" />
```

#### Define the default setting using the Support Library

- To define the default setting programmatically through the Support Library, call the[`TextViewCompat.setAutoSizeTextTypeWithDefaults(TextView textview, int autoSizeTextType)`](https://developer.android.com/reference/androidx/core/widget/TextViewCompat#setAutoSizeTextTypeWithDefaults(android.widget.TextView,int))method. Provide an instance of the`TextView`widget and one of the text types, such as`TextViewCompat.AUTO_SIZE_TEXT_TYPE_NONE`or`TextViewCompat.AUTO_SIZE_TEXT_TYPE_UNIFORM`.
- To define the default setting in XML through the Support Library, use the`app`namespace and set the`autoSizeTextType`attribute to*none* or*uniform*.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

  <TextView
      android:layout_width="match_parent"
      android:layout_height="200dp"
      app:autoSizeTextType="uniform" />

</LinearLayout>
```

### Granularity

You can define a range of minimum and maximum text sizes and a dimension that specifies the size of each step. The`TextView`scales uniformly in a range between the minimum and maximum size attributes. Each increment occurs as the step size set in the granularity attribute.

- To define a range of text sizes and a dimension programmatically, call the[setAutoSizeTextTypeUniformWithConfiguration(int autoSizeMinTextSize, int autoSizeMaxTextSize, int autoSizeStepGranularity, int unit)](https://developer.android.com/reference/android/widget/TextView#setAutoSizeTextTypeUniformWithConfiguration(int, int, int, int))method. Provide the maximum value, the minimum value, the granularity value, and any[TypedValue](https://developer.android.com/reference/android/util/TypedValue)dimension unit.
- To define a range of text sizes and a dimension in XML, use the`android`namespace and set the following attributes:
  - Set the`autoSizeTextType`attribute to either*none* or*uniform* . The*none* value is the default, and*uniform* lets`TextView`scale uniformly on horizontal and vertical axes.
- Set the[`autoSizeMinTextSize`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoSizeMinTextSize),[`autoSizeMaxTextSize`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoSizeMaxTextSize), and[`autoSizeStepGranularity`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoSizeStepGranularity)attributes to define the dimensions for the autosizing of`TextView`.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView
    android:layout_width="match_parent"
    android:layout_height="200dp"
    android:autoSizeTextType="uniform"
    android:autoSizeMinTextSize="12sp"
    android:autoSizeMaxTextSize="100sp"
    android:autoSizeStepGranularity="2sp" />
```

#### Define granularity using the Support Library

- To define a range of text sizes and a dimension programmatically through the Support Library, call the[`TextViewCompat.setAutoSizeTextTypeUniformWithConfiguration(int autoSizeMinTextSize, int autoSizeMaxTextSize, int autoSizeStepGranularity, int unit)`](https://developer.android.com/reference/androidx/core/widget/TextViewCompat#setAutoSizeTextTypeUniformWithConfiguration(android.widget.TextView,int,int,int,int))method. Provide the maximum value, the minimum value, the granularity value, and any`TypedValue`dimension unit.
- To define a range of text sizes and a dimension in XML through the Support Library, use the`app`namespace and set the`autoSizeText`,`autoSizeMinTextSize`,`autoSizeMaxTextSize`, and`autoSizeStepGranularity`attributes in the layout XML file.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

  <TextView
      android:layout_width="match_parent"
      android:layout_height="200dp"
      app:autoSizeTextType="uniform"
      app:autoSizeMinTextSize="12sp"
      app:autoSizeMaxTextSize="100sp"
      app:autoSizeStepGranularity="2sp" />

</LinearLayout>
```

### Preset sizes

Preset sizes let you specify the values that the`TextView`picks when autosizing text.

- To use preset sizes to set up the autosizing of`TextView`programmatically, call the[setAutoSizeTextTypeUniformWithPresetSizes(int[] presetSizes, int unit)](https://developer.android.com/reference/android/widget/TextView#setAutoSizeTextTypeUniformWithPresetSizes(int[], int))method. Provide an array of sizes and any`TypedValue`dimension unit for the size.
- To use preset sizes to set up the autosizing of`TextView`in XML, use the`android`namespace and set the following attributes:
  - Set the`autoSizeTextType`attribute to either*none* or*uniform* . The*none* value is the default, and*uniform* lets`TextView`scale uniformly on horizontal and vertical axes.
- Set the[`autoSizePresetSizes`](https://developer.android.com/reference/android/widget/TextView#attr_android:autoSizePresetSizes)attribute to an array of preset sizes. To access the array as a resource, define the array in the`res/values/arrays.xml`file.  

```xml
<resources>
  <array name="autosize_text_sizes">
    <item>10sp</item>
    <item>12sp</item>
    <item>20sp</item>
    <item>40sp</item>
    <item>100sp</item>
  </array>
</resources>
```  

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView
    android:layout_width="match_parent"
    android:layout_height="200dp"
    android:autoSizeTextType="uniform"
    android:autoSizePresetSizes="@array/autosize_text_sizes" />
```

#### Set up preset sizes using the Support Library

- To use preset sizes to set up the autosizing of`TextView`programmatically through the Support Library, call the[`TextViewCompat.setAutoSizeTextTypeUniformWithPresetSizes(TextView textView, int[] presetSizes, int unit)`](https://developer.android.com/reference/androidx/core/widget/TextViewCompat#setAutoSizeTextTypeUniformWithPresetSizes(android.widget.TextView,int[],int))method. Provide an instance of the`TextView`class, an array of sizes, and any`TypedValue`dimension unit for the size.
- To use preset sizes to set up the autosizing of`TextView`in XML through the Support Library, use the`app`namespace and set the`autoSizeTextType`and`autoSizePresetSizes`attributes in the layout XML file.  

```xml
<resources>
  <array name="autosize_text_sizes">
    <item>10sp</item>
    <item>12sp</item>
    <item>20sp</item>
    <item>40sp</item>
    <item>100sp</item>
  </array>
</resources>
```  

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

  <TextView
      android:layout_width="match_parent"
      android:layout_height="200dp"
      app:autoSizeTextType="uniform"
      app:autoSizePresetSizes="@array/autosize_text_sizes" />
</LinearLayout>
```

## Additional resources

For additional information on autosizing a`TextView`when working with dynamic content, watch[Android Jetpack: Autosizing TextView](https://www.youtube.com/watch?v=JYrpEAz_A1U).