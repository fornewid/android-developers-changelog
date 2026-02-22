---
title: https://developer.android.com/studio/gemini/data-and-privacy
url: https://developer.android.com/studio/gemini/data-and-privacy
source: md.txt
---

# Data and privacy

**Gemini in Android Studio is built with your privacy in mind.**

We know that verifying the privacy of your code is critical to earning and maintaining the trust of our developers. Gemini in Android Studio is designed so that your code never leaves your computer without your consent. If you choose to provide code context, Gemini uses that additional context to better answer your questions. You have full control over what data is shared.

At Google, we believe that trust comes from transparency. This page outlines our AI commitments, training philosophy, and technical controls to manage how your data is used.
> **Our assurances**
>
> Gemini is built with Google's[AI Principles](https://ai.google/responsibility/principles/%7B:.external%7D)in mind. These principles describe our commitment to developing AI technology responsibly.
>
> - When you use Gemini in Android Studio, Google handles your data in accordance with our[Privacy Policy](https://policies.google.com/privacy/%7B:.external%7D)and the[Gemini Privacy Notice](https://developer.android.com/studio/gemini/privacy-notice).
> - When you use Gemini in Android Studio for businesses by subscribing to Gemini Code Assist, Google handles your data in accordance with the[Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

## Data collection and use

Your code isn't shared with Gemini without your explicit consent. You have the option to share your code with Gemini in order to enable context awareness features, providing Gemini with the ability to offer project-specific responses.

Here's how your data may be collected and used:

- Your feedback data, such as thumbs up and thumbs down signals, may be used to train Gemini.
- If you're using Gemini in Android Studio for individuals, the code you explicitly enter into the chat experience may be used to train Gemini. If you opt in to context awareness, the information collected---including code--- may be used to improve our products and services, such as machine learning technologies. See our[privacy notice](https://developer.android.com/studio/gemini/privacy-notice)for more details.
- If you're using Gemini in Android Studio for businesses, the code you enter into the chat experience is never used to train Gemini. If you opt in to context awareness, the information collected---including code---is never used to improve our products and services, such as machine learning technologies. See the[Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice)for more details.

If you opt in to use the AI code completion feature, we use context from your codebase to provide higher quality responses.

You can use Gemini with context awareness features disabled, with the trade-off of less accurate features, and some features disabled such as ML powered code completion. Android Studio provides built-in privacy controls to adjust the level of context awareness you want to enable, using**File** (**Android Studio** on macOS) \>**Settings \> Tools \> Gemini** . To block context sharing for certain portions of your codebase, see[Configure context sharing with .aiexclude files](https://developer.android.com/studio/gemini/aiexclude).

The data is stored in a way where Google can't tell who provided it, and it's not possible to delete upon request. The data is retained for up to 18 months. For more information, see the[Gemini Privacy Notice](https://developer.android.com/studio/gemini/privacy-notice).

## Data submitted and received

Here are the different types of data submitted to and received from Gemini:

**Usage statistics**
:   Data specifying how you use Android Studio and its related tools, such as how you use features and resource usage. This includes software identifiers internal to Studio such as package names, class names, and plugin configuration. You can enable or disable this sharing from**File** (**Android Studio** on macOS) \>**Settings** \>**Appearance \& Behavior** \>**Data Sharing**.

**Prompts and responses**
:   The questions that you ask Gemini, including any input information or code that you submit to Gemini to analyze or complete, are called prompts. The answers or code completions that you receive from Gemini are called responses.

**Feedback signals**
:   Thumbs up and down votes and any other feedback that you provide.

**Context (optional)**
:   Gemini might send additional information from your codebase such as pieces of your code, file types, and any other information that might be necessary to provide context to the Large Language Model (LLM). This helps Gemini provide higher quality and relevant responses. This also lets Gemini provide additional experimental capabilities such as AI code completion.

## Developer choice

By default, Gemini can't see the code in the editor window and only uses the prompts and conversation history in the chatbot to respond. However, you can opt in to sharing context from your codebase to enable higher quality responses and access to experimental features such as AI code completion.

There are three mechanisms used to control sharing your project's source code for the purposes of providing context to Gemini:
![Gemini settings in Android Studio, showing the global opt-in preference for context awareness.](https://developer.android.com/static/studio/preview/gemini/images/gemini-settings.png)**Figure 1**: Gemini global settings in Android Studio.

### Global settings

Studio provides a global opt-in preference under**File** (**Android Studio** on macOS) \>**Settings \> Tools \> Gemini**, specifying whether source code may be sent to Gemini servers to provide context awareness.
![The 'Enable Gemini context awareness for this project?' dialog box in Android Studio.](https://developer.android.com/static/studio/gemini/images/project-confirmation.png)**Figure 2**: Project-specific context awareness confirmation dialog.

### Project-specific settings

If**Ask to decide per project** is selected in Studio's Gemini settings, a dialog is displayed the first time each project is opened asking whether context awareness should be enabled for that project. This setting is saved in the project's`.idea`directory.
![A .aiexclude file in a project directory within Android Studio's project view.](https://developer.android.com/static/studio/gemini/images/aiexclude.png)**Figure 3**: Example of an .aiexclude file in a project.

### Source code restrictions with .aiexclude files

Adding an`.aiexclude`file into your project's source code directory provides more granular control over which files are eligible to be used as context for AI models.

[Learn more about the .aiexclude format.](https://developer.android.com/studio/gemini/aiexclude)