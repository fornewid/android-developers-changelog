---
title: https://developer.android.com/identity/sign-in/smart-lock-migration
url: https://developer.android.com/identity/sign-in/smart-lock-migration
source: md.txt
---

# Migrate from Smart Lock for Passwords to Credential Manager

[Smart Lock for Passwords](https://developers.google.com/identity/smartlock-passwords/android/overview), which was deprecated in 2022, is now removed from the[Google Play Services Auth SDK](https://maven.google.com/web/index.html?q=play-services-auth#com.google.android.gms:play-services-auth)(`com.google.android.gms:play-services-auth`) . To minimize breaking changes that may impact existing integrations, Smart Lock capabilities for all existing apps in the Play Store will continue to work correctly. New app versions compiled with the updated SDK (`com.google.android.gms:play-services-auth:21.0.0`) are no longer able to access the Smart Lock for Password API and won't build successfully. All developers should migrate their Android projects to use[Credential Manager](https://developer.android.com/training/sign-in/passkeys)as soon as possible.

## Benefits of migration to the Credential Manager API

Credential Manager offers a simple, unified API that enables support for modern features and practices while improving the authentication experience for your users:

- Credential Manager fully[supports password saving and authentication](https://developer.android.com/training/sign-in/passkeys). This means no interruption for your users as your app migrates from Smart Lock to Credential Manager.
- Credential Manager integrates support for multiple sign in methods, including[passkeys](https://developers.google.com/identity/passkeys)and federated sign in methods like[Sign in with Google](https://developer.android.com/training/sign-in/credential-manager), to increase security and enable conversion if you plan to support either in the future.
- Starting with Android 14, Credential Manager supports third-party password and passkey providers.
- Credential Manager provides a consistent, unified[user experience](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys)across all authentication methods.

**Migration options**:

|                   Use case                    |                                                                                                      Recommendation                                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Save password and sign in with saved password | Use the password option from the[Sign in your user with Credential Manager](https://developer.android.com/training/sign-in/passkeys)guide. The detailed steps for password saving and authentication are described later. |
| Sign in with Google                           | Follow the[Integrate Credential Manager with Sign in with Google](https://developer.android.com/training/sign-in/credential-manager)guide.                                                                                |
| Show Phone number hint to users               | Use the[Phone Number Hint API](https://developers.google.com/identity/phone-number-hint/android)from Google Identity Services.                                                                                            |

## Sign in with passwords using Credential Manager

To use Credential Manager API, complete the steps outlined in the[prerequisites](https://developer.android.com/training/sign-in/passkeys#prerequisites)section of the Credential Manager guide, and make sure you do the following:

- [Add required dependencies](https://developer.android.com/training/sign-in/passkeys#add-dependencies)
- [Preserve classes in the ProGuard file](https://developer.android.com/training/sign-in/passkeys#proguard)
- [Add support for Digital Asset Links](https://developer.android.com/training/sign-in/passkeys#add-support-dal)(this step should be already implemented if you are using Smart Lock for Passwords)
- [Configure Credentials Manager](https://developer.android.com/training/sign-in/passkeys#configure)
- [Indicate credential fields](https://developer.android.com/training/sign-in/passkeys#indicate_credential_fields)
- [Save a user's password](https://developer.android.com/training/sign-in/passkeys#save-password)

## Sign in with saved passwords

To retrieve password options that are associated with the user's account, complete these steps:

1. Initialize the password and authentication option  

    // Retrieves the user's saved password for your app from their
    // password provider.
    val getPasswordOption = GetPasswordOption()

2. Use the options retrieved from the previous step to build the sign-in request  

    val getCredRequest = GetCredentialRequest(
        listOf(getPasswordOption)
    )

3. Launch the sign-in flow  

    fun launchSignInFlow() {
        coroutineScope.launch {
            try {
                // Attempt to retrieve the credential from the Credential Manager.
                val result = credentialManager.getCredential(
                    // Use an activity-based context to avoid undefined system UI
                    // launching behavior.
                    context = activityContext,
                    request = getCredRequest
                )

                // Process the successfully retrieved credential.
                handleSignIn(result)
            } catch (e: GetCredentialException) {
                // Handle any errors that occur during the credential retrieval
                // process.
                handleFailure(e)
            }
        }
    }

    private fun handleSignIn(result: GetCredentialResponse) {
        // Extract the credential from the response.
        val credential = result.credential

        // Determine the type of credential and handle it accordingly.
        when (credential) {
            is PasswordCredential -> {
                val username = credential.id
                val password = credential.password

                // Use the extracted username and password to perform
                // authentication.
            }

            else -> {
                // Handle unrecognized credential types.
                Log.e(TAG, "Unexpected type of credential")
            }
        }
    }

    private fun handleFailure(e: GetCredentialException) {
        // Handle specific credential retrieval errors.
        when (e) {
            is GetCredentialCancellationException -> {
                /* This exception is thrown when the user intentionally cancels
                    the credential retrieval operation. Update the application's state
                    accordingly. */
            }

            is GetCredentialCustomException -> {
                /* This exception is thrown when a custom error occurs during the
                    credential retrieval flow. Refer to the documentation of the
                    third-party SDK used to create the GetCredentialRequest for
                    handling this exception. */
            }

            is GetCredentialInterruptedException -> {
                /* This exception is thrown when an interruption occurs during the
                    credential retrieval flow. Determine whether to retry the
                    operation or proceed with an alternative authentication method. */
            }

            is GetCredentialProviderConfigurationException -> {
                /* This exception is thrown when there is a mismatch in
                    configurations for the credential provider. Verify that the
                    provider dependency is included in the manifest and that the
                    required system services are enabled. */
            }

            is GetCredentialUnknownException -> {
                /* This exception is thrown when the credential retrieval
                    operation fails without providing any additional details. Handle
                    the error appropriately based on the application's context. */
            }

            is GetCredentialUnsupportedException -> {
                /* This exception is thrown when the device does not support the
                    Credential Manager feature. Inform the user that credential-based
                    authentication is unavailable and guide them to an alternative
                    authentication method. */
            }

            is NoCredentialException -> {
                /* This exception is thrown when there are no viable credentials
                    available for the user. Prompt the user to sign up for an account
                    or provide an alternative authentication method. Upon successful
                    authentication, store the login information using
                    androidx.credentials.CredentialManager.createCredential to
                    facilitate easier sign-in the next time. */
            }

            else -> {
                // Handle unexpected exceptions.
                Log.w(TAG, "Unexpected exception type: ${e::class.java.name}")
            }
        }
    }

## Additional resources

- [Credential Manager sample reference](https://github.com/android/identity-samples/tree/glitch_me_version/CredentialManager)
- [Credential Manager codelab](https://codelabs.developers.google.com/credential-manager-api-for-android#0)
- [Sign in your user with Credential Manager](https://developer.android.com/training/sign-in/passkeys)