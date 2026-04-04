---
title: Enable private communication with Key Verifier  |  Privacy  |  Android Developers
url: https://developer.android.com/privacy-and-security/key-verifier
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Privacy](https://developer.android.com/privacy)
* [Guides](https://developer.android.com/privacy-and-security/about)

# Enable private communication with Key Verifier Stay organized with collections Save and categorize content based on your preferences.




The **Key Verifier SDK** works in conjunction with the
[**Android System Key Verifier**](/privacy-and-security/key-verifier/key-verifier), a Google system service available on
Android devices.

This service aims to improve **user privacy** in end-to-end encrypted (E2EE)
messaging applications. Key Verifier provides a unified system for public key
verification across different client apps.

The fundamental goal of Key Verifier is to enable **private communication**
through encryption by validating that you are communicating with the person you
expect.

The following are main functions of the system:

* **Key Verification**: Allows a user to verify a contact's public keys to
  confirm they are communicating with the person they intend to message.
* **Verification Methods**: Users can verify keys through a user interface
  that supports **QR code scanning or number comparison** (matching a sequence
  of numbers).
* **Key Management**: Exposes a service through an **AIDL interface** for
  client applications to insert, read, update, or delete keys.
* **Client SDK**: Provided to all apps, such as messaging or contacts
  management apps, to interact with the service.

Learn more about Key Verifier in the following documentation:

* [Android System Key Verifier](/privacy-and-security/key-verifier/key-verifier)
* [Key Verifier reference documentation](/privacy-and-security/key-verifier/reference)