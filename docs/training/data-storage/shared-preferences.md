---
title: https://developer.android.com/training/data-storage/shared-preferences
url: https://developer.android.com/training/data-storage/shared-preferences
source: md.txt
---

# Save simple data with SharedPreferences

If you have a relatively small collection of key-values that you'd like to save, you can use the[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences)APIs. A`SharedPreferences`object points to a file containing key-value pairs and provides simple methods to read and write them. Each`SharedPreferences`file is managed by the framework and can be private or shared.

This page shows you how to use the`SharedPreferences`APIs to store and retrieve simple values.
| **Caution:** `DataStore`is a modern data storage solution that you should use instead of`SharedPreferences`. It builds on Kotlin coroutines and Flow, and overcomes many of the drawbacks of`SharedPreferences`.
|
| Read the[DataStore guide](https://developer.android.com/topic/libraries/architecture/datastore)for more information.
| **Note:** The`SharedPreferences`APIs are for reading and writing key-value pairs, and you shouldn't confuse them with the[`Preference`](https://developer.android.com/reference/android/preference/Preference)APIs, which help you build a user interface for your app settings (although they also use`SharedPreferences`to save the user's settings). For information about the[`Preference`](https://developer.android.com/reference/android/preference/Preference)APIs, see the[Settings developer guide](https://developer.android.com/guide/topics/ui/settings).

## Get a handle to shared preferences

You can create a new shared preference file or access an existing one by calling one of these methods:

- **[`getSharedPreferences()`](https://developer.android.com/reference/android/content/Context#getSharedPreferences(java.lang.String,%20int)):** Use this if you need multiple shared preference files identified by name, which you specify with the first parameter. You can call this from any[`Context`](https://developer.android.com/training/data-storage/shared-preferences#kotlin:%7E:text=this%20from%20any-,Context,-in%20your%20app)in your app.
- **[`getPreferences()`](https://developer.android.com/reference/android/app/Activity#getPreferences(int)):** Use this from an[`Activity`](https://developer.android.com/reference/android/app/Activity)if you need to use only one shared preference file for the activity. Because this retrieves a default shared preference file that belongs to the activity, you don't need to supply a name.

For example, the following code accesses the shared preferences file that's identified by the resource string`R.string.preference_file_key`and opens it using the private mode so the file is accessible by only your app:  

### Kotlin

```kotlin
val sharedPref = activity?.getSharedPreferences(
        getString(R.string.preference_file_key), Context.MODE_PRIVATE)
```

### Java

```java
Context context = getActivity();
SharedPreferences sharedPref = context.getSharedPreferences(
        getString(R.string.preference_file_key), Context.MODE_PRIVATE);
```

When naming your shared preference files, you should use a name that's uniquely identifiable to your app. A good way to do this is prefix the file name with your[application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id). For example:`"com.example.myapp.PREFERENCE_FILE_KEY"`

Alternatively, if you need just one shared preference file for your activity, you can use the[`getPreferences()`](https://developer.android.com/reference/android/app/Activity#getPreferences(int))method:  

### Kotlin

```kotlin
val sharedPref = activity?.getPreferences(Context.MODE_PRIVATE)
```

### Java

```java
SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
```
| **Caution:** The[`MODE_WORLD_READABLE`](https://developer.android.com/reference/android/content/Context#MODE_WORLD_READABLE)and[`MODE_WORLD_WRITEABLE`](https://developer.android.com/reference/android/content/Context#MODE_WORLD_WRITEABLE)modes have been deprecated since API level 17.
|
| Starting with Android 7.0 (API level 24), Android throws a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)if you use them. If your app needs to share private files with other apps, it may use a[`FileProvider`](https://developer.android.com/reference/androidx/core/content/FileProvider)with the[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION). For more information, also see[Sharing Files](https://developer.android.com/training/secure-file-sharing).

If you're using the`SharedPreferences`API to save app settings, you should instead use[`getDefaultSharedPreferences()`](https://developer.android.com/reference/android/preference/PreferenceManager#getDefaultSharedPreferences(android.content.Context))to get the default shared preference file for your entire app. For more information, see the[Settings developer guide](https://developer.android.com/guide/topics/ui/settings).

## Write to shared preferences

To write to a shared preferences file, create a[`SharedPreferences.Editor`](https://developer.android.com/reference/android/content/SharedPreferences.Editor)by calling[`edit()`](https://developer.android.com/reference/android/content/SharedPreferences#edit())on your`SharedPreferences`.

Pass the keys and values you want to write with methods such as:[`putInt()`](https://developer.android.com/reference/android/content/SharedPreferences.Editor#putInt())and[`putString()`](https://developer.android.com/reference/android/content/SharedPreferences.Editor#putString()). Then call[`apply()`](https://developer.android.com/reference/android/content/SharedPreferences.Editor#apply())or[`commit()`](https://developer.android.com/reference/android/content/SharedPreferences.Editor#commit())to save the changes. For example:  

### Kotlin

```kotlin
val sharedPref = activity?.getPreferences(Context.MODE_PRIVATE) ?: return
with (sharedPref.edit()) {
    putInt(getString(R.string.saved_high_score_key), newHighScore)
    apply()
}
```

### Java

```java
SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
SharedPreferences.Editor editor = sharedPref.edit();
editor.putInt(getString(R.string.saved_high_score_key), newHighScore);
editor.apply();
```

`apply()`changes the in-memory`SharedPreferences`object immediately but writes the updates to disk asynchronously. Alternatively, you can use`commit()`to write the data to disk synchronously. But because`commit()`is synchronous, you should avoid calling it from your main thread because it could pause your UI rendering.

## Read from shared preferences

To retrieve values from a shared preferences file, call methods such as[`getInt()`](https://developer.android.com/reference/android/content/SharedPreferences#getInt(java.lang.String,%20int))and[`getString()`](https://developer.android.com/reference/android/content/SharedPreferences#getString(java.lang.String,%20java.lang.String)), providing the key for the value you want, and optionally a default value to return if the key isn't present. For example:  

### Kotlin

```kotlin
val sharedPref = activity?.getPreferences(Context.MODE_PRIVATE) ?: return
val defaultValue = resources.getInteger(R.integer.saved_high_score_default_key)
val highScore = sharedPref.getInt(getString(R.string.saved_high_score_key), defaultValue)
```

### Java

```java
SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
int defaultValue = getResources().getInteger(R.integer.saved_high_score_default_key);
int highScore = sharedPref.getInt(getString(R.string.saved_high_score_key), defaultValue);
```