---
title: https://developer.android.com/studio/write/app-link-indexing
url: https://developer.android.com/studio/write/app-link-indexing
source: md.txt
---

# Add Android App Links

| **Note:** Apps Links Assistant Web Checks is only available in the latest stable channel version of Android Studio and major versions (including their patches) released in the previous 10 months. If you are using an older version of Android Studio, you will need to update to access Cloud services. For more information, see[Android Studio and Cloud services compatibility](https://developer.android.com/studio/releases#service-compat).

Android App Links are HTTP URLs that bring users directly to specific content in your Android app. Android App Links can drive more traffic to your app, help you discover which app content is used most, and make it easier for users to find and share content in an installed app.  
To add support for Android App Links:

1. Create intent filters in your manifest.
2. Add code to your app's activities to handle incoming links.
3. Associate your app and your website with Digital Asset Links.

The App Links Assistant in Android Studio simplifies the process with a step-by-step wizard, as described below.

For more information about how app links work and the benefits they offer, read[Handling Android App Links](https://developer.android.com/training/app-links).  

## Add intent filters

The App Links Assistant in Android Studio can help you create[intent filters](https://developer.android.com/training/app-links/deep-linking#adding-filters)in your manifest and map existing URLs from your website to activities in your app. The App Links Assistant also adds template code in each corresponding activity to handle the intent.

To add intent filters and URL handling, follow these steps:

1. Select**Tools \> App Links Assistant**.
2. Click**Open URL Mapping Editor** and then click**Add** ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png)at the bottom of the**URL Mapping**list to add a new URL mapping.
3. Add details for the new URL mapping:

   ![The App Links Assistant walks you through basic URL mapping](https://developer.android.com/static/studio/images/write/app-links-assistant-URL-mapping_2x.png)

   **Figure 1.**Add basic details about your site's link structure to map URLs to activities in your app.
   1. Enter your website's URL in the**Host**field.
   2. Add a[`path`,`pathPrefix`, or`pathPattern`](https://developer.android.com/guide/topics/manifest/data-element#path)for the URLs you want to map.

      For example, if you have a recipe-sharing app with all the recipes available in the same activity, and your corresponding website's recipes are all in the same*/recipe* directory, use**pathPrefix** and enter*/recipe.* This way, the URL*http://www.recipe-app.com/recipe/grilled-potato-salad*maps to the activity you select in the following step.
   3. Select the**Activity**the URLs should take users to.
   4. Click**OK.**

   The URL Mapping Editor window appears. The App Links Assistant adds intent filters based on your URL mapping to the`AndroidManifest.xml`file and highlights the changes in the**Preview** field. If you'd like to make any changes, click**Open AndroidManifest.xml** to edit the intent filter. To learn more, see[intent filters for incoming links](https://developer.android.com/training/app-links/deep-linking#adding-filters).

   The main App Links Assistant tool window also displays all existing deep links in the`AndroidManifest.xml`file and lets you quickly fix any misconfigurations by clicking**Fix All Manifest Issues**.
   ![The App Links Assistant lets you fix manifest misconfigurations.](https://developer.android.com/static/studio/images/app-links-assistant.png)

   **Note:**To support future links without updating your app, define a URL mapping that supports URLs that you plan to add. Also, include a URL for your app home screen so it's included in search results.
4. To verify that your URL mapping works properly, enter a URL in the**Check URL Mapping**field.

   If it's working correctly, the success message shows that the URL you entered maps to the activity you selected.

## Handle incoming links

Once you've verified that your URL mapping is working correctly, add logic to handle the intent you created:

1. Click**Select Activity**from the App Links Assistant.
2. Select an activity from the list and click**Insert Code**.

The App Links Assistant adds code to your activity, similar to the following:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    // ATTENTION: This was auto-generated to handle app links.
    val appLinkIntent: Intent = intent
    val appLinkAction: String? = appLinkIntent.action
    val appLinkData: Uri? = appLinkIntent.data
    ...
}
```

### Java

```java
@Override
void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    ...
    // ATTENTION: This was auto-generated to handle app links.
    Intent appLinkIntent = getIntent();
    String appLinkAction = appLinkIntent.getAction();
    Uri appLinkData = appLinkIntent.getData();
    ...
}
```

This code isn't complete on its own. You must now take an action based on the URI in`appLinkData`, such as displaying the corresponding content. For example, for the recipe-sharing app, your code might look like the following sample:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    ...
    handleIntent(intent)
}

override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    handleIntent(intent)
}

private fun handleIntent(intent: Intent) {
    val appLinkAction = intent.action
    val appLinkData: Uri? = intent.data
    if (Intent.ACTION_VIEW == appLinkAction) {
        appLinkData?.lastPathSegment?.also { recipeId ->
            Uri.parse("content://com.recipe_app/recipe/")
                    .buildUpon()
                    .appendPath(recipeId)
                    .build().also { appData ->
                        showRecipe(appData)
                    }
        }
    }
}
```

### Java

```java
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  ...
  handleIntent(getIntent());
}

protected void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  handleIntent(intent);
}

private void handleIntent(Intent intent) {
    String appLinkAction = intent.getAction();
    Uri appLinkData = intent.getData();
    if (Intent.ACTION_VIEW.equals(appLinkAction) && appLinkData != null){
        String recipeId = appLinkData.getLastPathSegment();
        Uri appData = Uri.parse("content://com.recipe_app/recipe/").buildUpon()
            .appendPath(recipeId).build();
        showRecipe(appData);
    }
}
```

## Associate your app with your website

After setting up URL support for your app, the App Links Assistant generates a Digital Assets Links file you can use to[associate your website with your app](https://developer.android.com/training/app-links/verify-android-applinks#web-assoc).

As an alternative to using the Digital Asset Links file, you can[associate your site and app in Search Console](https://support.google.com/webmasters/answer/6212023).

If you're using[Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756)for your app, then the certificate fingerprint produced by the App Links Assistant usually doesn't match the one on users' devices. In this case, you can find the correct Digital Asset Links JSON snippet for your app in your[Play Console](https://play.google.com/console/)developer account under**Release \> Setup \> App signing**.

To associate your app and your website using the App Links Assistant, click**Open Digital Asset Links File Generator**from the App Links Assistant and follow these steps:
![The App Links Assistant walks you through basic URL mapping](https://developer.android.com/static/studio/images/write/app-links-assistant-dal-file-generator_2x.png)

**Figure 2.**Enter details about your site and app to generate a Digital Asset Links file.

1. Enter your**Site domain** and your[**Application ID**](https://developer.android.com/studio/build/configure-app-module#set-application-id).
2. To include support in your Digital Asset Links file for[One Tap sign-in](https://developers.google.com/identity/one-tap/android/overview), select**Support sharing credentials between the app and the website** and enter your site's sign-in URL.This adds the following string to your Digital Asset Links file declaring that your app and website share sign-in credentials:`delegate_permission/common.get_login_creds`.

3. Specify the[signing config](https://developer.android.com/studio/publish/app-signing#sign-auto)or select a[keystore file](https://developer.android.com/studio/publish/app-signing#certificates-keystores).

   Make sure you select the right release config or keystore file for the release build or the debug config or keystore file for the debug build of your app. If you want to set up your production build, use the release config. If you want to test your build, use the debug config.
4. Click**Generate Digital Asset Links file**.
5. Once Android Studio generates the file, click**Save file**to download it.
6. Upload the`assetlinks.json`file to your site, with read access for everyone, at`https://`<var translate="no">yoursite</var>`/.well-known/assetlinks.json`.

   **Important:** The system verifies the Digital Asset Links file via the encrypted HTTPS protocol. Make sure that the`assetlinks.json`file is accessible over an HTTPS connection, regardless of whether your app's intent filter includes`https`.
7. Click**Link and Verify**to confirm that you've uploaded the correct Digital Asset Links file to the correct location.

The App Link Assistant can validate the Digital Assets Links file that should be published on your website. For each domain that's declared in the manifest file, the Assistant parses the file on your website, performs validation checks, and provides a detailed explanation on how to fix any errors.

Learn more about associating your website with your app through the Digital Asset Links file in[Declare website associations](https://developer.android.com/training/app-links/verify-android-applinks#web-assoc).

## Test your Android App Links

To verify that your links open the correct activity, follow these steps:

1. In the App Links Assistant, click**Test App Links**.
2. Enter the URL that you want to test in the**URL** field; for example,*http://recipe-app.com/recipe/grilled-potato-salad*.  
![](https://developer.android.com/static/studio/images/write/app-links-assistant-link-testing_2x.png)

**Figure 3.** **Test App Links**dialog showing a URL being tested and a success message.
3. Click**Run Test**.

If the URL mapping isn't set up properly or doesn't exist, an error message appears under the URL in the**Test App Links** dialog. Otherwise, Android Studio launches your app in the device or emulator at the specified activity without showing the disambiguation dialog ("app chooser") and shows a success message in the**App Link Testing**dialog, as shown in figure 3.

If Android Studio can't launch the app, an error message appears in Android Studio's**Run**window.

To test Android App Links through the App Links Assistant, you must have a device connected or a virtual device available running Android 6.0 (API level 23) or higher. For more information, read about how to[connect a device](https://developer.android.com/studio/run/device)or[create an AVD](https://developer.android.com/studio/run/managing-avds#createavd).