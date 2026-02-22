---
title: https://developer.android.com/studio/intro/keyboard-shortcuts
url: https://developer.android.com/studio/intro/keyboard-shortcuts
source: md.txt
---

# Keyboard shortcuts are a useful way of quickly navigating around Android Studio and performing common actions. In many cases, using keyboard shortcuts is faster than using the GUI.

This page shows some common keyboard shortcuts. Since Android Studio is based on IntelliJ IDEA, you can find additional shortcuts in the[IntelliJ IDEA keymap reference documentation](https://resources.jetbrains.com/storage/products/intellij-idea/docs/IntelliJIDEA_ReferenceCard.pdf).

## Tool windows

You can use keyboard shortcuts to open tool windows. Table 1 lists the shortcuts for the most common windows.

**Table 1.**Keyboard shortcuts for common tool windows

|      Tool window      |      Windows and Linux       |            macOS             |
|-----------------------|------------------------------|------------------------------|
| Project               | <kbd>Alt+1</kbd>             | <kbd>Command+1</kbd>         |
| Version Control       | <kbd>Alt+9</kbd>             | <kbd>Command+9</kbd>         |
| Run                   | <kbd>Shift+F10</kbd>         | <kbd>Control+R</kbd>         |
| Debug                 | <kbd>Shift+F9</kbd>          | <kbd>Control+D</kbd>         |
| Logcat                | <kbd>Alt+6</kbd>             | <kbd>Command+6</kbd>         |
| Return to Editor      | <kbd>Esc</kbd>               | <kbd>Esc</kbd>               |
| Hide All Tool Windows | <kbd>Control+Shift+F12</kbd> | <kbd>Command+Shift+F12</kbd> |

## Code completion

Android Studio has three types of code completion, which you can access using keyboard shortcuts, as shown in the following table.

**Table 2.**Keyboard shortcuts for code completion

|         Type         |                                                                                                   Description                                                                                                   |       Windows and Linux        |             macOS              |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Basic Completion     | Displays basic suggestions for variables, types, methods, expressions, and so on. If you call basic completion twice in a row, you see more results, including private members and non-imported static members. | <kbd>Control+Space</kbd>       | <kbd>Control+Space</kbd>       |
| Smart Completion     | Displays relevant options based on the context. Smart completion takes into account the expected type and data flows. If you call Smart Completion twice in a row, you see more results, including chains.      | <kbd>Control+Shift+Space</kbd> | <kbd>Control+Shift+Space</kbd> |
| Statement Completion | Completes the current statement, adding missing parentheses, brackets, braces, formatting, and so on.                                                                                                           | <kbd>Control+Shift+Enter</kbd> | <kbd>Command+Shift+Enter</kbd> |

To perform quick fixes and show[intention actions](https://www.jetbrains.com/help/idea/intention-actions.html), press<kbd>Alt+Enter</kbd>.

## Navigation

Use the following tips to help navigate around Android Studio:

- Switch between your recently accessed files using the**Recent Files** action. To bring up the**Recent Files** action, press<kbd>Control+E</kbd>(<kbd>Command+E</kbd>on macOS). By default, the last accessed file is selected. You can also access any tool window through the left column in this action.
- View the structure of the current file using the**File Structure** action. To bring up the**File Structure** action, press<kbd>Control+F12</kbd>(<kbd>Command+F12</kbd>on macOS). Using this action, you can quickly navigate to any part of your current file.
- Search for and navigate to a specific class in your project using the**Navigate to Class** action. To bring up the**Navigate to Class** action, press<kbd>Control+N</kbd>(<kbd>Command+O</kbd>on macOS).

  **Navigate to Class** supports sophisticated expressions, including*camel humps* (which lets you search by the capitalized letters in an element's camel-cased name), paths,*line navigate to* (which lets you navigate to a specific line within the file), and*middle name matching*(which lets you search for a part of the class name). If you call it twice in a row, it shows you the results out of the project classes.
- Navigate to a file or folder using the**Navigate to File** action. To bring up the**Navigate to File** , press<kbd>Control+Shift+N</kbd>(<kbd>Command+Shift+O</kbd>on macOS). To search for folders rather than files, add a`/`at the end of your expression.

- Navigate to a method or field by name using the**Navigate to Symbol** action. To bring up the**Navigate to Symbol** action, press<kbd>Control+Alt+Shift+N</kbd>(<kbd>Command+Option+O</kbd>on macOS).

- To find all the pieces of code referencing the class, method, field, parameter, or statement at the current cursor position, press<kbd>Alt+F7</kbd>(<kbd>Option+F7</kbd>on macOS).

## Default keymaps

Android Studio includes keyboard shortcuts for many common actions. Table 3 shows the default keyboard shortcuts by operating system.

**Note:** In addition to the default keymaps in table 3, you can select from a number of preset keymaps or create a custom keymap. For more about customizing your keyboard shortcuts, see the[Configure custom keymaps](https://developer.android.com/studio/intro/keyboard-shortcuts#custom)section.

**Table 3.**Default keyboard shortcuts for Windows or Linux and macOS operating systems

|                                            Description                                             |                       Windows and Linux                       |                             macOS                             |
|                                                                                                         General actions                                                                                                          |||
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Save all                                                                                           | <kbd>Control+S</kbd>                                          | <kbd>Command+S</kbd>                                          |
| Synchronize                                                                                        | <kbd>Control+Alt+Y</kbd>                                      | <kbd>Command+Option+Y</kbd>                                   |
| Maximize/minimize editor                                                                           | <kbd>Control+Shift+F12</kbd>                                  | <kbd>Control+Command+F12</kbd>                                |
| Add to favorites                                                                                   | <kbd>Alt+Shift+F</kbd>                                        | <kbd>Option+Shift+F</kbd>                                     |
| Inspect current file with current profile                                                          | <kbd>Alt+Shift+I</kbd>                                        | <kbd>Option+Shift+I</kbd>                                     |
| Quick switch scheme                                                                                | <kbd>Control+`</kbd>(backtick)                                | <kbd>Control+`</kbd>(backtick)                                |
| Open settings dialog                                                                               | <kbd>Control+Alt+S</kbd>                                      | <kbd>Command+,</kbd>(comma)                                   |
| Open project structure dialog                                                                      | <kbd>Control+Alt+Shift+S</kbd>                                | <kbd>Command+;</kbd>(semicolon)                               |
| Switch between tabs and tool window                                                                | <kbd>Control+Tab</kbd>                                        | <kbd>Control+Tab</kbd>                                        |
| Search everything (including code and menus)                                                       | Press<kbd>Shift</kbd>twice                                    | Press<kbd>Shift</kbd>twice                                    |
| Find                                                                                               | <kbd>Control+F</kbd>                                          | <kbd>Command+F</kbd>                                          |
| Find next                                                                                          | <kbd>F3</kbd>                                                 | <kbd>Command+G</kbd>                                          |
| Find previous                                                                                      | <kbd>Shift+F3</kbd>                                           | <kbd>Command+Shift+G</kbd>                                    |
| Replace                                                                                            | <kbd>Control+R</kbd>                                          | <kbd>Command+R</kbd>                                          |
| Find action                                                                                        | <kbd>Control+Shift+A</kbd>                                    | <kbd>Command+Shift+A</kbd>                                    |
| Search by symbol name                                                                              | <kbd>Control+Alt+Shift+N</kbd>                                | <kbd>Command+Option+O</kbd>                                   |
| Find class                                                                                         | <kbd>Control+N</kbd>                                          | <kbd>Command+O</kbd>                                          |
| Find file (instead of class)                                                                       | <kbd>Control+Shift+N</kbd>                                    | <kbd>Command+Shift+O</kbd>                                    |
| Find in path                                                                                       | <kbd>Control+Shift+F</kbd>                                    | <kbd>Command+Shift+F</kbd>                                    |
| Open file structure dialog                                                                         | <kbd>Control+F12</kbd>                                        | <kbd>Command+F12</kbd>                                        |
| Navigate between open editor tabs                                                                  | <kbd>Alt+Right Arrow</kbd>or<kbd>Left Arrow</kbd>             | <kbd>Control+Right Arrow</kbd>or<kbd>Control+Left Arrow</kbd> |
| Jump to source                                                                                     | <kbd>F4</kbd>or<kbd>Control+Enter</kbd>                       | <kbd>F4</kbd>or<kbd>Command+Down Arrow</kbd>                  |
| Open current editor tab in new window                                                              | <kbd>Shift+F4</kbd>                                           | <kbd>Shift+F4</kbd>                                           |
| Recently opened files dialog                                                                       | <kbd>Control+E</kbd>                                          | <kbd>Command+E</kbd>                                          |
| Recently edited files dialog                                                                       | <kbd>Control+Shift+E</kbd>                                    | <kbd>Command+Shift+E</kbd>                                    |
| Go to last edit location                                                                           | <kbd>Control+Shift+Backspace</kbd>                            | <kbd>Command+Shift+Delete</kbd>                               |
| Close active editor tab                                                                            | <kbd>Control+F4</kbd>                                         | <kbd>Command+W</kbd>                                          |
| Return to editor window from a tool window                                                         | <kbd>Esc</kbd>                                                | <kbd>Esc</kbd>                                                |
| Hide active or last active tool window                                                             | <kbd>Shift+Esc</kbd>                                          | <kbd>Shift+Esc</kbd>                                          |
| Go to line                                                                                         | <kbd>Control+G</kbd>                                          | <kbd>Command+L</kbd>                                          |
| Open type hierarchy                                                                                | <kbd>Control+H</kbd>                                          | <kbd>Control+H</kbd>                                          |
| Open method hierarchy                                                                              | <kbd>Control+Shift+H</kbd>                                    | <kbd>Command+Shift+H</kbd>                                    |
| Open call hierarchy                                                                                | <kbd>Control+Alt+H</kbd>                                      | <kbd>Control+Option+H</kbd>                                   |
| Zoom in/out                                                                                        | <kbd>Control+plus</kbd>or<kbd>Control+minus</kbd>             | <kbd>Command+plus</kbd>or<kbd>Command+minus</kbd>             |
| Fit to screen                                                                                      | <kbd>Control+0</kbd>                                          | <kbd>Command+0</kbd>                                          |
| Actual size                                                                                        | <kbd>Control+Shift+1</kbd>                                    | <kbd>Command+Shift+1</kbd>                                    |
| Toggle between Design and Blueprint modes                                                          | <kbd>B</kbd>                                                  | <kbd>B</kbd>                                                  |
| Toggle between Portrait and Landscape modes                                                        | <kbd>O</kbd>                                                  | <kbd>O</kbd>                                                  |
| Toggle devices                                                                                     | <kbd>D</kbd>                                                  | <kbd>D</kbd>                                                  |
| Force refresh                                                                                      | <kbd>R</kbd>                                                  | <kbd>R</kbd>                                                  |
| Toggle render errors panel                                                                         | <kbd>E</kbd>                                                  | <kbd>E</kbd>                                                  |
| Delete constraints                                                                                 | <kbd>Delete</kbd>or<kbd>Control</kbd>+click                   | <kbd>Delete</kbd>or<kbd>Command</kbd>+click                   |
| Zoom in                                                                                            | <kbd>Control+plus</kbd>                                       | <kbd>Command+plus</kbd>                                       |
| Zoom out                                                                                           | <kbd>Control+minus</kbd>                                      | <kbd>Command+minus</kbd>                                      |
| Zoom to fit                                                                                        | <kbd>Control+0</kbd>                                          | <kbd>Command+0</kbd>                                          |
| Pan                                                                                                | Hold<kbd>Space</kbd>+click and drag                           | Hold<kbd>Space</kbd>+click and drag                           |
| Go to XML                                                                                          | <kbd>Control+B</kbd>                                          | <kbd>Command+B</kbd>                                          |
| Select all components                                                                              | <kbd>Control+A</kbd>                                          | <kbd>Command+A</kbd>                                          |
| Select multiple components                                                                         | <kbd>Shift</kbd>+click or<kbd>Control</kbd>+click             | <kbd>Shift</kbd>+click or<kbd>Command</kbd>+click             |
| Zoom in                                                                                            | <kbd>Control+plus</kbd>                                       | <kbd>Command+plus</kbd>                                       |
| Zoom out                                                                                           | <kbd>Control+minus</kbd>                                      | <kbd>Command+minus</kbd>                                      |
| Zoom to fit                                                                                        | <kbd>Control+0</kbd>                                          | <kbd>Command+0</kbd>                                          |
| Pan                                                                                                | Hold<kbd>Space</kbd>+click and drag                           | Hold<kbd>Space</kbd>+click and drag                           |
| Go to XML                                                                                          | <kbd>Control+B</kbd>                                          | <kbd>Command+B</kbd>                                          |
| Toggle render errors panel                                                                         | <kbd>E</kbd>                                                  | <kbd>E</kbd>                                                  |
| Group into nested graph                                                                            | <kbd>Control+G</kbd>                                          | <kbd>Command+G</kbd>                                          |
| Cycle through destinations                                                                         | <kbd>Tab</kbd>or<kbd>Shift+Tab</kbd>                          | <kbd>Tab</kbd>or<kbd>Shift+Tab</kbd>                          |
| Select all destinations                                                                            | <kbd>Control+A</kbd>                                          | <kbd>Command+A</kbd>                                          |
| Select multiple destinations                                                                       | <kbd>Shift</kbd>+click or<kbd>Control</kbd>+click             | <kbd>Shift</kbd>+click or<kbd>Command</kbd>+click             |
| Generate code (getters, setters, constructors,`hashCode`/`equals`,`toString`, new file, new class) | <kbd>Alt+Insert</kbd>                                         | <kbd>Command+N</kbd>                                          |
| Override methods                                                                                   | <kbd>Control+O</kbd>                                          | <kbd>Control+O</kbd>                                          |
| Implement methods                                                                                  | <kbd>Control+I</kbd>                                          | <kbd>Control+I</kbd>                                          |
| Surround with (`if...else`,`try...catch`, etc.)                                                    | <kbd>Control+Alt+T</kbd>                                      | <kbd>Command+Option+T</kbd>                                   |
| Delete line at caret                                                                               | <kbd>Control+Y</kbd>                                          | <kbd>Command+Delete</kbd>                                     |
| Collapse/expand current code block                                                                 | <kbd>Control+minus</kbd>or<kbd>Control+plus</kbd>             | <kbd>Command+minus</kbd>or<kbd>Command+plus</kbd>             |
| Collapse/expand all code blocks                                                                    | <kbd>Control+Shift+minus</kbd>or<kbd>Control+Shift+plus</kbd> | <kbd>Command+Shift+minus</kbd>or<kbd>Command+Shift+plus</kbd> |
| Duplicate current line or selection                                                                | <kbd>Control+D</kbd>                                          | <kbd>Command+D</kbd>                                          |
| Basic code completion                                                                              | <kbd>Control+Space</kbd>                                      | <kbd>Control+Space</kbd>                                      |
| Smart code completion (filters the list of methods and variables by expected type)                 | <kbd>Control+Shift+Space</kbd>                                | <kbd>Control+Shift+Space</kbd>                                |
| Complete statement                                                                                 | <kbd>Control+Shift+Enter</kbd>                                | <kbd>Command+Shift+Enter</kbd>                                |
| Quick documentation lookup                                                                         | <kbd>Control+Q</kbd>                                          | <kbd>Control+J</kbd>                                          |
| Show parameters for selected method                                                                | <kbd>Control+P</kbd>                                          | <kbd>Command+P</kbd>                                          |
| Go to declaration (directly)                                                                       | <kbd>Control+B</kbd>or<kbd>Control</kbd>+click                | <kbd>Command+B</kbd>or<kbd>Command</kbd>+click                |
| Go to implementations                                                                              | <kbd>Control+Alt+B</kbd>                                      | <kbd>Command+Option+B</kbd>                                   |
| Go to supermethod/superclass                                                                       | <kbd>Control+U</kbd>                                          | <kbd>Command+U</kbd>                                          |
| Open quick definition lookup                                                                       | <kbd>Control+Shift+I</kbd>                                    | <kbd>Command+Y</kbd>                                          |
| Toggle project tool window visibility                                                              | <kbd>Alt+1</kbd>                                              | <kbd>Command+1</kbd>                                          |
| Toggle bookmark                                                                                    | <kbd>F11</kbd>                                                | <kbd>F3</kbd>                                                 |
| Toggle bookmark with mnemonic                                                                      | <kbd>Control+F11</kbd>                                        | <kbd>Option+F3</kbd>                                          |
| Comment/uncomment with line comment                                                                | <kbd>Control+/</kbd>                                          | <kbd>Command+/</kbd>                                          |
| Comment/uncomment with block comment                                                               | <kbd>Control+Shift+/</kbd>                                    | <kbd>Command+Shift+/</kbd>                                    |
| Select successively increasing code blocks                                                         | <kbd>Control+W</kbd>                                          | <kbd>Option+Up</kbd>                                          |
| Decrease current selection to previous state                                                       | <kbd>Control+Shift+W</kbd>                                    | <kbd>Option+Down</kbd>                                        |
| Move to code block start                                                                           | <kbd>Control+[</kbd>                                          | <kbd>Option+Command+[</kbd>                                   |
| Move to code block end                                                                             | <kbd>Control+]</kbd>                                          | <kbd>Option+Command+]</kbd>                                   |
| Select to the code block start                                                                     | <kbd>Control+Shift+[</kbd>                                    | <kbd>Option+Command+Shift+[</kbd>                             |
| Select to the code block end                                                                       | <kbd>Control+Shift+]</kbd>                                    | <kbd>Option+Command+Shift+]</kbd>                             |
| Delete to end of word                                                                              | <kbd>Control+Delete</kbd>                                     | <kbd>Option+Delete</kbd>                                      |
| Delete to start of word                                                                            | <kbd>Control+Backspace</kbd>                                  | <kbd>Option+Delete</kbd>                                      |
| Optimize imports                                                                                   | <kbd>Control+Alt+O</kbd>                                      | <kbd>Control+Option+O</kbd>                                   |
| Project quick fix (show intention actions and quick fixes)                                         | <kbd>Alt+Enter</kbd>                                          | <kbd>Option+Enter</kbd>                                       |
| Reformat code                                                                                      | <kbd>Control+Alt+L</kbd>                                      | <kbd>Command+Option+L</kbd>                                   |
| Auto-indent lines                                                                                  | <kbd>Control+Alt+I</kbd>                                      | <kbd>Control+Option+I</kbd>                                   |
| Indent/unindent lines                                                                              | <kbd>Tab</kbd>or<kbd>Shift+Tab</kbd>                          | <kbd>Tab</kbd>or<kbd>Shift+Tab</kbd>                          |
| Smart line join                                                                                    | <kbd>Control+Shift+J</kbd>                                    | <kbd>Control+Shift+J</kbd>                                    |
| Smart line split                                                                                   | <kbd>Control+Enter</kbd>                                      | <kbd>Command+Enter</kbd>                                      |
| Start new line                                                                                     | <kbd>Shift+Enter</kbd>                                        | <kbd>Shift+Enter</kbd>                                        |
| Next/previous highlighted error                                                                    | <kbd>F2</kbd>or<kbd>Shift+F2</kbd>                            | <kbd>F2</kbd>or<kbd>Shift+F2</kbd>                            |
| Build                                                                                              | <kbd>Control+F9</kbd>                                         | <kbd>Command+F9</kbd>                                         |
| Build and run                                                                                      | <kbd>Shift+F10</kbd>                                          | <kbd>Control+R</kbd>                                          |
| Apply changes and restart activity                                                                 | <kbd>Control+F10</kbd>                                        | <kbd>Control+Command+R</kbd>                                  |
| Apply code changes                                                                                 | <kbd>Control+Alt+F10</kbd>                                    | <kbd>Control+Command+Shift+R</kbd>                            |
| Debug                                                                                              | <kbd>Shift+F9</kbd>                                           | <kbd>Control+D</kbd>                                          |
| Step over                                                                                          | <kbd>F8</kbd>                                                 | <kbd>F8</kbd>                                                 |
| Step into                                                                                          | <kbd>F7</kbd>                                                 | <kbd>F7</kbd>                                                 |
| Smart step into                                                                                    | <kbd>Shift+F7</kbd>                                           | <kbd>Shift+F7</kbd>                                           |
| Step out                                                                                           | <kbd>Shift+F8</kbd>                                           | <kbd>Shift+F8</kbd>                                           |
| Run to cursor                                                                                      | <kbd>Alt+F9</kbd>                                             | <kbd>Option+F9</kbd>                                          |
| Evaluate expression                                                                                | <kbd>Alt+F8</kbd>                                             | <kbd>Option+F8</kbd>                                          |
| Resume program                                                                                     | <kbd>F9</kbd>                                                 | <kbd>Command+Option+R</kbd>                                   |
| Toggle breakpoint                                                                                  | <kbd>Control+F8</kbd>                                         | <kbd>Command+F8</kbd>                                         |
| View breakpoints                                                                                   | <kbd>Control+Shift+F8</kbd>                                   | <kbd>Command+Shift+F8</kbd>                                   |
| Copy                                                                                               | <kbd>F5</kbd>                                                 | <kbd>F5</kbd>                                                 |
| Move                                                                                               | <kbd>F6</kbd>                                                 | <kbd>F6</kbd>                                                 |
| Safe delete                                                                                        | <kbd>Alt+Delete</kbd>                                         | <kbd>Command+Delete</kbd>                                     |
| Rename                                                                                             | <kbd>Shift+F6</kbd>                                           | <kbd>Shift+F6</kbd>                                           |
| Change signature                                                                                   | <kbd>Control+F6</kbd>                                         | <kbd>Command+F6</kbd>                                         |
| Inline                                                                                             | <kbd>Control+Alt+N</kbd>                                      | <kbd>Command+Option+N</kbd>                                   |
| Extract method                                                                                     | <kbd>Control+Alt+M</kbd>                                      | <kbd>Command+Option+M</kbd>                                   |
| Extract variable                                                                                   | <kbd>Control+Alt+V</kbd>                                      | <kbd>Command+Option+V</kbd>                                   |
| Extract field                                                                                      | <kbd>Control+Alt+F</kbd>                                      | <kbd>Command+Option+F</kbd>                                   |
| Extract constant                                                                                   | <kbd>Control+Alt+C</kbd>                                      | <kbd>Command+Option+C</kbd>                                   |
| Extract parameter                                                                                  | <kbd>Control+Alt+P</kbd>                                      | <kbd>Command+Option+P</kbd>                                   |
| Commit project to VCS                                                                              | <kbd>Control+K</kbd>                                          | <kbd>Command+K</kbd>                                          |
| Update project from VCS                                                                            | <kbd>Control+T</kbd>                                          | <kbd>Command+T</kbd>                                          |
| View recent changes                                                                                | <kbd>Alt+Shift+C</kbd>                                        | <kbd>Option+Shift+C</kbd>                                     |
| Open VCS dialog                                                                                    | <kbd>Alt+`</kbd>(backtick)                                    | <kbd>Control+V</kbd>                                          |

## Configure custom keymaps

The keymap settings in Android Studio let you choose from a list of preset options or create a custom keymap.

To open the keymap settings, choose**File \> Settings** (on macOS,**Android Studio \> Preferences** ) and navigate to the**Keymap**pane.

![](https://developer.android.com/static/studio/images/intro/keymap-options_2-2_2x.png)

**Figure 1.**The Android Studio keymap settings window on macOS.

1. **Keymaps menu:**Select the desired keymap from this menu to switch between preset keymaps.
2. **Actions list:**Right-click an action to modify it. You can add additional keyboard shortcuts for the action, add mouse shortcuts to associate an action with a mouse click, or remove current shortcuts. If you are using a preset keymap, modifying an action's shortcuts automatically creates a copy of the keymap and adds your modifications to the copy.
3. **Copy button:** Select a keymap from the menu to use as a starting point, and click**Copy**to create a new custom keymap. You can then modify the keymap name and shortcuts.
4. **Reset button:** Select a keymap from the menu and click**Reset**to revert it to its original configuration.
5. **Search box:**Type here to search for a keyboard shortcut by the action name.
6. **Search by Shortcut:**Click this button and type a shortcut to search for actions by their assigned shortcut.