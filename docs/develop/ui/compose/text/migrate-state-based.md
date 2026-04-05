---
title: https://developer.android.com/develop/ui/compose/text/migrate-state-based
url: https://developer.android.com/develop/ui/compose/text/migrate-state-based
source: md.txt
---

This page provides examples of how you can migrate value-based `TextField`s to
state-based `TextField`s. See the [Configure text fields](https://developer.android.com/develop/ui/compose/text/user-input) page for
information on the differences between value and state-based `TextField`s.

## Basic usage

### Value-based


```kotlin
@Composable
fun OldSimpleTextField() {
    var state by rememberSaveable { mutableStateOf("") }
    TextField(
        value = state,
        onValueChange = { state = it },
        singleLine = true,
    )
}
```

<br />

### State-based


```kotlin
@Composable
fun NewSimpleTextField() {
    TextField(
        state = rememberTextFieldState(),
        lineLimits = TextFieldLineLimits.SingleLine
    )
}
```

<br />

- Replace the `value, onValueChange`, and `remember { mutableStateOf("")` } with `rememberTextFieldState()`.
- Replace `singleLine = true` with `lineLimits =
  TextFieldLineLimits.SingleLine`.

## Filtering through `onValueChange`

### Value-based


```kotlin
@Composable
fun OldNoLeadingZeroes() {
    var input by rememberSaveable { mutableStateOf("") }
    TextField(
        value = input,
        onValueChange = { newText ->
            input = newText.trimStart { it == '0' }
        }
    )
}
```

<br />

### State-based


```kotlin
@Preview
@Composable
fun NewNoLeadingZeros() {
    TextField(
        state = rememberTextFieldState(),
        inputTransformation = InputTransformation {
            while (length > 0 && charAt(0) == '0') delete(0, 1)
        }
    )
}
```

<br />

- Replace the value callback loop with `rememberTextFieldState()`.
- Re-implement the filtering logic in `onValueChange` using `InputTransformation`.
- Use `TextFieldBuffer` from the receiver scope of `InputTransformation` to update the `state`.
  - `InputTransformation` is called exactly right after user input is detected.
  - Changes that are proposed by `InputTransformation` through `TextFieldBuffer` are applied immediately, avoiding a synchronization issue between the software keyboard and `TextField`.

## Credit card formatter `TextField`

### Value-based


```kotlin
@Composable
fun OldTextFieldCreditCardFormatter() {
    var state by remember { mutableStateOf("") }
    TextField(
        value = state,
        onValueChange = { if (it.length <= 16) state = it },
        visualTransformation = VisualTransformation { text ->
            // Making XXXX-XXXX-XXXX-XXXX string.
            var out = ""
            for (i in text.indices) {
                out += text[i]
                if (i % 4 == 3 && i != 15) out += "-"
            }

            TransformedText(
                text = AnnotatedString(out),
                offsetMapping = object : OffsetMapping {
                    override fun originalToTransformed(offset: Int): Int {
                        if (offset <= 3) return offset
                        if (offset <= 7) return offset + 1
                        if (offset <= 11) return offset + 2
                        if (offset <= 16) return offset + 3
                        return 19
                    }

                    override fun transformedToOriginal(offset: Int): Int {
                        if (offset <= 4) return offset
                        if (offset <= 9) return offset - 1
                        if (offset <= 14) return offset - 2
                        if (offset <= 19) return offset - 3
                        return 16
                    }
                }
            )
        }
    )
}
```

<br />

### State-based


```kotlin
@Composable
fun NewTextFieldCreditCardFormatter() {
    val state = rememberTextFieldState()
    TextField(
        state = state,
        inputTransformation = InputTransformation.maxLength(16),
        outputTransformation = OutputTransformation {
            if (length > 4) insert(4, "-")
            if (length > 9) insert(9, "-")
            if (length > 14) insert(14, "-")
        },
    )
}
```

<br />

