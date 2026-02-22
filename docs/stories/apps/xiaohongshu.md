---
title: https://developer.android.com/stories/apps/xiaohongshu
url: https://developer.android.com/stories/apps/xiaohongshu
source: md.txt
---

# Let the wonders of the world belong to everyone | Xiaohongshu intensifies its commitment to Android Accessibility

Explore, record, and share -- through videos, photos, and live streams, the online world presents a vibrant and diverse tapestry that draws innumerable visitors daily. Yet, an often-overlooked truth looms large: "innumerable visitors" does not equate to "all-inclusive participation." Particularly for individuals with visual impairments, the vivid and dynamic realm of multimedia remains largely inaccessible.

[The World Health Organization](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment)reports that only a fraction of people with vision impairments receive adequate treatment: 36% of those with refractive errors and 17% with cataracts. This leaves the vast majority without necessary medical care. In China alone, over 17 million individuals suffer from visual impairments due to various causes such as refractive errors, cataracts, diabetes, and aging.

Furthermore, there are numerous situations in daily life where people temporarily experience visual impairment. Examples include the recovery phase following eye surgery or environments where screen viewing is impractical. These scenarios add to the challenges faced by individuals in accessing screen-based information.

One certainty prevails: life persists even in the absence of light. For the team at Xiaohongshu, dedicated to the mission of "Inspiring Lives, sharing and discovering the wonders of the world," every life holds equal wonder, and every user is equally significant. Understanding the unique needs of these users, the team's response is clear and comprehensive: full support for the Android TalkBack screen reading service.

