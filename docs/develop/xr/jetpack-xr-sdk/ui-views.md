---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-views
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-views
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices.md.txt) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices.md.txt#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices.md.txt#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices.md.txt)

<br />

Using the [Android Jetpack Compose framework](https://developer.android.com/jetpack/compose) is the best way to take
advantage of the latest advancements in Android UI development and to verify
that your application remains current with industry best practices.

However, if you haven't migrated, and are working to spatialize an [Android
Views](https://developer.android.com/develop/ui/views/layout/declaring-layout) based app, there are a few approaches you can take.
[![](https://developer.android.com/static/images/spot-icons/jetpack-compose.svg) Try the Compose way Jetpack Compose using the Jetpack XR SDK is the recommended UI toolkit for building spatial UI on Android XR.](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose.md.txt)

## Reuse your existing Views within SpatialPanels

While a [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialPanel.composable.md.txt) is part of the Jetpack Compose for XR library, it
also accepts Views. When using [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary.md.txt#Subspace(kotlin.Function1)) in your MainActivity,
place an existing view into a `SpatialPanel` as shown in the following
example.


```kotlin
setContent {
    Subspace {
        SpatialPanel(
            modifier = SubspaceModifier.height(500.dp).width(500.dp).depth(25.dp)
        ) { MyCustomView(this@ActivityWithSubspaceContent) }
    }
}
```

<br />

## Use Android Views and Compose interoperability APIs

Consult [guidance on interoperability between Views and Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis.md.txt). This
documentation covers using these frameworks together and contains links to code
samples you can use.

### Use a ComposeView to add spatial panels and orbiters to an existing fragment

Use a [`ComposeView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView.md.txt) in your XML layout to add Composables and create new XR
content. Use [View binding](https://developer.android.com/topic/libraries/view-binding.md.txt) or [`findViewById`](https://developer.android.com/reference/kotlin/android/view/View.md.txt#findviewbyid) to find the
[`ComposeView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView.md.txt) in the [`onCreateView()`](https://developer.android.com/reference/kotlin/android/app/Fragment.md.txt#oncreateview) function.

[Read more about `ComposeView` guidance](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/compose-in-views.md.txt#compose-in-fragments).


```kotlin
override fun onCreateView(
    inflater: LayoutInflater,
    container: ViewGroup?,
    savedInstanceState: Bundle?
): View {
    val view = inflater.inflate(R.layout.example_fragment, container, false)
    view.findViewById<ComposeView>(R.id.compose_view).apply {
        // Dispose of the Composition when the view's LifecycleOwner
        // is destroyed
        setViewCompositionStrategy(ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed)
        setContent {
            // In Compose world
            SpatialPanel(SubspaceModifier.height(500.dp).width(500.dp)) {
                Text("Spatial Panel with Orbiter")
            }
        }
    }
    return view
}
```

<br />

## Work directly with the Jetpack SceneCore library

[Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk.md.txt#jetpack-compose) is built on top of [Jetpack SceneCore](https://developer.android.com/develop/xr/jetpack-xr-sdk.md.txt#jetpack-scenecore). If you are
spatializing a Views based app, you may continue to use your existing UI code
within Compose for XR or choose to work directly with Jetpack SceneCore's
[`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session.md.txt) instead.

You can build panels directly from SceneCore using [`PanelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity.md.txt). Set the
size of the panel in meters using [`dimensions`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity.md.txt#create(androidx.xr.runtime.Session,android.view.View,androidx.xr.runtime.math.FloatSize2d,kotlin.String,androidx.xr.runtime.math.Pose)), or in pixels using
[`pixelDimensions`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity.md.txt#create(androidx.xr.runtime.Session,android.view.View,androidx.xr.runtime.math.IntSize2d,kotlin.String,androidx.xr.runtime.math.Pose)). You can choose to make the panels movable or resizable
by using the corresponding components. For more information, see [Add common
behavior to entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities#add-common).


```kotlin
val panelContent = MyCustomView(this)
val panelEntity = PanelEntity.create(
    session = xrSession,
    view = panelContent,
    pixelDimensions = IntSize2d(500, 500),
    name = "panel entity"
)
```

<br />