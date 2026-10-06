---
title: Android Developers
url: https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent
source: html-scrape
---

Stay organized with collections

Save and categorize content based on your preferences.





```
package com.example.platform.ui.appwidgets.glance.layout.utils

import androidx.compose.runtime.Composable
import androidx.glance.action.Action
import androidx.glance.action.actionParametersOf
import androidx.glance.action.actionStartActivity
import com.example.platform.ui.appwidgets.glance.layout.ActionDemonstrationActivity
import com.example.platform.ui.appwidgets.glance.layout.ActionSourceMessageKey

/**
 * Utility functions for creating [Action]s.
 */
object ActionUtils {
  /**
   * [Action] for launching the [ActionDemonstrationActivity] with the given message.
   */
  @Composable
  fun actionStartDemoActivity(message: String) =
    actionStartActivity<ActionDemonstrationActivity>(
      actionParametersOf(
        ActionSourceMessageKey to message
      )
    )
}
```