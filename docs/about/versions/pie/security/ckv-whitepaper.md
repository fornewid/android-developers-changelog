---
title: https://developer.android.com/about/versions/pie/security/ckv-whitepaper
url: https://developer.android.com/about/versions/pie/security/ckv-whitepaper
source: md.txt
---

# Google Cloud Key Vault Service

We describe a cloud service that uses secure hardware to store cryptographic keys such that access to them is protected by a low entropy knowledge factor (e.g., a lockscreen PIN). The secure hardware is designed to prevent brute force attacks, by making the stored cryptographic keys permanently irretrievable after too many failed attempts to supply the correct knowledge factor.

**Author:** Shabsi Walfish  
**Version Date:**2018-03-06

Note: This document is still a work-in-progress, and details of the implementation are still being finalized. As the system stabilizes and more documentation can be produced, we will update this whitepaper with more detailed information (particularly in conjunction with relevant open source releases).

## Overview

Traditionally, encryption (which is used to ensure data privacy) requires the use of secrets that have high entropy from the attacker's perspective. High entropy is required because the encryption scheme must resist brute force attacks that explore the space of all likely secrets until the correct one is found. Given today's availability of computational power, a reasonable minimum entropy requirement for cryptographic secrets might be in the neighborhood of 70 to 80 bits. Unfortunately, human beings find it very difficult to memorize and reliably recall passwords or other secrets with that amount of entropy^[1](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fn1)^, especially if they are rarely used (but frequent use of a high entropy password is difficult and tedious). This leaves us with a challenging problem: how can we protect private data with encryption technology, if we want the secret to be a "knowledge factor" that is very likely to be remembered by the user? For a variety of reasons, this problem is so hard to solve that Cloud storage services typically only encrypt data with secrets that are managed by the Cloud storage provider itself, rather than relying on the user to remember their own secret.

One approach to bridge the gap between the requirements for cryptographic secrets and human memorable secrets is to use a Cloud Key Vault (CKV) service to store a high entropy "recovery key", protected by a low entropy human memorable secret. The CKV service will release the recovery key only to a party that proves knowledge of the correct human memorable secret. Brute force attacks against the human memorable secret can be thwarted by the CKV service, which will enforce an absolute limit on the number of failed attempts to prove knowledge of the secret. The recovery key itself is a standard cryptographic symmetric key, suitable for use with an (authenticated) encryption scheme that can easily encrypt a large volume of data (such as a disk backup) that can safely be stored anywhere -- such encrypted data is useless to anyone who cannot obtain the recovery key.

This whitepaper describes our approach to constructing a Cloud Key Vault service using Trusted Hardware Modules (THMs). Our first implementation of the CKV service is designed to protect recovery keys with the user's Lock Screen Knowledge Factor (LSKF) -- the secret PIN, password, or swipe pattern used to unlock smartphones. Human beings can reliably remember their LSKF. At the same time, such LSKF secrets typically have just enough entropy to resist an attacker who has a very limited number of attempts, making them a good fit for the CKV service.

The first application of our Cloud Key Vault service will be to enable client-side encrypted Android backups. Previously, files encrypted locally on the Android device used a key protected with the user's LSKF, but the backups of those files stored (and encrypted) in the Cloud were not protected by the LSKF. For the first time, the Cloud Key Vault enables lock screen protection for Android backups stored in the Cloud as well. This means that Google's servers have no ability to access or restore the contents of the encrypted backups -- only a device with the user's LSKF can decrypt the backups.

### Core Concepts

Initially, the only supported client platform for the Cloud Key Vault service is the Android 9 Pie operating system, and when we refer to the client throughout this whitepaper we are referring to a device running the Android 9 Pie operating system with Google Play services. Our server side implementation runs on specially designated Google servers that have an extra Titan chip^[2](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fn2)^installed in them. The Google-designed Titan chip serves as the hardware component in our Trusted Hardware Module, and we specially provision it with a custom bootloader and firmware that implements our protocols and security enforcement mechanisms (as described herein). We use hardware attestation techniques in order to gain assurances that our protocol is really running on the Titan hardware.

