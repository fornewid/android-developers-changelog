---
title: https://developer.android.com/agents/skills/system/glance-canonical-layouts/skill
url: https://developer.android.com/agents/skills/system/glance-canonical-layouts/skill
source: md.txt
---

To implement a widget Canonical Layout that follows the recommended design
patterns:

1. The project **MUST** use Jetpack Glance.
2. You **MUST** locate the requested layout from the list under **Canonical Layout Reference Files**.
3. Copy the layout reference files into your project's target app module (e.g., `src/main/java/` and `src/main/res/`) in one step to implement the exact design and reduce the number of tool calls.
4. You **MUST** set override val `sizeMode: SizeMode = SizeMode.Exact` in the widget provider class.
5. Validate that your project compiles, updating sample package declarations, import paths, and class names to match the target app's package name.
6. Clean your project's widget code, removing unused classes (for example, unused buttons).
7. You **MUST** register the widget receiver in `AndroidManifest.xml` inside `<application>` after `<activity>`, ensuring `android:resource="@xml/..."` matches the filename of the copied Widget Info XML. Otherwise, the widget won't appear in the widget picker:

<br />

```xml
<receiver android:name=".glance.MyReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
    </intent-filter>
    <meta-data
        android:name="android.appwidget.provider"
        android:resource="@xml/my_app_widget_info" />
</receiver>
```

<br />

## Dependencies

Add Jetpack Glance dependencies to the app module's `build.gradle.kts`
(`dependencies` block):

- `androidx.glance:glance-appwidget:1.2.0` or higher
- `androidx.glance:glance-material3:1.2.0` or higher
- `androidx.glance:glance-appwidget-preview:1.2.0` or higher
- `androidx.glance:glance-preview:1.2.0` or higher

Use version `1.3.0-alpha02` or higher with `compileSdk = 37` and Android Gradle
Plugin (AGP) 9.1.0 or higher (for example, `agp = "9.1.0"` in
`gradle/libs.versions.toml`) when implementing Snap Scrolling.

If copying sample data repositories that load bitmaps with Coil (such as
`FakeImageGridDataRepository.kt`, `FakeImageTextListDataRepository.kt`, or
`FakeTextWithImageRepository.kt`), also add an image loading library dependency
such as `io.coil-kt:coil` (e.g., `implementation("io.coil-kt:coil:2.7.0")`) if
one doesn't already exist.

## Canonical layout reference files

#### Action list layout (`action_list`)

