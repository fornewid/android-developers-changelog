---
title: https://developer.android.com/training/secure-file-sharing/share-file
url: https://developer.android.com/training/secure-file-sharing/share-file
source: md.txt
---

# Sharing a file

Once you have set up your app to share files using content URIs, you can respond to other apps' requests for those files. One way to respond to these requests is to provide a file selection interface from the server app that other applications can invoke. This approach allows a client application to let users select a file from the server app and then receive the selected file's content URI.

This lesson shows you how to create a file selection[Activity](https://developer.android.com/reference/android/app/Activity)in your app that responds to requests for files.

## Receive file requests

To receive requests for files from client apps and respond with a content URI, your app should provide a file selection[Activity](https://developer.android.com/reference/android/app/Activity). Client apps start this[Activity](https://developer.android.com/reference/android/app/Activity)by calling[startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int))with an[Intent](https://developer.android.com/reference/android/content/Intent)containing the action[ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK). When the client app calls[startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)), your app can return a result to the client app, in the form of a content URI for the file the user selected.

To learn how to implement a request for a file in a client app, see the lesson[Requesting a shared file](https://developer.android.com/training/secure-file-sharing/request-file).

## Create a file selection Activity

To set up the file selection[Activity](https://developer.android.com/reference/android/app/Activity), start by specifying the[Activity](https://developer.android.com/reference/android/app/Activity)in your manifest, along with an intent filter that matches the action[ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK)and the categories[CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)and[CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE). Also add MIME type filters for the files your app serves to other apps. The following snippet shows you how to specify the new[Activity](https://developer.android.com/reference/android/app/Activity)and intent filter:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    ...
        <application>
        ...
            <activity
                android:name=".FileSelectActivity"
                android:label="@File Selector" >
                <intent-filter>
                    <action
                        android:name="android.intent.action.PICK"/>
                    <category
                        android:name="android.intent.category.DEFAULT"/>
                    <category
                        android:name="android.intent.category.OPENABLE"/>
                    <data android:mimeType="text/plain"/>
                    <data android:mimeType="image/*"/>
                </intent-filter>
            </activity>
```

### Define the file selection Activity in code

Next, define an[Activity](https://developer.android.com/reference/android/app/Activity)subclass that displays the files available from your app's`files/images/`directory in internal storage and allows the user to pick the desired file. The following snippet demonstrates how to define this[Activity](https://developer.android.com/reference/android/app/Activity)and respond to the user's selection:  

### Kotlin

```kotlin
class MainActivity : Activity() {

    // The path to the root of this app's internal storage
    private lateinit var privateRootDir: File
    // The path to the "images" subdirectory
    private lateinit var imagesDir: File
    // Array of files in the images subdirectory
    private lateinit var imageFiles: Array<File>
    // Array of filenames corresponding to imageFiles
    private lateinit var imageFilenames: Array<String>

    // Initialize the Activity
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Set up an Intent to send back to apps that request a file
        resultIntent = Intent("com.example.myapp.ACTION_RETURN_FILE")
        // Get the files/ subdirectory of internal storage
        privateRootDir = filesDir
        // Get the files/images subdirectory;
        imagesDir = File(privateRootDir, "images")
        // Get the files in the images subdirectory
        imageFiles = imagesDir.listFiles()
        // Set the Activity's result to null to begin with
        setResult(Activity.RESULT_CANCELED, null)
        /*
         * Display the file names in the ListView fileListView.
         * Back the ListView with the array imageFilenames, which
         * you can create by iterating through imageFiles and
         * calling File.getAbsolutePath() for each File
         */
        ...
    }
    ...
}
```

### Java

```java
public class MainActivity extends Activity {
    // The path to the root of this app's internal storage
    private File privateRootDir;
    // The path to the "images" subdirectory
    private File imagesDir;
    // Array of files in the images subdirectory
    File[] imageFiles;
    // Array of filenames corresponding to imageFiles
    String[] imageFilenames;
    // Initialize the Activity
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // Set up an Intent to send back to apps that request a file
        resultIntent =
                new Intent("com.example.myapp.ACTION_RETURN_FILE");
        // Get the files/ subdirectory of internal storage
        privateRootDir = getFilesDir();
        // Get the files/images subdirectory;
        imagesDir = new File(privateRootDir, "images");
        // Get the files in the images subdirectory
        imageFiles = imagesDir.listFiles();
        // Set the Activity's result to null to begin with
        setResult(Activity.RESULT_CANCELED, null);
        /*
         * Display the file names in the ListView fileListView.
         * Back the ListView with the array imageFilenames, which
         * you can create by iterating through imageFiles and
         * calling File.getAbsolutePath() for each File
         */
         ...
    }
    ...
}
```

## Respond to a file selection

Once a user selects a shared file, your application must determine what file was selected and then generate a content URI for the file. Since the[Activity](https://developer.android.com/reference/android/app/Activity)displays the list of available files in a[ListView](https://developer.android.com/reference/android/widget/ListView), when the user clicks a file name the system calls the method[onItemClick()](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener#onItemClick(android.widget.AdapterView<?>, android.view.View, int, long)), in which you can get the selected file.

When using an intent to send a file's URI from one app to another, you must be careful to get a URI that other apps can read. Doing so on devices running Android 6.0 (API level 23) and later requires special care because of changes to the permissions model in that version of Android, particularly[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)'s becoming a[dangerous permission](https://developer.android.com/guide/topics/permissions/requesting#normal-dangerous), which the receiving app might lack.

With these considerations in mind, we recommend that you avoid using[Uri.fromFile()](https://developer.android.com/reference/android/net/Uri#fromFile(java.io.File)), which presents several drawbacks. This method:

- Does not allow file sharing across profiles.
- Requires that your app have[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)permission on devices running Android 4.4 (API level 19) or lower.
- Requires that receiving apps have the[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)permission, which will fail on important share targets, like Gmail, that don't have that permission.

Instead of using[Uri.fromFile()](https://developer.android.com/reference/android/net/Uri#fromFile(java.io.File)), you can use[URI permissions](https://developer.android.com/training/secure-file-sharing/share-file#GrantPermissions)to grant other apps access to specific URIs. While URI permissions don't work on`file://`URIs generated by[Uri.fromFile()](https://developer.android.com/reference/android/net/Uri#fromFile(java.io.File)), they do work on URIs associated with Content Providers. The[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)API can help you create such URIs. This approach also works with files that are not in external storage, but in the local storage of the app sending the intent.

In[onItemClick()](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener#onItemClick(android.widget.AdapterView<?>, android.view.View, int, long)), get a[File](https://developer.android.com/reference/java/io/File)object for the file name of the selected file and pass it as an argument to[getUriForFile()](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context, java.lang.String, java.io.File)), along with the authority that you specified in the[<provider>](https://developer.android.com/guide/topics/manifest/provider-element)element for the[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider). The resulting content URI contains the authority, a path segment corresponding to the file's directory (as specified in the XML meta-data), and the name of the file including its extension. How[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)maps directories to path segments based on XML meta-data is described in the section[Specify sharable directories](https://developer.android.com/training/secure-file-sharing/setup-sharing#DefineMetaData).

The following snippet shows you how to detect the selected file and get a content URI for it:  

### Kotlin

```kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Define a listener that responds to clicks on a file in the ListView
        fileListView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            /*
             * Get a File for the selected file name.
             * Assume that the file names are in the
             * imageFilename array.
             */
            val requestFile = File(imageFilenames[position])
            /*
             * Most file-related method calls need to be in
             * try-catch blocks.
             */
            // Use the FileProvider to get a content URI
            val fileUri: Uri? = try {
                FileProvider.getUriForFile(
                        this@MainActivity,
                        "com.example.myapp.fileprovider",
                        requestFile)
            } catch (e: IllegalArgumentException) {
                Log.e("File Selector",
                        "The selected file can't be shared: $requestFile")
                null
            }
            ...
        }
        ...
    }
```

### Java

```java
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // Define a listener that responds to clicks on a file in the ListView
        fileListView.setOnItemClickListener(
                new AdapterView.OnItemClickListener() {
            @Override
            /*
             * When a filename in the ListView is clicked, get its
             * content URI and send it to the requesting app
             */
            public void onItemClick(AdapterView<?> adapterView,
                    View view,
                    int position,
                    long rowId) {
                /*
                 * Get a File for the selected file name.
                 * Assume that the file names are in the
                 * imageFilename array.
                 */
                File requestFile = new File(imageFilename[position]);
                /*
                 * Most file-related method calls need to be in
                 * try-catch blocks.
                 */
                // Use the FileProvider to get a content URI
                try {
                    fileUri = FileProvider.getUriForFile(
                            MainActivity.this,
                            "com.example.myapp.fileprovider",
                            requestFile);
                } catch (IllegalArgumentException e) {
                    Log.e("File Selector",
                          "The selected file can't be shared: " + requestFile.toString());
                }
                ...
            }
        });
        ...
    }
```

Remember that you can only generate content URIs for files that reside in a directory you've specified in the meta-data file that contains the`<paths>`element, as described in the section[Specify sharable directories](https://developer.android.com/training/secure-file-sharing/setup-sharing#DefineMetaData). If you call[getUriForFile()](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context, java.lang.String, java.io.File))for a[File](https://developer.android.com/reference/java/io/File)in a path that you haven't specified, you receive an[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException).

## Grant permissions for the file

Now that you have a content URI for the file you want to share with another app, you need to allow the client app to access the file. To allow access, grant permissions to the client app by adding the content URI to an[Intent](https://developer.android.com/reference/android/content/Intent)and then setting permission flags on the[Intent](https://developer.android.com/reference/android/content/Intent). The permissions you grant are temporary and expire automatically when the receiving app's task stack is finished.

The following code snippet shows you how to set read permission for the file:  

### Kotlin

```kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Define a listener that responds to clicks on a file in the ListView
        fileListView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            ...
            if (fileUri != null) {
                // Grant temporary read permission to the content URI
                resultIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                ...
            }
            ...
        }
        ...
    }
```

### Java

```java
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // Define a listener that responds to clicks in the ListView
        fileListView.setOnItemClickListener(
                new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView,
                    View view,
                    int position,
                    long rowId) {
                ...
                if (fileUri != null) {
                    // Grant temporary read permission to the content URI
                    resultIntent.addFlags(
                        Intent.FLAG_GRANT_READ_URI_PERMISSION);
                }
                ...
             }
             ...
        });
    ...
    }
```

**Caution:** Calling[setFlags()](https://developer.android.com/reference/android/content/Intent#setFlags(int))is the only way to securely grant access to your files using temporary access permissions. Avoid calling[Context.grantUriPermission()](https://developer.android.com/reference/android/content/Context#grantUriPermission(java.lang.String, android.net.Uri, int))method for a file's content URI, since this method grants access that you can only revoke by calling[Context.revokeUriPermission()](https://developer.android.com/reference/android/content/Context#revokeUriPermission(android.net.Uri, int)).

Don't use[Uri.fromFile()](https://developer.android.com/reference/android/net/Uri#fromFile(java.io.File)). It forces receiving apps to have the[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)permission, won't work at all if you are trying to share across users, and in versions of Android lower than 4.4 (API level 19), would require your app to have[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE). And really important share targets, such as the Gmail app, don't have the[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE), causing this call to fail. Instead, you can use URI permissions to grant other apps access to specific URIs. While URI permissions don't work on file:// URIs as is generated by[Uri.fromFile()](https://developer.android.com/reference/android/net/Uri#fromFile(java.io.File)), they do work on Uris associated with Content Providers. Rather than implement your own just for this, you can and should use[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)as explained in[File sharing](https://developer.android.com/training/secure-file-sharing).

## Share the file with the requesting app

To share the file with the app that requested it, pass the[Intent](https://developer.android.com/reference/android/content/Intent)containing the content URI and permissions to[setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int)). When the[Activity](https://developer.android.com/reference/android/app/Activity)you have just defined is finished, the system sends the[Intent](https://developer.android.com/reference/android/content/Intent)containing the content URI to the client app. The following code snippet shows you how to do this:  

### Kotlin

```kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Define a listener that responds to clicks on a file in the ListView
        fileListView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            ...
            if (fileUri != null) {
                ...
                // Put the Uri and MIME type in the result Intent
                resultIntent.setDataAndType(fileUri, contentResolver.getType(fileUri))
                // Set the result
                setResult(Activity.RESULT_OK, resultIntent)
            } else {
                resultIntent.setDataAndType(null, "")
                setResult(RESULT_CANCELED, resultIntent)
            }
        }
    }
```

### Java

```java
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // Define a listener that responds to clicks on a file in the ListView
        fileListView.setOnItemClickListener(
                new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView,
                    View view,
                    int position,
                    long rowId) {
                ...
                if (fileUri != null) {
                    ...
                    // Put the Uri and MIME type in the result Intent
                    resultIntent.setDataAndType(
                            fileUri,
                            getContentResolver().getType(fileUri));
                    // Set the result
                    MainActivity.this.setResult(Activity.RESULT_OK,
                            resultIntent);
                    } else {
                        resultIntent.setDataAndType(null, "");
                        MainActivity.this.setResult(RESULT_CANCELED,
                                resultIntent);
                    }
                }
        });
```

Provide users with a way to return immediately to the client app once they have chosen a file. One way to do this is to provide a checkmark or**Done** button. Associate a method with the button using the button's[android:onClick](https://developer.android.com/reference/android/view/View#attr_android:onClick)attribute. In the method, call[finish()](https://developer.android.com/reference/android/app/Activity#finish()). For example:  

### Kotlin

```kotlin
    fun onDoneClick(v: View) {
        // Associate a method with the Done button
        finish()
    }
```

### Java

```java
    public void onDoneClick(View v) {
        // Associate a method with the Done button
        finish();
    }
```

For additional related information, refer to:

- [Designing Content URIs](https://developer.android.com/guide/topics/providers/content-provider-creating#ContentURI)
- [Implementing Content Provider Permissions](https://developer.android.com/guide/topics/providers/content-provider-creating#Permissions)
- [Permissions](https://developer.android.com/guide/topics/security/permissions)
- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)