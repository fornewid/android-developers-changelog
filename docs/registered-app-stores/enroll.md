---
title: https://developer.android.com/registered-app-stores/enroll
url: https://developer.android.com/registered-app-stores/enroll
source: md.txt
---

Before you begin the registration process, ensure you have completed the
enrollment prerequisites and prepared your store APK and mandatory policy URLs.
Your store package name must be registered through [Android developer
verification](https://developer.android.com/developer-verification) under the same developer account you use to apply, and your
store APK must be signed with a signing key registered for that package.

## Submit your package name

After your [interest form](https://support.google.com/android-developer-console/contact/registered_app_store_interest_form) has been accepted and pre-qualifications are
approved, complete the following steps to register your app store:

- In Android Developer Console, select your registered package name.
- Navigate to the **App Store Details** tab.
- In the **Details and declarations** step, add links to your developer agreement, user support and distribution network URLs, privacy and trust and safety policy URLs, and other applicable declarations.
- In the **Upload APK** step, upload your store's APK file. The APK must be signed with a signing key registered for your store package through Android developer verification. Uploads signed with an unregistered key will be rejected.
  - To pass the malware screening, ensure that your store APK binary exactly matches the current build that you publish across all your external web channels and distribution networks. To maintain an active Registered App Store status after initial approval, you must submit every subsequent version update of your store APK in Android Developer Console for malware screening.
- In the **Submit your app catalog** step, request access to your provisioned storage bucket and confirm the upload of your app catalog.
- In the **Preview and confirm** step, review your submitted metadata, accept the Registered App Store Terms of Service, and pay the registration fee. Payment must be submitted by an admin in Google's payment profile. You will update the tax ID in the payments profile before paying the fees. After these are complete, click **Submit**.

### Complete store declarations

When you apply in Android Developer Console, you must submit publicly accessible
web links covering mandatory operational areas.

To prepare for your application, ensure that you have the following URLs
available:

| Requirements | Details |
|---|---|
| Privacy policy | A publicly accessible privacy policy for both users and developers (cannot be paywalled). |
| Trust and safety policy | Publicly accessible store Trust \& Safety policies defining baseline developer and app rules. |
| Developer agreement / authorization | A publicly accessible generic developer agreement establishing direct contractual relationships and authorization to distribute third-party apps. |
| Intellectual property (IP) policy \& dispute process | Defined IP policy and a dedicated dispute submission channel. |
| Illegal content removal channel | A mechanism to report and remove illegal content, PHAs, financial scams, ransomware, or CSAM. |
| Deceptive practices policy | A publicly accessible policy against deceptive and disruptive practices. |
| Parental control features (user-facing) | A publicly accessible page explaining age assurance and parental control features for users and parents, where mandated by applicable laws, such as verifying users' ages and obtaining parental approval. |
| Parental control requirements (developer-facing) | A publicly accessible page explaining parental control requirements and features for developers, including age assurance and parental controls |
| Government request intake process | An operational channel to receive and process government requests (such as legal delisting or takedown orders). |
| Customer support channel | Readily accessible direct contact channel for end users (e.g., a support portal, help desk page, email, live chat, or phone number). |
| User-facing store terms | A publicly accessible page which contains your Terms of Service, Privacy policy, trust and safety standards, and user support channels. This is shown to users when installing your app store. |
| Mobile Application Security Assessment (MASA) certification documentation | The store must achieve MASA certification AL2, from [App Defense Alliance (ADA)](https://www.appdefensealliance.org/standards/masa). |

Note that the documentation must be submitted in English.

## Submit your app catalog

To maintain ecosystem safety, app stores must provide their entire hosted app
catalog to Google for ongoing malware scanning.

As part of the app store registration process, Google provisions a dedicated,
secure [Google Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) bucket for your store. This bucket serves as
the ingestion point for:

- **Your initial app catalog:** All existing APKs currently published in your store.
- **Ongoing app submissions**: Any new APKs or updates published to your store moving forward.

### Request access to upload your catalog apps

Before you can upload your app catalog, you must provide Google with the account
you will use to access the Google Cloud Storage bucket. The following account
types are supported:

- **Service account (Recommended)** : Best for automated backend ingestion systems, publishing workflows, and script-based uploads. Service accounts don't rely on individual employee credentials. [Learn more about service
  accounts](https://docs.cloud.google.com/iam/docs/service-account-overview).
- **Google account** : Best for manual uploads using the [Google Cloud
  console](https://console.cloud.google.com/).

Complete the following steps to request access:

1. [Provide your store details](https://docs.google.com/forms/d/e/1FAIpQLSfvrwMQmH6ePrCy2hMQY_aLBsyhQa4wTdhYL056le4ea1yi4w/viewform) and the email address of your Google Account or service account.
2. Once processed, we will notify your store's primary contact through email with bucket access details.

### Programmatically upload your catalog apps

For ongoing catalog APK submissions, automate uploads to the Google Cloud
Storage bucket using the Google Cloud CLI or Cloud Storage Client Libraries.

**Option A: Use Google Cloud CLI**   

The Google Cloud CLI (`gcloud`) lets you transfer files between your local
system or servers and the bucket. This is ideal for batch-uploading your
existing app catalog or running bash scripts.

- Authenticate for [the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) using the Google Account or service account you submitted during registration.
- Learn how to [upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects#upload-object-cli)
- Read the [`gcloud storage cp` command reference](https://cloud.google.com/sdk/gcloud/reference/storage/cp)

**Option B: Use Cloud Storage Client Libraries**   

For automated programmatic uploads integrated directly into your backend
ingestion systems or app publishing workflows, use the Google Cloud Storage
Client Libraries. These libraries allow you to upload catalog APKs using
languages like Python, Node.js, Java, and Go.

- [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) to authenticate your backend systems using the Google Account or service account you submitted during registration
- See [code samples for uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects#storage-upload-object-client-libraries)

## Monitor your evaluation status

Submitted applications undergo evaluation. You can monitor the status of your
application in Android Developer Console using the following status badges:

| Draft | Your application is in progress; the application is not yet submitted. |
|---|---|
| In review | The application is submitted and undergoing automated or manual evaluation. |
| Registered | Your payment is completed and the store is registered. Registered App Store capabilities become available on user devices gradually. |
| Rejected | Your application has been rejected. You may appeal this decision. |

### Manage registration fees and status

Active participation as a Registered App Store requires a $10,000 annual
registration fee. Pay this fee to initiate the eligibility review. If
registration is successful, your app's status updates to "Registered App Store"
in Android Developer Console.

Registered App Store capabilities, such as one-tap installs and background
updates, are delivered through Google System Services. These features launch
gradually to users' devices, so some users may see them before others.
Availability depends on the user's country, Android version, and device
management policies. For more information, see the [Google System release
notes](https://support.google.com/product-documentation/answer/14343500).

#### Annual renewal

If you are already enrolled, you receive a reminder 30 days before their annual
renewal date to review details and submit the annual renewal fee.

To complete your renewal:

1. Update your tax ID in the Google Payments profile.
2. Have a payments profile administrator submit the payment.

### Update your app store details

To update your APK with a new version, complete the following steps:

1. Open the Android Developer Console and select your store package name.
2. Navigate to the **App Store Details** tab.
3. Upload your updated store APK file.
4. Update any modified policy URLs or store metadata as needed.
5. Submit the updated store APK for review.

You can also update your declaration URLs. To do so, in the Android Developer
Console:

1. Navigate to your registered app store package name and open the **App Store
   Details** tab.
2. Locate the **Declarations** section and click the edit icon.
3. Update the field (for example, Privacy Policy) with your new URL.
4. Save your changes or resubmit your application if required.

## Get support

If your application to become a Registered App Store is rejected you can file a
formal appeal or contact us through the [Support Form](https://support.google.com/android-developer-console/contact/registered_app_store_enrollment_inquiries).