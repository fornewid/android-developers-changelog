---
title: https://developer.android.com/developer-verification/guides/android-developer-console
url: https://developer.android.com/developer-verification/guides/android-developer-console
source: md.txt
---

If you distribute apps only outside of Google Play, use the Android Developer
Console to manage your developer identity and register your app's package names.
This guide explains how to verify your account and ensure your apps are
installable on certified Android devices.

## Create an account

You can [sign up for an account](https://android.google.com/developerconsole/developers) using your Google Account. If you're a
student or hobbyist, you can create a special account type that has fewer
verification requirements and no fee.

## Choose how to distribute your apps

Your apps can still be sideloaded. Your user's experience depends on the path
you choose.

## Complete identity verification

There are different requirements for different account types. Review the [full
distribution account](https://developer.android.com/developer-verification/guides/full-distribution) and [limited distribution account](https://developer.android.com/developer-verification/guides/limited-distribution) guides to
determine which is best for you.

## Register your package names

Once verified, you can register your app's package names on the **Packages**
page. The registration process links your app to your verified developer
identity. Complete the following in the Android Developer Console to register:

1. **Enter the package name:** Provide the unique package name you want to register.
2. **Add your key:** Enter the SHA-256 certificate fingerprint from your app's signing key pair. The status will then become ***In review***.
3. **Prove ownership:** For existing package names, you must sign an APK with your private key and upload it. The Android Developer Console provides a snippet to add to the APK's asset folder for this challenge. Once registered, you will be notified by email and the package name status in the Developer Console will update to ***Registered***.

> [!NOTE]
> **Note:** Developers who are not eligible to register a package name can request to share it through an appeal-like process by providing proof of ownership and a legitimate reason for use.

## Automate your workflow

You can automate developer verification and package registration using our APIs:

- **Android Developer ID Status API**: Lets you check if a package name has already been registered and verify eligibility.
- **Android Developer Console API**: Lets you register and manage package names and keys directly within your development environment or CI/CD pipeline.

Both APIs support **OAuth delegation**, allowing third-party platforms (such as
alternative Android app stores) to perform these operations securely on your
behalf.

## Handle duplicate package names

If multiple developers use the same package name, the right to register is
determined by package name registration rules. The following rules aim to
allocate the package name to the developer whose signing key accounts for over
50% of total known installs:

- **Majority cluster**: If a developer's keys account for more than 50% of all installs, that developer holds priority for registration.
- **Sizeable cluster**: If no single key has over 50% installs, any developer with a "sizeable cluster" (50 or more installs) can register the package name.
- **First-come, first-serve basis**: If no sizeable cluster exists, any developer with a known key can register the package name on a first-come, first-served basis.

The following examples demonstrate these rules:

**Priority for majority key holder**:

The developer whose signing key accounts for over 50% of total known installs
holds priority for registration. All other developers will be required to use a
different package name.

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| A | com.test.1 | 11 | 1000 |
| B | com.test.1 | 12 | 100 |

<br />

In this scenario, Developer A is eligible to register the package name.
Developer B would need to use another name or apply for an exception.

**Eligibility for keys with 50+ installs**:

If no single key has over 50% of installs, then all keys with 50 or more
installs become eligible for registration. All other developers---those with keys
with fewer than 50 installs---will be required to request permission to use the
package name.

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| C | com.test.2 | 21 | 100 |
| D | com.test.2 | 22 | 100 |
| E | com.test.2 | 23 | 10 |

Here, no single key has a majority. Developers C and D, with 50 or more
installs, can register the package name. Developer E would need to use a
different package name, or request permission to use this one.

**First-come, first-served for keys under 50 installs**:

If no keys meet the 50-install threshold, any key can be registered on a
first-come, first-served basis. As soon as one developer registers the package
name, the other developers would need to use a different name for their package
names (or request exceptions).

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| F | com.test.3 | 31 | 10 |
| G | com.test.3 | 31 | 10 |

In this scenario, all developers with keys are eligible. Once one developer
registers the package name, the other would need to request permission.