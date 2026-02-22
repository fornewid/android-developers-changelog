---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors
source: md.txt
---

# Custom text editors are views that are not[`EditText`](https://developer.android.com/reference/kotlin/android/widget/EditText)components or[`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView)text widgets but nevertheless support text input by implementing the[`onCreateInputConnection()`](https://developer.android.com/reference/kotlin/android/view/View#oncreateinputconnection)callback, which is called when a view is focused and the system requests an[`InputConnection`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection)for the view.

A call to[`onCheckIsTextEditor()`](https://developer.android.com/reference/kotlin/android/view/View#oncheckistexteditor)from a custom text editor should return`true`.

## Support stylus handwriting in custom text editors

Android 14 (API level 34) and higher support stylus input in standard Android text entry components by default (see[Stylus input in text fields](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/stylus-input-in-text-fields)). However, custom text entry fields (or editors) require additional development.

To create a custom text editor, do the following:

1. Enable handwriting initiation
2. Declare handwriting support
3. Support handwriting gestures (select, delete, insert, and so on)
4. Provide cursor location and other position data to the IME
5. Show the stylus handwriting hover icon

## Enable handwriting initiation

If a view consists solely of a single text editor, the view system can automatically initiate stylus handwriting for the view. Otherwise, the view must implement its own handwriting initiation logic.

### Automatic handwriting initiation

If a view displays a single text editor and no other content, the view can opt into the view system's automatic handwriting initiation by calling[`setAutoHandwritingEnabled(true)`](https://developer.android.com/reference/kotlin/android/view/View#setautohandwritingenabled).

With auto handwriting enabled, stylus motion starting anywhere within the view's handwriting bounds automatically initiates handwriting mode. The input method editor ([IME](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method)) receives the stylus motion events and commits the recognized text.
![Input field with surrounding rectangle indicating the bounds for detection of stylus motion events.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/shared/edittext_handwriting_bounds.png)**Figure 1.** Handwriting within the bounds of a`EditText`field.

### Custom handwriting initiation

If a view contains multiple text editors or content in addition to a single text editor, the view must implement its own handwriting initiation logic as follows:

1. Opt out of the view system's automatic handwriting initiation by calling[`setAutoHandwritingEnabled(false)`](https://developer.android.com/reference/kotlin/android/view/View#setautohandwritingenabled).

2. Keep track of all text editors that are visible within the view.

3. Monitor motion events received by the view in[`dispatchTouchEvent()`](https://developer.android.com/reference/kotlin/android/view/View#dispatchtouchevent).

   - When stylus motion occurs within a text editor's handwriting bounds, focus the text editor (if not already focused).

   - If the editor was not already focused, restart the editor's IME with new contents by calling[`InputMethodManager#restartInput()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#restartinput).

   - Start the stylus handwriting session by calling[`InputMethodManager#startStylusHandwriting()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#startstylushandwriting).

| **Note:** By default, the handwriting bounds of an`EditText`include 40 dp of vertical padding and 10 dp of horizontal padding (see figure 1). Match these bounds in custom editor views.

If a text editor is inside a scrollable view, stylus movement within the editor's handwriting bounds should be considered handwriting, not scrolling. Use[`ViewParent#requestDisallowInterceptTouchEvent()`](https://developer.android.com/reference/kotlin/android/view/ViewParent#requestdisallowintercepttouchevent)to prevent a scrollable ancestor view from intercepting touch events from a text editor.

### API details

- [**`MotionEvent#getToolType()`**](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gettooltype)--- Indicates whether the`MotionEvent`is from a stylus, in which case the return value is[`TOOL_TYPE_STYLUS`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_stylus)or[`TOOL_TYPE_ERASER`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_eraser).

  | **Note:** When the user presses the eraser button on a stylus and then motions with the stylus, the motion event return type is`TOOL_TYPE_ERASER`. Start handwriting mode and let the IME determine how to recognize the stylus movement.
- [**`InputMethodManager#isStylusHandwritingAvailable()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#isstylushandwritingavailable)--- Indicates whether the IME supports stylus handwriting. Call this method before every call to`InputMethodManager#startStylusHandwriting()`since the handwriting availability may have changed.

- [**`InputMethodManager#startStylusHandwriting()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#startstylushandwriting)--- Causes the IME to enter handwriting mode. An[`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel)motion event is dispatched to the app to cancel the current gesture. Stylus motion events are no longer dispatched to the app.

  Stylus motion events of the current gesture that were already dispatched to the app are forwarded to the IME. The IME is required to show a stylus ink window through which the IME receives all following`MotionEvent`objects. The IME commits recognized handwriting text using the[`InputConnection`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection)APIs.

  If the IME can't enter handwriting mode, this method call is a no-op.
  | **Note:** You can successfully call`startStylusHandwriting()`only when the view argument has focus and an active input connection. The window containing the view must also have focus.

## Declare handwriting support

When filling in the[`EditorInfo`](https://developer.android.com/reference/kotlin/android/view/inputmethod/EditorInfo)argument of[`View#onCreateInputConnection(EditorInfo)`](https://developer.android.com/reference/kotlin/android/view/View#oncreateinputconnection)call[`setStylusHandwritingEnabled()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/EditorInfo#setstylushandwritingenabled)to inform the IME that the text editor supports handwriting. Declare supported gestures with[`setSupportedHandwritingGestures()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/EditorInfo#setsupportedhandwritinggestures)and[`setSupportedHandwritingGesturePreviews()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/EditorInfo#setsupportedhandwritinggesturepreviews).

## Support handwriting gestures

IMEs can support various handwriting gestures, such as circling text to select it or scribbling over text to delete it.
Your browser doesn't support the video tag.**Figure 2.**Circle to select text.Your browser doesn't support the video tag.**Figure 3.**Scribble to delete text.

Custom editors implement[`InputConnection#performHandwritingGesture()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection#performhandwritinggesture)and[`InputConnection#previewHandwritingGesture()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection#previewhandwritinggesture)to support different[`HandwritingGesture`](https://developer.android.com/reference/kotlin/android/view/inputmethod/HandwritingGesture)types, such as[`SelectGesture`](https://developer.android.com/reference/kotlin/android/view/inputmethod/SelectGesture),[`DeleteGesture`](https://developer.android.com/reference/kotlin/android/view/inputmethod/DeleteGesture), and[`InsertGesture`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InsertGesture).

Declare supported handwriting gestures when filling in the`EditorInfo`argument of`View#onCreateInputConnection(EditorInfo)`(see the[Declare handwriting support](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors#declare_handwriting_support)section).

### API details

- [**`InputConnection#performHandwritingGesture(HandwritingGesture, Executor,
  IntConsumer)`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection#performhandwritinggesture)--- Implements gestures. The`HandwritingGesture`argument contains location information which you can use to determine where in the text to perform the gesture. For example,`SelectGesture`provides a[`RectF`](https://developer.android.com/reference/kotlin/android/graphics/RectF)object that specifies the selected text range, and`InsertGesture`provides a[`PointF`](https://developer.android.com/reference/kotlin/android/graphics/PointF)object that specifies the text offset at which to insert text.

  Use the[`Executor`](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor)and[`IntConsumer`](https://developer.android.com/reference/kotlin/java/util/function/IntConsumer)parameters to send back the result of the operation. When both the executor and consumer arguments are provided, use the executor to call[`IntConsumer#accept()`](https://developer.android.com/reference/kotlin/java/util/function/IntConsumer#accept), for example:  


      executor.execute { consumer.accept(HANDWRITING_GESTURE_RESULT_SUCCESS) }

- [**`HandwritingGesture#getFallbackText()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/HandwritingGesture#getfallbacktext)--- Provides fallback text the IME commits at the cursor position if no applicable text is beneath the area of a handwriting gesture.

  Sometimes the IME is not able to determine whether a stylus gesture is intended to perform a gesture operation or to handwrite text. A custom text editor is responsible for determining the user's intention and performing the appropriate action (depending on context) at the gesture location.

  For example, if the IME cannot ascertain whether the user meant to draw a downward caret ⋁ to perform an insert space gesture or to handwrite the letter "v," the IME can send an`InsertGesture`with fallback text "v".

  The editor should first try to perform the insert space gesture. If the gesture cannot be performed (for example, there is no text at the location specified), the editor should fall back to inserting "v" at the cursor position.
- [**`InputConnection#previewHandwritingGesture(PreviewableHandwritingGesture,
  CancellationSignal)`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection#previewhandwritinggesture)--- Previews an ongoing gesture. For example, as the user begins to draw a circle around some text, a live preview of the resulting selection can be shown and continuously updated as the user continues drawing. Only certain gesture types are previewable (see[`PreviewableHandwritingGesture`](https://developer.android.com/reference/kotlin/android/view/inputmethod/PreviewableHandwritingGesture)).

  The`CancellationSignal`parameter can be used by the IME to cancel the preview. If other events disrupt the preview (for example, text is changed programmatically or new`InputConnection`commands occur), the custom editor can cancel the preview.

  Preview gestures are for display only and shouldn't change the editor's state. For example, a`SelectGesture`preview hides the editor's current selection range and highlights the gesture preview range. But once the preview is canceled, the editor should restore its previous selection range.

## Provide cursor location and other position data

In handwriting mode, the IME can request cursor location and other position data using[`InputConnection#requestCursorUpdates()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection#requestcursorupdates). The custom editor responds with a call to[`InputMethodManager#updateCursorAnchorInfo(View,
CursorAnchorInfo)`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#updatecursoranchorinfo). The data in[`CursorAnchorInfo`](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo)relevant to stylus handwriting is provided through the following[`CursorAnchorInfo.Builder`](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo.Builder)methods:

- [**`setInsertionMarkerLocation()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo.Builder#setinsertionmarkerlocation)--- Sets the location of the cursor. The IME uses the value to animate handwriting ink to the cursor location.
- [**`setEditorBoundsInfo()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo.Builder#seteditorboundsinfo)--- Sets the editor's bounds and the handwriting bounds. The IME uses this data to position the IME's handwriting toolbar on screen.
- [**`addVisibleLineBounds()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo.Builder#addvisiblelinebounds)--- Sets the bounds of all visible (or partially visible) text lines of the editor. The IME uses the line bounds to improve accuracy in recognizing handwriting gestures.
- [**`setTextAppearanceInfo()`**](https://developer.android.com/reference/kotlin/android/view/inputmethod/CursorAnchorInfo.Builder#settextappearanceinfo)--- Sets the text appearance with information derived from the text input field. The IME uses the information to style the handwriting ink.

## Show the stylus handwriting hover icon

Display the stylus handwriting hover icon when the stylus hovers over the handwriting bounds of your custom text editor and the selected IME supports stylus handwriting ([`InputMethodManager#isStylusHandwritingAvailable()`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager#isstylushandwritingavailable)).

Override[`View#onResolvePointerIcon()`](https://developer.android.com/reference/kotlin/android/view/View#onresolvepointericon)to get a hover icon for stylus handwriting. In the override, call[`PointerIcon.getSystemIcon(context, PointerIcon.TYPE_HANDWRITING)`](https://developer.android.com/reference/kotlin/android/view/PointerIcon#getsystemicon)to access the system's stylus handwriting hover icon.

## Additional resources

- [Stylus input in text fields](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/stylus-input-in-text-fields)