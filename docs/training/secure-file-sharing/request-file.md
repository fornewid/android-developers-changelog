---
title: https://developer.android.com/training/secure-file-sharing/request-file
url: https://developer.android.com/training/secure-file-sharing/request-file
source: md.txt
---

# Requesting a shared file

When an app wants to access a file shared by another app, the requesting app (the client) usually sends a request to the app sharing the files (the server). In most cases, the request starts an[Activity](https://developer.android.com/reference/android/app/Activity)in the server app that displays the files it can share. The user picks a file, after which the server app returns the file's content URI to the client app.

This lesson shows you how a client app requests a file from a server app, receives the file's content URI from the server app, and opens the file using the content URI.

## Send a request for the file

To request a file from the server app, the client app calls[startActivityForResult](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int))with an[Intent](https://developer.android.com/reference/android/content/Intent)containing the action such as[ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK)and a MIME type that the client app can handle.

For example, the following code snippet demonstrates how to send an[Intent](https://developer.android.com/reference/android/content/Intent)to a server app in order to start the[Activity](https://developer.android.com/reference/android/app/Activity)described in[Sharing a file](https://developer.android.com/training/secure-file-sharing/share-file#SendURI):  

### Kotlin

```kotlin
class MainActivity : Activity() {
    private lateinit var requestFileIntent: Intent
    private lateinit var inputPFD: ParcelFileDescriptor
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        requestFileIntent = Intent(Intent.ACTION_PICK).apply {
            type = "image/jpg"
        }
        ...
    }
    ...
    private fun requestFile() {
        /**
         * When the user requests a file, send an Intent to the
         * server app.
         * files.
         */
        startActivityForResult(requestFileIntent, 0)
        ...
    }
    ...
}
```

### Java

```java
public class MainActivity extends Activity {
    private Intent requestFileIntent;
    private ParcelFileDescriptor inputPFD;
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        requestFileIntent = new Intent(Intent.ACTION_PICK);
        requestFileIntent.setType("image/jpg");
        ...
    }
    ...
    protected void requestFile() {
        /**
         * When the user requests a file, send an Intent to the
         * server app.
         * files.
         */
            startActivityForResult(requestFileIntent, 0);
        ...
    }
    ...
}
```

## Access the requested file

The server app sends the file's content URI back to the client app in an[Intent](https://developer.android.com/reference/android/content/Intent). This[Intent](https://developer.android.com/reference/android/content/Intent)is passed to the client app in its override of[onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)). Once the client app has the file's content URI, it can access the file by getting its[FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor).

File security is preserved in this process only as long as you properly parse the content URI that the client app receives. When parsing content, you must ensure that this URI does not point to anything outside of the intended directory, ensuring that no[path traversal](https://developer.android.com/privacy-and-security/risks/path-traversal)is being attempted. Only the client app should gain access to the file, and only for the permissions granted by the server app. Permissions are temporary, so once the client app's task stack is finished, the file is no longer accessible outside the server app.

The next snippet demonstrates how the client app handles the[Intent](https://developer.android.com/reference/android/content/Intent)sent from the server app, and how the client app gets the[FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor)using the content URI:  

### Kotlin

```kotlin
/*
 * When the Activity of the app that hosts files sets a result and calls
 * finish(), this method is invoked. The returned Intent contains the
 * content URI of a selected file. The result code indicates if the
 * selection worked or not.
 */
public override fun onActivityResult(requestCode: Int, resultCode: Int, returnIntent: Intent) {
    // If the selection didn't work
    if (resultCode != Activity.RESULT_OK) {
        // Exit without doing anything else
        return
    }
    // Get the file's content URI from the incoming Intent
    returnIntent.data?.also { returnUri ->
        /*
         * Try to open the file for "read" access using the
         * returned URI. If the file isn't found, write to the
         * error log and return.
         */
        inputPFD = try {
            /*
             * Get the content resolver instance for this context, and use it
             * to get a ParcelFileDescriptor for the file.
             */
            contentResolver.openFileDescriptor(returnUri, "r")
        } catch (e: FileNotFoundException) {
            e.printStackTrace()
            Log.e("MainActivity", "File not found.")
            return
        }

        // Get a regular file descriptor for the file
        val fd = inputPFD.fileDescriptor
        ...
    }
}
```

### Java

```java
    /*
     * When the Activity of the app that hosts files sets a result and calls
     * finish(), this method is invoked. The returned Intent contains the
     * content URI of a selected file. The result code indicates if the
     * selection worked or not.
     */
    @Override
    public void onActivityResult(int requestCode, int resultCode,
            Intent returnIntent) {
        // If the selection didn't work
        if (resultCode != RESULT_OK) {
            // Exit without doing anything else
            return;
        } else {
            // Get the file's content URI from the incoming Intent
            Uri returnUri = returnIntent.getData();
            /*
             * Try to open the file for "read" access using the
             * returned URI. If the file isn't found, write to the
             * error log and return.
             */
            try {
                /*
                 * Get the content resolver instance for this context, and use it
                 * to get a ParcelFileDescriptor for the file.
                 */
                inputPFD = getContentResolver().openFileDescriptor(returnUri, "r");
            } catch (FileNotFoundException e) {
                e.printStackTrace();
                Log.e("MainActivity", "File not found.");
                return;
            }
            // Get a regular file descriptor for the file
            FileDescriptor fd = inputPFD.getFileDescriptor();
            ...
        }
    }
```

The method[openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String))returns a[ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor)for the file. From this object, the client app gets a[FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor)object, which it can then use to read the file.

For additional related information, refer to:

- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)
- [Retrieving Data from the Provider](https://developer.android.com/guide/topics/providers/content-provider-basics#SimpleQuery)