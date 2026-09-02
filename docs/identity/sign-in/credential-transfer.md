---
title: https://developer.android.com/identity/sign-in/credential-transfer
url: https://developer.android.com/identity/sign-in/credential-transfer
source: md.txt
---

Credential Manager's Credentials Transfer APIs enable secure, same-device
transfer of user credentials between credential providers. This guide details
how credential providers on Android can integrate with the APIs provided by the
[`androidx.credentials:providerevents`](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents) library. This feature supports
passwords, passkeys, address information, and custom fields using the
standardized [FIDO Credential Exchange Format (CXF)](https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html).

## Core concepts

The credential transfer framework facilitates peer-to-peer credential transfer
on the same device without exposing raw credentials to the Android OS or
unauthenticated apps.

The framework defines two primary roles:

- **Exporter (source provider):** A credential provider that currently holds user credentials. It pre-registers metadata about available exportable accounts ([`ExportEntry`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/ExportEntry)) with the system and responds to transfer requests when selected by the user.
- **Importer (client provider or setup wizard):** A credential provider or setup wizard that initiates an import request ([`ImportCredentialsRequest`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/ImportCredentialsRequest)) specifying what types of credentials and extensions it can receive.

> [!NOTE]
> **Note:** The framework uses a secure Content URI ([`FileProvider`](https://developer.android.com/reference/kotlin/androidx/core/content/FileProvider)) backed by temporary cache files as the transfer medium between providers, because user credential vaults can exceed the [1MB Android Binder transaction limit](https://developer.android.com/guide/components/activities/parcelables-and-bundles).

## Android version compatibility

The Credentials Transfer API works on devices running Android 8 (API level 26)
and later.

## Add dependencies

Add the `androidx.credentials:providerevents` dependency to your module's
`build.gradle` or `build.gradle.kts`:

    dependencies {
        implementation("androidx.credentials:providerevents:1.0.0-alpha06")
    }

## Instantiate the required class

Create an instance of the required [`ProviderEventsManager`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/ProviderEventsManager).


```kotlin
val providerEventsManager = ProviderEventsManager.create(context)
```

<br />

## Implement the exporter

To allow users to export credentials from your app to other credential providers
on the device, implement the exporter role.

### Register export entries

When your credential provider changes (for example, a user signs in, adds
credentials, or modifies accounts), register or update your `ExportEntry` items
using `ProviderEventsManager.registerExport()`.

Each `ExportEntry` requires:

- `id`: A secret, randomly generated string identifier uniquely representing this export entry. **You must persist this ID securely**; you will need it later to verify incoming transfer requests.
- `accountDisplayName`: Optional account label (for example, `"Personal
  Account"`).
- `userDisplayName`: The user's primary identifier (for example, `"alice@example.com"`).
- `icon`: A `Bitmap` icon representing the provider or account (automatically scaled to 32x32 PNG by the library).
- `supportedCredentialTypes`: A set of string constants from [`CredentialTypes`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/CredentialTypes) representing what types this entry holds.


```kotlin
suspend fun registerMyProviderForExport(
    providerEventsManager: ProviderEventsManager,
    providerIcon: Bitmap,
    // Randomly generated and stored in encrypted storage
    secretEntryId: String
) {
    val entry = ExportEntry(
        id = secretEntryId,
        accountDisplayName = "MyProvider Personal",
        userDisplayName = "alice@example.com",
        icon = providerIcon,
        supportedCredentialTypes = setOf(
            CredentialTypes.CREDENTIAL_TYPE_BASIC_AUTH, // Passwords
            CredentialTypes.CREDENTIAL_TYPE_PUBLIC_KEY, // Passkeys
            CredentialTypes.CREDENTIAL_TYPE_ADDRESS,
            CredentialTypes.CREDENTIAL_TYPE_CREDIT_CARD
        )
    )

    // RegisterExportRequest.create() attaches the default WASM matcher from assets
    val request = RegisterExportRequest.create(context, listOf(entry))

    try {
        val response = providerEventsManager.registerExport(request)
        // Registration successful
    } catch (e: Exception) {
        // Handle registration exceptions (e.g., RegisterExportProviderConfigurationException)
    }
}
```

<br />

> [!NOTE]
> **Note:** If the user signs out or disables exporting, clear all registered entries from the device by calling [`providerEventsManager.clearExport(ClearExportRequest())`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/ProviderEventsManager#clearExport(androidx.credentials.providerevents.transfer.ClearExportRequest)). Calling [`registerExport()`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/ProviderEventsManager#registerExport(androidx.credentials.providerevents.transfer.RegisterExportRequest)) with a new list directly overrides all previously registered entries without needing to call [`clearExport()`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/ProviderEventsManager#clearExport(androidx.credentials.providerevents.transfer.ClearExportRequest)) first.

### Declare the exporter activity in manifest file

When the user selects your `ExportEntry` on the system selector UI, the system
launches your designated handling `Activity`. Declare this activity with the
mandatory intent action and content URI scheme:

    <activity
        android:name="com.example.CredentialExportActivity"
        android:exported="true"
        android:label="@string/export_activity_label">
        <intent-filter>
            // This intent action is required for Credential Manager to invoke this activity
            <action android:name="androidx.identitycredentials.action.IMPORT_CREDENTIALS" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:scheme="content" />
        </intent-filter>
    </activity>

### Handle the transfer intent in your activity

In your `CredentialExportActivity`, use
`IntentHandler.retrieveProviderImportCredentialsRequest(intent)` to parse the
request, verify the calling app and `credId`, perform any required biometric
authentication, and write the FIDO CXF payload back to the provided content URI:

> [!NOTE]
> **Note:** In this sample, `isTrustedImporter` returns `true` as a placeholder. In a production application, you should implement actual verification logic to ensure the calling app is authorized to receive the credentials.


```kotlin
class CredentialExportActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 1. Extract the transfer request from the incoming Intent
        val request: ProviderImportCredentialsRequest? =
            IntentHandler.retrieveProviderImportCredentialsRequest(intent)

        if (request == null) {
            finishWithError()
            return
        }

        // 2. Validate CallingAppInfo and secret `credId`
        val callingAppPackage = request.callingAppInfo.packageName
        val receivedCredId = request.credId
        if (!verifySecretEntryId(receivedCredId) || !isTrustedImporter(callingAppPackage)) {
            // Secret ID mismatch or untrusted caller -> abort
            sendExceptionAndFinish(ImportCredentialsNoExportOptionException("Unauthorized request"))
            return
        }

        // 3. Optional: Prompt user for Biometric / PIN authentication before exporting
        authenticateUserThenExport(request)
    }

    private fun authenticateUserThenExport(request: ProviderImportCredentialsRequest) {
        // ... Biometric prompt logic ...
        // Once authenticated, generate the FIDO CXF JSON string matching the requested types
        val cxfJsonPayload = buildFidoCxfJsonPayload(
            requestedTypes = request.request.credentialTypes,
            requestedExtensions = request.request.knownExtensions
        )

        val response = ImportCredentialsResponse(cxfJsonPayload)

        // 4. Write the JSON payload to the Content URI and set Activity result
        IntentHandler.setImportCredentialsResponse(
            context = this,
            uri = request.uri,
            intent = intent,
            response = response
        )
        setResult(Activity.RESULT_OK, intent)
        finish()
    }

    private fun sendExceptionAndFinish(exception: androidx.credentials.providerevents.exception.ImportCredentialsException) {
        IntentHandler.setImportCredentialsException(intent, exception)
        setResult(Activity.RESULT_OK, intent)
        finish()
    }

    private fun verifySecretEntryId(credentialId: String): Boolean {
        // Check if credentialId matches what you stored when calling RegisterExportRequest
        return credentialId == getStoredSecretEntryId()
    }

    private fun isTrustedImporter(packageName: String): Boolean {
        // Implement any specific allowlisting / caller checks if required
        return true
    }

    private fun finishWithError() {
        setResult(Activity.RESULT_CANCELED)
        finish()
    }
}
```

<br />

> [!CAUTION]
> **Caution:** When returning an error to the importer using `IntentHandler.setImportCredentialsException(intent, exception)`, you must set the activity result to `Activity.RESULT_OK`. The system inspects the `Intent` extras on `RESULT_OK` to determine whether an exception was serialized. If `RESULT_CANCELED` is set directly, the importer receives a generic cancellation exception rather than your detailed failure reason.

### Export registration and clearing exceptions

All exceptions in this module are subclasses of
[`ImportCredentialsException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsException), [`RegisterExportException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/RegisterExportException), or
[`ClearExportException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ClearExportException).

- [`RegisterExportProviderConfigurationException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/RegisterExportProviderConfigurationException) or [`ClearExportProviderConfigurationException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ClearExportProviderConfigurationException): Thrown when registration or clearing fails due to provider setup issues (for example, empty `supportedCredentialTypes` in an `ExportEntry`, or calling on an unsupported OS tier).
- [`RegisterExportUnknownErrorException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/RegisterExportUnknownErrorException) or [`ClearExportUnknownErrorException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ClearExportUnknownErrorException): Unclassified system or storage error occurred while updating the export registry.

## Implement the importer

To import credentials into your app (for example, during onboarding or provider
import), implement the importer role and initiate the flow by calling
[`ProviderEventsManager`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/ProviderEventsManager)`.importCredentials()`.

### Construct the import request and launch flow

Specify which [`CredentialTypes`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/CredentialTypes) and [`KnownExtensions`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/KnownExtensions) your importer
supports:


```kotlin
suspend fun startCredentialImport(
    activityContext: Context,
    providerEventsManager: ProviderEventsManager
) {
    val importRequest = ImportCredentialsRequest(
        credentialTypes = setOf(
            CredentialTypes.CREDENTIAL_TYPE_BASIC_AUTH,
            CredentialTypes.CREDENTIAL_TYPE_PUBLIC_KEY,
            CredentialTypes.CREDENTIAL_TYPE_ADDRESS,
            CredentialTypes.CREDENTIAL_TYPE_NOTE
        ),
        knownExtensions = setOf(
            KnownExtensions.KNOWN_EXTENSION_SHARED
        )
    )

    try {
        // Launches the system Selector UI; suspends until user selects a provider and completes transfer
        val response = providerEventsManager.importCredentials(activityContext, importRequest)

        // 1. Inspect the source exporter's package info
        val exporterPackageName = response.callingAppInfo.packageName

        // 2. Parse the FIDO CXF JSON string
        val cxfJsonString = response.response.responseJson
        parseAndSaveImportedCredentials(cxfJsonString)
    } catch (e: ImportCredentialsException) {
        // Handle specific import exceptions (e.g., ImportCredentialsCancellationException)
        handleImportFailure(e)
    }
}

private fun parseAndSaveImportedCredentials(cxfJsonString: String) {
    val rootJson = JSONObject(cxfJsonString)
    // Parse according to FIDO Credential Exchange Format (CXF v1.0) specification:
    // https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html
}

// Helper function to make it compile
private fun handleImportFailure(e: ImportCredentialsException) {}
```

<br />

### Import flow exceptions

All exceptions in this module are subclasses of
[`ImportCredentialsException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsException), [`RegisterExportException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/RegisterExportException), or
[`ClearExportException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ClearExportException).

- [`ImportCredentialsCancellationException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsCancellationException): The user dismissed the selector UI or canceled the export activity (`Activity.RESULT_CANCELED`).
- [`ImportCredentialsNoExportOptionException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsNoExportOptionException): No registered export entries matched the requested credential types, or the selected exporter threw a rejection exception.
- [`ImportCredentialsProviderConfigurationException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsProviderConfigurationException): Configuration error (for example, empty `credentialTypes` set in [`ImportCredentialsRequest`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/transfer/ImportCredentialsRequest) or missing permissions).
- [`ImportCredentialsInvalidJsonException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsInvalidJsonException): The exporter returned a malformed or empty JSON payload that failed request validation.
- [`ImportCredentialsSystemErrorException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsSystemErrorException): Internal Android system or Binder transfer error occurred during import.
- [`ImportCredentialsUnknownCallerException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsUnknownCallerException): The calling app couldn't be verified by the framework.
- [`ImportCredentialsUnknownErrorException`](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/exception/ImportCredentialsUnknownErrorException): Unclassified or unexpected error during the import flow.

## Supported credential types and extensions

The `androidx.credentials.providerevents.transfer.CredentialTypes` object
defines standardized string constants corresponding to FIDO CXF item types:

| Constant | Value (`cxf` type) | Description |
|---|---|---|
| `CREDENTIAL_TYPE_BASIC_AUTH` | `"basic-auth"` | Username and password login credentials. |
| `CREDENTIAL_TYPE_PUBLIC_KEY` | `"passkey"` | FIDO2 or WebAuthn passkey public key credentials. |
| `CREDENTIAL_TYPE_ADDRESS` | `"address"` | Postal or shipping address info for form autofill. |
| `CREDENTIAL_TYPE_API_KEY` | `"api-key"` | API access keys and tokens. |
| `CREDENTIAL_TYPE_CREDIT_CARD` | `"credit-card"` | Credit and debit card payment information. |
| `CREDENTIAL_TYPE_CUSTOM_FIELDS` | `"custom-fields"` | Custom groupings or user-defined fields. |
| `CREDENTIAL_TYPE_DRIVERS_LICENSE` | `"drivers-license"` | Driver's license details. |
| `CREDENTIAL_TYPE_FILE` | `"file"` | Metadata and placeholder references for binary files. |
| `CREDENTIAL_TYPE_GENERATED_PASSWORD` | `"generated-password"` | Machine-generated secure passwords. |
| `CREDENTIAL_TYPE_IDENTITY_DOCUMENT` | `"identity-document"` | National ID cards, SSN, TIN, or passport references. |
| `CREDENTIAL_TYPE_ITEM_REFERENCE` | `"item-reference"` | Logical links pointing to another item in the payload. |
| `CREDENTIAL_TYPE_NOTE` | `"note"` | User-defined secure notes (UTF-8 string). |
| `CREDENTIAL_TYPE_PASSPORT` | `"passport"` | Passport travel document details. |
| `CREDENTIAL_TYPE_PERSON_NAME` | `"person-name"` | Person identity and naming details. |
| `CREDENTIAL_TYPE_SSH_KEY` | `"ssh-key"` | SSH public and private key pairs. |
| `CREDENTIAL_TYPE_TOTP` | `"totp"` | Time-based one-time password (2FA) secrets. |
| `CREDENTIAL_TYPE_WIFI` | `"wifi"` | Wi-Fi network SSID and passphrases. |

## Custom WASM (WebAssembly) matchers (Advanced)

By default, calling `RegisterExportRequest.create(context, entries)` bundles the
system-default `credential_transfer_matcher.wasm` from library assets, which
filters entries purely based on intersection of `supportedCredentialTypes`.

If your credential provider requires complex matching logic (for example,
dynamic capability checks or conditional filtering based on custom fields), you
can compile your own WebAssembly module matching the WASM credential transfer
API and pass the raw byte array directly:


```kotlin
// Loading a custom WASM matcher
val customMatcherBytes = context.assets.open("my_custom_matcher.wasm").use { it.readBytes() }
val customRequest = RegisterExportRequest(
    entries = myEntries,
    exportMatcher = customMatcherBytes
)
providerEventsManager.registerExport(customRequest)
```

<br />