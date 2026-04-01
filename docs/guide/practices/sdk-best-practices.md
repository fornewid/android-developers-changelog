---
title: https://developer.android.com/guide/practices/sdk-best-practices
url: https://developer.android.com/guide/practices/sdk-best-practices
source: md.txt
---

# About user safety and SDKs

As an**app developer**, you want to make sure that you can keep your users safe and your apps secure and stable from any vulnerabilities, including those that may be introduced by Software Development Kits (SDKs) that you use.

As an**SDK provider**, you don't want to have your SDK cause an app or game developer to violate Google Play Developer policies, which can disrupt their business and expose them to enforcement actions by Google Play.

Learn more about best practices for user safety, whether you're an app developer using an SDK or an SDK developer.

## For app developers

- Before you integrate an SDK into your app,[ensure you know](https://medium.com/androiddevelopers/getting-to-know-the-behaviors-of-your-sdk-dependencies-f3dfed07a311)what permissions it uses, what data it collects, and why. Include this information in your[Data safety form](https://support.google.com/googleplay/android-developer/answer/10787469). Note that you as the app developer are responsible for the SDK's data collection behavior, even if you don't use a particular function of the SDK.
- Review all[Google Play Developer policies](https://play.google.com/about/developer-content-policy/)relating to when you can and cannot extend the use of User Data you have collected. For use of device location, for example, you must make any sharing of this data with a third party/SDK known to end users through the[Prominent Disclosure and Consent requirements](https://support.google.com/googleplay/android-developer/answer/11150561).
- Stay up to date with[Google Play policy updates](https://support.google.com/googleplay/android-developer/answer/9934569?ref_topic=9877065)to make sure an SDK you have included in your app does not cause your app to violate Play Policies, such as updates to the[Device and Network Abuse Policy](https://support.google.com/googleplay/android-developer/answer/9888379),[Ads Policy](https://support.google.com/googleplay/android-developer/answer/9857753?ref_topic=9857752), and[User Data Policy with respect to Persistent Identifiers](https://support.google.com/googleplay/android-developer/answer/10144311).
- Do not sell personal and sensitive user information.
- If you receive an enforcement notice about an SDK-caused violation in your app that you need to address, refer to[our instructions for how to resubmit your app following a policy violation](https://support.google.com/googleplay/android-developer/answer/2477981#resubmit).
- Check out[Google Play SDK Index](https://play.google.com/sdks)to see which SDKs are registered on Google Play Console, which Android permissions those SDKs use, and more.

## For SDK providers

- Understand[Google Play Developer policies](https://play.google.com/about/developer-content-policy/).
- Keep up to date with Google Play policy[updates](https://support.google.com/googleplay/android-developer/answer/9934569?ref_topic=9877065)to make sure your SDK does not cause apps to violate Play Policies, such as updates to the[Device and Network Abuse Policy](https://support.google.com/googleplay/android-developer/answer/9888379),[Ads Policy](https://support.google.com/googleplay/android-developer/answer/9857753?ref_topic=9857752), and[User Data Policy with respect to Persistent Identifiers](https://support.google.com/googleplay/android-developer/answer/10144311). Apps that use your SDK may be in violation of these policies and therefore may face enforcement actions by Google Play. For example:

  - If your SDK uses Personal and Sensitive user data, then you must ensure that you have made this clear in your public documentation to apps using your SDK.
  - SDKs with interpreted languages (JavaScript, Python, Lua, etc.) loaded at run time (for example, not packaged with the app) must not allow potential violations (for example, collection of installed packages without appropriate purpose, disclosure and consent) of Google Play policies.
  - Do not sell personal and sensitive user information.
- Support the[latest API security and data minimization features](https://developer.android.com/google/play/requirements/target-sdk)in your SDKs. See an[April 2022 blog post](https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html)for more information.

- Help your customers understand what User Data your SDK may collect and the reason for its use, so that app developers can include this in their[Prominent Disclosure and Consent](https://support.google.com/googleplay/android-developer/answer/10144311)to end users, and in their Privacy Policies when this applies.

- You should implement logic that reads and adheres to the app developer-collected user preference, or ensure that a mechanism exists for the app developer to accurately initialize your SDK according to this user-facing consent event.

- Provide information about your data use in a format easy to access and consume publicly. Here is an[optional format](https://support.google.com/googleplay/android-developer/answer/10787469#optional_format_for_SDKs)that you may be interested in using to publish your information, as many developers are familiar with this format. For examples, see the[Google Firebase SDK data disclosure](https://support.google.com/analytics/answer/11582702)and the[Google AdMob SDK data disclosure](https://developers.google.com/admob/android/play-data-disclosure).