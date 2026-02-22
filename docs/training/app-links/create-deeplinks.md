---
title: https://developer.android.com/training/app-links/create-deeplinks
url: https://developer.android.com/training/app-links/create-deeplinks
source: md.txt
---

Deep linking lets you bring users directly into your app from web browsers,
notifications, social media, ads, and other sources. Deep links provide direct
app-to-app and web-to-app transitions that can help you increase engagement
through contextual, targeted content.

This guide explains how deep linking works and how to create and test deep links
to your content.

For deep links that reference your own website or domains, we recommend using
App Links, which provides a seamless, trusted experience for your users.

## How deep linking works

Deep linking is a general system capability of Android, supported on all
versions, on all devices. It takes advantage of Android's Intents system to
route deep links to interested apps. Apps that want to handle a specific deep
link URI declare a matching Intent filter in their app manifest files.

At runtime, when the user taps a link, Android triggers an intent and attempts
to route it to an app. Because multiple apps can declare intent filters that
match a given URI, Android takes these actions, in this order, to route the
intent:

1. Open the user's default app that can handle the URI, if one was designated.
2. Open the only available app that can handle the URI.
3. Allow the user to select an app from a *disambiguation dialog*.

This means that, even though your intent filters match a given URI, there is no
guarantee that the system will route the deep link intent to your app. The user
has a key role in managing which app handles the intent, which gives them
control and offers choice. For more control over deep links to your own website
and domains, try using App Links.

Android's disambiguation dialog lets the user see all of the installed apps that
have registered to handle a deep link intent. The user can also select an app as
the default for this type of link. Once the user sets a default, the system no
longer shows the dialog for that specific intent, and the chosen app will open
automatically.

