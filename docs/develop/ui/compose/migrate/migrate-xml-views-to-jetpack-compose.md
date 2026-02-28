---
title: https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose
url: https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose
source: md.txt
---

Jetpack Compose supports interoperability with Views --- you
can use Compose in Views, and Views in Compose. This allows adoption of
Compose in existing View-based apps without having to migrate all Views
immediately.

## Migration steps

1. **Create a plan:** Create a robust and step-by-step plan for performing the migration. We recommend a prioritized backlog of migration tasks.
2. **Identify the XML candidate for migration :** Identify and start from the smallest components that are leaf nodes in the hierarchy, and expand the migration plan from the bottom up to progressively higher components in the hierarchy. Good candidates for initial migration are small, stateless, and have fewer dependencies.
3. **Analyze the hierarchy:** Once you identify the XML View to migrate, analyze its XML layout structure and implementation.
4. **Capture the initial state:** Run a screenshot test to capture the initial state of the selected XML View.
5. **Prerequisite: Set up Compose dependencies** Identify if the project has Compose dependencies and Compiler set up. If it doesn't, follow [Setup Compose dependencies and Compiler](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler).
6. **Prerequisite: Set up Compose theming** Identify if the project has Compose theming setup already. If it doesn't, follow ompose theming. Keep the original XML theming while the app is interop [Migrate XML Theme to Compose](https://developer.android.com/develop/ui/compose/designsystems/migrate-xml-theme-to-compose) to understand patterns of how to state and until the project is fully migrated to Compose.
7. **Migrate the XML View to Compose:** Start the conversion of the XML code to Compose, apply the appropriate theming, and add Compose Previews for migrated composables. For common migration scenarios, refer to additional resources. For example, for migrating to Lazy APIs in Compose, follow the steps in [Migrate RecyclerView to Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/recycler-view).
8. **Replace usages:** Replace the previous usages of the XML View to use the new Compose component. To add Compose in Views, follow the steps in [Compose in Views](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/compose-in-views). To add Views in Compose, follow the steps in [Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose).
9. **Validate the migration:** Verify that the initial state captured in the screenshot test is same as the Compose Preview of the migrated composable. If they don't match, iterate on the new composable UI and improve it to align it with the initial state. Create new Compose UI tests for the new composable.
10. **XML removal:** Once the newly migrated composable is matching the initial XML UI, remove the obsolete XML View code and its tests.

## Common migration scenarios

Verify `dp` and `sp` extensions are used (`16.dp`, `20.sp`) in composables.
If `tools:text` is present in the XML View, use it in a separate `@Preview`
composable.

### Attribute to Modifier conversion

Most XML attributes become part of the `modifier` chain or parameters of the
composable function.

| XML Attribute | Compose Equivalent |
|---|---|
| `android:layout_width="match_parent"` | `Modifier.fillMaxWidth()` |
| `android:layout_height="match_parent"` | `Modifier.fillMaxHeight()` |
| `android:layout_width="wrap_content"` | (Default behavior, usually no modifier needed) |
| `android:padding="Xdp"` | `Modifier.padding(X.dp)` |
| `android:layout_margin="Xdp"` | `Modifier.padding(X.dp)` (Outer padding) |
| `android:gravity="center"` | `contentAlignment = Alignment.Center` (Box) or `horizontalAlignment` / `verticalArrangement` (Column/Row) |
| `android:background="@color/white"` | `Modifier.background(colorResource(R.color.white))` |
| `android:visibility="gone"` | Wrap in `if (visible) { ... }` block |

## Migrate styles (styles.xml)

XML styles often combine multiple attributes to create a style. In Compose,
this is done by creating a **composable** variation with a specific style.

Provide separate @Composable functions named according to the style and the
base component,
to signify the difference in styling and use cases for those components.

- **Pattern:** If an XML element uses a custom style (e.g., `style="@style/MyPrimaryButton"`), don't try to replicate the style inline. Instead, suggest creating a specific composable.
- **Example:**
  - *XML:* `<Button style="@style/MyPrimaryButton" ... />`
  - *Compose:* `MyPrimaryButton(onClick = { ... })`
- **Common Attribute Groups:** If a style sets common modifiers (like padding + height), extract them into a readable extension property or a shared Modifier variable.