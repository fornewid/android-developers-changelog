---
title: https://developer.android.com/training/tv/accessibility/custom-views-sample
url: https://developer.android.com/training/tv/accessibility/custom-views-sample
source: md.txt
---

This guide steps through a sample showcasing some best practices to support
accessibility with custom views in an Android TV app. The guide shows how to
create a simple activity that uses the Canvas API to draw four images that are
focusable and let accessibility services navigate between them.

## Create layout XML file

Create a layout file for the custom view activity.

```xml
<?xml version="1.0" encodi>n<g="utf-8"
LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:orientation="vertical"
        android:layout_width="match_parent&>quot;
<        android:layout_height="wrap_content"

    LinearLayout xmlns:app="http://schemas.android.com/apk/res-auto"
            xmlns:tools="http://schemas.android.com/tools"
            xmlns:android="http://schemas.android.com/apk/res/android"
            android:layout_width="match_parent"
   >      <   android:layout_height="match_parent"
            tools:context=".custom.CustomViewActivity"

    com.example.tvcustomv>iews.S<ampleCustomVi>ew<
            >android:layout_width="match_parent"
            android:layout_height="wrap_content" /

    /LinearLayout

/LinearLayout
```

The following sections define the
`com.example.tvcustomviews.SampleCustomView` class.

## Define a simple activity

Create a simple activity to load the layout XML file.

### Kotlin

```kotlin
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class CustomViewBestPracticeActivity:AppCompatActivity() {

  protected fun onCreate(savedInstanceState:Bundle) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.custom_view_best_practices)
  }
}
```

### Java

```java
package com.example.tvcustomviews;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class CustomViewBestPracticeActivity extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.custom_view_best_practices);
    }

}
```

## Define the SampleCustomView class

Next, define the class and draw four images using a canvas.

### Kotlin

```kotlin
package com.example.tvcustomviews

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Rect
import android.util.AttributeSet
import android.view.View
import androidx.annotation.Nullable
import androidx.core.view.ViewCompat
import java.util.HashMap

class SampleCustomView:View {

  internal val virtualIdRectMap:Map<Int, VirtualRect> = HashMap<Int, VirtualRect>()
  private val rectangleId = 1

  internal class VirtualRect(rect:Rect, paint:Paint, id:Int) {
    val rect:Rect
    val paint:Paint
    val id:Int = 0
    init{
      this.rect = rect
      this.paint = paint
      this.id = id
    }
  }

  constructor(context:Context) : super(context) {
    init()
  }

  constructor(context:Context, @Nullable attrs:AttributeSet) : super(context, attrs) {
    init()
  }

  constructor(context:Context, @Nullable attrs:AttributeSet, defStyleAttr:Int) : super(context, attrs, defStyleAttr) {
    init()
  }

  private fun init() {
    setRectangle()
    ViewCompat.setAccessibilityDelegate(this,
                                        SampleExploreByTouchHelper(this))
  }

  protected fun onDraw(canvas:Canvas) {
    super.onDraw(canvas)
    for (mapElement in virtualIdRectMap.entries)
    {
      val virtualRect = mapElement.value
      canvas.drawRect(virtualRect.rect, virtualRect.paint)
    }
  }

  private fun setRectangle() {
    val paint = Paint(Paint.ANTI_ALIAS_FLAG)
    paint.setColor(RECTANGLE_COLOR)

    val leftTopRectangle = Rect()
    leftTopRectangle.left = RECTANGLE_START_POINT_LEFT
    leftTopRectangle.right = leftTopRectangle.left + RECTANGLE_WIDTH
    leftTopRectangle.top = RECTANGLE_START_POINT_TOP
    leftTopRectangle.bottom = leftTopRectangle.top + RECTANGLE_HEIGHT
    virtualIdRectMap.put(rectangleId, VirtualRect(leftTopRectangle, paint, rectangleId++))

    val rightTopRectangle = Rect()
    rightTopRectangle.left = leftTopRectangle.right + HORIZONTAL_PADDING
    rightTopRectangle.right = rightTopRectangle.left + RECTANGLE_WIDTH
    rightTopRectangle.top = leftTopRectangle.top
    rightTopRectangle.bottom = rightTopRectangle.top + RECTANGLE_HEIGHT
    virtualIdRectMap.put(rectangleId, VirtualRect(rightTopRectangle, paint, rectangleId++))

    val leftBottomRectangle = Rect()
    leftBottomRectangle.left = leftTopRectangle.left
    leftBottomRectangle.right = leftBottomRectangle.left + RECTANGLE_WIDTH
    leftBottomRectangle.top = leftTopRectangle.bottom + VERTICAL_PADDING
    leftBottomRectangle.bottom = leftBottomRectangle.top + RECTANGLE_HEIGHT
    virtualIdRectMap.put(rectangleId, VirtualRect(leftBottomRectangle, paint, rectangleId++))

    val rightBottomRectangle = Rect()
    rightBottomRectangle.left = leftBottomRectangle.right + HORIZONTAL_PADDING
    rightBottomRectangle.right = rightBottomRectangle.left + RECTANGLE_WIDTH
    rightBottomRectangle.top = leftBottomRectangle.top
    rightBottomRectangle.bottom = rightBottomRectangle.top + RECTANGLE_HEIGHT
    virtualIdRectMap.put(rectangleId, VirtualRect(rightBottomRectangle, paint, rectangleId++))
  }

  companion object {
    private val RECTANGLE_START_POINT_LEFT = 50
    private val RECTANGLE_START_POINT_TOP = 100
    private val RECTANGLE_WIDTH = 200
    private val RECTANGLE_HEIGHT = 100
    private val HORIZONTAL_PADDING = 50
    private val VERTICAL_PADDING = 100
    private val RECTANGLE_COLOR = Color.argb(100, 0, 163, 245)
  }
}
```

