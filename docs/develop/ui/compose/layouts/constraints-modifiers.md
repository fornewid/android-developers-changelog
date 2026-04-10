---
title: https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers
url: https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers
source: md.txt
---

[Video](https://www.youtube.com/watch?v=OeC5jMV342A)

In Compose, you can chain multiple modifiers together to change the look and
feel of a composable. These modifier chains can affect the *constraints* passed
to composables, which define width and height bounds.

This page describes how chained modifiers affect constraints and, in turn, the
measurement and placement of composables.

## Modifiers in the UI tree

To understand how modifiers influence each other, it's helpful to visualize how
they appear in the UI tree, which is generated during the composition phase. For
more information, see the [Composition](https://developer.android.com/develop/ui/compose/phases#composition) section.

In the UI tree, you can visualize modifiers as wrapper nodes for the layout
nodes:
![Code for composables and modifiers, and their visual representation as a UI tree.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/modifier-wrapping.png) **Figure 1.** Modifiers wrapping layout nodes in the UI tree.

Adding more than one modifier to a composable creates a chain of modifiers. When
you chain multiple modifiers, each modifier node *wraps the rest of the chain
and the layout node within* . For example, when you chain a [`clip`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).clip(androidx.compose.ui.graphics.Shape)) and a
[`size`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).size(androidx.compose.ui.unit.Dp)) modifier, the `clip` modifier node wraps the `size` modifier node,
which then wraps the `Image` layout node.

