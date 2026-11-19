---
title: https://developer.android.com/developer-verification/guides/distributor-resources
url: https://developer.android.com/developer-verification/guides/distributor-resources
source: md.txt
---

> Documentation index: https://developer.android.com/developer-verification/guides/llms.txt

As an app distributor, you play a critical role in maintaining a safe and
trusted Android ecosystem. Android developer verification requires that apps
distributed on [certified Android devices](https://developer.android.com/developer-verification/guides/faq.md.txt#versions) are registered by a verified
developer.

On September 30, 2026, these protections went live for users in Brazil,
Indonesia, Singapore, and Thailand across [selected participating stores](https://developer.android.com/developer-verification/guides.md.txt#locations),
and will gradually expand globally for all app installations on certified
Android devices in 2027. This includes all installation sources and third-party
stores.

Close collaboration with the participating stores during the initial rollout
highlighted four effective practices for minimizing developer and user friction
and ensuring a smooth transition before verification requirements take effect:

- **Proactively encourage developers to register their apps early** : Early, multi-touch outreach campaigns, combining [email reminders](https://developer.android.com/developer-verification/guides/distributor-resources.md.txt#email-templates), developer portal [banners](https://developer.android.com/developer-verification/guides/distributor-resources.md.txt#banner-samples), and localized [step-by-step guides](https://developer.android.com/developer-verification/guides.md.txt), drive significantly higher package name registration coverage.
- **Audit your catalog with the Android Developer ID Status API** : Using the [Android Developer ID Status API](https://developer.android.com/developer-verification/guides/check-registration-status.md.txt) to check which apps (defined as a package name and signing certificate SHA-256 fingerprints) in your app catalog are already registered lets you measure baseline readiness, prioritize outreach to unregistered developers, and flag unregistered signing keys during app submission.
- **Streamline registration with the Android Developer Console API** : Integrating the [Android Developer Console API](https://developer.android.com/developer-verification/guides/developer-console-api.md.txt) directly into your developer portal or publishing workflow removes context-switching. With OAuth 2.0 delegation, you can register apps on behalf of your developers, in their account. This API also lets you verify key ownership for store-managed signing keys.
- **Manage unverified app delivery** : If your store chooses to permit the listing of unregistered apps, you may let users know when an app is unregistered and that installing or updating it on a certified Android device will require the user to enable the on-device [advanced flow](https://developer.android.com/developer-verification/guides/faq.md.txt#advanced-flow).

## Timeline

Developer verification will start to roll out globally in January 2027 with
seven participating stores (Google Play, Galaxy Store, Honor, Oppo, Xiaomi,
Transsion, and Vivo). User protections will continue to gradually expand to all
countries to cover all installation sources on certified Android devices, and
will be in effect for other stores by March 2027.

## Prepare for the Android developer verification rollout

Use the following milestones to plan your technical integrations and developer
outreach:

| Timeframe | Recommended actions |
|---|---|
| **November-December 2026** (T-90 days) | Run an initial catalog audit using the Android Developer ID Status API. |
| **November-December 2026** (T-90 days) | Add an advance notice banner in your developer portal. |
| **November-December 2026** (T-90 days) | Send an early notice email with each developer's unregistered package list. |
| **January 2027** (T-60 days) | Add automated checks to your APK/AAB ingestion pipeline (flagging unregistered keys on upload) using the Android Developer ID Status API. |
| **January 2027** (T-60 days) | Send a 60-day email reminder. |
| **February 2027** (T-30 days) | Integrate with the Android Developer Console API OAuth 2.0 workflow to streamline app registration and automate proof of ownership verification for store-managed keys. |
| **February 2027** (T-30 days) | Send a 30-day follow-up email. |
| **February 2027** (T-30 days) | Send a final 7-day notice to remaining unregistered developers. |
| **March 1, 2027** (Target readiness) | Update your developer portal banner to reflect that Android developer verification is in effect. |

## Support your developers

Early outreach gives your developers time to verify their identity and register
their package names and signing keys before enforcement takes effect, preventing
install interruptions for your users. Use the sample emails and developer portal
banners below as a starting point. Choose the ones that work for your audience,
translate and adapt them to fit your store's workflows and communication
channels, and add additional resources if you think they would be helpful.

### Email templates

We recommend sending emails to your developers, reminding them of the upcoming
rollout of Android developer verification, and how to get ready for it. This
could include a brief overview of the program with links to relevant resources
and a call to action.

To make this easier for your developers, you can include the list of apps that
are not registered in the email or let them know all their apps are registered,
so they have a clear next step. See [Check app registration status with the
Android Developer ID Status API](https://developer.android.com/developer-verification/guides/distributor-resources#check-app-registration-status-with-the-android-developer-id-status-api) below for more details on how to do this.

We suggest sending several emails, for example 90, 60, 30, and 7 days before the
Android developer verification user protections will be in effect on March 1,
2027.

Below are sample emails that you can use as a reference.

#### Early notice email template (for example, early December)

> **Subject:** Complete Android developer verification by March 1, 2027
>
> Hi,
>
> In line with the [recent Android announcements](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), our store is making
> changes to support [Android developer verification](https://developer.android.com/developer-verification). To raise Android
> security and enhance user protection, Google will only allow the installation
> of apps that are registered by verified developers on [certified Android
> devices](https://developer.android.com/developer-verification/guides/faq#versions), unless the user has enabled the [advanced flow](https://developer.android.com/developer-verification/guides/faq.md.txt#advanced-flow). This will
> start rolling out globally from January, over several months.
>
> All developers should verify their identity and register their apps by
> March 1, 2027 to ensure uninterrupted distribution.
>
> \[*Note to App Distributors: Choose one option below depending on whether your
> developer portal integrates with the Android Developer Console API*\]
>
> \[*Option 1 -- Standard workflow* \] Please ensure that all your apps and
> signing keys are registered by following [these steps](https://developer.android.com/developer-verification/guides.md.txt#you-need).
>
> \[*Option 2 -- With Android Developer Console API integration*\] Register your
> apps directly in our developer portal:
>
> 1. Link your Android Developer Console account \[Link to your OAuth 2.0 flow\].
> 2. Register your apps and signing keys. \[If your store manages app signing keys, let developers know you will register their package names and verify key ownership automatically.\]
>
> \[*Note to App Distributors: Using the Developer ID Status API you can check
> in advance which apps are not registered and list these here for the
> developer*\]
>
> **Support and resources**
>
> For detailed instructions and technical guidance, please check out:
>
> - [developer.android.com/developer-verification](https://developer.android.com/developer-verification): For guides and technical documentation.
> - [Android Developer Console Help Center](https://support.google.com/android-developer-console): For detailed support on navigating the Android Developer Console and [asking for help](https://support.google.com/android-developer-console/contact/developer_verification_issue) with specific issues.
> - [Play Console Help Center](https://support.google.com/googleplay/android-developer#topic=16689288): For documentation on Play Console verification and case-specific support.
>
> We value your partnership in keeping the Android ecosystem safe for everyone
> and encourage you to begin the verification process as soon as possible to
> ensure a seamless experience for your users.

#### Follow-up notice email template (for example, February 1, 2027)

> **Subject:** Reminder: 30 days left to complete Android developer verification
> by March 1, 2027
>
> Hi,
>
> In line with the [recent Android announcements](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), our store is making
> changes to support [Android developer verification](https://developer.android.com/developer-verification). To raise Android
> security and enhance user protection, Google will only allow the installation
> of apps that are registered by verified developers on [certified Android
> devices](https://developer.android.com/developer-verification/guides/faq#versions), unless the user has enabled the [advanced flow](https://developer.android.com/developer-verification/guides/faq.md.txt#advanced-flow).
>
> \[*Note to App Distributors: Choose one option below depending on whether your
> developer portal integrates with the Android Developer Console API*\]
>
> \[*Option 1 -- Standard workflow* \] To ensure uninterrupted distribution,
> follow [these steps](https://developer.android.com/developer-verification/guides.md.txt#you-need) to register all your apps and signing keys by
> March 1, 2027.
>
> \[*Option 2 -- With Android Developer Console API integration*\] Register your
> apps directly in our developer portal:
>
> 1. Link your Android Developer Console account \[Link to your OAuth 2.0 flow\].
> 2. Register your apps and signing keys. \[If your store manages app signing keys, let developers know you will register their package names and verify key ownership automatically.\]
>
> \[*Note to App Distributors: Using the Developer ID Status API you can check
> in advance which apps are not registered and list these here for the
> developer*\]
>
> For more information, please check out:
>
> - [developer.android.com/developer-verification](https://developer.android.com/developer-verification): For guides and technical documentation.
> - [Android Developer Console Help Center](https://support.google.com/android-developer-console): For detailed support on navigating the Android Developer Console and [asking for help](https://support.google.com/android-developer-console/contact/developer_verification_issue) with specific issues.
> - [Play Console Help Center](https://support.google.com/googleplay/android-developer#topic=16689288): For documentation on Play Console verification and case-specific support.
>
> We value your partnership in keeping the Android ecosystem safe for everyone
> and encourage you to complete the verification process as soon as possible to
> ensure a seamless experience for your users.

### Banner samples

Example banners that you can integrate into your developer portal to notify
developers about the upcoming Android developer verification rollout and
requirements. Consider showing each developer the list of apps that they have
not registered. See [Check app registration status with the Android Developer ID
Status API](https://developer.android.com/developer-verification/guides/distributor-resources#check-app-registration-status-with-the-android-developer-id-status-api) below for details on how to do this.

#### Advance notice banner

> The following apps are not registered with
> [Android developer verification](https://developer.android.com/developer-verification).
>
> \[*Option 1 -- Standard workflow* \] To ensure uninterrupted distribution,
> follow [these steps](https://developer.android.com/developer-verification/guides.md.txt#you-need) to register your apps and signing keys by DATE.
>
> \[*Option 2 -- With Android Developer Console API integration*\] To ensure
> uninterrupted distribution, register your apps directly in our developer
> portal by DATE:
>
> 1. Link your Android Developer Console account \[Link to your OAuth 2.0 flow\].
> 2. Register your apps and signing keys. \[If your store manages app signing keys, let developers know you will register their package names and verify key ownership automatically.\]
>
> \[List of apps that are not registered\]

#### Active requirement banner

> All Android apps must now be registered by a verified developer in order to be
> installable on [certified Android devices](https://developer.android.com/developer-verification/guides/faq.md.txt#versions), unless the user has enabled the
> [advanced flow](https://developer.android.com/developer-verification/guides/faq.md.txt#advanced-flow).
>
> \[*Option 1 -- Standard workflow* \] Follow [these steps](https://developer.android.com/developer-verification/guides.md.txt#you-need) to verify your
> identity and register your apps.
>
> \[*Option 2 -- With Android Developer Console API integration*\] Register your
> apps directly in our developer portal:
>
> 1. Link your Android Developer Console account \[Link to your OAuth 2.0 flow\].
> 2. Register your apps and signing keys. \[If your store manages app signing keys, let developers know you will register their package names and verify key ownership automatically.\]
>
> \[List of apps that are not registered\]

#### No action needed banner

> Great news! All the apps you distribute on our store are currently registered
> with [Android developer verification](https://developer.android.com/developer-verification). No further action is needed from
> you. Please make sure you register any new apps or signing keys you use.

## Automate your workflows with APIs

APIs are available to help you audit your app catalog and streamline app package
name and signing key registration.

### Check app registration status with the Android Developer ID Status API

Use this API to programmatically check whether package names and signing
certificate SHA-256 fingerprints in your store catalog are registered to a
verified developer.

- **When to use it:**
  - Catalog preparation: Audit your existing catalog immediately to measure baseline readiness and prioritize compliance outreach ahead of Android developer verification requirements.
  - Ongoing app submissions and updates: Run automated checks whenever a developer submits a new app, uploads an app update, or rotates signing keys. We recommend doing this before publishing the app so you can take action if an app is not registered.
- **Where to integrate:** Add status checks to your catalog backend batch jobs, APK or AAB ingestion pipelines, and developer portal app management views.
- **How to use it:** Check app package name and signing key registration states to segment outreach lists, flag unregistered keys during build upload, and surface verification status badges in your portal. See [Check
  app registration status](https://developer.android.com/developer-verification/guides/check-registration-status).

### Register package names with the Android Developer Console API

Use this API to manage package name and signing key registration on behalf of
developers.

- **When to use it:**
  - Developer onboarding and app publishing: Prompt developers to link their Android Developer Console account and register new or existing app package names and signing keys.
  - Catalog compliance and store-managed signing: Proactively register existing apps that use store-managed signing certificates.
- **Where to integrate:** Embed this workflow into your developer onboarding flow, account settings page, app submission wizard, and store-managed app signing service.
- **How to use it:** Let developers authorize your store with OAuth 2.0 to check developer verification status, register package names and signing keys, and automate key ownership verification without leaving your portal. See [Register package names with the Android Developer Console API](https://developer.android.com/developer-verification/guides/developer-console-api.md.txt).