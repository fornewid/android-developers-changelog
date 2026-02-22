---
title: https://developer.android.com/privacy-and-security/security-ssl
url: https://developer.android.com/privacy-and-security/security-ssl
source: md.txt
---

# Security with network protocols

Client-server encrypted interactions use[Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security)to protect your app's data.

This article discusses best practices related to secure network protocol best practices and[Public-Key Infrastructure (PKI)](https://en.wikipedia.org/wiki/Public-key_infrastructure)considerations. Read[Android Security Overview](https://source.android.com/tech/security/index.html)as well as[Permissions Overview](https://developer.android.com/guide/topics/security/permissions)for more details.

## Concepts

A server with a TLS certificate has a public key and a matching private key. The server uses[public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)to sign its certificate during the TLS handshake.

A simple handshake only proves that the server knows the certificate's private key. To address this situation, let the client trust multiple certificates. A given server is untrustworthy if its certificate doesn't appear in the client-side set of trusted certificates.

However, servers might use key rotation to change their certificate's public key with a new one. The server configuration change necessitates updating the client app. If the server is a third-party web service, such as a web browser or email app, it's more difficult to know when to update the client app.

Servers usually rely on[Certificate Authorities (CAs)](https://en.wikipedia.org/wiki/Certificate_authority)certificates to issue certificates, which keeps the client-side configuration more stable over time. A CA[signs](https://en.wikipedia.org/wiki/Digital_signature)a server certificate using its private key. The client can then check that the server has a platform-known CA certificate.

Trusted CAs are usually listed on the host platform. Android 8.0 (API level 26) includes over 100 CAs that are updated in each version and don't change between devices.

Client apps need a mechanism to verify the server because the CA offers certificates for numerous servers. The CA's certificate identifies the server using either a specific name, such as*gmail.com* , or using a wildcard, such as*\*.google.com*.

To view a website's server certificate information, use the[`openssl`](http://www.openssl.org/docs/apps/openssl.html)tool's`s_client`command, passing in the port number. By default, HTTPS uses port 443.

The command transmits`openssl s_client`output to`openssl x509`, which formats certificate information in[X.509 standard](https://en.wikipedia.org/wiki/X.509). The command requests the topic (server name) and issuer (CA).  

```
openssl s_client -connect WEBSITE-URL:443 | \
  openssl x509 -noout -subject -issuer
```

## An HTTPS example

Assuming you have a web server with a certificate issued by a well-known CA, you can make a secure request as shown in the following code:  

### Kotlin

```kotlin
val url = URL("https://wikipedia.org")
val urlConnection: URLConnection = url.openConnection()
val inputStream: InputStream = urlConnection.getInputStream()
copyInputStreamToOutputStream(inputStream, System.out)
```

### Java

```java
URL url = new URL("https://wikipedia.org");
URLConnection urlConnection = url.openConnection();
InputStream in = urlConnection.getInputStream();
copyInputStreamToOutputStream(in, System.out);
```

To customize HTTP requests, cast to[HttpURLConnection](https://developer.android.com/reference/java/net/HttpURLConnection). The Android`HttpURLConnection`documentation includes examples for handling request and response headers, publishing content, managing cookies, using proxies, caching responses, and more. The Android framework verifies certificates and hostnames using these APIs.

Use these APIs whenever possible. The following section covers common issues that require different solutions.

## Common problems verifying server certificates

Suppose that instead of returning content,[getInputStream()](https://developer.android.com/reference/java/net/URLConnection#getInputStream()), throws an exception:  

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found.
        at org.apache.harmony.xnet.provider.jsse.OpenSSLSocketImpl.startHandshake(OpenSSLSocketImpl.java:374)
        at libcore.net.http.HttpConnection.setupSecureSocket(HttpConnection.java:209)
        at libcore.net.http.HttpsURLConnectionImpl$HttpsEngine.makeSslConnection(HttpsURLConnectionImpl.java:478)
        at libcore.net.http.HttpsURLConnectionImpl$HttpsEngine.connect(HttpsURLConnectionImpl.java:433)
        at libcore.net.http.HttpEngine.sendSocketRequest(HttpEngine.java:290)
        at libcore.net.http.HttpEngine.sendRequest(HttpEngine.java:240)
        at libcore.net.http.HttpURLConnectionImpl.getResponse(HttpURLConnectionImpl.java:282)
        at libcore.net.http.HttpURLConnectionImpl.getInputStream(HttpURLConnectionImpl.java:177)
        at libcore.net.http.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:271)
```

This can happen for several reasons, including:

1. [The CA that issued the server certificate was unknown](https://developer.android.com/privacy-and-security/security-ssl#UnknownCa).
2. [The server certificate wasn't signed by a CA, but was self signed](https://developer.android.com/privacy-and-security/security-ssl#SelfSigned).
3. [The server configuration is missing an intermediate CA](https://developer.android.com/privacy-and-security/security-ssl#MissingCa).

The following sections discuss how to address these problems while keeping your connection to the server secure.

### Unknown certificate authority

The[SSLHandshakeException](https://developer.android.com/reference/javax/net/ssl/SSLHandshakeException)arises because the system doesn't trust the CA. This could be because you have a certificate from a new CA that Android doesn't trust or because your app is operating on an earlier version without the CA. Because it's private, a CA is rarely known. More often, a CA is unknown because it isn't a public CA, but rather a private one issued by an organization such as a government, corporation, or education institution for its own use.

To trust custom CAs without needing to change your app's code, change your[Network Security Config](https://developer.android.com/training/articles/security-config#TrustingAdditionalCas).

**Caution:** Many web sites describe a poor alternative solution, which is to install a[TrustManager](https://developer.android.com/reference/javax/net/ssl/TrustManager)that does nothing. Doing this leaves your users vulnerable to attacks when using a public Wi-Fi hotspot, because an attacker can use DNS tricks to send your users' traffic through a proxy that pretends to be your server. The attacker can then record passwords and other personal data. This works because the attacker can generate a certificate, and without a`TrustManager`validating that the certificate comes from a trusted source, you can't block this kind of attack. So don't do this, even temporarily. Instead, make your app trust the issuer of the server's certificate.

### Self-signed server certificate

Second,[SSLHandshakeException](https://developer.android.com/reference/javax/net/ssl/SSLHandshakeException)might occur because of a self-signed certificate, making the server its own CA. This is similar to an unknown certificate authority, so modify your application's Network Security Config to trust your self-signed certificates.

### Missing intermediate certificate authority

Third,[SSLHandshakeException](https://developer.android.com/reference/javax/net/ssl/SSLHandshakeException)occurs due to missing intermediate CA. Public CAs rarely sign server certificates. Instead, the root CA signs intermediate CAs.

To reduce compromise risk, CAs keep the root CA offline. However, operating systems like Android normally trust only root CAs directly, leaving a short trust gap between the server certificate---signed by the intermediate CA---and the certificate verifier, which recognizes the root CA.

To remove this trust gap, the server sends a chain of certificates from the server CA through any intermediates to a trusted root CA during the TLS handshake.

For example, here's the*mail.google.com* certificate chain as viewed by the[`openssl`](http://www.openssl.org/docs/apps/openssl.html)`s_client`command:  

```
$ openssl s_client -connect mail.google.com:443
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google LLC/CN=mail.google.com
   i:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
 1 s:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
   i:/C=US/O=VeriSign, Inc./OU=Class 3 Public Primary Certification Authority
---
```

This shows that the server sends a certificate for*mail.google.com* issued by the*Thawte SGC* CA, which is an intermediate CA, and a second certificate for the*Thawte SGC* CA issued by a*Verisign*CA, which is the primary CA that's trusted by Android.

However, a server might not be configured to include the necessary intermediate CA. For example, here is a server that can cause an error in Android browsers and exceptions in Android apps:  

```
$ openssl s_client -connect egov.uscis.gov:443
---
Certificate chain
 0 s:/C=US/ST=District Of Columbia/L=Washington/O=U.S. Department of Homeland Security/OU=United States Citizenship and Immigration Services/OU=Terms of use at www.verisign.com/rpa (c)05/CN=egov.uscis.gov
   i:/C=US/O=VeriSign, Inc./OU=VeriSign Trust Network/OU=Terms of use at https://www.verisign.com/rpa (c)10/CN=VeriSign Class 3 International Server CA - G3
---
```

Unlike an unknown CA or self-signed server certificate, most desktop browsers don't produce an error while communicating with this server. Desktop browsers cache trusted intermediate CAs. After learning about an intermediate CA from one site, a browser won't need it in the certificate chain again.

Some sites intentionally do this for resource-serving secondary web servers. To save bandwidth, they may serve their main HTML page from a server with a full certificate chain, but their pictures, CSS, and JavaScript without the CA. Unfortunately, occasionally these servers can be providing a web service you are trying to reach from your Android app, which isn't as tolerant.

To fix this issue, configure the server to include the intermediary CA in the server chain. Most CAs provide instructions on how to do this for common web servers.

## Warnings about using SSLSocket directly

So far, the examples have focused on HTTPS using[HttpsURLConnection](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection). Sometimes apps need to use TLS separate from HTTPS. For example, an email app might use TLS variants of SMTP, POP3, or IMAP. In those cases, the app can use[SSLSocket](https://developer.android.com/reference/javax/net/ssl/SSLSocket)directly, much the same way that`HttpsURLConnection`does internally.

The techniques described so far to deal with certificate verification issues also apply to`SSLSocket`. In fact, when using a custom[TrustManager](https://developer.android.com/reference/javax/net/ssl/TrustManager), what is passed to`HttpsURLConnection`is a[SSLSocketFactory](https://developer.android.com/reference/javax/net/ssl/SSLSocketFactory). So if you need to use a custom`TrustManager`with an`SSLSocket`, follow the same steps and use that`SSLSocketFactory`to create your`SSLSocket`.

**Caution:** `SSLSocket`**does not** perform hostname verification. It is up to your app to do its own hostname verification, preferably by calling[getDefaultHostnameVerifier()](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection#getDefaultHostnameVerifier())with the expected hostname. Also, be aware that[HostnameVerifier.verify()](https://developer.android.com/reference/javax/net/ssl/HostnameVerifier#verify(java.lang.String, javax.net.SSL.SSLSession))doesn't throw an exception on error. Instead, it returns a boolean result that you must explicitly check.

## Certificate validation

TLS relies on CAs to issue certificates to only the verified owners of servers and domains. In rare cases, CAs are either tricked or, in the case of[Comodo](https://en.wikipedia.org/wiki/Comodo_Group#Breach_of_security)or[DigiNotar](https://en.wikipedia.org/wiki/DigiNotar), breached, resulting in the certificates for a hostname being issued to someone other than the owner of the server or domain.

To mitigate this risk, Android handles certificate revocation system-wide, through a combination of a blocklist and certificate transparency, without relying on on-line certificate verification. In addition, Android will validate OCSP responses stapled to the TLS handshake.

To enable Certificate Transparency in your app, see the[Opt in to certificate transparency](https://developer.android.com/privacy-and-security/security-config#CertificateTransparencySummary)section in our Network Security Configuration documentation.

## Restricting your app to specific certificates

**Caution:**Certificate pinning, the practice of restricting the certificates that are considered valid for your app to those you have previously authorized, is not recommended for Android apps. Future server configuration changes, such as changing to another CA, render apps with pinned certificates unable to connect to the server without receiving a client software update.

If you want to restrict your app to accept only certificates that you specify, it's critical to include multiple backup pins, including at least one key that's fully in your control, and a sufficiently short expiration period to prevent compatibility issues. The[Network Security Config](https://developer.android.com/training/articles/security-config#CertificatePinning)provides pinning with these capabilities.

## Client certificates

This article focuses on the use of TLS to secure communications with servers. TLS also supports the notion of client certificates that let the server validate the identity of a client. While beyond the scope of this article, the techniques involved are similar to specifying a custom`TrustManager`.

## Nogotofail: A network traffic security testing tool

Nogotofail is a tool gives you an easy way to confirm that your apps are safe against known TLS/SSL vulnerabilities and misconfigurations. It's an automated, powerful, and scalable tool for testing network security issues on any device whose network traffic can be made to go through it.

Nogotofail is useful for three main use cases:

- Finding bugs and vulnerabilities.
- Verifying fixes and watching for regressions.
- Understanding what applications and devices are generating what traffic.

Nogotofail works for Android, iOS, Linux, Windows, ChromeOS, macOS, and in fact any device you use to connect to the internet. A client is available for configuring the settings and getting notifications on Android and Linux, and the attack engine itself can be deployed as a router, VPN server, or proxy.

You can access the tool at the[Nogotofail open source project](https://github.com/google/nogotofail).

## Updates to SSL and TLS

### Android 10

Some browsers, such as Google Chrome, allow users to choose a certificate when a TLS server sends a certificate request message as part of a TLS handshake. As of Android 10, KeyChain objects honor the issuers and key specification parameters when calling`KeyChain.choosePrivateKeyAlias()`to show users a certificate selection prompt. In particular, this prompt doesn't contain choices that don't adhere to server specifications.

If there are no user-selectable certificates available, as is the case when no certificates match the server specification or a device doesn't have any certificates installed, the certificate selection prompt doesn't appear at all.

In addition, it isn't necessary on Android 10 or higher to have a device screen lock to import keys or CA certificates into a KeyChain object.

#### TLS 1.3 enabled by default

In Android 10 and higher, TLS 1.3 is enabled by default for all TLS connections. Here are a few important details about our TLS 1.3 implementation:

- The TLS 1.3 cipher suites cannot be customized. The supported TLS 1.3 cipher suites are always enabled when TLS 1.3 is enabled. Any attempt to disable them by calling[`setEnabledCipherSuites()`](https://developer.android.com/reference/javax/net/ssl/SSLSocket#setEnabledCipherSuites(java.lang.String%5B%5D))is ignored.
- When TLS 1.3 is negotiated,[`HandshakeCompletedListener`](https://developer.android.com/reference/javax/net/ssl/HandshakeCompletedListener)objects are called before sessions are added to the session cache. (In TLS 1.2 and other previous versions, these objects are called after sessions are added to the session cache.)
- In some situations where SSLEngine instances throw an[`SSLHandshakeException`](https://developer.android.com/reference/javax/net/ssl/SSLHandshakeException)on previous versions of Android, these instances throw an[`SSLProtocolException`](https://developer.android.com/reference/javax/net/ssl/SSLProtocolException)instead on Android 10 and higher.
- 0-RTT mode isn't supported.

If desired, you can obtain an SSLContext that has TLS 1.3 disabled by calling[`SSLContext.getInstance("TLSv1.2")`](https://developer.android.com/reference/javax/net/ssl/SSLContext#getInstance(java.lang.String)). You can also enable or disable protocol versions on a per-connection basis by calling[`setEnabledProtocols()`](https://developer.android.com/reference/javax/net/ssl/SSLSocket#setEnabledProtocols(java.lang.String%5B%5D))on an appropriate object.

#### Certificates signed with SHA-1 aren't trusted in TLS

In Android 10, certificates that use the SHA-1 hash algorithm aren't trusted in TLS connections. Root CAs haven't issued such certificates since 2016, and they are no longer trusted in Chrome or other major browsers.

Any attempt to connect fails if the connection is to a site that presents a certificate using SHA-1.

#### KeyChain behavior changes and improvements

Some browsers, such as Google Chrome, allow users to choose a certificate when a TLS server sends a certificate request message as part of a TLS handshake. As of Android 10,[`KeyChain`](https://developer.android.com/reference/android/security/KeyChain)objects honor the issuers and key specification parameters when calling`KeyChain.choosePrivateKeyAlias()`to show users a certificate selection prompt. In particular, this prompt doesn't contain choices that don't adhere to server specifications.

If there are no user-selectable certificates available, as is the case when no certificates match the server specification or a device doesn't have any certificates installed, the certificate selection prompt doesn't appear at all.

In addition, it isn't necessary on Android 10 or higher to have a device screen lock to import keys or CA certificates into a KeyChain object.

#### Other TLS and cryptography changes

There have been several minor changes in the TLS and cryptography libraries that take effect on Android 10:

- The AES/GCM/NoPadding and ChaCha20/Poly1305/NoPadding ciphers return more accurate buffer sizes from`getOutputSize()`.
- The TLS_FALLBACK_SCSV cipher suite is omitted from connection attempts with a max protocol of TLS 1.2 or above. Because of improvements in TLS server implementations, we don't recommend attempting TLS-external fallback. Instead, we recommend relying on TLS version negotiation.
- ChaCha20-Poly1305 is an alias for ChaCha20/Poly1305/NoPadding.
- Hostnames with trailing dots aren't considered valid SNI hostnames.
- The supported_signature_algorithms extension in CertificateRequest is respected when choosing a signing key for certificate responses.
- Opaque signing keys, such as those from Android Keystore, can be used with RSA-PSS signatures in TLS.

#### HTTPS connection changes

If an app running Android 10 passes null into[`setSSLSocketFactory()`](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection#setSSLSocketFactory(javax.net.ssl.SSLSocketFactory)), an[`IllegalArgumentException`](https://developer.android.com/reference/java/lang/IllegalArgumentException)occurs. In previous versions, passing null into`setSSLSocketFactory()`had the same effect as passing in the current[default factory](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection#getDefaultSSLSocketFactory()).

### Android 11

#### SSL sockets use Conscrypt SSL engine by default

Android's default SSLSocket implementation is based on[`Conscrypt`](https://github.com/google/conscrypt). Since Android 11, that implementation is internally built on top of Conscrypt's SSLEngine.