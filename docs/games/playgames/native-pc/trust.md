---
title: https://developer.android.com/games/playgames/native-pc/trust
url: https://developer.android.com/games/playgames/native-pc/trust
source: md.txt
---

Play Integrity for PC helps you check that game events and server requests are
coming from a genuine instance of Google Play Games for PC on a genuine PC
device. By detecting potentially risky devices and unknown emulators, your
game's backend server can respond with appropriate actions to prevent cheating,
unauthorized access, fraudulent traffic, and abuse.

## Pre-requisites

- Complete the [SDK setup](https://developer.android.com/games/playgames/native-pc/setup).
- Review the Integrity API [security considerations](https://developer.android.com/google/play/integrity/overview#security-considerations).
- Read and understand the Integrity API [terms of service](https://developer.android.com/google/play/integrity/terms) and [data handling information](https://developer.android.com/google/play/integrity/terms#data-safety).
- In your [Google Cloud Console](https://console.cloud.google.com/), create a Cloud project or choose an existing Cloud project that you want to use with Play Integrity for PC. Navigate to **APIs \& services** and [enable Google Play Integrity API](https://console.cloud.google.com/marketplace/product/google/playintegrity.googleapis.com).
- If you expect to make over 10K Play Integrity for PC requests per day, you should [request to increase](https://developer.android.com/google/play/integrity/setup#increase-daily-max) your daily maximum.

> [!NOTE]
> **Note:** The Cloud project you're using with Play Integrity for PC does **not** need to be linked to your Google Play Console. The Integrity API features in the Play Console are only supported for mobile Android game integrations and won't work with Play Integrity for PC.

## Step 1: Decide how you'll use Play Integrity for PC in your game

Decide when you'll call Play Integrity for PC to obtain an integrity verdict
about the environment. For example, you could request a verdict when the game is
opened, when a player signs in, or when a player joins a multiplayer game. Then
decide how you'll handle different integrity responses. For example, you could:

- Collect the response without any enforcement actions, and analyze the data internally to understand if it's a useful signal of abuse.
- Collect the response and implement logic on your backend server to allow devices that pass integrity verdicts to play your game normally, while challenging or denying access to traffic that's coming from suspicious environments.
- Collect the response and implement logic on your backend to match players on devices that pass integrity checks together, while matching traffic coming from suspicious environments together.

## Step 2: Request integrity tokens in your game

### Warm up Play Integrity for PC

Prepare (or "warm up") Play Integrity for PC, which allows Google Play to
intelligently cache partial attestation information on the device in order to
decrease the latency on the critical path when you make a request for an
integrity verdict. You could do this asynchronously as soon as your game opens
so that you can make on-demand integrity requests when you need to.

```c++
void PrepareIntegrityToken(
  const PrepareIntegrityTokenParams & params,
  PrepareIntegrityTokenContinuation continuation
)
```

On success, the continuation will be called with a
[PrepareIntegrityTokenResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/prepare-integrity-token-result-value#structgoogle_1_1play_1_1integrity_1_1_prepare_integrity_token_result_value) containing a
[RequestTokenData](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-token-data#structgoogle_1_1play_1_1integrity_1_1_request_token_data) that should be used to request an
integrity token. This data should be cached in-memory and reused for the
duration of the application's session for calls to
[RequestIntegrityToken](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/integrity/integrity-client#classgoogle_1_1play_1_1integrity_1_1_integrity_client_1a4357e1b01ef9be5eb0e6a69bb45ed021).

Only if your application determines that it is necessary to entirely re-evaluate
the integrity verdict should a call to
[PrepareIntegrityToken](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/integrity/integrity-client#classgoogle_1_1play_1_1integrity_1_1_integrity_client_1a16b2300dfd23a2cbf3096e893f70a273) be made.

| Details |   |
|---|---|
| Parameters | `params`: Parameters containing a Google Cloud project number. `continuation`: The async callback to return the integrity token provider to. |

A code snippet showing how the
[PrepareIntegrityToken](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/integrity/integrity-client#classgoogle_1_1play_1_1integrity_1_1_integrity_client_1a16b2300dfd23a2cbf3096e893f70a273) action should be called is
provided as follows:

    google::play::integrity::IntegrityClient client_;

    google::play::integrity::PrepareIntegrityTokenResult
    IntegrityInterface::PrepareIntegrityToken(int64_t cloud_project_number) {
      google::play::integrity::PrepareIntegrityTokenParams params;
      params.cloud_project_number = cloud_project_number;

      auto promise = std::make_shared<
          std::promise<google::play::integrity::PrepareIntegrityTokenResult>>();
      client_.PrepareIntegrityToken(
          params,
          [promise](
              google::play::integrity::PrepareIntegrityTokenResult result) {
            promise->set_value(std::move(result));
          });

      return promise->get_future().get();
    }

### Request an integrity token

Integrity tokens are a mechanism for your game to verify the device is not
tampered with. Whenever your game makes a server request that you want to check
is genuine, you can request an integrity token and then send it to your game's
backend server for decryption and verification.

When you're checking a user action in your app with the Play Integrity API for
PC, you can use the [RequestIntegrityTokenParams::request_hash](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-integrity-token-params#structgoogle_1_1play_1_1integrity_1_1_request_integrity_token_params_1aa68139c18e6b5a565e04802f87a2cd19)
field to mitigate against tampering attacks. For example, you may want to report
the player's score to your game's backend server, and your server wants to
verify this score has not been tampered with by a proxy server. Play Integrity
for PC can return the value you set in this field, inside the signed integrity
response. Without the requestHash, the integrity token will be bound only to the
device, but not to the specific request, which opens up the possibility of
attack.

```c++
void RequestIntegrityToken(
  const RequestIntegrityTokenParams & params,
  RequestIntegrityTokenContinuation continuation
)
```

To mitigate the possibility of an attack, when you request an integrity verdict:

- Compute a digest of all relevant request parameters (e.g. SHA256 of a stable request serialization) from the user action or server request that is happening.
- Set the [RequestIntegrityTokenParams::request_hash](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-integrity-token-params#structgoogle_1_1play_1_1integrity_1_1_request_integrity_token_params_1aa68139c18e6b5a565e04802f87a2cd19) field to the digest.

| Details |   |
|---|---|
| Parameters | `params`: Parameters containing the prepared [RequestTokenData](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-token-data#structgoogle_1_1play_1_1integrity_1_1_request_token_data) and integrity check request hash. `continuation`: The async callback to return the data to. |

A code snippet showing how the [RequestIntegrityToken](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/integrity/integrity-client#classgoogle_1_1play_1_1integrity_1_1_integrity_client_1a4357e1b01ef9be5eb0e6a69bb45ed021)
action can be called is provided as follows:

    absl::StatusOr<google::play::integrity::RequestIntegrityTokenResult>
    IntegrityInterface::RequestIntegrityToken(
        const google::play::integrity::PrepareIntegrityTokenResult&
            prepare_integrity_token_result,
        const std::string& request_hash) {
      // Check if the prepare_integrity_token_result is OK
      if (!prepare_integrity_token_result.ok()) {
        return absl::FailedPreconditionError(
            absl::StrCat("PrepareIntegrityTokenResult is not OK. Error code: ",
                         prepare_integrity_token_result.error_code));
      }

      google::play::integrity::RequestIntegrityTokenParams params{
          .request_token_data =
              prepare_integrity_token_result.request_token_data,
          .request_hash = request_hash};

      auto promise = std::make_shared<std::promise<
          google::play::integrity::RequestIntegrityTokenResult>>();
      client_.RequestIntegrityToken(
          params,
          [promise](google::play::integrity::RequestIntegrityTokenResult result) {
            promise->set_value(std::move(result));
          });

      return promise->get_future().get();
    }

## Step 3: Decrypt and verify integrity tokens on your game's backend server next

### Decrypt an integrity token

After you request an integrity verdict, the Play Integrity API provides an
encrypted response token. To obtain the device integrity verdicts, you must
decrypt the integrity token on Google's servers:

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create) within the Google Cloud project that's linked to your app.
2. On your app's server, fetch the access token from your service account
   credentials using the playintegrity scope, and make the following request:

       playintegrity.googleapis.com/v1/<var>PACKAGE_NAME</var>:decodePcIntegrityToken -d \
        '{ "integrity_token": "<var>INTEGRITY_TOKEN</var>" }'

3. Read the JSON response.

The resulting payload is a plain-text token that contains integrity verdicts
and details alongside developer-provided information. A decrypted integrity
token looks as follows:

    {
      "requestDetails": {
        "requestPackageName": "com.your.package.name",
        "requestTime": "2025-08-29T13:10:37.285Z",
        "requestHash": "your_request_hash_string"
      },
      "deviceIntegrity": {
        "deviceRecognitionVerdict": [
          "MEETS_PC_INTEGRITY"
        ]
      },
      "accountDetails": {
        "appLicensingVerdict": "LICENSED"
      }
    }

### Verify the integrity token

The `requestDetails` field of the decoded integrity token contains information
about the request, including developer-provided information in the
`requestHash`.

The `requestHash` and `packageName` fields should match those of the original
request. Therefore, verify the `requestDetails` part of the JSON payload by
making sure that the `requestPackageName` and `requestHash` match what was sent
in the original request, as shown in the following code snippet:

    const auto& request_details = json_payload["requestDetails"];

    if (request_details.value("requestPackageName", "") != <YOUR_PACKAGE_NAME>) {
      // Don't trust the verdicts.
    }

    // Check for the existence of the request_hash.
    // If you set a request hash in the request and it's not present, you shouldn't
    // trust the verdicts.
    if (!request_details.contains("requestHash")) {
        // Don't trust the verdicts.
    }


    // The requestHash from request_details needs to match the request hash your
    // app provided.
    if (request_details.value("requestHash", "") != <PROVIDED_REQUEST_HASH>) {
        // Don't trust the verdicts.
    }

    // You can read the rest of payload's fields.

## Step 4: Decide what action to take based on the integrity verdict

The `deviceIntegrity` field can contain a single value,
`deviceRecognitionVerdict`. You can use this value to determine whether or not
your game is running on a PC that passes Play integrity checks (which is a
`MEETS_PC_INTEGRITY` response). The `accountDetails` field contains a single
value, `appLicensingVerdict`. You can use this value to determine whether or not
the user got licensed from Play. Your game's backend server can collect this
information and use it to determine what action your game should take, such as
allowing a game event to proceed or denying access to risky traffic.

    "deviceIntegrity": {
      "deviceRecognitionVerdict": ["MEETS_PC_INTEGRITY"]
    }
    "accountDetails": {
      "appLicensingVerdict": "LICENSED"
    }

### Device integrity verdicts

`deviceRecognitionVerdict` can have the following values:

`MEETS_PC_INTEGRITY`
:   The game is running on a genuine PC environment, where no on-device tampering
    was detected.

Empty (a blank value)
:   The game is running on a device that has signs of attack (such as API hooking)
    or system compromise (such as device running a tampered Google Desktop
    Services version), or the app is not running on a physical device (such as
    an emulator that does not pass Google Play integrity checks).

### Account details verdicts

`appLicensingVerdict` can have the following values:

`LICENSED`
:   The user has an app entitlement. In other words, the user installed or
    updated your app from Google Play on their device.

`UNLICENSED`
:   The user doesn't have an app entitlement. This happens when, for example, the
    user sideloads your app or doesn't acquire it from Google Play.

`UNEVALUATED`
:   Licensing details were not evaluated because a necessary requirement was
    missed.
    This could happen for several reasons, including the following:

    - The device is not trustworthy enough.
    - The version of your app installed on the device is unknown to Google Play.
    - The user is not signed in to Google Play.

## Step 5: Handle error codes

If your game makes a Play Integrity for PC request and the call fails, your game
receives an error code. These errors can happen for various reasons, such as
environmental issues like a poor network connection, problems with your API
integration, or malicious activity and active attacks.

### Retryable error codes

The cause of these errors is sometimes due to transient conditions, and thus you
should retry the call with an exponential back-off strategy.

| IntegrityError | Error Description | Error Code |
|---|---|---|
| `kNetworkError` | Network connectivity issue on device. | 5 |
| `kTooManyRequests` | Too many requests made from the device. | 6 |
| `kClientTransientError` | A transient issue with the client. | 7 |

See here for more recommendations on [retry strategies](https://developer.android.com/google/play/integrity/error-codes).

### Non-Retryable error codes

Automatic retries are unlikely to help in these cases. However, a manual retry
may help if the user addresses the condition that caused the issue.

| IntegrityError | Error Description | Error Code | Recommended Action |
|---|---|---|---|
| `kError` | Fatal error during SDK action. | 1 | Verify your API implementation before retrying. |
| `kCloudProjectNumberIsInvalid` | The Cloud Project number is invalid. | 2 | Verify that your cloud project number is configured on Google Cloud Console correctly and the requests are made with the correct cloud project number. |
| `kRequestHashTooLong` | The request hash is too long. | 3 | The generated request hashes are too long. Make sure they are less than 500 characters. |
| `kNoValidPreparedTokenFound` | There is no prepared token before making the token request. | 4 | Call the \[PrepareIntegrityToken\]\[prepare-token\] action before making the \[RequestIntegrityToken\]\[request-integrity-token\] call. |
| `kSdkRuntimeUpdateRequired` | An update is needed for the Play for Native SDK. | 8 | Make sure that the Google Play services client on the device is up to date and you are using the latest version of the Play for Native PC SDK. |

## Test different Play Integrity API responses within your app

You can create tests to evaluate how the Play Integrity API interacts with your
app.

1. Set up a Google group (or as many as you desire) with email addresses of
   users. You can select the integrity verdicts or error code these users should
   get in your app from Google Play's servers. This lets you test how your app
   reacts to all possible responses and errors.

2. [Create a ticket here](https://issuetracker.google.com/issues/new?component=1152695&template=2189328) and report which Google group will
   get which API response. Each group is assigned to receive one of the following
   choices:

   |   | Pass licensing verdict | Fail licensing verdict | Unable to evaluate licensing verdict |
   |---|---|---|---|
   | Pass device integrity | `ALLOWLIST_CONFIG_MEETS_PC_INTEGRITY_LICENSED` | `ALLOWLIST_CONFIG_MEETS_PC_INTEGRITY_UNLICENSED` | `ALLOWLIST_CONFIG_MEETS_PC_INTEGRITY_LICENSING_UNEVALUATED` |
   | Fail device integrity | N/A | N/A | `ALLOWLIST_CONFIG_NO_PC_INTEGRITY_LICENSING_UNEVALUATED` |

   If you fail the device integrity verdict, the licensing verdict will always return UNEVALUATED.

   <br />

3. You will be notified once the request has been processed and the test users
   are on the allowlist to receive the predefined integrity verdicts for testing.