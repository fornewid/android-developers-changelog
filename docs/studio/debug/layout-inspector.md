---
title: https://developer.android.com/studio/debug/layout-inspector
url: https://developer.android.com/studio/debug/layout-inspector
source: md.txt
---

The Layout Inspector in Android Studio lets you inspect and debug the layout
inside a running app in an emulator or physical device. You can inspect the
attributes of each component, compare your app layout with design mockups, and
display a magnified view of your app.

You can also use the Layout Inspector to check how often a composable is
recomposed or skipped, which can help identify issues with your app. For
example, some coding errors might force your UI to recompose excessively, which
can cause poor performance. Some coding errors can prevent your UI from
recomposing and, therefore, can prevent your UI changes from appearing on the
screen.

For more information, see [Debug your Compose UI](https://developer.android.com/develop/ui/compose/tooling/debug).
![](https://developer.android.com/static/studio/images/embedded-layout-inspector.png) **Figure 1.**Embedded Layout Inspector for the Jetchat app.

## Get started

To start the Layout Inspector, [run your app](https://developer.android.com/studio/run), go to the
**Running Devices** window, and click **Toggle Layout Inspector** ![Toggle
embedded layout inspector
button](https://developer.android.com/static/studio/images/design/start-embedded-layout-inspector.png). If you
switch among multiple devices or projects, the Layout Inspector automatically
connects to the debuggable processes running in the foreground of the connected
device.

Here's how to do some common tasks:

- To view hierarchy and inspect the attributes of each component, use the **Component Tree** and **Attributes** tool windows. Layout Inspector might require an activity restart to access the attributes.
- To select components, first enable **Toggle Deep Inspect** ![Toggle deep
  inspect button](https://developer.android.com/static/studio/images/design/deep-inspect.png), then click the components. Alternatively, navigate to your code by double-clicking the components.
- To interact with the app, disable **Toggle Deep Inspect** ![Toggle deep
  inspect button](https://developer.android.com/static/studio/images/design/deep-inspect.png).
- To inspect physical devices, enable [device mirroring](https://developer.android.com/studio/run/device#device-mirroring).
- To enable live updates as you update your app's UI, check that [Live Edit](https://developer.android.com/develop/ui/compose/tooling/iterative-development#live-edit) is enabled.

## Select or isolate a component

A component usually draws something the user can see and interact with. The
**Component Tree** shows your app's hierarchy in real time with each composable
component, which helps you debug your app's layout because you can visualize the
elements within your app and the values associated with them.

To select a component, click it in the **Component Tree** or the
**Layout Display** . All the layout attributes for the selected component appear
in the **Attributes** panel.

If your layout includes overlapping components, you can see all the components
in a region when you right-click in **Deep Inspect** mode ![Toggle deep inspect
button](https://developer.android.com/static/studio/images/design/deep-inspect.png). To select a component that
isn't in front, click it in the **Component Tree**.

To work with complex layouts, you can isolate individual components so that only
a subset of the layout is shown in the **Component Tree** and rendered in the
**Layout Display** . To isolate a component, right-click the component in the
**Component Tree** and select **Show Only Subtree** or
**Show Only Parents** . To return to the full view, right-click the component and
select **Show All**.

## Hide layout borders and view labels

To hide the bounding box or component labels for a layout element, click
**View Options** ![View Options
button](https://developer.android.com/static/studio/images/buttons/live-layout-inspector-view-options-icon.png) at
the top of the **Layout Display** and toggle **Show Borders** or **Show View
Label**.

## Capture layout hierarchy snapshots

Layout Inspector lets you save snapshots of your running app's layout hierarchy,
so that you can share them with others or refer to them later.

Snapshots capture the data you would typically see when using the Layout
Inspector, including a detailed rendering of your layout, the component tree of
your Compose, View, or hybrid layout, and detailed attributes for each component
of your UI. To save a snapshot, click **Snapshot Export/Import** ![Snapshot
Export/Import](https://developer.android.com/static/studio/images/design/li-snapshot.png) and then
**Export Snapshot**.

Load a previously saved Layout Inspector snapshot by clicking
**Import Snapshot**.

## Compare app layout to a reference image overlay

To compare your app layout with a reference image, such as a UI mockup, you can
load a bitmap image overlay in the Layout Inspector.

- To load an overlay, select the **Load Overlay** ![](https://developer.android.com/static/studio/images/li-load-overlay.png) option from the **Layout Inspector** toolbar. The overlay is scaled to fit the layout.
- To adjust the transparency of the overlay, use the **Overlay Alpha** slider.
- To remove the overlay, click **Clear Overlay** . ![](https://developer.android.com/static/studio/images/buttons/live-layout-inspector-remove-overlay-icon.png)

## Standalone Layout Inspector

For optimal performance, we recommend using the Layout Inspector in its default
embedded mode. If you want to un-embed the Layout Inspector, go to **File**
(**Android Studio** on macOS)\> **Settings** \> **Tools** \> **Layout Inspector**
and clear the **Enable embedded Layout Inspector** checkbox.

In standalone mode, enable live updates by clicking the **Live Updates**
![](https://developer.android.com/static/studio/images/buttons/layout-inspector-live-updates-button.png) option from
the **Layout Inspector** toolbar.

## Additional resources

### Views content

- [Debug your layout with Layout Inspector (Views)](https://developer.android.com/studio/views/layout-inspector-views)