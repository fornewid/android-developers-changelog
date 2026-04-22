---
title: https://developer.android.com/training/app-links/add-applinks
url: https://developer.android.com/training/app-links/add-applinks
source: md.txt
---

App Links are deep links that use the HTTP or HTTPS scheme and are verified by
Android as associated with your website. To register to handle App Links, follow
these steps:

1. Add one or more Intent filters to your app manifest that specify your website domain or URLs.
2. Add the `autoVerify="true"attribute` to the Intent filter elements. This signals to the system that it should attempt to verify the scheme and host domain(s) against your website's `assetlinks.json` configuration.
3. Declare website associations.

The following is an example of an App Link declaration with schemes and hosts as
well as `autoVerify="true`":

    <activity
        android:name=".MainActivity"
        android:exported="true"
        ...>
        <!-- Make sure you explicitly set android:autoVerify to "true". -->
        <intent-filter android:autoVerify="true">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />

            <!-- If a user clicks on a link that uses the "http" scheme, your
                 app should be able to delegate that traffic to "https". -->
            <!-- Do not include other schemes, as this will prevent verification. -->
            <data android:scheme="http" />
            <data android:scheme="https" />

            <!-- Include one or more domains that should be verified. -->
            <data android:host="www.example.com" />
            <data android:host="*.example.com" />
        </intent-filter>
    </activity>

## Key points about the code

- **AutoVerify** : The `android:autoVerify="true`" attribute is required for App Links. It signals to the system that it should attempt to verify the association between your app and the schemes and domain(s) specified in the `<data>` tags. It's recommended to add `autoVerify="true`" to every Intent filter that you want to be verifiable.
- **Data elements** : Each App Links Intent filter must include one or more `<data>` elements that specify the schemes and host formats that match your verifiable website domain.
- **Schemes** : The intent filter must include `<data>` elements for both `http` and `https` schemes.
- **Hosts** : You can optionally add `<data>` elements to match one or more
  hosts. Use a wildcard (`*`) to match multiple subdomains (such as
  `*.example.com`). The system will attempt to verify each host against your
  assetlinks.json file on your website. Note that any path-level routing should
  be handled by the assetlinks.json file (see the best practices section below).

- **Multiple Hosts**: If you declare multiple host domains, the system (on
  Android 12+) attempts to verify each one. If any host is verified, the app
  becomes the default handler for links from that verified host. On Android 11
  and lower, verification fails if even one host cannot be verified.

- **Multiple Intent filters** : It's important to create separate filters when
  your intention is to declare unique URLs (such as a specific combination of
  scheme and host), because multiple `<data>` elements in the same intent filter
  are merged together to account for all variations of their combined
  attributes.

> [!CAUTION]
> **Caution:** If multiple activities contain intent filters that resolve to the same verified App Link, then there's no guarantee as to which Activity handles the link.

## Considerations for manifest filter rules

If you are setting up filters for use with Dynamic App Links in Android 15 and
higher, it's important to remember that the dynamic rules declared in the
server-side assetlinks.json file can't expand the scope of the URL rules that
you declare statically in your app manifest.

For this reason, we recommend using this approach:

- In your app manifest, set the broadest possible scope, such as by declaring scheme and domain only
- Rely on the server-side assetlinks.json rules for further refinement, such as path-level routing.

With this ideal configuration, you will be able to dynamically add new App Links
paths in the `assetlinks.json` file as needed, knowing that they will fit within
the broad scope that you've set in the app manifest.

## Support App Links for multiple hosts

The system must be able to verify the host specified in the app's URL intent
filters' data elements against the Digital Asset Links files hosted on the
respective web domains in that intent filter. If the verification fails, the
system then defaults to its standard behavior to resolve the intent, as
described in [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking). However, the app can still
be verified as a default handler for any of the URL patterns defined in the
app's other intent filters.

> [!NOTE]
> **Note:** On Android 11 (API level 30) and lower, the system doesn't verify your app as a default handler unless it finds a matching Digital Asset Links file for *all* hosts that you define in the manifest.

For example, an app with the following intent filters would pass verification
only for `https://www.example.com` if an `assetlinks.json` file were found at
`https://www.example.com/.well-known/assetlinks.json` but not
`https://www.example.net/.well-known/assetlinks.json`:

    <application>

      <activity android:name="MainActivity">
        <intent-filter android:autoVerify="true">
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data android:scheme="http" />
          <data android:scheme="https" />
          <data android:host="www.example.com" />
        </intent-filter>
      </activity>
      <activity android:name="SecondActivity">
        <intent-filter>
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data android:scheme="https" />
         <data android:host="www.example.net" />
        </intent-filter>
      </activity>

    </application>

> [!NOTE]
> **Note:** All `<data>` elements in the same intent filter are merged together to account for all variations of their combined attributes. For example, the first intent filter includes a `<data>` element that only declares the HTTPS scheme. But it is combined with the other `<data>` element so that the intent filter supports both `http://www.example.com` and `https://www.example.com`. As such, you must create separate intent filters when you want to define specific combinations of URI schemes and domains.

### Support app linking for multiple subdomains

The Digital Asset Links protocol treats subdomains in your intent filters as
unique, separate hosts. So if your intent filter lists multiple hosts with
different subdomains, you must publish a valid `assetlinks.json` on each domain.
For example, the following intent filter includes `www.example.com` and
`mobile.example.com` as accepted intent URL hosts. So a valid `assetlinks.json`
must be published at both `https://www.example.com/.well-known/assetlinks.json`
and `https://mobile.example.com/.well-known/assetlinks.json`.

    <application>
      <activity android:name="MainActivity">
        <intent-filter android:autoVerify="true">
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data android:scheme="https" />
          <data android:scheme="https" />
          <data android:host="www.example.com" />
          <data android:host="mobile.example.com" />
        </intent-filter>
      </activity>
    </application>

