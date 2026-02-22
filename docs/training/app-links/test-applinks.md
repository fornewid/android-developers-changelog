---
title: https://developer.android.com/training/app-links/test-applinks
url: https://developer.android.com/training/app-links/test-applinks
source: md.txt
---

When implementing the app linking feature, you should test the linking
functionality to make sure the system can associate your app with your websites,
and handle URL requests, as you expect.

To test an existing statement file, you can use the [Statement List Generator
and Tester](https://developers.google.com/digital-asset-links/tools/generator)
tool.

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

| **Note:** Make sure you wait at least 20 seconds after installation of your app to allow for the system to complete the verification process.

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

| **Note:** If a user changes the app link settings for an app before verification is complete, you may see a false positive for a successful verification, even though verification has failed. This verification failure, however, does not matter if the user explicitly enabled the app to open supported links without asking. This is because user preferences take precedence over programmatic verification (or lack of it). As a result, the link goes directly to your app, without showing a dialog, just as if verification had succeeded.

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

To learn more about statement lists, see [Creating a Statement List](https://developers.google.com/digital-asset-links/v1/create-statement)