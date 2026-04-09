---
title: Kakao Mobility uses Gemini Nano on-device to reduce costs and boost call conversion by 45%  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/kakao-mobility-uses-gemini-nano-on-device-to-reduce-costs-and-boost-call-conversion-by-45
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Case Studies](/blog/categories/case-studies)

# Kakao Mobility uses Gemini Nano on-device to reduce costs and boost call conversion by 45%

###### 4-min read

![](/static/blog/assets/kakao_Mobility_fa49c20743_Z1YdLaQ.webp)

30

Oct
2025

[![](/static/blog/assets/Sa_ryong_Kang_34a2e9f899_2qsGGB.webp)](/blog/authors/sa-ryong-kang)[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/caren-chang)

##### [Sa-ryong Kang](/blog/authors/sa-ryong-kang) & [Caren Chang](/blog/authors/caren-chang)

[Kakao Mobility](https://www.kakaocorp.com/page/service/service/KakaoT?lang=en) is South Korea's leading mobility business, offering a range of transportation and delivery services, including taxi-hailing, navigation, bike and scooter-sharing, parking, and parcel delivery, through its [Kakao T](https://play.google.com/store/apps/details?id=com.kakao.taxi) app. The team at [Kakao Mobility utilized Gemini Nano](https://android-developers.googleblog.com/2025/10/ml-kit-genai-prompt-api-alpha-release.html) via [ML Kit’s GenAI Prompt API](https://developers.google.com/ml-kit/genai) to offer parking assistance for its bike-sharing service and an improved address entry experience for its navigation and delivery services.

The Kakao T app serves over 30 million total users, and its bike-sharing service is one of its most popular services. But unfortunately, many users were improperly parking the bikes or scooters when not in use. This behavior led to an influx of parking violations and safety concerns, resulting in public complaints, fines, and towing. These issues began to negatively affect public perception of both Kakao Mobility and its bike-sharing services.

![wisuk.png](/static/blog/assets/wisuk_3b441cbbfd_Z1EcxO8.webp)

*“By leveraging the ML Kit’s GenAI Prompt API and Gemini Nano, we were able to quickly implement features that improve social value without compromising user experience. Kakao Mobility will continue to actively adopt on-device AI to provide safer and more convenient mobility services.”*— Wisuk Ryu, Head of Client Development Div

To address these concerns, the team initially designed an image recognition model to notify users if their bike or scooter was parked correctly according to local laws and safety standards. Running this model through the cloud would have incurred significant server costs. In addition, the users’ uploaded photos contained information about their parking location, so the team wanted to avoid any privacy or security concerns. The team needed to find a more reliable and cost-effective solution.

The team also wanted to improve the entity extraction experience for the parcel delivery service within the Kakao T app. Previously, users were able to easily order parcel delivery on a chat interface, but drivers needed to enter the address into an order form manually to initiate the delivery order—a process which was cumbersome and prone to human error. The team sought to streamline this process, making order forms faster and less frustrating for delivery personnel.

**Enhancing the user experience with ML Kit’s GenAI Prompt API**

The team tested and compared cloud-based Gemini models against Gemini Nano, accessed via ML Kit’s GenAI Prompt API. “After reviewing privacy, cost, accuracy, and response speed, ML Kit’s GenAI Prompt API was clearly the optimal choice,” said Jinwoo Park, Android application developer at Kakao Mobility.

To address the issue of improperly parked bikes or scooters, the team used Gemini Nano's multimodal capability via the ML Kit GenAI API SDK to detect when a bike or scooter violates local regulations by parking on yellow tactile paving. With a carefully crafted prompt, they were able to evaluate more than 200 labeled images of parking photos while continually refining the inputs. This evaluation, measured through well-known metrics like accuracy, precision, recall, and the F1 score, ensured the feature met production-level quality and reliability standards.

Now users can take a photo of their parked bike or scooter, and the app will inform them if it is parked properly, or provide guidance if it is not. The entire process happens in seconds on the device, protecting the user’s location and information.

![bike.jpg](/static/blog/assets/bike_540326a218_Z1XQwEn.webp)

To create a streamlined entity extraction feature, the team again used ML Kit's GenAI Prompt API to process users' delivery orders written in natural language. If they had employed traditional machine learning, it would have required a large learning dataset and special expertise in machine learning. Instead, they could simply start with a prompt like, "Extract the recipient's name, address, and phone number from the message." The team prepared around 200 high-quality evaluation examples, and evaluated their prompt through many rounds of iteration to get the best result. The most effective method employed was a technique called few-shot prompting, and the results were carefully analyzed to ensure the output contained minimal hallucinations.

![jinwoo.png](/static/blog/assets/jinwoo_74aef50dca_PhkAE.webp)

*“ML Kit’s Prompt API reduces developer overhead while offering strong security and reliability on-device. It enables rapid prototyping, lowers infrastructure dependency, and incurs no additional cost. There is no reason not to recommend it.”*— Jinwoo Park, Android application developer at Kakao Mobility

**Delivering big results with ML Kit’s GenAI Prompt API**

As a result, the entity extraction feature correctly identifies the necessary details of each order, even when multiple names and addresses are entered. To maximize the feature's reach and provide a robust fallback, the team also implemented a cloud-based path using Gemini Flash.

Implementing ML Kit’s GenAI Prompt API has yielded a significant amount of cost savings for the Kakao Mobility team by shifting to on-device AI. While the bike parking analysis feature has not yet launched, the address entry improvement has already delivered excellent results:

* Order completion time for delivery orders has been reduced by 24%.
* The conversion rate has increased by 45% for new users and 6% for existing users.
* During peak seasons, AI-powered orders increase by over 200%.

“Small business owners in particular have shared very positive feedback, saying the feature has made their work much more efficient and significantly reduced stress,” Wisuk added.

After the image recognition feature for bike and scooter parking launches, the Kakao Mobility team is eager to improve it further. Urban parking environments can be challenging, and the team is exploring ways to filter out unnecessary regions from images.

“ML Kit’s GenAI Prompt API offers high-quality features without additional overhead,” said Jinwoo. “This reduced developer effort, shortened overall development time, and allowed us to focus on prompt tuning for higher-quality results.”

**Try ML Kit’s GenAI Prompt API for yourself**

Build and deploy on-device AI in your app with [ML Kit’s GenAI Prompt API](https://developers.google.com/ml-kit/genai) to harness the capabilities of Gemini Nano.

###### Written by:

* ## [Sa-ryong Kang](/blog/authors/sa-ryong-kang)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/sa-ryong-kang)

  ![](/static/blog/assets/Sa_ryong_Kang_34a2e9f899_2qsGGB.webp)

  ![](/static/blog/assets/Sa_ryong_Kang_34a2e9f899_2qsGGB.webp)
* ## [Caren Chang](/blog/authors/caren-chang)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/caren-chang)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

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
* [![](/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](/blog/authors/ben-trengrove)[![](/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)](/blog/authors/ajesh-pai)

  13

  Mar
  2026

  13

  Mar
  2026

  ![](/static/blog/assets/tiktok_Case_Study_ae91bba156_1Bjq08.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [TikTok reduces code size by 58% and improves app performance for new features with Jetpack Compose](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  [arrow\_forward](/blog/posts/tiktok-reduces-code-size-and-improves-app-performance-for-new-features-with-jetpack-compose)

  TikTok is a global short-video platform known for its massive user base and innovative features.

  ###### [Ben Trengrove](/blog/authors/ben-trengrove), [Ajesh Pai](/blog/authors/ajesh-pai) • 2 min read
* [![](/static/blog/assets/Mayuri_Khinvasara_Khabya_92848b1e1b_1xSr0w.webp)](/blog/authors/mayuri-khabya)

  05

  Mar
  2026

  05

  Mar
  2026

  ![](/static/blog/assets/meta_Header_2ac893569c_ZLkD4s.webp)

  #### [Case Studies](/blog/categories/case-studies)

  ## [Instagram and Facebook deliver instant playback and boost user engagement with Media3 PreloadManager](/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  [arrow\_forward](/blog/posts/instagram-and-facebook-deliver-instant-playback-and-boost-user-engagement-with-media3-preload-manager)

  In the dynamic world of social media, user attention is won or lost quickly. Meta apps (Facebook and Instagram) are among the world's largest social platforms and serve billions of users globally.

  ###### [Mayuri Khinvasara Khabya](/blog/authors/mayuri-khabya) • 4 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)