- **Widget Provider** : [ActionListAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/ActionListAppWidget.kt.rawcontent)
- **Layout Composable** : [ActionListLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ActionListLayout.kt.rawcontent)
- **Widget Info XML** : [sample_action_list_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_action_list_widget_info.xml.rawcontent)
- **Data Repository** : [FakeActionListDataRepository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeActionListDataRepository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_action_list_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_action_list_preview.png), [sample_home_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_home_icon.xml.rawcontent), [sample_power_settings_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_power_settings_icon.xml.rawcontent), [sample_bulb_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_bulb_icon.xml.rawcontent), [sample_thermostat_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_thermostat_icon.xml.rawcontent), [sample_ac_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_ac_icon.xml.rawcontent), [sample_door_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_door_icon.xml.rawcontent), [sample_arrow_right_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_arrow_right_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
- **Components** : [RoundedScrollingLazyVerticalGrid.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyVerticalGrid.kt.rawcontent), [ListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent), [VerticalListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent), [RoundedScrollingLazyColumn.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
- **Utilities** : [CollectionsKtx.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ActionUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Additional References** : [CanonicalLayoutActivity.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CanonicalLayoutActivity.kt.rawcontent), [ActionDemonstrationActivity.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ActionDemonstrationActivity.kt.rawcontent)
- **Guidance** :
  - Handle list item actions with Glance action callbacks and ensure proper state updates.

#### Check list layout (`check_list`)

- **Widget Provider** : [CheckListAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/CheckListAppWidget.kt.rawcontent)
- **Layout Composable** : [CheckListLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/CheckListLayout.kt.rawcontent)
- **Widget Info XML** : [sample_check_list_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_check_list_widget_info.xml.rawcontent)
- **Data Repository** : [FakeCheckListDataRepository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeCheckListDataRepository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_check_list_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_check_list_preview.png), [sample_pin_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_pin_icon.xml.rawcontent), [sample_checked_circle_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_checked_circle_icon.xml.rawcontent), [sample_circle_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_circle_icon.xml.rawcontent), [sample_delete_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample_edit_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent), [sample_snooze_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_snooze_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
- **Components** : [ListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent), [VerticalListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent), [RoundedScrollingLazyColumn.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
- **Utilities** : [CollectionsKtx.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ActionUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Implement checkbox state toggling using action parameters or callbacks to update collection items.
  - Use Glance Action callbacks (for example, `actionRunCallback`, `ActionCallback(actionParametersOf(...)` or `actionStartActivity(...)`) for widget onClick parameters to handle click events like tapping a checkbox.

#### Expressive toolbar layout (`expressive_toolbar`)

- **Widget Provider** : [ExpressiveToolbarAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/ExpressiveToolbarAppWidget.kt.rawcontent)
- **Layout Composable** : [ExpressiveToolbarLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/ExpressiveToolbarLayout.kt.rawcontent)
- **Widget Info XML** : [sample_expressive_toolbar_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_expressive_toolbar_widget_info.xml.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_expressive_toolbar_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_expressive_toolbar_preview.png), [four_side_cookie_background.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/four_side_cookie_background.xml.rawcontent), [sample_edit_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent), [sample_share_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_share_icon.xml.rawcontent), [sample_delete_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample_info_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample_file_upload_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_file_upload_icon.xml.rawcontent), [sample_mic_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent), [sample_camera_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent)
- **Components** : [Buttons.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
- **Utilities** : [ActionUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Avoid `ColorProvider` import errors: import `androidx.glance.unit.ColorProvider` and use `androidx.glance.color.ColorProvider(dayColor, nightColor)`.
  - Use `GlanceModifier.background(Color)` directly for solid background colors rather than `ColorProvider`.

#### Image grid layout (`image_grid`)

- **Widget Provider** : [ImageGridAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/ImageGridAppWidget.kt.rawcontent)
- **Layout Composable** : [ImageGridLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ImageGridLayout.kt.rawcontent)
- **Widget Info XML** : [sample_image_grid_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_image_grid_widget_info.xml.rawcontent)
- **Data Repository** : [FakeImageGridDataRepository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeImageGridDataRepository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_image_grid_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_image_grid_preview.png), [sample_placeholder_image.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample_grid_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_grid_icon.xml.rawcontent), [sample_refresh_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
- **Components** : [RoundedScrollingLazyVerticalGrid.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyVerticalGrid.kt.rawcontent), [EmptyListContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent), [VerticalListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent)
- **Utilities** : [CollectionsKtx.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ImageUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageUtils.kt.rawcontent), [ImageAspectRatio.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Use solid colors (`GlanceModifier.background`) or local drawables for image items unless an image loading library is configured or requested.

#### Image text list layout (`image_text_list`)

- **Widget Provider** : [ImageTextListAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/ImageTextListAppWidget.kt.rawcontent)
- **Layout Composable** : [ImageTextListLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ImageTextListLayout.kt.rawcontent)
- **Widget Info XML** : [sample_image_text_list_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_image_text_list_widget_info.xml.rawcontent)
- **Data Repository** : [FakeImageTextListDataRepository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeImageTextListDataRepository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_image_text_list_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_image_text_list_preview.png), [sample_placeholder_image.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample_image_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_image_icon.xml.rawcontent), [sample_heart_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_heart_icon.xml.rawcontent), [sample_refresh_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
- **Components** : [ListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent), [VerticalListItem.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent), [RoundedScrollingLazyColumn.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
- **Utilities** : [CollectionsKtx.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ImageUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageUtils.kt.rawcontent), [ImageAspectRatio.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Common Use Cases: News feeds, article lists, workout histories, message feeds, and vertical thumbnail lists.
  - Balance list row height and text clipping when combining thumbnail images with primary and secondary text.

#### Long text layout (`long_text`)

- **Widget Provider** : [LongTextAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/LongTextAppWidget.kt.rawcontent)
- **Layout Composable** : [LongTextLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/layout/LongTextLayout.kt.rawcontent)
- **Widget Info XML** : [sample_long_text_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_long_text_widget_info.xml.rawcontent)
- **Data Repository** : [FakeLongTextRespository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/data/FakeLongTextRespository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_long_text_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_long_text_preview.png), [sample_text_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_text_icon.xml.rawcontent), [sample_refresh_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent)
- **Utilities** : [FontUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Import `androidx.compose.ui.unit.times` if multiplying Dp (for example, `2 * padding`).
  - Follow sizing rules: ensure dimensions from dimens.xml are used for padding and typography scaling.

#### Search toolbar layout (`search_toolbar`)

- **Widget Provider** : [SearchToolBarAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/SearchToolBarAppWidget.kt.rawcontent)
- **Layout Composable** : [SearchToolBarLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/SearchToolBarLayout.kt.rawcontent)
- **Widget Info XML** : [sample_search_toolbar_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_search_toolbar_widget_info.xml.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_search_toolbar_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_search_toolbar_preview.png), [sample_search_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_search_icon.xml.rawcontent), [sample_refresh_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample_mic_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent), [sample_camera_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent), [sample_delete_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample_pin_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_pin_icon.xml.rawcontent)
- **Components** : [Buttons.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
- **Utilities** : [ActionUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Avoid `ColorProvider` import errors: import `androidx.glance.unit.ColorProvider` and use `androidx.glance.color.ColorProvider(dayColor, nightColor)`.
  - Use `GlanceModifier.background(Color)` directly for solid background colors rather than `ColorProvider`.

#### Full-bleed image layout and snap scrolling (`snap_scrolling`)

- **Widget Provider** : [FullBleedImageAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/FullBleedImageAppWidget.kt.rawcontent)
- **Layout Composable** : [FullBleedImageLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/layout/FullBleedImageLayout.kt.rawcontent)
- **Widget Info XML** : [sample_full_bleed_image_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_full_bleed_image_widget_info.xml.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_full_bleed_image_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_full_bleed_image_preview.png), [sample_scrim_gradient.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_scrim_gradient.xml.rawcontent), [sample_placeholder_image.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample_app_logo.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_app_logo.xml.rawcontent), [sample_info_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent)
- **Utilities** : [FontUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [ImageAspectRatio.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Set `verticalScrollMode =
    VerticalScrollMode.SnapScrollMatchHeight(size.height)` on `LazyColumn` for Snap Scrolling.
  - Glance 1.3.0-alpha02 (or higher), Compile SDK 37 (Baklava) or higher, and Android Gradle Plugin (AGP) 9.1.0 or higher are required if implementing Snap Scrolling.
  - Set override val sizeMode: SizeMode = SizeMode.Exact in the widget provider class.

#### Standard toolbar layout (`standard_toolbar`)

- **Widget Provider** : [ToolBarAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/ToolBarAppWidget.kt.rawcontent)
- **Layout Composable** : [ToolBarLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/ToolBarLayout.kt.rawcontent)
- **Widget Info XML** : [sample_toolbar_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_toolbar_widget_info.xml.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_toolbar_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_toolbar_preview.png), [sample_app_logo.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_app_logo.xml.rawcontent), [sample_search_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_search_icon.xml.rawcontent), [sample_add_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample_edit_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent), [sample_share_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_share_icon.xml.rawcontent), [sample_mic_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent), [sample_camera_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent), [sample_videocam_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_videocam_icon.xml.rawcontent)
- **Components** : [Buttons.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
- **Utilities** : [ActionUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Additional References** : [CanonicalLayoutActivity.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/CanonicalLayoutActivity.kt.rawcontent)
- **Guidance** :
  - See Troubleshooting to avoid `ColorProvider` import errors: use androidx.glance.color.ColorProvider(dayColor, nightColor).
  - Use GlanceModifier.background(Color) directly for solid background colors rather than `ColorProvider`.

#### Text with image layout (`text_with_image`)

- **Widget Provider** : [TextWithImageAppWidget.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/TextWithImageAppWidget.kt.rawcontent)
- **Layout Composable** : [TextWithImageLayout.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/layout/TextWithImageLayout.kt.rawcontent)
- **Widget Info XML** : [sample_text_with_image_widget_info.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_text_with_image_widget_info.xml.rawcontent)
- **Data Repository** : [FakeTextWithImageRepository.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/text/data/FakeTextWithImageRepository.kt.rawcontent)
- **Dimensions** : [dimens.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
- **Strings** : [strings.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
- **Drawables** : [sample_text_image_preview.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_text_image_preview.png), [sample_text_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_text_icon.xml.rawcontent), [sample_refresh_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample_placeholder_image.png](https://developer.android.com/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample_info_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent), [sample_no_data_icon.xml](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent)
- **Utilities** : [FontUtils.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [ImageAspectRatio.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
- **Theme** : [Color.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](https://developer.android.com/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
- **Guidance** :
  - Follow responsive layout sizing rules to accommodate text and image side-by-side or stacked based on available widget dimensions.

## Troubleshooting

1. **Background Colors** : Use `GlanceModifier.background(Color)` directly for solid background colors rather than `ColorProvider`, otherwise the background will be transparent.
2. **When using `ColorProvider` (outside of the background), avoid import errors** :
   1. Import type: `import androidx.glance.unit.ColorProvider`
   2. Use fully qualified creator: `androidx.glance.color.ColorProvider(dayColor, nightColor)`

## Checklist

- \[ \] Did you register the widget in the AndroidManifest?
- \[ \] Did you copy the corresponding **Widget Info XML** file and leave the given values including `minWidth`, `minHeight`, and `minResizeHeight` unchanged?
- \[ \] Did you use the given Glance Theme color values from the corresponding **Layout Composable** file?
- \[ \] Did you use dimension resource references for `android:minWidth` and `android:minHeight` in appwidget-provider XML definitions?
- \[ \] Did you override `val sizeMode: SizeMode = SizeMode.Exact` in the widget provider class?