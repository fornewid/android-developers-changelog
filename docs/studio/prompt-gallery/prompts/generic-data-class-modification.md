---
title: https://developer.android.com/studio/prompt-gallery/prompts/generic-data-class-modification
url: https://developer.android.com/studio/prompt-gallery/prompts/generic-data-class-modification
source: md.txt
---

# Generic data class modification and potential database migration

Add a field to a data class.

*** ** * ** ***

    This Kotlin file below defines a data class. I need to add a new field.

    Please prompt me for the name of the new field.

    Then with that information, update the data class, its constructor, and any
    functions in this file that use it to handle the new field, including proper
    null checks if applicable.  If database access is present, generate a migration
    function within this file to add the field to the corresponding table.

    $CURRENT_FILE

| To run this prompt in Android Studio, click**Gemini** in the sidebar and paste it in the chat field.  
| To save and retrieve prompts in the Studio IDE, go to**Settings \> Gemini \> Prompt Library**.

*** ** * ** ***