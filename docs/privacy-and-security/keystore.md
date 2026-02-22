---
title: https://developer.android.com/privacy-and-security/keystore
url: https://developer.android.com/privacy-and-security/keystore
source: md.txt
---

The Android Keystore system lets you store cryptographic keys in a container
to make them more difficult to extract from the device. Once keys are in the
keystore, you can use them for cryptographic operations, with the key material
remaining non-exportable. Also, the keystore system lets you restrict when
and how keys can be used, such as requiring user authentication for key use or
restricting keys to use only in certain cryptographic modes. See the
[Security Features](https://developer.android.com/privacy-and-security/keystore#SecurityFeatures) section for more
information.

<br />

The keystore system is used by the
`https://developer.android.com/reference/android/security/KeyChain`
API, introduced in Android 4.0 (API level 14), as well as the Android Keystore
provider feature, introduced in Android 4.3 (API level 18). This document goes
over when and how to use the Android Keystore system.

## Security features

The Android Keystore system protects key material from unauthorized use in two
ways. First, it reduces the risk of unauthorized use of key material from
*outside* the Android device by preventing the extraction of
the key material from application processes and from the Android device as a
whole. Second, the keystore system reduces the risk of unauthorized use
of key material *within* the Android device by making apps
specify the authorized uses of their keys and then enforcing those restrictions
outside of the apps' processes.

### Extraction prevention

Key material of Android Keystore keys is protected from extraction using two
security measures:

- Key material never enters the application process. When an app performs cryptographic operations using an Android Keystore key, behind the scenes plaintext, ciphertext, and messages to be signed or verified are fed to a system process that carries out the cryptographic operations. If the app's process is compromised, the attacker might be able to use the app's keys but can't extract their key material (for example, to be used outside of the Android device).
- Key material can be bound to the secure hardware of the Android device, such as the [Trusted Execution Environment (TEE)](https://source.android.com/docs/security/features/trusty) or [Secure Element (SE)](https://developer.android.com/privacy-and-security/keystore#strongbox_keymint_secure_element). When this feature is enabled for a key, its key material is never exposed outside of secure hardware. If the Android OS is compromised or an attacker can read the device's internal storage, the attacker might be able to use any app's Android Keystore keys on the Android device, but it can't extract them from the device. This feature is enabled only if the device's secure hardware supports the particular combination of key algorithm, block modes, padding schemes, and digests the key is authorized to be used with.

  <br />

  To check whether the feature is enabled for a key, obtain a
  `https://developer.android.com/reference/android/security/keystore/KeyInfo`
  for the key. The next step depends on your app's target SDK version:
  - If your app targets Android 10 (API level 29) or higher, inspect the return value of `https://developer.android.com/reference/android/security/keystore/KeyInfo#getSecurityLevel()`. Return values matching `KeyProperties.SecurityLevelEnum.TRUSTED_ENVIRONMENT` or `KeyProperties.SecurityLevelEnum.STRONGBOX` indicate that the key resides within secure hardware.
  - If your app targets Android 9 (API level 28) or lower, inspect the boolean return value of `https://developer.android.com/reference/android/security/keystore/KeyInfo#isInsideSecureHardware()`.

<br />

### StrongBox KeyMint secure element

Devices running Android 9 (API level 28) or higher can include a
[StrongBox KeyMint](https://source.android.com/docs/security/features/keystore),
an implementation of the KeyMint HAL that is backed by [StrongBox](https://source.android.com/docs/compatibility/15/android-15-cdd#9112_strongbox). While hardware security
modules (HSMs) broadly refer to secure key storage solutions resistant to Linux
kernel compromises, StrongBox specifically denotes implementations in embedded
SEs or integrated Secure Enclaves (iSE), providing stronger isolation and tamper
resistance compared to the TEE.

An implementation of StrongBox KeyMint must contain the following:

- Its own CPU
- Secure storage
- A true random-number generator
- Additional mechanisms to resist package tampering and unauthorized sideloading of apps
- A secure timer
- A reboot notification pin (or equivalent), like general-purpose input/output (GPIO)

A subset of algorithms and key sizes are supported to accommodate low-power StrongBox implementations:

- RSA 2048
- AES 128 and 256
- ECDSA, ECDH P-256
- HMAC-SHA256 (supports key sizes between 8 bytes and 64 bytes, inclusive)
- Triple DES
- Extended length APDUs

StrongBox also supports [key attestation](https://developer.android.com/privacy-and-security/security-key-attestation).
| **Caution:** StrongBox is appropriate for applications requiring the highest level of security, particularly those at risk of physical tampering or side-channel attacks. However, it is slower, more resource-constrained, and supports fewer concurrent operations. For most apps, StrongBox is not necessary. You should carefully evaluate whether its enhanced security aligns with your app's threat model and use case, as it may introduce performance trade-offs.

#### Use StrongBox KeyMint

Use [`FEATURE_STRONGBOX_KEYSTORE`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#feature_strongbox_keystore) to check whether StrongBox
is available on a device. If StrongBox is available, you can indicate a
preference for storing the key in the StrongBox KeyMint by passing `true` to the
following methods:

- Key generation: [`KeyGenParameterSpec.Builder.setIsStrongBoxBacked()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setIsStrongBoxBacked(boolean))
- Key import: [`KeyProtection.Builder.setIsStrongBoxBacked()`](https://developer.android.com/reference/android/security/keystore/KeyProtection.Builder#setIsStrongBoxBacked(boolean))

If the StrongBox KeyMint does not support the specified algorithm or key size,
the framework will throw a [`StrongBoxUnavailableException`](https://developer.android.com/reference/android/security/keystore/StrongBoxUnavailableException). If this occurs, generate or import the
key without calling `setIsStrongBoxBacked(true)`.

### Key use authorizations

To avoid unauthorized use of keys on the Android device, Android Keystore lets
apps specify authorized uses of their keys when they generate or import the
keys. Once a key is generated or imported, its authorizations can't be changed.
Authorizations are then enforced by the Android Keystore whenever the key is
used. This is an advanced security feature that is generally useful only if your
requirements are that a compromise of your application process after key
generation/import (but not before or during) can't lead to unauthorized uses of
the key.

Supported key use authorizations fall into the following categories:

- **Cryptography:** the key can only be used with authorized key algorithms, operations, or purposes (encrypt, decrypt, sign, verify), padding schemes, block modes, or digests.
- **Temporal validity interval:** the key is authorized for use only during a defined interval of time.
- **User authentication:** the key can only be used if the user has been authenticated recently enough. See [Require user authentication for key use](https://developer.android.com/privacy-and-security/keystore#UserAuthentication).

As an additional security measure for keys whose key material is inside secure hardware (see
[`KeyInfo.isInsideSecurityHardware()`](https://developer.android.com/reference/android/security/keystore/KeyInfo#isInsideSecureHardware())
or, for apps targeting Android 10 (API level 29) or higher,
[`KeyInfo.getSecurityLevel()`](https://developer.android.com/reference/android/security/keystore/KeyInfo#getSecurityLevel())),
some key use authorizations might be enforced by the secure hardware,
depending on the Android device.
Secure hardware normally enforces cryptographic and user authentication
authorizations. However, secure hardware doesn't usually enforce temporal
validity interval authorizations, because it normally doesn't have an
independent, secure real-time clock.

You can query whether a key's user authentication authorization is enforced by
the secure hardware using
`https://developer.android.com/reference/android/security/keystore/KeyInfo#isUserAuthenticationRequirementEnforcedBySecureHardware()`.

## Choose between a keychain and the
Android Keystore provider

Use the `https://developer.android.com/reference/android/security/KeyChain` API when you want
system-wide credentials. When an app requests the use of any credential
through the `KeyChain` API, users can
choose, through a system-provided UI, which of the installed credentials
an app can access. This lets several apps use the
same set of credentials with user consent.

Use the Android Keystore provider to let an individual app store its own
credentials, which only that app can access.
This provides a way for apps to manage credentials that only they can use
while providing the same security benefits that the
`KeyChain` API provides for system-wide credentials.
This method doesn't require the user to select the credentials.

## Use the Android Keystore provider


To use this feature, you use the standard `https://developer.android.com/reference/java/security/KeyStore`
and `https://developer.android.com/reference/java/security/KeyPairGenerator` or
`https://developer.android.com/reference/javax/crypto/KeyGenerator` classes along with the
`AndroidKeyStore` provider introduced in Android 4.3 (API level 18).

`AndroidKeyStore` is registered as a `KeyStore` type for use with the `https://developer.android.com/reference/java/security/KeyStore#getInstance(java.lang.String)`
method and as a provider for use with the `https://developer.android.com/reference/java/security/KeyPairGenerator#getInstance(java.lang.String, java.lang.String)` and `https://developer.android.com/reference/javax/crypto/KeyGenerator#getInstance(java.lang.String, java.lang.String)` methods.

Because cryptographic operations may be time-consuming, apps should avoid using
`AndroidKeyStore` on their main thread to ensure that the app's UI remains
responsive. (`StrictMode` can help you find places where this is not the case.)

### Generate a new private or secret key

To generate a new `KeyPair` containing a
`https://developer.android.com/reference/java/security/PrivateKey`,
you must specify the initial X.509 attributes of the certificate. You can use
`https://developer.android.com/reference/java/security/KeyStore#setKeyEntry(java.lang.String, java.security.Key, char[], java.security.cert.Certificate[])`
to replace the certificate at a later time with a certificate signed
by a certificate authority (CA).

To generate the key pair, use a `https://developer.android.com/reference/java/security/KeyPairGenerator`
with `https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec`:

### Kotlin

```kotlin
/*
 * Generate a new EC key pair entry in the Android Keystore by
 * using the KeyPairGenerator API. The private key can only be
 * used for signing or verification and only with SHA-256 or
 * SHA-512 as the message digest.
 */
val kpg: KeyPairGenerator = KeyPairGenerator.getInstance(
        KeyProperties.KEY_ALGORITHM_EC,
        "AndroidKeyStore"
)
val parameterSpec: KeyGenParameterSpec = KeyGenParameterSpec.Builder(
        alias,
        KeyProperties.PURPOSE_SIGN or KeyProperties.PURPOSE_VERIFY
).run {
    setDigests(KeyProperties.DIGEST_SHA256, KeyProperties.DIGEST_SHA512)
    build()
}

kpg.initialize(parameterSpec)

val kp = kpg.generateKeyPair()
```

### Java

```java
/*
 * Generate a new EC key pair entry in the Android Keystore by
 * using the KeyPairGenerator API. The private key can only be
 * used for signing or verification and only with SHA-256 or
 * SHA-512 as the message digest.
 */
KeyPairGenerator kpg = KeyPairGenerator.getInstance(
        KeyProperties.KEY_ALGORITHM_EC, "AndroidKeyStore");
kpg.initialize(new KeyGenParameterSpec.Builder(
        alias,
        KeyProperties.PURPOSE_SIGN | KeyProperties.PURPOSE_VERIFY)
        .setDigests(KeyProperties.DIGEST_SHA256,
            KeyProperties.DIGEST_SHA512)
        .build());

KeyPair kp = kpg.generateKeyPair();
```

### Import encrypted keys into secure hardware

Android 9 (API level 28) and higher lets you import encrypted keys
securely into the keystore using an ASN.1‑encoded key format. The
Keymaster then decrypts the keys in the keystore, so the content of the keys
never appears as plaintext in the device's host memory. This process
provides additional key decryption security.
| **Note:** This feature is supported only on devices that ship with Keymaster 4 or higher.

To support secure importing of encrypted keys into the keystore, complete the
following steps:

1. Generate a key pair that uses the
   [`PURPOSE_WRAP_KEY`](https://developer.android.com/reference/android/security/keystore/KeyProperties#PURPOSE_WRAP_KEY)
   purpose. We recommend that you add attestation to this key pair as well.

2. On a server or machine that you trust, generate the ASN.1 message for the
   `SecureKeyWrapper`.

   The wrapper contains the following schema:

          KeyDescription ::= SEQUENCE {
              keyFormat INTEGER,
              authorizationList AuthorizationList
          }

          SecureKeyWrapper ::= SEQUENCE {
              wrapperFormatVersion INTEGER,
              encryptedTransportKey OCTET_STRING,
              initializationVector OCTET_STRING,
              keyDescription KeyDescription,
              secureKey OCTET_STRING,
              tag OCTET_STRING
          }

3. Create a
   [`WrappedKeyEntry`](https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)
   object, passing in the ASN.1 message as a byte array.

4. Pass this `WrappedKeyEntry` object into the overload of
   [`setEntry()`](https://developer.android.com/reference/java/security/KeyStore#setEntry(java.lang.String,%20java.security.KeyStore.Entry,%20java.security.KeyStore.ProtectionParameter))
   that accepts a
   [`Keystore.Entry`](https://developer.android.com/reference/java/security/KeyStore.Entry) object.

### Work with keystore entries

You can access the `AndroidKeyStore` provider through
all the standard `https://developer.android.com/reference/java/security/KeyStore` APIs.

#### List entries

List entries in the keystore by calling the `https://developer.android.com/reference/java/security/KeyStore#aliases()` method:

### Kotlin

```kotlin
/*
 * Load the Android KeyStore instance using the
 * AndroidKeyStore provider to list the currently stored entries.
 */
val ks: KeyStore = KeyStore.getInstance("AndroidKeyStore").apply {
   load(null)
}
val aliases: Enumeration<String> = ks.aliases()
```

### Java

```java
/*
 * Load the Android KeyStore instance using the
 * AndroidKeyStore provider to list the currently stored entries.
 */
KeyStore ks = KeyStore.getInstance("AndroidKeyStore");
ks.load(null);
Enumeration<String> aliases = ks.aliases();
```

#### Sign and verify data

Sign data by fetching the `https://developer.android.com/reference/java/security/KeyStore.Entry` from the keystore and using the
`https://developer.android.com/reference/java/security/Signature` APIs, such as `https://developer.android.com/reference/java/security/Signature#sign()`:

### Kotlin

```kotlin
/*
 * Use a PrivateKey in the KeyStore to create a signature over
 * some data.
 */
val ks: KeyStore = KeyStore.getInstance("AndroidKeyStore").apply {
    load(null)
}
val entry: KeyStore.Entry = ks.getEntry(alias, null)
if (entry !is KeyStore.PrivateKeyEntry) {
    Log.w(TAG, "Not an instance of a PrivateKeyEntry")
    return null
}
val signature: ByteArray = Signature.getInstance("SHA256withECDSA").run {
    initSign(entry.privateKey)
    update(data)
    sign()
}
```

### Java

```java
/*
 * Use a PrivateKey in the KeyStore to create a signature over
 * some data.
 */
KeyStore ks = KeyStore.getInstance("AndroidKeyStore");
ks.load(null);
KeyStore.Entry entry = ks.getEntry(alias, null);
if (!(entry instanceof PrivateKeyEntry)) {
    Log.w(TAG, "Not an instance of a PrivateKeyEntry");
    return null;
}
Signature s = Signature.getInstance("SHA256withECDSA");
s.initSign(((PrivateKeyEntry) entry).getPrivateKey());
s.update(data);
byte[] signature = s.sign();
```

Similarly, verify data with the `https://developer.android.com/reference/java/security/Signature#verify(byte[])` method:

### Kotlin

```kotlin
/*
 * Verify a signature previously made by a private key in the
 * KeyStore. This uses the X.509 certificate attached to the
 * private key in the KeyStore to validate a previously
 * generated signature.
 */
val ks = KeyStore.getInstance("AndroidKeyStore").apply {
    load(null)
}
val entry = ks.getEntry(alias, null) as? KeyStore.PrivateKeyEntry
if (entry == null) {
    Log.w(TAG, "Not an instance of a PrivateKeyEntry")
    return false
}
val valid: Boolean = Signature.getInstance("SHA256withECDSA").run {
    initVerify(entry.certificate)
    update(data)
    verify(signature)
}
```

### Java

```java
/*
 * Verify a signature previously made by a private key in the
 * KeyStore. This uses the X.509 certificate attached to the
 * private key in the KeyStore to validate a previously
 * generated signature.
 */
KeyStore ks = KeyStore.getInstance("AndroidKeyStore");
ks.load(null);
KeyStore.Entry entry = ks.getEntry(alias, null);
if (!(entry instanceof PrivateKeyEntry)) {
    Log.w(TAG, "Not an instance of a PrivateKeyEntry");
    return false;
}
Signature s = Signature.getInstance("SHA256withECDSA");
s.initVerify(((PrivateKeyEntry) entry).getCertificate());
s.update(data);
boolean valid = s.verify(signature);
```

### Require user authentication for key use

When generating or importing a key into the `AndroidKeyStore`, you can specify that the key
is only authorized to be used if the user has been authenticated. The user is authenticated using a
subset of their secure lock screen credentials (pattern/PIN/password, biometric credentials).

This is an advanced security feature that is generally useful only if your requirements are that
a compromise of your application process after key generation/import (but not before or during)
can't bypass the requirement for the user to be authenticated to use the key.

When a key is only authorized to be used if the user has been authenticated, you can call
[`setUserAuthenticationParameters()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUserAuthenticationParameters(int,%20int))
to configure it to operate in one of the following modes:

Authorize for a duration of time
:   All keys are authorized for use as soon as the user authenticates using one of the credentials
    specified.

Authorize for the duration of a specific cryptographic operation

:   Each operation involving a specific key must be individually authorized by the user.

    Your app starts this process by calling
    [`authenticate()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt#authenticate(android.hardware.biometrics.BiometricPrompt.CryptoObject,%20android.os.CancellationSignal,%20java.util.concurrent.Executor,%20android.hardware.biometrics.BiometricPrompt.AuthenticationCallback))
    on an instance of `BiometricPrompt`.

For each key that you create, you can choose to support a
[strong
biometric credential](https://developer.android.com/reference/android/security/keystore/KeyProperties#AUTH_BIOMETRIC_STRONG), a
[lock screen
credential](https://developer.android.com/reference/android/security/keystore/KeyProperties#AUTH_DEVICE_CREDENTIAL), or both types of credentials. To determine whether the user has set up the credentials
that your app's key relies on, call
[`canAuthenticate()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager#canAuthenticate(int)).

If a key only supports biometric credentials, the key is invalidated by default whenever new
biometric enrollments are added. You can configure the key to remain valid when new biometric
enrollments are added. To do so, pass `false` into
[`setInvalidatedByBiometricEnrollment()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setInvalidatedByBiometricEnrollment(boolean)).

Learn more about how to add biometric authentication capabilities into your app, including how
to [show a biometric authentication dialog](https://developer.android.com/training/sign-in/biometric-auth).

## Supported algorithms

- [`Cipher`](https://developer.android.com/reference/javax/crypto/Cipher)
- [`KeyGenerator`](https://developer.android.com/reference/javax/crypto/KeyGenerator)
- [`KeyFactory`](https://developer.android.com/reference/java/security/KeyFactory)
- `KeyStore` (supports the same key types as `KeyGenerator` and `KeyPairGenerator`)
- [`KeyPairGenerator`](https://developer.android.com/reference/java/security/KeyPairGenerator)
- [`Mac`](https://developer.android.com/reference/javax/crypto/Mac)
- [`Signature`](https://developer.android.com/reference/java/security/Signature)
- [`SecretKeyFactory`](https://developer.android.com/reference/javax/crypto/SecretKeyFactory)

## What's next

- Check out [Unifying Key Store Access in ICS](http://android-developers.blogspot.com/2012/03/unifying-key-store-access-in-ics.html) on the Android Developers Blog.