The CKV service must scale to handle traffic from billions^[3](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fn3)^of Android devices, without losing any significant amount of user data due to hardware failures (e.g., burned-out chips) or experiencing any extended outages due to data center maintenance. For this reason, the servers with the Titan chips on them are organized into cohorts, where each cohort consists of several independent THMs that each contain a copy of the same key material. A given cohort will be distributed across physically disparate data centers in different maintenance zones, in order to ensure that the system can meet its availability and reliability goals. For scalability, clients will be sharded off to a number of different cohorts, so that we can adjust the capacity of the service by just adding more servers to increase the number of available cohorts.

We are now ready to enumerate the major components of the Cloud Key Vault service architecture.

#### Architectural Components / Glossary

**Lock Screen Knowledge Factor (LSKF):**A human-memorable secret, such as a short PIN, a swipe pattern over a 3 x 3 dot grid, or a password. This secret is used to protect the ability to unlock the device locally, and is considered to be a primary (or "strong") authentication factor for the user's local device screen lock.

**Client:**An end user device running the Android 9 Pie operating system and Google Play services, or equivalently supported software.

:   **Android Framework:** we use this generic term (or just**the Framework**) to refer to the APIs in the Android 9 Pie or later, and it is not meant to refer to any earlier releases.

    **Google Play services:**A collection of services and apps that run on the end user device, which enable it to work with Google's account system and custom server APIs.

    **Recovery Agent:**A system application running as part of Google Play services in user-space on an Android 9 Pie device (or similar). The Recovery Agent is responsible to execute the Client side of the various protocols, and to interface with the Android Operating System as necessary in order to craft any protocol messages that involve the LSKF.

    **Recovery Claim:**When the user wishes to retrieve the Recovery Key, they must create a Recovery Claim, which has an encrypted copy of the LSKF that the user claims to know. Typically, the user will be asked to enter their old device's LSKF on a new device that is trying to access the Recovery Key of the old one.

    **Recovery Key:**A cryptographic secret key that is protected by the Cloud Key Vault service, and is used to encrypt (and authenticate) data at the Client device. Once the Recovery Key has been put into a Vault (see below) the local copy can be deleted as soon as the Client is done using it to encrypt data.

**Cloud Key Vault (CKV) Service:**An internet service that enables Client devices to store cryptographic keys that are protected by a human-memorable LSKF.

:   **Cohort:**A collection of Vault Servers/THMs that are able to serve as redundant replicas of each other.

    **Cohort Public Key**: The public key from a key pair generated by a specific Cohort of THMs. The corresponding private key is only available inside of the THMs that were in the Cohort at key generation time.

    **Trusted Hardware Module (THM):**A dedicated security module (microcontroller) designed to provide a minimal and trustworthy computing environment. At a minimum, the secure element must be able to generate and/or store secret keys, and maintain some non-volatile evolving state (so that it can prevent attacks involving resets to an earlier state).

    **Vault:**A particular entry in the CKV Service's database, containing a single device's LSKF protected Recovery Key. An end user may have multiple Vaults on file, each corresponding to a different device or LSKF. Only the THM in a Vault Server can examine or extract the contents of a Vault.

    **Vault Server:**A general purpose machine operating in a Google data center that has been specially retrofitted to add a Trusted Hardware Module (THM).

### Protocol Design

The CKV protocol consists of several phases, as follows:

#### Initialization

To initialize the system, Google will supply a public key for a "root of trust" that the Framework will use to verify Google's hardware attestations. The signing key for this root of trust is stored offline and carefully secured such that it requires the participation of multiple employees in order to sign with it. The public key for this root of trust is baked into the Android OS, and can only be changed via an OS update.

Google also periodically publishes a list of public keys for each Cohort of THMs, together with an attestation on the list. The attestation on the list uses a signature that chains back to the root of trust. Each update of the published list also contains a sequence number, so that it is possible to prevent rollbacks. The Recovery Agent will fetch the most recent published list of Cohort public keys and supply it to the Framework. The Framework then verifies the attestation and randomly selects a Cohort Public Key from the list to be used in the Vault Creation phase.

#### Vault Creation

After helping the Framework complete Initialization by fetching the list of*Cohort Public Keys* , the Recovery Agent will request the Framework to create a new Vault. Whenever the LSKF is next entered by the user, the Framework will generate a fresh*Recovery Key* and encrypt it first with a key derived from a hash of the LSKF, and then with the*Cohort Public Key*selected by the Framework during Initialization. The resulting encrypted blob is the Vault that is passed back by the Framework to the Recovery Agent, which then uploads it to Google's CKV service.

