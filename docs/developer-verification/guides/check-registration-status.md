---
title: https://developer.android.com/developer-verification/guides/check-registration-status
url: https://developer.android.com/developer-verification/guides/check-registration-status
source: md.txt
---

Use the Android Developer Status API to check whether an Android app package
name is registered to a verified developer. If you build software development
tools, IDEs, or automated CI/CD workflows, you can integrate this
server-to-server API to do the following:

- Check whether an app package name is registered to a verified developer
- Validate whether an app's signing certificate SHA-256 fingerprint matches the credentials on file for the registered package name
- Prompt developers within your tool's interface to register unrecognized apps in the Android developer verification program

This API is designed to support various developer workflows:

| Use case | Description | API endpoint |
|---|---|---|
| **Package name eligibility** | Checking whether a package name has already been registered. Returns `REGISTERED` if the package name is linked to any verified developer, otherwise `NOT_REGISTERED`. | `CheckPackageRegistrationStatus` |
| **App has been registered** | Checking if a specific package name and certificate fingerprint pair is registered. Returns `REGISTERED` if the package name and certificate fingerprint pair is registered, `NOT_REGISTERED` if the package name and certificate fingerprint pair is not registered, or `REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT` if the package name is registered with a different certificate fingerprint. | `CheckPackageRegistrationStatus` |

This guide explains how to complete the following tasks:

1. Set up Google Cloud API access and authentication.
2. Verify if an app's package name and public certificate SHA-256 fingerprint pair have been registered with the Android developer verification program by a verified developer, with either the provided public certificate SHA-256 fingerprint, or a different public certificate SHA-256 fingerprint.
3. Handle API registration states in your IDE or developer tool workflow.

## Prerequisites

This document is intended for Android app developers or software development
tool developers. Before you begin, you should have:

- Administrative access to a Google Cloud project.
- A basic understanding of RESTful APIs, JSON, and SHA-256 certificate fingerprints.

You should also be familiar with the following terms:

| Term | Definition |
|---|---|
| **Android developer verification** | Android developer verification is a new requirement designed to link real-world entities (individuals and organizations) with their Android apps. Android will require all apps to be registered by verified developers in order to be installed by users on certified Android devices. |
| **Certificate fingerprint** | The SHA-256 hash of the public certificate used to sign the app. |
| **Registration state** | The status returned by the API for an app's package name or an app's package name and public certificate SHA-256 fingerprint pair. This state dictates the action you must take (for example, `REGISTERED`, `NOT_REGISTERED`). |

## Service endpoint

