---
title: https://developer.android.com/develop/ui/compose/text/rich-text-input
url: https://developer.android.com/develop/ui/compose/text/rich-text-input
source: md.txt
---

> [!NOTE]
> **Note:** The APIs discussed on this page are available starting in Compose Foundation `1.12.0` and Material 3 `1.5.0-alpha28`. Styles are saved and restored across configuration changes and process death starting in Compose Foundation `1.13.0-alpha01`.

Rich text input lets users format what they type, including bolding a word,
adding a heading, aligning a paragraph, or inserting a highlighted `@mention`.
In Compose, you build this on top of state-based text fields
([`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicTextField.composable#BasicTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.input.TextFieldDecorator,androidx.compose.foundation.ScrollState)) and [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable#TextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.ScrollState,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource))). Styles live in
[`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState) alongside the text, so they survive edits, selection
changes, and recompositions, and stay in sync as the user types, deletes, and
pastes.

This page shows how to apply, update, query, extract, and remove styles in a
`TextFieldState` using [`TextFieldBuffer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer), and how to drive a formatting
toolbar from [`TextFieldState.textStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#textStyles()).

> [!NOTE]
> **Note:** To apply visual-only formatting that isn't saved in `TextFieldState`, such as syntax highlighting or phone number formatting, call [`addStyle`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#addStyle(androidx.compose.ui.text.SpanStyle,androidx.compose.ui.text.TextRange,androidx.compose.foundation.text.input.ExpandPolicy)) inside an [`OutputTransformation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/OutputTransformation). Rich text styling in [`TextFieldState.edit`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#edit(kotlin.Function1)) and [`InputTransformation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/InputTransformation) is enabled by default in Compose Foundation `1.12.0` through [`ComposeFoundationFlags.isBasicTextFieldStyledTextEnabled`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/ComposeFoundationFlags#isBasicTextFieldStyledTextEnabled()). For more information on visual-only formatting, see [Format input before it's displayed](https://developer.android.com/develop/ui/compose/text/user-input?textfield=state-based#format-input-display).

## Apply inline and paragraph styles

You can apply character-level and paragraph-level formatting inside any
`TextFieldBuffer` receiver scope, including `TextFieldState.edit`,
[`InputTransformation.transformInput`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/InputTransformation#(androidx.compose.foundation.text.input.TextFieldBuffer).transformInput()), and
[`OutputTransformation.transformOutput`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/OutputTransformation#(androidx.compose.foundation.text.input.TextFieldBuffer).transformOutput()).

### Control boundary expansion with `ExpandPolicy`

When you call `addStyle`, you can pass an [`ExpandPolicy`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/ExpandPolicy) to define how the
styled range behaves when the user inserts new characters directly at its
`start` or `end` boundary:

- **Insertion inside `(start, end)`**: Always expands the styled range.
- **Insertion before `start`** : Always shifts both `start` and `end` offsets to the right.
- **Insertion directly at `start` or `end`** : Controlled by the `ExpandPolicy` you specify.

The following table describes the available `ExpandPolicy` options and their
typical use cases:

| **Policy** | **Boundary behavior** | **Recommended use cases** | **Example** |
|---|---|---|---|
| **`ExpandPolicy.InsideOnly`** | Text typed at `start` or `end` stays outside the styled range. | Discrete tokens such as `@mentions`, `#hashtags`, or background pills where typing next to the tag shouldn't inherit the tag's background color. | ![Animation showing text typed at the start or end of an ExpandPolicy.InsideOnly range remaining unstyled.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-expand-policy-inside-only.gif) |
| **`ExpandPolicy.AtStart`** | Text typed at `start` inherits the style, and text typed at `end` stays unstyled. | Text typed directly in front of the styled text should also adopt the same formatting. | ![Animation showing text typed at the start of an ExpandPolicy.AtStart range inheriting the style while text typed at the end remains unstyled.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-expand-policy-at-start.gif) |
| **`ExpandPolicy.AtEnd`** | Text typed at `end` inherits the style, and text typed at `start` stays unstyled. | Standard rich text editor typing, where continuing to type after a bold or italic word continues that formatting. | ![Animation showing text typed at the end of an ExpandPolicy.AtEnd range inheriting the style while text typed at the start remains unstyled.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-expand-policy-at-end.gif) |
| **`ExpandPolicy.AtBoth`** | Text typed at either `start` or `end` expands the range and inherits the style. | Active highlights or continuous formatted blocks that should grow from either edge. | ![Animation showing text typed at either the start or end of an ExpandPolicy.AtBoth range inheriting the style.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-expand-policy-at-both.gif) |

### Apply character formatting with `SpanStyle`

Use `addStyle` with a [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle) to apply character-level formatting,
such as text color, background highlight, [`FontWeight`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight), [`FontStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontStyle),
or underline to a specific [`TextRange`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextRange) in the buffer.

#### Key behaviors for `SpanStyle` ranges

- **Layering order** : Styles apply in the order you add them to the buffer. If multiple overlapping `SpanStyle` ranges set the same property with different values, the style added later renders on top.
- **Non-empty range requirement** : You must pass a non-collapsed range where `start` \< `end`. Calling `addStyle` on a collapsed selection of length `0` has no effect, and passing reversed or out-of-bounds indexes throws an `IllegalArgumentException`.

> [!NOTE]
> **Note:** Because `addStyle` has no effect on a collapsed selection, pressing a Bold button with only a cursor can't style anything yet. To make the next typed characters bold, track a pending `SpanStyle` in your state holder and apply it to each new range in [`changes`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#changes()) inside an `InputTransformation`, as shown in the following example.


```kotlin
TextField(
    state = rememberTextFieldState(),
    inputTransformation = InputTransformation {
        for (i in 0 until changes.changeCount) {
            val range = changes.getRange(i)
            if (!range.collapsed) {
                addStyle(
                    spanStyle = SpanStyle(
                        fontWeight = FontWeight.ExtraBold,
                        fontStyle = FontStyle.Italic,
                        color = Color.Red,
                    ),
                    range = range,
                    expandPolicy = ExpandPolicy.AtEnd
                )
            }
        }
    }
)
```

<br />

![A TextField dynamically applying bold and italic red formatting as the user types.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-character-styling.gif) **Figure 1.** Applying bold and italic red formatting to the user input dynamically.

### Apply block formatting with `ParagraphStyle`

Use [`addStyle`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#addStyle(androidx.compose.ui.text.ParagraphStyle,androidx.compose.ui.text.TextRange,androidx.compose.foundation.text.input.ExpandPolicy)) with a [`ParagraphStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle) to apply block-level
structural formatting such as [`textAlign`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle#textAlign()), [`lineHeight`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle#lineHeight()),
[`textDirection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle#textDirection()), or [`textIndent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle#textIndent()) to a paragraph range.


```kotlin
fun setParagraphAlignment(state: TextFieldState, alignment: TextAlign) {
    val targetRange = if (state.selection.collapsed) {
        TextRange(0, state.text.length)
    } else {
        state.selection
    }
    if (targetRange.collapsed) return
    state.edit {
        // 1. Remove existing paragraph styles in this range
        getParagraphStyles(targetRange).forEach { removeStyle(it) }
        // 2. Apply the new paragraph alignment
        addStyle(
            paragraphStyle = ParagraphStyle(textAlign = alignment),
            range = targetRange,
            expandPolicy = ExpandPolicy.InsideOnly
        )
    }
}
```

<br />

![A TextField toggling paragraph alignment between start, center, and end using ParagraphStyle.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-paragraph-alignment.gif) **Figure 2.** Toggling paragraph alignment between start, center, and end using `ParagraphStyle`.

> [!CAUTION]
> **Caution:** `ParagraphStyle` ranges in Compose must be strictly non-overlapping or completely nested. Partial overlaps such as `[0, 10)` and `[5, 15)` are invalid and cause layout measurement to throw an `IllegalArgumentException`. Always remove or adjust existing `ParagraphStyle` ranges before applying a new one to the same paragraph.

#### Pitfalls to avoid with `ParagraphStyle`

Because `ParagraphStyle` applies to entire blocks of text, avoid using it in the
following scenarios:

- **Expanding into adjacent paragraphs** : Set `ExpandPolicy` carefully so adjacent `ParagraphStyle` ranges don't overlap after user edits. For example, if `[0, 5)` uses `ExpandPolicy.AtEnd` and `[5, 10)` uses `ExpandPolicy.AtStart`, inserting text at index `5` expands both styles into an overlap and throws an `IllegalArgumentException`.
- **Nesting `ParagraphStyle` ranges** : Although completely nested ranges (such as `[0, 10)` and `[2, 8)`) are valid in `AnnotatedString`, avoid nesting `ParagraphStyle` ranges in a text field. Layout splits nested ranges into separate paragraphs and subsequent edits can inadvertently turn nested ranges into a partial overlap.

> [!NOTE]
> **Note:** In Compose `1.12.0`, `ParagraphStyle` boundaries act as paragraph breaks (matching static `AnnotatedString` behavior in `Text`). Applying a `ParagraphStyle` to a subrange of a paragraph or directly adjacent to a newline character (`\n`) can insert an extra visual line break. When styling multi-paragraph text, align your `ParagraphStyle` range with the full paragraph boundaries.

## Update a style in place with `TrackedRange`

Calling `addStyle` with a `TextRange` and `ExpandPolicy` returns a
[`TrackedRange`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TrackedRange) handle, which can be `TrackedRange<SpanStyle>` or
`TrackedRange<ParagraphStyle>`. A `TrackedRange` is a dynamic reference to a
style interval in the `TextFieldBuffer` that automatically updates its `start`
and `end` character offsets as text is inserted, deleted, or replaced around it.

### In-place mutability

You don't need to call `removeStyle` and `addStyle` to update an existing style
or adjust its boundaries. Inside a `TextFieldBuffer` scope, `TrackedRange`
provides extension properties that update the interval in place while preserving
its original layering order relative to other styles:

- `TrackedRange<SpanStyle>.spanStyle`: Reads or replaces the `SpanStyle` payload in place on a `TrackedRange<SpanStyle>`.
- `TrackedRange<ParagraphStyle>.paragraphStyle`: Reads or replaces the `ParagraphStyle` payload in place on a `TrackedRange<ParagraphStyle>`.
- `TrackedRange<*>.textRange`: Reads or updates the current `TextRange` bounds in place. Setting a collapsed, reversed, or out-of-bounds range throws an `IllegalArgumentException`.
- `TrackedRange<*>.expandPolicy`: Reads or updates the `ExpandPolicy` in place.
- `TrackedRange<*>.isValid`: Returns `true` if the style interval is still active in the buffer, or `false` if edits caused its length to collapse to `0` or if it was removed.


```kotlin
// Trim an existing bold span in place when the selection overlaps one edge
val range = style.textRange
if (range.start < selection.min && range.end <= selection.max) {
    // Selection covers the end of the span - shrink end boundary in place
    style.textRange = TextRange(range.start, selection.min)
} else if (range.start >= selection.min && range.end > selection.max) {
    // Selection covers the start of the span - shrink start boundary in place
    style.textRange = TextRange(selection.max, range.end)
}
```

<br />

### Scope confinement and lifecycle rules

Keep the following scope and lifecycle rules in mind when working with
`TrackedRange` instances:

- **Confined to `TextFieldBuffer`** : `TrackedRange` extension properties only exist within the `TextFieldBuffer` scope where the handle was created or queried.
- **Automatic pruning on collapse** : If user edits delete all characters covered by a `TrackedRange`, its length shrinks to `0`, `isValid` returns `false`, and the style is removed from the buffer.

> [!CAUTION]
> **Caution:** Don't store `TrackedRange` instances in long-lived `ViewModel` properties or external state holders. A `TrackedRange` is bound to a single `TextFieldBuffer` edit session, has no accessible properties outside that block, and becomes permanently invalid if the range is deleted, undone, or restored. To observe styles outside an edit block, read [`TextFieldState.textStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#textStyles()) instead.

## Query and remove styles

Compose provides two ways to inspect active styles, depending on whether you are
mutating the buffer or reading state for your UI:

- **Inside a `TextFieldBuffer` block** : Call [`getSpanStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#getSpanStyles(androidx.compose.ui.text.TextRange)) and [`getParagraphStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#getParagraphStyles(androidx.compose.ui.text.TextRange)) directly on the `TextFieldBuffer` receiver to obtain mutable `TrackedRange` handles.
- **Outside an edit block** : Read [`TextFieldState.textStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#textStyles()), which returns immutable `AnnotatedString.Range` lists that reflect the committed state.

> [!CAUTION]
> **Caution:** Don't query `state.textStyles` inside a `state.edit` block. `state.textStyles` only reflects the committed state prior to the edit session and doesn't include ongoing buffer changes.

### Query intersecting styles in `TextFieldBuffer`

[`TextFieldBuffer.getSpanStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#getSpanStyles(androidx.compose.ui.text.TextRange)) and
[`TextFieldBuffer.getParagraphStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#getParagraphStyles(androidx.compose.ui.text.TextRange)) return all `TrackedRange` instances
that intersect with the given `TextRange`, ordered by when they were added to
the buffer.

For example, you can query `getSpanStyles(selection)` inside `state.edit` to
inspect or update styles covering the user's current selection:


```kotlin
state.edit {
    if (selection.collapsed) return@edit
    // Query all bold spans that overlap with the current selection
    val boldStyles: List<TrackedRange<SpanStyle>> = getSpanStyles(selection).filter {
        it.spanStyle.fontWeight == FontWeight.Bold
    }
    // ...
}
```

<br />

Style intervals use a semi-open mathematical range **`[start, end)`**. Whether a
touching style is returned depends on whether you query a selection or a single
cursor point:

- **For a non-empty selection `[start, end)`** :
  - **Returned** : Any style that overlaps, contains, or sits inside the selection range. For example, query `[5, 15)` matches `[0, 20)`, `[8, 12)`, or `[0, 10)`.
  - **Not returned** : Styles that only touch the outer boundary edges without overlapping characters. For example, query `[5, 15)` excludes `[0, 5)` and `[15, 25)`.
- **For a collapsed cursor `[index, index]`** :
  - **Returned** : Any style containing the cursor or starting at the cursor position. For example, a cursor at `10` matches `[0, 20)` and `[10, 20)`.
  - **Not returned (touching end rule)** : Any style ending at the cursor position. For example, a cursor at `10` excludes `[0, 10)`.

> [!NOTE]
> **Note:** `getSpanStyles` and `getParagraphStyles` evaluate semi-open interval bounds `[start, end)` and ignore `ExpandPolicy`. To inspect a style touching the end boundary at a collapsed cursor (`index > 0`), query the preceding character window instead. Because `TextRange` counts UTF-16 code units and a single emoji can span several of them, compute the window start with [`BreakIterator.getCharacterInstance()`](https://developer.android.com/reference/java/text/BreakIterator#getCharacterInstance()) rather than `index - 1` so the query never starts in the middle of a character.

### Remove or toggle styles with `removeStyle`

Pass a `TrackedRange` handle to [`removeStyle`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer#removeStyle(androidx.compose.foundation.text.input.TrackedRange)) to delete that specific
style interval from the `TextFieldBuffer`.

`removeStyle` returns `true` if the `TrackedRange` was found and removed, or
`false` if it was already removed or belonged to a different buffer. It removes
only the targeted `TrackedRange` handle, leaving other overlapping styles
intact.


```kotlin
fun toggleBold(state: TextFieldState) {
    state.edit {
        if (selection.collapsed) return@edit
        // Query all bold spans that overlap with the current selection
        val boldStyles: List<TrackedRange<SpanStyle>> = getSpanStyles(selection).filter {
            it.spanStyle.fontWeight == FontWeight.Bold
        }
        if (boldStyles.isNotEmpty()) {
            // Remove or trim existing bold spans covering the selection
            for (style in boldStyles) {
                val range = style.textRange
                if (range.start >= selection.min && range.end <= selection.max) {
                    removeStyle(style)
                } else if (range.start < selection.min && range.end > selection.max) {
                    val oldEnd = range.end
                    style.textRange = TextRange(range.start, selection.min)
                    addStyle(
                        spanStyle = SpanStyle(fontWeight = FontWeight.Bold),
                        range = TextRange(selection.max, oldEnd),
                        expandPolicy = ExpandPolicy.AtEnd
                    )
                } else if (range.start < selection.min) {
                    style.textRange = TextRange(range.start, selection.min)
                } else {
                    style.textRange = TextRange(selection.max, range.end)
                }
            }
        } else {
            // No bold spans intersect the selection - apply bold
            addStyle(
                spanStyle = SpanStyle(fontWeight = FontWeight.Bold),
                range = selection,
                expandPolicy = ExpandPolicy.AtEnd
            )
        }
    }
}
```

<br />

![A TextField toggling bold formatting on and off for selected words.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-toggle-bold.gif) **Figure 3.** Toggling between bolding and unbolding of text.

## Extract or serialize rich text

To display formatted input in a read-only `Text` composable, or serialize it to
a backend service, read [`TextFieldState.textStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState#textStyles()) outside an edit block.

[`state.textStyles.getSpanStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldTextStyles#getSpanStyles(androidx.compose.ui.text.TextRange)) and
[`state.textStyles.getParagraphStyles`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldTextStyles#getParagraphStyles(androidx.compose.ui.text.TextRange)) return
`List<AnnotatedString.Range<SpanStyle>>` and
`List<AnnotatedString.Range<ParagraphStyle>>`, which you can pass directly to
the [`AnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString) constructor:


```kotlin
fun TextFieldState.toAnnotatedString(): AnnotatedString {
    val fullRange = TextRange(0, text.length)
    return AnnotatedString(
        text = text.toString(),
        spanStyles = textStyles.getSpanStyles(fullRange),
        paragraphStyles = textStyles.getParagraphStyles(fullRange)
    )
}
```

<br />

## Complete example in Jetchat

To see a complete implementation that combines inline character styling (bold,
italic, underline, strikethrough, and color), see the [Jetchat](https://github.com/android/compose-samples/tree/main/Jetchat) sample on
GitHub:

- [`RichTextState.kt`](https://github.com/android/compose-samples/blob/main/Jetchat/app/src/main/java/com/example/compose/jetchat/conversation/RichTextState.kt): Encapsulates `TextFieldState` style queries, span toggling, trimming or splitting across selection bounds, and more.
- [`UserInput.kt`](https://github.com/android/compose-samples/blob/main/Jetchat/app/src/main/java/com/example/compose/jetchat/conversation/UserInput.kt#L511): Connects `RichTextState` to the rich text formatting toolbar and message input field.

![The Jetchat sample app demonstrating rich text formatting in the message input bar.](https://developer.android.com/static/develop/ui/compose/images/text/richtext/rich-text-jetchat.gif) **Figure 4.** Rich text editing in Jetchat.