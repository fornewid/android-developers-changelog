---
title: https://developer.android.com/studio/prompt-gallery/prompts/analyze-compose-layout
url: https://developer.android.com/studio/prompt-gallery/prompts/analyze-compose-layout
source: md.txt
---

# Analyze Compose layout

Suggest improvements to follow Compose layout best practices.

*** ** * ** ***

    Please analyze the Compose layout below and suggest improvements to ensure it is performance and is aligned with best practices.

    Suggest specific optimizations, including but not limited to:


    - State Hoisting: Move state up to the lowest common ancestor that needs access to it. This improves testability and makes components more reusable.
    - Unidirectional Data Flow: Data flows down, events flow up. This makes debugging and reasoning about your UI easier. Use remember to store state, and pass lambdas for events.
    - Immutable Data: Use data classes and Immutable annotations where possible. This helps Compose optimize recompositions.
    - Using 'remember' to cache results, but only for values that should survive recompositions (as this could cause a memory leak)
    - Using the 'key' parameter in lazy layouts to avoid unnecessary recompositions
    - Using 'derivedStateOf' for rapidly changing states
    - Avoiding backwards writes, changing state after it has been in a composable ot prevent recomposition loops
    - Ensuring breaking down UI into smaller composables that do one thing well
    - Proper state management, hoisting state to parent comptables and using lifecycle-aware coroutine scopes like 'viewModelScope' or 'lifecycleScope' for async operations
    - Adhering to Jetpack Compose API guidelines for naming, layering components, and ensuring accessibility
    - Using Baseline Profiles and R8 optimizations
    - Passing a 'Modifier' parameter in composables to allow customization and maintain consistency
    - Not excessively overusing modifiers, resulting in reduced readability and clutter
    - Unnecessary use of WebView inside of Comparables

    Please only tell me where my code can be improved. Do not mention areas where my code is already compliant with best practices.

    Do not write code in your initial response. Instead, ask the developer whether they would like you to attempt to make some of these changes first.

    $CURRENT_FILE


| To run this prompt in Android Studio, click**Gemini** in the sidebar and paste it in the chat field.  
| To save and retrieve prompts in the Studio IDE, go to**Settings \> Gemini \> Prompt Library**.

*** ** * ** ***