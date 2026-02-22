---
title: https://developer.android.com/privacy-and-security/risks/insecure-api-usage
url: https://developer.android.com/privacy-and-security/risks/insecure-api-usage
source: md.txt
---

# Insecure API usage

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

Many mobile applications use an external API to provide features. Traditionally, a static token or key is used to authenticate the application connecting to the service.

However, in the context of a client-server setting (or mobile app and API) -- using a static key is generally not considered a secure authentication method for accessing sensitive data or services. Unlike internal infrastructure, anyone can access an external API and abuse the service if they have access to this key.

For example, it is possible for a static key to either be reverse engineered from the application or intercepted when a mobile application communicates with the external API. It is also more likely that this static key will be hard-coded within the application.

The risk to the API data and services occurs when sufficiently secure authentication and access controls are not used.

When using a static key, the API can be exploited by replaying requests or constructing new requests using the (intercepted or reverse engineered) key without any time restrictions.

## Impact

If a developer is paying for an AI or ML API service, it would be relatively easy for an attacker to steal this key and run up debt on their service or use it to create fake content.

Any user data, files, or PII stored on the API would be freely available, leading to damaging leaks.

An attacker might also use this access to conduct fraud, redirect services, and, in rare cases, gain full control of the servers.

## Mitigations

### Stateful API

If the application provides a user login or has the ability to track user sessions, we recommend developers use an API service like[Google Cloud](https://cloud.google.com/apis)for stateful integration with their app.

In addition, use secure authentication, client validation, and session controls provided by the API service, and consider using a dynamic token as an alternative to a static key. Make sure the token expires in a reasonably short time (1 hour is typical).

The dynamic token should then be used for authentication to provide access to the API.[These guidelines](https://developers.google.com/identity/protocols/oauth2/native-app#android)show how this can be achieved using OAuth 2.0. In addition to those guidelines, OAuth 2.0 can be further strengthened to reduce vulnerabilities in your Android app by implementing the following features.

Implement proper error handling and logging:

- Handle OAuth errors gracefully, visibly, and log them for debugging purposes.
  - A reduced attack surface will also help you identify and troubleshoot any issues that may arise.
  - Ensure any messages logged or presented to the user are clear but don't contain[information](https://owasp.org/www-community/Improper_Error_Handling)useful to an adversary.

Securely configure OAuth in the application:

- Send the`redirect_uri`parameter to both the authorization and token endpoints.
- If your app uses OAuth with a third-party service, configure Cross-Origin Resource Sharing ([CORS](https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny)) to restrict access to your app's resources.
  - This will help prevent unauthorized cross-site scripting ([XSS](https://owasp.org/www-community/attacks/xss/)) attacks.
- Use the state parameter to prevent[CSRF](https://owasp.org/www-community/attacks/csrf)attacks.

Use a security library:

- Consider using a security library like[AppAuth](https://openid.github.io/AppAuth-Android/)to simplify the implementation of secure OAuth[flows](https://developers.google.com/identity/protocols/oauth2/native-app).
  - These Android libraries can help automate many of the security best practices mentioned earlier.

Other authentication methods including Firebase and Google ID tokens are described in the[OpenAPI documentation](https://cloud.google.com/endpoints/docs/openapi/authentication-method).

### Stateless API

If the API service does not offer any of the protections recommended earlier and there is a requirement for stateless sessions without a user login, developers may need to provide their own middleware solutions.

This would involve 'proxying' requests between the app and API endpoint. One method to do this is to use[JSON Web Tokens](https://en.wikipedia.org/wiki/JSON_Web_Token)(JWT) and[JSON Web Signature](https://en.wikipedia.org/wiki/JSON_Web_Signature)(JWS), or provide a fully authenticated service as recommended earlier. This provides a way of storing the vulnerable static key server-side rather than in the application (client).

There are inherent problems with providing an end-to-end stateless solution in mobile applications. Some of the most critical challenges are validation of the client (app) and securely storing the private key or secret on the device.

The[Play Integrity API](https://developer.android.com/google/play/integrity/overview)provides validation of the integrity of the application and requests. This can mitigate some of the scenarios where this access can be abused. As for key management, in many cases[the keystore](https://developer.android.com/privacy-and-security/keystore)is the best location for secure storage of private keys.

Some mobile applications use a registration phase to check the integrity of the application and provide a key using a secure exchange. These methods are complex and out of scope of this document. However, a[cloud key management service](https://cloud.google.com/kms/docs/key-management-service)is one potential solution.

## Resources

- [OAuth 2.0 recommendations](https://developers.google.com/identity/protocols/oauth2/native-app)
- [Advice on using OAuth 2.0 and JWT](https://tech.justeattakeaway.com/2019/12/04/lessons-learned-from-handling-jwt-on-mobile/)
- [OAuth client recommendations](https://portswigger.net/web-security/oauth/preventing)