---
title: https://developer.android.com/develop/ui/views/search/training/backward-compat
url: https://developer.android.com/develop/ui/views/search/training/backward-compat
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose. [Filter a list →](https://developer.android.com/develop/ui/compose/quick-guides/content/filter-list-while-typing) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The `https://developer.android.com/reference/android/widget/SearchView` and action bar are only available on Android 3.0 and
later. To support older platforms, you can fall back to the search dialog. The search dialog is a
system provided UI that overlays on top of your application when invoked.

## Set Minimum and Target API levels

To setup the search dialog, first declare in your manifest that you want to support older
devices, but want to target Android 3.0 or later versions. When you do this, your application
automatically uses the action bar on Android 3.0 or later and uses the traditional menu system on
older devices:

```xml
<uses-sdk android:minSdkVersion="7" android:targetSdkVersion="15" />

<application>
...
```

## Provide the Search Dialog for Older Devices

To invoke the search dialog on older devices, call `https://developer.android.com/reference/android/app/Activity#onSearchRequested()` whenever a user selects the search
menu item from the options menu. Because Android 3.0 and higher devices show the
`https://developer.android.com/reference/android/widget/SearchView` in the action bar (as demonstrated in the first lesson), only versions
older than 3.0 call `https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected(android.view.MenuItem)` when the
user selects the search menu item.

### Kotlin

```kotlin
override fun onOptionsItemSelected(item: MenuItem): Boolean {
    return when (item.itemId) {
        R.id.search -> {
            onSearchRequested()
            true
        }
        else -> false
    }
}
```

### Java

```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    switch (item.getItemId()) {
        case R.id.search:
            onSearchRequested();
            return true;
        default:
            return false;
    }
}
```

## Check the Android Build Version at Runtime

At runtime, check the device version to make sure an unsupported use of `https://developer.android.com/reference/android/widget/SearchView` does not occur on older devices. In our example code, this happens in
the `https://developer.android.com/reference/android/app/Activity#onCreateOptionsMenu(android.view.Menu)` method:

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu): Boolean {

    menuInflater.inflate(R.menu.options_menu, menu)

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        val searchManager = getSystemService(Context.SEARCH_SERVICE) as SearchManager
        (menu.findItem(R.id.search).actionView as SearchView).apply {
            setSearchableInfo(searchManager.getSearchableInfo(componentName))
            setIconifiedByDefault(false)
        }
    }
    return true
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {

    MenuInflater inflater = getMenuInflater();
    inflater.inflate(R.menu.options_menu, menu);

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        SearchManager searchManager =
                (SearchManager) getSystemService(Context.SEARCH_SERVICE);
        SearchView searchView =
                (SearchView) menu.findItem(R.id.search).getActionView();
        searchView.setSearchableInfo(
                searchManager.getSearchableInfo(getComponentName()));
        searchView.setIconifiedByDefault(false);
    }
    return true;
}
```