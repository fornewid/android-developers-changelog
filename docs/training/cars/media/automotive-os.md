---
title: https://developer.android.com/training/cars/media/automotive-os
url: https://developer.android.com/training/cars/media/automotive-os
source: md.txt
---

# Add Android Automotive OS support to your media app

Android Automotive OS lets users install apps in the car. To reach users on this platform, you need to distribute a driver-optimized app that is compatible with Android Automotive OS. You can reuse almost all the code and resources in your Android Auto app, but you must create a separate build that meets the requirements on this page.
| **Caution:** If the primary content provided by your app is video, you should follow the guidance in[Build video apps for Android Automotive OS](https://developer.android.com/training/cars/parked/video)and[Build parked apps for cars](https://developer.android.com/training/cars/parked)instead.
| **Important:** This guide assumes that you already implemented the media features in[Build media apps for cars](https://developer.android.com/training/cars/media).

## Development overview

Adding Android Automotive OS support only requires a few steps, as described in the sections that follow:

1. [Enable automotive features in Android Studio](https://developer.android.com/training/cars/media/automotive-os#set-up-project).
2. [Create an automotive module](https://developer.android.com/training/cars/media/automotive-os#automotive-module).
3. [Update your Gradle dependencies](https://developer.android.com/training/cars/media/automotive-os#gradle).
4. Optionally,[Implement settings and sign-in activities](https://developer.android.com/training/cars/media/automotive-os#settings-sign-in).
5. Optionally,[Read media host hints](https://developer.android.com/training/cars/media/automotive-os#read-media-host-hints).

## Design considerations

Android Automotive OS takes care of laying out the media content that it receives from your app's[media browser service](https://developer.android.com/training/cars/media#tc-media-browser-service). This means that your app doesn't draw the UI and doesn't start any of your activities when a user triggers media playback.

If you are implementing[settings or sign-in activities](https://developer.android.com/training/cars/media/automotive-os#settings-sign-in), these activities must be[vehicle-optimized](https://developer.android.com/training/cars/media#tc-vehicle-optimized). Refer to the[Design guidelines](https://developers.google.com/cars/design/automotive-os)for Android Automotive OS while designing those areas of your app.

## Set up your project

You need to set up several parts of your app's project to enable support for Android Automotive OS.

### Enable automotive features in Android Studio

Use Android Studio 4.0 or higher to ensure that all Automotive OS features are enabled.

### Create an automotive module

Some components of Android Automotive OS, such as the manifest, have platform-specific requirements. Create a module that can keep the code for these components separate from other code in your project, such as the code used for your phone app.

Follow these steps to add an automotive module to your project:

1. In Android Studio, click**File \> New \> New Module**.
2. Select**Automotive Module** , then click**Next**.
3. Enter an**Application/Library name**. This is the name that users see for your app on Android Automotive OS.
4. Enter a**Module name**.
5. Adjust the**Package name**to match your app.
6. Select**API 28: Android 9.0 (Pie)** for the**Minimum SDK** , and then click**Next**.

   All cars that support Android Automotive OS run on Android 9 (API level 28) or higher, so selecting this value targets all compatible cars.
7. Select**No Activity** , and then click**Finish**.

After creating your module in Android Studio, open the`AndroidManifest.xml`in your new automotive module:  

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.media">

        <application
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            android:roundIcon="@mipmap/ic_launcher_round"
            android:supportsRtl="true"
            android:theme="@style/AppTheme" />

        <uses-feature
            android:name="android.hardware.type.automotive"
            android:required="true" />

    </manifest>

The[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)element has some standard app information as well as a[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element that declares support for Android Automotive OS. Note that there are no activities declared in the manifest.

If you implement[settings or sign-in activities](https://developer.android.com/training/cars/media/automotive-os#settings-sign-in), add them here. These activities are triggered by the system using explicit intents and are the only activities you declare within the manifest for your Android Automotive OS app.

After adding any settings or sign-in activities, complete your manifest file by setting the`<application>`element's`android:appCategory`attribute to`"audio"`.  

    <application
      ...
      android:appCategory="audio" />

### Declare feature requirements

All apps built for Android Automotive OS must meet certain requirements to be distributed using Google Play. See[Meet Google Play feature requirements](https://developer.android.com/training/cars/platforms/automotive-os#play-feature-requirements)for more information.

### Declare media support for Android Automotive OS

Use the following manifest entry to declare that your app supports Android Automotive OS:  

    <application>
        ...
        <meta-data android:name="com.android.automotive"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to an XML file that declares the automotive capabilities that your app supports.

To indicate that you have a media app, add an XML file named`automotive_app_desc.xml`to the`res/xml/`directory in your project. Include the following content in this file:  

    <automotiveApp>
        <uses name="media"/>
    </automotiveApp>

| **Note:** Don't include any references to the`com.google.android.gms.car.application`attribute that is required for Android Auto in your Android Automotive OS app.

#### Intent filters

Android Automotive OS uses explicit intents to trigger activities in your media app. Don't include any activities that have[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)or[`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN)intent filters in the manifest file.

Activities like the one in the following example usually target a phone or some other mobile device. Declare these activities in the module that builds the phone app, not in the module that builds your Android Automotive OS app.  

    <activity android:name=".MyActivity">
        <intent-filter>
            <!-- You can't use either of these intents for Android Automotive OS -->
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
            <!--
            In their place, you can include other intent filters for any activities
            that your app needs for Android Automotive OS, such as settings or
            sign-in activities.
            -->
        </intent-filter>
    </activity>

| **Caution:** Dependencies may add activities with these intent filters. Use the[Merged manifest view](https://developer.android.com/build/manage-manifests#inspect_the_merged_manifest_and_find_conflicts)to check the final manifest generated for your app. See[Manage manifest files](https://developer.android.com/build/manage-manifests#merge-manifests)for additional guidance.

### Update your Gradle dependencies

We recommend that you keep your[media browser service](https://developer.android.com/training/cars/media#tc-media-browser-service)in a separate module that you share between your phone app and your automotive module. If you're using this approach, you need to update your automotive module to include the shared module, as shown in the following snippet:

<var translate="no">my-auto-module</var>`/build.gradle`  

### Groovy

```groovy
buildscript {
    ...
    dependencies {
        ...
        implementation project(':<var translate="no">shared_module_name</var>')
    }
}
```

### Kotlin

```kotlin
buildscript {
    ...
    dependencies {
        ...
        implementation(project(":<var translate="no">shared_module_name</var>"))
    }
}
```

## Implement settings and sign-in activities

In addition to your media browser service, you can also provide[vehicle-optimized](https://developer.android.com/training/cars/media#tc-vehicle-optimized)settings and sign-in activities for your Android Automotive OS app. These activities let you provide app functionality that isn't included in the Android Media APIs.

Only implement these activities if your Android Automotive OS app needs to let users sign in or specify app settings. These activities aren't used by Android Auto.
| **Design guidelines:** While you implement your settings and sign-in activities, refer to[Adapt sign-in flow](https://developers.google.com/cars/design/automotive-os/apps/media/create-your-app/adapt-signin-flow)and[Design settings](https://developers.google.com/cars/design/automotive-os/apps/media/create-your-app/design-settings)in the Android Automotive OS app design guidelines.

### Activity workflows

The following diagram shows how a user interacts with your settings and sign-in activities using Android Automotive OS:

![Workflows for Settings and Sign-in activities](https://developer.android.com/static/images/training/cars/activity-workflows.png)

**Figure 1.**Settings and sign-in activity workflows.

<br />

### Discourage distractions in your settings and sign-in activities

To ensure your settings and/or sign-in activities are only available for use while the user's vehicle is parked, verify that the`<activity>`element(s) don't include the following`<meta-data>`element. Your app will be rejected during review if such an element is present.  

    <!-- NOT ALLOWED -->
    <meta-data
      android:name="distractionOptimized"
      android:value="true"/>

### Add a settings activity

You can add a vehicle-optimized settings activity so that users can configure settings for your app in their car. Your settings activity can also provide other workflows, like signing in or out of a user's account or switching user accounts. Remember that this activity is only triggered by an app running on Android Automotive OS. Phone apps connected to Android Auto do not use it.

#### Declare a settings activity

You must declare your settings activity in your app's manifest file, as shown in the following code snippet:  

    <application>
        ...
        <activity android:name=".AppSettingsActivity"
                  android:exported="true"
                  android:theme="@style/SettingsActivity"
                  android:label="@string/app_settings_activity_title">
            <intent-filter>
                <action android:name="android.intent.action.APPLICATION_PREFERENCES"/>
            </intent-filter>
        </activity>
        ...
    </application>

| **Caution:** The[`android:exported`](https://developer.android.com/guide/topics/manifest/service-element#exported)attribute is set to`true`to allow Android Automotive OS to invoke your settings activity, but this also allows other apps to invoke this activity. If your app needs to process any intent data passed in to your activity, be sure to validate the data to avoid potential security issues.

#### Implement your settings activity

When a user launches your app, Android Automotive OS detects the settings activity that you declared and displays an affordance, such as an icon. The user can tap or select this affordance using their car's display to navigate to the activity. Android Automotive OS sends the[`ACTION_APPLICATION_PREFERENCES`](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_PREFERENCES)intent that tells your app to start your settings activity.
| **Note:** Your settings activity must provide an affordance that lets the user return to Android Automotive OS. Your app can do this by calling the activity's[`finish()`](https://developer.android.com/reference/android/app/Activity#finish())method.

The rest of this section shows how you can adapt code from the[Universal Android Music Player (UAMP) sample app](https://github.com/android/uamp)to implement a settings activity for your app.

To begin, download the sample code:  

    # Clone the UAMP repository
    git clone https://github.com/android/uamp.git

    # Fetch the appropriate pull request to your local repository
    git fetch origin pull/323/head:<var translate="no">NEW_LOCAL_BRANCH_NAME</var>

    # Switch to the new branch
    git checkout <var translate="no">NEW_LOCAL_BRANCH_NAME</var>

To implement your activity, follow these steps:

1. Copy the`automotive/automotive-lib`folder into your automotive module.
2. Define a preferences tree as in`automotive/src/main/res/xml/preferences.xml`.
3. Implement a[`PreferenceFragmentCompat`](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat)that your settings activity displays. See the`SettingsFragment.kt`and`SettingsActivity.kt`files in UAMP and the[Android Settings guide](https://developer.android.com/guide/topics/ui/settings)for more information.

   | **Note:** Using a`PreferenceFragmentCompat`also ensures your settings persist in[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences).

As you implement your settings activity, consider these best practices for using some of the components in the Preference library:

- Have no more than two levels of depth below the main view in your settings activity.
- Don't use a[`DropDownPreference`](https://developer.android.com/reference/androidx/preference/DropDownPreference). Use a[`ListPreference`](https://developer.android.com/reference/androidx/preference/ListPreference)instead.
- Organizational components:
  - [`PreferenceScreen`](https://developer.android.com/reference/androidx/preference/PreferenceScreen)
    - This must be the top level of your preferences tree.
  - [`PreferenceCategory`](https://developer.android.com/reference/androidx/preference/PreferenceCategory)
    - Used to group`Preference`objects together.
    - Include a`title`.
- Include a`key`and`title`in all the following components. You can also include a`summary`, an`icon`, or both:
  - [`Preference`](https://developer.android.com/reference/androidx/preference/Preference)
    - Customize the logic in the`onPreferenceTreeClick()`callback of your`PreferenceFragmentCompat`implementation.
  - [`CheckBoxPreference`](https://developer.android.com/reference/androidx/preference/CheckBoxPreference)
    - Can have`summaryOn`or`summaryOff`instead of`summary`for conditional text.
  - [`SwitchPreference`](https://developer.android.com/reference/androidx/preference/SwitchPreference)
    - Can have`summaryOn`or`summaryOff`instead of`summary`for conditional text.
    - Can have`switchTextOn`or`switchTextOff`.
  - [`SeekBarPreference`](https://developer.android.com/reference/androidx/preference/SeekBarPreference)
    - Include a`min`,`max`, and`defaultValue`.
  - [`EditTextPreference`](https://developer.android.com/reference/androidx/preference/EditTextPreference)
    - Include`dialogTitle`,`positiveButtonText`, and`negativeButtonText`.
    - Can have`dialogMessage`and/or`dialogLayoutResource`.
  - `com.example.android.uamp.automotive.lib.ListPreference`
    - Derives mostly from`ListPreference`.
    - Used to display a single-choice list of`Preference`objects.
    - Must have an array of`entries`and corresponding`entryValues`.
  - `com.example.android.uamp.automotive.lib.MultiSelectListPreference`
    - Derives mostly from[`MultiSelectListPreference`](https://developer.android.com/reference/androidx/preference/MultiSelectListPreference)
    - Used to display a multiple-choice list of`Preference`objects.
    - Must have an array of`entries`and corresponding`entryValues`.

### Add a sign-in activity

If your app requires a user to sign in before they can use your app, you can add a vehicle-optimized sign-in activity that handles signing in and out of your app. You can also add sign-in and sign-out workflows to a[settings activity](https://developer.android.com/training/cars/media/automotive-os#settings-activity), but use a dedicated sign-in activity if your app can't be used until a user signs in. Remember that this activity is only triggered by an app running on Android Automotive OS. Phone apps connected to Android Auto do not use it.

#### Require sign in at app start

To require a user to sign in before they can use your app, your media browser service must do the following things:

1. In your service's`onLoadChildren()`method, send`null`result using the[`sendResult()`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat.Result#sendResult(T))method.
2. Set the media session's[`PlaybackStateCompat`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat)to[`STATE_ERROR`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_ERROR())using the[`setState()`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setState(int,%20long,%20float))method. This tells Android Automotive OS that no other operations can be performed until the error has been resolved.
3. Set the media session's`PlaybackStateCompat`error code to[`ERROR_CODE_AUTHENTICATION_EXPIRED`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ERROR_CODE_AUTHENTICATION_EXPIRED()). This tells Android Automotive OS that the user needs to authenticate.
4. Set the media session's`PlaybackStateCompat`error message using the[`setErrorMessage()`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage(int,%20java.lang.CharSequence))method. Because this error message is user-facing, localize it for the user's current locale.
5. Set the media session's`PlaybackStateCompat`extras using the[`setExtras()`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setExtras(android.os.Bundle))method. Include the following two keys:

   - [`PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL()): a string that is displayed on the button that begins the sign-in workflow. Because this string is user-facing, localize it for the user's current locale.
   - [`PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT()): a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)that directs the user to your sign-in activity when the user taps the button referred to by the`PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL`.

The following code snippet shows how your app can require the user to sign in before using your app:  

### Kotlin

```kotlin
import androidx.media.utils.MediaConstants

val signInIntent = Intent(this, SignInActivity::class.java)
val signInActivityPendingIntent = PendingIntent.getActivity(this, 0,
    signInIntent, 0)
val extras = Bundle().apply {
    putString(
        MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL,
        "Sign in"
    )
    putParcelable(
        MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT,
        signInActivityPendingIntent
    )
}

val playbackState = PlaybackStateCompat.Builder()
        .setState(PlaybackStateCompat.STATE_ERROR, 0, 0f)
        .setErrorMessage(
            PlaybackStateCompat.ERROR_CODE_AUTHENTICATION_EXPIRED,
            "Authentication required"
        )
        .setExtras(extras)
        .build()
mediaSession.setPlaybackState(playbackState)
```

### Java

```java
import androidx.media.utils.MediaConstants;

Intent signInIntent = new Intent(this, SignInActivity.class);
PendingIntent signInActivityPendingIntent = PendingIntent.getActivity(this, 0,
    signInIntent, 0);
Bundle extras = new Bundle();
extras.putString(
    MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL,
    "Sign in");
extras.putParcelable(
    MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT,
    signInActivityPendingIntent);

PlaybackStateCompat playbackState = new PlaybackStateCompat.Builder()
    .setState(PlaybackStateCompat.STATE_ERROR, 0, 0f)
    .setErrorMessage(
            PlaybackStateCompat.ERROR_CODE_AUTHENTICATION_EXPIRED,
            "Authentication required"
    )
    .setExtras(extras)
    .build();
mediaSession.setPlaybackState(playbackState);
```

After the user is successfully authenticated, set the`PlaybackStateCompat`back to a state other than`STATE_ERROR`, then take the user back to Android Automotive OS by calling the activity's[`finish()`](https://developer.android.com/reference/android/app/Activity#finish())method.
| **Note:** Your sign-in activity must also provide an affordance that lets the user cancel the sign-in process and return to Android Automotive OS. Do this by calling the activity's`finish()`method.

#### Implement your sign-in activity

Google offers a variety of[identity tools](https://developers.google.com/identity/)that you can use to help users sign in to your app in their cars. Some tools, such as Firebase Authentication, provide full-stack toolkits that can help you build customized authentication experiences. Other tools leverage a user's existing credentials or other technologies to help you build seamless sign-in experiences for users.

The following tools can help you build an easier sign-in experience for users who have previously signed in on another device:

- **One Tap Sign-in and Sign-up:** if you already implemented[One Tap](https://developers.google.com/identity/one-tap/android)for other devices, such as your phone app, implement it for your Android Automotive OS app to support existing One Tap users.
- **Google Sign-in:** if you already implemented[Google Sign-in](https://developers.google.com/identity/)for other devices, such as your phone app, implement Google Sign-in for your Android Automotive OS app to support existing Google Sign-in users.
- **Autofill with Google:** if users have opted into Autofill with Google on their other Android devices, their credentials are saved to the[Google password manager](https://passwords.google.com/?pli=1). When those users sign in to your Android Automotive OS app, Autofill with Google suggests relevant saved credentials. Using Autofill with Google requires no application development effort. However, application developers can[optimize their apps for better quality results](https://developer.android.com/guide/topics/text/autofill-optimize). Autofill with Google is supported by all devices running Android 8.0 (API level 26) or higher, including Android Automotive OS.

#### Use AccountManager

Android Automotive OS apps that have authentication must use[AccountManager](https://developer.android.com/training/id-auth/custom_auth), for the following reasons:

- **Better UX and ease of account management:**users can easily manage all their accounts from the accounts menu in the system settings, including sign-in and sign-out.
- **"Guest" experiences:** cars are shared devices, which means OEMs can enable "guest" experiences in the vehicle, where accounts cannot be added. This restriction is achieved using[`DISALLOW_MODIFY_ACCOUNTS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_MODIFY_ACCOUNTS)for`AccountManager`.

#### Permissions

If you need to request permissions from the user, use the same flow as the authentication activity or the settings activity in the[activity workflows diagram](https://developer.android.com/training/cars/media/automotive-os#activity-workflows)shown in a previous section.

## Start the media host app

You can create intents to open the media host app to your app or content within your app. For example:

- Your app can post a notification with a pending intent that allows a user to open your app to listen to a new piece of content.
- Your app can handle[deep links](https://developer.android.com/training/cars/media/automotive-os#support-deep-links)and open the host app to the most appropriate view.

### Determine media host capabilities

Versions of the media host app support different capabilities. Hosts indicate support for different capabilities by including intent filters for the following intent actions:

- [`android.car.intent.action.MEDIA_TEMPLATE`](https://developer.android.com/reference/android/car/media/CarMediaIntents#ACTION_MEDIA_TEMPLATE)
- [`androidx.car.app.mediaextensions.action.MEDIA_TEMPLATE_V2`](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaIntentExtras#ACTION_MEDIA_TEMPLATE_V2())

All media host apps support`MEDIA_TEMPLATE`intents. To determine if the media host supports`MEDIA_TEMPLATE_V2`intents, you can use[`queryIntentActivities()`](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))as follows:  

    val isMediaTemplateV2Supported = packageManager.queryIntentActivities(
      Intent(MediaIntentExtras.ACTION_MEDIA_TEMPLATE_V2),
      // https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY since the host should be started with implicit intents
      // https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_SYSTEM_ONLY excludes any apps that aren't preinstalled
      PackageManager.MATCH_DEFAULT_ONLY or PackageManager.MATCH_SYSTEM_ONLY
    ).size > 0

| **Caution:** Don't use`MEDIA_TEMPLATE_V2`as the action for your intent if`queryIntentActivities()`returns an empty list, as that means there is no activity that can handle it.

### Build and use an intent

Depending on which intent actions are supported by the media host and what your specific use case is, you can provide the following extras when building the intent you use to start the media host app.

|          Extra key          |   Type    |                                                                                                                                                 Description                                                                                                                                                  |          Supported actions           |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `EXTRA_KEY_MEDIA_COMPONENT` | `String`  | The[flattened component name](https://developer.android.com/reference/android/content/ComponentName#flattenToString())of the`MediaBrowserService`the media host app should connect to -- generally the one for your app. If this extra is not specified, the media host defaults to the active media source. | `MEDIA_TEMPLATE`,`MEDIA_TEMPLATE_V2` |
| `EXTRA_KEY_SEARCH_QUERY`    | `String`  | The search query to be used when calling                                                                                                                                                                                                                                                                     | `MEDIA_TEMPLATE`,`MEDIA_TEMPLATE_V2` |
| `EXTRA_KEY_MEDIA_ID`        | `String`  | The media ID to open in the browse view.                                                                                                                                                                                                                                                                     | `MEDIA_TEMPLATE_V2`                  |
| `EXTRA_KEY_SEARCH_ACTION`   | `Integer` | The action to take after the search for the`EXTRA_KEY_SEARCH_QUERY`completes.                                                                                                                                                                                                                                | `MEDIA_TEMPLATE_V2`                  |

For example, with a host that supports`MEDIA_TEMPLATE_V2`actions, the following code will open the media host app, have it connect to`MyMediaBrowserService`, perform a search for "Jazz", and then play the first item from the search results. On all other hosts, it will only open the media host app and perform a search for "Jazz", leaving the user to select an item to play from the results.  

    val startMediaHostIntent = Intent(ACTION_MEDIA_TEMPLATE)
      .putExtra(MediaIntentExtras.EXTRA_KEY_MEDIA_COMPONENT, MyMediaBrowserService::class.java)
      .putExtra(MediaIntentExtras.EXTRA_KEY_SEARCH_QUERY, "Jazz")
      .putExtra(MediaIntentExtras.EXTRA_KEY_SEARCH_ACTION, MediaIntentExtras.EXTRA_VALUE_PLAY_FIRST_ITEM_FROM_SEARCH)

    context.startActivity(startMediaHostIntent)

## Support deep links

To improve your media app's experience on Android Automotive OS devices, you can add support for[deep links](https://developer.android.com/training/app-links)to your app. For example, this allows users to open your app directly from a browser or when receiving a URL shared from a phone using[Quick Share](https://support.google.com/android/answer/9286773).

### Add deep link intent filters

To inform the OS that your app is able to handle deep links, it needs to have activities with the appropriate intent filters. See[Add intent filters for incoming links](https://developer.android.com/training/app-links/deep-linking#adding-filters)for guidance on the format of the intent filters used for deep links.

For the best user experience, support all deep links that your mobile app supports, if they can be reasonably supported by your in-car app. If your app has[settings or sign-in activities](https://developer.android.com/training/cars/media/automotive-os#settings-sign-in), intent filters for handling settings and sign-in deep links should be declared within the respective`<activity>`manifest elements. For media playback and browsing deep links, you can use a trampoline activity as described later in this section.
| **Caution:** Be careful not to include any[launcher intent filters](https://developer.android.com/training/cars/media/automotive-os#intent-filters)in any activities declared in your manifest.

### Handle deep link intents

See[Read data from incoming intents](https://developer.android.com/training/app-links/deep-linking#handling-intents)for guidance on how to read and react to the intent that was used to start your app's activity.

#### Handle media playback and browsing deep links

Because the UI for browsing and playback is drawn by the host app, the activity used to handle deep links for playback and browsing actions shouldn't have any UI of its own.

Instead, it should primarily be used to build and use an intent to[start the media host app](https://developer.android.com/training/cars/media/automotive-os#start-host). If necessary, it can also handle any additional changes to your app's state, such as adding a media items to the queue. The following snippet shows an example trampoline activity implementation:  

    fun DeepLinkTrampolineActivity : ComponentActivity() {

      override fun onCreate() {
        handleIntent(intent)
      }

      override fun onNewIntent(intent: Intent) {
        handleIntent(intent)
      }

      private fun handleIntent(intent: Intent) {
        // Handle any side effects, such as adding a song to the queue
        ...
        // Build the intent used to start the media host app
        val startMediaHostIntent = ...
        startActivity(intent)
        // Finish the activity immediately so it isn't shown on screen
        finish()
      }
    }

| **Warning:** Don't mark such an activity as[distraction optimized](https://developer.android.com/training/cars/platforms/automotive-os#distraction-optimization), or your app will be rejected upon submission to the Google Play store.

## Read media host hints

Depending on the system application (including its version) that connects to your media browser service, your application may receive the following extras:

- In[`MediaBrowserServiceCompat#onGetRoot`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onGetRoot(java.lang.String,int,android.os.Bundle)):

  - [KEY_ROOT_HINT_MEDIA_HOST_VERSION](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_ROOT_HINT_MEDIA_HOST_VERSION())
  - [KEY_ROOT_HINT_MEDIA_SESSION_API](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_ROOT_HINT_MEDIA_SESSION_API())
  - [BROWSER_ROOT_HINTS_KEY_MEDIA_ART_SIZE_PIXELS](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_MEDIA_ART_SIZE_PIXELS())
  - [BROWSER_ROOT_HINTS_KEY_CUSTOM_BROWSER_ACTION_LIMIT](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_CUSTOM_BROWSER_ACTION_LIMIT())
  - [BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_LIMIT](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_LIMIT())
  - [KEY_ROOT_HINT_MAX_QUEUE_ITEMS_WHILE_RESTRICTED](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_ROOT_HINT_MAX_QUEUE_ITEMS_WHILE_RESTRICTED())
- In[`MediaBrowserServiceCompat#onLoadChildren`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E,android.os.Bundle))and in[`MediaBrowserServiceCompat#onSearch`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onSearch(java.lang.String,android.os.Bundle,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E)):

  - [KEY_HINT_VIEW_MAX_ITEMS_WHILE_RESTRICTED](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_ROOT_HINT_MEDIA_SESSION_API())
  - [KEY_HINT_VIEW_MAX_LIST_ITEMS_COUNT_PER_ROW](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_HINT_VIEW_MAX_LIST_ITEMS_COUNT_PER_ROW())
  - [KEY_HINT_VIEW_MAX_CATEGORY_LIST_ITEMS_COUNT_PER_ROW](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_HINT_VIEW_MAX_CATEGORY_LIST_ITEMS_COUNT_PER_ROW())
  - [KEY_HINT_VIEW_MAX_GRID_ITEMS_COUNT_PER_ROW](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_HINT_VIEW_MAX_GRID_ITEMS_COUNT_PER_ROW())
  - [KEY_HINT_VIEW_MAX_CATEGORY_GRID_ITEMS_COUNT_PER_ROW](https://developer.android.com/reference/kotlin/androidx/car/app/mediaextensions/MediaBrowserExtras#KEY_HINT_VIEW_MAX_CATEGORY_GRID_ITEMS_COUNT_PER_ROW())

## Error Handling

Errors in media apps on Android Automotive OS are communicated via the media session's`PlaybackStateCompat`. For all errors, set an appropriate error code and error message in the`PlaybackStateCompat`. This causes a`Toast`to appear in the UI.

When an error occurs but playback can continue, issue a[non-fatal error](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session#errors). For example, a user might be able to play music in an app before signing in, but they must sign in before they can skip a song. When you use a non-fatal error, the system can suggest that the user log in without interrupting playback for the current media item.

When you issue a non-fatal error, preserve the rest of the`PlaybackStateCompat`as-is, aside from the error code and error message. Using this approach lets playback for the current media item to continue while the user decides whether to sign in.

When playback is not possible, such as when there is no internet connection and no offline content, set the`PlaybackStateCompat`state to`STATE_ERROR`.

On subsequent updates to your`PlaybackStateCompat`, clear any error codes and error messages to avoid displaying multiple warnings for the same error.

If at any point you are unable to load a browse tree---for example, if you require authentication and the user is not signed in---send an empty browse tree. To signify this, return a null result from`onLoadChildren()`for the root media node. When this happens, the system displays a full-screen error with the error message set in the`PlaybackStateCompat`.

### Actionable errors

If an error is actionable, additionally set the following two extras in the`PlaybackStateCompat`:

- [`PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_LABEL()): a label for the button to click to resolve the error. Because this string is user-facing, localize it for the user's current locale.
- [`PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_ERROR_RESOLUTION_ACTION_INTENT()): the`PendingIntent`that the button runs to resolve the error, such as by launching your sign-in activity.

Actionable errors appear as a`Dialog`and can resolved by users only when the car is stopped.

### Testing error cases

Verify that your app gracefully handles errors in all scenarios, including:

- **Different tiers of your product:**for example, free versus premium or signed in versus signed out
- **Different drive states:**for example, parked versus driving
- **Different connectivity states:**for example, online versus offline

## Other considerations

Keep these other considerations in mind when developing your Android Automotive OS app:

### Offline content

If applicable, implement offline playback support. Cars with Android Automotive OS are expected to have their own data connectivity, meaning a data plan is included in the cost of the vehicle or paid for by the user. However, cars are also expected to have more variable connectivity than mobile devices.

Here are a few things to keep in mind as you consider your offline support strategy:

- The best time to download content is while your app is in use.
- Do not assume that WiFi is available. A car might never come into WiFi range, or the OEM might have disabled WiFi in favor of a cellular network.
- While it is okay to smartly cache the content expect users to use, we recommend that you let the user change this behavior through your settings activity.
- The disk space on cars varies, so give users a way to delete offline content, such as through an option in your settings activity.

### WebView support

WebViews are supported in Android Automotive OS but are only allowed for your settings and sign-in activities. Activities that use a WebView must have a "close" or "back" affordance outside of the WebView.

Here are some examples of acceptable use-cases for WebViews:

- Displaying your privacy policy, terms of service, or other legal-related links in your settings activity.
- A web-based flow in your sign-in activity.

When using a WebView, you can[enable Javascript](https://developer.android.com/guide/webapps/webview#EnablingJavaScript).
| **Important:** Videos are not allowed.

#### Secure your WebView

Take all precautions possible to help ensure that your WebView is not an entry point into the greater internet. See the following code snippet for an example on how to lock the WebView to the URL used in the[`loadUrl()`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String))call and prevent redirects. We highly recommend that you implement safeguards like this when feasible, such as when displaying legal-related links.  

### Kotlin

```kotlin
override fun shouldOverrideUrlLoading(webView: WebView,
                             webResourceRequest: WebResourceRequest): Boolean {
  val originalUri: Uri = Uri.parse(webView.originalUrl)
  // Check for allowed URLs
  if (originalUri.equals(Uri.parse(BLANK_URL))
      || originalUri.equals(webResourceRequest.url)) {
    return false
  }
  if (webResourceRequest.isRedirect) {
    logger.w("Redirect detected, not following")
    return true
  }
  setupWizardWebViewClientListener.onUriBlocked(webResourceRequest.url)
  logger.w(
    String.format(
      "Navigation prevented to %s original is %s", webResourceRequest.url, originalUri))
  return true
}
```

### Java

```java
@Override
public boolean shouldOverrideUrlLoading(WebView webView, WebResourceRequest webResourceRequest) {
  Uri originalUri = Uri.parse(webView.getOriginalUrl());
  // Check for allowed URLs
  if (originalUri.equals(Uri.parse(BLANK_URL))
      || originalUri.equals(webResourceRequest.getUrl())) {
    return false;
  }
  if (webResourceRequest.isRedirect()) {
    logger.w("Redirect detected, not following");
    return true;
  }
  setupWizardWebViewClientListener.onUriBlocked(webResourceRequest.getUrl());
  logger.w(
      String.format(
          "Navigation prevented to %s original is %s", webResourceRequest.getUrl(), originalUri));
  return true;
}
```

### Package names

Because you distribute a separate Android Package Kit (APK) for Android Automotive OS, you can reuse the package name from your mobile app or create a new package name. If you use a different package name, your app has two separate Play Store listings. If you reuse your current package name, your app has a single listing across both platforms.

This is predominantly a business decision. For example, if you have one team working on the mobile app, and a separate team working on your Android Automotive OS app, then it might make sense to have separate package names and let each team manage its own Play Store listing. There is not a large difference in the technical effort required to use either approach.

The following table summarizes some other key differences between keeping your current package name and using a new package name:

|                                         Feature                                          |                                            Same package name                                            |                                      New package name                                       |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Store listing                                                                            | Single                                                                                                  | Multiple                                                                                    |
| Mirrored install                                                                         | Yes: "fast app reinstall" during the setup wizard                                                       | No                                                                                          |
| Play Store Review process                                                                | Blocking reviews: if the review fails for one APK, other APKs submitted in the same release are blocked | Individual reviews                                                                          |
| Statistics, metrics, and[vitals](https://developer.android.com/topic/performance/vitals) | Combined: you can filter for automotive-specific data.                                                  | Separate                                                                                    |
| Indexing and search ranking                                                              | Build off current standing                                                                              | No carryover                                                                                |
| Integrating with other apps                                                              | Most likely no changes needed, assuming media code is shared between both APKs                          | Might have to update the corresponding app, such as for URI playback with Google Assistant. |

## Frequently asked questions

See the following sections for answers to some frequently asked questions about Android Automotive OS.

### Hardware

#### Can my app get access to the microphone

For apps targeting Android 10 (API level 29) or higher, refer to the[sharing audio input](https://developer.android.com/guide/topics/media/sharing-audio-input)documentation. This is not feasible prior to API level 29.

#### Which car APIs can we get access to and how?

You are limited to the APIs that are exposed by the OEM. Processes are being developed to standardize how you access these APIs.

Apps can access car APIs using[`SetProperty()`](https://android.googlesource.com/platform/packages/services/Car/+/master/car-lib/src/android/car/hardware/property/CarPropertyManager.java#483)and[`GetProperty()`](https://android.googlesource.com/platform/packages/services/Car/+/master/car-lib/src/android/car/hardware/property/CarPropertyManager.java#436)in[`CarPropertyManager`](https://android.googlesource.com/platform/packages/services/Car/+/master/car-lib/src/android/car/hardware/property/CarPropertyManager.java). Refer to the[source code](https://android.googlesource.com/platform/packages/services/Car/+/master/car-lib/src/android/car/VehiclePropertyIds.java)or[reference documentation](https://developer.android.com/reference/android/car/VehiclePropertyIds)to see a list of all available properties. If the property is[annotated](https://android.googlesource.com/platform/packages/services/Car/+/master/car-lib/src/android/car/Car.java)with`@SystemApi`, it is limited to preloaded system apps.

#### What types of audio codecs are supported?

Refer to the[audio codec details](https://source.android.com/compatibility/10/android-10-cdd#5_1_3_audio_codecs_details)in the Android CDD.

#### Is Widevine DRM supported?

Yes.[Widevine DRM](https://www.widevine.com/solutions/widevine-drm)is supported.

### Development and testing

#### Are there any restrictions or recommendations for using third-party SDKs and libraries?

We don't have any specific guidelines on using third-party SDKs and libraries. If you choose to use third-party SDKs and libraries, you are still responsible for complying with all the car app quality requirements.

#### Can I use a foreground service?

The only allowed use-case for a foreground service is downloading content for offline use. If you have another use-case for a foreground service that you want to see support for, get in touch with us using the[Android Automotive OS discussion group](https://g.co/automotive-developers).

### Publishing Android Automotive OS apps

#### How do I publish my Android Automotive OS app using the Google Play Console?

For details on how to publish your Android Automotive OS app using the Google Play Console, see[Distribute to cars](https://developer.android.com/training/cars/distribute).
| **Warning:** Because a media app artifact cannot support both mobile and Android Automotive OS experiences, you[must use the dedicated Android Automotive OS track](https://developer.android.com/training/cars/distribute#choose-track-aaos)to distribute your media app to Android Automotive OS devices.

## Additional resources

To learn more about Android Automotive OS, see the following additional resources.

### Samples

- [Universal Android Music Player](https://github.com/android/uamp)

### Guides

- [Design for Driving](http://g.co/automotive-design)
- [Using the media controller test app](https://developer.android.com/guide/topics/media-apps/audio-app/media-controller-test)
- [Notifications on Android Automotive OS](https://developer.android.com/training/cars/platforms/automotive-os/notifications)
- [Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality)

### Blogs

- [Android Automotive OS updates for developers](https://android-developers.googleblog.com/2019/10/android-automotive-os-updates-for.html)
- [Developing Apps for Android Automotive OS](https://android-developers.googleblog.com/2019/05/developing-apps-for-android-automotive.html)

### Videos

- [How to Build Media Apps for Cars (Android Dev Summit '19)](https://www.youtube.com/watch?v=Ujwy_AoJnZs)
- [How to Build Android Apps for Cars (Google I/O'19)](https://www.youtube.com/watch?v=AHHERLwjUGo)

## Report an Android Automotive OS Media issue

If you run into an issue while developing your media app for Android Automotive OS, you can report it using the[Google Issue Tracker](https://issuetracker.google.com/issues?q=status:open+componentid:591842). Be sure to fill out all the requested information in the issue template.

[Create a new issue](https://issuetracker.google.com/issues/new?component=591842)

Before filing a new issue, check whether it is already reported in the issues list. You can subscribe and vote for issues by clicking the star for an issue in the tracker. For more information, see[Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).