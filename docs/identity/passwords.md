---
title: https://developer.android.com/identity/passwords
url: https://developer.android.com/identity/passwords
source: md.txt
---

While Credential Manager supports password-based sign-in, we strongly recommend
prioritizing modern, more secure authentication methods like [passkeys](https://developer.android.com/identity/passkeys) and
[Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg). These methods offer significantly better security and
user experience. However, if your application must support passwords, use this
guide as a reference to implement passwords with Credential Manager.

Credential Manager provides a unified API for your app to save and retrieve user
credentials, including usernames and passwords. This simplifies the sign-in
process for users and allows them to utilize credential providers seamlessly.

## Prerequisites

Credential Manager's passwords implementation works on devices running Android
4.4 (API level 19) and higher.

## Overview

This guide focuses on the changes required in your app to create, save, and sign
in with a password.

- **Add dependencies to your app**: Add the required Credential Manager libraries.
- **Instantiate Credential Manager**: Create a Credential Manager instance.
- **Save a user's password**: Store user credentials securely.
- **Sign in with a password**: Retrieve and use stored credentials for login.
- **Identify fields that should use autofill**: Use autofill for a better user experience.
- **Add support for Digital Asset Links**: Add support to share passwords across linked apps and websites.

## Add dependencies to your app

Add the following dependencies to your app module's `build.gradle` file:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.7.0-alpha02")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.7.0-alpha02"
}
```

## Instantiate Credential Manager

Use your app or activity context to create a `CredentialManager` object.

    // Use your app or activity context to instantiate a client instance of
    // CredentialManager.
    private val credentialManager = CredentialManager.create(context)

## Save a user's password

When a user successfully signs up or updates their password within your app,
save these credentials in their password manager.

1. **Construct a password request** : The
   [`CreatePasswordRequest`](https://developer.android.com/reference/androidx/credentials/CreatePasswordRequest) object contains the username and
   password to be saved. Call `credentialManager.createCredential()` to
   initiate the saving process.

2. **Handle the response** : Process the [`CreatePasswordResponse`](https://developer.android.com/reference/androidx/credentials/CreatePasswordResponse) and
   manage any errors (for example, if the user cancels the request).

    suspend fun registerPassword(username: String, password: String) {
        // Initialize a CreatePasswordRequest object.
        val createPasswordRequest =
            CreatePasswordRequest(id = username, password = password)

        // Create credential and handle result.
        coroutineScope {
            try {
                val result =
                    credentialManager.createCredential(
                        // Use an activity based context to avoid undefined
                        // system UI launching behavior.
                        activityContext,
                        createPasswordRequest
                    )
                // Handle register password result
            } catch (e: CreateCredentialException) {
                handleFailure(e)
            }
        }
    }

## Sign in with a password

To retrieve saved credentials, build a [`GetCredentialRequest`](https://developer.android.com/reference/androidx/credentials/GetCredentialRequest) with a
[`GetPasswordOption`](https://developer.android.com/reference/androidx/credentials/GetPasswordOption) and call [`getCredential()`](https://developer.android.com/reference/androidx/credentials/GetCredentialResponse#getCredential()). To filter which
passwords are fetched based on the specified user IDs, use the optional field
[`allowedUserIds`](https://developer.android.com/reference/androidx/credentials/GetPasswordOption#GetPasswordOption(kotlin.collections.Set,kotlin.Boolean,kotlin.collections.Set)).

    val getPasswordOption = GetPasswordOption()

    val credentialRequest = GetCredentialRequest.Builder()
        .addCredentialOption(getPasswordOption)
        .build()

## Identify fields that should use autofill

The `android:isCredential` attribute helps credential providers identify fields
intended for autofill, leading to a smoother user experience. This attribute
complements existing `autofillHints`.

> [!NOTE]
> **Note:** This is only available in Android 14+.

The benefits for indicating certain fields to be intended for autofill include:

- **Improved autofill accuracy**: Helps password managers and the Android system better identify fields intended for credentials.
- **Enhanced user experience**: Can lead to smoother and more reliable autofill suggestions.

Include the `isCredential` attribute in username and password fields as shown in
the following example:

    <EditText
        android:id="@+id/username_edittext"
        android:autofillHints="username"
        android:isCredential="true" />

    <EditText
        android:id="@+id/password_edittext"
        android:inputType="textPassword"
        android:autofillHints="password"
        android:isCredential="true" />

Alternatively, add the attribute programmatically as shown in the following
snippet:

    if (android.os.Build.VERSION.SDK_INT >=
        android.os.Build.VERSION_CODES.UPSIDE_DOWN_CAKE) { // Android 14
        usernameEditText.isCredential = true
        passwordEditText.isCredential = true
    }

## Add support for Digital Asset Links

To ensure compatibility with password managers, you must configure [Digital
Asset Links](https://developer.android.com/identity/credential-manager/prerequisites#configure-digital-asset-links) between your app and your website. This allows credentials to be
shared securely across both platforms.

> [!IMPORTANT]
> **Important:** Digital Asset Links are required for passkeys and highly recommended for password-based authentication.