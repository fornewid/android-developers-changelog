---
title: https://developer.android.com/studio/write/layout-editor
url: https://developer.android.com/studio/write/layout-editor
source: md.txt
---

# Develop a UI with Views

| **Note:** We recommend building your UI with Compose instead of Views where possible. To learn how to preview your Compose UI, see[Compose previews](https://developer.android.com/jetpack/compose/tooling/previews).

The Layout Editor enables you to quickly build`View`-based layouts by dragging UI elements into a visual design editor instead of writing layout XML. The design editor can preview your layout on different Android devices and versions, and you can dynamically resize the layout to be sure it works properly on different screen sizes.

The Layout Editor is especially powerful when[building a layout with`ConstraintLayout`](https://developer.android.com/training/constraint-layout).

This page provides an overview of the Layout Editor. To learn more about layout fundamentals, see[Layouts](https://developer.android.com/guide/topics/ui/declaring-layout).

## Introduction to the Layout Editor

The Layout Editor appears when you open an XML layout file.
![layout editor](https://developer.android.com/static/studio/images/write/layout-editor.png)**Figure 1.**The Layout Editor.

1. **Palette**: contains various views and view groups that you can drag into your layout.
2. **Component Tree**: shows the hierarchy of components in your layout.
3. **Toolbar**: has buttons that configure your layout appearance in the editor and change layout attributes.
4. **Design editor**: lets you edit your layout in Design view, Blueprint view, or both.
5. **Attributes**: has controls for the selected view's attributes.
6. **View mode** : lets you view your layout in either**Code** ![code mode icon](https://developer.android.com/static/images/studio/write/code-mode-icon-2x.png),**Split** ![split mode icon](https://developer.android.com/static/images/studio/write/split-mode-icon-2x.png), or**Design** ![design mode icon](https://developer.android.com/static/images/studio/write/design-mode-icon-2x.png)modes.**Split** mode shows the**Code** and**Design**windows at the same time.
7. **Zoom and pan controls**: control the preview size and position within the editor.

When you open an XML layout file, the design editor opens by default, as shown in figure 1. To edit the layout XML in the text editor, click the**Code** ![code mode icon](https://developer.android.com/static/images/studio/write/code-mode-icon-2x.png)button in the top-right corner of the window. Note that the**Palette** ,**Component Tree** , and**Attributes** panels are not available while editing your layout in**Code**view.

**Tip:** To switch between design and text editors, press`Alt`(`Control`on macOS) plus`Shift`and the right or left arrow key.

## Change the preview appearance

The buttons in the top row of the design editor let you configure the appearance of your layout in the editor.
![Buttons in the Layout Editor toolbar that configure the layout appearance](https://developer.android.com/static/studio/images/write/layout-editor-toolbar.png)**Figure 2.**Buttons in the Layout Editor toolbar that configure the layout appearance.

1. **Design and Blueprint** : Select how you want to view your layout in the editor. You can also press`B`to cycle through these view types.
   - Choose**Design**to see a rendered preview of your layout.
   - Choose**Blueprint**to see only outlines for each view.
   - Choose**Design + Blueprint**to see both views side by side.
2. **Screen orientation and layout variants** : Choose between landscape or portrait screen orientation or choose other screen modes that your app provides alternative layouts for, such as night mode. This menu also contains commands for[creating a new layout variant](https://developer.android.com/studio/write/layout-editor#create-variant), as described in a section on this page. You can also press the letter`O`on your keyboard to change orientation.
3. **System UI Mode** : If you've enabled[dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)in your app, switch wallpapers and see how your layouts react to different users chosen wallpaper. Note that you must first change the theme to a Material dynamic color theme, then change the wallpaper.

4. **Device type and size** : Select the device type (phone/tablet, Android TV, or Wear OS) and screen configuration (size and density). You can select from several pre-configured device types and your own AVD definitions, and you can create a new AVD by selecting**Add Device Definition**from the list, as shown in figure 3.

   - To resize the device, drag the bottom-right corner of the layout.
   - Press`D`to cycle through the device list.

   Testing your layout against the**Reference Devices**in this menu helps your app scale well to layout states on real devices.
   ![The device list menu with Reference Devices](https://developer.android.com/static/studio/images/releases/new-device-picker.png)**Figure 3.**The device list showing Reference Devices.
5. **API version**: Select the version of Android to preview your layout. The list of available Android versions depends on which SDK platform versions you have installed using SDK Manager.

6. **App theme**: Select which UI theme to apply to the preview. This works only for supported layout styles, so many themes in this list result in an error.

7. **Language** : Select the language to show for your UI strings. This list displays only the languages available in your string resources. If you'd like to edit your translations, click**Edit Translations** from the menu. For more information on working with translations, see[Localize the UI with Translations Editor](https://developer.android.com/studio/write/translations-editor).

| **Note:** Unless you add a new layout file from**Layout Variants**, these configurations don't affect your app's code or manifest. They affect only the layout preview.

## Create a new layout

When adding a new layout for your app, first create a default layout file in your project's default`layout/`directory so that it applies to all device configurations. Once you have a default layout, you can[create layout variations](https://developer.android.com/studio/write/layout-editor#create-variant), as described in a section on this page, for specific device configurations, such as for large screens.

You can create a new layout in one of the following ways:

### Use Android Studio's main menu

1. In the**Project**window, click the module you want to add a layout to.
2. In the main menu, select**File \> New \> XML \> Layout XML File**.
3. In the dialog that appears, provide the filename, the root layout tag, and the source set where the layout belongs.
4. Click**Finish**to create the layout.

### Use the Project view

1. Choose the**Project** view from within the**Project**window.
2. Right-click the layout directory where you'd like to add the layout.
3. In the context menu that appears, click**New \> Layout Resource File**.

### Use the Android view

1. Choose the**Android** view from within the**Project**window.
2. Right-click the`layout`folder.
3. In the context menu that appears, select**New \> Layout Resource File**.

### Use the Resource Manager

1. In the[Resource Manager](https://developer.android.com/studio/write/resource-manager), select the**Layout**tab.
2. Click the`+`button, and then click**Layout Resource File**.

## Use layout variants to optimize for different screens

A*layout variant*is an alternative version of an existing layout that is optimized for a certain screen size or orientation.

### Use a suggested layout variant

Android Studio includes common layout variants that you can use in your project. To use a suggested layout variant, do the following:

1. Open your default layout file.
2. Click the**Design** ![design mode icon](https://developer.android.com/static/images/studio/write/design-mode-icon-2x.png)icon in the top-right corner of the window.
3. The name of the layout file appears in the**Action to switch and create qualifiers for layout files**drop-down. Select the drop-down.
4. In the drop-down list, select a variant such as**Create Landscape Qualifier** or**Create Tablet Qualifier** .![The Create qualifiers dropdown](https://developer.android.com/static/studio/images/write/layout-editor-create-qualifiers_2x.png)**Figure 4.**Drop-down list of layout qualifiers.

A new layout directory is created.

### Create your own layout variant

If you'd like to create your own layout variant, do the following:

1. Open your default layout file.
2. Click the**Design** ![Design mode icon](https://developer.android.com/static/images/studio/write/design-mode-icon-2x.png)icon in the top-right corner of the window.
3. The name of the layout file appears in the**Action to switch and create qualifiers for layout files**drop-down. Select the drop-down.
4. In the drop-down list, select**Add Resource Qualifier**. (See figure 4 above.)

   The**Select Resource Directory**dialog appears.
5. In the**Select Resource Directory**dialog, define the resource qualifiers for the variant:

   1. Select a qualifier from the**Available qualifiers**list.
   2. Click the**Add** ![add qualifier button](https://developer.android.com/static/studio/images/buttons/add-arrows.png)button.
   3. Enter any required values.
   4. Repeat these steps to add other qualifiers.
6. Once you've added all of your qualifiers, click**OK**.

When you have multiple variations of the same layout, you can switch between them by selecting a variant from the**Action to switch and create qualifiers for layout files**drop-down.

For more information about how to create layouts for different displays, see[Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes).

## Convert a view or layout

You can convert a view to another kind of view, and you can convert a layout to another kind of layout:

1. Click the**Design**button in the top-right corner of the editor window.
2. In the**Component Tree** , right-click the view or layout, and then click**Convert view**.
3. In the dialog that appears, choose the new type of view or layout, and then click**Apply**.

### Convert a layout to ConstraintLayout

For improved layout performance, convert older layouts to[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout).`ConstraintLayout`uses a constraint-based layout system that lets you build most layouts without any nested view groups.

To convert an existing layout to a`ConstraintLayout`, do the following:

1. Open an existing layout in Android Studio.
2. Click the**Design** ![design mode icon](https://developer.android.com/static/images/studio/write/design-mode-icon-2x.png)icon in the top-right corner of the editor window.
3. In the**Component Tree** , right-click the layout, and then click**Convert`your-layout-type`to ConstraintLayout**.

To learn more about`ConstraintLayout`, see[Build a Responsive UI with ConstraintLayout](https://developer.android.com/training/constraint-layout).

## Find items in the Palette

To search for a view or view group by name in the**Palette** , click the**Search** ![palette search button](https://developer.android.com/static/studio/images/buttons/search.png)button at the top of the palette. Alternatively, you can type the name of the item whenever the**Palette**window has focus.

In the**Palette** , you can find frequently used items in the**Common** category. To add an item to this category, right-click a view or view group in the**Palette** and then click**Favorite**in the context menu.

## Open documentation from the Palette

To open the Android Developers reference documentation for a view or view group, select the UI element in the**Palette** and press`Shift`+`F1`.

To view Material Guidelines documentation for a view or view group, right-click the UI element in the**Palette** and select**Material Guidelines** from the context menu. If no specific entry exists for the item, then the command opens the homepage of the[Material Guidelines documentation](https://material.io/guidelines/).

## Add views to your layout

To start building your layout, drag views and view groups from the**Palette**into the design editor. As you place a view in the layout, the editor displays information about the view's relationship with the rest of the layout.

If you are using`ConstraintLayout`, you can[automatically create constraints](https://developer.android.com/training/constraint-layout#use-autoconnect-and-infer-constraints)using the Infer Constraints and Autoconnect features.

## Edit view attributes

![The](https://developer.android.com/static/images/studio/write/layout-editor-attributes-2x.png)**Figure 5.** The**Attributes**panel.

You can edit view attributes from the**Attributes** panel in the Layout Editor. This window is available only when the design editor is open, so view your layout in either**Design** or**Split**mode to use it.

When you select a view, whether by clicking the view in the**Component Tree** or in the design editor, the**Attributes**panel shows the following, as indicated in figure 5:

1. **Declared Attributes** : Lists attributes specified in the layout file. To add an attribute, click the**Add** ![add attribute button](https://developer.android.com/static/studio/images/buttons/layout-editor-plus-icon.png)button at the top of the section.
2. **Layout** : Contains controls for the width and height of the view. If the view is in a`ConstraintLayout`, this section also shows constraint bias and lists the constraints that the view uses. For more information on controlling the size of views with`ConstraintLayout`, see[Adjust the view size](https://developer.android.com/training/constraint-layout#adjust-the-view-size).
3. **Common Attributes** : Lists common attributes for the selected view. To see all available attributes, expand the**All Attributes**section at the bottom of the window.
4. **Search**: Lets you search for a specific view attribute.
5. The icons to the right of each attribute value indicate whether the attribute values are resource references. These indicators are solid![solid indicator icon](https://developer.android.com/static/studio/images/buttons/layout-editor-indicator-solid.png)when the value is a resource reference and empty![empty indicator icon](https://developer.android.com/static/studio/images/buttons/layout-editor-indicator-empty.png)when the value is hardcoded to help you recognize hardcoded values at a glance.

   Click indicators in either state to open the**Resources**dialog, where you can select a resource reference for the corresponding attribute.
6. A red highlight around an attribute value indicates an error with the value. For example, an error might indicate an invalid entry for a layout-defining attribute.

   An orange highlight indicates a warning for the value. For example, a warning might appear when you use a hardcoded value where a resource reference is expected.

## Add sample data to your view

Because many Android layouts rely on runtime data, it can be difficult to visualize the look and feel of a layout while designing your app. You can add sample preview data to a`TextView`, an`ImageView`, or a`RecyclerView`from within the Layout Editor.
| **Note:** When you add sample data to a`View`, Android Studio makes changes to your project as though you were using your own data. You can then modify these changes as needed.

To display the**Design-time View Attributes** window, right-click one of these view types and choose**Set Sample Data**, as shown in figure 6.
![design time view attributes window](https://developer.android.com/static/images/studio/write/layout-editor-design-time-view-attributes-2x.png)**Figure 6.** The**Design-time View Attributes**window.

For a`TextView`, you can choose between different sample text categories. When using sample text, Android Studio populates the`text`attribute of the`TextView`with your chosen sample data. Note that you can choose sample text via the**Design-time View Attributes** window only if the`text`attribute is empty.
![text view with sample data](https://developer.android.com/static/images/studio/write/textview-sample-data-2x.png)**Figure 7.** A`TextView`with sample data.

For an`ImageView`, you can choose between different sample images. When you choose a sample image, Android Studio populates the`tools:src`attribute of the`ImageView`(or`tools:srcCompat`if using AndroidX).
![image view with sample data](https://developer.android.com/static/images/studio/write/imageview-sample-data-2x.png)**Figure 8.** An`ImageView`with sample data.

For a`RecyclerView`, you can choose from a set of templates that contain sample images and texts. When using these templates, Android Studio adds a file to your`res/layout`directory,`recycler_view_item.xml`, that contains the layout for the sample data. Android Studio also adds metadata to the`RecyclerView`to properly display the sample data.
![recycler view with sample data](https://developer.android.com/static/images/studio/write/recyclerview-sample-data-2x.png)**Figure 9.** A`RecyclerView`with sample data.

## Show layout warnings and errors

The Layout Editor notifies you of any layout issues next to the corresponding view in the**Component Tree** by using a red circle exclamation icon![red circle exclamation icon indicating a layout error](https://developer.android.com/static/studio/images/buttons/layout-editor-errors.png)for errors or an orange triangle exclamation icon![orange triangle exclamation icon indicating a layout warning](https://developer.android.com/static/studio/images/buttons/layout-editor-warnings-inline.png)for warnings. Click the icon to see more details.

To see all known issues in a window below the editor, click**Show Warnings and Errors** (![red circle exclamation icon indicating a layout error](https://developer.android.com/static/studio/images/buttons/layout-editor-errors.png)or![orange triangle exclamation icon indicating a layout warning](https://developer.android.com/static/studio/images/buttons/layout-editor-warnings-inline.png)) in the toolbar.

## Download fonts and apply them to text

When using Android 8.0 (API level 26) or the[Jetpack Core library](https://developer.android.com/jetpack/androidx/releases/core), you can select from hundreds of fonts by following these steps:

1. In the Layout Editor, click the**Design** ![design mode icon](https://developer.android.com/static/images/studio/write/design-mode-icon-2x.png)icon to view your layout in the design editor.
2. Select a text view.
3. In the**Attributes** panel, expand**textAppearance** , and then expand the**fontFamily**box.
4. Scroll to the bottom of the list and click**More Fonts** to open the**Resources**dialog.
5. In the**Resources** dialog, to select a font, browse the list or type into the search bar at the top. If you select a font under**Downloadable** , then you can either click**Create downloadable font** to load the font at runtime as a[downloadable font](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts)or click**Add font to project** to package the TTF font file in your APK. The fonts listed under**Android**are provided by the Android system, so they don't need to be downloaded or bundled in your APK.
6. Click**OK**to finish.

## Layout Validation

Layout Validation is a visual tool for simultaneously previewing layouts for different devices and display configurations, helping you catch problems in your layouts earlier in the process. To access this feature, click the**Layout Validation**tab in the top-right corner of the IDE window:

![Screenshot of Layout Validation tab](https://developer.android.com/static/studio/images/debug/layout-validation-tab.png)

**Figure 10**. Layout Validation tab.

To switch between the available configuration sets, select one of the following from the**Reference Devices**drop-down at the top of the Layout Validation window:

- Reference Devices
- Custom
- Color Blind
- Font Sizes

![Screenshot of drop-down menu in the Layout Validation tool](https://developer.android.com/static/studio/images/debug/li-ref-devices-dropdown.png)

**Figure 11**. Reference Devices drop-down.

### Reference Devices

Reference devices are a set of devices that we recommend you test against. They include phone, foldable, tablet, and desktop interfaces. You should preview how your layout appears on this set of reference devices:

![Screenshot of layout previews for different reference devices](https://developer.android.com/static/studio/images/debug/layout-validation-ref-devices-array.png)

**Figure 12**. Reference device previews in the Layout Validation tool.

### Custom

To customize a display configuration to preview, choose from a variety of settings including language, device, or screen orientation:

![Customize a device display in the Layout Validation tool](https://developer.android.com/static/studio/images/debug/layout-validation-custom.png)

**Figure 16**. Configure a custom display in the Layout Validation tool.

### Color Blind

To help make your app more accessible for users who are color blind, validate your layout with simulations of common types of color blindness:

![Screenshot of simulation previews for different types of color blindness](https://developer.android.com/static/studio/images/debug/layout-validation-color-blind.png)

**Figure 13**. Color blindness simulation previews in the Layout Validation tool.

### Font Sizes

Validate your layouts at various font sizes, and improve your app's accessibility for visually impaired users by testing your layouts with larger fonts:

![Previews of app layouts at different font sizes with visible layout errors for large fonts](https://developer.android.com/static/studio/images/debug/layout-validation-font-sizes.png)

**Figure 14**. Variable font size previews in the Layout Validation tool.