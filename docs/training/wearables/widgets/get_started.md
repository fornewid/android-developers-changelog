---
title: https://developer.android.com/training/wearables/widgets/get_started
url: https://developer.android.com/training/wearables/widgets/get_started
source: md.txt
---

> [!NOTE]
> **Note:** This tutorial assumes you are building a new widget and don't have an existing tile. If you're updating an app that already has an existing tile, read the [Migrate from tiles to widgets](https://developer.android.com/training/wearables/widgets/migration) guide to configure your services.

## Prerequisites and Setup

Before you begin, ensure your environment meets the following requirements.

### Runtime Requirements

Wear Widgets require version **1.6.1 or higher** of the
`com.google.android.wearable.protolayout.renderer` APK on the target device.

Get a compatible version of the renderer in one of the following ways:

- **Wear OS 7 Emulator** : Use the Wear OS 7 emulator image. Versions lower than 7 are not suitable. For setup instructions, see [Set up the Wear OS 7
  emulator](https://developer.android.com/training/wearables/versions/7/setup).
- **Physical Device**: Use a physical Wear OS device that receives automatic updates from the Google Play Store, or a developer device signed in to the Google Play Store.

To check what version you have installed on your device, use the following
command:

    adb shell dumpsys package com.google.android.wearable.protolayout.renderer | \
      grep -m 1 versionName | \
      awk -F= '{print $2}'

### Gradle Configuration

Wear Widget libraries are available on **Google Maven**.

**1. Configure SDK Version**

Ensure your `compileSdk` and `targetSdk` are set to **37** or higher.

    android {
        compileSdk = 37
        // ...
        defaultConfig {
            targetSdk = 37
            // ...
        }
    }

**2. Add Dependencies**

Include the following dependencies in your app's `build.gradle.kts` file:

### Groovy

```groovy
dependencies {
    // Core Wear Widget and Remote Compose libraries
    implementation "androidx.compose.remote:remote-creation-compose:1.0.0-alpha18"
    implementation "androidx.compose.remote:remote-core:1.0.0-alpha18"
    implementation "androidx.glance.wear:wear:1.0.0-alpha17"
    implementation "androidx.glance.wear:wear-core:1.0.0-alpha17"
    implementation "androidx.wear.compose.remote:remote-material3:1.0.0-alpha10"

    // Tooling for previews (optional, but recommended)
    implementation "androidx.compose.remote:remote-tooling-preview:1.0.0-alpha18"
    implementation "androidx.wear.compose:compose-ui-tooling:1.6.2"
    implementation "androidx.wear.tiles:tiles-tooling-preview:1.6.2"
    debugImplementation "androidx.wear.tiles:tiles-renderer:1.6.2"
}
```

### Kotlin

```kotlin
dependencies {
    // Core Wear Widget and Remote Compose libraries
    implementation("androidx.compose.remote:remote-creation-compose:1.0.0-alpha18")
    implementation("androidx.compose.remote:remote-core:1.0.0-alpha18")
    implementation("androidx.glance.wear:wear:1.0.0-alpha17")
    implementation("androidx.glance.wear:wear-core:1.0.0-alpha17")
    implementation("androidx.wear.compose.remote:remote-material3:1.0.0-alpha10")

    // Tooling for previews (optional, but recommended)
    implementation("androidx.compose.remote:remote-tooling-preview:1.0.0-alpha18")
    implementation("androidx.wear.compose:compose-ui-tooling:1.6.2")
    implementation("androidx.wear.tiles:tiles-tooling-preview:1.6.2")
    debugImplementation("androidx.wear.tiles:tiles-renderer:1.6.2")
}
```

## Build a Hello World Widget

A Wear Widget consists of a service extending
[`GlanceWearWidgetService`](https://developer.android.com/reference/kotlin/androidx/glance/wear/GlanceWearWidgetService) and a widget class
extending [`GlanceWearWidget`](https://developer.android.com/reference/kotlin/androidx/glance/wear/GlanceWearWidget). You define the UI using
`@RemoteComposable` functions.

### Define the Service

The service is the entry point that the system binds to.

To define your widget, create a service that extends `GlanceWearWidgetService`.

<br />

```kotlin
@AssociateWithGlanceWearWidget(HelloWidget::class)
class HelloWidgetService : GlanceWearWidgetService() {
    override val widget: GlanceWearWidget = HelloWidget()
}
```

<br />

### Define the Widget

The widget class provides the data and layout for the widget.

<br />

```kotlin
class HelloWidget : GlanceWearWidget() {
    override suspend fun provideWidgetData(
        context: Context,
        params: WearWidgetParams,
    ): WearWidgetData {
        return WearWidgetDocument(
            background = WearWidgetBrush.color(Color.Blue.rc),
        ) {
            HelloWidgetContent()
        }
    }
}
```

<br />

> [!WARNING]
> **Warning:** Always supply your widget's background brush directly to `WearWidgetDocument(background = ...)` so the host system can paint and mask the background to the native OEM container shape. Setting a transparent or black canvas and drawing a custom rounded container inside the layout can cause floating box and letterboxing defects on some devices.

### Define the Content

The content is built using Remote Compose components.

<br />

```kotlin
@RemoteComposable
@Composable
fun HelloWidgetContent() {
    RemoteBox(
        modifier = RemoteModifier.fillMaxSize(),
        contentAlignment = RemoteAlignment.Center,
    ) {
        RemoteText(
            text = "Hello World".rs,
            color = Color.White.rc,
        )
    }
}
```

<br />

> [!WARNING]
> **Warning:** Ensure your root container composable uses `RemoteModifier.fillMaxSize()`. Because container DP dimensions and safe insets vary across watch models, hardcoding fixed dimensions or outer padding can cause clipping or misaligned layouts.

### Preview your widget in Android Studio

You can preview your widget layouts directly in Android Studio's **Design**
panel using
[`androidx.glance.wear:wear-tooling-preview`](https://developer.android.com/jetpack/androidx/releases/wear#wear-tooling-preview_2).

#### Predefined preview suites

The `wear-tooling-preview` library provides predefined
`PreviewParameterProvider` suites to test your layouts across different
container shapes and device configurations:

- **Squircle Suite (`SquircleAllWidgetPreviewParams`):** Rounded rectangle containers.
- **Round Suite (`RoundAllWidgetPreviewParams`):** Pill-shaped containers.
- **Rectangular Suite (`RectangularAllWidgetPreviewParams`):** Uncropped rectangular containers with safe padding. Images generated with this preview configuration are suitable for use as the APK-embedded preview images used by the widget picker (see [Generate preview image assets](https://developer.android.com/training/wearables/widgets/get_started#generate-preview-assets)).

To preview your widget in Android Studio, use `@WearWidgetPreview`:

<br />

```kotlin
@Preview
@Composable
fun HelloWidgetPreview(
    @PreviewParameter(SquircleAllWidgetPreviewParams::class) params: WearWidgetParams,
) {
    WearWidgetPreview(
        widget = HelloWidget(),
        params = params,
    )
}
```

<br />

> [!TIP]
> **Tip:** You can also preview `@RemoteComposable` layouts directly without instantiating the widget class by passing a content lambda and background brush to [`WearWidgetPreview`](https://developer.android.com/reference/kotlin/androidx/glance/wear/tooling/preview/WearWidgetPreview.composable).

### Create the Widget Configuration XML

Create a new file `res/xml/hello_widget_info.xml` to define the widget's
properties and supported sizes. For a complete reference of the supported XML
attributes in the `<wearwidget-provider>` tag, see the
[`WearWidgetProviderInfo`](https://developer.android.com/reference/kotlin/androidx/glance/wear/core/WearWidgetProviderInfo) documentation.

<br />

```xml
<wearwidget-provider
    description="@string/hello_widget_description"
    icon="@mipmap/ic_launcher"
    label="@string/hello_widget_label"
    preferredType="SMALL">

    <container
        type="SMALL"
        previewImage="@drawable/widget_preview_small" />
    <container
        type="LARGE"
        previewImage="@drawable/widget_preview_large" />
</wearwidget-provider>
```

<br />

#### Generate preview image assets

The `<container>` element's `previewImage` attribute references a drawable asset
shown in the system widget picker. To generate preview assets with the correct
bounds and density, use Android Studio Previews with
`RectangularAllWidgetPreviewParams` (which generates preview variants for both
small and large containers) and specify a 320 DPI smartwatch display density:

<br />

```kotlin
@Preview(
    name = "Widget Preview Asset",
    device = "spec:width=1000dp,height=1000dp,dpi=320",
)
@Composable
fun HelloWidgetCatalogPreview(
    @PreviewParameter(RectangularAllWidgetPreviewParams::class) params: WearWidgetParams,
) {
    WearWidgetPreview(
        widget = HelloWidget(),
        params = params,
    )
}
```

<br />

To extract the rendered preview images, complete the following steps:

1. In Android Studio, open the **Design** surface for the preview composable.
2. In the preview window, right-click the rendered preview or use the preview toolbar to select **Copy Image** or save the image. Alternatively, use CLI tooling or automated scripts to extract Compose previews.
3. Save the small and large image files into your app's `res/drawable-nodpi/` directory, such as `res/drawable-nodpi/widget_preview_small.png` and `res/drawable-nodpi/widget_preview_large.png`.

### Register in AndroidManifest.xml

Register the service in your `AndroidManifest.xml` with the required intent
filters and metadata.

<br />

```xml
<service
    android:name=".snippets.widget.HelloWidgetService"
    android:exported="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/hello_widget_label"
    android:permission="com.google.android.wearable.permission.BIND_TILE_PROVIDER">

    <intent-filter>
        <action android:name="androidx.glance.wear.action.BIND_WIDGET_PROVIDER" />
        <!-- If you already have a Tile, omit the following line. -->
        <action android:name="androidx.wear.tiles.action.BIND_TILE_PROVIDER" />
    </intent-filter>

    <meta-data
        android:name="androidx.glance.wear.widget.provider"
        android:resource="@xml/hello_widget_info" />

    <meta-data
        android:name="androidx.wear.tiles.PREVIEW"
        android:resource="@drawable/tile_preview" />
</service>
```

<br />

## Build and Deploy

After defining your service and widget, you can build your project and deploy it
to a device or emulator.

### Build and Install

Build the project and install the debug APK onto your connected device or
emulator:

    ./gradlew :app:installDebug

### Add and preview your widget

After the app is installed, use `adb` to programmatically add the widget to the
carousel and display it on the screen.

**Note:** Wear Widgets use the underlying tile infrastructure for debugging
purposes. As a result, the `adb` commands require the
[`add-tile`](https://developer.android.com/training/wearables/tiles/debug#adb) and [`show-tile`](https://developer.android.com/training/wearables/tiles/debug#adb) operations.

**1. Add the widget to the carousel:**

    adb shell am broadcast \
      -a com.google.android.wearable.app.DEBUG_SURFACE \
      --es operation add-tile \
      --ecn component <your_package_name>/.HelloWidgetService

> [!NOTE]
> **Note:** The preceding command adds a FULLSCREEN tile by default. You can also specify LARGE and SMALL sizes by passing `--ei type [0|1|2]` to the command (where type 0 is FULLSCREEN). Depending on the device state, app-triggered content updates using `triggerUpdate()` might fail for non-fullscreen types when using Wear Widget library versions up to `1.0.0-alpha10` (this is fixed starting in `1.0.0-alpha11`).

**2. Show the widget:**

    adb shell am broadcast \
      -a com.google.android.wearable.app.DEBUG_SYSUI \
      --es operation show-tile \
      --ei index 0