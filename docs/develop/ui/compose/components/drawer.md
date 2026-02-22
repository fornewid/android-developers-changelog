---
title: https://developer.android.com/develop/ui/compose/components/drawer
url: https://developer.android.com/develop/ui/compose/components/drawer
source: md.txt
---

The [navigation drawer](https://material.io/components/navigation-drawer) component is a slide-in menu that lets users navigate
to various sections of your app. Users can activate it by swiping from the side
or tapping a menu icon.

Consider these three use cases for implementing a Navigation Drawer:

- **Content organization:** Enable users to switch between different categories, such as in news or blogging apps.
- **Account management:** Provide quick links to account settings and profile sections in apps with user accounts.
- **Feature discovery:** Organize multiple features and settings in a single menu to facilitate user discovery and access in complex apps.

In Material Design, there are two types of navigation drawers:

- **Standard:** Share space within a screen with other content.
- **Modal:** Appears over the top of other content within a screen.

![An example of a Material Design 3 navigation drawer in light and dark mode.](https://developer.android.com/static/develop/ui/compose/images/layouts/material/m3-navigation-drawer.png) **Figure 1.** An example of a navigation drawer.

## Example

You can use the [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)) composable to implement a
navigation drawer.

Use the `drawerContent` slot to provide a [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and provide
the drawer's contents, as in the following example:


```kotlin
ModalNavigationDrawer(
    drawerContent = {
        ModalDrawerSheet {
            Text("Drawer title", modifier = Modifier.padding(16.dp))
            HorizontalDivider()
            NavigationDrawerItem(
                label = { Text(text = "Drawer Item") },
                selected = false,
                onClick = { /*TODO*/ }
            )
            // ...other drawer items
        }
    }
) {
    // Screen content
}
```

<br />

`ModalNavigationDrawer` accepts a number of additional drawer parameters. For
example, you can toggle whether or not the drawer responds to drags with the
`gesturesEnabled` parameter as in the following example:


```kotlin
ModalNavigationDrawer(
    drawerContent = {
        ModalDrawerSheet {
            // Drawer contents
        }
    },
    gesturesEnabled = false
) {
    // Screen content
}
```

<br />

## Control behavior

To control how the drawer opens and closes, use [`DrawerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState). You should
pass a `DrawerState` to `ModalNavigationDrawer` using the `drawerState`
parameter.

`DrawerState` provides access to the [`open`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState#open) and [`close`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState#close) functions, as
well as properties related to the current drawer state. These suspending
functions require a `CoroutineScope`, which you can instantiate using
[`rememberCoroutineScope`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope). You can also call the suspending functions in
response to UI events.


```kotlin
val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
val scope = rememberCoroutineScope()
ModalNavigationDrawer(
    drawerState = drawerState,
    drawerContent = {
        ModalDrawerSheet { /* Drawer content */ }
    },
) {
    Scaffold(
        floatingActionButton = {
            ExtendedFloatingActionButton(
                text = { Text("Show drawer") },
                icon = { Icon(Icons.Filled.Add, contentDescription = "") },
                onClick = {
                    scope.launch {
                        drawerState.apply {
                            if (isClosed) open() else close()
                        }
                    }
                }
            )
        }
    ) { contentPadding ->
        // Screen content
    }
}
```

<br />

## Create groups within a navigation drawer

The following snippet shows how to create a detailed navigation drawer, with
sections and dividers:


```kotlin
@Composable
fun DetailedDrawerExample(
    content: @Composable (PaddingValues) -> Unit
) {
    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()

    ModalNavigationDrawer(
        drawerContent = {
            ModalDrawerSheet {
                Column(
                    modifier = Modifier.padding(horizontal = 16.dp)
                        .verticalScroll(rememberScrollState())
                ) {
                    Spacer(Modifier.height(12.dp))
                    Text("Drawer Title", modifier = Modifier.padding(16.dp), style = MaterialTheme.typography.titleLarge)
                    HorizontalDivider()

                    Text("Section 1", modifier = Modifier.padding(16.dp), style = MaterialTheme.typography.titleMedium)
                    NavigationDrawerItem(
                        label = { Text("Item 1") },
                        selected = false,
                        onClick = { /* Handle click */ }
                    )
                    NavigationDrawerItem(
                        label = { Text("Item 2") },
                        selected = false,
                        onClick = { /* Handle click */ }
                    )

                    HorizontalDivider(modifier = Modifier.padding(vertical = 8.dp))

                    Text("Section 2", modifier = Modifier.padding(16.dp), style = MaterialTheme.typography.titleMedium)
                    NavigationDrawerItem(
                        label = { Text("Settings") },
                        selected = false,
                        icon = { Icon(Icons.Outlined.Settings, contentDescription = null) },
                        badge = { Text("20") }, // Placeholder
                        onClick = { /* Handle click */ }
                    )
                    NavigationDrawerItem(
                        label = { Text("Help and feedback") },
                        selected = false,
                        icon = { Icon(Icons.AutoMirrored.Outlined.Help, contentDescription = null) },
                        onClick = { /* Handle click */ },
                    )
                    Spacer(Modifier.height(12.dp))
                }
            }
        },
        drawerState = drawerState
    ) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = { Text("Navigation Drawer Example") },
                    navigationIcon = {
                        IconButton(onClick = {
                            scope.launch {
                                if (drawerState.isClosed) {
                                    drawerState.open()
                                } else {
                                    drawerState.close()
                                }
                            }
                        }) {
                            Icon(Icons.Default.Menu, contentDescription = "Menu")
                        }
                    }
                )
            }
        ) { innerPadding ->
            content(innerPadding)
        }
    }
}
```

<br />

### Key points about the code

- Populates the `drawerContent` with a `Column` containing sections, dividers, and navigation items.
- [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) provides Material Design styling for the drawer.
- [`HorizontalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color)) separates sections within the drawer.
- [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)) creates the drawer.
- `drawerContent` defines the content of the drawer.
- Inside the `ModalDrawerSheet`, a `Column` arranges the drawer elements vertically.
- [`NavigationDrawerItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationDrawerItem(kotlin.Function0,kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.NavigationDrawerItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) composables represent individual items in the drawer.
- The [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Scaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.FabPosition,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) provides the basic structure of the screen, including the [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)).
- The `navigationIcon` in the `TopAppBar` controls the drawer's open and close state.

### Result

The following image shows how the drawer appears when opened, with sections and
items displayed:
![A detailed navigation drawer with two sections, each with multiple labeled items and icons.](https://developer.android.com/static/develop/ui/compose/images/components/drawer-detailed.png) **Figure 2.** A navigation drawer opened with two nested groups.

## Additional resources

- Material Design: [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview)