---
title: Remediation dialogs  |  Play Integrity  |  Android Developers
url: https://developer.android.com/google/play/integrity/remediation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Integrity](https://developer.android.com/google/play/integrity)

# Remediation dialogs Stay organized with collections Save and categorize content based on your preferences.




This page describes how to handle issues with integrity verdicts.

After an integrity token is requested, you have the option to display a Google
Play dialog to the user. You may display the dialog when there is one or more
issues with the integrity verdict or if an exception occurred during an
Integrity API request. Once the dialog is closed, you can verify that the issue
is fixed with another integrity token request. If you make [standard requests](/google/play/integrity/standard), you need to warm up the token provider again
to obtain a fresh verdict.

**Note:** All integrity dialog types can be shown to users, regardless of the
contents of the integrity token. You should check the contents of the integrity
token on your server to determine which dialog should be shown.

## Request an integrity dialog to fix a verdict issue

When the client requests an integrity token, you can use the method offered in
the [`StandardIntegrityToken`](/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#showDialog(android.app.Activity,%20int)) (Standard API) and
[`IntegrityTokenResponse`](/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse#showDialog(android.app.Activity,%20int)) (Classic API):
`showDialog(Activity activity, int integrityDialogTypeCode)`.

**Note:** To use integrity dialogs, you must be using Integrity API Android library
version 1.3.0 or higher.

The following steps outline how you can use the Play Integrity API to show a
remediation dialog using the [`GET_LICENSED`](#get-licensed-dialog) dialog code.
Other dialog codes that your app can request are listed after this section.

1. Request an integrity token from your app, and send the token to your server.
   You can use the Standard or Classic request.

   ### Kotlin

   ```
   // Request an integrity token
   val tokenResponse: StandardIntegrityToken = requestIntegrityToken()
   // Send token to app server and get response on what to do next
   val yourServerResponse: YourServerResponse = sendToServer(tokenResponse.token())
   ```

   ### Java

   ```
   // Request an integrity token
   StandardIntegrityToken tokenResponse = requestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.token());
   ```

   ### Unity

   ```
   // Request an integrity token
   StandardIntegrityToken tokenResponse = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.Token);
   ```

   ### Unreal Engine

   ```
   // Request an integrity token
   StandardIntegrityToken* Response = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse YourServerResponse = SendToServer(Response->Token);
   ```

   ### Native

   ```
   /// Request an integrity token
   StandardIntegrityToken* response = requestIntegrityToken();
   /// Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(StandardIntegrityToken_getToken(response));
   ```
2. On your server, decrypt the integrity token and check the
   `appLicensingVerdict` field. It could look something like this:

   ```
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

   ```
   private fun getDialogTypeCode(integrityToken: String): Int{
     // Get licensing verdict from decrypted and verified integritytoken
     val licensingVerdict: String = getLicensingVerdictFromDecryptedToken(integrityToken)

     return if (licensingVerdict == "UNLICENSED") {
             1 // GET_LICENSED
         } else 0
   }
   ```

   ### Java

   ```
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

   ```
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

   ```
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

   ```
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

   ```
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

   ```
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

   ```
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

   ```
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

   ```
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
   closed the dialog, the Task completes with a [response code](/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode).
6. (Optional) Request another token to display any further dialogs. If you make
   [standard requests](/google/play/integrity/standard), you need to warm up
   the token provider again to obtain a fresh verdict.

## Request an integrity dialog to fix a client side exception

If an Integrity API request fails with a [`StandardIntegrityException`](/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException)
(Standard API) or [`IntegrityServiceException`](/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException) (Classic API) and the
exception is remediable, you can use either the [`GET_INTEGRITY`](#get-integrity-dialog) or
[`GET_STRONG_INTEGRITY`](#get-strong-integrity-dialog) dialogs to fix the error.

**Note:** Using the new `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialogs
requires the Integrity API Android library version 1.5.0 or higher. This
update provides access to the new `showDialog` method in
[`IntegrityManager`](/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager) (Classic API) or [`StandardIntegrityManager`](/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager)
(Standard API) for resolving client-side exceptions.

The following steps outline how you can use the [`GET_INTEGRITY`](#get-integrity-dialog)
dialog to fix a remediable client side error reported by Integrity API.

1. Check that the exception returned from an Integrity API request is remediable.

   ### Kotlin

   ```
   private fun isExceptionRemediable(exception: ExecutionException): Boolean {
     val cause = exception.cause
     if (cause is StandardIntegrityException && cause.isRemediable) {
         return true
     }
     return false
   }
   ```