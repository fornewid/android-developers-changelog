---
title: https://developer.android.com/topic/performance/vitals/render
url: https://developer.android.com/topic/performance/vitals/render
source: md.txt
---

# Slow rendering

UI rendering is the act of generating a frame from your app and displaying it on the screen. To help ensure that a user's interaction with your app is smooth, your app must render frames in under 16ms to achieve 60 frames per second (fps). To understand why 60 fps is preferred, see[Android Performance Patterns: Why 60fps?](https://www.youtube.com/watch?v=CaMTIgxCSqU). If you are trying to achieve 90 fps, then this window drops to 11ms, and for 120 fps it's 8ms.

If you overrun this window by 1ms, it doesn't mean that the frame is displayed 1ms late, but[`Choreographer`](https://developer.android.com/reference/android/view/Choreographer)drops the frame entirely. If your app suffers from slow UI rendering, then the system is forced to skip frames and the user perceives stuttering in your app. This is called*jank*. This page shows how to diagnose and fix jank.

If you are developing games that don't use the[`View`](https://developer.android.com/reference/android/view/View)system, then you bypass`Choreographer`. In this case the[Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing)helps[OpenGL](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)and[Vulkan](https://developer.android.com/ndk/guides/graphics)games achieve smooth rendering and correct frame pacing on Android.

