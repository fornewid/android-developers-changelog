---
title: https://developer.android.com/develop/ui/compose/styles/examples
url: https://developer.android.com/develop/ui/compose/styles/examples
source: md.txt
---

The following documentation contains examples of using Styles to create certain
kinds of components.

> [!NOTE]
> **Note:** These examples don't pull values from themes, as they are merely illustrative of what Styles can do. When using them within your projects, extract out the common themeable colors, shapes, and typography styles into your theme class.

## Buttons

Styles can be used to create many different kinds of buttons that may be
different from standard Material components.

### Base button

Consider the following button defined as a base for different types of buttons:


```kotlin
@Composable
fun BaseButton(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    style: Style = Style,
    enabled: Boolean = true,
    interactionSource: MutableInteractionSource? = null,
    content: @Composable RowScope.() -> Unit
) {
    val effectiveInteractionSource = interactionSource ?: remember {
        MutableInteractionSource()
    }
    val styleState = remember(effectiveInteractionSource) {
        MutableStyleState(effectiveInteractionSource)
    }
    styleState.isEnabled = enabled
    Row(
        modifier = modifier
            .semantics(properties = {
                role = Role.Button
            })
            .clickable(
                enabled = enabled,
                onClick = onClick,
                interactionSource = effectiveInteractionSource,
                indication = null,
            )
            .styleable(styleState, baseButtonStyle, style),
        content = content,
        verticalAlignment = Alignment.CenterVertically
    )
}
```

<br />

### Hover background translation button

To define a button with a background that moves on hover, use the following
code:
**Figure 1.** Button with background that translates on hover.


```kotlin
@Preview
@Composable
fun HoverButtonExample() {
    Box(
        modifier = Modifier.padding(32.dp),
        contentAlignment = Alignment.Center
    ) {
        BaseButton(
            onClick = {},
            style = Style {
                background(Color.Transparent)
                shape(RoundedCornerShape(0.dp))
                border(1.dp, Color.Black)
                contentColor(Color.Black)
                fontSize(16.sp)
                fontWeight(FontWeight.Light)
                letterSpacing(1.sp)
                contentPadding(vertical = 13.dp, horizontal = 20.dp)
                dropShadow(
                    Shadow(
                        spread = 0.dp, color = Color(0xFFFFE54C),
                        radius = 0.dp,
                        offset = DpOffset(7.dp, 7.dp)
                    )
                )
                hovered {
                    animate(tween(200)) {
                        dropShadow(
                            Shadow(
                                spread = 0.dp, color = Color(0xFFFFE54C),
                                radius = 0.dp,
                                offset = DpOffset(0.dp, 0.dp)
                            )
                        )
                    }
                }
                pressed {
                    animate(tween(200)) {
                        dropShadow(
                            Shadow(
                                spread = 0.dp, color = Color(0xFFFFE54C),
                                radius = 0.dp,
                                offset = DpOffset(0.dp, 0.dp)
                            )
                        )
                    }
                }
            }
        ) {
            BaseText("Button 52")
        }
    }
}
```

<br />

### Rounded depth button with shadow animation

To create a button with a depth press effect that translates the shadow up and
down on `pressed`, the following is how it can be achieved:
**Figure 2.** Button with depth effect, translating the shadow layer on press.


```kotlin
@Preview
@Composable
fun ShadowAnimationButton() {
    Box(modifier = Modifier.padding(32.dp)) {
        val density = LocalDensity.current
        val buttonStyle = Style {
            background(Color(0xFFFBEED0))
            border(2.dp, Color(0xFF422800))
            shape(RoundedCornerShape(30.dp))
            dropShadow(
                Shadow(
                    color = Color(0xFF422800), offset = DpOffset(4.dp, 4.dp),
                    radius = 0.dp, spread = 0.dp
                )
            )
            contentColor(Color(0xFF422800))
            fontWeight(FontWeight.SemiBold)
            fontSize(18.sp)
            contentPaddingHorizontal(25.dp)
            externalPadding(8.dp)
            height(50.dp)
            textAlign(TextAlign.Center)
            hovered {
                animate {
                    background(Color.White)
                }
            }
            pressed {
                animate {
                    dropShadow(
                        Shadow(
                            color = Color(0xFF422800),
                            offset = DpOffset(2.dp, 2.dp),
                            radius = 0.dp,
                            spread = 0.dp
                        )
                    )
                    translation(with(density) { 2.dp.toPx() }, with(density) { 2.dp.toPx() })
                }
            }
        }
        BaseButton(
            onClick = {},
            style = buttonStyle
        ) {
            BaseText("Button 74")
        }
    }
}
```

