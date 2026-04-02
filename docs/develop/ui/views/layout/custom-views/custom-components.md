---
title: https://developer.android.com/develop/ui/views/layout/custom-views/custom-components
url: https://developer.android.com/develop/ui/views/layout/custom-views/custom-components
source: md.txt
---

# Create custom view components

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.  
[Custom Layouts in Compose →](https://developer.android.com/jetpack/compose/layouts/custom)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Android offers a sophisticated and powerful componentized model for building your UI, based on the fundamental layout classes[View](https://developer.android.com/reference/android/view/View)and[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup). The platform includes a variety of prebuilt`View`and`ViewGroup`subclasses---called widgets and layouts, respectively---that you can use to construct your UI.

A partial list of available widgets includes[Button](https://developer.android.com/reference/android/widget/Button),[TextView](https://developer.android.com/reference/android/widget/TextView),[EditText](https://developer.android.com/reference/android/widget/EditText),[ListView](https://developer.android.com/reference/android/widget/ListView),[CheckBox](https://developer.android.com/reference/android/widget/CheckBox),[RadioButton](https://developer.android.com/reference/android/widget/RadioButton),[Gallery](https://developer.android.com/reference/android/widget/Gallery),[Spinner](https://developer.android.com/reference/android/widget/Spinner), and the more special-purpose[AutoCompleteTextView](https://developer.android.com/reference/android/widget/AutoCompleteTextView),[ImageSwitcher](https://developer.android.com/reference/android/widget/ImageSwitcher), and[TextSwitcher](https://developer.android.com/reference/android/widget/TextSwitcher).

Among the layouts available are[LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout),[FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout),[RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout), and others. For more examples, see[Common layouts](https://developer.android.com/develop/ui/views/layout/declaring-layout#CommonLayouts).

If none of the prebuilt widgets or layouts meet your needs, you can create your own`View`subclass. If you only need to make small adjustments to an existing widget or layout, you can subclass the widget or layout and override its methods.

Creating your own`View`subclasses gives you precise control over the appearance and function of a screen element. To give an idea of the control you get with custom views, here are some examples of what you can do with them:

- You can create a completely custom-rendered`View`type---for example, a "volume control" knob, rendered using 2D graphics, that resembles an analog electronic control.
- You can combine a group of`View`components into a new single component, perhaps to make something like a combo box (a combination of popup list and free entry text field), a dual-pane selector control (a left and right pane with a list in each where you can reassign which item is in which list), and so on.
- You can override the way an`EditText`component is rendered on the screen. The[NotePad](https://android.googlesource.com/platform/development/+/master/samples/NotePad)sample app uses this to good effect to create a lined notepad page.
- You can capture other events---like key presses---and handle them in a custom way, such as for a game.

The following sections explain how to create custom views and use them in your application. For detailed reference information, see the[View](https://developer.android.com/reference/android/view/View)class.

## The basic approach

Here is a high-level overview of what you need to know to create your own`View`components:

1. Extend an existing`View`class or subclass with your own class.
2. Override some of the methods from the superclass. The superclass methods to override start with`on`---for example,[onDraw()](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas)),[onMeasure()](https://developer.android.com/reference/android/view/View#onMeasure(int, int)), and[onKeyDown()](https://developer.android.com/reference/android/view/View#onKeyDown(int, android.view.KeyEvent)). This is similar to the`on`events in[Activity](https://developer.android.com/reference/android/app/Activity)or[ListActivity](https://developer.android.com/reference/android/app/ListActivity)that you override for lifecycle and other functionality hooks.
3. Use your new extension class. Once completed, you can use your new extension class in place of the view it was based on.

| **Tip:** Extension classes can be defined as inner classes inside the activities that use them. This is useful, because it controls access to them, but isn't necessary. For example, perhaps you want to create a new public`View`for wider use in your application.

## Fully customized components

You can create fully customized graphical components that appear however you want. Perhaps you want a graphical VU meter that looks like an old analog gauge, or a sing-along text view where a bouncing ball moves along the words as you sing along with a karaoke machine. You might want something that the built-in components can't do, no matter how you combine them.

Fortunately, you can create components that look and behave any way you want, limited only by your imagination, the size of the screen, and the available processing power, bearing in mind that your application might have to run on something with significantly less power than your desktop workstation.

To create a fully customized component, consider the following:

- The most generic view you can extend is`View`, so you usually start by extending this to create your new super component.
- You can supply a constructor, which can take attributes and parameters from the XML, and you can consume your own such attributes and parameters, such as the color and range of the VU meter or the width and damping of the needle.
- You probably want to create your own event listeners, property accessors, and modifiers as well as more sophisticated behavior in your component class.
- You almost certainly want to override`onMeasure()`and are also likely to need to override`onDraw()`if you want the component to show something. While both have default behavior, the default`onDraw()`does nothing, and the default`onMeasure()`always sets a size of 100x100, which you probably don't want.
- You can also override other`on`methods, as required.

### Extend onDraw() and onMeasure()

The`onDraw()`method delivers a[Canvas](https://developer.android.com/reference/android/graphics/Canvas)on which you can implement anything you want: 2D graphics, other standard or custom components, styled text, or anything else you can think of.
| **Note:** This doesn't apply to 3D graphics. If you want to use 3D graphics, extend[SurfaceView](https://developer.android.com/reference/android/view/SurfaceView)instead of`View`and draw from a separate thread. See the`GLSurfaceViewActivity`sample for details.

`onMeasure()`is a little more involved.`onMeasure()`is a critical piece of the rendering contract between your component and its container.`onMeasure()`must be overridden to efficiently and accurately report the measurements of its contained parts. This is made slightly more complex by the limit requirements from the parent---which are passed into the`onMeasure()`method---and by the requirement to call the`setMeasuredDimension()`method with the measured width and height once they are calculated. If you don't call this method from an overridden`onMeasure()`method, it results in an exception at measurement time.

At a high level, implementing`onMeasure()`looks something like this:

- The overridden`onMeasure()`method is called with width and height specifications, which are treated as requirements for the restrictions on the width and height measurements you produce.`widthMeasureSpec`and`heightMeasureSpec`parameters are both integer codes representing dimensions. A full reference to the kind of restrictions these specifications can require can be found in the reference documentation under[View.onMeasure(int, int)](https://developer.android.com/reference/android/view/View#onMeasure(int, int))This reference documentation also explains the whole measurement operation.
- Your component's`onMeasure()`method calculates a measurement width and height, which are required to render the component. It must try to stay within the specifications passed in, although it can exceed them. In this case, the parent can choose what to do, including clipping, scrolling, throwing an exception, or asking the`onMeasure()`to try again, perhaps with different measurement specifications.
- When the width and height are calculated, call the`setMeasuredDimension(int width, int height)`method with the calculated measurements. Failure to do this results in an exception.

Here's a summary of other standard methods that the framework calls on views:

|     Category     |                                                                       Methods                                                                       |                                                                                                              Description                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Creation         | Constructors                                                                                                                                        | There is a form of the constructor that is called when the view is created from code and a form that is called when the view is inflated from a layout file. The second form parses and applies attributes defined in the layout file. |
| Creation         | [onFinishInflate()](https://developer.android.com/reference/android/view/View#onFinishInflate())                                                    | Called after a view and all of its children are inflated from XML.                                                                                                                                                                     |
| Layout           | [onMeasure(int, int)](https://developer.android.com/reference/android/view/View#onMeasure(int, int))                                                | Called to determine the size requirements for this view and all of its children.                                                                                                                                                       |
| Layout           | [onLayout(boolean, int, int, int, int)](https://developer.android.com/reference/android/view/View#onLayout(boolean, int, int, int, int))            | Called when this view must assign a size and position to all of its children.                                                                                                                                                          |
| Layout           | [onSizeChanged(int, int, int, int)](https://developer.android.com/reference/android/view/View#onSizeChanged(int, int, int, int))                    | Called when the size of this view is changed.                                                                                                                                                                                          |
| Drawing          | [onDraw(Canvas)](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas))                                         | Called when the view must render its content.                                                                                                                                                                                          |
| Event processing | [onKeyDown(int, KeyEvent)](https://developer.android.com/reference/android/view/View#onKeyDown(int, android.view.KeyEvent))                         | Called when a key down event occurs.                                                                                                                                                                                                   |
| Event processing | [onKeyUp(int, KeyEvent)](https://developer.android.com/reference/android/view/View#onKeyUp(int, android.view.KeyEvent))                             | Called when a key up event occurs.                                                                                                                                                                                                     |
| Event processing | [onTrackballEvent(MotionEvent)](https://developer.android.com/reference/android/view/View#onTrackballEvent(android.view.MotionEvent))               | Called when a trackball motion event occurs.                                                                                                                                                                                           |
| Event processing | [onTouchEvent(MotionEvent)](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))                       | Called when a touchscreen motion event occurs.                                                                                                                                                                                         |
| Focus            | [onFocusChanged(boolean, int, Rect)](https://developer.android.com/reference/android/view/View#onFocusChanged(boolean, int, android.graphics.Rect)) | Called when the view gains or loses focus.                                                                                                                                                                                             |
| Focus            | [onWindowFocusChanged(boolean)](https://developer.android.com/reference/android/view/View#onWindowFocusChanged(boolean))                            | Called when the window containing the view gains or loses focus.                                                                                                                                                                       |
| Attaching        | [onAttachedToWindow()](https://developer.android.com/reference/android/view/View#onAttachedToWindow())                                              | Called when the view is attached to a window.                                                                                                                                                                                          |
| Attaching        | [onDetachedFromWindow()](https://developer.android.com/reference/android/view/View#onDetachedFromWindow())                                          | Called when the view is detached from its window.                                                                                                                                                                                      |
| Attaching        | [onWindowVisibilityChanged(int)](https://developer.android.com/reference/android/view/View#onWindowVisibilityChanged(int))                          | Called when the visibility of the window containing the view is changed.                                                                                                                                                               |

## Compound controls

If you don't want to create a completely customized component but instead are looking to put together a reusable component consisting of a group of existing controls, then creating a compound component (or compound control) might be best. In summary, this brings together a number of more atomic controls or views into a logical group of items that can be treated as a single thing. For example, a combo box can be a combination of a single line`EditText`field and an adjacent button with an attached popup list. If the user taps the button and selects something from the list, it populates the`EditText`field, but they can also type something directly into the`EditText`if they prefer.

In Android, there are two other views readily available to do this:`Spinner`and`AutoCompleteTextView`. Regardless, this concept for a combo box makes a good example.

To create a compound component, do the following:

- Just like with an`Activity`, use either the declarative (XML-based) approach to create the contained components or nest them programmatically from your code. The usual starting point is a`Layout`of some kind, so create a class that extends a`Layout`. In the case of a combo box, you might use a`LinearLayout`with horizontal orientation. You can nest other layouts inside, so the compound component can be arbitrarily complex and structured.
- In the constructor for the new class, take whatever parameters the superclass expects and pass them through to the superclass constructor first. Then, you can set up the other views to use within your new component. This is where you create the`EditText`field and the popup list. You might introduce your own attributes and parameters into the XML that your constructor can pull and use.
- Optionally, create listeners for events that your contained views might generate. An example is a listener method for the list item click listener to update the contents of the`EditText`if a list selection is made.
- Optionally, create your own properties with accessors and modifiers. For example, let the`EditText`value be set initially in the component and query for its contents when needed.
- Optionally, override`onDraw()`and`onMeasure()`. This is usually not necessary when extending a`Layout`, since the layout has default behavior that likely works fine.
- Optionally, override other`on`methods, like`onKeyDown()`, for example to choose certain default values from the popup list of a combo box when a certain key is tapped.

There are advantages to using a`Layout`as the basis for a custom control, including the following:

- You can specify the layout using the declarative XML files, just like with an activity screen, or you can create views programmatically and nest them into the layout from your code.
- The`onDraw()`and`onMeasure()`methods, plus most of the other`on`methods, have suitable behavior, so you don't have to override them.
- You can quickly construct arbitrarily complex compound views and re-use them as if they were a single component.

## Modify an existing view type

If there is a component that is similar to what you want, you can extend that component and override the behavior that you want to change. You can do all the things you do with a fully customized component, but by starting with a more specialized class in the`View`hierarchy, you can get some behavior that does what you want for free.

For example, the[NotePad](https://android.googlesource.com/platform/development/+/master/samples/NotePad)sample app demonstrates many aspects of using the Android platform. Among them is extending an`EditText`view to make a lined notepad. This isn't a perfect example, and the APIs for doing this might change, but it demonstrates the principles.

If you haven't done so already, import the NotePad sample into Android Studio or look at the source using the link provided. In particular, see the definition of`LinedEditText`in the[`NoteEditor.java`](https://android.googlesource.com/platform/development/+/master/samples/NotePad/src/com/example/android/notepad/NoteEditor.java)file.

Here are some things to note in this file:

1. **The definition**

   The class is defined with the following line:  
   `public static class LinedEditText extends EditText`

   `LinedEditText`is defined as an inner class within the`NoteEditor`activity, but it is public so that it can be accessed as`NoteEditor.LinedEditText`from outside the`NoteEditor`class.

   Also,`LinedEditText`is`static`, meaning it doesn't generate the so-called "synthetic methods" that let it access data from the parent class. This means it behaves as a separate class rather than something strongly related to`NoteEditor`. This is a cleaner way to create inner classes if they don't need access to state from the outer class. It keeps the generated class small and lets it be used easily from other classes.

   `LinedEditText`extends`EditText`, which is the view to customize in this case. When you finish, the new class can substitute for a normal`EditText`view.
2. **Class initialization**

   As always, the super is called first. This isn't a default constructor, but it is a parameterized one. The`EditText`is created with these parameters when it is inflated from an XML layout file. Thus, the constructor needs to take them and pass them to the superclass constructor as well.
3. **Overridden methods**

   This example overrides only the`onDraw()`method, but you might need to override others as you create your own custom components.

   For this sample, overriding the`onDraw()`method lets you paint the blue lines on the`EditText`view canvas. The canvas is passed into the overridden`onDraw()`method. The`super.onDraw()`method is called before the method ends. The superclass method must be invoked. In this case, invoke it at the end after you paint the lines you want to include.
4. **Custom component**

   You now have your custom component, but how can you use it? In the NotePad example, the custom component is used directly from the declarative layout, so look at`note_editor.xml`in the[`res/layout`](https://android.googlesource.com/platform/development/+/master/samples/NotePad/res/layout)folder:  

   ```xml
   <view xmlns:android="http://schemas.android.com/apk/res/android"
       class="com.example.android.notepad.NoteEditor$LinedEditText"
       android:id="@+id/note"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
       android:background="@android:color/transparent"
       android:padding="5dp"
       android:scrollbars="vertical"
       android:fadingEdge="vertical"
       android:gravity="top"
       android:textSize="22sp"
       android:capitalize="sentences"
   />
   ```

   The custom component is created as a generic view in the XML, and the class is specified using the full package. The inner class you define is referenced using the`NoteEditor$LinedEditText`notation, which is a standard way to refer to inner classes in the Java programming language.

   If your custom view component isn't defined as an inner class, you can declare the view component with the XML element name and exclude the`class`attribute. For example:  

   ```xml
   <com.example.android.notepad.LinedEditText
     id="@+id/note"
     ... />
   ```

   Notice that the`LinedEditText`class is now a separate class file. When the class is nested in the`NoteEditor`class, this technique doesn't work.

   The other attributes and parameters in the definition are the ones passed into the custom component constructor and then passed through to the`EditText`constructor, so they are the same parameters you use for an`EditText`view. It's possible to add your own parameters as well.

Creating custom components is only as complicated as you need it to be.

A more sophisticated component can override even more`on`methods and introduce its own helper methods, substantially customizing its properties and behavior. The only limit is your imagination and what you need the component to do.