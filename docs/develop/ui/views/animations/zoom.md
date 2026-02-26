---
title: https://developer.android.com/develop/ui/views/animations/zoom
url: https://developer.android.com/develop/ui/views/animations/zoom
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose. [Shared element transitions →](https://developer.android.com/develop/ui/compose/animation/shared-elements) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

This guide demonstrates how to implement a tap-to-zoom animation. Tap-to-zoom lets apps, such as
photo galleries, animate a view from a thumbnail to fill the screen.

Here's what a tap-to-zoom animation looks like when it expands a thumbnail to fill the
screen:


For a full working example, see the `UIAnimation` class from the
[WearSpeakerSample](https://github.com/android/wear-os-samples/tree/main/WearSpeakerSample)
project on GitHub.

## Create the views

Create a layout file that contains the small and large version of the content you want to zoom.
The following example creates an
`https://developer.android.com/reference/android/widget/ImageButton` for a tappable
image thumbnail and an
`https://developer.android.com/reference/android/widget/ImageView` that displays the
enlarged view of the image:

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/container"
        android:layout_width="match_parent"
        androi>d:layo<ut_height="match_parent"

        LinearLayout android:layout_width="match_parent"
            android:layout_height="wrap_content"
            a>ndroid:ori<entation="vertical"
            android:padding="16dp"

            ImageButton
                android:id="@+id/thumb_button_1"
                android:layout_width="100dp"
                android:layout_height="75dp"
                android:layout_marginRight="1dp"
                android:src="@drawa>ble/th<umb1"
      >      <    android:scaleType=&quot;centerCrop"
                android:contentDescription="@string/description_image_1" /

        /LinearLayout

        !-- This initially hidden ImageView holds the zoomed version of
             the preceding images. Without transformations applied, it fills the entire
             screen. To achieve the zoom an>imatio<n, this view's bounds are animated
             from the bounds of the preceding thumbnail button to its final laid-out
             bounds.
             --

        ImageView
            android:id="@+id/expanded_image"
            android:layout_width="matc>h_<parent">
            android:layout_height="match_parent"
            android:visibility="invisible"
            android:contentDescription="@string/description_zoom_touch_close" /

    /FrameLayout

## Set up the zoom animation

Once you apply your layout, set up the event handlers that trigger the zoom animation. The
following example adds a
`https://developer.android.com/reference/android/view/View.OnClickListener` to
the `ImageButton` to execute the zoom animation when the user taps the image button:

### Kotlin

```kotlin
class ZoomActivity : FragmentActivity() {

    // Hold a reference to the current animator so that it can be canceled
    // midway.
    private var currentAnimator: Animator? = null

    // The system "short" animation time duration in milliseconds. This duration
    // is ideal for subtle animations or animations that occur frequently.
    private var shortAnimationDuration: Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_zoom)

        // Hook up taps on the thumbnail views.

        binding.thumbButton1.setOnClickListener {
            zoomImageFromThumb(thumb1View, R.drawable.image1)
        }

        // Retrieve and cache the system's default "short" animation time.
        shortAnimationDuration = resources.getInteger(android.R.integer.config_shortAnimTime)
    }
    ...
}
```

### Java

```java
public class ZoomActivity extends FragmentActivity {
    // Hold a reference to the current animator so that it can be canceled
    // mid-way.
    private Animator currentAnimator;

    // The system "short" animation time duration in milliseconds. This duration
    // is ideal for subtle animations or animations that occur frequently.
    private int shortAnimationDuration;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_zoom);

        // Hook up taps on the thumbnail views.

        binding.thumbButton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                zoomImageFromThumb(thumb1View, R.drawable.image1);
            }
        });

        // Retrieve and cache the system's default "short" animation time.
        shortAnimationDuration = getResources().getInteger(
                android.R.integer.config_shortAnimTime);
    }
    ...
}
```

## Zoom the view

Animate from the normal-sized view to the zoomed view when appropriate. In general, you need to
animate from the bounds of the normal-sized view to the bounds of the larger-sized view. The
following methods show how to implement a zoom animation that zooms from a thumbnail to an enlarged
view. To do so, assign the high-res image to the hidden "zoomed-in" (enlarged)
`https://developer.android.com/reference/android/widget/ImageView`.

The following example loads a large image resource on the UI thread for simplicity. Load it in a
separate thread to prevent blocking on the UI thread, and then set the bitmap on the UI thread.
Generally, the bitmap must not be larger than the screen size. Next, calculate the starting and
ending bounds for the `ImageView`.

### Kotlin

```kotlin
    private fun zoomImageFromThumb(thumbView: View, imageResId: Int) {
        // If there's an animation in progress, cancel it immediately and
        // proceed with this one.
        currentAnimator?.cancel()

        // Load the high-resolution "zoomed-in" image.
        binding.expandedImage.setImageResource(imageResId)

        // Calculate the starting and ending bounds for the zoomed-in image.
        val startBoundsInt = Rect()
        val finalBoundsInt = Rect()
        val globalOffset = Point()

        // The start bounds are the global visible rectangle of the thumbnail,
        // and the final bounds are the global visible rectangle of the
        // container view. Set the container view's offset as the origin for the
        // bounds, since that's the origin for the positioning animation
        // properties (X, Y).
        thumbView.getGlobalVisibleRect(startBoundsInt)
        binding.container.getGlobalVisibleRect(finalBoundsInt, globalOffset)
        startBoundsInt.offset(-globalOffset.x, -globalOffset.y)
        finalBoundsInt.offset(-globalOffset.x, -globalOffset.y)

        val startBounds = RectF(startBoundsInt)
        val finalBounds = RectF(finalBoundsInt)

        // Using the "center crop" technique, adjust the start bounds to be the
        // same aspect ratio as the final bounds. This prevents unwanted
        // stretching during the animation. Calculate the start scaling factor.
        // The end scaling factor is always 1.0.
        val startScale: Float
        if ((finalBounds>.width() / finalBounds.height()  startBounds.width() / startBounds.height())) {
            // Extend start bounds horizontally.
            startScale = startBounds.height() / finalBounds.height()
            val startWidth: Float = startScale * finalBounds.width()
            val deltaWidth: Float = (startWidth - startBounds.width()) / 2
            startBounds.left -= deltaWidth.toInt()
            startBounds.right += deltaWidth.toInt()
        } else {
            // Extend start bounds vertically.
            startScale = startBounds.width() / finalBounds.width()
            val startHeight: Float = startScale * finalBounds.height()
            val deltaHeight: Float = (startHeight - startBounds.height()) / 2f
            startBounds.top -= deltaHeight.toInt()
            startBounds.bottom += deltaHeight.toInt()
        }

        // Hide the thumbnail and show the zoomed-in view. When the animation
        // begins, it positions the zoomed-in view in the place of the
        // thumbnail.
        thumbView.alpha = 0f

        animateZoomToLargeImage(startBounds, finalBounds, startScale)

        setDismissLargeImageAnimation(thumbView, startBounds, startScale)
    }
```

### Java

```java
    private void zoomImageFromThumb(final View thumbView, int imageResId) {
        // If there's an animation in progress, cancel it immediately and
        // proceed with this one.
        if (currentAnimator != null) {
            currentAnimator.cancel();
        }

        // Load the high-resolution "zoomed-in" image.
        binding.expandedImage.setImageResource(imageResId);

        // Calculate the starting and ending bounds for the zoomed-in image.
        final Rect startBounds = new Rect();
        final Rect finalBounds = new Rect();
        final Point globalOffset = new Point();

        // The start bounds are the global visible rectangle of the thumbnail,
        // and the final bounds are the global visible rectangle of the
        // container view. Set the container view's offset as the origin for the
        // bounds, since that's the origin for the positioning animation
        // properties (X, Y).
        thumbView.getGlobalVisibleRect(startBounds);
        findViewById(R.id.container)
                .getGlobalVisibleRect(finalBounds, globalOffset);
        startBounds.offset(-globalOffset.x, -globalOffset.y);
        finalBounds.offset(-globalOffset.x, -globalOffset.y);

        // Using the "center crop" technique, adjust the start bounds to be the
        // same aspect ratio as the final bounds. This prevents unwanted
        // stretching during the animation. Calculate the start scaling factor.
        // The end scaling factor is always 1.0.
        float startScale;
        if ((float) finalBounds.width() / final>Bounds.height()
                 (float) startBounds.width() / startBounds.height()) {
            // Extend start bounds horizontally.
            startScale = (float) startBounds.height() / finalBounds.height();
            float startWidth = startScale * finalBounds.width();
            float deltaWidth = (startWidth - startBounds.width()) / 2;
            startBounds.left -= deltaWidth;
            startBounds.right += deltaWidth;
        } else {
            // Extend start bounds vertically.
            startScale = (float) startBounds.width() / finalBounds.width();
            float startHeight = startScale * finalBounds.height();
            float deltaHeight = (startHeight - startBounds.height()) / 2;
            startBounds.top -= deltaHeight;
            startBounds.bottom += deltaHeight;
        }

        // Hide the thumbnail and show the zoomed-in view. When the animation
        // begins, it positions the zoomed-in view in the place of the
        // thumbnail.
        thumbView.setAlpha(0f);

        animateZoomToLargeImage(startBounds, finalBounds, startScale);

        setDismissLargeImageAnimation(thumbView, startBounds, startScale);
    }
```

Animate the four positioning and sizing
properties---`https://developer.android.com/reference/android/view/View#X`,
`https://developer.android.com/reference/android/view/View#Y`,
`https://developer.android.com/reference/android/view/View#SCALE_X`,
and
`https://developer.android.com/reference/android/view/View#SCALE_Y`---simultaneously,
from the starting bounds to the ending bounds. Add these four animations to an
`https://developer.android.com/reference/android/animation/AnimatorSet`
so that they start at the same time.

### Kotlin

```kotlin
    private fun animateZoomToLargeImage(startBounds: RectF, finalBounds: RectF, startScale: Float) {
        binding.expandedImage.visibility = View.VISIBLE

        // Set the pivot point for SCALE_X and SCALE_Y transformations to the
        // top-left corner of the zoomed-in view. The default is the center of
        // the view.
        binding.expandedImage.pivotX = 0f
        binding.expandedImage.pivotY = 0f

        // Construct and run the parallel animation of the four translation and
        // scale properties: X, Y, SCALE_X, and SCALE_Y.
        currentAnimator = AnimatorSet().apply {
            play(
                ObjectAnimator.ofFloat(
                    binding.expandedImage,
                    View.X,
                    startBounds.left,
                    finalBounds.left)
            ).apply {
                with(ObjectAnimator.ofFloat(binding.expandedImage, View.Y, startBounds.top, finalBounds.top))
                with(ObjectAnimator.ofFloat(binding.expandedImage, View.SCALE_X, startScale, 1f))
                with(ObjectAnimator.ofFloat(binding.expandedImage, View.SCALE_Y, startScale, 1f))
            }
            duration = shortAnimationDuration.toLong()
            interpolator = DecelerateInterpolator()
            addListener(object : AnimatorListenerAdapter() {

                override fun onAnimationEnd(animation: Animator) {
                    currentAnimator = null
                }

                override fun onAnimationCancel(animation: Animator) {
                    currentAnimator = null
                }
            })
            start()
        }
    }
```

### Java

```java
    private void animateZoomToLargeImage(Rect startBounds, Rect finalBounds, Float startScale) {

        binding.expandedImage.setVisibility(View.VISIBLE);

        // Set the pivot point for SCALE_X and SCALE_Y transformations to the
        // top-left corner of the zoomed-in view. The default is the center of
        // the view.
        binding.expandedImage.setPivotX(0f);
        binding.expandedImage.setPivotY(0f);

        // Construct and run the parallel animation of the four translation and
        // scale properties: X, Y, SCALE_X, and SCALE_Y.
        AnimatorSet set = new AnimatorSet();
        set
                .play(ObjectAnimator.ofFloat(binding.expandedImage, View.X,
                        startBounds.left, finalBounds.left))
                .with(ObjectAnimator.ofFloat(binding.expandedImage, View.Y,
                        startBounds.top, finalBounds.top))
                .with(ObjectAnimator.ofFloat(binding.expandedImage, View.SCALE_X,
                        startScale, 1f))
                .with(ObjectAnimator.ofFloat(binding.expandedImage,
                        View.SCALE_Y, startScale, 1f));
        set.setDuration(shortAnimationDuration);
        set.setInterpolator(new DecelerateInterpolator());
        set.addListener(new AnimatorListenerAdapter() {
            @Override
            public void onAnimationEnd(Animator animation) {
                currentAnimator = null;
            }

            @Override
            public void onAnimationCancel(Animator animation) {
                currentAnimator = null;
            }
        });
        set.start();
        currentAnimator = set;
    }
```

Zoom out by running a similar animation in reverse when the user taps the screen while the image
is zoomed in. Add a `View.OnClickListener` to the `ImageView`. When tapped,
the `ImageView` minimizes to the size of the image thumbnail and sets its visibility to
`https://developer.android.com/reference/android/view/View#GONE` to hide it.

### Kotlin

```kotlin
    private fun setDismissLargeImageAnimation(thumbView: View, startBounds: RectF, startScale: Float) {
        // When the zoomed-in image is tapped, it zooms down to the original
        // bounds and shows the thumbnail instead of the expanded image.
        binding.expandedImage.setOnClickListener {
            currentAnimator?.cancel()

            // Animate the four positioning and sizing properties in parallel,
            // back to their original values.
            currentAnimator = AnimatorSet().apply {
                play(ObjectAnimator.ofFloat(binding.expandedImage, View.X, startBounds.left)).apply {
                    with(ObjectAnimator.ofFloat(binding.expandedImage, View.Y, startBounds.top))
                    with(ObjectAnimator.ofFloat(binding.expandedImage, View.SCALE_X, startScale))
                    with(ObjectAnimator.ofFloat(binding.expandedImage, View.SCALE_Y, startScale))
                }
                duration = shortAnimationDuration.toLong()
                interpolator = DecelerateInterpolator()
                addListener(object : AnimatorListenerAdapter() {

                    override fun onAnimationEnd(animation: Animator) {
                        thumbView.alpha = 1f
                        binding.expandedImage.visibility = View.GONE
                        currentAnimator = null
                    }

                    override fun onAnimationCancel(animation: Animator) {
                        thumbView.alpha = 1f
                        binding.expandedImage.visibility = View.GONE
                        currentAnimator = null
                    }
                })
                start()
            }
        }
    }
```

### Java

```java
    private void setDismissLargeImageAnimation(View thumbView, Rect startBounds, Float startScale) {
        // When the zoomed-in image is tapped, it zooms down to the original
        // bounds and shows the thumbnail instead of the expanded image.
        final float startScaleFinal = startScale;
        binding.expandedImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (currentAnimator != null) {
                    currentAnimator.cancel();
                }

                // Animate the four positioning and sizing properties in
                // parallel, back to their original values.
                AnimatorSet set = new AnimatorSet();
                set.play(ObjectAnimator
                                .ofFloat(binding.expandedImage, View.X, startBounds.left))
                        .with(ObjectAnimator
                                .ofFloat(binding.expandedImage,
                                        View.Y,startBounds.top))
                        .with(ObjectAnimator
                                .ofFloat(binding.expandedImage,
                                        View.SCALE_X, startScaleFinal))
                        .with(ObjectAnimator
                                .ofFloat(binding.expandedImage,
                                        View.SCALE_Y, startScaleFinal));
                set.setDuration(shortAnimationDuration);
                set.setInterpolator(new DecelerateInterpolator());
                set.addListener(new AnimatorListenerAdapter() {
                    @Override
                    public void onAnimationEnd(Animator animation) {
                        thumbView.setAlpha(1f);
                        binding.expandedImage.setVisibility(View.GONE);
                        currentAnimator = null;
                    }

                    @Override
                    public void onAnimationCancel(Animator animation) {
                        thumbView.setAlpha(1f);
                        binding.expandedImage.setVisibility(View.GONE);
                        currentAnimator = null;
                    }
                });
                set.start();
                currentAnimator = set;
            }
        });
    }
```