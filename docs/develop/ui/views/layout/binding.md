---
title: AdapterView  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/layout/binding
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# AdapterView Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.

[Lists and Grids →](https://developer.android.com/jetpack/compose/lists#lazy)

![](/static/images/android-compose-ui-logo.png)

`AdapterView` is a [`ViewGroup`](/reference/android/view/ViewGroup) that displays items loaded into an adapter. The
most common type of adapter comes from an array-based data source.

This guide shows how to complete several key steps related to setting up
an adapter.

## Fill the layout with data

To add data into the layout that you create in your app's UI, add code
similar to the following:

### Kotlin

```
val PROJECTION = arrayOf(Contacts.People._ID, People.NAME)
...

// Get a Spinner and bind it to an ArrayAdapter that
// references a String array.
val spinner1: Spinner = findViewById(R.id.spinner1)
val adapter1 = ArrayAdapter.createFromResource(
        this, R.array.colors, android.R.layout.simple_spinner_item)
adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
spinner1.adapter = adapter1

// Load a Spinner and bind it to a data query.
val spinner2: Spinner = findViewById(R.id.spinner2)
val cursor: Cursor = managedQuery(People.CONTENT_URI, PROJECTION, null, null, null)
val adapter2 = SimpleCursorAdapter(this,
        // Use a template that displays a text view
        android.R.layout.simple_spinner_item,
        // Give the cursor to the list adapter
        cursor,
        // Map the NAME column in the people database to...
        arrayOf(People.NAME),
        // The "text1" view defined in the XML template
        intArrayOf(android.R.id.text1))
adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
spinner2.adapter = adapter2
```

### Java

```
// Get a Spinner and bind it to an ArrayAdapter that
// references a String array.
Spinner s1 = (Spinner) findViewById(R.id.spinner1);
ArrayAdapter adapter = ArrayAdapter.createFromResource(
    this, R.array.colors, android.R.layout.simple_spinner_item);
adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
s1.setAdapter(adapter);

// Load a Spinner and bind it to a data query.
private static String[] PROJECTION = new String[] {
        People._ID, People.NAME
    };

Spinner s2 = (Spinner) findViewById(R.id.spinner2);
Cursor cur = managedQuery(People.CONTENT_URI, PROJECTION, null, null);

SimpleCursorAdapter adapter2 = new SimpleCursorAdapter(this,
    android.R.layout.simple_spinner_item, // Use a template
                                          // that displays a
                                          // text view
    cur, // Give the cursor to the list adapter
    new String[] {People.NAME}, // Map the NAME column in the
                                         // people database to...
    new int[] {android.R.id.text1}); // The "text1" view defined in
                                     // the XML template

adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
s2.setAdapter(adapter2);
```

Note that it is necessary to have the People.\_ID column in projection used with CursorAdapter
or else you will get an exception.

If, during the course of your application's life, you change the underlying data that is read by your Adapter,
you should call `notifyDataSetChanged()`. This will notify the attached View
that the data has been changed and it should refresh itself.

**Note:** With Android Studio 3.6 and higher, the
[view binding](/topic/libraries/view-binding) feature can replace
`findViewById()` calls and provides compile-time type safety for
code that interacts with views. Consider using view binding instead of
`findViewById()`.

## Handle user selections

You handle the user's selection by setting the class's `AdapterView.OnItemClickListener` member to a listener and
catching the selection changes.

### Kotlin

```
val historyView: ListView = findViewById(R.id.history)
historyView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
    Toast.makeText(context, "You've got an event", Toast.LENGTH_SHORT).show()
}
```

### Java

```
// Create a message handling object as an anonymous class.
private OnItemClickListener messageClickedHandler = new OnItemClickListener() {
    public void onItemClick(AdapterView parent, View v, int position, long id)
    {
        // Display a messagebox.
        Toast.makeText(context,"You've got an event",Toast.LENGTH_SHORT).show();
    }
};

// Now hook into our object and set its onItemClickListener member
// to our class handler object.
historyView = (ListView)findViewById(R.id.history);
historyView.setOnItemClickListener(messageClickedHandler);
```

For more discussion see the [Spinner](/guide/topics/ui/controls/spinner) topic.