A [service endpoint](https://google.aip.dev/9#api_service_endpoint)
is a base URL that specifies the network address of an API service. This service
has the following service endpoint, and all URIs are relative to this
service endpoint:

    https://androiddeveloperidstatus.googleapis.com

## Enable the API

To use the Android Developer ID Status API, you must complete the setup steps to
create a project and enable the API.

### Create a Google Cloud project

1. Create a [Google Cloud account](https://console.cloud.google.com/freetrial) if you don't have one.
2. Open the [Google Cloud console](https://console.cloud.google.com/).
3. Create a [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

### Enable the API in your project

1. In the Google Cloud console, go to **APIs \& Services \> Library**.
2. Select your project from the drop-down menu.
3. Search for **Android Developer ID Status API**.
4. Click **Enable**.

## Authenticate

The API supports API key credentials. To obtain an API key:

1. In the Google Cloud console, navigate to **APIs \& Services \> Credentials**.
2. Click **+ Create credentials** and select **API key**.
3. Configure the key and copy it. Use this key in your request headers.

## Check app registration status

You can query the `PackageRegistrationStatus` resource to verify a package name
alone, or check a package name paired with a specific certificate fingerprint.

### Check a package name

To check if an app package name is registered by any verified developer, make an
authenticated `GET` request containing the package name of the Android app (for
example, `com.example.app`) to the `packageRegistrationStatus:check` endpoint
without optional parameters:

**Request:**

    curl -X GET "https://androiddeveloperidstatus.googleapis.com/v1/packages/com.example.app/packageRegistrationStatus:check" \
      -H "X-Goog-Api-Key: [key]"

#### Results

**Response (Registered):**

If the package name is registered, you will receive the following HTTP response
body with the HTTP response code `200`:

    {
      "name": "packages/com.example.app/packageRegistrationStatus",
      "state": "REGISTERED"
    }

Recommended action: Inform the developer that the package name is already
registered.

**Response (Not registered):**

If the package name is not registered, you will receive the following HTTP
response body with the HTTP response code `200`:

    {
      "name": "packages/com.example.app/packageRegistrationStatus",
      "state": "NOT_REGISTERED"
    }

### Verify package name and certificate fingerprint pairs

To check whether an app package name is registered with a specific public
certificate SHA-256 fingerprint, pass the `certificateFingerprint` query
parameter:

**Request:**

    curl -X GET "https://androiddeveloperidstatus.googleapis.com/v1/packages/com.example.app/packageRegistrationStatus:check?certificateFingerprint=d6ac89ed1d0a805aad4b087d06d5f41645b814480b133fbc867ef7498d069e06" \
      -H "X-Goog-Api-Key: [key]"

#### Results

**Response (Registered with matching certificate fingerprint):**

If the package name is registered with the supplied public certificate SHA-256
fingerprint, you will receive the following HTTP response body with the HTTP
response code `200`:

    {
      "name": "packages/com.example.app/packageRegistrationStatus",
      "state": "REGISTERED"
    }

**Response (Registered with different certificate fingerprint):**

If the package name is registered with a different certificate SHA-256
fingerprint to the one supplied, you will receive the following HTTP response
body with the HTTP response code `200`:

    {
      "name": "packages/com.example.app/packageRegistrationStatus",
      "state": "REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT"
    }

**Response (Not registered):**

If the package name is not registered with the supplied public certificate
SHA-256 fingerprint, you will receive the following HTTP response body with the
HTTP response code `200`:

    {
      "name": "packages/com.example.app/packageRegistrationStatus",
      "state": "NOT_REGISTERED"
    }

### Example Java implementation

The following Java class demonstrates how to call the API using Java 11's
standard `HttpClient`.

    import java.io.IOException;
    import java.net.URI;
    import java.net.URLEncoder;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;
    import java.nio.charset.StandardCharsets;

    public class DeveloperIdStatusClient {

      private static final String API_ENDPOINT = "https://androiddeveloperidstatus.googleapis.com";

      public static void main(String[] args) {
        String apiKey = "YOUR_API_KEY";
        String packageName = "com.example.app";
        String certificateFingerprint = "d6ac89ed1d0a805aad4b087d06d5f41645b814480b133fbc867ef7498d069e06";

        try {
          String response = checkPackageRegistrationStatus(apiKey, packageName, certificateFingerprint);
          System.out.println("Response: " + response);
        } catch (IOException | InterruptedException e) {
          e.printStackTrace();
        }
      }

      /**
       *   Checks the registration status of an Android package.
       *
       *   @param apiKey The Google API key for authentication.
       *   @param packageName The fully-qualified Android package name (for example, "com.example.app").
       *   @param certificateFingerprint Optional SHA-256 certificate fingerprint. Pass null or empty to omit.
       *   @return The JSON response string from the API.
       */
      public static String checkPackageRegistrationStatus(
          String apiKey, String packageName, String certificateFingerprint)
          throws IOException, InterruptedException {

        // 1. Build the URL path (accepts dots directly)
        // Format: /v1/packages/{package}/packageRegistrationStatus:check
        String path = String.format("/v1/packages/%s/packageRegistrationStatus:check", packageName);

        // 2. Build query parameters (only certificateFingerprint if provided)
        StringBuilder queryBuilder = new StringBuilder();
        if (certificateFingerprint != null && !certificateFingerprint.isEmpty()) {
          queryBuilder.append("certificateFingerprint=")
              .append(URLEncoder.encode(certificateFingerprint, StandardCharsets.UTF_8));
        }

        String fullUrl = API_ENDPOINT + path;
        if (queryBuilder.length() > 0) {
          fullUrl += "?" + queryBuilder.toString();
        }

        // 3. Create and send the HTTP GET request with API Key header
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(fullUrl))
            .header("Accept", "application/json")
            .header("X-Goog-Api-Key", apiKey)
            .GET()
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
          throw new IOException("Unexpected response code: " + response.statusCode() + ", body: " + response.body());
        }

        return response.body();
      }
    }

## Understand registration states and error handling

When an API request fails, the Android Developer ID Status API returns a
standard Google Cloud JSON error object in the response body. This object
provides a consistent structure for understanding and handling the error.

Example error response:

    {
      "error": {
        "code": 400,
        "message": "Request contains an invalid argument.",
        "status": "INVALID_ARGUMENT"
      }
    }

The error object contains the following key fields:

- `code`: The HTTP status code (for example, `400`, `403`, `500`).
- `message`: A developer-facing English description of the error. This message is not stable and can change, so don't build parsing logic around it.
- `status`: A canonical error code that programmatically identifies the error type (for example, `INVALID_ARGUMENT`, `PERMISSION_DENIED`). Your error handling logic should be built on this stable identifier.

The following table lists the most common errors returned by the API and the
recommended course of action.

| HTTP status | Canonical error code (`status`) | Meaning and common cause | Recommended action | Can be retried? |
|---|---|---|---|---|
| `400` Bad Request | `INVALID_ARGUMENT` | The request was malformed. | Don't retry. Inspect the details field in the error response to identify the specific field violation. Correct the request payload and send it again. | No |
| `401` Unauthorized | `UNAUTHENTICATED` | The access token is missing, expired, or invalid. | Don't retry immediately. Ensure you are using the correct access token or key. | No |
| `403` Forbidden | `PERMISSION_DENIED` | You are authenticated, but your project does not have permission to access the API. The most common cause is that you have not enabled the API in your Google Cloud project. | Don't retry. Verify you are using the correct project ID and that the API is enabled. | No |
| `429` Too Many Requests | `RESOURCE_EXHAUSTED` | You have exceeded the API quota for your project. | Stop sending requests and retry after a delay. Check your project's quotas in the Google Cloud console. | Yes |
| `500` Internal Server Error | `INTERNAL` | An unexpected error occurred on Google's servers. | This is likely a transient issue. Retry the request using an exponential backoff strategy. If the error persists, contact support. | Yes |
| `503` Service Unavailable | `UNAVAILABLE` | The service is temporarily unavailable. | Retry the request using an exponential backoff strategy. | Yes |

## Quota limits

Usage quotas are enforced on a per-project basis to ensure service reliability.

| API method | Default limit (per project) | Notes |
|---|---|---|
| `CheckPackageRegistrationStatus` | 1,000 requests per day | Callers are required to manage internal rate limiting to prevent abuse. |

## Monitor your usage

You can monitor your project's current API usage and see how close you are to
your quota limits directly in the Google Cloud console.

1. Navigate to the [APIs \& Services \> Dashboard](https://console.cloud.google.com/apis/dashboard) page.
2. Select the Android Developer ID Status API.
3. Click the **Quotas** tab.

This dashboard provides a detailed breakdown of your request volume over time.