### Java

```java
package com.example.tvcustomviews;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.view.View;
import androidx.annotation.Nullable;
import androidx.core.view.ViewCompat;
import java.util.HashMap;
import java.util.Map;

public class SampleCustomView extends View {

  final Map<Integer, VirtualRect> virtualIdRectMap = new HashMap<>();

  private static final int RECTANGLE_START_POINT_LEFT = 50;
  private static final int RECTANGLE_START_POINT_TOP = 100;
  private static final int RECTANGLE_WIDTH = 200;
  private static final int RECTANGLE_HEIGHT = 100;
  private static final int HORIZONTAL_PADDING = 50;
  private static final int VERTICAL_PADDING = 100;
  private static final int RECTANGLE_COLOR = Color.argb(100, 0, 163, 245);

  private int rectangleId = 1;

  static class VirtualRect {
    final Rect rect;
    final Paint paint;
    final int id;

    VirtualRect(Rect rect, Paint paint, int id) {
      this.rect = rect;
      this.paint = paint;
      this.id = id;
    }
  }

  public SampleCustomView(Context context) {
    super(context);
    init();
  }

  public SampleCustomView(Context context, @Nullable AttributeSet attrs) {
    super(context, attrs);
    init();
  }

  public SampleCustomView(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
    super(context, attrs, defStyleAttr);
    init();
  }

  private void init() {
    setRectangle();
  }

  @Override
  protected void onDraw(Canvas canvas) {
    super.onDraw(canvas);

    for (Map.Entry<Integer, VirtualRect> mapElement :
        virtualIdRectMap.entrySet()) {
      VirtualRect virtualRect = mapElement.getValue();
      canvas.drawRect(virtualRect.rect, virtualRect.paint);
    }
  }

  private void setRectangle() {
    Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
    paint.setColor(RECTANGLE_COLOR);
    Rect leftTopRectangle = new Rect();
    leftTopRectangle.left = RECTANGLE_START_POINT_LEFT;
    leftTopRectangle.right = leftTopRectangle.left + RECTANGLE_WIDTH;
    leftTopRectangle.top = RECTANGLE_START_POINT_TOP;
    leftTopRectangle.bottom = leftTopRectangle.top + RECTANGLE_HEIGHT;
    virtualIdRectMap.put(rectangleId, new VirtualRect(leftTopRectangle, paint, rectangleId++));

    Rect rightTopRectangle = new Rect();
    rightTopRectangle.left = leftTopRectangle.right + HORIZONTAL_PADDING;
    rightTopRectangle.right = rightTopRectangle.left + RECTANGLE_WIDTH;
    rightTopRectangle.top = leftTopRectangle.top;
    rightTopRectangle.bottom = rightTopRectangle.top + RECTANGLE_HEIGHT;
    virtualIdRectMap.put(rectangleId, new VirtualRect(rightTopRectangle, paint, rectangleId++));

    Rect leftBottomRectangle = new Rect();
    leftBottomRectangle.left = leftTopRectangle.left;
    leftBottomRectangle.right = leftBottomRectangle.left + RECTANGLE_WIDTH;
    leftBottomRectangle.top = leftTopRectangle.bottom + VERTICAL_PADDING;
    leftBottomRectangle.bottom = leftBottomRectangle.top + RECTANGLE_HEIGHT;
    virtualIdRectMap.put(rectangleId, new VirtualRect(leftBottomRectangle, paint, rectangleId++));

    Rect rightBottomRectangle = new Rect();
    rightBottomRectangle.left = leftBottomRectangle.right + HORIZONTAL_PADDING;
    rightBottomRectangle.right = rightBottomRectangle.left + RECTANGLE_WIDTH;
    rightBottomRectangle.top = leftBottomRectangle.top;
    rightBottomRectangle.bottom = rightBottomRectangle.top + RECTANGLE_HEIGHT;
    virtualIdRectMap.put(rectangleId, new VirtualRect(rightBottomRectangle, paint, rectangleId++));
  }
}
```