![](https://developer.android.com/static/training/app-links/images/app-disambiguation_2x.png)

**Figure 1.** The disambiguation dialog

The behavior of the disambiguation dialog has evolved across Android versions.
For example, on Android 12 and higher, web links that are not verified App
Links will generally open in a web browser by default, whereas on previous
versions, a disambiguation dialog might have appeared if an app could handle the
web link.

**Note**: Starting in Android 12 (API level 31), a generic web intent resolves
to an activity in your app only if your app is approved for the specific domain
contained in that web intent. If your app isn't approved for the domain, the web
intent resolves to the user's default browser app instead.

## Types of deep links

There are three types of deep links you can support on Android:

- **Custom deep links** : These are deep links that use a custom URI scheme (such as `example://products/123`) to take a user directly to a specific piece of content within an app. They are powerful for internal navigation or links from sources you control, but they are not standard web links and can still trigger the disambiguation dialog if another app registers the same custom scheme.
- **Web links** : These are deep links that use the standard `http` and `https` schemes. They are more versatile because they are standard URLs, but on Android 12 and higher they will almost always trigger the disambiguation dialog, meaning that they are likely to be handled by the user's web browser by default, rather than being routed to your app.
- **App Links** : Available since Android 6.0 (API level 23), these are *verified* web links. Through a process of website association, you can prove to the Android system that you own the domain. Once verified, the system automatically routes links for that domain directly to your app, skipping the disambiguation dialog entirely. This creates a trusted and seamless experience for your users.

## Add intent filters for incoming links

To create a link to your app content, add an intent filter that contains these
elements and attribute values in your manifest:

[`<action>`](https://developer.android.com/guide/topics/manifest/action-element)

Specify the [`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW) intent action so that the intent filter can be
reached from Google Search.

[`<data>`](https://developer.android.com/guide/topics/manifest/data-element)

Add one or more [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) tags, each of which represents a URI format that
resolves to the activity. At minimum, the [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) tag must include the
[`android:scheme`](https://developer.android.com/guide/topics/manifest/data-element#scheme) attribute.

You can add more attributes to further refine the type of URI that the activity
accepts. For example, you might have multiple activities that accept similar
URIs, but which differ simply based on the path name. In this case, use the
[`android:path`](https://developer.android.com/guide/topics/manifest/data-element#path) attribute or its `pathPattern` or `pathPrefix` variants to
differentiate which activity the system should open for different URI paths.

[`<category>`](https://developer.android.com/guide/topics/manifest/category-element)

Include the [`BROWSABLE`](https://developer.android.com/reference/android/content/Intent#CATEGORY_BROWSABLE) category. It is required in order for the intent
filter to be accessible from a web browser. Without it, clicking a link in a
browser cannot resolve to your app.

Also include the [`DEFAULT`](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category. This allows your app to respond to
implicit intents. Without this, the activity can be started only if the intent
specifies your app component name.

The following XML snippet shows how you might specify an intent filter in your
manifest for deep linking. The URIs `"example://gizmos"` and
`"http://www.example.com/gizmos"` both resolve to this activity.  

    <activity
        android:name="com.example.android.GizmosActivity"
        android:label="@string/title_gizmos" >
        <intent-filter android:label="@string/filter_view_http_gizmos">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />
            <!-- Accepts URIs that begin with "http://www.example.com/gizmos" -->
            <data android:scheme="http"
                  android:host="www.example.com"
                  android:pathPrefix="/gizmos" />
            <!-- note that the leading "/" is required for pathPrefix-->
        </intent-filter>
        <intent-filter android:label="@string/filter_view_example_gizmos">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />
            <!-- Accepts URIs that begin with "example://gizmos" -->
            <data android:scheme="example"
                  android:host="gizmos" />
        </intent-filter>
    </activity>

Notice that the two intent filters only differ by the `<data>` element. Although
it's possible to include multiple `<data>` elements in the same filter, it's
important that you create separate filters when your intention is to declare
unique URLs (such as a specific combination of `scheme` and `host`), because
multiple `<data>` elements in the same intent filter are actually merged
together to account for all variations of their combined attributes. For
example, consider the following:  

    <intent-filter>
      ...
      <data android:scheme="https" android:host="www.example.com" />
      <data android:scheme="app" android:host="open.my.app" />
    </intent-filter>

It might seem as though this supports only `https://www.example.com` and
`app://open.my.app`. However, it actually supports those two, plus these:
`app://www.example.com` and `https://open.my.app`.

**Caution**: If multiple activities contain intent filters that resolve to the
same verified Android App Link, then there's no guarantee as to which activity
handles the link.

Once you've added intent filters with URIs for activity content to your app
manifest, Android is able to route any [`Intent`](https://developer.android.com/reference/android/content/Intent) that has matching URIs to
your app at runtime.

To learn more about defining intent filters, see [Allow Other Apps to Start Your
Activity](https://developer.android.com/training/basics/intents/filters).

## Read data from incoming intents

Once the system starts your activity through an intent filter, you can use data
provided by the [`Intent`](https://developer.android.com/reference/android/content/Intent) to determine what you need to render. Call the
[`getData()`](https://developer.android.com/reference/android/content/Intent#getData()) and [`getAction()`](https://developer.android.com/reference/android/content/Intent#getAction()) methods to retrieve the data and
action associated with the incoming [`Intent`](https://developer.android.com/reference/android/content/Intent). You can call these methods
at any time during the lifecycle of the activity, but you should generally do so
during early callbacks such as [`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) or [`onStart`](https://developer.android.com/reference/android/app/Activity#onStart())().

Here's a snippet that shows how to retrieve data from an [`Intent`](https://developer.android.com/reference/android/content/Intent):  

### Kotlin

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)

        val action: String? = intent?.action
        val data: Uri? = intent?.data
    }

### Java

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        Intent intent = getIntent();
        String action = intent.getAction();
        Uri data = intent.getData();
    }

Follow these best practices to improve the user's experience:

- The deep link should take users directly to the content, without any prompts, interstitial pages, or logins. Make sure that users can see the app content even if they never previously opened the application. It is okay to prompt users on subsequent interactions or when they open the app from the Launcher.
- Follow the design guidance described in [Navigation with Back and Up](https://developer.android.com/guide/navigation/navigation-principles) so that your app matches users' expectations for backward navigation after they enter your app through a deep link.

## Test your deep links

You can use the [Android Debug Bridge](https://developer.android.com/tools/help/adb) with the activity manager (am) tool
to test that the intent filter URIs you specified for deep linking resolve to
the correct app activity. You can run the adb command against a device or an
emulator.

The general syntax for testing an intent filter URI with adb is:  

    $ adb shell am start
            -W -a android.intent.action.VIEW
            -d <URI> <PACKAGE>

For example, the following command tries to view a target app activity that is
associated with the specified URI.  

    $ adb shell am start
            -W -a android.intent.action.VIEW
            -d "example://gizmos" com.example.android

**Note** : When defining a collection of primitive types in a route, such as
`**@Serializable data class Product(val colors: List)**`, the automatically
generated deep link URL format is `**basePath?colors={value**}`. If you attempt
to specify a URI with multiple query params (for example,
`**basepath?colors=red&colors=blue**`), you must escape the ampersand
(for example, `**basepath?colors=red\&colors=blue**`).

The manifest declaration and intent handler you set define the connection
between your app and a website and what to do with incoming links. However, in
order to have the system treat your app as the default handler for a set of
URIs, you must also request that the system verify this connection.
[Verify App Links](https://developer.android.com/training/app-links/verify-applinks) explains how to implement this verification.

To learn more about intents and app links, see the following resources:

- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)
- [Allow Other Apps to Start Your Activity](https://developer.android.com/training/basics/intents/filters)
- [Add Android App Links with Android Studio](https://developer.android.com/studio/write/app-link-indexing)