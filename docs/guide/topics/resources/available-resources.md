---
title: https://developer.android.com/guide/topics/resources/available-resources
url: https://developer.android.com/guide/topics/resources/available-resources
source: md.txt
---

# Resource types overview

Each page in this section describes the usage, format, and syntax for a certain type of[app resource](https://developer.android.com/guide/topics/resources/providing-resources)that you can provide in your project resources directory (`res/`).

Here's a brief summary of each page:

[Animation resources](https://developer.android.com/guide/topics/resources/animation-resource)
:   Define pre-determined animations.  
    Tween animations are saved in`res/anim/`and accessed from the`R.anim`class.  
    Frame animations are saved in`res/drawable/`and accessed from the`R.drawable`class.

[Color state list resource](https://developer.android.com/guide/topics/resources/color-list-resource)
:   Define a color resource that changes based on the`View`state.  
    Saved in`res/color/`and accessed from the`R.color`class.

[Drawable resources](https://developer.android.com/guide/topics/resources/drawable-resource)
:   Define various graphics with bitmaps or XML.  
    Saved in`res/drawable/`and accessed from the`R.drawable`class.

[Layout resource](https://developer.android.com/guide/topics/resources/layout-resource)
:   Define the layout for your application UI.  
    Saved in`res/layout/`and accessed from the`R.layout`class.

[Menu resource](https://developer.android.com/guide/topics/resources/menu-resource)
:   Define the contents of your application menus.  
    Saved in`res/menu/`and accessed from the`R.menu`class.

[String resources](https://developer.android.com/guide/topics/resources/string-resource)
:   Define strings, string arrays, and plurals and include string formatting and styling.  
    Saved in`res/values/`and accessed from the`R.string`,`R.array`, and`R.plurals`classes.

[Style resource](https://developer.android.com/guide/topics/resources/style-resource)
:   Define the look and format for UI elements.  
    Saved in`res/values/`and accessed from the`R.style`class.

[Font resources](https://developer.android.com/guide/topics/resources/font-resource)
:   Define font families and include custom fonts in XML.  
    Saved in`res/font/`and accessed from the`R.font`class.

[More resource types](https://developer.android.com/guide/topics/resources/more-resources)
:   Define other primitive values as static resources, including the following:

    [Bool](https://developer.android.com/guide/topics/resources/more-resources#Bool)
    :   XML resource that carries a boolean value.

    [Color](https://developer.android.com/guide/topics/resources/more-resources#Color)
    :   XML resource that carries a hexadecimal color value.

    [Dimension](https://developer.android.com/guide/topics/resources/more-resources#Dimension)
    :   XML resource that carries a dimension value with a unit of measure.

    [ID](https://developer.android.com/guide/topics/resources/more-resources#Id)
    :   XML resource that provides a unique identifier for application resources and components.

    [Integer](https://developer.android.com/guide/topics/resources/more-resources#Integer)
    :   XML resource that carries an integer value.

    [Integer array](https://developer.android.com/guide/topics/resources/more-resources#IntegerArray)
    :   XML resource that provides an array of integers.

    [Typed array](https://developer.android.com/guide/topics/resources/more-resources#TypedArray)
    :   XML resource that provides a[TypedArray](https://developer.android.com/reference/android/content/res/TypedArray), which you can use for an array of drawables.