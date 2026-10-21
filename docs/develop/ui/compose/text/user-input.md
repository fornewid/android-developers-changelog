---
title: https://developer.android.com/develop/ui/compose/text/user-input
url: https://developer.android.com/develop/ui/compose/text/user-input
source: md.txt
---

> [!CAUTION]
> **Caution:** [Value-based text fields](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicTextField.composable#BasicTextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.ui.text.input.VisualTransformation,kotlin.Function1,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,kotlin.Function1)) are deprecated. To migrate to the recommended state-based text fields, see [Migrate to state-based text fields](https://developer.android.com/develop/ui/compose/text/migrate-state-based).

[`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable#TextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.ScrollState,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)) allows users to enter and modify text. This page describes how
you can implement `TextField`, style `TextField` input, and configure
other `TextField` options, like keyboard options and visually transforming
user input.

## Choose `TextField` implementation

There are two levels of `TextField` implementation:

1. `TextField` is the Material Design implementation. We recommend you choose this implementation as it follows [Material Design
   guidelines](https://material.io/components/text-fields):
   - Default styling is [filled](https://material.io/components/text-fields#filled-text-field)
   - `OutlinedTextField` is the [outlined](https://material.io/components/text-fields#outlined-text-field) styling version
2. [`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable#TextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.ScrollState,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)) enables users to edit text using the hardware or software keyboard, but provides no decorations like hint or placeholder.


```kotlin
TextField(
    state = rememberTextFieldState(initialText = "Hello"),
    label = { Text("Label") }
)
```

<br />

![An editable text field containing the word](https://developer.android.com/static/develop/ui/compose/images/text-textfield-hello.png)


```kotlin
OutlinedTextField(
    state = rememberTextFieldState(),
    label = { Text("Label") }
)
```

<br />

![An editable text field, with a purple border and label.](https://developer.android.com/static/develop/ui/compose/images/text-outlinedtextfield.png)

## Style `TextField`

`TextField` and `BasicTextField` share many common parameters for customization.
The complete list for `TextField` is available in the
[`TextField` source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/TextField.kt?q=file:androidx/compose/material3/TextField.kt+function:TextField). This is a non-exhaustive list of some of the
useful parameters:

- `textStyle`
- `lineLimits`


```kotlin
TextField(
    state = rememberTextFieldState("Hello\nWorld\nInvisible"),
    lineLimits = TextFieldLineLimits.MultiLine(maxHeightInLines = 2),
    placeholder = { Text("") },
    textStyle = TextStyle(color = Color.Blue, fontWeight = FontWeight.Bold),
    label = { Text("Enter text") },
    modifier = Modifier.padding(20.dp)
)
```

<br />

![A multiline TextField, with two editable lines plus the label](https://developer.android.com/static/develop/ui/compose/images/text-textfield-multiline.png)

We recommend `TextField` over `BasicTextField` when your design calls for a
Material `TextField` or `OutlinedTextField`. However, `BasicTextField` should be
used when building designs that don't need the decorations from the Material
spec.

## Configure line limits

`TextField` composables support scrolling along a single axis. The scrolling
behavior is determined by the `lineLimits` parameter. `TextField`s configured
for a single line scroll horizontally, while multi-line `TextField`s scroll
vertically.

Use `TextFieldLineLimits` to choose the appropriate line configuration for your
`TextField`:


```kotlin
TextField(
    state = rememberTextFieldState(),
    lineLimits = TextFieldLineLimits.SingleLine
)
```

<br />

![A single line text field with the text](https://developer.android.com/static/develop/ui/compose/images/text/single-line-config.png)

The `SingleLine` configuration has the following characteristics:

- The text never wraps, and doesn't allow for new lines.
- `TextField` always has a fixed height.
- If the text overflows, it scrolls horizontally.


```kotlin
TextField(
    state = rememberTextFieldState("Hello\nWorld\nHello\nWorld"),
    lineLimits = TextFieldLineLimits.MultiLine(1, 4)
)
```

<br />

![A multiline text field with the text](https://developer.android.com/static/develop/ui/compose/images/text/multi-line-config.png)

The `MultiLine` configuration has the following characteristics:

- Accepts two parameters: `minHeightInLines` and `maxHeightInLines`.
- The text field is at least `minHeightInLines` tall.
- If the text overflows, it will wrap.
- If the text requires more lines, the field grows until it is `maxHeightInLines` tall, and scrolls vertically.

## Style input with Brush API

You can use the [Brush API](https://developer.android.com/develop/ui/compose/text/style-text#brush) for more advanced styling in your `TextField`.
The following section describes how you can use a Brush to add a colored
gradient to `TextField` input.

For more information about using the Brush API to style text, see
[Enable advanced styling with Brush API](https://developer.android.com/develop/ui/compose/text/style-text#brush).

### Implement colored gradients using `TextStyle`

To implement a colored gradient as you type within a `TextField`, set your brush
of choice as a [`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle) for your `TextField`. In this example, we use a
built-in brush with a `linearGradient` to view the rainbow gradient effect as
text is typed into the `TextField`.


```kotlin
val brush = remember {
    Brush.linearGradient(
        colors = listOf(Color.Red, Color.Yellow, Color.Green, Color.Blue, Color.Magenta)
    )
}
TextField(
    state = rememberTextFieldState(), textStyle = TextStyle(brush = brush)
)
```

<br />

![Text being typed in a text field, displaying a rainbow gradient effect.](https://developer.android.com/static/develop/ui/compose/images/text-textfieldgradient.gif) **Figure 1.** A rainbow gradient effect for `TextField` content.

## Manage text field state

`TextField` uses a dedicated state holder class called `TextFieldState` for its
content and selection. `TextFieldState` is designed to be hoisted
wherever it fits in your architecture. There are 2 main properties that are
provided by `TextFieldState`:

- `initialText`: Contents of the `TextField`.
- `initialSelection`: Indicates where the cursor or the selection is.

What differentiates `TextFieldState` from other approaches, like the
`onValueChange` callback, is that `TextFieldState` fully encapsulates the entire
input flow. This includes using the correct backing data structures, inlining
filters and formatters, and also synchronizing all edits coming from different
sources.

> [!NOTE]
> **Note:** Although `TextFieldState` belongs to the Compose Foundation module, it has no UI dependencies and is designed to be a powerful state holder. `TextFieldState` only uses data structures provided by Compose's snapshot system. It is encouraged to instantiate and hold `TextFieldState` instances in your ViewModels.

You can use `TextFieldState()` to hoist state in `TextField`. For this, we
recommend using the `rememberTextFieldState()` function.
`rememberTextFieldState()` creates the `TextFieldState` instance in your
composable, makes sure the state object is remembered, and provides
built-in save and restore functionality:


```kotlin
val usernameState = rememberTextFieldState()
TextField(
    state = usernameState,
    lineLimits = TextFieldLineLimits.SingleLine,
    placeholder = { Text("Enter Username") }
)
```

<br />

`rememberTextFieldState` can have a blank parameter or have an initial value
passed in to represent the text's value on initialization. If a different value
is passed in a subsequent recomposition, the value of the state is not updated.
To update the state after it's initialized, call edit methods on
`TextFieldState`.


```kotlin
TextField(
    state = rememberTextFieldState(initialText = "Username"),
    lineLimits = TextFieldLineLimits.SingleLine,
)
```

<br />

![A TextField with the text Username appearing inside the text field.](https://developer.android.com/static/develop/ui/compose/images/text/tf-username.png) **Figure 2.** `TextField` with "Username" as the initial text.

### Modify text with `TextFieldBuffer`

A `TextFieldBuffer` serves as an editable text container, similar in function to
a `StringBuilder`. It holds both the text content and information about the
selection.

You often encounter `TextFieldBuffer` as a receiver scope on functions like
`TextFieldState.edit`, `InputTransformation.transformInput`, or
`OutputTransformation.transformOutput`. In these functions, you can read or
update the `TextFieldBuffer` as needed. Afterwards, these changes are either
committed to `TextFieldState`, or passed down to the rendering pipeline in the
case of `OutputTransformation`.

You can use standard editing functions like `append`, `insert`, `replace`, or
`delete` to modify the buffer's contents. To change the selection state, either
directly set its `selection: TextRange` variable, or use utility functions such
as `placeCursorAtEnd` or `selectAll`. The selection itself is represented by a
`TextRange`, where the start index is inclusive and the end index is exclusive.
A `TextRange` with identical start and end values, like `(3, 3)`, signifies a
cursor position with no characters selected.


```kotlin
val phoneNumberState = rememberTextFieldState("1234567890")

TextField(
    state = phoneNumberState,
    keyboardOptions = KeyboardOptions(
        keyboardType = KeyboardType.Phone
    ),
    inputTransformation = InputTransformation.maxLength(10).then {
        if (!asCharSequence().isDigitsOnly()) {
            revertAllChanges()
        }
    },
    outputTransformation = OutputTransformation {
        if (length > 0) insert(0, "(")
        if (length > 4) insert(4, ")")
        if (length > 8) insert(8, "-")
    }
)
```

<br />

### Edit text in `TextFieldState`

There are several methods that allow you to edit the state directly through
your state variable:

- `edit`: Lets you edit the state contents and gives you `TextFieldBuffer`
  functions so you can use methods like `insert`, `replace`, `append`, and more.


  ```kotlin
  // Initial textFieldState text passed in is "I love Android"
  // textFieldState.text : I love Android
  // textFieldState.selection: TextRange(14, 14)
  textFieldState.edit { insert(14, "!") }
  // textFieldState.text : I love Android!
  // textFieldState.selection: TextRange(15, 15)
  textFieldState.edit { replace(7, 14, "Compose") }
  // textFieldState.text : I love Compose!
  // textFieldState.selection: TextRange(15, 15)
  textFieldState.edit { append("!!!") }
  // textFieldState.text : I love Compose!!!!
  // textFieldState.selection: TextRange(18, 18)
  textFieldState.edit { selectAll() }
  // textFieldState.text : I love Compose!!!!
  // textFieldState.selection: TextRange(0, 18)
  ```

  <br />

- `setTextAndPlaceCursorAtEnd`: Clears the current text, replaces it with the
  given text, and sets the cursor at the end.


  ```kotlin
  textFieldState.setTextAndPlaceCursorAtEnd("I really love Android")
  // textFieldState.text : I really love Android
  // textFieldState.selection : TextRange(21, 21)
  ```

  <br />

- `clearText`: Clears all text.


  ```kotlin
  textFieldState.clearText()
  // textFieldState.text :
  // textFieldState.selection : TextRange(0, 0)
  ```

  <br />

For other `TextFieldState` functions, see the [`TextFieldState` reference](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#extension-functions_1).

## Modify user input

The following sections describe how to modify user input.
[Input transformation](https://developer.android.com/develop/ui/compose/text/user-input#filter-input-transformations)
lets you filter `TextField` input while the user is typing, while [output
transformation](https://developer.android.com/develop/ui/compose/text/user-input#format-input-display) formats user input before it's displayed
on-screen.

### Filter user input with input transformations

An input transformation lets you filter input from the user. For example, if
your `TextField` takes in an American phone number, you only want to accept 10
digits. The results of the `InputTransformation` are saved in the
`TextFieldState`.

> [!NOTE]
> **Note:** Don't mutate state inside the `InputTransformation.transformInput()` call. Instead, use the receiver scope `TextFieldBuffer` to edit text.

There are built-in filters for common `InputTransformation` use cases. To limit
length, call `InputTransformation.maxLength()`:


```kotlin
TextField(
    state = rememberTextFieldState(),
    lineLimits = TextFieldLineLimits.SingleLine,
    inputTransformation = InputTransformation.maxLength(10)
)
```

<br />

#### Custom input transformations

`InputTransformation` is a single function interface. When implementing your
custom `InputTransformation`, you need to override
`TextFieldBuffer.transformInput`:


```kotlin
class CustomInputTransformation : InputTransformation {
    override fun TextFieldBuffer.transformInput() {
    }
}
```

<br />

For a phone number, add a custom input transformation that only allows digits
to be typed into the `TextField`:


```kotlin
class DigitOnlyInputTransformation : InputTransformation {
    override fun TextFieldBuffer.transformInput() {
        if (!asCharSequence().isDigitsOnly()) {
            revertAllChanges()
        }
    }
}
```

<br />

#### Chain input transformations

To add multiple filters on your text input, chain `InputTransformation`s using
the [`then`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/InputTransformation#(androidx.compose.foundation.text.input.InputTransformation).then(androidx.compose.foundation.text.input.InputTransformation)) extension function. Filters are executed sequentially. As a
best practice, apply the most selective filters first to avoid unnecessary
transformations on data that would ultimately be filtered out.


```kotlin
TextField(
    state = rememberTextFieldState(),
    inputTransformation = InputTransformation.maxLength(6)
        .then(CustomInputTransformation()),
)
```

<br />

After adding input transformations, the `TextField` input accepts 10 digits
maximum.

### Format input before it's displayed

`OutputTransformation`s let you format user input before it is rendered on the
screen. Unlike `InputTransformation`, the formatting done through the
`OutputTransformation` is not saved in the `TextFieldState`. Building on the
previous phone number example, you need to add parentheses and dashes in
the appropriate places:
![An American phone number, properly formatted with parentheses, dashes, and corresponding indexes.](https://developer.android.com/static/develop/ui/compose/images/text/tf-phonenumber.png) **Figure 3.** An American phone number with proper formatting and corresponding indexes.

`OutputTransformation` replaces `VisualTransformation` from value-based text
fields, with the key difference being that you don't calculate offset mappings.

`OutputTransformation` is a single abstract method interface. In order to
implement a custom `OutputTransformation`, you need to override the
`transformOutput` method:


```kotlin
class CustomOutputTransformation : OutputTransformation {
    override fun TextFieldBuffer.transformOutput() {
    }
}
```

<br />

To format a phone number, add an opening parenthesis at index 0, a closing
parenthesis at index 4, and a dash at index 8 to your `OutputTransformation`:


```kotlin
class PhoneNumberOutputTransformation : OutputTransformation {
    override fun TextFieldBuffer.transformOutput() {
        if (length > 0) insert(0, "(")
        if (length > 4) insert(4, ")")
        if (length > 8) insert(8, "-")
    }
}
```

<br />

Next, add your `OutputTransformation` to `TextField`:


```kotlin
TextField(
    state = rememberTextFieldState(),
    outputTransformation = PhoneNumberOutputTransformation()
)
```

<br />

### How transformations work together

The following diagram shows the flow from text input to transformation to
output:
![A visualization of how text input goes through transformations before it becomes text output.](https://developer.android.com/static/develop/ui/compose/images/text/tf-transformation-diagram.png) **Figure 4.** A diagram showing how text input goes through transformations before it becomes text output.

1. Input is received from the input source.
2. The input is filtered through an `InputTransformation`, which gets saved in the TextFieldState.
3. The input is passed through an `OutputTransformation` for formatting.
4. The input is presented in the `TextField`.

## Set keyboard options

`TextField` lets you set keyboard configuration options, such as the keyboard
layout, or enable the autocorrect if it's supported by the keyboard. Some
options may not be guaranteed if the software keyboard doesn't comply with the
options provided here. Here is the list of the [supported keyboard
options](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/KeyboardOptions#KeyboardOptions(androidx.compose.ui.text.input.KeyboardCapitalization,kotlin.Boolean,androidx.compose.ui.text.input.KeyboardType,androidx.compose.ui.text.input.ImeAction)):

- `capitalization`
- `autoCorrect`
- `keyboardType`
- `imeAction`

The `KeyboardOptions` class now includes a new boolean parameter,
`showKeyboardOnFocus`, which you use specifically for `TextField` components
that are integrated with `TextFieldState`. This option governs the behavior of
the software keyboard when the `TextField` acquires focus through means other
than direct user interaction (for example, programmatically).

When `KeyboardOptions.showKeyboardOnFocus` is set to true, the software keyboard
does not automatically appear if the `TextField` gains focus indirectly. In
such cases, the user is required to explicitly tap on the `TextField` itself to
reveal the keyboard.

### Define keyboard interaction logic

The action button on Android's software keyboard allows for interactive
responses within your application. For more information about configuring the
action button, see the [Set keyboard options](https://developer.android.com/develop/ui/compose/text/user-input#keyboard-options) section.
![A software keyboard action button (a checkmark icon) circled in red.](https://developer.android.com/static/develop/ui/compose/images/text/tf-action-button.png) **Figure 5.** Software keyboard action button.

To define what occurs when a user taps this action button, use the
`onKeyboardAction` parameter. This parameter accepts an optional functional
interface named `KeyboardActionHandler`. The `KeyboardActionHandler` interface
contains a single method, `onKeyboardAction(performDefaultAction: () -> Unit)`.
By providing an implementation for this `onKeyboardAction` method, you can
introduce custom logic that executes when a user presses the keyboard's action
button.

Several standard keyboard action types come with built-in default behaviors.
For example, selecting `ImeAction.Next` or `ImeAction.Previous` as the action
type will, by default, shift focus to the subsequent or preceding input field,
respectively. Similarly, an action button set to `ImeAction.Done` typically
dismisses the software keyboard. These default functionalities are executed
automatically and don't require you to supply a `KeyboardActionHandler`.

You can also implement custom behavior in addition to these default actions.
When you provide your `KeyboardActionHandler`, its `onKeyboardAction` method
receives a `performDefaultAction` function. You can call this
`performDefaultAction()` function at any point within your custom logic to also
trigger the standard default behavior associated with the current IME action.


```kotlin
TextField(
    state = textFieldViewModel.usernameState,
    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Next),
    onKeyboardAction = { performDefaultAction ->
        textFieldViewModel.validateUsername()
        performDefaultAction()
    }
)
```

<br />

This snippet illustrates a common use case on a registration screen
featuring a username field. For this field, `ImeAction.Next` is selected for
its keyboard action button. This choice enables quick, seamless navigation to
the subsequent password field.

In addition to this standard navigation, there's a requirement to initiate a
background validation process for the username as the user proceeds to enter
their password. To make sure that the default focus-switching behavior inherent
to `ImeAction.Next` is retained alongside this custom validation logic, the
`performDefaultAction()` function is invoked. Calling `performDefaultAction()`
implicitly triggers the underlying focus management system to move the focus to
the next appropriate UI element, preserving the expected navigational flow.

## Create a secure password field

[`SecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SecureTextField.composable#SecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)) is a composable built on top of state-based text fields
for writing a password field. We recommend using `SecureTextField` for creating
password text fields, as it hides character input by default and disables cut
and copy actions.

`SecureTextField` has a `textObfuscationMode`, which controls how the user sees
character input. `textObfuscationMode` has the following options:

- `Hidden`: Hides all input. Default behavior on desktop platforms.

  ![A secure text field where typed characters are hidden.](https://developer.android.com/static/develop/ui/compose/images/text/hide-input.gif)
- `Visible`: Shows all input.

  ![A secure text field where typed characters are visible.](https://developer.android.com/static/develop/ui/compose/images/text/show-input.gif)
- `RevealLastTyped`: Hides all input except the last character. Default
  behavior on mobile devices.

  ![A secure text field where only the last typed character is briefly revealed.](https://developer.android.com/static/develop/ui/compose/images/text/reveal-last-typed.gif)

## Additional resources

- [Auto-format a phone number in a text field](https://developer.android.com/develop/ui/compose/quick-guides/content/auto-format-phone-number)
- [Show or hide password based on a user toggle](https://developer.android.com/develop/ui/compose/quick-guides/content/show-hide-password)
- [Validate input as the user types](https://developer.android.com/develop/ui/compose/quick-guides/content/validate-input)

## Recommended for you

- [Architecting your Compose UI](https://developer.android.com/develop/ui/compose/architecture)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)