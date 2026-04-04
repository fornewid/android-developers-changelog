---
title: https://developer.android.com/training/tv/playback/leanback/guided-step
url: https://developer.android.com/training/tv/playback/leanback/guided-step
source: md.txt
---

Build better with Compose Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS. [Compose for TV →](https://developer.android.com/training/tv/playback/compose) ![](https://developer.android.com/static/images/android-compose-tv-logo.png) **Warning:** The Leanback library is deprecated. Use [Jetpack Compose for
| Android TV OS](https://developer.android.com/training/tv/playback/compose) instead.


Your application might have multi-step tasks for users. For example, your app might need to guide
users through purchasing additional content, setting up a complex configuration setting, or
confirming a decision. All these tasks require walking users through one or more ordered steps or
decisions.


The deprecated [androidx.leanback library](https://developer.android.com/training/tv/get-started/create#leanback) provides classes to implement multi-step
user tasks. This page discusses how to use the
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment` class
to guide a user through a series of decisions to accomplish a task by using
`GuidedStepSupportFragment`.

## Provide details for a step


A `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment` represents a single step in a series
of steps. Visually, it provides a guidance view with a
list of possible actions or decisions for the step.
![](https://developer.android.com/static/images/training/tv/playback/guided-step-screen.png)

**Figure 1.** An example guided step.


For each step in your multi-step task, extend
`GuidedStepSupportFragment` and provide context information about
the step and actions the user can take. Override
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateGuidance(android.os.Bundle)`
and return a new
`https://developer.android.com/reference/androidx/leanback/widget/GuidanceStylist.Guidance` that contains context
information, such as the step title, description, and icon, as shown in the following example:

### Kotlin

```kotlin
override fun onCreateGuidance(savedInstanceState: Bundle?): GuidanceStylist.Guidance {
    return GuidanceStylist.Guidance(
            getString(R.string.guidedstep_first_title),
            getString(R.string.guidedstep_first_description),
            getString(R.string.guidedstep_first_breadcrumb),
            activity.getDrawable(R.drawable.guidedstep_main_icon_1)
    )
}
```

### Java

```java
@Override
public GuidanceStylist.Guidance onCreateGuidance(Bundle savedInstanceState) {
    String title = getString(R.string.guidedstep_first_title);
    String breadcrumb = getString(R.string.guidedstep_first_breadcrumb);
    String description = getString(R.string.guidedstep_first_description);
    Drawable icon = getActivity().getDrawable(R.drawable.guidedstep_main_icon_1);
    return new GuidanceStylist.Guidance(title, description, breadcrumb, icon);
}
```


Add your `GuidedStepSupportFragment` subclass to your desired
activity by calling
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#add(androidx.fragment.app.FragmentManager, androidx.leanback.app.GuidedStepSupportFragment)`
in your activity's `https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)` method.


If your activity contains only `GuidedStepSupportFragment`
objects, use `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#addAsRoot(androidx.fragment.app.FragmentActivity, androidx.leanback.app.GuidedStepSupportFragment, int)`
instead of `add()` to add the first `GuidedStepSupportFragment`. Using
`addAsRoot()` helps ensure that if the user presses the Back button on the TV remote when viewing
the first `GuidedStepSupportFragment`, both the
`GuidedStepSupportFragment` and the parent activity close.

**Note:** Add
`GuidedStepSupportFragment` objects programmatically,
not in your layout XML files.

## Create and handle user actions


Add user actions by overriding
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateActions(java.util.List<androidx.leanback.widget.GuidedAction>, android.os.Bundle)`.
In your override, add a new `https://developer.android.com/reference/androidx/leanback/widget/GuidedAction` for each
action item and provide the action string, description, and ID. Use
`https://developer.android.com/reference/androidx/leanback/widget/GuidedAction.Builder` to add new actions.

### Kotlin

```kotlin
override fun onCreateActions(actions: MutableList<GuidedAction>, savedInstanceState: Bundle?) {
    super.onCreateActions(actions, savedInstanceState)

    // Add "Continue" user action for this step
    actions.add(GuidedAction.Builder()
            .id(CONTINUE)
            .title(getString(R.string.guidedstep_continue))
            .description(getString(R.string.guidedstep_letsdoit))
            .hasNext(true)
            .build())
    ...
```

### Java

```java
@Override
public void onCreateActions(List<GuidedAction> actions, Bundle savedInstanceState) {
    // Add "Continue" user action for this step
    actions.add(new GuidedAction.Builder()
           .id(CONTINUE)
           .title(getString(R.string.guidedstep_continue))
           .description(getString(R.string.guidedstep_letsdoit))
           .hasNext(true)
           .build());
...
```


Actions aren't limited to single-line selections. Here are additional types of
actions you can create:

- Add an information label action to provide additional information about user choices by setting `https://developer.android.com/reference/androidx/leanback/widget/GuidedAction.BuilderBase#infoOnly(boolean)`. When `infoOnly` is true, users can't select the action.
- Add an editable text action by setting `https://developer.android.com/reference/androidx/leanback/widget/GuidedAction.BuilderBase#editable(boolean)`. When `editable` is true, the user can enter text in a selected action using the remote or a connected keyboard. Override `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onGuidedActionEditedAndProceed(androidx.leanback.widget.GuidedAction)` to get the modified text the user entered. You can also override `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onGuidedActionEditCanceled(androidx.leanback.widget.GuidedAction)` to know when the user cancels input.
- Add a set of actions that behave like checkable radio buttons by using `https://developer.android.com/reference/androidx/leanback/widget/GuidedAction.BuilderBase#checkSetId(int)` with a common ID value to group actions into a set. All actions in the same list with the same check-set ID are considered linked. When the user selects one of the actions within that set, that action becomes checked and all other actions become unchecked.
- Add a date-picker action by using `GuidedDatePickerAction.Builder` instead of `GuidedAction.Builder` in `onCreateActions()`. Override `onGuidedActionEditedAndProceed()` to get the modified date value the user entered.
- Add an action that uses subactions to let the user pick from an extended list of choices. Subactions are described in the [Add subactions](https://developer.android.com/training/tv/playback/leanback/guided-step#subactions) section.
- Add a button action that appears to the right of the actions list and is easily accessible. Button actions are described in the [Add button
  actions](https://developer.android.com/training/tv/playback/leanback/guided-step#buttonactions) section.


You can also add a visual indicator that selecting an action
leads to a new step by setting
`https://developer.android.com/reference/androidx/leanback/widget/GuidedAction#hasNext()`.

For all the different attributes that you can set, see
`https://developer.android.com/reference/androidx/leanback/widget/GuidedAction`.


To respond to actions, override
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onGuidedActionClicked(androidx.leanback.widget.GuidedAction)` and process the passed-in
`GuidedAction`. Identify the selected action by
examining `https://developer.android.com/reference/androidx/leanback/widget/Action#getId()`.

### Add subactions


Some actions could require you to give the user an additional set of choices. A
`https://developer.android.com/reference/androidx/leanback/widget/GuidedAction` can specify a list of
subactions that display as a menu of child actions.
![](https://developer.android.com/static/images/training/tv/playback/guided-step-subaction.png)

**Figure 2.** Guided step subactions.


The subaction list can contain regular actions or radio button actions, but
not date-picker or editable text actions. Also, a subaction can't have its own
set of subactions, because the system doesn't support more than one level of subactions.


To add subactions, first create and populate a list of
`GuidedAction` objects that act as subactions, as shown in the following example:

### Kotlin

```kotlin
subActions.add(GuidedAction.Builder()
        .id(SUBACTION1)
        .title(getString(R.string.guidedstep_subaction1_title))
        .description(getString(R.string.guidedstep_subaction1_desc))
        .build())
...
```

### Java

```java
List<GuidedAction> subActions = new ArrayList<GuidedAction>();
subActions.add(new GuidedAction.Builder()
       .id(SUBACTION1)
       .title(getString(R.string.guidedstep_subaction1_title))
       .description(getString(R.string.guidedstep_subaction1_desc))
       .build());
...
```


In `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateActions(java.util.List<androidx.leanback.widget.GuidedAction>, android.os.Bundle)`, create a top-level
`GuidedAction` that displays the
list of subactions when selected:

### Kotlin

```kotlin
    ...
    actions.add(GuidedAction.Builder()
            .id(SUBACTIONS)
            .title(getString(R.string.guidedstep_subactions_title))
            .description(getString(R.string.guidedstep_subactions_desc))
            .subActions(subActions)
            .build())
    ...
```

### Java

```java
@Override
public void onCreateActions(List<GuidedAction> actions, Bundle savedInstanceState) {
...
    actions.add(new GuidedAction.Builder()
           .id(SUBACTIONS)
           .title(getString(R.string.guidedstep_subactions_title))
           .description(getString(R.string.guidedstep_subactions_desc))
           .subActions(subActions)
           .build());
...
}
```


Finally, respond to subaction selections by overriding
`onSubGuidedActionClicked()`:

### Kotlin

```kotlin
override fun onSubGuidedActionClicked(action: GuidedAction): Boolean {
    // Check for which action was clicked and handle as needed
    when(action.id) {
        SUBACTION1 -> {
            // Subaction 1 selected
        }
    }
    // Return true to collapse the subactions menu or
    // false to keep the menu expanded
    return true
}
```

### Java

```java
@Override
public boolean onSubGuidedActionClicked(GuidedAction action) {
   // Check for which action was clicked and handle as needed
   if (action.getId() == SUBACTION1) {
       // Subaction 1 selected
   }
   // Return true to collapse the subactions menu or
   // false to keep the menu expanded
   return true;
}
```

### Add button actions


If your guided step has a large list of actions, users might have to scroll through the list
to access the most commonly used actions. Use button actions to separate
commonly used actions from the action list. Button actions appear next to
the action list and are easy to navigate to.
![](https://developer.android.com/static/images/training/tv/playback/guided-step-buttonaction.png)

**Figure 3.** Guided step button actions.


Button actions are created and handled just like regular actions, but you create
button actions in
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateButtonActions(java.util.List%3Candroidx.leanback.widget.GuidedAction%3E,android.os.Bundle)`
instead of `onCreateActions()`. Respond to button actions in
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onGuidedActionClicked(androidx.leanback.widget.GuidedAction)`.


Use button actions for simple actions, such as navigation actions between steps.
Don't use the date-picker action or other editable actions as button actions.
Also, button actions cannot have subactions.

## Group guided steps into a guided sequence


A `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment`
represents a single step. To create an ordered sequence of steps, group multiple
`GuidedStepSupportFragment` objects together using
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#add(androidx.fragment.app.FragmentManager, androidx.leanback.app.GuidedStepSupportFragment)` to add
the next step in the sequence to the fragment stack.

### Kotlin

```kotlin
override fun onGuidedActionClicked(action: GuidedAction) {
    val fm = fragmentManager
    when(action.id) {
        CONTINUE -> GuidedStepSupportFragment.add(fm, SecondStepFragment())
    }
}
```

### Java

```java
@Override
public void onGuidedActionClicked(GuidedAction action) {
    FragmentManager fm = getFragmentManager();
    if (action.getId() == CONTINUE) {
       GuidedStepSupportFragment.add(fm, new SecondStepFragment());
    }
...
```


If the user presses the Back button on the TV remote, the device shows the previous
`GuidedStepSupportFragment` on the fragment stack. If you
provide your own `https://developer.android.com/reference/androidx/leanback/widget/GuidedAction` that
returns to the previous step, you can implement the Back behavior by calling
`https://developer.android.com/reference/android/app/FragmentManager#popBackStack()`.
If you need to return the user to an even earlier step in the sequence, use
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#popBackStackToGuidedStepSupportFragment(java.lang.Class%3C?%3E,int)`
to return to a specific `GuidedStepSupportFragment` in the fragment stack.


When the user finishes the last step in the sequence, use
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#finishGuidedStepSupportFragments()` to remove all
`GuidedStepSupportFragment` instances
from the current stack and return to the original parent activity. If the
first `GuidedStepSupportFragment` is added
using `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#addAsRoot(androidx.fragment.app.FragmentActivity, androidx.leanback.app.GuidedStepSupportFragment, int)`, calling
`finishGuidedStepSupportFragments()` also closes the parent activity.

## Customize step presentation


The `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment` class can use custom
themes that control presentation aspects such as title text formatting or step transition
animations. Custom themes must inherit from
`Theme_Leanback_GuidedStep` and can provide
overriding values for attributes defined in
`https://developer.android.com/reference/androidx/leanback/widget/GuidanceStylist` and
`https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist`.


To apply a custom theme to your `GuidedStepSupportFragment`,
do one of the following:

- Apply the theme to the parent activity by setting the `android:theme` attribute to the activity element in the Android manifest. Setting this attribute applies the theme to all child views and is the most straightforward way to apply a custom theme if the parent activity contains only `GuidedStepSupportFragment` objects.
- If your activity already uses a custom theme and you don't want to apply `GuidedStepSupportFragment` styles to other views in the activity, add the `LeanbackGuidedStepTheme_guidedStepTheme` attribute to your existing custom activity theme. This attribute points to the custom theme that only the `GuidedStepSupportFragment` objects in your activity use.
- If you use `GuidedStepSupportFragment` objects in different activities that are part of the same overall multi-step task and want to use a consistent visual theme across all steps, override `https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onProvideTheme()` and return your custom theme.


For more information on how to add styles and themes, see
[Styles and Themes](https://developer.android.com/guide/topics/ui/themes).


The `GuidedStepSupportFragment` class uses special
*stylist classes* to access and apply theme attributes.
The `https://developer.android.com/reference/androidx/leanback/widget/GuidanceStylist` class uses theme information
to control presentation of the left guidance view, while the
`https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist` class uses theme information
to control presentation of the right actions view.


To customize the visual style of your steps beyond what theme customization provides, subclass
`GuidanceStylist` or
`GuidedActionsStylist` and return your subclass in
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateGuidanceStylist()` or
`https://developer.android.com/reference/androidx/leanback/app/GuidedStepSupportFragment#onCreateActionsStylist()`.
For details on what you can customize in these subclasses, see the documentation on
`https://developer.android.com/reference/androidx/leanback/widget/GuidanceStylist` and
`https://developer.android.com/reference/androidx/leanback/widget/GuidedActionsStylist`.