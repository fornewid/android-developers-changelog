---
title: https://developer.android.com/about/versions/oreo/android-8.1
url: https://developer.android.com/about/versions/oreo/android-8.1
source: md.txt
---

Android 8.1 (API level 27) introduces a variety of
new features and capabilities for users and developers.
This document highlights what's new for developers.

## Android Oreo (Go edition)


[Android Go](https://android-developers.googleblog.com/2017/05/whats-new-in-android-o-developer.html) is our initiative to optimize the Android experience for
billions of people coming online around the world. Starting with Android 8.1,
we're making Android a great platform for entry-level devices. Features in the Android Oreo
(Go edition) configuration include:

- **Memory optimizations.** Improved memory usage across the platform to ensure that apps can run efficiently on devices with 1GB or less RAM.
- **Flexible targeting options.** New [hardware feature
  constants](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_RAM_LOW) to let you target the distribution of your apps to normal or low-RAM devices through Google Play.
- **Google Play.** While all apps will be available on devices running Android Oreo (Go edition), Google Play will give visibility to apps specifically optimized by developers to provide a great experience for billions of people with the building for billions [guidelines.](https://developer.android.com/develop/quality-guidelines/building-for-billions.html)


We've updated the building for billions
[guidelines](https://developer.android.com/develop/quality-guidelines/building-for-billions.html) with additional guidance on how to
[optimize your app for devices running
Android Oreo (Go edition)](https://developer.android.com/develop/quality-guidelines/building-for-billions-device-capacity.html#androidgo). For most developers, optimizing your existing APK or using
Google Play's [Multiple APK feature](https://developer.android.com/google/play/publishing/multiple-apks.html) to target a version of your APK to low-RAM devices
is the best way to prepare for devices running Android Oreo (Go edition). Remember that making your
app [lighter and more efficient](https://medium.com/googleplaydev/shrinking-apks-growing-installs-5d3fcba23ce2) benefits your whole audience, regardless of device.

## Neural Networks API


The Neural Networks API provides accelerated computation and inference for on-device machine
learning frameworks like [TensorFlow
Lite](https://www.tensorflow.org/mobile/tflite/)---Google's cross-platform ML library for mobile---
as well as Caffe2 and others. Visit the TensorFlow Lite
[open source
repo](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite) for downloads and docs.
TensorFlow Lite works with the Neural Networks API to run models like
[MobileNets](https://research.googleblog.com/2017/06/mobilenets-open-source-models-for.html),
[Inception v3](https://arxiv.org/abs/1512.00567),
and [Smart Reply](https://research.googleblog.com/2017/11/on-device-conversational-modeling-with.html) efficiently on your mobile device.

## Autofill framework updates


Android 8.1 (API level 27) provides several improvements to the Autofill
Framework that you can incorporate into your apps.


The `https://developer.android.com/reference/android/widget/BaseAdapter.html`
class now includes the `https://developer.android.com/reference/android/widget/BaseAdapter.html#setAutofillOptions(java.lang.CharSequence...)`
method, which allows you to provide string representations of the values in an
adapter. This is useful for [spinner](https://developer.android.com/guide/topics/ui/controls/spinner)
controls that dynamically generate the values in their adapters. For example,
you can use the `setAutofillOptions()` method to provide a string
representation of the list of years that the users can choose as part of a
credit card expiration date. Autofill services can use the string representation
to appropriately fill out the views that require the data.


Additionally, the `https://developer.android.com/reference/android/view/autofill/AutofillManager.html`
class includes the `https://developer.android.com/reference/android/view/autofill/AutofillManager.html#notifyViewVisibilityChanged(android.view.View,
int, boolean)` method
that you can call to notify the framework about changes in the visibility of a
view in a virtual structure. There's also an overload of the method for non
virtual structures. However, non virtual structures usually don't require you to
explicitly notify the framework because the method is already called by the
`https://developer.android.com/reference/android/view/View.html`
class.


Android 8.1 also gives Autofill Services more ability to customize the save UI
affordance by adding support for `https://developer.android.com/reference/android/service/autofill/CustomDescription.html` `https://developer.android.com/reference/android/service/autofill/Validator.html`
within `https://developer.android.com/reference/android/service/autofill/SaveInfo.html`.


Custom descriptions are useful to help the autofill service clarify what is
being saved; for example, when the screen contains a credit card, it could
display a logo of the credit card bank, the last four digits of the credit card
number, and its expiration number. To learn more, see the `https://developer.android.com/reference/android/service/autofill/CustomDescription.html`
class.


`https://developer.android.com/reference/android/service/autofill/Validator.html`
objects are used to avoid displaying the autofill save UI when the Validator
condition isn't satisfied. To learn more, see the [Validator](https://developer.android.com/reference/android/service/autofill/Validator.html) class along with its subclasses, [LuhnChecksumValidator](https://developer.android.com/reference/android/service/autofill/LuhnChecksumValidator.html) and [RegexValidator](https://developer.android.com/reference/android/service/autofill/RegexValidator.html).

## Notifications


Android 8.1 includes the following changes to notifications:

- Apps can now only make a notification alert sound once per second. Alert sounds that exceed this rate aren't queued and are lost. This change doesn't affect other aspects of notification behavior and notification messages still post as expected.
- `https://developer.android.com/reference/android/service/notification/NotificationListenerService` and `https://developer.android.com/reference/android/service/notification/ConditionProviderService` are not supported on low-RAM Android-powered devices that return `true` when `https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()` is called.

## EditText update

Beginning with API level 27, the `https://developer.android.com/reference/android/widget/EditText#getText()` method returns an `https://developer.android.com/reference/android/text/Editable`; previously
it returned a `https://developer.android.com/reference/java/lang/CharSequence`. This change is
backward-compatible, as `https://developer.android.com/reference/android/text/Editable` implements
`https://developer.android.com/reference/java/lang/CharSequence`.

The `https://developer.android.com/reference/android/text/Editable` interface provides valuable additional
functionality. For example, because `https://developer.android.com/reference/android/text/Editable` also
implements the `https://developer.android.com/reference/android/text/Spannable` interface, you can apply markup to
content within an instance of `https://developer.android.com/reference/android/widget/EditText`.

## Programmatic Safe Browsing actions

By using the [`WebView` implementation](https://developer.android.com/reference/android/webkit/WebView) of the Safe Browsing API, your app can
detect when an instance of `https://developer.android.com/reference/android/webkit/WebView` attempts to navigate
to a URL that Google has classified as a known threat. By default, the
`WebView` shows an interstitial that warns users of the known threat.
This screen gives users the option to load the URL anyway or return to a
previous page that's safe.

In Android 8.1, you can define programmatically how your
app responds to a known threat:

- You can control whether your app reports known threats to Safe Browsing.
- You can have your app automatically perform a particular action---such as going back to safety---each time it encounters a URL that Safe Browsing classifies as a known threat.

**Note:** For optimal protection against known threats, wait
until you've initialized Safe Browsing before you invoke a
`https://developer.android.com/reference/android/webkit/WebView` object's `https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)` method.

The following code snippets show how you can instruct your app's instances of
`https://developer.android.com/reference/android/webkit/WebView` to always go back to safety after encountering a
known threat:


AndroidManifest.xml

```text
<manifest>
    <application>
        ...
        <meta-data android:name="android.webkit.WebView.EnableSafeBrowsing"
                   android:value="true" />
    </application>
</manifest>
```


MyWebActivity.java

### Kotlin

```kotlin
private var superSafeWebView: WebView? = null
private var safeBrowsingIsInitialized: Boolean = false

// ...

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    superSafeWebView = WebView(this).apply {
        webViewClient = MyWebViewClient()
        safeBrowsingIsInitialized = false
        startSafeBrowsing(this@SafeBrowsingActivity, { success ->
            safeBrowsingIsInitialized = true
            if (!success) {
                Log.e("MY_APP_TAG", "Unable to initialize Safe Browsing!")
            }
        })
    }
}
```

### Java

```java
private WebView superSafeWebView;
private boolean safeBrowsingIsInitialized;

// ...

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    superSafeWebView = new WebView(this);
    superSafeWebView.setWebViewClient(new MyWebViewClient());
    safeBrowsingIsInitialized = false;

    superSafeWebView.startSafeBrowsing(this, new ValueCallback<Boolean>() {
        @Override
        public void onReceiveValue(Boolean success) {
            safeBrowsingIsInitialized = true;
            if (!success) {
                Log.e("MY_APP_TAG", "Unable to initialize Safe Browsing!");
            }
        }
    });
}
```


MyWebViewClient.java

### Kotlin

```kotlin
class MyWebViewClient : WebViewClient() {
    // Automatically go "back to safety" when attempting to load a website that
    // Safe Browsing has identified as a known threat. An instance of WebView
    // calls this method only after Safe Browsing is initialized, so there's no
    // conditional logic needed here.
    override fun onSafeBrowsingHit(
            view: WebView,
            request: WebResourceRequest,
            threatType: Int,
            callback: SafeBrowsingResponse
    ) {
        // The "true" argument indicates that your app reports incidents like
        // this one to Safe Browsing.
        callback.backToSafety(true)
        Toast.makeText(view.context, "Unsafe web page blocked.", Toast.LENGTH_LONG).show()
    }
}
```

### Java

```java
public class MyWebViewClient extends WebViewClient {
    // Automatically go "back to safety" when attempting to load a website that
    // Safe Browsing has identified as a known threat. An instance of WebView
    // calls this method only after Safe Browsing is initialized, so there's no
    // conditional logic needed here.
    @Override
    public void onSafeBrowsingHit(WebView view, WebResourceRequest request,
            int threatType, SafeBrowsingResponse callback) {
        // The "true" argument indicates that your app reports incidents like
        // this one to Safe Browsing.
        callback.backToSafety(true);
        Toast.makeText(view.getContext(), "Unsafe web page blocked.",
                Toast.LENGTH_LONG).show();
    }
}
```

## Video thumbnail extractor

The `https://developer.android.com/reference/android/media/MediaMetadataRetriever` class has a new method, [`getScaledFrameAtTime()`](https://developer.android.com/reference/android/media/MediaMetadataRetriever#getScaledFrameAtTime(
long,%20int,%20int,%20int)), that finds
a frame near a given time position and returns a bitmap with the same aspect
ratio as the source frame, but scaled to fit into a rectangle of given width and
height. This is useful for generating thumbnail images from video.

We recommend using this method rather than `https://developer.android.com/reference/android/media/MediaMetadataRetriever#getFrameAtTime()` which can waste memory
because it returns a bitmap with the same resolution as the source video. For
example, a frame from a 4K video would be a 16MB bitmap, far larger than you
would need for a thumbnail image.

## Shared memory API


Android 8.1 (API level 27) introduces a new
[`SharedMemory`](https://developer.android.com/reference/android/os/SharedMemory)
API. This class allows you to create, map, and manage an anonymous
[`SharedMemory`](https://developer.android.com/reference/android/os/SharedMemory)
instance. You set the memory protection
on a
[`SharedMemory`](https://developer.android.com/reference/android/os/SharedMemory)
object for reading and/or writing, and, since the
[`SharedMemory`](https://developer.android.com/reference/android/os/SharedMemory)
object is Parcelable, you can easily pass it to another process through AIDL.


The [`SharedMemory`](https://developer.android.com/reference/android/os/SharedMemory)
API interoperates with the
`ASharedMemory` facility in the NDK.
`ASharedMemory` gives access
to a file descriptor, which can then be mapped to read and write. It's a great
way to share large amounts
of data between apps or between multiple processes within a single app.

## WallpaperColors API


Android 8.1 (API level 27) allows your live wallpaper to provide color
information to the system UI. You do this by creating a `https://developer.android.com/reference/android/app/WallpaperColors.html`
object from a bitmap, a drawable, or by using three manually-selected colors.
You can also retrieve this color information.


To create a `https://developer.android.com/reference/android/app/WallpaperColors.html`
object, do either of the following:

- To create a `https://developer.android.com/reference/android/app/WallpaperColors.html` object by using three colors, create an instance of the `https://developer.android.com/reference/android/app/WallpaperColors.html` class by passing the primary, the secondary, and the tertiary color. The primary color *must not* be null.
- To create a `https://developer.android.com/reference/android/app/WallpaperColors.html` object from a bitmap, call the `https://developer.android.com/reference/android/app/WallpaperColors.html#fromBitmap(android.graphics.Bitmap)` method by passing the bitmap source as parameter.
- To create a `https://developer.android.com/reference/android/app/WallpaperColors.html` object from a drawable, call the `https://developer.android.com/reference/android/app/WallpaperColors.html#fromDrawable(android.graphics.drawable.Drawable)` method by passing the drawable source as parameter.


To retrieve the primary, secondary, or tertiary color details from the
wallpaper, call the following methods:

- `https://developer.android.com/reference/android/app/WallpaperColors.html#getPrimaryColor()` returns the most visually-representativecolor of the wallpaper.
- `https://developer.android.com/reference/android/app/WallpaperColors.html#getSecondaryColor()` returns the second most preeminent color of the wallpaper.
- `https://developer.android.com/reference/android/app/WallpaperColors.html#getTertiaryColor()` method returns the third most preeminent color of the wallpaper.


To notify the system about any significant color changes in your live wallpaper,
call the `https://developer.android.com/reference/android/service/wallpaper/WallpaperService.Engine.html#notifyColorsChanged()`
method. This method triggers an `https://developer.android.com/reference/android/service/wallpaper/WallpaperService.Engine.html#onComputeColors()` lifecycle
event where you have an opportunity to provide a new `https://developer.android.com/reference/android/app/WallpaperColors.html`
object.


To add a listener for color changes, you can call the `https://developer.android.com/reference/android/app/WallpaperManager.html#addOnColorsChangedListener(android.app.WallpaperManager.OnColorsChangedListener,
android.os.Handler)` method. You can
also call the `https://developer.android.com/reference/android/app/WallpaperManager.html#getWallpaperColors(int)` method
to retrieve the primary colors of a wallpaper.

## Fingerprint updates

The `https://developer.android.com/reference/android/hardware/fingerprint/FingerprintManager` class has
introduced the following error codes:

- `FINGERPRINT_ERROR_LOCKOUT_PERMANENT` -- The user has tried too many times to unlock their device using the fingerprint reader.
- `FINGERPRINT_ERROR_VENDOR` -- A vendor-specific fingerprint reader error occurred.

## Cryptography updates

A number of cryptography changes have been made with Android 8.1:

- New algorithms have been implemented in Conscrypt. The Conscrypt implementation is preferentially used over the existing Bouncy Castle implementation. New algorithms include:
  - `AlgorithmParameters:GCM`
  - `KeyGenerator:AES`
  - `KeyGenerator:DESEDE`
  - `KeyGenerator:HMACMD5`
  - `KeyGenerator:HMACSHA1`
  - `KeyGenerator:HMACSHA224`
  - `KeyGenerator:HMACSHA256`
  - `KeyGenerator:HMACSHA384`
  - `KeyGenerator:HMACSHA512`
  - `SecretKeyFactory:DESEDE`
  - `Signature:NONEWITHECDSA`
- [`Cipher.getParameters().getParameterSpec(IvParameterSpec.class)`](https://developer.android.com/reference/java/security/AlgorithmParameters#getParameterSpec(java.lang.Class<T>)) no longer works for algorithms that use GCM. Instead, use `getParameterSpec(GCMParameterSpec.class)`.
- Many internal Conscrypt classes associated with TLS were refactored. Since developers sometimes access these reflectively, shims have been left in place to support previous usage, but some details have changed. For example, sockets previously were of type `OpenSSLSocketImpl`, but now they're of type `ConscryptFileDescriptorSocket` or `ConscryptEngineSocket`, both of which extend `OpenSSLSocketImpl`.
- `https://developer.android.com/reference/javax/net/ssl/SSLSession` methods used to throw `IllegalArgumentException` when passed a null reference, they now throw `NullPointerException`.
- The RSA `https://developer.android.com/reference/java/security/KeyFactory` no longer allows generation of keys from byte arrays that are larger than the encoded key. Calls to `https://developer.android.com/reference/java/security/KeyFactory#generatePrivate(java.security.spec.KeySpec)` and `https://developer.android.com/reference/java/security/KeyFactory#generatePublic(java.security.spec.KeySpec)` that provide a `https://developer.android.com/reference/java/security/spec/KeySpec` where the key structure does not fill the entire buffer will result in an `https://developer.android.com/reference/java/security/spec/InvalidKeySpecException`.
- When a socket read is interrupted by the socket being closed, Conscrypt used to return -1 from the read. The read now throws `SocketException`.
- The set of root CA certificates has been changed, mostly removing a large number of obsolete certificates, but also removing the root certificates for WoSign and StartCom. For more information on this decision, see the Google Security Blog post, [Final
  removal of trust in WoSign and StartCom Certificates](https://security.googleblog.com/2017/07/final-removal-of-trust-in-wosign-and.html).