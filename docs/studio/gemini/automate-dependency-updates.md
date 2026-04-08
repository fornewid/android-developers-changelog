---
title: Automate dependency updates  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/automate-dependency-updates
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Automate dependency updates Stay organized with collections Save and categorize content based on your preferences.




Upgrading dependencies can be a complex and time-consuming task.

Android apps rely on various external library dependencies for things like
networking, image loading, and UI components. These libraries are constantly
evolving, with new versions offering bug fixes, performance improvements, and
new features.

Gemini in Android Studio automates and simplifies the dependency update
process, eliminating tedious work and improving project maintainability.

## How Gemini in Android Studio helps you

Agent mode reliably automates dependency management to keep your project
current, allowing you to focus on building high-quality apps. With a single
click, you can seamlessly update all your dependencies and get the benefits of
the latest versions.

## How the update works

Gemini in Android Studio intelligently handles the update process as follows:

* **Identifies and updates dependencies**: Automatically identifies
  dependencies that can be updated and updates them to the latest compatible
  version.
* **Resolves build errors**: Iterates through the build process, resolving any
  build errors that arise from the updates.
* **Validates the project**: Runs tests to validate that the updated project
  still functions as expected.
* **Generates an update report**: After the process is complete, Gemini in
  Android Studio provides a detailed report of all the changes. You can review
  these changes at a high level or drill down to individual file-level diffs
  before accepting them.

You start the update process from the **Refactor** menu by selecting **Update
Dependencies**:

![The Refactor menu, showing the Update Dependencies menu item.](/static/studio/gemini/images/refactor_menu.png)


**Figure 1.** Select **Update Dependencies** from the
**Refactor** menu.

or, from the `libs.versions.toml` file: hover over a version that is underlined,
click the **Show Context Actions**
![](/static/studio/images/buttons/show-context-actions.png)
menu that appears, and then click **Update all libraries with Gemini**.

![Update libraries from the version catalog.](/static/studio/gemini/images/update-all-libraries-with-gemini.png)


**Figure 2.** Update libraries from the version catalog.

**Note:** Use the [Android Gradle plugin (AGP) Upgrade Assistant](/build/agp-upgrade-assistant) to upgrade
versions of AGP. You can invoke the AGP Upgrade Assistant from the **Show
Context Actions** menu for the AGP entry in your `libs.versions.toml` file. Run
the AGP Upgrade Assistant before asking Gemini to update all the other
dependencies.

Whichever way you start the process, Gemini in Android Studio provides a
high-level overview of its update plan so you can adjust the plan, monitor
progress step by step, and review all changes before applying them:

![A checklist of the libraries Gemini in Android Studio has
         proposed to update. You can uncheck items to remove them from the update.](/static/studio/gemini/images/refactor_checklist.png)


**Figure 3.** Review, modify, approve, or cancel Gemini's plan.

You can review, accept, or roll back changes, or stop the process at any point.

## Additional resources

* [Upgrade dependency versions](/build/version-upgrade-strategies)