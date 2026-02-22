---
title: https://developer.android.com/studio/debug/layout-inspector
url: https://developer.android.com/studio/debug/layout-inspector
source: md.txt
---

The Layout Inspector in Android Studio lets you debug the layout of your app by
showing a view hierarchy where you can inspect the properties of each view. With
the Layout Inspector, you can compare your app layout with design mockups,
display a magnified or 3D view of your app, and examine details of its layout at
runtime. This is especially useful when your layout is built at runtime rather
than entirely in XML and the layout is behaving unexpectedly.
![](https://developer.android.com/static/studio/images/embedded-layout-inspector.png) **Figure 1.**Embedded Layout Inspector for the Jetchat app.

## Get started

To start the Layout Inspector, [run your app](https://developer.android.com/studio/run), go to the
**Running Devices** window, and click **Toggle Layout Inspector** ![Toggle embedded layout inspector button](https://developer.android.com/static/studio/images/design/start-embedded-layout-inspector.png).
If you switch among multiple devices or projects, the Layout Inspector
automatically connects to the debuggable processes running in the foreground of
the connected device.

Here's how to do some common tasks:

- To view hierarchy and inspect the properties of each view, use the **Component Tree** and **Attributes** tool windows. Layout Inspector might require an activity restart to access the attributes. For more information, see [View Attribute Inspection](https://developer.android.com/studio/debug/layout-inspector#view-attribute-inspection).
- To select views by single clicking directly on the views or navigate to code by double clicking on the views, enable **Toggle Deep Inspect** ![Toggle deep inspect button](https://developer.android.com/static/studio/images/design/deep-inspect.png).
- To interact with the app, disable **Toggle Deep Inspect** ![Toggle deep inspect button](https://developer.android.com/static/studio/images/design/deep-inspect.png).
- To inspect physical devices, enable [device mirroring](https://developer.android.com/studio/run/device#device-mirroring).
- To enable live updates as you update your app's UI, check that [Live Edit](https://developer.android.com/develop/ui/compose/tooling/iterative-development#live-edit) is enabled.
- To use [3D mode](https://developer.android.com/studio/debug/layout-inspector#rotate-layout), take a Layout Inspector snapshot ![Layout Inspector Snapshot](https://developer.android.com/static/studio/images/design/li-snapshot.png) and then click **3D Mode** ![3D button](https://developer.android.com/static/studio/images/buttons/layout-inspector-rotation-icon.png).

## Select or isolate a view

A view usually draws something the user can see and interact with. The
**Component Tree** shows your app's hierarchy in real time with each view
component, which helps you debug your app's layout because you can visualize the
elements within your app and the values associated with them.

To select a view, click it in the **Component Tree** or the **Layout Display** .
All of the layout attributes for the selected view appear in the **Attributes**
panel.

If your layout includes overlapping views, you can see all the views in a region
when you right-click in **Deep Inspect** mode
![Toggle deep inspect button](https://developer.android.com/static/studio/images/design/deep-inspect.png). To select
a view that isn't in front, click it in the **Component Tree** or
[rotate the layout](https://developer.android.com/studio/debug/layout-inspector#rotate-layout).

To work with complex layouts, you can isolate individual views so that only a
subset of the layout is shown in the **Component Tree** and rendered in the
**Layout Display** . To isolate a view, take a snapshot
![Layout Inspector Snapshot](https://developer.android.com/static/studio/images/design/li-snapshot.png), right-click
the view in the **Component Tree** and select **Show Only Subtree** or
**Show Only Parents** . To return to the full view, right-click the view and
select **Show All**. You must take a snapshot before isolating a view.

> [!NOTE]
> **Note:** The ability to isolate a view [is temporarily
> unavailable](https://developer.android.com/studio/known-issues#layout-inspector-isolate-view). We're working on fixing this issue.

## Hide layout borders and view labels

To hide the bounding box or view labels for a layout element, click **View
Options** ![View Options button](https://developer.android.com/static/studio/images/buttons/live-layout-inspector-view-options-icon.png)
at the top of the **Layout Display** and toggle **Show Borders** or **Show View
Label**.

## Capture layout hierarchy snapshots

Layout Inspector lets you save snapshots of your running app's layout hierarchy,
so that you can share them with others or refer to them later.

Snapshots capture the data you would typically see when using the Layout
Inspector, including a detailed 3D rendering of your layout, the component tree
of your View, Compose, or hybrid layout, and detailed attributes for each
component of your UI. To save a snapshot, click **Snapshot Export/Import**
![Snapshot Export/Import](https://developer.android.com/static/studio/images/design/li-snapshot.png) and then
**Export Snapshot**.

Load a previously saved Layout Inspector snapshot by clicking
**Import Snapshot**.

## 3D mode

The **Layout Display** features an advanced 3D visualization of your
app's view hierarchy at runtime. To use this feature, take a snapshot
![Snapshot Export/Import](https://developer.android.com/static/studio/images/design/li-snapshot.png), click
the **3D Mode** button
![3D button](https://developer.android.com/static/studio/images/buttons/layout-inspector-rotation-icon.png) in the
snapshot Inspector window, and rotate it by dragging the mouse.
![Layout Inspector: 3D view](https://developer.android.com/static/studio/images/li-3d-mode.png) **Figure 2.**Rotated 3D view of a Layout. ![Layout inspector: layer spacing view](https://developer.android.com/static/studio/images/debug/layout-inspector-layer-spacing.png) **Figure 3.** To expand or contract the layers of the Layout, use the **Layer Spacing** slider.

### Compare app layout to a reference image overlay

To compare your app layout with a reference image, such as a UI mockup, you can
load a bitmap image overlay in the Layout Inspector.

- To load an overlay, select the **Load Overlay** ![](https://developer.android.com/static/studio/images/li-load-overlay.png) option from the **Layout Inspector** toolbar. The overlay is scaled to fit the layout.
- To adjust the transparency of the overlay, use the **Overlay Alpha** slider.
- To remove the overlay, click **Clear Overlay** ![](https://developer.android.com/static/studio/images/buttons/live-layout-inspector-remove-overlay-icon.png)

## Inspect Compose

Layout Inspector lets you inspect a Compose layout inside a running app in
an emulator or physical device. You can use the Layout Inspector to check how
often a composable is recomposed or skipped, which can help identify issues with
your app. For example, some coding errors might force your UI to recompose
excessively, which can cause poor performance. Some coding errors can prevent
your UI from recomposing and, therefore, preventing your UI changes from showing
up on the screen.

[Learn more about Layout Inspector for Compose](https://developer.android.com/develop/ui/compose/tooling/debug)

## View Attribute Inspection

Layout Inspector requires the following global setting to function properly:

    adb shell settings put global debug_view_attributes 1

This option generates extra information for inspection on all of the
processes on the device.

Layout Inspector automatically enables the setting when started. This
causes the current foreground Activity to restart. You will not see another
Activity restart unless the flag is manually disabled on the device.

To disable the flag, run the following adb command:

    adb shell settings delete global debug_view_attributes

Alternatively, turn off [Enable view attribute inspection](https://developer.android.com/studio/debug/dev-options#debugging)
from your device's [developer options](https://developer.android.com/studio/debug/dev-options#enable).

## Standalone Layout Inspector

For optimal performance, we recommend using the Layout Inspector in its default
embedded mode. If you want to un-embed the Layout Inspector, go to **File**
(**Android Studio** on macOS)\> **Settings** \> **Tools** \> **Layout Inspector**
and clear the **Enable embedded Layout Inspector** checkbox.

In standalone mode, enable live updates by clicking the **Live Updates**
![](https://developer.android.com/static/studio/images/buttons/layout-inspector-live-updates-button.png) option from
the **Layout Inspector** toolbar.