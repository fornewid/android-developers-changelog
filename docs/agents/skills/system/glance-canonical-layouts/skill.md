---
title: Glance canonical widget layout skill  |  Android Developers
url: https://developer.android.com/agents/skills/system/glance-canonical-layouts/skill
source: html-scrape
---

# Glance canonical widget layout skill Stay organized with collections Save and categorize content based on your preferences.





To implement a widget Canonical Layout that follows the recommended design
patterns:

1. The project **MUST** use Jetpack Glance.
2. You **MUST** locate the requested layout from the list under **Canonical Layout Reference Files**.
3. Copy the layout reference files into your project's target app module (e.g., `src/main/java/` and `src/main/res/`) in one step to implement the exact design and reduce the number of tool calls.
4. You **MUST** set override val `sizeMode: SizeMode = SizeMode.Exact` in the widget provider class.
5. Validate that your project compiles, updating sample package declarations, import paths, and class names to match the target app's package name.
6. Clean your project's widget code, removing unused classes (for example, unused buttons).
7. You **MUST** register the widget receiver in `AndroidManifest.xml` inside
   `<application>` after `<activity>`, ensuring `android:resource="@xml/..."`
   matches the filename of the copied Widget Info XML. Otherwise, the widget won't
   appear in the widget picker:

```
<receiver android:name=".glance.MyReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
    </intent-filter>
    <meta-data
        android:name="android.appwidget.provider"
        android:resource="@xml/my_app_widget_info" />
</receiver>

AndroidManifest.xml
```

## Dependencies

Add Jetpack Glance dependencies to the app module's `build.gradle.kts`
(`dependencies` block):

* `androidx.glance:glance-appwidget:1.2.0` or higher
* `androidx.glance:glance-material3:1.2.0` or higher
* `androidx.glance:glance-appwidget-preview:1.2.0` or higher
* `androidx.glance:glance-preview:1.2.0` or higher

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

