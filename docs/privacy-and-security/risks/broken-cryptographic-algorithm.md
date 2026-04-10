---
title: https://developer.android.com/privacy-and-security/risks/broken-cryptographic-algorithm
url: https://developer.android.com/privacy-and-security/risks/broken-cryptographic-algorithm
source: md.txt
---

# Broken or risky cryptographic algorithm

<br />

**OWASP category:** [MASVS-CRYPTO: Cryptography](https://mas.owasp.org/MASVS/06-MASVS-CRYPTO)

## Overview

Despite the widespread use of cryptography to protect data confidentiality and integrity, a significant risk arises when developers inadvertently implement weak or outdated cryptographic algorithms. This vulnerability stems from the inherent weaknesses in these algorithms, which can be exploited by malicious actors possessing the necessary computational power or knowledge. The consequences of such exploitation can be severe, potentially leading to unauthorized access, data breaches, and manipulation of sensitive information.

## Impact

Sensitive data can be exposed, modified, or forged. Broken or risky cryptographic algorithms might lead to vulnerabilities and can be abused to decrypt sensitive information, tamper with data, or impersonate legitimate entities. The impact of exploiting such vulnerabilities can range from data breaches and financial losses to reputational damage and loss of user trust.

## Risk: Weak or broken cryptographic hash functions

The use of weak or broken cryptographic hash functions (such as`MD5`or`SHA1`) poses a significant risk to the security and integrity of data. Hash functions are designed to create unique, fixed-length fingerprints (hashes) of input data, making them useful for various purposes, including data integrity verification, password storage, and digital signatures. However, when weak or compromised hash functions are employed, several vulnerabilities can arise:

- **Collision Attacks**: Weak hash functions are susceptible to collision attacks, where an attacker finds two different inputs that produce the same hash value. This can allow them to substitute malicious data for legitimate data without detection, compromising data integrity.
- **Data Breaches**: If passwords are hashed with a weak algorithm, a successful breach of a system could lead to the exposure of user credentials. Attackers could then use rainbow tables or other techniques to crack the passwords, gaining unauthorized access to accounts.
- **Repudiation of Digital Signatures**: Weak hash functions used in digital signatures can be exploited to create forged signatures, making it difficult to determine the authenticity and integrity of documents or messages.

### Mitigations

To mitigate these risks, it is crucial to use strong, well-vetted cryptographic hash functions like[`SHA-2`](https://en.wikipedia.org/wiki/SHA-2)or[`SHA-3`](https://en.wikipedia.org/wiki/SHA-3), and to keep them updated as new vulnerabilities are discovered. Additionally, adopting security practices such as salting passwords and using password-specific hashing algorithms like[`bcrypt`](https://en.wikipedia.org/wiki/Bcrypt)or[`Argon2`](https://en.wikipedia.org/wiki/Argon2)can further enhance data protection.

*** ** * ** ***

## Risk: Weak or broken cryptographic encryption functions

The use of weak or broken cryptographic encryption functions (such as`DES`or`RC4`) poses severe risks to the confidentiality of sensitive data. Encryption is designed to protect information by transforming it into an unreadable format, but if the encryption algorithm is flawed, these protections can be bypassed:

- **Data Breaches:**Weak encryption algorithms are susceptible to various attacks, including brute-force attacks, known-plaintext attacks, and cryptanalysis techniques. If successful, these attacks can expose encrypted data, allowing unauthorized access to sensitive information such as personal details, financial records, or confidential business data.
- **Data Manipulation and Tampering:**Even if an attacker cannot fully decrypt the data, they may still be able to manipulate it without detection if the encryption algorithm is weak. This can lead to unauthorized modifications of data, potentially resulting in fraud, misrepresentation, or other malicious activities.

### Mitigations

#### Use strong cryptographic algorithms in encryption functions

To mitigate these risks, it is crucial to use strong, well-vetted cryptographic algorithms and follow best practices for key management and encryption implementation. Regularly updating encryption algorithms and staying informed about emerging threats is also essential to maintain robust data security.

Some recommended default algorithms to use:

- Symmetric encryption:
  - `AES-128`/`AES-256`with[`GCM`](https://en.wikipedia.org/wiki/Galois/Counter_Mode)mode
  - `Chacha20`
- Asymmetric encryption:
  - `RSA-2048`/`RSA-4096`with[`OAEP`](https://datatracker.ietf.org/doc/html/rfc8017)padding

#### Use secure primitives from a cryptography library to reduce common pitfalls

While selecting an appropriate encryption algorithm is crucial, to truly minimize security vulnerabilities, consider using a cryptography library that offers a streamlined API and emphasizes secure default configurations. This approach not only strengthens the security of your applications but also significantly reduces the likelihood of introducing vulnerabilities through coding errors. For example,[Tink](https://developers.google.com/tink)simplifies encryption choices by offering two distinct options:[`AEAD`](https://developers.google.com/tink/streaming-aead)and[`Hybrid`](https://developers.google.com/tink/hybrid)encryption, making it easier for developers to make informed security decisions.

*** ** * ** ***

## Risk: Weak or broken cryptographic signature functions

The use of weak or broken cryptographic signature functions (such as[`RSA-PKCS#1 v1.5`](https://www.rfc-editor.org/rfc/rfc2313), or the ones based on weak hash functions) poses severe risks to the integrity of data and communication. Digital signatures are designed to provide authentication, non-repudiation, and data integrity, ensuring that a message or document originates from a specific sender and has not been tampered with. However, when the underlying signature algorithm is flawed, these assurances can be compromised:

- **Forging signatures**: Weak signature algorithms can be vulnerable to attacks that allow malicious actors to create forged signatures. This means they can impersonate legitimate entities, fabricate documents, or tamper with messages without detection.
- **Repudiation of signatures**: If a signature algorithm is broken, a signer may be able to falsely claim that they did not sign a document, undermining the principle of non-repudiation and creating legal and logistical challenges.
- **Data manipulation and tampering**: In scenarios where signatures are used to protect the integrity of data, a weak algorithm could allow attackers to modify the data without invalidating the signature, leading to undetected tampering and potential compromise of critical information.

### Mitigations

#### Use strong cryptographic signature algorithms

To mitigate these risks, it is crucial to use strong, well-vetted cryptographic signature algorithms:

- `RSA-2048`/`RSA-4096`with[`PSS`](https://datatracker.ietf.org/doc/html/rfc8017)padding
- Elliptic Curve Digital Signature Algorithm ([`ECDSA`](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)) with secure curves

#### Use secure primitives from a cryptography library to reduce common pitfalls

Choosing the right signature algorithm is essential, but to truly minimize security vulnerabilities, consider a cryptography library that provides robust security assurances by default.[Tink](https://developers.google.com/tink), for example, simplifies signature choices by offering`ECDSA`with secure curves as its default option, all within a straightforward and comprehensive API. This approach not only enhances security but also streamlines development by eliminating the need for complex configuration or decision-making.

*** ** * ** ***

## Resources

- [Tink cryptography library](https://developers.google.com/tink/what-is)
- [Android App quality: Cryptography](https://developer.android.com/privacy-and-security/cryptography)
- [Digital Signature with Tink](https://developers.google.com/tink/digital-signature)
- [Hybrid Encryption with Tink](https://developers.google.com/tink/hybrid)
- [Authenticated Encryption with Tink](https://developers.google.com/tink/streaming-aead)
- [Weak or broken cryptographic hash and encryption functions Android security lint](https://github.com/google/android-security-lints/blob/main/checks/src/main/java/com/example/lint/checks/BadCryptographyUsageDetector.kt)
- [CWE-327: Use of a Broken or Risky Cryptographic Algorithm](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-328: Use of Weak Hash](https://cwe.mitre.org/data/definitions/328.html)
- [CWE-780: Use of RSA Algorithm without OAEP](https://cwe.mitre.org/data/definitions/780.html)
- [NIST page about Approved Hash Functions](https://csrc.nist.gov/projects/hash-functions)
- [Advanced Encryption Standard (Wikipedia)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [Secure Hash Algorithm 2 (Wikipedia)](https://en.wikipedia.org/wiki/SHA-2)
- [Secure Hash Algorithm 3 (Wikipedia)](https://en.wikipedia.org/wiki/SHA-3)
- [RSA cryptosystem (Wikipedia)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Elliptic Curve Digital Signature Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [Stream cipher ChaCha (Wikipedia)](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [Salting password (Wikipedia)](https://en.wikipedia.org/wiki/Salt_(cryptography))
- [Hybrid cryptosystem (Wikipedia)](https://en.wikipedia.org/wiki/Hybrid_cryptosystem)
- [Authenticated encryption](https://en.wikipedia.org/wiki/Authenticated_encryption)