---
title: https://developer.android.com/agents/skills/system/glance-appwidget-updates-and-memory/references/proguard-rules.pro.rawcontent
url: https://developer.android.com/agents/skills/system/glance-appwidget-updates-and-memory/references/proguard-rules.pro.rawcontent
source: md.txt
---

    -keep class * implements androidx.glance.appwidget.action.ActionCallback {
        public <init>();
    }