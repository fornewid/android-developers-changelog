---
title: Introduce first-time users to your app  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/leanback/onboarding
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Introduce first-time users to your app Stay organized with collections Save and categorize content based on your preferences.




Build better with Compose

Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.

[Compose for TV →](https://developer.android.com/training/tv/playback/compose)

![](/static/images/android-compose-tv-logo.png)

**Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
Android TV OS](/training/tv/playback/compose) instead.

To show a first-time user how to get the most from your app, present
onboarding information at app startup. Here are some examples of onboarding
information:

* Present detailed information on which channels are available when a user
  first accesses a channel app.
* Call attention to noteworthy features in your app.
* Illustrate any required or recommended steps for users to take when
  using the app for the first time.

The [androidx.leanback library](/training/tv/get-started/create#leanback) provides the
`OnboardingSupportFragment` class for
presenting first-time user information. This guide describes how to use the
`OnboardingSupportFragment` class to present
introductory information that is shown when the app launches for the first
time.

`OnboardingSupportFragment` uses TV UI
best practices to present information in a way that matches TV UI styles
and is easy to navigate on TV devices.

![](/static/images/training/tv/playback/onboarding-fragment.png)

**Figure 1.** An example
`OnboardingSupportFragment`.

`OnboardingSupportFragment` is not appropriate for every use case.
Don't use `OnboardingSupportFragment` when you need to include
UI elements that require user input, such as buttons and fields.
Also, don't use `OnboardingSupportFragment` for tasks the user will do
regularly. Finally, if you need to present a multi-page UI that requires
user input, consider using a
`GuidedStepSupportFragment`.

## Add an OnboardingSupportFragment

To add an `OnboardingSupportFragment`
to your app, implement a class that extends
the `OnboardingSupportFragment` class. Add
this fragment to an activity, either using the activity's layout XML or
programmatically. Make sure the activity or
fragment uses a theme derived from
`Theme_Leanback_Onboarding`,
as described in the [Customize themes](#themes) section.

In the `onCreate()` method of your
app's main activity, call
`startActivity()`
with an `Intent` that points to
the parent activity of your `OnboardingSupportFragment`.
This helps ensure that your
`OnboardingSupportFragment` appears as
soon as your app starts.

To help ensure that the
`OnboardingSupportFragment` only appears the
first time that the user starts your app, use a
`SharedPreferences` object
to track whether the user has already viewed the
`OnboardingSupportFragment`. Define a boolean
value that changes to true when the user finishes viewing the
`OnboardingSupportFragment`. Check
this value in your main activity’s
`onCreate()` method and only start the
`OnboardingSupportFragment` parent activity if
the value is false.

The following example shows an override of `onCreate()` that checks for a
`SharedPreferences` value and, if it is not set to true, calls
`startActivity()` to show the `OnboardingSupportFragment`:

### Kotlin

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
    PreferenceManager.getDefaultSharedPreferences(this).apply {
        // Check if we need to display our OnboardingSupportFragment
        if (!getBoolean(MyOnboardingSupportFragment.COMPLETED_ONBOARDING_PREF_NAME, false)) {
            // The user hasn't seen the OnboardingSupportFragment yet, so show it
            startActivity(Intent(this@OnboardingActivity, OnboardingActivity::class.java))
        }
    }
}
```

### Java

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    SharedPreferences sharedPreferences =
            PreferenceManager.getDefaultSharedPreferences(this);
    // Check if we need to display our OnboardingSupportFragment
    if (!sharedPreferences.getBoolean(
            MyOnboardingSupportFragment.COMPLETED_ONBOARDING_PREF_NAME, false)) {
        // The user hasn't seen the OnboardingSupportFragment yet, so show it
        startActivity(new Intent(this, OnboardingActivity.class));
    }
}
```

After the user views the
`OnboardingSupportFragment`, mark it as viewed
using the `SharedPreferences` object. To do this, override
`onFinishFragment()`
in your `OnboardingSupportFragment` and set your `SharedPreferences`
value to true, as shown in the following example:

### Kotlin

```
override fun onFinishFragment() {
    super.onFinishFragment()
    // User has seen OnboardingSupportFragment, so mark our SharedPreferences
    // flag as completed so that we don't show our OnboardingSupportFragment
    // the next time the user launches the app
    PreferenceManager.getDefaultSharedPreferences(context).edit().apply {
        putBoolean(COMPLETED_ONBOARDING_PREF_NAME, true)
        apply()
    }
}
```

### Java

```
@Override
protected void onFinishFragment() {
    super.onFinishFragment();
    // User has seen OnboardingSupportFragment, so mark our SharedPreferences
    // flag as completed so that we don't show our OnboardingSupportFragment
    // the next time the user launches the app
    SharedPreferences.Editor sharedPreferencesEditor =
            PreferenceManager.getDefaultSharedPreferences(getContext()).edit();
    sharedPreferencesEditor.putBoolean(
            COMPLETED_ONBOARDING_PREF_NAME, true);
    sharedPreferencesEditor.apply();
}
```

## Add OnboardingSupportFragment pages

An `OnboardingSupportFragment`
displays content in a series of ordered pages. After you add your
`OnboardingSupportFragment`, you need to define
the onboarding pages. Each page can have a title, a description, and
several subviews that can contain images or animations.

![](/static/images/training/tv/playback/onboarding-fragment-diagram.png)

**Figure 2.** `OnboardingSupportFragment`
page elements.

Figure 2 shows an example page with callouts marking customizable page
elements that your `OnboardingSupportFragment`
can provide. The page elements are:

1. The page title.
2. The page description.
3. The page content view, in this case a simple green checkmark in a grey box.
   This view is optional. Use this view to illustrate page details. For example, you might
   include a screenshot that highlights the app feature the page describes.
4. The page background view, in this case a simple blue gradient. This view
   always renders behind other views on the page. This view is optional.
5. The page foreground view, in this case a logo. This view always renders
   in front of all other views on the page. This view is optional.

Initialize page information when your
`OnboardingSupportFragment` is first created
or attached to the parent activity, as the system requests page
information when it creates the fragment's view. You can initialize page
information in your class constructor or in an override of
`onAttach()`.

Override each of the following methods, which provide page information
to the system:

* `getPageCount()` returns the number of pages in your
  `OnboardingSupportFragment`.
* `getPageTitle()` returns the title for the requested page number.
* `getPageDescription()` returns the description for the requested page
  number.

Override each of the following methods to provide optional subviews
to display images or animations:

* `onCreateBackgroundView()`
  returns a `View` that you
  create to act as the background view or null if no background view is needed.* `onCreateContentView()`
    returns a `View` that you
    create to act as the content view or null if no content view is needed.* `onCreateForegroundView()`
      returns a `View` that you
      create to act as the foreground view or null if no foreground view is needed.

The system adds the `View` that you create to the page
layout. The following example overrides
`onCreateContentView()` and returns an
`ImageView`:

### Kotlin

```
private lateinit var contentView: ImageView
...
override fun onCreateContentView(inflater: LayoutInflater?, container: ViewGroup?): View? {
    return ImageView(context).apply {
        scaleType = ImageView.ScaleType.CENTER_INSIDE
        setImageResource(R.drawable.onboarding_content_view)
        setPadding(0, 32, 0, 32)
        contentView = this
    }
}
```

### Java

```
private ImageView contentView;
...
@Override
protected View onCreateContentView(LayoutInflater inflater, ViewGroup container) {
    contentView = new ImageView(getContext());
    contentView.setScaleType(ImageView.ScaleType.CENTER_INSIDE);
    contentView.setImageResource(R.drawable.onboarding_content_view);
    contentView.setPadding(0, 32, 0, 32);
    return contentView;
}
```

## Add an initial logo screen

Your `OnboardingSupportFragment` can start
with an optional logo screen that introduces your app. If you want to display
a `Drawable`
as your logo screen, call
`setLogoResourceId()`
with the ID of your `Drawable`
in the `onCreate()`
method of your `OnboardingSupportFragment`.
The system fades in and briefly displays the
`Drawable`, and then fades out the `Drawable`
before displaying the first page of your `OnboardingSupportFragment`.

If you want to provide a custom animation for your logo screen, instead of
calling `setLogoResourceId()`, override
`onCreateLogoAnimation()` and return an `Animator`
object that renders your custom animation, as shown in the following example:

### Kotlin

```
public override fun onCreateLogoAnimation(): Animator =
        AnimatorInflater.loadAnimator(context, R.animator.onboarding_logo_screen_animation)
```

### Java

```
@Override
public Animator onCreateLogoAnimation() {
    return AnimatorInflater.loadAnimator(getContext(),
            R.animator.onboarding_logo_screen_animation);
}
```

## Customize page animations

The system uses default animations when displaying the first page of your
`OnboardingSupportFragment` and when the user
navigates to a different page. You can customize these animations by
overriding methods in your
`OnboardingSupportFragment`.

To customize the animation that appears on your first page,
override
`onCreateEnterAnimation()`
and return an `Animator`.
The following example creates an `Animator` that scales the content view
horizontally:

### Kotlin

```
override fun onCreateEnterAnimation(): Animator =
    ObjectAnimator.ofFloat(contentView, View.SCALE_X, 0.2f, 1.0f)
            .setDuration(ANIMATION_DURATION)
```

### Java

```
@Override
protected Animator onCreateEnterAnimation() {
    Animator startAnimator = ObjectAnimator.ofFloat(contentView,
            View.SCALE_X, 0.2f, 1.0f).setDuration(ANIMATION_DURATION);
    return startAnimator;
}
```

To customize the animation used when the user navigates to a different page,
override
`onPageChanged()`.
In your `onPageChanged()` method, create `Animator` objects
that remove the previous page and display the next page, add these to an
`AnimatorSet`, and play the set. The following
example uses a fade-out animation to remove the previous page, updates the
content view image, and uses a fade-in animation to display the next page:

### Kotlin

```
override fun onPageChanged(newPage: Int, previousPage: Int) {
    // Create a fade-out animation for previousPage and, once
    // done, swap the contentView image with the next page's image
    val fadeOut = ObjectAnimator.ofFloat(mContentView, View.ALPHA, 1.0f, 0.0f)
            .setDuration(ANIMATION_DURATION)
            .apply {
                addListener(object : AnimatorListenerAdapter() {

                    override fun onAnimationEnd(animation: Animator) {
                        mContentView.setImageResource(pageImages[newPage])
                    }
                })
            }
    // Create a fade-in animation for nextPage
    val fadeIn = ObjectAnimator.ofFloat(mContentView, View.ALPHA, 0.0f, 1.0f)
            .setDuration(ANIMATION_DURATION)
    // Create AnimatorSet with fade-out and fade-in animators and start it
    AnimatorSet().apply {
        playSequentially(fadeOut, fadeIn)
        start()
    }
}
```

### Java

```
@Override
protected void onPageChanged(final int newPage, int previousPage) {
    // Create a fade-out animation for previousPage and, once
    // done, swap the contentView image with the next page's image
    Animator fadeOut = ObjectAnimator.ofFloat(mContentView,
            View.ALPHA, 1.0f, 0.0f).setDuration(ANIMATION_DURATION);
    fadeOut.addListener(new AnimatorListenerAdapter() {
        @Override
        public void onAnimationEnd(Animator animation) {
            mContentView.setImageResource(pageImages[newPage]);
        }
    });
    // Create a fade-in animation for nextPage
    Animator fadeIn = ObjectAnimator.ofFloat(mContentView,
            View.ALPHA, 0.0f, 1.0f).setDuration(ANIMATION_DURATION);
    // Create AnimatorSet with fade-out and fade-in animators and start it
    AnimatorSet set = new AnimatorSet();
    set.playSequentially(fadeOut, fadeIn);
    set.start();
}
```

For more details about how to create
`Animator` objects and
`AnimatorSet` objects, see
[Property Animation Overview](https://developer.android.com/guide/topics/graphics/prop-animation.html).

## Customize themes

Any `OnboardingSupportFragment`
implementation must use either the
`Theme_Leanback_Onboarding` theme
or a theme that inherits from `Theme_Leanback_Onboarding`. Set the
theme for your `OnboardingSupportFragment` by doing one of the following:

* Set the parent activity of the `OnboardingSupportFragment` to use the
  desired theme. The following example shows how to set an activity to use
  `Theme_Leanback_Onboarding` in the app manifest:

  ```
  <activity
     android:name=".OnboardingActivity"
     android:enabled="true"
     android:exported="true"
     android:theme="@style/Theme.Leanback.Onboarding">
  </activity>
  ```
* Set the theme in the parent activity by using the
  `LeanbackOnboardingTheme_onboardingTheme`
  attribute in a custom activity theme. Point this attribute to another
  custom theme that only the `OnboardingSupportFragment`
  objects in your activity use. Use this approach if your activity already uses
  a custom theme and you don't want to apply
  `OnboardingSupportFragment` styles to other
  views in the activity.
* Override
  `onProvideTheme()` and return the desired theme. Use this approach if
  multiple activities use your
  `OnboardingSupportFragment`
  or if the parent activity can't use the desired theme.
  The following example overrides `onProvideTheme()` and returns
  `Theme_Leanback_Onboarding`:

  ### Kotlin

  ```
  override fun onProvideTheme(): Int = R.style.Theme_Leanback_Onboarding
  ```

  ### Java

  ```
  @Override
  public int onProvideTheme() {
     return R.style.Theme_Leanback_Onboarding;
  }
  ```

[Previous

arrow\_back

Use transport controls](/training/tv/playback/leanback/transport-controls)

[Next

Add a guided step

arrow\_forward](/training/tv/playback/leanback/guided-step)