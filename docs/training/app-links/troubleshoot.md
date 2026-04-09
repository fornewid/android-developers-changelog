---
title: https://developer.android.com/training/app-links/troubleshoot
url: https://developer.android.com/training/app-links/troubleshoot
source: md.txt
---

This guide describes common issues and how to troubleshoot them. You can
also use the troubleshooting tools in the Play Console Deep Links page or the
Android Studio App Links Assistant. For more information, see
[App Links developer tools](https://developer.android.com/training/app-links/tools).

## App link opens in the browser instead of the app

- **Problem**: You click a link that should open your app, but it opens in a web browser or shows a disambiguation dialog.
- **Solution** :
  - **Check `assetlinks.json`** : Ensure the file is valid JSON, accessible at `https://<your-domain>/.well-known/assetlinks.json`, and served over HTTPS with no redirects. Use an online validator.
  - **Verify SHA-256 Fingerprint** : Double-check that the `sha256_cert_fingerprints` in `assetlinks.json` exactly matches the fingerprint of the signing key for your app release (use the one from the Play Console if you use Play App Signing). The signature should be uppercase.
  - **Verify `autoVerify`** : Make sure the `<intent-filter>` in your `AndroidManifest.xml` includes `android:autoVerify="true`".
  - **Check for server-side redirects** : Redirects from `http` to `https` or from a non-www domain to `www` can cause verification to fail.
  - **Force Re-verification** : Run the ADB commands in the [Test App Links](https://developer.android.com/training/app-links/verify-applinks) guide to get a fresh verification result.

## Dynamic rules on Android 15+ aren't updating

- Problem: You've updated the rules in your `assetlinks.json` file, but the new links are not being handled by the app.
- **Solution** :
  - **Force re-verification** : The most reliable way to test changes is to force a re-fetch with `adb shell pm verify-app-links --re-verify.
    <your-package-name>`.
  - **Check for typos**: Carefully review your pattern matchers in your rules for any syntax errors.
  - **Check manifest filter rules**: review the intent filter rules in the app manifest to make sure that the link path is not being filtered out. If the link is being filtered out, make the intent filter in the app manifest less restrictive.

## Fix common implementation errors

If you can't verify your Android App Links, check for the following common
errors. This section uses `example.com` as a placeholder domain name; when
performing these checks, substitute `example.com` with your server's actual
domain name.

Incorrect intent filter set up
:   Check to see whether you include a URL that your app doesn't own in an
    `<intent-filter>` element.

Incorrect server configuration

:   Check to your server's JSON configuration, and make sure the SHA value is
    correct.

    Also, check that `example.com.` (with the trailing period) serves the same
    content as `example.com`.

Server-side redirects

:   The system doesn't verify **any** Android App Links for your app if you set up
    a redirect such as the following:

    - `http://example.com` to `https://example.com`
    - `example.com` to `www.example.com`

    This behavior protects your app's security.

Server robustness

:   Check whether your client apps can connect to your server.

Non-verifiable links

:   For testing purposes, you might intentionally add non-verifiable links. Keep
    in mind that, on Android 11 and lower, these links cause the
    system to not verify **all** Android App Links for your app.

Incorrect signature in assetlinks.json

:   Verify that your signature is correct and matches the signature used to sign
    your app. Common mistakes include:

    - Signing the app with a debug certificate and only having the release signature in `assetlinks.json`.
    - Having a lower case signature in `assetlinks.json`. The signature should be in upper case.
    - If you are using Play App Signing, make sure you're using the signature that Google uses to sign each of your releases. You can verify these details, including a complete JSON snippet, by following instructions about [declaring website associations](https://developer.android.com/training/app-links/troubleshoot#web-assoc).