---
title: Add spinners to your app  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/spinner
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add spinners to your app Stay organized with collections Save and categorize content based on your preferences.



Spinners provide a quick way to select one value from a set. In the default
state, a spinner shows its currently selected value. Tapping the spinner
displays a menu showing all other values the user can select.

![](/static/images/ui/spinner.png)


**Figure 1.** A menu from a spinner, showing the available
values.

You can add a spinner to your layout with the
`Spinner`
object, which you usually do in your XML layout with a
`<Spinner>` element. This is shown in the following
example:

```
<Spinner
    android:id="@+id/planets_spinner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

To populate the spinner with a list of choices, specify a
`SpinnerAdapter`
in your
`Activity` or
`Fragment`
source code.

If you are using Material Design Components,
[exposed
dropdown menus](https://www.material.io/components/menus/android#exposed-dropdown-menus) are the equivalent of a `Spinner`.

## Populate the spinner with user choices

The choices you provide for the spinner can come from any source, but you
must provide them through a `SpinnerAdapter`, such as an
`ArrayAdapter`
if the choices are available in an array or a
`CursorAdapter`
if the choices are available from a database query.

For example, if the available choices for your spinner are pre-determined,
you can provide them with a string array defined in a
[string resource
file](/guide/topics/resources/string-resource):

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="planets_array">
        <item>Mercury</item>
        <item>Venus</item>
        <item>Earth</item>
        <item>Mars</item>
        <item>Jupiter</item>
        <item>Saturn</item>
        <item>Uranus</item>
        <item>Neptune</item>
    </string-array>
</resources>
```

With an array like this, you can use the following code in your
`Activity` or `Fragment` to supply the spinner with the
array using an instance of `ArrayAdapter`:

### Kotlin

```
val spinner: Spinner = findViewById(R.id.planets_spinner)
// Create an ArrayAdapter using the string array and a default spinner layout.
ArrayAdapter.createFromResource(
        this,
        R.array.planets_array,
        android.R.layout.simple_spinner_item
).also { adapter ->
    // Specify the layout to use when the list of choices appears.
    adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
    // Apply the adapter to the spinner.
    spinner.adapter = adapter
}
```

### Java

```
Spinner spinner = (Spinner) findViewById(R.id.planets_spinner);
// Create an ArrayAdapter using the string array and a default spinner layout.
ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(
        this,
        R.array.planets_array,
        android.R.layout.simple_spinner_item
);
// Specify the layout to use when the list of choices appears.
adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
// Apply the adapter to the spinner.
spinner.setAdapter(adapter);
```

The
`createFromResource()`
method lets you create an `ArrayAdapter` from the string array. The
third argument for this method is a layout resource that defines how the
selected choice appears in the spinner control. The platform provides the
`simple_spinner_item`
layout. This is the default layout unless you want to define your own layout for
the spinner's appearance.

Call
`setDropDownViewResource(int)`
to specify the layout the adapter uses to display the list of spinner choices.
`simple_spinner_dropdown_item`
is another standard layout defined by the platform.

Call
`setAdapter()`
to apply the adapter to your `Spinner`.

## Respond to user selections

When the user selects an item from the spinner's menu, the
`Spinner` object
receives an on-item-selected event.

To define the selection event handler for a spinner, implement the
[`AdapterView.OnItemSelectedListener`](/reference/android/widget/AdapterView.OnItemSelectedListener)
interface and the corresponding
`onItemSelected()`
callback method. For example, here's an implementation of the interface in an
`Activity`:

### Kotlin

```
class SpinnerActivity : Activity(), AdapterView.OnItemSelectedListener {
    ...
    override fun onItemSelected(parent: AdapterView<*>, view: View?, pos: Int, id: Long) {
        // An item is selected. You can retrieve the selected item using
        // parent.getItemAtPosition(pos).
    }

    override fun onNothingSelected(parent: AdapterView<*>) {
        // Another interface callback.
    }
}
```

### Java

```
public class SpinnerActivity extends Activity implements OnItemSelectedListener {
    ...
    public void onItemSelected(AdapterView<?> parent, View view,
            int pos, long id) {
        // An item is selected. You can retrieve the selected item using
        // parent.getItemAtPosition(pos).
    }

    public void onNothingSelected(AdapterView<?> parent) {
        // Another interface callback.
    }
}
```

The
`AdapterView.OnItemSelectedListener` interface requires the
`onItemSelected()` and
`onNothingSelected()`
callback methods.

Specify the interface implementation by calling
`setOnItemSelectedListener()`:

### Kotlin

```
val spinner: Spinner = findViewById(R.id.planets_spinner)
spinner.onItemSelectedListener = this
```

### Java

```
Spinner spinner = (Spinner) findViewById(R.id.planets_spinner);
spinner.setOnItemSelectedListener(this);
```

If you implement the `AdapterView.OnItemSelectedListener`
interface with your `Activity` or `Fragment`, as in the
preceding example, you can pass `this` as the interface instance.