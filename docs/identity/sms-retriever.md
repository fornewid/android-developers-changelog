---
title: https://developer.android.com/identity/sms-retriever
url: https://developer.android.com/identity/sms-retriever
source: md.txt
---

To automatically verify phone numbers, you must implement both the client and
server portions of the verification flow. This document describes how to
implement the client portion in an Android app.

To start the phone number verification flow in an Android app, you send the
phone number to your verification server and call the SMS Retriever API to begin
listening for an SMS message containing a one-time code for your app. After you
receive the message, you send the one-time code back to your server to complete
the verification process.

To prepare your app, complete the steps in the following sections.

## App prerequisites

Make sure that your app's build file uses the following values:

- A minSdkVersion of 19 or higher
- A compileSdkVersion of 28 or higher

## Configure your app

In your project-level `build.gradle` file, include
[Google's Maven repository](https://maven.google.com/web/index.html) and [Maven central repository](https://search.maven.org/artifact) in both your
`buildscript` and `allprojects` sections:

    buildscript {
        repositories {
            google()
            mavenCentral()
        }
    }

    allprojects {
        repositories {
            google()
            mavenCentral()
        }
    }

Add the [Google Play services](http://developer.google.com/android) dependency for the SMS Retriever API to your
[module's Gradle build file](https://developer.android.com/studio/build#module-level), which is commonly `app/build.gradle`:

    dependencies {
      implementation 'com.google.android.gms:play-services-auth:21.5.1'
      implementation 'com.google.android.gms:play-services-auth-api-phone:18.3.0'
    }

## Obtain the user's phone number

You can obtain the user's phone number in whatever way is appropriate for your
app. Often, it is the best user experience to use the hint picker to prompt the
user to choose from the phone numbers stored on the device and thereby avoid
having to manually type a phone number. To use the hint picker:

    // Construct a request for phone numbers and show the picker
    private void requestHint() {
        HintRequest hintRequest = new HintRequest.Builder()
                .setPhoneNumberIdentifierSupported(true)
                .build();

        PendingIntent intent = Auth.CredentialsApi.getHintPickerIntent(
                apiClient, hintRequest);
        startIntentSenderForResult(intent.getIntentSender(),
                RESOLVE_HINT, null, 0, 0, 0);
    }

    // Obtain the phone number from the result
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
      super.onActivityResult(requestCode, resultCode, data);
      if (requestCode == RESOLVE_HINT) {
          if (resultCode == RESULT_OK) {
              Credential credential = data.getParcelableExtra(Credential.EXTRA_KEY);
              // credential.getId();  <-- will need to process phone number string
          }
      }
    }

## Start the SMS retriever

When you are ready to verify the user's phone number, get an instance of the
`SmsRetrieverClient` object, call `startSmsRetriever`, and attach success and
failure listeners to the SMS retrieval task:

    // Get an instance of SmsRetrieverClient, used to start listening for a matching
    // SMS message.
    SmsRetrieverClient client = SmsRetriever.getClient(this /* context */);

    // Starts SmsRetriever, which waits for ONE matching SMS message until timeout
    // (5 minutes). The matching SMS message will be sent using a Broadcast Intent
    // with action SmsRetriever#SMS_RETRIEVED_ACTION.
    Task<Void> task = client.startSmsRetriever();

    // Listen for success/failure of the start Task. If in a background thread, this
    // can be made blocking using Tasks.await(task, [timeout]);
    task.addOnSuccessListener(new OnSuccessListener<Void>() {
      @Override
      public void onSuccess(Void aVoid) {
        // Successfully started retriever, expect broadcast intent
        // ...
      }
    });

    task.addOnFailureListener(new OnFailureListener() {
      @Override
      public void onFailure(@NonNull Exception e) {
        // Failed to start retriever, inspect Exception for more details
        // ...
      }
    });

The SMS retrieval task listens for up to five minutes for an SMS message that
contains a unique string that identifies your app.

## Send the phone number to your server

After you have obtained the user's phone number and started to listen for SMS
messages, send the user's phone number to your verification server using any
method (usually with an HTTPS POST request).

Your server generates a verification message and sends it by SMS to the phone
number you specified. See [Perform SMS Verification on the Server](https://developers.google.com/identity/sms-retriever/verify).

## Receive verification messages

When a verification message is received on the user's device, Play services
explicitly broadcasts to your app a `SmsRetriever.SMS_RETRIEVED_ACTION` Intent,
which contains the text of the message. Use a `BroadcastReceiver` to receive
this verification message.

In the `BroadcastReceiver`'s `onReceive` handler, get the text of the
verification message (and optionally the sender address) from the Intent's
extras:

    /**
      *   BroadcastReceiver to wait for SMS messages. This can be registered either
      *   in the AndroidManifest or at runtime. Filters Intents on
      *   SmsRetriever.SMS_RETRIEVED_ACTION.
      */
    public class MySMSBroadcastReceiver extends BroadcastReceiver {

      @Override
      public void onReceive(Context context, Intent intent) {
        if (SmsRetriever.SMS_RETRIEVED_ACTION.equals(intent.getAction())) {
          Bundle extras = intent.getExtras();
          Status status = (Status) extras.get(SmsRetriever.EXTRA_STATUS);

          switch(status.getStatusCode()) {
            case CommonStatusCodes.SUCCESS:
              // (Optional) Get SMS Sender address - only available in
              // GMS version 24.20 onwards, else it will return null
              String senderAddress = extras.getString(SmsRetriever.EXTRA_SMS_ORIGINATING_ADDRESS);
              // Get SMS message contents
              String message = extras.getString(SmsRetriever.EXTRA_SMS_MESSAGE);
              // Extract one-time code from the message and complete verification
              // by sending the code back to your server.
              break;
            case CommonStatusCodes.TIMEOUT:
              // Waiting for SMS timed out (5 minutes)
              // Handle the error ...
              break;
          }
        }
      }
    }

To register this `BroadcastReceiver`, use the following:

- **Intent filter:** `com.google.android.gms.auth.api.phone.SMS_RETRIEVED` (the value of the `SmsRetriever.SMS_RETRIEVED_ACTION` constant)
- **Permission:** `com.google.android.gms.auth.api.phone.permission.SEND` (the value of the `SmsRetriever.SEND_PERMISSION` constant)

You can register the receiver in your app's `AndroidManifest.xml` file, as in
the following example, or dynamically using `Context.registerReceiver`.

    <receiver android:name=".MySMSBroadcastReceiver" android:exported="true"
              android:permission="com.google.android.gms.auth.api.phone.permission.SEND">
        <intent-filter>
            <action android:name="com.google.android.gms.auth.api.phone.SMS_RETRIEVED"/>
        </intent-filter>
    </receiver>

> [!IMPORTANT]
> **Important:** You can detect that the broadcast intent is from SMS Retriever API by adding the `com.google.android.gms.auth.api.phone.permission.SEND` permission to your receiver. This permission setting is available in Google Play services version 19.8.31 or higher.

> [!IMPORTANT]
> **Important:** Don't add the permission `com.google.android.gms.auth.api.phone.permission.SEND` to your app. This permission should only be used to detect the intent is from the SMS Retriever API on the broadcast receiver.

## Send the one-time code from the verification message to your server

Now that you have the text of the verification message, use a regular expression
or some other logic to get the one-time code from the message. The format of the
one-time code depends on how you implemented them in your server.

Finally, send the one-time code to your server over a secure connection. When
your server receives the one-time code, it records that the phone number has
been verified.

> [!IMPORTANT]
> **Important:** You must perform verification of the one-time code on your server, and not in your client app.