* **Widget Provider**: [ActionListAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/collections/ActionListAppWidget.kt.rawcontent)
* **Layout Composable**: [ActionListLayout.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ActionListLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_action\_list\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_action_list_widget_info.xml.rawcontent)
* **Data Repository**: [FakeActionListDataRepository.kt](/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeActionListDataRepository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_action\_list\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_action_list_preview.png), [sample\_home\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_home_icon.xml.rawcontent),
  [sample\_power\_settings\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_power_settings_icon.xml.rawcontent), [sample\_bulb\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_bulb_icon.xml.rawcontent),
  [sample\_thermostat\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_thermostat_icon.xml.rawcontent), [sample\_ac\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_ac_icon.xml.rawcontent), [sample\_door\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_door_icon.xml.rawcontent),
  [sample\_arrow\_right\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_arrow_right_icon.xml.rawcontent), [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
* **Components**: [RoundedScrollingLazyVerticalGrid.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyVerticalGrid.kt.rawcontent), [ListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent),
  [VerticalListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent), [RoundedScrollingLazyColumn.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent),
  [NoDataContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
* **Utilities**: [CollectionsKtx.kt](/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ActionUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Additional References**: [CanonicalLayoutActivity.kt](/agents/skills/system/glance-canonical-layouts/references/CanonicalLayoutActivity.kt.rawcontent),
  [ActionDemonstrationActivity.kt](/agents/skills/system/glance-canonical-layouts/references/ActionDemonstrationActivity.kt.rawcontent)
* **Guidance**:
  + Handle list item actions with Glance action callbacks and ensure proper
    state updates.

#### Check list layout (`check_list`)

* **Widget Provider**: [CheckListAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/collections/CheckListAppWidget.kt.rawcontent)
* **Layout Composable**: [CheckListLayout.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/CheckListLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_check\_list\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_check_list_widget_info.xml.rawcontent)
* **Data Repository**: [FakeCheckListDataRepository.kt](/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeCheckListDataRepository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_check\_list\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_check_list_preview.png), [sample\_pin\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_pin_icon.xml.rawcontent),
  [sample\_checked\_circle\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_checked_circle_icon.xml.rawcontent), [sample\_circle\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_circle_icon.xml.rawcontent),
  [sample\_delete\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample\_edit\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent), [sample\_snooze\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_snooze_icon.xml.rawcontent),
  [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
* **Components**: [ListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent), [VerticalListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent),
  [RoundedScrollingLazyColumn.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
* **Utilities**: [CollectionsKtx.kt](/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ActionUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Implement checkbox state toggling using action parameters or callbacks to
    update collection items.
  + Use Glance Action callbacks (for example, `actionRunCallback`,
    `ActionCallback(actionParametersOf(...)` or `actionStartActivity(...)`) for
    widget onClick parameters to handle click events like tapping a checkbox.

#### Expressive toolbar layout (`expressive_toolbar`)

* **Widget Provider**: [ExpressiveToolbarAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/ExpressiveToolbarAppWidget.kt.rawcontent)
* **Layout Composable**: [ExpressiveToolbarLayout.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/ExpressiveToolbarLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_expressive\_toolbar\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_expressive_toolbar_widget_info.xml.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_expressive\_toolbar\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_expressive_toolbar_preview.png),
  [four\_side\_cookie\_background.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/four_side_cookie_background.xml.rawcontent), [sample\_edit\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent),
  [sample\_share\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_share_icon.xml.rawcontent), [sample\_delete\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample\_info\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent),
  [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample\_file\_upload\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_file_upload_icon.xml.rawcontent), [sample\_mic\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent),
  [sample\_camera\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent)
* **Components**: [Buttons.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
* **Utilities**: [ActionUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Avoid `ColorProvider` import errors: import
    `androidx.glance.unit.ColorProvider` and use
    `androidx.glance.color.ColorProvider(dayColor, nightColor)`.
  + Use `GlanceModifier.background(Color)` directly for solid background colors
    rather than `ColorProvider`.

#### Image grid layout (`image_grid`)

* **Widget Provider**: [ImageGridAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/collections/ImageGridAppWidget.kt.rawcontent)
* **Layout Composable**: [ImageGridLayout.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ImageGridLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_image\_grid\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_image_grid_widget_info.xml.rawcontent)
* **Data Repository**: [FakeImageGridDataRepository.kt](/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeImageGridDataRepository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_image\_grid\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_image_grid_preview.png),
  [sample\_placeholder\_image.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample\_grid\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_grid_icon.xml.rawcontent),
  [sample\_refresh\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent), [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
* **Components**: [RoundedScrollingLazyVerticalGrid.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyVerticalGrid.kt.rawcontent), [EmptyListContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent),
  [NoDataContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent), [VerticalListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent)
* **Utilities**: [CollectionsKtx.kt](/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ImageUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageUtils.kt.rawcontent), [ImageAspectRatio.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent),
  [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Use solid colors (`GlanceModifier.background`) or local drawables for image
    items unless an image loading library is configured or requested.

#### Image text list layout (`image_text_list`)

* **Widget Provider**: [ImageTextListAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/collections/ImageTextListAppWidget.kt.rawcontent)
* **Layout Composable**: [ImageTextListLayout.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ImageTextListLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_image\_text\_list\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_image_text_list_widget_info.xml.rawcontent)
* **Data Repository**: [FakeImageTextListDataRepository.kt](/agents/skills/system/glance-canonical-layouts/references/collections/data/FakeImageTextListDataRepository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_image\_text\_list\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_image_text_list_preview.png),
  [sample\_placeholder\_image.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png), [sample\_image\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_image_icon.xml.rawcontent),
  [sample\_heart\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_heart_icon.xml.rawcontent), [sample\_refresh\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent),
  [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent)
* **Components**: [ListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/ListItem.kt.rawcontent), [VerticalListItem.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/VerticalListItem.kt.rawcontent),
  [RoundedScrollingLazyColumn.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/RoundedScrollingLazyColumn.kt.rawcontent), [EmptyListContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/EmptyListContent.kt.rawcontent), [NoDataContent.kt](/agents/skills/system/glance-canonical-layouts/references/collections/layout/NoDataContent.kt.rawcontent)
* **Utilities**: [CollectionsKtx.kt](/agents/skills/system/glance-canonical-layouts/references/CollectionsKtx.kt.rawcontent), [ImageUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageUtils.kt.rawcontent), [ImageAspectRatio.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent),
  [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Common Use Cases: News feeds, article lists, workout histories, message
    feeds, and vertical thumbnail lists.
  + Balance list row height and text clipping when combining thumbnail images
    with primary and secondary text.

#### Long text layout (`long_text`)

* **Widget Provider**: [LongTextAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/text/LongTextAppWidget.kt.rawcontent)
* **Layout Composable**: [LongTextLayout.kt](/agents/skills/system/glance-canonical-layouts/references/text/layout/LongTextLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_long\_text\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_long_text_widget_info.xml.rawcontent)
* **Data Repository**: [FakeLongTextRespository.kt](/agents/skills/system/glance-canonical-layouts/references/text/data/FakeLongTextRespository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_long\_text\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_long_text_preview.png), [sample\_text\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_text_icon.xml.rawcontent),
  [sample\_refresh\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent)
* **Utilities**: [FontUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Import `androidx.compose.ui.unit.times` if multiplying Dp (for example, `2 * padding`).
  + Follow sizing rules: ensure dimensions from dimens.xml are used for padding
    and typography scaling.

#### Search toolbar layout (`search_toolbar`)

* **Widget Provider**: [SearchToolBarAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/SearchToolBarAppWidget.kt.rawcontent)
* **Layout Composable**: [SearchToolBarLayout.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/SearchToolBarLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_search\_toolbar\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_search_toolbar_widget_info.xml.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_search\_toolbar\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_search_toolbar_preview.png), [sample\_search\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_search_icon.xml.rawcontent),
  [sample\_refresh\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample\_mic\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent), [sample\_camera\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent),
  [sample\_delete\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_delete_icon.xml.rawcontent), [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample\_pin\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_pin_icon.xml.rawcontent)
* **Components**: [Buttons.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
* **Utilities**: [ActionUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Avoid `ColorProvider` import errors: import
    `androidx.glance.unit.ColorProvider` and use
    `androidx.glance.color.ColorProvider(dayColor, nightColor)`.
  + Use `GlanceModifier.background(Color)` directly for solid background colors
    rather than `ColorProvider`.

#### Full-bleed image layout and snap scrolling (`snap_scrolling`)

* **Widget Provider**: [FullBleedImageAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/text/FullBleedImageAppWidget.kt.rawcontent)
* **Layout Composable**: [FullBleedImageLayout.kt](/agents/skills/system/glance-canonical-layouts/references/text/layout/FullBleedImageLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_full\_bleed\_image\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_full_bleed_image_widget_info.xml.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_full\_bleed\_image\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_full_bleed_image_preview.png),
  [sample\_scrim\_gradient.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_scrim_gradient.xml.rawcontent), [sample\_placeholder\_image.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png),
  [sample\_app\_logo.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_app_logo.xml.rawcontent), [sample\_info\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent), [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent)
* **Utilities**: [FontUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [ImageAspectRatio.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Set `verticalScrollMode =
    VerticalScrollMode.SnapScrollMatchHeight(size.height)` on `LazyColumn` for
    Snap Scrolling.
  + Glance 1.3.0-alpha02 (or higher), Compile SDK 37 (Baklava) or higher, and
    Android Gradle Plugin (AGP) 9.1.0 or higher are required if implementing Snap
    Scrolling.
  + Set override val sizeMode: SizeMode = SizeMode.Exact in the widget provider
    class.

#### Standard toolbar layout (`standard_toolbar`)

* **Widget Provider**: [ToolBarAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/ToolBarAppWidget.kt.rawcontent)
* **Layout Composable**: [ToolBarLayout.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/ToolBarLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_toolbar\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_toolbar_widget_info.xml.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_toolbar\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_toolbar_preview.png), [sample\_app\_logo.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_app_logo.xml.rawcontent),
  [sample\_search\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_search_icon.xml.rawcontent), [sample\_add\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_add_icon.xml.rawcontent), [sample\_edit\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_edit_icon.xml.rawcontent),
  [sample\_share\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_share_icon.xml.rawcontent), [sample\_mic\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_mic_icon.xml.rawcontent), [sample\_camera\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_camera_icon.xml.rawcontent),
  [sample\_videocam\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_videocam_icon.xml.rawcontent)
* **Components**: [Buttons.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/Buttons.kt.rawcontent), [LayoutComponents.kt](/agents/skills/system/glance-canonical-layouts/references/toolbars/layout/LayoutComponents.kt.rawcontent)
* **Utilities**: [ActionUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ActionUtils.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Additional References**: [CanonicalLayoutActivity.kt](/agents/skills/system/glance-canonical-layouts/references/CanonicalLayoutActivity.kt.rawcontent)
* **Guidance**:
  + See Troubleshooting to avoid `ColorProvider` import errors: use
    androidx.glance.color.ColorProvider(dayColor, nightColor).
  + Use GlanceModifier.background(Color) directly for solid background colors
    rather than `ColorProvider`.

#### Text with image layout (`text_with_image`)

* **Widget Provider**: [TextWithImageAppWidget.kt](/agents/skills/system/glance-canonical-layouts/references/text/TextWithImageAppWidget.kt.rawcontent)
* **Layout Composable**: [TextWithImageLayout.kt](/agents/skills/system/glance-canonical-layouts/references/text/layout/TextWithImageLayout.kt.rawcontent)
* **Widget Info XML**: [sample\_text\_with\_image\_widget\_info.xml](/agents/skills/system/glance-canonical-layouts/references/res/xml/sample_text_with_image_widget_info.xml.rawcontent)
* **Data Repository**: [FakeTextWithImageRepository.kt](/agents/skills/system/glance-canonical-layouts/references/text/data/FakeTextWithImageRepository.kt.rawcontent)
* **Dimensions**: [dimens.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/dimens.xml.rawcontent)
* **Strings**: [strings.xml](/agents/skills/system/glance-canonical-layouts/references/res/values/strings.xml.rawcontent)
* **Drawables**: [sample\_text\_image\_preview.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable-nodpi/sample_text_image_preview.png), [sample\_text\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_text_icon.xml.rawcontent),
  [sample\_refresh\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_refresh_icon.xml.rawcontent), [sample\_placeholder\_image.png](/static/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_placeholder_image.png),
  [sample\_info\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_info_icon.xml.rawcontent), [sample\_no\_data\_icon.xml](/agents/skills/system/glance-canonical-layouts/references/res/drawable/sample_no_data_icon.xml.rawcontent)
* **Utilities**: [FontUtils.kt](/agents/skills/system/glance-canonical-layouts/references/utils/FontUtils.kt.rawcontent), [ImageAspectRatio.kt](/agents/skills/system/glance-canonical-layouts/references/utils/ImageAspectRatio.kt.rawcontent), [PreviewAnnotations.kt](/agents/skills/system/glance-canonical-layouts/references/utils/PreviewAnnotations.kt.rawcontent)
* **Theme**: [Color.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Color.kt.rawcontent), [Theme.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Theme.kt.rawcontent), [Type.kt](/agents/skills/system/glance-canonical-layouts/references/ui/theme/Type.kt.rawcontent)
* **Guidance**:
  + Follow responsive layout sizing rules to accommodate text and image
    side-by-side or stacked based on available widget dimensions.

## Troubleshooting

1. **Background Colors**: Use `GlanceModifier.background(Color)` directly for solid background colors rather than `ColorProvider`, otherwise the background will be transparent.
2. **When using `ColorProvider` (outside of the background), avoid import errors**:
   1. Import type: `import androidx.glance.unit.ColorProvider`
   2. Use fully qualified creator: `androidx.glance.color.ColorProvider(dayColor, nightColor)`

## Checklist

* [ ] Did you register the widget in the AndroidManifest?
* [ ] Did you copy the corresponding **Widget Info XML** file and leave the given values including `minWidth`, `minHeight`, and `minResizeHeight` unchanged?
* [ ] Did you use the given Glance Theme color values from the corresponding **Layout Composable** file?
* [ ] Did you use dimension resource references for `android:minWidth` and
  `android:minHeight` in appwidget-provider XML definitions?
* [ ] Did you override `val sizeMode: SizeMode = SizeMode.Exact` in the widget provider class?