---
title: https://developer.android.com/develop/ui/views/animations/reveal-or-hide-view
url: https://developer.android.com/develop/ui/views/animations/reveal-or-hide-view
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.  
[Crossfade →](https://developer.android.com/jetpack/compose/animation/composables-modifiers#crossfade)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

While your app is being used, new information appears on the screen and old
information is removed. Changing what shows on the screen immediately can be
jarring, and users can miss new content that appears suddenly. Animations slow
down the changes and draw the user's eye with motion so that the updates are
more obvious.
| **Note:** [Jetpack Compose](https://developer.android.com/jetpack/compose) is the preferred way to build Android apps. See the Compose [Animations](https://developer.android.com/jetpack/compose/animation) documentation.

There are three common animations you can use to show or hide a view: reveal
animations, crossfade animations, and cardflip animations.

## Create a crossfade animation

A crossfade animation---also known as a *dissolve* ---gradually fades out
one [`View`](https://developer.android.com/reference/android/view/View) or
[`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup) while simultaneously
fading in another. This animation is useful for situations where you want to
switch content or views in your app. The crossfade animation shown here uses
[`ViewPropertyAnimator`](https://developer.android.com/reference/android/view/ViewPropertyAnimator),
which is available for Android 3.1 (API level 12) and higher.

Here's an example of a crossfade from a progress indicator to text content:  
**Figure 1.** Crossfade animation.

### Create the views

Create the two views that you want to crossfade. The following example creates a
progress indicator and a scrollable text view:  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
            android:id="@+id/content"
            android:layout_width="match_parent"
            android:layout_height="match_parent">

            <TextView style="?android:textAppearanceMedium"
                android:lineSpacingMultiplier="1.2"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="@string/lorem_ipsum"
                android:padding="16dp" />

        </ScrollView>

        <ProgressBar android:id="@+id/loading_spinner"
            style="?android:progressBarStyleLarge"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center" />

    </FrameLayout>

### Set up the crossfade animation

To set up the crossfade animation, do the following:

1. Create member variables for the views that you want to crossfade. You need these references later when modifying the views during the animation.
2. Set the visibility of the view that is being faded in to [`GONE`](https://developer.android.com/reference/android/view/View#GONE). This prevents the view from using layout space and omits it from layout calculations, which speeds up processing
3. Cache the [`config_shortAnimTime`](https://developer.android.com/reference/android/R.integer#config_shortAnimTime) system property in a member variable. This property defines a standard "short" duration for the animation. This duration is ideal for subtle animations or animations that occur frequently. [`config_longAnimTime`](https://developer.android.com/reference/android/R.integer#config_longAnimTime) and [`config_mediumAnimTime`](https://developer.android.com/reference/android/R.integer#config_mediumAnimTime) are also available.

Here's an example using the layout from the previous code snippet as the
activity content view:  

### Kotlin

```kotlin
class CrossfadeActivity : Activity() {

    private lateinit var contentView: View
    private lateinit var loadingView: View
    private var shortAnimationDuration: Int = 0
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_crossfade)

        contentView = findViewById(R.id.content)
        loadingView = findViewById(R.id.loading_spinner)

        // Initially hide the content view.
        contentView.visibility = View.GONE

        // Retrieve and cache the system's default "short" animation time.
        shortAnimationDuration = resources.getInteger(android.R.integer.config_shortAnimTime)
    }
    ...
}
```

### Java

```java
public class CrossfadeActivity extends Activity {

    private View contentView;
    private View loadingView;
    private int shortAnimationDuration;
    ...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_crossfade);

        contentView = findViewById(R.id.content);
        loadingView = findViewById(R.id.loading_spinner);

        // Initially hide the content view.
        contentView.setVisibility(View.GONE);

        // Retrieve and cache the system's default "short" animation time.
        shortAnimationDuration = getResources().getInteger(
                android.R.integer.config_shortAnimTime);
    }
    ...
}
```

### Crossfade the views

When the views are properly set up, crossfade them by doing the following:

1. For the view that is fading in, set the alpha value to 0 and the visibility to [`VISIBLE`](https://developer.android.com/reference/android/view/View#VISIBLE) from its initial setting of `GONE`. This makes the view visible but transparent.
2. For the view that is fading in, animate its alpha value from 0 to 1. For the view that is fading out, animate the alpha value from 1 to 0.
3. Using [`onAnimationEnd()`](https://developer.android.com/reference/android/animation/Animator.AnimatorListener#onAnimationEnd(android.animation.Animator)) in an [`Animator.AnimatorListener`](https://developer.android.com/reference/android/animation/Animator.AnimatorListener), set the visibility of the view that is fading out to `GONE`. Even though the alpha value is 0, setting the view's visibility to `GONE` prevents the view from using layout space and omits it from layout calculations, which speeds up processing.

The following method shows an example of how to do this:  

### Kotlin

```kotlin
class CrossfadeActivity : Activity() {

