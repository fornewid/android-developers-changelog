---
title: Redefining Location Privacy: New Tools and Improvements for Android 17  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Redefining Location Privacy: New Tools and Improvements for Android 17

###### 3-min read

![](/static/blog/assets/Redefining_Location_5e4a362604_Z1wl0mf.webp)

26

Mar
2026

[![](/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)](/blog/authors/robert-clifford)

[##### Robert Clifford](/blog/authors/robert-clifford)

###### Developer Relations Engineer

A pillar of the Android ecosystem is our shared commitment to user trust. As the mobile landscape has evolved, so does our approach to protecting sensitive information. In Android 17, we’re introducing a suite of new location privacy features designed to give users more control and provide developers elegant solutions for data minimization and product safety. Our strategy focuses on introducing new tools to balance high-quality experiences with robust privacy protections, and improving transparency for users to help manage their data.

#### Introducing the location button: simplified access for one time use

For many common tasks, like finding a nearby shop or tagging a social post, your app doesn’t need permanent or background access to a user's precise location.With Android 17, we are introducing the location button, a new UI element designed to provide a well-lit path for responsible one time precise location access. Industry partners have requested this new feature as a way to bring a simpler, and more private location flow to their users.

![local-cafe.gif](/static/blog/assets/local_cafe_c248e0055c_1T3F4r.webp)

#### Users get better privacy protection

Moving the decision making for location sharing to the point where a user takes action, helps the user make a clearer choice about how much information they want to share and for how long. This empowers users to limit data sharing to only what apps need in that session. Once consent is provided, this session based access eliminates repeated prompts for location dependent features. This benefits developers by creating a smoother experience for their users and providing high confidence in user intent, as access is explicitly requested at the moment of action.

#### Full UI customization to match your app’s aesthetic

The location button provides extensive customization options to ensure integration with your app's aesthetic while maintaining system-wide recognizability. You can modify the button's visual style including:

* Background and icon color scheme
* Outline style
* Size and shape

Additionally, you can select the appropriate text label from a predefined list of options. To ensure security and trust, the location icon itself remains mandatory and non-customizable, while the font size is system-managed to respect user accessibility settings.

![location-buttons-examples.png](/static/blog/assets/location_buttons_examples_9fda058cb6_160lV0.webp)

#### Simplified Integration with Jetpack and automatic backwards compatibility

The location button will be provided as a Jetpack library, ensuring easy integration into your existing app layouts similar to any other Jetpack view implementation, and simplifying how you request permission to access precise location. Additionally, when you implement location button with the Jetpack library it will automatically handle backwards compatibility by defaulting to the existing location prompt when a user taps it on a device running Android 16 or below.  
  
The Android location button is available for testing as of Android 17 Beta 3.

#### Location access transparency

Users often struggle to understand the tools they can use to monitor and control access to their location data. In Android 17, we are aligning location permission transparency with the high standards already set for the Microphone and Camera.

![Location-access-transparency.png](/static/blog/assets/Location_access_transparency_67f8904e53_Z1YyQNd.webp)

* Updated Location Indicator: A persistent indicator will now appear to inform a user whenever a non-system app accesses their location
* Attribution & Control: Users can tap the indicator to see exactly which apps have recently accessed their location and manage those permissions immediately through a "Recent app use" dialog.

#### Strengthening user privacy with density-based Coarse Location

Android 17 is also improving the algorithm for approximate (coarse) locations to be aware of population density. Previously, coarse locations used a static 2 km-wide grid, which in low-population areas may not be sufficiently private since a 2km square could often contain only a handful of users. The new approach replaces this fixed grid with a dynamically-sized area based on local population density. By increasing the grid for areas with lower population density, Android ensures a more consistent privacy guarantee across different environments from dense urban centers to remote regions.

#### Improved runtime permission dialog

The runtime permission dialog for location is one of the more complex flows for users to navigate, with users being asked to decide on the granularity and length of permission access they are willing to grant to each app. In an effort to help users to make the most informed privacy decisions with less friction, we’ve redesigned the dialog to make "**Precise**" and "**Approximate**" choices more visually distinct, encouraging users to select the level of access which best suits their needs.

![location-grant-dialog.gif](/static/blog/assets/location_grant_dialog_e2870b657c_Z5crBH.webp)

#### Start building for Android 17

The new location privacy tools are available now in Beta 3. We’re looking for your feedback to help refine these features before the general release.

* Feedback: Report issues on the [[Official Tracker]](/about/versions/17/feedback).

Build a smoother, more private experience today.

* [#Android 17](/blog/topics/android-17)

###### Written by:

* ## [Robert Clifford](/blog/authors/robert-clifford)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/robert-clifford)

  ![](/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)

  ![](/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)

## Continue reading

* [![](/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](/blog/authors/matthew-mccullough)

  26

  Mar
  2026

  26

  Mar
  2026

  ![](/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](/blog/categories/product-news)

  ## [The Third Beta of Android 17](/blog/posts/the-third-beta-of-android-17)

  [arrow\_forward](/blog/posts/the-third-beta-of-android-17)

  Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.

  ###### [Matthew McCullough](/blog/authors/matthew-mccullough) • 5 min read

  + [#Android 17](/blog/topics/android-17)
  + [#beta](/blog/topics/beta)
* [![](/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](/blog/authors/matthew-warner)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow\_forward](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](/blog/authors/matthew-warner) • 2 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/matt-dyor)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow\_forward](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](/blog/authors/matt-dyor) • 3 min read

  + [#Android Studio](/blog/topics/android-studio)

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)