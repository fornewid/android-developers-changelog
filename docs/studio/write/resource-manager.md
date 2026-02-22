---
title: https://developer.android.com/studio/write/resource-manager
url: https://developer.android.com/studio/write/resource-manager
source: md.txt
---

# Manage your app&#39;s UI resources with Resource Manager

Resource Manager is a tool window for importing, creating, managing, and using resources in your app. To open the tool window, select**View \> Tool Windows \> Resource Manager** from the menu or select**Resource Manager**in the left side bar.

![](https://developer.android.com/static/images/studio/write/resource-manager-2x.png)

**Figure 1.**The Resource Manager tool window.

1. Click**Add** ![](https://developer.android.com/static/studio/images/buttons/ic_plus_dark.png)to add a new resource to your project. You can add image assets, vector assets, fonts, or resource files and values, or you can[import drawables](https://developer.android.com/studio/write/resource-manager#import)into your project.
2. Select a module to view resources specific to that module.
3. Search for a resource across all modules in your project using the search bar.
4. Display your resources according to[type](https://developer.android.com/guide/topics/resources/available-resources)in the Resource Manager. Use these tabs to switch between resource types. Click the overflow icon![overflow icon](https://developer.android.com/static/images/studio/write/overflow-icon-2x.png)to show additional resource types.
5. Filter the displayed resources from local dependent modules, external libraries, and the Android framework using the filter button. You can also use the filter to show theme attributes.
6. Preview your resources in the main content area. Right-click a resource to see a context menu where you can rename the resource and search your app for where the resource is used.
7. Click these buttons to view your resources as either tiles or lists.
8. Click these buttons to change the preview size of your resources.

In addition to these features, the Resource Manager provides a way to bulk-import drawables into your project. To bulk-import, you can either:

- Drag your image files---including SVG files---directly onto the Resource Manager.
- Use the**Import Drawables**wizard.

For more information, see the[Import drawables into your project](https://developer.android.com/studio/write/resource-manager#import)section.

To see more detailed information, double-click a resource in Resource Manager. If you have multiple versions of a resource, this detailed view displays each version along with any associated qualifiers, as shown in figure 2. From here, you can double-click a specific version to open it in an editor window.

![](https://developer.android.com/static/images/studio/write/resource-manager-flowers-2x.png)

**Figure 2.**The Resource Manager showing versions of an image resource for different screen densities.

## Import drawables into your project

You can use the Resource Manager to import image resources into your project. For a list of supported image types, see[Image support](https://developer.android.com/guide/topics/media/media-formats#image-formats).

To import image resources into your project, do the following:

1. Drag your images directly onto the**Resource Manager**window in Android Studio.

   - Alternatively, you can:
     1. Click the plus icon (**+**).
     2. Choose**Import Drawables**, as shown in figure 3.
     3. Select the files and folders that you want to import.

   ![](https://developer.android.com/static/images/studio/write/import-drawables-menu-2x.png)

   **Figure 3.** Select**Import Drawables**from the menu.
2. The**Import drawables**dialog appears, as shown in figure 4. This dialog displays a list of the resources you're importing. You can rename resources by clicking the text box above a resource's preview.

   If you're providing multiple versions of the same resource, add[device configuration qualifiers](https://developer.android.com/studio/write/resource-manager#automatic-parsing), as described in the following section, that describe the specific configuration that each resource supports.

   For example, if you're providing multiple versions of the same resource for different screen densities, you can add a**Density**qualifier for each version. Note that if two or more resources have the same name and qualifiers, only one version is imported.

   For more information on resource qualifiers, see[Providing alternative resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources).

   ![](https://developer.android.com/static/images/studio/write/import-drawables-add-qualifiers-2x.png)

   **Figure 4.** The**Import drawables**dialog.

   Once you've named your resources and added any necessary qualifiers, click**Next**.
3. The next screen shows a summary of the resources you're importing. When you're ready to import, click**Import**.

In the**Resource Manager**window, your resources are now ready for you to use in your project, as shown in figure 5.

![](https://developer.android.com/static/images/studio/write/resource-manager-after-import-2x.png)

**Figure 5.**The Resource Manager now shows your imported images.

### Automatically parse drawable densities

When you import a file or folder and its path contains a density qualifier, the Resource Manager automatically applies the density qualifier as part of the import. The Resource Manager can parse both Android's density qualifiers and iOS's scale factors.

This table lists how different supported densities are represented for Android and iOS:

|                  Density                   | Android density qualifier | iOS scaling factor |
|--------------------------------------------|---------------------------|--------------------|
| Low-density (\~120 dpi)                    | `ldpi`                    | not supported      |
| Medium-density (\~160 dpi)                 | `mdpi`                    | original scale     |
| High-density (\~240 dpi)                   | `hdpi`                    | not supported      |
| Extra-high-density (\~320 dpi)             | `xhdpi`                   | @2x                |
| Extra-extra-high-density (\~480 dpi)       | `xxhdpi`                  | @3x                |
| Extra-extra-extra-high-density (\~640 dpi) | `xxxhdpi`                 | @4x                |

Here are some examples of how input paths translate to resource paths after import:

Android density qualifier:`hdpi`
:   **Input path:** /UserFolder/icon1/***hdpi*** /icon.png  
    **Resource path:** *\<projectFolder\>* /*\<moduleFolder\>* /src/main/res/***drawable-hdpi***/icon.png

Android density qualifier:`xxhdpi`
:   **Input path:** /UserFolder/icon1/abc-***xxhdpi*** /icon.png  
    **Resource path:** *\<projectFolder\>* /*\<moduleFolder\>* /src/main/res/***drawable-xxhdpi***/icon.png

iOS scaling factor: @2x
:   **Input path:** /UserFolder/icon1/icon***@2x*** .png  
    **Resource path:** *\<projectFolder\>* /*\<moduleFolder\>* /src/main/res/***drawable-xhdpi***/icon.png

iOS scaling factor: @2x
:   **Input path:** /UserFolder/icon1/icon***@2x*** _alternate.png  
    **Resource path:** *\<projectFolder\>* /*\<moduleFolder\>* /src/main/res/***drawable-xhdpi***/icon_alternate.png

For more information on supporting devices with different pixel densities, see[Support different pixel densities](https://developer.android.com/training/multiscreen/screendensities).

## Drag drawables into your layout

You can drag drawables from the Resource Manager directly onto a layout. When you drag a resource onto a layout, the Resource Manager creates a corresponding`ImageView`for that drawable, as shown in animation 1:

![](https://developer.android.com/static/images/studio/write/resource-manager-drag-and-drop-design.gif)

**Animation 1.** Drag drawables onto a layout in**Design**view.

You can also drag directly onto the XML of the layout, as shown in animation 2:

![](https://developer.android.com/static/images/studio/write/resource-manager-drag-and-drop-xml.gif)

**Animation 2.** Drag drawables onto a layout in**Text**view.

When dragging a drawable onto a layout in the**Text**tab, the generated code differs depending on where you place the drawable in the layout:

- If you drag a drawable onto a blank area, the Resource Manager generates a corresponding`ImageView`.
- If you drag a drawable onto any attribute in the layout XML, the Resource Manager replaces that attribute value with a reference to the drawable. You can also drag any other resource type onto an XML attribute to replace the attribute value.
- If you drag a drawable onto an existing`ImageView`element, the Resource Manager replaces the corresponding source attribute.