    private lateinit var contentView: View
    private lateinit var loadingView: View
    private var shortAnimationDuration: Int = 0
    ...
    private fun crossfade() {
        contentView.apply {
            // Set the content view to 0% opacity but visible, so that it is
            // visible but fully transparent during the animation.
            alpha = 0f
            visibility = View.VISIBLE

            // Animate the content view to 100% opacity and clear any animation
            // listener set on the view.
            animate()
                    .alpha(1f)
                    .setDuration(shortAnimationDuration.toLong())
                    .setListener(null)
        }
        // Animate the loading view to 0% opacity. After the animation ends,
        // set its visibility to GONE as an optimization step so it doesn't
        // participate in layout passes.
        loadingView.animate()
                .alpha(0f)
                .setDuration(shortAnimationDuration.toLong())
                .setListener(object : AnimatorListenerAdapter() {
                    override fun onAnimationEnd(animation: Animator) {
                        loadingView.visibility = View.GONE
                    }
                })
    }
}
```

### Java

```java
public class CrossfadeActivity extends Activity {

    private View contentView;
    private View loadingView;
    private int shortAnimationDuration;
    ...
    private void crossfade() {

        // Set the content view to 0% opacity but visible, so that it is
        // visible but fully transparent during the animation.
        contentView.setAlpha(0f);
        contentView.setVisibility(View.VISIBLE);

        // Animate the content view to 100% opacity and clear any animation
        // listener set on the view.
        contentView.animate()
                .alpha(1f)
                .setDuration(shortAnimationDuration)
                .setListener(null);

        // Animate the loading view to 0% opacity. After the animation ends,
        // set its visibility to GONE as an optimization step so it doesn't
        // participate in layout passes.
        loadingView.animate()
                .alpha(0f)
                .setDuration(shortAnimationDuration)
                .setListener(new AnimatorListenerAdapter() {
                    @Override
                    public void onAnimationEnd(Animator animation) {
                        loadingView.setVisibility(View.GONE);
                    }
                });
    }
}
```

## Create a card flip animation

Card flips switch between views of content by showing an animation that emulates
a card flipping over. The card flip animation shown here uses
[`FragmentTransaction`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction).

Here's what a card flip looks like:  
**Figure 2.** Card flip animation.

### Create the animator objects

To create the card flip animation, you need four animators. Two animators are
for when the front of the card animates out and to the left and when it animates
in and from the left. The other two animators are for when the back of the card
animates in and from the right and when it animates out and to the right.

card_flip_left_in.xml  

    <set xmlns:android="http://schemas.android.com/apk/res/android">
        <!-- Before rotating, immediately set the alpha to 0. -->
        <objectAnimator
            android:valueFrom="1.0"
            android:valueTo="0.0"
            android:propertyName="alpha"
            android:duration="0" />

        <!-- Rotate. -->
        <objectAnimator
            android:valueFrom="-180"
            android:valueTo="0"
            android:propertyName="rotationY"
            android:interpolator="@android:interpolator/accelerate_decelerate"
            android:duration="@integer/card_flip_time_full" />

        <!-- Halfway through the rotation, set the alpha to 1. See startOffset. -->
        <objectAnimator
            android:valueFrom="0.0"
            android:valueTo="1.0"
            android:propertyName="alpha"
            android:startOffset="@integer/card_flip_time_half"
            android:duration="1" />
    </set>

card_flip_left_out.xml  

    <set xmlns:android="http://schemas.android.com/apk/res/android">
        <!-- Rotate. -->
        <objectAnimator
            android:valueFrom="0"
            android:valueTo="180"
            android:propertyName="rotationY"
            android:interpolator="@android:interpolator/accelerate_decelerate"
            android:duration="@integer/card_flip_time_full" />

        <!-- Halfway through the rotation, set the alpha to 0. See startOffset. -->
        <objectAnimator
            android:valueFrom="1.0"
            android:valueTo="0.0"
            android:propertyName="alpha"
            android:startOffset="@integer/card_flip_time_half"
            android:duration="1" />
    </set>

card_flip_right_in.xml  

    <set xmlns:android="http://schemas.android.com/apk/res/android">
        <!-- Before rotating, immediately set the alpha to 0. -->
        <objectAnimator
            android:valueFrom="1.0"
            android:valueTo="0.0"
            android:propertyName="alpha"
            android:duration="0" />

        <!-- Rotate. -->
        <objectAnimator
            android:valueFrom="180"
            android:valueTo="0"
            android:propertyName="rotationY"
            android:interpolator="@android:interpolator/accelerate_decelerate"
            android:duration="@integer/card_flip_time_full" />

        <!-- Halfway through the rotation, set the alpha to 1. See startOffset. -->
        <objectAnimator
            android:valueFrom="0.0"
            android:valueTo="1.0"
            android:propertyName="alpha"
            android:startOffset="@integer/card_flip_time_half"
            android:duration="1" />
    </set>

card_flip_right_out.xml  

    <set xmlns:android="http://schemas.android.com/apk/res/android">
        <!-- Rotate. -->
        <objectAnimator
            android:valueFrom="0"
            android:valueTo="-180"
            android:propertyName="rotationY"
            android:interpolator="@android:interpolator/accelerate_decelerate"
            android:duration="@integer/card_flip_time_full" />

        <!-- Halfway through the rotation, set the alpha to 0. See startOffset. -->
        <objectAnimator
            android:valueFrom="1.0"
            android:valueTo="0.0"
            android:propertyName="alpha"
            android:startOffset="@integer/card_flip_time_half"
            android:duration="1" />
    </set>

### Create the views

Each side of the card is a separate layout that can contain any content you
want, such as two text views, two images, or any combination of views to flip
between. Use the two layouts in the fragments that you animate later. The
following layout creates one side of a card, which shows text:  

    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:background="#a6c"
        android:padding="16dp"
        android:gravity="bottom">

        <TextView android:id="@android:id/text1"
            style="?android:textAppearanceLarge"
            android:textStyle="bold"
            android:textColor="#fff"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/card_back_title" />

        <TextView style="?android:textAppearanceSmall"
            android:textAllCaps="true"
            android:textColor="#80ffffff"
            android:textStyle="bold"
            android:lineSpacingMultiplier="1.2"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/card_back_description" />

    </LinearLayout>

And the next layout creates the other side of the card, which displays an
[`ImageView`](https://developer.android.com/reference/android/widget/ImageView):  

    <ImageView xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:src="@drawable/image1"
        android:scaleType="centerCrop"
        android:contentDescription="@string/description_image_1" />

### Create the fragments

Create fragment classes for the front and back of the card. In your fragment
classes, return the layouts that you created from the
[`onCreateView()`](https://developer.android.com/reference/android/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle))
method. You can then create instances of this fragment in the parent activity
where you want to show the card.

The following example shows nested fragment classes inside the parent activity
that uses them:  

### Kotlin

```kotlin
class CardFlipActivity : FragmentActivity() {
    ...
    /**

                    *   A fragment representing the front of the card.
     */
    class CardFrontFragment : Fragment() {

