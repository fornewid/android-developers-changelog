---
title: https://developer.android.com/privacy-and-security/risks/implicit-intent-hijacking
url: https://developer.android.com/privacy-and-security/risks/implicit-intent-hijacking
source: md.txt
---

# Implicit intent hijacking

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

The[implicit intent](https://developer.android.com/guide/components/intents-filters#Types)hijacking vulnerability occurs when an application does not specify a fully-qualified component class name or package when invoking an intent. This allows a malicious application to register an intent filter to intercept the intent instead of the intended application.

Depending on the intent content, attackers could read or modify sensitive information or interact with mutable objects, such as[mutable](https://developer.android.com/reference/android/app/PendingIntent#FLAG_MUTABLE)[PendingIntents](https://developer.android.com/reference/android/app/PendingIntent)or[Binders](https://developer.android.com/reference/android/os/Binder).

Hijacking an implicit intent can also allow an attacker to perform arbitrary actions such as launching attacker-controlled components.

## Impact

If an implicit intent handling sensitive data passes a session token within an extra URL string to open a WebView, any application specifying the proper intent filters can read this token. This can allow any properly-configured application on the device to intercept the intent and read the sensitive data within, allowing attackers to exfiltrate data such as PII or session tokens.

## Mitigations

Unless the application requires it, make intents explicit by calling`setPackage()`. This allows the intent to be interpreted only by a specific component (either in-app or from other applications), preventing untrusted applications from intercepting the data sent along with the intent. The following snippet shows how to make an intent explicit:  

### Kotlin

    val intent = Intent("android.intent.action.CREATE_DOCUMENT").apply {
        addCategory("android.intent.category.OPENABLE")
        setPackage("com.some.packagename")
        setType("*/*")
        putExtra("android.intent.extra.LOCAL_ONLY", true)
        putExtra("android.intent.extra.TITLE", "Some Title")
    }
    startActivity(intent)

### Java

    Intent intent = new Intent("android.intent.action.CREATE_DOCUMENT");
    intent.addCategory("android.intent.category.OPENABLE");
    intent.setPackage("com.some.packagename");
    intent.setType("*/*");
    intent.putExtra("android.intent.extra.LOCAL_ONLY", true);
    intent.putExtra("android.intent.extra.TITLE", "Some Title");
    startActivity(intent);

If you need to use implicit intents, omit any sensitive information or mutable objects that you don't want to expose. Implicit intents may need to be used when an app does not have exact knowledge about which app will resolve the action (e.g. composing an email, taking a picture, etc.).

## Resources

- [Manifest intent-filter element](https://developer.android.com/guide/topics/manifest/intent-filter-element)
- [Privileged Permission Allowlisting](https://source.android.com/devices/tech/config/perms-allowlist)
- [Intents and Intent filters](https://developer.android.com/guide/components/intents-filters)
- [Forcing chooser for implicit intents](https://developer.android.com/guide/components/intents-filters#ForceChooser)
- [Common implicit intents](https://developer.android.com/guide/components/intents-common)