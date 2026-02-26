---
title: https://developer.android.com/develop/devices/assistant/test-tool
url: https://developer.android.com/develop/devices/assistant/test-tool
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

The Google Assistant plugin tests App Actions within Android Studio.
During development and testing, you use the plugin to create a preview of your
App Actions in Assistant for your Google Account. You can then test how your
App Action handles various parameters prior to submitting it for deployment.

## How it works

The Google Assistant plugin includes the App Actions Test Tool, a feature that
parses your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file and creates a preview of your App Actions for a
single Google Account. These previews enable Google Assistant to recognize your
App Actions prior to deploying the production version of your app to the Google
Play Console.

For each built-in intent (BII) in your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file, the tool renders
a corresponding JSON-LD object and provides default parameter values. You can
then modify those values to test your App Actions with meaningful parameter
combinations and ensure they perform the correct app functions. Previews are
created, updated, and deleted in the test tool, letting you iterate and
test your App Actions in a safe environment.

Once a preview is created, you can trigger an App Action on your test device
directly from the test tool window. For BIIs that are available
for user triggering, you can use the `app name` directly in Assistant on your
device to try out your App Action. For example, you can say, *"Hey Google,
start my exercise using Example App"* to launch an App Action that uses the
[`actions.intent.START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII.

## Locale support

Creating previews for specific locales in the test tool varies by BII.
The page for each BII in the [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents) provides
information on what functionality is available for that BII, like
whether the test tool supports creating previews for a specific locale, and
whether App Actions are available for users to trigger.

## Get the plugin

The Google Assistant plugin is available for Android Studio. For
information about installing and using Android Studio, see the
[Android Studio](https://developer.android.com/studio) page.

To install the Google Assistant plugin in Android Studio, follow these steps:

1. Go to **File** \> **Settings** (**Android Studio** \> **Preferences** on macOS).
2. In the **Plugins** section, go to **Marketplace** and search for "Google Assistant plugin."
3. Install the tool and restart Android Studio.

You can also download the plugin directly from the
[Jetbrains public repository](https://plugins.jetbrains.com/plugin/16739-google-assistant).

## Setup requirements

Using the Google Assistant plugin requires a number of configuration steps to
let your App Action be successfully tested. In particular, you must use the
*same user account* in Android Studio, on your test device, and for Google Play
console access.

Prepare your development environment with the following configurations:

- [Sign in](https://developer.android.com/studio/intro#sign-in) to Android Studio (version 4.0 or later).
- With the same account, sign in to the Google app on your Android test device.
- With the same account, get [Play Console access](https://support.google.com/googleplay/android-developer/answer/2528691) to the uploaded app package to be tested.
- Open the Google app on your Android test device and finish the initial Assistant setup process.
- Enable [device data syncing](https://myaccount.google.com/deviceapps) on your test device.

## Limitations

The Google Assistant plugin has the following limitations:

- App Actions that incorporate [web inventory](https://developer.android.com/guide/app-actions/web-inventory) and [foreground app invocation](https://developer.android.com/guide/app-actions/foreground-app) can't be tested directly in the test tool or by Android debug bridge (`adb`) commands. To test those App Actions, first create a preview using the test tool. Then, trigger those App Actions by interacting with Google Assistant on your physical device.
- Inline inventory for the [`actions.intent.OPEN_APP_FEATURE`](https://developer.android.com/reference/app-actions/built-in-intents/common/open-app-feature) BII can only be tested for a period of six hours after a preview is created or updated. Update the test tool preview or create a new preview to reset the six-hour time period.

## Add additional testers

You can invite additional users to your project so they can test your
App Actions integration. This is useful when you want to share the project
with other members of your development team so they can all test, or when
sharing your project with quality assurance (QA) testers in preparation for
production launch. Testers must be added as *license testers* on the Google
Play Store and granted read-only access to Google Play Console.

To add additional testers, follow these steps:

1. Sign in to the [Play Console](https://play.google.com/apps/publish).
2. Follow the instructions under **Set up application licensing** in this
   [Play Console Help topic](https://support.google.com/googleplay/android-developer/answer/6062777).

   ![Add a license tester via the Google Play Console.](https://developer.android.com/static/guide/app-actions/images/license-tester-1.png) **Figure 1.** Adding a license tester.

   > [!NOTE]
   > **Note:** This step grants read and write preview access to the Google Account.

3. Invite the license tester's Google Account as a Google Play Console read-only
   user.

   1. Select **User and permissions \> Invite new users \> Add app**.
   2. In **App Access** , ensure the **Admin (all permissions)** checkbox is cleared.

> [!NOTE]
> **Note:** Testers must accept the invitation to access the preview.

For each tester you want to enable for preview testing, you must log in
separately to Android Studio with that user's Google Account. Once logged in,
use the Google Assistant plugin to [create a preview](https://developer.android.com/develop/devices/assistant/test-tool#preview) for the test user.

## Use the Google Assistant plugin

Access the App Actions test tool in Android Studio by going to **Tools \> Google Assistant \>
App Actions test tool**. When you open the tool, the view changes based on
whether you have an active test tool preview.

### Create, update, and delete previews

You can use a draft version of the app for testing. For more information,
see [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348). Test your app in draft mode before
submitting it for review.

> [!NOTE]
> **Note:** Use the App Actions test tool with app builds installed to your device from Android Studio.

The test tool creates previews based on your Google Account and app package name
([application ID](https://developer.android.com/studio/build/application-id)), so you can test multiple apps with the same
Google Account. As long as your application ID is different for each app, you
can continue to use the same Google Account for preview creation and testing.
Multiple Google Accounts with access to the same app package can each use the
test tool to create separate previews for that app.

> [!NOTE]
> **Note:** If you don't have an active preview, then you must create one before you can use the plugin for testing your App Action.

To create a preview, do the following in Android Studio:

1. Open the App Actions test tool.
2. Optionally enter an app name and locale for testing. The default app name and locale are `test app action` and `en`.
3. Click **Create Preview** . If prompted, review and accept the App Actions policies and terms of service. Once your preview is created, the test tool window updates to display information about BIIs found in your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file.

The test tool uses the app name to construct and simulate Assistant
queries for your App Actions. Deployed App Actions use your Play Store app name
for invocation, but you can use any invocation name in the test tool.
However, we recommend using the name of your app as your invocation name in the
test tool.

The locale you provide must match the language of Google Assistant on your
test device, and you can only create a preview in one locale at a time. For
example, if your Assistant language is English (US), you can enter `en-US` but
not `en-**`, `en-GB`, or `en-US, en-GB`. You can use a root locale, such
as `en`, to include both `en-GB` and `en-US`.

To change the app name or selected locale for an existing preview, click
the **Delete** button in the test tool. Then, enter the desired
app name and locale before creating a new preview.

To update an existing preview to match your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file, click the
**Update** button in the test tool. Information about your current
preview is in the **Test App Action** section of the test tool window.

> [!CAUTION]
> **Caution:** Changes you make to your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file don't automatically propagate to your existing preview. You must update your preview in the test tool before you can test new changes.

### Configure a BII

Once you create a preview for your app, you can test various parameter
values for BIIs in the plugin. For each BII in your
[shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file, the plugin renders a corresponding
JSON-LD object and provides default parameter values. You can modify those
default values to test your App Actions with meaningful parameter combinations
and ensure they perform the correct app functions.

Parameters and their values typically follow the `schema.org` or
`schema.googleapis.com` structure for properties and descriptions. You can find
information about any BII parameter by accessing the schema
type descriptions of a parameter and its higher-level parameters.

For example, the [`actions.intent.GET_FOOD_OBSERVATION`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/get-food-observation) BII
supports the intent parameter `foodObservation.forMeal`.
The
`schema.googleapis.com` page for `MealType` lists `name` as a
property.
The `forMeal` property is a mode of transfer, and it expects
values (like `MealTypeLunch`) of the enumerated `MealType` type.

In the
test tool, you can provide any of the enumerations as the value of
`foodObservation.forMeal`:

- `https://schema.googleapis.com/MealTypeSnack`
- `https://schema.googleapis.com/MealTypeBrunch`
- `https://schema.googleapis.com/MealTypeLunch`
- `https://schema.googleapis.com/MealTypeBreakfast`
- `https://schema.googleapis.com/MealTypeDinner`
- `https://schema.googleapis.com/MealTypeDesert`

### Trigger App Actions

After creating a preview and configuring a BII, you can trigger an
App Action on your test device directly from the test tool window.

To trigger an App Action with the test tool, do the following:

1. Connect your test device.
2. In the **Select Target Device** section, choose the device where you want to trigger your App Action.
3. In the **Test App Action** section, click the **Run App Action** button.

App Actions triggered in the test tool use the displayed
[Android Debug Bridge](https://developer.android.com/studio/command-line/adb) (`adb`) command. The generated `adb` shell command
includes all the metadata required by the Google app to execute a BII.
This approach mimics the behavior of your App Action after Assistant
extracts key pieces of information from a query.

### Android Studio logging

Logs specific to the test tool are available in the
[Android Studio log files](https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files), not as Logcat
output. Processes running directly on your workstation generate Android Studio
logs. You can use them to troubleshoot test tool operations like creating,
updating, or deleting a preview.

To access your Android Studio log files, go to **Help \> Show log in explorer**
(**Help \> Show log in finder** on macOS).

Logs related to App Actions for your app are available in [Logcat](https://developer.android.com/studio/debug/am-logcat).
Logcat captures logs from virtual or physical devices connected to Android
Studio.

To get App Actions logs for your device, follow these steps:

1. Access your Logcat log messages by clicking **Logcat** in the Android Studio tool window bar.
2. Search for logs that include `ActivityTaskManager`.

### Get support and additional resources

The Google Assistant plugin provides links to documentation, codelabs,
and other resources for learning and getting help using the test tool.

You can open the assistant in Android Studio by selecting
**Tools \> Google Assistant \> Help**.

![App Actions test tool assistant](https://developer.android.com/static/guide/app-actions/images/test-tool-helper.png)
**Figure 2.** The help section of the Google Assistant plugin.