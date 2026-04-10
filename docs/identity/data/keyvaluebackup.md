---
title: https://developer.android.com/identity/data/keyvaluebackup
url: https://developer.android.com/identity/data/keyvaluebackup
source: md.txt
---

# Back up key-value pairs with Android Backup Service

Android Backup Service provides cloud storage backup and restore for key-value data in your Android app. During a key-value backup operation, the app's backup data is passed to the device's backup transport. If the device is using the default Google backup transport, then the data is passed to Android Backup Service for archiving.
| **Note:** Key-value backup requires you to write code to define your backup content explicitly, while Auto Backup requires no code and will back up entire files. Most apps should use[Auto Backup](https://developer.android.com/guide/topics/data/autobackup)to implement backup and restore. Your app can implement Auto Backup or key-value backup, but not both.  
|
| In the past, developers registered their app to get a service key. You no longer need to register your app for key-value backup.

Data is limited to 5MB per user of your app. There is no charge for storing backup data.
| **Note:** The backup transport provided by Android Backup Service is not guaranteed to be available on all Android-powered devices that support backup. Some devices might support backup using a different transport, some devices might not support backup at all, and there is no way for your app to know what transport is used on the device.

For an overview of Android's backup options and guidance about which data you should back up and restore, see the[Data backup overview](https://developer.android.com/guide/topics/data/backup).

## Implement key-value backup

To back up your app data, you need to implement a backup agent. Your backup agent is called by the Backup Manager both during backup and restore.

To implement a backup agent, you must:

1. Declare your backup agent in your manifest file with the[`android:backupAgent`](https://developer.android.com/guide/topics/manifest/application-element#agent)attribute.

2. Define a backup agent by doing one of the following:

   - [Extending`BackupAgent`](https://developer.android.com/identity/data/keyvaluebackup#BackupAgent)

     The[`BackupAgent`](https://developer.android.com/reference/android/app/backup/BackupAgent)class provides the central interface that your app uses to communicate with the Backup Manager. If you extend this class directly, you must override[`onBackup()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onBackup(android.os.ParcelFileDescriptor,%20android.app.backup.BackupDataOutput,%20android.os.ParcelFileDescriptor))and[`onRestore()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onRestore(android.app.backup.BackupDataInput,%20int,%20android.os.ParcelFileDescriptor))to handle the backup and restore operations for your data.
   - [Extending`BackupAgentHelper`](https://developer.android.com/identity/data/keyvaluebackup#BackupAgentHelper)

     The[`BackupAgentHelper`](https://developer.android.com/reference/android/app/backup/BackupAgentHelper)class provides a convenient wrapper around the`BackupAgent`class, minimizing the amount of code you need to write. In your`BackupAgentHelper`, you must use one or more helper objects, which automatically back up and restore certain types of data, so that you don't need to implement`onBackup()`and`onRestore()`. Unless you need full control over your app's backups, we recommend using the`BackupAgentHelper`to handle your app's backups.

     Android currently provides backup helpers that will back up and restore complete files from[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences)and[internal storage](https://developer.android.com/guide/topics/data/data-storage#filesInternal).

## Declare the backup agent in your manifest

Once you've decided on the class name for your backup agent, declare it in your manifest using the`android:backupAgent`attribute in the[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)tag.

For example:  

```xml
<manifest ... >
    ...
    <application android:label="MyApplication"
                 android:backupAgent="MyBackupAgent">
        <meta-data android:name="com.google.android.backup.api_key"
            android:value="unused" />
        <activity ... >
            ...
        </activity>
    </application>
</manifest>
```

To support older devices, we recommend adding the API key`<meta-data>`to your Android manifest file. The Android Backup Service no longer requires a service key, but some older devices might still check for a key when backing up. Set`android:name`to`com.google.android.backup.api_key`and the`android:value`to`unused`.

The[`android:restoreAnyVersion`](https://developer.android.com/guide/topics/manifest/application-element#restoreany)attribute takes a boolean value to indicate whether you want to restore the app data regardless of the current app version compared to the version that produced the backup data. The default value is`false`. See[Check the restore data version](https://developer.android.com/identity/data/keyvaluebackup#RestoreVersion)for more information.

## Extend BackupAgentHelper

You should build your backup agent using`BackupAgentHelper`if you want to back up complete files from either`SharedPreferences`or internal storage. Building your backup agent with`BackupAgentHelper`requires far less code than extending`BackupAgent`, because you don't have to implement`onBackup()`and`onRestore()`.

Your implementation of`BackupAgentHelper`must use one or more backup helpers. A backup helper is a specialized component that`BackupAgentHelper`summons to perform backup and restore operations for a particular type of data. The Android framework currently provides two different helpers:

- [`SharedPreferencesBackupHelper`](https://developer.android.com/reference/android/app/backup/SharedPreferencesBackupHelper)to back up`SharedPreferences`files.
- [`FileBackupHelper`](https://developer.android.com/reference/android/app/backup/FileBackupHelper)to back up files from internal storage.

You can include multiple helpers in your`BackupAgentHelper`, but only one helper is needed for each data type. That is, if you have multiple`SharedPreferences`files, then you need only one`SharedPreferencesBackupHelper`.

For each helper you want to add to your`BackupAgentHelper`, you must do the following during your[`onCreate()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onCreate())method:

1. Instantiate an instance of the desired helper class. In the class constructor, you must specify the file(s) you want to back up.
2. Call[`addHelper()`](https://developer.android.com/reference/android/app/backup/BackupAgentHelper#addHelper(java.lang.String,%20android.app.backup.BackupHelper))to add the helper to your`BackupAgentHelper`.

The following sections describe how to create a backup agent using each of the available helpers.

### Back up SharedPreferences

When you instantiate a`SharedPreferencesBackupHelper`, you must include the name of one or more`SharedPreferences`files.

For example, to back up a`SharedPreferences`file named`user_preferences`, a complete backup agent using`BackupAgentHelper`looks like this:  

### Kotlin

```kotlin
// The name of the SharedPreferences file
const val PREFS = "user_preferences"

// A key to uniquely identify the set of backup data
const val PREFS_BACKUP_KEY = "prefs"

class MyPrefsBackupAgent : BackupAgentHelper() {
    override fun onCreate() {
        // Allocate a helper and add it to the backup agent
        SharedPreferencesBackupHelper(this, PREFS).also {
            addHelper(PREFS_BACKUP_KEY, it)
        }
    }
}
```

### Java

```java
public class MyPrefsBackupAgent extends BackupAgentHelper {
    // The name of the SharedPreferences file
    static final String PREFS = "user_preferences";

    // A key to uniquely identify the set of backup data
    static final String PREFS_BACKUP_KEY = "prefs";

    // Allocate a helper and add it to the backup agent
    @Override
    public void onCreate() {
        SharedPreferencesBackupHelper helper =
                new SharedPreferencesBackupHelper(this, PREFS);
        addHelper(PREFS_BACKUP_KEY, helper);
    }
}
```

The`SharedPreferencesBackupHelper`includes all the code needed to back up and restore a`SharedPreferences`file.

When the Backup Manager calls`onBackup()`and`onRestore()`,`BackupAgentHelper`calls your backup helpers to back up and restore your specified files.
| **Note:** The methods of`SharedPreferences`are thread-safe, so you can safely read and write the shared preferences file from your backup agent and other activities.

### Back up other files

When you instantiate a`FileBackupHelper`, you must include the name of one or more files that are saved to your app's internal storage, as specified by[`getFilesDir()`](https://developer.android.com/reference/android/content/ContextWrapper#getFilesDir()), which is the same location where[`openFileOutput()`](https://developer.android.com/reference/android/content/Context#openFileOutput(java.lang.String,%20int))writes files.

For example, to back up two files named`scores`and`stats`, a backup agent using`BackupAgentHelper`looks like this:  

### Kotlin

```kotlin
// The name of the file
const val TOP_SCORES = "scores"
const val PLAYER_STATS = "stats"
// A key to uniquely identify the set of backup data
const val FILES_BACKUP_KEY = "myfiles"

class MyFileBackupAgent : BackupAgentHelper() {
    override fun onCreate() {
        // Allocate a helper and add it to the backup agent
        FileBackupHelper(this, TOP_SCORES, PLAYER_STATS).also {
            addHelper(FILES_BACKUP_KEY, it)
        }
    }
}
```

### Java

```java
public class MyFileBackupAgent extends BackupAgentHelper {
    // The name of the file
    static final String TOP_SCORES = "scores";
    static final String PLAYER_STATS = "stats";

    // A key to uniquely identify the set of backup data
    static final String FILES_BACKUP_KEY = "myfiles";

    // Allocate a helper and add it to the backup agent
    @Override
    public void onCreate() {
        FileBackupHelper helper = new FileBackupHelper(this,
                TOP_SCORES, PLAYER_STATS);
        addHelper(FILES_BACKUP_KEY, helper);
    }
}
```

The`FileBackupHelper`includes all the code necessary to back up and restore files that are saved to your app's internal storage.

However, reading and writing to files on internal storage is**not thread-safe**. To ensure that your backup agent does not read or write your files at the same time as your activities, you must use synchronized statements each time you perform a read or write. For example, in any activity where you read and write the file, you need an object to use as the intrinsic lock for the synchronized statements:  

### Kotlin

```kotlin
// Object for intrinsic lock
companion object {
    val sDataLock = Any()
}
```

### Java

```java
// Object for intrinsic lock
static final Object sDataLock = new Object();
```

Then create a synchronized statement with this lock each time you read or write the files. For example, here's a synchronized statement for writing the latest score in a game to a file:  

### Kotlin

```kotlin
try {
    synchronized(MyActivity.sDataLock) {
        val dataFile = File(filesDir, TOP_SCORES)
        RandomAccessFile(dataFile, "rw").apply {
            writeInt(score)
        }
    }
} catch (e: IOException) {
    Log.e(TAG, "Unable to write to file")
}
```

### Java

```java
try {
    synchronized (MyActivity.sDataLock) {
        File dataFile = new File(getFilesDir(), TOP_SCORES);
        RandomAccessFile raFile = new RandomAccessFile(dataFile, "rw");
        raFile.writeInt(score);
    }
} catch (IOException e) {
    Log.e(TAG, "Unable to write to file");
}
```

You should synchronize your read statements with the same lock.

Then, in your`BackupAgentHelper`, you must override`onBackup()`and`onRestore()`to synchronize the backup and restore operations with the same intrinsic lock. For example, the`MyFileBackupAgent`example from above needs the following methods:  

### Kotlin

```kotlin
@Throws(IOException::class)
override fun onBackup(
        oldState: ParcelFileDescriptor,
        data: BackupDataOutput,
        newState: ParcelFileDescriptor
) {
    // Hold the lock while the FileBackupHelper performs back up
    synchronized(MyActivity.sDataLock) {
        super.onBackup(oldState, data, newState)
    }
}

@Throws(IOException::class)
override fun onRestore(
        data: BackupDataInput,
        appVersionCode: Int,
        newState: ParcelFileDescriptor
) {
    // Hold the lock while the FileBackupHelper restores the file
    synchronized(MyActivity.sDataLock) {
        super.onRestore(data, appVersionCode, newState)
    }
}
```

### Java

```java
@Override
public void onBackup(ParcelFileDescriptor oldState, BackupDataOutput data,
          ParcelFileDescriptor newState) throws IOException {
    // Hold the lock while the FileBackupHelper performs back up
    synchronized (MyActivity.sDataLock) {
        super.onBackup(oldState, data, newState);
    }
}

@Override
public void onRestore(BackupDataInput data, int appVersionCode,
        ParcelFileDescriptor newState) throws IOException {
    // Hold the lock while the FileBackupHelper restores the file
    synchronized (MyActivity.sDataLock) {
        super.onRestore(data, appVersionCode, newState);
    }
}
```

## Extend BackupAgent

Most apps shouldn't need to extend the`BackupAgent`class directly, but should instead[extend`BackupAgentHelper`](https://developer.android.com/identity/data/keyvaluebackup#BackupAgentHelper)to take advantage of the built-in helper classes that automatically back up and restore your files. However, you might extend`BackupAgent`directly to do the following:

- **Version your data format.** For instance, if you anticipate the need to revise the format in which you write your app data, you can build a backup agent to cross-check your app version during a restore operation and perform any necessary compatibility work if the version on the device is different than that of the backup data. For more information, see[Check the restore data version](https://developer.android.com/identity/data/keyvaluebackup#RestoreVersion).
- **Specify the portions of data to back up.**Instead of backing up an entire file, you can specify the portions of data to back up and how each portion is then restored to the device. This can also help you manage different versions, because you read and write your data as unique entities, rather than complete files.
- **Back up data in a database.** If you have an SQLite database that you want to restore when the user re-installs your app, you need to build a custom`BackupAgent`that reads the appropriate data during a backup operation, then create your table and insert the data during a restore operation.

If you don't need to perform any of the tasks above and want to back up complete files from`SharedPreferences`or internal storage, see[Extending`BackupAgentHelper`](https://developer.android.com/identity/data/keyvaluebackup#BackupAgentHelper).

### Required methods

When you create a`BackupAgent`, you must implement the following callback methods:

`onBackup()`
:   The Backup Manager calls this method after you[request a backup](https://developer.android.com/identity/data/keyvaluebackup#RequestingBackup). In this method, you read your app data from the device and pass the data you want to back up to the Backup Manager, as described in[Perform a back up](https://developer.android.com/identity/data/keyvaluebackup#PerformingBackup).

`onRestore()`

:   The Backup Manager calls this method during a restore operation. This method delivers your backup data, which your app can use to restore its former state, as described in[Perform a restore](https://developer.android.com/identity/data/keyvaluebackup#PerformingRestore).

    The system calls this method to restore any backup data when the user re-installs your app, but your app can also[request a restore](https://developer.android.com/identity/data/keyvaluebackup#RequestingRestore).

### Perform a back up

A backup request does not result in an immediate call to your`onBackup()`method. Instead, the Backup Manager waits for an appropriate time, then performs a backup for all apps that have requested a backup since the last backup was performed. This is the point at which you must provide your app data to the Backup Manager so it can be saved to cloud storage.

Only the Backup Manager can call your backup agent's`onBackup()`method. Each time that your app data changes and you want to perform a backup, you must request a backup operation by calling[`dataChanged()`](https://developer.android.com/reference/android/app/backup/BackupManager#dataChanged()). See[Request a backup](https://developer.android.com/identity/data/keyvaluebackup#RequestingBackup)for more information.

**Tip** : While developing your app, you can initiate an immediate backup operation from the Backup Manager with the[`bmgr`tool](https://developer.android.com/tools/help/bmgr).

When the Backup Manager calls your`onBackup()`method, it passes three parameters:

`oldState`
:   An open, read-only[`ParcelFileDescriptor`](https://developer.android.com/reference/android/os/ParcelFileDescriptor)pointing to the last backup state provided by your app. This is not the backup data from cloud storage, but a local representation of the data that was backed up the last time`onBackup()`was called, as defined by`newState`or from`onRestore()`.`onRestore()`is covered in the next section. Because`onBackup()`does not allow you to read existing backup data in the cloud storage, you can use this local representation to determine whether your data has changed since the last backup.

`data`
:   A[`BackupDataOutput`](https://developer.android.com/reference/android/app/backup/BackupDataOutput)object, which you use to deliver your backup data to the Backup Manager.

`newState`
:   An open, read/write`ParcelFileDescriptor`pointing to a file in which you must write a representation of the data that you delivered to`data`. A representation can be as simple as the last-modified timestamp for your file. This object is returned as`oldState`the next time the Backup Manager calls your`onBackup()`method. If you don't write your backup data to`newState`, then`oldState`will point to an empty file next time Backup Manager calls`onBackup()`.

Using these parameters, implement your`onBackup()`method to do the following:

1. Check whether your data has changed since the last backup by comparing`oldState`to your current data. How you read data in`oldState`depends on how you originally wrote it to`newState`(see step 3). The easiest way to record the state of a file is with its last-modified timestamp. For example, here's how you can read and compare a timestamp from`oldState`:

   ### Kotlin

   ```kotlin
   val instream = FileInputStream(oldState.fileDescriptor)
   val dataInputStream = DataInputStream(instream)
   try {
      // Get the last modified timestamp from the state file and data file
      val stateModified = dataInputStream.readLong()
      val fileModified: Long = dataFile.lastModified()
      if (stateModified != fileModified) {
          // The file has been modified, so do a backup
          // Or the time on the device changed, so be safe and do a backup
      } else {
          // Don't back up because the file hasn't changed
          return
      }
   } catch (e: IOException) {
      // Unable to read state file... be safe and do a backup
   }
   ```

   ### Java

   ```java
   // Get the oldState input stream
   FileInputStream instream = new FileInputStream(oldState.getFileDescriptor());
   DataInputStream in = new DataInputStream(instream);

   try {
      // Get the last modified timestamp from the state file and data file
      long stateModified = in.readLong();
      long fileModified = dataFile.lastModified();

      if (stateModified != fileModified) {
          // The file has been modified, so do a backup
          // Or the time on the device changed, so be safe and do a backup
      } else {
          // Don't back up because the file hasn't changed
          return;
      }
   } catch (IOException e) {
      // Unable to read state file... be safe and do a backup
   }
   ```

   If nothing has changed and you don't need to back up, skip to step 3.
2. If your data has changed, compared to`oldState`, write the current data to`data`to back it up to the cloud storage.

   You must write each chunk of data as an entity in the`BackupDataOutput`. An entity is a flattened binary data record that is identified by a unique key string. Thus, the data set that you back up is conceptually a set of key-value pairs.

   To add an entity to your backup data set, you must:
   1. Call[`writeEntityHeader()`](https://developer.android.com/reference/android/app/backup/BackupDataOutput#writeEntityHeader(java.lang.String,%20int)), passing a unique string key for the data you're about to write and the data size.

   2. Call[`writeEntityData()`](https://developer.android.com/reference/android/app/backup/BackupDataOutput#writeEntityData(byte%5B%5D,%20int)), passing a byte buffer that contains your data and the number of bytes to write from the buffer, which should match the size passed to`writeEntityHeader()`.

   For example, the following code flattens some data into a byte stream and writes it into a single entity:  

   ### Kotlin

   ```kotlin
   val buffer: ByteArray = ByteArrayOutputStream().run {
      DataOutputStream(this).apply {
          writeInt(playerName)
          writeInt(playerScore)
      }
      toByteArray()
   }
   val len: Int = buffer.size
   data.apply {
      writeEntityHeader(TOPSCORE_BACKUP_KEY, len)
      writeEntityData(buffer, len)
   }
   ```

   ### Java

   ```java
   // Create buffer stream and data output stream for our data
   ByteArrayOutputStream bufStream = new ByteArrayOutputStream();
   DataOutputStream outWriter = new DataOutputStream(bufStream);
   // Write structured data
   outWriter.writeUTF(playerName);
   outWriter.writeInt(playerScore);
   // Send the data to the Backup Manager via the BackupDataOutput
   byte[] buffer = bufStream.toByteArray();
   int len = buffer.length;
   data.writeEntityHeader(TOPSCORE_BACKUP_KEY, len);
   data.writeEntityData(buffer, len);
   ```

   Perform this for each piece of data that you want to back up. How you divide your data into entities is up to you. You might even use just one entity.
3. Whether or not you perform a backup (in step 2), write a representation of the current data to the`newState``ParcelFileDescriptor`. The Backup Manager retains this object locally as a representation of the data that is currently backed up. It passes this back to you as`oldState`the next time it calls`onBackup()`so you can determine whether another backup is necessary, as handled in step 1. If you don't write the current data state to this file, then`oldState`will be empty during the next callback.

   The following example saves a representation of the current data into`newState`using the file's last-modified timestamp:  

   ### Kotlin

   ```kotlin
   val modified = dataFile.lastModified()
   FileOutputStream(newState.fileDescriptor).also {
      DataOutputStream(it).apply {
          writeLong(modified)
      }
   }
   ```

   ### Java

   ```java
   FileOutputStream outstream = new FileOutputStream(newState.getFileDescriptor());
   DataOutputStream out = new DataOutputStream(outstream);

   long modified = dataFile.lastModified();
   out.writeLong(modified);
   ```

| **Caution:** If your app data is saved to a file, make sure that you use synchronized statements while accessing the file so that your backup agent does not read the file while an activity in your app is also writing the file.

### Perform a restore

When it's time to restore your app data, the Backup Manager calls your backup agent's`onRestore()`method. When it calls this method, the Backup Manager delivers your backup data so you can restore it onto the device.

Only the Backup Manager can call`onRestore()`, which happens automatically when the system installs your app and finds existing backup data.
| **Note:** While developing your app, you can also request a restore operation with the`bmgr`tool.

When the Backup Manager calls your`onRestore()`method, it passes three parameters:

`data`
:   A[`BackupDataInput`](https://developer.android.com/reference/android/app/backup/BackupDataInput)object, which allows you to read your backup data.

`appVersionCode`
:   An integer representing the value of your app's[`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)manifest attribute, as it was when this data was backed up. You can use this to cross-check the current app version and determine if the data format is compatible. For more information about using this to handle different versions of restore data, see[Check the restore data version](https://developer.android.com/identity/data/keyvaluebackup#RestoreVersion).

`newState`
:   An open, read/write`ParcelFileDescriptor`pointing to a file in which you must write the final backup state that was provided with`data`. This object is returned as`oldState`the next time`onBackup()`is called. Recall that you must also write the same`newState`object in the`onBackup()`callback---also doing it here ensures that the`oldState`object given to`onBackup()`is valid even the first time`onBackup()`is called after the device is restored.

In your implementation of`onRestore()`, you should call[`readNextHeader()`](https://developer.android.com/reference/android/app/backup/BackupDataInput#readNextHeader())on the`data`to iterate through all entities in the data set. For each entity found, do the following:

1. Get the entity key with[`getKey()`](https://developer.android.com/reference/android/app/backup/BackupDataInput#getKey()).
2. Compare the entity key to a list of known key values that you should have declared as static final strings inside your`BackupAgent`class. When the key matches one of your known key strings, enter into a statement to extract the entity data and save it to the device:

   1. Get the entity data size with[`getDataSize()`](https://developer.android.com/reference/android/app/backup/BackupDataInput#getDataSize())and create a byte array of that size.
   2. Call[`readEntityData()`](https://developer.android.com/reference/android/app/backup/BackupDataInput#readEntityData(byte%5B%5D,%20int,%20int))and pass it the byte array, which is where the data will go, and specify the start offset and the size to read.
   3. Your byte array is now full. Read the data and write it to the device however you like.
3. After you read and write your data back to the device, write the state of your data to the`newState`parameter the same as you do during`onBackup()`.

For example, here's how you can restore the data backed up by the example in the previous section:  

### Kotlin

```kotlin
@Throws(IOException::class)
override fun onRestore(data: BackupDataInput, appVersionCode: Int,
                       newState: ParcelFileDescriptor) {
    with(data) {
        // There should be only one entity, but the safest
        // way to consume it is using a while loop
        while (readNextHeader()) {
            when(key) {
                TOPSCORE_BACKUP_KEY -> {
                    val dataBuf = ByteArray(dataSize).also {
                        readEntityData(it, 0, dataSize)
                    }
                    ByteArrayInputStream(dataBuf).also {
                        DataInputStream(it).apply {
                            // Read the player name and score from the backup data
                            playerName = readUTF()
                            playerScore = readInt()
                        }
                        // Record the score on the device (to a file or something)
                        recordScore(playerName, playerScore)
                    }
                }
                else -> skipEntityData()
            }
        }
    }

    // Finally, write to the state blob (newState) that describes the restored data
    FileOutputStream(newState.fileDescriptor).also {
        DataOutputStream(it).apply {
            writeUTF(playerName)
            writeInt(mPlayerScore)
        }
    }
}
```

### Java

```java
@Override
public void onRestore(BackupDataInput data, int appVersionCode,
                      ParcelFileDescriptor newState) throws IOException {
    // There should be only one entity, but the safest
    // way to consume it is using a while loop
    while (data.readNextHeader()) {
        String key = data.getKey();
        int dataSize = data.getDataSize();

        // If the key is ours (for saving top score). Note this key was used when
        // we wrote the backup entity header
        if (TOPSCORE_BACKUP_KEY.equals(key)) {
            // Create an input stream for the BackupDataInput
            byte[] dataBuf = new byte[dataSize];
            data.readEntityData(dataBuf, 0, dataSize);
            ByteArrayInputStream baStream = new ByteArrayInputStream(dataBuf);
            DataInputStream in = new DataInputStream(baStream);

            // Read the player name and score from the backup data
            playerName = in.readUTF();
            playerScore = in.readInt();

            // Record the score on the device (to a file or something)
            recordScore(playerName, playerScore);
        } else {
            // We don't know this entity key. Skip it. (Shouldn't happen.)
            data.skipEntityData();
        }
    }

    // Finally, write to the state blob (newState) that describes the restored data
    FileOutputStream outstream = new FileOutputStream(newState.getFileDescriptor());
    DataOutputStream out = new DataOutputStream(outstream);
    out.writeUTF(playerName);
    out.writeInt(mPlayerScore);
}
```

In this example, the`appVersionCode`parameter passed to`onRestore()`is not used. However, you might want to use it if you've chosen to perform a backup when the user's version of the app has actually moved backward (for example, the user went from version 1.5 of your app to 1.0). For more information, see the next section.

## Check the restore data version

When the Backup Manager saves your data to cloud storage, it automatically includes the version of your app, as defined by your manifest file's`android:versionCode`attribute. Before the Backup Manager calls your backup agent to restore your data, it looks at the`android:versionCode`of the installed app and compares it to the value recorded in the restore data set. If the version recorded in the restore data set is*newer* than the app version on the device, then the user has downgraded their app. In this case, the Backup Manager will abort the restore operation for your app and not call your`onRestore()`method, because the restore set is considered meaningless to an older version.

You can override this behavior with the`android:restoreAnyVersion`attribute. Set this attribute to`true`to indicate that you want to restore the app regardless of the restore set version. The default value is`false`. If you set this to`true`then the Backup Manager will ignore the`android:versionCode`and call your`onRestore()`method in all cases. In doing so, you can manually check for the version difference in your`onRestore()`method and take any steps necessary to make the data compatible if the versions don't match.

To help you handle different versions during a restore operation, the`onRestore()`method passes you the version code included with the restore data set as the`appVersionCode`parameter. You can then query the current app's version code with the[`PackageInfo.versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionCode)field. For example:  

### Kotlin

```kotlin
val info: PackageInfo? = try {
    packageManager.getPackageInfo(packageName, 0)
} catch (e: PackageManager.NameNotFoundException) {
    null
}

val version: Int = info?.versionCode ?: 0
```

### Java

```java
PackageInfo info;
try {
    String name = getPackageName();
    info = getPackageManager().getPackageInfo(name, 0);
} catch (NameNotFoundException nnfe) {
    info = null;
}

int version;
if (info != null) {
    version = info.versionCode;
}
```

Then compare the`version`acquired from[`PackageInfo`](https://developer.android.com/reference/android/content/pm/PackageInfo)to the`appVersionCode`passed into`onRestore()`.
| **Caution:** Be certain you understand the consequences of setting`android:restoreAnyVersion`to`true`for your app. If each version of your app that supports backup does not properly account for variations in your data format during`onRestore()`, then the data on the device could be saved in a format incompatible with the version currently installed on the device.

## Request a backup

You can request a backup operation at any time by calling`dataChanged()`. This method notifies the Backup Manager that you'd like to back up your data using your backup agent. The Backup Manager then calls your backup agent's`onBackup()`method at time in the future. Typically, you should request a backup each time your data changes (such as when the user changes an app preference that you'd like to back up). If you call`dataChanged()`several times before the Backup Manager requests a backup from your agent, your agent still receives just one call to`onBackup()`.
| **Note:** While developing your app, you can request a backup and initiate an immediate backup operation with the`bmgr`tool.

## Request a restore

During the normal life of your app, you shouldn't need to request a restore operation. The system automatically checks for backup data and performs a restore when your app is installed.
| **Note:** While developing your app, you can request a restore operation with the`bmgr`tool.

## Migrate to Auto Backup

You can transition your app to full-data backups by setting[`android:fullBackupOnly`](https://developer.android.com/guide/topics/manifest/application-element#fullBackupOnly)to`true`in the`<application>`element in the manifest file. When running on a device with Android 5.1 (API level 22) or lower, your app ignores this value in the manifest, and continues performing key-value backups. When running on a device with Android 6.0 (API level 23) or higher, your app performs Auto Backup instead of key-value backup.

## User privacy

At Google, we are keenly aware of the trust users place in us and our responsibility to protect users' privacy. Google securely transmits backup data to and from Google servers in order to provide backup and restore features. Google treats this data as personal information in accordance with Google's[Privacy Policy](http://www.google.com/privacypolicy).

In addition, users can disable data backup functionality through the Android system's backup settings. When a user disables backup, Android Backup Service deletes all saved backup data. A user can re-enable backup on the device, but Android Backup Service will not restore any previously deleted data.