---
title: https://developer.android.com/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration
url: https://developer.android.com/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# Zoho Achieves 6x Faster Logins with Passkey and Credential Manager Integration

###### 10-min read

![](https://developer.android.com/static/blog/assets/ANDDM_Zoho_Header_6260da2eab_3BTtG.webp) 07 May 2025 [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/Joseph_Lewis_a7854037dd_qbEP3.webp)](https://developer.android.com/blog/authors/joseph-lewis)

##### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)
\&
[Joseph Lewis](https://developer.android.com/blog/authors/joseph-lewis)

As an Android developer, you're constantly looking for ways to enhance security, improve user experience, and streamline development. Zoho, a comprehensive cloud-based software suite focused on security and seamless experiences, achieved significant improvements by adopting passkeys in their [OneAuth](https://play.google.com/store/apps/details?id=com.zoho.accounts.oneauth) Android app.

Since integrating passkeys in 2024, Zoho achieved **login speeds up to 6x faster** than previous methods and a **31% month-over-month (MoM) growth in passkey adoption**.

This case study examines Zoho's adoption of passkeys and Android's [Credential Manager API](https://developer.android.com/training/sign-in/passkeys) to address authentication difficulties. It details the technical implementation process and highlights the impactful results.

## Overcoming authentication challenges

Zoho utilizes a combination of authentication methods to protect user accounts. This included Zoho [OneAuth](https://www.zoho.com/accounts/oneauth/), their own multi-factor authentication (MFA) solution, which supported both password-based and password-less authentication using push notifications, QR codes, and time-based one-time passwords (TOTP). Zoho also supported federated logins, allowing authentication through Security Assertion Markup Language (SAML) and other third-party identity providers.

### Challenges

Zoho, like many organizations, aimed to improve authentication security and user experience while reducing operational burdens. The primary challenges that led to the adoption of passkeys included:

- Security vulnerabilities: Traditional password-based methods left users susceptible to phishing attacks and password breaches.
- User friction: Password fatigue led to forgotten passwords, frustration, and increased reliance on cumbersome recovery processes.
- Operational inefficiencies: Handling password resets and MFA issues generated significant support overhead.
- Scalability concerns: A growing user base demanded a more secure and efficient authentication solution.

### Why the shift to passkeys?

Passkeys were implemented in Zoho's apps to address authentication challenges by offering a password-less approach that significantly improves security and user experience. This solution leverages phishing-resistant authentication, cloud-synchronized credentials for effortless cross-device access, and biometrics (such as a fingerprint or facial recognition), PIN, or pattern for secure logins, thereby reducing the vulnerabilities and inconveniences associated with traditional passwords.

By adopting passkeys with Credential Manager, Zoho cut login times by **up to 6x** , slashed password-related support costs, and saw **strong** user adoption -- **doubling** passkey sign-ins in 4 months with **31% MoM growth** . Zoho users now enjoy **faster, easier logins and phishing-resistant security**.
![ANDDM_Zoho_Quote_fabrice.png](https://developer.android.com/static/blog/assets/ANDDM_Zoho_Quote_fabrice_356f884394_Z1JvEJx.webp)

## Implementation with Credential Manager on Android

So, how did Zoho achieve these results? They used Android's Credential Manager API, the recommended Jetpack library for implementing authentication on Android.

Credential Manager provides a unified API that simplifies handling of the various authentication methods. Instead of juggling different APIs for passwords, passkeys, and federated logins (like Sign in with Google), you use a single interface.

Implementing passkeys at Zoho required both client-side and server-side adjustments. Here's a detailed breakdown of the passkey creation, sign-in, and server-side implementation process.

### Passkey creation

![passkey.png](https://developer.android.com/static/blog/assets/passkey_45c3050ce8_Z1gp6Bb.webp)

To [create a passkey](https://developer.android.com/identity/sign-in/credential-manager#registration-flows), the app first retrieves configuration details from Zoho's server. This process includes a unique verification, such as a fingerprint or facial recognition. This verification data, formatted as a `requestJson` string), is used by the app to build a `CreatePublicKeyCredentialRequest`. The app then calls the `credentialManager.createCredential` method, which prompts the user to authenticate using their device screen lock (biometrics, fingerprint, PIN, etc.).

Upon successful user confirmation, the app receives the new passkey credential data, sends it back to Zoho's server for verification, and the server then stores the passkey information linked to the user's account. Failures or user cancellations during the process are caught and handled by the app.

### Sign-in

The Zoho Android app initiates the [passkey sign-in](https://developer.android.com/identity/sign-in/credential-manager#sign-in) process by requesting sign-in options, including a unique `challenge`, from Zoho's backend server. The app then uses this data to construct a `GetCredentialRequest`, indicating it will authenticate with a passkey. It then invokes the Android `CredentialManager.getCredential()` API with this request. This action triggers a standardized Android system interface, prompting the user to choose their Zoho account (if multiple passkeys exist) and authenticate using their device's configured screen lock (fingerprint, face scan, or PIN). After successful authentication, Credential Manager returns a signed assertion (proof of login) to the Zoho app. The app forwards this assertion to Zoho's server, which verifies the signature against the user's stored public key and validates the challenge, completing the secure sign-in process.

### Server-side implementation

Zoho's transition to supporting passkeys benefited from their backend systems already being FIDO WebAuthn compliant, which streamlined the server-side implementation process. However, specific modifications were still necessary to fully integrate passkey functionality.

The most significant challenge involved adapting the credential storage system. Zoho's existing authentication methods, which primarily used passwords and FIDO security keys for multi-factor authentication, required different storage approaches than passkeys, which are based on cryptographic public keys. To address this, Zoho implemented a new database schema specifically designed to securely store passkey public keys and related data according to WebAuthn protocols. This new system was built alongside a lookup mechanism to validate and retrieve credentials based on user and device information, ensuring backward compatibility with older authentication methods.

Another server-side adjustment involved implementing the ability to handle requests from Android devices. Passkey requests originating from Android apps use a unique origin format (`android:apk-key-hash:example`) that is distinct from standard web origins that use a URI-based format (`https://example.com/app`). The server logic needed to be updated to correctly parse this format, extract the SHA-256 fingerprint hash of the app's signing certificate, and validate it against a pre-registered list. This verification step ensures that authentication requests genuinely originate from Zoho's Android app and protects against phishing attacks.

This code snippet demonstrates how the server checks for the Android-specific origin format and validates the certificate hash:

```
val origin: String = clientData.getString("origin")

if (origin.startsWith("android:apk-key-hash:")) { 
    val originSplit: List<String> = origin.split(":")
    if (originSplit.size > 3) {
               val androidOriginHashDecoded: ByteArray = Base64.getDecoder().decode(originSplit[3])

                if (!androidOriginHashDecoded.contentEquals(oneAuthSha256FingerPrint)) {
            throw IAMException(IAMErrorCode.WEBAUTH003)
        }
    } else {
        // Optional: Handle the case where the origin string is malformed    }
}
```

### Error handling

Zoho implemented robust [error handling mechanisms](https://developer.android.com/identity/sign-in/credential-manager-troubleshooting-guide) to manage both user-facing and developer-facing errors. A common error, `CreateCredentialCancellationException`, appeared when users manually canceled their passkey setup. Zoho tracked the frequency of this error to assess potential UX improvements. Based on Android's [UX recommendations](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys), Zoho took steps to better educate their users about passkeys, ensure users were aware of passkey availability, and promote passkey adoption during subsequent sign-in attempts.

This code example demonstrates Zoho's approach for how they handled their most common passkey creation errors:

```
private fun handleFailure(e: CreateCredentialException) {
    val msg = when (e) {
        is CreateCredentialCancellationException -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_SETUP_CANCELLED", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "The operation was canceled by the user."
        }
        is CreateCredentialInterruptedException -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_SETUP_INTERRUPTED", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "Passkey setup was interrupted. Please try again."
        }
        is CreateCredentialProviderConfigurationException -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_PROVIDER_MISCONFIGURED", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "Credential provider misconfigured. Contact support."
        }
        is CreateCredentialUnknownException -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_SETUP_UNKNOWN_ERROR", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "An unknown error occurred during Passkey setup."
        }
        is CreatePublicKeyCredentialDomException -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_WEB_AUTHN_ERROR", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "Passkey creation failed: ${e.domError}"
        }
        else -> {
            Analytics.addAnalyticsEvent(eventProtocol: "PASSKEY_SETUP_FAILED", GROUP_NAME)
            Analytics.addNonFatalException(e)
            "An unexpected error occurred. Please try again."
        }
    }
}
```

### Testing passkeys in intranet environments

Zoho faced an initial challenge in testing passkeys within a closed intranet environment. The Google Password Manager [verification process](https://developer.android.com/identity/sign-in/credential-manager#add-support-dal) for passkeys requires public domain access to validate the relying party (RP) domain. However, Zoho's internal testing environment lacked this public Internet access, causing the verification process to fail and hindering successful passkey authentication testing. To overcome this, Zoho created a publicly accessible test environment, which included hosting a temporary server with an [asset link file](https://developer.android.com/identity/sign-in/credential-manager#add-support-dal) and domain validation.

This example from the `assetlinks.json` file used in Zoho's public test environment demonstrates how to associate the relying party domain with the specified Android app for passkey validation.

```
[
    {
        "relation": [
            "delegate_permission/common.handle_all_urls",
            "delegate_permission/common.get_login_creds"
        ],
        "target": {
            "namespace": "android_app",
            "package_name": "com.zoho.accounts.oneauth",
            "sha256_cert_fingerprints": [
                "SHA_HEX_VALUE" 
            ]
        }
    }
]
```

### Integrate with an existing FIDO server

Android's passkey system utilizes the modern FIDO2 WebAuthn standard. This standard requires requests in a specific JSON format, which helps maintain consistency between native applications and web platforms. To enable Android passkey support, Zoho did minor compatibility and structural changes to correctly generate and process requests that adhere to the required FIDO2 JSON structure.

This server update involved several specific technical adjustments:

1. **Encoding conversion:** The server converts the Base64 URL encoding (commonly used in WebAuthn for fields like credential IDs) to standard Base64 encoding before it stores the relevant data. The snippet below shows how a rawId might be encoded to standard Base64:

```
// Convert rawId bytes to a standard Base64 encoded string for storage
val base64RawId: String = Base64.getEncoder().encodeToString(rawId.toByteArray())
```

2. **Transport list format:** To ensure consistent data processing, the server logic handles lists of transport mechanisms (such as USB, NFC, and Bluetooth, which specify how the authenticator communicated) as JSON arrays.

3. **Client data alignment:** The Zoho team adjusted how the server encodes and decodes the clientDataJson field. This ensures the data structure aligns precisely with the expectations of Zoho's existing internal APIs. The example below illustrates part of the conversion logic applied to client data before the server processes it:

```
private fun convertForServer(type: String): String {
    val clientDataBytes = BaseEncoding.base64().decode(type)
    val clientDataJson = JSONObject(String(clientDataBytes, StandardCharsets.UTF_8))
    val clientJson = JSONObject()
    val challengeFromJson = clientDataJson.getString("challenge")
    // 'challenge' is a technical identifier/token, not localizable text.
    clientJson.put("challenge", BaseEncoding.base64Url()
        .encode(challengeFromJson.toByteArray(StandardCharsets.UTF_8))) 

    clientJson.put("origin", clientDataJson.getString("origin"))
    clientJson.put("type", clientDataJson.getString("type"))
    clientJson.put("androidPackageName", clientDataJson.getString("androidPackageName"))
    return BaseEncoding.base64().encode(clientJson.toString().toByteArray())
}
```

### User guidance and authentication preferences

A central part of Zoho's passkey strategy involved encouraging user adoption while providing flexibility to align with different organizational requirements. This was achieved through careful UI design and policy controls.

Zoho recognized that organizations have varying security needs. To accommodate this, Zoho implemented:

- **Admin enforcement:** Through the [Zoho Directory](https://www.zoho.com/directory/) admin panel, administrators can designate passkeys as the mandatory, default authentication method for their entire organization. When this policy is enabled, employees are required to set up a passkey upon their next login and use it going forward.
- **User choice:** If an organization does not enforce a specific policy, individual users maintain control. They can choose their preferred authentication method during login, selecting from passkeys or other configured options via their authentication settings.

To make adopting passkeys appealing and straightforward for end-users, Zoho implemented:

- **Easy setup:** Zoho integrated passkey setup directly into the Zoho OneAuth mobile app (available for both [Android](https://play.google.com/store/apps/details?id=com.zoho.accounts.oneauth) and [iOS](https://apps.apple.com/in/app/authenticator-app-oneauth/id1142928979)). Users can conveniently configure their passkeys within the app at any time, smoothing the transition.
- **Consistent access:** Passkey support was implemented across key user touchpoints, ensuring users can register and authenticate using passkeys via:
- The Zoho OneAuth mobile app (Android \& iOS);
- Their Zoho web [accounts](https://accounts.zoho.com/home#multiTFA/pfamodes) page.

This method ensured that the process of setting up and using passkeys was accessible and integrated into the platforms they already use, regardless of whether it was mandated by an admin or chosen by the user. You can learn more about how to create smooth user flows for passkey authentication by exploring our comprehensive [passkeys user experience guide](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys).

## Impact on developer velocity and integration efficiency

Credential Manager, as a unified API, also helped improve developer productivity compared to older sign-in flows. It reduced the complexity of handling multiple authentication methods and APIs separately, leading to faster integration, from months to weeks, and fewer implementation errors. This collectively streamlined the sign-in process and improved overall reliability.

By implementing passkeys with Credential Manager, Zoho achieved significant, measurable improvements across the board:

- **Dramatic speed improvements**
  - **2x faster** login compared to traditional password authentication.
  - **4x faster** login compared to username or mobile number with email or SMS OTP authentication.
  - **6x faster** login compared to username, password, and SMS or authenticator OTP authentication.
- **Reduced support costs**
  - **Reduced password-related support requests**, especially for forgotten passwords.
  - **Lower costs** associated with SMS-based 2FA, as existing users can onboard directly with passkeys.
- **Strong user adoption \& enhanced security:**
  - **Passkey sign-ins doubled** in just 4 months, showing high user acceptance.
  - Users migrating to passkeys are **fully protected** from common phishing and password breach threats.
  - With **31% MoM adoption growth**, more users are benefiting daily from enhanced security against vulnerabilities like phishing and SIM swaps.

## Recommendations and best practices

To successfully implement passkeys on Android, developers should consider the following best practices:

- **Leverage Android's Credential Manager API:**
  - Credential Manager simplifies credential retrieval, reducing developer effort and ensuring a unified authentication experience.
  - Handles passwords, passkeys, and federated login flows in a single interface.
- **Ensure data encoding consistency while migrating from other FIDO authentication solutions:**
  - Make sure you handle consistent formatting for all inputs/outputs while migrating from other FIDO authentication solutions such as FIDO security keys.
- **Optimize error handling and logging:**
  - Implement robust error handling for a seamless user experience.
  - Provide localized error messages and use detailed logs to debug and resolve unexpected failures.
- **Educate users on passkey recovery options:**
  - Prevent lockout scenarios by proactively guiding users on recovery options.
- **Monitor adoption metrics and user feedback:**
  - Track user engagement, passkey adoption rates, and login success rates to keep optimizing user experience.
  - Conduct A/B testing on different authentication flows to improve conversion and retention.

Passkeys, combined with the [Android Credential Manager API](https://developer.android.com/training/sign-in/passkeys), offer a powerful, unified authentication solution that enhances security while simplifying user experience. Passkeys significantly reduce phishing risks, credential theft, and unauthorized access. We encourage developers to try out the experience in their app and bring the most secure authentication to their users.

## Get started with passkeys and Credential Manager

Get hands on with passkeys and Credential Manager on Android using our [public sample code](https://github.com/android/identity-samples/tree/credman-compose).

If you have any questions or issues, you can share with us through the [Android Credentials issues tracker](https://issuetracker.google.com/issues?q=1301097).

###### Written by:

-

  ## [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/niharika-arora) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)
-

  ## [Joseph Lewis](https://developer.android.com/blog/authors/joseph-lewis)

  ###### Staff Technical Writing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/joseph-lewis) ![](https://developer.android.com/static/blog/assets/Joseph_Lewis_a7854037dd_qbEP3.webp) ![](https://developer.android.com/static/blog/assets/Joseph_Lewis_a7854037dd_qbEP3.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora) 18 Nov 2025 18 Nov 2025 ![](https://developer.android.com/static/blog/assets/uber_Credentials_12e7f1f5c4_Zjh724.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How Uber is reducing manual logins by 4 million per year with the Restore Credentials API](https://developer.android.com/blog/posts/how-uber-is-reducing-manual-logins-by-4-million-per-year-with-the-restore-credentials-api)

  [arrow_forward](https://developer.android.com/blog/posts/how-uber-is-reducing-manual-logins-by-4-million-per-year-with-the-restore-credentials-api) Uber leveraged the Android Restore Credentials API to streamline new device sign-in, projecting a reduction of 4 million manual logins per year and increasing user retention.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora) 21 Nov 2024 21 Nov 2024 ![](https://developer.android.com/static/blog/assets/x_Passkeys_45bf854440_G2vTP.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [X improved login success rate by 2x after adopting passkeys](https://developer.android.com/blog/posts/x-improved-login-success-rate-after-adopting-passkeys)

  [arrow_forward](https://developer.android.com/blog/posts/x-improved-login-success-rate-after-adopting-passkeys) From breaking news and entertainment to sports and politics, X is a social media app that aims to help nearly 500 million users worldwide get the full story with all the live commentary.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow_forward](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)