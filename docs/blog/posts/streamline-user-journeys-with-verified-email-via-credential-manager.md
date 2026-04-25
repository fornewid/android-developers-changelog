---
title: https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager
url: https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Streamline User Journeys with Verified Email via Credential Manager

###### 3-min read

![](https://developer.android.com/static/blog/assets/Streamline_user_animation_V02_Strapi_abd12985d7_SvAX9.webp) 22 Apr 2026 [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/jean-pierre-pralle)

##### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)
\&
[Jean-Pierre Pralle](https://developer.android.com/blog/authors/jean-pierre-pralle)

In the modern digital landscape, the first encounter a user has with an app is often the most critical. Yet, for decades, this initial interaction has been hindered by the friction of traditional verification methods. Today, we're excited to announce a [new verified email credential issued by Google](https://developer.android.com/identity/digital-credentials/email-verification), which developers can now retrieve directly from Android's Credential Manager Digital Credential API.

### **The Problem: Authentication Friction in the Modern Era**

The "current era" of authentication is defined by a trade-off between security and convenience. To ensure that a user owns the email address they provide, you typically rely on One-Time Passwords (OTPs) or "magic links" sent by email or SMS.

While effective, these traditional steps introduce significant hurdles:

- **Context switching**: Users must leave the app, open their inbox or messaging app, find the code, and return, a process where many potential users simply drop off.
- **Delivery issues**: While Emails are free, they can be delayed or diverted to spam folders..
- **Onboarding friction**: Every extra second spent in the "verification loop" is a second where a user might lose interest, directly impacting conversion rates.

### **The Solution: Seamless, Verified Email**

Google now issues a cryptographically verified email credential directly to Android devices. This verified email credential is delivered through the [Credential Manager API](https://developer.android.com/identity/credential-manager), which is Android's implementation of the [W3C's Digital Credential API](https://www.w3.org/TR/digital-credentials/) standard.

For users, this completely removes the need to manually verify their email through external channels. For developers, the API securely delivers these verified user claims for any scenario whether you are building an account creation flow, a recovery process, or a high-risk step-up authentication.

While this specific verified email address is sourced securely from the user's Google Account on their device, the underlying Digital Credentials API is issuer-agnostic. This fosters an open ecosystem, allowing any holder of a digital credential with an email claim to offer that verification to your app.

### **User Experience**

The beauty of this API lies in its simplicity for the end user. Instead of hunting for OTP codes, the experience is integrated directly into the Android OS:

1. **Initiation:** The process begins when a user focuses on an email input field or taps a "Sign up" or "Recover account" button. You can also initiate the process on page load.
2. **Transparency**: A native Android bottom sheet appears, clearly detailing exactly what data is being requested (for example, user's verified email address).
3. **One-tap consent**: The user simply taps "Agree and continue" to share the data.
4. **Immediate progress** : Once consent is given, the app receives the data instantly. For sign-up or account recovery flows, you can then seamlessly transition the user into passkey creation, ensuring:
   1. Users do not have to enter any user information manually, as compared to the traditional username/password registration.
   2. Their next login is even faster and more secure.

### **Use case 1. Sign up**

Accelerate onboarding by fetching a verified email the moment the user taps "Sign up". We strongly recommend you pair the verified email retrieval with passkey creation, also part of the Credential Manager API:
![UseCase1.png](https://developer.android.com/static/blog/assets/Use_Case1_01f7f551f9_Z1z8zha.webp)

*Note: You can also fetch other unverified fields such as a user's given name, family name, name, profile picture and the hosted domain connected with the verified email.*

### **Use case 2. Account recovery**

Eliminate the frustration of users hunting for recovery codes in their spam folders by allowing them to recover their account using the verified email securely stored on their device:
![UseCase2.png](https://developer.android.com/static/blog/assets/Use_Case2_65aec97666_2gaag0.webp)

### **Use case 3. Re-authentication for sensitive actions**

Protect sensitive user actions, such as changing settings or updating profile details, by requiring a quick re-authentication step. Instead of an OTP, you can provide a low-friction verification using the device's verified email:
![UseCase3.png](https://developer.android.com/static/blog/assets/Use_Case3_ea0ca9b117_1NwCFc.webp)

### **Important Considerations**

As you design your authentication architecture around the Digital Credentials API, keep the following details in mind:

- **Account support**: For the specific email credential issued by Google, only regular consumer Google Accounts are supported (Workspace and supervised accounts are currently not supported). Keep in mind that the Credential Manager API itself is issuer-agnostic, meaning other identity providers can issue credentials with their own account support policies.
- **Other user data:** Beyond email, you can request the user's given name, family name, full name, and profile picture. However, note that only the email is verified by Google.
- **Auto verify your @gmail accounts:** The API provides verified emails for all consumer Google Accounts. We recommend auto-verifying @gmail.com users and routing custom domains to your existing verification flow - for example, an OTP flow. This ensures you maintain long-term access for external domains not directly managed by Google.
- **Complementary to Sign in with Google** : While both the new verified email credential \& Sign in with Google API provides a verified email, the choice depends on the intended user experience:
  - **Use Sign in with Google** when your users want to create a federated login session.
  - **Use Verified Email** when your users want to sign in traditionally with a username/password or passkey but want to auto-verify the email address without the manual chore of an OTP.

### **Conclusion and Next steps**

By integrating [the new verified email via Credential Manager API](https://developer.android.com/identity/digital-credentials/email-verification), you can drastically reduce onboarding friction and provide users with a more streamlined, secure authentication journey. This represents a shift toward a future where "verification" is no longer a manual chore for the user, but a seamless, integrated part of the native mobile experience.

Ready to see how this fits into your own app? To get started, update your project to the latest Credential Manager API and explore our [Integration Guide](https://developer.android.com/identity/digital-credentials/email-verification). We encourage you to explore how this streamlined verification can simplify your critical user journeys from optimizing account creation, to enhancing re-authentication flows.

###### Written by:

-

  ## [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/niharika-arora) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)
-

  ## [Jean-Pierre Pralle](https://developer.android.com/blog/authors/jean-pierre-pralle)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/jean-pierre-pralle) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/Vinisha_Athwani_e54ba64bd3_2x1elG.webp)](https://developer.android.com/blog/authors/vinisha-athwani) 04 Sep 2025 04 Sep 2025 ![](https://developer.android.com/static/blog/assets/passkeys_Credential_27ba66338c_ZzmQtB.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Best practices for migrating users to passkeys with Credential Manager](https://developer.android.com/blog/posts/best-practices-for-migrating-users-to-passkeys-with-credential-manager)

  [arrow_forward](https://developer.android.com/blog/posts/best-practices-for-migrating-users-to-passkeys-with-credential-manager) For Android developers, the Credential Manager API helps you guide your users towards using passkeys while ensuring continued support for traditional sign-in mechanisms, such as passwords.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Vinisha Athwani](https://developer.android.com/blog/authors/vinisha-athwani) •
  6 min read

- [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Android CLI and skills: Build Android apps 3x faster using any agent](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent) Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando), [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)