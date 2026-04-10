---
title: How Uber is reducing manual logins by 4 million per year with the Restore Credentials API  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/how-uber-is-reducing-manual-logins-by-4-million-per-year-with-the-restore-credentials-api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Case Studies](/blog/categories/case-studies)

# How Uber is reducing manual logins by 4 million per year with the Restore Credentials API

###### 5-min read

![](/static/blog/assets/uber_Credentials_12e7f1f5c4_Zjh724.webp)

18

Nov
2025

[![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)](/blog/authors/niharika-arora)

[##### Niharika Arora](/blog/authors/niharika-arora)

###### Developer Relations Engineer

[Uber](https://www.uber.com/in/en/) is the world’s largest ridesharing company, getting millions of people from here to there while also supporting food delivery, healthcare transportation, and freight logistics. Simplicity of access is crucial to its success; when users switch to a new device, they expect a seamless transition without needing to log back into the Uber app or go through SMS-based one-time password authentication. This frequent device turnover presents a challenge, as well as an opportunity for strong user retention.

To maintain user continuity, Uber’s engineers turned to the [Restore Credentials](/identity/sign-in/restore-credentials) feature, an essential tool for a time when 40% of people in the United States replace their smartphone every year. Following an assessment of user demand and code prototyping, they introduced Restore Credentials support in the [Uber rider app](https://play.google.com/store/apps/details?id=com.ubercab). To validate that restoring credentials helps remove friction for re-logins, the Uber team ran a successful A/B experiment for a five-week period. The integration led to a reduction in manual logins that, when projected across Uber's massive user base, is estimated to eliminate 4 million manual logins annually.

### **Eliminating login friction with Restore Credentials**

![restore-credentials.gif](/static/blog/assets/restore_credentials_e5878fb6dd_Z2lRiR5.webp)

There were past attempts at account restoration on new devices using solutions like regular data [backup](/identity/data/backup) and [BlockStore](https://www.google.com/search?q=blockstore&oq=blockstore&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIGCAMQABgeMgYIBBAAGB4yBggFEEUYQDIGCAYQRRhAMgYIBxBFGEDSAQgyMzY3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8), though both solutions required sharing authentication tokens directly, from source device to destination device. Since token information is highly sensitive, these solutions are only used to some extent, to pre-fill login fields on the destination device and reduce some friction during the sign-in flows. Passkeys are also used to provide a secure and fast login method, but their user-initiated nature limits their impact on seamless device transitions.

“Some users don’t use the Uber app on a daily basis, but they expect it will just work when they need it,” said Thomás Oliveira Horta, an Android engineer at Uber. “Finding out you’re logged out just as you open the app to request a ride on your new Android phone can be an unpleasant, off-putting experience.”

With [Restore Credentials](/identity/sign-in/restore-credentials), the engineers were able to bridge this gap. The API generates a unique token on the old device, which is seamlessly and silently moved to the new device when the user restores their app data during the standard onboarding process. This process leverages Android OS’s native backup and restore mechanism, ensuring the safe transfer of the restore key along with the app's data. The streamlined approach guarantees a simple and safe account transfer, meeting Uber's security requirements without any additional user input or development overhead.

**Note:** Restore keys and passkeys use the same underlying server implementation. However, when you save them in your database, you must differentiate between them. This distinction is crucial because user-created passkeys can be managed directly by the user, while restore keys are system-managed and hidden from the user interface.

“With the adoption of Restore Credentials on Uber’s rider app, we started seeing consistent usage,” Thomás said. “An average of **10,000 unique daily users** have signed in with Restore Credentials in the current rollout stage, and they’ve enjoyed a seamless experience when opening the app for the first time on a new device. We expect that number to **double** once we expand the rollout to our whole user base.”

![image_thomas2.png](/static/blog/assets/image_thomas2_540836154e_Zd2DWB.webp)

### **Implementation Considerations**

“Integration was pretty easy with minor adjustments on the Android side by following the [sample code](https://github.com/android/identity-samples/tree/main/Shrine) and [documentation](/identity/sign-in/restore-credentials),” Thomás said. “Our app already used Credential Manager for passkeys, and the backend required just a couple of small tweaks. Therefore, we simply needed to update the Credential Manager dependency to its latest version to get access to the new Restore Credentials API. We created a restore key via the same [passkey creation flow](/identity/sign-in/restore-credentials#implementation) and when our app is launched on a new device, the app proactively checks for this key by attempting a silent passkey retrieval. If the restore key is found, it is immediately utilized to automatically sign the user in, bypassing any manual login.”

Throughout the development process, Uber's engineers navigated a few challenges during implementation—from choosing the right entry point to managing the credential lifecycle on the backend.

### **Choosing the Restore Credentials entry point**

The engineers carefully weighed the tradeoffs between a perfectly seamless user experience and implementation simplicity when selecting which Restore Credentials **entry point to use for recovery**. Ultimately, they prioritized a solution that offered an ideal balance.

“This can take place during App Launch or in the background during device restoration and setup, using BackupAgent,” Thomás said. “The background login entry point is more seamless for the user, but it presented challenges with background operations and required usage of the [BackupAgent API](/reference/android/app/backup/BackupAgent), which would have led to increased complexity in a codebase as large as Uber’s.” They decided to implement the feature during the **first app launch**, which was significantly faster than the manual login.

### **Addressing server-side challenges**

A few server-side challenges arose during integration with the backend WebAuthn APIs, as their design assumed user verification would always be required, and that all credentials would be listed in a user's account settings; neither of these assumptions worked for the non-user-managed Restore Credential keys.

The Uber team resolved this by making minor changes to the WebAuthn services, creating new credential types to distinguish passkeys from Restore Credentials and process them appropriately.

### **Managing the Restore Credentials lifecycle**

Uber’s engineers faced several challenges in managing the credential keys on the backend, with specialized support from backend engineer Ryan O’Laughlin:

* **Preventing orphaned keys**: A significant challenge was defining a strategy for deleting registered Public Keys to prevent them from becoming "orphaned." For example, uninstalling the app deletes the local credential, but because this action doesn't signal the backend, it leaves an unused key on the server.
* **Balancing key lifespan**: Keys needed a "time to live" that was long enough to handle edge cases. For example, if a user goes through a backup and restore, then manually logs out from the old device, the key is deleted from that old device. However, the key must remain valid on the server so the new device can still use it.
* **Supporting multiple devices**: Since a user might have multiple devices (and could initiate a backup and restore from any of them), the backend needed to support multiple Restore Credentials per user (one for each device).

Uber’s engineers addressed these challenges by establishing rules for server-side key deletion based on new credential registration and credential usage.

The feature went from design to delivery in a rapid two-month development and testing process. Afterward, a five-week A/B experiment (time to validate the feature with users) went smoothly and yielded undeniable results.

### **Preventing user drop-off with Restore Credentials**

By eliminating manual logins on new devices, Uber retained users who might have otherwise abandoned the sign-in flow on a new device. This boost in customer ease was reflected in a wide array of improvements, and though they may seem slight at a glance, the impact is massive at the scale of Uber’s user base:

* 3.4% decrease in manual logins (SMS OTP, passwords, social login).
* 1.2% reduction in expenses for logins requiring SMS OTP.
* 0.575% increase in Uber’s access rate (% of devices that successfully reached the app home screen).
* 0.614% rise in devices with completed trips.

Today, Restore Credentials is well on its way to becoming a **standard** part of Uber’s rider app, with over **95% of users** in the trial group registered.

![uber-devices.png](/static/blog/assets/uber_devices_66c9180609_Zcyhtd.webp)

During new device setup, users can restore app data and credentials from a backup. After selecting Uber for restoration and the background process finishes, the app will automatically sign the user in on the new device's first launch.

![image_thomas.png](/static/blog/assets/image_thomas_cfa94e0c4f_254KJd.webp)

### **The invisible yet massive impact of Restore Credentials**

In the coming months, Uber plans to expand the integration of Restore Credentials. Projecting from the trial’s results, they estimate the change will eliminate 4 million manual logins annually. By simplifying app access and removing a key pain point, they are actively building a more satisfied and loyal customer base, one ride at a time.

"Integrating Google's RestoreCredentials allowed us to deliver the seamless 'it just works' experience our users expect on a new device,” said Matt Mueller, Lead Product Manager (Core Identity) at Uber. “This directly translated to a measurable increase in revenue, proving that reducing login friction is key to user engagement and retention."

### **Ready to enhance your app's login experience?**

Learn how to facilitate a seamless login experience when switching devices with [Restore Credentials](/identity/sign-in/restore-credentials) and read more in the [blog post](https://android-developers.googleblog.com/2024/11/maintain-strong-user-relationships-with-restore-credentials.html). In the latest canary of the [Android Studio Otter](/studio/releases?_gl=1*yzmh3l*_up*MQ..&gclid=CjwKCAiAt8bIBhBpEiwAzH1w6fR90Bfyvr4pM57qxapc5Gqj9O7gQ2V6Jgr9AQjWOEinAJrzTVzg9xoC9E0QAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAAC-IOZl-aH6KKZCkBUS3NwKxqyaUj) you can validate your integration, as new features help mock the backup and restoring mechanisms.

If you are new to Credential Manager, you can refer to our official [documentation](/identity/sign-in/credential-manager), [codelab](https://codelabs.developers.google.com/credential-manager-api-for-android#0) and [samples](https://github.com/android/identity-samples) for help with integration

###### Written by:

* ## [Niharika Arora](/blog/authors/niharika-arora)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/niharika-arora)

  ![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)

  ![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)

## Continue reading

* [![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)](/blog/authors/niharika-arora)[![](/static/blog/assets/Joseph_Lewis_a7854037dd_qbEP3.webp)](/blog/authors/joseph-lewis)

  07

  May
  2025

  07

  May
  2025

  ![](/static/blog/assets/ANDDM_Zoho_Header_6260da2eab_3BTtG.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Zoho Achieves 6x Faster Logins with Passkey and Credential Manager Integration](/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration)

  [arrow\_forward](/blog/posts/zoho-achieves-6x-faster-logins-with-passkey-and-credential-manager-integration)

  Zoho, a comprehensive cloud-based software suite focused on security and seamless experiences, achieved significant improvements by adopting passkeys in their OneAuth Android app.

  ###### [Niharika Arora](/blog/authors/niharika-arora), [Joseph Lewis](/blog/authors/joseph-lewis) • 10 min read
* [![](/static/blog/assets/niharika_2910f6d612_C99s1.webp)](/blog/authors/niharika-arora)

  21

  Nov
  2024

  21

  Nov
  2024

  ![](/static/blog/assets/x_Passkeys_45bf854440_G2vTP.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [X improved login success rate by 2x after adopting passkeys](/blog/posts/x-improved-login-success-rate-after-adopting-passkeys)

  [arrow\_forward](/blog/posts/x-improved-login-success-rate-after-adopting-passkeys)

  From breaking news and entertainment to sports and politics, X is a social media app that aims to help nearly 500 million users worldwide get the full story with all the live commentary.

  ###### [Niharika Arora](/blog/authors/niharika-arora) • 3 min read
* [![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

  30

  Mar
  2026

  30

  Mar
  2026

  ![](/static/blog/assets/monzo_boosts_performance_aff3a37917_6VY99.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Monzo boosts performance metrics by up to 35% with a simple R8 update](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  [arrow\_forward](/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update)

  Monzo is a UK digital bank with 15 million customers and growing. As the app scaled, the engineering team identified app startup time as a critical area for improvement but worried it would require significant changes to their codebase.

  ###### [Ben Weiss](/blog/authors/ben-weiss) • 2 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)