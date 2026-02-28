---
title: https://developer.android.com/develop/devices/assistant/troubleshoot
url: https://developer.android.com/develop/devices/assistant/troubleshoot
source: md.txt
---

When developing App Actions, you might encounter issues with your setup or with
the App Actions test tool. This page describes some commonly encountered issues
and their fixes.

## General

### Error: "No App found to open URL" appears in a toast notification

Check your fulfillment `urlTemplate` in your `actions.xml` to make sure it's
configured correctly. If using App Links URLs, ensure you can trigger your URL
manually using `ACTION_VIEW` and the URL. If using intent-based URLs, ensure
your Activity is correctly configured to start using the provided parameters.

### Error: "App isn't installed"

This error may mean that the `<intent-filter>` in your `AndroidManifest.xml`
file doesn't filter the deep link that you specified in your `actions.xml`.
Make sure you check this first before filing a bug.

### Error: "An entity set reference containing neither an entity set ID nor a URL filter was found." appears in Android Studio

This condition is caused by a known linter issue for the
`<entity-set-reference>` tag. You can safely ignore this message. As a
workaround, you can disable lint check for this tag by adding the
`tools:ignore="ValidActionsXml"` attribute to it.

Here's an example of an entity set reference with a disabled lint check:

```
<entity-set-reference entitySetId="example" tools:ignore="ValidActionsXml" />
```

<br />

### Error: "Invalid location" for actions schema document when uploading APK

Your APK upload may fail if you use an obfuscation or optimization tool that
affects resources for your release APK. Tools like ProGuard that avoid
resource files do not cause this issue.

To resolve this issue, try disabling the tool for your app's `actions.xml`
file (for example, by using an allowlist).

### Error: "An active APK or Android App Bundle contains an actions.xml file. In order to continue, accept the Actions on Google Terms of Service." appears in Google Play Console

You may see this error while creating an app release in the Play Console. To
accept the Actions on Google Terms of Service, follow these steps:

1. Select your app in the Play Console.
2. Navigate to **Setup \> Advanced Settings**.
3. Click the **Actions on Google** tab.
4. Check the box labeled **Integrate my services with App Actions using Actions
   on Google**, and follow the instructions.

### The "Accept" button on Play Terms of Service form is disabled.

This might mean that the signed in user doesn't have the required access
level to accept those terms. Make sure the first submission is done by the
administrator of the Play Console profile.

## App Actions test tool

Before attempting any of the following fixes, update your installation of the
App Actions test tool to the most recent version.

### The App Actions test tool plugin cannot locate my `actions.xml` file.

Ensure you have added the correct `<meta-data>` tag in your
`AndroidManifest.xml` file.

### My App Action preview doesn't match my current `actions.xml` file.

Your preview does not update itself dynamically with the content of your
`actions.xml` file. After you change your `actions.xml` file manually or after
switching build variants in Android Studio, save your `actions.xml` file and
click **Update Preview** in the test tool.

### The App Actions test tool plugin stopped working or is generating errors.

First, make sure you've updated Android Studio to the latest version. If
you are getting a 403 error, you also might be running the plugin on a
package where you don't have permissions to run on.

If the error still persists, please file a bug and send the following
details to Google:

- Details of the error dialog
- Android Studio Logs. Go to **Help \> Show Log in Finder** . This shows you the location of the `idea.log` in your Finder. Search for "Submit Actions Request Body:" in the log file, and paste the server responses (there should be two results for actions).

### The App Actions test tool generates `UnknownHostException`, or other network errors

The App Actions test tool creates a preview of your App Actions, enabling you to
test Google Assistant integrations with a single Google Account. To create these
previews, the test tool requires an active internet connection and, if
necessary, proxy access to Google domains.

To resolve network issues when running the test tool, check for these common
issues:

- Ensure you have an active internet connection before generating previews.
- If your internet connection is active, and your local network uses a proxy
  server, check the following:

  - Verify your IDE proxy configuration. For more information, see proxy configuration instructions for [Android Studio](https://developer.android.com/studio/intro/studio-config#proxy), or [IntelliJ](https://www.jetbrains.com/help/idea/settings-http-proxy.html).
  - If your proxy requires an access control list (ACL), update the ACL to allow this URL pattern: `https://actions.googleapis.com/**`.

### When invoking the App Action with the test plugin, the Assistant says, "Sorry, I couldn't find that."

Depending on your setup, this response may appear for different reasons. Try
the following steps:

1. Sign in to Android Studio, the Play Console, and your test device with the same Google Account.
2. Enable [device data syncing](https://myaccount.google.com/deviceapps).
3. Set the device and Google Assistant language to `en-US`.
4. Check that the package name of the application in the Google Play Console matches with the package name in the test application.
5. In the fulfillment `urlTemplate`definition in your `actions.xml` file, make sure that the `android:host` and `android:scheme` values match what's declared in the `AndroidManifest` file.
6. Remove all previous installations of your app from your test device and install a fresh build.
7. Delete the preview from App Actions test tool and create a new preview again.
8. Check in the Logcat tool for failures related to fulfillment for Google Assistant. You should see an intent launched to your app.
9. [Enable the 'App info for your devices' setting](https://support.google.com/accounts/answer/9503395?co=GENIE.Platform%3DAndroid) for the account.
10. Open Google Assistant and ensure you have completed setup. (Usually the setup progress bar appears as a blue bar at the bottom of the screen, but it may look different in some cases.)
11. When using Google Assistant to trigger an App Action, make sure that the invocation name matches the preview created by the App Actions test tool.
12. Try using text input instead of voice to avoid any transcription errors.
13. Configure your test build so that the `applicationId` exactly matches an APK or AAB uploaded to the Google Play Console. Note that optional `applicationIdSuffix` properties can change the final `applicationId` of builds for certain product flavors and build variants. In this [example](https://www.google.com/url?sa=D&q=https://github.com/android/architecture-samples/blob/master/app/build.gradle%23L53), the `applicationId` for the mock product flavor is `com.example.android.architecture.blueprints.master.mock`, instead of `com.example.android.architecture.blueprints`.
14. Configure your preview to use a unique invocation name. Try using a unique word that reduces the chances for collision with other apps.
15. To isolate issues when troubleshooting a shareable codebase, try running the [the sample App Actions Fitness App](https://github.com/actions-on-google/appactions-fitness-kotlin). Make sure that the Fitness app works end-to-end. Then incrementally add additional features on top of this app to see if you can replicate issues.
16. If using G Suite accounts, make sure Google Assistant is [turned on by the
    administrator](https://support.google.com/a/answer/9620347#:%7E:text=As%20an%20administrator%2C%20you%20control,or%20while%20working%20from%20home). We recommend creating a non-G Suite test account as a workaround and setting it up as a [licensed tester through Play Store](https://developers.google.com/assistant/app/test-tool#additional-testers). From that account, testers should be able to create previews for their app and test using that account on their device successfully.
17. If you downloaded Google Assistant as a separate app, try force stopping it on your device. You can usually force stop an app through your phone's Settings app.
18. If none of these steps work, raise a issue in the [App Action issue tracker](https://issuetracker.google.com/issues?q=componentid:617864+status:open).