    override fun onCreateView(
                inflater: LayoutInflater,
                container: ViewGroup?,
                savedInstanceState: Bundle?
    ): View = inflater.inflate(R.layout.fragment_card_front, container, false)
    }

    /**
    *   A fragment representing the back of the card.
    */
    class CardBackFragment : Fragment() {

    override fun onCreateView(
                inflater: LayoutInflater,
                container: ViewGroup?,
                savedInstanceState: Bundle?
    ): View = inflater.inflate(R.layout.fragment_card_back, container, false)
    }
}
```

### Java

```java
public class CardFlipActivity extends FragmentActivity {
    ...
    /**
    *   A fragment representing the front of the card.
    */
    public class CardFrontFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            return inflater.inflate(R.layout.fragment_card_front, container, false);
    }
    }

    /**
    *   A fragment representing the back of the card.
    */
    public class CardBackFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            return inflater.inflate(R.layout.fragment_card_back, container, false);
    }
    }
}
```

### Animate the card flip

Display the fragments inside a parent activity. To do this, create the layout
for your activity. The following example creates a
[`FrameLayout`](https://developer.android.com/reference/android/widget/FrameLayout) that you can add
fragments to at runtime:  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/container"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

In the activity code, set the content view to be the layout that you create.
It's good practice to show a default fragment when the activity is created. The
following example activity shows how to display the front of the card by
default:  

### Kotlin

```kotlin
class CardFlipActivity : FragmentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_activity_card_flip)
        if (savedInstanceState == null) {
            supportFragmentManager.beginTransaction()
                    .add(R.id.container, CardFrontFragment())
                    .commit()
        }
    }
    ...
}
```

### Java

```java
public class CardFlipActivity extends FragmentActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_activity_card_flip);

        if (savedInstanceState == null) {
            getSupportFragmentManager()
                    .beginTransaction()
                    .add(R.id.container, new CardFrontFragment())
                    .commit();
        }
    }
    ...
}
```

With the front of the card showing, you can show the back of the card with the
flip animation at an appropriate time. Create a method to show the other side of
the card that does the following things:

- Sets the custom animations that you created for the fragment transitions.
- Replaces the displayed fragment with a new fragment and animates this event with the custom animations you created.
- Adds the previously displayed fragment to the fragment back stack, so when the user taps the Back button, the card flips back over.

### Kotlin

```kotlin
class CardFlipActivity : FragmentActivity() {
    ...
    private fun flipCard() {
        if (showingBack) {
            supportFragmentManager.popBackStack()
            return
        }

        // Flip to the back.

        showingBack = true

        // Create and commit a new fragment transaction that adds the fragment
        // for the back of the card, uses custom animations, and is part of the
        // fragment manager's back stack.

        supportFragmentManager.beginTransaction()

                // Replace the default fragment animations with animator
                // resources representing rotations when switching to the back
                // of the card, as well as animator resources representing
                // rotations when flipping back to the front, such as when the
                // system Back button is tapped.
                .setCustomAnimations(
                        R.animator.card_flip_right_in,
                        R.animator.card_flip_right_out,
                        R.animator.card_flip_left_in,
                        R.animator.card_flip_left_out
                )

                // Replace any fragments in the container view with a fragment
                // representing the next page, indicated by the just-incremented
                // currentPage variable.
                .replace(R.id.container, CardBackFragment())

                // Add this transaction to the back stack, letting users press
                // the Back button to get to the front of the card.
                .addToBackStack(null)

                // Commit the transaction.
                .commit()
    }
}
```

### Java

```java
public class CardFlipActivity extends FragmentActivity {
    ...
    private void flipCard() {
        if (showingBack) {
            getSupportFragmentManager().popBackStack();
            return;
        }

        // Flip to the back.

        showingBack = true;

        // Create and commit a new fragment transaction that adds the fragment
        // for the back of the card, uses custom animations, and is part of the
        // fragment manager's back stack.

        getSupportFragmentManager()
                .beginTransaction()

                // Replace the default fragment animations with animator
                // resources representing rotations when switching to the back
                // of the card, as well as animator resources representing
                // rotations when flipping back to the front, such as when the
                // system Back button is pressed.
                .setCustomAnimations(
                        R.animator.card_flip_right_in,
                        R.animator.card_flip_right_out,
                        R.animator.card_flip_left_in,
                        R.animator.card_flip_left_out)

                // Replace any fragments in the container view with a fragment
                // representing the next page, indicated by the just-incremented
                // currentPage variable.
                .replace(R.id.container, new CardBackFragment())

                // Add this transaction to the back stack, letting users press
                // Back to get to the front of the card.
                .addToBackStack(null)

                // Commit the transaction.
                .commit();
    }
}
```

## Create a circular reveal animation

Reveal animations provide users visual continuity when you show or hide a group
of UI elements. The
[`ViewAnimationUtils.createCircularReveal()`](https://developer.android.com/reference/android/view/ViewAnimationUtils#createCircularReveal(android.view.View,%20int,%20int,%20float,%20float))
method lets you animate a clipping circle to reveal or hide a view. This
animation is provided in the
[`ViewAnimationUtils`](https://developer.android.com/reference/android/view/ViewAnimationUtils) class,
which is available for Android 5.0 (API level 21) and higher.

Here is an example showing how to reveal a previously invisible view:  

### Kotlin

```kotlin
// A previously invisible view.
val myView: View = findViewById(R.id.my_view)

