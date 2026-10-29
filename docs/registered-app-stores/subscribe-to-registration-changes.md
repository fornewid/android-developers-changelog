---
title: https://developer.android.com/registered-app-stores/subscribe-to-registration-changes
url: https://developer.android.com/registered-app-stores/subscribe-to-registration-changes
source: md.txt
---

The Android Developer ID API lets Registered App Stores check if specific
Android apps come from a verified developer and can be installed. It also lets
you retrieve pre-authentication certificates for on-device checks. Google Cloud
hosts this API.

The API provides server-to-server capabilities to verify app status for the
following purposes:

- Enhance app listing quality by deciding on the display of apps with invalid
  statuses.

- Proactively inform developers about issues with apps that have invalid
  statuses.

- Improve user experience by preventing on-device installation problems caused
  by apps failing verification checks.

- Retrieve pre-authentication tokens to enable a fast and seamless
  installation experience for apps that have been registered by a verified
  developer.

To subscribe to app registration status changes, complete the following steps:

- [Review prerequisites](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#review-prerequisites)
- [Configure your Google Cloud project](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#configure-project)
- [Authenticate the API](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#authenticate-the-api)
- [Review common use cases](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#review-common-use-cases)
- [Manage resources and endpoints](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#manage-resources-and-endpoints)
- [Handle errors](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#handle-errors)
- [Review examples](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#review-examples)
- [Review SLOs](https://developer.android.com/registered-app-stores/subscribe-to-registration-changes#review-slos)

## Review prerequisites

Before you begin, you should have:

1. Registered an app store in Android Developer Console.

2. Administrative access to a Google Cloud project.

3. A basic understanding of [RESTful APIs](https://cloud.google.com/discover/what-is-rest-api), [APK structure](https://developer.android.com/topic/performance/reduce-apk-size#apk-structure), [Android
   app signing](https://developer.android.com/studio/publish/app-signing), and [generating SHA-256 digests](https://support.google.com/android-developer-console/answer/16641489)

You should also be familiar with the following terms:

| Term | Definition |
|---|---|
| **Android developer verification** | A new requirement designed to link real-world entities (individuals and organizations) with their Android apps. Android will require all apps to be registered by verified developers in order to be installed by users on certified Android devices. This API is the primary tool to check that an app meets this requirement and can be installed. |
| **App Attention Set (AAS)** | A server-side resource that you create and manage with this API. Think of it as a 'watchlist' of all the apps in your catalog. You add apps to this set to query their installation eligibility status. |
| **Package Certificate ID** | A unique identifier you create by combining an app's package name and the SHA-256 digest of its signing certificate. This ID is the primary key used to reference an app in your App Attention Set. |
| **Installable State** | The status returned by the API for an app in your AAS. This state dictates the action you must take (for example, `INSTALLABLE` versus `NOT_INSTALLABLE`). |
| **Pre-Authentication Certificate** | A short-lived token provided by the API for apps with an `INSTALLABLE` status, valid for approximately one week. Passing this token to the on-device installer lets the app be installed without requiring a live server check, ensuring a faster and smoother user experience. |
| **Update Time** | An ISO 8601 timestamp indicating when an app's Installable State last changed, or when it is time to refresh the Pre-Authentication Certificate to avoid its expiration. To ensure sufficient time to retrieve the new certificate, the system issues a replacement and updates this timestamp approximately three days before expiration. |

## Configure your Google Cloud project

Complete the following steps to access the Android Developer ID API:

### Create a project

1. If you don't already have one, create a Google Cloud account.
2. In your browser, open the Google Cloud console.
3. In the console, create a Google Cloud project.

### Request API access

1. Fill in [the request form](https://docs.google.com/forms/d/e/1FAIpQLSdk8DkJeZsahhzfEdZMb9igu1CxIclSwl3RuWARGy6u7dlvaw/viewform) to
   request access to the Android Developer ID API.

2. Once your request has been reviewed, you will receive an email confirmation.

3. Proceed to enable the API in your Google Cloud project.

### Enable the API

1. In your browser, open the Google Cloud console.
2. In the navigation menu (☰), select **APIs \& Services \> Library**.
3. In the project drop-down menu, select the Google Cloud project in which you want to enable the API.
4. In the **APIs \& Services** search bar, enter **Android Developer ID API**.
5. Enable the API using the following steps:
   1. In the search results, select the API's overview page.
   2. On the overview page, click **Enable**. Google Cloud activates the API for your selected project.

## Authenticate the API

To authenticate your calls to the Android Developer ID API, choose one of the
following mechanisms:

| Option | Use case |
|---|---|
| **OAuth 2.0 service account (recommended)** | Best suited for production backend and server-to-server integrations. Service accounts provide fine-grained access control through OAuth 2.0 scopes and automatic credential rotation. |
| **API key** | Useful for quick prototyping, testing, or development environments. |

### Authenticate using an OAuth 2.0 service account

To authenticate using a service account, you must first create the account

and download its JSON key.

#### Create a service account and download the key

1. In the Google Cloud console, navigate to **IAM \& Admin \> Service Accounts**.

2. Click **+ Create service account**.

3. Enter a **Service account name** (for example,
   `android-developer-id-client`)

   and description, and then click **Create and continue**.
4. Click **Done**.

5. Select the newly created service account in the service accounts list.

6. Click the **Keys** tab and then **Add key \> Create new key \> JSON**.

7. Click **Create** and store the downloaded JSON key file in a secure
   location.

#### OAuth 2.0 scopes

The API defines two OAuth 2.0 scopes:

| Scope URI | Access level | Supported methods |
|---|---|---|
| `https://www.googleapis.com/auth/androiddeveloperid` | Full access (read and write) | All methods: `CreateAppAttentionSet`, `DeleteAppAttentionSet`, `CreatePackageCertificate`, `BatchCreatePackageCertificates`, `DeletePackageCertificate`, `GetAppAttentionSet`, `ListAppAttentionSets`, `GetPackageCertificate`, `ListPackageCertificates` |
| `https://www.googleapis.com/auth/androiddeveloperid.readonly` | Read-only access | `GetAppAttentionSet`, `ListAppAttentionSets`, `GetPackageCertificate`, `ListPackageCertificates` |

#### Use service account credentials to call the API

API requests made using service account credentials must include an OAuth 2.0
Bearer access token in the Authorization HTTP header:

    Authorization: Bearer &lt;ACCESS_TOKEN&gt;

### Authenticate with an API key

To obtain an API key:

1. In Google Cloud Console, navigate to **APIs \& Services** \> **Credentials**.

2. Click **+ Create credentials** at the top of the page and select **API
   key**.

3. (Optional) Under **API restrictions**, restrict the key to the \*\*Android

   Developer ID API\*\* to enhance security.
4. Give the API key a name and click **Create**.

5. A new key will be generated and displayed. Copy this key and store it in a

   secure location. You will use this API key in your requests.

#### Use an API key to call the API

When making requests with an API key, pass it with the `X-Goog-Api-Key` header
or as a query parameter:

    X-Goog-Api-Key: &lt;API_KEY&gt;

## Review common use cases

This API is designed to support the complete lifecycle of app management in

your store. The primary workflows include:

| Use Case | Description | Primary API Endpoints |
|---|---|---|
| **1. Initial Catalog Onboarding** | Adding your entire existing app catalog to the Android Developer ID system for the first time. This is typically a one-off, large-scale operation. | `appAttentionSets.create` `appAttentionSets.batchCreatePackageCertificate` |
| **2. Daily Status Synchronization** | Efficiently retrieving the latest installation eligibility status for all apps in your catalog. This is a crucial daily task to catch any status changes (for example, a developer's verification lapsing). | `appAttentionSets.listPackageCertificates` (using the filter parameter for delta updates) |
| **3. New App Ingestion / Update** | Checking the status of a single new app or an app update as it is submitted to your store. This lets you perform real-time gating at the point of submission. | `appAttentionSets.createPackageCertificate` `appAttentionSets.getPackageCertificate` |

## Manage resources and endpoints

All write operations have a propagation delay of up to 1 minute. Changes made
using the following endpoints may not be immediately reflected in subsequent
read requests: `CreateAppAttentionSet`, `DeleteAppAttentionSet`,
`CreatePackageCertificate`, `BatchCreatePackageCertificates`,
`DeletePackageCertificate`.

### Resource: appAttentionSet

**Resource name:** `androiddeveloperid.googleapis.com/v1/appAttentionSets`

**Description:**

This resource is designed to facilitate the following actions related to App
Attention Sets (AAS):

1. Create new App Attention Sets.

2. Manage existing App Attention Sets by adding or removing package names and

   developer certificates.
3. Retrieve data from App Attention Sets.

Most partners will only need to create and maintain a single

`appAttentionSet` to manage their entire app catalog.

#### HTTP Methods

The following HTTP methods are available for managing App Attention Sets:

##### CreateAppAttentionSet

`POST https://androiddeveloperid.googleapis.com/v1/appAttentionSets`

- **Description:** Create a new attention set.

- **Parameters:**

  - `app_attention_set_id` (string): Identifier of the attention set. Must

  contain only lowercase alphanumeric characters and dashes (-). Maximum

  length is 20 characters. (Required)
  - Example: `app_attention_set_id=mysetid`

**Request Body:**

    {
      "name": ""
    }

**Responses:**

- **200 OK:**

    {
      "name": "appAttentionSets/{app_attention_set_id}"
    }

##### DeleteAppAttentionSet

    DELETE https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}

- **Description:** Deletes an existing App Attention Set. By default, a
  non-empty App Attention Set can't be deleted. Setting force to true
  overwrites this default.

- **Parameters:**

  - `force` (bool): Force delete (Optional)

  - Example: `force=true`

**Responses:**

- **200 OK:** `{}`

##### ListAppAttentionSet

`GET https://androiddeveloperid.googleapis.com/v1/appAttentionSets`

- **Description:** Lists all App Attention Sets under the project.

- **Parameters:**

  - `page_size` (int): The maximum number of app attention sets to return per

  page (maximum 1,000). Default is 1,000. (Optional)
  - Example: `page_size=100`

  - `page_token` (string): A token for retrieving the next page of results.

  (Optional)
  - Example: `page_token=cmcKAhAACgpCCGN1cmx0ZXN0ChFCD2NvbS5zZXAxNy5kZW1vMQpCQkBkNmFjODllZDFkMGE4MDVhYWQ0YjA4N2QwNmQ1ZjQxNjQ1YjgxNDQ4MGIxMzNmYmM4NjdlZjc0OThkMDY5ZTA2`

**Responses:**

- **200 OK:**

    {
      "app_attention_sets": [
        {
          "name": "appAttentionSets/{app_attention_set_id#1}",
          "packageCertificatesCount": "40000"
        }
      ]
    }

##### GetAppAttentionSet

    GET https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}

- **Description:** Get a specific App Attention Set.

**Responses:**

- **200 OK:**

    {
      "name": "appAttentionSets/{app_attention_set_id}",
      "packageCertificatesCount": "40000"
    }

### Resource: packageCertificate

**Resource name:**

    androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates

**Description:**

This resource is designed to facilitate the following actions related to

package certificates within an App Attention Set (AAS):

1. Add package name and SHA-256 certificate fingerprints to an AAS.

2. Retrieve the installation eligibility status and pre-authentication tokens

   for specific apps.
3. List or batch manage package certificates to synchronize catalog statuses.

#### HTTP Methods

The following HTTP methods are available for managing package certificates
within an App Attention Set:

##### CreatePackageCertificate

    POST https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates

- **Description:** Add package name and SHA-256 certificate fingerprint to the
  App Attention Set.

- **Parameters:**

  - `package_certificate_id` (string): Concatenation of the package name and

  the SHA-256 certificate fingerprint. Format: Package name + `-` (dash) +

  lower case hex representation of the SHA-256 certificate fingerprint (64

  characters). (Required)
  - Example: `For com.sep17.demo2:
    package_certificate_id=com.sep17.demo2-d6ac89ed1d0a805aad4b087d06d5f41645b814480b133fbc867ef7498d069e06`

**Request Body:**

    {
      "name": ""
    }

**Responses:**

- **200 OK:**

    {
      "name": "appAttentionSets/{app_attention_set_id}/packageCertificates/{package_certificates_id}",
      "app": "{package_name}",
      "installableState": "{installable_state}",
      "preAuthCertificate": {
        "certificate": "{pre-authentication certificate}",
        "expireTime": "{pre-authentication certificate expiration time}"
      },
      "updateTime": "{update time}"
    }

##### BatchCreatePackageCertificates

    POST https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates:batchCreate

- **Description:** Adds multiple package names and SHA-256 certificate fingerprints to an App Attention Set. An App Attention Set can have a maximum of 4,000,000 package-certificate pairs. Maximum 40,000 package-certificate pairs per call.

**Request Body:**

    {
      "requests": [
        {
          "package_certificate_id": "{package_certificate_id#1}"
        }
      ]
    }

**Responses:**

- **200 OK:**

    {
      "packageCertificates": [
        {
          "name": "appAttentionSets/{app_attention_set_id}/packageCertificates/{package_certificate_id#1}",
          "app": "{package_name#1}",
          "updateTime": "{update time}"
        }
      ]
    }

##### DeletePackageCertificate

    DELETE https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates/{package_certificate_id}

- **Description:** Deletes specific package name and SHA-256 certificate fingerprint from an App Attention Set.

**Responses:**

- **200 OK:** `{}`

##### ListPackageCertificates

    GET https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates

- **Description:** Retrieve data for all apps in an App Attention Set.

- **Parameters:**

  - `page_size` (int): The maximum number of apps to return per page (maximum

  100,000). Default is 1,000. (Optional)
  - Example: `page_size=100`

  - `page_token` (string): A token for retrieving the next page of results.

  (Optional)
  - Example:
    `page_token=cmcKAhAACgpCCGN1cmx0ZXN0ChFCD2NvbS5zZXAxNy5kZW1vMQpCQkBkNmFjODllZDFkMGE4MDVhYWQ0YjA4N2QwNmQ1ZjQxNjQ1YjgxNDQ4MGIxMzNmYmM4NjdlZjc0OThkMDY5ZTA2`

  - `filter` (string): Show only the apps with a specific
    `installable_state`

  or `update_time`. (Optional)
  - Example: `filter=installable_state%3AINSTALLABLE_PRE_AUTH_CERTIFICATE_AVAILABLE`

##### Installable States

| installableState | Meaning | Recommended OEM Action |
|---|---|---|
| `INSTALLABLE_PRE_AUTH_CERTIFICATE_AVAILABLE` | The app has been registered by a verified developer and can be installed. | Proceed with installation. Provide the `preAuthCertificate` to the on-device installer. |
| `INSTALLABLE_PRE_AUTH_CERTIFICATE_UNAVAILABLE` | The app has been registered by a verified developer and can be installed. The `preAuthCertificate` is currently unavailable due to a transient issue. | Proceed with installation. The device will perform a real-time online check since the `preAuthCertificate` can't be provided to the on-device installer. |
| `NOT_INSTALLABLE` | The app has not been registered by a verified developer or has been blocked from being installed on GMS Android devices. | Block installation. Hide the app from your store or disable the install button. Notify the app's developer that they must complete Android developer verification. |

##### GetPackageCertificate

    GET https://androiddeveloperid.googleapis.com/v1/appAttentionSets/{app_attention_set_id}/packageCertificates/{package_certificate_id}

- **Description:** Retrieve data for a single app.

**Responses:**

- **200 OK:**

    {
      "name": "appAttentionSets/{app_attention_set_id}/packageCertificates/{package_certificate_id}",
      "app": "{package_name}",
      "installableState": "{installable_state}",
      "preAuthCertificate": {
        "certificate": "{pre-authentication certificate}",
        "expireTime": "{pre-authentication certificate expiration time}"
      },
      "updateTime": "{update time}"
    }

## Handle errors

The Android Developer ID API uses standard Google Cloud error structures.

Review the following sections to understand the error model and how to resolve
common errors you might encounter.

### Error Model

When an API request fails, the Android Developer ID API returns a standard
Google Cloud JSON error object in the response body.

Example Error Response:

    {
      "error": {
        "code": 400,
        "message": "Invalid package certificate name: 'invalid-id'...",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.BadRequest",
            "fieldViolations": [
              {
                "field": "packageCertificate.name",
                "description": "Name must be in the format 'sha256_hex_of_cert_bytes:package_name'"
              }
            ]
          }
        ]
      }
    }

### Common Errors and Resolutions

| HTTP Status | gRPC Status (status) | Recommended Action |
|---|---|---|
| **400 Bad Request** | `INVALID_ARGUMENT` | Don't retry. Inspect the `details` field to identify the specific violation. |
| **401 Unauthorized** | `UNAUTHENTICATED` | Don't retry immediately. Ensure you are using the correct access token or key. |
| **403 Forbidden** | `PERMISSION_DENIED` | Don't retry. Verify your project is allowed. |
| **404 Not Found** | `NOT_FOUND` | Don't retry. Check that the resource name is correct. |
| **429 Too Many Requests** | `RESOURCE_EXHAUSTED` | Stop sending requests and retry after a delay. Check quotas. |
| **500 Internal Server Error** | `INTERNAL` | Retry the request using an exponential backoff strategy. |
| **503 Service Unavailable** | `UNAVAILABLE` | Retry the request using an exponential backoff strategy. |

## Review examples

This section contains practical examples of how to interact with the API
endpoints to create attention sets and list package certificates.

### Example: CreateAppAttentionSet

    curl -X POST -H "X-Goog-Api-Key: [key]" -H "Content-Type: application/json" \
    "https://androiddeveloperid.googleapis.com/v1/appAttentionSets?app_attention_set_id=curltest" \
    -d '{"name": ""}'

**Success Response:**

    {
      "name": "appAttentionSets/curltest"
    }

### Example: ListPackageCertificates

    curl -X GET -H "X-Goog-Api-Key: [key]" -H "Content-Type: application/json" \
    "https://androiddeveloperid.googleapis.com/v1/appAttentionSets/curltest/packageCertificates?page_size=100"

**Success Response:**

    {
      "packageCertificates": [
        {
          "name": "appAttentionSets/curltest/packageCertificates/com.sep17.demo2-d6ac89ed1d0a805aad4b087d06d5f41645b814480b133fbc867ef7498d069e06",
          "app": "com.sep17.demo2",
          "installableState": "INSTALLABLE",
          "preAuthCertificate": {
            "certificate": "CAESTwoPY2...",
            "expireTime": "2026-10-09T13:00:00Z"
          },
          "updateTime": "2026-09-29T13:00:00Z"
        }
      ]
    }

## Review SLOs

The API has an availability SLO of 99% and the following P99 thresholds for

the most common API methods:

- `CreatePackageCertificate`: P99 ≤ 2 seconds

- `GetPackageCertificate`: P99 ≤ 2 seconds

- `ListPackageCertificates`: P99 ≤ 60 seconds

- `BatchCreatePackageCertificates`: P99 ≤ 60 seconds

## See also

- [Overview of Registered App Stores](https://developer.android.com/registered-app-stores/overview)
- [Enroll as a Registered App Store](https://developer.android.com/registered-app-stores/enroll)