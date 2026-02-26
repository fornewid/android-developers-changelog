---
title: https://developer.android.com/develop/ui/views/animations/screen-slide-2
url: https://developer.android.com/develop/ui/views/animations/screen-slide-2
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Pager in Compose. [Pager →](https://developer.android.com/develop/ui/compose/layouts/pager) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Screen slides are transitions from one entire screen to another and are common with UIs like
setup wizards and slideshows. This topic shows you how to do screen slides with a
`https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2`
object. `ViewPager2` objects can animate screen slides automatically. Here's an example
of a screen slide that transitions from one screen of content to the next:
**Figure 1.** Screen slide animation.

If you want to jump ahead and see a full working example,
[view
this sample app](https://github.com/android/views-widgets-samples/tree/main/ViewPager2) on GitHub.

> [!NOTE]
> **Note:** If your app already uses `https://developer.android.com/reference/kotlin/androidx/viewpager/widget/ViewPager`, see [Migrate from ViewPager to ViewPager2](https://developer.android.com/training/animation/vp2-migration).

To use `ViewPager2`, you need to add some
[AndroidX dependencies](https://developer.android.com/jetpack/androidx/releases/viewpager2#androidx-deps) to your
project. Then follow the steps outlined in the following sections.

## Create the views

Create a layout file to use later for the content of a fragment. You also need to define a string
for the contents of the fragment. The following example contains a text view that displays some
text:

```xml
<!-- fragment_screen_slide_page.xml -->
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    an@droid:id="+id/content"
    android:layout_width="match_parent"
    android>:layou<t_height="match_parent" 

    TextView style="?android:textAppearanceMedium"
        android:padding="16dp"
        android:lineSpacingMultiplier="1.2"
        android:layout_width="match_parent"
        a>n<droid:layou>t_height="wrap_content"
        android:text="@string/lorem_ipsum" /
/ScrollView
```

## Create the fragment

Create a
`https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment` class that
returns the layout that you created in the
`https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater, android.view.ViewGroup, android.os.Bundle)`
method. You can then create instances of this fragment in the parent activity whenever you need a
new page to display to the user:

### Kotlin

```kotlin
import androidx.fragment.app.Fragment

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
import androidx.fragment.app.Fragment;
...
public class ScreenSlidePageFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        return (ViewGroup) inflater.inflate(
                R.layout.fragment_screen_slide_page, container, false);
    }
}
```

## Add a ViewPager2

`ViewPager2` objects have built-in swipe gestures to transition through pages, and
they display screen slide animations by default, so you don't need to create your own animation.
`ViewPager2` uses
`https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter`
objects as a supply for new pages to display, so the `FragmentStateAdapter` uses the
fragment class that you created.

To begin, create a layout that contains a `ViewPager2` object:

```xml
<!-- activity_screen_slide.xml -->
<androidx.viewpager2.widget.ViewPager2
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/pager"
    android:layout_width="match_parent"
    android:>layout_height="match_parent" /
```

Create an activity that does the following:

- Sets the content view to be the layout with the `ViewPager2`.
- Creates a class that extends the `FragmentStateAdapter` abstract class and implements the `https://developer.android.com/reference/kotlin/androidx/viewpager2/adapter/FragmentStateAdapter#createFragment(int)` method to supply instances of `ScreenSlidePageFragment` as new pages. You must implement the `https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter#getItemCount()` method for the pager adapter, which returns the number of pages the adapter creates. There are five in the example.
- Hooks up the `FragmentStateAdapter` to the `ViewPager2` objects.

### Kotlin

```kotlin
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
...
/**
 * The number of pages (wizard steps) to show in this demo.
 */
private const val NUM_PAGES = 5

class ScreenSlidePagerActivity : FragmentActivity() {

    /**
     * The pager widget, which handles animation and allows swiping horizontally
     * to access previous and next wizard steps.
     */
    private lateinit var viewPager: ViewPager2

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_screen_slide)

        // Instantiate a ViewPager2 and a PagerAdapter.
        viewPager = findViewById(R.id.pager)

        // The pager adapter, which provides the pages to the view pager widget.
        val pagerAdapter = ScreenSlidePagerAdapter(this)
        viewPager.adapter = pagerAdapter
    }

    override fun onBackPressed() {
        if (viewPager.currentItem == 0) {
            // If the user is currently looking at the first step, allow the system to handle
            // the Back button. This calls finish() on this activity and pops the back stack.
            super.onBackPressed()
        } else {
            // Otherwise, select the previous step.
            viewPager.currentItem = viewPager.currentItem - 1
        }
    }

    /**
     * A simple pager adapter that represents 5 ScreenSlidePageFragment objects, in
     * sequence.
     */
    private inner class ScreenSlidePagerAdapter(fa: FragmentActivity) : FragmentStateAdapter(fa) {
        override fun getItemCount(): Int = NUM_PAGES

        override fun createFragment(position: Int): Fragment = ScreenSlidePageFragment()
    }
}
```

### Java

```java
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
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
    private ViewPager2 viewPager;

    /**
     * The pager adapter, which provides the pages to the view pager widget.
     */
    private FragmentStateAdapter pagerAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_screen_slide);

        // Instantiate a ViewPager2 and a PagerAdapter.
        viewPager = findViewById(R.id.pager);
        pagerAdapter = new ScreenSlidePagerAdapter(this);
        viewPager.setAdapter(pagerAdapter);
    }

    @Override
    public void onBackPressed() {
        if (viewPager.getCurrentItem() == 0) {
            // If the user is currently looking at the first step, allow the system to handle the
            // Back button. This calls finish() on this activity and pops the back stack.
            super.onBackPressed();
        } else {
            // Otherwise, select the previous step.
            viewPager.setCurrentItem(viewPager.getCurrentItem() - 1);
        }
    }

    /**
     * A simple pager adapter that represents 5 ScreenSlidePageFragment objects, in
     * sequence.
     */
    private class ScreenSlidePagerAdapter extends FragmentStateAdapter {
        public ScreenSlidePagerAdapter(FragmentActivity fa) {
            super(fa);
        }

        @Override
        public Fragment createFragment(int position) {
            return new ScreenSlidePageFragment();
        }

        @Override
        public int getItemCount() {
            return NUM_PAGES;
        }
    }
}
```

## Customize the animation using PageTransformer

To display a different animation from the default screen slide animation, implement the
`https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2.PageTransformer`
interface and supply it to the `ViewPager2` object. The interface exposes a single
method,
`https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2.PageTransformer#transformPage(android.view.View, float)`.
At each point in the screen's transition, this method is called once for each visible page---there's
usually only one visible page---and for adjacent pages off the screen. For example, if page three is
visible and the user drags towards page four, `transformPage()` is called for pages two,
three, and four at each step of the gesture.

In your implementation of `transformPage()`, you can then create custom slide
animations by determining which pages need to be transformed based on the position of the page on
the screen. Obtain the page position from the `position` parameter of the
`transformPage()` method.

The `position` parameter indicates where a given page is located relative to the
center of the screen. This parameter is a dynamic property that changes as the user scrolls through
a series of pages. When a page fills the screen, its position value is `0`. When a page
is drawn off the right side of the screen, its position value is `1`. If the user scrolls
halfway between pages one and two, page one has a position of `-0.5`, and page two has a
position of `0.5`. Based on the position of the pages on the screen, you can create
custom slide animations by setting page properties with methods such as
`https://developer.android.com/reference/kotlin/android/view/View#setalpha`,
`https://developer.android.com/reference/kotlin/android/view/View#settranslationx`,
or
`https://developer.android.com/reference/kotlin/android/view/View#setscaley`.

When you have an implementation of a
`https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2.PageTransformer`,
call
`https://developer.android.com/reference/kotlin/androidx/viewpager2/widget/ViewPager2#setPageTransformer(androidx.viewpager2.widget.ViewPager2.PageTransformer)`
with your implementation to apply your custom animations. For example, if you have a
`PageTransformer` named `ZoomOutPageTransformer`, you can set your custom
animations like this:

### Kotlin

```kotlin
val viewPager: ViewPager2 = findViewById(R.id.pager)
...
viewPager.setPageTransformer(ZoomOutPageTransformer())
```

### Java

```java
ViewPager2 viewPager = findViewById(R.id.pager);
...
viewPager.setPageTransformer(new ZoomOutPageTransformer());
```

See the [Zoom-out page transformer](https://developer.android.com/develop/ui/views/animations/screen-slide-2#zoom-out) and
[Depth page transformer](https://developer.android.com/develop/ui/views/animations/screen-slide-2#depth-page) sections for examples of a
`PageTransformer`.

### Zoom-out page transformer

This page transformer shrinks and fades pages when scrolling between adjacent pages. As a page
gets closer to the center, it grows back to its normal size and fades in.
**Figure 2.** `ZoomOutPageTransformer` example.

### Kotlin

```kotlin
private const val MIN_SCALE = 0.85f
private const val MIN_ALPHA = 0.5f

class ZoomOutPageTransformer : ViewPager2.PageTransformer {

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
                    // Modify the default slide transition to shrink the page as well.
                    val scaleFactor = Math.max(MIN_SCALE, 1 - Math.abs(position))
                    val vertMargin = pageHeight * (1 - scaleFactor) / 2
                    val horzMargin = pageWidth * (1 - scaleFactor) / 2
                    translationX = if (position < 0) {
                        horzMargin - vertMargin / 2
                    } else {
                        horzMargin + vertMargin / 2
                    }

                    // Scale the page down (between MIN_SCALE and 1).
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
public class ZoomOutPageTransformer implements ViewPager2.PageTransformer {
    private static final float MIN_SCALE = 0.85f;
    private static final float MIN_ALPHA = 0.5f;

    public void transformPage(View view, float position) {
        int pageWidth = view.getWidth();
        int pageHeight = view.getHeight();

        if (position < -1) { // [-Infinity,-1)
            // This page is way off-screen to the left.
            view.setAlpha(0f);

        } else if (position <= 1) { // [-1,1]
            // Modify the default slide transition to shrink the page as well.
            float scaleFactor = Math.max(MIN_SCALE, 1 - Math.abs(position));
            float vertMargin = pageHeight * (1 - scaleFactor) / 2;
            float horzMargin = pageWidth * (1 - scaleFactor) / 2;
            if (position < 0) {
                view.setTranslationX(horzMargin - vertMargin / 2);
            } else {
                view.setTranslationX(-horzMargin + vertMargin / 2);
            }

            // Scale the page down (between MIN_SCALE and 1).
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

This page transformer uses the default slide animation for sliding pages to the left, while using
a "depth" animation for sliding pages to the right. This depth animation fades the page out and
scales it down linearly.
**Figure 3.** `DepthPageTransformer` example.

During the depth animation, the default animation (a screen slide) still takes place, so you must
counteract the screen slide with a negative X translation. For example:

### Kotlin

```kotlin
view.translationX = -1 * view.width * position
```

### Java

```java
view.setTranslationX(-1 * view.getWidth() * position);
```

The following example shows how to counteract the default screen slide animation in a working
page transformer:

### Kotlin

```kotlin
private const val MIN_SCALE = 0.75f

@RequiresApi(21)
class DepthPageTransformer : ViewPager2.PageTransformer {

    override fun transformPage(view: View, position: Float) {
        view.apply {
            val pageWidth = width
            when {
                position < -1 -> { // [-Infinity,-1)
                    // This page is way off-screen to the left.
                    alpha = 0f
                }
                position <= 0 -> { // [-1,0]
                    // Use the default slide transition when moving to the left page.
                    alpha = 1f
                    translationX = 0f
                    translationZ = 0f
                    scaleX = 1f
                    scaleY = 1f
                }
                position <= 1 -> { // (0,1]
                    // Fade the page out.
                    alpha = 1 - position

                    // Counteract the default slide transition.
                    translationX = pageWidth * -position
                    // Move it behind the left page.
                    translationZ = -1f

                    // Scale the page down (between MIN_SCALE and 1).
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
@RequiresApi(21)
public class DepthPageTransformer implements ViewPager2.PageTransformer {
    private static final float MIN_SCALE = 0.75f;

    public void transformPage(View view, float position) {
        int pageWidth = view.getWidth();

        if (position < -1) { // [-Infinity,-1)
            // This page is way off-screen to the left.
            view.setAlpha(0f);

        } else if (position <= 0) { // [-1,0]
            // Use the default slide transition when moving to the left page.
            view.setAlpha(1f);
            view.setTranslationX(0f);
            view.setTranslationZ(0f);
            view.setScaleX(1f);
            view.setScaleY(1f);

        } else if (position <= 1) { // (0,1]
            // Fade the page out.
            view.setAlpha(1 - position);

            // Counteract the default slide transition.
            view.setTranslationX(pageWidth * -position);
            // Move it behind the left page
            view.setTranslationZ(-1f);

            // Scale the page down (between MIN_SCALE and 1).
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

## Additional resources

To learn more about `ViewPager2`, see the following additional resources.

### Samples

- [ViewPager2 samples](https://goo.gle/viewpager2-sample) on GitHub.

### Videos

- [Turning the Page:
  Migrating to ViewPager2](https://www.youtube.com/watch?v=lAP6cz1HSzA) (Android Dev Summit '19)