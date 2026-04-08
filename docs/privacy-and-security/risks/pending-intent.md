---
title: Pending intents  |  Security  |  Android Developers
url: https://developer.android.com/privacy-and-security/risks/pending-intent
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Guides](https://developer.android.com/privacy-and-security/security-tips)

# Pending intents Stay organized with collections Save and categorize content based on your preferences.




**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

A [`PendingIntent`](/reference/android/app/PendingIntent) is a reference to a token maintained by the system. Application A can pass a PendingIntent to application B in order to allow application B to execute predefined actions on behalf of application A; regardless of whether application A is still alive.

## Risk: Mutable Pending Intents

A PendingIntent can be mutable, which means that the inner intent that specifies the action can be updated by application B following the logic described in the [`fillIn()`](/reference/android/content/Intent#fillIn(android.content.Intent,%20int)) documentation. In other words, the unfilled fields of a PendingIntent can be modified by a malicious app and allow access to otherwise non-exported components of the vulnerable application.

### Impact

The impact of this vulnerability varies depending on the implementation of the targeted unexported functionality of the app.

### Mitigations

#### General

Make sure action, component, and package are set to avoid the worst vulnerabilities:

### Kotlin

```
val intent = Intent(intentAction)

// Or other component setting APIs e.g. setComponent, setClass
intent.setClassName(packageName, className)

PendingIntent pendingIntent =
    PendingIntent.getActivity(
        context,
        /* requestCode = */ 0,
        intent, /* flags = */ PendingIntent.FLAG_IMMUTABLE
    )
```

### Java

```
Intent intent = new Intent(intentAction);

// Or other component setting APIs e.g. setComponent, setClass
intent.setClassName(packageName, className);

PendingIntent pendingIntent =
        PendingIntent.getActivity(
            getContext(),
            /* requestCode= */ 0,
            intent, /* flags= */ 0);
```

#### Flag IMMUTABLE

If your app targets Android 6 (API level 23) or higher, [specify mutability](/guide/components/intents-filters#DeclareMutabilityPendingIntent). For example, this can be done by using [`FLAG_IMMUTABLE`](/reference/android/app/PendingIntent#FLAG_IMMUTABLE) to prevent unfilled fields from being filled in by a malicious application:

### Kotlin

```
val pendingIntent =
    PendingIntent.getActivity(
        context,
        /* requestCode = */ 0,
        Intent(intentAction),
        PendingIntent.FLAG_IMMUTABLE)
```

### Java

```
PendingIntent pendingIntent =
        PendingIntent.getActivity(
            getContext(),
            /* requestCode= */ 0,
            new Intent(intentAction),
            PendingIntent.FLAG_IMMUTABLE);
```

On Android 11 (API level 30) and higher, you have to specify which fields to make mutable, which mitigates accidental vulnerabilities of this type.

### Resources

* [Remediation of PendingIntent vulnerability](https://support.google.com/faqs/answer/9267555)
* [Blog post about the vulnerability](https://valsamaras.medium.com/pending-intents-a-pentesters-view-92f305960f03)

---

## Risk: Replaying Pending Intents

A PendingIntent can be replayed unless the [FLAG\_ONE\_SHOT](/reference/android/app/PendingIntent#FLAG_ONE_SHOT) flag is set. It is important to use FLAG\_ONE\_SHOT to avoid replay attacks (performing actions that should not be repeatable).

### Impact

The impact of this vulnerability varies depending on the implementation of the receiving end of the intent. A malicious app exploiting a PendingIntent that was created without setting the FLAG\_ONE\_SHOT flag could capture and re-use the intent to repeat actions that should only be able to be done once.

### Mitigations

Pending Intents not intended to be fired multiple times should use the [FLAG\_ONE\_SHOT](/reference/android/app/PendingIntent#FLAG_ONE_SHOT) flag to avoid replay attacks.

### Kotlin

```
val pendingIntent =
      PendingIntent.getActivity(
          context,
          /* requestCode = */ 0,
          Intent(intentAction),
          PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_ONE_SHOT)
```

### Java

```
PendingIntent pendingIntent =
        PendingIntent.getActivity(
            getContext(),
            /* requestCode= */ 0,
            new Intent(intentAction),
            PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_ONE_SHOT);
```

### Resources

* [PendingIntent.FLAG\_ONE\_SHOT](/reference/android/app/PendingIntent#FLAG_ONE_SHOT)

---

## Resources

* [PendingIntent documentation](/reference/android/app/PendingIntent)
* [PendingIntent and intent filters](/guide/components/intents-filters#PendingIntent)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Intent redirection](/topic/security/risks/intent-redirection)