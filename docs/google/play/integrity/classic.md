---
title: https://developer.android.com/google/play/integrity/classic
url: https://developer.android.com/google/play/integrity/classic
source: md.txt
---

If you're only planning to make [standard API
requests](https://developer.android.com/google/play/integrity/standard), which are suitable for the majority
of developers, you can skip ahead to [integrity
verdicts](https://developer.android.com/google/play/integrity/verdicts). This page describes making classic
API requests for integrity verdicts, which are supported on Android 4.4 (API
level 19) or higher.

## Considerations

### Compare standard and classic requests

You can make standard requests, classic requests, or a combination of the two
depending on your app's security and anti-abuse needs. Standard requests are
suitable for all apps and games and can be used to check that any action or
server call is genuine, while delegating some protection against replayability
and exfiltration to Google Play. Classic requests are more expensive to make and
you are responsible for correctly implementing them to protect against
exfiltration and certain types of attacks. Classic requests should be made less
frequently than standard requests, for example as an occasional one-off to check
if a highly valuable or sensitive action is genuine.

The following table highlights the key differences between the two types of
requests:

|   | **Standard API request** | **Classic API request** |
| **Pre-requisites** |   |   |
|---|---|---|
| Minimum Android SDK required**\*** | Android 6.0 (API level 23) or higher | Android 6.0 (API level 23) or higher |
| Google Play requirements | Google Play Store and Google Play services | Google Play Store and Google Play services |
| API warm up required | ✔️ (a few seconds) | ❌ |
| Typical request latency | A few hundred milliseconds | A few seconds |
| Potential request frequency | Frequent (on-demand check for any action or request) | Infrequent (one-off check for highest value actions or most sensitive requests) |
| Timeouts | Most warm ups are under 10s but they involve a server call, so a long timeout is recommended (e.g. 1 minute). Verdict requests happen client-side | Most requests are under 10s but they involve a server call, so a long timeout is recommended (e.g. 1 minute) |
| Contains device, app, and account details | ✔️ | ✔️ |
| Token caching | Protected on-device caching by Google Play | Not recommended |
| Decrypt and verify token via Google Play server | ✔️ | ✔️ |
| Typical decryption server-to-server request latency | 10s of milliseconds with three-nines availability | 10s of milliseconds with three-nines availability |
| Decrypt and verify token locally in a secure server environment | ❌ | ✔️ |
| Decrypt and verify token client-side | ❌ | ❌ |
| Integrity verdict freshness | Some automatic caching and refreshing by Google Play | All verdicts recomputed on each request |
| Requests per app per day | 10,000 by default (an increase can be requested) | 10,000 by default (an increase can be requested) |
| Requests per app instance per minute | Warm ups: 5 per minute Integrity tokens: No public limit**\*\*** | Integrity tokens: 5 per minute |
| Mitigate against tampering and similar attacks | Use `requestHash` field | Use `nonce` field with content binding based on request data |
| Mitigate against replay and similar attacks | Automatic mitigation by Google Play | Use `nonce` field with server side logic |

***\*** For the Play Integrity API library [v1.4.0](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-4-0) and later, the minimum
supported Android SDK is the same for both request types and is determined by
the library's `minSdkVersion`. For [v1.3.0](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-3-0) and earlier releases, the minimum
Android SDK required is Android 5.0 (API level 21) for Standard API requests and
Android 4.4 (API level 19) for Classic API requests.*

***\*\*** All requests, including those without public limits, are subject to
non-public defensive limits at high values.*

### Make classic requests infrequently

Generating an integrity token uses time, data, and battery, and each app has a
maximum number of classic requests it can make per day. Therefore you should
only make classic requests to check the highest value or most sensitive actions
are genuine when you want an additional guarantee to a standard request. You
shouldn't make classic requests for high-frequency or low-value actions. Don't
make classic requests every time the app goes to the foreground nor every few
minutes in the background, and avoid calling from a large number of devices at
the same time. An app making too many classic requests calls may be throttled to
protect users from incorrect implementations.

### Avoid caching verdicts

Caching a verdict increases the risk of attacks such as exfiltration and replay,
where a good verdict is reused from an untrusted environment. If you're
considering making a classic request and then caching it for use later, it's
recommended instead to perform a standard request on demand. Standard requests
involve some caching on the device but Google Play uses additional protection
techniques to mitigate the risk of replay attacks and exfiltration.

### Use the nonce field to protect classic requests

The Play Integrity API offers a field called `nonce`, which can be used to
further protect your app against certain attacks, such as replay and tampering
attacks. The Play Integrity API returns the value you set in this field, inside
the signed integrity response. Carefully follow the guidance on [how to generate
nonces](https://developer.android.com/google/play/integrity/classic#nonce) to protect your app from attacks.
| **Caution:** The value passed as the `nonce` is visible in cleartext to your app, and to Google. You should encrypt or hash the data you wish to set in this field before passing it to the Play Integrity API.

### Retry classic requests with exponential backoff

Environmental conditions, such as an unstable Internet connection or an
overloaded device, can cause device integrity checks to fail. This can lead to
no labels being generated for a device that is otherwise trustworthy. To
mitigate these scenarios, include a retry option with exponential backoff.

## Overview

![](https://developer.android.com/static/images/google/play/integrity/api-usage.svg) **Figure 1.** Sequence diagram that shows the high-level design of the Play Integrity API.

When the user performs a high-value action in your app that you want to protect
with an integrity check, complete the following steps:

1. Your app's server-side backend generates and sends a unique value to the client-side logic. The remaining steps refer to this logic as your "app".
2. Your app creates the `nonce` from the unique value and the content of your high-value action. It then calls the Play Integrity API, passing in the `nonce`.
3. Your app receives a signed and encrypted verdict from the Play Integrity API.
4. Your app passes the signed and encrypted verdict to your app's backend.
5. Your app's backend sends the verdict to a Google Play server. The Google Play server decrypts and verifies the verdict, returning the results to your app's backend.
6. Your app's backend determines how to proceed, based on the signals contained in the token payload.
7. Your app's backend sends the decision outcomes to your app.

## Generate a nonce

When you protect an action in your app with the Play Integrity API, you can
leverage the `nonce` field to mitigate certain types of attacks, such as
person-in-the-middle (PITM) tampering attacks and replay attacks. The Play
Integrity API returns the value you set in this field inside the signed
integrity response.

The value set in the `nonce` field must be correctly formatted:

- `String`
- URL-safe
- Encoded as Base64 and non-wrapping
- Minimum of 16 characters
- Maximum of 500 characters

The following are some common ways to use the `nonce` field in the Play
Integrity API. To get the strongest protection from the `nonce`, you can combine
the methods below.

### Include a request hash to protect against tampering

You can use the `nonce` parameter in a classic API request similarly to the
`requestHash` parameter in a standard API request to protect the contents of a
request against tampering.

When you request an integrity verdict:

1. Compute a digest of all critical request parameters (e.g. SHA256 of a stable request serialization) from the user action or server request that is happening.
2. Use `setNonce` to set the `nonce` field to the value of the computed digest.

When you receive an integrity verdict:

1. Decode and verify the integrity token, and obtain the digest from the `nonce` field.
2. Compute a digest of the request in the same manner as in the app (e.g. SHA256 of a stable request serialization).
3. Compare the app-side and server-side digests. If they do not match, the request is not trustworthy.

| **Note:** You should also verify both the device and app integrity signals to ensure that the results of the high-value action were created by your untampered app on an untampered device.

### Include unique values to protect against replay attacks

In order to prevent malicious users from reusing previous responses from the
Play Integrity API, you can use the `nonce` field to uniquely identify each
message.

When you request an integrity verdict:

1. Obtain a globally unique value in a way that malicious users cannot predict. For example, a cryptographically-secure random number generated on the server side can be such a value, or a pre-existing ID, such as a session or a transaction ID. A simpler and less secure variant is to generate a random number on the device. We recommend creating values 128 bits or larger.
2. Call `setNonce()` to set the `nonce` field to the unique value from step 1.

When you receive an integrity verdict:

1. Decode and verify the integrity token, and obtain the unique value from the `nonce` field.
2. If the value from step 1 was generated on the server, check that the received unique value was one of the generated values, and that it's being used for the first time (your server will need to keep a record of generated values for a suitable duration). If the received unique value has been used already or does not appear in the record, reject the request
3. Otherwise, if the unique value was generated on the device, check that the received value is being used for the first time (your server needs to keep a record of already seen values for a suitable duration). If the received unique value has been used already, reject the request.

### Combine both protections against tampering and replay attacks (recommended)

It is possible to use the `nonce` field to protect against both tampering and
replay attacks at the same time. To do so, generate the unique value as
described above, and include it as part of your request. Then compute the
request hash, making sure to include the unique value as part of the hash. An
implementation that combines both approaches is as follows:

When you request an integrity verdict:

1. The user initiates the high-value action.
2. Obtain a unique value for this action as described in the [Include unique
   values to protect against replay attacks](https://developer.android.com/google/play/integrity/classic#include-unique) section.
3. Prepare a message you want to protect. Include the unique value from step 2 in the message.
4. Your app calculates a digest of the message it wants to protect, as described in the [Include a request hash to protect against
   tampering](https://developer.android.com/google/play/integrity/classic#include-request) section. Since the message contains the unique value, the unique value is part of the hash.
5. Use `setNonce()` to set the `nonce` field to the computed digest from the previous step.

When you receive an integrity verdict:

1. Obtain the unique value from the request
2. Decode and verify the integrity token, and obtain the digest from the `nonce` field.
3. As described in the [Include a request hash to protect against tampering](https://developer.android.com/google/play/integrity/classic#include-request) section, recompute the digest on the server side, and check that it matches the digest obtained from the integrity token.
4. As described in the [Include unique values to protect against replay
   attacks](https://developer.android.com/google/play/integrity/classic#include-unique) section, check the validity of the unique value.

The following sequence diagram illustrates these steps with a server-side
`nonce`:
![](https://developer.android.com/static/images/google/play/integrity/play-integrity-api-nonce-content-binding.svg) **Figure 2.** Sequence diagram that shows how to protect against both tampering and replay attacks.

## Request an integrity verdict

After generating a `nonce`, you can request an integrity verdict from Google
Play. To do so, complete the following steps:

1. Create an `IntegrityManager`, as shown in the following examples.
2. Construct an `IntegrityTokenRequest`, supplying the `nonce` through the `setNonce()` method in the associated builder. Apps exclusively distributed outside of Google Play and SDKs also have to specify their Google Cloud project number through the `setCloudProjectNumber()` method. Apps on Google Play are linked to a Cloud project in the Play Console and do not need to set the Cloud project number in the request.
3. Use the manager to call `requestIntegrityToken()`, supplying the
   `IntegrityTokenRequest`.

   | **Caution:** `nonce` values are passed as-is to Google's systems, so you shouldn't include personally identifiable information or other sensitive data directly or indirectly in the `nonce`.

### Kotlin

```kotlin
// Receive the nonce from the secure server.
val nonce: String = ...

// Create an instance of a manager.
val integrityManager =
    IntegrityManagerFactory.create(applicationContext)

// Request the integrity token by providing a nonce.
val integrityTokenResponse: Task<IntegrityTokenResponse> =
    integrityManager.requestIntegrityToken(
        IntegrityTokenRequest.builder()
             .setNonce(nonce)
             .build())
```

### Java

```java
import com.google.android.gms.tasks.Task; ...

// Receive the nonce from the secure server.
String nonce = ...

// Create an instance of a manager.
IntegrityManager integrityManager =
    IntegrityManagerFactory.create(getApplicationContext());

// Request the integrity token by providing a nonce.
Task<IntegrityTokenResponse> integrityTokenResponse =
    integrityManager
        .requestIntegrityToken(
            IntegrityTokenRequest.builder().setNonce(nonce).build());
```

### Unity

```c#
IEnumerator RequestIntegrityTokenCoroutine() {
    // Receive the nonce from the secure server.
    var nonce = ...

    // Create an instance of a manager.
    var integrityManager = new IntegrityManager();

    // Request the integrity token by providing a nonce.
    var tokenRequest = new IntegrityTokenRequest(nonce);
    var requestIntegrityTokenOperation =
        integrityManager.RequestIntegrityToken(tokenRequest);

    // Wait for PlayAsyncOperation to complete.
    yield return requestIntegrityTokenOperation;

    // Check the resulting https://developer.android.com/google/play/integrity/error-codes.
    if (requestIntegrityTokenOperation.Error != IntegrityErrorCode.NoError)
    {
        AppendStatusLog("IntegrityAsyncOperation failed with error: " +
                requestIntegrityTokenOperation.Error);
        yield break;
    }

    // Get the response.
    var tokenResponse = requestIntegrityTokenOperation.GetResult();
}
```

### Unreal Engine

```c++
// .h
void MyClass::OnRequestIntegrityTokenCompleted(
  EIntegrityErrorCode ErrorCode,
  UIntegrityTokenResponse* Response)
{
  // Check the resulting error code.
  if (ErrorCode == EIntegrityErrorCode::Integrity_NO_ERROR)
  {
    // Get the token.
    FString Token = Response->Token;
  }
}

// .cpp
void MyClass::RequestIntegrityToken()
{
  // Receive the nonce from the secure server.
  FString Nonce = ...

  // Create the Integrity Token Request.
  FIntegrityTokenRequest Request = { Nonce };

  // Create a delegate to bind the callback function.
  FIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnRequestIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnRequestIntegrityTokenCompleted);

  // Initiate the integrity token request, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UIntegrityManager>()
    ->RequestIntegrityToken(Request, Delegate);
}
```

### Native

```c++
/// Create an IntegrityTokenRequest opaque object.
const char* nonce = RequestNonceFromServer();
IntegrityTokenRequest* request;
IntegrityTokenRequest_create(&request);
IntegrityTokenRequest_setNonce(request, nonce);

/// Prepare an IntegrityTokenResponse opaque type pointer and call
/// IntegerityManager_requestIntegrityToken().
IntegrityTokenResponse* response;
IntegrityErrorCode error_code =
        IntegrityManager_requestIntegrityToken(request, &response);

/// ...
/// Proceed to polling iff error_code == INTEGRITY_NO_ERROR
if (error_code != INTEGRITY_NO_ERROR)
{
    /// Remember to call the *_destroy() functions.
    return;
}
/// ...
/// Use polling to wait for the async operation to complete.
/// Note, the polling shouldn't block the thread where the IntegrityManager
/// is running.

IntegrityResponseStatus response_status;

/// Check for https://developer.android.com/google/play/integrity/error-codes.
IntegrityErrorCode error_code =
        IntegrityTokenResponse_getStatus(response, &response_status);
if (error_code == INTEGRITY_NO_ERROR
    && response_status == INTEGRITY_RESPONSE_COMPLETED)
{
    const char* integrity_token = IntegrityTokenResponse_getToken(response);
    SendTokenToServer(integrity_token);
}
/// ...
/// Remember to free up resources.
IntegrityTokenRequest_destroy(request);
IntegrityTokenResponse_destroy(response);
IntegrityManager_destroy();
```

## Decrypt and verify the integrity verdict

When you request an integrity verdict, the Play Integrity API provides a signed
response token. The `nonce` that you include in your request becomes part of the
response token.

### Token format

The token is a nested [JSON Web Token (JWT)](https://jwt.io/), that
is [JSON Web Encryption (JWE)](https://tools.ietf.org/html/rfc7516)
of [JSON Web Signature (JWS)](https://tools.ietf.org/html/rfc7515).
The JWE and JWS components are represented using [compact
serialization](https://datatracker.ietf.org/doc/html/rfc7515#section-3.1)
.

The encryption / signing algorithms are well-supported across various JWT
implementations:

- JWE uses A256KW for [alg](https://tools.ietf.org/html/rfc7516#section-4.1.1) and A256GCM for [enc](https://tools.ietf.org/html/rfc7516#section-4.1.2)

- JWS uses ES256.

### Decrypt and verify on Google's servers (recommended)

The Play Integrity API allows you to decrypt and verify the integrity verdict on
Google's servers, which enhances your app's security. To do so, complete these
steps:

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create) within the Google Cloud project that's linked to your app.
2. On your app's server, fetch the access token from your service account
   credentials using the `playintegrity` scope, and make the following request:

   ```
   playintegrity.googleapis.com/v1/PACKAGE_NAME:decodeIntegrityToken -d \
   '{ "integrity_token": "INTEGRITY_TOKEN" }'
   ```
   | **Note:** To access the API's REST interface, you can use the [Google API Client Library](https://developers.google.com/api-client-library), which is available in many programming languages, [including Java](https://github.com/googleapis/google-api-java-client-services/tree/main/clients/google-api-services-playintegrity/v1).
3. Read the JSON response.

### Decrypt and verify locally

| **Note:** To protect your app's security, it's recommended that you [allow Google
| Play to manage your response encryption](https://developer.android.com/google/play/integrity/classic#decrypt-verify-google-servers) for your app.

If you choose to manage and download your response encryption keys, you can
decrypt and verify the returned token within your own secure server environment.
You can obtain the returned token by using the `IntegrityTokenResponse#token()`
method.

The following example shows how to decode the AES key and the DER-encoded public
EC key for signature verification from the Play Console to language-specific
(the Java programming language, in our case) keys in the app's backend. Note
that the keys are base64-encoded using default flags.  

### Kotlin

```kotlin
// base64OfEncodedDecryptionKey is provided through Play Console.
var decryptionKeyBytes: ByteArray =
    Base64.decode(base64OfEncodedDecryptionKey, Base64.DEFAULT)

// Deserialized encryption (symmetric) key.
var decryptionKey: SecretKey = SecretKeySpec(
    decryptionKeyBytes,
    /* offset= */ 0,
    AES_KEY_SIZE_BYTES,
    AES_KEY_TYPE
)

// base64OfEncodedVerificationKey is provided through Play Console.
var encodedVerificationKey: ByteArray =
    Base64.decode(base64OfEncodedVerificationKey, Base64.DEFAULT)

// Deserialized verification (public) key.
var verificationKey: PublicKey = KeyFactory.getInstance(EC_KEY_TYPE)
    .generatePublic(X509EncodedKeySpec(encodedVerificationKey))
```

### Java

```java
// base64OfEncodedDecryptionKey is provided through Play Console.
byte[] decryptionKeyBytes =
    Base64.decode(base64OfEncodedDecryptionKey, Base64.DEFAULT);

// Deserialized encryption (symmetric) key.
SecretKey decryptionKey =
    new SecretKeySpec(
        decryptionKeyBytes,
        /* offset= */ 0,
        AES_KEY_SIZE_BYTES,
        AES_KEY_TYPE);

// base64OfEncodedVerificationKey is provided through Play Console.
byte[] encodedVerificationKey =
    Base64.decode(base64OfEncodedVerificationKey, Base64.DEFAULT);
// Deserialized verification (public) key.
PublicKey verificationKey =
    KeyFactory.getInstance(EC_KEY_TYPE)
        .generatePublic(new X509EncodedKeySpec(encodedVerificationKey));
```

Next, use these keys to first decrypt the integrity token (JWE part) and then
verify and extract the nested JWS part.  

### Kotlin

```kotlin
val jwe: JsonWebEncryption =
    JsonWebStructure.fromCompactSerialization(integrityToken) as JsonWebEncryption
jwe.setKey(decryptionKey)

// This also decrypts the JWE token.
val compactJws: String = jwe.getPayload()

val jws: JsonWebSignature =
    JsonWebStructure.fromCompactSerialization(compactJws) as JsonWebSignature
jws.setKey(verificationKey)

// This also verifies the signature.
val payload: String = jws.getPayload()
```

### Java

```java
JsonWebEncryption jwe =
    (JsonWebEncryption)JsonWebStructure
        .fromCompactSerialization(integrityToken);
jwe.setKey(decryptionKey);

// This also decrypts the JWE token.
String compactJws = jwe.getPayload();

JsonWebSignature jws =
    (JsonWebSignature) JsonWebStructure.fromCompactSerialization(compactJws);
jws.setKey(verificationKey);

// This also verifies the signature.
String payload = jws.getPayload();
```

The resulting payload is a plain-text token that contains [integrity
verdicts](https://developer.android.com/google/play/integrity/verdicts).

## Remediate verdict issues with a Google Play prompt (optional)

After your server receives an integrity verdict, the server can determine how to proceed.
If the verdict indicates there's an issue---such as the app being unlicensed,
tampered with, or the device being compromised---you can give users a chance
to fix the issue themselves.

The Play Integrity API provides an option to show a Google Play dialog that
prompts the user to take action, for example, to get the official version of
your app from Google Play.

To learn how to trigger these dialogs from your app based on the server's
response, see [Remediation dialogs](https://developer.android.com/google/play/integrity/remediation).
| **Tip:** At any time, users can [check their device's Play Protect certification
| status and troubleshoot issues](https://support.google.com/googleplay/answer/7165974) in the Play Store app. You can point your users to this support page if they need help troubleshooting a device integrity issue.