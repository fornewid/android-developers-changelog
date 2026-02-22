---
title: https://developer.android.com/develop/ui/views/layout/webapps/webview-privacy
url: https://developer.android.com/develop/ui/views/layout/webapps/webview-privacy
source: md.txt
---

For users who [share usage statistics and diagnostics with
Google](https://support.google.com/accounts/answer/6078260), `WebView` sends
usage statistics and crash reports to Google. Usage statistics contain
information such as system information, active field trials, feature usage,
responsiveness, performance, and memory usage. They don't include any personally
identifying details.

## Usage statistics

Collected usage statistics are used to improve
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) performance, assess the impact of
changes to existing features, and guide the development of new features.

The stable channel of `WebView` gathers usage statistics from a small percentage
of users. Pre-stable channels might sample from a greater percentage of users.

Starting with `WebView` 71, these statistics are associated with the app package
name. This lets Google proactively monitor and address `WebView` issues that
might degrade the performance of specific apps without causing crashes.

Before `WebView` 104, for any given app, at most 10% of users upload reports
containing the package name. Other users upload blank package names or no upload
records at all.

Starting with `WebView` 104, app package names are always recorded for apps that
are in a list of allowed popular apps. Other apps upload blank package names.

### Opt out usage statistics

Apps can opt out of usage statistics collection by including the following in
the `<application>` section of their manifest:  

    <meta-data android:name="android.webkit.WebView.MetricsOptOut" android:value="true" />

This disables usage statistics collection for all users of the app, regardless
of whether they have the corresponding setting enabled. It doesn't disable crash
reporting.
| **Note:** Opting out of usage statistics collection decreases Google's ability to preemptively detect and address problems in `WebView` updates.

### Opt out of metrics collection

`WebView` has the ability to upload anonymous diagnostic data to Google when the
user gives their consent. Data is collected on a per-app basis for each app that
instantiates a `WebView`. You can opt out of this feature by creating the
following tag in the manifest's `<application>` element:  

```xml
<manifest>
    <application>
    ...
    <meta-data android:name="android.webkit.WebView.MetricsOptOut"
               android:value="true" />
    </application>
</manifest>
```

Data is only uploaded from an app if the user consents **and** the app doesn't
opt out. For more information about opting out of diagnostic data reporting, see
the following section on crash reports.

## Crash reports

Crash reports are collected when a
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) object is likely to be the cause
of the crash. Crash reports contain information required to determine the state
of the `WebView` at the time of the crash. This includes system information,
active field trials, and stack memory from the app required to generate the
sequence of calls made within the thread.

Stack memory is sanitized to remove strings, with the intent of capturing only
the information required to generate stack traces. No URLs are collected as part
of usage statistics or crash reports.

## Pseudonymous identifiers and data privacy

Crash reports and usage statistics collected by `WebView` each contain a
randomly generated 128-bit token used to pseudonymously de-duplicate reports and
maintain accuracy in statistics. Token values aren't shared between apps, and
crash reports and usage statistics have independent tokens. All apps' usage
statistics tokens are cleared when the user opts out of sharing usage statistics
and diagnostics with Google. The crash report token is cleared when the app
cache is cleared. Both tokens are cleared when the app is uninstalled or app
data is cleared.

## Additional resources

To learn more about user privacy, see [Build apps to be private](https://developer.android.com/privacy).