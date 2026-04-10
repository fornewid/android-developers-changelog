---
title: https://developer.android.com/studio/intro/accessibility
url: https://developer.android.com/studio/intro/accessibility
source: md.txt
---

This document describes accessibility features available in Android Studio,
including keyboard navigation.

IntelliJ IDEA updated accessibility features in release 2021.1, which is the
basis of Android Studio Bumblebee, so all versions of Android Studio from
Bumblebee onward also benefit from these updates. The
[IntelliJ documentation](https://www.jetbrains.com/help/idea/2025.3/accessibility.html)
contains full details of accessibility features such as setting up screen
readers and customizing the IDE for greater accessibility.

## Use the keyboard

You can use keyboard shortcuts to navigate through all controls in Android
Studio.

**Note:** Some Android Studio elements are
keyboard-accessible only when using the object navigation feature
of your screen reader. For help with object navigation or its equivalent, consult
your screen reader documentation, such as the [NVDA
user guide](http://www.nvaccess.org/files/nvda/documentation/userGuide.html).

This section includes useful keyboard shortcuts for navigating around
Android Studio. For a complete guide to the default Android Studio keyboard
shortcuts, read [Keyboard shortcuts](https://developer.android.com/studio/intro/keyboard-shortcuts).

### Activate the main menu

To open the main menu and other top-level menus, use these shortcuts:

- To open the main menu, press <kbd>F10</kbd>.
- To open a top-level menu on a Windows machine, press <kbd>Alt+[<em>mnemonic</em>]</kbd>. For example, to open the File menu, press <kbd>Alt+F</kbd>.

### Navigate between files and tool windows

To navigate between files and tool windows, use these shortcuts:

- To move to a tool window, press <kbd>Alt+[<em>number</em>]</kbd> (on macOS, <kbd>Command+[<em>number</em>]</kbd>). For example, to move to the Project structure tool window, press <kbd>Alt+0</kbd> (on macOS, <kbd>Command+0</kbd>).
- To move between files and tool windows, press <kbd>Control+Tab</kbd> (on macOS, <kbd>Command+Tab</kbd>). To move through all entries, keep pressing <kbd>Control+Tab</kbd>.

### Use the navigation bar

The navigation bar lets you move between files in a project using the following
shortcuts:

- To activate the navigation bar, press Alt+Home (on macOS, <kbd>Option+Fn+Left</kbd>).
- To switch between items in the navigation hierarchy, press the left arrow or the right arrow.
- To open a popup window displaying the contents of the current item, press the spacebar.

## Disable code folding

By default, the Android Studio editor folds part of the text into expandable
regions. For example, the list of imports at the beginning of a Java source
file is folded into a single line containing the text "`import ...`".

When using a screen reader, code folding can make navigation difficult. To
modify code folding options, navigate to
**File \> Settings \> Editor \> General \> Code Folding** (on macOS,
**Android Studio \> Preferences \> Editor \> General \> Code Folding**).

## Disable auto-insertion features

By default, Android Studio automatically inserts closing curly braces,
quotes, or parentheses.

When using a screen reader, automatic insertion might not be useful. To
modify automatic insertion options, navigate to
**File \> Settings \> Editor \> General \> Smart Keys** (on macOS,
**Android Studio \> Preferences \> Editor \> General \> Smart Keys**).

## Disable automatic code completion popup

By default, Android Studio automatically shows the code completion popup
when certain keystrokes are typed, and if it finds only a single match,
it auto-inserts that match. This behavior can cause confusion
with screen readers.

To modify auto popup and auto-insertion options for code completion, navigate to
**File \> Settings \> Editor \> General \> Code Completion** (on macOS,
**Android Studio \> Preferences \> Editor \> General \> Code Completion**).

## Access errors, warnings, and code inspections

Use your keyboard to view and navigate through errors, warnings, and code
inspections.

### Review errors in all files in a project

When you click **Build \> Make Project** , all warnings and errors appear in
the **Messages** window.

To review errors in the **Messages** window, use these shortcuts:

- To activate the **Messages** window, press <kbd>Alt+0</kbd> (on macOS, <kbd>Option+0</kbd>).
- To navigate through all messages, press the up and down arrows.

Alternatively, you can use the text editor to view and navigate through all
errors. To use the editor to review errors, press
<kbd>Control+Alt+Up/Down</kbd> (on macOS,
<kbd>Command+Option+Up/Down</kbd>).

### Review errors and code inspections in a single file

To review errors in a single file, use these shortcuts:

- To go to the next or previous error, press <kbd>F2</kbd> or <kbd>Shift+F2</kbd> (on macOS, <kbd>F2</kbd> or <kbd>Shift+F2</kbd>).
- To open a tooltip containing the error message, press <kbd>Control+F1</kbd> (on macOS, <kbd>Command+F1</kbd>).

To navigate to all code inspections---not just errors:

1. Click **File \> Settings \> Editor \> General** (on macOS, **Android Studio \> Preferences \> Editor \> General**).
2. Deselect **'Next error' action goes to high priority problems only**.

## Use tab indentation

By default, Android Studio uses the space character for indentation. Screen
reader users may prefer tab indentation because the verbalization is more
concise.

To change to tab indentation:

1. Navigate to **File \> Settings \> Editor \> Code Style \> Java \> Tabs and Indents** (on macOS, **Android Studio \> Preferences \> Editor \> Code Style \> Java \> Tabs and Indents**).
2. Select **Use tab character**.