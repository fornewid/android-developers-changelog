---
title: https://developer.android.com/games/pgs/android/troubleshooting
url: https://developer.android.com/games/pgs/android/troubleshooting
source: md.txt
---

This page describes how to troubleshoot issues that you might encounter while
developing Android games with Google Play Games Services.

## Logging

To troubleshoot problems with your game, you can turn on verbose logging
on your device using the `adb shell` command. You can then view the
Google Play Games Services log messages using logcat.

### Enable logging

To enable logging on your test device:

1. Connect the device to a machine that has the Android SDK installed.

2. Open a terminal and run this command:

   ```
   adb shell setprop log.tag.Games VERBOSE
   ```
3. Run your game on the device and reproduce the problem you are trying to
   debug.

4. View logs:

   ```
   adb logcat
   ```

### Disable logging

To disable verbose logging for the Play Games Services on your device and
revert to the original logging behavior, run the following command:

```
adb shell setprop log.tag.Games INFO
```

## Unable to authenticate

If you are unable to authenticate players into your game, first make sure that you have
followed the instructions to
[create your client IDs](https://developers.google.com/games/services/console/enabling)
and
[configure games services](https://developers.google.com/games/services/console/configuring).
If you still encounter authentication errors, check the following items to make sure
that your game is set up correctly.

### Check your metadata tags

Your `AndroidManifest.xml` must contain a games metadata tag. To verify that
your metadata tags are correctly set up:

1. Open your `AndroidManifest.xml` and verify that it contains a `meta-data` tag as shown below:

       <meta-data android:name="com.google.android.gms.games.APP_ID"
           android:value="@string/app_id" />

2. Locate the definition of your `@string/app_id` resource. It is usually defined in an XML file
   located in the `res/xml` directory, for example `res/xml/strings.xml` or `res/xml/ids.xml`.

3. Verify that the value of the `@string/app_id` resource matches your application's numeric ID.
   The value of this resource should only contain digits. For example:

       <string name="app_id">123456789012</string>

| **Warning:** Do not use the full client ID (`1233456789012.apps.googleusercontent.com`) as your app ID. This will result in errors.

### Check your package name

Your game's package name must match the package name on your client ID. To verify the package name:

1. Open your `AndroidManifest.xml` and verify that your game's package name is correct. The package
   name is the value of the `package` attribute in the `manifest` tag.

2. Verify the package name you supplied when creating your client ID. To verify
   the package name in Google Play Console, go to the
   Play Console and click on the entry corresponding to your game.

3. Go to the **Linked Apps** tab and examine the list of client IDs. There
   should be an Android linked app in this list whose package name matches the
   package name in your `AndroidManifest.xml`. If there is a mismatch, create a new
   client ID with the correct package name and try to authenticate again.

### Check the certificate fingerprint

The certificate with which you are authenticating your game should match the
certificate fingerprint associated to your client ID. To verify this, first
check your certificate's SHA1 fingerprint as follows:

1. Find your certificate file and obtain its SHA1 fingerprint. To obtain the
   SHA1 fingerprint, run this command:

       keytool -exportcert -alias your-key-name -keystore /path/to/your/keystore/file -list -v

2. Take note of the sequence of hexadecimal digits labeled `SHA1:` in the
   output. That is your certificate's fingerprint.

| **Note:** If you are using a debug certificate, replace `your-key-name` with `androiddebugkey` in the command above. If using a release certificate, use the name you chose for your key when creating the certificate.

Next, check that your build tool is using this certificate:

1. Generate your game's APK from your build tool and sign it with the desired certificate. Copy the generated APK to a temporary directory.
2. In the temporary directory, run the following command to unzip your APK.

       unzip YourGame.apk

3. Generate a private key using an RSA certificate file:

       keytool -printcert -file META-INF/CERT.RSA

   Alternatively, you can generate the private key using a DSA certificate file:

       keytool -printcert -file META-INF/CERT.DSA

4. Note the sequence of hexadecimal digits on the line labeled `SHA1:`.

   This sequence of digits should match your certificate fingerprint from the
   previous step. If there is a mismatch, your build tool or system is not
   configured to sign your application with your certificate. In this case,
   consult your build environment's documentation to determine how to configure
   it correctly and try to authenticate again.

Next, check if the certificate fingerprint matches the fingerprint configured
in your client ID. To do this:

1. Open the Play Console and navigate to your game.
2. On the **Game Details** page, scroll to the bottom and click the link to the linked Google Cloud Platform project.
3. Select your project.
4. In the sidebar on the left, select **APIs \& auth** . Make sure that the Google Play games services API status is **ON** in the displayed list of APIs.
5. In the sidebar on the left, select **Registered apps**.
6. Expand the OAuth 2.0 Client ID section and note the certificate fingerprint (SHA1).

If this fingerprint does not match your certificate's fingerprint from the
previous steps, you must create a new client ID with the correct certificate
fingerprint. You must create the new client ID in the
Play Console, not in the Google Cloud Platform project.
| **Note:** If you are debugging your game using your debug certificate but have configured games services using your release certificate, you should add a second linked app using the same package name and your debug certificate's SHA-1 fingerprint. This will allow you to authenticate to the application whether it's signed with the debug or release certificates.

### Check that test accounts are enabled

Before a game is published, the account that created the game in the
Play Console must also be enabled as a tester. To check that
this is correctly configured:

1. Open the Play Console and navigate to your game.
2. Open the **Testing** tab.
3. Check that the account you are trying to authenticate with is in the list of testers.

If the account you are trying to authenticate with is not listed, add it to the list, wait a few minutes
and try to authenticate again.
| **Warning:** The account that created the game in the Play Console does not automatically become a tester. If you wish to authenticate to the game with that account, you must add it as a tester explicitly.

## Proguard issues

If you are using Proguard and are seeing errors on the obfuscated APK, check the target API level
on your `AndroidManifest.xml`. Make sure to set it to 17 or above.

## Other causes of setup issues

Check for other common causes of errors:

- If your game is published, check that the game settings are also published (it is possible to publish the application without publishing the games settings). To do this, go to Google Play Console and navigate to your app, and check that the box next to the game's name indicates that it's published. If indicates that it is in another state, such as "Ready to Publish" or "Ready to Test", click the box and select **Publish Game**.
- If you can't publish your game, check that exactly one of the client IDs has the **This app is
  preferred for new installations** option enabled.

## Anonymous listeners

Do not use anonymous listeners. Anonymous listeners are implementations of a listener interface
that are defined inline, as illustrated below.

        ImageManager im = ...;

        // Anonymous listener -- dangerous:
        im.loadImage(new ImageManager.OnImageLoadedListener() {
            @Override
            public void onImageLoaded(Uri uri, Drawable drawable) {
                // ...code...
            }
        }

Anonymous listeners are unreliable because the Play Games SDK maintains them as weak references,
which means that they might be reclaimed by the garbage collector before they are
invoked. Instead, you should implement the listener using a persistent object
such as the
[`Activity`](https://developer.android.com/reference/android/app/Activity).

        public class MyActivity extends Activity
                implements ImageManager.OnImageLoadedListener {

            private void loadOurImages() {
                ImageManager im = ...;
                im.loadImage(this);
            }

            @Override
            public void onImageLoaded(Uri uri, Drawable drawable) {
                // ...code...
            }
        }