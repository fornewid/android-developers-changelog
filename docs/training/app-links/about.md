---
title: https://developer.android.com/training/app-links/about
url: https://developer.android.com/training/app-links/about
source: md.txt
---

Android App Links is a special deep linking capability in Android 6 and later
that allows your verified website URLs to immediately open corresponding content
in your Android app, without requiring the user to select your app from a
disambiguation dialog. To make this possible, Android uses [Digital Asset
Links](https://developers.google.com/digital-asset-links) statements hosted on your website to establish a secure
and verified association between your website and your app. After verifying the
association, Android can automatically route your deep links to your website
directly to your app for handling.

Starting with Android 15, App Links are even more powerful with the introduction
of [Dynamic App Links](https://developer.android.com/training/app-links/about#dynamic-app-links). With the new dynamic capabilities,
you can refine your app's deep link behaviors on the fly, with more control, and
without needing to release a new version of your app.

## Why you should use App Links:

- Seamless user experience -- Directly take users to specific content in your app from search results, websites, messaging, and other apps. Since App Links use a single URL for the same content on your website and in your app, users who don't have the app installed go to your website instead --- no 404s, no errors.
- Enhanced security -- App Links require verification of domain ownership, preventing other apps from intercepting your links.
- Dynamic configuration (Android 15+) -- Update your app's deep linking behavior on the fly, allowing for more flexibility and faster updates for things like vanity URLs, seasonal campaigns, or user-specific links.
- Engagement -- You can engage users through links in search results, ads, web pages, messaging, and more.

## How to support App Links

1. **Create deep links to specific content in your app**: In your app manifest, create intent filters for your website URIs and configure your app to use data from the intents to send users to the right content in your app.
2. **Add verification for your deep links**: Configure your app to request verification of app links. Then, publish a Digital Asset Links JSON file on your websites to verify ownership.

Alternatively, you can use the [Android App Links Assistant](https://developer.android.com/studio/write/app-link-indexing) in Android
Studio to guide you through each of the steps required to create and verify
Android App Links. For more information, see [App Links developer tools](https://developer.android.com/training/app-links/tools).

## App Links availability

- Dynamic App Links -- Android 15 (API level 35) or later, on devices with Google services installed.
- App Links -- Android 6 (API level 23) and later, on devices with Google services installed.
- Normal (user-managed) deep linking -- All Android versions, on all devices.

## How App Links works

App Links is a special way of deep linking that gives you full control over the
handling of links to your own website. It builds on the same intent-based system
used by other deep link types, but it adds a verification step for your links
using a Digital Asset Links file on your website.

App Links creates a secure, trusted association between your app and your
website using app data and a special `assetlinks.json` file that you host on
your website or domain. The `assetlinks.json` file declares Digital Asset Link
statements to verify the app association.

Here's the conceptual flow:

1. **Your app's manifest** declares URLs in an intent filter with `android:autoVerify="true`" and points to your website host.
2. **When the app is installed** , the Android system fetches the `assetlinks.json` file from a known location on your web server.
3. **The system verifies** that the `assetlinks.json` file is valid and the `sha256_cert_fingerprints` matches your app's signing certificate.
4. **When the user clicks a matching link**, the system routes them to your app directly, without showing a disambiguation dialog.

Because App Links use HTTP URLs and association with a website, users who
don't have your app installed go directly to content on your site. In this way,
App Links offers a trusted and seamless experience for your users who tap deep
links to your web properties.

## Dynamic App Links

Starting with Android 15, App Links are even more powerful with the introduction
of Dynamic App Links. With Dynamic App Links, you have the option to update your
deep linking rules on the server side, in your `assetlinks.json` file, without
needing to publish a new version of your app. Dynamic App Links supports Digital
Asset Links fields to refine your deep linking rules. Android devices with
Google services installed will refresh your file periodically and apply your new
deep linking rules dynamically. No app update is needed.

Previously, this file was primarily used for basic verification. Now, it's a
powerful configuration tool that lets you specify paths, query parameters,
fragments, and exclusions, providing a dynamic and robust deep linking solution:

- **Exclusions support**: You can specify certain paths or sections of a URL that shouldn't open your app, even if they would otherwise match your App Link configuration.
- **Query parameters support**: With the new Query parameters functionality you can define specific parameters that, if present in a URL, will prevent your app from opening. This opens up exciting possibilities for dynamic exclusions, A/B Testing and gradually enabling app linking for certain user segments.
- **Dynamic updates** : Make updates to your App Links configuration without needing to update your app by specifying the URL paths that your app handles directly within the `assetlinks.json` file hosted on your server.

Dynamic App Links also gives you fine-grained control over the URLs that you
want to open your app, including matching for URL paths, fragments, and query
parameters. You can also exclude any of the matches so that they are not allowed
to open your app. For more information, see [Configure dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks#configure-dynamic).

Here's the conceptual flow for Dynamic App Links:

1. **Your app's manifest** declares URLs in an intent filter with `android:autoVerify="true`" and points to your website host.
2. **When the app is installed** , the Android system fetches the `assetlinks.json` file from a known location on your web server.
3. **The system verifies** that the file is valid and the `sha256_cert_fingerprints` matches your app's signing certificate.
4. **The system parses** any deep linking rules you've defined within the `dynamic_app_deep_link_components` field in the Digital Asset Links statement, and merges them with the manifest-declared rules.
   1. **When the user clicks a matching link**, the system directs them to your app directly, without showing a disambiguation dialog.
5. **The system periodically re-fetches** the `assetlinks.json` file to get the latest rules, allowing you to update your links without an app update. Periodic re-fetching is supported on devices running Android 15 (API level 35) or later that have Google services installed.

### Example use-cases

- Seasonal marketing campaigns: A retail app could add a rule for "/promo/summer-sale" to the `assetlinks.json` file to direct users to a specific sale screen. Once the sale is over, the rule can be removed without requiring users to update the app.
- Vanity URLs for partners: If you have a partnership with an influencer, you could create a custom URL like "/partner/influencer-name" and add a rule for it. You can then track, update or remove this URL dynamically as partnerships change.
- A/B testing URL Paths: A developer could publish a new feature under a specific URL path and add a rule for it in the `assetlinks.json` file. This allows them to test the feature with a subset of users and then modify the routing without a full app deployment.
- Short-lived events: A ticketing or event app could add URL rules for specific events. Once the event has passed, you can delete these rules from the server.

### Compatibility with App Links implementations

The Dynamic App Links extensions in Android 15 are designed for full
compatibility with existing implementations of App Links on devices running
earlier versions of Android. Lower app versions aren't able to use the dynamic
configuration or configuration features, they will fall back to any rules
declared in the manifest. Your App link can still correctly open your app or
fall back gracefully to the web for users on previous Android versions. In most
cases, you can safely deploy dynamic rules without affecting the experience for
the rest of your user base.

### Considerations for setting up Dynamic App Links filter rules

If you are setting up Intent filters for use with Dynamic App Links in Android
15 and higher, keep in mind that path-level routing rules defined in your
server-side assetlinks.json file cannot **expand the scope that** you've set
statically in your manifest file Intent filter rules.

For this reason, we recommend setting up the broadest possible scope in your
manifest intent filters, and then relying on the server-side assetlinks.json
rules for further refinement. With this ideal configuration, you will then be
able to add new App Links dynamically that fit within the broad scope set in the
manifest.

## Plan your App Links implementation

Supporting App Links requires an implementation in your app, as well as
server-side work to set up your `assetlinks.json` file. The general preparation
and implementation tasks are listed here, with links to other resources for
details.

- Planning your deep links -- Start with an assessment of the deep links that you need, the URL patterns that they will use, how and when you will update them, and the Activity or action that you want each URL to resolve to in your app.
- Support Dynamic App Links - Give users on the latest Android devices the best possible experience. Take advantage of Dynamic App Links for users on Android 15 or later.
- Plan your dynamic filter rules -- If you are using Dynamic App Links, plan how your server-side rules will work with the statically defined rules in your app manifest. Keep in mind that the filter rules in your assetlinks.json file cannot expand the scope of your app manifest filters. You should plan for your manifest filters to declare the broadest possible scope, and then your server-side rules can refine those rules as needed. For more information, see [Configure dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks).
- Create and test intent filters for your links -- declare your deep links in intent filters and test the URL pattern matching and the incoming intent handling. To support Dynamic App Links, note that you might need to move some fine-grained paths to your server-side JSON file instead.
- Read data from incoming App Link intents - Handle incoming deep link intents properly, resolving them to the appropriate Activity. The implementation for App Links is the same as for normal deep links, covered in [Read data from incoming intents](https://developer.android.com/training/app-links/create-deeplinks#read-data).
- Configure website associations and dynamic rules - To support App Links, you need to configure a server-side file that's hosted on your website or domain. Android devices will retrieve this file to validate your App Links implementation with your app. More here.
- Test App Links verification - Check that the Android system is able to successfully auto-verify your deep links. Use debugging and end-to-end testing to check that your configuration is secure and functioning correctly across all verified App Link paths.
- Learn about the tools you can use to set up App Links, including Android Studio and Play Console. More here.