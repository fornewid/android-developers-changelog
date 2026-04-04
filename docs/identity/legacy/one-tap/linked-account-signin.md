---
title: https://developer.android.com/identity/legacy/one-tap/linked-account-signin
url: https://developer.android.com/identity/legacy/one-tap/linked-account-signin
source: md.txt
---

| **Caution:** One Tap for Android is deprecated. To ensure the continued security and usability of your app, [migrate to
| Credential Manager](https://developer.android.com/identity/sign-in/credential-manager). Credential Manager supports passkey, password, and federated identity authentication (such as Sign-in with Google), stronger security, and a more consistent user experience.

[Google Account Linking](https://developers.google.com/identity/account-linking) enables Google Account holders to quickly, seamlessly and safely connect to your services and share data with Google.

Linked Account Sign-In enables [One Tap Sign-In With Google](https://developers.google.com/identity/one-tap/android/legacy-get-saved-credentials) for users that already have their Google Account linked to your service. This improves the experience for users as they can sign in with one click, without re-entering their username and password. It also reduces the chances of users creating duplicate accounts on your service.
| **Note:** Linked Account Sign-In is only available on Android.

## Requirements

To implement Linked Account Sign-In, you must fulfill the following requirements:

- You have a [Google Account OAuth Linking](https://developers.google.com/identity/account-linking/oauth-linking?oauth=code) implementation that supports the OAuth 2.0 authorization code flow. Your OAuth implementation must include the following endpoints:
  - [authorization endpoint](https://developers.google.com/identity/account-linking/oauth-linking?oauth=code#handle_authorization_requests) to handle authorization requests.
  - [token endpoint](https://developers.google.com/identity/account-linking/oauth-linking?oauth=code#handle_token_exchange_requests) to handle request for access and refresh tokens.
  - [userinfo endpoint](https://developers.google.com/identity/account-linking/oauth-linking?oauth=code#handle_userinfo_requests) to retrieve basic account information about the linked user which is displayed to the user during the Linked Account Sign-In process.
- You have an Android app.

## How it works

Prerequisite : The user has previously linked their Google Account with their account on your service.

1. You opt-in to show linked accounts during the One Tap Sign-In flow.
2. The user is shown a One Tap Sign-In prompt with an option to sign in to your service with their linked account.
3. If the user chooses to continue with the linked account, Google sends a request to your token endpoint to save an authorization code. The request contains the user's access token issued by your service and a Google authorization code.
4. You exchange the Google authorization code for a Google ID token which contains information about the user's Google account.
5. Your app also receives an ID token when the flow finishes and you match this against the user identifier in the ID token that was received by your server in order to sign the user into your app.

| **Note:** Steps 3 \& 4 are done the first time the user attempts to sign in with a linked account. The steps are skipped for subsequent sign-ins with the same account.
![Linked Account Sign-In.](https://developer.android.com/static/identity/legacy/one-tap/images/linked-account-signin.png) **Figure 1.** Linked Account Sign-In Flow. If the user has multiple signed-in accounts on their device, the user may see an account chooser and is only taken to the Linked Account Sign-In view if they select a linked account.

## Implement Linked Account Sign-In in your Android app

To support Linked Account Sign-In on your Android app, follow the instructions in the [Android implementation guide](https://developer.android.com/identity/legacy/one-tap/linked-account-signin-client).

## Handle authorization code requests from Google

| **Note:** You must have [registered your OAuth2 endpoints](https://developers.google.com/identity/account-linking/registration) with Google before proceeding with the below steps.

Google makes a POST request to your token endpoint to save an authorization code which you exchange for the user's ID token. The request contains the user's access token and a Google issued OAuth2 authorization code.

Before saving the authorization code, you must verify the access token was granted by you to Google, identified by the `client_id`.

### HTTP Request

#### Sample request

    POST /token HTTP/1.1
    Host: server.example.com
    Content-Type: application/x-www-form-urlencoded

    code=GOOGLE_AUTHORIZATION_CODE
    &grant_type=urn:ietf:params:oauth:grant-type:reciprocal
    &client_id=CLIENT_ID
    &client_secret=CLIENT_SECRET
    &access_token=ACCESS_TOKEN

Your token exchange endpoint must be able to handle the following request parameters:
| **Note:** This requires an update to your token endpoint. In the [Google Account Linking OAuth token request](https://developers.google.com/identity/account-linking/oauth-linking?oauth=code#handle_token_exchange_requests), Google calls your token endpoint to exchange an authorization code provided by you for an access or refresh token. In the Linked Account Sign-In token request, Google calls your token endpoint to save an authorization code.

| Token endpoint parameters ||
|---|---|
| `code` | **Required** Google OAuth2 authorization code |
| `client_id` | **Required** Client ID that you issued to Google |
| `client_secret` | **Required** Client secret that you issued to Google |
| `access_token` | **Required** Access token that you issued to Google. You will use this to get the context of the user |
| `grant_type` | **Required** Value MUST be set to `urn:ietf:params:oauth:grant-type:reciprocal` |

Your token exchange endpoint should respond to the POST request by doing the following:

- Verify the `access_token` was granted to Google identified by the `client_id`.
- Respond with either an HTTP 200 (OK) response if the request is valid and the auth code is successfully exchanged for a Google ID token, or an HTTP error code if the request is invalid.

### HTTP Response

#### Success

Return HTTP status code 200 OK

##### Sample success response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache
    {}

#### Errors

In the event of an invalid HTTP request, respond with one of the following HTTP error codes:

| HTTP Status Code | Body | Description |
|---|---|---|
| 400 | `{"error": "invalid_request"}` | The request is missing a parameter so the server can't proceed with the request. This may also be returned if the request includes an unsupported parameter or repeats a parameter |
| 401 | `{"error": "invalid_request"}` | Client authentication failed, such as if the request contains an invalid client ID or secret |
| 401 | `{"error": "invalid_token"}` *Include "WWW-Authentication: Bearer" auth challenge in the response header* | Partner access token is invalid. |
| 403 | `{"error": "insufficient_permission"}` *Include "WWW-Authentication: Bearer" auth challenge in the response header* | Partner access token doesn't contain the necessary scope(s) to perform the Reciprocal OAuth |
| 500 | `{"error": "internal_error"}` | Server error |

The error response should contain the following fields :

| Error response fields ||
|---|---|
| `error` | **Required** Error string |
| `error_description` | Human readable description of the error |
| `error_uri` | URI that provides more details about the error |

##### Sample error 400 response

    HTTP/1.1 400 Bad Request
    Content-Type: application/json;charset=UTF-8
    Cache-Control: no-store
    Pragma: no-cache

    {
      "error": "invalid_request",
      "error_description": "Request was missing the 'access_token' parameter."
    }

## Exchange authorization code for ID token

You will need to exchange the authorization code you received for a Google ID token which contains information about the user's Google account.

To exchange an authorization code for a Google ID token, call the `https://oauth2.googleapis.com/token` endpoint and set the following parameters:

| Request fields ||
|---|---|
| `client_id` | **Required** The client ID obtained from the API Console [Credentials page](https://console.developers.google.com/apis/credentials). This will typically be the credential with the name *New Actions on Google App* |
| `client_secret` | **Required** The client secret obtained from the API Console [Credentials page](https://console.developers.google.com/apis/credentials) |
| `code` | **Required** The authorization code sent in the initial request |
| `grant_type` | **Required** [As defined in the OAuth 2.0 specification](https://tools.ietf.org/html/rfc6749#section-4.1.3), this field's value must be set to `authorization_code`. |

##### Sample request

    POST /oauth2/v4/token HTTP/1.1
    Host: www.googleapis.com
    Content-Type: application/x-www-form-urlencoded

    code=GOOGLE_AUTHORIZATION_CODE
    &grant_type=authorization_code
    &client_id=GOOGLE_CLIENT_ID
    &client_secret=GOOGLE_CLIENT_SECRET

Google responds to this request by returning a JSON object that contains a short-lived access token and a refresh token.

The response contains the following fields:

| Response fields ||
|---|---|
| `access_token` | Google-issued access token that your application sends to authorize a Google API request |
| `id_token` | The ID token contains the user's Google Account information. The [Validate Response section](https://developer.android.com/identity/legacy/one-tap/linked-account-signin#validate_id_token_response) contains details on how to decode and validate the ID token response |
| `expires_in` | The remaining lifetime of the access token in seconds |
| `refresh_token` | A token that you can use to obtain a new access token. Refresh tokens are valid until the user revokes access |
| `scope` | This field's value is always set to openid for the Linked Account Sign-In use case |
| `token_type` | The type of token returned. At this time, this field's value is always set to `Bearer` |

##### Sample response

    HTTP/1.1 200 OK
    Content-type: application/json; charset=utf-8

    {
      "access_token": "Google-access-token",
      "id_token": "Google-ID-token",
      "expires_in": 3599,
      "token_type": "Bearer",
      "scope": "openid",
      "refresh_token": "Google-refresh-token"
    }


    POST /oauth2/v4/token HTTP/1.1
    Host: www.googleapis.com
    Content-Type: application/x-www-form-urlencoded

    code=Google authorization code
    &grant_type=authorization_code
    &client_id=Google client id
    &client_secret=Google client secret

## Validate the ID Token response