![TalkBack launch announcement](https://developer.android.com/static/images/distribute/stories/xiaohongshu-talkback-launch-poster.png)△ Coinciding with White Cane Safety Day, Xiaohongshu officially implemented support for the TalkBack feature on October 15

## Platform-level Accessibility support

For product teams aiming to offer accessibility features, addressing "standardization" is vital: while adapting to different interaction paradigms in each app may be a "hassle" for those with normal vision, for visually impaired users, it can be an insurmountable barrier.

Android's screen reader,[TalkBack](https://support.google.com/accessibility/android/answer/6283677), plays a critical role here: offering standardized, system-level, and intuitive gestures. These features enable users to learn the most universal screen reading interactions with minimal effort.

Additionally, many of these gestures are as straightforward as using an extra finger compared to regular interactions, substantially reducing the learning curve for users who temporarily need to use TalkBack.

![An example of Talkback support in the Xiaohongshu app](https://developer.android.com/static/images/distribute/stories/xiaohongshu-talkback-screen-login.png)△ From the outset, including the sign-up process and EULA, Xiaohongshu offers support for TalkBack.  

![From sharing button to input textbox, Xiaohongshu app is announcing every finger touch](https://developer.android.com/static/images/distribute/stories/xiaohongshu-talkback-screen-controls.png)△ By dragging a finger across the screen, TalkBack will vocalize the contents and available interactions  

![An example of the activated Talkback menu](https://developer.android.com/static/images/distribute/stories/xiaohongshu-talkback-screen-system-menu.png)△ A three-finger tap activates the TalkBack menu

## Guided by the accessibility framework

The Xiaohongshu team has been familiar with accessibility features for some time. Standard options such as "change font size" in contemporary apps and "color contrast" during design have been catering to the needs of users with visual impairments. Nevertheless, the transition to a fully "eyes-free" interaction model requires extensive industry insights. Having diligently studied Google's "[Building accessible apps](https://developer.android.com/guide/topics/ui/accessibility)," the team resolved to incorporate all aspects of accessibility --- design, development, and testing --- into a holistic approach.

### Identifying issues through automated testing

The eyes-free interaction enabled by TalkBack relies on "touch." If a control is too small, it may be untouchable for users, rendering it unannounced by the system. To address this, the team initially utilizes Google's[Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor)for a preliminary assessment. They then adjust the sizes of interface elements according to the touch target size recommendations provided in the scan results.

![Google\'s Accessibility Scanner Play Store entry](https://developer.android.com/static/images/distribute/stories/xiaohongshu-play-store-scanner-app.png)△ The Accessibility Scanner examines interface elements, providing recommendations on aspects like size and contrast

### Creating a standard for accessibility in design

The objective in design is to distill complex operations into a succinct and user-friendly paradigm. Xiaohongshu's design team, after thoroughly studying Material Design's accessibility guidelines, crafted a comprehensive set of guidelines tailored for their app. This includes specifications for touch targets, gestures, and label strings specifically for TalkBack integration.

△ A dedicated TalkBack guideline for the Xiaohongshu app.

Certain specifications challenge typical development norms. For instance, interface elements with multiple nested layers conventionally require labels and descriptions for each component. But, having TalkBack read each label sequentially could be time-consuming. To address this, the team collaborates to determine the most effective division of touch targets and identifies which labels can be consolidated for a more streamlined user experience.

Take, for instance, the social feed displayed in a two-column layout on the homepage, which includes numerous child elements. Logically, this can be considered as a single TalkBack element. The team amalgamates the essential information on each card, enabling TalkBack to announce only the most meaningful aspects to users. This approach not only simplifies the interface but also lessens the cognitive load for the user, making the experience more efficient and user-friendly.

![An example of message merge](https://developer.android.com/static/images/distribute/stories/xiaohongshu-announcement-merge.png)△ Consolidating significant labels into a single TalkBack announcement, for example: "Meow's little home" posts, "if it weren't for personally decorating, I wouldn't believe this is the same bedroom," receiving "344 likes".

### A straightforward development task yielding unforeseen advantages

Initially, the development team required an additional two workdays to revise the existing code, as they had to accommodate two different interaction paradigms: the regular one and the one for TalkBack.

Fortunately, Google's accessibility API is impressively designed and capable of addressing more than 80% of interaction scenarios. For the remaining scenarios, typically, only adjustments to the sequence of screen reader announcements are necessary, eliminating the need to develop custom accessibility services.

As the team gained deeper understanding of the Android Accessibility framework, they developed more generic utility classes, which effectively reduced the adaptation costs for various business modules. Consequently, in the later stages of implementing accessibility features, the team required only one additional workday for each new feature, streamlining the process significantly.

△ The team customizes the Android Accessibility framework to align with their specific business logic

An unforeseen advantage arose from the necessity for TalkBack's announcements to depend on the labeling of elements, prompting the team to meticulously reassess the ordering and naming of interface elements. This rigorous review led to the serendipitous resolution of some previously overlooked issues: the standardization of naming for graphics with similar meanings, and the rectification of certain pop-ups that were missing exit buttons.

![An Android Studio code sample](https://developer.android.com/static/images/distribute/stories/xiaohongshu-code-check-UI.png)△ A review of interface elements within Android Studio

### Dedicated to preparing for the "Comprehensive Evaluation"

Inviting actual visually impaired users from the real world to test the app constitutes the widely recognized "Grand Test" for the entire team. However, for an app with a multitude of features, conducting such an extensive "Grand Test" for every minor adjustment is not feasible.

In response, the team immersed themselves in understanding user gestures in accessibility mode and actively integrated insights from accessibility practices observed in other apps. They segmented the testing tasks according to different business modules. Following a cycle of iterations within these modules, an integration test is conducted, drawing participation from all roles in the product development process, including product management, design, development, and testing. This collaborative effort focuses on exploratory testing (ET) of the features. Only after gathering and addressing feedback from this round of testing do they invite external visually impaired users, referred to as "Grand Testers," to perform the comprehensive "Grand Test" for the app.

## Accessibility: A collaborative endeavor by the team

At Xiaohongshu, the accessibility team operates as a cross-functional project group, spearheaded by dedicated coordinators and backed by various business divisions. These coordinators play a pivotal role in centralizing accessibility knowledge, crafting guidelines, and overseeing the project to guarantee both standardization and excellence in accessibility practices. The team initiated their efforts with comprehensive user interviews and market research. This foundational work was crucial for conveying the significance of accessibility experiences, like TalkBack, to the company's executive leadership, ensuring understanding at the C-level, and securing necessary resources from the organization.

Within Xiaohongshu, each business department bears the responsibility of incorporating accessibility considerations into their product design, development, and testing workflows. In the actual development process, before beginning accessibility adaptation work, a representative from the accessibility team provides presentations to developers. This team member also assists in gathering and preparing essential development documentation, including common accessibility use cases and frequently asked questions. This approach ensures that all team members are well-informed and equipped with the necessary resources to integrate accessibility seamlessly into their work.

△ Accessibility is advocated for at both the executive (C-level) and code levels

Following the official rollout of the accessibility features, various departments including business, PR, editorial, and others will actively engage in collaborative efforts. This entails internal and external promotional activities as well as event planning to raise awareness and celebrate the inclusion of these accessibility features.

Through the combined dedication of the entire company, Xiaohongshu successfully implemented the TalkBack feature adaptation in a remarkably swift three-month timeframe. The project was initiated in July 2023 and culminated with the release in late September, corresponding to app version 8.9. This adaptation comprehensively addresses core user interactions, encompassing key areas such as login/sign-up, the homepage, navigating social posts, search functionality, user profiles, live streaming, and content publishing, among others.

![Positive feedback from a Xiaohongshu user: It's not just a minor tweak; it's a substantial and comprehensive upgrade. Everything now operates much more seamlessly. Prior to this update, there was always a sense of... bumpiness.](https://developer.android.com/static/images/distribute/stories/xiaohongshu-user-feedback.png)△ Users gave positive feedbacks on TalkBack adaptation.  

![#AccessibleLives UGC social event went viral in the accessibility community!](https://developer.android.com/static/images/distribute/stories/xiaohongshu-UGC-event.png)△ Xiaohongshu has organized the "Love and Share Your Accessible Lives" social event scheduled for October 15th, coinciding with White Cane Safety Day

## Occasionally, well-intentioned actions have unintended consequences

Prior to a specific "Grand Test," the team made the decision to temporarily disable certain features that had not yet been fully adapted. This was done to ensure that users could have the "proper" TalkBack experience during the testing phase.

However, the "Grand Testers" expressed strong opposition to this version. They conveyed to the team that although some features might pose challenges in their current state, users believed they could still navigate and offer valuable feedback for further optimization. Blocking these features was perceived as a form of differential treatment for visually impaired users, inadvertently creating a divide within the community.
> *"We should treat all users equally. The incomplete adaptation of accessibility features is not the users' problem; it's our problem."*
>
> *---- Xiaohongshu accessibility team*

The team quickly realized the value of this lesson. When a user expressed her desire to attend an exhibition but was informed by the organizers that guide dogs were not permitted, she shared this incident on Xiaohongshu. In response, numerous users offered her advice on advocating for her rights. Ultimately, the organizers reconsidered their policy and allowed guide dogs, showcasing the positive impact of inclusive and supportive user engagement.

Whether receiving assistance or offering a helping hand, accessibility features enable everyone to transcend physical differences and live diverse yet interconnected lives.
> *"Improving the lives of everyone is the core value of the Xiaohongshu community."*
>
> *---- Product lead, Xiaohongshu app*

## Welcoming a diverse range of lives

Xiaohongshu continues to strongly emphasize its commitment to accessibility.

The accessibility project at Xiaohongshu received recognition and an award during the company's quarterly evaluations. Additionally, the team is actively working on extending the adaptations to cover additional app versions and platforms. Their overarching goal is to broaden accessibility support, making it accessible to an even wider user base and addressing diverse needs within the accessibility community. Furthermore, they have plans to organize more online and offline events, campaigns, editorial content, and services aimed at increasing awareness and visibility of accessibility features within the community.

Recognizing that the elderly population often encounters more accessibility challenges, Xiaohongshu is planning to introduce campaigns like the "Elderly Home-Friendly Guide." These initiatives are designed to encourage elderly users to actively engage with the user community and contribute to app improvements through feedback and iteration.

![Xiaohongshu's call to embrace the elderly population into the community](https://developer.android.com/static/images/distribute/stories/xiaohongshu-elderly-friendly.png)△ The "Elderly Home-Friendly" campaign.

The accessibility experience will not only lead to more considerate designs but also present[tangible growth](https://developer.android.com/guide/topics/ui/accessibility)opportunities for developers.

Xiaohongshu is in an ongoing pursuit of the answer to the "Grand Test." This response is a work in progress and may never reach completion, as the app will continually evolve, presenting new accessibility scenarios to address. However, the "Grand Testers" remain content as long as the team persists in responding to their needs and striving for improvement.

We anticipate that more developers within the Android community will follow suit in creating thoughtful and inclusive accessible apps, thereby expanding their user base and welcoming additional users to their communities!