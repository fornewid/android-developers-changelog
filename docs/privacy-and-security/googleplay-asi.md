---
title: https://developer.android.com/privacy-and-security/googleplay-asi
url: https://developer.android.com/privacy-and-security/googleplay-asi
source: md.txt
---

# App security improvement program

The App Security Improvement program is a service provided to Google Play app developers to improve the security of their apps. The program provides tips and recommendations for building more secure apps and identifies potential security enhancements when your apps are uploaded to Google Play. To date, the program has facilitated developers to fix over 1,000,000 apps on Google Play.

## How it works

Before any app is accepted into Google Play, we scan it for safety and security, including potential security issues. We also continuously re-scan the over one million apps on Google Play for additional threats.

If your app is flagged for a potential security issue, we'll notify you immediately to help you quickly address the issue and help keep your users safe. We'll deliver alerts to you using both email and the Google Play Console, with links to a support page with details about how to improve the app.

Typically, these notifications will include a timeline for delivering the improvement to users as quickly as possible. For some kinds of issues, we may require you to make security improvements in the app before you can publish any more updates to it.

You can confirm that you've fully addressed the issue by uploading the new version of your app to the Google Play Console. Be sure to[increment the version number](https://developer.android.com/studio/publish/versioning)of the fixed app. After a few hours, check the Play Console for the security alert; if it's no longer there, you're all set.  
![](https://developer.android.com/static/images/google/asi_warning.png)

Example of a security improvement alert for an app in the Play Console.

## Get involved

The success of this program rests on our partnership with you---the developers of apps on Google Play---and the security community. We're all responsible for providing safe, secure apps to our users. For feedback or questions, please reach out to us through the[Google Play Developer Help Center](https://support.google.com/googleplay/android-developer/contact/publishing). To report potential security issues in apps, please reach out to us at`security+asi@android.com`.

## Campaigns and remediations

Below are the most recent security issues flagged to developers on Google Play. Vulnerability and remediation details are available in each campaign's support page link.

**Table 1**: Warning campaigns with associated deadline for remediation.

|                           Campaign                           |  Started   |                          Support Page                          |
|--------------------------------------------------------------|------------|----------------------------------------------------------------|
| Exposed Firebase Cloud Messaging Sever Keys                  | 10/12/2021 | [Support page](https://support.google.com/faqs/topic/11015404) |
| Intent Redirection                                           | 5/16/2019  | [Support page](https://support.google.com/faqs/answer/9267555) |
| JavaScript Interface Injection                               | 12/4/2018  | [Support page](https://support.google.com/faqs/answer/9095419) |
| Scheme Hijacking                                             | 11/15/2018 | [Support page](https://support.google.com/faqs/answer/9101196) |
| Cross App Scripting                                          | 10/30/2018 | [Support page](https://support.google.com/faqs/answer/9084685) |
| File-based Cross-Site Scripting                              | 6/5/2018   | [Support page](https://support.google.com/faqs/answer/7668153) |
| SQL Injection                                                | 6/4/2018   | [Support page](https://support.google.com/faqs/answer/7668308) |
| Path Traversal                                               | 9/22/2017  | [Support page](https://support.google.com/faqs/answer/7496913) |
| Insecure Hostname Verification                               | 11/29/2016 | [Support page](https://support.google.com/faqs/answer/7188426) |
| Fragment Injection                                           | 11/29/2016 | [Support page](https://support.google.com/faqs/answer/7188427) |
| Supersonic Ad SDK                                            | 9/28/2016  | [Support page](https://support.google.com/faqs/answer/7126517) |
| Libpng                                                       | 6/16/2016  | [Support page](https://support.google.com/faqs/answer/7011127) |
| Libjpeg-turbo                                                | 6/16/2016  | [Support page](https://support.google.com/faqs/answer/7008337) |
| Vpon Ad SDK                                                  | 6/16/2016  | [Support page](https://support.google.com/faqs/answer/7012047) |
| Airpush Ad SDK                                               | 3/31/2016  | [Support page](https://support.google.com/faqs/answer/6376737) |
| MoPub Ad SDK                                                 | 3/31/2016  | [Support page](https://support.google.com/faqs/answer/6345928) |
| OpenSSL ("logjam" and CVE-2015-3194, CVE-2014-0224)          | 3/31/2016  | [Support page](https://support.google.com/faqs/answer/6376725) |
| TrustManager                                                 | 2/17/2016  | [Support page](https://support.google.com/faqs/answer/6346016) |
| AdMarvel                                                     | 2/8/2016   | [Support page](https://support.google.com/faqs/answer/6345881) |
| Libupup (CVE-2015-8540)                                      | 2/8/2016   | [Support page](https://support.google.com/faqs/answer/6346109) |
| Apache Cordova (CVE-2015-5256, CVE-2015-1835)                | 12/14/2015 | [Support page](https://support.google.com/faqs/answer/6325474) |
| Vitamio Ad SDK                                               | 12/14/2015 | [Support page](https://support.google.com/faqs/answer/6365106) |
| GnuTLS                                                       | 10/13/2015 | [Support page](https://support.google.com/faqs/answer/6344084) |
| Webview SSLErrorHandler                                      | 7/17/2015  | [Support page](https://support.google.com/faqs/answer/7071387) |
| Vungle Ad SDK                                                | 6/29/2015  | [Support page](https://support.google.com/faqs/answer/6313713) |
| Apache Cordova (CVE-2014-3500, CVE-2014-3501, CVE-2014-3502) | 6/29/2015  | [Support page](https://support.google.com/faqs/answer/6325474) |

**Table 2**: Warning-only campaigns (no remediation deadline).

|                 Campaign                 |  Started   |                          Support Page                           |
|------------------------------------------|------------|-----------------------------------------------------------------|
| Implicit PendingIntent                   | 2/22/2022  | [Support page](https://support.google.com/faqs/answer/10437428) |
| Implicit Internal Intent                 | 6/22/2021  | [Support page](https://support.google.com/faqs/answer/10399926) |
| Unsafe Encryption Mode                   | 10/13/2020 | [Support page](https://support.google.com/faqs/answer/10046138) |
| Unsafe Encryption                        | 9/17/2019  | [Support page](https://support.google.com/faqs/answer/9450925)  |
| Zipfile Path Traversal                   | 5/21/2019  | [Support page](https://support.google.com/faqs/answer/9294009)  |
| Embedded Foursquare OAuth Token          | 9/28/2016  | [Support page](https://support.google.com/faqs/answer/7050471)  |
| Embedded Facebook OAuth Token            | 9/28/2016  | [Support page](https://support.google.com/faqs/answer/7126515)  |
| Google Play Billing interception         | 7/28/2016  | [Support page](https://support.google.com/faqs/answer/7054270)  |
| Embedded Google Refresh Token OAuth      | 7/28/2016  | [Support page](https://support.google.com/faqs/answer/7052200)  |
| Developer URL Leaked Credentials         | 6/16/2016  | [Support page](https://support.google.com/faqs/answer/7026406)  |
| Embedded Keystore files                  | 10/2/2014  |                                                                 |
| Amazon Web Services embedded credentials | 6/12/2014  |                                                                 |