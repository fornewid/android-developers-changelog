---
title: https://developer.android.com/privacy-and-security/key-verifier
url: https://developer.android.com/privacy-and-security/key-verifier
source: md.txt
---

# Android System Key Verifier

The Key Verifier for Android provides a unified and secure way for users to verify that they are communicating with the right person in your end-to-end encrypted (E2EE) app. It protects users from man-in-the-middle attacks by allowing them to confirm the authenticity of a contact's public encryption keys through a trusted, and consistent system UI.

This feature is provided by the[Key Verifier](https://play.google.com/store/apps/details?id=com.google.android.contactkeys), a system service that is part of Google System Services and is distributed using the Play Store. It acts as a centralized, on-device repository for E2EE public keys.

## Why you should integrate with Key Verifier

- **Provide a unified UX:**Instead of building your own verification flow, you can launch the system's standard UI, giving users a consistent and trustworthy experience across all their apps.
- **Increase user confidence:**A clear, system-backed verification status assures users that their conversations are secure and private.
- **Reduce development overhead:**Offload the complexity of key verification UI, storage, and status management to the system service.

| **Important:** This service is for verifying keys, not providing encryption. Your app must already implement E2EE with keys stored on the user's device.

## Key terms

- **lookupKey:** An opaque, persistent identifier for a contact, stored in the[LOOKUP_KEY](https://developer.android.com/identity/providers/contacts-provider#ContactBasics)column of the contacts provider. Unlike a`contact ID`, a`lookupKey`remains stable even if the underlying contact details are changed or merged, making it the recommended way to reference a contact.
- **accountId:**An app-specific identifier for a user's account on a device. This ID is defined by your app and helps distinguish between multiple accounts a single user might have. This is displayed to the user in the UI, it's recommended to use something meaningful like a phone number, email address, or user handle
- **deviceId:**A unique identifier for a specific device associated with a user's account. This allows a user to have multiple devices, each with its own set of cryptographic keys. Doesn't necessarily represent a physical device, but could be a way to distinguish between multiple keys used for the same account

## Getting started

Before you begin, set up your app to communicate with the Key Verifier service.

**Declare permissions:**In your AndroidManifest.xml, declare the following permissions. You must also request these from the user at runtime.  

    <uses-permission android:name="android.permission.READ_CONTACTS" />
    <uses-permission android:name="android.permission.WRITE_CONTACTS" />

**Get the client instance:** Get an instance of`ContactKeys`, which is your entry point to the API.  

    import com.google.android.gms.contactkeys.ContactKeys

    val contactKeyClient = ContactKeys.getClient(context)

## Guidance for messaging app developers

As a messaging app developer, your primary role is to publish your users' public keys and their contacts' keys to the Key Verifier service.

### Publish a user's public keys

To allow others to find and verify your user, publish their public key to the on-device repository. For added security, consider creating keys in the[Android Keystore](https://developer.android.com/privacy-and-security/keystore).  

    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.tasks.Tasks

    suspend fun publishSelfKey(
        contactKeyClient: ContactKeyClient,
        accountId: String,
        deviceId: String,
        publicKey: ByteArray
    ) {
        try {
            Tasks.await(
              contactKeyClient.updateOrInsertE2eeSelfKey(
                deviceId,
                accountId,
                publicKey
              )
            )
            // Self key published successfully.
        } catch (e: Exception) {
            // Handle error.
        }
    }

### Associate public keys with contacts

When your app receives a public key for one of the user's contacts, you must store it and associate it with that contact in the central repository. This allows the key to be verified and lets other apps display the verification status for the contact. To do this, you need the contact's[lookupKey](https://developer.android.com/identity/providers/contacts-provider#ContactBasics)from the Android Contacts Provider. This is typically triggered when fetching a key from your key distribution server or during a periodic sync of local keys.  

    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.tasks.Tasks

    suspend fun storeContactKey(
        contactKeyClient: ContactKeyClient,
        contactLookupKey: String,
        contactAccountId: String,
        contactDeviceId: String,
        contactPublicKey: ByteArray
    ) {
        try {
            Tasks.await(
                contactKeyClient.updateOrInsertE2eeContactKey(
                    contactLookupKey,
                    contactDeviceId,
                    contactAccountId,
                    contactPublicKey
                )
            )
            // Contact's key stored successfully.
        } catch (e: Exception) {
            // Handle error.
        }
    }

| **Note:** You can associate one key with multiple contacts by using the`updateOrInsertE2eeContactKey`overload that accepts a list of lookup keys.

### Retrieve keys and verification status

After you have published keys, users may verify them through in-person QR Code scanning. Your app's UI should reflect whether a conversation is using a verified key. Each key has a verification status that you can use to inform your UI.

**Understand verification states:**

- `UNVERIFIED`: This is the default state for every new key. It means the key exists, but the user has not yet confirmed its authenticity. In your UI, you should treat this as a neutral state and typically display no special indicator.

- `VERIFIED`: This status indicates a high level of trust. It means the user has successfully completed a verification flow (like a QR Code scan) and confirmed that the key belongs to the intended contact. In your UI, you should display a clear, positive indicator, such as a green checkmark or shield.

- `VERIFICATION_FAILED`: This is a warning state. It means the key associated with the contact does not match the key that was previously verified. This can happen if a contact gets a new device, but it could also indicate a potential security risk. In your UI, alert the user with a prominent warning and suggest they re-verify before sending sensitive information.

You can retrieve an aggregate status for all keys associated with a contact. We recommend using`VerificationState.leastVerifiedFrom()`to resolve the status when multiple keys are present, as it will correctly prioritize`VERIFICATION_FAILED`over`VERIFIED`.

- **Getting aggregate status at a contact level**

    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.contactkeys.constants.VerificationState
    import com.google.android.gms.tasks.Tasks

    suspend fun displayContactVerificationStatus(
        contactKeyClient: ContactKeyClient,
        contactLookupKey: String
    ) {
        try {
            val keysResult = Tasks.await(contactKeyClient.getAllE2eeContactKeys(contactLookupKey))
            val states =
              keysResult.keys.map { VerificationState.fromState(it.localVerificationState) }
            val contactStatus = VerificationState.leastVerifiedFrom(states)
            updateUi(contactLookupKey, contactStatus)
        } catch (e: Exception) {
            // Handle error.
        }
    }

- **Getting aggregate status at an account level**

    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.contactkeys.constants.VerificationState
    import com.google.android.gms.tasks.Tasks

    suspend fun displayAccountVerificationStatus(
        contactKeyClient: ContactKeyClient,
        accountId: String
    ) {
        try {
            val keys = Tasks.await(contactKeyClient.getE2eeAccountKeysForAccount(accountId))
            val states = keys.map { VerificationState.fromState(it.localVerificationState) }
            val accountStatus = VerificationState.leastVerifiedFrom(states)
            updateUi(accountId, accountStatus)
        } catch (e: Exception) {
            // Handle error.
        }
    }

### Observe key changes in real time

To verify your app's UI always shows the correct trust status, you should listen for updates. The recommended way is to use the Flow-based API, which emits a new list of keys whenever a key for a subscribed account is added, removed, or has its verification status changed. This is especially useful for keeping a group conversation's member list up-to-date. The verification status for a key can change when:

- The user successfully completes a verification flow (for example, QR Code scan).
- A contact's key is modified, causing it to no longer match the previously verified value.

    fun observeKeyUpdates(contactKeyClient: ContactKeyClient, accountIds: List<String>) {
        lifecycleScope.launch {
            contactKeyClient.getAccountContactKeysFlow(accountIds)
                .collect { updatedKeys ->
                    // A key was added, removed, or updated.
                    // Refresh your app's UI and internal state.
                    refreshUi(updatedKeys)
                }
        }
    }

#### Perform in-person key verification

The most secure way for users to verify a key is through in-person verification, often by scanning a QR Code or comparing a sequence of numbers. The Key Verifier app provides standard UI flows for this process, which your app can launch. After a verification attempt, the API automatically updates the key's verification status, and your app will be notified if you are observing key updates.

- **Start the key verification process for a user-selected contact** Launch the`PendingIntent`provided by`getScanQrCodeIntent`using the`lookupKey`of the selected contact. The UI lets the user verify all keys for the given contact.

    import android.app.ActivityOptions
    import android.app.PendingIntent
    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.tasks.Tasks

    suspend fun initiateVerification(contactKeyClient: ContactKeyClient, lookupKey: String) {
        try {
            val pendingIntent = Tasks.await(contactKeyClient.getScanQrCodeIntent(lookupKey))
            val options =
              ActivityOptions.makeBasic()
                .setPendingIntentBackgroundActivityStartMode(
                  ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOWED
                )
                .toBundle()
            pendingIntent.send(options)
        } catch (e: Exception) {
            // Handle error.
        }
    }

- **Start the key verification process for a user-selected account** If the user wants to verify an account not directly linked to a contact (or a specific account of a contact), you can launch the`PendingIntent`provided by`getScanQrCodeIntentForAccount`. This is typically used for your own app's package name and account ID.

    import android.app.ActivityOptions
    import android.app.PendingIntent
    import com.google.android.gms.contactkeys.ContactKeyClient
    import com.google.android.gms.tasks.Tasks

    suspend fun initiateVerification(contactKeyClient: ContactKeyClient, packageName: String, accountId: String) {
        try {
            val pendingIntent = Tasks.await(contactKeyClient.getScanQrCodeIntentForAccount(packageName, accountId))
            // Allow activity start from background on Android SDK34+
            val options =
              ActivityOptions.makeBasic()
                .setPendingIntentBackgroundActivityStartMode(
                  ActivityOptions.MODE_BACKGROUND_ACTIVITY_START_ALLOWED
                )
                .toBundle()
            pendingIntent.send(options)
        } catch (e: Exception) {
            // Handle error.
        }
    }