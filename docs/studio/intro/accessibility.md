---
title: Accessibility features  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/intro/accessibility
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Accessibility features Stay organized with collections Save and categorize content based on your preferences.



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
shortcuts, read [Keyboard shortcuts](/studio/intro/keyboard-shortcuts).

### Activate the main menu

To open the main menu and other top-level menus, use these shortcuts:

* To open the main menu, press `F10`.
* To open a top-level menu on a Windows machine, press
  `Alt+[mnemonic]`.
  For example, to open the File menu, press `Alt+F`.

### Navigate between files and tool windows

To navigate between files and tool windows, use these shortcuts:

* To move to a tool window, press `Alt+[number]` (on macOS,
  `Command+[number]`). For example, to move to the Project
  structure tool window, press `Alt+0` (on macOS,
  `Command+0`).
* To move between files and tool windows, press `Control+Tab`
  (on macOS, `Command+Tab`). To move through all entries, keep
  pressing `Control+Tab`.

### Use the navigation bar

The navigation bar lets you move between files in a project using the following
shortcuts:

* To activate the navigation bar, press Alt+Home (on macOS,
  `Option+Fn+Left`).
* To switch between items in the navigation hierarchy, press the left
  arrow or the right arrow.
* To open a popup window displaying the contents of the current item,
  press the spacebar.

## Disable code folding

By default, the Android Studio editor folds part of the text into expandable
regions. For example, the list of imports at the beginning of a Java source
file is folded into a single line containing the text "`import …`".

When using a screen reader, code folding can make navigation difficult. To
modify code folding options, navigate to
**File > Settings > Editor > General > Code Folding** (on macOS,
**Android Studio > Preferences > Editor > General > Code Folding**).

## Disable auto-insertion features

By default, Android Studio automatically inserts closing curly braces,
quotes, or parentheses.

When using a screen reader, automatic insertion might not be useful. To
modify automatic insertion options, navigate to
**File > Settings > Editor > General > Smart Keys** (on macOS,
**Android Studio > Preferences > Editor > General > Smart Keys**).

## Disable automatic code completion popup

By default, Android Studio automatically shows the code completion popup
when certain keystrokes are typed, and if it finds only a single match,
it auto-inserts that match. This behavior can cause confusion
with screen readers.

To modify auto popup and auto-insertion options for code completion, navigate to
**File > Settings > Editor > General > Code Completion** (on macOS,
**Android Studio > Preferences > Editor > General > Code Completion**).

## Access errors, warnings, and code inspections

Use your keyboard to view and navigate through errors, warnings, and code
inspections.

### Review errors in all files in a project

When you click **Build > Make Project**, all warnings and errors appear in
the **Messages** window.

To review errors in the **Messages** window, use these shortcuts:

* To activate the **Messages** window, press `Alt+0` (on macOS,
  `Option+0`).
* To navigate through all messages, press the up and down arrows.

Alternatively, you can use the text editor to view and navigate through all
errors. To use the editor to review errors, press
`Control+Alt+Up/Down` (on macOS,
`Command+Option+Up/Down`).

### Review errors and code inspections in a single file

To review errors in a single file, use these shortcuts:

* To go to the next or previous error, press `F2` or
  `Shift+F2` (on macOS, `F2` or `Shift+F2`).
* To open a tooltip containing the error message, press
  `Control+F1` (on macOS, `Command+F1`).

To navigate to all code inspections—not just errors:

1. Click **File > Settings > Editor > General** (on macOS,
   **Android Studio > Preferences > Editor > General**).
2. Deselect **'Next error' action goes to high priority problems only**.

## Use tab indentation

By default, Android Studio uses the space character for indentation. Screen
reader users may prefer tab indentation because the verbalization is more
concise.

To change to tab indentation:

1. Navigate to
   **File > Settings > Editor > Code Style > Java > Tabs and Indents**
   (on macOS,
   **Android Studio > Preferences > Editor > Code Style > Java > Tabs and Indents**).
2. Select **Use tab character**.