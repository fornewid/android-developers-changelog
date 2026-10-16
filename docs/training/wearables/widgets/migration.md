---
title: https://developer.android.com/training/wearables/widgets/migration
url: https://developer.android.com/training/wearables/widgets/migration
source: md.txt
---

> [!NOTE]
> **Note:** This migration guide only applies if you have an existing tile that you want to migrate to a Wear Widget.

Although both tiles and widgets display your content on a remote system surface,
building them requires distinct approaches. Migrating your existing tile to a
widget means transitioning from rigid layout generation to a dynamic,
declarative UI, unlocking new capabilities and a simplified development model.

## Choose your implementation strategy

If you're migrating an app that maintains a legacy tile, you must decide how
your app provides content to the system. While brand-new widgets should use a
single Widget Service, apps with existing tiles must choose between maintaining
both services or consolidating on a single Widget Service.

### Recommended: Dual service (tile + widget)

Maintaining both a tile and a widget is the recommended path for all apps that
have an existing tile. Providing two distinct services provides the best
possible user experience across different devices.

- **Tile Service:** Extend [`TileService`](https://developer.android.com/reference/kotlin/androidx/wear/tiles/TileService) and declare an intent filter for [`androidx.wear.tiles.action.BIND_TILE_PROVIDER`](https://developer.android.com/reference/kotlin/androidx/wear/tiles/TileService#ACTION_BIND_TILE_PROVIDER()).
- **Widget Service:** Extend [`GlanceWearWidgetService`](https://developer.android.com/reference/kotlin/androidx/glance/wear/GlanceWearWidgetService) and declare an intent filter for [`androidx.glance.wear.action.BIND_WIDGET_PROVIDER`](https://developer.android.com/reference/kotlin/androidx/glance/wear/GlanceWearWidgetService#ACTION_BIND_WIDGET_PROVIDER()).
- **Logical Grouping:** Use the [`group`](https://developer.android.com/reference/kotlin/androidx/glance/wear/core/WearWidgetProviderInfo#group()) attribute in the widget configuration to link the new implementation to your existing `TileService`. This allows the system to recognize them as a single logical component and automatically migrate the user's existing carousel slot to the new widget on Wear OS 7 or higher.

**System Behavior for Dual-Service Setup:**

| OS / Device Capability | Resulting Experience |
|---|---|
| **Wear OS 3** | **Tile** is used |
| **Wear OS 4, 5, 6** | **Tile** is used |
| **Wear OS 7 (No partial-height support, e.g., Pixel Watch)** | **Tile** is used |
| **Wear OS 7 (Partial-height support, e.g., Galaxy Watch)** | **Widget** is used |

### Alternative: Single service (widget only)

A single service handles both protocols. While this approach is faster to
implement, it relies on a compatibility mode to "adapt" your widget into a tile
on devices running lower versions of Wear OS.

If you choose this approach:

1. **Specify both intent filters:** Your service must include intent filters for both `androidx.wear.tiles.action.BIND_TILE_PROVIDER` and `androidx.glance.wear.action.BIND_WIDGET_PROVIDER`. This ensures your widget is displayed on tile surfaces in Wear 4, 5, 6, and 7 (where required).
2. **Maintain your existing service name (for seamless upgrades):** If you are replacing an active tile, keeping the same service class name ensures that users who have your tile in their carousel will see it automatically update to the new widget. While Wear OS 7 uses the `group` attribute in the widget configuration XML to logically link different components, versions of Wear OS lower than 7 rely on the service name to identify them as the "same" component. If you prefer to use a new service name, your app will still function perfectly; however, users on devices running Wear OS version 6 or lower will need to manually re-add the widget to their carousel.

**System Behavior for Single Service Setup:**

| OS / Device Capability | Resulting Experience |
|---|---|
| **Wear OS 3** | **Not supported** |
| **Wear OS 4, 5, 6** | Widget is **displayed as a full screen tile** |
| **Wear OS 7 (No partial-height support)** | Widget is **translated to a tile** |
| **Wear OS 7 (Partial-height support)** | **Widget** is used |

\*Requires renderer 1.6+.

## UI Translation Tips

When translating your UI from ProtoLayout (Tiles) to Remote Compose (Widgets),
the mental model shifts from imperative layout builders to a state-driven,
Compose-based architecture where UI updates are handled through recomposition.
Keep the following principles in mind:

- **Adopt Declarative UI:** Replace imperative ProtoLayout builders ([`LayoutElementBuilders`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders)) with declarative Remote Compose equivalents, such as [`RemoteText`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/layout/RemoteText.composable), [`RemoteColumn`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/layout/RemoteColumn.composable), and [`RemoteBox`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/layout/RemoteBox.composable).
- **Focus on the Core Content (`mainSlot`):** Partial-height widgets (e.g., `SMALL` and `LARGE` container types) provide a focused, glanceable surface. Rather than porting a dense, full-screen Tile layout one-to-one, streamline your design to emphasize primary information within the main content area.
- **Redesign Edge-Aligned Actions:** In the tiles architecture, screen-hugging components like the [`EdgeButton`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/EdgeButton.composable) were anchored to a dedicated `bottomSlot`. Because partial-height widgets integrate directly into a vertically scrolling surface, this fixed `bottomSlot` paradigm no longer exists. Because edge-aligned buttons often served as highly prominent primary actions, migrating requires a deliberate UI redesign rather than a direct component swap. Evaluate alternative UX strategies for your primary actions:
  - **Inline Actions:** Integrate an inline [`RemoteButton`](https://developer.android.com/reference/kotlin/androidx/wear/compose/remote/material3/RemoteButton.composable) directly within your `mainSlot` layout.
  - **Container Taps:** Consolidate the interaction by making the entire widget container tappable using a [`PendingIntentAction`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/action/pendingIntentAction.composable).
  - **Content Pivot:** Re-evaluate the widget's focus. Without a dedicated action slot, consider surfacing richer glanceable data and relying on a single tap to open the full application rather than isolating specific actions on the widget surface.
- **Migrate Event Handling (Actions vs. Lambdas):** Tiles rely on interactions (like `LoadAction`) triggering full service callbacks to refresh the UI. Wear Widgets are client-side driven. Standard Compose lambdas cannot be run remotely; instead, provide serializable **Declarative Actions** (like [`ValueChange`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/action/package-summary#ValueChange(androidx.compose.remote.creation.compose.state.MutableRemoteState,androidx.compose.remote.creation.compose.state.RemoteState)) or [`PendingIntentAction`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/action/pendingIntentAction.composable)). Combine these with declarative state (e.g., [`rememberMutableRemoteInt`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/state/rememberMutableRemoteInt.composable)) to support instant UI updates without app round-trips.
- **Adapt Dimensions and Types:** When migrating layout dimensions, prefer deferred layout resolution using [`RemoteDp`](https://developer.android.com/reference/kotlin/androidx/compose/remote/creation/compose/state/RemoteDp) (e.g., `10.rdp`) over the standard `Dp`. This ensures the system renderer correctly calculates pixel values at display time. Similarly, use Remote Compose extension functions (`.rc` for `Color`, `.rs` for `String`, `.rdp` for `Dp`) to seamlessly convert standard Kotlin and Remote Compose types.
- **Review Sample Code:** To see comprehensive examples of how to build layouts, apply semantic typography, and manage state in Remote Compose, explore the official sample code available in the [Wear OS Samples
  repository](https://github.com/android/wear-os-samples/tree/main/WearWidget).