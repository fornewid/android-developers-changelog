---
title: https://developer.android.com/guide/topics/ui/accessibility/views/apps-views
url: https://developer.android.com/guide/topics/ui/accessibility/views/apps-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/guide/topics/ui/accessibility/apps)

Try to make your Android app usable for everyone, including people with
accessibility needs.

People with impaired vision, color blindness, impaired hearing, impaired
dexterity, cognitive disabilities, and many other disabilities use Android
devices. When you develop apps with
accessibility in mind, you make the user experience better for people with
accessibility needs.

This page presents guidelines for implementing key elements of accessibility
so that everyone can use your app more easily. For more in-depth guidance on
how to make your app more accessible, see [Principles for improving app
accessibility](https://developer.android.com/guide/topics/ui/accessibility/principles).

## Use large, simple controls

Your app's UI is easier to use if its controls are easier to see
and tap. We recommend that each interactive UI element have a focusable area, or
*touch target size*, of at least 48dpx48dp. Larger is even better.

For a given UI element to have a large enough touch target size, the following
conditions should **both** be true:

- The sum of the values of [`android:paddingLeft`](https://developer.android.com/reference/android/view/View#attr_android:paddingLeft), [`android:minWidth`](https://developer.android.com/reference/android/view/View#attr_android:minWidth), and [`android:paddingRight`](https://developer.android.com/reference/android/view/View#attr_android:paddingRight) is greater than or equal to 48dp.
- The sum of the values of [`android:paddingTop`](https://developer.android.com/reference/android/view/View#attr_android:paddingTop), [`android:minHeight`](https://developer.android.com/reference/android/view/View#attr_android:minHeight), and [`android:paddingBottom`](https://developer.android.com/reference/android/view/View#attr_android:paddingBottom) is greater than or equal to 48dp.

The padding values allow an object's *visible* size to be less than 48dpx48dp
while still having the recommended touch target size.

The following code snippet shows an element that has the recommended touch
target size:

```xml
<ImageButton ...
    android:paddingLeft="4dp"
    android:minWidth="40dp"
    android:paddingRight="4dp"

    android:paddingTop="8dp"
    android:minHeight="32dp"
    android:paddingBottom="8dp" />
```

## Describe each UI element

For each UI element in your app, include a description that
describes the element's purpose. In most cases, you include this description in
the element's `contentDescription` attribute, as shown in the following code
snippet:

```xml
<!-- Use string resources for easier localization. -->
<!-- The en-US value for the following string is "Inspect". -->
<ImageView
    ...
    android:contentDescription="@string/inspect" />
```

> [!NOTE]
> **Note:** Don't provide descriptions for [`TextView`](https://developer.android.com/reference/android/widget/TextView) elements. Android accessibility services automatically announce the text itself as the description.

When adding descriptions to your app's UI elements, keep the following best
practices in mind:

- Don't include the type of UI element in the content description. Screen
  readers automatically announce both the element's type and description. For
  example, if selecting a button causes a "submit" action to occur in your app,
  make the button's description `"Submit"`, not `"Submit button"`.

- Each description must be unique. That way, when screen reader users
  encounter a repeated element description, they correctly recognize that the
  focus is on an element that already had focus earlier. In particular, each item
  within a view group such as
  [`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView) must have
  a different description. Each description must reflect the content that's unique
  to a given item, such as the name of a city in a list of locations.

- If your app's `minSdkVersion` is `16` or higher, you can set the
  [`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility)
  attribute to `"no"` for graphical elements that are only used for decorative
  effect.

## Additional resources

To learn more about making your app more accessible, see the following
additional resources:

### Codelabs

- [Starting Android
  Accessibility](https://codelabs.developers.google.com/codelabs/starting-android-accessibility)