---
title: Make custom views more accessible  |  App quality  |  Android Developers
url: https://developer.android.com/guide/topics/ui/accessibility/custom-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Make custom views more accessible Stay organized with collections Save and categorize content based on your preferences.



If your application requires a
[custom view component](/guide/topics/ui/custom-components),
you must make the view more accessible. The following steps can improve your custom view's
accessibility, as described on this page:

* Handle directional controller clicks.
* Implement accessibility API methods.
* Send `AccessibilityEvent`
  objects specific to your custom view.
* Populate `AccessibilityEvent` and
  `AccessibilityNodeInfo`
  for your view.

## Handle directional controller clicks

On most devices, clicking a view using a directional controller sends a
`KeyEvent` with
`KEYCODE_DPAD_CENTER`
to the view currently in focus. All standard Android views handle
`KEYCODE_DPAD_CENTER` appropriately. When building a custom
`View`
control, make sure this event has the same effect as tapping the view on the touchscreen.

Your custom control must treat the
`KEYCODE_ENTER`
event the same as `KEYCODE_DPAD_CENTER`. This makes interactions with a full keyboard
easier for users.

**Note:** If your view uses
`ImeAction`,
it must handle `KEYCODE_DPAD_CENTER` and `KEYCODE_ENTER` the same way it
handles the `ImeAction`.

## Implement accessibility API methods

Accessibility events are messages about users' interactions with your app's visual interface
components. These messages are handled by [accessibility services](/guide/topics/ui/accessibility/services), which
use the information in these events to produce supplemental feedback and prompts. The accessibility
methods are part of the `View` and
`View.AccessibilityDelegate`
classes. The methods are as follows:

`dispatchPopulateAccessibilityEvent()`
:   The system calls this method when your custom view generates an accessibility event. The default
    implementation of this method calls `onPopulateAccessibilityEvent()` for this view
    and then the `dispatchPopulateAccessibilityEvent()` method for each child of this
    view.

`onInitializeAccessibilityEvent()`
:   The system calls this method to obtain additional information about the state of the view beyond
    text content. If your custom view provides interactive control beyond a simple
    `TextView` or
    `Button`, override this method
    and set the additional information about your view—such as password field type, checkbox
    type, or states that provide user interaction or feedback into the event—using this
    method. If you override this method, call its super implementation and only modify properties
    that are not set by the super class.

`onInitializeAccessibilityNodeInfo()`
:   This method provides accessibility services with information about the state of the view. The
    default `View` implementation has a standard set of view properties, but if your
    custom view provides interactive control beyond a simple `TextView` or
    `Button`, override this method and set the additional information about your view
    into the `AccessibilityNodeInfo` object handled by this method.

`onPopulateAccessibilityEvent()`
:   This method sets the spoken text prompt of the `AccessibilityEvent` for your
    view. It is also called if the view is a child of a view that generates an accessibility
    event.
    **Note:** Modifying additional attributes beyond the text within this method potentially
    overwrites properties set by other methods. While you can modify attributes of the
    accessibility event with this method, limit these changes to text content, and use the
    `onInitializeAccessibilityEvent()` method to modify other properties of the
    event. Also, if your implementation of this event completely overrides the output text
    without letting other parts of your layout to modify its content, then don't call the super
    implementation of this method in your code.

`onRequestSendAccessibilityEvent()`
:   The system calls this method when a child of your view generates an
    `AccessibilityEvent`. This step lets the parent view amend the accessibility
    event with additional information. Implement this method only if your custom view can have
    child views and if the parent view can provide context information to the accessibility
    event that is useful to accessibility services.

`sendAccessibilityEvent()`
:   The system calls this method when a user takes action on a view. The event is classified with
    a user action type, such as `TYPE_VIEW_CLICKED`. In general, you must send an
    `AccessibilityEvent` whenever the content of your custom view changes.

`sendAccessibilityEventUnchecked()`
:   This method is used when the calling code needs to directly control the check for
    accessibility being enabled on the device
    (`AccessibilityManager.isEnabled()`).
    If you implement this method, perform the call as if accessibility is enabled, regardless of the
    system setting. You typically don't need to implement this method for a custom view.

To support accessibility, override and implement the preceding accessibility methods directly in
your custom view class.

At minimum, implement the following accessibility methods for your custom view class:

* `dispatchPopulateAccessibilityEvent()`
* `onInitializeAccessibilityEvent()`
* `onInitializeAccessibilityNodeInfo()`
* `onPopulateAccessibilityEvent()`

