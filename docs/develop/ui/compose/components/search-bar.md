---
title: https://developer.android.com/develop/ui/compose/components/search-bar
url: https://developer.android.com/develop/ui/compose/components/search-bar
source: md.txt
---

Use a [search bar](https://m3.material.io/components/search/guidelines#3b162db3-8d55-425a-920b-95b1041ff999) to implement search functionality. A search
bar is a persistent search field that lets users enter a keyword or phrase to
display relevant results within your app, and is recommended when search is the
primary focus of your app.

> [!NOTE]
> **Note:** The [`SearchBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.Function0,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) composable is experimental.

![Two search bars are shown. The one on the left only has a text field.
The search bar on the left has a text field and a search suggestion beneath it.](https://developer.android.com/static/develop/ui/compose/images/components/m3-search-bar.png) **Figure 1.** A basic search bar (1) and a search bar with a suggestion (2).

## API surface

Use the [`SearchBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.Function0,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) composable to implement search bars. Key parameters for
this composable include the following:

- `inputField`: Defines the input field of the search bar. It typically utilizes `SearchBarDefaults.InputField`, which allows customization of:
  - `query`: The query text to be shown in the input field..
  - `onQueryChange`: Lambda to handle changes in the query string.
- `expanded`: A boolean indicating whether the search bar is expanded to show suggestions or filtered results.
- `onExpandedChange`: Lambda to handle changes in the dropdown's expanded state.

- `content`: The content of this search bar to display search results below the
  `inputField`.

## Search bar with suggestions

This snippet shows a basic implementation of `SearchBar` with suggestions:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SimpleSearchBar(
    textFieldState: TextFieldState,
    onSearch: (String) -> Unit,
    searchResults: List<String>,
    modifier: Modifier = Modifier
) {
    // Controls expansion state of the search bar
    var expanded by rememberSaveable { mutableStateOf(false) }

    Box(
        modifier
            .fillMaxSize()
            .semantics { isTraversalGroup = true }
    ) {
        SearchBar(
            modifier = Modifier
                .align(Alignment.TopCenter)
                .semantics { traversalIndex = 0f },
            inputField = {
                SearchBarDefaults.InputField(
                    query = textFieldState.text.toString(),
                    onQueryChange = { textFieldState.edit { replace(0, length, it) } },
                    onSearch = {
                        onSearch(textFieldState.text.toString())
                        expanded = false
                    },
                    expanded = expanded,
                    onExpandedChange = { expanded = it },
                    placeholder = { Text("Search") }
                )
            },
            expanded = expanded,
            onExpandedChange = { expanded = it },
        ) {
            // Display search results in a scrollable column
            Column(Modifier.verticalScroll(rememberScrollState())) {
                searchResults.forEach { result ->
                    ListItem(
                        headlineContent = { Text(result) },
                        modifier = Modifier
                            .clickable {
                                textFieldState.edit { replace(0, length, result) }
                                expanded = false
                            }
                            .fillMaxWidth()
                    )
                }
            }
        }
    }
}
```

<br />

### Key points about the code

- `rememberSaveable` ensures that whether the search bar is expanded or collapsed is preserved across configuration changes. It writes the remembered value into the hosting Activity's `savedInstanceState` bundle before the Activity is destroyed during a configuration change.
- The `semantics` modifier controls the TalkBack traversal order.
  - `isTraversalGroup` is set for `Box` to group all its child composables.
  - `traversalIndex` is set to specify the order in which TalkBack reads accessibility information from each group peer. TalkBack reads accessibility information on a peer with a negative value, such as `-1`, before a peer with a positive value, such as `1`. Because the value is a float, you can specify a custom order of many peers by setting values in between `-1.0` and `1.0` on each peer.
- The `SearchBar` contains an `inputField` for user input and a [`Column`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)) to display search suggestions.
  - `SearchBarDefaults.InputField` creates the input field and handles changes to the user query.
  - `onQueryChange` handles the text input and updates the state whenever the text in the input field changes.
  - `The expanded` state controls the visibility of the suggestion list.
- `searchResults.forEach { result -> ... }` iterates through the `searchResults` list and creates a `ListItem` for each result.
  - When a `ListItem` is clicked, it updates the `textFieldState`, collapses the search bar, and fills the `textField` with the selected search result.

### Result

![A search bar is shown with the letter 'a' typed inside of the bar. A list containing six search suggestions is displayed below the search bar.](https://developer.android.com/static/develop/ui/compose/images/components/search bar with suggestions displayed.png) **Figure 2.** A search bar with suggestions displayed.

## Search bar with filtered list

This example shows a `SearchBar` that filters a list based on the user's search
query:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CustomizableSearchBar(
    query: String,
    onQueryChange: (String) -> Unit,
    onSearch: (String) -> Unit,
    searchResults: List<String>,
    onResultClick: (String) -> Unit,
    modifier: Modifier = Modifier,
    // Customization options
    placeholder: @Composable () -> Unit = { Text("Search") },
    leadingIcon: @Composable (() -> Unit)? = { Icon(Icons.Default.Search, contentDescription = "Search") },
    trailingIcon: @Composable (() -> Unit)? = null,
    supportingContent: (@Composable (String) -> Unit)? = null,
    leadingContent: (@Composable () -> Unit)? = null,
) {
    // Track expanded state of search bar
    var expanded by rememberSaveable { mutableStateOf(false) }

    Box(
        modifier
            .fillMaxSize()
            .semantics { isTraversalGroup = true }
    ) {
        SearchBar(
            modifier = Modifier
                .align(Alignment.TopCenter)
                .semantics { traversalIndex = 0f },
            inputField = {
                // Customizable input field implementation
                SearchBarDefaults.InputField(
                    query = query,
                    onQueryChange = onQueryChange,
                    onSearch = {
                        onSearch(query)
                        expanded = false
                    },
                    expanded = expanded,
                    onExpandedChange = { expanded = it },
                    placeholder = placeholder,
                    leadingIcon = leadingIcon,
                    trailingIcon = trailingIcon
                )
            },
            expanded = expanded,
            onExpandedChange = { expanded = it },
        ) {
            // Show search results in a lazy column for better performance
            LazyColumn {
                items(count = searchResults.size) { index ->
                    val resultText = searchResults[index]
                    ListItem(
                        headlineContent = { Text(resultText) },
                        supportingContent = supportingContent?.let { { it(resultText) } },
                        leadingContent = leadingContent,
                        colors = ListItemDefaults.colors(containerColor = Color.Transparent),
                        modifier = Modifier
                            .clickable {
                                onResultClick(resultText)
                                expanded = false
                            }
                            .fillMaxWidth()
                            .padding(horizontal = 16.dp, vertical = 4.dp)
                    )
                }
            }
        }
    }
}
```

<br />

### Key points about the code

- The `onQueryChange` lambda function is called whenever the user types or deletes text in the search bar.
- `SearchBarDefaults.InputField` contains a `leadingIcon`, which adds a search icon to the beginning of the input field, and a `trailingIcon`, which adds a "more options" icon to the end of the input field. Here, you can provide sorting and filtering options to the user.
- `onSearch = { ... }` calls the `onSearch` lambda and collapses the search bar when the search is submitted.
- A `LazyColumn` handles a potentially large number of search results efficiently. It iterates through the `searchResults` list and displays each result as a `ListItem`.
- Each `ListItem` composable shows the item text, text showing additional information, and a star icon as the item's `leadingContent`. In this example, an option to favorite the item is presented.
- For the filtering logic, see `CustomizableSearchBarExample` in the [full
  source code on GitHub](https://github.com/android/snippets/blob/030dddb8f6f319ffb1b3809fe71add6417531fe2/compose/snippets/src/main/java/com/example/compose/snippets/components/SearchBar.kt).

### Result

![A search bar containing the words hinted text search inside is shown. Below the search bar, a list of search suggestions is displayed, with a star icon beside each suggestion.](https://developer.android.com/static/develop/ui/compose/images/components/search bar with relevant suggestions displayed.png) **Figure 3.** A search bar with relevant suggestions displayed.

## Additional resources

- Material Design: [Search bar](https://m3.material.io/components/search/guidelines#3b162db3-8d55-425a-920b-95b1041ff999)