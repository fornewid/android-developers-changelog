---
title: https://developer.android.com/studio/prompt-gallery/prompts/suggest-missing-permissions
url: https://developer.android.com/studio/prompt-gallery/prompts/suggest-missing-permissions
source: md.txt
---

# Suggest missing permissions

Suggest Android system permissions.

*** ** * ** ***

    Please analyze the following file and let me know what Android system permissions it is likely to need, and which of those are missing.

    Please be succinct in your output.

    Use the following format for each permission identified in this file:

    Permission analysis...
    * {PERMISSION NAME}
    Why: (REASON WHY PERMISSION MAY BE REQUIRED)

    Summary of missing permissions...
    * {PERMISSION NAME}
    * ...

    Additional comments...
    {ADDITIONAL OBSERVATIONS}

    $CURRENT_FILE

| To run this prompt in Android Studio, click**Gemini** in the sidebar and paste it in the chat field.  
| To save and retrieve prompts in the Studio IDE, go to**Settings \> Gemini \> Prompt Library**.

*** ** * ** ***