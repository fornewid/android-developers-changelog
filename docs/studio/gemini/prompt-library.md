---
title: https://developer.android.com/studio/gemini/prompt-library
url: https://developer.android.com/studio/gemini/prompt-library
source: md.txt
---

# Save and manage prompts with the Prompt Library

Use the Prompt Library to save and manage your frequently used prompts and quickly recall them when needed. If there's a prompt that you use often for different files or different sections of code, you can use a prompt template variable that is automatically replaced with the selected code or file during prompt execution. This streamlined workflow eliminates the need to retype commonly used prompts, saving you time and effort.
![The Prompt Library in Android Studio, showing a list of saved prompts.](https://developer.android.com/static/studio/gemini/images/gemini-prompt-library.png)Figure 1: The Prompt Library in Android Studio.

To open the Prompt Library, go to**File** (**Android Studio** on macOS)**\> Settings \> Tools \> Gemini \> Prompt Library**.

## Save a prompt

To add a prompt, follow these steps:

1. Open the Prompt Library by clicking**File** (**Android Studio** on macOS)**\> Settings \> Tools \> Gemini \> Prompt Library**.
2. Set the scope of the prompt using the**Scope** drop-down:
   - IDE-level rules are private to yourself and can be used across multiple projects.
   - Project-level rules can be[shared among teammates](https://developer.android.com/studio/gemini/prompt-library#share-project-prompts)working on the same project.
3. Add a new prompt by clicking**Add** ![](https://developer.android.com/static/studio/gemini/images/prompt-library-add.png).
4. Give the prompt a name. This name is what appears in the[Prompt Library menu](https://developer.android.com/studio/gemini/prompt-library#use-saved-prompt)if you want to apply the prompt from the editor.
5. Enter the prompt in the field provided. If the prompt involves referencing specific code, you can add the relevant code during prompt execution by using the following variables in your prompt:
   - `$SELECTION`- Represents the selected text, or text surrounding the cursor if no text is selected.
   - `$CURRENT_FILE`- Represents all the text in the file that's active in the editor.
6. Optional: Clear the**Show in Prompt Library menu** checkbox if you don't want the prompt to appear in the[Prompt Library menu](https://developer.android.com/studio/gemini/prompt-library#use-saved-prompt).
7. Click the**Apply** button to save changes and continue configuring settings. To save changes and exit the settings dialog immediately, click the**OK**button.

You can also right-click on a prompt in chat to save it for later use. To apply a saved prompt, right-click in the Editor and navigate to**Gemini \> Prompt Library**to apply the prompt.
![The 'Add to Prompt Library' context menu in Android Studio.](https://developer.android.com/static/studio/gemini/images/add-to-prompt-library.png)Figure 2: Save a prompt from the editor.

## Use a saved prompt

To use a prompt from the Prompt Library, follow these steps:

1. Highlight the relevant code, if applicable to the prompt that you're planning to use. If the prompt doesn't reference specific code, it doesn't matter where your cursor is in the file.
2. To get your list of prompts, right-click in the editor and go to**Gemini \> Prompt Library**.
3. To submit the prompt to Gemini, select the prompt from the menu.

## Share and manage project-level prompts

You can share and manage project-level prompts with teammates working on the same project. When you save a prompt at the project level in the Prompt Library, the prompt is stored at`<project-root>/.idea/project.prompts.xml`. To share and manage project-level prompts, add the`.idea`folder to your version control system.