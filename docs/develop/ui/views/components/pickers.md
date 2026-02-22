---
title: https://developer.android.com/develop/ui/views/components/pickers
url: https://developer.android.com/develop/ui/views/components/pickers
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.  
[Date pickers →](https://developer.android.com/develop/ui/compose/components/datepickers)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Android provides controls for the user to pick a time or date as
ready-to-use dialogs. These *pickers* provide controls for selecting each
part of the time (hour, minute, AM/PM) or date (month, day, year).
| **Note:** For a better user experience, see the Material Design [date
| picker](https://m3.material.io/components/date-pickers/overview) and [time
| picker](https://m3.material.io/components/time-pickers/overview) documentation.
![An example of time picker from material.io](https://lh3.googleusercontent.com/zc0VQbWKABZLd8xag4YoJd_oHUvxJoEz3s3UHlVPYU4oT_Tlrh9F5r-546Hf_AOfEEbA-iCxEJgAFBeuLvwGRs4F_guyW1JZob_WhMR5CMukcQ=s0) **Figure 1.** Hour selection in a mobile calendar picker.

Using these pickers helps ensure that your users can pick a time or date that
is valid, formatted correctly, and adjusted to the user's locale.
![An example of modal date picker from material.io](https://lh3.googleusercontent.com/cEgaDjOwIz7l1a2E7vuBocyVDbpSsBtkVG5iQepRyiaoSzTZbL5JWbywwxKf1KLCPFFnfLbZ5Vnm3dT9HDczHCXyGOxqudikKXFe7miiuQg=s0) **Figure 2.** Modal date picker.

We recommend you use
[DialogFragment](https://developer.android.com/reference/androidx/fragment/app/DialogFragment)
to host each time or date picker. The `DialogFragment` manages the
dialog lifecycle for you and lets you display pickers in different layout
configurations, such as in a basic dialog on handsets or as an embedded part of
the layout on large screens.

## Create a time picker

To display a
[TimePickerDialog](https://developer.android.com/reference/android/app/TimePickerDialog)
using `DialogFragment`, define a fragment class that extends
`DialogFragment` and return a `TimePickerDialog` from the
fragment's
[onCreateDialog()](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onCreateDialog(android.os.Bundle))
method.

### Extend DialogFragment for a time picker

To define a `DialogFragment` for a `TimePickerDialog`,
do the following:

- Define the `onCreateDialog()` method to return an instance of `TimePickerDialog`.
- Implement the [TimePickerDialog.OnTimeSetListener](https://developer.android.com/reference/android/app/TimePickerDialog.OnTimeSetListener) interface to receive a callback when the user sets the time.

Here's an example:  

### Kotlin

```kotlin
class TimePickerFragment : DialogFragment(), TimePickerDialog.OnTimeSetListener {

    override fun onCreateDialog(savedInstanceState: Bundle): Dialog {
        // Use the current time as the default values for the picker.
        val c = Calendar.getInstance()
        val hour = c.get(Calendar.HOUR_OF_DAY)
        val minute = c.get(Calendar.MINUTE)

        // Create a new instance of TimePickerDialog and return it.
        return TimePickerDialog(activity, this, hour, minute, DateFormat.is24HourFormat(activity))
    }

    override fun onTimeSet(view: TimePicker, hourOfDay: Int, minute: Int) {
        // Do something with the time the user picks.
    }
}
```

### Java

```java
public static class TimePickerFragment extends DialogFragment
                            implements TimePickerDialog.OnTimeSetListener {

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        // Use the current time as the default values for the picker.
        final Calendar c = Calendar.getInstance();
        int hour = c.get(Calendar.HOUR_OF_DAY);
        int minute = c.get(Calendar.MINUTE);

        // Create a new instance of TimePickerDialog and return it.
        return new TimePickerDialog(getActivity(), this, hour, minute,
                DateFormat.is24HourFormat(getActivity()));
    }

    public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
        // Do something with the time the user picks.
    }
}
```

See the `TimePickerDialog` class for information about the
constructor arguments.

Now you just need an event that adds an instance of this fragment to your
activity.

### Show the time picker

After you define a `DialogFragment` like the one in the preceding
example, you can display the time picker by creating an instance of the
`DialogFragment` and calling the
[show()](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#show(androidx.fragment.app.FragmentManager,java.lang.String))
method.

For example, here's a button that, when tapped, calls a method to show the
dialog:  

```xml
<Button
    android:id="@+id/pickTime"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pick time" />
```

When the user taps this button, the system calls the following method:  

### Kotlin

```kotlin
findViewById<Button>(R.id.pickTime).setOnClickListener {
    TimePickerFragment().show(supportFragmentManager, "timePicker")
}
```

### Java

```java
findViewById<Button>(R.id.pickTime).setOnClickListener {
    TimePickerFragment().show(supportFragmentManager, "timePicker");
}
```

This method calls `show()` on a new instance of the
`DialogFragment` defined in the preceding example. The
`show()` method requires an instance of
[FragmentManager](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)
and a unique tag name for the fragment.

## Create a date picker

Creating a
[DatePickerDialog](https://developer.android.com/reference/android/app/DatePickerDialog)
is like creating a `TimePickerDialog`. The difference is the dialog
you create for the fragment.

To display a `DatePickerDialog` using `DialogFragment`,
define a fragment class that extends `DialogFragment` and return a
`DatePickerDialog` from the fragment's `onCreateDialog()`
method.

### Extend DialogFragment for a date picker

To define a `DialogFragment` for a `DatePickerDialog`,
do the following:

- Define the `onCreateDialog()` method to return an instance of `DatePickerDialog`.
- Implement the [DatePickerDialog.OnDateSetListener](https://developer.android.com/reference/android/app/DatePickerDialog.OnDateSetListener) interface to receive a callback when the user sets the date.

Here's an example:  

### Kotlin

```kotlin
class DatePickerFragment : DialogFragment(), DatePickerDialog.OnDateSetListener {

    override fun onCreateDialog(savedInstanceState: Bundle): Dialog {
        // Use the current date as the default date in the picker.
        val c = Calendar.getInstance()
        val year = c.get(Calendar.YEAR)
        val month = c.get(Calendar.MONTH)
        val day = c.get(Calendar.DAY_OF_MONTH)

        // Create a new instance of DatePickerDialog and return it.
        return DatePickerDialog(requireContext(), this, year, month, day)

    }

    override fun onDateSet(view: DatePicker, year: Int, month: Int, day: Int) {
        // Do something with the date the user picks.
    }
}
```

### Java

```java
public static class DatePickerFragment extends DialogFragment
                            implements DatePickerDialog.OnDateSetListener {

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        // Use the current date as the default date in the picker.
        final Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        int month = c.get(Calendar.MONTH);
        int day = c.get(Calendar.DAY_OF_MONTH);

        // Create a new instance of DatePickerDialog and return it.
        return new DatePickerDialog(requireContext(), this, year, month, day);
    }

    public void onDateSet(DatePicker view, int year, int month, int day) {
        // Do something with the date the user picks.
    }
}
```

See the
[DatePickerDialog](https://developer.android.com/reference/android/app/DatePickerDialog)
class for information about the constructor arguments.

You just need an event that adds an instance of this fragment to your
activity.

### Show the date picker

After you define a `DialogFragment` like the preceding example,
you can display the date picker by creating an instance of the
`DialogFragment` and calling `show()`.

For example, here's a button that, when tapped, calls a method to show the
dialog:  

```xml
<Button
    android:id="@+id/pickDate"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pick date"/>
```

When the user taps this button, the system calls the following method:  

### Kotlin

```kotlin
findViewById<Button>(R.id.pickDate).setOnClickListener {
    val newFragment = DatePickerFragment()
    newFragment.show(supportFragmentManager, "datePicker")
}
```

### Java

```java
findViewById<Button>(R.id.pickDate).setOnClickListener {
    val newFragment = DatePickerFragment();
    newFragment.show(supportFragmentManager, "datePicker");
}
```

This method calls `show()` on a new instance of the
`DialogFragment` defined in the preceding example. The
`show()` method requires an instance of `FragmentManager`
and a unique tag name for the fragment.

## Use pickers with autofill

In 2017, Android introduced the
[Autofill framework](https://developer.android.com/guide/topics/text/autofill), which lets
users save data that can be used to fill out forms in different apps. Pickers
can be useful in autofill scenarios by providing a UI that lets users change the
value of a field that stores date or time data. For example, in a credit card
form, a date picker lets users enter or change the expiration date of their
credit card.

Because pickers are dialogs, they aren't displayed in an activity along with
other fields. To display the picker data when the picker isn't visible, you can
use another view, such as an
[EditText](https://developer.android.com/reference/android/widget/EditText),
which can display the value when the picker isn't visible.

An `EditText` object natively expects autofill data of type
[AUTOFILL_TYPE_TEXT](https://developer.android.com/reference/android/view/View#AUTOFILL_TYPE_TEXT).
In contrast, autofill services save the data as
[AUTOFILL_TYPE_DATE](https://developer.android.com/reference/android/view/View#AUTOFILL_TYPE_DATE)
to create an appropriate representation of it. To solve the inconsistency in
types, we recommended that you create a custom view that inherits from
`EditText` and implements the methods required to correctly handle
values of type `AUTOFILL_TYPE_DATE`.

Take the following steps to create a subclass of `EditText` that
can handle values of type `AUTOFILL_TYPE_DATE`:

1. Create a class that inherits from `EditText`.
2. Implement the [getAutofillType()](https://developer.android.com/reference/android/view/View#getAutofillType()) method, which returns `AUTOFILL_TYPE_DATE`.
3. Implement the [getAutofillValue()](https://developer.android.com/reference/android/view/View#getAutofillValue()) method, which returns an [AutofillValue](https://developer.android.com/reference/android/view/autofill/AutofillValue) object that represents the date in milliseconds. To create the return object, use the [forDate()](https://developer.android.com/reference/android/view/autofill/AutofillValue#forDate(long)) method to generate an `AutofillValue` object.
4. Implement the [autofill()](https://developer.android.com/reference/android/view/View#autofill(android.view.autofill.AutofillValue)) method. This method provides the logic to handle the `AutofillValue` parameter, which is of type `AUTOFILL_TYPE_DATE`. To handle the parameter, create a proper string representation of it, such as `mm/yyyy`. Use the string representation to set the `text` property of your view.
5. Implement functionality that displays a picker when the user wants to edit the date in the custom subclass of `EditText`. The view updates the `text` property with a string representation of the value that the user selects on the picker.

For an example of a subclass of `EditText` that handles
`AUTOFILL_TYPE_DATE` values, see the Autofill Framework sample in
[Java](https://github.com/android/input-samples/tree/main/AutofillFramework)
or
[Kotlin](https://github.com/android/input-samples/tree/main/AutofillFrameworkKotlin).

To learn more about proving autofill support for your custom views, see
[Autofill framework](https://developer.android.com/guide/topics/text/autofill#support_for_custom_views).