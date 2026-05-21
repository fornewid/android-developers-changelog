---
title: https://developer.android.com/blog/posts/android-cli-now-stable-1-accelerate-developing-for-android-using-any-agent
url: https://developer.android.com/blog/posts/android-cli-now-stable-1-accelerate-developing-for-android-using-any-agent
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android CLI Now Stable 1.0: Accelerate developing for Android using any agent

###### 5-min read

![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp) 19 May 2026 [![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp)](https://developer.android.com/blog/authors/simona-milanovic)[![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)](https://developer.android.com/blog/authors/ben-trengrove)

##### [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic)
\&
[Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove)

As Android developers, you have many choices when it comes to the agents, tools, command-line interfaces (CLI), and LLMs you use for app development. Whether you use Gemini in Android Studio, Antigravity 2.0, Antigravity CLI, or third-party agents like Anthropic's Claude Code or OpenAI'sCodex, our mission remains the same: to ensure that high-quality Android development is possible everywhere.
[Video](https://www.youtube.com/watch?v=aqmpZocmR8o)

At **Google I/O '26** , we shared the latest leaps forward in agentic development, and showcased some of the newest capabilities of [Android CLI](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#)---now stable at version 1.0 and ready for all Android developers to use. From new skills to enabling agent access to powerful Android Studio capabilities, we're giving your agents the right tools to build alongside you.

If you're already using Android CLI and want to jump into using all the new features, just run `android update`. Otherwise, read further to learn more about how we're making the agents you choose be better at building for Android.

### Android development unlocked for Antigravity

[Google Antigravity](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#) now includes an optional bundle of Android resources---including the Android CLI and skills---that you can install. You can either install the bundle during onboarding after installation, or later from the **Settings \> Customizations \> Build With Google Plugins** menu.

This provides Antigravity with all the powerful tools and knowledge of Android CLI, enabling it to perform the core tasks necessary for Android app development more easily and efficiently---from creating projects to deploying your app on a new Android virtual device.
![agy-android-cli.png](https://developer.android.com/static/blog/assets/agy_android_cli_668b5f6f18_Z2niFn9.webp)

### Unlocking Android Studio capabilities for any agent

Android CLI provides a lightweight interface for AI Agents to perform tasks and retrieve knowledge about Android development. However, there's benefits to specialization --- Android Studio contains over a decade of Android expertise, built to handle even the most complex Android projects. This includes Android Studio's powerful static analysis engine, refactoring tools, dependency management, UI design and rendering libraries, and more. AI Agents can now tap into Android Studio's tools to gain many of these same capabilities.
![agy-android-studio.png](https://developer.android.com/static/blog/assets/agy_android_studio_a1414d1291_187NUY.webp)

The latest version of Android CLI introduces the new `android studio` command. This enables the agent of your choice to leverage the deep, contextual capabilities of Android Studio to better understand and perform actions on an open Android project. By running Android Studio alongside your preferred agent with Android CLI, your agent's tasks can more efficiently navigate the codebase to produce more precise code changes. And, when you use Android CLI to create and iterate on your project, transitioning to Android Studio is much easier, so that you can use the purpose built tools---such as, performance profilers, Compose Previews, and Android Device Streaming---to get that production-grade polish.

When you have a project open in the latest [preview version](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#) of Android Studio Quail, you (or your agent) can run the following command to check whether Android CLI has a connection established with your open project:

```
$ android studio check
pid: 32942
version: Android Studio
Projects:
    READY     JetSet /Users/adarshf/AndroidStudioProjects/jetset-main
```

From there, the agents can use the `android studio` command to access powerful IDE tools to interact with projects more efficiently. Key commands include:

- **analyze-file:** Analyzes a file for errors and warnings using the editor's built-in inspections.
- **find-declaration:** Finds the exact definition site of a symbol (class, method, variable, field, constant, or Android resource/color) across the project using semantic resolution.
- **find-usages:**Finds all references and declarations of a symbol (class, method, variable, or Android resource) across the entire project using semantic analysis.
- **render-compose-preview:**Renders a Jetpack Compose UI Preview and returns a path to the image and UI hierarchy if successful.
- **version-lookup:** Get the latest information about which versions for specified app dependencies are available in common repositories, such as the Google Maven repository. By providing a programmatic solution, dependency management is less tedious and much less prone to flakiness.
- **open-file:**Opens a file directly in Android Studio. This is useful if the agent wants to direct your attention to view Compose Previews, performance traces, or other specific files in the IDE.

For example, agents can now run the following commands to render a Compose preview for a new layout for your Android app, and then open the previews in Android Studio for you to take advantage of seeing multiple Compose Previews side by side and make AI-assisted edits right from the IDE.

```
$ android studio find-declaration HotelDetailScreen
$ android studio analyze-file .../JetPacker/feature/detail/src/main/java/com/example/jetset/feature/detail/HotelDetailScreen.kt
$ android studio open-file feature/detail/src/main/java/com/example/jetset/feature/detail/HotelDetailScreen.kt
```

To learn more about how to use these commands, run `android help`. And, to make sure your agents understand how to work with this tool, make sure to update the Android CLI skill by running `android init`.

### More ways to get started

To make integrating Android CLI into your environments as seamless as possible, we're making it available in more ways. You can now download and install Android CLI using more package managers: apt-get, winget, and homebrew. For example, you can run the following to install Android CLI using winget:

```
winget install -e --id Google.AndroidCLI
```

We've also updated the installation to a user-local directory, by default. You can find the commands for all supported operating systems plus additional download options on the [Android CLI page](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#).

### Support for Journeys

![android-cli-write-journey.png](https://developer.android.com/static/blog/assets/android_cli_write_journey_3dd0275369_1euJck.webp)

We are also introducing support for [Journeys](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#). With Journeys tools and skills included with Android CLI, any agent of your choice can now create and run Journeys---which are natural language descriptions of user journeys for your app that are saved directly to your project.
![android-cli-journey-run.gif](https://developer.android.com/static/blog/assets/android_cli_journey_run_ff5ebd47bc_Z1N8cuX.webp)

Agents can run these journeys using the Android CLI to navigate your app exactly like a user would. This unlocks entirely new ways to test, validate, or collect data across the critical experiences of your app, all driven by natural language and executed by your agent.

### Expanding Android skills

To help models better understand and execute specific patterns that follow our best practices, we are continuing to expand our [library of Android skills](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#). We're shipping new skills that make Android development everywhere more capable, efficient, and productive:

- **Display Glasses and Jetpack Compose Glimmer for XR:**Provides guidelines for developing projected applications for Android Display Glasses using the Jetpack Compose Glimmer UI toolkit.
- **Migration to CameraX:** Helps you migrate legacy Android camera implementations (Camera1 or raw Camera2 APIs) to CameraX.
- **Perfetto SQL:** Translates natural language data prompts into Perfetto SQL queries and executes them against a local trace file.
- **Adaptive UI:** Instructions to make or update an app's UI so that it adapts to different Android devices
- **Testing setup:**Creates a basic testing strategy.
- **Styles:** Helps with adoption of the new Jetpack Compose Style API for new components, and supports migration to Styles API.
- **AppFunctions:**Analyzes Android codebases to recommend and implement new AppFunctions, and refines KDoc documentation for Model Context Protocol optimization.

You can add these new skills to your workflow directly from the command line. To help your agents understand and use Android CLI right away, you can initialize your environment and install the base android-cli skill by running:

`android init`  

From there, you can browse and set up your agent workflow by searching for the exact capabilities your agent needs:

`android skills list`

Once you've found the right skill, install it to your environment by running:

`android skills add --skill=`

### Get started today

To download the stable 1.0 release of the Android CLI, explore the new tools, and browse the complete documentation, head over to [d.android.com/tools/agents](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#) today! Also, make sure you update to the [latest preview version of Android Studio](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#) to unlock the latest features that Android CLI offers. We can't wait to see what you build with Android CLI 1.0 and how these new features supercharge your daily workflows. Join our vibrant community on [LinkedIn](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#), [Medium](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#), [YouTube](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#), or [X](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#) and share your feedback.

Explore this announcement and all Google I/O 2026 updates on [io.google.](https://draft.blogger.com/u/0/blog/post/edit/6755709643044947179/7947913907519760349#)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)

###### Written by:

-

  ## [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/simona-milanovic) ![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp) ![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp)
-

  ## [Ben Trengrove](https://developer.android.com/blog/authors/ben-trengrove)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-trengrove) ![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp) ![](https://developer.android.com/static/blog/assets/Ben_Trengrove_b9e17c8c2e_2uVqlp.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/IO_26_Blog_Strapi_Icons_2000x1000px_0a8b06b49b_Z1e2APA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [I/O 2026: What's new in Google Play](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play) At this year's Google I/O, we talked about our evolving business model that offers more choice and new ways for your apps and content to be discovered on and off the store. We also unveiled advanced tools and insights that will help scale your business with less complexity.

  ###### [Paul Feng](https://developer.android.com/blog/authors/paul-feng) •
  6 min read

  - [#Google Play](https://developer.android.com/blog/topics/google-play)
  - [#Play Console](https://developer.android.com/blog/topics/play-console)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android Developers](https://developer.android.com/blog/topics/android-developers)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)