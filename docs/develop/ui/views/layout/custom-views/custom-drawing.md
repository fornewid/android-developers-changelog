---
title: Create a custom drawing  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/layout/custom-views/custom-drawing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create a custom drawing Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.

[Canvas in Compose →](https://developer.android.com/jetpack/compose/graphics/draw/overview)

![](/static/images/android-compose-ui-logo.png)

The most important part of a custom view is its appearance. Custom drawing
can be easy or complex according to your application's needs. This document
covers some of the most common operations.

For more information, see
[Drawables overview](/guide/topics/graphics/2d-graphics).

## Override onDraw()

The most important step in drawing a custom view is to override the
`onDraw()`
method. The parameter to `onDraw()` is a
`Canvas`
object that the view can use to draw itself. The `Canvas` class
defines methods for drawing text, lines, bitmaps, and many other graphics
primitives. You can use these methods in `onDraw()` to create your
custom user interface (UI).

Start by creating a
`Paint` object.
The next section discusses `Paint` in more detail.

## Create drawing objects

The
`android.graphics`
framework divides drawing into two areas:

* *What* to draw, handled by `Canvas`.
* *How* to draw, handled by `Paint`.

For example, `Canvas` provides a method to draw a line, and
`Paint` provides methods to define that line's color.
`Canvas` has a method to draw a rectangle, and `Paint`
defines whether to fill that rectangle with a color or leave it empty.
`Canvas` defines shapes that you can draw on the screen, and
`Paint` defines the color, style, font, and so forth of each shape
you draw.

Before you draw anything, create one or more `Paint` objects. The
following example does this in a method called `init`. This method is
called from the constructor from Java, but it can be initialized inline in
Kotlin.

### Kotlin

```
@ColorInt
private var textColor    // Obtained from style attributes.

@Dimension
private var textHeight   // Obtained from style attributes.

private val textPaint = Paint(ANTI_ALIAS_FLAG).apply {
    color = textColor
    if (textHeight == 0f) {
        textHeight = textSize
    } else {
        textSize = textHeight
    }
}

private val piePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
    style = Paint.Style.FILL
    textSize = textHeight
}

private val shadowPaint = Paint(0).apply {
    color = 0x101010
    maskFilter = BlurMaskFilter(8f, BlurMaskFilter.Blur.NORMAL)
}
```

### Java

```
private Paint textPaint;
private Paint piePaint;
private Paint shadowPaint;

@ColorInt
private int textColor;       // Obtained from style attributes.

@Dimension
private float textHeight;    // Obtained from style attributes.

private void init() {
   textPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
   textPaint.setColor(textColor);
   if (textHeight == 0) {
       textHeight = textPaint.getTextSize();
   } else {
       textPaint.setTextSize(textHeight);
   }

   piePaint = new Paint(Paint.ANTI_ALIAS_FLAG);
   piePaint.setStyle(Paint.Style.FILL);
   piePaint.setTextSize(textHeight);

   shadowPaint = new Paint(0);
   shadowPaint.setColor(0xff101010);
   shadowPaint.setMaskFilter(new BlurMaskFilter(8, BlurMaskFilter.Blur.NORMAL));
   ...
}
```

Creating objects ahead of time is an important optimization. Views are
redrawn frequently, and many drawing objects require expensive initialization.
Creating drawing objects within your `onDraw()` method significantly
reduces performance and can make your UI sluggish.

## Handle layout events

To properly draw your custom view, find out what size it is. Complex custom
views often need to perform multiple layout calculations depending on the size
and shape of their area on screen. Never make assumptions about the size of your
view on the screen. Even if only one app uses your view, that app needs to
handle different screen sizes, multiple screen densities, and various aspect
ratios in both portrait and landscape mode.

Although `View`
has many methods for handling measurement, most of them don't need to be
overridden. If your view doesn't need special control over its size, only
override one method:
`onSizeChanged()`.

`onSizeChanged()` is called when your view is first assigned a
size, and again if the size of your view changes for any reason. Calculate
positions, dimensions, and any other values related to your view's size in
`onSizeChanged()`, instead of recalculating them every time you draw.
In the following example, `onSizeChanged()` is where the view
calculates the bounding rectangle of the chart and the relative position of the
text label and other visual elements.

When your view is assigned a size, the layout manager assumes that the size
includes the view's padding. Handle the padding values when you calculate your
view's size. Here's a snippet from `onSizeChanged()` that shows how
to do this:

### Kotlin

```
private val showText    // Obtained from styled attributes.
private val textWidth   // Obtained from styled attributes.

override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
    super.onSizeChanged(w, h, oldw, oldh)
    // Account for padding.
    var xpad = (paddingLeft + paddingRight).toFloat()
    val ypad = (paddingTop + paddingBottom).toFloat()

    // Account for the label.
    if (showText) xpad += textWidth.toFloat()
    val ww = w.toFloat() - xpad
    val hh = h.toFloat() - ypad

    // Figure out how big you can make the pie.
    val diameter = Math.min(ww, hh)
}
```

### Java

```
private Boolean showText;    // Obtained from styled attributes.
private int textWidth;       // Obtained from styled attributes.

@Override
protected void onSizeChanged(int w, int h, int oldw, int oldh) {
    super.onSizeChanged(w, h, oldw, oldh);
    // Account for padding.
    float xpad = (float)(getPaddingLeft() + getPaddingRight());
    float ypad = (float)(getPaddingTop() + getPaddingBottom());

    // Account for the label.
    if (showText) xpad += textWidth;

    float ww = (float)w - xpad;
    float hh = (float)h - ypad;

    // Figure out how big you can make the pie.
    float diameter = Math.min(ww, hh);
}
```

If you need finer control over your view's layout parameters, implement
`onMeasure()`.
This method's parameters are
`View.MeasureSpec`
values that tell you how big your view's parent wants your view to be and
whether that size is a hard maximum or just a suggestion. As an optimization,
these values are stored as packed integers, and you use the static methods of
`View.MeasureSpec` to unpack the information stored in each integer.

Here's an example implementation of `onMeasure()`. In this
implementation, it attempts to make its area big enough to make the chart as big
as its label:

### Kotlin

```
override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
    // Try for a width based on your minimum.
    val minw: Int = paddingLeft + paddingRight + suggestedMinimumWidth
    val w: Int = View.resolveSizeAndState(minw, widthMeasureSpec, 1)

    // Whatever the width is, ask for a height that lets the pie get as big as
    // it can.
    val minh: Int = View.MeasureSpec.getSize(w) - textWidth.toInt() + paddingBottom + paddingTop
    val h: Int = View.resolveSizeAndState(minh, heightMeasureSpec, 0)

    setMeasuredDimension(w, h)
}
```

### Java

```
@Override
protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
   // Try for a width based on your minimum.
   int minw = getPaddingLeft() + getPaddingRight() + getSuggestedMinimumWidth();
   int w = resolveSizeAndState(minw, widthMeasureSpec, 1);

   // Whatever the width is, ask for a height that lets the pie get as big as it
   // can.
   int minh = MeasureSpec.getSize(w) - (int)textWidth + getPaddingBottom() + getPaddingTop();
   int h = resolveSizeAndState(minh, heightMeasureSpec, 0);

   setMeasuredDimension(w, h);
}
```

There are three important things to note in this code:

* The calculations take into account the view's padding. As mentioned
  earlier, this is the view's responsibility.
* The helper method
  `resolveSizeAndState()`
  is used to create the final width and height values. This helper returns
  an appropriate `View.MeasureSpec` value by comparing the
  view's needed size to the value passed into `onMeasure()`.
* `onMeasure()` has no return value. Instead, the method
  communicates its results by calling
  `setMeasuredDimension()`.
  Calling this method is mandatory. If you omit this call, the
  `View` class throws a runtime exception.

## Draw

After you define your object creation and measuring code, you can implement
`onDraw()`. Every view implements `onDraw()` differently,
but there are some common operations that most views share:

* Draw text using
  `drawText()`.
  Specify the typeface by calling
  `setTypeface()`
  and the text color by calling
  `setColor()`.
* Draw primitive shapes using
  `drawRect()`,
  `drawOval()`,
  and
  `drawArc()`.
  Change whether the shapes are filled, outlined, or both by calling
  `setStyle()`.
* Draw more complex shapes using the
  `Path`
  class. Define a shape by adding lines and curves to a `Path`
  object, then draw the shape using
  `drawPath()`.
  As with primitive shapes, paths can be outlined, filled, or both,
  depending on `setStyle()`.
* Define gradient fills by creating `LinearGradient`
  objects. Call
  `setShader()`
  to use your `LinearGradient` on filled shapes.* Draw bitmaps using
    `drawBitmap()`.

The following code draws a mix of text, lines, and shapes:

### Kotlin

```
private val data = mutableListOf<Item>() // A list of items that are displayed.

private var shadowBounds = RectF()       // Calculated in onSizeChanged.
private var pointerRadius: Float = 2f    // Obtained from styled attributes.
private var pointerX: Float = 0f         // Calculated in onSizeChanged.
private var pointerY: Float = 0f         // Calculated in onSizeChanged.
private var textX: Float = 0f            // Calculated in onSizeChanged.
private var textY: Float = 0f            // Calculated in onSizeChanged.
private var bounds = RectF()             // Calculated in onSizeChanged.
private var currentItem: Int = 0         // The index of the currently selected item.

override fun onDraw(canvas: Canvas) {
    super.onDraw(canvas)

    canvas.apply {
        // Draw the shadow.
        drawOval(shadowBounds, shadowPaint)

        // Draw the label text.
        drawText(data[currentItem].label, textX, textY, textPaint)

        // Draw the pie slices.
        data.forEach {item ->
            piePaint.shader = item.shader
            drawArc(
                bounds,
                360 - item.endAngle,
                item.endAngle - item.startAngle,
                true,
                piePaint
            )
        }

        // Draw the pointer.
        drawLine(textX, pointerY, pointerX, pointerY, textPaint)
        drawCircle(pointerX, pointerY, pointerRadius, textPaint)
    }
}

// Maintains the state for a data item.
private data class Item(
    var label: String,      
    var value: Float = 0f,

    @ColorInt
    var color: Int = 0,

    // Computed values.
    var startAngle: Float = 0f,
    var endAngle: Float = 0f,

    var shader: Shader
)
```

### Java

```
private List<Item> data = new ArrayList<Item>();  // A list of items that are displayed.

private RectF shadowBounds;                       // Calculated in onSizeChanged.
private float pointerRadius;                      // Obtained from styled attributes.
private float pointerX;                           // Calculated in onSizeChanged.
private float pointerY;                           // Calculated in onSizeChanged.
private float textX;                              // Calculated in onSizeChanged.
private float textY;                              // Calculated in onSizeChanged.
private RectF bounds;                             // Calculated in onSizeChanged.
private int currentItem = 0;                      // The index of the currently selected item.

protected void onDraw(Canvas canvas) {
    super.onDraw(canvas);

    // Draw the shadow.
    canvas.drawOval(
            shadowBounds,
            shadowPaint
    );

    // Draw the label text.
    canvas.drawText(data.get(currentItem).label, textX, textY, textPaint);

    // Draw the pie slices.
    for (int i = 0; i < data.size(); ++i) {
        Item it = data.get(i);
        piePaint.setShader(it.shader);
        canvas.drawArc(
                bounds,
                360 - it.endAngle,
                it.endAngle - it.startAngle,
                true, 
                piePaint
        );
    }

    // Draw the pointer.
    canvas.drawLine(textX, pointerY, pointerX, pointerY, textPaint);
    canvas.drawCircle(pointerX, pointerY, pointerRadius, textPaint);
}

// Maintains the state for a data item.
private class Item {
    public String label;
    public float value;
    @ColorInt
    public int color;

    // Computed values.
    public int startAngle;
    public int endAngle;

    public Shader shader;
}
```

## Apply graphics effects

Android 12 (API level 31) adds the
`RenderEffect`
class, which applies common graphics effects such as blurs, color filters,
Android shader effects, and more to
`View` objects and
rendering hierarchies. You can combine effects as chain effects, which consist
of an inner and outer effect, or blended effects. Support for this feature
varies depending on device processing power.

You can also apply effects to the underlying
`RenderNode` for
a `View` by calling
`View.setRenderEffect(RenderEffect)`.

To implement a `RenderEffect` object, do the following:

```
view.setRenderEffect(RenderEffect.createBlurEffect(radiusX, radiusY, SHADER_TILE_MODE))
```

You can create the view programmatically or inflate it from an XML layout and
retrieve it using [View bindingor
[`findViewById()`](/reference/android/view/View#findViewById(int)).](/topic/libraries/view-binding)