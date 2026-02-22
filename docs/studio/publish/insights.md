---
title: https://developer.android.com/studio/publish/insights
url: https://developer.android.com/studio/publish/insights
source: md.txt
---

# Play Policy Insights in Android Studio

| **Note:** Play Policy Insights is only available in the latest stable channel version of Android Studio and major versions (including their patches) released in the previous 10 months. If you are using an older version of Android Studio, you will need to update to access Play Policy Insights. For more information, see[Android Studio and Cloud services compatibility](https://developer.android.com/studio/releases#service-compat).

Android Studio provides richer insights and guidance on Google Play policies that may impact your app. This information helps you build safer apps from the start, preventing issues that could disrupt your launch process and cost more time and resources to fix later on.

You can see Play Policy Insights as lint checks. These lint checks present the following information:

- An overview of the relevant policy.
- Dos and don'ts to avoid common pitfalls.
- Links to Play policy pages where you can find details and more helpful information and resources.

This feature is intended to provide helpful pre-review guidance so you can have smoother app submission experiences. It doesn't cover every policy, nor does it provide final app review decisions. Always review the full policy in the[Policy Center](https://play.google/developer-content-policy/)to ensure compliance.

To see if there are any Play Policy Insights for your project, go to**Code \> Inspect for Play Policy Insights** Insights appear in the**Problems**tool window and also as lint warnings in the corresponding files.
![](https://developer.android.com/static/studio/images/publish/ppi-window.png)

You can run the Play Policy Insights lint checks in your Continuous Integration (CI) builds by adding the latest version of the[com.google.play.policy.insights:insights-lint](https://maven.google.com/web/index.html?q=com.google.play.policy.insights#com.google.play.policy.insights:insights-lint)library to your project dependencies (as a`lintChecks`dependency):  

    lintChecks("com.google.play.policy.insights:insights-lint:LATEST_VERSION")

and[setting up lint](https://developer.android.com/studio/write/lint#commandline)to run as part of your CI builds.

## Understand Play Policy Insights lint checks

Unlike traditional lint checks that often suggest specific code changes or quick fixes, Play Policy Insights lint checks operate differently. Their primary purpose is to make you aware of potential policy issues related to certain permissions or functionalities within the application. The goal is for you to be able to do the following:

- **Understand**the potential policy implications.
- **Make necessary changes**to their app's design or implementation to ensure compliance. Some of the insights may not be fully resolvable in Android Studio and may require actions in the Google Play Console.

These insights are designed to provide early warnings and guide you toward policy-compliant practices from the outset of the development process. Therefore, quick fixes don't exist for Play Policy Insights lint checks in the same way they do for other lint warnings. Instead, these insights should prompt a deeper review of your app's intended behavior and its alignment with Google Play policies.

## Disable Play Policy Insights lint checks

You can disable lint checks for the Play Policy Insights feature by unchecking them in the default inspection profile. To do this, navigate to**File \> Settings \> Editor \> Inspections** (on Windows/Linux) or**Android Studio \> Settings \> Editor \> Inspections** (on macOS). From there, you can disable individual Play Policy Insights checks under**Android \> Lint \> Play Policy**.
![](https://developer.android.com/static/studio/images/publish/ppi-disable.png)**Caution:** Disabling these lint checks means that you won't receive proactive policy guidance within Android Studio, which may increase the risk of encountering policy compliance issues during app submission.

## Feedback

We are continuously working to improve the Play Policy Insights feature. Your feedback is valuable in shaping its future development. If you have any suggestions or encounter any issues, please[report them](https://developer.android.com/studio/report-bugs).