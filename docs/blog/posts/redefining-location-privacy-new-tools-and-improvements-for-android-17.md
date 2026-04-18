---
title: https://developer.android.com/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17
url: https://developer.android.com/blog/posts/redefining-location-privacy-new-tools-and-improvements-for-android-17
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Redefining Location Privacy: New Tools and Improvements for Android 17

###### 3-min read

![](https://developer.android.com/static/blog/assets/Redefining_Location_5e4a362604_Z1wl0mf.webp) 26 Mar 2026 [![](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)](https://developer.android.com/blog/authors/robert-clifford) [##### Robert Clifford](https://developer.android.com/blog/authors/robert-clifford)

###### Developer Relations Engineer

A pillar of the Android ecosystem is our shared commitment to user trust. As the mobile landscape has evolved, so does our approach to protecting sensitive information. In Android 17, we're introducing a suite of new location privacy features designed to give users more control and provide developers elegant solutions for data minimization and product safety. Our strategy focuses on introducing new tools to balance high-quality experiences with robust privacy protections, and improving transparency for users to help manage their data.

#### Introducing the location button: simplified access for one time use

For many common tasks, like finding a nearby shop or tagging a social post, your app doesn't need permanent or background access to a user's precise location.With Android 17, we are introducing the location button, a new UI element designed to provide a well-lit path for responsible one time precise location access. Industry partners have requested this new feature as a way to bring a simpler, and more private location flow to their users.
![local-cafe.gif](https://developer.android.com/static/blog/assets/local_cafe_c248e0055c_1T3F4r.webp)

#### Users get better privacy protection

Moving the decision making for location sharing to the point where a user takes action, helps the user make a clearer choice about how much information they want to share and for how long. This empowers users to limit data sharing to only what apps need in that session. Once consent is provided, this session based access eliminates repeated prompts for location dependent features. This benefits developers by creating a smoother experience for their users and providing high confidence in user intent, as access is explicitly requested at the moment of action.

#### Full UI customization to match your app's aesthetic

The location button provides extensive customization options to ensure integration with your app's aesthetic while maintaining system-wide recognizability. You can modify the button's visual style including:

- Background and icon color scheme
- Outline style
- Size and shape

Additionally, you can select the appropriate text label from a predefined list of options. To ensure security and trust, the location icon itself remains mandatory and non-customizable, while the font size is system-managed to respect user accessibility settings.
![location-buttons-examples.png](https://developer.android.com/static/blog/assets/location_buttons_examples_9fda058cb6_160lV0.webp)

#### Simplified Integration with Jetpack and automatic backwards compatibility

The location button will be provided as a Jetpack library, ensuring easy integration into your existing app layouts similar to any other Jetpack view implementation, and simplifying how you request permission to access precise location. Additionally, when you implement location button with the Jetpack library it will automatically handle backwards compatibility by defaulting to the existing location prompt when a user taps it on a device running Android 16 or below.  

The Android location button is available for testing as of Android 17 Beta 3.

#### Location access transparency

Users often struggle to understand the tools they can use to monitor and control access to their location data. In Android 17, we are aligning location permission transparency with the high standards already set for the Microphone and Camera.
![Location-access-transparency.png](https://developer.android.com/static/blog/assets/Location_access_transparency_67f8904e53_Z1YyQNd.webp)

- Updated Location Indicator: A persistent indicator will now appear to inform a user whenever a non-system app accesses their location
- Attribution \& Control: Users can tap the indicator to see exactly which apps have recently accessed their location and manage those permissions immediately through a "Recent app use" dialog.

#### Strengthening user privacy with density-based Coarse Location

Android 17 is also improving the algorithm for approximate (coarse) locations to be aware of population density. Previously, coarse locations used a static 2 km-wide grid, which in low-population areas may not be sufficiently private since a 2km square could often contain only a handful of users. The new approach replaces this fixed grid with a dynamically-sized area based on local population density. By increasing the grid for areas with lower population density, Android ensures a more consistent privacy guarantee across different environments from dense urban centers to remote regions.

#### Improved runtime permission dialog

The runtime permission dialog for location is one of the more complex flows for users to navigate, with users being asked to decide on the granularity and length of permission access they are willing to grant to each app. In an effort to help users to make the most informed privacy decisions with less friction, we've redesigned the dialog to make "**Precise** " and "**Approximate**" choices more visually distinct, encouraging users to select the level of access which best suits their needs.
![location-grant-dialog.gif](https://developer.android.com/static/blog/assets/location_grant_dialog_e2870b657c_Z5crBH.webp)

#### Start building for Android 17

The new location privacy tools are available now in Beta 3. We're looking for your feedback to help refine these features before the general release.

- Feedback: Report issues on the [\[Official Tracker\]](https://developer.android.com/about/versions/17/feedback).

Build a smoother, more private experience today.
- [#Android 17](https://developer.android.com/blog/topics/android-17)

###### Written by:

-

  ## [Robert Clifford](https://developer.android.com/blog/authors/robert-clifford)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/robert-clifford) ![](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp) ![](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Third Beta of Android 17](https://developer.android.com/blog/posts/the-third-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-third-beta-of-android-17) Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  5 min read

  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#beta](https://developer.android.com/blog/topics/beta)
- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)