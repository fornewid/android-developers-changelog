---
title: https://developer.android.com/training/app-links/configure-assetlinks
url: https://developer.android.com/training/app-links/configure-assetlinks
source: md.txt
---

To support App Links, you must create a [Digital Asset Links](https://developers.google.com/digital-asset-links)
JSON file called `assetlinks.json` and publish it in a well-known location on
your website. This file publicly declares which apps are authorized to handle
links for your domain, and Android devices will retrieve this file from your
server to verify your deep links.

For dynamic App Links in Android 15+, the `assetlinks.json` file is also
where you [define your dynamic rules configuration](https://developer.android.com/training/app-links/configure-assetlinks#configure-dynamic), such as pattern matchers
for path, fragment, and query parameters. Android devices running Android 15
(API level 35) or later that have Google services installed will periodically
retrieve the file and merge your dynamic configuration with the static
configuration in the app's manifest.

This guide describe how to prepare an `assetlinks.json` file and publish
it on your website. If you prefer, you can generate an `assetlinks.json`
file from the Play Deep Links tool or the Android Studio App Links Assistant.
For more information, see [App Links developer tools](https://developer.android.com/training/app-links/tools).

## Declare website associations

You must publish a [Digital Asset Links](https://developers.google.com/digital-asset-links/v1/getting-started) JSON file on your
website to indicate the Android apps that are associated with the website and
verify the app's URL intents. The JSON file uses the following fields to
identify associated apps:

- `package_name`: The [application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id) declared in the app's `build.gradle` file.
- `sha256_cert_fingerprints`: The SHA256 fingerprints of your app's signing certificate. You can use the following command to generate the fingerprint using the Java keytool:

`keytool -list -v -keystore my-release-key.keystore`

- This field supports multiple fingerprints, which can be used to support different versions of your app, such as debug and production builds. If you're using [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756) for your app, then the certificate fingerprint produced by running `keytool` locally will usually not match the one on users' devices. You can verify whether you're using Play App Signing for your app in your [Play Console](https://play.google.com/console/) developer account under `Release > Setup > App signing`; if you do, then you'll also find the correct Digital Asset Links JSON snippet for your app on the same page.

The following example `assetlinks.json` file grants link-opening rights to a
`com.example` Android app:  

    [{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "com.example",
        "sha256_cert_fingerprints":
        ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
      }
    }]

### Associate a website with multiple apps

A website can declare associations with multiple apps within the same
`assetlinks.json` file. The following file listing shows an example of a
statement file that declares association with two apps, separately, and resides
at `https://www.example.com/.well-known/assetlinks.json`:  

    [{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "com.example.puppies.app",
        "sha256_cert_fingerprints":
        ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
      }
      },
      {
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "com.example.monkeys.app",
        "sha256_cert_fingerprints":
        ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
      }
    }]

Different apps may handle links for different resources under the same web host.
For example, app1 may declare an intent filter for
`https://example.com/articles`, and app2 may declare an intent filter for
`https://example.com/videos`.
| **Note:** Multiple apps associated with a domain may be signed with the same or different certificates.

### Associate multiple websites with a single app

Multiple websites can declare associations with the same app in their respective
`assetlinks.json` files. The following file listings show an example of how to
declare the association of example.com and example.net with app1. The first
listing shows the association of example.com with app1:

https://www.example.com/.well-known/assetlinks.json  

    [{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "com.mycompany.app1",
        "sha256_cert_fingerprints":
        ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
      }
    }]

The next listing shows the association of example.net with app1. Only the
location where these files are hosted is different (.`com` and .`net`):

https://www.example.net/.well-known/assetlinks.json  

    [{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "com.mycompany.app1",
        "sha256_cert_fingerprints":
        ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
      }
    }]

## Configure dynamic rules

Dynamic App Links in Android 15+ lets you use server-side deep link matching
rules that work together with the rules you've defined statically in your app
manifest. Your `assetlinks.json` file is where you define dynamic rules. This
is optional to include.

Android devices running Android 15 (API level 35) or later that have Google
services installed will periodically retrieve this file from your server and
merge your dynamic rules configuration with the static configuration in the
app's manifest. The following is an example of an `assetlinks.json` file with
dynamic rules:  

    [
      {
        "relation": [
          "delegate_permission/common.handle_all_urls"
        ],
        "target": {
          "namespace": "android_app",
          "package_name": "com.example.app",
          "sha256_cert_fingerprints": [...]
        },
        "relation_extensions": {
          "delegate_permission/common.handle_all_urls": {
            "dynamic_app_link_components": [
              {"?": {"dl": "*"}},
              {"#": "app"},
              {"/": "/products/*"},
              {"/": "/shoes", "?": {"in_app": "true"}},
              {"/": "*", "exclude": true}
            ]
          }
        }
      }
    ]

### Key points about the code

- Dynamic App Links adds a new Digital Asset Links relation extension called `dynamic_app_link_components`, which is where you configure your dynamic rules.
- Dynamic rules can include pattern matchers for path, fragment, and query parameters.
- You can also mark any pattern matcher as excluded, so that matching URLs don't open your app.
- This example shows examples of matchers for path (`"/"`), fragment (`"#"`), and query parameters (`"?"`), and also excluded matchers (`"exclude"`)
- If any of the fields in the file are malformed or empty, Android discards the dynamic rules and the device falls back to the rules that are statically defined in the app's manifest.

Dynamic rules can only specify rules that apply within the scope of the domains
that you declare in your app's manifest file. See below.

### Declare dynamic rules