In the layout phase, the [algorithm that walks the tree](https://developer.android.com/develop/ui/compose/phases#layout) stays the same, but
each modifier node is visited as well. This way, a modifier can change the size
requirements and placement of the modifier or layout node that it wraps.

As shown in Figure 2, the implementation of the `Image` and `Text` composables
themselves consists of a chain of modifiers wrapping a single layout node.

The implementations of `Row` and `Column` are layout nodes that describe how
to lay out their children.
![The tree structure from before, but now each node is just a simple layout, with a lot of modifier wrapping nodes around it.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/composables-modifiers.png) **Figure 2.** The same tree structure as in Figure 1, but with composables in the UI tree visualized as chains of modifiers.

To summarize:

- Modifiers wrap a single modifier or layout node.
- Layout nodes can lay out multiple child nodes.

The following sections describe how to use this mental model to reason about
modifier chaining and how it influences the size of composables.

## Constraints in the layout phase

[The layout phase](https://developer.android.com/develop/ui/compose/phases#layout) follows a three-step algorithm to find each layout
node's width, height, and x, y coordinate:

1. **Measure children**: A node measures its children, if any.
2. **Decide own size**: Based on those measurements, a node decides on its own size.
3. **Place children**: Each child node is placed relative to a node's own position.

[`Constraints`](https://developer.android.com/reference/kotlin/androidx/compose/ui/unit/Constraints) help find the right sizes for the nodes during the first two
steps of the algorithm. Constraints define the minimum and maximum bounds for a
node's width and height. When the node decides on its size, its measured size
should fall within this size range.

### Types of constraints

A constraint can be one of the following:

- **Bounded**: The node has a maximum and minimum width and height.

![Bounded constraints of different sizes within a container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/bounded-constraints.png) **Figure 3.** Bounded constraints.

- **Unbounded**: The node is not constrained to any size. The maximum width and height bounds are set to infinity.

![Unbounded constraints that have the width and height set to infinity. The constraints extend beyond the container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/unbounded-constraints.png) **Figure 4.** Unbounded constraints.

- **Exact**: The node is asked to follow an exact size requirement. The minimum and maximum bounds are set to the same value.

![Exact constraints that conform to an exact size requirement within the container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/exact-constraints.png) **Figure 5.** Exact constraints.

- **Combination**: The node follows a combination of the preceding constraint types. For example, a constraint could bound the width while allowing for an unbounded maximum height, or set an exact width but provide a bounded height.

![Two containers that show combinations of bounded and unbounded constraints and exact widths and heights.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/combination-constraints.png) **Figure 6.** Combinations of bounded and unbounded constraints and exact widths and heights.

The next section describes how these constraints are passed from a parent to a
child.

### How constraints are passed from parent to child

During the first step of the algorithm described in [Constraints in the layout
phase](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers#constraints-layout), constraints are passed down from parent to child
in the UI tree.

When a parent node measures its children, it provides these constraints to each
child to let them know how big or small they're allowed to be. Then, when it
decides its own size, it also adheres to the constraints that were passed in by
its own parents.

At a high level, the algorithm works in the following way:

1. To decide the size it actually wants to occupy, the root node in the UI tree measures its children and forwards the same constraints to its first child.
2. If the child is a modifier that does not impact measurement, it forwards the constraints to the next modifier. The constraints are passed down the modifier chain as-is unless a modifier that impacts measurement is reached. The constraints are then re-sized accordingly.
3. Once a node is reached that doesn't have any children (referred to as a "leaf node"), it decides its size based on the constraints that were passed in, and returns this resolved size to its parent.
4. The parent adapts its constraints based on this child's measurements, and calls its next child with these adjusted constraints.
5. Once all children of a parent are measured, the parent node decides on its own size and communicates that to its own parent.
6. This way, the whole tree is traversed depth-first. Eventually, all the nodes have decided on their sizes, and the measurement step is completed.

For an in-depth example, see the [Constraints and modifier order](https://www.youtube.com/watch?v=OeC5jMV342A&t=204s)
video.

## Modifiers that affect constraints

You learned in the previous section that some modifiers can affect constraint
size. The following sections describe specific modifiers that impact
constraints.

### The `size` modifier

The [`size`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).size(androidx.compose.ui.unit.Dp)) modifier declares the preferred size of the content.

For example, the following UI tree should be rendered in a container of `300dp`
by `200dp`. The constraints are bounded, allowing widths between `100dp` and
`300dp`, and heights between `100dp` and `200dp`:
![A portion of a UI tree with the size modifier wrapping a layout node, and the
representation of the bounded constraints set by the size modifier in a container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/size-modifier.png) **Figure 7.** Bounded constraints in the UI tree and its representation in a container.

The `size` modifier adapts incoming constraints to match the value passed to it.
In this example, the value is `150dp`:
![The same as Figure 7, except with the size modifier adapting incoming constraints to match the value passed to it.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/size-modifier-2.png) **Figure 8.** The `size` modifier adjusting constraints to `150dp`.

If the width and height are smaller than the smallest constraint bound, or
larger than the largest constraint bound, the modifier matches the passed
constraints as closely as it can while still adhering to the constraints passed
in:
![Two UI trees and their corresponding representations in containers. In the first, the
size modifier accepts the incmoing constraints; in the second, the size modifier adapts to the
too-large constraints as closely as possible, resulting in constraints that fill the container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/size-modifier-3.png) **Figure 9.** The `size` modifier adhering to the passed constraint as closely as possible.

Note that chaining multiple `size` modifiers does not work. The first `size`
modifier sets both the minimum and maximum constraints to a fixed value. Even if
the second size modifier requests a smaller or larger size, it still needs to
adhere to the exact bounds passed in, so it won't override those values:
![A chain of two size modifiers in the UI tree and its representation in a container,
which is the result of the first value passed in and not the second value.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/size-modifier-4.png) **Figure 10.** A chain of two `size` modifiers, in which the second value passed in (`50dp`) does not override the first value (`100dp`).

### The `requiredSize` modifier

Use the [`requiredSize`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).requiredSize(androidx.compose.ui.unit.Dp)) modifier instead of [`size`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).size(androidx.compose.ui.unit.Dp)) if you need your
node to override the incoming constraints. The `requiredSize` modifier replaces
the incoming constraints and passes the size you specify as exact bounds.

When the size is passed back up the tree, the child node will be centered in the
available space:
![The size and requiredSize modifier chained in a UI tree, and the corresponding
representation in a container. The requiredSize modifier constraints override the size modifier
constraints.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/requiredsize-modifier.png) **Figure 11.** The `requiredSize` modifier overriding incoming constraints from the `size` modifier.

### The `width` and `height` modifiers

The `size` modifier adapts both the width and height of the constraints. With
the `width` modifier, you can set a fixed width but leave the height undecided.
Similarly, with the `height` modifier, you can set a fixed height, but leave the
width undecided:
![Two UI trees, one with the width modifier and its container representation and the other
with the height modifier and its representation.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/width-height-modifier.png) **Figure 12.** The `width` modifier and `height` modifier setting a fixed width and height, respectively.

### The `sizeIn` modifier

The `sizeIn` modifier lets you set exact minimum and maximum constraints
for width and height. Use the `sizeIn` modifier if you need fine-grained control
over the constraints.
![A UI tree with the sizeIn modifier with minimum and maximum widths and heights set,
and its representation within a container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/sizein-modifier.png) **Figure 13.** The `sizeIn` modifier with `minWidth`, `maxWidth`, `minHeight`, and `maxHeight` set.

## Examples

This section shows and explains the output from several code snippets with
chained modifiers.


```kotlin
Image(
    painterResource(R.drawable.hero),
    contentDescription = null,
    Modifier
        .fillMaxSize()
        .size(50.dp)
)
```

<br />

This snippet produces the following output:
![A blue square that fills its parent container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/example-1.png) **Figure 14.** The `Image` fills the maximum size as a result of the modifier chain.

- The [`fillMaxSize`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fillMaxSize(kotlin.Float)) modifier changes the constraints to set both the minimum width and height to the maximum value --- `300dp` in width and `200dp` in height.
- Even though the `size` modifier wants to use a size of `50dp`, it still needs to adhere to the incoming minimum constraints. So the `size` modifier will also output the exact constraint bounds of `300` by `200`, effectively ignoring the value provided in the `size` modifier.
- The `Image` follows these bounds and reports a size of `300` by `200`, which is passed all the way up the tree.


```kotlin
Image(
    painterResource(R.drawable.hero),
    contentDescription = null,
    Modifier
        .fillMaxSize()
        .wrapContentSize()
        .size(50.dp)
)
```

<br />

This snippet produces the following output:
![A small blue square centered within its parent container.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/example-2.png) **Figure 15.** The `Image` is centered and sized to `50dp`.

- The `fillMaxSize` modifier adapts the constraints to set both the minimum width and height to the maximum value --- `300dp` in width, and `200dp` in height.
- The `wrapContentSize` modifier resets the minimum constraints. So, while `fillMaxSize` resulted in fixed constraints, `wrapContentSize` *resets it back
  to bounded constraints*. The following node can now take up the whole space again, or be smaller than the entire space.
- The `size` modifier sets the constraints to minimum and maximum bounds of `50`.
- The `Image` resolves to a size of `50` by `50`, and the `size` modifier forwards that.
- The [`wrapContentSize`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).wrapContentSize(androidx.compose.ui.Alignment,kotlin.Boolean)) modifier has a special property. It takes its child and *puts it in the center of the available minimum bounds* that were passed to it. The size it communicates to its parents is thus equal to the minimum bounds that were passed into it.

By combining just three modifiers, you can define a size for the composable and
center it in its parent.


```kotlin
Image(
    painterResource(R.drawable.hero),
    contentDescription = null,
    Modifier
        .clip(CircleShape)
        .padding(10.dp)
        .size(100.dp)
)
```

<br />

This snippet produces the following output:
![A circular shape that is incorrectly clipped because of
modifier order.](https://developer.android.com/static/develop/ui/compose/images/layouts/constraints-modifiers/example-3.png) **Figure 16.** An incorrectly clipped shape due to modifier order.

- The `clip` modifier does not change the constraints.
- The `padding` modifier lowers the maximum constraints.
- The `size` modifier sets all constraints to `100dp`.
- The `Image` adheres to those constraints and reports a size of `100dp` by `100dp`.
- The `padding` modifier adds `10dp` on all sides to the size reported by the `Image`, so the layout with padding reports a width and height of `120dp`.
- Now, in the drawing phase, the `clip` modifier acts on a canvas of `120dp` by `120dp`. It creates a circle mask of that size.
- The `padding` modifier then insets its content by `10dp` on all sides, which lowers the canvas size for the `Image` to `100dp` by `100dp`.
- The `Image` is drawn in that smaller canvas. The image is clipped based on the original circle of `120dp`, so the output is a non-round result.