---
title: https://developer.android.com/identity/phone-number-hint
url: https://developer.android.com/identity/phone-number-hint
source: md.txt
---

The Phone Number Hint API, a library powered by [Google Play services](https://developers.google.com/android),
provides a frictionless way to show a user's (SIM-based) phone numbers as a
hint.

The benefits to using Phone Number Hint include the following:

- No additional permission requests are needed
- Eliminates the need for the user to manually type in the phone number
- No Google Account is needed
- Not directly tied to sign-in or sign-up workflows
- Wider support for Android versions compared to Autofill

## How it works

The Phone Number Hint API utilizes a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)
to initiate the flow. Once the PendingIntent has been launched the user will be
presented with a UI, listing out all (SIM-based) phone numbers. The user can
then choose to select a phone number they would like to use or cancel the flow.
The selected phone number will then be made available to the developer to
retrieve from the [`Intent`](https://developer.android.com/reference/android/content/Intent).
![Phone Number Hint UI and Settings.](https://developer.android.com/static/identity/phone-number-hint/images/phone_number_hint_ui.png) **Figure 1.** Phone Number Hint UI and Settings

To prepare your app, complete the steps in the following sections.

## Configure your app

Add the [Google Play services](https://developers.google.com/android)
dependency for the Phone Number Hint API to your
[module's Gradle build file](https://developer.android.com/studio/build#module-level),
which is commonly `app/build.gradle`:

      apply plugin: 'com.android.application'

      ...

      dependencies {
        implementation 'com.google.android.gms:play-services-auth:21.5.1'
      }

### Create a GetPhoneNumbeHintIntentRequest object

Start by creating a [`GetPhoneNumberHintIntentRequest`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/GetPhoneNumberHintIntentRequest) object using the
provided [`GetPhoneNumberHintIntentRequest.Builder()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/GetPhoneNumberHintIntentRequest.Builder)
method. This request object can then be used to get an `Intent` to start the
Phone Number Hint flow.

### Kotlin

```kotlin
val request: GetPhoneNumberHintIntentRequest = GetPhoneNumberHintIntentRequest.builder().build()
```

### Java

```java
GetPhoneNumberHintIntentRequest request = GetPhoneNumberHintIntentRequest.builder().build();
```

### Requesting Phone Number Hint

Call [`SignInClient.getPhoneNumberHintIntent()`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/SignInClient#getPhoneNumberHintIntent(com.google.android.gms.auth.api.identity.GetPhoneNumberHintIntentRequest)),
passing in the previous `GetPhoneNumberHintIntentRequest` object,
to retrieve the `PendingIntent` to initiate the Phone Number Hint flow.

### Kotlin

```kotlin
val phoneNumberHintIntentResultLauncher = ...

Identity.getSignInClient(activity)
.getPhoneNumberHintIntent(request)
.addOnSuccessListener { result: PendingIntent ->
  try {
    phoneNumberHintIntentResultLauncher.launch(
      IntentSenderRequest.Builder(result).build()
    )
  } catch (e: Exception) {
      Log.e(TAG, "Launching the PendingIntent failed")
  }
}
.addOnFailureListener {
    Log.e(TAG, "Phone Number Hint failed")
}
```

### Java

```java
ActivityResultLauncher phoneNumberHintIntentResultLauncher = ...

Identity.getSignInClient(activity)
  .getPhoneNumberHintIntent(request)
  .addOnSuccessListener( result -> {
      try {
          phoneNumberHintIntentResultLauncher.launch(result.getIntentSender());
      } catch(Exception e) {
          Log.e(TAG, "Launching the PendingIntent failed", e);
      }
  })
  .addOnFailureListener(e -> {
      Log.e(TAG, "Phone Number Hint failed", e);
  });
```

### Retrieving the phone number

Pass in the `Intent` to [`SignInClient.getPhoneNumberFromIntent`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/SignInClient#getPhoneNumberFromIntent(android.content.Intent))
to retrieve the phone number.

### Kotlin

```kotlin
val phoneNumberHintIntentResultLauncher =
registerForActivityResult(ActivityResultContracts.StartIntentSenderForResult()) { result ->
      try {
          val phoneNumber = Identity.getSignInClient(activity).getPhoneNumberFromIntent(result.data)
      } catch(e: Exception) {
          Log.e(TAG, "Phone Number Hint failed")
      }
  }
```

### Java

```java
ActivityResultLauncher phoneNumberHintIntentResultLauncher =
  registerForActivityResult(
      new ActivityResultContracts.StartActivityForResult(),
      new ActivityResultCallback() {
          @Override
          public void onActivityResult(ActivityResult result) {
              try {
                  String phoneNumber = Identity.getSignInClient(activity).getPhoneNumberFromIntent(result.getData());
              } catch {
                  Log.e(TAG, "Phone Number Hint failed", e);
              }
          }
  });
```