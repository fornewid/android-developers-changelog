---
title: https://developer.android.com/identity/legacy/gsi/offline-access
url: https://developer.android.com/identity/legacy/gsi/offline-access
source: md.txt
---

| **Warning:**
|
| **The Google Sign-In for Android API is outdated and no longer supported.**
| To ensure the continued security and usability of your app, [migrate your Sign in with
| Google implementation to Credential Manager](https://developer.android.com/identity/sign-in/credential-manager-siwg) today. Credential Manager
| supports passkey, password, and federated identity authentication (such as
| Sign-in with Google), stronger security, and a more consistent user
| experience.
|
| **For Wear developers:** Credential Manager is supported in Wear OS
| 5.1 and later on selected watches. Developers actively supporting Wear OS 3, 4
| and 5.0 devices with Sign in with Google should continue using Google Sign-in
| for Android for your Wear applications. Sign in with Google support will be
| available on Credential Manager APIs for these versions of WearOS at a later
| date.

With the earlier [Add Sign-In](https://developer.android.com/identity/legacy/gsi/legacy-sign-in#add_the_google_sign-in_button_to_your_app)
procedure, your app authenticates the user on the client side only; in that case,
you can access the Google APIs only while the user is actively using your app.
If you want your servers to be able to make Google API calls on behalf of
users---possibly while they are offline---your server requires an access
token.

## Before you begin

- Configure a project in Android Studio
- [Add a Google Sign-In button to your app](https://developer.android.com/identity/legacy/gsi/legacy-sign-in)
- Create an OAuth 2.0 web application client ID for your backend server. This client ID is different from your app's client ID. You can find or create a client ID for your server in the [Google API Console](https://console.cloud.google.com/apis/credentials).

## Enable server-side API access for your app

1. When you [configure Google Sign-In](https://developer.android.com/identity/legacy/gsi/legacy-sign-in#configure_google_sign-in_and_the_googlesigninclient_object),
   build the `GoogleSignInOptions` object with the [`requestServerAuthCode`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInOptions.Builder.html#requestServerAuthCode(java.lang.String))
   method and specify the scopes that your app's backend needs to access with
   the \[`requestScopes`\]\[55\]
   method.

   Pass your server's client ID to the `requestServerAuthCode` method.

   ```scilab
   // Configure sign-in to request offline access to the user's ID, basic
   // profile, and Google Drive. The first time you request a code you will
   // be able to exchange it for an access token and refresh token, which
   // you should store. In subsequent calls, the code will only result in
   // an access token. By asking for profile access (through
   // DEFAULT_SIGN_IN) you will also get an ID Token as a result of the
   // code exchange.
   String serverClientId = getString(R.string.server_client_id);
   GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
           .requestScopes(new Scope(Scopes.DRIVE_APPFOLDER))
           .requestServerAuthCode(serverClientId)
           .requestEmail()
           .build();
   ```
2. After the user [successfully signs in](https://developer.android.com/identity/legacy/gsi/legacy-sign-in#start_the_sign-in_flow),
   get an auth code for the user with [`getServerAuthCode`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInAccount.html#getServerAuthCode()):

   ```text
   Task<GoogleSignInAccount> task = GoogleSignIn.getSignedInAccountFromIntent(data);
   try {
       GoogleSignInAccount account = task.getResult(ApiException.class);
       String authCode = account.getServerAuthCode();

       // Show signed-un UI
       updateUI(account);

       // TODO(developer): send code to server and exchange for access/refresh/ID tokens
   } catch (ApiException e) {
       Log.w(TAG, "Sign-in failed", e);
       updateUI(null);
   }
   ```
3. Send the auth code to your app's backend using HTTPS POST:

       HttpPost httpPost = new HttpPost("https://yourbackend.example.com/authcode");

       try {
           List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(1);
           nameValuePairs.add(new BasicNameValuePair("authCode", authCode));
           httpPost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

           HttpResponse response = httpClient.execute(httpPost);
           int statusCode = response.getStatusLine().getStatusCode();
           final String responseBody = EntityUtils.toString(response.getEntity());
       } catch (ClientProtocolException e) {
           Log.e(TAG, "Error sending auth code to backend.", e);
       } catch (IOException e) {
           Log.e(TAG, "Error sending auth code to backend.", e);
       }

4. On your app's backend server, exchange the auth code for access and refresh
   tokens. Use the access token to call Google APIs on behalf of the user and,
   optionally, store the refresh token to acquire a new access token when the
   access token expires.

   If you requested profile access, you also get an ID token that contains
   basic profile information for the user.

   For example:

   ##### Java

   ```java
   // (Receive authCode via HTTPS POST)

   if (request.getHeader("X-Requested-With") == null) {
   // Without the `X-Requested-With` header, this request could be forged. Aborts.
   }

   // Set path to the Web application client_secret_*.json file you downloaded from the
   // Google API Console: https://console.cloud.google.com/apis/credentials
   // You can also find your Web application client ID and client secret from the
   // console and specify them directly when you create the GoogleAuthorizationCodeTokenRequest
   // object.
   String CLIENT_SECRET_FILE = "/path/to/client_secret.json";

   // Exchange auth code for access token
   GoogleClientSecrets clientSecrets =
       GoogleClientSecrets.load(
           JacksonFactory.getDefaultInstance(), new FileReader(CLIENT_SECRET_FILE));
   GoogleTokenResponse tokenResponse =
           new GoogleAuthorizationCodeTokenRequest(
               new NetHttpTransport(),
               JacksonFactory.getDefaultInstance(),
               "https://oauth2.googleapis.com/token",
               clientSecrets.getDetails().getClientId(),
               clientSecrets.getDetails().getClientSecret(),
               authCode,
               REDIRECT_URI)  // Specify the same redirect URI that you use with your web
                               // app. If you don't have a web version of your app, you can
                               // specify an empty string.
               .execute();

   String accessToken = tokenResponse.getAccessToken();

   // Use access token to call API
   GoogleCredential credential = new GoogleCredential().setAccessToken(accessToken);
   Drive drive =
       new Drive.Builder(new NetHttpTransport(), JacksonFactory.getDefaultInstance(), credential)
           .setApplicationName("Auth Code Exchange Demo")
           .build();
   File file = drive.files().get("appfolder").execute();

   // Get profile info from ID token
   GoogleIdToken idToken = tokenResponse.parseIdToken();
   GoogleIdToken.Payload payload = idToken.getPayload();
   String userId = payload.getSubject();  // Use this value as a key to identify a user.
   String email = payload.getEmail();
   boolean emailVerified = Boolean.valueOf(payload.getEmailVerified());
   String name = (String) payload.get("name");
   String pictureUrl = (String) payload.get("picture");
   String locale = (String) payload.get("locale");
   String familyName = (String) payload.get("family_name");
   String givenName = (String) payload.get("given_name");
   ```

   ##### Python

   ```python
   from apiclient import discovery
   import httplib2
   from oauth2client import client

   # (Receive auth_code by HTTPS POST)

   # If this request does not have `X-Requested-With` header, this could be a CSRF
   if not request.headers.get('X-Requested-With'):
       abort(403)

   # Set path to the Web application client_secret_*.json file you downloaded from the
   # Google API Console: https://console.cloud.google.com/apis/credentials
   CLIENT_SECRET_FILE = '/path/to/client_secret.json'

   # Exchange auth code for access token, refresh token, and ID token
   credentials = client.credentials_from_clientsecrets_and_code(
       CLIENT_SECRET_FILE,
       ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
       auth_code)

   # Call Google API
   http_auth = credentials.authorize(httplib2.Http())
   drive_service = discovery.build('drive', 'v3', http=http_auth)
   appfolder = drive_service.files().get(fileId='appfolder').execute()

   # Get profile info from ID token
   userid = credentials.id_token['sub']
   email = credentials.id_token['email']
   ```

\[55\]: https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInOptions.Builder.html#requestScopes(com.google.android.gms.common.api.Scope, com.google.android.gms.common.api.Scope...)