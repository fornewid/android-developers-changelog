---
title: https://developer.android.com/privacy-and-security/security-android-protected-confirmation
url: https://developer.android.com/privacy-and-security/security-android-protected-confirmation
source: md.txt
---

To help you confirm users' intentions when they initiate a sensitive
transaction, such as making a payment, supported devices that run Android 9 (API
level 28) or higher let you use Android Protected Confirmation. When using this
workflow, your app displays a prompt to the user, asking them to approve a short
statement that reaffirms their intent to complete the sensitive transaction.

If the user accepts the statement, your app can use a key from Android Keystore
to sign the message shown in the dialog. The signature indicates, with very high
confidence, that the user has seen the statement and has agreed to it.  
**Caution:**Android Protected Confirmation doesn't provide a
secure information channel for the user. Your app can't assume any
confidentiality guarantees beyond those that the Android platform offers. In
particular, don't use this workflow to display sensitive information that you
wouldn't ordinarily show on the user's device.

After the user confirms the message, the message's integrity is assured,
but your app must still use data-in-transit encryption to protect the
confidentiality of the signed message.

To provide support for high-assurance user confirmation in your app, complete
the following steps:

1. [Generate an asymmetric signing key](https://developer.android.com/training/articles/keystore#GeneratingANewPrivateKey)
   using the
   [`KeyGenParameterSpec.Builder`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder)
   class. When creating the key, pass `true` into
   [`setUserConfirmationRequired()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUserConfirmationRequired(boolean)).
   Also, call [`setAttestationChallenge()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestationChallenge(byte%5B%5D)),
   passing a suitable challenge value provided by the relying party.

2. Enroll the newly generated key and your key's attestation certificate with
   the appropriate relying party.

3. Send transaction details to your server and have it generate and return a
   binary large object (BLOB) of *extra data*. Extra data might include the
   to-be-confirmed data or parsing hints, such as the locale of the prompt string.

   For a more secure implementation, the BLOB must contain a cryptographic
   nonce for protection against
   [replay attacks](https://www.pcmag.com/encyclopedia/term/50439/replay-attack)
   and to disambiguate transactions.
   | **Caution:** If the extra data field includes to-be-confirmed data, the relying party must verify the equivalent data that's sent with the prompt string. Android Protected Confirmation doesn't render the extra data, so your app can't assume that the user confirmed this data.
4. Set up the
   [`ConfirmationCallback`](https://developer.android.com/reference/android/security/ConfirmationCallback)
   object that informs your app when the user has accepted the prompt shown in a
   confirmation dialog:

   ### Kotlin

   ```kotlin
   class MyConfirmationCallback : ConfirmationCallback() {

         override fun onConfirmed(dataThatWasConfirmed: ByteArray?) {
             super.onConfirmed(dataThatWasConfirmed)
             // Sign dataThatWasConfirmed using your generated signing key.
             // By completing this process, you generate a signed statement.
         }

         override fun onDismissed() {
             super.onDismissed()
             // Handle case where user declined the prompt in the
             // confirmation dialog.
         }

         override fun onCanceled() {
             super.onCanceled()
             // Handle case where your app closed the dialog before the user
             // responded to the prompt.
         }

         override fun onError(e: Exception?) {
             super.onError(e)
             // Handle the exception that the callback captured.
         }
     }
   ```

   ### Java

   ```java
   public class MyConfirmationCallback extends ConfirmationCallback {

     @Override
     public void onConfirmed(@NonNull byte[] dataThatWasConfirmed) {
         super.onConfirmed(dataThatWasConfirmed);
         // Sign dataThatWasConfirmed using your generated signing key.
         // By completing this process, you generate a signed statement.
     }

     @Override
     public void onDismissed() {
         super.onDismissed();
         // Handle case where user declined the prompt in the
         // confirmation dialog.
     }

     @Override
     public void onCanceled() {
         super.onCanceled();
         // Handle case where your app closed the dialog before the user
         // responded to the prompt.
     }

     @Override
     public void onError(Throwable e) {
         super.onError(e);
         // Handle the exception that the callback captured.
     }
   }
   ```

   If the user approves the dialog, the `onConfirmed()` callback is
   called. The `dataThatWasConfirmed` BLOB is a
   [CBOR data structure](http://cbor.io/) that contains,
   among other details, the prompt text that the user saw as well as the extra
   data that you passed into the
   [`ConfirmationPrompt`](https://developer.android.com/reference/android/security/ConfirmationPrompt)
   builder. Use the previously created key to sign the
   `dataThatWasConfirmed` BLOB, then pass this BLOB, along with the
   signature and transaction details, back to the relying party.
   | **Note:** Because the key was created using [`setUserConfirmationRequired()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUserConfirmationRequired(boolean)), it can only be used to sign data that's returned in the `dataThatWasConfirmed` parameter. Attempting to sign any other kind of data fails.

   To make full use of the security assurance that Android Protected
   Confirmation offers, the relying party must perform the following steps upon
   receiving a signed message:
   1. Check the signature over the message as well as the attestation certificate chain of the signing key.
   2. Check that the attestation certificate has the `TRUSTED_CONFIRMATION_REQUIRED` flag set, which indicates that the signing key requires trusted user confirmation. If the signing key is an RSA key, check that it doesn't have the [`PURPOSE_ENCRYPT`](https://developer.android.com/reference/android/security/keystore/KeyProperties#PURPOSE_ENCRYPT) or [`PURPOSE_DECRYPT`](https://developer.android.com/reference/android/security/keystore/KeyProperties#PURPOSE_DECRYPT) property.
   3. Check `extraData` to make sure that this confirmation message belongs to a new request and hasn't been processed yet. This step protects against replay attacks.
   4. Parse the `promptText` for information about the confirmed action or request. Remember that the `promptText` is the only part of the message that the user actually confirmed. The relying party must never assume that to-be confirmed data included in `extraData` corresponds to the `promptText`.
5. Add logic similar to that shown in the following code snippet to display the
   dialog itself:

   ### Kotlin

   ```kotlin
   // This data structure varies by app type. This is an example.
     data class ConfirmationPromptData(val sender: String,
             val receiver: String, val amount: String)

     val myExtraData: ByteArray = byteArrayOf()
     val myDialogData = ConfirmationPromptData("Ashlyn", "Jordan", "$500")
     val threadReceivingCallback = Executor { runnable -> runnable.run() }
     val callback = MyConfirmationCallback()

     val dialog = ConfirmationPrompt.Builder(context)
             .setPromptText("${myDialogData.sender}, send
                             ${myDialogData.amount} to
                             ${myDialogData.receiver}?")
             .setExtraData(myExtraData)
             .build()
     dialog.presentPrompt(threadReceivingCallback, callback)
   ```

   ### Java

   ```java
     // This data structure varies by app type. This is an example.
     class ConfirmationPromptData {
         String sender, receiver, amount;
         ConfirmationPromptData(String sender, String receiver, String amount) {
             this.sender = sender;
             this.receiver = receiver;
             this.amount = amount;
         }
     };
     final int MY_EXTRA_DATA_LENGTH = 100;
     byte[] myExtraData = new byte[MY_EXTRA_DATA_LENGTH];
     ConfirmationPromptData myDialogData = new ConfirmationPromptData("Ashlyn", "Jordan", "$500");
     Executor threadReceivingCallback = Runnable::run;
     MyConfirmationCallback callback = new MyConfirmationCallback();
     ConfirmationPrompt dialog = (new ConfirmationPrompt.Builder(getApplicationContext()))
             .setPromptText("${myDialogData.sender}, send ${myDialogData.amount} to ${myDialogData.receiver}?")
             .setExtraData(myExtraData)
             .build();
     dialog.presentPrompt(threadReceivingCallback, callback);
   ```
   | **Note:** The confirmation prompt UI, which consists of a full-screen dialog, isn't customizable. However, the framework takes care of localizing button text for you.

## Additional resources

For more information about Android Protected Confirmation, consult the following
resources.

### Blogs

- [Android Protected Confirmation: Taking transaction security to the next
  level](https://android-developers.googleblog.com/2018/10/android-protected-confirmation.html)