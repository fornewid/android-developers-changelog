---
title: https://developer.android.com/blog/posts/x-improved-login-success-rate-after-adopting-passkeys
url: https://developer.android.com/blog/posts/x-improved-login-success-rate-after-adopting-passkeys
source: md.txt
---

#### [Case Studies](https://developer.android.com/blog/categories/case-studies)

# X improved login success rate by 2x after adopting passkeys

###### 3-min read

![](https://developer.android.com/static/blog/assets/x_Passkeys_45bf854440_G2vTP.webp) 21 Nov 2024 [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora) [##### Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)

###### Developer Relations Engineer

From breaking news and entertainment to sports and politics, [X](https://play.google.com/store/apps/details?id=com.twitter.android) is a social media app that aims to help nearly 500 million users worldwide get the full story with all the live commentary. Recently, X developers revamped the Android app's login process so users never miss out on the conversations they're interested in. Using the [Credential Manager API](https://developer.android.com/identity/sign-in/credential-manager), the team implemented new [passkey](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys) authentication for quicker, easier, and safer access to the app.

### Simplifying login with passkeys

Today, traditional password-based authentication systems are [less secure and more prone to cyber attacks](https://www.youtube.com/watch?v=2xdV-xut7EQ). Many users often choose easy-to-guess passwords, which bad actors can easily crack using brute force attacks. They also reuse the same passwords across multiple accounts, meaning if one password is hacked, all accounts are compromised.

Passkeys address the growing concern of account security from weak passwords and phishing attacks by eliminating the need for passwords entirely. The feature provides a safer, more seamless sign-in experience, freeing users from having to remember their usernames or passwords.

"Passkeys are a simpler, more secure way to log in, replacing passwords with pins or biometric data like fingerprints or facial recognition," said Kylie McRoberts, head of safety at X. "We explored using passkeys to make signing in easier and safer for users, helping protect their accounts without the hassle of remembering passwords."

Since implementing passkeys, the X team has seen a substantial reduction in login times and metrics showing improved login flow. With passkeys, **the app's successful login rate has doubled** compared to when it only relied on passwords. The team has also seen a decline in password reset requests from users who have enabled passkeys.

According to X developers, adopting passkeys even came with benefits beyond enhanced security and a simplified login experience, like lower costs and improved UX.

"Passkeys allowed us to cut down on expenses related to SMS-based two-factor authentication because they offer strong, inherent authentication," said Kylie. "And with the ease of login, users are more likely to engage with our platform since there's less friction to remember or reset passwords."

Passkeys rely on public-key cryptography to authenticate users and provide them with private keys. That means websites and apps can see and store the public key, but never the private key, which is encrypted and stored by the user's credential provider. As keys are unique and tied to the website or app, they cannot be phished, further enhancing their security.
![xSaurabh.png](https://developer.android.com/static/blog/assets/x_Saurabh_798337a48c_Z1Fin9T.webp)

### Seamless integration using the Credential Manager API

To integrate passkeys, X developers used Android's Credential Manager API, which made the process "extremely smooth," according to Kylie. The API unifies Smart Lock, One Tap, and Google Sign-In into a single, streamlined workflow. This also allowed developers to remove hundreds of lines of code, boosting implementation and reducing maintenance overhead.

In the end, the migration to Credential Manager took X developers only two weeks to complete, followed by an additional two weeks to fully support passkeys. This was a "very fast migration" and the team "didn't expect it to be that simple and straightforward," said Saurabh Arora, a staff engineer at X. Thanks to Credential Manager's simple, coroutine-powered API, the complexities of handling multiple authentication options were essentially removed, reducing code, the likelihood of bugs, and overall developer efforts.

X developers saw a significant improvement in developer velocity by integrating the Credential Manager API. With their shift to passkey adoption through Credential Manager API, they achieved an:

- **80% code reduction in the authentication module**
- **90% resolution of legacy edge case bugs**
- **85% decrease in GIS, One Tap, and Smart Lock handling code**

Using the Credential Manager API's top-level methods, like `createCredential` and `getCredential`, simplified integration by removing custom logic complexities surrounding individual protocols. This uniform approach also meant X developers could use a single, consistent interface to handle various authentication types, such as passkeys, passwords, and federated sign-ins like Sign in with Google.

"With Credential Manager's simple API methods, we could retrieve passkeys, passwords, and federated tokens with a single call, cutting down on branching logic and making response handling cleaner," said Saurabh. "Using different API methods, like `createCredential()` and `getCredential()`, also simplified credential storage, letting us handle passwords and passkeys in one place."

X developers didn't face many challenges when adopting Sign in With Google using the Credential Manager API. Replacing X's previous Google Sign In, One Tap, and Smart Lock code with a simpler Credential Manager implementation meant developers no longer had to handle connection or disconnection statuses and activity results, reducing the margin of error.
![passkeys.png](https://developer.android.com/static/blog/assets/passkeys_560dd9df7b_sp0Ld.webp)

### A future with passkeys

X's integration of passkeys shows that achieving a more secure and user-friendly authentication experience can be achieved. By leveraging Credential Manager API, X developers simplified the integration process, reduced potential bugs, and improved both security and developer velocity---all while sharpening the user experience.

"Our advice for developers considering passkey integration would be to take advantage of the Credential Manager API," said Saurabh. "It really simplifies the process and reduces code you need to write and maintain, making implementation better for developers."

Looking ahead, X plans to further enhance the user experience by allowing sign-ups with passkeys alone and providing a dedicated passkey management screen.

### Get started

Learn how to improve your app's login UX using [passkeys](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys) and the [Credential Manager API](https://developer.android.com/identity/sign-in/credential-manager).

###### Written by:

-

  ## [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/niharika-arora) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp) ![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora) 18 Nov 2025 18 Nov 2025 ![](https://developer.android.com/static/blog/assets/uber_Credentials_12e7f1f5c4_Zjh724.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How Uber is reducing manual logins by 4 million per year with the Restore Credentials API](https://developer.android.com/blog/posts/how-uber-is-reducing-manual-logins-by-4-million-per-year-with-the-restore-credentials-api)

  [arrow_forward](https://developer.android.com/blog/posts/how-uber-is-reducing-manual-logins-by-4-million-per-year-with-the-restore-credentials-api) Uber leveraged the Android Restore Credentials API to streamline new device sign-in, projecting a reduction of 4 million manual logins per year and increasing user retention.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/Joseph_Lewis_a7854037dd_qbEP3.webp)](https://developer.android.com/blog/authors/joseph-lewis) 07 May 2025 07 May 2025 ![](https://developer.android.com/static/blog/assets/ANDDM_Zoho_Header_6260da2eab_3BTtG.webp)

  #### [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Zoho Achieves 6x Faster Logins with Passkey and Credential Manager Integration](https://developer.android.com/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration)

  [arrow_forward](https://developer.android.com/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration) Zoho, a comprehensive cloud-based software suite focused on security and seamless experiences, achieved significant improvements by adopting passkeys in their OneAuth Android app.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Joseph Lewis](https://developer.android.com/blog/authors/joseph-lewis) •
  10 min read

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