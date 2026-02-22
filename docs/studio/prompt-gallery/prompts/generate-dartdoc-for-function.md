---
title: https://developer.android.com/studio/prompt-gallery/prompts/generate-dartdoc-for-function
url: https://developer.android.com/studio/prompt-gallery/prompts/generate-dartdoc-for-function
source: md.txt
---

# Generate DartDoc for Function

Generates a DartDoc comment describing the properties of the selected function.

*** ** * ** ***

    Create a DartDoc comment that could describe this function in the current file:

    $SELECTION

    The comment should consist of a single sentence describing what the function does, followed by a line of whitespace, and then zero or more additional sentences.
    If the function takes parameters, include a sentence to describe them.
    Do not include a sentence for parameters if there are no parameters.
    If the function has a return type other than void, include a sentence describing what kind of value is returned and why.
    If the function has side effects, include a sentence describing them.

    Use a line length of 80 characters.

| To run this prompt in Android Studio, click**Gemini** in the sidebar and paste it in the chat field.  
| To save and retrieve prompts in the Studio IDE, go to**Settings \> Gemini \> Prompt Library**.

*** ** * ** ***