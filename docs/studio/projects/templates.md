---
title: https://developer.android.com/studio/projects/templates
url: https://developer.android.com/studio/projects/templates
source: md.txt
---

# Add code from a template

Android Studio provides code templates that follow the Android design and development best practices to get you on the right track to creating beautiful, functional apps. You can use templates to create new app modules, individual activities, or other specific Android project components.

Some templates provide starter code for common usage contexts, such as navigation drawers or login screens. You can choose from these app module and activity templates when you first[create your project](https://developer.android.com/studio/projects/create-project), when you[add a new app module within an existing project](https://developer.android.com/studio/projects/add-app-module), or when you add a new activity within an app module.

In addition to activities, you can also add other Android project components to an existing app using templates. These templates include both code components, such as services and fragments, and non-code components, such as folders and XML files.

This page discusses how to add Android project components like activities to your project and describes the commonly used activity templates available in Android Studio. Note that most templates depend on the[Android Support Library](https://developer.android.com/tools/support-library/features)to include user interface principles based on[Material Design](https://developer.android.com/design/material).

## Add a project component

![](https://developer.android.com/static/studio/images/projects/templates-menu.png)

**Figure 1** . The templates menu, accessible through the**File** \>**New** menu or by right-clicking in the**Project**window.

Android Studio groups templates by the type of component that they add, such as an**Activity** or an**XML**file, as shown in figure 1.

To add an Android project component using a template, use the**Project** ![](https://developer.android.com/static/studio/images/buttons/window-project.png)window. Right-click on the folder in which you want to add the new component, and select**New**. Based on what components can be added to the folder you clicked on, you then see a list of template types like those shown in figure 1.

When you select the template you want to add, a corresponding wizard window appears and asks for the component's configuration information, such as its name. After you enter the configuration information, Android Studio creates and opens the files for your new component. It also runs a Gradle build to sync your project.

## Select an activity template

![](https://developer.android.com/static/studio/images/projects/empty-compose-activity-template.png)

**Figure 2**. The Empty Compose Activity template.

One of the most common uses of templates is adding new activities to an existing app module. There are templates for creating screens for logging into an account, presenting a list of items with details, or scrolling through a long block of text.

Android Studio also provides templates for a variety of different app module types, including Wear OS, Android TV, and Cloud App Engine. You can view templates for these different module types when[adding a project component](https://developer.android.com/studio/projects/templates#FindTemplates). Templates also exist for more API-specific modules and activities, such as Google AdMobs Ads and Google Maps.

One of the most commonly used templates is the Empty Compose Activity template, which creates an empty activity with a sample composable and a preview of the composable. It lets you to start from scratch when building your app module or activity.

## Use the Gemini API template

| **Note:** The Gemini API template has been temporarily removed starting in Android Studio Narwhal \| 2025.1.1. To use the template, download a previous version of Android Studio, which still supports the template, from the[Android Studio download archive](https://developer.android.com/studio/archive)as a temporary workaround.

Use the Gemini API template to build an application that implements Generative AI using the[Google AI SDK](http://ai.google.dev/tutorials/android_quickstart?utm_source=android&utm_medium=referral).

### Step 1: Build on the New Project template for AI

Start Android Studio and open a new project using**File \> New Project** . Select the**Gemini API Starter**template.
![](https://developer.android.com/static/studio/images/new-project-templates.png)Choose the Gemini API template on the**New Project**screen.

### Step 2: Generate the API key

In the next step of the wizard, after you choose a project name and location, provide an API key for authentication to the Gemini API. If you don't have a Gemini API key, click the link provided in the wizard to navigate to[Google AI Studio](https://makersuite.google.com/app/apikey)and request a new key. Once completed, copy your new API key back into the wizard. Click**Finish**.
![](https://developer.android.com/static/studio/images/gemini-api-template-project-setup.png)New Project wizard for the Gemini API template.![](https://developer.android.com/static/studio/images/gemini-api-template-api-key.png)Copy and paste the API key into the New Project wizard.

### Step 3: Start prototyping

Android Studio automatically sets up a project for you with a connection to the Gemini API, simplifying your workflow. Click**Run** to see the code in action in the Android Emulator. The app comes with a hard-coded prompt asking the model to "Summarize the following text for me"; you can edit or expand the prompt directly in the code to modify what it can do. You can learn more about creating prompts in the[Google AI Studio documentation](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart).
![](https://developer.android.com/static/studio/images/gemini-api-new-template-details.png)Start prototyping with Gemini APIs.**Important:** Remember, your API key is a secret! Don't share it with anyone, and it is strongly recommended that you don't check in an API key into your version control. The Gemini API Starter template stores the API key in a`local.properties`file (which is located in your project's root directory, but excluded from version control) and uses the[Secrets Gradle plugin](https://github.com/google/secrets-gradle-plugin)for Android to read the API key as a build configuration variable.

### Learn more

Learn more about the Google AI SDK for Android by reviewing the Google AI SDK for Android[quick start guide](http://ai.google.dev/tutorials/android_quickstart?utm_source=android&utm_medium=referral). And for even more code samples, you can import the Generative AI code sample into Android Studio through**File \> New \> Import Sample** and searching for**Generative AI Sample**.
![](https://developer.android.com/static/studio/images/gemini-api-template-samples.png)Import Generative AI Sample Wizard.

Try out Gemini's chat, text, and multi-modal capabilities in the sample app.

<br />

![](https://developer.android.com/static/studio/images/gemini-api-template-sample-app.png)Gemini's chat, text and multi-modal capabilities.c

<br />