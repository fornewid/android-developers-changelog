---
title: Best practices for migrating users to passkeys with Credential Manager  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/best-practices-for-migrating-users-to-passkeys-with-credential-manager
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [How-tos](/blog/categories/how-tos)

# Best practices for migrating users to passkeys with Credential Manager

###### 6-min read

![](/static/blog/assets/passkeys_Credential_27ba66338c_ZzmQtB.webp)

04

Sep
2025

[![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)](/blog/authors/niharika-arora)[![](/static/blog/assets/Vinisha_Athwani_e54ba64bd3_2x1elG.webp)](/blog/authors/vinisha-athwani)

##### [Niharika Arora](/blog/authors/niharika-arora) & [Vinisha Athwani](/blog/authors/vinisha-athwani)

In a world where digital security is becoming increasingly critical, passwords have become a notorious weak link – they're cumbersome, often insecure, and a source of frustration for users and developers. But there's good news: [passkeys](https://fidoalliance.org/passkeys/) are gaining popularity as the most user-friendly, phishing-resistant, and secure authentication mechanism available. For Android developers, the [Credential Manager API](/identity/sign-in/credential-manager) helps you guide your users towards using passkeys while ensuring continued support for traditional sign-in mechanisms, such as passwords.

In this blog, we discuss some of the best practices you should follow while encouraging users to transition to passkeys.

## Understand authentication with passkeys

Before diving into the recommendations for encouraging the transition to passkeys, here’s an overview of the fundamentals of authentication with passkeys:

* [**Passkeys**](https://fidoalliance.org/passkeys/)**:** These are cryptographic credentials that replace passwords. Passkeys are associated with device unlocking mechanisms, and are the recommended method of authentication for apps and sites.
* [**Credential Manager**](/training/sign-in/passkeys)**:** A Jetpack API that provides a unified API interface for interacting with different types of authentication, including passkeys, passwords, and federated sign-in mechanisms like Sign in with Google.

## How do passkeys help your users?

There are several tangible benefits that users experience in apps that allow them to use passkeys to sign in. The highlights of using passkey for users are as follows:

* **Improved sign-in experience:** Users get the same UI whether they use passwords, passkeys or federated sign-in mechanisms like Sign in with Google.
* **Reduced sign-in time:** Instead of typing out passwords, users use their phone unlock mechanisms, such as biometrics, resulting in a smooth sign-in experience.
* **Improved security:** Passkeys use public-key cryptography so that data breaches of service providers don't result in a compromise of passkey-protected accounts, and are based on industry standard APIs and protocols to ensure they are not subject to phishing attacks. (Read more about syncing and security [here](https://security.googleblog.com/2022/10/SecurityofPasskeysintheGooglePasswordManager.html)).
* **Unified experience across devices:** With the ability to sync passkeys across devices, users benefit from simplified authentication regardless of the device they’re using.
* **No friction due to forgotten passwords!**

Underscoring the improved experience with passkeys, we heard from several prominent apps. **X** observed that login rates improved [2x after adding passkeys to their authentication flows](https://android-developers.googleblog.com/2024/11/x-improved-login-success-rate-after-adopting-passkeys.html). **KAYAK**, a travel search engine, observed that the average time it takes their users to sign up and sign in [reduced by 50%](https://developers.googleblog.com/en/how-kayak-reduced-sign-in-time-by-50-and-improved-security-with-passkeys/) after they incorporated passkeys into their authentication flows. **Zoho**, a comprehensive cloud-based software suite focused on security and seamless experiences, [achieved 6x faster logins by adopting passkeys](https://android-developers.googleblog.com/2025/05/zoho-achieves-faster-logins-passkey-credential-manager-integration.html) in their OneAuth Android app.

## What’s in it for you?

When you migrate your app to use passkeys, you’ll be leveraging the Credential Manager API which is the **recommended** standard for identity and authentication on Android.

Apart from passkeys, the Credential Manager API supports traditional sign-in mechanisms, simplifying the development and maintenance of your authentication flows!

For all of these sign-in mechanisms, Credential Manager offers an integrated bottom-sheet UI, saving you development efforts while offering users a consistent experience.

## When should you prompt users to use passkeys?

Now that we’ve established the benefits of passkeys, let’s discuss how you should encourage your users to migrate to passkeys.

The following are a list of UX flows in which you can promote passkeys:

* **User account registration:** Introduce passkey [creation](/identity/sign-in/credential-manager#create-passkey) prompts at key moments, such as when your users create their accounts:

![contextualprompts.png](/static/blog/assets/contextualprompts_ec9b3bf2aa_1U09TJ.webp)

*Contextual Prompts during account creation*

* **Sign in:** We recommend you encourage users to prompt passkeys in the moment after a user [signs](/identity/sign-in/credential-manager#sign-in) in with an OTP, password, or other-sign in mechanisms.

![passkeys-credential-manager-sign-in.png](/static/blog/assets/passkeys_credential_manager_sign_in_3e69b4ba8d_Z2eOysy.webp)

*Prompt passkey creation during sign-in*

* **Account recovery:** The critical user journey (CUJ) for account recovery is one that historically presents friction to users. Prompting users to adopt passkeys during account recovery is a recommended path. Users who adopt passkeys experience a familiar account recovery experience as during sign-in.

![passkeys-account-recovery.png](/static/blog/assets/passkeys_account_recovery_65d119446f_ZPCoxI.webp)

*Account Recovery flow*

* **Password resets:** This is the perfect moment to prompt users to create a passkey; after the frustration of a password reset, users are typically more receptive to the convenience and security passkeys offer.

![passkeys-new-password-created.png](/static/blog/assets/passkeys_new_password_created_4f0566c0a0_ZT7ljG.webp)

*Create a passkey for faster sign-in next time*

## How should you encourage the transition to passkeys?

Encouraging users to transition from passwords to passkeys requires a clear strategy. A few recommended best practices are as follows:

* **Clear value proposition:** Use simple, user-centric prompts to explain the benefits of passkeys. Use messaging that highlights the benefits for users. Emphasize the following benefits:
  + Improved security benefits, such as safety from phishing.
  + No need to type out a password.
  + Ability to use the same passkey across devices/platforms.
  + A consistent authentication experience.

![create-passkeys-clear-value-proposition.png](/static/blog/assets/create_passkeys_clear_value_proposition_6ab75cb095_snx5w.webp)

*Passkey prompt with clear value proposition*

* **Provide a seamless user experience:**
  + Use the [unified UI](/design/ui/mobile/guides/patterns/passkeys#unified_sign-in) provided by Credential Manager to show all available [sign-in options](/identity/sign-in/credential-manager#sign-in), allowing the user to choose their preferred method without having to remember which one they used last.
  + Use the official [passkey icon](/design/ui/mobile/guides/patterns/passkeys) to build user familiarity and create a consistent experience.
  + Make sure that users can fall back to their traditional sign-in methods or a recovery method, such as a username and password, if a passkey is not available or if they are using a different device.
* **Provide users with clarity about credentials within your app’s Settings UI:** Make sure your users understand their authentications options by displaying helpful information about each passkey within your app’s settings. To learn more about adding credentials metadata, see the [Credential Manager documentation](/identity/sign-in/credential-manager#show-info).

![passkeys-authentication-settings-ui.png](/static/blog/assets/passkeys_authentication_settings_ui_875626c229_ZU2NzI.webp)

*Passkey Metadata on App’s Settings screen*

* **Educate users:** Supplement the messaging to adopt passkeys with in-app educational resources or links that explain [passkeys](https://developers.google.com/identity/passkeys) in detail.
* **Progressive rollout:** Consider a phased rollout to introduce passkeys to a subset of your user base to gather feedback and refine the user experience before a broader launch.

## Developer Case Studies

Real-world developer experiences often highlight how small design choices—like when and where to surface a passkey prompt—can significantly influence adoption and user trust. To see this in action, let’s explore how top apps have strategically surfaced passkey prompts at key moments in their apps to drive stronger adoption :

### Uber

To accelerate passkeys adoption, [Uber](https://play.google.com/store/apps/details?id=com.ubercab) is proactively promoting passkeys in various user journeys, alongside marketing strategies.

*Uber has shared: "**90+% of passkey enrollments come from promoting passkey creation at key moments inside the app as compared to onboarding and authentication CUJs**", underscoring the effectiveness of their proactive strategy.*

#### **Key learnings and strategies from their implementation:**

* **Offer passkeys without disrupting the core user experience:** Uber added a new account checkup experience in their account settings to highlight passkey benefits, resulting in high passkey adoption rates.

![checkupflow.png](/static/blog/assets/checkupflow_f30ae96b3e_18cHAq.webp)

*User Account checkup flow*

* **Proactively bring passkeys to users:** They learned not to wait for users to discover passkeys organically because relying on organic adoption would have been slower despite observed benefits like faster sign-ins and increased login success rates for passkey users.
* **Use additional mediums to promote passkeys:** Uber is also experimenting to promote passkeys through **email campaigns or banners** on a user's account screen to highlight the new sign-in method, making their next sign-in easier and more secure.
* **Respect your user’s choice:** Recognizing that not all users are ready for passkeys, Uber implemented **backoff logic** in critical flows as sign in, signup screens and, in some contexts, offers passkeys alongside other familiar authentication methods.

**Here’s what Uber has to say:**

*"At Uber, we’ve seen users who adopt passkeys enjoy a faster, more seamless, and more secure login experience. To help more users benefit from passkeys, we’ve added nudges to create a passkey at key moments in the user experience: account settings, signup, and login. These proactive outreaches have significantly accelerated our passkey adoption."*

***Ryan O’Laughlin, Senior Software Engineer, Uber***

### Economic Times

[Economic Times](https://play.google.com/store/apps/details?id=com.et.reader.activities&pli=1), part of the Times Internet ecosystem, used a **seamless user experience as the primary motivation for users to transition to passkeys**.

*After introducing targeted nudges, Economic Times observed **~10%** improvements in passkey creation completion rate within the initial rollout period.*

**Key learnings and strategies from their implementation:**

* **Strategic passkey generation prompts:** Initially, Economic Times was aggressively prompting passkey creation in multiple user flows, but it was observed that this approach **disrupted business-critical journeys** such as subscription purchases or unlocking premium features and was leading to abandoned carts.
* **Refined approach:** Economic Times made a deliberate decision to remove passkey generation prompts from sensitive flows (such as the subscription checkout flow) to prioritize immediate action completion.
* **Targeted prompts:** They strategically maintained passkey generation in areas where user intent to sign-in or manage authentication is high, such as initial sign-up flows, explicit sign in pages, or account management sections.
* **Positive outcome:** This refined deployment resulted in improved passkey generation numbers, indicating strong user adoption, without compromising user experience in critical business flows.

![econiomic-times-passkeys-workflow.png](/static/blog/assets/econiomic_times_passkeys_workflow_d65a18f3ca_3Cbr1.webp)

*Passkeys Management Screen*

## Conclusion

Integrating passkeys with Android's Credential Manager isn't just about adopting new technology; it's about building a fundamentally more secure, convenient, and delightful experience for your users. By focusing on intelligent passkey introduction, you're not just securing accounts–you're building trust and future-proofing your application's authentication strategy.

To provide your users the best, optimized and seamless experience, follow the [UX guidelines](/design/ui/mobile/guides/patterns/passkeys) while implementing passkeys authentication with [Credential Manager](/identity/sign-in/credential-manager). Check out the docs today!

* [Sample with UX best practices](https://github.com/android/identity-samples)
* [Sign in your user with Credential Manager](/identity/sign-in/credential-manager%20)
* [API Reference – androidx.credentials](/jetpack/androidx/releases/credentials)
* [User authentication with passkeys](/design/ui/mobile/guides/patterns/passkeys%20)
* [Google Safety Center - Passkey](https://safety.google/authentication/passkey/%20)
* [Google Security Blog: Security of Passkeys in the Google Password Manager](https://security.googleblog.com/2022/10/SecurityofPasskeysintheGooglePasswordManager.html)

###### Written by:

* ## [Niharika Arora](/blog/authors/niharika-arora)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/niharika-arora)

  ![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)

  ![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)
* ## [Vinisha Athwani](/blog/authors/vinisha-athwani)

  ###### Technical Writer

  [read\_more
  View profile](/blog/authors/vinisha-athwani)

  ![](/static/blog/assets/Vinisha_Athwani_e54ba64bd3_2x1elG.webp)

  ![](/static/blog/assets/Vinisha_Athwani_e54ba64bd3_2x1elG.webp)

## Continue reading

* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  04

  Mar
  2026

  04

  Mar
  2026

  ![](/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow\_forward](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 8 min read
* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](/blog/authors/ivy-knight)

  02

  Dec
  2025

  02

  Dec
  2025

  ![](/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow\_forward](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan), [Ivy Knight](/blog/authors/ivy-knight) • 2 min read
* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  20

  Nov
  2025

  20

  Nov
  2025

  ![](/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow\_forward](/blog/posts/leveling-guide-for-your-performance-journey)

  The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 9 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)