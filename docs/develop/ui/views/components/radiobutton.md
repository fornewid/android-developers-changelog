---
title: https://developer.android.com/develop/ui/views/components/radiobutton
url: https://developer.android.com/develop/ui/views/components/radiobutton
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.  
[Radio buttons →](https://developer.android.com/develop/ui/compose/components/radio-button)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Radio buttons let the user select one option from a set of mutually exclusive
options. Use radio buttons if the user needs to see all available options
listed. If it's not necessary to show all options, use a
[spinner](https://developer.android.com/guide/topics/ui/controls/spinner) instead.
| **Note:** For a better user experience, see the Material Design [Radio
| button](https://m3.material.io/components/radio-button/overview) documentation.
![An example of radio buttons from material.io](https://lh3.googleusercontent.com/axlkVaJVMYP-eyhYyeGfy9OOtWQgrBbA3AvwyPc5muL8-_pjkzbvum1cHH8sNVES7fBsXyg3S8K9ptWH1LB_oyAbBdQ29N_Uurp9C7Mbc521gw=s0) **Figure 1.** An example of radio buttons from [Material
Design](https://m3.material.io/components/radio-button/overview).

To create each radio button option, create a
[RadioButton](https://developer.android.com/reference/android/widget/RadioButton)
in your layout. Because radio buttons are mutually exclusive, group them inside
a
[RadioGroup](https://developer.android.com/reference/android/widget/RadioGroup).
The system ensures that only one radio button within a group can be selected at
a time.

## Respond to click events

When the user selects a radio button, the corresponding
`RadioButton` object receives an on-click event.

The following example shows a reaction to the user tapping a
`RadioButton` object in a group:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<RadioGroup
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">
    <RadioButton android:id="@+id/radio_pirates"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Pirates"/>
    <RadioButton android:id="@+id/radio_ninjas"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Ninjas"/>
</RadioGroup>
```
| **Note:** `RadioGroup` is a subclass of [LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout) that has a vertical orientation by default.

Within the `Activity` or `Fragment` that hosts this
layout, find your radio buttons and set a change listener for each of them, as
follows:  

### Kotlin

```kotlin
findViewById<RadioButton>(R.id.radio_pirates).setOnCheckedChangeListener { buttonView, isChecked ->
    Log.d("RADIO", "Pirates is checked: $isChecked")
}

findViewById<RadioButton>(R.id.radio_ninjas).setOnCheckedChangeListener { buttonView, isChecked ->
    Log.d("RADIO", "Ninjas is checked: $isChecked")
}
```

### Java

```java
findViewById<RadioButton>(R.id.radio_pirates).setOnCheckedChangeListener { buttonView, isChecked ->
    Log.d("RADIO", "Pirates is checked: $isChecked");
}

findViewById<RadioButton>(R.id.radio_ninjas).setOnCheckedChangeListener { buttonView, isChecked ->
    Log.d("RADIO", "Ninjas is checked: $isChecked");
}
```

In this example, when the user taps one of the radio buttons, a message
prints in Logcat.
| **Tip:** If you need to change the radio button state yourself, use the [setChecked(boolean)](https://developer.android.com/reference/android/widget/CompoundButton#setChecked(boolean)) or [toggle()](https://developer.android.com/reference/android/widget/CompoundButton#toggle()) method.