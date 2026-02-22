---
title: https://developer.android.com/training/tv/accessibility/talkback-support
url: https://developer.android.com/training/tv/accessibility/talkback-support
source: md.txt
---

# Support TalkBack in TV apps

TV apps sometimes have use cases that make it difficult for users who rely on[TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback)to use the app. To provide a better TalkBack experience for these users, review each of the sections in this guide and implement changes in your app where necessary. If your app uses custom views, you should also refer to the[corresponding guide](https://developer.android.com/training/tv/accessibility/custom-views)that describes how to support accessibility with custom views.

## Handle nested views

Nested views can be hard for TalkBack users to navigate. Whenever possible, make either the parent or the child view focusable by TalkBack, but not both.

To make a view focusable by TalkBack, set the[`focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable)and the[`focusableInTouchMode`](https://developer.android.com/reference/android/view/View#attr_android:focusableInTouchMode)attribute to`true`. This step is necessary because some TV devices might enter and exit touch mode while TalkBack is active.

To make a view non-focusable, it is sufficient to set the[`focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable)attribute to`false`. However, if the view is actionable (that is, its corresponding`AccessibilityNodeInfo`has[`ACTION_CLICK`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_CLICK)), it might still be focusable.

## Change descriptions for Actions

By default, TalkBack announces "Press select to activate" for actionable views. For some actions, the term "activate" might not be a good description. To provide a more accurate description, you can change it:  

### Kotlin

```kotlin
findViewById<View>(R.id.custom_actionable_view).accessibilityDelegate = object : View.AccessibilityDelegate() {
  override fun onInitializeAccessibilityNodeInfo(host: View, info: AccessibilityNodeInfo) {
    super.onInitializeAccessibilityNodeInfo(host, info)
    info.addAction(
      AccessibilityAction(
        AccessibilityAction.ACTION_CLICK.id,
        getString(R.string.custom_label)
      )
    )
  }
}
```

### Java

```java
findViewById(R.id.custom_actionable_view).setAccessibilityDelegate(new AccessibilityDelegate() {
  @Override
  public void onInitializeAccessibilityNodeInfo(View host, AccessibilityNodeInfo info) {
    super.onInitializeAccessibilityNodeInfo(host, info);
    AccessibilityAction action = new AccessibilityAction(
        AccessibilityAction.ACTION_CLICK.getId(), getString(R.string.custom_label));
    info.addAction(action);
  }
});
```

## Add support for sliders

TalkBack on TV has special support for sliders. To enable slider mode, add[`ACTION_SET_PROGRESS`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_SET_PROGRESS)to a view together with a[`RangeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.RangeInfo)object.

The user enters the slider mode by pressing the center button of the TV remote. In this mode, the arrow buttons generate[`ACTION_SCROLL_FORWARD`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_SCROLL_FORWARD)and[`ACTION_SCROLL_BACKWARD`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction#ACTION_SCROLL_BACKWARD)accessibility actions.

The following example implements a volume slider with levels from 1 to 10:  

### Kotlin

```kotlin
/**
 *   This example only provides slider functionality for TalkBack users. Additional logic should
 *   be added for other users. Such logic may reuse the increase and decrease methods.
 */
class VolumeSlider(context: Context?, attrs: AttributeSet?) : LinearLayout(context, attrs) {
  private val min = 1
  private val max = 10
  private var current = 5
  private var textView: TextView? = null

  init {
    isFocusable = true
    isFocusableInTouchMode = true
    val rangeInfo =
      AccessibilityNodeInfo.RangeInfo(
        AccessibilityNodeInfo.RangeInfo.RANGE_TYPE_INT,
        min.toFloat(),
        max.toFloat(),
        current.toFloat()
      )
    accessibilityDelegate =
      object : AccessibilityDelegate() {
        override fun onInitializeAccessibilityNodeInfo(host: View, info: AccessibilityNodeInfo) {
          super.onInitializeAccessibilityNodeInfo(host, info)
          info.addAction(AccessibilityNodeInfo.AccessibilityAction.ACTION_SET_PROGRESS)
          info.rangeInfo = rangeInfo
        }

        override fun performAccessibilityAction(host: View, action: Int, args: Bundle?): Boolean {
          if (action == AccessibilityNodeInfo.AccessibilityAction.ACTION_SCROLL_FORWARD.id) {
            increase()
            return true
          }
          if (action == AccessibilityNodeInfo.AccessibilityAction.ACTION_SCROLL_BACKWARD.id) {
            decrease()
            return true
          }
          return super.performAccessibilityAction(host, action, args)
        }
      }
  }

  override fun onFinishInflate() {
    super.onFinishInflate()
    textView = findViewById(R.id.text)
    textView!!.text = context.getString(R.string.level, current)
  }

  private fun increase() {
    update((current + 1).coerceAtMost(max))
  }

  private fun decrease() {
    update((current - 1).coerceAtLeast(min))
  }

  private fun update(newLevel: Int) {
    if (textView == null) {
      return
    }
    val newText = context.getString(R.string.level, newLevel)
    // Update the user interface with the new volume.
    textView!!.text = newText
    // Announce the new volume.
    announceForAccessibility(newText)
    current = newLevel
  }
}
```

### Java

```java
/**
 *   This example only provides slider functionality for TalkBack users. Additional logic should
 *   be added for other users. Such logic can reuse the increase and decrease methods.
 */
public class VolumeSlider extends LinearLayout {
  private final int min = 1;
  private final int max = 10;
  private int current = 5;
  private TextView textView;

  public VolumeSlider(Context context, AttributeSet attrs) {
    super(context, attrs);
    setFocusable(true);
    setFocusableInTouchMode(true);
    RangeInfo rangeInfo = new RangeInfo(RangeInfo.RANGE_TYPE_INT, min, max, current);
    setAccessibilityDelegate(
        new AccessibilityDelegate() {
          @Override
          public void onInitializeAccessibilityNodeInfo(View host, AccessibilityNodeInfo info) {
            super.onInitializeAccessibilityNodeInfo(host, info);
            info.addAction(AccessibilityAction.ACTION_SET_PROGRESS);
            info.setRangeInfo(rangeInfo);
          }

          @Override
          public boolean performAccessibilityAction(View host, int action, Bundle args) {
            if (action == AccessibilityAction.ACTION_SCROLL_FORWARD.getId()) {
              increase();
              return true;
            }
            if (action == AccessibilityAction.ACTION_SCROLL_BACKWARD.getId()) {
              decrease();
              return true;
            }
            return super.performAccessibilityAction(host, action, args);
          }
        });
  }

  @Override
  protected void onFinishInflate() {
    super.onFinishInflate();
    textView = findViewById(R.id.text);
    textView.setText(getContext().getString(R.string.level, current));
  }

  private void increase() {
    update(Math.min(current + 1, max));
  }

  private void decrease() {
    update(Math.max(current - 1, min));
  }

  private void update(int newLevel) {
    if (textView == null) {
      return;
    }
    String newText = getContext().getString(R.string.level, newLevel);
    // Update the user interface with the new volume.
    textView.setText(newText);
    // Announce the new volume.
    announceForAccessibility(newText);
    current = newLevel;
  }
}
```