---
title: https://developer.android.com/privacy-and-security/risks/create-package-context
url: https://developer.android.com/privacy-and-security/risks/create-package-context
source: md.txt
---

# createPackageContext

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

    public abstract Context createPackageContext (String packageName, int flags)

The method[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int))is used when a developer wants to create a context for another application in their own application.

For example, if developers want to get resources from a 3rd-party application or call methods from it, they would use`createPackageContext`.

However, if an application calls`createPackageContext`with the[`CONTEXT_IGNORE_SECURITY`](https://developer.android.com/reference/android/content/Context#CONTEXT_IGNORE_SECURITY)and[`CONTEXT_INCLUDE_CODE`](https://developer.android.com/reference/android/content/Context#CONTEXT_INCLUDE_CODE)flags, and then calls[`getClassLoader()`](https://developer.android.com/reference/android/content/Context#getClassLoader()), this could result in making the application vulnerable to code execution by a malicious application. This can occur, for example, when an attacker impersonates an unclaimed package name (package squatting) that the developer had expected to be present on the user's device.

To summarize the criteria that have to be met to make an application vulnerable to this kind of attack:

Vulnerable App:

- Calls[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int))with[`CONTEXT_IGNORE_SECURITY`](https://developer.android.com/reference/android/content/Context#CONTEXT_IGNORE_SECURITY)and[`CONTEXT_INCLUDE_CODE`](https://developer.android.com/reference/android/content/Context#CONTEXT_INCLUDE_CODE).
- Calls[`getClassLoader()`](https://developer.android.com/reference/android/content/Context#getClassLoader())on the retrieved context.

Malicious App:

- Is able to claim the package name that the vulnerable app passes to[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int)).
- Exports android:appComponentFactory.

## Impact

When createPackageContext is used in an insecure way by an application, this can lead to a malicious application being able to gain arbitrary code execution in the context of the vulnerable application.

## Mitigations

Don't call[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int))with[`CONTEXT_IGNORE_SECURITY`](https://developer.android.com/reference/android/content/Context#CONTEXT_IGNORE_SECURITY)and[`CONTEXT_INCLUDE_CODE`](https://developer.android.com/reference/android/content/Context#CONTEXT_INCLUDE_CODE)unless absolutely necessary.

In cases where this is unavoidable, make sure to implement a mechanism to verify the identity of the package you are executing[`createPackageContext`](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int))on (e.g. by verifying the package's signature).

## Resources

- [createPackageContext Documentation](https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int))
- [OverSecured blog post on createPackageContext code execution](https://blog.oversecured.com/Android-arbitrary-code-execution-via-third-party-package-contexts)