#### Vault Opening

When the*Recovery Agent* on new device needs to get access to the*Recovery Key* that is stored in a particular*Vault* , it will first prompt the user to enter the LSKF of the original device that created the*Vault* . The*Recovery Agent* will then ask the Framework to create a*Recovery Claim* using that LSKF. The Framework will generate a fresh Claimant Key, and encrypt that Claimant Key as well as the hash of the claimed LSKF, with the same*Cohort Public Key* that the*Vault* was originally encrypted with. The resulting encrypted blob is called the*Recovery Claim*, and the Framework passes this to the Recovery Agent, which then presents it to the CKV service.

The CKV routes the*Recovery Claim* (and its corresponding*Vault* ) to the*Vault Servers* that are part of the correct Cohort. The THM in the Vault Servers then decrypts the*Recovery Claim* and attempts to extract the*Recovery Key* from the original*Vault* by using the claimed LSKF hash (to derive the inner encryption key). If the original LSKF hash and the claimed LSKF hash match, the THM will extract the*Recovery Key* from the Vault and re-encrypt it with the*Claimant Key* that was in the*Recovery Claim* . If not, the THM will bump a failed attempt counter. Once the failed attempt counter reaches its limit, the THM will refuse to process any subsequent*Recovery Claim* s for this*Vault*.

Finally, if all went well, the re-encrypted*Recovery Key* (which is now encrypted under the*Claimant Key* ) is sent back from the Vault Server all the way to the Framework. The Framework uses its copy of the*Claimant Key* to decrypt the*Recovery Key*, and the protocol is now complete.

## Security Measures

The Cloud Key Vault system aims to provide "defense in depth" by including security protections at multiple levels of our stack. To give a sense of how these protections work, we will start by describing the Client and work our way up the stack to the Cloud Key Vault Service.

### Client Security

Depending on the particular OEM and device, the Lock Screen Knowledge Factor (LSKF) is normally stored and protected on the device using a variety of methods that vary by OEM. For example, Google's Pixel 2 devices make use of a tamper-resistant hardware security module to store the LSKF at rest, and to enforce hardware based rate limits on LSKF validation. The new Framework APIs that are being introduced to enable the use of the Cloud Key Vault are designed to preserve existing security guarantees to the greatest extent possible, even when the device uses such a hardware security module to protect storage of the LSKF.

We will focus this section specifically on the relevant security issues and protections that affect the new Cloud Key Vault feature, rather than attempting to provide a complete picture of all the security mechanisms associated with the LSKF.

#### Securing the Framework APIs

The new Framework APIs that were added to support the CKV service are marked as @SystemApi and require special permissions, which ensure they are only available to OEM approved system apps such as Google Play services. This largely removes any direct attack surface that might be exposed to apps the user installs on the device.

The Framework APIs also ensure that Vaults are only created for Cohort Public Keys that were attested by a root of trust. The root of trust is baked into the Framework by the OEM when it is shipped, and cannot be changed without an OS update. This provides confidence that the LSKF is only being used to create Vaults that will properly enforce hardware-based brute force protections. By relying on the THMs in the Cloud Key Vault service for brute force protection for the LSKF, we can achieve security comparable to using secure hardware on the device for the same thing (as Google Pixel 2 devices do).

Since we don't assume that the LSKF will be stored anywhere on the device outside of secure hardware, a new Vault can only be created immediately following a device unlock. At the time the user enters the LSKF to unlock the device, the LSKF is briefly made available to the Framework in RAM. That is the moment at which the new API to create the Vault makes use of it. It is not possible to create a new LSKF protected Vault while the device is locked, because the LSKF is not available.

#### Securing the Recovery Agent

The primary security protection we provide at the Recovery Agent is that the protocol is designed to prevent the Recovery Agent from ever seeing the LSKF of the current device or any Recovery Keys. Only the Framework should see those things on the Client side, making it much harder to exploit any potential bugs or security vulnerabilities in the Recovery Agent. The Recovery Agent is mostly used to manage lifecycle events and the passing of data back and forth between the Cloud and the Framework. The sole exception to this happens during a recovery just prior to the Vault Opening protocol, when the user must enter the old device's LSKF -- the UI that gathers the claimed LSKF for the old device is implemented in the Recovery Agent^[4](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fn4)^. However, the Recovery Agent implementation does "forget" the claimed LSKF as soon as the Framework takes over construction of the Recovery Claim.

