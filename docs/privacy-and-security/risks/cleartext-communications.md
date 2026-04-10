---
title: https://developer.android.com/privacy-and-security/risks/cleartext-communications
url: https://developer.android.com/privacy-and-security/risks/cleartext-communications
source: md.txt
---

# Cleartext communications

<br />

**OWASP category:** [MASVS-NETWORK: Network Communication](https://mas.owasp.org/MASVS/08-MASVS-NETWORK)

## Overview

Allowing cleartext network communications in an Android app means that anyone monitoring network traffic can see and manipulate the data that is being transmitted. This is a vulnerability if the transmitted data includes sensitive information such as passwords, credit card numbers, or other personal information.

Regardless of if you are sending sensitive information or not, using cleartext can still be a vulnerability as cleartext traffic can also be manipulated through network attacks such as ARP or DNS poisoning, thus potentially enabling attackers to influence the behavior of an app.

## Impact

When an Android application sends or receives data in cleartext over a network, anyone who is monitoring the network can intercept and read that data. If this data includes sensitive information such as passwords, credit card numbers, or personal messages, this can lead to identity theft, financial fraud, and other serious problems.

For example, an app transmitting passwords in cleartext could expose these credentials to a malicious actor intercepting the traffic. This data could then be used to gain unauthorized access to the user's accounts.

## Risk: Unencrypted communication channels

Transmitting data over unencrypted communication channels exposes the data shared between the device and the application endpoints. Said data can be intercepted and potentially modified by an attacker.

### Mitigations

Data should be sent over encrypted communication channels. Secure protocols should be used as an alternative to protocols that don't offer encryption capabilities.

## Specific Risks

This section gathers risks that require non-standard mitigation strategies or were mitigated at certain SDK level and are here for completeness.

### Risk: HTTP

The guidance in this section applies only to apps that target Android 8.1 (API level 27) or earlier. Starting with Android 9 (API level 28), HTTP Clients such as URLConnection,[Cronet](https://developer.android.com/develop/connectivity/cronet), and[OkHttp](https://square.github.io/okhttp/)enforce the use of HTTPS, therefore cleartext support is disabled by default. However, be aware that other HTTP Client libraries such as[Ktor](https://ktor.io/)are unlikely to enforce these restrictions on cleartext and should be used with care.

#### Mitigations

Use the[NetworkSecurityConfig.xml](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted)feature to opt-out of cleartext traffic and enforce HTTPS for your app, with exceptions for only the specific domains required (usually for debugging purposes):  

### Xml

    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <base-config cleartextTrafficPermitted="false">
        <domain-config cleartextTrafficPermitted="true">
            <domain includeSubdomains="true">debug.domain.com</domain>
        </domain-config>
    </network-security-config>

This option helps prevent accidental regressions in apps due to changes in URLs provided by external sources such as backend servers.

*** ** * ** ***

### Risk: FTP

Using the FTP protocol to exchange files between devices presents several risks, the most significant being the lack of encryption over the communication channel. Safer alternatives such as SFTP or HTTPS should be used instead.

#### Mitigations

When implementing data exchange mechanisms over the internet in your application, you should use a secure protocol such as HTTPS. Android makes a[set of APIs](https://developer.android.com/develop/connectivity/network-ops/connecting)available that allow developers to create a client-server logic. This can be secured using[Transport Layer Security (TLS)](https://developer.android.com/privacy-and-security/security-ssl), ensuring that data exchange between two endpoints is encrypted, therefore preventing malicious users from eavesdropping on communications and retrieving sensitive data.

Commonly, client-server architectures rely on developer-owned APIs. If your application depends on a set of API endpoints, ensure security-in-depth by following these security best practices to protect HTTPS communications:

- Authentication -- Users should authenticate themselves using secure mechanisms such as[OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/native-app). Basic authentication is generally discouraged, as it doesn't provide session management mechanisms and, if credentials are improperly stored, can be decoded from Base64.
- Authorization -- Users should be restricted to access only intended resources following the principle of least-privilege. This can be implemented by adopting careful access control solutions for the application's assets.
- Ensure that thoughtful and most recent cipher suites are used, following security best practices. For example, consider supporting the[TLSv1.3 protocol](https://wiki.mozilla.org/Security/Server_Side_TLS)with backward compatibility, if needed, for HTTPS communications.

*** ** * ** ***

### Risk: Custom-Communication Protocols

Implementing custom communication protocols, or trying to implement well-known ones manually, can be dangerous.

While custom protocols allow developers to tailor a unique solution that adapts to the intended needs, any error during the development process can potentially result in security vulnerabilities. For example, errors in developing session handling mechanisms can potentially result in attackers being able to eavesdrop on communications, and retrieve sensitive information on the fly.

On the other hand, implementing well-known protocols such as HTTPS without using OS or well-maintained third-party libraries, increases the likelihood of introducing coding errors that may make it difficult, if not impossible, to update the protocol that you implemented when needed. Additionally, this can introduce the same kind of security vulnerabilities as using custom protocols.

#### Mitigations

##### Use maintained libraries to implement well-known communication protocols

To implement well-known protocols such as HTTPS in your application, OS libraries or maintained third-party libraries should be used.

This gives developers the security of opting for solutions that have been thoroughly tested, were improved over time, and are continuously receiving security updates to fix common vulnerabilities.

In addition, by opting for well-known protocols, developers benefit from broad compatibility across various systems, platforms, and IDEs, reducing the likelihood of human errors during the development process.

##### Use SFTP

This protocol encrypts the data in transit. Additional measures should be taken into consideration when using this kind of file exchange protocol:

- SFTP supports different kinds of authentication. Instead of password-based authentication, the public key authentication method should be used. Such keys should be securely created and stored,[Android Keystore](https://developer.android.com/privacy-and-security/keystore)is recommended for this purpose.
- Ensure that supported ciphers follow security best practices.

*** ** * ** ***

## Resources

- [Ktor](https://ktor.io/)
- [Perform network operations using Cronet](https://developer.android.com/develop/connectivity/cronet)
- [OkHttp](https://square.github.io/okhttp/)
- [Cleartext Traffic Opt-out for Network Security Configuration](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted)
- [Connect to the network](https://developer.android.com/develop/connectivity/network-ops/connecting)
- [Security with network protocols](https://developer.android.com/privacy-and-security/security-ssl)
- [OAuth 2.0 for Mobile \& Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)
- [HTTP Over TLS RFC](https://www.ietf.org/rfc/rfc2818.txt)
- [HTTP Authentication Schemes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemesl)
- [Mozilla web security recommendations](https://infosec.mozilla.org/guidelines/web_security)
- [Mozilla SSL recommended configuration generator](https://ssl-config.mozilla.org/)
- [Mozilla Server Side TLS recommendations](https://wiki.mozilla.org/Security/Server_Side_TLS)
- [OpenSSH main manual page](https://www.openssh.com/manual.html)
- [SSH RFC, which details the configurations and schemes that can be used for this protocol](https://www.ietf.org/rfc/rfc4251.txt)
- [Mozilla OpenSSH security recommendations](https://infosec.mozilla.org/guidelines/openssh.html)
- [Android Keystore system](https://developer.android.com/privacy-and-security/keystore)