---
title: https://developer.android.com/training/app-links/test-applinks
url: https://developer.android.com/training/app-links/test-applinks
source: md.txt
---

When implementing the app linking feature, you should test the linking
functionality to make sure the system can associate your app with your websites,
and handle URL requests, as you expect.

To test an existing statement file, you can use the [Statement List Generator
and Tester](https://developers.google.com/digital-asset-links/tools/generator) tool.

The following sections describe how to test your App Links verification
manually. If you prefer, you can test verification from Play Deep Links tool or
the Android Studio App Links Assistant.

## Confirm the list of hosts to verify

When testing, you should confirm the list of associated hosts that the system
should verify for your app. Make a list of all URLs whose corresponding intent
filters include the following attributes and elements:

- `android:scheme` attribute with a value of `http` or `https`
- `android:host` attribute with a domain URL pattern
- `android.intent.action.VIEW` action element
- `android.intent.category.BROWSABLE` category element

Use this list to check that a Digital Asset Links JSON file is provided on each
named host and subdomain.

## Confirm the Digital Asset Links files

For each website, use the Digital Asset Links API to confirm that the Digital
Asset Links JSON file is properly hosted and defined:

    https://digitalassetlinks.googleapis.com/v1/statements:list?
       source.web.site=https://<var>domain.name</var>:<var>optional_port</var>&amp;
       relation=delegate_permission/common.handle_all_urls

For Dynamic App Links, you can also check the relation extensions.

    https://digitalassetlinks.googleapis.com/v1/statements:list?source.web.site=https://www.example.com&relation=delegate_permission/common.handle_all_urls&return_relation_extensions=true

### Check link policies

As part of your testing process, you can check the current system settings for
link handling. Use the following command to get a listing of existing
link-handling policies for all apps on your connected device:

    adb shell dumpsys package domain-preferred-apps

The following command does the same thing:

    adb shell dumpsys package d

> [!NOTE]
> **Note:** Make sure you wait at least 20 seconds after installation of your app to allow for the system to complete the verification process.

The command returns a listing of each user or profile defined on the device,
preceded by a header in the following format:

    App linkages for user 0:

Following this header, the output uses the following format to list the
link-handling settings for that user:

    Package: com.android.vending
    Domains: play.google.com market.android.com
    Status: always : 200000002

This listing indicates which apps are associated with which domains for that
user:

- `Package` - Identifies an app by its package name, as declared in its manifest.
- `Domains` - Shows the full list of hosts whose web links this app handles, using blank spaces as delimiters.
- `Status` - Shows the current link-handling setting for this app. An app that has passed verification, and whose manifest contains `android:autoVerify="true"`, shows a status of `always`. The hexadecimal number after this status is related to the Android system's record of the user's app linkage preferences. This value does not indicate whether verification succeeded.

> [!NOTE]
> **Note:** If a user changes the app link settings for an app before verification is complete, you may see a false positive for a successful verification, even though verification has failed. This verification failure, however, does not matter if the user explicitly enabled the app to open supported links without asking. This is because user preferences take precedence over programmatic verification (or lack of it). As a result, the link goes directly to your app, without showing a dialog, just as if verification had succeeded.

### Test example

For app link verification to succeed, the system must be able to verify your app
with each of the websites that you specify in a given intent filter that meets
the criteria for app links. The following example shows a manifest configuration
with several app links defined:

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
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="https" />
                <data android:host="www.example2.com" />
            </intent-filter>
        </activity>

        <activity android:name="SecondActivity">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="https" />
                <data android:host="account.example.com" />
            </intent-filter>
        </activity>

          <activity android:name="ThirdActivity">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <data android:scheme="https" />
                <data android:host="map.example.com" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="market" />
                <data android:host="example.com" />
            </intent-filter>
          </activity>

    </application>

The list of hosts that the platform would attempt to verify from the preceding
manifest is:

    www.example.com
    mobile.example.com
    www.example2.com
    account.example.com

The list of hosts that the platform wouldn't attempt to verify from the
preceding manifest is:

    map.example.com (it does not have android.intent.category.BROWSABLE)
    market://example.com (it does not have either an "http" or "https" scheme)

To learn more about statement lists, see [Creating a Statement List](https://developers.google.com/digital-asset-links/v1/create-statement).

## Diagnose link resolution with the debug-link flag

Starting in Android 17, you can use the `--debug-link` flag with the activity
manager (`am start`) command to diagnose how the system resolves a specific
URL. This tool provides a detailed breakdown of candidate apps that matched the
intent, along with the specific rules from the app manifest and the
`assetlinks.json` file (for Dynamic App Links) that were evaluated during
resolution.

To test link resolution for a specific URL, run the following command in a
terminal window:

    adb shell am start --debug-link -a android.intent.action.VIEW -d "https://xyz.com/foo"

The diagnostic output is printed under the header `App Link Resolution Debug`
and contains the following sections to help you understand the resolution
process:

- **Target details:** Identifies each matching candidate app by its package name and target activity.
- **Intent Filter Match (`AndroidManifest.xml`):** Shows which static attributes in the manifest intent filter (such as `scheme`, `host`, `path`, `pathPrefix`, or `pathPattern`) matched the URI.
- **App Link Verification:** Shows the current domain verification state (such as `STATE_SUCCESS`).
- **Dynamic App Links:** If the app uses Dynamic App Links matching rules in its `assetlinks.json` file, this section lists every rule that was evaluated against the URI. Each rule indicates the matched URI filters (such as path prefixes or patterns) and an `allow` field:
  - `allow = 0`: An **allow/inclusion** rule (`allow: true`). If this rule matches, the app is allowed to open the URI.
  - `allow = 1`: A **block/exclusion** rule (`allow: false` / `exclude:
    true`). If this rule matches, the app is prevented from opening the URI.
  - *Note* : An empty filter string (`filter =`) indicates an empty path prefix that matches all paths under the domain (acting as a wildcard or catch-all).

### Example debug output

Consider an app (`com.example.xyzapp`) associated with the domain
`https://xyz.com` that defines dynamic rules in its `assetlinks.json` file to
exclude `/foo*` while allowing all other paths:

    [
      {
        "relation": [
          "delegate_permission/common.handle_all_urls"
        ],
        "target": {
          "namespace": "android_app",
          "package_name": "com.example.xyzapp",
          "sha256_cert_fingerprints": ["..."]
        },
        "relation_extensions": {
          "delegate_permission/common.handle_all_urls": {
            "dynamic_app_link_components": [
              {"/": "/foo*", "exclude": true},
              {"/": "*"}
            ]
          }
        }
      }
    ]

When diagnosing the URL `https://xyz.com/foo` using `--debug-link`:

    adb shell am start --debug-link -a android.intent.action.VIEW -d "https://xyz.com/foo"

The command outputs the following diagnostic breakdown:

    --- App Link Resolution Debug ---

    URI: https://xyz.com/foo
    Resolution: Ambiguous (Multiple apps or Browser fallback)
    This usually happens when multiple apps can handle the link and no default is set.

    All Matching Candidates:

    Target:
      Package: com.example.xyzapp
      Activity: com.example.xyzapp.MainActivity

      Intent Filter Match (AndroidManifest.xml)
        Scheme: 'https' matched android:scheme="https"
        Host: 'xyz.com' matched android:host="xyz.com"

    App Link Verification:
      Verification status: STATE_SUCCESS
      Dynamic App Links:
        -> Matched Rule 0: UriRelativeFilterGroup { allow = 1, uri_filters = {UriRelativeFilter { uriPart = PATH, patternType = PREFIX, filter = /foo }},  }
        -> Matched Rule 1: UriRelativeFilterGroup { allow = 0, uri_filters = {UriRelativeFilter { uriPart = PATH, patternType = PREFIX, filter =  }},  }

    Target:
      Package: org.chromium.webview_shell
      Activity: org.chromium.webview_shell.WebViewBrowserActivity

      Intent Filter Match (AndroidManifest.xml)
        Scheme: 'https' matched android:scheme="https"

    ---

    Starting: Intent { act=android.intent.action.VIEW dat=https://xyz.com/foo }

In this example, the system evaluated the two Dynamic App Link rules from
`assetlinks.json`:

- **Rule 0 (`allow = 1`, `filter = /foo`):** Generated from `{"/": "/foo*", "exclude": true}`, this is an exclusion rule (`allow: false`) blocking URLs starting with the `/foo` path prefix.
- **Rule 1 (`allow = 0`, `filter =`):** Generated from `{"/": "*"}`, this is an inclusion rule (`allow: true`) with an empty path prefix (`filter =`), which matches all paths under `xyz.com` (catch-all).

**How resolution works in this scenario:**

1. Both Rule 0 and Rule 1 match the URL `https://xyz.com/foo`.
2. Dynamic App Link rules are evaluated in sequential order from top to bottom (first matching rule wins).
3. Because **Rule 0** appears first in the statement list and is an exclusion rule (`allow = 1`), it takes precedence over the general allow rule (**Rule
   1**).
4. The app is therefore excluded from handling `https://xyz.com/foo`, causing the system to fall back to the browser or display a disambiguation dialog.