// Check whether the runtime version is at least Android 5.0.
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Get the center for the clipping circle.
    val cx = myView.width / 2
    val cy = myView.height / 2

    // Get the final radius for the clipping circle.
    val finalRadius = Math.hypot(cx.toDouble(), cy.toDouble()).toFloat()

    // Create the animator for this view. The start radius is 0.
    val anim = ViewAnimationUtils.createCircularReveal(myView, cx, cy, 0f, finalRadius)
    // Make the view visible and start the animation.
    myView.visibility = View.VISIBLE
    anim.start()
} else {
    // Set the view to invisible without a circular reveal animation below
    // Android 5.0.
    myView.visibility = View.INVISIBLE
}
```

### Java

```java
// A previously invisible view.
View myView = findViewById(R.id.my_view);

// Check whether the runtime version is at least Android 5.0.
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Get the center for the clipping circle.
    int cx = myView.getWidth() / 2;
    int cy = myView.getHeight() / 2;

    // Get the final radius for the clipping circle.
    float finalRadius = (float) Math.hypot(cx, cy);

    // Create the animator for this view. The start radius is 0.
    Animator anim = ViewAnimationUtils.createCircularReveal(myView, cx, cy, 0f, finalRadius);

    // Make the view visible and start the animation.
    myView.setVisibility(View.VISIBLE);
    anim.start();
} else {
    // Set the view to invisible without a circular reveal animation below
    // Android 5.0.
    myView.setVisibility(View.INVISIBLE);
}
```

The `ViewAnimationUtils.createCircularReveal()` animation takes five parameters.
The first parameter is the view that you want to hide or show on the screen. The
next two parameters are the X and Y coordinates for the center of the clipping
circle. Typically, this is the center of the view, but you can also use the
point that the user taps so that the animation starts where they select. The
fourth parameter is the starting radius of the clipping circle.

In the previous example, the initial radius is set to zero so that the view
being displayed is hidden by the circle. The last parameter is the final radius
of the circle. When displaying a view, make the final radius larger than the
view so that the view can be fully revealed before the animation finishes.

To hide a previously visible view, do the following:  

### Kotlin

```kotlin
// A previously visible view.
val myView: View = findViewById(R.id.my_view)