For more information about implementing these methods, see the section about
[populating accessibility events](#populate-events).

## Send accessibility events

Depending on the specifics of your custom view, it might need to send
`AccessibilityEvent` objects at different times or for events not handled by the default
implementation. The `View` class provides a default implementation for these event
types:

* `TYPE_VIEW_CLICKED`
* `TYPE_VIEW_FOCUSED`
* `TYPE_VIEW_HOVER_ENTER`
* `TYPE_VIEW_HOVER_EXIT`
* `TYPE_VIEW_LONG_CLICKED`
* `TYPE_VIEW_SCROLLED`

**Note:** Hover events are associated with the Explore by Touch feature, which uses these
events as triggers for providing audible prompts for user interface elements.

In general, you must send an `AccessibilityEvent` whenever the content of your custom
view changes. For example, if you are implementing a custom slider bar that lets the user select a
numeric value by pressing the left or right arrow key, your custom view must emit an event of
`TYPE_VIEW_TEXT_CHANGED`
whenever the slider value changes. The following code sample demonstrates the use of the
`sendAccessibilityEvent()` method to report this event.

### Kotlin

```
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
    return when(keyCode) {
        KeyEvent.KEYCODE_DPAD_LEFT -> {
            currentValue--
            sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_TEXT_CHANGED)
            true
        }
        ...
    }
}
```

### Java

```
@Override
public boolean onKeyUp (int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_DPAD_LEFT) {
        currentValue--;
        sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_TEXT_CHANGED);
        return true;
    }
    ...
}
```

## Populate accessibility events

Each `AccessibilityEvent` has a set of required properties that describe the current
state of the view. These properties include things such as the view's class name, content
description, and checked state. The specific properties required for each event type are described
in the
`AccessibilityEvent`
reference documentation.

The `View` implementation provides default values for these
required properties. Many of these values, including the class name and event timestamp, are
provided automatically. If you are creating a custom view component, you must provide information
about the content and characteristics of the view. This information can be as simple as a button
label and can include additional state information that you want to add to the event.

Use the
`onPopulateAccessibilityEvent()`
and
`onInitializeAccessibilityEvent()`
methods to populate or modify the information in an `AccessibilityEvent`. Use the
`onPopulateAccessibilityEvent()` method specifically for adding or modifying the text
content of the event, which is turned into audible prompts by accessibility services such as
TalkBack. Use the `onInitializeAccessibilityEvent()` method for populating additional
information about the event, such as the selection state of the view.

In addition, implement the
`onInitializeAccessibilityNodeInfo()`
method. Accessibility services use the `AccessibilityNodeInfo` objects populated by this
method to investigate the view hierarchy that generates an accessibility event after it is received
and provide appropriate feedback to users.

The following code example shows how to override these three methods in your view:

### Kotlin

```
override fun onPopulateAccessibilityEvent(event: AccessibilityEvent?) {
    super.onPopulateAccessibilityEvent(event)
    // Call the super implementation to populate its text for the
    // event. Then, add text not present in a super class.
    // You typically only need to add the text for the custom view.
    if (text?.isNotEmpty() == true) {
        event?.text?.add(text)
    }
}

override fun onInitializeAccessibilityEvent(event: AccessibilityEvent?) {
    super.onInitializeAccessibilityEvent(event)
    // Call the super implementation to let super classes
    // set appropriate event properties. Then, add the new checked
    // property that is not supported by a super class.
    event?.isChecked = isChecked()
}

override fun onInitializeAccessibilityNodeInfo(info: AccessibilityNodeInfo?) {
    super.onInitializeAccessibilityNodeInfo(info)
    // Call the super implementation to let super classes set
    // appropriate info properties. Then, add the checkable and checked
    // properties that are not supported by a super class.
    info?.isCheckable = true
    info?.isChecked = isChecked()
    // You typically only need to add the text for the custom view.
    if (text?.isNotEmpty() == true) {
        info?.text = text
    }
}
```

### Java

```
@Override
public void onPopulateAccessibilityEvent(AccessibilityEvent event) {
    super.onPopulateAccessibilityEvent(event);
    // Call the super implementation to populate its text for the
    // event. Then, add the text not present in a super class.
    // You typically only need to add the text for the custom view.
    CharSequence text = getText();
    if (!TextUtils.isEmpty(text)) {
        event.getText().add(text);
    }
}

@Override
public void onInitializeAccessibilityEvent(AccessibilityEvent event) {
    super.onInitializeAccessibilityEvent(event);
    // Call the super implementation to let super classes
    // set appropriate event properties. Then, add the new checked
    // property that is not supported by a super class.
    event.setChecked(isChecked());
}

@Override
public void onInitializeAccessibilityNodeInfo(AccessibilityNodeInfo info) {
    super.onInitializeAccessibilityNodeInfo(info);
    // Call the super implementation to let super classes set
    // appropriate info properties. Then, add the checkable and checked
    // properties that are not supported by a super class.
    info.setCheckable(true);
    info.setChecked(isChecked());
    // You typically only need to add the text for the custom view.
    CharSequence text = getText();
    if (!TextUtils.isEmpty(text)) {
        info.setText(text);
    }
}
```

You can implement these methods directly in your custom view class.

## Provide a customized accessibility context

Accessibility services can inspect the containing view hierarchy of a user interface component
that generates an accessibility event. This lets accessibility services provide richer contextual
information to aid users.

There are cases where accessibility services can't get adequate information from the view
hierarchy. An example of this is a custom interface control that has two or more separately
clickable areas, such as a calendar control. In this case, the services can't get adequate
information because the clickable subsections are not part of the view hierarchy.

![](/static/guide/topics/ui/accessibility/calendar.png)

**Figure 1.** A custom calendar view with selectable day elements.

In the example in figure 1, the entire calendar is implemented as a single view, so accessibility
services don't receive enough information about the content of the view and the user's selection
within the view unless the developer provides additional information. For example, if a user clicks
on the day labeled **17**, the accessibility framework only receives the description information
for the whole calendar control. In this case, the TalkBack accessibility service announces
"Calendar" or "April Calendar," and the user doesn't know what day is selected.

To provide adequate context information for accessibility services in situations like this, the
framework provides a way to specify a virtual view hierarchy. A *virtual view hierarchy* is a
way for app developers to provide a complementary view hierarchy to accessibility services that more
closely matches the information on screen. This approach lets accessibility services provide more
useful context information to users.

Another situation where a virtual view hierarchy might be needed is a user interface containing
a set of `View` controls that have closely related functions, where an action on one
control affects the contents of one or more elements—such as a number picker with separate up
and down buttons. In this case, accessibility services can't get adequate information because an
action on one control changes content in another, and the relationship of those controls might not
be apparent to the service.

To handle this situation, group the related controls with a containing view and provide a virtual
view hierarchy from this container to clearly represent the information and behavior provided by the
controls.

To provide a virtual view hierarchy for a view, override the
`getAccessibilityNodeProvider()`
method in your custom view or view group and return an implementation of
`AccessibilityNodeProvider`.
You can implement a virtual view hierarchy by using the Support Library with the
`ViewCompat.getAccessibilityNodeProvider()`
method and provide an implementation with
`AccessibilityNodeProviderCompat`.

To simplify the task of providing information to accessibility services and managing
accessibility focus, you can instead implement
`ExploreByTouchHelper`.
It provides an `AccessibilityNodeProviderCompat` and can be attached as a view's
`AccessibilityDelegateCompat` by calling
[`setAccessibilityDelegate`](/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,%20androidx.core.view.AccessibilityDelegateCompat)).
For an example, see
`ExploreByTouchHelperActivity`.
`ExploreByTouchHelper` is also used by framework widgets such as
`CalendarView`, through its
child view
`SimpleMonthView`.