Dynamic App Links supports a new `dynamic_app_link_components` relation
extension, which holds an array of rules objects. Each rule is defined using
pattern matchers for paths, fragments, and query parameters that will open your
app. Matchers can also be individually excluded so that they will not open your
app. All of these are optional.

- Path matching
  - Key: "/"
  - Value: Single string, matching expression for the URL path
- Fragment matching
  - Key: "#"
  - Value: Single string, matching expression for the URL fragment
- Query parameter matching
  - Key: "?"
  - Value: Dictionary to match key/value pairs in the URL query parameters.
  - For example the dictionary {"`?", {"dl": "*", "in_app":"true`"} will match the query string "`?in_app=true&dl=abc`".
  - The order of key/value pairs in the dictionary does not need to match the order of the pairs in the query string. Additionally, the dictionary does not need to match all key/value pairs in the query string, but a match must be found for every dictionary entry.
  - For example the dictionary would also match the query string "`?lang=en&in_app=true&tz=pst&dl=abc`", but not match the query string "`?lang=en&tz=pst&dl=abc`"
- Excluded
  - Key: "exclude"
  - Value: Optional true/false value for each rule defined in `dynamic_app_link_components` (see example).

You can use these special characters in pattern matchers:

- "\*" matches zero or more characters up until the character after the wildcard in the pattern is found in the matching string
- "?" matches any single character
- "?\*" matches 1 or more characters

There are no other character restrictions for values.

### Order dynamic rules

The order in which the rules are declared matters. Android evaluates each rule
in order until it finds a match.

The following example shows how ordering can affect handling. The first rule
matches all paths ("\*") but excludes matches (exclude: true), meaning that it
excludes all URLs from opening the app. In this case, the second rule that
allows "/path1" will never be evaluated.  

    dynamic_app_link_components: [
      {"/": "*", "exclude": true},
      {"/": "/path1"}
    ]

However, in the next example, the "/path1" rule is declared first, so it will be
evaluated first and will open the app for a URL matching "/path1". The second
rule, that excludes all URLs from opening the app, will be evaluated second, but
only if the first rule is not a match.  

    dynamic_app_link_components: [
      {"/": "/path1"},
      {"/": "*", "exclude": true}
    ]

If no matches are found in the list of declared components, the URL won't open
the app. In the following example, none of the paths match "/path3" so the
device will treat this path as excluded.  

    dynamic_app_link_components: [
      {"/": "/path1"},
      {"/": "/path2"}
    ]

This behavior is important if you want `dynamic_app_link_components` to only
exclude certain URL parts but allow all others. In the following example,
omitting the final rule to allow all remaining paths would mean that all URLs
are excluded from the app.  

    dynamic_app_link_components: [
      {"/": "/path1", "exclude": true},
      {"/": "*"}
    ]

### Properly scope your dynamic rules

When defining your server-side rules for use with Dynamic App Links in Android
15 and higher, it's important to scope them appropriately, so that they work
with and complement the static intent filters declared in your app manifest.

Dynamic rules declared in the assetlinks.json file can only specify rules for
the hosts that you declare in your app's `AndroidManifest.xml` file. The dynamic
rules **cannot expand the scope of the URL rules that you declare statically in
your app manifest**.

For this reason, we recommend using this approach across your dynamic and static
rules:

- In your app manifest, set rules with the broadest possible scope, such as by declaring scheme and domain only
- Rely on the server-side dynamic rules for further refinement, such as path-level routing.

With this ideal configuration, you will be able to dynamically add new App Links
paths in the assetlinks.json file as needed, knowing that they will fit within
the broad scope that you've set in the app manifest.

### Declare dynamic_app_link_components only once

For proper handling of your rules, declare only one dynamic_app_link_components
object across the statements for a given site, relation, and app.

- Look for multiple statements for the same site, relation, and app, that declare a dynamic_app_link_components object.
- Look for multiple dynamic_app_link_components objects that are declared in a single statement

In cases like these, Android does not guarantee which dynamic rules
configuration will be used.

### Dynamic rules compatibility with earlier App Links configurations

If you are already supporting App Links, you can add support for Dynamic App
Links directly in your existing assetlinks.json file. The relation fields for
verifying your App Links remain the same, and you can add the new relation
extension fields for dynamic rules without any other changes.

Android devices running Android 14 (API level 34 or earlier) ignore the new
relation extension fields for dynamic rules, while devices running Android 15
and later will merge those rules with your manifest-defined rules.

## Publish the JSON verification file

You must publish your JSON verification file at the following location:

`https://domain.name/.well-known/assetlinks.json`

Be sure of the following:

- The `assetlinks.json` file is served with content-type `application/json`.
- The `assetlinks.json` file must be accessible over an HTTPS connection, regardless of whether your app's intent filters declare HTTPS as the data scheme.
- The `assetlinks.json` file must be accessible without any redirects (no 301 or 302 redirects).
- If your app links support multiple host domains, then you must publish the `assetlinks.json` file on each domain. See [Supporting app linking for
  multiple hosts](https://developer.android.com/training/app-links/verify-android-applinks#multi-host).
- Don't publish your app with test URLs in the manifest file that may not be accessible to the public (such as any that are accessible only with a VPN). A work-around in such cases is to [configure build variants](https://developer.android.com/studio/build/build-variants) to generate a different manifest file for dev builds.

See the following related guides:

- [Creating a Statement List](https://developers.google.com/digital-asset-links/v1/create-statement)
- [App Links Assistant in Android Studio](https://developer.android.com/tools/help/app-link-indexing)
- [App Links developer tools](https://developer.android.com/training/app-links/tools)