<br />

### Multiple layered styles with pressed animation

The following code creates a button that has a depth pressed effect with Styles,
that has multiple layers of styles, that all use the same `StyleState`:
**Figure 3.** Button with depth pressed effect and multiple style layers.


```kotlin
@Preview
@Composable
fun MultipleStylesButton() {
    val interactionSource = remember { MutableInteractionSource() }
    val styleState = remember(interactionSource) { MutableStyleState(interactionSource) }
    val density = LocalDensity.current

    Box(
        modifier = Modifier
            .styleable(styleState) {
                size(200.dp, 48.dp)
                externalPadding(32.dp)
            }
            .clickable(interactionSource, indication = null) {},
        contentAlignment = Alignment.Center
    ) {
        val edgeStyle = Style {
            fillSize()
            shape(RoundedCornerShape(16.dp))
            background(Color(0xFF1CB0F6))
        }

        val frontStyle = Style {
            fillSize()
            background(Color(0xFF1899D6))
            shape(RoundedCornerShape(16.dp))
            contentPadding(vertical = 12.dp, horizontal = 16.dp)
            translationY(with(density) { (-4).dp.toPx() })
            pressed {
                animate {
                    translationY(with(density) { (0).dp.toPx() })
                }
            }
        }
        Box(modifier = Modifier.semantics(properties = {
            role = Role.Button
        }).styleable(styleState, edgeStyle)) {
            Box(
                modifier = Modifier
                    .styleable(styleState, frontStyle),
                contentAlignment = Alignment.Center
            ) {
                BaseText(
                    "Button 19".toUpperCase(Locale.current),
                    style = Style {
                        contentColor(Color.White)
                        fontSize(15.sp)
                        fontWeight(FontWeight.Bold)
                        letterSpacing(0.8.sp)
                    }
                )
            }
        }
    }
}
```

<br />

### Gradient glow effect button

To achieve a gradient glow effect that infinitely animates, you can use Styles
in combination with `rememberInfiniteTransition`, as follows:

> [!NOTE]
> **Note:** Infinite animations are not supported by the Styles API. This example uses a combination of `rememberInfiniteTransition` and Styles.

**Figure 4.** Gradient glow effect button.


```kotlin
@Preview
@Composable
fun GradientGlowButtonExample() {
    val infiniteTransition = rememberInfiniteTransition(label = "glowing_button_85_animation")
    val animatedProgress by infiniteTransition.animateFloat(
        initialValue = 0f,
        targetValue = 1f,
        animationSpec = infiniteRepeatable(
            animation = tween(durationMillis = 20000, easing = LinearEasing),
        ), label = "progress"
    )

    val gradientColors = listOf(
        Color(0xffff0000), Color(0xffff7300), Color(0xfffffb00), Color(0xff48ff00),
        Color(0xff00ffd5), Color(0xff002bff), Color(0xff7a00ff), Color(0xffff00c8),
        Color(0xffff0000)
    )

    val glowingBrush = remember(animatedProgress) {
        object : ShaderBrush() {
            override fun createShader(size: Size): Shader {
                val width = size.width * 4
                val brushSize = width * animatedProgress
                return LinearGradientShader(
                    colors = gradientColors,
                    from = Offset(brushSize, 0f),
                    to = Offset(brushSize + width, 0f),
                    tileMode = TileMode.Repeated
                )
            }
        }
    }


    Box(
        modifier = Modifier
            .padding(32.dp),
        contentAlignment = Alignment.Center
    ) {
        BaseButton(
            onClick = { },
            style = Style {
                dropShadow(
                    Shadow(
                        brush = glowingBrush,
                        radius = 5.dp
                    )
                )
                transformOrigin(TransformOrigin.Center)
                pressed {
                    animate {
                        dropShadow(
                            Shadow(
                                brush = glowingBrush,
                                radius = 10.dp
                            )
                        )
                        scale(0.95f)
                    }

                }
                size(width = 200.dp, height = 50.dp)
                background(Color(0xFF111111))
                shape(RoundedCornerShape(10.dp))
                contentColor(Color.White)
                contentPadding(vertical = (0.6f * 14).dp, horizontal = (2f * 14).dp)
                border(width = 0.dp, color = Color.Transparent)
            }
        ) {
            BaseText(text = "Button 85")
        }
    }
}
```

<br />