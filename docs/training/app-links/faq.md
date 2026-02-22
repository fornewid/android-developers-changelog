---
title: https://developer.android.com/training/app-links/faq
url: https://developer.android.com/training/app-links/faq
source: md.txt
---

### What happens on devices running lower versions of Android?

Dynamic App Links on Android 15+ uses the same `handle_all_urls` relation type
as App Links on earlier versions, but uses a new field,
`dynamic_app_link_components`. Earlier versions will ignore the new
`dynamic_app_link_components` field to allow for compatibility. If you need to
support specific paths on older Android versions, you must declare them in the
manifest as you traditionally would.

### Can I use both manifest-based path rules and dynamic rules at the same time?

Yes, the system will merge your dynamic rules with manifest-based rules.
However, note that the rules defined in your manifest set the maximum allowed
scope for your App Link paths, so all of your dynamic rules must be within that
scope. The system does not allow dynamic rules to change or expand the static
scope that you have declared in your manifest paths. A typical Dynamic App Links
implementation would have a fairly broad scope set in the manifest
configuration, with dynamic rules managed from the server that fine-tune the
paths.

### What's the best way to get the SHA-256 fingerprint for the assetlinks.json file?

The most reliable way is to get it from the Google Play Console. Navigate to
your app's **Setup \> App integrity** page. Under
**App signing key certificate** , you will find the SHA-256 certificate
fingerprint. This is the same key that Google Play uses to sign your app
release. Alternatively, for local builds, you can use the `keytool`
command-line utility on your keystore file.