Alternatively, if you declare your hostname with a wildcard (such as
`*.example.com`), you must publish your `assetlinks.json` file at the root
hostname (`example.com`). For example, an app with the following intent filter
will pass verification for any sub-name of `example.com` (such as
`foo.example.com`) as long as the `assetlinks.json` file is published at
`https://example.com/.well-known/assetlinks.json`:

    <application>
      <activity android:name="MainActivity">
        <intent-filter android:autoVerify="true">
          <action android:name="android.intent.action.VIEW" />
          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="android.intent.category.BROWSABLE" />
          <data android:scheme="https" />
          <data android:host="*.example.com" />
        </intent-filter>
      </activity>
    </application>

### Check for multiple apps associated with the same domain

If you publish multiple apps that are each associated with the same domain, they
can each be successfully verified. However, if the apps can resolve the exact
same domain host and path, as might be the case with lite and full versions of
an app, only the app that was installed most recently can resolve web intents
for that domain.

In a case like this, check for possible conflicting apps on the user's device,
provided that you have the necessary [package visibility](https://developer.android.com/training/package-visibility). Then, in your app,
show a custom chooser dialog that contains the results from calling
[`queryIntentActivities`](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities)(). The user can select their preferred app from the
list of matching apps that appear in the dialog.

> [!NOTE]
> **Note:** Consider storing the matching path so that the user doesn't have to re-select if a similar web intent is launched later.

## Dynamic App Links backward compatibility for Android 14 and lower

Dynamic App Link features, including advanced matching rules in
`assetlinks.json` and the use of `<uri-relative-filter-group>`, are only fully
supported on Android 15 (API level 35) and higher.

On Android 14 (API level 34) and lower, the system only considers the `scheme`
and `host` declared in your manifest's `<data>` elements for App Link
verification. Path-specific rules, exclusions, and dynamic updates from
assetlinks.json are not applied.

This means if your manifest only specifies `scheme` and `host`, your app might
unexpectedly capture all paths for the verified domain on Android 14 and lower,
regardless of the path-specific rules defined in your `assetlinks.json` for
Android 15 and higher.

### Fallback strategy for lower Android versions to be configured with no deep links

To prevent your app from handling all links for a domain on Android 14 and
lower when you intend to use Dynamic App Links for more specific paths on
Android 15 and higher, include a non-matching path in your manifest's intent
filter.
Add a `<data>` element with an `android:path` attribute that is unlikely to
ever be a valid path for your links. This ensures that the intent filter
doesn't match all paths on lower versions.

Example:

    <activity
        android:name=".MainActivity"
        android:exported="true"
        ...>
        <intent-filter android:autoVerify="true">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />

            <data android:scheme="http" />
            <data android:scheme="https" />
            <data android:host="www.example.com" />

            <!-- Add a non-matching path for backward compatibility -->
            <data android:path="/no_match_for_older_android_versions" />

            <uri-relative-filter-group android:allow="true">
              <data android:pathPattern="/.*"/>
            </uri-relative-filter-group>
        </intent-filter>
    </activity>

By adding `<data android:path="/no_match_for_older_android_versions" />`, you
ensure that on Android 14 and lower, this intent filter doesn't match any
incoming links, while still allowing the domain to be verified for use with
Dynamic App Links on Android 15 and higher based on the advanced matching
rules in your `assetlinks.json` rules.

> [!WARNING]
> **Warning:** If you configure `<uri-relative-filter-group>` in your manifest for Android 15 and higher, ensure that a valid `assetlinks.json` file is accessible at the specified host. If the `assetlinks.json` file is missing or invalid, App Links verification fails on Android 15 and higher, and your app doesn't handle any links for that domain. In other cases, where the `assetlinks.json` file is valid but missing the dynamic configuration, the app might open for all paths on Android 15 and higher based on the static manifest declaration.

### Migrating existing App Links

If you already have App Links with specific path rules (such as
`android:pathPrefix`) in your manifest and want to start using Dynamic App Links
on Android 15 and higher, you can safely add the `<uri-relative-filter-group>`
element directly to your existing intent filters.

Because Android 14 and lower ignore the `<uri-relative-filter-group>` element,
your existing App Links continue to work exactly as they do now on devices
running lower versions of Android.

However, you must carefully consider how Android 15 and higher evaluates the
"mixed" configuration:

- **Two-layer filtering:** On Android 15 and higher, the system evaluates intent filters as a union. A URL passes the manifest check if it satisfies either your legacy static `<data>` tags or the broad rules in your `<uri-relative-filter-group>`. Once the URL passes this initial manifest check, the system then applies the dynamic rules defined in your `assetlinks.json` file as a second layer of fine-grained filtering. This means the server-side JSON rules ultimately dictate which of those matched URLs actually open the app.

**Example of a hybrid configuration:**

    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />

        <data android:scheme="https" />
        <data android:host="www.example.com" />

        <!-- Legacy rule: Android 14 and lower use this. Android 15 and higher
             also use this. -->
        <data android:pathPrefix="/store" />

        <!--
          Dynamic rule: Android 14 and lower ignore this. Android 15 and higher
          evaluate this as a union between all paths and the configuration
          specified in the assetlinks.json file. Make sure to apply further
          refinements in the assetlinks.json file to prevent all URL paths from
          opening in the app.
        -->
        <uri-relative-filter-group android:allow="true">
            <data android:pathPrefix="/" />
        </uri-relative-filter-group>
    </intent-filter>