---
title: https://developer.android.com/studio/gemini/manage-dependencies
url: https://developer.android.com/studio/gemini/manage-dependencies
source: md.txt
---

Upgrading dependencies can be a complex and time-consuming task. Starting with
Android Studio Panda 2, the AI agent automates and simplifies the dependency
upgrade process, eliminating tedious work and improving project maintainability.
With just a few clicks, you can seamlessly upgrade all your
dependencies and get the benefits of the latest versions, so you can focus on
building high-quality apps.
![Update libraries from the version catalog.](https://developer.android.com/static/studio/gemini/images/update-all-libraries-with-gemini.png) Update libraries from the version catalog.

To update dependencies using the AI agent, do one of the following:

- Click **Refactor** (or right-click in the editor or project view) **\> Update
  dependencies**.
- In the `libs.versions.toml` file, hover over a version that is underlined,
  click the **Show Context Actions**
  ![](https://developer.android.com/static/studio/images/buttons/show-context-actions.png)
  menu that appears, and then click **Update all libraries with Gemini**.

  > [!NOTE]
  > **Note:** You should use the [Android Gradle plugin (AGP) Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant) to upgrade versions of AGP. You can invoke the AGP Upgrade Assistant from the **Show Context Actions** menu for the AGP entry in your `libs.versions.toml` file. We recommend you run the AGP Upgrade Assistant before asking Gemini to update all the other dependencies.

Throughout the process, the agent provides a high-level overview of its upgrade
plan so you can monitor progress step by step and review all changes before
applying them. The agent iterates through the build process, resolving any build
errors that arise from the upgrades. You can review, accept, or roll back
changes, and you can stop the agent at any point.