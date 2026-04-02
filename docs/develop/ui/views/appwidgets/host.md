---
title: https://developer.android.com/develop/ui/views/appwidgets/host
url: https://developer.android.com/develop/ui/views/appwidgets/host
source: md.txt
---

The Android home screen, available on most Android-powered devices, lets the
user embed [app widgets](https://developer.android.com/guide/topics/appwidgets/overview) (or *widgets* ) for
quick access to content. If you're building a home screen replacement or a
similar app, you can also let the user embed widgets by implementing
[`AppWidgetHost`](https://developer.android.com/reference/android/appwidget/AppWidgetHost). This isn't
something that most apps need to do, but if you are creating your own host, it's
important to understand the contractual obligations a host implicitly agrees to.
[Video](https://www.youtube.com/watch?v=15Q7xqxBGG0)

This page focuses on the responsibilities involved in implementing a custom
`AppWidgetHost`. For a specific example of how to implement an `AppWidgetHost`,
look at the source code for the Android home screen
[`LauncherAppWidgetHost`](https://cs.android.com/android/platform/superproject/+/master:packages/apps/Launcher3/src/com/android/launcher3/widget/LauncherAppWidgetHost.java;l=57?q=LauncherAppWidgetHost).

Here is an overview of key classes and concepts involved in implementing a
custom `AppWidgetHost`:

- **App widget host** : the `AppWidgetHost` provides the interaction with the
  AppWidget service for apps that embed widgets in their UI. An `AppWidgetHost`
  must have an ID that is unique within the host's own package. This ID persists
  across all uses of the host. The ID is typically a hardcoded value that you
  assign in your app.

- **App widget ID** : each widget instance is assigned a unique ID at the time
  of binding. See
  [`bindAppWidgetIdIfAllowed()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#bindAppWidgetIdIfAllowed(int,%20android.content.ComponentName))
  and, for more detail, the [Binding widgets](https://developer.android.com/develop/ui/views/appwidgets/host#bind) section that follows. The
  host obtains the unique ID using
  [`allocateAppWidgetId()`](https://developer.android.com/reference/android/appwidget/AppWidgetHost#allocateAppWidgetId()).
  This ID persists across the lifetime of the widget until it is deleted from the
  host. Any host-specific state---such as the size and location of the
  widget---must be persisted by the hosting package and associated with the
  app widget ID.

- **App widget host view** : think of
  [`AppWidgetHostView`](https://developer.android.com/reference/android/appwidget/AppWidgetHostView) as a frame
  that the widget is wrapped in whenever it needs to be displayed. A widget is
  associated with an `AppWidgetHostView` every time the widget is inflated by the
  host.

  - By default, the system creates an `AppWidgetHostView`, but the host can create its own subclass of `AppWidgetHostView` by extending it.
  - Starting in Android 12 (API level 31), `AppWidgetHostView` introduces the the [`setColorResources()`](https://developer.android.com/reference/android/appwidget/AppWidgetHostView#setColorResources(android.util.SparseIntArray)) and [`resetColorResources()`](https://developer.android.com/reference/android/appwidget/AppWidgetHostView#resetColorResources()) methods for handling dynamically overloaded colors. The host is responsible for providing the colors to these methods.
- **Options bundle** : the `AppWidgetHost` uses the options bundle to
  communicate information to the
  [`AppWidgetProvider`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider)
  about how the widget is displayed---for example, the
  [list of size ranges](https://developer.android.com/guide/topics/appwidgets/layouts#provide-exact-layouts)---and whether the
  widget is on a lockscreen or the home screen. This information lets the
  `AppWidgetProvider` tailor the widget's contents and appearance based on how and
  where it is displayed. You can use
  [`updateAppWidgetOptions()`](https://developer.android.com/reference/android/appwidget/AppWidgetHostView#updateAppWidgetOptions(android.os.Bundle))
  and
  [`updateAppWidgetSize()`](https://developer.android.com/reference/android/appwidget/AppWidgetHostView#updateAppWidgetSize(android.os.Bundle,%20java.util.List%3Candroid.util.SizeF%3E))
  to modify a widget's bundle. Both of these methods trigger the
  [`onAppWidgetOptionsChanged()`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider#onAppWidgetOptionsChanged(android.content.Context,%20android.appwidget.AppWidgetManager,%20int,%20android.os.Bundle))
  callback to the `AppWidgetProvider`.

## Binding widgets

When a user adds a widget to a host, a process called *binding* occurs. Binding
refers to associating a particular app widget ID with a specific host and a
specific `AppWidgetProvider`.

Binding APIs also make it possible for a host to provide a custom UI for
binding. To use this process, your app must declare the
[`BIND_APPWIDGET`](https://developer.android.com/reference/android/Manifest.permission#BIND_APPWIDGET)
permission in the host's manifest:

    <uses-permission android:name="android.permission.BIND_APPWIDGET" />

But this is just the first step. At runtime, the user must explicitly grant
permission to your app to let it add a widget to the host. To test whether your
app has permission to add the widget, use the
[`bindAppWidgetIdIfAllowed()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#bindAppWidgetIdIfAllowed(int,%20android.content.ComponentName))
method. If `bindAppWidgetIdIfAllowed()` returns `false`, your app must display a
dialog prompting the user to grant permission: "allow" for the current widget
addition, or "always allow" to cover all future widget additions.

This snippet gives an example of how to display the dialog:

### Kotlin

```kotlin
val intent = Intent(AppWidgetManager.ACTION_APPWIDGET_BIND).apply {
    putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetId)
    putExtra(AppWidgetManager.EXTRA_APPWIDGET_PROVIDER, info.componentName)
    // This is the options bundle described in the preceding section.
    putExtra(AppWidgetManager.EXTRA_APPWIDGET_OPTIONS, options)
}
startActivityForResult(intent, REQUEST_BIND_APPWIDGET)
```

### Java

```java
Intent intent = new Intent(AppWidgetManager.ACTION_APPWIDGET_BIND);
intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, appWidgetId);
intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_PROVIDER, info.componentName);
// This is the options bundle described in the preceding section.
intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_OPTIONS, options);
startActivityForResult(intent, REQUEST_BIND_APPWIDGET);
```

The host must check whether the widget that a user adds needs configuration. For
more information, see [Enable users to configure app
widgets](https://developer.android.com/guide/topics/appwidgets/configuration).

## Host responsibilities

You can specify a number of configuration settings for widgets using the
[`AppWidgetProviderInfo` metadata](https://developer.android.com/develop/ui/views/appwidgets#components).
You can retrieve these configuration options, covered in more detail in the
following sections, from the
[`AppWidgetProviderInfo`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo)
object associated with a widget provider.

Regardless of the version of Android you are targeting, all hosts have the
following responsibilities:

- When adding a widget, allocate the widget ID as described earlier. When a
  widget is removed from the host, call
  [`deleteAppWidgetId()`](https://developer.android.com/reference/android/appwidget/AppWidgetHost#deleteAppWidgetId(int))
  to deallocate the widget ID.

- When adding a widget, check whether the configuration activity needs to be
  launched. Typically, the host needs to launch the widget's configuration
  activity if it exists and isn't marked as optional by specifying both the
  `configuration_optional` and `reconfigurable` flags. See
  [Update the widget from the configuration activity](https://developer.android.com/guide/topics/appwidgets/configuration#update)
  for details. This is a necessary step for many widgets before they can display.

  > [!NOTE]
  > **Note:** Handle irregular cases where the configuration activity doesn't return or finishes with errors.

- Widgets specify a default width and height in the `AppWidgetProviderInfo`
  metadata. These values are defined in cells---starting in
  Android 12, if `targetCellWidth` and `targetCellHeight` are
  specified---or dps if only `minWidth` and `minHeight` are specified. See
  [Widget sizing attributes](https://developer.android.com/guide/topics/appwidgets#widget-sizing-attributes).

  Make sure that the widget is laid out with at least this many dps. For
  example, many hosts align icons and widgets in a grid. In this scenario, by
  default the host adds the a widget using the minimum number of cells that
  satisfy the `minWidth` and `minHeight` constraints.

In addition to the requirements listed in the preceding section, specific
platform versions introduce features that place new responsibilities on the
host.

### Determine your approach based on the targeted Android version

#### Android 12

Android 12 (API level 31) bundles an extra `List<SizeF>` that contains the list
of possible sizes in dps that a widget instance can take in the options bundle.
The number of sizes provided depends on the host implementation. Hosts typically
provide two sizes for phones---portrait and landscape---and four sizes
for foldables.

There is a limit of `MAX_INIT_VIEW_COUNT` (16) on the number of different
`RemoteViews` that an `AppWidgetProvider` can provide to
[`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews#RemoteViews(java.util.Map%3Candroid.util.SizeF,%20android.widget.RemoteViews%3E)).
Since `AppWidgetProvider` objects map a `RemoteViews` object to each size in the
`List<SizeF>`, don't provide more than `MAX_INIT_VIEW_COUNT` sizes.

Android 12 also introduces the
[`maxResizeWidth`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#maxResizeWidth)
and
[`maxResizeHeight`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#maxResizeHeight)
attributes in dps. We recommend that a widget that uses at least one of these
attributes doesn't exceed the size specified by the attributes.

## Additional resources

- See the [`Glance`](https://developer.android.com/jetpack/androidx/releases/glance) reference documentation.