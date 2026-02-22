---
title: https://developer.android.com/privacy-and-security/certificate-transparency-policy
url: https://developer.android.com/privacy-and-security/certificate-transparency-policy
source: md.txt
---

# Android Certificate Transparency Policy

*Please direct any questions about this Policy to the CT Policy forum:[ct-policy@chromium.org](https://groups.google.com/a/chromium.org/forum/#!forum/ct-policy)*

When a connection's Transport Layer Security (TLS) certificate is validated in an app that[opts-in to Certificate Transparency](https://developer.android.com/privacy-and-security/security-config#CertificateTransparencySummary), it is evaluated for compliance against the Android Certificate Transparency (CT) Policy. Certificates that are accompanied by Signed Certificate Timestamp (SCTs) that satisfy this Policy are said to be CT Compliant.

CT Compliance is achieved by a certificate and set of accompanying SCTs meeting a set of technical requirements enforced by popular TLS libraries (including the built-in Conscrypt) during certificate validation, which are defined in this Policy.

## CT Log States

CT Compliance in Android is determined by evaluating SCTs from CT logs and ensuring that these logs are in the correct state(s) at time of check. The set of possible states a CT log can be in is:

- `Pending`
- `Qualified`
- `Usable`
- `ReadOnly`
- `Retired`
- `Rejected`

In order to assist with understanding the requirements for CT compliance in Android, the definition of these states, the requirements of Logs in each state, as well as how these states impact Android behavior are described in detail in the[CT Log Lifecycle Explainer](https://googlechrome.github.io/CertificateTransparency/log_states.html)of Chrome's documentation.

## CT Compliant Certificates

A TLS certificate is CT*Compliant*if it is accompanied by a set of SCTs that satisfies at least one of the criteria defined later, depending on how the SCTs are delivered to Android. In CT-enforcing apps of Android, all publicly-trusted TLS certificates are required to be CT Compliant to successfully validate; however, certificates that are not logged to CT or have insufficient SCTs are not considered to be mis-issued.

When evaluating a certificate for CT Compliance, Android considers several factors including how many SCTs are present, who operates the CT Log that issued the SCT, and what state the CT Log that issued the SCT was in, both at the time the certificate is being validated, and at the time the SCT was created by the CT Log.

Depending on how the SCTs are presented to Android, CT compliance can be achieved by meeting one of the following criteria:

**Embedded SCTs:**

1. At least one Embedded SCT from a CT Log that was`Qualified`,`Usable`, or`ReadOnly`at the time of check; and
2. There are Embedded SCTs from at least N distinct CT Logs that were`Qualified`,`Usable`,`ReadOnly`, or`Retired`at the time of check, where N is defined in the following table; and
3. Among the SCTs satisfying requirement 2, at least two SCTs must be issued from distinct CT Log Operators as recognized by Android; and
4. Among the SCTs satisfying requirement 2, at least one SCT must be issued from a log recognized by Android as being[RFC 6962-compliant](https://datatracker.ietf.org/doc/html/rfc6962).

| Certificate Lifetime | Number of SCTs from distinct CT Logs |
|----------------------|--------------------------------------|
| \<= 180 days         | 2                                    |
| \> 180 days          | 3                                    |

**SCTs delivered via OCSP or TLS:**

1. At least two SCTs from a CT Log that was`Qualified`,`Usable`, or`ReadOnly`at the time of check; and
2. Among the SCTs satisfying requirement 1, at least two SCTs must be issued from distinct CT Log Operators as recognized by Android; and
3. Among the SCTs satisfying requirement 1, at least one SCT must be issued from a CT log recognized by Android as being RFC6962-compliant.

For both embedded SCTs and those delivered using OCSP or TLS, Log Operator uniqueness is defined as having separate entries within the operators section of the[log list](https://developer.android.com/privacy-and-security/certificate-transparency-policy#log-list).

In the rare situation that a CT Log changes operators during its lifetime, CT logs optionally contain an list of`previous_operators`, accompanied by the final timestamp that this log was operated by the previous operator. To prevent log operator changes from breaking existing certificates, each SCT's log operator is determined to be the operator at the time of SCT issuance, by comparing the SCT timestamp against the`previous_operators`timestamps, if present.

**Important notes**

So long as one of the preceding CT Compliance criteria is met by some combination of SCTs presented in the handshake, additional SCTs, regardless of the status of the SCT, won't affect a certificate's CT Compliance status positively or negatively.

In order to contribute to a certificate's CT Compliance, an SCT must have been issued before the Log's`Retired`timestamp, if one exists. Android uses the earliest SCT among all SCTs presented to evaluate CT compliance against CT Log`Retired`timestamps. This accounts for edge cases in which a CT Log becomes Retired during the process of submitting certificate logging requests.

"Embedded SCT" means an SCT delivered using the`SignedCertificateTimestampList`X.509v3 extension within the certificate itself. Many TLS servers don't support OCSP Stapling or the TLS extension, so CAs should be prepared to embed SCTs into issued certificates to ensure successful validation or EV treatment in Android.

## How CT Logs are added to Android

The criteria for how CT Logs can become`Qualified`, as well as what circumstances can cause them to become`Retired`, can be found in the Chrome CT[Log Policy](https://googlechrome.github.io/CertificateTransparency/log_policy.html).

## CT Enforcement Timeout

Every day, Google publishes a new CT Log list that contains a fresh`log_list_timestamp`. Once a day, Android devices will attempt to download the latest version of this list for verification purposes. At any given time, if no log list is available on the device or if the timestamp of the log list is older than 70 days, then CT enforcement will be disabled. This timeout provides a critical assurance to the CT ecosystem that new CT Logs are able to safely transition to Usable within a fixed amount of time after becoming`Qualified`.

## Android log list

The Android log list is published in[log_list.json](https://www.gstatic.com/android/certificate_transparency/v2/log_list.json), which is updated daily. This log list is offered without a stable API, SLA or availability guarantees.

Android makes its CT log list available for the purposes of certificate submitters (such as certification authorities) and CT monitors and auditors wishing to remain compatible with, or investigate the contents of, the CT and WebPKI ecosystems.
| **Caution:** The Android CT log list may not be used to facilitate CT enforcement in TLS clients other than the Android platform itself without explicit written permission from the Android CT team.

Unauthorized reliance on the Android CT log list endangers not just your users, but Android users and the CT ecosystem as a whole. If you are exploring adding CT enforcement into your app, use a[mechanism supported by the Android platform](https://developer.android.com/privacy-and-security/security-config#CertificateTransparencySummary).

Using the Android CT log list out of line with this policy is done at your own risk, and may result in breakage of your application or library. Android must be able to make changes to the CT log list in response to incidents in the CT ecosystem so as to maintain the safety and security of Android users. Android may take steps to ensure that third-party dependencies on the CT log list don't risk Android's ability to respond to such incidents, including unannounced changes to the log list to disrupt unauthorized use.