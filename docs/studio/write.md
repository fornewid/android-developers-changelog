---
title: https://developer.android.com/studio/write
url: https://developer.android.com/studio/write
source: md.txt
---

# Write your app

Android Studio includes tools for every stage of development, but what's most important is simply writing your app: writing the code, building layouts, creating images, and being productive along the way.

That's what this section is all about: the tools that help you write your app and write it quickly.

## Coding productivity

The following are just a few features to help you be more productive when coding.

### Code completion

Code completion speeds up app development by reducing typing errors and the need to look up class, method, and variable names. The code editor provides basic completion, smart completion, and statement completion.

Learn more about[Code completion](https://developer.android.com/studio/intro#code_completion).

### Create custom code-completion templates

Live templates allow you to enter code snippets for fast insertion and completion of small chunks of code. To insert a live template, type the template abbreviation and press the**Tab**key. Android Studio inserts the code snippet associated with the template into your code.

For example, the`comp`abbreviation followed by**Tab** inserts the code for a new composable function. Or type`loge`to find the`Log.e()`method and[log from your code](https://developer.android.com/studio/command-line/logcat#logClass).

To see the list of supported live templates and customize them, click**File \> Settings \> Editor \> Live Templates** (**Android Studio \> Settings \> Editor \> Live Templates**on macOS).

Learn more about[Live templates](https://medium.com/google-developers/writing-more-code-by-writing-less-code-with-android-studio-live-templates-244f648d17c7#.h1jn0hq31).

### Get quick fixes from lint

Android Studio provides a code scanning tool called Lint to help you to identify and correct problems with the structural quality of your code, without executing the app or writing tests.

Every time you build your app, Android Studio runs Lint to check your source files for potential bugs and looks for optimization improvements in correctness, security, performance, usability, accessibility, and internationalization.

Learn more about[Lint](https://developer.android.com/studio/write/lint).

### See documentation and resource details

You can view documentation for an API by placing the caret on the method/member/class name and pressing**F1**.

Information is also available for other resources, such as images and themes. For example, if you place the caret on the theme name in your Android manifest file and press**F1**, you can see the theme inheritance hierarchy and colors or images for the various attributes.

### Quickly create new files

When you want to create a new file, click the desired directory in the Project window, then press**Alt + Insert** (**Command + N**on Mac). Android Studio shows a small window with a list of suggested file types, as appropriate for the selected directory.

## Working with resources

Android Studio includes the following features and tools to help you create and manage resource files.

Learn more about[adding resources](https://developer.android.com/studio/write/add-resources).

### Create images for all screen densities

Android Studio includes a tool called Vector Asset Studio that helps you create images that support each screen density. You can upload your own SVG file for editing or select from one of the many Google-provided material design icons. To get started, click**File \> New \> Vector Asset**.

Learn more about[Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio).

### Preview images and colors

When referencing images and icons in your code, a preview of the image appears in the left margin to help you verify the image or icon reference.

To view the full size image, click the thumbnail in the left margin. Or, place the caret on the inline reference to the asset and press**F1**to see the image details, including all the alternative sizes.

### Create new layouts

Android Studio lets you preview your composable layouts when you use the[composable preview](https://developer.android.com/develop/ui/compose/tooling/previews)function. Previews of your composables appear in the**Design**view of the file and update in real time as you edit the composables.

If you're using XML layouts, Android Studio offers the[Layout Editor](https://developer.android.com/studio/write/layout-editor)to preview your layout while editing the XML.

### Translate UI strings

The Translations Editor tool gives you a single view of all of your translated resources, making it easy to change or add translations, and even find missing translations without opening every version of the`strings.xml`file. You can even upload your strings file to order translation services.

To get started, right-click on any copy of your`strings.xml`file then click**Open Translations Editor**.

Learn more about the[Translations Editor](https://developer.android.com/studio/write/translations-editor).