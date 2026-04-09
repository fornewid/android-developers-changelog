---
title: redBus uses Gemini Flash via Firebase AI Logic to boost the length of customer reviews by 57%  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/red-bus-uses-gemini-flash-via-firebase-ai-logic-to-boost-the-length-of-customer-reviews-by-57
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Case Studies](/blog/categories/case-studies)

# redBus uses Gemini Flash via Firebase AI Logic to boost the length of customer reviews by 57%

###### 3-min read

![](/static/blog/assets/thomas_bc2cd0efa0_19rH0O.webp)

30

Oct
2025

[![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)

[##### Thomas Ezan](/blog/authors/thomas-ezan)

###### Senior Developer Relations Engineer

As the world's largest online bus ticketing platform, [redBus](https://play.google.com/store/apps/details?id=in.redbus.android) serves millions of travelers across India, Southeast Asia, and Latin America. The service is predominantly mobile-first, with over 90% of all bookings occurring through its app. However, this presents a significant challenge in gathering helpful feedback from a user base that speaks dozens of different languages. Typing reviews is inconvenient for many users, and a review written in Tamil, for instance, offers little value to a bus operator who only speaks Hindi.  
  
To improve the quality and volume of user feedback, developers at redBus used [Gemini Flash](/ai/gemini), a Google AI model providing low latency, to instantly transcribe and translate user voice recordings. To connect this powerful AI to their app without dealing with complex backend work, they used [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic). This new feature removed language barriers and simplified the review process, leading to a significant increase in user engagement and feedback quality.

**Simplifying user feedback with a voice-first approach**

The previous in-app review experience on redBus was text-based, which presented some key challenges. "At our scale, reliable user reviews are critical: they build trust for travelers and give operators actionable insights. While our existing text-based system served us well, we found that customers often struggled to articulate their full experience, which resulted in our user feedback lacking the necessary detail and volume we needed to deliver maximum value to both travelers and operators. What's more, language barriers limited the usefulness of reviews, as reviews in one language were not helpful for users or bus operators who spoke another. Our primary motivation was to leverage the expressive power of voice and overcome the language barrier to capture more authentic and detailed user feedback," said Abhi Muktheeswarar, a senior tech lead in mobile engineering at redBus.  
  
The developer team wanted to create a frictionless, voice-first experience, so they designed a new flow where users could simply speak their review in their native language. To encourage adoption, the team implemented a prominent, animated mic button paired with a text mentioning: “Your voice matters, share your review in your own language.” This mention appears in the user’s native language, consistent with their app language settings.

![ANDDM_redBus_02_mic_R2.gif](/static/blog/assets/ANDDM_red_Bus_02_mic_R2_9339626aa4_BFGyU.webp)

Using Gemini Flash, the application processes the user’s voice recording. It first transcribes the speech into text, then translates it into English, and finally analyzes the sentiment to automatically generate a star rating and predict relevant tags based on the review content. It then creates a concise summary and autofills the review form fields with the generated content.  
  
Developers chose Firebase AI Logic because it allowed them to build and ship the feature without the help from the backend team, dramatically reducing development time and complexity. “The Firebase AI SDK was a key differentiator because it was the only solution that empowered our frontend team to build and ship the feature independently,” Abhi explained. This approach enabled the team to go from concept to launch in just 30 days.  
  
During implementation, the engineers used [structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output?api=dev), enabling the Gemini Flash model to return well-formed JSON responses, including the transcription, translation, sentiment analysis, and star rating, making it easy to then populate the UI. This ensured a seamless user experience. Users are then shown both the original transcribed text in their own language and the translated, summarized version in English. Most importantly, the user is given full control to review and edit all AI-generated text and change the star rating before submitting the review. They can even speak again to add more content.

![abhi.png](/static/blog/assets/abhi_378e1e96ba_ZoKx3h.webp)

**Driving engagement and capturing deeper user insights**  
The AI-powered voice review feature had a significant positive impact on user engagement. By enabling users to speak in their native language, redBus saw a 57% increase in review length and a notable increase in the overall volume of reviews.

The new feature successfully engaged a segment of the user base that was previously hesitant to type a review. Since implementation, user feedback has been overwhelmingly positive: customers appreciate the accuracy of the transcription and translation, and find the AI-generated summaries to be a concise overview of their longer, more detailed reviews.  
  
Gemini Flash, although hosted in the cloud, delivered a highly responsive user experience. “A common observation from our partners and stakeholders has been that the level of responsiveness from our new AI feature is so fast and seamless that it feels like the AI is running directly on the device,” said Abhi. “This is a testament to the low latency of the Gemini Flash model, which has been a key factor in its success.”

![abhi2.png](/static/blog/assets/abhi2_78ba46f962_Z21nvhb.webp)

**An easier way to build with AI**  
  
For the redBus team, the project demonstrated how Firebase AI Logic and Gemini Flash empower mobile developers to build features that would otherwise require backend implementation. This reduces dependency on server-side changes and allows developers to iterate quickly and independently.  
  
Following the success of the voice review feature, the team at redBus is exploring other use cases for on-device generative AI to further enhance their app. They also plan to use [Google AI Studio](https://aistudio.google.com/prompts/new_chat) to test and iterate on prompts moving forward. For Abhi, the lesson is clear: “It’s no longer about complex backend setups,” he said. “It’s about crafting the right prompt to build the next innovative feature that directly enhances the user experience.”

![gemini2.png](/static/blog/assets/gemini2_761aa5877c_MAWqP.webp)

**Get started**

Learn more about how you can use [Gemini](https://firebase.google.com/docs/ai-logic/get-started?platform=android&api=dev) and [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic) to build generative AI features for your own app.

###### Written by:

* ## [Thomas Ezan](/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/thomas-ezan)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

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