- Replace the filtering in `onValueChange` with an `InputTransformation` to set the max length of the input.
  - Refer to the [Filtering through `onValueChange`](https://developer.android.com/develop/ui/compose/text/migrate-state-based#filtering-through) section.
- Replace `VisualTransformation` with `OutputTransformation` to add in dashes.
  - With `VisualTransformation`, you are responsible for both creating the new text with the dashes and also calculating how the indices are mapped between the visual text and the backing state.
  - `OutputTransformation` takes care of the offset mapping automatically. You just need to add the dashes in correct places using the `TextFieldBuffer` from `OutputTransformation.transformOutput`'s receiver scope.

## Updating the state (simple)

### Value-based


```kotlin
@Composable
fun OldTextFieldStateUpdate(userRepository: UserRepository) {
    var username by remember { mutableStateOf("") }
    LaunchedEffect(Unit) {
        username = userRepository.fetchUsername()
    }
    TextField(
        value = username,
        onValueChange = { username = it }
    )
}
```

<br />

### State-based


```kotlin
@Composable
fun NewTextFieldStateUpdate(userRepository: UserRepository) {
    val usernameState = rememberTextFieldState()
    LaunchedEffect(Unit) {
        usernameState.setTextAndPlaceCursorAtEnd(userRepository.fetchUsername())
    }
    TextField(state = usernameState)
}
```

<br />

- Replace the value callback loop with `rememberTextFieldState()`.
- Change the value assignment with `TextFieldState.setTextAndPlaceCursorAtEnd`.

## Updating the state (complex)

### Value-based


```kotlin
@Composable
fun OldTextFieldAddMarkdownEmphasis() {
    var markdownState by remember { mutableStateOf(TextFieldValue()) }
    Button(onClick = {
        // add ** decorations around the current selection, also preserve the selection
        markdownState = with(markdownState) {
            copy(
                text = buildString {
                    append(text.take(selection.min))
                    append("**")
                    append(text.substring(selection))
                    append("**")
                    append(text.drop(selection.max))
                },
                selection = TextRange(selection.min + 2, selection.max + 2)
            )
        }
    }) {
        Text("Bold")
    }
    TextField(
        value = markdownState,
        onValueChange = { markdownState = it },
        maxLines = 10
    )
}
```

<br />

### State-based


```kotlin
@Composable
fun NewTextFieldAddMarkdownEmphasis() {
    val markdownState = rememberTextFieldState()
    LaunchedEffect(Unit) {
        // add ** decorations around the current selection
        markdownState.edit {
            insert(originalSelection.max, "**")
            insert(originalSelection.min, "**")
            selection = TextRange(originalSelection.min + 2, originalSelection.max + 2)
        }
    }
    TextField(
        state = markdownState,
        lineLimits = TextFieldLineLimits.MultiLine(1, 10)
    )
}
```

<br />

In this use case, a button adds the Markdown decorations to make the text bold
around the cursor or the current selection. It also maintains the selection
position after the changes.

- Replace the value callback loop with `rememberTextFieldState()`.
- Replace `maxLines = 10` with `lineLimits =
  TextFieldLineLimits.MultiLine(maxHeightInLines = 10)`.
- Change the logic of calculating a new `TextFieldValue` with a `TextFieldState.edit` call.
  - A new `TextFieldValue` is generated by splicing the existing text based on the current selection, and inserting the Markdown decorations in between.
  - Also the selection is adjusted according to new indices of the text.
  - `TextFieldState.edit` has a more natural way of editing the current state with the use of `TextFieldBuffer`.
  - The selection explicitly defines where to insert the decorations.
  - Then, adjust the selection, similar to the `onValueChange` approach.

## ViewModel `StateFlow` architecture

Many applications follow the [Modern app development guidelines](https://developer.android.com/topic/architecture/ui-layer/state-production), which
promote using a `StateFlow` to define the UI state of a screen or a component
through a single immutable class that carries all the information.

In these types of applications, a form like a Login screen with text input is
usually designed as follows:


```kotlin
class LoginViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState>
        get() = _uiState.asStateFlow()

    fun updateUsername(username: String) = _uiState.update { it.copy(username = username) }

    fun updatePassword(password: String) = _uiState.update { it.copy(password = password) }
}

data class UiState(
    val username: String = "",
    val password: String = ""
)

@Composable
fun LoginForm(
    loginViewModel: LoginViewModel,
    modifier: Modifier = Modifier
) {
    val uiState by loginViewModel.uiState.collectAsStateWithLifecycle()
    Column(modifier) {
        TextField(
            value = uiState.username,
            onValueChange = { loginViewModel.updateUsername(it) }
        )
        TextField(
            value = uiState.password,
            onValueChange = { loginViewModel.updatePassword(it) },
            visualTransformation = PasswordVisualTransformation()
        )
    }
}
```

<br />

This design perfectly fits with the `TextFields` that use the `value,
onValueChange` state hoisting paradigm. However, there are unpredictable
downsides to this approach when it comes to text input. The deep synchronization
issues with this approach are explained in detail in the [Effective state
management for TextField in Compose](https://medium.com/androiddevelopers/effective-state-management-for-textfield-in-compose-d6e5b070fbe5) blog post.

The problem is that the new `TextFieldState` design is not directly compatible
with the `StateFlow` backed ViewModel UI state. It may look strange to replace
`username: String` and `password: String` with `username: TextFieldState` and
`password: TextFieldState`, since `TextFieldState` is an inherently mutable data
structure.

A common recommendation is to avoid placing UI dependencies into a `ViewModel`.
Although this is generally a good practice, it can sometimes be misinterpreted.
This is particularly true for Compose dependencies that are purely data
structures and don't carry any UI elements with them, like `TextFieldState`.

Classes like `MutableState` or `TextFieldState` are simple state holders that
are backed by Compose's Snapshot state system. They are no different from
dependencies like `StateFlow` or `RxJava`. Therefore,we encourage you to
re-evaluate how you apply the "no UI dependencies in ViewModel" principle in
your code. Keeping a reference to a `TextFieldState` within your `ViewModel` is
not an inherently bad practice.

> [!NOTE]
> **Note:** The `@Composable rememberTextFieldState()` function includes the save-and-restore mechanism that comes with `rememberSaveable` and `TextFieldState.Saver`. If you initialize your `TextFieldState` in your ViewModel, handle this logic separately, as described in the [Saved State
> module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate) page.

### Recommended simple approach

We recommend you extract values like `username` or `password` from `UiState`,
and keep a separate reference for them in the `ViewModel`.


```kotlin
class LoginViewModel : ViewModel() {
    val usernameState = TextFieldState()
    val passwordState = TextFieldState()
}

@Composable
fun LoginForm(
    loginViewModel: LoginViewModel,
    modifier: Modifier = Modifier
) {
    Column(modifier) {
        TextField(state = loginViewModel.usernameState,)
        SecureTextField(state = loginViewModel.passwordState)
    }
}
```

<br />

- Replace `MutableStateFlow<UiState>` with a couple `TextFieldState` values.
- Pass those `TextFieldState` objects to `TextFields` in the `LoginForm` composable.

### Conforming approach

These types of architectural changes are not always easy. You may not have the
freedom to make these changes, or the time investment could outweigh the
benefits of using the new `TextField`s. In this case, you can still use
state-based text fields with a little tweak.


```kotlin
class LoginViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState>
        get() = _uiState.asStateFlow()

    fun updateUsername(username: String) = _uiState.update { it.copy(username = username) }

    fun updatePassword(password: String) = _uiState.update { it.copy(password = password) }
}

data class UiState(
    val username: String = "",
    val password: String = ""
)

@Composable
fun LoginForm(
    loginViewModel: LoginViewModel,
    modifier: Modifier = Modifier
) {
    val initialUiState = remember(loginViewModel) { loginViewModel.uiState.value }
    Column(modifier) {
        val usernameState = rememberTextFieldState(initialUiState.username)
        LaunchedEffect(usernameState) {
            snapshotFlow { usernameState.text.toString() }.collectLatest {
                loginViewModel.updateUsername(it)
            }
        }
        TextField(usernameState)

        val passwordState = rememberTextFieldState(initialUiState.password)
        LaunchedEffect(usernameState) {
            snapshotFlow { usernameState.text.toString() }.collectLatest {
                loginViewModel.updatePassword(it)
            }
        }
        SecureTextField(passwordState)
    }
}
```

<br />

- Keep your `ViewModel` and `UiState` classes the same.
- Instead of hoisting the state directly into `ViewModel` and making it the source of the truth for `TextFields`, turn `ViewModel` into a simple data holder.
  - To do this, observe the changes to each `TextFieldState.text` by collecting a `snapshotFlow` in a `LaunchedEffect`.
- Your `ViewModel` will still have the latest values from UI, but its `uiState:
  StateFlow<UiState>` won't be driving the `TextField`s.
- Any other persistence logic implemented in your `ViewModel` can stay the same.