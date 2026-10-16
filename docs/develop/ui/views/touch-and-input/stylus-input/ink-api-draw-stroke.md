---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-draw-stroke
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-draw-stroke
source: md.txt
---

In view-based layouts, you need to handle users' touch inputs inside a[`InProgressStrokesView`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView)in addition to[`MotionEventPredictor`](https://developer.android.com/reference/kotlin/androidx/input/motionprediction/MotionEventPredictor).

To achieve optimal drawing performance, use the[`startStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#startStroke(android.view.MotionEvent,kotlin.Int,androidx.ink.brush.Brush,android.graphics.Matrix,android.graphics.Matrix))(),[`addToStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#addToStroke(androidx.ink.strokes.StrokeInputBatch,androidx.ink.authoring.InProgressStrokeId,androidx.ink.strokes.StrokeInputBatch))(), and[`finishStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#finishStroke(android.view.MotionEvent,kotlin.Int,androidx.ink.authoring.InProgressStrokeId))methods of the[`InProgressStrokesView`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView)class, passing[`MotionEvent`](https://developer.android.com/reference/android/view/MotionEvent)objects as input:

1. **Set up UI component**

   For view-based layouts, add[`InProgressStrokesView`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView)to your view hierarchy.  

       <FrameLayout>

         <ScrollView
           android:id="@+id/my_content"
           android:width="match_parent"
           android:height="match_parent"
           >
           <!-- Your content here. -->
         </ScrollView>

         <androidx.ink.authoring.InProgressStrokesView
           android:id="@+id/in_progress_strokes_view"
           android:width="match_parent"
           android:height="match_parent"
           />

       </FrameLayout>

2. **Instantiate`InProgressStrokesView`**

   Within your activity or fragment's[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate%28android.os.Bundle%29)method, get a reference to the[`InProgressStrokesView`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView)and set a touch listener to manage user input.

   Within your activity or fragment's \[`onCreate()`\]\[ink-draw-include6\] method, obtain a reference to the[`InProgressStrokesView`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView)and establish a touch listener for managing user input.  

       class MyActivity : View.OnTouchListener {
           private lateinit var contentView: ScrollView
           private lateinit var inProgressStrokesView: InProgressStrokesView
           private lateinit var predictor: MotionEventPredictor

           // ... other variables

           override fun onCreate(savedInstanceState: Bundle?) {
               super.onCreate(savedInstanceState)
             predictor = MotionEventPredictor.newInstance(contentView)
               contentView = findViewById(R.id.my_content)
               contentView.setOnTouchListener(touchListener)
               inProgressStrokesView = findViewById(R.id.in_progress_strokes_view)
           }

           // ... (touchListener implementation)
       }

   | **Note:** Use[`MotionEventPredictor`](https://developer.android.com/reference/kotlin/androidx/input/motionprediction/MotionEventPredictor)to improve stroke latency by predicting upcoming touch events. Even if your app's`minSdk`is API 34 or higher, you should still use Jetpack's`MotionEventPredictor`instead of the Android SDK's[`MotionPredictor`](https://developer.android.com/reference/android/view/MotionPredictor). The Jetpack implementation automatically uses the system implementation where appropriate.
3. **Handle touch events**

   Having established the UI components, you can initiate drawing based on touch events.

   |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
   | **`MotionEvent`action**                                                                                                                                                                              | **`InProgressStrokesView`method**                                                                                                                                                                                                                 | **Description**                                          |
   | [`ACTION_DOWN`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN)                                                                                                        | [`startStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#startStroke(android.view.MotionEvent,kotlin.Int,androidx.ink.brush.Brush,android.graphics.Matrix,android.graphics.Matrix))          | Begin stroke rendering                                   |
   | [`ACTION_MOVE`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_MOVE)                                                                                                        | [`addToStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#addToStroke(androidx.ink.strokes.StrokeInputBatch,androidx.ink.authoring.InProgressStrokeId,androidx.ink.strokes.StrokeInputBatch)) | Extend the stroke                                        |
   | [`ACTION_UP`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP)                                                                                                            | [`finishStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#finishStroke(android.view.MotionEvent,kotlin.Int,androidx.ink.authoring.InProgressStrokeId))                                       | Finish inputs, prepare to finalize the stroke's geometry |
   | [`ACTION_CANCEL`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_CANCEL)or[`FLAG_CANCELED`](https://developer.android.com/reference/android/view/MotionEvent#FLAG_CANCELED) | [`cancelStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#cancelStroke(androidx.ink.authoring.InProgressStrokeId,android.view.MotionEvent))                                                  | Cancel the stroke                                        |

   **Note:** If your view supports panning, zooming, or rotation, you must provide these transformations to`startStroke`. This ensures newly drawn strokes are recorded in the same world coordinate system as your existing finished strokes. You do this by creating a matrix that represents the transform from the raw`MotionEvent`coordinates back to your world coordinates. It should be the inverse of the transformation you apply to your finished strokes Canvas.  

       class MyActivity : View.OnTouchListener {
         private lateinit var contentView: ScrollView
         private lateinit var inProgressStrokesView: InProgressStrokesView

         private var pointerId = -1
         private var strokeId: InProgressStrokeId? = null
         private lateinit var predictor: MotionEventPredictor

         override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)

           contentView = findViewById(R.id.my_content)
           predictor = MotionEventPredictor.create(contentView)
           contentView.setOnTouchListener(touchListener)
           inProgressStrokesView = findViewById(R.id.in_progress_strokes_view)
         }

         private val touchListener = { view: View, event: MotionEvent ->
           predictor.record(event)
             when (event.actionMasked) {
               MotionEvent.ACTION_DOWN -> {
                 // First pointer - treat it as inking.
                 view.requestUnbufferedDispatch(event)
                 val pointerIndex = event.actionIndex
                 pointerIdToStrokeId[event.getPointerId(pointerIndex)] =
                   inProgressStrokesView.startStroke(event, pointerId)
                 return true
               }
               MotionEvent.ACTION_POINTER_DOWN -> {
                 val stroke = strokeId ?: return false
                 inProgressStrokesView.cancelStroke(stroke, event)
                 strokeId = null
                 pointerId = -1
                 return false
               }
               MotionEvent.ACTION_MOVE -> {
                 val predictedEvent = predictor.predict()
                 try
                 {
                   for (pointerIndex in 0 until pointerCount) {
                     val strokeId =
                     pointerIdToStrokeId[event.getPointerId(pointerIndex)] ?: continue
                     inProgressStrokesView.addToStroke(event, pointerId, strokeId, predictedEvent)
                   } finally {
                     predictedEvent?.recycle()
                   }
                 }
               }
               MotionEvent.ACTION_UP -> {
                 val pointerIndex = event.actionIndex
                 val strokeId =
                   pointerIdToStrokeId[event.getPointerId(pointerIndex)] ?: return false
                 inProgressStrokesView.finishStroke(event, pointerId, strokeId)
                 return true
               }
               MotionEvent.ACTION_CANCEL -> {
                 val pointerIndex = event.actionIndex
                 val strokeId =
                   pointerIdToStrokeId[event.getPointerId(pointerIndex)] ?: return false
                 inProgressStrokesView.cancelStroke(strokeId, event)
                 return true
               }
             }
           return false
         }
       }

4. **Handle finished strokes**

   After[`finishStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#finishStroke(android.view.MotionEvent,kotlin.Int,androidx.ink.authoring.InProgressStrokeId)), the stroke is almost complete. The stroke is fully processed and becomes accessible to your application once there are no other strokes in progress. This ensures all drawing operations are completed before the stroke is handed off to the client.

   To retrieve finished strokes, you have two options:
   - Implement the[`InProgressStrokesFinishedListener`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesFinishedListener)interface within your activity or[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel), and register the listener with the`InProgressStrokesView`by calling[`addFinishedStrokesListener`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView).
   - Call[`InProgressStrokesView.getFinishedStrokes()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#getFinishedStrokes())to get all finished strokes directly.

   <br />

       class MyActivity : ComponentActivity(), InProgressStrokesFinishedListener {
         ...

         private val finishedStrokesState = mutableStateOf(emptySet<Stroke>())

         override fun onCreate(savedInstanceState: Bundle?) {
           ...
           inProgressStrokesView.addFinishedStrokesListener(this)
         }

         // ... (handle touch events)

         @UiThread
         override fun onStrokesFinished(strokes: Map<InProgressStrokeId, Stroke>) {
           finishedStrokesState.value += strokes.values
           inProgressStrokesView.removeFinishedStrokes(strokes.keys)
         }
       }

   Once you have retrieved the finished strokes, you can use[`ViewStrokeRenderer`](https://developer.android.com/reference/androidx/ink/rendering/android/view/ViewStrokeRenderer)to draw them:  

       class DrawingView(context: Context) : View(context) {
         private val viewStrokeRenderer = ViewStrokeRenderer(myCanvasStrokeRenderer, this)

         override fun onDraw(canvas: Canvas) {
           viewStrokeRenderer.drawWithStrokes(canvas) { scope ->
             canvas.scale(myZoomLevel)
             canvas.rotate(myRotation)
             canvas.translate(myPanX, myPanY)
             scope.drawStroke(myStroke)
             // Draw other objects including more strokes, apply more transformations, ...
           }
         }
       }