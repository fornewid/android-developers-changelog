---
title: https://developer.android.com/registered-app-stores/enroll
url: https://developer.android.com/registered-app-stores/enroll
source: md.txt
---

Before you begin the registration process, ensure you have completed the
enrollment prerequisites and prepared your store APK and mandatory policy URLs.

## Submit your package name

After your [interest form](https://support.google.com/android-developer-console/contact/registered_app_store_interest_form) has been accepted and pre-qualifications are
approved, complete the following steps to register your app store:

- In Android Developer Console, select your registered package name.
- Navigate to the **App Store Details** tab.
- In the **Details \& declarations** step, add links to your developer agreement, user support and distribution network URLs, privacy and trust and safety policy URLs, and other applicable declarations.
- In the **Upload APK** step, upload your store's APK file.
  - To pass the malware screening, ensure that your store APK binary exactly matches the current build that you publish across all your external web channels and distribution networks. To maintain an active Registered App Store status after initial approval, you must submit every subsequent version update of your store APK in Android Developer Console for malware screening.
- In the **Submit your app catalog** step, request access to your provisioned storage bucket and confirm the upload of your app catalog.
- In the **Preview and confirm** step, review your submitted metadata, accept the Registered App Store Terms of Service, and pay the registration fee. An admin must submit the payment in Google's payment profile. Ensure that you update the tax ID in the payments profile before paying the fees. After these are complete, click **Submit**.

### Complete store declarations

When you apply in Android Developer Console, you must submit publicly accessible
web links covering mandatory operational areas.

To prepare for your application, ensure that you have the following URLs
available:

| Requirements | Details |
|---|---|
| Privacy policy | A publicly accessible privacy policy for both users and developers (cannot be paywalled). |
| Trust and safety policy | Publicly accessible store Trust \& Safety policies defining baseline developer and app rules. |
| Developer agreement / authorization | A publicly available generic developer agreement establishing direct contractual relationships and authorization to distribute third-party apps. |
| Intellectual property (IP) policy \& dispute process | Defined IP policy and a dedicated dispute submission channel. |
| Illegal content removal channel | A mechanism to report and remove illegal content, PHAs, financial scams, ransomware, or CSAM. |
| Parental control policy | A publicly available page explaining parental control requirements and features for developers. |
| Government request intake process | An operational channel to receive and process government requests (such as legal delisting or takedown orders). |
| Customer support channel | Readily accessible direct contact channel for end users (e.g., a support portal, help desk page, email, live chat, or phone number). |
| Store terms for the installation flow | A publicly accessible link presenting the Terms of Service, Privacy Policy, Trust \& Safety standards, and user support channels, embedded directly within the installation journey. |
| Mobile Application Security Assessment (MASA) certification documentation | The store must achieve MASA certification AL2, from App Defense Alliance (ADA). |

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
| Registered | Your payment is completed, the store is verified, and the registered status is synced to the Android OS. |
| Rejected | Your application has been rejected. You may appeal this decision. |

### Manage registration fees

Active participation as a Registered App Store requires an annual registration
fee of $10,000. You must pay the registration fee to initiate eligibility
review. If registration is successful, after you have completed annual payment
for your Registered App Store your app's status should update to "Registered App
Store" in Android Developer Console.

For developers already enrolled in the program, you will receive a reminder 30
days before your annual renewal date to review your details and submit the
annual renewal fee. Payment must be submitted by an admin in Google's payment
profile. You will update the tax ID in the payments profile before paying any
fees.

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