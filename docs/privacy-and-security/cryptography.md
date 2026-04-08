---
title: Cryptography  |  Security  |  Android Developers
url: https://developer.android.com/privacy-and-security/cryptography
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Guides](https://developer.android.com/privacy-and-security/security-tips)

# Cryptography Stay organized with collections Save and categorize content based on your preferences.




This document describes the proper way to use Android's cryptographic facilities
and includes some examples of their use. If your app requires greater key
security, use the [Android Keystore system](/training/articles/keystore).

**Note:** Except where specified, this advice applies to all Android versions.

## Specify a provider only with the Android Keystore system

If you're using the Android Keystore system,
you **must** specify a provider.

In other situations, however, Android doesn't guarantee a particular provider
for a given algorithm. Specifying a provider without using the Android Keystore
system can cause compatibility problems in future releases.

## Choose a recommended algorithm

When you have the freedom to choose which algorithm to use (such as when you
don't require compatibility with a third-party system), we recommend using the
following algorithms:

| Class | Recommendation |
| --- | --- |
| Cipher | AES in either CBC or GCM mode with 256-bit keys (such as `AES/GCM/NoPadding`) |
| MessageDigest | SHA-2 family (such as `SHA-256`) |
| Mac | SHA-2 family HMAC (such as `HMACSHA256`) |
| Signature | SHA-2 family with ECDSA (such as `SHA256withECDSA`) |

**Note:** When reading and writing local files, your app can use the [Security
library](/topic/security/data) to perform these actions in a more secure manner.
The library specifies a recommended encryption algorithm.

## Perform common cryptographic operations

The following sections include snippets that demonstrate how you can complete
common cryptographic operations in your app.

### Encrypt a message

### Kotlin

```
val plaintext: ByteArray = ...
val keygen = KeyGenerator.getInstance("AES")
keygen.init(256)
val key: SecretKey = keygen.generateKey()
val cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING")
cipher.init(Cipher.ENCRYPT_MODE, key)
val ciphertext: ByteArray = cipher.doFinal(plaintext)
val iv: ByteArray = cipher.iv
```

### Java

```
byte[] plaintext = ...;
KeyGenerator keygen = KeyGenerator.getInstance("AES");
keygen.init(256);
SecretKey key = keygen.generateKey();
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
cipher.init(Cipher.ENCRYPT_MODE, key);
byte[] ciphertext = cipher.doFinal(plaintext);
byte[] iv = cipher.getIV();
```

### Generate a message digest

### Kotlin

```
val message: ByteArray = ...
val md = MessageDigest.getInstance("SHA-256")
val digest: ByteArray = md.digest(message)
```

### Java

```
byte[] message = ...;
MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] digest = md.digest(message);
```

### Generate a digital signature

You need to have a [`PrivateKey`](/reference/java/security/PrivateKey) object
containing the signing key, which you
can generate at runtime, read from a file bundled with your app, or obtain from
some other source depending on your needs.

### Kotlin

```
val message: ByteArray = ...
val key: PrivateKey = ...
val s = Signature.getInstance("SHA256withECDSA")
        .apply {
            initSign(key)
            update(message)
        }
val signature: ByteArray = s.sign()
```

### Java

```
byte[] message = ...;
PrivateKey key = ...;
Signature s = Signature.getInstance("SHA256withECDSA");
s.initSign(key);
s.update(message);
byte[] signature = s.sign();
```

### Verify a digital signature

You need to have a [`PublicKey`](/reference/kotlin/java/security/PublicKey)
object containing the signer's public key,
which you can read from a file bundled with your app, [extract from a
certificate](/reference/javax/security/cert/Certificate#getPublicKey()), or
obtain from some other source depending on your needs.

### Kotlin

```
val message: ByteArray = ...
val signature: ByteArray = ...
val key: PublicKey = ...
val s = Signature.getInstance("SHA256withECDSA")
        .apply {
            initVerify(key)
            update(message)
        }
val valid: Boolean = s.verify(signature)
```

### Java

```
byte[] message = ...;
byte[] signature = ...;
PublicKey key = ...;
Signature s = Signature.getInstance("SHA256withECDSA");
s.initVerify(key);
s.update(message);
boolean valid = s.verify(signature);
```

## Implementation complexities

There are some details of the Android cryptography implementation that seem
unusual but are present due to compatibility concerns. This section discusses
the ones that you'll most likely encounter.

### OAEP MGF1 message digest

RSA OAEP ciphers are parameterized by two different message digests: the “main”
digest and the MGF1 digest. There are [`Cipher`](/reference/javax/crypto/Cipher)
identifiers that include digest
names, such as `Cipher.getInstance("RSA/ECB/OAEPwithSHA-256andMGF1Padding")`,
which specifies the main digest and leaves the MGF1 digest unspecified. For Android
Keystore, SHA-1 is used for the MGF1 digest, whereas for other Android
cryptographic providers, the two digests are the same.

To have more control over the digests that your app uses, request a
cipher with OAEPPadding, as in `Cipher.getInstance("RSA/ECB/OAEPPadding")`, and
provide an `OAEPParameterSpec` to `init()` to explicitly choose both digests.
This is shown in the code that follows:

### Kotlin

```
val key: Key = ...
val cipher = Cipher.getInstance("RSA/ECB/OAEPPadding")
        .apply {
            // To use SHA-256 the main digest and SHA-1 as the MGF1 digest
            init(Cipher.ENCRYPT_MODE, key, OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA1, PSource.PSpecified.DEFAULT))
            // To use SHA-256 for both digests
            init(Cipher.ENCRYPT_MODE, key, OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA256, PSource.PSpecified.DEFAULT))
        }
```

### Java

```
Key key = ...;
Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");
// To use SHA-256 the main digest and SHA-1 as the MGF1 digest
cipher.init(Cipher.ENCRYPT_MODE, key, new OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA1, PSource.PSpecified.DEFAULT));
// To use SHA-256 for both digests
cipher.init(Cipher.ENCRYPT_MODE, key, new OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA256, PSource.PSpecified.DEFAULT));
```

## Deprecated functionality

The following sections describe deprecated functionality. Don't use it in your
app.

### Bouncy Castle algorithms

The [Bouncy Castle](https://www.bouncycastle.org/)
implementations of many algorithms [are
deprecated](https://android-developers.googleblog.com/2018/03/cryptography-changes-in-android-p.html).
This only affects cases where you explicitly request the Bouncy Castle provider,
as shown in the following example:

### Kotlin

```
Cipher.getInstance("AES/CBC/PKCS7PADDING", "BC")
// OR
Cipher.getInstance("AES/CBC/PKCS7PADDING", Security.getProvider("BC"))
```

### Java

```
Cipher.getInstance("AES/CBC/PKCS7PADDING", "BC");
// OR
Cipher.getInstance("AES/CBC/PKCS7PADDING", Security.getProvider("BC"));
```

As noted in the section about
[specifying a provider only with the Android Keystore system](#provider-android-keystore),
requesting a specific provider is discouraged. If you follow
that guideline, this deprecation doesn't affect you.

### Password-based encryption ciphers without an initialization vector

Password-based encryption (PBE) ciphers that require an initialization vector
(IV) can obtain it from the key, if it's suitably constructed, or from an
explicitly passed IV. If you pass a PBE key that doesn't contain an IV and don't
pass an explicit IV, the PBE ciphers on Android currently assume an IV of zero.

When using PBE ciphers, always pass an explicit IV, as shown in the following
code snippet:

### Kotlin

```
val key: SecretKey = ...
val cipher = Cipher.getInstance("PBEWITHSHA256AND256BITAES-CBC-BC")
val iv = ByteArray(16)
SecureRandom().nextBytes(iv)
cipher.init(Cipher.ENCRYPT_MODE, key, IvParameterSpec(iv))
```

### Java

```
SecretKey key = ...;
Cipher cipher = Cipher.getInstance("PBEWITHSHA256AND256BITAES-CBC-BC");
byte[] iv = new byte[16];
new SecureRandom().nextBytes(iv);
cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(iv));
```

### Crypto provider

As of Android 9 (API level 28), the Crypto Java Cryptography Architecture
(JCA) provider has been removed. If your app requests an instance of the
Crypto provider, such as by calling the following method, a
[`NoSuchProviderException`](/reference/java/security/NoSuchProviderException)
occurs.

### Kotlin

```
SecureRandom.getInstance("SHA1PRNG", "Crypto")
```

### Java

```
SecureRandom.getInstance("SHA1PRNG", "Crypto");
```

### Jetpack security-crypto library

All APIs in the
[`security-crypto`](/reference/androidx/security/crypto/package-summary)
Jetpack library were deprecated in the stable release of
[version `1.1.0`](/jetpack/androidx/releases/security#security-crypto_version_110_2).
There won't be any subsequent releases of this library.

The deprecation annotations are visible if you have any of the following
dependencies in your app module's `build.gradle` file:

### Groovy

```
dependencies {
    implementation "androidx.security:security-crypto:1.1.0"
    // or
    implementation "androidx.security:security-crypto-ktx:1.1.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.security:security-crypto:1.1.0")
    // or
    implementation("androidx.security:security-crypto-ktx:1.1.0")
}
```

## Supported algorithms

These are the JCA algorithm identifiers that are supported on Android:

* [`AlgorithmParameterGenerator`](/reference/java/security/AlgorithmParameterGenerator)
* [`AlgorithmParameters`](/reference/java/security/AlgorithmParameters)
* [`CertPathBuilder`](/reference/java/security/cert/CertPathBuilder)
* [`CertPathValidator`](/reference/java/security/cert/CertPathValidator)
* [`CertStore`](/reference/java/security/cert/CertStore)
* [`CertificateFactory`](/reference/java/security/cert/CertificateFactory)
* [`Cipher`](/reference/kotlin/javax/crypto/Cipher)
* [`KeyAgreement`](/reference/kotlin/javax/crypto/KeyAgreement)
* [`KeyFactory`](/reference/java/security/KeyFactory)
* [`KeyGenerator`](/reference/kotlin/javax/crypto/KeyGenerator)
* [`KeyManagerFactory`](/reference/javax/net/ssl/KeyManagerFactory)
* [`KeyPairGenerator`](/reference/java/security/KeyPairGenerator)
* [`KeyStore`](/reference/java/security/KeyStore)
* [`Mac`](/reference/kotlin/javax/crypto/Mac)
* [`MessageDigest`](/reference/java/security/MessageDigest)
* [`SSLContext`](/reference/javax/net/ssl/SSLContext)
* [`SSLEngine.Supported`](/reference/javax/net/ssl/SSLEngine)
* [`SSLSocket.Supported`](/reference/javax/net/ssl/SSLSocket)
* [`SecretKeyFactory`](/reference/kotlin/javax/crypto/SecretKeyFactory)
* [`SecureRandom`](/reference/java/security/SecureRandom)
* [`Signature`](/reference/java/security/Signature)
* [`TrustManagerFactory`](/reference/javax/net/ssl/TrustManagerFactory)