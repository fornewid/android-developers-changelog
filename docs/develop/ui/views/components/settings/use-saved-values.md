---
title: https://developer.android.com/develop/ui/views/components/settings/use-saved-values
url: https://developer.android.com/develop/ui/views/components/settings/use-saved-values
source: md.txt
---

# Use saved Preference values
Part of [Android Jetpack](https://developer.android.com/jetpack).

This document describes how to store and use
[`Preference`](https://developer.android.com/jetpack/androidx/releases/preference) values that are saved by
the Preference library.

## Preference data storage

This section describes how a `Preference` can persist data.

### SharedPreferences

By default, a `Preference` uses
[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences) to save
values. The `SharedPreferences` API supports reading and writing simple
key-value pairs from a file that is saved across application sessions. The
Preference library uses a private `SharedPreferences` instance so that only your
application can access it.

As an example, assume the following
[`SwitchPreferenceCompat`](https://developer.android.com/reference/androidx/preference/SwitchPreferenceCompat):

```xml
<SwitchPreferenceCompat
        app:key="notifications"
        app:title="Enable message notifications"/>
```

When a user toggles this switch to the "on" state, the `SharedPreferences` file
updates with a key-value pair of `"notifications" : "true"`. The key used is the
same as the key set for the `Preference`.

For more information about the `SharedPreferences` API, see [Save key-value
data](https://developer.android.com/training/data-storage/shared-preferences).

For information about the different ways of storing data on Android, see [Data
and file storage overview](https://developer.android.com/guide/topics/data/data-storage).

### PreferenceDataStore

Although the Preference library persists data with `SharedPreferences` by
default, `SharedPreferences` aren't always an ideal solution. For example, if
your application requires a user to sign in, you might want to persist
application settings in the cloud so that the settings are reflected across
other devices and platforms. Similarly, if your application has configuration
options that are device-specific, each user on the device has separate settings,
making `SharedPreferences` a less-than-ideal solution.

A [`PreferenceDataStore`](https://developer.android.com/reference/androidx/preference/PreferenceDataStore)
lets you use a custom storage backend to persist `Preference` values. For more
information, see [Use a custom datastore](https://developer.android.com/develop/ui/views/components/settings/use-saved-values#custom-data-store).

## Read Preference values

To retrieve the `SharedPreferences` object that is being used, call
[`PreferenceManager.getDefaultSharedPreferences()`](https://developer.android.com/reference/androidx/preference/PreferenceManager#getDefaultSharedPreferences(android.content.Context)).
Although this method works from anywhere in your application, we recommend that
you split your app into layers. For more information, see [Data
layer](https://developer.android.com/topic/architecture/data-layer).

For example, given an `EditTextPreference` with a key of `"signature"`, as
follows:

```xml
<EditTextPreference
        app:key="signature"
        app:title="Your signature"/>
```

You can retrieve the saved value for this `Preference` globally, as follows:

### Kotlin

```kotlin
val sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this /* Activity context */)
val name = sharedPreferences.getString("signature", "")
```

### Java

```java
SharedPreferences sharedPreferences =
        PreferenceManager.getDefaultSharedPreferences(this /* Activity context */);
String name = sharedPreferences.getString("signature", "");
```

## Listen for changes to Preference values

To listen for changes to `Preference` values, you can choose between two
interfaces:

- [`Preference.OnPreferenceChangeListener`](https://developer.android.com/reference/androidx/preference/Preference.OnPreferenceChangeListener)
- [`SharedPreferences.OnSharedPreferenceChangeListener`](https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener)

The following table shows how the two interfaces differ:

| `OnPreferenceChangeListener` | `OnSharedPreferenceChangeListener` |
|---|---|
| Set on a single `Preference`. | Applies to all `Preference` objects. |
| Called when a `Preference` is about to change its saved value, even if the pending value is the same as the saved value. | Called only when the value saved for a `Preference` changes. |
| Only called through the `Preference` library. A separate part of the application can change the saved value. | Called whenever the saved value changes, even if it is from a separate part of the application. |
| Called before the pending value is saved. | Called after the value is saved. |
| Called when using `SharedPreferences` or a `PreferenceDataStore`. | Called only when using `SharedPreferences`. |

### Implement OnPreferenceChangeListener

Implementing an `OnPreferenceChangeListener` lets you listen for a pending
change to the value of a `Preference`. Then, you can validate whether the change
occurs. For example, the following code shows how to listen for a change to the
value of an `EditTextPreference` with a key of `"name"`:

### Kotlin

```kotlin
override fun onPreferenceChange(preference: Preference, newValue: Any): Boolean {
    Log.e("preference", "Pending Preference value is: $newValue")
    return true
}
```

### Java

```java
@Override
public boolean onPreferenceChange(Preference preference, Object newValue) {
    Log.e("preference", "Pending Preference value is: " + newValue);
    return true;
}
```

Next, you need to set this listener directly with
[`setOnPreferenceChangeListener()`](https://developer.android.com/reference/androidx/preference/Preference#setOnPreferenceChangeListener(androidx.preference.Preference.OnPreferenceChangeListener)),
as follows:

### Kotlin

```kotlin
preference.onPreferenceChangeListener = ...
```

### Java

```java
preference.setOnPreferenceChangeListener(...);
```

### Implement OnSharedPreferenceChangeListener

When persisting `Preference` values using `SharedPreferences`, you can also use
a `SharedPreferences.OnSharedPreferenceChangeListener` to listen for changes.
This lets you listen for when the values saved by your `Preference` are changed,
such as when syncing settings with a server. The following example shows how to
listen for a change to the value of an `EditTextPreference` with a key of
`"name"`:

### Kotlin

```kotlin
override fun onSharedPreferenceChanged(sharedPreferences: SharedPreferences, key: String) {
    if (key == "signature") {
        Log.i(TAG, "Preference value was updated to: " + sharedPreferences.getString(key, ""))
    }
}
```

### Java

```java
@Override
public void onSharedPreferenceChanged(SharedPreferences sharedPreferences, String key) {
    if (key.equals("signature")) {
        Log.i(TAG, "Preference value was updated to: " + sharedPreferences.getString(key, ""));
    }
}
```

Register the listener using
[`registerOnSharedPreferenceChangedListener()`](https://developer.android.com/reference/android/content/SharedPreferences#registerOnSharedPreferenceChangeListener(android.content.SharedPreferences.OnSharedPreferenceChangeListener)),
as follows:

### Kotlin

```kotlin
preferenceManager.sharedPreferences.registerOnSharedPreferenceChangeListener(...)
```

### Java

```java
getPreferenceManager().getSharedPreferences().registerOnSharedPreferenceChangeListener(...);
```

> [!WARNING]
> **Warning:** To prevent unintended garbage collection, store a strong reference to the listener. When you call `registerOnSharedPreferenceChangeListener()`, the `SharedPreferenceManager` doesn't store a strong reference to the listener. To address this, you can implement `onSharedPreferenceChanged()` directly in your `PreferenceFragmentCompat`. You can also create an instance variable, as shown in the following example:

<br />

### Kotlin

```kotlin
    val listener: SharedPreferences.OnSharedPreferenceChangeListener =
            SharedPreferences.OnSharedPreferenceChangeListener {...}
    
```

### Java

```java
    SharedPreferences.OnSharedPreferenceChangeListener listener =
            new SharedPreferences.OnSharedPreferenceChangeListener() {...}
    
```

<br />

For proper lifecycle management in your `Activity` or `Fragment`, register and
unregister this listener in the `onResume()` and `onPause()` callbacks, as shown
in the following example:

### Kotlin

```kotlin
override fun onResume() {
    super.onResume()
    preferenceManager.sharedPreferences.registerOnSharedPreferenceChangeListener(this)
}

override fun onPause() {
    super.onPause()
    preferenceManager.sharedPreferences.unregisterOnSharedPreferenceChangeListener(this)
}
```

### Java

```java
@Override
public void onResume() {
    super.onResume();
    getPreferenceManager().getSharedPreferences().registerOnSharedPreferenceChangeListener(this);
}

@Override
public void onPause() {
    super.onPause();
    getPreferenceManager().getSharedPreferences().unregisterOnSharedPreferenceChangeListener(this);
}
```

## Use a custom datastore

Although we recommend persisting `Preference` objects using `SharedPreferences`,
you can also use a custom datastore. A custom datastore can be useful if your
application persists values to a database or if values are device-specific, as
shown in the following examples.

### Implement the datastore

To implement a custom datastore, create a class that extends
`PreferenceDataStore`. The following example creates a datastore that handles
`String` values:

### Kotlin

```kotlin
class DataStore : PreferenceDataStore() {
    override fun putString(key: String, value: String?) {
        // Save the value somewhere.
    }

    override fun getString(key: String, defValue: String?): String? {
        // Retrieve the value.
    }
}
```

### Java

```java
public class DataStore extends PreferenceDataStore {
    @Override
    public void putString(String key, @Nullable String value) {
        // Save the value somewhere.
    }
    @Override
    @Nullable
    public String getString(String key, @Nullable String defValue) {
        // Retrieve the value.
    }
}
```

> [!NOTE]
> **Note:** Only override methods that are used by your `Preference` objects. Calling a method that you didn't implement results in an `UnsupportedOperationException`.

Run any time-consuming operations off the main thread to avoid blocking the user
interface. Since it's possible for the `Fragment` or `Activity` containing the
datastore to be destroyed while persisting a value, serialize the data so you
don't lose any values changed by the user.

### Enable the datastore

After you implement your datastore, set the new datastore in
`onCreatePreferences()` so that `Preference` objects persist values with the
datastore instead of using the default `SharedPreferences`. You can enable a
datastore for each `Preference` or for the entire hierarchy.

To enable a custom datastore for a specific `Preference`, call
[`setPreferenceDataStore()`](https://developer.android.com/reference/androidx/preference/Preference#setPreferenceDataStore(androidx.preference.PreferenceDataStore))
on the `Preference`, as shown in the following example:

### Kotlin

```kotlin
val preference: Preference? = findPreference("key")
preference?.preferenceDataStore = dataStore
```

### Java

```java
Preference preference = findPreference("key");
if (preference != null) {
    preference.setPreferenceDataStore(dataStore);
}
```

To enable a custom datastore for an entire hierarchy, call
`setPreferenceDataStore()` on the `PreferenceManager`:

### Kotlin

```kotlin
val preferenceManager = preferenceManager
preferenceManager.preferenceDataStore = dataStore
```

### Java

```java
PreferenceManager preferenceManager = getPreferenceManager();
preferenceManager.setPreferenceDataStore(dataStore);
```

A datastore that is set for a specific `Preference` overrides any datastore that
is set for the corresponding hierarchy. In most cases, you set a datastore for
the whole hierarchy.

> [!NOTE]
> **Note:** If you set a datastore for a `Preference` after the `Preference` is attached to the hierarchy, the initial value for the `Preference` isn't propagated again.