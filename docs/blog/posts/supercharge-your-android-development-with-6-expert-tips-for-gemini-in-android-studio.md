---
title: https://developer.android.com/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio
url: https://developer.android.com/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Supercharge your Android development with 6 expert tips for Gemini in Android Studio

###### 4-min read

![](https://developer.android.com/static/blog/assets/supercharge_99f4219536_Z2aoaib.webp) 02 Mar 2026 [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) [##### Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

###### Staff Developer Programs Engineer

In January we [announced](https://android-developers.googleblog.com/2026/01/llm-flexibility-agent-mode-improvements.html) Android Studio Otter 3 Feature Drop in stable, including Agent Mode enhancements and many other updates to provide more control and flexibility over using AI to help you build high quality Android apps. To help you get the most out of Gemini in Android Studio and all the new capabilities, we sat down with Google engineers and Google Developer Experts to gather their best practices for working with the latest features---including Agent mode and the New Project Assistant. Here are some useful insights to help you get the best out of your development:

<br />

[Video](https://www.youtube.com/watch?v=9caMeFQYCLk)

<br />

**1. Build apps from scratch with the New Project Assistant**

The new Project Assistant---now available in the latest Canary builds---integrates Gemini with the Studio's New Project wizard. By simply providing prompts and (optionally) design mockups, you can generate entire applications from scratch, including scaffolding, architecture, and Jetpack Compose layouts.

Integrated with the Android Emulator, it can deploy your build and "walk through" the app, making sure it's functioning correctly and that the rendered screens actually match your vision. Additionally, you can use Agent Mode to then continue to work on the app and iterate, leveraging Gemini to refine your app to fit your vision.

Also, while this feature works with the default (no-cost) model, we highly recommend using this feature with an AI Studio API Key to access the latest models --- like Gemini 3.1 Pro or 3.0 Flash --- which excel at agentic workflows. Additionally, adding your API Key allows the New Project Assistant to use Nano Banana behind the scenes to help with ideating on UI design, improving the visual fidelity of the generated application! - Trevor Johns, Developer Relations Engineer.
![newproject.png](https://developer.android.com/static/blog/assets/newproject_eb36203df7_185KLb.webp)

*Dialog for setting up a new project.*

**2. Ask the Agent to refine your code by providing it with 'intentional' contexts**

When using Gemini Agents, the quality of the output is directly tied to the boundaries you set. Don't just ask it to "fix this code"--- be very intentional with the context that you provide it and be specific about what you want (and what you don't). Improve the output by providing recent blogs or docs so the model can make accurate suggestions based on these.

Ask the Agent to simplify complex logic, or if it see's any fundamental problems with it, or even ask it to scan for security risks in areas where you feel uncertain. Being firm with your instructions---even telling the model "please do not invent things" in instances where you are using very new or experimental APIs---helps keep the AI focused on the outputs you are trying to achieve. - Alejandra Stamato, Android Google Developer Expert and Android Engineer at HubSpot.

**3. Use documentation with Agent mode to provide context for new libraries**

To prevent the model from hallucinating code for niche or brand-new libraries, leverage Android Studio's **Agent tools,** tohave access to documentation: Search Android Docs and Fetch Android Docs. You can direct Gemini to search the **Android Knowledge Base** or specific documentation articles. The model can choose to use this if it thinks it's missing some information, which is good especially when you use niche API's, or one's which aren't as common.

If you are certain you want the model to consult the documentation and to make sure those tools are triggered, a good trick is to add something like 'search the official documentation' or 'check the docs' to your prompts. And for documentation on different libraries which aren't Android specific, install a MCP Server that lets you access documentation like Context7 (or something similar). - Jose Alcérreca, Android Developer Relations Engineer, Google.

**4. Use AI to help build** [**Agents.md**](http://agent.md/)**files for using custom frameworks, libraries and design systems**

To make sure Agent uses custom frameworks, libraries and design systems you have two options 1) In settings, Android Studio allows you to specify rules to be followed when Gemini is performing these actions for you. Or 2) Create [Agents.md](http://agent.md/) files in your application and specify how things should be done or act as guidance for when AI is performing a task, specific frameworks, design systems, or specific ways of doing things (such as the exact architecture, things to do or what not to do), in a standard bullet point way to give AI clear instructions.
![agents.png](https://developer.android.com/static/blog/assets/agents_0b8a6623f6_8OIAk.webp)

*Manage *AGENTS.md* files as context.*

You can also use Agents.md file at the root of the project, and can have them in different modules (or even subdirectories) of your project as well! The more context you have or the more guidance available when you're working, that will be available for AI to access. If you get stuck creating these [Agents.md](http://agent.md/) files you can use AI to help build them, or give you foundations based on the projects you have and then edit them so you don't have to start from scratch. - Joe Birch, Android Google Developer Expert and Staff Engineer at Buffer.

**5. Offload the tedious tasks to Agent and save yourself time**

You can get Gemini in Android Studio agent to help you make tasks such as writing and reviewing faster. For example it can help writing commit messages, giving you a good summary which you can then review and save yourself time. Additionally, get it to write tests; under your direction the Agent can look at the other tests in your project and write a good test for you to run following best practices just by looking at them. Another good example of a tedious task is writing a new parser for a certain JSON format. Just give Gemini a few examples and it will get you started very quickly. - Diego Perez, Android Software Engineer, Google

**6. Control what you are sharing with AI using simple opt-outs or commands, alongside paid models.**

If you want to control what is shared with AI whilst on the no-cost plans, you can opt out some or all your code from model training by adding an AI exclusions file ('.aiexclude') to your project. This file uses glob pattern matching similar to a .gitignore file, specifying sensitive directories or files that should be hidden from the AI. You can place .aiexclude files anywhere within the project and its VCS roots to control which files AI features are allowed to access.
![asExclude.png](https://developer.android.com/static/blog/assets/as_Exclude_5d514d1da1_Z2hPKLj.webp)

*An example of an \`.aiexclude\` file in Android Studio.*

Alternatively, in Android Studio settings, you can also opt out of context sharing either on a per project or per user basis (although this method limits the functionality of a number of features because the AI won't see your code).

Remember, paid plans never use your code for model training. This includes both users using an AI Studio API Key, and businesses who are subscribed to Gemini Code Assist. - Trevor Johns, Developer Relations Engineer.

Hear more from the Android team and Google Developer Experts about Gemini in Android Studio in our recent [fireside chat](https://www.youtube.com/watch?v=9caMeFQYCLk) and download [Android Studio](https://developer.android.com/studio?utm_source=blog&utm_medium=referral&utm_campaign=gias_firesidediscordfeb26_blog) to get started.

###### Written by:

-

  ## [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns)

  ###### Staff Developer Programs Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/trevor-johns) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](https://developer.android.com/blog/authors/sandhya-mohan)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) 15 Jan 2026 15 Jan 2026 ![](https://developer.android.com/static/blog/assets/as_Otter3feb_2dc12a1b18_Z1VaHAk.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [LLM flexibility, Agent Mode improvements, and new agentic experiences in Android Studio Otter 3 Feature Drop](https://developer.android.com/blog/posts/llm-flexibility-agent-mode-improvements-and-new-agentic-experiences-in-android-studio-otter-3-feature-drop)

  [arrow_forward](https://developer.android.com/blog/posts/llm-flexibility-agent-mode-improvements-and-new-agentic-experiences-in-android-studio-otter-3-feature-drop) We are excited to announce that Android Studio Otter 3 Feature Drop is now stable! This feature-packed release brings a huge update to your agentic workflows in Android Studio, and offers you more flexibility and control for how you use AI to help you build Android apps.

  ###### [Sandhya Mohan](https://developer.android.com/blog/authors/sandhya-mohan), [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) •
  9 min read

- [![](https://developer.android.com/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](https://developer.android.com/blog/authors/sandhya-mohan)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) 04 Dec 2025 04 Dec 2025 ![](https://developer.android.com/static/blog/assets/as_Otter2_96831eedef_Z19EUHu.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Otter 2 Feature Drop is stable!](https://developer.android.com/blog/posts/android-studio-otter-2-feature-drop-is-stable)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-otter-2-feature-drop-is-stable) The Android Studio Otter 2 Feature Drop is here to supercharge your productivity.

  ###### [Sandhya Mohan](https://developer.android.com/blog/authors/sandhya-mohan), [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) 15 Apr 2026 15 Apr 2026 ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boosting user privacy and business protection with updated Play policies](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)

  [arrow_forward](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies) Making Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)