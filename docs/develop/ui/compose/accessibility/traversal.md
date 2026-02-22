---
title: https://developer.android.com/develop/ui/compose/accessibility/traversal
url: https://developer.android.com/develop/ui/compose/accessibility/traversal
source: md.txt
---

Traversal order is the order in which accessibility services navigate through
UI elements. In a Compose app, elements are arranged in expected reading order,
which is usually left-to-right, then top-to-bottom. However, there are some
scenarios where Compose might need additional hints to determine the correct
reading order.

[`isTraversalGroup`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).isTraversalGroup()) and [`traversalIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).traversalIndex()) are semantic properties that
let you influence the traversal order for accessibility services in scenarios
where Compose's default sorting algorithm is not sufficient. `isTraversalGroup`
identifies semantically important groups that need customization, while
`traversalIndex` adjusts the order of individual elements within those groups.
You can use `isTraversalGroup` alone to signify that all elements within a group
should be selected together, or with `traversalIndex` for further customization.

Use `isTraversalGroup` and `traversalIndex` in your
app to control screen reader traversal order.

## Group elements for traversal

`isTraversalGroup` is a boolean property that defines whether a [semantics](https://developer.android.com/develop/ui/compose/semantics)
node is a traversal group. This type of node is one whose function is to serve
as a boundary or border in organizing the node's children.

Setting `isTraversalGroup = true` on a node means that all children of that node
are visited before moving to other elements. You can set `isTraversalGroup` on
non-screen reader focusable nodes, such as columns, rows, or boxes.

The following example uses `isTraversalGroup`. It emits four text elements. The
left two elements belong to one `CardBox` element, while the right two elements
belong to another `CardBox` element:


```kotlin
// CardBox() function takes in top and bottom sample text.
@Composable
fun CardBox(
    topSampleText: String,
    bottomSampleText: String,
    modifier: Modifier = Modifier
) {
    Box(modifier) {
        Column {
            Text(topSampleText)
            Text(bottomSampleText)
        }
    }
}

@Composable
fun TraversalGroupDemo() {
    val topSampleText1 = "This sentence is in "
    val bottomSampleText1 = "the left column."
    val topSampleText2 = "This sentence is "
    val bottomSampleText2 = "on the right."
    Row {
        CardBox(
            topSampleText1,
            bottomSampleText1
        )
        CardBox(
            topSampleText2,
            bottomSampleText2
        )
    }
}
```

<br />

The code produces output similar to the following:
![Layout with two columns of text, with the left column reading 'This
sentence is in the left column' and the right column reading 'This sentence is on the right.'](https://developer.android.com/static/develop/ui/compose/images/a11y-istraversalgroup-example.png) **Figure 1.** A layout with two sentences (one in the left column and one in the right column).

Because no semantics have been set, the default behavior of the screen reader is
to traverse elements from left to right and top to bottom. Because of this
default, TalkBack reads out the sentence fragments in the wrong order:

"This sentence is in" → "This sentence is" → "the left column." → "on the
right."

To order the fragments correctly, modify the original snippet to set
`isTraversalGroup` to `true`:


```kotlin
@Composable
fun TraversalGroupDemo2() {
    val topSampleText1 = "This sentence is in "
    val bottomSampleText1 = "the left column."
    val topSampleText2 = "This sentence is"
    val bottomSampleText2 = "on the right."
    Row {
        CardBox(
//      1,
            topSampleText1,
            bottomSampleText1,
            Modifier.semantics { isTraversalGroup = true }
        )
        CardBox(
//      2,
            topSampleText2,
            bottomSampleText2,
            Modifier.semantics { isTraversalGroup = true }
        )
    }
}
```

<br />

Because `isTraversalGroup` is set specifically on each `CardBox`, the `CardBox`
boundaries apply when sorting their elements. In this case, the left
`CardBox` is read first, followed by the right `CardBox`.

Now, TalkBack reads out the sentence fragments in the correct order:

"This sentence is in" → "the left column." → "This sentence is" → "on the
right."

> [!NOTE]
> **Note:** `isTraversalGroup` is `true` by default on scroll containers (like `LazyColumn`) and Material surfaces. If needed, you can disable this default behavior with `Modifier.semantics { isTraversalGroup = false` }. Setting `isTraversalGroup` to `false` reinstates the default traversal order.

## Customize traversal order

[`traversalIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).traversalIndex()) is a float property that lets you customize TalkBack
traversal order. If grouping elements together is not enough for TalkBack to
work correctly, use `traversalIndex` in conjunction with
`isTraversalGroup` to further customize screen reader ordering.

