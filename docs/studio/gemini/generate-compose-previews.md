---
title: https://developer.android.com/studio/gemini/generate-compose-previews
url: https://developer.android.com/studio/gemini/generate-compose-previews
source: md.txt
---

[Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews) are a powerful tool for
visualizing composables at design time in Android Studio, but manually setting
up mock data for the preview parameters can be time-consuming. Gemini in Android
Studio includes a feature that solves this problem: automated Compose preview
generation.

You can access this tool in two ways:

- Within any composable, right-click and navigate to **Gemini \> Generate
  "\<composable\>" Preview** or **Generate Compose Previews for this file**.

  | **Note:** You only see the option to generate Compose previews for the whole file if there are multiple composables in the file that don't have associated previews.

  ![Compose preview generation from context menu](https://developer.android.com/static/studio/gemini/images/compose-preview-menu.png)
- If you don't have any previews set up yet, in the empty preview panel click
  **Auto-generate Compose Previews for this file**.

  ![Compose preview generation from preview panel](https://developer.android.com/static/studio/gemini/images/compose-preview-panel.png)

When you ask Gemini to generate Compose previews, you get a diff view with
Gemini's suggested Compose preview code where you can accept or reject the
proposed changes. Gemini's code should provide a valuable starting point to
accelerate your development workflow.