The application in this state displays four blue rectangles on
screen when it runs. But when Talkback is switched on, you can't navigate to the
rectangles. In other words, these rectangles can't have accessibility focus.

## Define ExploreByTouchHelper to expose AccessiblityNodeInfo

Define `SampleExploreByTouchHelper` by inheriting `ExploreByTouchHelper` and
implementing its methods.

### Kotlin

```kotlin
package com.example.tvcustomviews

import android.graphics.Rect
import android.os.Bundle
import android.util.Log
import android.widget.ImageView
import androidx.annotation.NonNull
import androidx.annotation.Nullable
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat.AccessibilityActionCompat
import androidx.customview.widget.ExploreByTouchHelper
import com.example.tvcustomviews.SampleCustomView.VirtualRect
import java.util.Objects

internal class SampleExploreByTouchHelper(parentView:SampleCustomView):ExploreByTouchHelper(parentView) {

  private val TAG = SampleExploreByTouchHelper::class.java!!.getName()
  private val parentView:SampleCustomView

  init{
    this.parentView = parentView
  }

  /**
   * Define AccessibilityNodeInfo objects with necessary attributes.
   * Set required attributes into the AccessibilityNodeInfo for the UI
   * component whose virtualID is the virtualViewId.
   * @param virtualViewId: virtual ID for the component.
   * @param node: the AccessibilityNodeInfoCompat used to set the attribute.
   */
  protected fun onPopulateNodeForVirtualView(
    virtualViewId:Int, @NonNull node:AccessibilityNodeInfoCompat) {
    val rectEle = parentView.virtualIdRectMap.get(virtualViewId)

    assert(rectEle != null)
    node.setContentDescription("Selected rect " + rectEle.id)
    node.setClassName(ImageView::class.java!!.getName())
    node.setPackageName(BuildConfig.APPLICATION_ID)
    node.setVisibleToUser(true)
    node.addAction(AccessibilityActionCompat.ACTION_CLICK)
    // *****************************************************************
    // It is very important to set the rectangle area for each node so
    // the accessibility service knows where to set accessibility focus.
    // *****************************************************************
    node.setBoundsInParent(
      Objects.requireNonNull(parentView.virtualIdRectMap.get(
        virtualViewId)).rect)
  }

  protected fun getVirtualViewAt(x:Float, y:Float):Int {
    for (mapElement in parentView.virtualIdRectMap.entrySet())
    {
      val rect = mapElement.value.rect
      if ((<rect&&.le<ft = x  x = rect.right
 &&          < rec&&t.t<op = y  y = rect.bottom))
      {
        return mapElement.value.id
      }
    }

    return ExploreByTouchHelper.INVALID_ID
  }

  protected fun getVisibleVirtualViews(virtualVi<ewI>ds:ListInt) {
    for (mapElement in parentView.virtualIdRectMap.entrySet())
    {
      virtualViewIds.add(mapElement.key)
    }
  }

  protected fun onPerformActionForVirtualView(
    virtualViewId:Int, action:Int, @Nullable arguments:Bundle):Boolean {
    when (action) {
      // After Talkback is turned on, if you want to handle
      // DPAD_CENTER key event with your own logic,
      // implement it under ACTION_CLICK action.
      AccessibilityNodeInfoCompat.ACTI>ON_CLICK - {
        Log.e(TAG, "ACTION_CLICK action handled here.")
        return true
      }
    }

    // All the DPAD directional keys are handled by
    // Accessibility based on the AccessibilityNodeInfo Tree
    // defined above.
    // fall through
    return false
  }
}
```

