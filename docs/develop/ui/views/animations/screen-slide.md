---
title: https://developer.android.com/develop/ui/views/animations/screen-slide
url: https://developer.android.com/develop/ui/views/animations/screen-slide
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Pager in Compose.  
[Pager →](https://developer.android.com/develop/ui/compose/layouts/pager)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)


Screen slides are transitions between one entire screen to another and are common with UIs
like setup wizards or slideshows. This lesson shows you how to do screen slides with
a [ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager) provided by the [support library](https://developer.android.com/tools/support-library).
[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager) objects can animate screen slides
automatically. Here's what a screen slide looks like that transitions from
one screen of content to the next:  
Screen slide animation  

[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)
is part of AndroidX. For more information, see
[Using AndroidX](https://developer.android.com/jetpack/androidx#using_androidx).
| **Note:** For sliding screens, we recommend the improved [ViewPager2](https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2) library. For more information, see [Slide
| between fragments using ViewPager2](https://developer.android.com/training/animation/screen-slide-2) and [the ViewPager2 migration guide](https://developer.android.com/training/animation/vp2-migration).

## Create the views

Create a layout file that you'll later use for the content of a fragment. You also need
to define a string for the contents of the fragment. The following example
contains a text view to display some text:  

```xml
<!-- fragment_screen_slide_page.xml -->
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/content"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >

    <TextView style="?android:textAppearanceMedium"
        android:padding="16dp"
        android:lineSpacingMultiplier="1.2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/lorem_ipsum" />
</ScrollView>
```

## Create the fragment

Create a [Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment) class that returns the layout
that you just created in the [onCreateView()](https://developer.android.com/reference/android/app/Fragment#onCreateView(android.view.LayoutInflater, android.view.ViewGroup, android.os.Bundle))
method. You can then create instances of this fragment in the parent activity whenever you need a new page to
display to the user:  

### Kotlin

```kotlin
import android.support.v4.app.Fragment

class ScreenSlidePageFragment : Fragment() {

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View = inflater.inflate(R.layout.fragment_screen_slide_page, container, false)
}
```

### Java

```java
import android.support.v4.app.Fragment;
...
public class ScreenSlidePageFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        ViewGroup rootView = (ViewGroup) inflater.inflate(
                R.layout.fragment_screen_slide_page, container, false);

        return rootView;
    }
}
```

## Add a ViewPager

[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager) objects have built-in swipe gestures to transition
through pages, and they display screen slide animations by default, so you don't need to create
your own animation. [ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager) uses
[PagerAdapter](https://developer.android.com/reference/androidx/viewpager/widget/PagerAdapter) objects as a supply for new pages to display, so the [PagerAdapter](https://developer.android.com/reference/androidx/viewpager/widget/PagerAdapter) will use the
fragment class that you created earlier.

To begin, create a layout that contains a [ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager):  

```xml
<!-- activity_screen_slide.xml -->
<android.support.v4.view.ViewPager
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/pager"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

Create an activity that does the following things:

- Sets the content view to be the layout with the [ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager).
- Creates a class that extends the [FragmentStatePagerAdapter](https://developer.android.com/reference/androidx/legacy/app/FragmentStatePagerAdapter) abstract class and implements the [getItem()](https://developer.android.com/reference/androidx/fragment/app/FragmentStatePagerAdapter#getItem(int)) method to supply instances of `ScreenSlidePageFragment` as new pages. The pager adapter also requires that you implement the [getCount()](https://developer.android.com/reference/androidx/viewpager/widget/PagerAdapter#getCount()) method, which returns the amount of pages the adapter will create (five in the example).
- Hooks up the [PagerAdapter](https://developer.android.com/reference/androidx/viewpager/widget/PagerAdapter) to the [ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager).

### Kotlin

```kotlin
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
...
/**
 * The number of pages (wizard steps) to show in this demo.
 */
private const val NUM_PAGES = 5

class ScreenSlidePagerActivity : FragmentActivity() {

    /**
     * The pager widget, which handles animation and allows swiping horizontally to access previous
     * and next wizard steps.
     */
    private lateinit var mPager: ViewPager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_screen_slide)

        // Instantiate a ViewPager and a PagerAdapter.
        mPager = findViewById(R.id.pager)

        // The pager adapter, which provides the pages to the view pager widget.
        val pagerAdapter = ScreenSlidePagerAdapter(supportFragmentManager)
        mPager.adapter = pagerAdapter
    }

    override fun onBackPressed() {
        if (mPager.currentItem == 0) {
            // If the user is currently looking at the first step, allow the system to handle the
            // Back button. This calls finish() on this activity and pops the back stack.
            super.onBackPressed()
        } else {
            // Otherwise, select the previous step.
            mPager.currentItem = mPager.currentItem - 1
        }
    }

    /**
     * A simple pager adapter that represents 5 ScreenSlidePageFragment objects, in
     * sequence.
     */
    private inner class ScreenSlidePagerAdapter(fm: FragmentManager) : FragmentStatePagerAdapter(fm) {
        override fun getCount(): Int = NUM_PAGES

        override fun getItem(position: Int): Fragment = ScreenSlidePageFragment()
    }
}
```

### Java

```java
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
...
public class ScreenSlidePagerActivity extends FragmentActivity {
    /**
     * The number of pages (wizard steps) to show in this demo.
     */
    private static final int NUM_PAGES = 5;

    /**
     * The pager widget, which handles animation and allows swiping horizontally to access previous
     * and next wizard steps.
     */
    private ViewPager mPager;

    /**
     * The pager adapter, which provides the pages to the view pager widget.
     */
    private PagerAdapter pagerAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_screen_slide);

        // Instantiate a ViewPager and a PagerAdapter.
        mPager = (ViewPager) findViewById(R.id.pager);
        pagerAdapter = new ScreenSlidePagerAdapter(getSupportFragmentManager());
        mPager.setAdapter(pagerAdapter);
    }

    @Override
    public void onBackPressed() {
        if (mPager.getCurrentItem() == 0) {
            // If the user is currently looking at the first step, allow the system to handle the
            // Back button. This calls finish() on this activity and pops the back stack.
            super.onBackPressed();
        } else {
            // Otherwise, select the previous step.
            mPager.setCurrentItem(mPager.getCurrentItem() - 1);
        }
    }

    /**
     * A simple pager adapter that represents 5 ScreenSlidePageFragment objects, in
     * sequence.
     */
    private class ScreenSlidePagerAdapter extends FragmentStatePagerAdapter {
        public ScreenSlidePagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            return new ScreenSlidePageFragment();
        }

        @Override
        public int getCount() {
            return NUM_PAGES;
        }
    }
}
```

## Customize the animation using PageTransformer

To display a different animation from the default screen slide animation, implement the
[ViewPager.PageTransformer](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer) interface and supply it to
the view pager. The interface exposes a single method, [transformPage()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer#transformPage(android.view.View, float)). At each point in the screen's transition, this method is called once for each visible page (generally there's only one visible page) and for adjacent pages just off the screen.
For example, if page three is visible and the user drags towards page four,
[transformPage()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer#transformPage(android.view.View, float)) is called
for pages two, three, and four at each step of the gesture.


In your implementation of [transformPage()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer#transformPage(android.view.View, float)),
you can then create custom slide animations by determining which pages need to be transformed based on the
position of the page on the screen, which is obtained from the `position` parameter
of the [transformPage()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer#transformPage(android.view.View, float)) method.

The `position` parameter indicates where a given page is located relative to the center of the screen.
It is a dynamic property that changes as the user scrolls through the pages. When a page fills the screen, its position value is `0`.
When a page is drawn just off the right side of the screen, its position value is `1`. If the user scrolls halfway between pages one and two, page one has a position of -0.5 and page two has a position of 0.5. Based on the position of the pages on the screen, you can create custom slide animations by setting page properties with methods such as [setAlpha()](https://developer.android.com/reference/android/view/View#setAlpha(float)), [setTranslationX()](https://developer.android.com/reference/android/view/View#setTranslationX(float)), or
[setScaleY()](https://developer.android.com/reference/android/view/View#setScaleY(float)).

When you have an implementation of a [PageTransformer](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer),
call [setPageTransformer()](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager#setPageTransformer(boolean, android.support.v4.view.ViewPager.PageTransformer)) with
your implementation to apply your custom animations. For example, if you have a
[PageTransformer](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer) named
`ZoomOutPageTransformer`, you can set your custom animations
like this:  

### Kotlin

```kotlin
val mPager: ViewPager = findViewById(R.id.pager)
...
mPager.setPageTransformer(true, ZoomOutPageTransformer())
```

### Java

```java
ViewPager mPager = (ViewPager) findViewById(R.id.pager);
...
mPager.setPageTransformer(true, new ZoomOutPageTransformer());
```

See the [Zoom-out page transformer](https://developer.android.com/develop/ui/views/animations/screen-slide#zoom-out) and [Depth page transformer](https://developer.android.com/develop/ui/views/animations/screen-slide#depth-page)
sections for examples and videos of a [PageTransformer](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager.PageTransformer).

### Zoom-out page transformer


This page transformer shrinks and fades pages when scrolling between
adjacent pages. As a page gets closer to the center, it grows back to
its normal size and fades in.  
`ZoomOutPageTransformer` example  

### Kotlin

```kotlin
private const val MIN_SCALE = 0.85f
private const val MIN_ALPHA = 0.5f

class ZoomOutPageTransformer : ViewPager.PageTransformer {

    override fun transformPage(view: View, position: Float) {
        view.apply {
            val pageWidth = width
            val pageHeight = height
            when {
                position < -1 -> { // [-Infinity,-1)
                    // This page is way off-screen to the left.
                    alpha = 0f
                }
                position <= 1 -> { // [-1,1]
                    // Modify the default slide transition to shrink the page as well
                    val scaleFactor = Math.max(MIN_SCALE, 1 - Math.abs(position))
                    val vertMargin = pageHeight * (1 - scaleFactor) / 2
                    val horzMargin = pageWidth * (1 - scaleFactor) / 2
                    translationX = if (position < 0) {
                        horzMargin - vertMargin / 2
                    } else {
                        horzMargin + vertMargin / 2
                    }

                    // Scale the page down (between MIN_SCALE and 1)
                    scaleX = scaleFactor
                    scaleY = scaleFactor

                    // Fade the page relative to its size.
                    alpha = (MIN_ALPHA +
                            (((scaleFactor - MIN_SCALE) / (1 - MIN_SCALE)) * (1 - MIN_ALPHA)))
                }
                else -> { // (1,+Infinity]
                    // This page is way off-screen to the right.
                    alpha = 0f
                }
            }
        }
    }
}
```

### Java

```java
public class ZoomOutPageTransformer implements ViewPager.PageTransformer {
    private static final float MIN_SCALE = 0.85f;
    private static final float MIN_ALPHA = 0.5f;

    public void transformPage(View view, float position) {
        int pageWidth = view.getWidth();
        int pageHeight = view.getHeight();

        if (position < -1) { // [-Infinity,-1)
            // This page is way off-screen to the left.
            view.setAlpha(0f);

        } else if (position <= 1) { // [-1,1]
            // Modify the default slide transition to shrink the page as well
            float scaleFactor = Math.max(MIN_SCALE, 1 - Math.abs(position));
            float vertMargin = pageHeight * (1 - scaleFactor) / 2;
            float horzMargin = pageWidth * (1 - scaleFactor) / 2;
            if (position < 0) {
                view.setTranslationX(horzMargin - vertMargin / 2);
            } else {
                view.setTranslationX(-horzMargin + vertMargin / 2);
            }

            // Scale the page down (between MIN_SCALE and 1)
            view.setScaleX(scaleFactor);
            view.setScaleY(scaleFactor);

            // Fade the page relative to its size.
            view.setAlpha(MIN_ALPHA +
                    (scaleFactor - MIN_SCALE) /
                    (1 - MIN_SCALE) * (1 - MIN_ALPHA));

        } else { // (1,+Infinity]
            // This page is way off-screen to the right.
            view.setAlpha(0f);
        }
    }
}
```

### Depth page transformer


This page transformer uses the default slide animation for sliding pages
to the left, while using a "depth" animation for sliding pages to the
right. This depth animation fades the page out, and scales it down linearly.  
`DepthPageTransformer` example  

During the depth animation, the default animation (a screen slide) still
takes place, so you must counteract the screen slide with a negative X translation.

For example:  

### Kotlin

```kotlin
view.translationX = -1 * view.width * position
```

### Java

```java
view.setTranslationX(-1 * view.getWidth() * position);
```


The following example shows how to counteract the default screen slide animation
in a working page transformer:  

### Kotlin

```kotlin
private const val MIN_SCALE = 0.75f

class DepthPageTransformer : ViewPager.PageTransformer {

    override fun transformPage(view: View, position: Float) {
        view.apply {
            val pageWidth = width
            when {
                position < -1 -> { // [-Infinity,-1)
                    // This page is way off-screen to the left.
                    alpha = 0f
                }
                position <= 0 -> { // [-1,0]
                    // Use the default slide transition when moving to the left page
                    alpha = 1f
                    translationX = 0f
                    scaleX = 1f
                    scaleY = 1f
                }
                position <= 1 -> { // (0,1]
                    // Fade the page out.
                    alpha = 1 - position

                    // Counteract the default slide transition
                    translationX = pageWidth * -position

                    // Scale the page down (between MIN_SCALE and 1)
                    val scaleFactor = (MIN_SCALE + (1 - MIN_SCALE) * (1 - Math.abs(position)))
                    scaleX = scaleFactor
                    scaleY = scaleFactor
                }
                else -> { // (1,+Infinity]
                    // This page is way off-screen to the right.
                    alpha = 0f
                }
            }
        }
    }
}
```

### Java

```java
public class DepthPageTransformer implements ViewPager.PageTransformer {
    private static final float MIN_SCALE = 0.75f;

    public void transformPage(View view, float position) {
        int pageWidth = view.getWidth();

        if (position < -1) { // [-Infinity,-1)
            // This page is way off-screen to the left.
            view.setAlpha(0f);

        } else if (position <= 0) { // [-1,0]
            // Use the default slide transition when moving to the left page
            view.setAlpha(1f);
            view.setTranslationX(0f);
            view.setScaleX(1f);
            view.setScaleY(1f);

        } else if (position <= 1) { // (0,1]
            // Fade the page out.
            view.setAlpha(1 - position);

            // Counteract the default slide transition
            view.setTranslationX(pageWidth * -position);

            // Scale the page down (between MIN_SCALE and 1)
            float scaleFactor = MIN_SCALE
                    + (1 - MIN_SCALE) * (1 - Math.abs(position));
            view.setScaleX(scaleFactor);
            view.setScaleY(scaleFactor);

        } else { // (1,+Infinity]
            // This page is way off-screen to the right.
            view.setAlpha(0f);
        }
    }
}
```