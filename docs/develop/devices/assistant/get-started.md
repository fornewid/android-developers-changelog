---
title: https://developer.android.com/develop/devices/assistant/get-started
url: https://developer.android.com/develop/devices/assistant/get-started
source: md.txt
---

App Actions let users launch functionality in your Android app by asking
Google Assistant or by using Android shortcuts suggested by Assistant. These
are the primary steps to extend your Android app with App Actions:

1. Identify the in-app functionality to trigger and its matching [built-in intent (BII)](https://developer.android.com/reference/app-actions/built-in-intents).
2. Provide fulfillment details for the BII.
3. Push shortcuts for your App Action to Assistant.
4. Preview your App Actions on a test device.
5. Create a test release of your app.
6. Request App Actions review and deployment.

Optionally, you can define dynamic shortcuts to provide to Assistant so it can
suggest them to your users. Create an App Action using a sample app by
following the [App Actions codelab](https://codelabs.developers.google.com/codelabs/appactions/).

> [!CAUTION]
> **Caution:** Due to regulatory restrictions, apps participating in the [Designed
> for Families](https://support.google.com/googleplay/android-developer/answer/9893335) (DFF) program are not allowed to have App Actions. If you submit an App Action for review for an app that is included in the DFF program, it cannot be approved.

## Requirements

Before you start developing App Actions, make sure you and your app meet the
following requirements:

- You must have a Google Account with access to the [Google Play Console](https://play.google.com/apps/publish/).
- Your app must be published to the Google Play Store, because App Actions are only available for apps published there. Also, make sure that your app is not intended to be used in a work profile, as App Actions are not supported by Managed Google Play.
- You need a physical or virtual device to test your App Actions on.
- Install the latest compatible version of Android Studio supported by the [Google Assistant Plugin](https://plugins.jetbrains.com/plugin/16739-google-assistant/versions).
- You must use the same Google Account to [sign in](https://developer.android.com/studio/intro#sign-in) to Android Studio, the Google app on your test device, and the Google Play Console.
- You must set up Assistant on your test device and test it by performing a touch \& hold on the **Home** button.

## Match built-in intents with app functionality

Identify the functionality in your Android app that users might want
to jump to with a spoken request and review the
[built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents) to find appropriate BIIs
for your use cases. BIIs model user queries for tasks they want to
perform, so look for BIIs that match key functionality and user
flows in your app.

There are [common BIIs](https://developer.android.com/reference/app-actions/built-in-intents/common) that almost any Android app can use, such as extending
your in-app search to Assistant with the [`actions.intent.GET_THING`](https://developer.android.com/reference/app-actions/built-in-intents/common/get-thing)
BII or letting users launch specific app features with their voice by
implementing the [`actions.intent.OPEN_APP_FEATURE`](https://developer.android.com/reference/app-actions/built-in-intents/common/open-app-feature) BII.

> [!IMPORTANT]
> **Important:** As part of the [App Actions deployment requirements](https://developer.android.com/guide/app-actions/get-started#request-review), apps that have a search function must implement the `actions.intent.GET_THING` BII so that users can search for content in your app with commonly used voice commands like *"Hey Google, search for running shoes on
> Example App."*

There are also BIIs that enable *vertical* , or category-specific, use cases. For
example, an exercise app might use the [`actions.intent.START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise)
BII.

> [!NOTE]
> **Note:** For cases where there isn't a BII for your app functionality, you can use a [custom intent](https://developer.android.com/guide/app-actions/custom-intents) to extend your app with App Actions.

To ensure a great user experience, and avoid possible approval delays, make
sure that each BII you implement is relevant to your in-app functionality.

App Actions work by starting Android intents from the Assistant app to take
users directly to specific content in your app. You can define intents to
launch an activity [explicitly](https://developer.android.com/guide/components/intents-filters#ExampleExplicit) by specifying the `targetClass` and
`targetPackage` fields. If your app already implements [Android deep link](https://developer.android.com/training/app-links/deep-linking)
URLs, you have the option to configure the intent to use a deep link for
fulfillment. For more details, see the [Test your activity deep
links](https://developer.android.com/develop/devices/assistant/get-started#deep-links) section.

## Provide fulfillment details for built-in intents

Most of building an App Action is declaring a [capability](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities) in the
[`shortcuts.xml`](https://developer.android.com/guide/app-actions/action-schema) resource file of your Android app where you
specify your selected BII and its corresponding fulfillment. A BII models the
user query for a task, and a fulfillment intent provides Assistant with
information on how to perform the task.

In your `shortcuts.xml` file, BIIs are represented as `<capability>`
elements, and each fulfillment is represented as an `<intent>` element:

    <shortcuts>
        <capability android:name="actions.intent.START_EXERCISE">
            <intent
                android:action="android.intent.action.VIEW"
                android:targetPackage="com.example.app"
                android:targetClass="com.example.app.browse">
                <parameter
                    android:name="exercise.name"
                    android:key="exercise_name">
                </parameter>
            </intent>
        </capability>

> [!NOTE]
> **Note:** The Jetpack library [`androidx.core:core:1.6.0`](https://developer.android.com/jetpack/androidx/releases/core) (or later) is required in your Android project to avoid compilation errors when defining App Actions capabilities in `shortcuts.xml`. For details, see [Getting started with Android Jetpack](https://developer.android.com/jetpack/getting-started).

For most BIIs, you extract intent parameters from the user query
based on [schema.org](https://schema.org) entities. Your app then uses those BII
parameters to direct users to the selected capability. For example, the
preceding
code maps the `exercise.name` BII parameter to the `exercise_name` Android
`intent` parameter.

If you are fulfilling actions using deep links, you use the `urlTemplate` field
to define the deep link URL Assistant generates:

    <shortcuts>
        <capability android:name="actions.intent.START_EXERCISE">
            <intent android:action="android.intent.action.VIEW">
                <url-template android:value="myexerciseapp://start{?exercise_name}" />
                <parameter android:name="exercise.name"
                    android:key="exercise_name"
                    android:mimeType="text/*">
                </parameter>
            </intent>
        </capability>
    </shortcuts>

> [!NOTE]
> **Tip:** When your app provides multiple intents to fulfill for a single BII, Assistant attempts to resolve them in the order they appear in within the `capability` element.

For important details about adding App Actions to the `shortcuts.xml` file,
refer to [Create `shortcuts.xml`](https://developer.android.com/guide/app-actions/action-schema). That page also
describes how to specify the parameter values your app expects.

## Implement the GET_THING built-in intent

If your app has a search function, you are required to implement the
`actions.intent.GET_THING` BII for that function. Assistant can then forward
users to your app's search function for in-app results when they make queries
like *"Hey Google, search for Example Thing on Example App."*

In your `shortcuts.xml` file, implement a `<capability>` for
the `actions.intent.GET_THING` BII as you
[implement any other BII](https://developer.android.com/guide/app-actions/intents). You can use multiple fulfillments for
`GET_THING` as long as you provide at least one fulfillment that passes the user
query to your app's search function.

Here's an example of adding the `actions.intent.GET_THING` BII in
`shortcuts.xml`:

      <capability android:name="actions.intent.GET_THING">
        <intent
          android:targetPackage="com.example.myapp"
          android:targetClass="com.example.myapp.MySearchActivity">
          <parameter android:name="thing.name" android:key="query" />
        </intent>
      </capability>

In your search `Activity`, extract the search query from the extra data of the
`intent` and pass it to your app's search function. In the preceding code, the
search query, passed as the `query` key, maps to the `"thing.name"`
BII parameter. Then, perform a search with the query and display the results in
the user interface.

## Optional: Push shortcuts for your App Action to Assistant

Once you define a capability for your action, users can launch your
action by saying something like, *"Hey Google, order a pizza on Example App."*
Assistant can suggest Android shortcuts for your actions to users at relevant
times, letting them to discover and replay your actions. Assistant
can suggest both dynamic and static shortcuts.

To push dynamic shortcuts to Assistant, use the Google Shortcuts Integration
library. This Jetpack library enables Assistant to take in your shortcuts and
suggest them to users at the appropriate time.

For more details, see [Push dynamic shortcuts to Assistant](https://developer.android.com/guide/app-actions/dynamic-shortcuts).

## Preview your App Actions

During development and testing, use the
[Google Assistant plugin](https://developer.android.com/guide/app-actions/test-tool) for Android Studio to test that
App Actions work for your app. The plugin creates a preview of your App Actions
in Assistant for your Google Account. Using the test tool, you can test your
fulfillments on a physical test device or emulator by providing BIIs with input
parameters you expect to receive from users.

> [!NOTE]
> **Note:** You can also add additional testers for your App Actions integration, even if they don't share the same Play console account. To learn more, see [Add additional testers](https://developer.android.com/guide/app-actions/test-tool#additional-testers).

While previewing your App Actions, you can trigger queries by voice on the
device. This functionality is only available for queries listed in the
BII reference for App Actions. Use voice
triggering only for demonstration, not for regular testing.

> [!NOTE]
> **Note:** The App Actions test tool only supports testing BIIs in the en-US locale unless example queries for other locales are provided in the corresponding [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents).

Test your app in draft mode using the developer tools for the Google Play
Console before submitting the app for review.
For more information on using Google Play Console to deploy a draft
of your app, see [Prepare and launch a
release](https://support.google.com/googleplay/android-developer/answer/9859348).

## Create a test release

When you're ready to test your App Actions with additional testers,
create an internal or closed [test release](https://support.google.com/googleplay/android-developer/answer/9845334) of your app.
By default, your internal and
closed release testers can access App Actions that have already been
[reviewed and approved](https://developer.android.com/develop/devices/assistant/get-started#request-review).

To grant testing access to all App Actions, including unapproved actions,
instruct your testers to join the
[App Actions Development Program](https://groups.google.com/g/app-actions-development-program) Google Group. Members of this
group have access to all App Actions in closed and
internal test releases without having to create previews using the
[app actions test tool](https://developer.android.com/guide/app-actions/test-tool). It can take up to three hours after joining the group
for access to become available.

> [!NOTE]
> **Note:** App Actions in open testing track releases are not available to users until the actions have been reviewed and approved. For more information, see the next section.

## Request App Actions review and deployment

App Actions aren't available to users of your published apps or open test
releases until they're reviewed and approved. The App Actions review does not
affect your Android app review and deployment status in Google Play. Even if
your app submission is approved and published to the Play store, your
`shortcuts.xml` might be under review by Google. App Actions don't work for your
end users until that review is also approved.

When you deploy your app, App Actions stay activated. However,
redeployed versions are subject to review by Google. If the new version is
not working properly or contains policy violations, Google es the right to
deactivate App Actions for your app.

To submit your App Actions for review, do the following:

1. Accept the App Actions terms of service in the Google Play Console
   (**Advanced settings \> App Actions**):

   ![App Actions Terms of Service in the Google Play console.](https://developer.android.com/static/guide/app-actions/images/play_app_actions_tos.png)
2. [Upload your app](https://developer.android.com/studio/publish/upload-bundle), containing `shortcuts.xml`, to the
   Google Play Console as normal for publishing.

3. After you upload your app to the Play Console, Google contacts you at the
   email in your Play Console account with more information regarding the status
   of your App
   Actions review. You can also [contact](https://support.google.com/actions-console/contact/support) Assistant Developer Support
   with questions regarding your App Actions review status. In the contact
   form, provide your app package ID and choose **App Action review** in the
   **How can we help you?** selection box.

> [!NOTE]
> **Note:** If your app is restricted based on login credentials, provide a test login with app submission. To provide test credentials, select your app in the Play Console, browse to **Policy \> App Content** , and follow the instructions listed for **App access**.

## Optional: Test your activity deep links

To use a deep link to launch an `Activity` using an App Action, the `Activity`
must be set up with deep link URLs and have a corresponding intent filter in
the Android app manifest.

> [!NOTE]
> **Note:** The deep link can be based on [App Links URLs](https://developer.android.com/studio/write/app-link-indexing), [intent-based URLs](https://developer.chrome.com/multidevice/android/intents), or custom schemes, like `myapp://do.thing/param=value`.

To test that your activities are accessible and can be triggered using
App Actions using deep links, run the following `adb` command:

    $ adb shell am start -a android.intent.action.VIEW -d "AppLinksURL"

For example:

    $ adb shell am start -a android.intent.action.VIEW -d "https://www.example.com/deeplink"

If your activity doesn't launch correctly with the `adb` command, then
check the following:

- In your app manifest file, the activity has `android:exported=true`, so it can be launched using intents from Google Assistant.
- If using App Links URLs, follow all the steps in [Handling Android App Links](https://developer.android.com/training/app-links).

## App Actions policies

App Actions must comply with specific policies to help ensure that the users who
trigger them receive the intended experience. Review these policies before
submitting your apps to provide the best user experience and to avoid Play
Store review delays or rejections.

- **Direct users to user-intended content**

  App Action built-in intents (BIIs) and/or parameters must only direct users to
  the relevant and user-intended action. This can include in-app content,
  website content, or information shown in slices or widgets so long as the
  experience was intended by the user.

  For example, implementations of the [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII help users
  initiate an exercise of a certain type, for example, running or swimming. The only
  exception to this policy is when your [`OPEN_APP_FEATURE`](https://developer.android.com/reference/app-actions/built-in-intents/common/open-app-feature) BII directs users
  to your app's home screen.
- **Implement relevant App Actions BIIs**

  Implemented BIIs must be directly related to the app's content and
  functionality.

  For example, if your app is in the Communications Play Store category,
  don't implement the [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII, which is
  recommended for apps in the Heath and Fitness category.
- **Implement relevant custom intents**

  Defined queries for [custom intents](https://developer.android.com/guide/app-actions/custom-intents) relate to the app's content and
  functionality. An example of a potential violation to this
  policy is creating the intent `custom.action.intent.GET_RECIPE` with the
  associated query pattern "Show me burrito recipes" for an app in the
  Transportation Play Store category.

*** ** * ** ***