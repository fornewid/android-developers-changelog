---
title: https://developer.android.com/media/camera/camera-deprecated/photobasics
url: https://developer.android.com/media/camera/camera-deprecated/photobasics
source: md.txt
---

**Note:** This page refers to the
[Camera](https://developer.android.com/reference/android/hardware/Camera) class, which is deprecated. We
recommend using [CameraX](https://developer.android.com/media/camera/camerax) or, for specific use cases,
[Camera2](https://developer.android.com/media/camera/camera2). Both CameraX and Camera2 support Android 5.0
(API level 21) and higher.


This lesson teaches how to capture a photo by delegating the work to another camera app on the
device. (If you'd rather build your own camera functionality, see
[Controlling the camera](https://developer.android.com/training/camera-deprecated/cameradirect).)


Suppose you are implementing a crowd-sourced weather service that makes a global weather map by
blending together pictures of the sky taken by devices running your client app. Integrating photos
is only a small part of your application. You want to take photos with minimal fuss, not reinvent
the camera. Happily, most Android-powered devices already have at least one camera application
installed. In this lesson, you learn how to make it take a picture for you.

## Request the camera feature


If an essential function of your application is taking pictures, then restrict its visibility on
Google Play to devices that have a camera. To advertise that your application depends on having a
camera, put a
[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) tag in
your manifest file:  

```xml
<manifest ... >
    <uses-feature android:name="android.hardware.camera"
                  android:required="true" />
    ...
</manifest>
```


If your application uses, but does not require a camera in order to function, instead set
`android:required` to `false`. In doing so, Google Play will allow devices
without a camera to download your application. It's then your responsibility to check for the
availability of the camera at runtime by calling
[hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)).
If a camera is not available, you should then disable your camera features.

## Get the thumbnail


If the simple feat of taking a photo is not the culmination of your app's ambition, then you
probably want to get the image back from the camera application and do something with it.


The Android Camera application encodes the photo in the return
[Intent](https://developer.android.com/reference/android/content/Intent) delivered to
[onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent))
as a small [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) in the extras,
under the key `"data"`. The following code retrieves this image and displays it in an
[ImageView](https://developer.android.com/reference/android/widget/ImageView).  

### Kotlin

```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
        val imageBitmap = data.extras.get("data") as Bitmap
        imageView.setImageBitmap(imageBitmap)
    }
}
```

### Java

```java
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
        Bundle extras = data.getExtras();
        Bitmap imageBitmap = (Bitmap) extras.get("data");
        imageView.setImageBitmap(imageBitmap);
    }
}
```


**Note:** This thumbnail image from `"data"` might be good for an icon,
but not a lot more. Dealing with a full-sized image takes a bit more work.

## Save the full-size photo


The Android Camera application saves a full-size photo if you give it a file to save into. You
must provide a fully qualified file name where the camera app should save the photo.


Generally, any photos that the user captures with the device camera should be saved on the device
in the public external storage so they are accessible by all apps. The proper directory for shared
photos is provided by
[getExternalStoragePublicDirectory()](https://developer.android.com/reference/android/os/Environment#getExternalStoragePublicDirectory(java.lang.String)),
with the
[DIRECTORY_PICTURES](https://developer.android.com/reference/android/os/Environment#DIRECTORY_PICTURES)
argument. The directory provided by this method is shared among all apps. On Android 9 (API level
28) and lower, reading and writing to this directory requires the
[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
and
[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)
permissions, respectively:  

```xml
<manifest ...>
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    ...
</manifest>
```


On Android 10 (API level 29) and higher, the proper directory for sharing photos is the
[`MediaStore.Images`](https://developer.android.com/reference/android/provider/MediaStore.Images) table.
You don't need to declare any storage permissions, as long as your app only needs to access the
photos that the user took using your app.


However, if you'd like the photos to remain private to your app only, you can instead use the
directory provided by
[Context.getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)).
On Android 4.3 and lower, writing to this directory also requires the
[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)
permission. Beginning with Android 4.4, the permission is no longer required because the directory
is not accessible by other apps, so you can declare the permission should be requested only on the
lower versions of Android by adding the
[`maxSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-permission-element#maxSdk)
attribute:  

```xml
<manifest ...>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
                     android:maxSdkVersion="28" />
    ...
</manifest>
```


**Note:** Files you save in the directories provided by
[getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String))
or
[getFilesDir()](https://developer.android.com/reference/android/content/Context#getFilesDir()) are
deleted when the user uninstalls your app.


Once you decide the directory for the file, you need to create a collision-resistant file name.
You may wish also to save the path in a member variable for later use. Here's an example solution
in a method that returns a unique file name for a new photo using a date-time stamp.
(This example assumes you are calling the method from inside a `Context`.)  

### Kotlin

```kotlin
lateinit var currentPhotoPath: String

@Throws(IOException::class)
private fun createImageFile(): File {
    // Create an image file name
    val timeStamp: String = SimpleDateFormat("yyyyMMdd_HHmmss").format(Date())
    val storageDir: File = getExternalFilesDir(Environment.DIRECTORY_PICTURES)
    return File.createTempFile(
            "JPEG_${timeStamp}_", /* prefix */
            ".jpg", /* suffix */
            storageDir /* directory */
    ).apply {
        // Save a file: path for use with ACTION_VIEW intents
        currentPhotoPath = absolutePath
    }
}
```

### Java

```java
String currentPhotoPath;

private File createImageFile() throws IOException {
    // Create an image file name
    String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
    String imageFileName = "JPEG_" + timeStamp + "_";
    File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
    File image = File.createTempFile(
        imageFileName,  /* prefix */
        ".jpg",         /* suffix */
        storageDir      /* directory */
    );

    // Save a file: path for use with ACTION_VIEW intents
    currentPhotoPath = image.getAbsolutePath();
    return image;
}
```


With this method available to create a file for the photo, you can now create and invoke the
[Intent](https://developer.android.com/reference/android/content/Intent) like this:  

### Kotlin

```kotlin
private fun dispatchTakePictureIntent() {
    Intent(MediaStore.ACTION_IMAGE_CAPTURE).also { takePictureIntent ->
        // Ensure that there's a camera activity to handle the intent
        takePictureIntent.resolveActivity(packageManager)?.also {
            // Create the File where the photo should go
            val photoFile: File? = try {
                createImageFile()
            } catch (ex: IOException) {
                // Error occurred while creating the File
                ...
                null
            }
            // Continue only if the File was successfully created
            photoFile?.also {
                val photoURI: Uri = FileProvider.getUriForFile(
                        this,
                        "com.example.android.fileprovider",
                        it
                )
                takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI)
                startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
            }
        }
    }
}
```

### Java

```java
private void dispatchTakePictureIntent() {
    Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    // Ensure that there's a camera activity to handle the intent
    if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
        // Create the File where the photo should go
        File photoFile = null;
        try {
            photoFile = createImageFile();
        } catch (IOException ex) {
            // Error occurred while creating the File
            ...
        }
        // Continue only if the File was successfully created
        if (photoFile != null) {
            Uri photoURI = FileProvider.getUriForFile(this,
                                                  "com.example.android.fileprovider",
                                                  photoFile);
            takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI);
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }
}
```


**Note:** We are using
[getUriForFile(Context, String, File)](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context, java.lang.String, java.io.File))
which returns a `content://` URI. For more recent apps targeting Android 7.0 (API level
24) and higher, passing a `file://` URI across a package boundary causes a
[FileUriExposedException](https://developer.android.com/reference/android/os/FileUriExposedException).
Therefore, we now present a more generic way of storing images using a
[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider).


Now, you need to configure the
[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider). In your
app's manifest, add a provider to your application:  

```xml
<application>
   ...
   <provider
        android:name="androidx.core.content.FileProvider"
        android:authorities="com.example.android.fileprovider"
        android:exported="false"
        android:grantUriPermissions="true">
        <meta-data
            android:name="android.support.FILE_PROVIDER_PATHS"
            android:resource="@xml/file_paths"></meta-data>
    </provider>
    ...
</application>
```


Make sure that the authorities string matches the second argument to
[getUriForFile(Context, String, File)](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context, java.lang.String, java.io.File)).
In the meta-data section of the provider definition, you can see that the provider expects
eligible paths to be configured in a dedicated resource file, res/xml/file_paths.xml. Here
is the content required for this particular example:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-files-path name="my_images" path="Pictures" />
</paths>
```


The path component corresponds to the path that is returned by
[getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String))
when called with
[Environment.DIRECTORY_PICTURES](https://developer.android.com/reference/android/os/Environment#DIRECTORY_PICTURES).
Make sure that you replace `com.example.package.name` with the actual package name of
your app. Also, checkout the documentation of
[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider) for an
extensive description of path specifiers that you can use besides `external-path`.

## Add the photo to a gallery


When you create a photo through an intent, you should know where your image is located, because
you said where to save it in the first place. For everyone else, perhaps the easiest way to make
your photo accessible is to make it accessible from the system's Media Provider.


**Note:** If you saved your photo to the directory provided by
[getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)),
the media scanner cannot access the files because they are private to your app.


The following example method demonstrates how to invoke the system's media scanner to add your
photo to the Media Provider's database, making it available in the Android Gallery application and
to other apps.  

### Kotlin

```kotlin
private fun galleryAddPic() {
    Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE).also { mediaScanIntent ->
        val f = File(currentPhotoPath)
        mediaScanIntent.data = Uri.fromFile(f)
        sendBroadcast(mediaScanIntent)
    }
}
```

### Java

```java
private void galleryAddPic() {
    Intent mediaScanIntent = new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE);
    File f = new File(currentPhotoPath);
    Uri contentUri = Uri.fromFile(f);
    mediaScanIntent.setData(contentUri);
    this.sendBroadcast(mediaScanIntent);
}
```

## Decode a scaled image


Managing multiple full-sized images can be tricky with limited memory. If you find your
application running out of memory after displaying just a few images, you can dramatically reduce
the amount of dynamic heap used by expanding the JPEG into a memory array that's already scaled to
match the size of the destination view. The following example method demonstrates this technique.  

### Kotlin

```kotlin
private fun setPic() {
    // Get the dimensions of the View
    val targetW: Int = imageView.width
    val targetH: Int = imageView.height

    val bmOptions = BitmapFactory.Options().apply {
        // Get the dimensions of the bitmap
        inJustDecodeBounds = true

        BitmapFactory.decodeFile(currentPhotoPath, bmOptions)

        val photoW: Int = outWidth
        val photoH: Int = outHeight

        // Determine how much to scale down the image
        val scaleFactor: Int = Math.max(1, Math.min(photoW / targetW, photoH / targetH))

        // Decode the image file into a Bitmap sized to fill the View
        inJustDecodeBounds = false
        inSampleSize = scaleFactor
        inPurgeable = true
    }
    BitmapFactory.decodeFile(currentPhotoPath, bmOptions)?.also { bitmap ->
        imageView.setImageBitmap(bitmap)
    }
}
```

### Java

```java
private void setPic() {
    // Get the dimensions of the View
    int targetW = imageView.getWidth();
    int targetH = imageView.getHeight();

    // Get the dimensions of the bitmap
    BitmapFactory.Options bmOptions = new BitmapFactory.Options();
    bmOptions.inJustDecodeBounds = true;

    BitmapFactory.decodeFile(currentPhotoPath, bmOptions);

    int photoW = bmOptions.outWidth;
    int photoH = bmOptions.outHeight;

    // Determine how much to scale down the image
    int scaleFactor = Math.max(1, Math.min(photoW/targetW, photoH/targetH));

    // Decode the image file into a Bitmap sized to fill the View
    bmOptions.inJustDecodeBounds = false;
    bmOptions.inSampleSize = scaleFactor;
    bmOptions.inPurgeable = true;

    Bitmap bitmap = BitmapFactory.decodeFile(currentPhotoPath, bmOptions);
    imageView.setImageBitmap(bitmap);
}
```