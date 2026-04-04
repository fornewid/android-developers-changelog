---
title: https://developer.android.com/training/sync-adapters/creating-stub-provider
url: https://developer.android.com/training/sync-adapters/creating-stub-provider
source: md.txt
---

# Create a stub content provider

The sync adapter framework is designed to work with device data managed by the flexible and highly secure content provider framework. For this reason, the sync adapter framework expects that an app that uses the framework has already defined a content provider for its local data. If the sync adapter framework tries to run your sync adapter, and your app doesn't have a content provider, your sync adapter crashes.

If you're developing a new app that transfers data from a server to the device, you should strongly consider storing the local data in a content provider. Besides their importance for sync adapters, content providers offer a variety of security benefits and are specifically designed to handle data storage on Android systems. To learn more about creating a content provider, see[Creating a Content Provider](https://developer.android.com/guide/topics/providers/content-provider-creating).

However, if you're already storing local data in another form, you can still use a sync adapter to handle data transfer. To satisfy the sync adapter framework requirement for a content provider, add a stub content provider to your app. A stub provider implements the content provider class, but all of its required methods return`null`or`0`. If you add a stub provider, you can then use a sync adapter to transfer data from any storage mechanism you choose.

If you already have a content provider in your app, you don't need a stub content provider. In that case, you can skip this lesson and proceed to the lesson[Creating a Sync Adapter](https://developer.android.com/training/sync-adapters/creating-sync-adapter). If you don't yet have a content provider, this lesson shows you how to add a stub content provider that allows you to plug your sync adapter into the framework.

## Add a stub content provider

To create a stub content provider for your app, extend the class[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)and stub out its required methods. The following snippet shows you how to create the stub provider:  

### Kotlin

```kotlin
/*
 * Define an implementation of ContentProvider that stubs out
 * all methods
 */
class StubProvider : ContentProvider() {
    /*
     * Always return true, indicating that the
     * provider loaded correctly.
     */
    override fun onCreate(): Boolean  = true

    /*
     * Return no type for MIME type
     */
    override fun getType(uri: Uri): String?  = null

    /*
     * query() always returns no results
     *
     */
    override fun query(
            uri: Uri,
            projection: Array<String>,
            selection: String,
            selectionArgs: Array<String>,
            sortOrder: String
    ): Cursor?  = null

    /*
     * insert() always returns null (no URI)
     */
    override fun insert(uri: Uri, values: ContentValues): Uri? = null

    /*
     * delete() always returns "no rows affected" (0)
     */
    override fun delete(uri: Uri, selection: String, selectionArgs: Array<String>): Int = 0

    /*
     * update() always returns "no rows affected" (0)
     */
    override fun update(
            uri: Uri,
            values: ContentValues,
            selection: String,
            selectionArgs: Array<String>
    ): Int = 0
}
```

### Java

```java
/*
 * Define an implementation of ContentProvider that stubs out
 * all methods
 */
public class StubProvider extends ContentProvider {
    /*
     * Always return true, indicating that the
     * provider loaded correctly.
     */
    @Override
    public boolean onCreate() {
        return true;
    }
    /*
     * Return no type for MIME type
     */
    @Override
    public String getType(Uri uri) {
        return null;
    }
    /*
     * query() always returns no results
     *
     */
    @Override
    public Cursor query(
            Uri uri,
            String[] projection,
            String selection,
            String[] selectionArgs,
            String sortOrder) {
        return null;
    }
    /*
     * insert() always returns null (no URI)
     */
    @Override
    public Uri insert(Uri uri, ContentValues values) {
        return null;
    }
    /*
     * delete() always returns "no rows affected" (0)
     */
    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        return 0;
    }
    /*
     * update() always returns "no rows affected" (0)
     */
    public int update(
            Uri uri,
            ContentValues values,
            String selection,
            String[] selectionArgs) {
        return 0;
    }
}
```

## Declare the provider in the manifest

The sync adapter framework verifies that your app has a content provider by checking that your app has declared a provider in its app manifest. To declare the stub provider in the manifest, add a[<provider>](https://developer.android.com/guide/topics/manifest/provider-element)element with the following attributes:

`android:name="com.example.android.datasync.provider.StubProvider"`
:   Specifies the fully-qualified name of the class that implements the stub content provider.

`android:authorities="com.example.android.datasync.provider"`
:   A URI authority that identifies the stub content provider. Make this value your app's package name with the string ".provider" appended to it. Even though you're declaring your stub provider to the system, nothing tries to access the provider itself.

`android:exported="false"`
:   Determines whether other apps can access the content provider. For your stub content provider, set the value to`false`, since there's no need to allow other apps to see the provider. This value doesn't affect the interaction between the sync adapter framework and the content provider.

`android:syncable="true"`
:   Sets a flag that indicates that the provider is syncable. If you set this flag to`true`, you don't have to call[setIsSyncable()](https://developer.android.com/reference/android/content/ContentResolver#setIsSyncable(android.accounts.Account, java.lang.String, int))in your code. The flag allows the sync adapter framework to make data transfers with the content provider, but transfers only occur if you do them explicitly.

The following snippet shows you how to add the[<provider>](https://developer.android.com/guide/topics/manifest/provider-element)element to the app manifest:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.network.sync.BasicSyncAdapter"
    android:versionCode="1"
    android:versionName="1.0" >
    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme" >
    ...
    <provider
        android:name="com.example.android.datasync.provider.StubProvider"
        android:authorities="com.example.android.datasync.provider"
        android:exported="false"
        android:syncable="true"/>
    ...
    </application>
</manifest>
```

Now that you have created the dependencies required by the sync adapter framework, you can create the component that encapsulates your data transfer code. This component is called a sync adapter. The next lesson shows you how to add this component to your app.