The `traversalIndex` property has the following characteristics:

- Elements with lower `traversalIndex` values are prioritized first.
- Can be positive or negative.
- The default value is `0f`.
- In order for the traversal index to influence traversal behavior, it must be set on a component that will be selectable and focusable by accessibility services, such as on-screen elements like text or buttons.
  - Setting only `traversalIndex` on, for example, a `Column` would have no effect, unless the column has `isTraversalGroup` set on it as well.

The following example shows how you can use `traversalIndex` and
`isTraversalGroup` together.

A clock face is a common scenario where standard traversal ordering does not
work. The example in this section is a time picker, where a user can traverse
through the numbers on a clock face and select digits for the hour and minute
slots.
![A clock face with a time picker above it.](https://developer.android.com/static/develop/ui/compose/images/a11y-clock-face.png) **Figure 2.** An image of a clock face.

In the following simplified snippet, there is a `CircularLayout` in which 12
numbers are drawn, starting with 12 and moving clockwise around the circle:


```kotlin
@Composable
fun ClockFaceDemo() {
    CircularLayout {
        repeat(12) { hour ->
            ClockText(hour)
        }
    }
}

@Composable
private fun ClockText(value: Int) {
    Box(modifier = Modifier) {
        Text((if (value == 0) 12 else value).toString())
    }
}
```

<br />

Because the clock face is not read logically with the default left-to-right and
top-to-bottom ordering, TalkBack reads the numbers out of order. To rectify
this, use the incrementing counter value, as shown in the following snippet:


```kotlin
@Composable
fun ClockFaceDemo() {
    CircularLayout(Modifier.semantics { isTraversalGroup = true }) {
        repeat(12) { hour ->
            ClockText(hour)
        }
    }
}

@Composable
private fun ClockText(value: Int) {
    Box(modifier = Modifier.semantics { this.traversalIndex = value.toFloat() }) {
        Text((if (value == 0) 12 else value).toString())
    }
}
```

<br />

To properly set the traversal ordering, first make the `CircularLayout` a
traversal group and set `isTraversalGroup = true`. Then, as each clock text is
drawn onto the layout, set its corresponding `traversalIndex` to the counter
value.

Because the counter value continually increases, each clock value's
`traversalIndex` is larger as numbers are added to the screen---the clock value 0
has a `traversalIndex` of 0, and the clock value 1 has a `traversalIndex` of 1.
In this way, the order that TalkBack reads them in is set. Now, the numbers
inside the `CircularLayout` are read in the expected order.

Because the `traversalIndexes` that have been set are only relative to other
indexes within the same grouping, the rest of the screen ordering has been
preserved. In other words, the semantic changes shown in the preceding code
snippet only modify the ordering within the clock face that has
`isTraversalGroup = true` set.

Note that, without setting `CircularLayout's` semantics to `isTraversalGroup =
true`, the `traversalIndex` changes still apply. However, without the
`CircularLayout` to bind them, the twelve digits of the clock face are read
last, after all other elements on the screen have been visited. This occurs
because all other elements have a default `traversalIndex` of `0f`, and the
clock text elements are read after all other `0f` elements.

## API considerations

Consider the following when using the traversal APIs:

- `isTraversalGroup = true` should be set on the parent containing the grouped elements.
- `traversalIndex` should be set on a child component that contains semantics and will be selected by accessibility services.
- Ensure that all the elements you're investigating are at the same [`zIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary#(androidx.compose.ui.Modifier).zIndex(kotlin.Float)) level, as that also affects semantics and traversal order.
- Ensure that no semantics are unnecessarily merged, as this may affect which components traversal indices are applied to.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Accessibility in Compose](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).isTraversalGroup())
- \[Material Design 2 in Compose\]\[19\]
- [Testing your Compose layout](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/package-summary#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).traversalIndex())