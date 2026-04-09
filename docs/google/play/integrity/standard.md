---
title: https://developer.android.com/google/play/integrity/standard
url: https://developer.android.com/google/play/integrity/standard
source: md.txt
---

This page describes making standard API requests for integrity verdicts, which are supported on Android 5.0 (API level 21) or higher. You can make a standard API request for an integrity verdict whenever your app is making a server call to check whether the interaction is genuine.

## Overview

![](https://developer.android.com/static/images/google/play/integrity/play-integrity-api-standard.svg)**Figure 1.**Sequence diagram that shows the high-level design of the Play Integrity API.

A standard request consists of two parts:

- **Prepare the integrity token provider (one off)**: You need to call the Integrity API to prepare the integrity token provider well before you need to obtain the integrity verdict. For example, you can do this when your app launches or in the background before the integrity verdict is needed.
- **Request an integrity token (on demand)**: Whenever your app makes a server request that you want to check is genuine, you request an integrity token and send it to your app's backend server for decryption and verification. Then your backend server can determine how to act.

Prepare the integrity token provider (one off):

1. Your app calls the integrity token provider with your Google Cloud project number.
2. Your app holds the integrity token provider in memory for further attestation check calls.

Request an integrity token (on demand):

1. For the user action which needs to be protected, your app computes the hash (using any suitable hash algorithm such as SHA256) of the request to be made.
2. Your app requests an integrity token, passing the request hash.
3. Your app receives the signed and encrypted integrity token from the Play Integrity API.
4. Your app passes the integrity token to your app's backend.
5. Your app's backend sends the token to a Google Play server. The Google Play server decrypts and verifies the verdict, returning the results to your app's backend.
6. Your app's backend determines how to proceed, based on the signals contained in the token payload.
7. Your app's backend sends the decision outcomes to your app.

## Prepare the integrity token provider (one off)

Before you make a standard request for an integrity verdict from Google Play, you must prepare (or "warm up") the integrity token provider. This allows Google Play to smartly cache partial attestation information on the device in order to decrease the latency on the critical path when you make a request for an integrity verdict. Preparing the token provider again is a way to repeat less resource heavy integrity checks which will make the next integrity verdict that you request more up to date.

You might prepare the integrity token provider:

- When your app launches (i.e. on cold start up). Preparing the token provider is asynchronous and so will not impact the start up time. This option would work well if you plan to make an integrity verdict request shortly after the app is launched, for example when a user signs in or a player joins a game.
- When your app is opened (i.e. on warm start up). However, note that each app instance can only prepare the integrity token up to 5 times per minute.
- At any time in the background when you want to prepare the token in advance of an integrity verdict request.

To prepare the integrity token provider do the following:

1. Create a`StandardIntegrityManager`, as shown in the following examples.
2. Construct a`PrepareIntegrityTokenRequest`, supplying the Google Cloud project number through the`setCloudProjectNumber()`method.
3. Use the manager to call`prepareIntegrityToken()`, supplying the`PrepareIntegrityTokenRequest`.

**Tip:** Typical warm up latency is a few seconds and the majority of all warm ups are under 10s. However, warming up invokes a server call so a timeout that accommodates a long tail of requests is recommended (e.g. of 1 minute).  

### Java

```java
import com.google.android.gms.tasks.Task;

// Create an instance of a manager.
StandardIntegrityManager standardIntegrityManager =
    IntegrityManagerFactory.createStandard(applicationContext);

StandardIntegrityTokenProvider integrityTokenProvider;
long cloudProjectNumber = ...;

// Prepare integrity token. Can be called once in a while to keep internal
// state fresh.
standardIntegrityManager.prepareIntegrityToken(
    PrepareIntegrityTokenRequest.builder()
        .setCloudProjectNumber(cloudProjectNumber)
        .build())
    .addOnSuccessListener(tokenProvider -> {
        integrityTokenProvider = tokenProvider;
    })
    .addOnFailureListener(exception -> handleError(exception));
```

### Unity

```c#
IEnumerator PrepareIntegrityTokenCoroutine() {
    long cloudProjectNumber = ...;

    // Create an instance of a standard integrity manager.
    var standardIntegrityManager = new StandardIntegrityManager();

    // Request the token provider.
    var integrityTokenProviderOperation =
      standardIntegrityManager.PrepareIntegrityToken(
        new PrepareIntegrityTokenRequest(cloudProjectNumber));

    // Wait for PlayAsyncOperation to complete.
    yield return integrityTokenProviderOperation;

    // Check the resulting https://developer.android.com/reference/unity/namespace/Google/Play/Integrity.
    if (integrityTokenProviderOperation.Error != StandardIntegrityErrorCode.NoError)
    {
        AppendStatusLog("StandardIntegrityAsyncOperation failed with error: " +
                integrityTokenProviderOperation.Error);
        yield break;
    }

    // Get the response.
    var integrityTokenProvider = integrityTokenProviderOperation.GetResult();
}
```

### Unreal Engine

```c++
// .h
void MyClass::OnPrepareIntegrityTokenCompleted(
  EStandardIntegrityErrorCode ErrorCode,
  UStandardIntegrityTokenProvider* Provider)
{
  // Check the resulting error code.
  if (ErrorCode == EStandardIntegrityErrorCode::StandardIntegrity_NO_ERROR)
  {
    // ...
  }
}

// .cpp
void MyClass::PrepareIntegrityToken()
{
  int64 CloudProjectNumber = ...

  // Create the Integrity Token Request.
  FPrepareIntegrityTokenRequest Request = { CloudProjectNumber };

  // Create a delegate to bind the callback function.
  FPrepareIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnPrepareIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnPrepareIntegrityTokenCompleted);

  // Initiate the prepare integrity token operation, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSu<bsystemUStandardIntegrity>Manager()
    ->PrepareIntegrityToken(Request, Delegate);
}
```

### Native

```c++
/// Initialize StandardIntegrityManager
StandardIntegrityManager_init(/* app's java vm */, /* an android context */);
/// Create a PrepareIntegrityTokenRequest opaque object.
int64_t cloudProjectNumber = ...;
PrepareIntegrityTokenRequest* tokenProviderRequest;
PrepareIntegrityTokenRequest_create(&tokenProviderRequest);
PrepareIntegrityTokenRequest_setCloudProjectNumber(tokenProviderRequest, cloudProjectNumber);

/// Prepare a StandardIntegrityTokenProvider opaque type pointer and call
/// StandardIntegrityManager_prepareIntegrityToken().
StandardIntegrityTokenProvider* tokenProvider;
StandardIntegrityErrorCode error_code =
        StandardIntegrityManager_prepareIntegrityToken(tokenProviderRequest, &tokenProvider);

/// ...
/// Proceed to polling iff error_code == STANDARD_INTEGRITY_NO_ERROR
if (error_code != STANDARD_INTEGRITY_NO_ERROR)
{
    /// Remember to call the *_destroy() functions.
    return;
}
/// ...
/// Use polling to wait for the async operation to complete.

IntegrityResponseStatus token_provider_status;

//https://developer.android.com/reference/native/play/core/group/integrity error codes.
StandardIntegrityErrorCode error_code =
        StandardIntegrityTokenProvider_getStatus(tokenProvider, &token_provider_status);
if (error_code == STANDARD_INTEGRITY_NO_ERROR
    && token_provider_status == INTEGRITY_RESPONSE_COMPLETED)
{
    /// continue to request token from the token provider
}
/// ...
/// Remember to free up resources.
PrepareIntegrityTokenRequest_destroy(tokenProviderRequest);
```

## Protect requests against tampering (recommended)

When you're checking a user action in your app with the Play Integrity API, you can leverage the`requestHash`field to mitigate against tampering attacks. For example, a game may want to report the player's score to the game's backend server, and your server wants to ensure this score has not been tampered with by a proxy server. The Play Integrity API returns the value you set in the`requestHash`field, inside the signed integrity response. Without the`requestHash`, the integrity token will be bound only to the device, but not to the specific request, which opens up the possibility of attack. The following instructions describe how to make use of the`requestHash`field effectively:

When you request an integrity verdict:

- Compute a digest of all relevant request parameters (e.g. SHA256 of a stable request serialization) from the user action or server request that is happening. The value set in the`requestHash`field has a maximum length of 500 bytes. Include any app request data in the`requestHash`that is crucial or relevant to the action that you are checking or protecting. The`requestHash`field is included in the integrity token verbatim, so long values may increase the request size.
- Provide the digest as the`requestHash`field to the Play Integrity API, and obtain the integrity token.

| **Caution:** Never put any sensitive information as plain-text into the`requestHash`argument. Instead, hash all the input by default.

When you receive an integrity verdict:

- Decode the integrity token, and extract the`requestHash`field.
- Compute a digest of the request in the same manner as in the app (e.g. SHA256 of a stable request serialization).
- Compare the app-side and server-side digests. If they do not match, the request is not trustworthy.

| **Note:** Standard requests are[automatically protected against replay attacks](https://developer.android.com/google/play/integrity/standard#replay-protection).

## Request an integrity verdict (on demand)

After you have prepared the integrity token provider, you can start requesting integrity verdicts from Google Play. To do so, complete the following steps:

1. [Obtain a`StandardIntegrityTokenProvider`](https://developer.android.com/google/play/integrity/standard#prepare-integrity).
2. Construct an`StandardIntegrityTokenRequest`, supplying the request hash of the user action you want to protect through the`setRequestHash`method.
3. Use the integrity token provider to call`request()`, supplying the`StandardIntegrityTokenRequest`.

### Java

```java
import com.google.android.gms.tasks.Task;

StandardIntegrityTokenProvider integrityTokenProvider;

// See above how to prepare integrityTokenProvider.

// Request integrity token by providing a user action request hash. Can be called
// several times for different user actions.
String requestHash = "2cp24z...&q<uot;;
TaskStandardInte>grityToken integrityTokenResponse =
    integrityTokenProvider.request(
        StandardIntegrityTokenRequest.builder()
            .setRequestHash(requestHash)
            .build());
integrityTokenResponse
    .addOnSuccessListener(response -> sendToServer(response.token()))
    .addOnFailureListener(exception -> handleError(exception));
```

### Unity

```c#
IEnumerator RequestIntegrityTokenCoroutine() {
    StandardIntegrityTokenProvider integrityTokenProvider;

    // See above how to prepare integrityTokenProvider.

    // Request integrity token by providing a user action request hash. Can be called
    // several times for different user actions.
    String requestHash = "2cp24z...";
    var integrityTokenOperation = integrityTokenProvider.Request(
      new StandardIntegrityTokenRequest(requestHash)
    );

    // Wait for PlayAsyncOperation to complete.
    yield return integrityTokenOperation;

    // Check the https://developer.android.com/reference/unity/namespace/Google/Play/Integrityerror code.
    if (integrityTokenOperation.Error != StandardIntegrityErrorCode.NoError)
    {
        AppendStatusLog("StandardIntegrityAsyncOperation failed with error: " +
                integrityTokenOperation.Error);
        yield break;
    }

    // Get the response.
    var integrityToken = integrityTokenOperation.GetResult();
}
```

### Unreal Engine

```c++
// .h
void MyClass::OnRequestIntegrityTokenCompleted(
  EStandardIntegrityErrorCode ErrorCode,
  UStandardIntegrityToken* Response)
{
  // Check the resulting error code.
  if (ErrorCode == EStandardIntegrityErrorCode::StandardIntegrity_NO_ERROR)
  {
    // Get the token.
    FString Token = Response->Token;
  }
}

// .cpp
void MyClass::RequestIntegrityToken()
{
  UStandardIntegrityTokenProvider* Provider = ...

  // Prepare the UStandardIntegrityTokenProvider.

  // Request integrity token by providing a user action request hash. Can be called
  // several times for different user actions.
  FString RequestHash = ...;
  FStandardIntegrityTokenRequest Request = { RequestHash };

  // Create a delegate to bind the callback function.
  FStandardIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnRequestIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnRequestIntegrityTokenCompleted);

  // Initiate the standard integrity token request, passing the delegate to handle the result.
  Provider->Request(Request, Delegate);
}
```

### Native

```c++
/// Create a StandardIntegrityTokenRequest opaque object.
const char* requestHash = ...;
StandardIntegrityTokenRequest* tokenRequest;
StandardIntegrityTokenRequest_create(&tokenRequest);
StandardIntegrityTokenRequest_setRequestHash(tokenRequest, requestHash);

/// Prepare a StandardIntegrityToken opaque type pointer and call
/// StandardIntegrityTokenProvider_request(). Can be called several times for
/// different user actions. See above how to prepare token provider.
StandardIntegrityToken* token;
StandardIntegrityErrorCode error_code =
        StandardIntegrityTokenProvider_request(tokenProvider, tokenRequest, &token);

/// ...
/// Proceed to polling iff error_code == STANDARD_INTEGRITY_NO_ERROR
if (error_code != STANDARD_INTEGRITY_NO_ERROR)
{
    /// Remember to call the *_destroy() functions.
    return;
}
/// ...
/// Use polling to wait for the async operation to complete.

IntegrityResponseStatus token_status;

/// Chhttps://developer.android.com/reference/native/play/core/group/integrityor codes.
StandardIntegrityErrorCode error_code =
        StandardIntegrityToken_getStatus(token, &token_status);
if (error_code == STANDARD_INTEGRITY_NO_ERROR
    && token_status == INTEGRITY_RESPONSE_COMPLETED)
{
    const char* integrityToken = StandardIntegrityToken_getToken(token);
}
/// ...
/// Remember to free up resources.
StandardIntegrityTokenRequest_destroy(tokenRequest);
StandardIntegrityToken_destroy(token);
StandardIntegrityTokenProvider_destroy(tokenProvider);
StandardIntegrityManager_destroy();
```

If your app uses the same token provider for too long, the token provider can expire which results in the[INTEGRITY_TOKEN_PROVIDER_INVALID](https://developer.android.com/google/play/integrity/error-codes#iErr_19)error on the next token request. You should handle this error by requesting a new provider.

## Decrypt and verify the integrity verdict

After you request an integrity verdict, the Play Integrity API provides an encrypted response token. To obtain the device integrity verdicts, you must decrypt the integrity token on Google's servers. To do so, complete these steps:

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create)within the Google Cloud project that's linked to your app.
2. On your app's server, fetch the access token from your service account credentials using the playintegrity scope, and make the following request:

   ```
   playintegrity.googleapis.com/v1/PACKAGE_NAME:decodeIntegrityToken -d \
   '{ "integrity_token": "INTEGRITY_TOKEN" }'
   ```
   | **Note:** To access the API's REST interface, you can use the[Google API Client Library](https://developers.google.com/api-client-library), which is available in many programming languages,[including Java](https://github.com/googleapis/google-api-java-client-services/tree/main/clients/google-api-services-playintegrity/v1).
3. Read the JSON response.

The resulting payload is a plain-text token that contains[integrity verdicts](https://developer.android.com/google/play/integrity/verdicts).

### Automatic replay protection

To mitigate replay attacks, Google Play automatically prevents integrity tokens from being reused many times. Attempting to repeatedly decrypt the same token will result in cleared verdicts as follows:

- The device recognition verdict will be empty.
- The app recognition verdict and app licensing verdict will be set to`UNEVALUATED`.
- Any of the optional verdicts that are enabled using the Play Console will be set to`UNEVALUATED`(or to an empty verdict if it is a multi-value verdict).

## Remediate verdict issues with a Google Play prompt (optional)

After your server receives an integrity verdict, it can determine how to proceed. If the verdict indicates there's an issue---such as the app being unlicensed, tampered with, or the device being compromised---you can give users a chance to fix the issue themselves.

The Play Integrity API provides an option to show a Google Play dialog that prompts the user to take action, for example, to get the official version of your app from Google Play.

To learn how to trigger these dialogs from your app based on the server's response, see[Remediation dialogs](https://developer.android.com/google/play/integrity/remediation).
| **Tip:** At any time, users can[check their device's Play Protect certified status and troubleshoot issues](https://support.google.com/googleplay/answer/7165974)in the Play Store app. You can point your users to this support page if they need help troubleshooting a device integrity issue.