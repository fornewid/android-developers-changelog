---
title: https://developer.android.com/develop/ui/views/components/spinner
url: https://developer.android.com/develop/ui/views/components/spinner
source: md.txt
---

Spinners provide a quick way to select one value from a set. In the default
state, a spinner shows its currently selected value. Tapping the spinner
displays a menu showing all other values the user can select.
![](https://developer.android.com/static/images/ui/spinner.png) **Figure 1.** A menu from a spinner, showing the available values.

You can add a spinner to your layout with the
`https://developer.android.com/reference/android/widget/Spinner`
object, which you usually do in your XML layout with a
`<Spinner>` element. This is shown in the following
example:

```xml
<Spinner
    android:id="@+id/planets_spinner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

To populate the spinner with a list of choices, specify a
`https://developer.android.com/reference/android/widget/SpinnerAdapter`
in your
`https://developer.android.com/reference/android/app/Activity` or
`https://developer.android.com/reference/androidx/fragment/app/Fragment`
source code.

If you are using Material Design Components,
[exposed
dropdown menus](https://www.material.io/components/menus/android#exposed-dropdown-menus) are the equivalent of a `Spinner`.

## Populate the spinner with user choices

The choices you provide for the spinner can come from any source, but you
must provide them through a `SpinnerAdapter`, such as an
`https://developer.android.com/reference/android/widget/ArrayAdapter`
if the choices are available in an array or a
`https://developer.android.com/reference/android/widget/CursorAdapter`
if the choices are available from a database query.

For example, if the available choices for your spinner are pre-determined,
you can provide them with a string array defined in a
[string resource
file](https://developer.android.com/guide/topics/resources/string-resource):

```xml
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

```kotlin
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

```java
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
`https://developer.android.com/reference/android/widget/ArrayAdapter#createFromResource(android.content.Context, int, int)`
method lets you create an `ArrayAdapter` from the string array. The
third argument for this method is a layout resource that defines how the
selected choice appears in the spinner control. The platform provides the
`https://developer.android.com/reference/android/R.layout#simple_spinner_item`
layout. This is the default layout unless you want to define your own layout for
the spinner's appearance.

Call
`https://developer.android.com/reference/android/widget/ArrayAdapter#setDropDownViewResource(int)`
to specify the layout the adapter uses to display the list of spinner choices.
`https://developer.android.com/reference/android/R.layout#simple_spinner_dropdown_item`
is another standard layout defined by the platform.

Call
`https://developer.android.com/reference/android/widget/AdapterView#setAdapter(T)`
to apply the adapter to your `Spinner`.

## Respond to user selections

When the user selects an item from the spinner's menu, the
`https://developer.android.com/reference/android/widget/Spinner` object
receives an on-item-selected event.

To define the selection event handler for a spinner, implement the
[`AdapterView.OnItemSelectedListener`](https://developer.android.com/reference/android/widget/AdapterView.OnItemSelectedListener)
interface and the corresponding
`https://developer.android.com/reference/android/widget/AdapterView.OnItemSelectedListener#onItemSelected(android.widget.AdapterView<?>, android.view.View, int, long)`
callback method. For example, here's an implementation of the interface in an
`Activity`:

### Kotlin

```kotlin
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

```java
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
`https://developer.android.com/reference/android/widget/AdapterView.OnItemSelectedListener#onNothingSelected(android.widget.AdapterView<?>)`
callback methods.

Specify the interface implementation by calling
`https://developer.android.com/reference/android/widget/AdapterView#setOnItemSelectedListener(android.widget.AdapterView.OnItemSelectedListener)`:

### Kotlin

```kotlin
val spinner: Spinner = findViewById(R.id.planets_spinner)
spinner.onItemSelectedListener = this
```

### Java

```java
Spinner spinner = (Spinner) findViewById(R.id.planets_spinner);
spinner.setOnItemSelectedListener(this);
```

If you implement the `AdapterView.OnItemSelectedListener`
interface with your `Activity` or `Fragment`, as in the
preceding example, you can pass `this` as the interface instance.