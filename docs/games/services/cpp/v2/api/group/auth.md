---
title: Play Games Services Auth  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/auth
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# Play Games Services Auth

Auth scopes for Play Games Services native SDK.

## Summary

| Enumerations | |
| --- | --- |
| `PgsAuthScope{   PGS_AUTH_SCOPE_EMAIL,   PGS_AUTH_SCOPE_PROFILE,   PGS_AUTH_SCOPE_OPENID }` | enum Represents type-safe constants for OAuth 2.0 authorization scopes. |

## Enumerations

### PgsAuthScope

```
 PgsAuthScope
```

Represents type-safe constants for OAuth 2.0 authorization scopes.

OAuth 2.0 authorization scopes define the permissions your application needs. These scopes specify which data and functionality are accessible via authorization. For example, user email, profile data, or access to certain Google services. The scopes are presented to the user via a consent screen during the authorization process.

| Properties | |
| --- | --- |
| `PGS_AUTH_SCOPE_EMAIL` | Scope for accessing the user's primary Google Account email address.  This scope allows your application to retrieve the email address associated with the user's Google account.  **See also:** <https://developers.google.com/identity/protocols/oauth2/scopes#oauth2> |
| `PGS_AUTH_SCOPE_OPENID` | Scope for accessing the user's OpenID information.  This scope allows your application to authenticate the user via their OpenID and retrieve basic account information.  **See also:** <https://developers.google.com/identity/protocols/oauth2/scopes#oauth2> |
| `PGS_AUTH_SCOPE_PROFILE` | Scope for accessing the user's basic profile information.  This scope allows your application to access personal information, including the user's name, profile picture, and any other information they have made publicly available.  **See also:** <https://developers.google.com/identity/protocols/oauth2/scopes#oauth2> |