// Check whether the runtime version is at least Android 5.0.
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Get the center for the clipping circle.
    val cx = myView.width / 2
    val cy = myView.height / 2

    // Get the initial radius for the clipping circle.
    val initialRadius = Math.hypot(cx.toDouble(), cy.toDouble()).toFloat()

    // Create the animation. The final radius is 0.
    val anim = ViewAnimationUtils.createCircularReveal(myView, cx, cy, initialRadius, 0f)

    // Make the view invisible when the animation is done.
    anim.addListener(object : AnimatorListenerAdapter() {

        override fun onAnimationEnd(animation: Animator) {
            super.onAnimationEnd(animation)
            myView.visibility = View.INVISIBLE
        }
    })

    // Start the animation.
    anim.start()
} else {
    // Set the view to visible without a circular reveal animation below
    // Android 5.0.
    myView.visibility = View.VISIBLE
}
```

### Java

```java
// A previously visible view.
final View myView = findViewById(R.id.my_view);

// Check whether the runtime version is at least Android 5.0.
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Get the center for the clipping circle.
    int cx = myView.getWidth() / 2;
    int cy = myView.getHeight() / 2;

    // Get the initial radius for the clipping circle.
    float initialRadius = (float) Math.hypot(cx, cy);

    // Create the animation. The final radius is 0.
    Animator anim = ViewAnimationUtils.createCircularReveal(myView, cx, cy, initialRadius, 0f);

    // Make the view invisible when the animation is done.
    anim.addListener(new AnimatorListenerAdapter() {
        @Override
        public void onAnimationEnd(Animator animation) {
            super.onAnimationEnd(animation);
            myView.setVisibility(View.INVISIBLE);
        }
    });

    // Start the animation.
    anim.start();
} else {
    // Set the view to visible without a circular reveal animation below Android
    // 5.0.
    myView.setVisibility(View.VISIBLE);
}
```

In this case, the initial radius of the clipping circle is set to be as large as
the view so that the view is visible before the animation starts. The final
radius is set to zero so that the view is hidden when the animation finishes.
Add a listener to the animation so that the view's visibility can be set to
[`INVISIBLE`](https://developer.android.com/reference/android/view/View#INVISIBLE) when the animation
completes.

## Additional resources

- [Animation](https://developer.android.com/jetpack/compose/animation) with Jetpack Compose.
- [Gestures](https://developer.android.com/jetpack/compose/touch-input/gestures) with Jetpack Compose.