To help improve app quality, Android automatically monitors your app for jank and displays the information in the Android vitals dashboard. For information about how the data is collected, see[Monitor your app's technical quality with Android vitals](https://support.google.com/googleplay/android-developer/answer/7385505).
| **Note:** The Android vitals dashboard and Android system keep track of render time statistics for apps that use the`View`-based UI toolkit, where the user-visible portion of the app is drawn from[`Canvas`](https://developer.android.com/reference/android/graphics/Canvas)or the`View`hierarchy. If your app doesn't use the`View`-based UI toolkit, as is the case for apps that are built with Vulkan,[Unity](https://unity3d.com/),[Unreal](https://www.unrealengine.com), or OpenGL, then render time statistics aren't available in the Android vitals dashboard. To determine if your device is logging render time metrics for your app, run`adb shell dumpsys
| gfxinfo <package name>`.

## Identify jank

Finding the code in your app that is causing jank can be difficult. This section describes three methods for identifying jank:

- [Visual inspection](https://developer.android.com/topic/performance/vitals/render#visual-inspection)
- [Systrace](https://developer.android.com/topic/performance/vitals/render#systrace)
- [Custom performance monitoring](https://developer.android.com/topic/performance/vitals/render#custom-monitoring)

*Visual inspection* lets you run through all the use cases in your app in a few minutes, but it doesn't provide as much detail as Systrace.*Systrace* provides more details, but if you run Systrace for all the use cases in your app, you can be flooded with so much data that can be difficult to analyze. Both visual inspection and Systrace detect jank on your local device. If you can't reproduce jank on local devices, you can build*custom performance monitoring*to measure specific parts of your app on devices running in the field.

### Visual inspection

Visual inspection helps you identify the use cases that are producing jank. To perform a visual inspection, open your app and manually go through the different parts of your app and look for jank in your UI.

Here are some tips for performing visual inspections:

- Run a release---or at least non-debuggable---version of your app. The ART runtime disables several important optimizations to support debugging features, so make sure you're looking at something similar to what a user sees.
- [Enable Profile GPU Rendering](https://developer.android.com/studio/profile/dev-options-rendering#ProfileGPURendering). Profile GPU Rendering displays bars on the screen that give you a visual representation of how much time it takes to render the frames of a UI window relative to the 16-ms-per-frame benchmark. Each bar has colored components that map to a stage in the rendering pipeline, so you can see which portion is taking the longest. For example, if the frame spends a lot of time handling input, look at your app code that handles user input.
- Run through components that are[common sources of jank](https://developer.android.com/topic/performance/vitals/render#common-jank), such as[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView).
- Launch the app from a[cold start](https://developer.android.com/topic/performance/launch-time#cold).
- Run your app on a slower device to exacerbate the problem.

When you find use cases that produce jank, you might have a good idea of what is causing the jank in your app. If you need more information, you can use Systrace to look further into the cause.

### Systrace

Although Systrace is a tool that shows what the entire device is doing, it can be useful for identifying jank in your app. Systrace has minimal system overhead, so you can experience realistic jankiness during instrumentation.

Record a trace with[Systrace](https://developer.android.com/topic/performance/tracing)while performing the janky use case on your device. For instructions on how to use Systrace, see[Capture a system trace on the command line](https://developer.android.com/topic/performance/tracing/command-line). Systrace is split by processes and threads. Look for your app's process in Systrace, which look something like figure 1.
![Systrace example](https://developer.android.com/static/topic/performance/vitals/images/systrace.png)**Figure 1.**Systrace example.

The Systrace example in figure 1 contains the following information for identifying jank:

1. Systrace shows when each frame is drawn and color codes each frame to highlight slow render times. This helps you find individual janky frames more accurately than visual inspection. For more information, see[Inspect UI frames and alerts](https://developer.android.com/topic/performance/tracing/navigate-report#frames-alerts).
2. Systrace detects problems in your app and displays**alerts** both in individual frames and the[alerts](https://developer.android.com/topic/performance/tracing/navigate-report#frames-alerts)panel. It's best to follow the directions in the alert.
3. Parts of the Android framework and libraries, such as`RecyclerView`, contain trace markers. So, the systrace timeline shows when those methods are executed on the UI thread and how long they take to execute.

After you look at the Systrace output, there might be methods in your app that you suspect are causing jank. For example, if the timeline shows that a slow frame is caused by`RecyclerView`taking a long time, you can[add custom trace events](https://developer.android.com/topic/performance/tracing/custom-events)to the relevant code and re-run Systrace for more information. In the new Systrace, the timeline shows when your app's methods are called and how long they take to execute.

If Systrace doesn't show you details about why UI thread work is taking a long time, then use[Android CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler#method_traces)to record either a sampled or instrumented method trace. Generally, method traces aren't good for identifying jank because they produce false-positive janks due to heavy overhead, and they can't see when threads are running versus blocked. But, method traces can help you identify the methods in your app that are taking the most time. After identifying these methods,[add Trace markers](https://developer.android.com/topic/performance/tracing/custom-events)and re-run Systrace to see whether these methods are causing jank.
| **Note:** When recording a Systrace, each trace marker---a begin and end pair that is executed---adds roughly 10µs of overhead. To avoid false-positive janks, don't add trace markers to methods that are called dozens of times in one frame or are shorter than around 200µs.

For more information, see[Understand Systrace](https://source.android.com/devices/tech/debug/systrace).

### Custom performance monitoring

If you can't reproduce jank on a local device, you can build custom performance monitoring into your app to help identify the source of jank on devices in the field.

To do this, collect frame render times from specific parts of your app with[`FrameMetricsAggregator`](https://developer.android.com/reference/androidx/core/app/FrameMetricsAggregator)and record and analyze the data using[Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon/).

To learn more, see[Get started with Performance Monitoring for Android](https://firebase.google.com/docs/perf-mon/get-started-android#pdc).

## Frozen frames

Frozen frames are UI frames that take longer than 700ms to render. This is a problem because your app appears to be stuck and is unresponsive to user input for almost a full second while the frame is rendering. We recommend optimizing apps to render a frame within 16ms to ensure smooth UI. However, during app start up or while transitioning to a different screen, it's normal for the initial frame to take longer than 16ms to draw because your app must inflate views, lay out the screen, and perform the initial draw all from scratch. That's why Android tracks frozen frames separately from slow rendering. No frames in your app should ever take longer than 700ms to render.

To help you improve app quality, Android automatically monitors your app for frozen frames and displays the information in the Android Vitals dashboard. For information on how the data is collected, see[Monitor your app's technical quality with Android vitals](https://support.google.com/googleplay/android-developer/answer/7385505).

Frozen frames are an extreme form of slow rendering, so the procedure for diagnosing and fixing the problem is the same.
| **Note:** The Android Vitals dashboard and Android system keep track of frozen frames for apps that use the UI Toolkit---the user-visible portion of the app is being drawn from[`Canvas`](https://developer.android.com/reference/android/graphics/Canvas)or[`View`](https://developer.android.com/reference/android/view/View)hierarchy. If your app doesn't use the UI Toolkit, as is the case for apps that are built with[Vulkan](https://developer.android.com/ndk/guides/graphics),[Unity](https://unity3d.com/),[Unreal](https://www.unrealengine.com), or[OpenGL](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl), then frozen frames and other render time statistics are not available in the Android Vitals report. To determine if your device is logging render time metrics for your app, run`adb shell dumpsys gfxinfo `<var translate="no">package_name </var>. However, even if that command produces output, it may only cover some of the rendering in your app but not all of it.

## Tracking jank

[FrameTimeline](https://perfetto.dev/docs/data-sources/frametimeline)in[Perfetto](https://perfetto.dev/)can help in tracking slow or frozen frames.

### Relationship between slow frames, frozen frames, and ANRs

Slow frames, frozen frames, and ANRs are all different forms of jank that your app may encounter. See the table below to understand the difference.

|                          |                                             Slow frames                                              |                                        Frozen frames                                        |                                                                                                                                                            ANRs                                                                                                                                                             |
|--------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rendering time           | Between 16ms and 700ms                                                                               | Between 700ms and 5s                                                                        | Greater than 5s                                                                                                                                                                                                                                                                                                             |
| Visible user impact area | - `RecyclerView`scroll behaving abruptly - On screens with complex animations not animating properly | - During app startup - Moving from one screen to anothe---for example, screen transitioning | - While your activity is in the foreground, your app has not responded to an input event or`BroadcastReceiver`---such as key press or screen tap events---within five seconds. - While you don't have an activity in the foreground, your`BroadcastReceiver`hasn't finished executing within a considerable amount of time. |

### Track slow frames and frozen frames separately

During app start up or while transitioning to a different screen, it's normal for the initial frame to take longer than 16ms to draw because the app must inflate views, lay out the screen, and perform the initial draw from scratch.

#### Best practices for prioritizing and resolving jank

Keep the following best practices in mind when looking to resolve jank in your app:

- Identify and resolve the most easily reproducible instances of jank.
- Prioritize ANRs. While slow or frozen frames might make an app appear sluggish, ANRs cause the app to stop responding.
- Slow rendering is hard to reproduce, but you can start by killing 700ms frozen frames. This is most common while the app is starting up or changing screens.

## Fixing jank

To fix jank, inspect which frames aren't completing in 16ms and look for what's wrong. Check whether`Record View#draw`or`Layout`is taking abnormally long in some frames. See[Common sources of jank](https://developer.android.com/topic/performance/vitals/render#common-jank)for these problems and others.

To avoid jank, run long-running tasks asynchronously outside of the UI thread. Always be aware of what thread your code is running on and use caution when posting non-trivial tasks to the main thread.

If you have a complex and important primary UI for your app---such as the central scrolling list---consider[writing instrumentation tests](https://developer.android.com/training/testing/performance#automate)that can automatically detect slow render times and run the tests frequently to prevent regressions.

## Common sources of jank

The following sections explain common sources of jank in apps using the`View`system and best practices for addressing them. For information on fixing performance issues with[Jetpack Compose](https://developer.android.com/jetpack/compose), see[Jetpack Compose performance](https://developer.android.com/jetpack/compose/performance).

### Scrollable lists

[`ListView`](https://developer.android.com/reference/android/widget/ListView)---and especially`RecyclerView`---are commonly used for complex scrolling lists that are most susceptible to jank. They both contain Systrace markers, so you can use Systrace to see whether they are contributing to jank in your app. Pass the command-line argument`-a
<your-package-name>`to get trace sections in`RecyclerView`---as well as any trace markers you added---to show up. If available, follow the guidance of the alerts generated in the Systrace output. Inside Systrace, you can click`RecyclerView`-traced sections to see an explanation of the work`RecyclerView`is doing.

#### RecyclerView: notifyDataSetChanged()

If you see every item in your`RecyclerView`being rebound---and thus re-laid out and re-drawn in one frame---make sure you're*not* calling[`notifyDataSetChanged()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#notifyDataSetChanged()),[`setAdapter(Adapter)`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView#setAdapter(androidx.recyclerview.widget.RecyclerView.Adapter)), or[`swapAdapter(Adapter,
boolean)`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView#swapAdapter(androidx.recyclerview.widget.RecyclerView.Adapter,boolean))for small updates. These methods signal that there are changes to the entire list content and show up in Systrace as**RV FullInvalidate** . Instead, use[`SortedList`](https://developer.android.com/reference/androidx/recyclerview/widget/SortedList)or[`DiffUtil`](https://developer.android.com/reference/androidx/recyclerview/widget/DiffUtil)to generate minimal updates when content is changed or added.

For example, consider an app that receives a new version of a list of news content from a server. When you post this information to the Adapter, it's possible to call`notifyDataSetChanged()`, as shown in the following example:  

### Kotlin

```kotlin
fun onNewDataArrived(news: List<News>) {
    myAdapter.news = news
    myAdapter.notifyDataSetChanged()
}
```

### Java

```java
void onNewDataArrived(List<News> news) {
    myAdapter.setNews(news);
    myAdapter.notifyDataSetChanged();
}
```

The downside to this is if there is a trivial change, such as a single item added to the top, the`RecyclerView`isn't aware. Therefore, it is told to drop its entire cached item state and thus needs to rebind everything.

We recommend you use`DiffUtil`, which calculates and dispatches minimal updates for you:  

### Kotlin

```kotlin
fun onNewDataArrived(news: List<News>) {
    val oldNews = myAdapter.items
    val result = DiffUtil.calculateDiff(MyCallback(oldNews, news))
    myAdapter.news = news
    result.dispatchUpdatesTo(myAdapter)
}
```

### Java

```java
void onNewDataArrived(List<News> news) {
    List<News> oldNews = myAdapter.getItems();
    DiffResult result = DiffUtil.calculateDiff(new MyCallback(oldNews, news));
    myAdapter.setNews(news);
    result.dispatchUpdatesTo(myAdapter);
}
```

To inform`DiffUtil`how to inspect your lists, define your`MyCallback`as a[`Callback`](https://developer.android.com/reference/androidx/recyclerview/widget/DiffUtil.Callback)implementation.

#### RecyclerView: Nested RecyclerViews

It's common to nest multiple instances of`RecyclerView`, especially with a vertical list of horizontally scrolling lists. An example of this is the grids of apps on the Play Store main page. This can work great, but it's also a lot of views moving around.

If you see a lot of inner items inflating when you first scroll down the page, you might want to check that you're sharing[`RecyclerView.RecycledViewPool`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.RecycledViewPool)between inner (horizontal) instances of`RecyclerView`. By default, each`RecyclerView`has its own pool of items. However, in the case with a dozen`itemViews`on screen at the same time, it's problematic when`itemViews`can't be shared by the different horizontal lists if all the rows are showing similar types of views.  

### Kotlin

```kotlin
class OuterAdapter : RecyclerView.Adapter<OuterAdapter.ViewHolder>() {

    ...

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        // Inflate inner item, find innerRecyclerView by ID.
        val innerLLM = LinearLayoutManager(parent.context, LinearLayoutManager.HORIZONTAL, false)
        innerRv.apply {
            layoutManager = innerLLM
            recycledViewPool = sharedPool
        }
        return OuterAdapter.ViewHolder(innerRv)
    }
    ...
```

### Java

```java
class OuterAdapter extends RecyclerView.Adapter<OuterAdapter.ViewHolder> {
    RecyclerView.RecycledViewPool sharedPool = new RecyclerView.RecycledViewPool();

    ...

    @Override
    public void onCreateViewHolder(ViewGroup parent, int viewType) {
        // Inflate inner item, find innerRecyclerView by ID.
        LinearLayoutManager innerLLM = new LinearLayoutManager(parent.getContext(),
                LinearLayoutManager.HORIZONTAL);
        innerRv.setLayoutManager(innerLLM);
        innerRv.setRecycledViewPool(sharedPool);
        return new OuterAdapter.ViewHolder(innerRv);

    }
    ...
```

If you want to optimize further, you can also call[`setInitialPrefetchItemCount(int)`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager#setInitialPrefetchItemCount(int))on the[`LinearLayoutManager`](https://developer.android.com/reference/androidx/recyclerview/widget/LinearLayoutManager)of the inner`RecyclerView`. If, for example, you always have 3.5 items visible in a row, call`innerLLM.setInitialItemPrefetchCount(4)`. This signals to the`RecyclerView`that when a horizontal row is about to come on screen, it must attempt to prefetch the items inside if there's spare time on the UI thread.

#### RecyclerView: Too much inflation or Create is taking too long

In most cases, the prefetch feature in`RecyclerView`can help work around the cost of inflation by doing the work ahead of time while the UI thread is idle. If you're seeing inflation during a frame and not in a section labeled**RV Prefetch** , be sure you're testing on a supported device and using a recent version of the[Support Library](https://developer.android.com/topic/libraries/support-library). Prefetch is only supported on Android 5.0 API Level 21 and later.

If you frequently see inflation causing jank as new items come on screen, verify that you don't have more view types than you need. The fewer the view types in the content of a`RecyclerView`, the less inflation needs to be done when new item types come on screen. If possible, merge view types where reasonable. If only an icon, color, or piece of text changes between types, you can make that change at bind time and avoid inflation, which reduces your app's memory footprint at the same time.

If your view types look good, look at reducing the cost of your inflation. Reducing unnecessary container and structural views can help. Consider building`itemViews`with[`ConstraintLayout`](https://developer.android.com/training/constraint-layout), which can help reduce structural views.

If you want to further optimize for performance, and your items hierarchies are simple and you don't need complex theming and style features, consider calling the constructors yourself. However, it's often not worth the tradeoff of losing the simplicity and features of XML.

#### RecyclerView: Bind taking too long

Bind---that is,[`onBindViewHolder(VH,
int)`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onBindViewHolder(VH,%0Aint))--- must be straightforward and take much less than one millisecond for everything but the most complex items. It must take plain old Java object (POJO) items from your adapter's internal item data and call setters on views inthe`ViewHolder`. If**RV OnBindView**is taking a long time, verify that you're doing minimal work in your bind code.

If you're using basic POJO objects to hold data in your adapter, you can completely avoid writing the binding code in`onBindViewHolder`by using the[Data Binding Library](https://developer.android.com/topic/libraries/data-binding).

#### RecyclerView or ListView: Layout or draw taking too long

For issues with draw and layout, see the[Layout performance](https://developer.android.com/topic/performance/vitals/render#layout)and[Rendering performance](https://developer.android.com/topic/performance/vitals/render#render)sections.

#### ListView: Inflation

You can accidentally disable recycling in`ListView`if you aren't careful. If you see inflation every time an item comes on screen, check that your implementation of[`Adapter.getView()`](https://developer.android.com/reference/android/widget/Adapter#getView(int,%20android.view.View,%20android.view.ViewGroup))is musing, re-binding, and returning the`convertView`parameter. If your`getView()`implementation always inflates, your app doesn't get the benefits of recycling in`ListView`. The structure of your`getView()`must almost always be similar to the following implementation:  

### Kotlin

```kotlin
fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
    return (convertView ?: layoutInflater.inflate(R.layout.my_layout, parent, false)).apply {
        // Bind content from position to convertView.
    }
}
```

### Java

```java
View getView(int position, View convertView, ViewGroup parent) {

    if (convertView == null) {
        // Only inflate if no convertView passed.
        convertView = layoutInflater.inflate(R.layout.my_layout, parent, false)
    }
    // Bind content from position to convertView.
    return convertView;
}
```

### Layout performance

If Systrace shows that the**Layout** segment of`Choreographer#doFrame`is working too much or working too often, this means you're hitting layout performance issues. The layout performance of your app depends on what portion of the view hierarchy has changing layout parameters or inputs.

#### Layout performance: Cost

If the segments are longer than a few milliseconds, it's possible that you're hitting worst-case nesting performance for[`RelativeLayouts`](https://developer.android.com/guide/topics/ui/layout/relative), or[`weighted-LinearLayouts`](https://developer.android.com/guide/topics/ui/layout/linear#Weight). Each of these layouts can trigger multiple measure and layout passes of its children, so nesting them can lead to`O(n^2)`behavior on the depth of nesting.

Try avoiding`RelativeLayout`or the weight feature of`LinearLayout`in all but the lowest leaf nodes of the hierarchy. The following are ways you can do this:

- Reorganize your structural views.
- Define custom layout logic. See[Optimize layout hierarchies](https://developer.android.com/develop/ui/views/layout/improving-layouts/optimizing-layouts)for a specific example. You can try converting to[`ConstraintLayout`](https://developer.android.com/training/constraint-layout), which provides similar features, without the performance drawbacks.

#### Layout performance: Frequency

Layout is expected to happen when new content comes on screen, for example when a new item scrolls into view in`RecyclerView`. If significant layout is happening on each frame, it's possible that you're animating layout, which is likely to cause dropped frames.

Generally, animations must run on drawing properties of`View`, such as the following:

- [`setTranslationX()`](https://developer.android.com/reference/android/view/View#setTranslationX(float))
- [`setTranslationY()`](https://developer.android.com/reference/android/view/View#setTranslationY(float))
- [`setTranslationZ()`](https://developer.android.com/reference/android/view/View#setTranslationZ(float))
- [`setRotation()`](https://developer.android.com/reference/android/view/View#setRotation(float))
- [`setAlpha()`](https://developer.android.com/reference/android/view/View#setAlpha(float))

You can change all of these much more cheaply than layout properties, such as padding, or margins. Generally, it's also much cheaper to change drawing properties of a view by calling a setter which triggers an[`invalidate()`](https://developer.android.com/reference/android/view/View#invalidate()), followed by[`draw(Canvas)`](https://developer.android.com/reference/android/view/View#draw(android.graphics.Canvas))in the next frame. This re-records drawing operations for the view that is invalidated and is also generally much cheaper than layout.

### Rendering performance

Android UI works in two phases:

- **Record View#draw** on the UI thread, which runs`draw(Canvas)`on every invalidated view, and can invoke calls into custom views or into your code.
- **DrawFrame** on the`RenderThread`, which runs on the native`RenderThread`but operates based on work generated by the**Record View#draw**phase.

#### Rendering performance: UI Thread

If**Record View#draw** is taking a long time, it's common that a bitmap is being painted on the UI thread. Painting to a bitmap uses CPU rendering, so generally avoid this when possible. You can use method tracing with the[Android CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler#method_traces)to see if this is the problem.

Painting to a bitmap is often done when an app wants to decorate a bitmap before displaying it---sometimes a decoration like adding rounded corners:  

### Kotlin

```kotlin
val paint = Paint().apply {
    isAntiAlias = true
}
Canvas(roundedOutputBitmap).apply {
    // Draw a round rect to define the shape:
    drawRoundRect(
            0f,
            0f,
            roundedOutputBitmap.width.toFloat(),
            roundedOutputBitmap.height.toFloat(),
            20f,
            20f,
            paint
    )
    paint.xfermode = PorterDuffXfermode(PorterDuff.Mode.MULTIPLY)
    // Multiply content on top to make it rounded.
    drawBitmap(sourceBitmap, 0f, 0f, paint)
    setBitmap(null)
    // Now roundedOutputBitmap has sourceBitmap inside, but as a circle.
}
```

### Java

```java
Canvas bitmapCanvas = new Canvas(roundedOutputBitmap);
Paint paint = new Paint();
paint.setAntiAlias(true);
// Draw a round rect to define the shape:
bitmapCanvas.drawRoundRect(0, 0,
        roundedOutputBitmap.getWidth(), roundedOutputBitmap.getHeight(), 20, 20, paint);
paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.MULTIPLY));
// Multiply content on top to make it rounded.
bitmapCanvas.drawBitmap(sourceBitmap, 0, 0, paint);
bitmapCanvas.setBitmap(null);
// Now roundedOutputBitmap has sourceBitmap inside, but as a circle.
```

If this is the sort of work you're doing on the UI thread, you can instead do this on the decoding thread in the background. In some cases, like the preceding example, you can even do the work at draw time. So, if your[`Drawable`](https://developer.android.com/reference/android/graphics/drawable/Drawable)or[`View`](https://developer.android.com/reference/android/view/View)code looks something like this:  

### Kotlin

```kotlin
fun setBitmap(bitmap: Bitmap) {
    mBitmap = bitmap
    invalidate()
}

override fun onDraw(canvas: Canvas) {
    canvas.drawBitmap(mBitmap, null, paint)
}
```

### Java

```java
void setBitmap(Bitmap bitmap) {
    mBitmap = bitmap;
    invalidate();
}

void onDraw(Canvas canvas) {
    canvas.drawBitmap(mBitmap, null, paint);
}
```

You can replace it with this:  

### Kotlin

```kotlin
fun setBitmap(bitmap: Bitmap) {
    shaderPaint.shader = BitmapShader(bitmap, Shader.TileMode.CLAMP, Shader.TileMode.CLAMP)
    invalidate()
}

override fun onDraw(canvas: Canvas) {
    canvas.drawRoundRect(0f, 0f, width, height, 20f, 20f, shaderPaint)
}
```

### Java

```java
void setBitmap(Bitmap bitmap) {
    shaderPaint.setShader(
            new BitmapShader(bitmap, TileMode.CLAMP, TileMode.CLAMP));
    invalidate();
}

void onDraw(Canvas canvas) {
    canvas.drawRoundRect(0, 0, width, height, 20, 20, shaderPaint);
}
```

You can also do this for background protection, such as when drawing a gradient on top of the bitmap, and image filtering with[`ColorMatrixColorFilter`](https://developer.android.com/reference/android/graphics/ColorMatrixColorFilter)---two other common operations done modifying bitmaps.

If you're drawing to a bitmap for another reason---possibly using it as a cache---try to draw to the hardware-accelerated`Canvas`passed to your`View`or`Drawable`directly. If necessary, also consider calling[`setLayerType()`](https://developer.android.com/reference/android/view/View#setLayerType(int,%20android.graphics.Paint))with[`LAYER_TYPE_HARDWARE`](https://developer.android.com/reference/android/view/View#LAYER_TYPE_HARDWARE)to cache complex rendering output and still take advantage of GPU rendering.

#### Rendering performance: RenderThread

Some`Canvas`operations are cheap to record but trigger expensive computation on the`RenderThread`. Systrace generally calls these out with alerts.

##### Animating large Paths

When[`Canvas.drawPath()`](https://developer.android.com/reference/android/graphics/Canvas#drawPath(android.graphics.Path,%0Aandroid.graphics.Paint))is called on the hardware-accelerated`Canvas`passed to`View`, Android draws these paths first on CPU and uploads them to the GPU. If you have large paths, avoid editing them from frame to frame, so that they can be cached and drawn efficiently.[`drawPoints()`](https://developer.android.com/reference/android/graphics/Canvas#drawPoints(float%5B%5D,%20android.graphics.Paint)),`drawLines()`, and`drawRect/Circle/Oval/RoundRect()`are more efficient and better to use even if you use more draw calls.

##### Canvas.clipPath

[`clipPath(Path)`](https://developer.android.com/reference/android/graphics/Canvas#clipPath(android.graphics.Path))triggers expensive clipping behavior, and must generally be avoided. When possible, opt for drawing shapes instead of clipping to non-rectangles. It performs better and supports anti-aliasing. For example, the following`clipPath`call can be expressed differently:  

### Kotlin

```kotlin
canvas.apply {
    save()
    clipPath(circlePath)
    drawBitmap(bitmap, 0f, 0f, paint)
    restore()
}
```

### Java

```java
canvas.save();
canvas.clipPath(circlePath);
canvas.drawBitmap(bitmap, 0f, 0f, paint);
canvas.restore();
```

Instead, express the preceding example as follows:  

### Kotlin

```kotlin
paint.shader = BitmapShader(bitmap, Shader.TileMode.CLAMP, Shader.TileMode.CLAMP)
// At draw time:
canvas.drawPath(circlePath, mPaint)
```

### Java

```java
// One time init:
paint.setShader(new BitmapShader(bitmap, TileMode.CLAMP, TileMode.CLAMP));
// At draw time:
canvas.drawPath(circlePath, mPaint);
```

##### Bitmap uploads

Android displays bitmaps as OpenGL textures, and the first time a bitmap is displayed in a frame, it's uploaded to the GPU. You can see this in Systrace as**Texture upload(id) width x height**. This can take several milliseconds, as shown in figure 2, but it's necessary to display the image with the GPU.

If these are taking a long time, first check the width and height numbers in the trace. Ensure that the bitmap being displayed isn't significantly bigger than the area on screen it's showing in. If it is, this wastes upload time and memory. Generally, bitmap loading libraries provide a means of requesting an appropriately sized bitmap.

In Android 7.0, bitmap loading code---generally done by libraries---can call[`prepareToDraw()`](https://developer.android.com/reference/android/graphics/Bitmap#prepareToDraw())to trigger an early upload before it's needed. This way, the upload happens early while the`RenderThread`is idle. You can do this after decoding or when binding a bitmap to a view, as long as you know the bitmap. Ideally, your bitmap loading library does this for you, but if you're managing your own or want to ensure you don't hit uploads on newer devices, you can call`prepareToDraw()`in your own code.
![An app spends significant time in a frame uploading a large bitmap](https://developer.android.com/static/topic/performance/vitals/images/texture-upload.png)**Figure 2.** An app spends significant time in a frame uploading a large bitmap. Either reduce its size or trigger it early when you decode it with`prepareToDraw()`.

### Thread scheduling delays

The thread scheduler is the part of the Android operating system in charge of deciding which threads in the system must run, when they run, and for how long.

Sometimes, jank occurs because your app's UI Thread is blocked or not running. Systrace uses different colors, as shown in figure 3, to indicate when a thread is*sleeping* (gray),*runnable* (blue: it can run, but isn't picked by the scheduler to run yet),*actively running* (green), or in*uninterruptible sleep*(red or orange). This is extremely useful for debugging jank issues that are caused by thread scheduling delays.
| **Note:** Earlier versions of Android have more frequent scheduling problems that aren't the app's fault. This area is continuously improved, so consider debugging thread scheduling issues more on later OS versions, where descheduled threads are more likely to be caused by the app.
![Highlights a period when the UI thread is sleeping](https://developer.android.com/static/topic/performance/vitals/images/thread-sleep.png)**Figure 3.**Highlight of a period when the UI thread is sleeping.**Note:** There are parts of a frame when the UI thread or`RenderThread`aren't expected to run. For example, the UI thread is blocked while the`syncFrameState`of the`RenderThread`is running and bitmaps are uploaded. This is so the`RenderThread`can safely copy data used by the UI thread. Another example, the`RenderThread`can be blocked when it uses IPC to acquire a buffer at the beginning of a frame, query information from it, or pass the buffer back to the compositor with`eglSwapBuffers`.

Often, binder calls---the inter-process communication (IPC) mechanism on Android---cause long pauses in your app's execution. On later versions of Android, it's one of the most common reasons for the UI thread to stop running. Generally, the fix is to avoid calling functions that make binder calls. If it's unavoidable, cache the value or move work to background threads. As codebases get larger, you can accidentally add a binder call by invoking some low-level method if you aren't careful. However, you can find and fix them with tracing.

If you have binder transactions, you can capture their call stacks with the following[`adb`](https://developer.android.com/studio/command-line/adb)commands:  

    $ adb shell am trace-ipc start
    ... use the app - scroll/animate ...
    $ adb shell am trace-ipc stop --dump-file /data/local/tmp/ipc-trace.txt
    $ adb pull /data/local/tmp/ipc-trace.txt

Sometimes calls that seem innocuous, like[`getRefreshRate()`](https://developer.android.com/reference/android/view/Display#getRefreshRate()), can trigger binder transactions and cause big problems when they're called frequently. Tracing periodically can help you find and fix these issues as they show up.
![Shows the UI thread sleeping due to binder transactions in a RV fling. Keep your bind logic focused, and use trace-ipc to track down and remove binder calls.](https://developer.android.com/static/topic/performance/vitals/images/rv-fling.png)**Figure 4.** The UI thread is sleeping due to binder transactions in a RV fling. Keep your bind logic simple and use`trace-ipc`to track down and remove binder calls.

If you aren't seeing binder activity but still aren't seeing your UI thread run, be sure you're not waiting on a lock or other operation from another thread. Typically, the UI thread doesn't have to wait on results from other threads. Other threads must post information to it.

### Object allocation and garbage collection

Object allocation and garbage collection (GC) are significantly less of an issue since ART was introduced as the default runtime in Android 5.0, but it's still possible to weigh down your threads with this extra work. It's fine to allocate in response to a rare event that doesn't happen many times per second---like a user tapping a button---but remember that each allocation comes with a cost. If it's in a tight loop that's called frequently, consider avoiding the allocation to lighten the load on the GC.

Systrace shows you if GC is running frequently, and the[Android Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)can show you where allocations are coming from. If you avoid allocations when possible, especially in tight loops, you're less likely to have problems.
![Shows a 94ms GC on the HeapTaskDaemon](https://developer.android.com/static/topic/performance/vitals/images/gc.png)**Figure 5.**A 94ms GC on the HeapTaskDaemon thread.

On recent versions of Android, GC generally runs on a background thread named**HeapTaskDaemon**. Significant amounts of allocation can mean more CPU resources spent on GC, as shown in figure 5.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Benchmark your app](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)
- [Best practices for app optimization](https://developer.android.com/topic/performance/appstartup/best-practices)