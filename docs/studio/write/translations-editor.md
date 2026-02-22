---
title: https://developer.android.com/studio/write/translations-editor
url: https://developer.android.com/studio/write/translations-editor
source: md.txt
---

The Translations Editor provides a consolidated and editable view of all of your default and
translated [string resources](https://developer.android.com/guide/topics/resources/string-resource).

For an introduction to translating your app for different languages, read
[Supporting different
languages and cultures](https://developer.android.com/training/basics/supporting-devices/languages).
![](https://developer.android.com/static/studio/images/write/translations-editor-basic_2x.png)

**Figure 1.** The **Translations Editor** showing app text before
translation

## String resources


The string resources for a project are contained in `strings.xml` files. Your project
has a default `strings.xml` file that contains string resources in the default
language for your app, which is the language you expect most of your app users
to speak. You can also have translated `strings.xml` files that contain string
resources for other languages that you want your app to accommodate.


Once you have your default `strings.xml` file completed, you can add the translations
yourself, or pay a professional service to do the translations. Either way, you should take
advantage of the Android Studio features to help you [manage and test
localizable text](https://developer.android.com/studio/write/translations-editor#localize). For information
about professional translation services, see [Order translation services](https://developer.android.com/studio/write/translations-editor#ordering).

## Open the Translations Editor


You can access the Translations Editor from the following places in Android Studio.

### Open from the Android view

1. In the **Project \> Android** panel on the left, select **<var translate="no">ModuleName</var> \> res \> values**.
2. Right-click the **strings.xml** file, and select **Open Translations Editor** .


   The Translations Editor displays the key and value pairs from the
   `strings.xml` file.

   **Note:**
   When you have translated `strings.xml` files, your project has multiple corresponding
   **values** folders with suffixes that indicate the language, such as
   **values-es** for Spanish. Your default `strings.xml` file is always in the
   **values** (no suffix) folder.


Figure 1 shows the default app text (in this case, English) in the Translations Editor for
a simple app before translation work has been done. The contents of translated
`strings.xml` files will appear to the right of the **Untranslatable** column with
one column per language as shown in figure 2.

### Open from within strings.xml


You can access the **Translations Editor** from within any of your `strings.xml` files.

1. In the **Project \> Android** panel on the left, select **<var translate="no">ModuleName</var> \> res \> values**.
2. Double-click **strings.xml** to open it for editing.
3. In **strings.xml** , click the **Open editor** link in the upper-right corner.

**Note:** If you click the **Hide notification** link, the **Open
editor** link goes away. To bring it back, close and reopen the project.

### Open from the Design Editor


You can open the **Translations Editor** from the Layout Editor's Design Editor to edit your
default and translated
text to better fit your layout. For information about switching languages in the Design Editor,
see [Display translated text in the Design Editor](https://developer.android.com/studio/write/translations-editor#view).

1. In the **Project \> Android** panel on the left, select **<var translate="no">ModuleName</var> \> res \> layout**.
2. Double-click **content_main.xml** to open it for editing.
3. Click the **Design** tab in the lower-left corner to display the **Design** Editor.
4. In the Design Editor, select the **Language** ![](https://developer.android.com/static/studio/images/buttons/layout-editor-language-icon.png) drop-down list.
5. Select **Edit Translations** ![](https://developer.android.com/static/studio/images/buttons/translations-edit-icon.png).

## Configure untranslatable rows


In the **Translations Editor** , you can select **Unstranslatable** to
indicate that you do not want the text in this row to be translated. Text that you would
not want translated might be product-specific text like trade names and trade marks,
or technical terms that do not have a translation.


When you check **Untranslatable** , the corresponding line in the default
`strings.xml` file adds **translatable="false"** . In the following example,
**EasyApp**
in the top line is not translated because it is the product name.

```xml
<resources>
    <string name="app_name" translatable="false">EasyApp</string>
    <string name="action_settings">Settings</string>
    <string name="easy_app">I am a Simple App!</string>
    <string name="next_page">Next Page</string>
    <string name="second_page_message">I am the Second Page!</string>
    <string name="title_activity_second">SecondActivity</string>
</resources>
```

## Add and delete languages


The **Translations Editor** supports
[BCP 47](https://tools.ietf.org/html/bcp47) and
combines locale and region (country) codes into a single selection for targeted localizations.
A locale defines more than the language. A locale includes country-dependent formatting for
things like the date and time, currencies, and decimals.


To add a language, do the following:

1. In the **Translations Editor** , click the globe icon ![](https://developer.android.com/static/studio/images/buttons/translations-edit-icon.png).
2. From the drop-down list, select the language you want to add.
   The new language appears in the **Translations Editor** , and a **values-\***
   folder with a `strings.xml` file is added to the project. For example,
   **values-es** for Spanish.

To delete a language, do the following:

You can delete a language in the **Translations Editor** by deleting every value in the column
(see
[Edit, add, or delete text](https://developer.android.com/studio/write/translations-editor#editaddtext)), or you can delete the project folder
for that language, as follows:

1. In the **Project \> Android** panel on the left, select **<var translate="no">ModuleName</var> \> res**.
2. Right click the **values-\*** folder for the language you want to delete. For example, **values-hi** for Hindi.
3. From the drop-down list, select **Delete** to delete the folder and its **strings.xml** file.

## Edit, add, and delete text


You can operate on the text settings directly in the `strings.xml` file or
through the **Translations Editor** . This section describes the
**Translations Editor** approach. In the **Translations Editor** , you can edit, add, or
delete text through the list view or through
the **Translation** field at the bottom of the **Translations Editor**.
![](https://developer.android.com/static/studio/images/write/translation-field_2x.png)

**Figure 2.** List view on the top and the **Translation** field
on the bottom

#### List view

To edit or add text, do the following:

1. Double-click the cell where you want to edit or add text.
2. Do a keyboard copy-paste, or if you have a keyboard that supports diacritic marks, type directly into the list view.
3. **Tab** or move the cursor out of the field.

To delete text, do the following:

1. Double-click the cell you want to delete.
2. In the list view, select the text and press **Delete**.
3. **Tab** or move the cursor out of the field.

#### Translation field

To edit or add text, do the following:

1. In the list view, single-click the cell where you want to edit or add text.
2. In the **Translation** field, do a keyboard copy-paste, or if you have a keyboard that supports diacritic marks, type directly into the **Translation** field.
3. **Tab** or move the cursor out of the field.

To delete text, do the following:

1. Single-click the cell you want to delete.
2. In the **Translation** field, select the text and press **Delete**.

## Add and delete keys

In the Translations Editor, the **Key** column lists the unique identifiers for each
data item in your `strings.xml` files. You can add and delete keys through the
Translations Editor. When you delete a key, the Translations Editor deletes it and all of its
associated translations. The Translations Editor uses the Safe Delete refactoring to
delete a key so you know if the key text is used elsewhere and have a chance
to make necessary adjustments before you delete the key. The Safe Delete refatoring ensures that
your code still compiles after you delete the key.

To add a key, do the following:

1. In the **Translations Editor** , click **Add Key** ![](https://developer.android.com/static/studio/images/buttons/add-sign-green-icon.png).
2. In the dialog, enter a key name, default value, and the location of the default **strings.xml** file. ![](https://developer.android.com/static/studio/images/write/addkey_2x.png)

   **Figure 3.** Add a key

To delete a key, do the following:

1. In the Translations Editor, select the key you want to delete.
2. Click **Remove Keys** ![](https://developer.android.com/static/studio/images/buttons/ic_minus.png).
3. In the **Delete** dialog, decide if you want a safe delete and whether you
   want to search in comments and strings, and click **OK**.

   ![](https://developer.android.com/static/studio/images/write/translations-editor-delete-dialog_2x.png)

   **Figure 4.** Delete dialog


   If there are no references (usages) to the deleted key, or if all references are safely
   collapsible, the key is deleted. Otherwise, the Translations Editor displays the
   **Usages Detected** dialog with information about the problems detected.
   ![](https://developer.android.com/static/studio/images/write/translations-editor-usages-detected_2x.png)

   **Figure 5.** Delete dialog
4. Select **View Usages** to review what will be deleted. The **Find Safe Delete
   Conflicts** dialog shows all of the usages that are not safe to delete so you can edit your corresponding code. ![](https://developer.android.com/static/studio/images/write/translations-editor-delete-key_2x.png)

   **Figure 6.** Unsafe usages
5. Right-click a usage to display the context menu and select **Jump to Source** so you can make the needed changes.
6. In the **Find Safe Delete Conflicts** panel, select **Rerun Safe Delete** to make sure there are no other usages that need attention.
7. When the usages are cleaned up, click **Do Refactor** to delete the key.

## Correct errors


Figure 7 shows the **Translations Editor** displaying the contents of the English, Spanish,
and French
`strings.xml` files. The red text indicates lines that have errors.
![](https://developer.android.com/static/studio/images/write/translations-editor_2x.png)

**Figure 7.** Red text indicates an error condition that you
must fix

To correct an error, hover over the red text to display an explanation of the problem and its
resolution.


When you make changes in the **Translations Editor** , the underlying
`strings.xml` files update with your changes. When you make
changes in a `strings.xml` file, the corresponding column in the **Translations Editor**
updates with your changes.

Example **Translations Editor** corrections:

- Figure 7 shows that the **app_name** row has **Untranslatable** checked, but there is a Spanish translation provided. Delete the Spanish translation to correct the error.
- Figure 7 shows that the **next_page** row is missing a French translation. Use your keyboard to copy **Page Suivante** into the cell to correct the error. A keyboard copy-paste operation copies the text with the diacritic marks into the cell.

## Display translated text in the Design Editor


To see how the translated text displays in your app layout, toggle the
text between the default and translated versions in the Design Editor, as follows:

1. In the **Project \> Android** panel on the left, select **<var translate="no">ModuleName</var> \> res \> layout**.
2. Double-click **content_main.xml** to open it for editing.
3. Click the **Design** tab in the lower-left corner to display the **Design** Editor.
4. In the Design Editor, select the **Language** ![](https://developer.android.com/static/studio/images/buttons/layout-editor-language-icon.png) drop-down list.
5. Select **Edit Translations** ![](https://developer.android.com/static/studio/images/buttons/translations-edit-icon.png).
6. Select the language you want to use to view your app.
   ![](https://developer.android.com/static/studio/images/write/spanish-language_2x.png)

   **Figure 8.** The language drop-down list with Spanish selected

The Design Editor displays your app layout in the selected language, which in this case is
Spanish.
![](https://developer.android.com/static/studio/images/write/spanish-translation_2x.png)

**Figure 9.** The Design Editor displaying translated text in
Spanish

## Set the Design Editor to the default language


To set the language back to the default, select **es \> Language**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-language-icon.png).
![](https://developer.android.com/static/studio/images/write/changelanguage_2x.png)

**Figure 10.** Set to the default language

## Manage and test localizable text


The Android platform and Android Studio provide several features to help you manage and test
your localizable app
text. These features have options to help you target issues with right-to-left (RTL) scripts,
such as Arabic or Hebrew. Testing your localizable text allows you to make adjustments to the UI
text and its layout before you commit your messages to the source repository to be sent for
translation later.

### Refactor your project for RTL support


Android Studio has a refactoring command that enables support for bidirectional text
in [`TextView`](https://developer.android.com/reference/android/widget/TextView),
[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout), and
[`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout) elements so
your apps can display and allow users to edit text in both left-to-right (LTR) and right-to-left
(RTL) scripts. The command also provides automatic mirroring of app UI layouts and all view
widgets. To see the text direction change and the layout mirroring, you must also set the
[text and layout direction properties](https://developer.android.com/studio/write/translations-editor#direction)
in the [Layout Editor](https://developer.android.com/studio/write/layout-editor.html).


The following procedure shows how to refactor your project for RTL support:

1. Select **Refactor \> Add RTL support where possible** to display the dialog shown in figure 11. ![](https://developer.android.com/static/studio/images/write/localize-add-rtl-support_2x.png)

   **Figure 11.** Add RTL support
   - If the `<application>` element in your `AndroidManifest.xml` file does not have the `android:supportsRTL="true"` attribute, then select the **Update AndroidManifest.xml** checkbox.
   - If your app's `targetSdkVersion` is 17 or higher, select **Replace Left/Right Properties with Start/End Properties** . In this case, your properties should use "start" and "end" instead of "left" and "right". For example, `android:paddingLeft` becomes `android:paddingStart`.
   - If your app's `targetSdkVersion` is 16 or less, select **Generate -v17 Versions** In this case, your XML should use both sets of properties. For example, your XML should use both `android:paddingLeft` and `android:paddingStart`.
2. To display the **Find Refactoring Preview** window, click **Run** . ![](https://developer.android.com/static/studio/images/write/localize-find-refactor-preview_2x.png)

   **Figure 12.** Check the preview
3. Click **Do Refactor**.


For more information about refactoring your project for RTL support, see
[Native RTL support in Android 4.2](https://android-developers.googleblog.com/2013/03/native-rtl-support-in-android-42.html).

### Text and layout direction properties


The Properties window on the right provides the **textDirection** property to use with
text widgets and the **layoutDirection** property to use with layout widgets to
change the direction of text and layout components. The direction properties are listed in
the **Properties** window on the right, and work with API Level 17 or higher.


To see the text direction change and the layout mirroring, you must also
[refactor](https://developer.android.com/studio/write/translations-editor#refactor) the project for RTL support. In English, the text direction
change moves only punctuation from the right side to the
left side of the text; for example, "Hello World!" becomes "!Hello World". To see LTR text
switch to RTL, you have to use an RTL language in your app. If you want to use English and see
the text switch to RTL for testing purposes, use [pseudolocales](https://developer.android.com/studio/write/translations-editor#pseudolocales).
Pseudolocales are independent of the refactoring command and the direction properties.


To access and use the direction properties, do the following:

1. In the [Layout Editor](https://developer.android.com/studio/write/layout-editor#intro), select a text widget.
2. Open the **Properties** window and search for the RTL property you want to use.


   To set the property value, select one of the following:
   - **firstStrong:** Default for the root view. The first strong directional character determines the paragraph direction. If there is no strong directional character, the paragraph direction is the view's resolved layout direction.
   - **anyRtl:** The paragraph direction is RTL if it contains any strong RTL character; otherwise, it is LTR if it contains any strong LTR characters. If there are neither, the paragraph direction is the view's resolved layout direction.
   - **ltr:** The paragraph direction is LTR.
   - **rtl:** The paragraph direction is RTL.
   - **locale:** The paragraph direction comes from the system locale.
   - **inherit:** Default. Use the direction set in the parent.

   > [!NOTE]
   > **Note:** Strong directional characters have their own predefined direction, such as most alphabetic and syllabic characters, non-European and non-Arabic digits, Han ideographs, and punctuation characters that are specific to only those scripts.

3. To review the reversed text and layout, run the app.

### Pseudolocales


A pseudolocale is a simulated locale that is designed to assume the characteristics of languages
that cause
UI, layout, RTL, and other translation problems when an app is translated. Pseudolocales provide
instant and automatic translations that are readable in English for all localizable messages. This
makes it possible for you to catch untranslatable messages in your source code.


For information about how to use pseudolocales, see
[Test
Your App with Pseudolocales](https://developer.android.com/guide/topics/resources/pseudolocales).