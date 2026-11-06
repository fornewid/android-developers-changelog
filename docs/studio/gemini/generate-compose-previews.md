---
title: https://developer.android.com/studio/gemini/generate-compose-previews
url: https://developer.android.com/studio/gemini/generate-compose-previews
source: md.txt
---

[Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews) are a powerful tool for
visualizing composables at design time in Android Studio, but manually setting
up mock data for the preview parameters can be time-consuming. AI in Android
Studio includes a feature that solves this problem: automated Compose preview
generation.

You can access this tool in two ways:

- Within any composable, right-click and navigate to **AI \> Generate Compose
  Preview for "\<composable\>"** ; or, select **Generate Preview for Composable**
  and then select a composable.

  ![Compose preview generation from context menu](https://developer.android.com/static/studio/gemini/images/generate-compose-preview-menu.png)

When you ask the agent to generate Compose previews, you get a diff view with
the agent's suggested Compose preview code where you can accept or reject the
proposed changes. The agent's code should provide a valuable starting point to
accelerate your development workflow.