## Handle custom touch events

Custom view controls might require non-standard touch event behavior, as demonstrated in the
following examples.

### Define click-based actions

If your widget uses the
[`OnClickListener`](/reference/android/view/View.OnClickListener) or
[`OnLongClickListener`](/reference/android/view/View.OnLongClickListener)
interface, the system handles the
[`ACTION_CLICK`](/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.AccessibilityActionCompat#ACTION_CLICK())
and
[`ACTION_LONG_CLICK`](/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.AccessibilityActionCompat#ACTION_LONG_CLICK())
actions for you. If your app uses a more customized widget that relies on the
[`OnTouchListener`](/reference/android/view/View.OnTouchListener) interface,
define custom handlers for the click-based accessibility actions. To do so, call the
[`replaceAccessibilityAction()`](/reference/androidx/core/view/ViewCompat#replaceAccessibilityAction(android.view.View,%20androidx.core.view.accessibility.AccessibilityNodeInfoCompat.AccessibilityActionCompat,%20java.lang.CharSequence,%20androidx.core.view.accessibility.AccessibilityViewCommand))
method for each action, as shown in the following code snippet:

### Kotlin

```
override fun onCreate(savedInstanceState: Bundle?) {
    ...

    // Assumes that the widget is designed to select text when tapped, and selects
    // all text when tapped and held. In its strings.xml file, this app sets
    // "select" to "Select" and "select_all" to "Select all".
    ViewCompat.replaceAccessibilityAction(
        binding.textSelectWidget,
        ACTION_CLICK,
        getString(R.string.select)
    ) { view, commandArguments ->
        selectText()
    }

    ViewCompat.replaceAccessibilityAction(
        binding.textSelectWidget,
        ACTION_LONG_CLICK,
        getString(R.string.select_all)
    ) { view, commandArguments ->
        selectAllText()
    }
}
```

### Java

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    ...

    // Assumes that the widget is designed to select text when tapped, and select
    // all text when tapped and held. In its strings.xml file, this app sets
    // "select" to "Select" and "select_all" to "Select all".
    ViewCompat.replaceAccessibilityAction(
            binding.textSelectWidget,
            ACTION_CLICK,
            getString(R.string.select),
            (view, commandArguments) -> selectText());

    ViewCompat.replaceAccessibilityAction(
            binding.textSelectWidget,
            ACTION_LONG_CLICK,
            getString(R.string.select_all),
            (view, commandArguments) -> selectAllText());
}
```

### Create custom click events

A custom control can use the `onTouchEvent(MotionEvent)`
listener method to detect the
`ACTION_DOWN` and
`ACTION_UP` events and
trigger a special click event. To maintain compatibility with accessibility services, the code that
handles this custom click event must do the following:

1. Generate an appropriate `AccessibilityEvent` for the interpreted click action.
2. Enable accessibility services to perform the custom click action for users who are unable to
   use a touch screen.

To handle these requirements efficiently, your code must override the
`performClick()` method,
which must call the super implementation of this method and then execute whatever actions are
required by the click event. When the custom click action is detected, that code must then call your
`performClick()` method. The following code example demonstrates this pattern.

### Kotlin

```
class CustomTouchView(context: Context) : View(context) {

    var downTouch = false

    override fun onTouchEvent(event: MotionEvent): Boolean {
        super.onTouchEvent(event)

        // Listening for the down and up touch events.
        return when (event.action) {
            MotionEvent.ACTION_DOWN -> {
                downTouch = true
                true
            }

            MotionEvent.ACTION_UP -> if (downTouch) {
                downTouch = false
                performClick() // Call this method to handle the response and
                // enable accessibility services to
                // perform this action for a user who can't
                // tap the touchscreen.
                true
            } else {
                false
            }

            else -> false  // Return false for other touch events.
        }
    }

    override fun performClick(): Boolean {
        // Calls the super implementation, which generates an AccessibilityEvent
        // and calls the onClick() listener on the view, if any.
        super.performClick()

        // Handle the action for the custom click here.

        return true
    }
}
```

### Java

```
class CustomTouchView extends View {

    public CustomTouchView(Context context) {
        super(context);
    }

    boolean downTouch = false;

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        super.onTouchEvent(event);

        // Listening for the down and up touch events
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                downTouch = true;
                return true;

            case MotionEvent.ACTION_UP:
                if (downTouch) {
                    downTouch = false;
                    performClick(); // Call this method to handle the response and
                                    // enable accessibility services to
                                    // perform this action for a user who can't
                                    // tap the touchscreen.
                    return true;
                }
        }
        return false; // Return false for other touch events.
    }

    @Override
    public boolean performClick() {
        // Calls the super implementation, which generates an AccessibilityEvent
        // and calls the onClick() listener on the view, if any.
        super.performClick();

        // Handle the action for the custom click here.

        return true;
    }
}
```

The preceding pattern helps ensure that the custom click event is compatible with accessibility
services by using the `performClick()` method to generate an accessibility event and
provide an entry point for accessibility services to act on behalf of a user performing the custom
click event.

**Note:** If your custom view has distinct clickable regions, such as a custom calendar view,
implement a [virtual view hierarchy](#virtual-hierarchy) by overriding
`getAccessibilityNodeProvider()` in your custom view to be compatible with
accessibility services.