### Security Features of the Protocol

While a full analysis of the protocol is beyond the scope of this document, we want to highlight a few of the protections built-in to the protocol. In particular, the protocol only uses the hash of the LSKF throughout. This means that, if the LSKF has high entropy (e.g., if it is a good high-entropy password) storing the Vault is strictly better than storing a password hash, and in this case the password hash can provide a measure of security independent of the security of the THMs. For this reason, we do support salted "memory hard" hashing of the LSKF as part of the protocol. We also cryptographically bind the Vault to an identifier for the device that created it, and bind the Recovery Claim to a nonce that is used as a challenge during the Vault Opening protocol to ensure that the Recovery Claim is fresh.

Since the Recovery Key is generated freshly on each Vault creation, we implement key rotation by overwriting an existing Vault entry with a newly created Vault. The address for the failed attempt counter used by the Vault is selected during Vault creation, and the Framework ensures that the counter address used for any subsequent Vaults will not change unless either the LSKF has been changed or there is a new attested list of Cohort Public Keys. Thus, rotation of the Recovery Key can be done without harming the brute force protection for the LSKF.

### Server Security for the Cloud Key Vault Service

The server is implemented using a combination of software running on ordinary server hardware, and firmware running on specialized hardware (the Titan chip). We will describe the protections offered at each layer.

#### Hardware protections

The primary security protection implemented on the server side of the CKV service is the Trusted Hardware Modules (THMs) that are built using Google's own custom-designed Titan chips. The chips are running firmware that exposes the necessary APIs to implement the CKV protocols. In particular, they can generate and securely share a key pair with other members of their Cohort such that the firmware logic protects the private key from leaking outside of the Titan chips in the Cohort. They can also perform the Vault Opening operation, and maintain a strictly incrementing per-Vault counter of failed attempts (where the counter is backed by state stored inside the Titan chip). A more detailed description of the protocol executed by the CKV Titan chip firmware will be provided in a future release of this document.

Given that the server security derives from the firmware logic in the Titan chips, we must ensure that the logic does not change in a way that allows the chips to leak secrets or ignore the counter limits. To accomplish this goal, we also alter the Titan boot loader to ensure that the chip's stored data (such as the private key for the Cohort) is completely wiped before any update is applied. The downside of this protection is that we cannot patch bugs in the firmware without experiencing some data loss--updating the firmware is functionally equivalent to destroying the existing hardware and replacing it with new chips. In the event that a critical firmware patch is required, Google will need to produce and publish an entirely new list of attested Cohort Public Keys and gradually migrate all users over to the new list. To mitigate this risk, we try to keep the firmware codebase fairly minimal, and carefully audit it for any potential security issues.

#### Software protections

In addition to the hard per-Vault failure limits imposed by the THMs, the CKV service also implements software-based rate limiting. The rate limiting is designed to prevent a hijacker from getting into a user's account and quickly exhausting their limit of failed recovery attempts, effectively locking out the real user's access to their Recovery Keys. Similar to the time delays imposed by the user's device after too many failed attempts to unlock the screen, the CKV service will enforce an increasing time delay after each subsequent failed Vault Opening request.

We also implement standard security measures for Cloud services that host user data, including strict access controls, monitoring, and auditing.

## Detailed Protocol Specification

The detailed protocol specification is still in progress, and this document will be updated to include those details along with the publication of the client code in the Android Open Source Project later this year.

## Notes

1. "Towards Reliable Storage of 56-bit Secrets in Human Memory \| USENIX." 1 Aug. 2014,<https://www.usenix.org/node/184458>.[↩](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fnref1)
2. "Google Cloud Platform Blog: Titan in depth: Security in plaintext." 24 Aug. 2017,<https://cloudplatform.googleblog.com/2017/08/Titan-in-depth-security-in-plaintext.html>.[↩](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fnref2)
3. "Google announces over 2 billion monthly active devices on Android ...." 17 May. 2017,<https://www.theverge.com/2017/5/17/15654454/android-reaches-2-billion-monthly-active-users>.[↩](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fnref3)
4. This allows us to provide flexible UIs for entering the LSKF of another device -- the Framework of the current device might not have an appropriate UI for the entering the LSKF of the old device.[↩](https://developer.android.com/about/versions/pie/security/ckv-whitepaper#fnref4)