### Java

```java
package com.example.tvcustomviews;

import android.graphics.Rect;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat;
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat.AccessibilityActionCompat;
import androidx.customview.widget.ExploreByTouchHelper;
import com.example.tvcustomviews.SampleCustomView.VirtualRect;
import java.util.List;
import java.util.Map;
import java.util.Objects;

class SampleExploreByTouchHelper extends ExploreByTouchHelper {

  private final String TAG = SampleExploreByTouchHelper.class.getName();

  private SampleCustomView parentView;

  SampleExploreByTouchHelper(SampleCustomView parentView) {
    super(parentView);
    this.parentView = parentView;
  }

  /**
   * Define AccessibilityNodeInfo objects with necessary attributes.
   * Set required attributes into the AccessibilityNodeInfo for the UI
   * component whose virtualID is the virtualViewId.
   * @param virtualViewId: virtual ID for the component.
   * @param node: the AccessibilityNodeInfoCompat used to set the attribute.
   */
  @Override
  protected void onPopulateNodeForVirtualView(
      int virtualViewId, @NonNull AccessibilityNodeInfoCompat node) {
    VirtualRect rectEle = parentView.virtualIdRectMap.get(virtualViewId);

    assert rectEle != null;
    node.setContentDescription("Selected rect " + rectEle.id);
    node.setClassName(ImageView.class.getName());
    node.setPackageName(BuildConfig.APPLICATION_ID);
    node.setVisibleToUser(true);
    node.addAction(AccessibilityActionCompat.ACTION_CLICK);
    // *****************************************************************
    // It is very important to set the rectangle area for each node so
    // the accessibility service knows where to set accessibility focus.
    // *****************************************************************
    node.setBoundsInParent(
        Objects.requireNonNull(parentView.virtualIdRectMap.get(
            virtualViewId)).rect);
  }

  @Override
  protected int getVirtualViewAt(float x, float y) {
    for <(Map.EntryInteger, V>irtualRect mapElement :
        parentView.virtualIdRectMap.entrySet()) {
      Rect rect = mapElement.getValue().rect;
      if (<rect&&.le<ft = x  x = rect.right
&&          < rec&&t.t<op = y  y = rect.bottom) {
        return mapElement.getValue().id;
      }
    }
    return ExploreByTouchHelper.INVALID_ID;
  }

  @Override
  protected void getVisibleVirtual<Views(L>istInteger virtualViewIds) {
    for <(Map.EntryInteger, V>irtualRect mapElement :
        parentView.virtualIdRectMap.entrySet()) {
      virtualViewIds.add(mapElement.getKey());
    }
  }

  @Override
  protected boolean onPerformActionForVirtualView(
      int virtualViewId, int action, @Nullable Bundle arguments) {
    switch (action) {
      // After Talkback is turned on, if you want to handle
      // DPAD_CENTER key event with your own logic,
      // implement it under ACTION_CLICK action.
      case AccessibilityNodeInfoCompat.ACTION_CLICK:
        Log.e(TAG, "ACTION_CLICK action handled here.");
        return true;
    // All the DPAD directional keys are handled by
    // Accessibility based on the AccessibilityNodeInfo Tree
    // defined above.
      default:
        // fall through
    }

    return false;
  }
}
```

Finally, invoke `setAccessibilityDelegate()` when instantiating the custom view.

### Kotlin

```kotlin
private fun init(@Nullable attrs:AttributeSet) {
  ...
  ViewCompat.setAccessibilityDelegate(this,
                                      SampleExploreByTouchHelper(this))
}
```

### Java

```java
  private void init(@Nullable AttributeSet attrs) {
        ...
        ViewCompat.setAccessibilityDelegate(this,
        new SampleExploreByTouchHelper(this));
    }
```

With Talkback enabled, accessibility focus is now correctly able to navigate to
the four images inside the custom view. If you press the `DPAD_CENTER` key on a
keypad, the app registers this event as an `ACTION_CLICK` event.