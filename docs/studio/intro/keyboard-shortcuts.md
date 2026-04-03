---
title: Keyboard shortcuts  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/intro/keyboard-shortcuts
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Keyboard shortcuts Stay organized with collections Save and categorize content based on your preferences.



Keyboard shortcuts are a useful way of quickly navigating around Android
Studio and performing common actions. In many cases, using keyboard shortcuts is
faster than using the GUI.

This page shows some common keyboard shortcuts. Since Android Studio
is based on IntelliJ IDEA, you can find additional shortcuts in
the [IntelliJ IDEA keymap reference documentation](https://resources.jetbrains.com/storage/products/intellij-idea/docs/IntelliJIDEA_ReferenceCard.pdf).

## Tool windows

You can use keyboard shortcuts to open tool windows. Table 1 lists the
shortcuts for the most common windows.

**Table 1.** Keyboard shortcuts for common tool windows

| Tool window | Windows and Linux | macOS |
| --- | --- | --- |
| Project | `Alt+1` | `Command+1` |
| Version Control | `Alt+9` | `Command+9` |
| Run | `Shift+F10` | `Control+R` |
| Debug | `Shift+F9` | `Control+D` |
| Logcat | `Alt+6` | `Command+6` |
| Return to Editor | `Esc` | `Esc` |
| Hide All Tool Windows | `Control+Shift+F12` | `Command+Shift+F12` |

## Code completion

Android Studio has three types of code completion, which you can access using
keyboard shortcuts, as shown in the following table.

**Table 2.** Keyboard shortcuts for code completion

| Type | Description | Windows and Linux | macOS |
| --- | --- | --- | --- |
| Basic Completion | Displays basic suggestions for variables, types, methods, expressions, and so on. If you call basic completion twice in a row, you see more results, including private members and non-imported static members. | `Control+Space` | `Control+Space` |
| Smart Completion | Displays relevant options based on the context. Smart completion takes into account the expected type and data flows. If you call Smart Completion twice in a row, you see more results, including chains. | `Control+Shift+Space` | `Control+Shift+Space` |
| Statement Completion | Completes the current statement, adding missing parentheses, brackets, braces, formatting, and so on. | `Control+Shift+Enter` | `Command+Shift+Enter` |

To perform quick fixes and show [intention actions](https://www.jetbrains.com/help/idea/intention-actions.html),
press `Alt+Enter`.

## Navigation

Use the following tips to help navigate around Android Studio:

* Switch between your recently accessed files using the **Recent Files**
  action. To bring up the **Recent Files** action, press `Control+E`
  (`Command+E` on macOS). By default, the last accessed file is
  selected. You can also access any tool window through the left column
  in this action.
* View the structure of the current file using the **File Structure** action.
  To bring up the **File Structure** action, press `Control+F12`
  (`Command+F12` on macOS). Using this action, you can quickly
  navigate to any part of your current file.
* Search for and navigate to a specific class in your project using the
  **Navigate to Class** action. To bring up the **Navigate to Class** action,
  press `Control+N` (`Command+O` on macOS).

  **Navigate to Class** supports sophisticated expressions, including
  *camel humps* (which lets you search by the capitalized letters in an
  element's camel-cased name), paths, *line navigate to* (which lets you
  navigate to a specific line within the file), and *middle name matching*
  (which lets you search for a part of the class name). If
  you call it twice in a row, it shows you the results out of the project
  classes.
* Navigate to a file or folder using the **Navigate to File** action. To
  bring up the **Navigate to File**, press `Control+Shift+N`
  (`Command+Shift+O` on macOS). To search for folders rather
  than files, add a `/` at the end of your expression.
* Navigate to a method or field by name using the **Navigate to Symbol**
  action. To bring up the **Navigate to Symbol** action, press
  `Control+Alt+Shift+N` (`Command+Option+O` on macOS).
* To find all the pieces of code referencing the class, method, field,
  parameter, or statement at the current cursor position, press
  `Alt+F7` (`Option+F7` on macOS).

## Default keymaps

Android Studio includes keyboard shortcuts for many common actions. Table 3
shows the default keyboard shortcuts by operating system.

**Note:** In addition to the default keymaps in
table 3, you can select from a number of preset keymaps or create a custom
keymap. For more about customizing your keyboard shortcuts, see the
[Configure custom keymaps](#custom) section.

**Table 3.** Default keyboard shortcuts for Windows or Linux and
macOS operating systems

| Description | Windows and Linux | macOS |
| --- | --- | --- |
| General actions | | |
| Save all | `Control+S` | `Command+S` |
| Synchronize | `Control+Alt+Y` | `Command+Option+Y` |
| Maximize/minimize editor | `Control+Shift+F12` | `Control+Command+F12` |
| Add to favorites | `Alt+Shift+F` | `Option+Shift+F` |
| Inspect current file with current profile | `Alt+Shift+I` | `Option+Shift+I` |
| Quick switch scheme | `` Control+` `` (backtick) | `` Control+` `` (backtick) |
| Open settings dialog | `Control+Alt+S` | `Command+,` (comma) |
| Open project structure dialog | `Control+Alt+Shift+S` | `Command+;` (semicolon) |
| Switch between tabs and tool window | `Control+Tab` | `Control+Tab` |
| Navigate and search within Android Studio | | |
| Search everything (including code and menus) | Press `Shift` twice | Press `Shift` twice |
| Find | `Control+F` | `Command+F` |
| Find next | `F3` | `Command+G` |
| Find previous | `Shift+F3` | `Command+Shift+G` |
| Replace | `Control+R` | `Command+R` |
| Find action | `Control+Shift+A` | `Command+Shift+A` |
| Search by symbol name | `Control+Alt+Shift+N` | `Command+Option+O` |
| Find class | `Control+N` | `Command+O` |
| Find file (instead of class) | `Control+Shift+N` | `Command+Shift+O` |
| Find in path | `Control+Shift+F` | `Command+Shift+F` |
| Open file structure dialog | `Control+F12` | `Command+F12` |
| Navigate between open editor tabs | `Alt+Right Arrow` or `Left Arrow` | `Control+Right Arrow` or `Control+Left Arrow` |
| Jump to source | `F4` or `Control+Enter` | `F4` or `Command+Down Arrow` |
| Open current editor tab in new window | `Shift+F4` | `Shift+F4` |
| Recently opened files dialog | `Control+E` | `Command+E` |
| Recently edited files dialog | `Control+Shift+E` | `Command+Shift+E` |
| Go to last edit location | `Control+Shift+Backspace` | `Command+Shift+Delete` |
| Close active editor tab | `Control+F4` | `Command+W` |
| Return to editor window from a tool window | `Esc` | `Esc` |
| Hide active or last active tool window | `Shift+Esc` | `Shift+Esc` |
| Go to line | `Control+G` | `Command+L` |
| Open type hierarchy | `Control+H` | `Control+H` |
| Open method hierarchy | `Control+Shift+H` | `Command+Shift+H` |
| Open call hierarchy | `Control+Alt+H` | `Control+Option+H` |
| View layouts | | |
| Zoom in/out | `Control+plus` or `Control+minus` | `Command+plus` or `Command+minus` |
| Fit to screen | `Control+0` | `Command+0` |
| Actual size | `Control+Shift+1` | `Command+Shift+1` |
| Design tools: Layout Editor | | |
| Toggle between Design and Blueprint modes | `B` | `B` |
| Toggle between Portrait and Landscape modes | `O` | `O` |
| Toggle devices | `D` | `D` |
| Force refresh | `R` | `R` |
| Toggle render errors panel | `E` | `E` |
| Delete constraints | `Delete` or `Control`+click | `Delete` or `Command`+click |
| Zoom in | `Control+plus` | `Command+plus` |
| Zoom out | `Control+minus` | `Command+minus` |
| Zoom to fit | `Control+0` | `Command+0` |
| Pan | Hold `Space`+click and drag | Hold `Space`+click and drag |
| Go to XML | `Control+B` | `Command+B` |
| Select all components | `Control+A` | `Command+A` |
| Select multiple components | `Shift`+click or `Control`+click | `Shift`+click or `Command`+click |
| Design tools: Navigation Editor | | |
| Zoom in | `Control+plus` | `Command+plus` |
| Zoom out | `Control+minus` | `Command+minus` |
| Zoom to fit | `Control+0` | `Command+0` |
| Pan | Hold `Space`+click and drag | Hold `Space`+click and drag |
| Go to XML | `Control+B` | `Command+B` |
| Toggle render errors panel | `E` | `E` |
| Group into nested graph | `Control+G` | `Command+G` |
| Cycle through destinations | `Tab` or `Shift+Tab` | `Tab` or `Shift+Tab` |
| Select all destinations | `Control+A` | `Command+A` |
| Select multiple destinations | `Shift`+click or `Control`+click | `Shift`+click or `Command`+click |
| Write code | | |
| Generate code (getters, setters, constructors, `hashCode`/`equals`, `toString`, new file, new class) | `Alt+Insert` | `Command+N` |
| Override methods | `Control+O` | `Control+O` |
| Implement methods | `Control+I` | `Control+I` |
| Surround with (`if...else`, `try...catch`, etc.) | `Control+Alt+T` | `Command+Option+T` |
| Delete line at caret | `Control+Y` | `Command+Delete` |
| Collapse/expand current code block | `Control+minus` or `Control+plus` | `Command+minus` or `Command+plus` |
| Collapse/expand all code blocks | `Control+Shift+minus` or `Control+Shift+plus` | `Command+Shift+minus` or `Command+Shift+plus` |
| Duplicate current line or selection | `Control+D` | `Command+D` |
| Basic code completion | `Control+Space` | `Control+Space` |
| Smart code completion (filters the list of methods and variables by expected type) | `Control+Shift+Space` | `Control+Shift+Space` |
| Complete statement | `Control+Shift+Enter` | `Command+Shift+Enter` |
| Quick documentation lookup | `Control+Q` | `Control+J` |
| Show parameters for selected method | `Control+P` | `Command+P` |
| Go to declaration (directly) | `Control+B` or `Control`+click | `Command+B` or `Command`+click |
| Go to implementations | `Control+Alt+B` | `Command+Option+B` |
| Go to supermethod/superclass | `Control+U` | `Command+U` |
| Open quick definition lookup | `Control+Shift+I` | `Command+Y` |
| Toggle project tool window visibility | `Alt+1` | `Command+1` |
| Toggle bookmark | `F11` | `F3` |
| Toggle bookmark with mnemonic | `Control+F11` | `Option+F3` |
| Comment/uncomment with line comment | `Control+/` | `Command+/` |
| Comment/uncomment with block comment | `Control+Shift+/` | `Command+Shift+/` |
| Select successively increasing code blocks | `Control+W` | `Option+Up` |
| Decrease current selection to previous state | `Control+Shift+W` | `Option+Down` |
| Move to code block start | `Control+[` | `Option+Command+[` |
| Move to code block end | `Control+]` | `Option+Command+]` |
| Select to the code block start | `Control+Shift+[` | `Option+Command+Shift+[` |
| Select to the code block end | `Control+Shift+]` | `Option+Command+Shift+]` |
| Delete to end of word | `Control+Delete` | `Option+Delete` |
| Delete to start of word | `Control+Backspace` | `Option+Delete` |
| Optimize imports | `Control+Alt+O` | `Control+Option+O` |
| Project quick fix (show intention actions and quick fixes) | `Alt+Enter` | `Option+Enter` |
| Reformat code | `Control+Alt+L` | `Command+Option+L` |
| Auto-indent lines | `Control+Alt+I` | `Control+Option+I` |
| Indent/unindent lines | `Tab` or `Shift+Tab` | `Tab` or `Shift+Tab` |
| Smart line join | `Control+Shift+J` | `Control+Shift+J` |
| Smart line split | `Control+Enter` | `Command+Enter` |
| Start new line | `Shift+Enter` | `Shift+Enter` |
| Next/previous highlighted error | `F2` or `Shift+F2` | `F2` or `Shift+F2` |
| Build and run | | |
| Build | `Control+F9` | `Command+F9` |
| Build and run | `Shift+F10` | `Control+R` |
| Apply changes and restart activity | `Control+F10` | `Control+Command+R` |
| Apply code changes | `Control+Alt+F10` | `Control+Command+Shift+R` |
| Debug | | |
| Debug | `Shift+F9` | `Control+D` |
| Step over | `F8` | `F8` |
| Step into | `F7` | `F7` |
| Smart step into | `Shift+F7` | `Shift+F7` |
| Step out | `Shift+F8` | `Shift+F8` |
| Run to cursor | `Alt+F9` | `Option+F9` |
| Evaluate expression | `Alt+F8` | `Option+F8` |
| Resume program | `F9` | `Command+Option+R` |
| Toggle breakpoint | `Control+F8` | `Command+F8` |
| View breakpoints | `Control+Shift+F8` | `Command+Shift+F8` |
| Refactor | | |
| Copy | `F5` | `F5` |
| Move | `F6` | `F6` |
| Safe delete | `Alt+Delete` | `Command+Delete` |
| Rename | `Shift+F6` | `Shift+F6` |
| Change signature | `Control+F6` | `Command+F6` |
| Inline | `Control+Alt+N` | `Command+Option+N` |
| Extract method | `Control+Alt+M` | `Command+Option+M` |
| Extract variable | `Control+Alt+V` | `Command+Option+V` |
| Extract field | `Control+Alt+F` | `Command+Option+F` |
| Extract constant | `Control+Alt+C` | `Command+Option+C` |
| Extract parameter | `Control+Alt+P` | `Command+Option+P` |
| Version control/local history | | |
| Commit project to VCS | `Control+K` | `Command+K` |
| Update project from VCS | `Control+T` | `Command+T` |
| View recent changes | `Alt+Shift+C` | `Option+Shift+C` |
| Open VCS dialog | `` Alt+` `` (backtick) | `Control+V` |

## Configure custom keymaps

The keymap settings in Android Studio let you choose from a list of preset
options or create a custom keymap.

To open the keymap settings, choose **File > Settings** (on macOS, **Android
Studio > Preferences**) and navigate to the **Keymap** pane.

![](/static/studio/images/intro/keymap-options_2-2_2x.png)

**Figure 1.** The Android Studio keymap settings window on macOS.

1. **Keymaps menu:** Select the desired keymap from this menu to switch
   between preset keymaps.
2. **Actions list:** Right-click an action to modify it. You can add
   additional keyboard shortcuts for the action, add mouse shortcuts to
   associate an action with a mouse click, or remove current shortcuts. If you
   are using a preset keymap, modifying an action’s shortcuts
   automatically creates a copy of the keymap and adds your modifications to
   the copy.
3. **Copy button:** Select a keymap from the menu to use as a
   starting point, and click **Copy** to create a new custom
   keymap. You can then modify the keymap name and shortcuts.
4. **Reset button:** Select a keymap from the menu and click
   **Reset** to revert it to its original configuration.
5. **Search box:** Type here to search for a keyboard shortcut by the
   action name.
6. **Search by Shortcut:** Click this button
   and type a shortcut to search for actions by their assigned shortcut.