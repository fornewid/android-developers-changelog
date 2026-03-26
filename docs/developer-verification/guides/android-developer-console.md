---
title: https://developer.android.com/developer-verification/guides/android-developer-console
url: https://developer.android.com/developer-verification/guides/android-developer-console
source: md.txt
---

If you distribute apps only outside of Google Play, use the Android Developer Console
to manage your developer identity and register your app's package names. This
guide explains how to verify your account and ensure your apps are installable
on certified Android devices.

## Create an account

When the Android Developer Console launches, you can sign up for an account
using your Google Account. If you're a student or hobbyist, you can create a
special account type that has fewer verification requirements and no fee.

## Choose how to distribute your apps

*Your apps can still be sideloaded. Your user's experience depends on the path you choose.*

## Complete identity verification

You must provide official documentation to verify your identity. The requirements vary based on whether you register as an individual or an organization. Completing this process typically takes about 10 minutes if you have all of the required information ready.

#### Required information for all accounts

- **Legal name and address**: Individuals must submit a government-issued
  photo ID and proof of address document as part of the verification program.
  An example of acceptable ID and proof of address documents for individuals
  in the United States are:

  - Passport
  - State identification
  - Driving license
  - Permanent resident card or Green card
  - Government issued photo ID with address listed
  - Utility bill for electricity, water, gas, internet, cable TV
  - Insurance statement (home insurance, health insurance, and so on)
  - Credit card or bank statement
- **Contact details**: A private email address and phone number, verified with
  a one-time password (OTP).

#### Additional requirements for organizations

- **D-U-N-S number**: A unique 9-digit identifier for your organization provided by Dun \& Bradstreet that is used globally to establish your business's legal identity. If your organization does not have one, you can get one at no cost from the Dun \& Bradstreet website.
- **Verified website**: Your organization's website must be verified using Google Search Console.
- **Official organization documents** : The following are examples of what organizations in the United States must provide. The documents required in your location may be different.
  - Any document, notice, or letter either issued by the IRS or stamped by the IRS that states your Organization name. Some examples are CP575, 147C, CP299, 988, 937, 1050, 5822 etc.
  - Forms submitted to the IRS will only be accepted if a copy of the form is available on the IRS website. Some examples are Forms 8871 and 990.
  - Certificate of Business Incorporation issued by the state where you conduct business activities that states your Organization name
  - Your most recent SEC filing (for example, 10-K, 10-Q or 8-K forms) that state the Organization name
  - Business credit reports that state your Organization name from Experian, Equifax, or TransUnion
  - Only for government departments and agencies: an official letter including full name, address and date

## Register your package names

Once verified, you can register your app's package names on the **Packages**
page. The registration process links your app to your verified developer
identity. Complete the following in the Android Developer Console to register:

1. **Enter the package name:** Provide the unique package name you want to register.
2. **Add your key:** Enter the SHA-256 certificate fingerprint from your app's signing key pair. The status will then become ***In review***.
3. **Prove ownership:** For existing package names, you must sign an APK with your private key and upload it. The Android Developer Console provides a snippet to add to the APK's asset folder for this challenge. Once registered, you will be notified by email and the package status in the Developer Console will update to ***Registered***.

> [!NOTE]
> **Note:** Developers who are not eligible to register a package name can request to share it through an appeal-like process by providing proof of ownership and a legitimate reason for use.

## Transfer your package names

You can also transfer package names between developer accounts. Transfers are
managed through the **Settings** page. The following are required to initiate a
transfer:

- **Verified status:** Both the source and target accounts must be verified and in good standing.
- **Registered key:** The package name must have a registered key and be installable.
- **Required info:** You need the target developer ID, order IDs for both accounts, and a stated reason for the transfer.

## Handle duplicate package names

If multiple developers use the same package name, the right to register it is
determined by package claim rules. The following rules aim to allocate the
package name to the developer whose signing key accounts for over 50% of total
known installs:

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
Developer B would need to use another name or apply for an exception_.

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

_Here, no single key has a majority. Developers C and D, with 50 or more
installs, can register the package name. Developer E would need to use a
different namerequest permission.

**First-come, first-served for keys under 50 installs**:

If no keys meet the 50-install threshold, all known keys are eligible for
registration on a first-come, first-served basis. As soon as one developer
registers the package name, the other developers would need to use a different
name for their packages (or request exceptions).

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| F | com.test.3 | 31 | 10 |
| G | com.test.3 | 31 | 10 |

In this scenario, all developers with keys are eligible. Once one developer
registers the package name, the other would need to request permission_.