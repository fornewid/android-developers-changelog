---
title: https://developer.android.com/privacy-and-security/risks/intent-redirection
url: https://developer.android.com/privacy-and-security/risks/intent-redirection
source: md.txt
---

# Intent redirection

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

An intent redirection occurs when an attacker can partly or fully control the contents of an intent used to launch a new component in the context of a vulnerable app.

The intent used to launch the new component can be supplied in several ways, most commonly either as a serialized intent in an`extras`field, or marshaled to a string and parsed. Partial control of parameters can also lead to the same result.

## Impact

The impact can vary. An attacker might execute internal features in the vulnerable app, or it might access private components like unexported ContentProvider objects.

## Mitigations

In general, don't expose features related to redirecting nested intents. In cases where it's unavoidable, apply the following mitigation methods:

- Properly sanitize the bundled information. It's important to remember to check or clear flags (`FLAG_GRANT_READ_URI_PERMISSION,
  FLAG_GRANT_WRITE_URI_PERMISSION, FLAG_GRANT_PERSISTABLE_URI_PERMISSION, and
  FLAG_GRANT_PREFIX_URI_PERMISSION`), and to check where the intent is being redirected.[`IntentSanitizer`](https://developer.android.com/reference/kotlin/androidx/core/content/IntentSanitizer)can help with this process.
- Use[`PendingIntent`](https://developer.android.com/guide/components/intents-filters#PendingIntent)objects. This prevents your component from being exported and makes the target action intent immutable.

Apps can check where an intent is being redirected using methods such as[`ResolveActivity`](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager)):  

### Kotlin

    val intent = getIntent()
    // Get the component name of the nested intent.
    val forward = intent.getParcelableExtra<Parcelable>("key") as Intent
    val name: ComponentName = forward.resolveActivity(packageManager)
    // Check that the package name and class name contain the expected values.
    if (name.packagename == "safe_package" && name.className == "safe_class") {
        // Redirect the nested intent.
        startActivity(forward)
    }

### Java

    Intent intent = getIntent()
    // Get the component name of the nested intent.
    Intent forward = (Intent) intent.getParcelableExtra("key");
    ComponentName name = forward.resolveActivity(getPackageManager());
    // Check that the package name and class name contain the expected values.
    if (name.getPackageName().equals("safe_package") &&
            name.getClassName().equals("safe_class")) {
        // Redirect the nested intent.
        startActivity(forward);
    }

Apps can use[`IntentSanitizer`](https://developer.android.com/reference/kotlin/androidx/core/content/IntentSanitizer)using logic similar to the following:  

### Kotlin

    val intent = IntentSanitizer.Builder()
         .allowComponent("com.example.ActivityA")
         .allowData("com.example")
         .allowType("text/plain")
         .build()
         .sanitizeByThrowing(intent)

### Java

    Intent intent = new  IntentSanitizer.Builder()
         .allowComponent("com.example.ActivityA")
         .allowData("com.example")
         .allowType("text/plain")
         .build()
         .sanitizeByThrowing(intent);

#### Default protection

Android 16 introduces a by-default security hardening solution to`Intent`redirection exploits. In most cases, apps that use intents normally won't experience any compatibility issues.

##### Opt out of Intent redirection handling

Android 16 introduces a new API that allows apps to opt out of launch security protections. This might be necessary in specific cases where the default security behavior interferes with legitimate app use cases.
| **Important:** Opting out of security protections should be done with caution and only when absolutely necessary, as it can increase the risk of security vulnerabilities. Carefully assess the potential impact on your app's security before using this API.

In Android 16, you can opt out of security protections by using the`removeLaunchSecurityProtection()`method on the`Intent`object. For example:  

    val i = intent
    val iSublevel: Intent? = i.getParcelableExtra("sub_intent")
    iSublevel?.removeLaunchSecurityProtection() // Opt out from hardening
    iSublevel?.let { startActivity(it) }

#### Common mistakes

- Checking if`getCallingActivity()`returns a non-null value. Malicious apps can supply a null value for this function.
- Assuming that`checkCallingPermission()`works in all contexts, or that the method throws an exception when it is actually returning an integer.

#### Debugging features

For apps that target Android 12 (API level 31) or higher, you can enable a[debugging feature](https://developer.android.com/guide/components/intents-filters#DetectUnsafeIntentLaunches)that, in some cases, helps you detect whether your app is performing an unsafe launch of an intent.

If your app performs**both** of the following actions, the system detects an unsafe intent launch, and a`StrictMode`violation occurs:

- Your app unparcels a nested intent from the extras of a delivered intent.
- Your app immediately starts an app component using that nested intent, such as passing the intent into`startActivity()`,`startService()`, or`bindService()`.

## Resources

- [Remediation for Intent Redirection](https://support.google.com/faqs/answer/9267555)
- [Intents and intent filters](https://developer.android.com/guide/components/intents-filters#DetectUnsafeIntentLaunches)