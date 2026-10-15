---
title: API source code for Glimmer List component  |  Android Developers
url: https://developer.android.com/agents/skills/xr/display-glasses-with-jetpack-compose-glimmer/references/list-source
source: html-scrape
---

# API source code for Glimmer List component Stay organized with collections Save and categorize content based on your preferences.





When creating a Glimmer List component, refer to the following source code in
`GlimmerLazyColumnSamples.kt`:

```
@Composable
fun GlimmerLazyColumnSample() {
    GlimmerLazyColumn {
        item { ListItem { Text("Header") } }
        items(count = 10) { index -> ListItem { Text("Item-$index") } }
        item { ListItem { Text("Footer") } }
    }
}

GlimmerLazyColumnSamples.kt
```

```
@Composable
fun GlimmerLazyColumnWithTitleChipSample() {
    val ingredientItems =
        listOf("Milk", "Flour", "Egg", "Salt", "Apples", "Butter", "Vanilla", "Sugar", "Cinnamon")
    GlimmerLazyColumn(title = { TitleChip { Text("Ingredients") } }) {
        items(ingredientItems) { text -> ListItem { Text(text) } }
    }
}

GlimmerLazyColumnSamples.kt
```