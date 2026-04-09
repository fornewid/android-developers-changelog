---
title: LLM flexibility, Agent Mode improvements, and new agentic experiences in Android Studio Otter 3 Feature Drop  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/llm-flexibility-agent-mode-improvements-and-new-agentic-experiences-in-android-studio-otter-3-feature-drop
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# LLM flexibility, Agent Mode improvements, and new agentic experiences in Android Studio Otter 3 Feature Drop

###### 9-min read

![](/static/blog/assets/as_Otter3feb_2dc12a1b18_Z1VaHAk.webp)

15

Jan
2026

[![](/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](/blog/authors/sandhya-mohan)[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/trevor-johns)

##### [Sandhya Mohan](/blog/authors/sandhya-mohan) & [Trevor Johns](/blog/authors/trevor-johns)

We are excited to announce that Android Studio Otter 3 Feature Drop is now stable! This feature-packed release brings a huge update to your agentic workflows in Android Studio, and offers you more flexibility and control for how you use AI to help you build Android apps.

* **Bring Your Own Model:**You can now use any LLM to power the AI functionality in Android Studio.
* **Agent Mode Enhancements:** You can now more easily have Agent Mode interact with your app on devices, review and accept suggested changes, and have multiple conversations threads.
* **Run user journey tests using natural language:** with Journeys in Android Studio.
* **Enable Agent Mode to connect to more tools:**including the ability to connect to remote servers via MCP.
* **Build, iterate and test your UI:**with UI agentic experiences in Android Studio.
* **Build deep links using natural language:** with the new app links assistant.
* **Debug R8 optimized code:** with Automatic Logcat retracing.
* **Simplify Android library modules:**with the Fused library plugin.

Here’s a deep dive into what’s new:

### **Bring Your Own Model (BYOM)**

Every developer has a unique workflow when using AI, and different companies have different policies on AI model usage. With this release, Android Studio now brings you more flexibility by allowing you to choose the LLM that powers the AI functionality in Android Studio, giving you more control over performance, privacy, and cost.

#### **Use a remote model**

You can now integrate remote models—such as OpenAI’s GPT, Anthropic’s Claude, or a similar model—directly into Android Studio. This allows you to leverage your preferred model provider without changing your IDE. To get started, configure a remote model provider in Settings by adding your API endpoint and key. Once configured, you can select your custom model directly from the picker in the AI chat window.

![1.png](/static/blog/assets/1_d65edd818b_2tIfGM.webp)

*Enter the remote model provider information*

#### **Use a local model**

If you have limited internet connectivity, strict data privacy requirements, or a desire to experiment with open-source research, Android Studio now supports local models via providers like **LM Studio** or **Ollama**. While Gemini in Android Studio remains the default recommendation—tuned specifically for Android development with full context awareness—if you have a specific model preference, Android Studio supports it.

![2.png](/static/blog/assets/2_318d2c5d5c_Z23Quc5.webp)

*Model picker in Android Studio*

A local model offers an alternative to the LLM support built into Android Studio, and typically requires significant local system RAM and hard drive space to run well. However, Gemini in Android Studio provides the best Android development experience because Gemini is tuned for Android and supports all features of Android Studio. With Gemini, you can choose from a variety of models for your Android development tasks, including the no-cost default model or models accessed with a paid Gemini API key.

#### **Use your Gemini API key**

While Android Studio includes access to a default Gemini model with generous quotas at no cost, some developers need more. By adding your Gemini API key, Android Studio can directly access all the latest Gemini models available from Google.

For example, this allows you to use the most recent [Gemini 3 Pro](https://android-developers.googleblog.com/2025/11/gemini-3-is-now-available-for-ai.html) and [Gemini 3 Flash](https://android-developers.googleblog.com/2025/12/build-smarter-apps-with-gemini-3-flash.html) models (among others) with expanded context windows and quota. This is especially useful for developers who are using Agent Mode for extended coding sessions, where this additional processing power can provide higher fidelity responses.

You can also [read more about how we're rolling out Gemini 3 to all Android Studio users](https://android-developers.googleblog.com/2025/11/gemini-3-is-now-available-for-ai.html), including Gemini Code Assist subscribers and developers accessing the default Gemini in Android Studio model at no-cost.

### **Agent Mode enhancements**

Agent Mode is the semi-autonomous AI assistant in Android Studio that aids in your software development, used by many developers, including [the Ultrahuman team](https://android-developers.googleblog.com/2026/01/ultrahuman-launches-features-15-faster.html). Get more out of Agent Mode with these new updates.

#### Run your app and interact with it on devices

Agent Mode can now deploy an application to the connected device, inspect what is currently shown on the screen, take screenshots, check Logcat for errors, and interact with the running application. This lets the agent help you with changes or fixes that involve re-running the application, checking for errors, and verifying that a particular update was made successfully (for example, by taking and reviewing screenshots).

![3.png](/static/blog/assets/3_e67f5f7882_Z2pJMHU.webp)

*Agent mode uses device actions to deploy and verify changes*

#### **Find and review changes using the changes drawer**

You can now see and manage all changes made by the AI agent using the changes drawer. When the agent makes changes to your codebase, you can see the files that were edited in **Files to review**. From there, you can keep or revert the changes individually or all together. Click an individual file in the drawer to see the code diff in the editor and make refinements if needed. With the changes drawer, you can keep track of edits made by the agent during your chat and revisit specific changes without scrolling back through your conversation history.

![4.png](/static/blog/assets/4_024e2c4e29_Z2hx2xj.webp)

*See all the files that the agent has proposed edits to in the changes drawer*

Note: If the **Don't ask to edit files** setting is disabled in **Agent Options**, Agent Mode will request permission for every individual change. Each change must be accepted before it appears in the changes drawer. To allow multiple file edits to appear in the drawer simultaneously, enable the **Don't ask to edit files** option.

![5.png](/static/blog/assets/5_d3c1a90b4f_llUam.webp)

*Accept a change to add it to the changes drawer*

#### **Manage multiple conversation threads**

You can now organize your conversations with Gemini in Android Studio into multiple threads. This lets you create a new chat or agent thread when you need to start with a clean slate, and you can go back to older conversations in the history tab. Using separate threads for each distinct task can improve response quality by limiting the scope of the AI's context to only the topic at hand.

To start a new thread, click *New Conversation*. To see your conversation history, click *Recent Chats.*

![6.png](/static/blog/assets/6_b29c950a51_NWOKv.webp)

*See prior conversations in the “Recent Chats” tab*

Your conversation history is saved to your account, so if you have to sign out or switch accounts you can resume right where you left off when you come back.

### **Journeys for Android Studio**

Running end-to-end UI tests can improve confidence that you’re shipping a high-quality app to production, but writing and maintaining those tests can be difficult, brittle, and limited in what you’re able to test. [Journeys for Android Studio](/studio/gemini/journeys) leverages the reasoning and vision capabilities of Gemini to enable you to write and maintain end-to-end UI tests using natural language instructions—and it’s now available in the latest stable release of Android Studio when you enable it from Studio Labs in your Android Studio Settings.

![7.png](/static/blog/assets/7_d6e86f478a_al5Hs.webp)

*Journeys for Android Studio*

These natural language instructions are converted into interactions that Gemini performs directly on your app. This not only makes your tests easier to write and understand, but also enables you to define complex assertions that Gemini evaluates based on what it “sees” on the device screen. Because Gemini reasons about *how* to achieve your goals, these tests are more resilient to subtle changes in your app's layout, significantly reducing flaky tests when running against different app versions or device configurations.

![8.gif](/static/blog/assets/8_4e97d53936_Z2p05FI.webp)

*Journeys for Android Studio*

You can [write and run journeys](/studio/gemini/journeys)directly from Android Studio against any local or remote device. The IDE provides a new editor experience for crafting your test steps in an XML file, using either a code view or a dedicated design view. When you run a journey, Android Studio provides rich, detailed results that help you follow Gemini's execution. The test panel breaks down the entire journey into its discrete steps, showing you screenshots for each action, what action was taken, and Gemini's reasoning for why it took that action, making debugging and validation clearer than ever. And because journeys are run as Gradle tasks, you can run them from the command line after you authenticate with a Google Cloud Project.

### **Support for remote MCP servers**

Android Studio now lets you connect directly to remote Model Context Protocol (MCP) servers such as Figma, Notion, Canva, Linear, and more. This significantly reduces your context switching since it enables the AI agent in Android Studio to leverage external tools, helping you stay in your flow. For example, you can connect to Figma's remote MCP server to access files and provide this information to Agent Mode, generating more accurate code from your designs. To learn more about how to add an MCP server, see [Add an MCP server](/studio/gemini/add-mcp-server).

![9.png](/static/blog/assets/9_e02698c210_Z2fzUoe.webp)

*Connect to the Figma remote MCP server in Android Studio Settings*

![10.gif](/static/blog/assets/10_76df938d43_Z2injI7.webp)

*Quickly add a screen to your app using the Figma remote MCP server*

### **Supercharge your UI development with Agent Mode**

Gemini in Android Studio is now integrated into the UI development workflow directly from within the [Compose Preview](/develop/ui/compose/tooling/previews) panel, helping you go from design to a high-quality implementation faster. These new agentic capabilities are designed to assist you at every stage of development, from initial code generation to iteration, refinement, and debugging, with entry points in the context of your work.

#### **Create new UI from a design mock**

Accelerate your initial UI implementation by generating Compose code directly from a design mock. Simply click **Generate Code From Screenshot** in an empty Preview panel, and Gemini will use the image to generate a starting implementation, saving you from writing boilerplate from scratch.

![11.gif](/static/blog/assets/11_3931a02d3f_jfcTq.webp)

*Generate code from a screenshot in an empty Preview panel*

![12.png](/static/blog/assets/12_83c2ea9261_ZrGC12.webp)

*Example turning design into Compose code*

#### **Match your UI with a target image**

Once you have an initial implementation, you can iteratively refine it to be pixel-perfect. Right-click your Compose Preview and select **AI Actions > Match UI to Target Image**. Upload a reference design, and the agent will suggest code changes to make your UI match the design as closely as possible.

![13.gif](/static/blog/assets/13_e36cf18eb2_ZYsCQs.webp)

*Example of using "Match UI to Target Image"*

#### **Iterate on your UI with natural language**

For more specific or creative changes, right-click on your preview and use the **AI Actions >  Change UI**. This capability now leverages Agent Mode to validate the results, making it more powerful and accurate. You can use natural language prompts like "change the button color to blue" or "add padding around this text," and Gemini will apply the code modifications instantly.

![14.png](/static/blog/assets/14_b032255279_Z2p4cDn.webp)

*Example of using "Change UI"*

**Find and fix UI quality issues**

Verifying your UI is high-quality and more accessible is a critical final step. The **AI Actions > Fix all UI check** tool audits your UI for common problems, such as accessibility issues. The agent will then propose and apply fixes to resolve the detected issues.

![15.gif](/static/blog/assets/15_5cdbf5c9aa_Z2uUyR.webp)

*Entry point to trigger "Fix all UI check issues"*

You can also find the same functionality by using the **Fix with AI** button in Compose UI check mode:

![16.png](/static/blog/assets/16_fd4d43bec0_ZomyOm.webp)

*"Fix with AI" in UI Check mode*

The features mentioned above are also accessible by the toolbar icon in the Preview panel:

![17.png](/static/blog/assets/17_e3bff9d09a_Wlpa2.webp)

*Second entry point to UI development AI features*

Beyond iterating on your UI, Gemini also helps streamline your development environment.

To accelerate your setup, you can:

* **Generate Compose Previews**: This feature is now enhanced by Agent Mode to provide more accurate results. When working in a file that has Composable functions but no @Preview annotations, you can right-click on the Composable and select **Gemini > Generate [Composable name] Preview**. The agent will now better analyze your Composable to generate the necessary boilerplate with correct parameters, to help verify that a successfully rendered preview is added.

![18.png](/static/blog/assets/18_0d50d7f5b5_8bUsz.webp)

*Entry point to generate Compose Preview*

* ***Fix Preview rendering errors:** When a Compose Preview fails to render, Gemini can now analyze the error message and your code to find the root cause and apply a fix.*

![19.gif](/static/blog/assets/19_74a0841106_Z1wesLf.webp)

*Using "Fix with AI" on Preview render error*

### **App Links Assistant**

The App Links Assistant now integrates with Agent Mode to automate the creation of deep link logic, simplifying one of the most time-consuming steps of implementation. Instead of manually writing code to parse incoming intents and navigate users to the correct screen, you can now let Gemini generate the necessary code and tests. Gemini presents a diff view of the suggested code changes for your review and approval, streamlining the process of handling deep links and ensuring users are seamlessly directed to the right content in your app.

To get started, open the App Links Assistant through the tools menu, then choose **Create Applink**. In the second step, **Add logic to handle the intent**, select **Generate code with AI assistance**. If a sample URL is available, enter it, and then click **Insert Code**.

![20.gif](/static/blog/assets/20_0210927b16_IgYV3.webp)

*App Links Assistant*

### **Automatic Logcat Retracing**

Debugging R8-optimized code just became seamless. Previously, when R8 was enabled (minifyEnabled = true in your build.gradle.kts file), it would obfuscate stack traces, changing class names, methods, and line numbers. To find the source of a crash, developers had to manually use the R8 retrace command line tool.

Starting with **Android Studio Otter 3** **Feature Drop** with **AGP versions 8.12 and above**, this extra step is no longer necessary. Logcat now automatically detects and retraces R8-processed stack traces, so you can see the original, human-readable stack trace directly in the IDE. This provides a much-improved debugging experience with no extra work required.

![21.png](/static/blog/assets/21_48b4126007_whviM.webp)

*Logcat now automatically detects and retraces R8-processed stack traces*

### **Fused Library Plugin: Publish multiple Android libraries as one**

The new Fused Library plugin bundled with Android Gradle Plugin 9.0 allows you to package multiple Android library modules into a single, publishable Android Library (AAR). **This was one of the most requested features**for Android Gradle Plugin, and we are making it available for you today. This plugin enables you to modularize your code and resources internally while simplifying the integration process for your users by exposing only a single dependency. In addition to streamlining project setup and version management, distributing a fused library can help reduce library size through improved code shrinking and offer better control over your internal implementation details. To learn more about the Fused Library plugin see [Publish multiple Android libraries as one with Fused Library](/build/publish-library/fused-library).

![22.png](/static/blog/assets/22_e004353eb8_LP49X.webp)

### **Get started**

Ready to dive in and accelerate your development? [Download](/studio) Android Studio Otter 3 Feature Drop and start exploring these powerful new features today!

As always, your feedback is crucial to us. [Check known issues](/studio/known-issues), [report bugs](/studio/report-bugs), and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://twitter.com/androidstudio). Let's build the future of Android apps together!

###### Written by:

* ## [Sandhya Mohan](/blog/authors/sandhya-mohan)

  ###### Product Manager

  [read\_more
  View profile](/blog/authors/sandhya-mohan)

  ![](/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)

  ![](/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)
* ## [Trevor Johns](/blog/authors/trevor-johns)

  ###### Staff Developer Programs Engineer

  [read\_more
  View profile](/blog/authors/trevor-johns)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

  ![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

* [![](/static/blog/assets/Sandhya_Mohan_30435468a9_1b689e.webp)](/blog/authors/sandhya-mohan)[![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/trevor-johns)

  04

  Dec
  2025

  04

  Dec
  2025

  ![](/static/blog/assets/as_Otter2_96831eedef_Z19EUHu.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android Studio Otter 2 Feature Drop is stable!](/blog/posts/android-studio-otter-2-feature-drop-is-stable)

  [arrow\_forward](/blog/posts/android-studio-otter-2-feature-drop-is-stable)

  The Android Studio Otter 2 Feature Drop is here to supercharge your productivity.

  ###### [Sandhya Mohan](/blog/authors/sandhya-mohan), [Trevor Johns](/blog/authors/trevor-johns) • 3 min read
* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/trevor-johns)

  02

  Mar
  2026

  02

  Mar
  2026

  ![](/static/blog/assets/supercharge_99f4219536_Z2aoaib.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Supercharge your Android development with 6 expert tips for Gemini in Android Studio](/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio)

  [arrow\_forward](/blog/posts/supercharge-your-android-development-with-6-expert-tips-for-gemini-in-android-studio)

  In January we announced Android Studio Otter 3 Feature Drop in stable, including Agent Mode enhancements and many other updates to provide more control and flexibility over using AI to help you build high quality Android apps.

  ###### [Trevor Johns](/blog/authors/trevor-johns) • 4 min read
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

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)