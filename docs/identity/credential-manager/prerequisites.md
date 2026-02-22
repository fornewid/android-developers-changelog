---
title: https://developer.android.com/identity/credential-manager/prerequisites
url: https://developer.android.com/identity/credential-manager/prerequisites
source: md.txt
---

# Prerequisites

A primary prerequisite for implementing a seamless sign-in experience with Credential Manager across your app and website is establishing a secure association between them. This is achieved using Digital Asset Links files, which enable credential providers to securely share credentials between your app and website. For example, a website can declare that it shares credentials with an Android app or another website by using a Digital Asset Links file. Using Digital Asset Links lets your users have a seamless sign-in experience and use the same saved credentials across associated apps and websites.
| **Note:** Using Digital Asset Links is required for passkeys because they are often synced across devices and platforms, and strongly recommended for passwords.

### Configure Digital Asset Links between your app and website

To allow credential providers to use passkeys and passwords commonly across your app and website, create a Digital Asset Links file for your app with the following steps:

#### 1. Create the Digital Asset Links JSON file

Create a file named`assetlinks.json`with the following structure:  

    [
        {
        "relation" : [
            "<array_of_permissions_granted_to_app>"
        ],
        "target" : {
            "namespace" : "android_app",
            "package_name" : "<android_application_package_name>",
            "sha256_cert_fingerprints" : [
                "<sha256_certificate_fingerprint_of_signing_key>"
    ]
        }
    }
    ]

- **`relation`**: An array of one or more strings that describe the relationship being declared. To declare that apps and sites share sign-in credentials, specify the following relationships in an array:

  - **`delegate_permission/common.handle_all_urls`**: This relation enables Android App Links, which lets your Android app handle all web URLs for a specific domain.

  - **`delegate_permission/common.get_login_creds`**: This relation enables sharing credentials between your website and your Android app.

- **`target`**: An object that specifies the asset that the declaration applies to.

  - **`target.namespace`** : Set this to`android_app`.
  - **`target.package_name`** : Set this to the package name declared in the app's manifest, for example,`com.example.android`.
- **`sha256_cert_fingerprints`** : The SHA256 fingerprints of your app's signing certificate. To retrieve the SHA256 fingerprint for your app, see[Declare website associations](https://developer.android.com/training/app-links/configure-assetlinks#declare-website).

An example target for an app is as follows:  

    [
      {
        "relation" : [
          "delegate_permission/common.handle_all_urls",
          "delegate_permission/common.get_login_creds"
        ],
        "target" : {
          "namespace" : "android_app",
          "package_name" : "com.example.android",
          "sha256_cert_fingerprints" : [
            SHA_HEX_VALUE
          ]
        }
      }
    ]

| **Note:** To register different app versions, such as debug and release, add multiple entries to the array in the`assetlinks.json`file, each with a distinct package name, corresponding to your app version.

#### 2. Host the Digital Asset Links JSON file

Host the Digital Asset Links file at the following location on the sign-in domain for your website:  

    https://<var translate="no">domain</var>[:<var translate="no">optional_port</var>]/.well-known/assetlinks.json

For example, if your sign-in domain is`signin.example.com`, host the file at:`https://signin.example.com/.well-known/assetlinks.json`.

The MIME type for the Digital Asset Links file must be`JSON`. Make sure that the server sends a`Content-Type: application/json`header in the response, with the HTTP status set to`200`.

#### 3. Allow retrieval of the Digital Asset Links file

Update your host to permit Google to retrieve your Digital Asset Links file. Most websites allow any automated agent to retrieve files in the`/.well-known/`path so that other services can access the metadata in those files.

If you have a`robots.txt`file, allow web crawlers to retrieve`/.well-known/assetlinks.json`by updating the`robots.txt`as follows:  

    User-agent: *
    Allow: /.well-known/

#### 4. Update the app's manifest

In your app's manifest file, add the following lines under`<application>`:  

    <meta-data android:name="asset_statements" android:resource="@string/asset_statements" />

#### 5. Configure Digital Asset Links for passwords

If you are using Credential Manager for passwords, you must complete an additional step to configure digital asset links.

Add an object that specifies the`assetlinks.json`files to load in the manifest file. You must escape any apostrophes and quotation marks you use in the string as shown in the following example:  

    <string name="asset_statements" translatable="false">
    [{
      \"include\": \"https://signin.example.com/.well-known/assetlinks.json\"
    }]
    </string>

The`https://signin.example.com/.well-known/assetlinks.json`link must return an`HTTP 200`response and have a`Content-Type`header of`application/json`. Verification fails if the response has a`301`or`302`HTTP redirect or a non-JSON`Content-Type`.

The following example shows a sample request and the expected response headers:  

    > GET /.well-known/assetlinks.json HTTP/1.1
    > User-Agent: curl/7.35.0
    > Host: signin.example.com

    < HTTP/1.1 200 OK
    < Content-Type: application/json

### Next steps

After adding the necessary dependencies and configuring Digital Asset Links for passkeys, you can use Credential Manager to implement the supported authentication methods: Passkeys and Sign in with Google. To get started, see the following developer guides:

- [**Set up passkeys with Credential Manager**](https://developer.android.com/identity/passkeys): Learn how to implement passkeys, the modern, phishing-resistant method for secure and user-friendly authentication.
- [**Set up Sign in with Google with Credential Manager**](https://developer.android.com/identity/sign-in/credential-manager-siwg): Integrate "Sign in with Google" for streamlined user sign-in with Google Accounts.
- [**Troubleshoot common errors with Credential Manager**](https://developer.android.com/identity/sign-in/credential-manager-troubleshooting-guide): Learn how to resolve common errors with Credential Manager.
- [**Integrate Firebase authentication**](https://firebase.google.com/docs/auth/android/google-signin): Let your users authenticate with Firebase using their Google Accounts.