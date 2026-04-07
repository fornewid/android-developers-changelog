---
title: Add checkboxes to your app  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/checkbox
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add checkboxes to your app Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.

[Checkbox →](https://developer.android.com/develop/ui/compose/components/checkbox)

![](/static/images/android-compose-ui-logo.png)

**Note:** For a better user experience, see the
[Material Design Checkbox](https://m3.material.io/components/checkbox/overview)
documentation.

Checkboxes let the user select one or more options from a set. Typically, you present checkbox
options in a vertical list.

![An image showing an example of checkboxes from material.io](https://lh3.googleusercontent.com/5myEkgWrS1SEYui5V_VRDXNyYFr25CRPVAKm5sCPhapurUx9EgorjTWNx8s-Sj1Mb4mHw9stQ6Bo6Nkg3LpF0NRZRH1qVOU2r-Nbjr27S3CT=s0)


**Figure 1.** An example of checkboxes from
[Material Design Checkbox](https://m3.material.io/components/checkbox/guidelines).

To create each checkbox option, create a
`CheckBox` in your layout. Because
a set of checkbox options lets the user select multiple items, each checkbox is managed separately,
and you must register a click listener for each one.

## Respond to click events

Begin by creating a layout with `CheckBox` objects in a list:

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <CheckBox android:id="@+id/checkbox_meat"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Meat" />
    <CheckBox android:id="@+id/checkbox_cheese"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Cheese"/>
</LinearLayout>
```

Once your layout is ready, head to your `Activity` or `Fragment`, find your
`CheckBox` views, and set a change listener, as in the following example:

### Kotlin

```
findViewById<CheckBox>(R.id.checkbox_meat)
    .setOnCheckedChangeListener { buttonView, isChecked ->
        Log.d("CHECKBOXES", "Meat is checked: $isChecked")
    }

findViewById<CheckBox>(R.id.checkbox_cheese)
    .setOnCheckedChangeListener { buttonView, isChecked ->
        Log.d("CHECKBOXES", "Cheese is checked: $isChecked")
    }
```

### Java

```
findViewById<CheckBox>(R.id.checkbox_meat)
    .setOnCheckedChangeListener { buttonView, isChecked ->
        Log.d("CHECKBOXES", "Meat is checked: $isChecked");
    }

findViewById<CheckBox>(R.id.checkbox_cheese)
    .setOnCheckedChangeListener { buttonView, isChecked ->
        Log.d("CHECKBOXES", "Cheese is checked: $isChecked");
    }
```

The previous code prints a message in Logcat every time the checkboxes change status.

**Tip:** If you need to change the checkbox state yourself, use the
`setChecked(boolean)`
or `toggle()`
method.