---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/anchors
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/anchors
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Geospatial anchors are a type of [anchor](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors) that allow you to place 3D
content with geographical coordinates using the [Geospatial
API](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial).

Geospatial anchors use a latitude and longitude to determine their positioning.
The latitude and longitude are defined by the [WGS84 specification](https://nsgreg.nga.mil/doc/view?i=4085),
which are the same coordinates shown in a typical GPS system.

## Determine the latitude and longitude of a location

If you have a specific point of interest in mind, use [Google Maps](https://www.google.com/maps)
to determine its latitude and longitude:

1. Go to [Google Maps](https://www.google.com/maps) on a desktop computer.
2. Navigate to **Layers \> More**.

   ![The layers button on Google Maps](https://developers.google.com/ar/develop/geospatial/images/google-maps-layers.png)

   ![The more button on Google Maps](https://developers.google.com/ar/develop/geospatial/images/google-maps-more.png)
3. Change the **Map Type** to **Satellite** and clear the **Globe View**
   checkbox at the bottom left corner of the screen.

   ![The map type options on Google Maps](https://developers.google.com/ar/develop/geospatial/images/google-maps-map-type-satellite-globe-view.png)

   This forces a 2D perspective and eliminates possible errors that can come
   from an angled 3D view.
4. On the map, right-click the location and select the longitude and
   latitude to copy it to your clipboard.

## Convert a position in the user's area to a Geospatial anchor

If you are able to travel to the point of interest, you can determine the
latitude, longitude, and altitude from a local reading by [converting a
device-local pose to a Geospatial pose](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/positioning#local-to-geospatial).

## Position content at a Geospatial anchor

Geospatial anchors require an altitude value, which is relative to the WGS84
ellipsoid or relative to the terrain or rooftop.

- For altitude values relative to the WGS84 ellipsoid, use
  [`Geospatial.createAnchor`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createAnchor(kotlin.Double,kotlin.Double,kotlin.Double,androidx.xr.runtime.math.Quaternion)):


  ```kotlin
  val createAnchorResult = geospatial.createAnchor(
      latitude,
      longitude,
      altitude,
      Quaternion.Identity,
  )
  ```

  <br />

- For altitude values relative to the terrain or a rooftop, use
  [`Geospatial.createAnchorOnSurface`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createAnchorOnSurface(kotlin.Double,kotlin.Double,kotlin.Double,androidx.xr.runtime.math.Quaternion,androidx.xr.arcore.Geospatial.Surface)),
  using `GeospatialSurface.TERRAIN` and `GeospatialSurface.ROOFTOP`
  respectively to specify how the final altitude should be interpreted:


  ```kotlin
  val createAnchorResult = geospatial.createAnchorOnSurface(
      latitude,
      longitude,
      altitude,
      Quaternion.Identity,
      GeospatialSurface.TERRAIN,
  )
  ```

  <br />

  When using `GeospatialSurface.ROOFTOP`, the altitude defaults to the terrain
  altitude when not placed on a building.

Then, check the result of the creation call:


```kotlin
when (createAnchorResult) {
    is AnchorCreateSuccess -> {
        // Use anchorCreateResult.anchor to render content at the result.
    }

    else -> {
        // Anchor create failed.
        // See AnchorCreateResult for possible failure reasons.
    }
}
```

<br />

Finally, use the anchor to position 3D content:

### Compose XR


```kotlin
Subspace(FollowTarget.anchor(anchorCreateResult.anchor)) {
    SpatialPanel {
        GeospatialContent()
    }
}
```

<br />

### SceneCore


```kotlin
val anchorSpace = AnchorSpace.create(session, anchorCreateResult.anchor)
val contentEntity = createGeospatialContentEntity(context, session)
anchorSpace.addChild(contentEntity)
```

<br />