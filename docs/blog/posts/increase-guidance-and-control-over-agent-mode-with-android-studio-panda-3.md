---
title: https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3
url: https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Increase Guidance and Control over Agent Mode with Android Studio Panda 3

###### 3-min read

![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp) 02 Apr 2026 [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) [##### Matt Dyor](https://developer.android.com/blog/authors/matt-dyor)

###### Senior Product Manager

Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

Whether you're bringing new capabilities to an existing app or standing up a brand new app, these updates elevate your development experience by allowing your AI Agent in Android Studio to learn your specific practices and giving you granular control over its permissions.

Lastly, in addition to AI skills and Agent Mode enchantments, Android Studio Panda 3 also includes updated support for build Android apps for cars.

Here's a deep dive into what's new:

## Agent skills

Create a more helpful AI agent by using agent skills in Android Studio. Agent skills are specialized instructions that teach the agent new capabilities and best practices for a specific workflow, which the agent can then leverage as needed. This significantly reduces the level of detail required for your day-to-day prompts. Agent skills work with Gemini in Android Studio or with other [remote 3rd party LLMs](https://developer.android.com/studio/gemini/use-a-remote-model) you integrate into the agent framework in Android Studio.

You and members of your team can create skills that tell the agent exactly how you want to handle specific tasks in your codebase. For example, you could create a custom "code review" skill tailored to your organization's coding standards, or custom skill to provide the agent with more information on using an in-house library.

Once you have created a skill, the agent will be able to use it automatically, or you can manually trigger it by typing @ followed by the skill name. Check out the [documentation](http://d.android.com/studio/gemini/skills) to learn more about how to create skills for your codebase, or better yet---ask your agent to help you build a new skill and it will guide you through the details!
![large_CROPPED-1-3-skill-used-REV.png](https://developer.android.com/static/blog/assets/large_CROPPED_1_3_skill_used_REV_c50fa79b7a_YtsKV.webp) Manually Trigger Agent Skill in Android Studio

#### Getting Started

To build a skill for your project, do the following:

- Create a .skills directory inside your project's root folder.
- Place a SKILL.md file inside this new directory.
- Add a name and description to the file to define your custom workflow, and your skill is ready.
- Optionally include scripts, assets, and references to provide even more guidance to your agent.

![large_CROPPED-1-2-skill-md-REV.png](https://developer.android.com/static/blog/assets/large_CROPPED_1_2_skill_md_REV_cfae04a78f_pKwUV.webp) Agent skills in Android Studio

## Manage permissions for Agent Mode

You control your codebase, and you can now be more deliberate with which data and capabilities you choose to share with AI agents. The new granular agent permissions in Android Studio let you decide exactly what agents can do for you.

When Agent Mode needs to read files, run shell commands, or access the web, it explicitly asks for your permission. We know that 'approval fatigue' is a real risk in AI workflows---when a tool asks for permission too often, it's easy to start clicking 'Allow' without fully reviewing the action. By offering granular 'Always Allow' rules for trusted operations and an optional sandbox for experimental ones, Android Studio helps you stay focused on the high-stakes decisions that actually require your manual sign-off.
![large_2-2-alt-permission-request-REV (1).png](https://developer.android.com/static/blog/assets/large_2_2_alt_permission_request_REV_1_e8252696bb_19ChPO.webp) Agent Permissions

Agent permissions are intuitive to set up and use. For example, granting high-level permissions automatically authorizes related sub-tools, while commands you have previously approved will run automatically without interrupting your flow. Rest assured, accessing sensitive files like SSH keys will always require your explicit sign-off.

For even more security, you can also use an optional sandbox to enforce strict, isolated control over the agent.
![large_2-3-sandbox-REV.png](https://developer.android.com/static/blog/assets/large_2_3_sandbox_REV_8390abb783_Z1RIqE6.webp) Agent Shell Sandbox

## Empty Car App Library App template

We're making it easier to build Android apps for cars. Building apps for the car used to mean wrestling with complex configurations just to get the project to build successfully.

Now, you can accelerate your development with the new "Empty Car App Library App" template in Android Studio. This template takes care of the required boilerplate code for a driving-optimized app on both Android Auto and Android Automotive OS, saving you significant time and effort. Instead of getting bogged down in setup, you can focus on creating the best experience for your users on the road.

#### Getting Started

To use the new template:

- Select **New Project** on the Welcome to Android Studio screen (or **File \> New \> New Project** from within a project).
- Search for or select the **Empty Car App Library App** template.
- Name your app and click **Finish** to generate your driving-optimized app.

![large_3-1-empty-car-app-library-app-template-REV.png](https://developer.android.com/static/blog/assets/large_3_1_empty_car_app_library_app_template_REV_76dd6fd360_brsRp.webp) Empty Car App Library App template

## Android Studio Panda releases

Panda 3 builds off last month's AI-focused Panda 2 release. Check out [Go from prompt to working prototype with Android Studio Panda 2](https://android-developers.googleblog.com/2026/05/go-from-prompt-to-working-prototype.html) post to learn more about new Android Studio features, including the AI-powered New Project Flow that takes you from prompt to prototype and the Version Upgrade Assistant that takes the toil out of updating your dependencies.

## Get started

Dive in and accelerate your development. [Download](https://developer.android.com/studio) Android Studio Panda 3 and start exploring these powerful new agentic features today.

As always, your feedback is crucial to us. [Check known issues](https://developer.android.com/studio/known-issues), [report bugs](https://developer.android.com/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio). Happy coding!
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)

###### Written by:

-

  ## [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matt-dyor) ![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp) ![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)