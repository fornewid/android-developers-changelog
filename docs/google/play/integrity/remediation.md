---
title: https://developer.android.com/google/play/integrity/remediation
url: https://developer.android.com/google/play/integrity/remediation
source: md.txt
---

This page describes how to handle issues with integrity verdicts.

After an integrity token is requested, you have the option to display a Google
Play dialog to the user. You may display the dialog when there is one or more
issues with the integrity verdict or if an exception occurred during an
Integrity API request. Once the dialog is closed, you can verify that the issue
is fixed with another integrity token request. If you make [standard requests](https://developer.android.com/google/play/integrity/standard), you need to warm up the token provider again
to obtain a fresh verdict.
| **Note:** All integrity dialog types can be shown to users, regardless of the contents of the integrity token. You should check the contents of the integrity token on your server to determine which dialog should be shown.

## Request an integrity dialog to fix a verdict issue

When the client requests an integrity token, you can use the method offered in
the [`StandardIntegrityToken`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#showDialog(android.app.Activity,%20int)) (Standard API) and
[`IntegrityTokenResponse`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse#showDialog(android.app.Activity,%20int)) (Classic API):
`showDialog(Activity activity, int integrityDialogTypeCode)`.
| **Note:** To use integrity dialogs, you must be using Integrity API Android library version 1.3.0 or higher.

The following steps outline how you can use the Play Integrity API to show a
remediation dialog using the [`GET_LICENSED`](https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog) dialog code.
Other dialog codes that your app can request are listed after this section.

1. Request an integrity token from your app, and send the token to your server.
   You can use the Standard or Classic request.

   ### Kotlin

   ```kotlin
   // Request an integrity token
   val tokenResponse: StandardIntegrityToken = requestIntegrityToken()
   // Send token to app server and get response on what to do next
   val yourServerResponse: YourServerResponse = sendToServer(tokenResponse.token())  
   ```

   ### Java

   ```java
   // Request an integrity token
   StandardIntegrityToken tokenResponse = requestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.token());  
   ```

   ### Unity

   ```c#
   // Request an integrity token
   StandardIntegrityToken tokenResponse = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.Token); 
   ```

   ### Unreal Engine

   ```c++
   // Request an integrity token
   StandardIntegrityToken* Response = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse YourServerResponse = SendToServer(Response->Token); 
   ```

   ### Native

   ```c++
   /// Request an integrity token
   StandardIntegrityToken* response = requestIntegrityToken();
   /// Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(StandardIntegrityToken_getToken(response));
   ```
2. On your server, decrypt the integrity token and check the
   `appLicensingVerdict` field. It could look something like this:

   ```json
   // Licensing issue
   {
     ...
     "accountDetails": {
         "appLicensingVerdict": "UNLICENSED"
     }
   }
   ```
3. If the token contains `appLicensingVerdict: "UNLICENSED"`, reply to your app
   client, requesting it show the licensing dialog:

   ### Kotlin

   ```kotlin
   private fun getDialogTypeCode(integrityToken: String): Int{
     // Get licensing verdict from decrypted and verified integritytoken
     val licensingVerdict: String = getLicensingVerdictFromDecryptedToken(integrityToken)

     return if (licensingVerdict == "UNLICENSED") {
             1 // GET_LICENSED
         } else 0
   }
   ```

   ### Java

   ```java
   private int getDialogTypeCode(String integrityToken) {
     // Get licensing verdict from decrypted and verified integrityToken
     String licensingVerdict = getLicensingVerdictFromDecryptedToken(integrityToken);

     if (licensingVerdict.equals("UNLICENSED")) {
       return 1; // GET_LICENSED
     }
     return 0;
   }
   ```

   ### Unity

   ```c#
   private int GetDialogTypeCode(string IntegrityToken) {
     // Get licensing verdict from decrypted and verified integrityToken
     string licensingVerdict = GetLicensingVerdictFromDecryptedToken(IntegrityToken);

     if (licensingVerdict == "UNLICENSED") {
       return 1; // GET_LICENSED
     }
     return 0;
   } 
   ```

   ### Unreal Engine

   ```c++
   private int GetDialogTypeCode(FString IntegrityToken) {
     // Get licensing verdict from decrypted and verified integrityToken
     FString LicensingVerdict = GetLicensingVerdictFromDecryptedToken(IntegrityToken);

     if (LicensingVerdict == "UNLICENSED") {
       return 1; // GET_LICENSED
     }
     return 0;
   } 
   ```

   ### Native

   ```c++
   private int getDialogTypeCode(string integrity_token) {
     /// Get licensing verdict from decrypted and verified integrityToken
     string licensing_verdict = getLicensingVerdictFromDecryptedToken(integrity_token);

     if (licensing_verdict == "UNLICENSED") {
       return 1; // GET_LICENSED
     }
     return 0;
   }
   ```
4. On your app, call `showDialog` with the requested code retrieved from your
   server:

   ### Kotlin

   ```kotlin
   // Show dialog as indicated by the server
   val showDialogType: Int? = yourServerResponse.integrityDialogTypeCode()
   if (showDialogType == null) {
      return
   }

   // Create dialog request
   val dialogRequest = StandardIntegrityDialogRequest.builder()
           .setActivity(activity)
           .setTypeCode(showDialogType)
           .setStandardIntegrityResponse(StandardIntegrityResponse.TokenResponse(token))
           .build()

   // Call showDialog, the dialog will be shown on top of the provided activity
   // and the task will complete when the dialog is closed.
   val result: Task<Int> = standardIntegrityManager.showDialog(dialogRequest)

   // Handle response code, call the Integrity API again to confirm that the
   // verdict issue has been resolved. 
   ```

   ### Java

   ```java
   // Show dialog as indicated by the server
   @Nullable Integer showDialogType = yourServerResponse.integrityDialogTypeCode();
   if (showDialogType == null) {
      return;
   }

   // Create dialog request
   StandardIntegrityDialogRequest dialogRequest =
       StandardIntegrityDialogRequest.builder()
           .setActivity(getActivity())
           .setTypeCode(showDialogTypeCode)
           .setStandardIntegrityResponse(new StandardIntegrityResponse.TokenResponse(token))
           .build();

   // Call showDialog, the dialog will be shown on top of the provided activity
   // and the task will complete when the dialog is closed.
   Task<Integer> result = standardIntegrityManager.showDialog(dialogRequest);

   // Handle response code, call the Integrity API again to confirm that the
   // verdict issue has been resolved.
   ```

   ### Unity

   ```c#
   IEnumerator ShowDialogCoroutine() {
     int showDialogType = yourServerResponse.IntegrityDialogTypeCode();

     // Call showDialog with type code, the dialog will be shown on top of the
     // provided activity and complete when the dialog is closed.
     var showDialogTask = tokenResponse.ShowDialog(showDialogType);

     // Wait for PlayAsyncOperation to complete.
     yield return showDialogTask;

     // Handle response code, call the Integrity API again to confirm that the
     // verdict issue been resolved.
   } 
   ```

   ### Unreal Engine

   ```c++
   // .h
   void MyClass::OnShowDialogCompleted(
     EStandardIntegrityErrorCode Error,
     EIntegrityDialogResponseCode Response)
   {
     // Handle response code, call the Integrity API again to confirm that the
     // verdict issue has been resolved.
   }

   // .cpp
   void MyClass::RequestIntegrityToken()
   {
     UStandardIntegrityToken* Response = ...
     int TypeCode = YourServerResponse.integrityDialogTypeCode();

     // Create a delegate to bind the callback function.
     FShowDialogStandardOperationCompletedDelegate Delegate;

     // Bind the completion handler (OnShowDialogCompleted) to the delegate.
     Delegate.BindDynamic(this, &MyClass::OnShowDialogCompleted);

     // Call ShowDialog with TypeCode which completes when the dialog is closed.
     Response->ShowDialog(TypeCode, Delegate);
   }
   ```

   ### Native

   ```c++
   // Show dialog as indicated by the server
   int show_dialog_type = yourServerResponse.integrityDialogTypeCode();
   if(show_dialog_type == 0){
   return;
   }

   /// Create dialog request
   StandardIntegrityDialogRequest* dialog_request;
   StandardIntegrityDialogRequest_create(&dialog_request);
   StandardIntegrityDialogRequest_setTypeCode(dialog_request, show_dialog_type);
   StandardIntegrityDialogRequest_setActivity(dialog_request, activity);
   StandardIntegrityDialogRequest_setStandardIntegrityToken(dialog_request,
                                                 token_response);

   /// Call showDialog with the dialog request. The dialog will be shown on top
   /// of the provided activity and complete when the dialog is closed by the
   /// user.
   StandardIntegrityDialogResponse* dialog_response;
   StandardIntegrityErrorCode error_code =
     StandardIntegrityManager_showDialog(dialog_request, &dialog_response);

   /// Use polling to wait for the async operation to complete. Note, the polling
   /// shouldn't block the thread where the StandardIntegrityManager is running.
   IntegrityDialogResponseCode response_code = INTEGRITY_DIALOG_RESPONSE_UNKNOWN;
   while (error_code == STANDARD_INTEGRITY_NO_ERROR) {
     error_code = StandardIntegrityDialogResponse_getResponseCode(dialog_response, &response_code);
     if(response_code != INTEGRITY_DIALOG_RESPONSE_UNKNOWN){
       break;
     }
   }

   /// Free memory
   StandardIntegrityDialogRequest_destroy(dialog_request);
   StandardIntegrityDialogResponse_destroy(dialog_response);

   /// Handle response code, call the Integrity API again to confirm that the
   /// verdict issues have been resolved.
   ```
5. The dialog is displayed on top of the provided activity. When the user has
   closed the dialog, the Task completes with a [response code](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode).

6. (Optional) Request another token to display any further dialogs. If you make
   [standard requests](https://developer.android.com/google/play/integrity/standard), you need to warm up
   the token provider again to obtain a fresh verdict.

## Request an integrity dialog to fix a client side exception

If an Integrity API request fails with a [`StandardIntegrityException`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException)
(Standard API) or [`IntegrityServiceException`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException) (Classic API) and the
exception is remediable, you can use either the [`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog) or
[`GET_STRONG_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog) dialogs to fix the error.
| **Note:** Using the new `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialogs requires the Integrity API Android library version 1.5.0 or higher. This update provides access to the new `showDialog` method in [`IntegrityManager`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager) (Classic API) or [`StandardIntegrityManager`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager) (Standard API) for resolving client-side exceptions.

The following steps outline how you can use the [`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog)
dialog to fix a remediable client side error reported by Integrity API.

1. Check that the exception returned from an Integrity API request is remediable.

   <br />

   ### Kotlin

   ```kotlin
   private fun isExceptionRemediable(exception: ExecutionException): Boolean {
     val cause = exception.cause
     if (cause is StandardIntegrityException && cause.isRemediable) {
         return true
     }
     return false
   }
   ```

   <br />

   <br />

   ### Java

   ```java
   private boolean isExceptionRemediable(ExecutionException exception) {
     Throwable cause = exception.getCause();
     if (cause instanceof StandardIntegrityException integrityException
   && integrityException.isRemediable()) {
         return true;
     }
     return false;
   }
   ```

   <br />

   ### Native

   ```c++
   bool IsErrorRemediable(StandardIntegrityToken* token) {
     /// Check if the error associated with the token is remediable
     bool isRemediable = false;
     if(StandardIntegrityToken_getIsRemediable(response, &isRemediable) == STANDARD_INTEGRITY_NO_ERROR){
       return isRemediable;
     }
     return false;
   }
   ```

<br />

<br />

1. If the exception is remediable, request the `GET_INTEGRITY` dialog using the
   returned exception. The dialog will be displayed over the provided activity and
   the returned Task completes with a [response code](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode) after the user closes the
   dialog.

   ### Kotlin

   ```kotlin
   private fun showDialog(exception: StandardIntegrityException) {
     // Create a dialog request
     val standardIntegrityDialogRequest =
         StandardIntegrityDialogRequest.builder()
             .setActivity(activity)
             .setType(IntegrityDialogTypeCode.GET_INTEGRITY)
             .setStandardIntegrityResponse(ExceptionDetails(exception))
             .build()

     // Request dialog
     val responseCode: Task<Int> =
           standardIntegrityManager.showDialog(standardIntegrityDialogRequest)
   }
    
   ```

   ### Java

   ```java
   private void showDialog(StandardIntegrityException exception) {
     // Create a dialog request
     StandardIntegrityDialogRequest standardIntegrityDialogRequest =
         StandardIntegrityDialogRequest.builder()
             .setActivity(this.activity)
             .setType(IntegrityDialogTypeCode.GET_INTEGRITY)
             .setStandardIntegrityResponse(new ExceptionDetails(exception))
             .build();

     // Request dialog
     Task<Integer> responseCode =
           standardIntegrityManager.showDialog(standardIntegrityDialogRequest);
   }  
   ```

   ### Native

   ```c++
   private void showDialogToFixError(StandardIntegrityToken* token) {
     /// If the token request failed, and the underlying error is not fixable
     /// then return early
     if(isErrorRemediable(token)) {
       return;
     }

     /// Create dialog request
     StandardIntegrityDialogRequest* dialog_request;
     StandardIntegrityDialogRequest_create(&dialog_request);
     StandardIntegrityDialogRequest_setTypeCode(dialog_request,
                                        kGetIntegrityDialogTypeCode);
     StandardIntegrityDialogRequest_setActivity(dialog_request, activity);
     StandardIntegrityDialogRequest_setStandardIntegrityToken(dialog_request,
                                                     token_response);

     /// Call showDialog with the dialog request. The dialog will be shown on
     /// top of the provided activity and complete when the dialog is closed by
     /// the user.
     StandardIntegrityDialogResponse* dialog_response;
     StandardIntegrityErrorCode error_code =
         StandardIntegrityManager_showDialog(dialog_request, &dialog_response);

     /// Use polling to wait for the async operation to complete.
     /// Note, the polling shouldn't block the thread where the
     /// StandardIntegrityManager is running.
     IntegrityDialogResponseCode response_code = INTEGRITY_DIALOG_RESPONSE_UNKNOWN;
     while (error_code == STANDARD_INTEGRITY_NO_ERROR) {
         error_code = StandardIntegrityDialogResponse_getResponseCode(response, &response_code);
         if(response_code != INTEGRITY_DIALOG_RESPONSE_UNKNOWN){
           break;
         }
     }

     /// Free memory
     StandardIntegrityDialogRequest_destroy(dialog_request);
     StandardIntegrityDialogResponse_destroy(dialog_response);

   }
   ```
2. If the returned response code indicates a success, the next request for an
   integrity token should succeed without any exceptions. If you make standard
   requests, you need to warm up the token provider again to obtain a fresh
   verdict.

## Integrity dialog codes

### [GET_LICENSED](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_LICENSED) (Type Code 1)

#### Verdict issue

This dialog is appropriate for two issues:

- **Unauthorized access** : `appLicensingVerdict: "UNLICENSED"`. This means the user account does not have an entitlement for your app, which can happen if the user sideloaded it or acquired it from a different app store than Google Play.
- **Tampered app** : `appRecognitionVerdict: "UNRECOGNIZED_VERSION"`. This means that your app's binary has been modified or is not a version recognized by Google Play.

| **Note:** The [`GET_INTEGRITY`](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog) dialog addresses the same issues as `GET_LICENSED` in addition to addressing device integrity issues and remediable error codes.

#### Remediation

You can show the `GET_LICENSED` dialog to prompt the user to acquire the
genuine app from Google Play. This single dialog addresses both scenarios:

- For an *unlicensed* user, it grants them a Play license. This enables the user to receive app updates from Google Play.
- For a user with a *tampered* app version, it guides them to installing the unmodified app from Google Play.

When the user completes the dialog, subsequent integrity checks return
`appLicensingVerdict: "LICENSED"` and `appRecognitionVerdict: "PLAY_RECOGNIZED"`.

#### Example UX

![](https://developer.android.com/static/images/google/play/integrity/get_licensing_ux.png) **Figure 1.** GET_LICENSED Play dialog.

### [CLOSE_UNKNOWN_ACCESS_RISK](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_UNKNOWN_ACCESS_RISK) (Type Code 2)

#### Verdict issue

When `environmentDetails.appAccessRiskVerdict.appsDetected` contains
`"UNKNOWN_CAPTURING"` or `"UNKNOWN_CONTROLLING"`, it means there are other apps
(not installed by Google Play or preloaded on the system partition by the device
manufacturer) running on the device that could be capturing the screen or
controlling the device.

#### Remediation

You can show the `CLOSE_UNKNOWN_ACCESS_RISK` dialog to prompt the user to close
all unknown apps which could be capturing the screen or controlling the device.
If the user taps the `Close all` button, all such apps are closed.

#### Example UX

![](https://developer.android.com/static/images/google/play/integrity/close_unknown_access_risk_ux.png) **Figure 2.** Dialog for close unknown access risk.

### [CLOSE_ALL_ACCESS_RISK](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#CLOSE_ALL_ACCESS_RISK) (Type Code 3)

#### Verdict issue

When `environmentDetails.appAccessRiskVerdict.appsDetected` contains any of
`"KNOWN_CAPTURING"`, `"KNOWN_CONTROLLING"`,`"UNKNOWN_CAPTURING"` or
`"UNKNOWN_CONTROLLING"`, it means there are apps running on the device that
could be capturing the screen or controlling the device.

#### Remediation

You can show the `CLOSE_ALL_ACCESS_RISK` dialog to prompt the user to close all
the apps which could be capturing the screen or controlling the device. If the
user taps the `Close all` button, all such apps are closed on the device.

#### Example UX

![](https://developer.android.com/static/images/google/play/integrity/close_unknown_access_risk_ux.png) **Figure 3.** Dialog for close all access risk.

### [GET_INTEGRITY](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_INTEGRITY) (Type Code 4)

#### Verdict issue

This dialog is appropriate for any of the following issues:

- **Weak device integrity** : When the `deviceRecognitionVerdict` does
  not contain `MEETS_DEVICE_INTEGRITY`, the device might not be a genuine and
  certified Android device. This can happen, for example, if the
  device's bootloader is unlocked or its loaded Android OS is not a certified
  manufacturer image.

- **Unauthorized access** : `appLicensingVerdict: "UNLICENSED"`. This means the
  user account does not have an entitlement for your app, which can happen if the
  user sideloaded it or acquired it from a different app store than Google Play.

- **Tampered app** : `appRecognitionVerdict: "UNRECOGNIZED_VERSION"`. This means
  that your app's binary has been modified or is not a version recognized by
  Google Play.

- **Client side exceptions** : When a remediable exception occurs during an
  Integrity API request. Remediable exceptions are Integrity API exceptions with
  error codes like
  `PLAY_SERVICES_VERSION_OUTDATED`, `NETWORK_ERROR`, `PLAY_SERVICES_NOT_FOUND`,
  etc. You can use the [`exception.isRemediable()`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#isRemediable()) method to check if an
  exception is fixable by the dialog.

#### Remediation

The `GET_INTEGRITY` dialog is designed to streamline the user's experience by
handling multiple remediation steps within a single, continuous flow. This
prevents the user from having to interact with multiple separate dialogs to fix
different issues.

When you request the dialog, it automatically detects which of the targeted
verdict issues are present and provides the appropriate remediation steps.
This means a single dialog request can address multiple problems at once,
including:

- **Device integrity** : If a device integrity issue is detected, the dialog will guide the user to improve the device's security status to meet the requirements for a `MEETS_DEVICE_INTEGRITY` verdict.
- **App integrity**: If issues like unauthorized access or app tampering are detected, the dialog will direct users to acquire the app from the Play Store to fix them.

| **Note:** `GET_INTEGRITY` dialog automatically detects and tries to resolve multiple verdict issues when requested. To remediate only issues with account licensing or app integrity, we recommend using the [`GET_LICENSED`](https://developer.android.com/google/play/integrity/remediation#get-licensed-dialog) dialog.

- **Client-side exceptions**: The dialog checks for and attempts to resolve any underlying issues that caused an Integrity API exception. For example, it might prompt the user to update an outdated version of Google Play services.

#### Example UX

![](https://developer.android.com/static/images/google/play/integrity/get_integrity_network_error_ux.gif) **Figure 4.** GET_INTEGRITY dialog network error remediation flow

### [GET_STRONG_INTEGRITY](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode#GET_STRONG_INTEGRITY) (Type Code 5)

#### Verdict issue

This dialog is designed to fix all of the same issues that
[GET_INTEGRITY](https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog)
addresses, with the added capability of fixing problems that prevent a device
from receiving a `MEETS_STRONG_INTEGRITY` verdict and fixing Play Protect
verdict issues.
| **Note:** [MEETS_STRONG_INTEGRITY](https://developer.android.com/google/play/integrity/verdicts#optional-device-labels) and [playProtectVerdict](https://developer.android.com/google/play/integrity/verdicts#environment-details-field) are optional verdicts and, you should only check for them if you've [opted in to receive additional labels](https://developer.android.com/google/play/integrity/setup#configure-api).

#### Remediation

`GET_STRONG_INTEGRITY` is designed to streamline the user's experience by
handling multiple remediation steps within a single, continuous flow. The dialog
automatically checks for an address applicable integrity problems, including:

- **Device integrity** : If a device integrity issue is detected, the dialog will guide the user to improve the device's security status to meet the requirements for a `MEETS_STRONG_INTEGRITY` verdict.
- **Play protect status** : If the `playProtectVerdict` indicates an issue, the
  dialog will guide the user to fix it:

  - If Play Protect is disabled (`playProtectVerdict == POSSIBLE_RISK`), the dialog will prompt the user to enable it and perform a scan of all apps on the device.
  - If harmful apps are detected (`playProtectVerdict == MEDIUM_RISK` or `HIGH_RISK`), the dialog will direct the user to uninstall them using Google Play Protect.
- **App integrity**: If issues like unauthorized access or app tampering are
  detected, the dialog will prompt the user to acquire the app from the Play Store
  to fix the problem.

- **Client-side exceptions** : The dialog also attempts to resolve any underlying
  issues that caused an Integrity API exception. For example, it may prompt the
  user to enable Google Play services if it's found to be disabled. Remediable
  exceptions are Integrity API exceptions with error codes like
  `PLAY_SERVICES_VERSION_OUTDATED`,
  `NETWORK_ERROR`, or
  `PLAY_SERVICES_NOT_FOUND`.
  You can use the [`exception.isRemediable()`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#isRemediable()) method to check if an error is
  fixable by the dialog.

#### Example UX

![](https://developer.android.com/static/images/google/play/integrity/get_strong_integrity_update_play_services_ux.gif) **Figure 5.** GET_STRONG_INTEGRITY dialog updating Play services.